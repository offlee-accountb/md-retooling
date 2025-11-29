#!/usr/bin/env python3
"""
Keyword-based Injector: 키워드 패턴 기반 HWPX 데이터 주입기
==========================================================
패턴: "(키워드)" 뒤에 내용 삽입

예시 MD:
 ◦ (추진 배경) 중소기업의 스마트공장 도입 시 ...
 ◦ (구성) 지역별 산업 특성과 수요에 따라 ...

예시 HWPX:
 <hp:t>(추진 배경)</hp:t> + 빈 run
 → <hp:t>(추진 배경)</hp:t> + <hp:t>중소기업의...</hp:t>
"""

import json
import re
import shutil
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
from dataclasses import dataclass


# XML 네임스페이스
NS = {
    'hp': 'http://www.hancom.co.kr/hwpml/2011/paragraph',
    'hs': 'http://www.hancom.co.kr/hwpml/2011/section',
    'hc': 'http://www.hancom.co.kr/hwpml/2011/core',
}

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
    fields_found: int
    errors: List[str]
    details: List[str]


@dataclass 
class KeywordField:
    """키워드 필드 정보"""
    keyword: str       # 예: "추진 배경"
    full_match: str    # 예: "(추진 배경)"
    paragraph_id: str
    value: Optional[str] = None


