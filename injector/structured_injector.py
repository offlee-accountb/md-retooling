#!/usr/bin/env python3
"""
Structured Injector: 구조화된 HWPX 데이터 주입기
================================================
복수의 표와 텍스트를 구분하여 주입하는 확장 가능한 injector

지원 패턴:
1. 주제목 (TITLE): 첫 번째 표의 본문 셀
2. 섹션 제목 (SECTION): "< 제목 >" 패턴
3. 키워드 (KEYWORD): "(키워드)" 패턴 뒤에 내용
4. 표 데이터 (TABLE): 테이블 인덱스 + 셀 좌표로 주입

MD 파싱 → 구조화된 데이터 → HWPX 주입
"""

import json
import re
import shutil
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum, auto


# XML 네임스페이스
NS = {
    'hp': 'http://www.hancom.co.kr/hwpml/2011/paragraph',
    'hs': 'http://www.hancom.co.kr/hwpml/2011/section',
    'hc': 'http://www.hancom.co.kr/hwpml/2011/core',
}

for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

# linesegarray 제거 패턴
LINESEGARRAY_PATTERN = re.compile(r'<hp:linesegarray[^>]*>.*?</hp:linesegarray>', re.DOTALL)


class ContentType(Enum):
    """콘텐츠 유형"""
    TITLE = auto()          # 주제목
    SECTION = auto()        # 섹션 제목 (< 제목 >)
    KEYWORD = auto()        # 키워드 패턴 (키워드)
    TABLE = auto()          # 표 데이터
    PARAGRAPH = auto()      # 일반 문단


@dataclass
class ContentBlock:
    """콘텐츠 블록"""
    type: ContentType
    key: str                    # 식별자 (키워드명, 테이블 인덱스 등)
    value: Any                  # 값 (문자열 또는 표 데이터)
    metadata: Dict = field(default_factory=dict)


@dataclass
class TableData:
    """표 데이터"""
    headers: List[str]          # 헤더 행
    rows: List[List[str]]       # 데이터 행들
    table_index: int = 0        # HWPX 내 테이블 인덱스


@dataclass
class StructuredData:
    """구조화된 문서 데이터"""
    title: Optional[str] = None
    sections: Dict[str, str] = field(default_factory=dict)
    keywords: Dict[str, str] = field(default_factory=dict)
    tables: List[TableData] = field(default_factory=list)
    paragraphs: List[str] = field(default_factory=list)


@dataclass
class TemplateInfo:
    """템플릿 분석 정보"""
    title_table_index: Optional[int] = None     # 주제목 표 인덱스
    data_table_indices: List[int] = field(default_factory=list)  # 데이터 표 인덱스들
    section_patterns: List[str] = field(default_factory=list)    # 섹션 패턴들
    keyword_patterns: List[str] = field(default_factory=list)    # 키워드 패턴들
    table_structures: Dict[int, Tuple[int, int]] = field(default_factory=dict)  # {index: (rows, cols)}


@dataclass
class InjectionResult:
    """주입 결과"""
    success: bool
    output_path: str
    injected_count: int
    errors: List[str]
    details: List[str]


