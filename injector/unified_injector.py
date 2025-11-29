#!/usr/bin/env python3
"""
Unified Injector: 통합 HWPX 데이터 주입기
=========================================
지원 모드:
1. placeholder: {{KEY}} 텍스트 치환
2. gov_form: name="AAA*..." 속성 기반 주입
3. coordinate: 테이블 좌표 기반 주입

모든 모드를 자동 감지하여 처리
"""

import json
import re
import shutil
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Any, Optional, List
from dataclasses import dataclass

from template_analyzer import TemplateAnalyzer, TemplateType


# XML 네임스페이스
NS = {
    'hp': 'http://www.hancom.co.kr/hwpml/2011/paragraph',
    'hs': 'http://www.hancom.co.kr/hwpml/2011/section',
    'hc': 'http://www.hancom.co.kr/hwpml/2011/core',
}

# ElementTree에 네임스페이스 등록 (출력 시 prefix 유지)
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

# linesegarray 제거 패턴 - 한글이 자동 재계산하도록
LINESEGARRAY_PATTERN = re.compile(r'<hp:linesegarray[^>]*>.*?</hp:linesegarray>', re.DOTALL)


@dataclass
class InjectionResult:
    """주입 결과"""
    success: bool
    output_path: str
    fields_injected: int
    errors: List[str]