class KeywordInjector:
    """키워드 패턴 기반 HWPX 주입기"""
    
    # 키워드 패턴: (키워드) 형태
    KEYWORD_PATTERN = re.compile(r'\(([^)]+)\)')
    
    def __init__(self, template_path: str | Path):
        self.template_path = Path(template_path)
    
    def analyze(self) -> Tuple[List[KeywordField], str]:
        """
        템플릿에서 키워드 필드 분석
        
        Returns:
            (필드 목록, LLM 컨텍스트)
        """
        fields = []
        
        with tempfile.TemporaryDirectory() as tmpdir:
            with zipfile.ZipFile(self.template_path, 'r') as z:
                z.extractall(tmpdir)
            
            contents_dir = Path(tmpdir) / 'Contents'
            if not contents_dir.exists():
                return fields, "템플릿 분석 실패: Contents 폴더 없음"
            
            for xml_file in contents_dir.glob('section*.xml'):
                fields.extend(self._extract_keywords(xml_file))
        
        # LLM 컨텍스트 생성
        context = self._build_context(fields)
        return fields, context
    
    def _extract_keywords(self, xml_path: Path) -> List[KeywordField]:
        """XML에서 키워드 필드 추출"""
        fields = []
        
        with open(xml_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        try:
            root = ET.fromstring(content)
        except ET.ParseError:
            return fields
        
        # 모든 paragraph 순회
        for p in root.iter():
            if not p.tag.endswith('}p'):
                continue
            
            p_id = p.get('id', '')
            
            # paragraph 내 모든 텍스트 수집
            p_text = self._get_paragraph_text(p)
            
            # 키워드 패턴 찾기
            for match in self.KEYWORD_PATTERN.finditer(p_text):
                keyword = match.group(1)
                full_match = match.group(0)
                
                # 필터: 너무 짧거나 숫자만 있는 건 제외
                if len(keyword) < 2:
                    continue
                if keyword.isdigit():
                    continue
                    
                fields.append(KeywordField(
                    keyword=keyword,
                    full_match=full_match,
                    paragraph_id=p_id,
                ))
        
        return fields
    
    def _get_paragraph_text(self, p: ET.Element) -> str:
        """paragraph의 모든 텍스트 추출"""
        texts = []
        for t in p.iter():
            if t.tag.endswith('}t') and t.text:
                texts.append(t.text)
        return ''.join(texts)
    
    def _build_context(self, fields: List[KeywordField]) -> str:
        """LLM용 분석 컨텍스트 생성"""
        lines = [
            "## 키워드 기반 템플릿 분석",
            f"- 파일: {self.template_path.name}",
            f"- 감지된 키워드 필드: {len(fields)}개",
            "",
            "### 키워드 목록",
            "| 키워드 | 패턴 | 문단ID |",
            "|--------|------|--------|",
        ]
        
        for f in fields:
            lines.append(f"| {f.keyword} | `{f.full_match}` | {f.paragraph_id} |")
        
        lines.extend([
            "",
            "### 데이터 형식",
            "```json",
            "{",
        ])
        
        for f in fields:
            lines.append(f'  "{f.keyword}": "내용...",')
        
        lines.extend([
            "}",
            "```",
        ])
        
        return '\n'.join(lines)
    
    def inject(self, data: Dict[str, str], output_path: str | Path) -> InjectionResult:
        """
        데이터 주입 실행
        
        Args:
            data: {"키워드": "주입할 내용", ...}
            output_path: 출력 HWPX 경로
        
        Returns:
            InjectionResult
        """
        output_path = Path(output_path)
        errors = []
        details = []
        fields_injected = 0
        fields_found = 0
        
        with tempfile.TemporaryDirectory() as tmpdir:
            # 압축 해제
            with zipfile.ZipFile(self.template_path, 'r') as z:
                z.extractall(tmpdir)
            
            contents_dir = Path(tmpdir) / 'Contents'
            if contents_dir.exists():
                for xml_file in contents_dir.glob('section*.xml'):
                    try:
                        found, injected, detail_list = self._process_section(xml_file, data)
                        fields_found += found
                        fields_injected += injected
                        details.extend(detail_list)
                    except Exception as e:
                        errors.append(f"{xml_file.name}: {str(e)}")
            
            # 다시 압축
            output_path.parent.mkdir(parents=True, exist_ok=True)
            self._rezip(tmpdir, output_path)
        
        return InjectionResult(
            success=len(errors) == 0,
            output_path=str(output_path),
            fields_injected=fields_injected,
            fields_found=fields_found,
            errors=errors,
            details=details,
        )
    
    def _process_section(self, xml_path: Path, data: Dict[str, str]) -> Tuple[int, int, List[str]]:
        """section XML 처리"""
        with open(xml_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # linesegarray 제거 - 한글이 열 때 자동 재계산하므로 줄바꿈 문제 해결
        content = LINESEGARRAY_PATTERN.sub('', content)
        
        found = 0
        injected = 0
        details = []
        
        # 방법 1: 텍스트 기반 치환 (가장 간단하고 안정적)
        # "(키워드)" 뒤에 공백 하나 있으면 그 뒤에 내용 추가
        # "(키워드) " → "(키워드) 내용"
        
        for keyword, value in data.items():
            # 패턴: (키워드) 뒤의 기존 텍스트를 새 값으로 치환
            # 하지만 XML 구조 때문에 간단한 replace가 어려움
            pass
        
        # 방법 2: XML 파싱 기반 - run 단위로 처리
        try:
            root = ET.fromstring(content)
            found, injected, details = self._inject_keywords_xml(root, data)
            
            # 저장
            new_content = '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>'
            new_content += ET.tostring(root, encoding='unicode')
            
            with open(xml_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
        except ET.ParseError as e:
            details.append(f"XML 파싱 실패: {e}")
        
        return found, injected, details
    
    def _inject_keywords_xml(self, root: ET.Element, data: Dict[str, str]) -> Tuple[int, int, List[str]]:
        """
        XML 파싱으로 키워드 뒤에 내용 주입
        
        전략:
        1. 각 paragraph에서 "(키워드)" 텍스트를 가진 <hp:t> 찾기
        2. 그 다음 run이나 같은 run의 다음 <hp:t>에 값 설정
        """
        found = 0
        injected = 0
        details = []
        
        # 대소문자 무관 매칭용 정규화
        data_normalized = {k.strip(): v for k, v in data.items()}
        
        for p in root.iter():
            if not p.tag.endswith('}p'):
                continue
            
            # paragraph 내 모든 run과 t 태그 수집
            runs = list(p)
            runs = [r for r in runs if r.tag.endswith('}run')]
            
            for i, run in enumerate(runs):
                # 이 run에서 키워드 찾기
                for t in run.iter():
                    if not t.tag.endswith('}t'):
                        continue
                    if not t.text:
                        continue
                    
                    # 키워드 패턴 체크
                    for match in self.KEYWORD_PATTERN.finditer(t.text):
                        keyword = match.group(1).strip()
                        found += 1
                        
                        # 데이터에서 해당 키워드 값 찾기
                        value = data_normalized.get(keyword)
                        if value is None:
                            details.append(f"  ⚠️ '{keyword}' 데이터 없음")
                            continue
                        
                        # 주입 위치 결정:
                        # Case 1: 같은 <hp:t> 내에 "(키워드) " 형태 → 뒤에 추가
                        # Case 2: 다음 run의 <hp:t>가 비어있으면 거기 주입
                        # Case 3: 키워드 텍스트 자체를 "(키워드) 값" 으로 변경
                        
                        # Case 3 사용 (가장 안전)
                        original = t.text
                        # "(키워드)" 뒤에 내용 추가
                        new_text = original.replace(
                            match.group(0), 
                            f"{match.group(0)} {value}"
                        )
                        t.text = new_text
                        injected += 1
                        details.append(f"  ✅ '{keyword}' 주입: {value[:30]}...")
        
        return found, injected, details
    
    def _rezip(self, src_dir: str, out_path: Path):
        """디렉토리를 HWPX로 압축"""
        import os
        
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


def parse_md_to_data(md_content: str) -> Dict[str, str]:
    """
    MD 파일에서 키워드 데이터 추출
    
    형식:
    ◦ (키워드) 내용...
    (키워드) 내용...
    
    Returns:
        {"키워드": "내용", ...}
    """
    data = {}
    lines = md_content.strip().split('\n')
    
    # 패턴: (키워드) 내용
    pattern = re.compile(r'\(([^)]+)\)\s+(.+)')
    
    for line in lines:
        # 앞의 기호 제거 (◦, -, * 등)
        line = line.strip()
        line = re.sub(r'^[◦○•\-\*]\s*', '', line)
        
        match = pattern.search(line)
        if match:
            keyword = match.group(1).strip()
            content = match.group(2).strip()
            data[keyword] = content
    
    return data


def main():
    """CLI"""
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='키워드 기반 HWPX 데이터 주입기')
    parser.add_argument('template', help='템플릿 HWPX 파일')
    parser.add_argument('--md', '-m', help='MD 데이터 파일')
    parser.add_argument('--json', '-j', help='JSON 데이터 파일')
    parser.add_argument('--output', '-o', help='출력 HWPX 파일')
    parser.add_argument('--analyze', '-a', action='store_true', help='분석만 수행')
    
    args = parser.parse_args()
    
    if not Path(args.template).exists():
        print(f"❌ 파일 없음: {args.template}")
        sys.exit(1)
    
    injector = KeywordInjector(args.template)
    
    # 분석 모드
    if args.analyze:
        fields, context = injector.analyze()
        print(context)
        sys.exit(0)
    
    # 데이터 로드
    if args.md:
        with open(args.md, 'r', encoding='utf-8') as f:
            md_content = f.read()
        data = parse_md_to_data(md_content)
        print(f"📝 MD에서 추출된 데이터: {len(data)}개 키워드")
        for k, v in data.items():
            print(f"  - ({k}): {v[:50]}...")
    elif args.json:
        with open(args.json, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        print("❌ --md 또는 --json 옵션 필요")
        sys.exit(1)
    
    # 출력 경로
    output = args.output or args.template.replace('.hwpx', '_injected.hwpx')
    
    # 주입 실행
    result = injector.inject(data, output)
    
    print()
    print("=" * 60)
    print(f"📄 템플릿: {args.template}")
    print(f"📁 출력: {result.output_path}")
    print("=" * 60)
    print(f"🔍 감지된 키워드: {result.fields_found}개")
    print(f"✅ 주입 성공: {result.fields_injected}개")
    
    if result.details:
        print("\n📋 상세:")
        for d in result.details:
            print(d)
    
    if result.errors:
        print("\n⚠️ 오류:")
        for err in result.errors:
            print(f"  - {err}")


if __name__ == "__main__":
    main()