class MDParser:
    """마크다운 파서 - 구조화된 데이터 추출"""
    
    # 패턴들
    TITLE_PATTERN = re.compile(r'^<주제목>\s*(.+)$', re.MULTILINE)
    SECTION_PATTERN = re.compile(r'^<\s*([^>]+)\s*>$', re.MULTILINE)
    KEYWORD_PATTERN = re.compile(r'[◦○•\-\*]?\s*\(([^)]+)\)\s+(.+)')
    TABLE_PATTERN = re.compile(r'^\|(.+)\|$', re.MULTILINE)
    
    @classmethod
    def parse(cls, md_content: str) -> StructuredData:
        """MD 콘텐츠를 구조화된 데이터로 파싱"""
        data = StructuredData()
        
        lines = md_content.strip().split('\n')
        current_section = None
        table_lines = []
        in_table = False
        
        for line in lines:
            line = line.strip()
            
            # 빈 줄
            if not line:
                if in_table and table_lines:
                    # 표 종료
                    table_data = cls._parse_table(table_lines)
                    if table_data:
                        data.tables.append(table_data)
                    table_lines = []
                    in_table = False
                continue
            
            # 주제목
            title_match = cls.TITLE_PATTERN.match(line)
            if title_match:
                data.title = title_match.group(1).strip()
                continue
            
            # 섹션 제목 (< 제목 > 형태)
            section_match = cls.SECTION_PATTERN.match(line)
            if section_match:
                current_section = section_match.group(1).strip()
                data.sections[current_section] = ""
                continue
            
            # 표 행
            if line.startswith('|') and line.endswith('|'):
                in_table = True
                table_lines.append(line)
                continue
            
            # 키워드 패턴
            keyword_match = cls.KEYWORD_PATTERN.match(line)
            if keyword_match:
                keyword = keyword_match.group(1).strip()
                content = keyword_match.group(2).strip()
                data.keywords[keyword] = content
                continue
            
            # 일반 문단
            if line and not line.startswith('|'):
                data.paragraphs.append(line)
        
        # 마지막 표 처리
        if table_lines:
            table_data = cls._parse_table(table_lines)
            if table_data:
                data.tables.append(table_data)
        
        return data
    
    @classmethod
    def _parse_table(cls, lines: List[str]) -> Optional[TableData]:
        """표 라인들을 TableData로 파싱"""
        if len(lines) < 2:
            return None
        
        rows = []
        for line in lines:
            # | col1 | col2 | col3 | 형식 파싱
            cells = [c.strip() for c in line.strip('|').split('|')]
            rows.append(cells)
        
        # 첫 행 = 헤더, 두 번째 행이 구분선(---)이면 스킵
        headers = rows[0]
        data_rows = []
        
        for i, row in enumerate(rows[1:], 1):
            # 구분선 체크 (---로만 구성)
            if all(c.replace('-', '').strip() == '' for c in row):
                continue
            data_rows.append(row)
        
        return TableData(
            headers=headers,
            rows=data_rows,
            table_index=0  # 나중에 매핑
        )


