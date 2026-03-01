"""표 렌더러: 제목/강조/마크다운/요약 표 생성.

_create_table_row, _append_title_table, _append_emphasis_table,
_append_markdown_table, _append_summary_table
"""
from __future__ import annotations

import xml.etree.ElementTree as ET
from typing import List

from converter.models import BlockType, Block, TableBlock, SummaryTableBlock
from converter.config import (
    _attach_secpr,
    _q, mm_to_hwp, CONFIG,
    PARA_STYLE_MAP, RUN_CHAR_OVERRIDE_MAP, STYLE_ID_MAP,
    INLINE_BOLD_CHAR_ID,
    TABLE_WIDTH_HWP, TITLE_BODY_HEIGHT_HWP, ONE_PT_HWP,
    TITLE_TABLE_ROW_HEIGHTS, EMPH_TABLE_HEIGHT_HWP, EMPH_TABLE_ROW_HEIGHT,
    TABLE_LINE_HEIGHT_HWP, TABLE_MIN_ROW_HEIGHT_HWP, TABLE_ROW_PADDING_HWP,
    TITLE_TABLE_SPACER_CHAR_ID, TITLE_TABLE_SPACER_BORDER_ID,
    TITLE_TABLE_BODY_BORDER_ID, EMPH_TABLE_BORDER_ID,
    TABLE_TITLE_PARA_ID, TABLE_HEADER_PARA_ID, TABLE_BODY_PARA_ID,
    TABLE_TITLE_STYLE_ID, TABLE_HEADER_STYLE_ID, TABLE_BODY_STYLE_ID,
    TABLE_BODY_CHAR_ID, TABLE_HEADER_CHAR_ID,
    SUMMARY_TABLE_PARA_ID, SUMMARY_BODY_PARA_ID, SUMMARY_DESC_PARA_ID,
    SUMMARY_BODY_STYLE_ID, SUMMARY_DESC_STYLE_ID, SUMMARY_TABLE_BORDER_ID,
    SPACER_CHAR_MAP, SPACER_MARKER_MAP,
)
from converter.renderers.inline import (
    _append_text_with_bold, _append_text_with_bold_custom,
)
from converter.renderers.text_fitting import (
    TABLE_FIT_CHAR_IDS, TABLE_FIT_BOLD_CHAR_IDS,
    _fit_cell_text, _compute_col_widths, _estimate_line_count,
)

def _create_table_row(
    tbl: ET.Element,
    *,
    row_idx: int,
    text: str,
    para_id: str,
    style_id: str,
    char_id: str | None,
    cell_margin: dict,
    cell_height: str,
    border_fill: str,
    has_margin: str,
    p_id: int,
    secpr_attached: bool,
) -> tuple[int, bool]:
    tr = ET.SubElement(tbl, _q("hp", "tr"))
    tc = ET.SubElement(
        tr,
        _q("hp", "tc"),
        {
            "name": "",
            "header": "0",
            "hasMargin": has_margin,
            "protect": "0",
            "editable": "0",
            "dirty": "0",
            "borderFillIDRef": border_fill,
        },
    )
    sub_list = ET.SubElement(
        tc,
        _q("hp", "subList"),
        {
            "id": "",
            "textDirection": "HORIZONTAL",
            "lineWrap": "BREAK",
            "vertAlign": "CENTER",
            "linkListIDRef": "0",
            "linkListNextIDRef": "0",
            "textWidth": "0",
            "textHeight": "0",
            "hasTextRef": "0",
            "hasNumRef": "0",
        },
    )
    p = ET.SubElement(
        sub_list,
        _q("hp", "p"),
        {
            "id": str(p_id),
            "paraPrIDRef": para_id,
            "styleIDRef": style_id,
            "pageBreak": "0",
            "columnBreak": "0",
            "merged": "0",
        },
    )
    _append_text_with_bold(p, char_id, text)
    ET.SubElement(tc, _q("hp", "cellAddr"), {"colAddr": "0", "rowAddr": str(row_idx)})
    ET.SubElement(tc, _q("hp", "cellSpan"), {"colSpan": "1", "rowSpan": "1"})
    ET.SubElement(tc, _q("hp", "cellSz"), {"width": TABLE_WIDTH_HWP, "height": cell_height})
    ET.SubElement(tc, _q("hp", "cellMargin"), cell_margin)
    return p_id + 1, secpr_attached


