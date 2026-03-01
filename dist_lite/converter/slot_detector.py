#!/usr/bin/env python3
"""한국 공문서 양식 자동 슬롯 탐지기.

HWPX 템플릿에서 사용자가 채워야 할 입력란을 자동으로 식별한다.
한국 공문서에서 흔히 쓰이는 패턴:
  - 빈 셀 (라벨 옆의 empty cell)
  - '___' 또는 '          ' (밑줄/공백 = "여기 쓰세요")
  - 'ooo', 'OOO', '000', 'ООО' 등 (= "이름 쓰세요")
  - '년   월   일' (날짜 입력란)
  - '신청기업명 :', '신청자 :', '대표자 :' 등 (= 콜론 뒤에 빈값)
  - '☐' (체크박스)
  - '(인)', '(서명)', '(법인인감)' (= 서명란, 보통 skip)
"""

import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

HP = "http://www.hancom.co.kr/hwpml/2011/paragraph"


def _q(tag: str) -> str:
    return f"{{{HP}}}{tag}"


# ---------------------------------------------------------------------------
# 패턴 정의
# ---------------------------------------------------------------------------

# "여기 쓰세요" 패턴  (밑줄 3개 이상 or 공백 5개 이상)
BLANK_FILL_PATTERN = re.compile(r"[_]{3,}|[ ]{5,}$")

# "이름 쓰세요" 패턴  (ooo, OOO, 000, ○○○ 등)
NAME_PLACEHOLDER = re.compile(r"[oO0○◯ㅇ]{2,}")

# 날짜 입력란
DATE_PATTERN = re.compile(r"(\d{4})?년\s+월\s+일|20\s+\.\s+\.\s+\.\s*자")

# "콜론 뒤 빈값" 패턴 (신청기업명 : , 대표자 : 등)
LABEL_COLON_EMPTY = re.compile(r"(기업명|신청자|대표자|대표이사|성\s*명|연\s*락\s*처)\s*[:：]\s*$")

# 서명란 (skip 대상)
SIGNATURE_PATTERN = re.compile(r"\(인\)|\(서명\)|\(법인\s*서명\)|\(개인\s*서명\)|\(법인인감\)")

# 체크박스
CHECKBOX_PATTERN = re.compile(r"[☐☑]")


# ---------------------------------------------------------------------------
# 슬롯 분류
# ---------------------------------------------------------------------------

SLOT_TYPE_EMPTY_CELL = "empty_cell"        # 라벨 옆 빈 셀
SLOT_TYPE_BLANK_FILL = "blank_fill"        # ___ 또는 공백
SLOT_TYPE_NAME_PLACEHOLDER = "name_placeholder"  # ooo 등
SLOT_TYPE_DATE = "date"                    # 년 월 일
SLOT_TYPE_LABEL_EMPTY = "label_empty"      # 콜론 뒤 빈값
SLOT_TYPE_CHECKBOX = "checkbox"            # ☐
SLOT_TYPE_SIGNATURE = "signature"          # (인) — skip 대상


# ---------------------------------------------------------------------------
# <hp:t> 단위 분석
# ---------------------------------------------------------------------------

