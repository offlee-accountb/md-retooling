#!/usr/bin/env python3
"""HWPX Template Injector — 기존 HWPX 양식에 데이터를 주입하여 새 파일 생성.

핵심 원칙:
  - header.xml은 절대 건드리지 않는다 (폰트/스타일 보존)
  - section0.xml 내 특정 셀의 <hp:t> 텍스트만 교체
  - 다른 모든 XML 속성, 구조는 그대로 유지
  - 결과물은 원본과 동일한 ZIP 구조로 재패키징

주입 타입:
  - cell: 셀 전체 텍스트 교체
  - t_element: 셀 내 특정 <hp:t> 인덱스의 텍스트 교체
  - text_replace: 셀 내 특정 문자열을 찾아 교체
  - checkbox: ☐/☑ 토글
  - paragraph: 문단 전체 텍스트 교체
"""

import json
import re
import shutil
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from copy import deepcopy

# ---------------------------------------------------------------------------
# HWPX Namespace 정의
# ---------------------------------------------------------------------------
NS = {
    "ha": "http://www.hancom.co.kr/hwpml/2011/app",
    "hp": "http://www.hancom.co.kr/hwpml/2011/paragraph",
    "hs": "http://www.hancom.co.kr/hwpml/2011/section",
    "hh": "http://www.hancom.co.kr/hwpml/2011/head",
    "hc": "http://www.hancom.co.kr/hwpml/2011/core",
}

for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

HP = "http://www.hancom.co.kr/hwpml/2011/paragraph"


def _q(prefix: str, tag: str) -> str:
    return f"{{{NS[prefix]}}}{tag}"


# ---------------------------------------------------------------------------
# 테이블 셀 텍스트 추출 (구조 분석용)
# ---------------------------------------------------------------------------

def extract_table_structure(section_xml: bytes) -> list[dict]:
    """section XML에서 모든 테이블의 셀 내용을 추출한다."""
    root = ET.fromstring(section_xml)
    tables = []

    for tbl_idx, tbl in enumerate(root.iter(_q("hp", "tbl"))):
        table_data = {"index": tbl_idx, "rows": []}
        for row_idx, tr in enumerate(tbl.findall(_q("hp", "tr"))):
            row_cells = []
            for cell_idx, tc in enumerate(tr.findall(_q("hp", "tc"))):
                texts = []
                for t_elem in tc.iter(_q("hp", "t")):
                    if t_elem.text:
                        texts.append(t_elem.text.strip())
                cell_text = " ".join(texts)
                row_cells.append({
                    "cell_idx": cell_idx,
                    "text": cell_text,
                    "is_empty": len(cell_text.strip()) == 0,
                })
            table_data["rows"].append({
                "row_idx": row_idx,
                "cells": row_cells,
            })
        tables.append(table_data)

    return tables


# ---------------------------------------------------------------------------
# 셀 텍스트 교체 (핵심)
# ---------------------------------------------------------------------------

def _find_table(root: ET.Element, table_idx: int) -> ET.Element | None:
    """root 하위의 n번째 <hp:tbl>을 찾는다."""
    for i, tbl in enumerate(root.iter(_q("hp", "tbl"))):
        if i == table_idx:
            return tbl
    return None


def _find_cell(tbl: ET.Element, row_idx: int, cell_idx: int) -> ET.Element | None:
    """표에서 특정 행/열의 <hp:tc>를 찾는다."""
    rows = tbl.findall(_q("hp", "tr"))
    if row_idx >= len(rows):
        return None
    cells = rows[row_idx].findall(_q("hp", "tc"))
    if cell_idx >= len(cells):
        return None
    return cells[cell_idx]


def _set_cell_text(tc: ET.Element, new_text: str) -> None:
    """셀 내 첫 번째 <hp:t>의 텍스트만 교체한다.

    기존 run/charPr 구조는 유지하고, <hp:t>.text만 변경.
    빈 셀의 경우 첫 번째 run의 t를 교체.
    """
    # 모든 <hp:t> 요소 탐색
    t_elements = list(tc.iter(_q("hp", "t")))

    if t_elements:
        # 첫 번째 <hp:t>에 텍스트 설정
        t_elements[0].text = new_text
        # 나머지 <hp:t>는 비움 (기존 텍스트 제거)
        for t_elem in t_elements[1:]:
            t_elem.text = ""
    else:
        # <hp:t>가 없는 경우: 첫 번째 run을 찾아서 t 추가
        for run in tc.iter(_q("hp", "run")):
            t = ET.SubElement(run, _q("hp", "t"))
            t.text = new_text
            break