def _append_title_table(
    parent: ET.Element, block: Block, *, table_id: int, p_id: int, secpr_attached: bool
) -> tuple[int, int, bool]:
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
    if not secpr_attached:
        run_sec = ET.SubElement(p_wrapper, _q("hp", "run"), {"charPrIDRef": RUN_CHAR_OVERRIDE_MAP[BlockType.PLAIN]})
        _attach_secpr(run_sec)
        secpr_attached = True
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
            "repeatHeader": "1",
            "rowCnt": "3",
            "colCnt": "1",
            "cellSpacing": "0",
            "borderFillIDRef": "3",  # 표 외곽 테두리 (SOLID)
            "noAdjust": "0",
        },
    )
    total_height = str(int(TITLE_TABLE_ROW_HEIGHTS[0]) + int(TITLE_BODY_HEIGHT_HWP) + int(TITLE_TABLE_ROW_HEIGHTS[2]))
    ET.SubElement(
        tbl,
        _q("hp", "sz"),
        {"width": TABLE_WIDTH_HWP, "widthRelTo": "ABSOLUTE", "height": total_height, "heightRelTo": "ABSOLUTE", "protect": "0"},
    )
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
    ET.SubElement(tbl, _q("hp", "inMargin"), {"left": "510", "right": "510", "top": "141", "bottom": "141"})
    row_specs = [
        {
            "text": " ",
            "para_id": "0",
            "style_id": "0",
            "char_id": TITLE_TABLE_SPACER_CHAR_ID,
            "cell_margin": {"left": "0", "right": "0", "top": "0", "bottom": "0"},
            "cell_height": TITLE_TABLE_ROW_HEIGHTS[0],
            "border_fill": TITLE_TABLE_SPACER_BORDER_ID,
            "has_margin": "0",
        },
        {
            "text": block.text,
            "para_id": PARA_STYLE_MAP[BlockType.TITLE],
            "style_id": STYLE_ID_MAP[BlockType.TITLE],
            "char_id": RUN_CHAR_OVERRIDE_MAP[BlockType.TITLE],
            "cell_margin": {"left": "1417", "right": "1417", "top": "141", "bottom": "141"},
            "cell_height": TITLE_TABLE_ROW_HEIGHTS[1],
            "border_fill": TITLE_TABLE_BODY_BORDER_ID,
            "has_margin": "1",
        },
        {
            "text": " ",
            "para_id": "0",
            "style_id": "0",
            "char_id": TITLE_TABLE_SPACER_CHAR_ID,
            "cell_margin": {"left": "0", "right": "0", "top": "0", "bottom": "0"},
            "cell_height": TITLE_TABLE_ROW_HEIGHTS[2],
            "border_fill": TITLE_TABLE_SPACER_BORDER_ID,
            "has_margin": "0",
        },
    ]
    for idx, spec in enumerate(row_specs):
        p_id, secpr_attached = _create_table_row(
            tbl,
            row_idx=idx,
            text=spec["text"],
            para_id=spec["para_id"],
            style_id=spec["style_id"],
            char_id=spec["char_id"],
            cell_margin=spec["cell_margin"],
            cell_height=spec["cell_height"],
            border_fill=spec["border_fill"],
            has_margin=spec["has_margin"],
            p_id=p_id,
            secpr_attached=secpr_attached,
        )
    return p_id, table_id + 1, secpr_attached