def _analyze_t_elements(tc_elem) -> list[dict]:
    """셀 내 개별 <hp:t> 요소를 분석하여 슬롯 후보를 반환."""
    slots = []
    t_elements = list(tc_elem.iter(_q("t")))

    for t_idx, t_elem in enumerate(t_elements):
        text = t_elem.text or ""

        # 서명란 (참고로만)
        if SIGNATURE_PATTERN.search(text):
            slots.append({
                "t_idx": t_idx,
                "type": SLOT_TYPE_SIGNATURE,
                "original_text": text.strip(),
                "description": "서명란 (수정 불필요)",
            })
            continue

        # 날짜
        m = DATE_PATTERN.search(text)
        if m:
            slots.append({
                "t_idx": t_idx,
                "type": SLOT_TYPE_DATE,
                "original_text": text.strip(),
                "description": "날짜 입력란",
            })
            continue

        # 콜론 뒤 빈값
        if LABEL_COLON_EMPTY.search(text.strip()):
            slots.append({
                "t_idx": t_idx,
                "type": SLOT_TYPE_LABEL_EMPTY,
                "original_text": text.strip(),
                "description": "라벨 뒤 빈 값",
            })
            continue

        # 이름 placeholder (ooo 등)
        if NAME_PLACEHOLDER.search(text):
            slots.append({
                "t_idx": t_idx,
                "type": SLOT_TYPE_NAME_PLACEHOLDER,
                "original_text": text.strip(),
                "description": "이름 placeholder (o/O/0 반복)",
            })
            continue

        # 밑줄/공백 채우기
        if BLANK_FILL_PATTERN.search(text):
            slots.append({
                "t_idx": t_idx,
                "type": SLOT_TYPE_BLANK_FILL,
                "original_text": text.strip() or "(공백)",
                "description": "밑줄/공백 입력란",
            })
            continue

    return slots


# ---------------------------------------------------------------------------
# 테이블 단위 탐지
# ---------------------------------------------------------------------------

# 라벨 키워드 (이 단어가 있는 셀 옆은 입력란일 가능성 높음)
LABEL_KEYWORDS = [
    "기업명", "회사명", "상호", "대표자", "대표이사", "설립일자",
    "사업자등록번호", "법인번호", "주소", "전화", "휴대폰", "팩스",
    "부서명", "직위", "성명", "이메일", "이름", "연락처",
    "기업체명", "사업자번호",
]


def detect_slots(section_xml: bytes) -> list[dict]:
    """section XML에서 입력 슬롯 후보를 탐지한다."""
    root = ET.fromstring(section_xml)
    results = []

    for tbl_idx, tbl in enumerate(root.iter(_q("tbl"))):
        rows = tbl.findall(_q("tr"))
        for row_idx, tr in enumerate(rows):
            cells = tr.findall(_q("tc"))

            for cell_idx, tc in enumerate(cells):
                # 1) 개별 <hp:t> 분석
                t_slots = _analyze_t_elements(tc)

                # label_empty 보정: "라벨 :" 셀의 오른쪽 셀이 비어있으면
                # text_replace가 아니라 옆 빈 셀에 cell 로 넣는게 맞음
                corrected_slots = []
                for slot in t_slots:
                    if slot["type"] == SLOT_TYPE_LABEL_EMPTY:
                        # 오른쪽 셀이 비어있는지 확인
                        next_idx = cell_idx + 1
                        if next_idx < len(cells):
                            next_text = ""
                            for t in cells[next_idx].iter(_q("t")):
                                if t.text:
                                    next_text += t.text
                            if not next_text.strip():
                                # 라벨 옆 빈 셀 → empty_cell 로 변환
                                corrected_slots.append({
                                    "table_idx": tbl_idx,
                                    "row_idx": row_idx,
                                    "cell_idx": next_idx,
                                    "type": SLOT_TYPE_EMPTY_CELL,
                                    "original_text": "(empty)",
                                    "description": f"'{slot['original_text'][:20]}' 옆 빈 셀",
                                })
                                continue  # label_empty 는 추가하지 않음
                    # 기본: 원래 슬롯 유지
                    slot["table_idx"] = tbl_idx
                    slot["row_idx"] = row_idx
                    slot["cell_idx"] = cell_idx
                    corrected_slots.append(slot)

                results.extend(corrected_slots)

                # 2) 빈 셀 + 왼쪽 라벨 확인
                all_text = ""
                for t in tc.iter(_q("t")):
                    if t.text:
                        all_text += t.text

                if not all_text.strip():
                    # 왼쪽 셀이 라벨인지 확인
                    label_text = ""
                    if cell_idx > 0:
                        prev_cell = cells[cell_idx - 1]
                        for t in prev_cell.iter(_q("t")):
                            if t.text:
                                label_text += t.text

                    if any(kw in label_text for kw in LABEL_KEYWORDS) or \
                       any(kw in re.sub(r'\s+', '', label_text) for kw in LABEL_KEYWORDS):
                        # 이미 corrected_slots에서 추가됐는지 중복 확인
                        already = any(
                            s["type"] == SLOT_TYPE_EMPTY_CELL
                            and s.get("row_idx") == row_idx
                            and s.get("cell_idx") == cell_idx
                            for s in results
                        )
                        if not already:
                            results.append({
                                "table_idx": tbl_idx,
                                "row_idx": row_idx,
                                "cell_idx": cell_idx,
                                "type": SLOT_TYPE_EMPTY_CELL,
                                "original_text": "(empty)",
                                "description": f"'{label_text.strip()[:20]}' 옆 빈 셀",
                            })

                # 3) 체크박스 탐지
                if CHECKBOX_PATTERN.search(all_text):
                    # 이미 t_slots에서 잡혔을 수도 있음
                    if not any(s["type"] == SLOT_TYPE_CHECKBOX for s in t_slots):
                        results.append({
                            "table_idx": tbl_idx,
                            "row_idx": row_idx,
                            "cell_idx": cell_idx,
                            "type": SLOT_TYPE_CHECKBOX,
                            "original_text": all_text.strip()[:40],
                            "description": "체크박스 항목",
                        })

    return results