class TemplateAnalyzer:
    """HWPX 템플릿 분석기"""
    
    def __init__(self, template_path: str | Path):
        self.template_path = Path(template_path)
    
    def analyze(self) -> TemplateInfo:
        """템플릿 구조 분석"""
        info = TemplateInfo()
        
        with tempfile.TemporaryDirectory() as tmpdir:
            with zipfile.ZipFile(self.template_path, 'r') as z:
                z.extractall(tmpdir)
            
            contents_dir = Path(tmpdir) / 'Contents'
            if not contents_dir.exists():
                return info
            
            for xml_file in contents_dir.glob('section*.xml'):
                self._analyze_section(xml_file, info)
        
        return info
    
    def _analyze_section(self, xml_path: Path, info: TemplateInfo):
        """section XML 분석"""
        with open(xml_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        try:
            root = ET.fromstring(content)
        except ET.ParseError:
            return
        
        # 테이블 분석
        tables = [el for el in root.iter() if el.tag.endswith('}tbl')]
        
        for i, tbl in enumerate(tables):
            row_cnt = int(tbl.get('rowCnt', 0))
            col_cnt = int(tbl.get('colCnt', 0))
            info.table_structures[i] = (row_cnt, col_cnt)
            
            # 주제목 표 판별 (3x1 구조, 가운데 셀에 텍스트)
            if row_cnt == 3 and col_cnt == 1:
                info.title_table_index = i
            else:
                info.data_table_indices.append(i)
        
        # 키워드 패턴 찾기
        keyword_pattern = re.compile(r'\(([^)]+)\)')
        for p in root.iter():
            if not p.tag.endswith('}p'):
                continue
            texts = [t.text for t in p.iter() if t.tag.endswith('}t') and t.text]
            full_text = ''.join(texts)
            
            for match in keyword_pattern.finditer(full_text):
                keyword = match.group(1)
                if len(keyword) >= 2 and not keyword.isdigit():
                    if keyword not in info.keyword_patterns:
                        info.keyword_patterns.append(keyword)
        
        # 섹션 패턴 찾기 (< 제목 > 형태)
        section_pattern = re.compile(r'<\s*([^>]+)\s*>')
        for p in root.iter():
            if not p.tag.endswith('}p'):
                continue
            texts = [t.text for t in p.iter() if t.tag.endswith('}t') and t.text]
            full_text = ''.join(texts)
            
            for match in section_pattern.finditer(full_text):
                section = match.group(1).strip()
                if section and section not in info.section_patterns:
                    info.section_patterns.append(section)


class StructuredInjector:
    """구조화된 HWPX 주입기"""
    
    def __init__(self, template_path: str | Path):
        self.template_path = Path(template_path)
        self.analyzer = TemplateAnalyzer(template_path)
        self.template_info = self.analyzer.analyze()
    
    def analyze(self) -> str:
        """템플릿 분석 결과 출력"""
        info = self.template_info
        
        lines = [
            "## 템플릿 분석 결과",
            f"- 파일: {self.template_path.name}",
            "",
            "### 테이블 구조",
        ]
        
        for idx, (rows, cols) in info.table_structures.items():
            role = ""
            if idx == info.title_table_index:
                role = " (주제목)"
            elif idx in info.data_table_indices:
                role = " (데이터)"
            lines.append(f"- 테이블 {idx}: {rows}행 x {cols}열{role}")
        
        if info.keyword_patterns:
            lines.extend(["", "### 키워드 패턴"])
            for kw in info.keyword_patterns:
                lines.append(f"- `({kw})`")
        
        if info.section_patterns:
            lines.extend(["", "### 섹션 패턴"])
            for sec in info.section_patterns:
                lines.append(f"- `< {sec} >`")
        
        return '\n'.join(lines)
    
    def generate_prompt(self, context: str = "") -> str:
        """
        데이터 수집을 위한 LLM 프롬프트 생성
        
        Args:
            context: 추가 컨텍스트 (원본 문서, 참고자료 등)
        
        Returns:
            LLM에게 보낼 프롬프트
        """
        info = self.template_info
        
        # 테이블 헤더 추출
        table_headers = self._extract_table_headers()
        
        lines = [
            "# 데이터 입력 요청",
            "",
            "아래 HWPX 템플릿에 채워넣을 데이터를 마크다운 형식으로 제공해주세요.",
            "",
            "---",
            "",
            "## 필요한 데이터",
            "",
        ]
        
        # 1. 주제목
        if info.title_table_index is not None:
            lines.extend([
                "### 1. 주제목",
                "```",
                "<주제목> [문서의 주제목을 입력]",
                "```",
                "",
            ])
        
        # 2. 키워드 필드
        if info.keyword_patterns:
            lines.extend([
                "### 2. 키워드 필드",
                "다음 키워드들의 내용을 채워주세요:",
                "```",
            ])
            for kw in info.keyword_patterns:
                lines.append(f"◦ ({kw}) [내용 입력]")
            lines.extend(["```", ""])
        
        # 3. 섹션
        if info.section_patterns:
            lines.extend([
                "### 3. 섹션 제목",
                "다음 섹션들이 있습니다 (필요시 내용 추가):",
            ])
            for sec in info.section_patterns:
                lines.append(f"- < {sec} >")
            lines.append("")
        
        # 4. 표 데이터
        if info.data_table_indices:
            lines.extend([
                "### 4. 표 데이터",
                "다음 표를 마크다운 형식으로 채워주세요:",
                "",
            ])
            
            for tbl_idx in info.data_table_indices:
                rows, cols = info.table_structures.get(tbl_idx, (0, 0))
                headers = table_headers.get(tbl_idx, [])
                
                lines.append(f"**표 {tbl_idx}** ({rows}행 x {cols}열):")
                lines.append("```")
                
                if headers:
                    lines.append("| " + " | ".join(headers) + " |")
                    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
                    # 샘플 행
                    lines.append("| " + " | ".join(["데이터"] * len(headers)) + " |")
                    lines.append("| ... |")
                else:
                    lines.append(f"| 컬럼1 | 컬럼2 | ... | 컬럼{cols} |")
                    lines.append("| --- | --- | ... | --- |")
                    lines.append("| 데이터 | 데이터 | ... | 데이터 |")
                
                lines.extend(["```", ""])
        
        # 5. 컨텍스트 (있으면)
        if context:
            lines.extend([
                "---",
                "",
                "## 참고 자료",
                "",
                context,
                "",
            ])
        
        # 6. 출력 형식 안내
        lines.extend([
            "---",
            "",
            "## 출력 형식",
            "",
            "위 항목들을 모두 포함한 마크다운 문서를 작성해주세요.",
            "표는 마크다운 테이블 형식(`| col1 | col2 |`)으로 작성해주세요.",
            "",
        ])
        
        return '\n'.join(lines)
    
    def _extract_table_headers(self) -> Dict[int, List[str]]:
        """템플릿에서 테이블 헤더 추출"""
        headers = {}
        
        with tempfile.TemporaryDirectory() as tmpdir:
            with zipfile.ZipFile(self.template_path, 'r') as z:
                z.extractall(tmpdir)
            
            contents_dir = Path(tmpdir) / 'Contents'
            if not contents_dir.exists():
                return headers
            
            for xml_file in contents_dir.glob('section*.xml'):
                with open(xml_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                try:
                    root = ET.fromstring(content)
                except ET.ParseError:
                    continue
                
                tables = [el for el in root.iter() if el.tag.endswith('}tbl')]
                
                for i, tbl in enumerate(tables):
                    if i not in self.template_info.data_table_indices:
                        continue
                    
                    # 첫 번째 행(헤더) 추출
                    row_headers = []
                    for tc in tbl.iter():
                        if not tc.tag.endswith('}tc'):
                            continue
                        
                        cell_addr = None
                        for child in tc:
                            if child.tag.endswith('}cellAddr'):
                                cell_addr = child
                                break
                        
                        if cell_addr is not None and cell_addr.get('rowAddr') == '0':
                            # 헤더 행
                            texts = [t.text for t in tc.iter() if t.tag.endswith('}t') and t.text]
                            text = ''.join(texts).strip() or f"컬럼{len(row_headers)+1}"
                            row_headers.append(text)
                    
                    if row_headers:
                        headers[i] = row_headers
        
        return headers
    
    def inject(self, data: StructuredData, output_path: str | Path) -> InjectionResult:
        """구조화된 데이터 주입"""
        output_path = Path(output_path)
        errors = []
        details = []
        injected_count = 0
        
        with tempfile.TemporaryDirectory() as tmpdir:
            # 압축 해제
            with zipfile.ZipFile(self.template_path, 'r') as z:
                z.extractall(tmpdir)
            
            contents_dir = Path(tmpdir) / 'Contents'
            if contents_dir.exists():
                for xml_file in contents_dir.glob('section*.xml'):
                    try:
                        count, detail_list = self._process_section(xml_file, data)
                        injected_count += count
                        details.extend(detail_list)
                    except Exception as e:
                        errors.append(f"{xml_file.name}: {str(e)}")
            
            # 다시 압축
            output_path.parent.mkdir(parents=True, exist_ok=True)
            self._rezip(tmpdir, output_path)
        
        return InjectionResult(
            success=len(errors) == 0,
            output_path=str(output_path),
            injected_count=injected_count,
            errors=errors,
            details=details,
        )
    
    def _process_section(self, xml_path: Path, data: StructuredData) -> Tuple[int, List[str]]:
        """section XML 처리"""
        with open(xml_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # linesegarray 제거
        content = LINESEGARRAY_PATTERN.sub('', content)
        
        count = 0
        details = []
        
        try:
            root = ET.fromstring(content)
        except ET.ParseError as e:
            return 0, [f"XML 파싱 실패: {e}"]
        
        # 1. 주제목 주입
        if data.title and self.template_info.title_table_index is not None:
            c, d = self._inject_title(root, data.title)
            count += c
            details.extend(d)
        
        # 2. 키워드 주입
        if data.keywords:
            c, d = self._inject_keywords(root, data.keywords)
            count += c
            details.extend(d)
        
        # 3. 표 데이터 주입
        if data.tables:
            c, d = self._inject_tables(root, data.tables)
            count += c
            details.extend(d)
        
        # 저장
        new_content = '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>'
        new_content += ET.tostring(root, encoding='unicode')
        
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return count, details
    
    def _inject_title(self, root: ET.Element, title: str) -> Tuple[int, List[str]]:
        """주제목 주입 (첫 번째 3x1 표의 가운데 셀)"""
        tables = [el for el in root.iter() if el.tag.endswith('}tbl')]
        
        if self.template_info.title_table_index is None:
            return 0, ["⚠️ 주제목 표를 찾을 수 없음"]
        
        if self.template_info.title_table_index >= len(tables):
            return 0, ["⚠️ 주제목 표 인덱스 범위 초과"]
        
        tbl = tables[self.template_info.title_table_index]
        
        # 가운데 셀 (rowAddr=1) 찾기
        for tc in tbl.iter():
            if not tc.tag.endswith('}tc'):
                continue
            
            cell_addr = None
            for child in tc:
                if child.tag.endswith('}cellAddr'):
                    cell_addr = child
                    break
            
            if cell_addr is not None and cell_addr.get('rowAddr') == '1':
                # 이 셀에 주제목 설정
                for t in tc.iter():
                    if t.tag.endswith('}t'):
                        t.text = title
                        return 1, [f"✅ 주제목 주입: {title[:30]}..."]
        
        return 0, ["⚠️ 주제목 셀을 찾을 수 없음"]
    
    def _inject_keywords(self, root: ET.Element, keywords: Dict[str, str]) -> Tuple[int, List[str]]:
        """키워드 패턴 뒤에 내용 주입"""
        count = 0
        details = []
        keyword_pattern = re.compile(r'\(([^)]+)\)')
        
        for p in root.iter():
            if not p.tag.endswith('}p'):
                continue
            
            for run in p:
                if not run.tag.endswith('}run'):
                    continue
                
                for t in run.iter():
                    if not t.tag.endswith('}t') or not t.text:
                        continue
                    
                    for match in keyword_pattern.finditer(t.text):
                        kw = match.group(1).strip()
                        if kw in keywords:
                            value = keywords[kw]
                            # "(키워드)" → "(키워드) 값"
                            original = t.text
                            t.text = original.replace(
                                match.group(0),
                                f"{match.group(0)} {value}"
                            )
                            count += 1
                            details.append(f"✅ ({kw}) 주입: {value[:30]}...")
        
        return count, details
    
    def _inject_tables(self, root: ET.Element, tables_data: List[TableData]) -> Tuple[int, List[str]]:
        """표 데이터 주입"""
        count = 0
        details = []
        
        # HWPX 내 테이블들
        hwpx_tables = [el for el in root.iter() if el.tag.endswith('}tbl')]
        
        # 데이터 테이블 인덱스들에 순차적으로 매핑
        for data_idx, table_data in enumerate(tables_data):
            if data_idx >= len(self.template_info.data_table_indices):
                details.append(f"⚠️ 표 {data_idx}: 매핑할 템플릿 테이블 없음")
                continue
            
            tbl_idx = self.template_info.data_table_indices[data_idx]
            if tbl_idx >= len(hwpx_tables):
                continue
            
            tbl = hwpx_tables[tbl_idx]
            tbl_rows, tbl_cols = self.template_info.table_structures.get(tbl_idx, (0, 0))
            
            details.append(f"📊 표 {tbl_idx} ({tbl_rows}x{tbl_cols}) 주입 시작")
            
            # 셀 매핑 (헤더 제외, row 1부터)
            for row_idx, row_data in enumerate(table_data.rows):
                hwpx_row = row_idx + 1  # 헤더 스킵
                
                for col_idx, cell_value in enumerate(row_data):
                    if col_idx >= tbl_cols:
                        continue
                    
                    # 해당 좌표의 셀 찾기
                    injected = self._set_table_cell(tbl, hwpx_row, col_idx, cell_value)
                    if injected:
                        count += 1
            
            details.append(f"  → {len(table_data.rows)}행 x {len(table_data.headers)}열 주입 완료")
        
        return count, details
    
    def _set_table_cell(self, tbl: ET.Element, row: int, col: int, value: str) -> bool:
        """테이블 셀에 값 설정"""
        for tc in tbl.iter():
            if not tc.tag.endswith('}tc'):
                continue
            
            cell_addr = None
            for child in tc:
                if child.tag.endswith('}cellAddr'):
                    cell_addr = child
                    break
            
            if cell_addr is None:
                continue
            
            if cell_addr.get('rowAddr') == str(row) and cell_addr.get('colAddr') == str(col):
                # 이 셀에 값 설정
                for t in tc.iter():
                    if t.tag.endswith('}t'):
                        t.text = value
                        return True
                
                # hp:t가 없으면 생성
                for sublist in tc.iter():
                    if sublist.tag.endswith('}subList'):
                        for p in sublist:
                            if p.tag.endswith('}p'):
                                for run in p:
                                    if run.tag.endswith('}run'):
                                        t = ET.SubElement(run, f'{{{NS["hp"]}}}t')
                                        t.text = value
                                        return True
        
        return False
    
    def _rezip(self, src_dir: str, out_path: Path):
        """HWPX로 압축"""
        import os
        
        with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as z:
            mimetype_path = Path(src_dir) / 'mimetype'
            if mimetype_path.exists():
                with open(mimetype_path, 'rb') as f:
                    z.writestr('mimetype', f.read(), compress_type=zipfile.ZIP_STORED)
            
            for root_dir, dirs, files in os.walk(src_dir):
                for fn in files:
                    if fn == 'mimetype':
                        continue
                    full_path = Path(root_dir) / fn
                    arcname = full_path.relative_to(src_dir)
                    z.write(full_path, arcname)


def main():
    """CLI"""
    import argparse
    
    parser = argparse.ArgumentParser(description='구조화된 HWPX 데이터 주입기')
    parser.add_argument('template', help='템플릿 HWPX 파일')
    parser.add_argument('--md', '-m', help='MD 데이터 파일')
    parser.add_argument('--output', '-o', help='출력 HWPX 파일')
    parser.add_argument('--analyze', '-a', action='store_true', help='분석만 수행')
    parser.add_argument('--prompt', '-p', action='store_true', help='데이터 수집용 프롬프트 생성')
    parser.add_argument('--context', '-c', help='프롬프트에 포함할 참고자료 파일')
    
    args = parser.parse_args()
    
    if not Path(args.template).exists():
        print(f"❌ 파일 없음: {args.template}")
        return 1
    
    injector = StructuredInjector(args.template)
    
    # 분석 모드
    if args.analyze:
        print(injector.analyze())
        return 0
    
    # 프롬프트 생성 모드
    if args.prompt:
        context = ""
        if args.context and Path(args.context).exists():
            with open(args.context, 'r', encoding='utf-8') as f:
                context = f.read()
        
        print(injector.generate_prompt(context))
        return 0
    
    # 주입 모드
    if not args.md:
        print("❌ --md 옵션 필요")
        return 1
    
    # MD 파싱
    with open(args.md, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    data = MDParser.parse(md_content)
    
    print("📝 MD 파싱 결과:")
    if data.title:
        print(f"  - 주제목: {data.title[:50]}...")
    if data.sections:
        print(f"  - 섹션: {list(data.sections.keys())}")
    if data.keywords:
        print(f"  - 키워드: {list(data.keywords.keys())}")
    if data.tables:
        for i, tbl in enumerate(data.tables):
            print(f"  - 표 {i}: {len(tbl.rows)}행 x {len(tbl.headers)}열")
    print()
    
    # 출력 경로
    output = args.output or args.template.replace('.hwpx', '_injected.hwpx')
    
    # 주입 실행
    result = injector.inject(data, output)
    
    print("=" * 60)
    print(f"📄 템플릿: {args.template}")
    print(f"📁 출력: {result.output_path}")
    print("=" * 60)
    print(f"✅ 주입 성공: {result.injected_count}개")
    
    if result.details:
        print("\n📋 상세:")
        for d in result.details:
            print(f"  {d}")
    
    if result.errors:
        print("\n⚠️ 오류:")
        for err in result.errors:
            print(f"  - {err}")
    
    return 0 if result.success else 1


if __name__ == "__main__":
    exit(main())
