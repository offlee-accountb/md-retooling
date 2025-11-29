#!/usr/bin/env python3
"""
Data Extractor: HWPX에서 데이터 추출 및 LLM 컨텍스트 생성
=========================================================
기능:
1. HWPX에서 텍스트/표 데이터 추출
2. 템플릿 필드와 매칭용 프롬프트 생성
3. LLM 응답 검증

워크플로우:
  데이터 HWPX → Python 추출 → LLM 프롬프트 → LLM 매칭 → MD 출력 → 템플릿 주입
"""

import json
import re
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field


@dataclass
class ExtractedTable:
    """추출된 표 데이터"""
    index: int
    rows: int
    cols: int
    headers: List[str]
    data: List[List[str]]
    raw_cells: Dict[Tuple[int, int], str] = field(default_factory=dict)


@dataclass
class ExtractedData:
    """HWPX에서 추출된 전체 데이터"""
    tables: List[ExtractedTable] = field(default_factory=list)
    paragraphs: List[str] = field(default_factory=list)
    keywords: Dict[str, str] = field(default_factory=dict)  # (키워드) → 뒤따르는 내용
    title: Optional[str] = None
    raw_text: str = ""


class DataExtractor:
    """HWPX 데이터 추출기"""
    
    KEYWORD_PATTERN = re.compile(r'\(([^)]{2,30})\)\s*([^◦○•\-\n]+)?')
    
    def __init__(self, hwpx_path: str | Path):
        self.hwpx_path = Path(hwpx_path)
    
    def extract(self) -> ExtractedData:
        """HWPX에서 모든 데이터 추출"""
        data = ExtractedData()
        
        with tempfile.TemporaryDirectory() as tmpdir:
            with zipfile.ZipFile(self.hwpx_path, 'r') as z:
                z.extractall(tmpdir)
            
            contents_dir = Path(tmpdir) / 'Contents'
            if not contents_dir.exists():
                return data
            
            for xml_file in sorted(contents_dir.glob('section*.xml')):
                self._extract_from_section(xml_file, data)
        
        return data
    
    def _extract_from_section(self, xml_path: Path, data: ExtractedData):
        """section XML에서 데이터 추출"""
        with open(xml_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        try:
            root = ET.fromstring(content)
        except ET.ParseError:
            return
        
        # 1. 테이블 추출
        tables = [el for el in root.iter() if el.tag.endswith('}tbl')]
        for i, tbl in enumerate(tables):
            extracted = self._extract_table(tbl, i)
            if extracted:
                data.tables.append(extracted)
        
        # 2. 문단 추출
        for p in root.iter():
            if not p.tag.endswith('}p'):
                continue
            
            # 테이블 내부 문단 제외
            is_in_table = False
            for parent in root.iter():
                if parent.tag.endswith('}tbl'):
                    if p in parent.iter():
                        is_in_table = True
                        break
            
            if is_in_table:
                continue
            
            texts = [t.text for t in p.iter() if t.tag.endswith('}t') and t.text]
            full_text = ''.join(texts).strip()
            
            if full_text and len(full_text) > 2:
                data.paragraphs.append(full_text)
                
                # 키워드 패턴 추출
                for match in self.KEYWORD_PATTERN.finditer(full_text):
                    keyword = match.group(1)
                    content = match.group(2)
                    if content:
                        data.keywords[keyword] = content.strip()
        
        # 3. 전체 텍스트
        all_texts = []
        for t in root.iter():
            if t.tag.endswith('}t') and t.text:
                all_texts.append(t.text)
        data.raw_text = '\n'.join(all_texts)
        
        # 4. 제목 추출 (첫 번째 3x1 표가 있으면)
        for tbl_data in data.tables:
            if tbl_data.rows == 3 and tbl_data.cols == 1:
                # 가운데 셀이 제목
                if (1, 0) in tbl_data.raw_cells:
                    data.title = tbl_data.raw_cells[(1, 0)]
                break
    
    def _extract_table(self, tbl: ET.Element, index: int) -> Optional[ExtractedTable]:
        """테이블에서 데이터 추출"""
        row_cnt = int(tbl.get('rowCnt', 0))
        col_cnt = int(tbl.get('colCnt', 0))
        
        if row_cnt == 0 or col_cnt == 0:
            return None
        
        # 셀 데이터 수집
        cells: Dict[Tuple[int, int], str] = {}
        
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
            
            row = int(cell_addr.get('rowAddr', 0))
            col = int(cell_addr.get('colAddr', 0))
            
            texts = [t.text for t in tc.iter() if t.tag.endswith('}t') and t.text]
            text = ''.join(texts).strip()
            
            cells[(row, col)] = text
        
        # 헤더 추출 (첫 번째 행)
        headers = []
        for c in range(col_cnt):
            headers.append(cells.get((0, c), f"컬럼{c+1}"))
        
        # 데이터 행 추출
        data_rows = []
        for r in range(1, row_cnt):
            row_data = []
            for c in range(col_cnt):
                row_data.append(cells.get((r, c), ""))
            data_rows.append(row_data)
        
        return ExtractedTable(
            index=index,
            rows=row_cnt,
            cols=col_cnt,
            headers=headers,
            data=data_rows,
            raw_cells=cells,
        )
    
    def to_markdown(self) -> str:
        """추출된 데이터를 마크다운으로 변환"""
        data = self.extract()
        lines = []
        
        # 제목
        if data.title:
            lines.append(f"# {data.title}")
            lines.append("")
        
        # 키워드 데이터
        if data.keywords:
            lines.append("## 키워드 데이터")
            lines.append("")
            for kw, content in data.keywords.items():
                lines.append(f"- **({kw})**: {content}")
            lines.append("")
        
        # 테이블
        for tbl in data.tables:
            # 1x1 테이블은 인용문으로 처리
            if tbl.rows == 1 and tbl.cols == 1:
                text = tbl.raw_cells.get((0, 0), "")
                if text:
                    lines.append(f"> {text[:200]}...")
                    lines.append("")
                continue
            
            # 3x1 주제목 표는 스킵 (이미 제목으로 처리)
            if tbl.rows == 3 and tbl.cols == 1:
                continue
            
            lines.append(f"## 표 {tbl.index} ({tbl.rows}x{tbl.cols})")
            lines.append("")
            
            # 마크다운 테이블
            lines.append("| " + " | ".join(tbl.headers) + " |")
            lines.append("| " + " | ".join(["---"] * len(tbl.headers)) + " |")
            
            for row in tbl.data[:20]:  # 최대 20행
                # 셀 내용 정리 (줄바꿈, 긴 텍스트 처리)
                cleaned = [cell.replace('\n', ' ')[:50] for cell in row]
                lines.append("| " + " | ".join(cleaned) + " |")
            
            if len(tbl.data) > 20:
                lines.append(f"| ... ({len(tbl.data) - 20}행 더) |")
            
            lines.append("")
        
        # 주요 문단
        if data.paragraphs:
            lines.append("## 주요 문단")
            lines.append("")
            for p in data.paragraphs[:30]:  # 최대 30개
                if len(p) > 10:
                    lines.append(f"- {p[:100]}...")
            lines.append("")
        
        return '\n'.join(lines)


class ContextGenerator:
    """LLM 프롬프트 컨텍스트 생성기"""
    
    def __init__(self, source_hwpx: str | Path, template_hwpx: str | Path):
        self.source_extractor = DataExtractor(source_hwpx)
        self.template_path = Path(template_hwpx)
        
        # 템플릿 분석 (structured_injector 재사용)
        from structured_injector import TemplateAnalyzer
        self.template_analyzer = TemplateAnalyzer(template_hwpx)
        self.template_info = self.template_analyzer.analyze()
    
    def generate_prompt(self) -> str:
        """LLM 매칭용 프롬프트 생성"""
        # 1. 원본 데이터 추출
        source_md = self.source_extractor.to_markdown()
        
        # 2. 템플릿 필드 추출
        template_fields = self._get_template_fields()
        
        # 3. 프롬프트 조합
        prompt = f"""# 데이터 매칭 요청

아래 **원본 데이터**를 분석하여, **템플릿 필드**에 맞는 값을 추출해주세요.

---

## 원본 데이터

{source_md}

---

## 템플릿 필드 (채워야 할 항목)

{template_fields}

---

## 출력 형식

아래 마크다운 형식으로 정확히 출력해주세요:

```markdown
<주제목> [추출한 주제목]

[키워드 필드가 있으면]
◦ (키워드1) [매칭된 내용]
◦ (키워드2) [매칭된 내용]

[표가 있으면]
| 헤더1 | 헤더2 | ... |
|-------|-------|-----|
| 데이터 | 데이터 | ... |
```

**주의사항:**
- 원본 데이터에서 정확히 매칭되는 값을 추출하세요
- 값이 없으면 "(데이터 없음)"으로 표시하세요
- 표의 행 수는 원본 데이터에 맞춰주세요
"""
        
        return prompt
    
    def _get_template_fields(self) -> str:
        """템플릿 필드 목록 생성"""
        info = self.template_info
        lines = []
        
        # 주제목
        if info.title_table_index is not None:
            lines.append("### 1. 주제목")
            lines.append("- 문서의 주제목을 추출하세요")
            lines.append("")
        
        # 키워드
        if info.keyword_patterns:
            lines.append("### 2. 키워드 필드")
            for kw in info.keyword_patterns:
                lines.append(f"- `({kw})`: 해당 내용 추출")
            lines.append("")
        
        # 표
        if info.data_table_indices:
            lines.append("### 3. 표 데이터")
            for idx in info.data_table_indices:
                rows, cols = info.table_structures.get(idx, (0, 0))
                lines.append(f"- 표 {idx}: {rows}행 x {cols}열")
                
                # 헤더 정보 (있으면)
                headers = self._get_table_headers(idx)
                if headers:
                    lines.append(f"  - 헤더: {', '.join(headers)}")
            lines.append("")
        
        return '\n'.join(lines)
    
    def _get_table_headers(self, table_idx: int) -> List[str]:
        """템플릿 테이블의 헤더 추출"""
        headers = []
        
        with tempfile.TemporaryDirectory() as tmpdir:
            with zipfile.ZipFile(self.template_path, 'r') as z:
                z.extractall(tmpdir)
            
            contents_dir = Path(tmpdir) / 'Contents'
            for xml_file in contents_dir.glob('section*.xml'):
                with open(xml_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                try:
                    root = ET.fromstring(content)
                except ET.ParseError:
                    continue
                
                tables = [el for el in root.iter() if el.tag.endswith('}tbl')]
                if table_idx >= len(tables):
                    continue
                
                tbl = tables[table_idx]
                
                for tc in tbl.iter():
                    if not tc.tag.endswith('}tc'):
                        continue
                    
                    cell_addr = None
                    for child in tc:
                        if child.tag.endswith('}cellAddr'):
                            cell_addr = child
                            break
                    
                    if cell_addr is not None and cell_addr.get('rowAddr') == '0':
                        texts = [t.text for t in tc.iter() if t.tag.endswith('}t') and t.text]
                        text = ''.join(texts).strip()
                        headers.append(text or f"컬럼{len(headers)+1}")
        
        return headers


def main():
    """CLI"""
    import argparse
    
    parser = argparse.ArgumentParser(description='HWPX 데이터 추출기')
    parser.add_argument('source', help='데이터 원본 HWPX 파일')
    parser.add_argument('--template', '-t', help='템플릿 HWPX 파일 (매칭용)')
    parser.add_argument('--extract', '-e', action='store_true', help='데이터만 추출 (MD 출력)')
    parser.add_argument('--prompt', '-p', action='store_true', help='LLM 프롬프트 생성')
    parser.add_argument('--output', '-o', help='출력 파일')
    
    args = parser.parse_args()
    
    if not Path(args.source).exists():
        print(f"❌ 파일 없음: {args.source}")
        return 1
    
    # 데이터 추출만
    if args.extract:
        extractor = DataExtractor(args.source)
        md = extractor.to_markdown()
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(md)
            print(f"✅ 저장됨: {args.output}")
        else:
            print(md)
        return 0
    
    # LLM 프롬프트 생성
    if args.prompt:
        if not args.template:
            print("❌ --template 옵션 필요")
            return 1
        
        if not Path(args.template).exists():
            print(f"❌ 템플릿 파일 없음: {args.template}")
            return 1
        
        generator = ContextGenerator(args.source, args.template)
        prompt = generator.generate_prompt()
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(prompt)
            print(f"✅ 저장됨: {args.output}")
        else:
            print(prompt)
        return 0
    
    # 기본: 데이터 요약 출력
    extractor = DataExtractor(args.source)
    data = extractor.extract()
    
    print(f"📄 파일: {args.source}")
    print(f"📊 테이블: {len(data.tables)}개")
    print(f"📝 문단: {len(data.paragraphs)}개")
    print(f"🔑 키워드: {len(data.keywords)}개")
    if data.title:
        print(f"📌 제목: {data.title[:50]}...")
    
    return 0


if __name__ == "__main__":
    exit(main())
