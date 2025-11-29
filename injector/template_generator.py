#!/usr/bin/env python3
"""
Template Generator - 기존 HWPX에서 빈 템플릿 생성

기능:
1. 데이터가 있는 문서에서 구조 추출
2. 데이터 → 플레이스홀더로 변환
3. 빈 템플릿 HWPX 생성

사용:
    python template_generator.py source.hwpx --output template.hwpx
    python template_generator.py source.hwpx --analyze  # 구조만 분석
"""

import argparse
import zipfile
import tempfile
import shutil
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
from enum import Enum

# XML 네임스페이스
NAMESPACES = {
    'hp': 'http://www.hancom.co.kr/hwpml/2011/paragraph',
    'hp2': 'http://www.hancom.co.kr/hwpml/2011/head',
    'hc': 'http://www.hancom.co.kr/hwpml/2011/core',
    'hs': 'http://www.hancom.co.kr/hwpml/2011/section',
}

class FieldType(Enum):
    """필드 유형"""
    KEYWORD = "keyword"      # (키워드) 패턴
    TABLE_CELL = "table"     # 테이블 셀
    PARAGRAPH = "paragraph"  # 일반 문단
    TITLE = "title"          # 제목


@dataclass
class FieldInfo:
    """추출된 필드 정보"""
    field_type: FieldType
    name: str                    # 플레이스홀더 이름
    original_value: str          # 원본 값
    location: str                # 위치 정보 (테이블:행,열 / 문단:인덱스)
    xpath: str = ""              # XML 경로
    

@dataclass
class TemplateStructure:
    """템플릿 구조"""
    fields: List[FieldInfo] = field(default_factory=list)
    tables: List[Dict] = field(default_factory=list)  # 테이블 구조
    sections: List[str] = field(default_factory=list)  # 섹션 제목