class UnifiedInjector:
    """통합 HWPX 주입기"""
    
    PLACEHOLDER_PATTERN = re.compile(r'\{\{\s*([A-Za-z0-9_가-힣]+)\s*\}\}')
    
    def __init__(self, template_path: str | Path):
        self.template_path = Path(template_path)
        self.analyzer = TemplateAnalyzer(template_path)
        self.analysis = self.analyzer.analyze()
    
    def inject(self, data: Dict[str, Any], output_path: str | Path) -> InjectionResult:
        """
        데이터 주입 실행
        
        Args:
            data: 주입할 데이터
                - 플레이스홀더용: {"TITLE": "값", "NAME": "값", ...}
                - 정부양식용: {"TABLE*FIELD": "값", ...}
                - 좌표용: {"tables": {"0": {"1,2": "값"}}}
                - 혼합 가능
            output_path: 출력 HWPX 경로
        
        Returns:
            InjectionResult
        """
        output_path = Path(output_path)
        errors = []
        fields_injected = 0
        
        # 임시 디렉토리에 추출
        tmpdir = tempfile.mkdtemp()
        try:
            # HWPX 압축 해제
            with zipfile.ZipFile(self.template_path, 'r') as z:
                z.extractall(tmpdir)
            
            # section*.xml 파일들 처리
            contents_dir = Path(tmpdir) / 'Contents'
            if contents_dir.exists():
                for xml_file in contents_dir.glob('section*.xml'):
                    try:
                        count = self._process_section(xml_file, data)
                        fields_injected += count
                    except Exception as e:
                        errors.append(f"{xml_file.name}: {str(e)}")
            
            # 다시 압축
            output_path.parent.mkdir(parents=True, exist_ok=True)
            self._rezip(tmpdir, output_path)
            
        finally:
            shutil.rmtree(tmpdir)
        
        return InjectionResult(
            success=len(errors) == 0,
            output_path=str(output_path),
            fields_injected=fields_injected,
            errors=errors,
        )
    
    def _process_section(self, xml_path: Path, data: Dict[str, Any]) -> int:
        """section XML 처리"""
        with open(xml_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # linesegarray 제거 - 한글이 열 때 자동 재계산하므로 줄바꿈 문제 해결
        content = LINESEGARRAY_PATTERN.sub('', content)
        
        count = 0
        
        # 1. 플레이스홀더 치환 (텍스트 기반, 가장 안전)
        content, ph_count = self._inject_placeholders(content, data)
        count += ph_count
        
        # 2. 정부 양식 필드 주입 (XML 파싱)
        # 3. 좌표 기반 주입 (XML 파싱)
        if self.analysis.template_type in [TemplateType.GOV_FORM, TemplateType.MIXED, TemplateType.PLAIN]:
            content, xml_count = self._inject_xml_based(content, data)
            count += xml_count
        
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return count
    
    def _inject_placeholders(self, content: str, data: Dict[str, Any]) -> tuple[str, int]:
        """{{KEY}} 플레이스홀더 치환"""
        count = 0
        
        def replace(match):
            nonlocal count
            key = match.group(1)
            
            # 대소문자 무관 매칭
            value = None
            for k, v in data.items():
                if k.upper() == key.upper():
                    value = v
                    break
            
            if value is None:
                return match.group(0)  # 매칭 안 되면 원본 유지
            
            count += 1
            
            # 리스트 처리: 여러 문단으로 확장
            if isinstance(value, list):
                escaped = [self._escape_xml(str(x)) for x in value]
                return '</hp:t></hp:run></hp:p>\n<hp:p><hp:run><hp:t>'.join(escaped)
            else:
                return self._escape_xml(str(value))
        
        new_content = self.PLACEHOLDER_PATTERN.sub(replace, content)
        return new_content, count
    
    def _inject_xml_based(self, content: str, data: Dict[str, Any]) -> tuple[str, int]:
        """XML 파싱 기반 주입 (정부양식 + 좌표)"""
        count = 0
        
        try:
            root = ET.fromstring(content)
        except ET.ParseError:
            return content, 0
        
        # 정부 양식 필드 주입
        if 'fields' not in data or any('*' in k for k in data.keys()):
            gov_data = {k: v for k, v in data.items() if '*' in k}
            count += self._inject_gov_fields(root, gov_data)
        
        # 좌표 기반 주입
        if 'tables' in data:
            count += self._inject_by_coordinates(root, data['tables'])
        
        # XML 직렬화 (선언 포함)
        new_content = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        new_content += ET.tostring(root, encoding='unicode')
        
        return new_content, count
    
    def _inject_gov_fields(self, root: ET.Element, data: Dict[str, str]) -> int:
        """정부 양식 name 속성 기반 주입"""
        count = 0
        
        for tc in root.iter():
            if not tc.tag.endswith('}tc'):
                continue
            
            name_attr = tc.get('name', '')
            if not name_attr or '*' not in name_attr:
                continue
            
            # "AAA*TABLE*FIELD*N" → "TABLE*FIELD" 매칭
            parts = name_attr.split('*')
            if len(parts) >= 3:
                field_key = '*'.join(parts[1:-1])
            else:
                field_key = name_attr
            
            # 데이터 찾기
            value = data.get(field_key) or data.get(name_attr)
            if value is None:
                continue
            
            # 셀에 텍스트 설정
            if self._set_cell_text(tc, str(value)):
                count += 1
        
        return count
    
    def _inject_by_coordinates(self, root: ET.Element, tables_data: Dict[str, Dict[str, str]]) -> int:
        """좌표 기반 주입"""
        count = 0
        
        # 테이블 찾기
        tables = list(root.iter())
        tables = [el for el in tables if el.tag.endswith('}tbl')]
        
        for tbl_idx, tbl in enumerate(tables):
            tbl_key = str(tbl_idx)
            if tbl_key not in tables_data:
                continue
            
            cells_data = tables_data[tbl_key]
            
            for tc in tbl.iter():
                if not tc.tag.endswith('}tc'):
                    continue
                
                # cellAddr 찾기
                cell_addr = None
                for child in tc:
                    if child.tag.endswith('}cellAddr'):
                        cell_addr = child
                        break
                
                if cell_addr is None:
                    continue
                
                row = cell_addr.get('rowAddr', '0')
                col = cell_addr.get('colAddr', '0')
                coord_key = f"{row},{col}"
                
                if coord_key in cells_data:
                    if self._set_cell_text(tc, cells_data[coord_key]):
                        count += 1
        
        return count
    
    def _set_cell_text(self, tc: ET.Element, text: str) -> bool:
        """셀에 텍스트 설정"""
        # hp:t 태그 찾기
        for elem in tc.iter():
            if elem.tag.endswith('}t'):
                elem.text = text
                return True
        
        # hp:t가 없으면 생성 시도
        # subList > p > run > t 구조
        for sublist in tc.iter():
            if sublist.tag.endswith('}subList'):
                for p in sublist:
                    if p.tag.endswith('}p'):
                        for run in p:
                            if run.tag.endswith('}run'):
                                # hp:t 생성
                                t = ET.SubElement(run, f'{{{NS["hp"]}}}t')
                                t.text = text
                                return True
        
        return False
    
    def _escape_xml(self, s: str) -> str:
        """XML 특수문자 이스케이프"""
        return (s.replace('&', '&amp;')
                 .replace('<', '&lt;')
                 .replace('>', '&gt;')
                 .replace('"', '&quot;')
                 .replace("'", '&apos;'))
    
    def _rezip(self, src_dir: str, out_path: Path):
        """디렉토리를 HWPX로 압축"""
        with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as z:
            # mimetype은 압축 없이 먼저
            mimetype_path = Path(src_dir) / 'mimetype'
            if mimetype_path.exists():
                with open(mimetype_path, 'rb') as f:
                    z.writestr('mimetype', f.read(), compress_type=zipfile.ZIP_STORED)
            
            # 나머지 파일들
            for root, dirs, files in os.walk(src_dir):
                for fn in files:
                    if fn == 'mimetype':
                        continue
                    full_path = Path(root) / fn
                    arcname = full_path.relative_to(src_dir)
                    z.write(full_path, arcname)


import os


def main():
    """CLI 테스트"""
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='HWPX 데이터 주입기')
    parser.add_argument('template', help='템플릿 HWPX 파일')
    parser.add_argument('--data', '-d', help='JSON 데이터 파일')
    parser.add_argument('--output', '-o', help='출력 HWPX 파일')
    parser.add_argument('--analyze', '-a', action='store_true', help='분석만 수행')
    
    args = parser.parse_args()
    
    if not Path(args.template).exists():
        print(f"❌ 파일 없음: {args.template}")
        sys.exit(1)
    
    # 분석 모드
    if args.analyze:
        analyzer = TemplateAnalyzer(args.template)
        print(analyzer.get_llm_context())
        sys.exit(0)
    
    # 주입 모드
    if not args.data:
        print("❌ --data 옵션 필요")
        sys.exit(1)
    
    # 데이터 로드
    with open(args.data, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 출력 경로
    output = args.output or args.template.replace('.hwpx', '_injected.hwpx')
    
    # 주입 실행
    injector = UnifiedInjector(args.template)
    result = injector.inject(data, output)
    
    print("=" * 60)
    print(f"📄 템플릿: {args.template}")
    print(f"📊 데이터: {args.data}")
    print(f"📁 출력: {result.output_path}")
    print("=" * 60)
    print(f"✅ 성공: {result.success}")
    print(f"📝 주입된 필드: {result.fields_injected}개")
    
    if result.errors:
        print("⚠️ 오류:")
        for err in result.errors:
            print(f"  - {err}")


if __name__ == "__main__":
    main()