def _set_t_element_text(tc: ET.Element, t_idx: int, new_text: str) -> bool:
    """셀 내 특정 인덱스의 <hp:t>만 교체한다 (다른 t 요소는 보존)."""
    t_elements = list(tc.iter(_q("hp", "t")))
    if t_idx >= len(t_elements):
        return False
    t_elements[t_idx].text = new_text
    return True


def _text_replace_in_cell(tc: ET.Element, find: str, replace: str) -> int:
    """셀 내 모든 <hp:t>에서 find 문자열을 replace로 교체. 교체 횟수 반환."""
    count = 0
    for t_elem in tc.iter(_q("hp", "t")):
        if t_elem.text and find in t_elem.text:
            t_elem.text = t_elem.text.replace(find, replace)
            count += 1
    return count


def _regex_replace_in_cell(tc: ET.Element, pattern: str, replacement: str) -> int:
    """셀 내 모든 <hp:t>에서 정규식 패턴을 교체. 교체 횟수 반환."""
    count = 0
    compiled = re.compile(pattern)
    for t_elem in tc.iter(_q("hp", "t")):
        if t_elem.text and compiled.search(t_elem.text):
            t_elem.text = compiled.sub(replacement, t_elem.text)
            count += 1
    return count


def _set_paragraph_text(root: ET.Element, para_idx: int, new_text: str) -> bool:
    """root 하위의 n번째 <hp:p>의 텍스트를 교체한다."""
    paragraphs = list(root.iter(_q("hp", "p")))
    if para_idx >= len(paragraphs):
        return False
    p = paragraphs[para_idx]
    t_elements = list(p.iter(_q("hp", "t")))
    if t_elements:
        t_elements[0].text = new_text
        for t_elem in t_elements[1:]:
            t_elem.text = ""
        return True
    return False


def _set_paragraph_t_element(root: ET.Element, para_idx: int, t_idx: int, new_text: str) -> bool:
    """root 하위 n번째 <hp:p>의 특정 <hp:t>를 교체한다."""
    paragraphs = list(root.iter(_q("hp", "p")))
    if para_idx >= len(paragraphs):
        return False
    p = paragraphs[para_idx]
    t_elements = list(p.iter(_q("hp", "t")))
    if t_idx >= len(t_elements):
        return False
    t_elements[t_idx].text = new_text
    return True


def _text_replace_in_paragraph(root: ET.Element, para_idx: int, find: str, replace: str) -> int:
    """문단 내 모든 <hp:t>에서 find를 replace로 교체."""
    paragraphs = list(root.iter(_q("hp", "p")))
    if para_idx >= len(paragraphs):
        return 0
    count = 0
    for t_elem in paragraphs[para_idx].iter(_q("hp", "t")):
        if t_elem.text and find in t_elem.text:
            t_elem.text = t_elem.text.replace(find, replace)
            count += 1
    return count


# ---------------------------------------------------------------------------
# 체크박스 토글
# ---------------------------------------------------------------------------

def _toggle_checkbox(tc: ET.Element, check: bool) -> None:
    """셀 내의 ☐/☑ 체크박스를 토글한다."""
    for t_elem in tc.iter(_q("hp", "t")):
        if t_elem.text:
            if check:
                t_elem.text = t_elem.text.replace("☐", "☑")
            else:
                t_elem.text = t_elem.text.replace("☑", "☐")


# ---------------------------------------------------------------------------
# 메인 주입 함수
# ---------------------------------------------------------------------------