class TemplateGenerator:
    """HWPX에서 빈 템플릿 생성"""
    
    def __init__(self, source_path: str):
        self.source_path = source_path
        self.structure = TemplateStructure()
        self.field_counter = 0
        
    def analyze(self) -> TemplateStructure:
        """문서 구조 분석"""
        with zipfile.ZipFile(self.source_path, 'r') as zf:
            # section0.xml 분석
            section_path = 'Contents/section0.xml'
            if section_path in zf.namelist():
                content = zf.read(section_path).decode('utf-8')
                self._analyze_section(content)
                
        return self.structure
    
    def _analyze_section(self, content: str):
        """섹션 XML 분석"""
        # 네임스페이스 등록
        for prefix, uri in NAMESPACES.items():
            ET.register_namespace(prefix, uri)
            
        root = ET.fromstring(content)
        
        # 1. 테이블 분석
        self._analyze_tables(root)
        
        # 2. 키워드 패턴 분석
        self._analyze_keywords(content)
        
        # 3. 일반 문단 분석
        self._analyze_paragraphs(root)
        
    def _analyze_tables(self, root):
        """테이블 구조 분석"""
        tables = root.findall('.//{http://www.hancom.co.kr/hwpml/2011/paragraph}tbl')
        
        for tbl_idx, tbl in enumerate(tables):
            rows = tbl.findall('.//{http://www.hancom.co.kr/hwpml/2011/paragraph}tr')
            table_data = {
                'index': tbl_idx,
                'rows': len(rows),
                'cols': 0,
                'cells': []
            }
            
            for row_idx, row in enumerate(rows):
                cells = row.findall('.//{http://www.hancom.co.kr/hwpml/2011/paragraph}tc')
                if row_idx == 0:
                    table_data['cols'] = len(cells)
                    
                for col_idx, cell in enumerate(cells):
                    # 셀 텍스트 추출
                    texts = []
                    for t_elem in cell.findall('.//{http://www.hancom.co.kr/hwpml/2011/paragraph}t'):
                        if t_elem.text:
                            texts.append(t_elem.text)
                    
                    cell_text = ''.join(texts).strip()
                    
                    if cell_text and len(cell_text) > 1:  # 의미있는 내용만
                        # 헤더 vs 데이터 구분
                        is_header = row_idx < 2 or self._looks_like_header(cell_text)
                        
                        if not is_header:
                            field_name = f"T{tbl_idx}_R{row_idx}_C{col_idx}"
                            self.structure.fields.append(FieldInfo(
                                field_type=FieldType.TABLE_CELL,
                                name=field_name,
                                original_value=cell_text[:100],  # 최대 100자
                                location=f"테이블{tbl_idx} [{row_idx},{col_idx}]"
                            ))
                            
                        table_data['cells'].append({
                            'row': row_idx,
                            'col': col_idx,
                            'text': cell_text[:50],
                            'is_header': is_header
                        })
                        
            self.structure.tables.append(table_data)
            
    def _looks_like_header(self, text: str) -> bool:
        """헤더인지 판단"""
        header_keywords = ['구분', '항목', '내용', '비고', '코드', '명칭', '연도', '예산', 
                          '사업', '담당', '실국', '과', '부장', '과장', '대리']
        return any(kw in text for kw in header_keywords) and len(text) < 30
    
    def _analyze_keywords(self, content: str):
        """(키워드) 패턴 분석"""
        # (키워드) 패턴 찾기
        pattern = r'\(([^)]{2,30})\)'
        
        for match in re.finditer(pattern, content):
            keyword = match.group(1)
            
            # 이미 등록된 키워드 스킵
            if any(f.name == keyword for f in self.structure.fields):
                continue
                
            # 숫자만 있는 경우 스킵
            if keyword.replace(',', '').replace('.', '').replace('-', '').isdigit():
                continue
                
            self.structure.fields.append(FieldInfo(
                field_type=FieldType.KEYWORD,
                name=keyword,
                original_value=f"({keyword})",
                location="키워드 패턴"
            ))
            
    def _analyze_paragraphs(self, root):
        """일반 문단 분석 - 주요 내용 추출"""
        paras = root.findall('.//{http://www.hancom.co.kr/hwpml/2011/paragraph}p')
        
        important_patterns = [
            (r'□\s*\(([^)]+)\)\s*(.+)', 'section'),  # □ (제목) 내용
            (r'◦\s*\(([^)]+)\)\s*(.+)', 'subsection'),  # ◦ (소제목) 내용
            (r'[①②③④⑤⑥⑦⑧⑨⑩]\s*(.+)', 'numbered'),  # 번호 항목
        ]
        
        for p_idx, para in enumerate(paras):
            texts = []
            for t_elem in para.findall('.//{http://www.hancom.co.kr/hwpml/2011/paragraph}t'):
                if t_elem.text:
                    texts.append(t_elem.text)
            
            para_text = ''.join(texts).strip()
            
            if not para_text or len(para_text) < 10:
                continue
                
            # 중요 패턴 매칭
            for pattern, ptype in important_patterns:
                match = re.match(pattern, para_text)
                if match:
                    if ptype == 'section':
                        section_name = match.group(1)
                        self.structure.sections.append(section_name)
                    break
                    
    def generate_template(self, output_path: str, mode: str = 'placeholder'):
        """
        빈 템플릿 생성
        
        mode:
        - 'placeholder': 데이터 → (필드명) 플레이스홀더
        - 'empty': 데이터 → 빈 칸
        - 'marker': 데이터 → {{필드명}} 마커
        """
        # 임시 디렉토리에 압축 해제
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(self.source_path, 'r') as zf:
                zf.extractall(temp_dir)
            
            # section0.xml 수정
            section_path = os.path.join(temp_dir, 'Contents', 'section0.xml')
            with open(section_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 데이터 → 플레이스홀더 변환
            modified_content = self._convert_to_placeholders(content, mode)
            
            # linesegarray 제거 (자동 줄바꿈 위해)
            modified_content = re.sub(
                r'<hp:linesegarray[^>]*>.*?</hp:linesegarray>',
                '',
                modified_content,
                flags=re.DOTALL
            )
            
            with open(section_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            
            # 새 HWPX로 압축
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf_out:
                for root_dir, dirs, files in os.walk(temp_dir):
                    for file in files:
                        file_path = os.path.join(root_dir, file)
                        arc_name = os.path.relpath(file_path, temp_dir)
                        zf_out.write(file_path, arc_name)
                        
        print(f"✅ 템플릿 생성: {output_path}")
        return output_path
    
    def _convert_to_placeholders(self, content: str, mode: str) -> str:
        """데이터를 플레이스홀더로 변환 - XML 파싱으로 <hp:t> 텍스트만 수정"""
        
        # 분석 먼저 수행
        if not self.structure.fields:
            self.analyze()
        
        # XML 파싱
        for prefix, uri in NAMESPACES.items():
            ET.register_namespace(prefix, uri)
        
        root = ET.fromstring(content)
        
        # 모든 <hp:t> 태그 찾기
        hp_ns = '{http://www.hancom.co.kr/hwpml/2011/paragraph}'
        
        for t_elem in root.iter(f'{hp_ns}t'):
            # 텍스트 노드만 수정 (속성은 건드리지 않음)
            if t_elem.text:
                if mode == 'placeholder':
                    t_elem.text = re.sub(
                        r'(?<![0-9])(\d{1,3}(?:,\d{3})+|\d{4,})(?![0-9-])',
                        r'(금액)',
                        t_elem.text
                    )
                elif mode == 'empty':
                    t_elem.text = re.sub(
                        r'(?<![0-9])(\d{1,3}(?:,\d{3})+|\d{4,})(?![0-9-])',
                        r'',
                        t_elem.text
                    )
                elif mode == 'marker':
                    t_elem.text = re.sub(
                        r'(?<![0-9])(\d{1,3}(?:,\d{3})+|\d{4,})(?![0-9-])',
                        r'{{금액}}',
                        t_elem.text
                    )
        
        # XML로 다시 변환
        modified = ET.tostring(root, encoding='unicode')
        
        # XML 선언 복원 (원본에 있었다면)
        if content.startswith('<?xml'):
            xml_decl = content.split('?>')[0] + '?>\n'
            modified = xml_decl + modified
            
        return modified
    
    def export_field_map(self, output_path: str = None) -> str:
        """필드 맵 YAML/JSON 출력"""
        if not self.structure.fields:
            self.analyze()
            
        lines = ["# 템플릿 필드 맵", "# 이 파일을 참고하여 데이터를 매핑하세요", ""]
        
        # 섹션별 정리
        lines.append("## 섹션 목록")
        for section in self.structure.sections:
            lines.append(f"- {section}")
        lines.append("")
        
        # 키워드 필드
        keyword_fields = [f for f in self.structure.fields if f.field_type == FieldType.KEYWORD]
        if keyword_fields:
            lines.append("## 키워드 필드")
            for f in keyword_fields:
                lines.append(f"- ({f.name}): ")
            lines.append("")
            
        # 테이블 구조
        lines.append("## 테이블 구조")
        for tbl in self.structure.tables:
            lines.append(f"\n### 테이블 {tbl['index']} ({tbl['rows']}x{tbl['cols']})")
            
            # 헤더 표시
            headers = [c for c in tbl['cells'] if c['is_header']]
            if headers:
                lines.append("헤더: " + ", ".join(c['text'][:15] for c in headers[:5]))
                
        output = '\n'.join(lines)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"📋 필드맵 저장: {output_path}")
            
        return output


def print_analysis(structure: TemplateStructure):
    """분석 결과 출력"""
    print("\n" + "="*60)
    print("📊 문서 구조 분석 결과")
    print("="*60)
    
    print(f"\n📑 섹션: {len(structure.sections)}개")
    for s in structure.sections[:10]:
        print(f"  - {s}")
    if len(structure.sections) > 10:
        print(f"  ... 외 {len(structure.sections)-10}개")
        
    print(f"\n📦 테이블: {len(structure.tables)}개")
    for tbl in structure.tables[:5]:
        print(f"  - 테이블 {tbl['index']}: {tbl['rows']}행 x {tbl['cols']}열")
    if len(structure.tables) > 5:
        print(f"  ... 외 {len(structure.tables)-5}개")
        
    keyword_fields = [f for f in structure.fields if f.field_type == FieldType.KEYWORD]
    table_fields = [f for f in structure.fields if f.field_type == FieldType.TABLE_CELL]
    
    print(f"\n🔑 키워드 필드: {len(keyword_fields)}개")
    for f in keyword_fields[:10]:
        print(f"  - ({f.name})")
    if len(keyword_fields) > 10:
        print(f"  ... 외 {len(keyword_fields)-10}개")
        
    print(f"\n📝 테이블 데이터 필드: {len(table_fields)}개")
    
    print("\n" + "="*60)


def main():
    parser = argparse.ArgumentParser(description='HWPX 템플릿 생성기')
    parser.add_argument('source', help='원본 HWPX 파일')
    parser.add_argument('--output', '-o', help='출력 템플릿 파일')
    parser.add_argument('--analyze', '-a', action='store_true', help='구조 분석만')
    parser.add_argument('--mode', choices=['placeholder', 'empty', 'marker'], 
                       default='placeholder', help='변환 모드')
    parser.add_argument('--fieldmap', '-f', help='필드맵 출력 파일')
    
    args = parser.parse_args()
    
    generator = TemplateGenerator(args.source)
    
    if args.analyze:
        structure = generator.analyze()
        print_analysis(structure)
        
        if args.fieldmap:
            generator.export_field_map(args.fieldmap)
    else:
        # 기본: 분석 + 템플릿 생성
        structure = generator.analyze()
        print_analysis(structure)
        
        if args.output:
            generator.generate_template(args.output, args.mode)
            
        if args.fieldmap:
            generator.export_field_map(args.fieldmap)


if __name__ == '__main__':
    main()
