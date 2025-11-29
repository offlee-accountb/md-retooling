#!/usr/bin/env python3
"""
Template Analyzer: HWPX 템플릿 분석 및 필드 추출
================================================
- 템플릿 유형 자동 감지 (placeholder, gov_form, plain)
- 필드 목록 추출 ({{KEY}}, name 속성, 좌표)
- LLM 컨텍스트 생성용 구조 분석
"""

import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum


class TemplateType(Enum):
    PLACEHOLDER = "placeholder"  # {{KEY}} 패턴
    GOV_FORM = "gov_form"        # name="AAA*..." 패턴
    PLAIN = "plain"              # 태깅 없음 (좌표 기반 필요)
    MIXED = "mixed"              # 복합


@dataclass
class FieldInfo:
    """추출된 필드 정보"""
    name: str                    # 필드명
    field_type: str              # "placeholder", "gov_field", "coordinate"
    location: str                # "body" or "table_{idx}"
    context: str = ""            # 주변 텍스트 (헤더 등)
    coordinate: Optional[Tuple[int, int]] = None  # (row, col) for table cells
    table_index: Optional[int] = None
    editable: bool = True


@dataclass
class TableInfo:
    """테이블 구조 정보"""
    index: int
    rows: int
    cols: int
    cells: List[Dict] = field(default_factory=list)  # [{row, col, text, name, editable}]
    headers: List[str] = field(default_factory=list)  # 첫 행 텍스트


@dataclass
class AnalysisResult:
    """분석 결과"""
    template_type: TemplateType
    fields: List[FieldInfo]
    tables: List[TableInfo]
    body_text_preview: str = ""
    raw_placeholders: List[str] = field(default_factory=list)
    raw_gov_fields: List[str] = field(default_factory=list)


# XML 네임스페이스
NS = {
    'hp': 'http://www.hancom.co.kr/hwpml/2011/paragraph',
    'hs': 'http://www.hancom.co.kr/hwpml/2011/section',
    'hc': 'http://www.hancom.co.kr/hwpml/2011/core',
}