def inject_into_hwpx(
    template_path: Path,
    output_path: Path,
    injections: list[dict],
    section_file: str = "Contents/section0.xml",
) -> Path:
    """HWPX 템플릿에 데이터를 주입하여 새 파일을 생성한다.

    Args:
        template_path: 원본 HWPX 파일 경로
        output_path: 출력 HWPX 파일 경로
        injections: 주입할 데이터 리스트. 각 항목:
            {
                "type": "cell",          # cell | paragraph | checkbox
                "table_idx": 1,          # 테이블 인덱스
                "row_idx": 0,            # 행 인덱스
                "cell_idx": 1,           # 열 인덱스
                "value": "텍스트데이터"   # 주입할 값
            }
        section_file: 수정할 section XML 파일명

    Returns:
        출력 파일 경로
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        # 1) 원본 ZIP 해제
        with zipfile.ZipFile(template_path, "r") as zf:
            zf.extractall(tmpdir)

        # 2) section XML 파싱
        section_path = tmpdir / section_file
        tree = ET.parse(section_path)
        root = tree.getroot()

        # 3) 주입 실행
        applied = 0
        errors = []
        for inj in injections:
            try:
                inj_type = inj.get("type", "cell")

                if inj_type == "cell":
                    tbl = _find_table(root, inj["table_idx"])
                    if tbl is None:
                        errors.append(f"Table {inj['table_idx']} not found")
                        continue
                    tc = _find_cell(tbl, inj["row_idx"], inj["cell_idx"])
                    if tc is None:
                        errors.append(f"Cell ({inj['row_idx']},{inj['cell_idx']}) in table {inj['table_idx']} not found")
                        continue
                    _set_cell_text(tc, inj["value"])
                    applied += 1

                elif inj_type == "t_element":
                    tbl = _find_table(root, inj["table_idx"])
                    if tbl is None:
                        errors.append(f"Table {inj['table_idx']} not found")
                        continue
                    tc = _find_cell(tbl, inj["row_idx"], inj["cell_idx"])
                    if tc is None:
                        errors.append(f"Cell ({inj['row_idx']},{inj['cell_idx']}) in table {inj['table_idx']} not found")
                        continue
                    ok = _set_t_element_text(tc, inj["t_idx"], inj["value"])
                    if ok:
                        applied += 1
                    else:
                        errors.append(f"t_element index {inj['t_idx']} not found in cell")

                elif inj_type == "text_replace":
                    if "table_idx" in inj:
                        tbl = _find_table(root, inj["table_idx"])
                        if tbl is None:
                            errors.append(f"Table {inj['table_idx']} not found")
                            continue
                        tc = _find_cell(tbl, inj["row_idx"], inj["cell_idx"])
                        if tc is None:
                            errors.append(f"Cell not found")
                            continue
                        cnt = _text_replace_in_cell(tc, inj["find"], inj["replace"])
                    elif "para_idx" in inj:
                        cnt = _text_replace_in_paragraph(root, inj["para_idx"], inj["find"], inj["replace"])
                    else:
                        errors.append("text_replace needs table_idx or para_idx")
                        continue
                    if cnt > 0:
                        applied += 1
                    else:
                        errors.append(f"text_replace: '{inj['find']}' not found")

                elif inj_type == "checkbox":
                    tbl = _find_table(root, inj["table_idx"])
                    if tbl is None:
                        errors.append(f"Table {inj['table_idx']} not found")
                        continue
                    tc = _find_cell(tbl, inj["row_idx"], inj["cell_idx"])
                    if tc is None:
                        errors.append(f"Cell ({inj['row_idx']},{inj['cell_idx']}) in table {inj['table_idx']} not found")
                        continue
                    _toggle_checkbox(tc, inj.get("checked", True))
                    applied += 1

                elif inj_type == "paragraph":
                    ok = _set_paragraph_text(root, inj["para_idx"], inj["value"])
                    if ok:
                        applied += 1
                    else:
                        errors.append(f"Paragraph {inj['para_idx']} not found")

                elif inj_type == "para_t_element":
                    ok = _set_paragraph_t_element(root, inj["para_idx"], inj["t_idx"], inj["value"])
                    if ok:
                        applied += 1
                    else:
                        errors.append(f"Para {inj['para_idx']} t{inj['t_idx']} not found")

                elif inj_type == "para_text_replace":
                    cnt = _text_replace_in_paragraph(root, inj["para_idx"], inj["find"], inj["replace"])
                    if cnt > 0:
                        applied += 1
                    else:
                        errors.append(f"para_text_replace: '{inj['find']}' not found")

            except Exception as e:
                errors.append(f"Error applying injection {inj}: {e}")

        # 4) 수정된 XML 저장
        tree.write(section_path, encoding="utf-8", xml_declaration=True)

        # 5) ZIP 재패키징 (원본 구조 유지)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for fpath in sorted(tmpdir.rglob("*")):
                if fpath.is_file():
                    arcname = str(fpath.relative_to(tmpdir))
                    # mimetype은 STORED로 (HWPX 규격)
                    if arcname == "mimetype":
                        zout.write(fpath, arcname, compress_type=zipfile.ZIP_STORED)
                    else:
                        zout.write(fpath, arcname)

        print(f"[ok] Injected {applied}/{len(injections)} fields → {output_path}")
        if errors:
            for e in errors:
                print(f"  [warn] {e}", file=sys.stderr)

    return output_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    """Usage: template_injector.py <template.hwpx> <data.json> <output.hwpx>

    data.json format:
    {
        "injections": [
            {"type": "cell", "table_idx": 1, "row_idx": 0, "cell_idx": 1, "value": "주식회사 테스트"},
            {"type": "checkbox", "table_idx": 2, "row_idx": 0, "cell_idx": 1, "checked": true},
            ...
        ]
    }
    """
    if len(sys.argv) < 4:
        print(__doc__)
        print(main.__doc__)
        return 1

    template = Path(sys.argv[1])
    data_file = Path(sys.argv[2])
    output = Path(sys.argv[3])

    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    inject_into_hwpx(template, output, data["injections"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
