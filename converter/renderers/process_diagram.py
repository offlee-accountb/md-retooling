"""프로세스 흐름도 + 도식도 렌더러.

_append_process_table, _append_diagram_table
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from typing import List

from converter.models import BlockType, Block, DiagramBox, DiagramBlock
from converter.config import (
    _attach_secpr,
    _q, mm_to_hwp, CONFIG,
    TABLE_WIDTH_HWP,
    TABLE_TITLE_PARA_ID, TABLE_HEADER_PARA_ID,
    TABLE_TITLE_STYLE_ID, TABLE_HEADER_STYLE_ID,
    TABLE_BODY_CHAR_ID, TABLE_HEADER_CHAR_ID,
    PROCESS_STEP_BORDER_ID, PROCESS_ARROW_BORDER_ID,
    PROCESS_TITLE_BORDER_ID, PROCESS_DESC_BORDER_ID,
)
from converter.renderers.inline import (
    _append_text_with_bold, _append_text_with_bold_custom,
)
from converter.renderers.text_fitting import (
    TABLE_FIT_CHAR_IDS, TABLE_FIT_BOLD_CHAR_IDS,
    _estimate_line_count,
)

def _append_process_table(
    parent: ET.Element, block, *, table_id: int, p_id: int, secpr_attached: bool
) -> tuple[int, int, bool]:
    """프로세스 흐름도를 표로 렌더링한다. (038 스타일: 2행 블록)

    각 단계 = 상단 제목행 (번호+단계명, 배경색) + 하단 설명행 (담당자, 흰 배경)
    화살표 셀 = rowSpan=2로 상하 병합
    block.proc_rows: [(steps, is_reversed), ...]
    steps = [(name, desc), ...]
    """
    if not block.proc_rows:
        return p_id, table_id, secpr_attached

    # 제목 표기
    p_title = ET.SubElement(
        parent,
        _q("hp", "p"),
        {
            "id": str(p_id),
            "paraPrIDRef": TABLE_TITLE_PARA_ID,
            "styleIDRef": TABLE_TITLE_STYLE_ID,
            "pageBreak": "0",
            "columnBreak": "0",
            "merged": "0",
        },
    )
    if not secpr_attached:
        run_sec = ET.SubElement(p_title, _q("hp", "run"), {"charPrIDRef": TABLE_HEADER_CHAR_ID})
        _attach_secpr(run_sec)
        secpr_attached = True
    title_run = ET.SubElement(p_title, _q("hp", "run"), {"charPrIDRef": TABLE_HEADER_CHAR_ID})
    title_t = ET.SubElement(title_run, _q("hp", "t"))
    title_t.text = f"< {block.proc_title} >"
    p_id += 1

    # 최대 단계 수 (열 수 계산: 단계 셀 + 화살표 셀)
    max_steps = max(len(steps) for steps, _ in block.proc_rows)
    col_cnt = max_steps * 2 - 1  # 단계1, →, 단계2, →, 단계3 ...
    if col_cnt < 1:
        col_cnt = 1

    # 행 수 계산: 각 proc_row마다 2행(제목+설명), 행 사이에 화살표행 1개
    data_rows = len(block.proc_rows) * 2  # 제목행 + 설명행 per proc_row
    arrow_rows = len(block.proc_rows) - 1  # 행간 ↓ 화살표행
    row_count = data_rows + arrow_rows

    total_width = int(TABLE_WIDTH_HWP)
    arrow_col_width = 1800  # 화살표 열 너비
    n_arrow_cols = max_steps - 1
    remaining = total_width - (n_arrow_cols * arrow_col_width)
    step_col_width = remaining // max_steps if max_steps > 0 else total_width
    # 열별 너비 배열: [단계, 화살표, 단계, ...]
    step_widths = []
    for i in range(col_cnt):
        if i % 2 == 0:
            step_widths.append(step_col_width)
        else:
            step_widths.append(arrow_col_width)
    used = sum(step_widths)
    if used != total_width and step_widths:
        step_widths[-1] += (total_width - used)

    title_row_height = 1600   # 상단 제목 행 높이
    desc_row_height = 1800    # 하단 설명 행 높이
    arrow_row_height = 1200   # ↓ 화살표 행 높이

    total_h = data_rows // 2 * (title_row_height + desc_row_height) + arrow_rows * arrow_row_height

    # 표 wrapper
    p_wrapper = ET.SubElement(
        parent,
        _q("hp", "p"),
        {
            "id": str(p_id),
            "paraPrIDRef": "0",
            "styleIDRef": "0",
            "pageBreak": "0",
            "columnBreak": "0",
            "merged": "0",
        },
    )
    p_id += 1

    run_tbl = ET.SubElement(p_wrapper, _q("hp", "run"))
    tbl = ET.SubElement(
        run_tbl,
        _q("hp", "tbl"),
        {
            "id": str(table_id),
            "zOrder": str(table_id),
            "numberingType": "TABLE",
            "textWrap": "TOP_AND_BOTTOM",
            "textFlow": "BOTH_SIDES",
            "lock": "0",
            "dropcapstyle": "None",
            "pageBreak": "CELL",
            "repeatHeader": "0",
            "rowCnt": str(row_count),
            "colCnt": str(col_cnt),
            "cellSpacing": "0",
            "borderFillIDRef": "1",
            "noAdjust": "0",
        },
    )

    ET.SubElement(tbl, _q("hp", "sz"),
        {"width": TABLE_WIDTH_HWP, "widthRelTo": "ABSOLUTE",
         "height": str(total_h), "heightRelTo": "ABSOLUTE", "protect": "0"})
    ET.SubElement(
        tbl,
        _q("hp", "pos"),
        {
            "treatAsChar": "0",
            "affectLSpacing": "0",
            "flowWithText": "1",
            "allowOverlap": "0",
            "holdAnchorAndSO": "0",
            "vertRelTo": "PARA",
            "horzRelTo": "COLUMN",
            "vertAlign": "TOP",
            "horzAlign": "LEFT",
            "vertOffset": "0",
            "horzOffset": "0",
        },
    )
    ET.SubElement(tbl, _q("hp", "outMargin"), {"left": "283", "right": "283", "top": "283", "bottom": "283"})
    ET.SubElement(tbl, _q("hp", "inMargin"), {"left": "283", "right": "283", "top": "141", "bottom": "141"})

    p_counter = p_id

    CIRCLED_NUMS = ["①","②","③","④","⑤","⑥","⑦","⑧","⑨","⑩","⑪","⑫","⑬","⑭","⑮","⑯","⑰","⑱","⑲","⑳"]

    def _get_circled(n: int) -> str:
        if 1 <= n <= len(CIRCLED_NUMS):
            return CIRCLED_NUMS[n - 1]
        return f"({n})"

    step_number = 1

    def _make_cell(tr_el, col_idx, row_idx_val, width, height, *,
                   text="", border_id="1", char_id=TABLE_BODY_CHAR_ID,
                   row_span=1, auto_fit=False, is_bold=False):
        """범용 셀 생성 헬퍼. auto_fit=True이면 자간/폰트 자동조정."""
        nonlocal p_counter

        # 텍스트 피팅: 셀 너비에 맞게 자간 축소 (프로세스 전용: 11pt, -15%까지)
        PROC_FIT_CANDIDATES = [(11, 0), (11, -5), (11, -10), (11, -15)]
        actual_char_id = char_id
        if auto_fit and text:
            best = (11, 0)
            best_lines = _estimate_line_count(text, width, 11, 0)
            if best_lines > 1:
                for font_pt, spacing in PROC_FIT_CANDIDATES[1:]:
                    lines = _estimate_line_count(text, width, font_pt, spacing)
                    if lines < best_lines:
                        best_lines = lines
                        best = (font_pt, spacing)
                    if best_lines <= 1:
                        break
            if best != (11, 0):
                ids = TABLE_FIT_BOLD_CHAR_IDS if is_bold else TABLE_FIT_CHAR_IDS
                fit_id = ids.get(best)
                if fit_id:
                    actual_char_id = fit_id

        tc = ET.SubElement(tr_el, _q("hp", "tc"),
            {"name": "", "header": "0", "hasMargin": "0", "protect": "0",
             "editable": "0", "dirty": "0", "borderFillIDRef": border_id})
        sub_list = ET.SubElement(tc, _q("hp", "subList"),
            {"id": "", "textDirection": "HORIZONTAL", "lineWrap": "BREAK",
             "vertAlign": "CENTER", "linkListIDRef": "0", "linkListNextIDRef": "0",
             "textWidth": "0", "textHeight": "0", "hasTextRef": "0", "hasNumRef": "0"})
        p_el = ET.SubElement(sub_list, _q("hp", "p"),
            {"id": str(p_counter), "paraPrIDRef": TABLE_HEADER_PARA_ID,
             "styleIDRef": TABLE_HEADER_STYLE_ID, "pageBreak": "0",
             "columnBreak": "0", "merged": "0"})
        if text:
            run_el = ET.SubElement(p_el, _q("hp", "run"), {"charPrIDRef": actual_char_id})
            t_el = ET.SubElement(run_el, _q("hp", "t"))
            t_el.text = text
        p_counter += 1
        ET.SubElement(tc, _q("hp", "cellAddr"), {"colAddr": str(col_idx), "rowAddr": str(row_idx_val)})
        ET.SubElement(tc, _q("hp", "cellSpan"), {"colSpan": "1", "rowSpan": str(row_span)})
        ET.SubElement(tc, _q("hp", "cellSz"), {"width": str(width), "height": str(height)})
        is_arrow = (border_id == PROCESS_ARROW_BORDER_ID)
        margin_lr = "28" if is_arrow else "170"
        ET.SubElement(tc, _q("hp", "cellMargin"),
            {"left": margin_lr, "right": margin_lr, "top": "56", "bottom": "56"})

    actual_row = 0
    for proc_idx, (steps, is_reversed) in enumerate(block.proc_rows):
        display_steps = list(steps)
        if is_reversed:
            display_steps = list(reversed(display_steps))

        # === 제목 행 (상단, 배경색) ===
        tr_title = ET.SubElement(tbl, _q("hp", "tr"))
        cell_idx = 0
        for si, (name, desc) in enumerate(display_steps):
            title_text = f"{_get_circled(step_number)} {name}"
            _make_cell(tr_title, cell_idx, actual_row,
                       step_widths[cell_idx] if cell_idx < len(step_widths) else step_widths[-1],
                       title_row_height,
                       text=title_text,
                       border_id=PROCESS_TITLE_BORDER_ID,
                       char_id=TABLE_HEADER_CHAR_ID,
                       auto_fit=True, is_bold=True)
            step_number += 1
            cell_idx += 1
            # 화살표 셀 (rowSpan=2)
            if si < len(display_steps) - 1 and cell_idx < col_cnt:
                arrow_char = "←" if is_reversed else "→"
                _make_cell(tr_title, cell_idx, actual_row,
                           step_widths[cell_idx] if cell_idx < len(step_widths) else step_widths[-1],
                           title_row_height + desc_row_height,
                           text=arrow_char,
                           border_id=PROCESS_ARROW_BORDER_ID,
                           char_id=TABLE_BODY_CHAR_ID,
                           row_span=2)
                cell_idx += 1
        # 남은 열 채우기
        while cell_idx < col_cnt:
            _make_cell(tr_title, cell_idx, actual_row,
                       step_widths[cell_idx] if cell_idx < len(step_widths) else step_widths[-1],
                       title_row_height,
                       border_id=PROCESS_ARROW_BORDER_ID)
            cell_idx += 1
        actual_row += 1

        # === 설명 행 (하단, 흰 배경) ===
        tr_desc = ET.SubElement(tbl, _q("hp", "tr"))
        cell_idx = 0
        si_counter = 0
        for si, (name, desc) in enumerate(display_steps):
            _make_cell(tr_desc, cell_idx, actual_row,
                       step_widths[cell_idx] if cell_idx < len(step_widths) else step_widths[-1],
                       desc_row_height,
                       text=desc,
                       border_id=PROCESS_DESC_BORDER_ID,
                       char_id=TABLE_BODY_CHAR_ID,
                       auto_fit=True, is_bold=False)
            cell_idx += 1
            # 화살표 셀은 rowSpan으로 이미 병합됨 → 건너뜀
            if si < len(display_steps) - 1 and cell_idx < col_cnt:
                cell_idx += 1  # skip merged arrow cell
        while cell_idx < col_cnt:
            _make_cell(tr_desc, cell_idx, actual_row,
                       step_widths[cell_idx] if cell_idx < len(step_widths) else step_widths[-1],
                       desc_row_height,
                       border_id=PROCESS_ARROW_BORDER_ID)
            cell_idx += 1
        actual_row += 1

        # === ↓ 화살표 행 (행 사이) ===
        if proc_idx < len(block.proc_rows) - 1:
            tr_arrow = ET.SubElement(tbl, _q("hp", "tr"))
            if is_reversed:
                down_col = 0
            else:
                down_col = (len(display_steps) - 1) * 2
            for ci in range(col_cnt):
                arrow_txt = "↓" if ci == down_col else ""
                _make_cell(tr_arrow, ci, actual_row,
                           step_widths[ci] if ci < len(step_widths) else step_widths[-1],
                           arrow_row_height,
                           text=arrow_txt,
                           border_id=PROCESS_ARROW_BORDER_ID)
            actual_row += 1

    p_id = p_counter
    return p_id, table_id + 1, secpr_attached


def _append_diagram_table(
    parent: ET.Element, block, *, table_id: int, p_id: int, secpr_attached: bool
) -> tuple[int, int, bool]:
    """도식도를 레이어 스택 모델로 렌더링한다.

    각 레이어 = 테이블 행 (박스 셀들)
    레이어 사이 = 화살표 행 (↓ 또는 ↔)
    """
    if not block.layers:
        return p_id, table_id, secpr_attached

    # ↔ 커넥터 전처리: 인접 레이어를 합쳐서 좌우 병렬 배치
    merged_layers = []
    merged_connectors = []
    lr_split_at = {}  # layer_idx → 왼쪽 그룹 박스 수 (↔ 분리 지점)
    i = 0
    while i < len(block.layers):
        # 현재 레이어 뒤에 ↔ 커넥터가 있으면 다음 레이어와 합침
        if (i < len(block.connectors) and block.connectors[i] == "↔"
                and i + 1 < len(block.layers)):
            left_n = len(block.layers[i])
            combined = list(block.layers[i]) + list(block.layers[i + 1])
            lr_split_at[len(merged_layers)] = left_n
            merged_layers.append(combined)
            # ↔ 다음의 커넥터가 있으면 그것을 사용
            if i + 1 < len(block.connectors):
                merged_connectors.append(block.connectors[i + 1])
            i += 2
        else:
            merged_layers.append(list(block.layers[i]))
            if i < len(block.connectors):
                merged_connectors.append(block.connectors[i])
            i += 1
    # 커넥터 길이 보정 (layers - 1)
    while len(merged_connectors) >= len(merged_layers):
        merged_connectors.pop()

    # 이후 merged_layers, merged_connectors를 사용
    layers = merged_layers
    connectors = merged_connectors

    # 제목 표기
    p_title = ET.SubElement(
        parent,
        _q("hp", "p"),
        {
            "id": str(p_id),
            "paraPrIDRef": TABLE_TITLE_PARA_ID,
            "styleIDRef": TABLE_TITLE_STYLE_ID,
            "pageBreak": "0",
            "columnBreak": "0",
            "merged": "0",
        },
    )
    if not secpr_attached:
        run_sec = ET.SubElement(p_title, _q("hp", "run"), {"charPrIDRef": TABLE_HEADER_CHAR_ID})
        _attach_secpr(run_sec)
        secpr_attached = True
    title_run = ET.SubElement(p_title, _q("hp", "run"), {"charPrIDRef": TABLE_HEADER_CHAR_ID})
    title_t = ET.SubElement(title_run, _q("hp", "t"))
    title_t.text = f"< {block.diagram_title} >"
    p_id += 1

    # 최대 열 수 결정 (가장 많은 박스를 가진 레이어 기준)
    max_boxes = max(len(layer) for layer in layers)
    # 열 구성: [박스1, 여백, 박스2, 여백, ..., 박스N]
    # 여백 열은 박스 사이 간격 (화살표 없음)
    col_cnt = max_boxes * 2 - 1 if max_boxes > 1 else 1

    total_width = int(TABLE_WIDTH_HWP)
    # ↔ 좌우비교형이 있으면 간격 열을 넓게 잡음
    has_lr = bool(lr_split_at)
    gap_col_width = 3000 if has_lr else 800  # ↔: ~10.6mm, ↓: ~2.7mm
    n_gap_cols = max_boxes - 1 if max_boxes > 1 else 0
    remaining = total_width - (n_gap_cols * gap_col_width)
    box_col_width = remaining // max_boxes if max_boxes > 0 else total_width

    col_widths = []
    for c in range(col_cnt):
        if c % 2 == 0:
            col_widths.append(box_col_width)
        else:
            col_widths.append(gap_col_width)
    # 보정
    used = sum(col_widths)
    if used != total_width and col_widths:
        col_widths[-1] += (total_width - used)

    # 행 수 계산
    row_count = len(layers) * 2 - 1  # 레이어행 + 화살표행
    box_row_height = 3200   # 박스 행 높이
    arrow_row_height = 1200  # 화살표 행 높이

    total_h = 0
    for ri in range(row_count):
        total_h += box_row_height if ri % 2 == 0 else arrow_row_height

    # 표 wrapper
    p_wrapper = ET.SubElement(
        parent,
        _q("hp", "p"),
        {
            "id": str(p_id),
            "paraPrIDRef": "0",
            "styleIDRef": "0",
            "pageBreak": "0",
            "columnBreak": "0",
            "merged": "0",
        },
    )
    p_id += 1

    run_tbl = ET.SubElement(p_wrapper, _q("hp", "run"))
    tbl = ET.SubElement(
        run_tbl,
        _q("hp", "tbl"),
        {
            "id": str(table_id),
            "zOrder": str(table_id),
            "numberingType": "TABLE",
            "textWrap": "TOP_AND_BOTTOM",
            "textFlow": "BOTH_SIDES",
            "lock": "0",
            "dropcapstyle": "None",
            "pageBreak": "CELL",
            "repeatHeader": "0",
            "rowCnt": str(row_count),
            "colCnt": str(col_cnt),
            "cellSpacing": "0",
            "borderFillIDRef": "1",
            "noAdjust": "0",
        },
    )

    ET.SubElement(tbl, _q("hp", "sz"),
        {"width": TABLE_WIDTH_HWP, "widthRelTo": "ABSOLUTE",
         "height": str(total_h), "heightRelTo": "ABSOLUTE", "protect": "0"})
    ET.SubElement(
        tbl,
        _q("hp", "pos"),
        {
            "treatAsChar": "0",
            "affectLSpacing": "0",
            "flowWithText": "1",
            "allowOverlap": "0",
            "holdAnchorAndSO": "0",
            "vertRelTo": "PARA",
            "horzRelTo": "COLUMN",
            "vertAlign": "TOP",
            "horzAlign": "LEFT",
            "vertOffset": "0",
            "horzOffset": "0",
        },
    )
    ET.SubElement(tbl, _q("hp", "outMargin"), {"left": "283", "right": "283", "top": "283", "bottom": "283"})
    ET.SubElement(tbl, _q("hp", "inMargin"), {"left": "283", "right": "283", "top": "141", "bottom": "141"})

    p_counter = p_id

    def _add_diagram_cell(tr_el, col_idx, row_idx_val, width, height, *,
                          box=None, arrow_text=""):
        """도식도 셀 하나를 추가한다."""
        nonlocal p_counter
        is_box = box is not None
        border_ref = PROCESS_STEP_BORDER_ID if is_box else PROCESS_ARROW_BORDER_ID
        tc = ET.SubElement(tr_el, _q("hp", "tc"),
            {"name": "", "header": "0", "hasMargin": "0", "protect": "0",
             "editable": "0", "dirty": "0", "borderFillIDRef": border_ref})
        sub_list = ET.SubElement(tc, _q("hp", "subList"),
            {"id": "", "textDirection": "HORIZONTAL", "lineWrap": "BREAK",
             "vertAlign": "CENTER", "linkListIDRef": "0", "linkListNextIDRef": "0",
             "textWidth": "0", "textHeight": "0", "hasTextRef": "0", "hasNumRef": "0"})

        if is_box:
            # 제목 줄 (Bold)
            p1 = ET.SubElement(sub_list, _q("hp", "p"),
                {"id": str(p_counter), "paraPrIDRef": TABLE_HEADER_PARA_ID,
                 "styleIDRef": TABLE_HEADER_STYLE_ID, "pageBreak": "0",
                 "columnBreak": "0", "merged": "0"})
            run1 = ET.SubElement(p1, _q("hp", "run"), {"charPrIDRef": TABLE_HEADER_CHAR_ID})
            t1 = ET.SubElement(run1, _q("hp", "t"))
            t1.text = box.title
            p_counter += 1

            # 내용 항목들 (일반체)
            for item in box.items:
                p_item = ET.SubElement(sub_list, _q("hp", "p"),
                    {"id": str(p_counter), "paraPrIDRef": TABLE_HEADER_PARA_ID,
                     "styleIDRef": TABLE_HEADER_STYLE_ID, "pageBreak": "0",
                     "columnBreak": "0", "merged": "0"})
                run_item = ET.SubElement(p_item, _q("hp", "run"), {"charPrIDRef": TABLE_BODY_CHAR_ID})
                t_item = ET.SubElement(run_item, _q("hp", "t"))
                t_item.text = item
                p_counter += 1
        else:
            # 화살표 또는 빈 셀
            p_a = ET.SubElement(sub_list, _q("hp", "p"),
                {"id": str(p_counter), "paraPrIDRef": TABLE_HEADER_PARA_ID,
                 "styleIDRef": TABLE_HEADER_STYLE_ID, "pageBreak": "0",
                 "columnBreak": "0", "merged": "0"})
            if arrow_text:
                run_a = ET.SubElement(p_a, _q("hp", "run"), {"charPrIDRef": TABLE_BODY_CHAR_ID})
                t_a = ET.SubElement(run_a, _q("hp", "t"))
                t_a.text = arrow_text
            p_counter += 1

        ET.SubElement(tc, _q("hp", "cellAddr"), {"colAddr": str(col_idx), "rowAddr": str(row_idx_val)})

        # colspan 계산: 단일 박스 레이어는 전체 병합
        ET.SubElement(tc, _q("hp", "cellSpan"), {"colSpan": "1", "rowSpan": "1"})
        ET.SubElement(tc, _q("hp", "cellSz"), {"width": str(width), "height": str(height)})
        if is_box:
            ET.SubElement(tc, _q("hp", "cellMargin"),
                {"left": "170", "right": "170", "top": "113", "bottom": "113"})
        else:
            ET.SubElement(tc, _q("hp", "cellMargin"),
                {"left": "28", "right": "28", "top": "113", "bottom": "113"})

    actual_row = 0
    for layer_idx, layer in enumerate(layers):
        tr = ET.SubElement(tbl, _q("hp", "tr"))
        n_boxes = len(layer)

        if n_boxes == 1 and col_cnt > 1:
            # 단일 박스 → 전체 열을 합쳐서 1개 셀로 (colspan)
            box = layer[0]
            border_ref = PROCESS_STEP_BORDER_ID
            tc = ET.SubElement(tr, _q("hp", "tc"),
                {"name": "", "header": "0", "hasMargin": "0", "protect": "0",
                 "editable": "0", "dirty": "0", "borderFillIDRef": border_ref})
            sub_list = ET.SubElement(tc, _q("hp", "subList"),
                {"id": "", "textDirection": "HORIZONTAL", "lineWrap": "BREAK",
                 "vertAlign": "CENTER", "linkListIDRef": "0", "linkListNextIDRef": "0",
                 "textWidth": "0", "textHeight": "0", "hasTextRef": "0", "hasNumRef": "0"})
            p1 = ET.SubElement(sub_list, _q("hp", "p"),
                {"id": str(p_counter), "paraPrIDRef": TABLE_HEADER_PARA_ID,
                 "styleIDRef": TABLE_HEADER_STYLE_ID, "pageBreak": "0",
                 "columnBreak": "0", "merged": "0"})
            run1 = ET.SubElement(p1, _q("hp", "run"), {"charPrIDRef": TABLE_HEADER_CHAR_ID})
            t1 = ET.SubElement(run1, _q("hp", "t"))
            t1.text = box.title
            p_counter += 1
            for item in box.items:
                pi = ET.SubElement(sub_list, _q("hp", "p"),
                    {"id": str(p_counter), "paraPrIDRef": TABLE_HEADER_PARA_ID,
                     "styleIDRef": TABLE_HEADER_STYLE_ID, "pageBreak": "0",
                     "columnBreak": "0", "merged": "0"})
                ri = ET.SubElement(pi, _q("hp", "run"), {"charPrIDRef": TABLE_BODY_CHAR_ID})
                ti = ET.SubElement(ri, _q("hp", "t"))
                ti.text = item
                p_counter += 1

            ET.SubElement(tc, _q("hp", "cellAddr"), {"colAddr": "0", "rowAddr": str(actual_row)})
            ET.SubElement(tc, _q("hp", "cellSpan"), {"colSpan": str(col_cnt), "rowSpan": "1"})
            ET.SubElement(tc, _q("hp", "cellSz"), {"width": str(total_width), "height": str(box_row_height)})
            ET.SubElement(tc, _q("hp", "cellMargin"),
                {"left": "170", "right": "170", "top": "113", "bottom": "113"})
        else:
            # 다중 박스 레이어
            # ↔ 분리 지점 확인 (왼쪽 그룹의 마지막 박스 인덱스)
            split_box_idx = lr_split_at.get(layer_idx)
            cell_idx = 0
            for bi, box in enumerate(layer):
                _add_diagram_cell(tr, cell_idx, actual_row,
                                  col_widths[cell_idx] if cell_idx < len(col_widths) else col_widths[-1],
                                  box_row_height,
                                  box=box)
                cell_idx += 1
                # 간격 셀
                if bi < n_boxes - 1 and cell_idx < col_cnt:
                    # ↔ 분리 지점이면 화살표 표시
                    gap_arrow = "↔" if (split_box_idx is not None and bi == split_box_idx - 1) else ""
                    _add_diagram_cell(tr, cell_idx, actual_row,
                                      col_widths[cell_idx] if cell_idx < len(col_widths) else col_widths[-1],
                                      box_row_height,
                                      arrow_text=gap_arrow)
                    cell_idx += 1
            # 남은 열 채우기
            while cell_idx < col_cnt:
                _add_diagram_cell(tr, cell_idx, actual_row,
                                  col_widths[cell_idx] if cell_idx < len(col_widths) else col_widths[-1],
                                  box_row_height)
                cell_idx += 1

        actual_row += 1

        # 화살표 행 (레이어 사이)
        if layer_idx < len(layers) - 1:
            tr_arrow = ET.SubElement(tbl, _q("hp", "tr"))
            connector = connectors[layer_idx] if layer_idx < len(connectors) else "↓"

            if connector == "↔":
                # 좌우 비교: 가운데에 ↔ 표시
                mid = col_cnt // 2
                for ci in range(col_cnt):
                    arrow_txt = "↔" if ci == mid else ""
                    _add_diagram_cell(tr_arrow, ci, actual_row,
                                      col_widths[ci] if ci < len(col_widths) else col_widths[-1],
                                      arrow_row_height,
                                      arrow_text=arrow_txt)
            else:
                # ↓ 분기/수렴: 각 박스 위치에 ↓ 배치
                # 위 레이어 N개 → 아래 M개: 양쪽에 모두 ↓
                next_layer = layers[layer_idx + 1]
                cur_n = len(layer)
                next_n = len(next_layer)
                # 화살표 위치 결정
                if cur_n == 1 and next_n > 1:
                    # 분기: 각 박스 위치에 ↓
                    arrow_cols = set()
                    for bi in range(next_n):
                        arrow_cols.add(bi * 2)  # 짝수 열 = 박스 위치
                elif cur_n > 1 and next_n == 1:
                    # 수렴: 각 박스 위치에 ↓
                    arrow_cols = set()
                    for bi in range(cur_n):
                        arrow_cols.add(bi * 2)
                else:
                    # 1:1 또는 N:N
                    arrow_cols = set()
                    for bi in range(max(cur_n, next_n)):
                        arrow_cols.add(bi * 2)

                for ci in range(col_cnt):
                    arrow_txt = "↓" if ci in arrow_cols else ""
                    _add_diagram_cell(tr_arrow, ci, actual_row,
                                      col_widths[ci] if ci < len(col_widths) else col_widths[-1],
                                      arrow_row_height,
                                      arrow_text=arrow_txt)

            actual_row += 1

    p_id = p_counter
    return p_id, table_id + 1, secpr_attached