# ---------------------------------------------------------------------------
# 비테이블 문단에서의 슬롯 탐지 (날짜, 이름 등)
# ---------------------------------------------------------------------------

def detect_paragraph_slots(section_xml: bytes) -> list[dict]:
    """테이블 밖의 문단에서 입력 슬롯을 탐지한다."""
    root = ET.fromstring(section_xml)
    results = []

    # 트리를 순회하면서 테이블 안의 p는 제외
    table_paras = set()
    for tbl in root.iter(_q("tbl")):
        for p in tbl.iter(_q("p")):
            table_paras.add(id(p))

    para_idx = 0
    for p in root.iter(_q("p")):
        if id(p) in table_paras:
            para_idx += 1
            continue

        for t_idx, t_elem in enumerate(p.iter(_q("t"))):
            text = t_elem.text or ""
            if DATE_PATTERN.search(text):
                results.append({
                    "para_idx": para_idx,
                    "t_idx": t_idx,
                    "type": SLOT_TYPE_DATE,
                    "original_text": text.strip(),
                })
            if NAME_PLACEHOLDER.search(text):
                results.append({
                    "para_idx": para_idx,
                    "t_idx": t_idx,
                    "type": SLOT_TYPE_NAME_PLACEHOLDER,
                    "original_text": text.strip(),
                })
            if BLANK_FILL_PATTERN.search(text):
                results.append({
                    "para_idx": para_idx,
                    "t_idx": t_idx,
                    "type": SLOT_TYPE_BLANK_FILL,
                    "original_text": text.strip() or "(공백)",
                })
            if LABEL_COLON_EMPTY.search(text.strip()):
                results.append({
                    "para_idx": para_idx,
                    "t_idx": t_idx,
                    "type": SLOT_TYPE_LABEL_EMPTY,
                    "original_text": text.strip(),
                })

        para_idx += 1

    return results


# ---------------------------------------------------------------------------
# LLM용 구조화 출력
# ---------------------------------------------------------------------------

# 슬롯 타입 → 추천 주입 타입 매핑
INJECTION_TYPE_MAP = {
    SLOT_TYPE_EMPTY_CELL: "cell",
    SLOT_TYPE_BLANK_FILL: "t_element",
    SLOT_TYPE_NAME_PLACEHOLDER: "text_replace",
    SLOT_TYPE_DATE: "text_replace",
    SLOT_TYPE_LABEL_EMPTY: "text_replace",
    SLOT_TYPE_CHECKBOX: "checkbox",
    SLOT_TYPE_SIGNATURE: None,  # skip
}