def _append_emphasis_table(
    parent: ET.Element, block: Block, *, table_id: int, p_id: int, secpr_attached: bool
) -> tuple[int, int, bool]:
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
    if not secpr_attached:
        run_sec = ET.SubElement(p_wrapper, _q("hp", "run"), {"charPrIDRef": RUN_CHAR_OVERRIDE_MAP[BlockType.PLAIN]})
        _attach_secpr(run_sec)
        secpr_attached = True
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
            "repeatHeader": "1",
            "rowCnt": "1",
            "colCnt": "1",
            "cellSpacing": "0",
            "borderFillIDRef": "3",  # 표 외곽 테두리 (SOLID)
            "noAdjust": "0",
        },
    )
    ET.SubElement(
        tbl,
        _q("hp", "sz"),
        {"width": TABLE_WIDTH_HWP, "widthRelTo": "ABSOLUTE", "height": EMPH_TABLE_HEIGHT_HWP, "heightRelTo": "ABSOLUTE", "protect": "0"},
    )
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
    ET.SubElement(tbl, _q("hp", "inMargin"), {"left": "510", "right": "510", "top": "141", "bottom": "141"})
    text = f"◈ {block.text}"
    p_id, secpr_attached = _create_table_row(
        tbl,
        row_idx=0,
        text=text,
        para_id=PARA_STYLE_MAP[BlockType.EMPHASIS],
        style_id=STYLE_ID_MAP[BlockType.EMPHASIS],
        char_id=RUN_CHAR_OVERRIDE_MAP[BlockType.EMPHASIS],
        cell_margin={"left": "566", "right": "566", "top": "566", "bottom": "566"},
        cell_height=EMPH_TABLE_ROW_HEIGHT,
        border_fill=EMPH_TABLE_BORDER_ID,
        has_margin="1",
        p_id=p_id,
        secpr_attached=secpr_attached,
    )
    return p_id, table_id + 1, secpr_attached