class TemplateAnalyzer:
    """HWPX 템플릿 분석기"""
    
    # 패턴 정의
    PLACEHOLDER_PATTERN = re.compile(r'\{\{\s*([A-Za-z0-9_가-힣]+)\s*\}\}')
    GOV_FIELD_PATTERN = re.compile(r'name="([A-Z]+\*[^"]+)"')
    
    def __init__(self, hwpx_path: str | Path):
        self.hwpx_path = Path(hwpx_path)
        self.section_xmls: Dict[str, str] = {}
        self._load_sections()
    
    def _load_sections(self):
        """HWPX에서 section*.xml 로드"""
        with zipfile.ZipFile(self.hwpx_path, 'r') as z:
            for name in z.namelist():
                if 'section' in name.lower() and name.endswith('.xml'):
                    self.section_xmls[name] = z.read(name).decode('utf-8')
    
    def analyze(self) -> AnalysisResult:
        """전체 분석 수행"""
        all_placeholders = []
        all_gov_fields = []
        all_fields = []
        all_tables = []
        body_texts = []
        
        for section_name, xml_content in self.section_xmls.items():
            # 플레이스홀더 추출
            placeholders = self._extract_placeholders(xml_content)
            all_placeholders.extend(placeholders)
            
            # 정부 양식 필드 추출
            gov_fields = self._extract_gov_fields(xml_content)
            all_gov_fields.extend(gov_fields)
            
            # 테이블 구조 분석
            tables = self._analyze_tables(xml_content)
            all_tables.extend(tables)
            
            # 본문 텍스트 미리보기
            body_texts.append(self._extract_body_preview(xml_content))
        
        # 필드 정보 통합
        all_fields = self._build_field_list(all_placeholders, all_gov_fields, all_tables)
        
        # 템플릿 타입 결정
        template_type = self._determine_type(all_placeholders, all_gov_fields, all_tables)
        
        return AnalysisResult(
            template_type=template_type,
            fields=all_fields,
            tables=all_tables,
            body_text_preview="\n".join(body_texts)[:500],
            raw_placeholders=list(set(all_placeholders)),
            raw_gov_fields=list(set(all_gov_fields)),
        )
    
    def _extract_placeholders(self, xml_content: str) -> List[str]:
        """{{KEY}} 패턴 추출"""
        return self.PLACEHOLDER_PATTERN.findall(xml_content)
    
    def _extract_gov_fields(self, xml_content: str) -> List[str]:
        """name="AAA*..." 패턴 추출 (빈 값 제외)"""
        matches = self.GOV_FIELD_PATTERN.findall(xml_content)
        # 빈 name="" 제외, 실제 필드명만
        return [m for m in matches if m and '*' in m]
    
    def _analyze_tables(self, xml_content: str) -> List[TableInfo]:
        """테이블 구조 분석"""
        tables = []
        
        try:
            # XML 파싱 (네임스페이스 처리)
            root = ET.fromstring(xml_content)
        except ET.ParseError:
            return tables
        
        # hp:tbl 찾기
        for tbl_idx, tbl in enumerate(root.findall('.//hp:tbl', NS)):
            row_cnt = int(tbl.get('rowCnt', 0))
            col_cnt = int(tbl.get('colCnt', 0))
            
            cells = []
            headers = []
            
            # hp:tr → hp:tc 순회
            for tr_idx, tr in enumerate(tbl.findall('.//hp:tr', NS)):
                for tc in tr.findall('hp:tc', NS):
                    cell_addr = tc.find('hp:cellAddr', NS)
                    if cell_addr is None:
                        continue
                    
                    row = int(cell_addr.get('rowAddr', 0))
                    col = int(cell_addr.get('colAddr', 0))
                    
                    # 셀 텍스트 추출
                    cell_text = self._extract_cell_text(tc)
                    
                    # name 속성
                    name_attr = tc.get('name', '')
                    
                    # protect 속성 (편집 가능 여부)
                    protect = tc.get('protect', '0')
                    editable = protect != '1'
                    
                    cell_info = {
                        'row': row,
                        'col': col,
                        'text': cell_text,
                        'name': name_attr,
                        'editable': editable,
                    }
                    cells.append(cell_info)
                    
                    # 첫 행은 헤더로
                    if row == 0:
                        headers.append(cell_text)
            
            tables.append(TableInfo(
                index=tbl_idx,
                rows=row_cnt,
                cols=col_cnt,
                cells=cells,
                headers=headers,
            ))
        
        return tables
    
    def _extract_cell_text(self, tc_element) -> str:
        """셀에서 텍스트 추출"""
        texts = []
        for t in tc_element.iter():
            if t.tag.endswith('}t') and t.text:
                texts.append(t.text)
        return ' '.join(texts).strip()
    
    def _extract_body_preview(self, xml_content: str) -> str:
        """본문 텍스트 미리보기 추출"""
        try:
            root = ET.fromstring(xml_content)
        except ET.ParseError:
            return ""
        
        texts = []
        for t in root.iter():
            if t.tag.endswith('}t') and t.text:
                texts.append(t.text.strip())
        
        return ' '.join(texts)[:200]
    
    def _build_field_list(self, placeholders: List[str], gov_fields: List[str], 
                          tables: List[TableInfo]) -> List[FieldInfo]:
        """필드 정보 목록 생성"""
        fields = []
        
        # 플레이스홀더 → FieldInfo
        for ph in set(placeholders):
            fields.append(FieldInfo(
                name=ph,
                field_type="placeholder",
                location="body",  # TODO: 테이블 내부인지 구분
            ))
        
        # 정부 양식 필드 → FieldInfo
        for gf in set(gov_fields):
            # "AAA*TABLE*FIELD*N" → "TABLE*FIELD"
            parts = gf.split('*')
            if len(parts) >= 3:
                field_name = '*'.join(parts[1:-1])
            else:
                field_name = gf
            
            fields.append(FieldInfo(
                name=field_name,
                field_type="gov_field",
                location="table",
                context=gf,  # 원본 패턴 보존
            ))
        
        # 테이블 셀 중 빈 칸 + 편집 가능 → 좌표 기반 필드
        for tbl in tables:
            for cell in tbl.cells:
                # 빈 칸이고 편집 가능하면 잠재적 입력 필드
                if not cell['text'] and cell['editable'] and not cell['name']:
                    fields.append(FieldInfo(
                        name=f"table{tbl.index}_r{cell['row']}_c{cell['col']}",
                        field_type="coordinate",
                        location=f"table_{tbl.index}",
                        coordinate=(cell['row'], cell['col']),
                        table_index=tbl.index,
                    ))
        
        return fields
    
    def _determine_type(self, placeholders: List[str], gov_fields: List[str],
                        tables: List[TableInfo]) -> TemplateType:
        """템플릿 타입 결정"""
        has_placeholder = len(placeholders) > 0
        has_gov_field = len(gov_fields) > 0
        
        if has_placeholder and has_gov_field:
            return TemplateType.MIXED
        elif has_placeholder:
            return TemplateType.PLACEHOLDER
        elif has_gov_field:
            return TemplateType.GOV_FORM
        else:
            return TemplateType.PLAIN
    
    def get_llm_context(self) -> str:
        """LLM에 전달할 컨텍스트 문자열 생성"""
        result = self.analyze()
        
        lines = [
            "## 템플릿 분석 결과",
            f"- 타입: {result.template_type.value}",
            f"- 플레이스홀더: {result.raw_placeholders}",
            f"- 정부양식 필드: {len(result.raw_gov_fields)}개",
            f"- 테이블: {len(result.tables)}개",
            "",
        ]
        
        # 테이블 구조
        for tbl in result.tables:
            lines.append(f"### 테이블 {tbl.index} ({tbl.rows}x{tbl.cols})")
            lines.append("| 좌표 | 텍스트 | 필드명 | 편집가능 |")
            lines.append("|------|--------|--------|---------|")
            for cell in tbl.cells[:20]:  # 최대 20개만
                coord = f"({cell['row']},{cell['col']})"
                text = cell['text'][:15] if cell['text'] else "(빈칸)"
                name = cell['name'][:20] if cell['name'] else "-"
                edit = "✅" if cell['editable'] else "❌"
                lines.append(f"| {coord} | {text} | {name} | {edit} |")
            if len(tbl.cells) > 20:
                lines.append(f"| ... | ({len(tbl.cells) - 20}개 더) | ... | ... |")
            lines.append("")
        
        # 필드 목록
        lines.append("### 감지된 필드")
        for f in result.fields[:30]:
            lines.append(f"- `{f.name}` ({f.field_type}) @ {f.location}")
        
        return "\n".join(lines)


def main():
    """CLI 테스트"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python template_analyzer.py <hwpx_file>")
        print("\nExample:")
        print("  python template_analyzer.py input/test_templates/tier1_1_body_only.hwpx")
        sys.exit(1)
    
    hwpx_path = sys.argv[1]
    
    if not Path(hwpx_path).exists():
        print(f"❌ 파일 없음: {hwpx_path}")
        sys.exit(1)
    
    analyzer = TemplateAnalyzer(hwpx_path)
    result = analyzer.analyze()
    
    print("=" * 60)
    print(f"📄 파일: {hwpx_path}")
    print("=" * 60)
    print(f"템플릿 타입: {result.template_type.value}")
    print(f"플레이스홀더: {result.raw_placeholders}")
    print(f"정부양식 필드: {len(result.raw_gov_fields)}개")
    print(f"테이블: {len(result.tables)}개")
    print()
    
    print("--- LLM Context ---")
    print(analyzer.get_llm_context())


if __name__ == "__main__":
    main()