def _build_injection_hint(slot: dict) -> dict | None:
    """슬롯에 대한 JSON injection 힌트를 생성한다."""
    slot_type = slot["type"]
    inj_type = INJECTION_TYPE_MAP.get(slot_type)
    if inj_type is None:
        return None  # signature — skip

    hint = {"type": inj_type}

    if "table_idx" in slot:
        hint["table_idx"] = slot["table_idx"]
        hint["row_idx"] = slot["row_idx"]
        hint["cell_idx"] = slot["cell_idx"]
    elif "para_idx" in slot:
        hint["para_idx"] = slot["para_idx"]
        if inj_type in ("t_element", "text_replace"):
            hint["type"] = f"para_{inj_type}"

    # text_replace needs "find" + "replace"
    if inj_type == "text_replace":
        hint["find"] = slot["original_text"]
        hint["replace"] = "{{여기에_값}}"
    elif inj_type == "t_element" and "t_idx" in slot:
        hint["t_idx"] = slot["t_idx"]
        hint["value"] = "{{여기에_값}}"
    elif inj_type == "cell":
        hint["value"] = "{{여기에_값}}"
    elif inj_type == "checkbox":
        hint["checked"] = True

    return hint


def generate_llm_context(hwpx_path: Path, section_file: str = "Contents/section0.xml") -> dict:
    """LLM에게 전달할 구조화된 슬롯 정보를 생성한다."""
    with zipfile.ZipFile(hwpx_path, "r") as zf:
        section_xml = zf.read(section_file)

    table_slots = detect_slots(section_xml)
    para_slots = detect_paragraph_slots(section_xml)

    fillable_slots = []
    for idx, slot in enumerate(table_slots + para_slots):
        if slot["type"] == SLOT_TYPE_SIGNATURE:
            continue
        hint = _build_injection_hint(slot)
        if hint is None:
            continue
        fillable_slots.append({
            "slot_id": idx + 1,
            "location": slot.get("description", ""),
            "slot_type": slot["type"],
            "original_text": slot.get("original_text", ""),
            "injection_template": hint,
        })

    return {
        "template_file": hwpx_path.name,
        "total_slots": len(fillable_slots),
        "slots": fillable_slots,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import json as _json

    if len(sys.argv) < 2:
        print("Usage: slot_detector.py <template.hwpx> [--json] [section_file]")
        return 1

    hwpx_path = Path(sys.argv[1])
    json_mode = "--json" in sys.argv
    section_file = "Contents/section0.xml"
    for arg in sys.argv[2:]:
        if arg != "--json" and not arg.startswith("-"):
            section_file = arg

    if json_mode:
        ctx = generate_llm_context(hwpx_path, section_file)
        print(_json.dumps(ctx, ensure_ascii=False, indent=2))
        return 0

    # --- Human-readable output ---
    with zipfile.ZipFile(hwpx_path, "r") as zf:
        section_xml = zf.read(section_file)

    print(f"📋 Analyzing: {hwpx_path.name}")
    print(f"{'='*60}")

    table_slots = detect_slots(section_xml)
    para_slots = detect_paragraph_slots(section_xml)

    if table_slots:
        print(f"\n📊 Table Slots ({len(table_slots)} found):")
        for s in table_slots:
            icon = "📝" if s["type"] not in (SLOT_TYPE_SIGNATURE, SLOT_TYPE_CHECKBOX) else (
                "✍️" if s["type"] == SLOT_TYPE_SIGNATURE else "☐"
            )
            loc = f"T{s['table_idx']} R{s['row_idx']} C{s['cell_idx']}"
            if "t_idx" in s:
                loc += f" t{s['t_idx']}"
            print(f"  {icon} [{s['type']:18s}] {loc:18s} → {s.get('description', s['original_text'][:40])}")

    if para_slots:
        print(f"\n📄 Paragraph Slots ({len(para_slots)} found):")
        for s in para_slots:
            loc = f"P{s['para_idx']} t{s['t_idx']}"
            print(f"  📝 [{s['type']:18s}] {loc:10s} → {s['original_text'][:50]}")

    total = len(table_slots) + len(para_slots)
    print(f"\n{'='*60}")
    print(f"Total: {total} slots detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