def _append_markdown_table(
    parent: ET.Element, block: TableBlock, *, table_id: int, p_id: int, secpr_attached: bool
) -> tuple[int, int, bool]:
    """일반 마크다운 표를 생성한다."""

    col_cnt = max(len(block.header), max((len(r) for r in block.rows), default=0))
    if col_cnt == 0:
        return p_id, table_id, secpr_attached

    # 표 제목 앞 spacer (4pt) 확보
    p_sp = ET.SubElement(
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
    run_sp = ET.SubElement(p_sp, _q("hp", "run"), {"charPrIDRef": "4"})
    t_sp = ET.SubElement(run_sp, _q("hp", "t"))
    t_sp.text = " "
    p_id += 1

    # 표 제목
    if block.title:
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
        _append_text_with_bold_custom(p_title, "7", f"< {block.title} >", "13")
        p_id += 1

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
    if not secpr_attached:
        run_sec = ET.SubElement(p_wrapper, _q("hp", "run"), {"charPrIDRef": RUN_CHAR_OVERRIDE_MAP[BlockType.PLAIN]})
        _attach_secpr(run_sec)
        secpr_attached = True

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
            "repeatHeader": "1",
            "rowCnt": str(len(block.rows) + 1),
            "colCnt": str(col_cnt),
            "cellSpacing": "0",
            "borderFillIDRef": "1",
            "noAdjust": "0",
        },
    )
    # 열 너비 계산 (콘텐츠 기반 자동 조정) — 높이 계산보다 먼저 필요
    total_width = int(TABLE_WIDTH_HWP)
    col_widths = _compute_col_widths(block.header, block.rows, col_cnt, total_width)

    # 행별 동적 높이 계산 함수
    def _calc_row_height(cells: List[str], widths: List[int]) -> int:
        """셀 내용 기반으로 행 높이를 동적 계산한다."""
        max_lines = 1
        for idx, cell_text in enumerate(cells[:col_cnt]):
            clean = cell_text.lstrip("@합계").strip() if cell_text.startswith("@합계") else cell_text
            if not clean:
                continue
            w = widths[idx] if idx < len(widths) else widths[-1]
            lines = _estimate_line_count(clean, w, 11, 0)
            if lines > max_lines:
                max_lines = int(lines)
        return max(TABLE_MIN_ROW_HEIGHT_HWP, max_lines * TABLE_LINE_HEIGHT_HWP + TABLE_ROW_PADDING_HWP)

    # 모든 행의 높이를 미리 계산
    header_height = _calc_row_height(block.header, col_widths)
    body_heights = [_calc_row_height(row, col_widths) for row in block.rows]
    total_height = str(header_height + sum(body_heights))
    ET.SubElement(
        tbl,
        _q("hp", "sz"),
        {"width": TABLE_WIDTH_HWP, "widthRelTo": "ABSOLUTE", "height": total_height, "heightRelTo": "ABSOLUTE", "protect": "0"},
    )
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
    ET.SubElement(tbl, _q("hp", "inMargin"), {"left": "510", "right": "510", "top": "141", "bottom": "141"})

    # 테이블 테두리 ID (CONFIG에서 가져오기, 없으면 기본값)
    if CONFIG.tables and CONFIG.tables.borders:
        _tb = CONFIG.tables.borders
        TABLE_HEADER_BORDERS = tuple(str(x) for x in _tb.header)
        TABLE_BODY_TOP_BORDERS = tuple(str(x) for x in _tb.body_top)
        TABLE_BODY_MIDDLE_BORDERS = tuple(str(x) for x in _tb.body_middle)
        TABLE_BODY_BOTTOM_BORDERS = tuple(str(x) for x in _tb.body_bottom)
    else:
        TABLE_HEADER_BORDERS = ("12", "13", "14")
        TABLE_BODY_TOP_BORDERS = ("9", "10", "11")
        TABLE_BODY_MIDDLE_BORDERS = ("4", "3", "5")
        TABLE_BODY_BOTTOM_BORDERS = ("6", "7", "8")

    def _pick_border_id(border_ids: tuple[str, str, str], col_idx: int) -> str:
        left_id, mid_id, right_id = border_ids
        if col_cnt == 1:
            return mid_id
        if col_idx == 0:
            return left_id
        if col_idx == col_cnt - 1:
            return right_id
        return mid_id

    def _body_border_for_row(row_idx: int) -> tuple[str, str, str]:
        """본문 행의 위치에 따라 적절한 borderFill ID 튜플 반환.
        
        Pattern (inputmodel 분석 결과):
        - 헤더 바로 다음 행 (body_idx=0): TOP (9,10,11) - 상단 이중선
        - 본문 마지막 행: BOTTOM (6,7,8) - 하단 굵은 실선
        - 본문 중간 행: MIDDLE (4,3,5) - 일반 실선
        - 본문 1행만 있는 경우: TOP 우선 (헤더 아래 이중선 필요)
        """
        body_rows = len(block.rows)
        if body_rows == 0:
            return TABLE_BODY_BOTTOM_BORDERS
        if body_rows == 1:
            # 본문 1행만: 헤더 바로 다음이므로 TOP 사용 (이중선)
            return TABLE_BODY_TOP_BORDERS
        body_idx = row_idx - 1
        if body_idx == 0:
            return TABLE_BODY_TOP_BORDERS
        if body_idx == body_rows - 1:
            return TABLE_BODY_BOTTOM_BORDERS
        return TABLE_BODY_MIDDLE_BORDERS

    cell_margin_attrs = {"left": "510", "right": "510", "top": "141", "bottom": "141"}

    def _add_row(row_cells: List[str], *, is_header: bool, row_idx: int, border_ids: tuple[str, str, str], p_counter: int, cur_row_height: int) -> int:
        tr = ET.SubElement(tbl, _q("hp", "tr"))
        padded = list(row_cells) + [""] * (col_cnt - len(row_cells))

        # @합계 태그 감지: 첫 셀이 "@합계"로 시작하면 합계 행
        is_total_row = False
        if padded and isinstance(padded[0], str) and padded[0].strip().startswith("@합계"):
            is_total_row = True
            padded[0] = padded[0].strip()[len("@합계"):].strip()  # 태그 제거

        for col_idx, cell_text in enumerate(padded[:col_cnt]):
            # 합계 행 전용 border: 상단 이중선 + 하단 0.5mm 굵은선
            if is_total_row:
                TOTAL_ROW_BORDERS = ("38", "39", "40")
                border_fill = _pick_border_id(TOTAL_ROW_BORDERS, col_idx)
            else:
                border_fill = _pick_border_id(border_ids, col_idx)
            tc = ET.SubElement(
                tr,
                _q("hp", "tc"),
                {
                    "name": "",
                    "header": "0",
                    "hasMargin": "0",
                    "protect": "0",
                    "editable": "0",
                    "dirty": "0",
                    "borderFillIDRef": border_fill,
                },
            )
            sub_list = ET.SubElement(
                tc,
                _q("hp", "subList"),
                {
                    "id": "",
                    "textDirection": "HORIZONTAL",
                    "lineWrap": "BREAK",
                    "vertAlign": "CENTER",
                    "linkListIDRef": "0",
                    "linkListNextIDRef": "0",
                    "textWidth": "0",
                    "textHeight": "0",
                    "hasTextRef": "0",
                    "hasNumRef": "0",
                },
            )
            p = ET.SubElement(
                sub_list,
                _q("hp", "p"),
                {
                    "id": str(p_counter),
                    "paraPrIDRef": TABLE_HEADER_PARA_ID if (is_header or is_total_row) else TABLE_BODY_PARA_ID,
                    "styleIDRef": TABLE_HEADER_STYLE_ID if (is_header or is_total_row) else TABLE_BODY_STYLE_ID,
                    "pageBreak": "0",
                    "columnBreak": "0",
                    "merged": "0",
                },
            )
            # 합계 행은 강제 Bold, 아니면 기존 텍스트 피팅 로직
            if is_total_row:
                char_id = TABLE_HEADER_CHAR_ID  # Bold
                bold_id = TABLE_HEADER_CHAR_ID
            else:
                # 셀별 텍스트 피팅: 최적 (font_size, spacing) 조합 결정
                fit_font, fit_spacing = _fit_cell_text(
                    cell_text, col_widths[col_idx], is_header=is_header
                )
                fit_key = (fit_font, fit_spacing)
                if is_header:
                    char_id = TABLE_FIT_BOLD_CHAR_IDS.get(fit_key, TABLE_HEADER_CHAR_ID)
                    bold_id = char_id
                else:
                    char_id = TABLE_FIT_CHAR_IDS.get(fit_key, TABLE_BODY_CHAR_ID)
                    bold_id = TABLE_FIT_BOLD_CHAR_IDS.get(fit_key, TABLE_HEADER_CHAR_ID)
            _append_text_with_bold_custom(p, char_id, cell_text, bold_id)
            ET.SubElement(tc, _q("hp", "cellAddr"), {"colAddr": str(col_idx), "rowAddr": str(row_idx)})
            ET.SubElement(tc, _q("hp", "cellSpan"), {"colSpan": "1", "rowSpan": "1"})
            ET.SubElement(tc, _q("hp", "cellSz"), {"width": str(col_widths[col_idx]), "height": str(cur_row_height)})
            ET.SubElement(
                tc,
                _q("hp", "cellMargin"),
                cell_margin_attrs,
            )
            p_counter += 1
        return p_counter

    p_counter = p_id
    p_counter = _add_row(block.header, is_header=True, row_idx=0, border_ids=TABLE_HEADER_BORDERS, p_counter=p_counter, cur_row_height=header_height)
    for idx, row in enumerate(block.rows):
        row_idx = idx + 1
        border_ids = _body_border_for_row(row_idx)
        p_counter = _add_row(row, is_header=False, row_idx=row_idx, border_ids=border_ids, p_counter=p_counter, cur_row_height=body_heights[idx])

    return p_counter, table_id + 1, secpr_attached


def _append_summary_table(
    parent: ET.Element, block: SummaryTableBlock, *, table_id: int, p_id: int, secpr_attached: bool
) -> tuple[int, int, bool]:
    """요약표 블록을 표 형태로 렌더링한다."""

    if not block.items:
        return p_id, table_id, secpr_attached

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
    if not secpr_attached:
        run_sec = ET.SubElement(p_wrapper, _q("hp", "run"), {"charPrIDRef": RUN_CHAR_OVERRIDE_MAP[BlockType.PLAIN]})
        _attach_secpr(run_sec)
        secpr_attached = True

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
            "repeatHeader": "1",
            "rowCnt": "1",
            "colCnt": "1",
            "cellSpacing": "0",
            "borderFillIDRef": SUMMARY_TABLE_BORDER_ID,
            "noAdjust": "0",
        },
    )
    row_height = int(TITLE_BODY_HEIGHT_HWP)
    total_height = str(row_height * len(block.items))
    ET.SubElement(
        tbl,
        _q("hp", "sz"),
        {"width": TABLE_WIDTH_HWP, "widthRelTo": "ABSOLUTE", "height": total_height, "heightRelTo": "ABSOLUTE", "protect": "0"},
    )
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
    ET.SubElement(
        tbl,
        _q("hp", "inMargin"),
        {"left": mm_to_hwp(5.0), "right": mm_to_hwp(5.0), "top": mm_to_hwp(2.0), "bottom": mm_to_hwp(2.0)},
    )

    p_counter = p_id
    tr = ET.SubElement(tbl, _q("hp", "tr"))
    tc = ET.SubElement(
        tr,
        _q("hp", "tc"),
        {
            "name": "",
            "header": "0",
            "hasMargin": "1",
            "protect": "0",
            "editable": "0",
            "dirty": "0",
            "borderFillIDRef": SUMMARY_TABLE_BORDER_ID,
        },
    )
    sub_list = ET.SubElement(
        tc,
        _q("hp", "subList"),
        {
            "id": "",
            "textDirection": "HORIZONTAL",
            "lineWrap": "BREAK",
            "vertAlign": "CENTER",
            "linkListIDRef": "0",
            "linkListNextIDRef": "0",
            "textWidth": "0",
            "textHeight": "0",
            "hasTextRef": "0",
            "hasNumRef": "0",
        },
    )

    for idx, item in enumerate(block.items):
        # 첫 번째 항목이 아니면 줄간격용 빈 줄 추가 (맑은 고딕 4pt, space 1칸)
        if idx > 0:
            spacer_p = ET.SubElement(
                sub_list,
                _q("hp", "p"),
                {
                    "id": str(p_counter),
                    "paraPrIDRef": "0",
                    "styleIDRef": "0",
                    "pageBreak": "0",
                    "columnBreak": "0",
                    "merged": "0",
                },
            )
            spacer_run = ET.SubElement(spacer_p, _q("hp", "run"), {"charPrIDRef": "3"})  # 맑은 고딕 4pt
            spacer_t = ET.SubElement(spacer_run, _q("hp", "t"))
            spacer_t.text = " "
            p_counter += 1

        para_pr = SUMMARY_BODY_PARA_ID if item.type == BlockType.BODY else SUMMARY_DESC_PARA_ID
        style_pr = SUMMARY_BODY_STYLE_ID if item.type == BlockType.BODY else SUMMARY_DESC_STYLE_ID
        char_id = "7" if item.type == BlockType.BODY else TABLE_BODY_CHAR_ID
        bold_id = "13" if item.type == BlockType.BODY else "12"
        
        # 출력 텍스트: 본문은 ◦, 설명은 - 붙임
        if item.type == BlockType.BODY:
            display_text = f"◦ {item.text}"
        else:
            display_text = f"- {item.text}"
        
        p = ET.SubElement(
            sub_list,
            _q("hp", "p"),
            {
                "id": str(p_counter),
                "paraPrIDRef": para_pr,
                "styleIDRef": style_pr,
                "pageBreak": "0",
                "columnBreak": "0",
                "merged": "0",
            },
        )
        _append_text_with_bold_custom(p, char_id, display_text, bold_id)
        p_counter += 1

    ET.SubElement(tc, _q("hp", "cellAddr"), {"colAddr": "0", "rowAddr": "0"})
    ET.SubElement(tc, _q("hp", "cellSpan"), {"colSpan": "1", "rowSpan": "1"})
    ET.SubElement(tc, _q("hp", "cellSz"), {"width": TABLE_WIDTH_HWP, "height": str(row_height * max(1, len(block.items)))})
    ET.SubElement(
        tc,
        _q("hp", "cellMargin"),
        {"left": mm_to_hwp(5.0), "right": mm_to_hwp(5.0), "top": mm_to_hwp(2.0), "bottom": mm_to_hwp(2.0)},
    )

    return p_counter, table_id + 1, secpr_attached


