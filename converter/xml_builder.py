"""HWPX XML 빌더: header.xml, section0.xml, content.hpf 등 패키지 파일 생성.

build_header_xml, build_section0_xml, build_content_hpf,
build_container_xml, build_version_xml, build_settings_xml,
build_manifest_xml, build_container_rdf,
_append_header_footer_ctrl,
_build_document_metadata, _build_header_footer_text
"""
from __future__ import annotations

import getpass
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import List, Optional

from converter.models import (
    BlockType, Block, TableBlock, SummaryTableBlock,
    ProcessBlock, DiagramBlock, DocumentMetadata,
)
from converter.config import (
    CONFIG, _q, NS, mm_to_hwp, _attach_secpr,
    PARA_STYLE_MAP, RUN_CHAR_OVERRIDE_MAP, STYLE_ID_MAP,
    INLINE_BOLD_CHAR_ID,
    TABLE_WIDTH_HWP,
    HEADER_PARA_ID, FOOTER_PARA_ID, HEADER_CHAR_ID, FOOTER_CHAR_ID,
    HEADER_STYLE_ID, FOOTER_STYLE_ID,
    TABLE_TITLE_PARA_ID, TABLE_HEADER_PARA_ID, TABLE_BODY_PARA_ID,
    SUMMARY_BODY_PARA_ID, SUMMARY_DESC_PARA_ID,
    TABLE_BODY_CHAR_ID, TABLE_HEADER_CHAR_ID,
    SPACER_CHAR_MAP, SPACER_MARKER_MAP,
)
from converter.renderers.inline import (
    _append_text_with_bold, _append_text_with_bold_custom, _strip_bold_markup,
)
from converter.renderers.tables import (
    _append_title_table, _append_emphasis_table,
    _append_markdown_table, _append_summary_table,
)
from converter.renderers.process_diagram import (
    _append_process_table, _append_diagram_table,
)


# ---------------------------------------------------------------------------
# 문서 메타데이터 유틸
# ---------------------------------------------------------------------------

KOREAN_WEEKDAY_NAMES = [
    "월요일", "화요일", "수요일", "목요일",
    "금요일", "토요일", "일요일",
]


def _format_localized_datetime(local_dt: datetime) -> str:
    weekday = KOREAN_WEEKDAY_NAMES[local_dt.weekday()]
    ampm = "오전" if local_dt.hour < 12 else "오후"
    hour12 = local_dt.hour % 12 or 12
    return (
        f"{local_dt.year}년 {local_dt.month:02d}월 {local_dt.day:02d}일 "
        f"{weekday} {ampm} {hour12}:{local_dt.minute:02d}:{local_dt.second:02d}"
    )


def _isoformat_utc(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _safe_get_username() -> str:
    try:
        return getpass.getuser()
    except Exception:
        return "auto"


def _extract_doc_title(blocks: List[Block]) -> str:
    for block in blocks:
        if block.type == BlockType.TITLE and block.text.strip():
            return _strip_bold_markup(block.text).strip()
    for block in blocks:
        if block.text.strip():
            return _strip_bold_markup(block.text).strip()
    return "Untitled"


def _build_header_footer_text(meta: DocumentMetadata) -> tuple[str, str]:
    """머리말/꼬리말에 넣을 기본 문자열을 구성한다."""
    title = meta.title.strip() or "Untitled"
    header_text = f"추진단 자료 스타일 보고서 - {title}"
    footer_text = ""
    return header_text, footer_text


def _build_document_metadata(blocks: List[Block]) -> DocumentMetadata:
    title = _extract_doc_title(blocks)
    user = _safe_get_username()
    now_utc = datetime.now(timezone.utc)
    local = now_utc.astimezone()
    return DocumentMetadata(
        title=title,
        creator=user,
        subject=title,
        description=title,
        last_saved_by=user,
        keyword=title,
        created_at=now_utc,
        modified_at=now_utc,
        display_date=_format_localized_datetime(local),
    )


def _append_header_footer_ctrl(root: ET.Element, header_text: str, footer_text: str) -> None:
    """Tier1 샘플 패턴을 따르는 머리말/꼬리말 컨트롤을 추가한다.

    - 머리말: 첫 번째 문단(`id="0"`) 안, 제목 테이블(run) 바로 뒤에 header ctrl 삽입.
    - 꼬리말: 첫 번째 SUBTITLE 문단 안, 선행 run 으로 footer ctrl 삽입.
    - 둘 다 오른쪽 정렬 스타일을 사용한다.

    섹션 구조가 예상과 다를 경우에는 조용히 건너뛰도록 방어적으로 동작한다.
    """

    # 1) Header: p id="0" 안의 테이블(run) 뒤에 header ctrl 주입
    first_p = None
    for p in root.findall(_q("hp", "p")):
        first_p = p
        break

    if first_p is not None:
        # 제목 테이블을 담고 있는 run 찾기
        header_run = None
        for run in first_p.findall(_q("hp", "run")):
            tbl = run.find(_q("hp", "tbl"))
            if tbl is not None:
                header_run = run
                break

        if header_run is not None:
            header_ctrl = ET.SubElement(header_run, _q("hp", "ctrl"))
            header_elem = ET.SubElement(
                header_ctrl,
                _q("hp", "header"),
                {
                    "id": "1",
                    "applyPageType": "BOTH",
                },
            )
            header_sublist = ET.SubElement(
                header_elem,
                _q("hp", "subList"),
                {
                    "id": "",
                    "textDirection": "HORIZONTAL",
                    "lineWrap": "BREAK",
                    "vertAlign": "TOP",
                    "linkListIDRef": "0",
                    "linkListNextIDRef": "0",
                    "textWidth": TABLE_WIDTH_HWP,
                    "textHeight": "2834",
                    "hasTextRef": "0",
                    "hasNumRef": "0",
                },
            )
            # Tier1 샘플과 동일한 오른쪽 정렬 스타일을 사용한다.
            # (샘플 기준: paraPrIDRef="8", styleIDRef="0")
            header_p = ET.SubElement(
                header_sublist,
                _q("hp", "p"),
                {
                    "id": "0",
                    "paraPrIDRef": HEADER_PARA_ID,
                    "styleIDRef": HEADER_STYLE_ID,
                    "pageBreak": "0",
                    "columnBreak": "0",
                    "merged": "0",
                },
            )
            header_run_inner = ET.SubElement(
                header_p,
                _q("hp", "run"),
                {"charPrIDRef": HEADER_CHAR_ID},
            )
            # 오른쪽 정렬 시 샘플처럼 앞에 탭을 하나 두어 위치를 맞춘다.
            t = ET.SubElement(header_run_inner, _q("hp", "t"))
            # 탭 요소는 단순 오른쪽 정렬용이므로 상수값 사용
            t.text = ""
            tab = ET.SubElement(
                t,
                _q("hp", "tab"),
                {
                    "width": "39188",
                    "leader": "0",
                    "type": "2",
                },
            )
            # 실제 텍스트는 탭 뒤에 이어붙이기
            t.tail = header_text

    # 2) Footer: 첫 번째 SUBTITLE 문단 안에 footer ctrl run을 prepend
    #    스타일 통일 후 paraPrIDRef로 구분 불가 → run의 charPrIDRef로 식별
    subtitle_char_id = RUN_CHAR_OVERRIDE_MAP[BlockType.SUBTITLE]
    first_subtitle_p = None
    for p in root.findall(_q("hp", "p")):
        for run_el in p.findall(_q("hp", "run")):
            if run_el.get("charPrIDRef") == subtitle_char_id:
                first_subtitle_p = p
                break
        if first_subtitle_p is not None:
            break

    if first_subtitle_p is not None:
        # 기존 run 들 앞에 footer ctrl run 을 하나 삽입
        footer_run = ET.Element(
            _q("hp", "run"),
            {"charPrIDRef": FOOTER_CHAR_ID},
        )
        footer_ctrl = ET.SubElement(footer_run, _q("hp", "ctrl"))
        footer_elem = ET.SubElement(
            footer_ctrl,
            _q("hp", "footer"),
            {
                "id": "3",
                "applyPageType": "BOTH",
            },
        )
        footer_sublist = ET.SubElement(
            footer_elem,
            _q("hp", "subList"),
            {
                "id": "",
                "textDirection": "HORIZONTAL",
                "lineWrap": "BREAK",
                "vertAlign": "BOTTOM",
                "linkListIDRef": "0",
                "linkListNextIDRef": "0",
                "textWidth": TABLE_WIDTH_HWP,
                "textHeight": "2834",
                "hasTextRef": "0",
                "hasNumRef": "0",
            },
        )
        # Tier1 샘플과 동일한 꼬리말용 paraPr/스타일을 사용한다.
        # (샘플 기준: paraPrIDRef="9", styleIDRef="0")
        footer_p = ET.SubElement(
            footer_sublist,
            _q("hp", "p"),
            {
                "id": "0",
                "paraPrIDRef": FOOTER_PARA_ID,
                "styleIDRef": FOOTER_STYLE_ID,
                "pageBreak": "0",
                "columnBreak": "0",
                "merged": "0",
            },
        )
        footer_run_inner = ET.SubElement(
            footer_p,
            _q("hp", "run"),
            {"charPrIDRef": FOOTER_CHAR_ID},
        )
        t_footer = ET.SubElement(footer_run_inner, _q("hp", "t"))
        t_footer.text = footer_text

        # 새 run 을 첫 child 로 삽입
        existing = list(first_subtitle_p)
        for child in existing:
            first_subtitle_p.remove(child)
        first_subtitle_p.append(footer_run)
        for child in existing:
            first_subtitle_p.append(child)


def build_header_xml() -> bytes:
    """header.xml (head/refList) 빌더.

    - style_textbook에서 사용하는 글꼴/문단/스타일 정의를 포함한다.
    - 머리말/꼬리말용 별도 스타일은 아직 두지 않고, 기본 PLAIN 스타일을 재사용한다.
    """

    head = ET.Element(
        _q("hh", "head"),
        {
            "version": "1.4",
            "secCnt": "1",
            "xmlns:ha": NS["ha"],
            "xmlns:hp": NS["hp"],
            "xmlns:hp10": NS["hp10"],
            "xmlns:hs": NS["hs"],
            "xmlns:hc": NS["hc"],
            "xmlns:hh": NS["hh"],
            "xmlns:hhs": NS["hhs"],
            "xmlns:hm": NS["hm"],
            "xmlns:hpf": NS["hpf"],
            "xmlns:dc": NS["dc"],
            "xmlns:opf": NS["opf"],
            "xmlns:ooxmlchart": NS["ooxmlchart"],
            "xmlns:hwpunitchar": NS["hwpunitchar"],
            "xmlns:epub": NS["epub"],
            "xmlns:config": NS["config"],
        },
    )

    # beginNum: 최소 번호 설정
    ET.SubElement(
        head,
        _q("hh", "beginNum"),
        {"page": "1", "footnote": "1", "endnote": "1", "pic": "1", "tbl": "1", "equation": "1"},
    )

    ref_list = ET.SubElement(head, _q("hh", "refList"))

    # fontfaces: 7개 언어 전부 정의 (CRITICAL - Hangul requires all 7 languages)
    # style_textbook에서 실제로 사용하는 글꼴만 정의:
    # - id=0: HY헤드라인M
    # - id=1: 휴먼명조
    # - id=2: 맑은 고딕
    fontfaces = ET.SubElement(ref_list, _q("hh", "fontfaces"), {"itemCnt": "7"})

    def _add_font(ff_parent, font_id: int, face: str) -> None:
        font = ET.SubElement(
            ff_parent,
            _q("hh", "font"),
            {"id": str(font_id), "face": face, "type": "TTF", "isEmbedded": "0"},
        )
        ET.SubElement(
            font,
            _q("hh", "typeInfo"),
            {
                "familyType": "FCAT_GOTHIC",
                "weight": "5",
                "proportion": "3",
                "contrast": "2",
                "strokeVariation": "0",
                "armStyle": "0",
                "letterform": "2",
                "midline": "0",
                "xHeight": "4",
            },
        )

    def add_fontface(lang: str) -> None:
        ff = ET.SubElement(fontfaces, _q("hh", "fontface"), {"lang": lang, "fontCnt": "3"})
        _add_font(ff, 0, "HY헤드라인M")
        _add_font(ff, 1, "휴먼명조")
        _add_font(ff, 2, "맑은 고딕")

    # 7개 언어 모두 추가
    for lang in ["HANGUL", "LATIN", "HANJA", "JAPANESE", "OTHER", "SYMBOL", "USER"]:
        add_fontface(lang)

    # borderFills: Phase1.5 requires the reference table palette plus a few custom fills
    border_fills = ET.SubElement(ref_list, _q("hh", "borderFills"), {"itemCnt": "0"})
    border_fill_count = 0

    def add_border_fill(bf_id: int, *, fill_brush: dict | None = None) -> None:
        nonlocal border_fill_count
        bf = ET.SubElement(
            border_fills,
            _q("hh", "borderFill"),
            {
                "id": str(bf_id),
                "threeD": "0",
                "shadow": "0",
                "centerLine": "NONE",
                "breakCellSeparateLine": "0",
            },
        )
        ET.SubElement(bf, _q("hh", "slash"), {"type": "NONE", "Crooked": "0", "isCounter": "0"})
        ET.SubElement(bf, _q("hh", "backSlash"), {"type": "NONE", "Crooked": "0", "isCounter": "0"})
        ET.SubElement(bf, _q("hh", "leftBorder"), {"type": "NONE", "width": "0.1 mm", "color": "#000000"})
        ET.SubElement(bf, _q("hh", "rightBorder"), {"type": "NONE", "width": "0.1 mm", "color": "#000000"})
        ET.SubElement(bf, _q("hh", "topBorder"), {"type": "NONE", "width": "0.1 mm", "color": "#000000"})
        ET.SubElement(bf, _q("hh", "bottomBorder"), {"type": "NONE", "width": "0.1 mm", "color": "#000000"})
        ET.SubElement(bf, _q("hh", "diagonal"), {"type": "SOLID", "width": "0.1 mm", "color": "#000000"})
        if fill_brush is not None:
            brush = ET.SubElement(bf, _q("hc", "fillBrush"))
            ET.SubElement(brush, _q("hc", "winBrush"), fill_brush)
        border_fill_count += 1

    def add_border_fill_custom(
        bf_id: int,
        *,
        fill_brush: dict | None = None,
        borders: dict[str, tuple[str, str]] | None = None,
    ) -> None:
        """borders={'top':('SOLID','0.5 mm'), 'bottom':('DOUBLE','0.5 mm')}"""

        nonlocal border_fill_count
        bf = ET.SubElement(
            border_fills,
            _q("hh", "borderFill"),
            {
                "id": str(bf_id),
                "threeD": "0",
                "shadow": "0",
                "centerLine": "NONE",
                "breakCellSeparateLine": "0",
            },
        )
        ET.SubElement(bf, _q("hh", "slash"), {"type": "NONE", "Crooked": "0", "isCounter": "0"})
        ET.SubElement(bf, _q("hh", "backSlash"), {"type": "NONE", "Crooked": "0", "isCounter": "0"})

        def _add_edge(tag: str, default_type: str = "NONE", default_width: str = "0.1 mm") -> None:
            typ, width = (borders.get(tag) if borders and tag in borders else (default_type, default_width))
            ET.SubElement(bf, _q("hh", f"{tag}Border"), {"type": typ, "width": width, "color": "#000000"})

        _add_edge("left")
        _add_edge("right")
        _add_edge("top")
        _add_edge("bottom")
        ET.SubElement(bf, _q("hh", "diagonal"), {"type": "SOLID", "width": "0.1 mm", "color": "#000000"})
        if fill_brush is not None:
            brush = ET.SubElement(bf, _q("hc", "fillBrush"))
            ET.SubElement(brush, _q("hc", "winBrush"), fill_brush)
        border_fill_count += 1

    add_border_fill(1)
    add_border_fill(2, fill_brush={"faceColor": "none", "hatchColor": "#999999", "alpha": "0"})

    reference_borders: list[tuple[int, dict[str, tuple[str, str]], dict | None]] = [
        (3, {"left": ("SOLID", "0.12 mm"), "right": ("SOLID", "0.12 mm"), "top": ("SOLID", "0.12 mm"), "bottom": ("SOLID", "0.12 mm")}, None),
        (4, {"left": ("NONE", "0.12 mm"), "right": ("SOLID", "0.12 mm"), "top": ("SOLID", "0.12 mm"), "bottom": ("SOLID", "0.12 mm")}, None),
        (5, {"left": ("SOLID", "0.12 mm"), "right": ("NONE", "0.12 mm"), "top": ("SOLID", "0.12 mm"), "bottom": ("SOLID", "0.12 mm")}, None),
        (6, {"left": ("NONE", "0.12 mm"), "right": ("SOLID", "0.12 mm"), "top": ("SOLID", "0.12 mm"), "bottom": ("SOLID", "0.5 mm")}, None),
        (7, {"left": ("SOLID", "0.12 mm"), "right": ("SOLID", "0.12 mm"), "top": ("SOLID", "0.12 mm"), "bottom": ("SOLID", "0.5 mm")}, None),
        (8, {"left": ("SOLID", "0.12 mm"), "right": ("NONE", "0.12 mm"), "top": ("SOLID", "0.12 mm"), "bottom": ("SOLID", "0.5 mm")}, None),
        (9, {"left": ("NONE", "0.12 mm"), "right": ("SOLID", "0.12 mm"), "top": ("DOUBLE_SLIM", "0.5 mm"), "bottom": ("SOLID", "0.12 mm")}, None),
        (10, {"left": ("SOLID", "0.12 mm"), "right": ("SOLID", "0.12 mm"), "top": ("DOUBLE_SLIM", "0.5 mm"), "bottom": ("SOLID", "0.12 mm")}, None),
        (11, {"left": ("SOLID", "0.12 mm"), "right": ("NONE", "0.12 mm"), "top": ("DOUBLE_SLIM", "0.5 mm"), "bottom": ("SOLID", "0.12 mm")}, None),
        (12, {"left": ("NONE", "0.12 mm"), "right": ("SOLID", "0.12 mm"), "top": ("SOLID", "0.5 mm"), "bottom": ("DOUBLE_SLIM", "0.5 mm")}, {"faceColor": "#EBDEF1", "hatchColor": "#999999", "alpha": "0"}),
        (13, {"left": ("SOLID", "0.12 mm"), "right": ("SOLID", "0.12 mm"), "top": ("SOLID", "0.5 mm"), "bottom": ("DOUBLE_SLIM", "0.5 mm")}, {"faceColor": "#EBDEF1", "hatchColor": "#999999", "alpha": "0"}),
        (14, {"left": ("SOLID", "0.12 mm"), "right": ("NONE", "0.12 mm"), "top": ("SOLID", "0.5 mm"), "bottom": ("DOUBLE_SLIM", "0.5 mm")}, {"faceColor": "#EBDEF1", "hatchColor": "#999999", "alpha": "0"}),
    ]
    for bf_id, borders, fill in reference_borders:
        add_border_fill_custom(bf_id, borders=borders, fill_brush=fill)

    add_border_fill_custom(
        15,
        borders={
            "left": ("NONE", "0.1 mm"),
            "right": ("NONE", "0.1 mm"),
            "top": ("NONE", "0.1 mm"),
            "bottom": ("NONE", "0.1 mm"),
        },
        fill_brush={"faceColor": "none", "hatchColor": "#000000", "alpha": "0"},
    )
    add_border_fill_custom(
        16,
        borders={
            "left": ("SOLID", "0.12 mm"),
            "right": ("SOLID", "0.12 mm"),
            "top": ("SOLID", "0.5 mm"),
            "bottom": ("DOUBLE_SLIM", "0.5 mm"),
        },
        fill_brush={"faceColor": "#EBDEF1", "hatchColor": "#999999", "alpha": "0"},
    )
    add_border_fill_custom(
        17,
        borders={
            "left": ("SOLID", "0.12 mm"),
            "right": ("NONE", "0.12 mm"),
            "top": ("SOLID", "0.5 mm"),
            "bottom": ("DOUBLE_SLIM", "0.5 mm"),
        },
        fill_brush={"faceColor": "#EBDEF1", "hatchColor": "#999999", "alpha": "0"},
    )
    add_border_fill_custom(
        18,
        borders={
            "left": ("DASH", "0.12 mm"),
            "right": ("DASH", "0.12 mm"),
            "top": ("DASH", "0.12 mm"),
            "bottom": ("DASH", "0.12 mm"),
        },
    )

    # Stylebook 표 세트 (170mm 폭, 헤더 배경 연보라, 좌우선 제거)
    add_border_fill_custom(
        19,
        fill_brush={"faceColor": "#EBDEF1", "hatchColor": "#999999", "alpha": "0"},
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.5 mm"),
            "bottom": ("DOUBLE", "0.5 mm"),
        },
    )
    add_border_fill_custom(
        20,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.12 mm"),
            "bottom": ("SOLID", "0.12 mm"),
        },
    )
    add_border_fill_custom(
        21,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.12 mm"),
            "bottom": ("SOLID", "0.5 mm"),
        },
    )
    add_border_fill_custom(
        22,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("DOUBLE", "0.5 mm"),
            "bottom": ("SOLID", "0.12 mm"),
        },
    )
    add_border_fill_custom(
        23,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("DOUBLE", "0.5 mm"),
            "bottom": ("SOLID", "0.5 mm"),
        },
    )

    # Stylebook (no vertical lines, uniform per-row)
    add_border_fill_custom(
        24,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.5 mm"),
            "bottom": ("DOUBLE", "0.5 mm"),
        },
        fill_brush={"faceColor": "#EBDEF1", "hatchColor": "#999999", "alpha": "0"},
    )
    add_border_fill_custom(
        25,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.12 mm"),
            "bottom": ("SOLID", "0.12 mm"),
        },
    )
    add_border_fill_custom(
        26,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.12 mm"),
            "bottom": ("SOLID", "0.5 mm"),
        },
    )
    add_border_fill_custom(
        27,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.5 mm"),
            "bottom": ("DOUBLE", "0.5 mm"),
        },
        fill_brush={"faceColor": "#EBDEF1", "hatchColor": "#999999", "alpha": "0"},
    )
    add_border_fill_custom(
        28,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.12 mm"),
            "bottom": ("SOLID", "0.12 mm"),
        },
    )
    add_border_fill_custom(
        29,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.12 mm"),
            "bottom": ("SOLID", "0.5 mm"),
        },
    )

    # Row-locked fills (no verticals)
    add_border_fill_custom(
        30,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.5 mm"),
            "bottom": ("DOUBLE", "0.5 mm"),
        },
        fill_brush={"faceColor": "#EBDEF1", "hatchColor": "#999999", "alpha": "0"},
    )
    add_border_fill_custom(
        31,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.12 mm"),
            "bottom": ("SOLID", "0.12 mm"),
        },
    )
    add_border_fill_custom(
        32,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.5 mm"),
            "bottom": ("SOLID", "0.5 mm"),
        },
        fill_brush={"faceColor": "#EBDEF1", "hatchColor": "#999999", "alpha": "0"},
    )
    add_border_fill_custom(
        33,
        borders={
            "left": ("NONE", "0 mm"),
            "right": ("NONE", "0 mm"),
            "top": ("SOLID", "0.12 mm"),
            "bottom": ("SOLID", "0.5 mm"),
        },
    )

    # Dedicated fills for converter-specific tables
    # ID 34: 대제목 1,3행 spacer - 연보라 배경 + 테두리 NONE
    add_border_fill_custom(
        34,
        borders={
            "left": ("NONE", "0.12 mm"),
            "right": ("NONE", "0.12 mm"),
            "top": ("NONE", "0.12 mm"),
            "bottom": ("NONE", "0.12 mm"),
        },
        fill_brush={"faceColor": "#EBDEF1", "hatchColor": "#999999", "alpha": "0"},
    )
    # ID 35: 대제목 본문 (2행) - 테두리 NONE, 배경 없음
    add_border_fill_custom(
        35,
        borders={
            "left": ("NONE", "0.12 mm"),
            "right": ("NONE", "0.12 mm"),
            "top": ("NONE", "0.12 mm"),
            "bottom": ("NONE", "0.12 mm"),
        },
    )
    # ID 36: 강조 표 - 연두 배경 + 0.12mm 실선 테두리
    add_border_fill_custom(
        36,
        borders={
            "left": ("SOLID", "0.12 mm"),
            "right": ("SOLID", "0.12 mm"),
            "top": ("SOLID", "0.12 mm"),
            "bottom": ("SOLID", "0.12 mm"),
        },
        fill_brush={"faceColor": "#CDF2E4", "hatchColor": "#999999", "alpha": "0"},
    )
    # ID 37: 요약표 - 점선 0.12mm 테두리
    add_border_fill_custom(
        37,
        borders={
            "left": ("DOT", "0.12 mm"),
            "right": ("DOT", "0.12 mm"),
            "top": ("DOT", "0.12 mm"),
            "bottom": ("DOT", "0.12 mm"),
        },
    )
    # ID 38~40: 합계 행 전용 (상단 이중선 + 하단 0.5mm 굵은선)
    add_border_fill_custom(
        38,
        borders={
            "left": ("NONE", "0.12 mm"),
            "right": ("SOLID", "0.12 mm"),
            "top": ("DOUBLE_SLIM", "0.5 mm"),
            "bottom": ("SOLID", "0.5 mm"),
        },
    )
    add_border_fill_custom(
        39,
        borders={
            "left": ("SOLID", "0.12 mm"),
            "right": ("SOLID", "0.12 mm"),
            "top": ("DOUBLE_SLIM", "0.5 mm"),
            "bottom": ("SOLID", "0.5 mm"),
        },
    )
    add_border_fill_custom(
        40,
        borders={
            "left": ("SOLID", "0.12 mm"),
            "right": ("NONE", "0.12 mm"),
            "top": ("DOUBLE_SLIM", "0.5 mm"),
            "bottom": ("SOLID", "0.5 mm"),
        },
    )

    # ID 41: 프로세스 제목 행 (연회색 배경 + 실선 테두리)
    add_border_fill_custom(
        41,
        borders={
            "left": ("SOLID", "0.12 mm"),
            "right": ("SOLID", "0.12 mm"),
            "top": ("SOLID", "0.12 mm"),
            "bottom": ("SOLID", "0.12 mm"),
        },
        fill_brush={"faceColor": "#D6E4F0", "hatchColor": "#999999", "alpha": "0"},
    )
    # ID 42: 프로세스 설명 행 (흰 배경 + 실선 테두리, 상단선 없음 — 제목행이 이미 있음)
    add_border_fill_custom(
        42,
        borders={
            "left": ("SOLID", "0.12 mm"),
            "right": ("SOLID", "0.12 mm"),
            "top": ("NONE", "0.12 mm"),
            "bottom": ("SOLID", "0.12 mm"),
        },
    )

    border_fills.set("itemCnt", str(border_fill_count))

    # charProperties: 글자 모양 정의 (style_textbook 기준)
    char_props = ET.SubElement(ref_list, _q("hh", "charProperties"), {"itemCnt": "0"})

    def add_char_pr(
        char_id: int, height: int, hangul_font_id: int,
        *, bold: bool = False, spacing: int = 0,
    ) -> None:
        char = ET.SubElement(
            char_props,
            _q("hh", "charPr"),
            {
                "id": str(char_id),
                "height": str(height),
                "textColor": "#000000",
                "shadeColor": "none",
                "useFontSpace": "0",
                "useKerning": "0",
                "symMark": "NONE",
                "borderFillIDRef": "2",
            },
        )
        ET.SubElement(
            char,
            _q("hh", "fontRef"),
            {
                "hangul": str(hangul_font_id),
                "latin": str(hangul_font_id),
                "hanja": str(hangul_font_id),
                "japanese": str(hangul_font_id),
                "other": str(hangul_font_id),
                "symbol": str(hangul_font_id),
                "user": str(hangul_font_id),
            },
        )
        ET.SubElement(
            char,
            _q("hh", "ratio"),
            {
                "hangul": "100",
                "latin": "100",
                "hanja": "100",
                "japanese": "100",
                "other": "100",
                "symbol": "100",
                "user": "100",
            },
        )
        sp = str(spacing)
        ET.SubElement(
            char,
            _q("hh", "spacing"),
            {
                "hangul": sp,
                "latin": sp,
                "hanja": sp,
                "japanese": sp,
                "other": sp,
                "symbol": sp,
                "user": sp,
            },
        )
        ET.SubElement(
            char,
            _q("hh", "relSz"),
            {
                "hangul": "100",
                "latin": "100",
                "hanja": "100",
                "japanese": "100",
                "other": "100",
                "symbol": "100",
                "user": "100",
            },
        )
        ET.SubElement(
            char,
            _q("hh", "offset"),
            {
                "hangul": "0",
                "latin": "0",
                "hanja": "0",
                "japanese": "0",
                "other": "0",
                "symbol": "0",
                "user": "0",
            },
        )
        ET.SubElement(
            char,
            _q("hh", "underline"),
            {"type": "NONE", "shape": "SOLID", "color": "#000000"},
        )
        ET.SubElement(char, _q("hh", "strikeout"), {"shape": "NONE", "color": "#000000"})
        ET.SubElement(char, _q("hh", "outline"), {"type": "NONE"})
        ET.SubElement(
            char,
            _q("hh", "shadow"),
            {"type": "NONE", "color": "#B2B2B2", "offsetX": "10", "offsetY": "10"},
        )
        if bold:
            ET.SubElement(char, _q("hh", "bold"))

    # 기본 charPr 정의 (id, height, font_id, bold, spacing)
    char_defs: list[tuple[int, int, int, bool, int]] = [
        (0, 1500, 1, False, 0),    # 본문 휴먼명조 15pt
        (1, 1000, 2, False, 0),    # spacer 10pt
        (2, 800, 2, False, 0),     # spacer 8pt
        (3, 600, 2, False, 0),     # spacer 6pt
        (4, 400, 2, False, 0),     # spacer 4pt
        (5, 1500, 0, True, 0),     # 주제목 HY 15pt Bold
        (6, 1500, 0, False, 0),    # 소제목 HY 15pt
        (7, 1200, 2, False, 0),    # 설명3 맑은고딕 12pt
        (8, 1500, 1, True, 0),     # 강조 휴먼 15pt Bold
        (9, 100, 2, False, 0),     # 1pt filler
        (10, 1300, 1, False, 0),   # 머리말/꼬리말 휴먼명조 13pt
        (11, 1100, 2, False, 0),   # 표 본문 맑은고딕 11pt
        (12, 1100, 2, True, 0),    # 표 헤더 맑은고딕 11pt Bold
        (13, 1200, 2, True, 0),    # 표/요약표 볼드 맑은고딕 12pt
        # --- 표 텍스트 피팅용 변형 charPr (일반) ---
        (14, 1100, 2, False, -5),  # 11pt spacing -5%
        (15, 1100, 2, False, -10), # 11pt spacing -10%
        (16, 1100, 2, False, -15), # 11pt spacing -15%
        (17, 1100, 2, False, -20), # 11pt spacing -20%
        (18, 1000, 2, False, 0),   # 10pt spacing 0%
        (19, 1000, 2, False, -5),  # 10pt spacing -5%
        (20, 1000, 2, False, -10), # 10pt spacing -10%
        (21, 1000, 2, False, -15), # 10pt spacing -15%
        (22, 1000, 2, False, -20), # 10pt spacing -20%
        # --- 표 텍스트 피팅용 변형 charPr (볼드/헤더) ---
        (23, 1100, 2, True, -5),   # 11pt Bold spacing -5%
        (24, 1100, 2, True, -10),  # 11pt Bold spacing -10%
        (25, 1100, 2, True, -15),  # 11pt Bold spacing -15%
        (26, 1100, 2, True, -20),  # 11pt Bold spacing -20%
        (27, 1000, 2, True, 0),    # 10pt Bold spacing 0%
        (28, 1000, 2, True, -5),   # 10pt Bold spacing -5%
        (29, 1000, 2, True, -10),  # 10pt Bold spacing -10%
        (30, 1000, 2, True, -15),  # 10pt Bold spacing -15%
        (31, 1000, 2, True, -20),  # 10pt Bold spacing -20%
        # --- 제목/소제목 inline bold용 (HY헤드라인M) ---
        (32, 1500, 0, True, 0),    # HY헤드라인M 15pt Bold (소제목/제목 bold)
    ]
    for cid, height, font_id, is_bold, sp in char_defs:
        add_char_pr(cid, height, font_id, bold=is_bold, spacing=sp)
    char_props.set("itemCnt", str(len(char_defs)))

    # tabProperties: 3개 (참조 파일 기준)
    tab_props = ET.SubElement(ref_list, _q("hh", "tabProperties"), {"itemCnt": "3"})
    ET.SubElement(tab_props, _q("hh", "tabPr"), {"id": "0", "autoTabLeft": "0", "autoTabRight": "0"})
    ET.SubElement(tab_props, _q("hh", "tabPr"), {"id": "1", "autoTabLeft": "1", "autoTabRight": "0"})
    ET.SubElement(tab_props, _q("hh", "tabPr"), {"id": "2", "autoTabLeft": "0", "autoTabRight": "1"})

    # paraProperties: 문단 모양 정의 (id 0 = 기본, 나머지는 BlockType/여백용)
    para_props = ET.SubElement(ref_list, _q("hh", "paraProperties"), {"itemCnt": "0"})

    def add_para_pr(
        para_id: int,
        horizontal_align: str,
        line_spacing_value: int,
        *,
        font_line_height: str = "0",
        snap_to_grid: str = "1",
        margin: Optional[dict] = None,
        border_fill_id: str = "1",
    ) -> None:
        para = ET.SubElement(
            para_props,
            _q("hh", "paraPr"),
            {
                "id": str(para_id),
                "tabPrIDRef": "0",
                "condense": "0",
                "fontLineHeight": font_line_height,
                "snapToGrid": snap_to_grid,
                "suppressLineNumbers": "0",
                "checked": "0",
            },
        )
        ET.SubElement(
            para,
            _q("hh", "align"),
            {"horizontal": horizontal_align, "vertical": "BASELINE"},
        )
        ET.SubElement(para, _q("hh", "heading"), {"type": "NONE", "idRef": "0", "level": "0"})
        ET.SubElement(
            para,
            _q("hh", "breakSetting"),
            {
                "breakLatinWord": "KEEP_WORD",
                "breakNonLatinWord": "KEEP_WORD",
                "widowOrphan": "0",
                "keepWithNext": "0",
                "keepLines": "0",
                "pageBreakBefore": "0",
                "lineWrap": "BREAK",
            },
        )
        ET.SubElement(para, _q("hh", "autoSpacing"), {"eAsianEng": "0", "eAsianNum": "0"})
        margin_el = ET.SubElement(para, _q("hh", "margin"))
        margin_values = {"intent": "0", "left": "0", "right": "0", "prev": "0", "next": "0"}
        if margin:
            for key, value in margin.items():
                if key in margin_values:
                    margin_values[key] = str(value)
        for key, value in margin_values.items():
            ET.SubElement(margin_el, _q("hc", key), {"value": value, "unit": "HWPUNIT"})
        ET.SubElement(
            para,
            _q("hh", "lineSpacing"),
            {"type": "PERCENT", "value": str(line_spacing_value), "unit": "PERCENT"},
        )
        ET.SubElement(
            para,
            _q("hh", "border"),
            {
                "borderFillIDRef": border_fill_id,
                "offsetLeft": "0",
                "offsetRight": "0",
                "offsetTop": "0",
                "offsetBottom": "0",
                "connect": "0",
                "ignoreMargin": "0",
            },
        )

    para_defs = [
        (0, "JUSTIFY", 160, {"font_line_height": "1", "snap_to_grid": "0"}),
        (1, "CENTER", 130, {}),
        (2, "LEFT", 160, {}),
        (3, "LEFT", 160, {}),
        (4, "LEFT", 160, {}),
        (5, "LEFT", 160, {}),
        (6, "CENTER", 130, {}),
        # 예비 paraPr 5종 (Option A 대비)
        (7, "LEFT", 150, {"font_line_height": "0", "snap_to_grid": "1"}),
        (
            8,
            "LEFT",
            160,
            {
                "font_line_height": "0",
                "snap_to_grid": "1",
                # DESC2 hanging indent 37.5pt → 3750 HWP units.
                "margin": {"intent": -3750},
            },
        ),
        (
            9,
            "JUSTIFY",
            160,
            {
                "font_line_height": "0",
                "snap_to_grid": "0",
                # Body paragraphs target 30pt indent (3000 HWP units).
                "margin": {"intent": -3000},
            },
        ),
        (
            10,
            "LEFT",
            160,
            {
                "font_line_height": "0",
                "snap_to_grid": "1",
                # DESC3 indent tuned to 35pt (3500 HWP units) while staying left aligned.
                "margin": {"intent": -3500},
            },
        ),
        (11, "LEFT", 135, {"font_line_height": "0", "snap_to_grid": "1"}),
        (12, "RIGHT", 160, {"font_line_height": "0", "snap_to_grid": "1"}),  # 머리말
        (13, "RIGHT", 160, {"font_line_height": "0", "snap_to_grid": "1"}),  # 꼬리말
        (14, "CENTER", 160, {"font_line_height": "0", "snap_to_grid": "1"}),  # 표 제목
        (15, "CENTER", 130, {"font_line_height": "0", "snap_to_grid": "1"}),  # 표 헤더
        (16, "CENTER", 130, {"font_line_height": "0", "snap_to_grid": "1"}),  # 표 본문
        (17, "CENTER", 130, {"font_line_height": "0", "snap_to_grid": "1"}),  # 요약표 셀 wrapper
        (
            18,
            "LEFT",
            130,
            {
                "font_line_height": "0",
                "snap_to_grid": "1",
                "margin": {"intent": 0},
            },
        ),  # 요약표 본문 (들여쓰기 0)
        (
            19,
            "LEFT",
            130,
            {
                "font_line_height": "0",
                "snap_to_grid": "1",
                "margin": {"intent": 500},
            },
        ),  # 요약표 설명 (들여쓰기 5pt)
        (12, "RIGHT", 130, {"font_line_height": "0", "snap_to_grid": "1"}),  # 머리말
        (13, "RIGHT", 130, {"font_line_height": "0", "snap_to_grid": "1"}),  # 꼬리말
    ]
    for pid, align, spacing, extra in para_defs:
        add_para_pr(
            pid,
            align,
            spacing,
            font_line_height=extra.get("font_line_height", "0"),
            snap_to_grid=extra.get("snap_to_grid", "1"),
            margin=extra.get("margin"),
            border_fill_id=extra.get("border_fill_id", "1"),
        )
    para_props.set("itemCnt", str(len(para_defs)))

    # numberings: 번호 매기기 정의 (참조 파일 기준)
    numberings = ET.SubElement(ref_list, _q("hh", "numberings"), {"itemCnt": "1"})
    numbering = ET.SubElement(numberings, _q("hh", "numbering"), {"id": "1", "start": "0"})

    # 10개 레벨의 paraHead 추가
    levels = [
        {"level": "1", "numFormat": "DIGIT", "text": "^1."},
        {"level": "2", "numFormat": "HANGUL_SYLLABLE", "text": "^2."},
        {"level": "3", "numFormat": "DIGIT", "text": "^3)"},
        {"level": "4", "numFormat": "HANGUL_SYLLABLE", "text": "^4)"},
        {"level": "5", "numFormat": "DIGIT", "text": "(^5)"},
        {"level": "6", "numFormat": "HANGUL_SYLLABLE", "text": "(^6)"},
        {"level": "7", "numFormat": "CIRCLED_DIGIT", "checkable": "1", "text": "^7"},
        {"level": "8", "numFormat": "CIRCLED_HANGUL_SYLLABLE", "checkable": "1", "text": "^8"},
        {"level": "9", "numFormat": "HANGUL_JAMO", "text": ""},
        {"level": "10", "numFormat": "ROMAN_SMALL", "checkable": "1", "text": ""},
    ]

    for lvl in levels:
        attrs = {
            "start": "1",
            "level": lvl["level"],
            "align": "LEFT",
            "useInstWidth": "1",
            "autoIndent": "1",
            "widthAdjust": "0",
            "textOffsetType": "PERCENT",
            "textOffset": "50",
            "numFormat": lvl["numFormat"],
            "charPrIDRef": "4294967295",
            "checkable": lvl.get("checkable", "0"),
        }
        para_head = ET.SubElement(numbering, _q("hh", "paraHead"), attrs)
        para_head.text = lvl["text"]

    # styles: BlockType별 문단 스타일 정의
    styles = ET.SubElement(ref_list, _q("hh", "styles"), {"itemCnt": "0"})

    def add_style(style_id: int, name: str, eng_name: str, para_ref: int, char_ref: int) -> None:
        ET.SubElement(
            styles,
            _q("hh", "style"),
            {
                "id": str(style_id),
                "type": "PARA",
                "name": name,
                "engName": eng_name,
                "paraPrIDRef": str(para_ref),
                "charPrIDRef": str(char_ref),
                "nextStyleIDRef": str(style_id),
                "langID": "1042",
                "lockForm": "0",
            },
        )

    style_defs = [
        (0, "바탕글", "Normal", 0, 0),
        (1, "주제목", "MainTitle", 1, 5),
        (2, "소제목", "SubTitle", 2, 6),
        (3, "본문", "Body", 9, 0),
        (4, "설명2", "Desc2", 8, 0),
        (5, "설명3", "Desc3", 10, 0),   # style charPr=0(휴먼) 통일, run charPr=7(맑은고딕) 유지 — 문단 합침 시 폰트 보존
        (6, "강조", "Emphasis", 6, 8),
        (7, "예비제목", "ReserveHeading", 7, 5),
        (8, "예비본문A", "ReserveBodyA", 8, 0),
        (9, "예비본문B", "ReserveBodyB", 9, 7),
        (10, "예비캡션", "ReserveCaption", 10, 7),
        (11, "예비강조", "ReserveEmphasis", 11, 8),
        (12, "머리말", "Header", int(HEADER_PARA_ID), int(HEADER_CHAR_ID)),
        (13, "꼬리말", "Footer", int(FOOTER_PARA_ID), int(FOOTER_CHAR_ID)),
        (14, "표제목", "TableTitle", int(TABLE_TITLE_PARA_ID), 7),
        (15, "표헤더", "TableHeader", int(TABLE_HEADER_PARA_ID), int(TABLE_HEADER_CHAR_ID)),
        (16, "표본문", "TableBody", int(TABLE_BODY_PARA_ID), int(TABLE_BODY_CHAR_ID)),
        (17, "요약본문", "SummaryBody", int(SUMMARY_BODY_PARA_ID), 7),
        (18, "요약설명", "SummaryDesc", int(SUMMARY_DESC_PARA_ID), int(TABLE_BODY_CHAR_ID)),
    ]
    for sid, name, eng, para_ref, char_ref in style_defs:
        add_style(sid, name, eng, para_ref, char_ref)
    styles.set("itemCnt", str(len(style_defs)))

    # compatibility / options (한글 구현 관행에 맞춤)
    compatible = ET.SubElement(head, _q("hh", "compatibleDocument"), {"targetProgram": "HWP201X"})
    ET.SubElement(compatible, _q("hh", "layoutCompatibility"))

    doc_option = ET.SubElement(head, _q("hh", "docOption"))
    ET.SubElement(
        doc_option,
        _q("hh", "linkinfo"),
        {"path": "", "pageInherit": "0", "footnoteInherit": "0"},
    )

    ET.SubElement(head, _q("hh", "trackchageConfig"), {"flags": "56"})

    return ET.tostring(head, encoding="utf-8", xml_declaration=True)


def build_section0_xml(blocks: List[Block], doc_meta: DocumentMetadata) -> bytes:
    """Build section0.xml with hs:sec root and content paragraphs.

    - 첫 부분에 머리말/꼬리말 컨트롤을 추가한다.
    - 본문 첫 실질 문단에는 페이지/섹션 설정을 위한 hp:secPr를 포함한다.
    """

    root = ET.Element(
        _q("hs", "sec"),
        {
            "xmlns:ha": NS["ha"],
            "xmlns:hp": NS["hp"],
            "xmlns:hp10": NS["hp10"],
            "xmlns:hs": NS["hs"],
            "xmlns:hc": NS["hc"],
            "xmlns:hh": NS["hh"],
            "xmlns:hhs": NS["hhs"],
            "xmlns:hm": NS["hm"],
            "xmlns:hpf": NS["hpf"],
            "xmlns:dc": NS["dc"],
            "xmlns:opf": NS["opf"],
            "xmlns:ooxmlchart": NS["ooxmlchart"],
            "xmlns:hwpunitchar": NS["hwpunitchar"],
            "xmlns:epub": NS["epub"],
            "xmlns:config": NS["config"],
        },
    )

    # 텍스트가 하나도 없으면 빈 문단 하나라도 만들어 둔다.
    text_blocks = [b for b in blocks if b.text]
    if not text_blocks:
        text_blocks = [Block(BlockType.PLAIN, "", "테스트입니다")]  # fallback

    # 본문 문단/테이블을 먼저 구성한 뒤, 마지막에 머리말/꼬리말 ctrl을 주입한다.
    p_id = 0
    secpr_attached = False
    table_id = 0

    # Option A flag (2025-11-16): paragraph layout/indent tweaks are deferred until
    # Tier1 parity testing proves stable. Do not modify the geometry logic below
    # without running the full validator loop on converter/sample_input.md.
    for block in text_blocks:
        if isinstance(block, TableBlock):
            p_id, table_id, secpr_attached = _append_markdown_table(
                root, block, table_id=table_id, p_id=p_id, secpr_attached=secpr_attached
            )
            continue
        if isinstance(block, SummaryTableBlock):
            p_id, table_id, secpr_attached = _append_summary_table(
                root, block, table_id=table_id, p_id=p_id, secpr_attached=secpr_attached
            )
            continue
        if isinstance(block, ProcessBlock):
            p_id, table_id, secpr_attached = _append_process_table(
                root, block, table_id=table_id, p_id=p_id, secpr_attached=secpr_attached
            )
            continue
        if isinstance(block, DiagramBlock):
            p_id, table_id, secpr_attached = _append_diagram_table(
                root, block, table_id=table_id, p_id=p_id, secpr_attached=secpr_attached
            )
            continue

        # 1) 필요하면 spacer 문단 추가
        spacer_char_id = SPACER_CHAR_MAP.get(block.type)
        if spacer_char_id is not None:
            spacer_marker = SPACER_MARKER_MAP.get(block.type, "↕↕")
            # spacer에도 뒤따르는 블록의 style/paraPr를 부여하여
            # 백스페이스로 합쳐질 때 글꼴이 초기화되지 않도록 한다.
            spacer_style_id = STYLE_ID_MAP.get(block.type, "0")
            spacer_para_id = PARA_STYLE_MAP.get(block.type, "0")
            p = ET.SubElement(
                root,
                _q("hp", "p"),
                {
                    "id": str(p_id),
                    "paraPrIDRef": spacer_para_id,
                    "styleIDRef": spacer_style_id,
                    "pageBreak": "0",
                    "columnBreak": "0",
                    "merged": "0",
                },
            )
            # spacer에는 secPr를 붙이지 않는다
            run_sp = ET.SubElement(p, _q("hp", "run"), {"charPrIDRef": spacer_char_id})
            t_sp = ET.SubElement(run_sp, _q("hp", "t"))
            t_sp.text = spacer_marker
            p_id += 1

        if block.type == BlockType.TITLE:
            p_id, table_id, secpr_attached = _append_title_table(
                root, block, table_id=table_id, p_id=p_id, secpr_attached=secpr_attached
            )
            continue
        if block.type == BlockType.EMPHASIS:
            p_id, table_id, secpr_attached = _append_emphasis_table(
                root, block, table_id=table_id, p_id=p_id, secpr_attached=secpr_attached
            )
            continue

        # 2) 실제 내용 문단
        para_id = PARA_STYLE_MAP.get(block.type, "0")
        style_id = STYLE_ID_MAP.get(block.type, "0")
        p = ET.SubElement(
            root,
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

        # 첫 실제 문단에만 secPr/페이지 설정 포함
        if not secpr_attached:
            char_id_for_sec = RUN_CHAR_OVERRIDE_MAP.get(block.type)
            run_sec_attrs = {}
            if char_id_for_sec is not None:
                run_sec_attrs["charPrIDRef"] = char_id_for_sec
            run_sec = ET.SubElement(p, _q("hp", "run"), run_sec_attrs)
            _attach_secpr(run_sec)
            secpr_attached = True

        # 실제 텍스트 run (inline bold 지원)
        char_id = RUN_CHAR_OVERRIDE_MAP.get(block.type)
        if block.type == BlockType.SUBTITLE:
            text_content = f"□ {block.text}"
        elif block.type == BlockType.BODY:
            text_content = f" ◦ {block.text}"
        elif block.type == BlockType.DESC2:
            text_content = f"   - {block.text}"
        elif block.type == BlockType.DESC3:
            text_content = f"    * {block.text}"
        elif block.type == BlockType.EMPHASIS:
            text_content = f"◈ {block.text}"
        else:
            text_content = block.text

        # 제목/소제목은 HY헤드라인M Bold charPr을 사용
        if block.type in (BlockType.TITLE, BlockType.SUBTITLE):
            _append_text_with_bold_custom(p, char_id, text_content, "32")
        else:
            _append_text_with_bold(p, char_id, text_content)

        p_id += 1

    # 머리말/꼬리말 텍스트를 만들고, 섹션 구조가 예상과 다르면 조용히 무시한다.
    try:
        header_text, footer_text = _build_header_footer_text(doc_meta)
        _append_header_footer_ctrl(root, header_text, footer_text)
    except Exception:
        pass

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_content_hpf(doc_meta: DocumentMetadata) -> bytes:
    """Build Contents/content.hpf (opf:package) with manifest and spine."""

    root = ET.Element(
        _q("opf", "package"),
        {
            "version": "",
            "unique-identifier": "",
            "id": "",
            "xmlns:ha": NS["ha"],
            "xmlns:hp": NS["hp"],
            "xmlns:hp10": NS["hp10"],
            "xmlns:hs": NS["hs"],
            "xmlns:hc": NS["hc"],
            "xmlns:hh": NS["hh"],
            "xmlns:hhs": NS["hhs"],
            "xmlns:hm": NS["hm"],
            "xmlns:hpf": NS["hpf"],
            "xmlns:hwpunitchar": NS["hwpunitchar"],
            "xmlns:ooxmlchart": NS["ooxmlchart"],
            "xmlns:dc": NS["dc"],
            "xmlns:epub": NS["epub"],
            "xmlns:config": NS["config"],
            "xmlns:ocf": NS["ocf"],
            "xmlns:rdf": NS["rdf"],
            "xmlns:pkg": NS["pkg"],
        },
    )

    # Metadata
    metadata_el = ET.SubElement(root, _q("opf", "metadata"))
    title_el = ET.SubElement(metadata_el, _q("opf", "title"))
    title_el.text = doc_meta.title or "Untitled"
    lang_el = ET.SubElement(metadata_el, _q("opf", "language"))
    lang_el.text = "ko"
    meta_entries = [
        ("creator", doc_meta.creator),
        ("subject", doc_meta.subject),
        ("description", doc_meta.description),
        ("lastsaveby", doc_meta.last_saved_by),
        ("CreatedDate", _isoformat_utc(doc_meta.created_at)),
        ("ModifiedDate", _isoformat_utc(doc_meta.modified_at)),
        ("date", doc_meta.display_date),
        ("keyword", doc_meta.keyword),
    ]
    for name, value in meta_entries:
        ET.SubElement(
            metadata_el,
            _q("opf", "meta"),
            {
                "name": name,
                "content": value or "",
            },
        )

    # Manifest - list all content files
    manifest = ET.SubElement(root, _q("opf", "manifest"))
    ET.SubElement(
        manifest,
        _q("opf", "item"),
        {"id": "header", "href": "Contents/header.xml", "media-type": "application/xml"},
    )
    ET.SubElement(
        manifest,
        _q("opf", "item"),
        {"id": "section0", "href": "Contents/section0.xml", "media-type": "application/xml"},
    )
    ET.SubElement(
        manifest,
        _q("opf", "item"),
        {"id": "settings", "href": "settings.xml", "media-type": "application/xml"},
    )

    # Spine - define reading order (required by Hangul)
    spine = ET.SubElement(root, _q("opf", "spine"))
    ET.SubElement(spine, _q("opf", "itemref"), {"idref": "header", "linear": "yes"})
    ET.SubElement(spine, _q("opf", "itemref"), {"idref": "section0", "linear": "no"})

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_container_xml() -> bytes:
    """Build META-INF/container.xml pointing to Contents/content.hpf and container.rdf.

    Based on test_inputmodel.hwpx structure.
    """

    root = ET.Element(_q("ocf", "container"))
    root.set("xmlns:hpf", NS["hpf"])
    rootfiles = ET.SubElement(root, _q("ocf", "rootfiles"))

    # Main content file
    ET.SubElement(
        rootfiles,
        _q("ocf", "rootfile"),
        {
            "full-path": "Contents/content.hpf",
            "media-type": "application/hwpml-package+xml",
        },
    )

    # Preview text for Hangul quick preview
    ET.SubElement(
        rootfiles,
        _q("ocf", "rootfile"),
        {
            "full-path": "Preview/PrvText.txt",
            "media-type": "text/plain",
        },
    )

    # RDF metadata (required by Hangul)
    ET.SubElement(
        rootfiles,
        _q("ocf", "rootfile"),
        {
            "full-path": "META-INF/container.rdf",
            "media-type": "application/rdf+xml",
        },
    )

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_version_xml() -> bytes:
    """Build version.xml (HCFVersion) with all required attributes.

    Based on test_inputmodel.hwpx structure.
    """

    hv_ns = "http://www.hancom.co.kr/hwpml/2011/version"
    root = ET.Element(
        f"{{{hv_ns}}}HCFVersion",
        {
            "tagetApplication": "WORDPROCESSOR",
            "major": "5",
            "minor": "1",
            "micro": "0",
            "buildNumber": "1",
            "os": "1",
            "xmlVersion": "1.4",
            "application": "Hancom Office Hangul",
            "appVersion": "11, 0, 0, 8808 WIN32LEWindows_10",
        },
    )
    root.set("xmlns:hv", hv_ns)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_settings_xml() -> bytes:
    """Build settings.xml with CaretPosition.

    Based on test_inputmodel.hwpx structure.
    """

    root = ET.Element(_q("ha", "HWPApplicationSetting"))
    root.set("xmlns:config", "urn:oasis:names:tc:opendocument:xmlns:config:1.0")

    # Add caret position (required by Hangul)
    ET.SubElement(
        root,
        _q("ha", "CaretPosition"),
        {"listIDRef": "0", "paraIDRef": "0", "pos": "0"},
    )

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_manifest_xml() -> bytes:
    """Build META-INF/manifest.xml (ODF manifest structure).

    Based on test_inputmodel.hwpx structure.
    Required by Hangul for package validation.
    """

    odf_ns = "urn:oasis:names:tc:opendocument:xmlns:manifest:1.0"
    root = ET.Element(f"{{{odf_ns}}}manifest")
    root.set("xmlns:odf", odf_ns)

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_container_rdf() -> bytes:
    """Build META-INF/container.rdf (RDF metadata linking document parts).

    Based on test_inputmodel.hwpx structure.
    Required by Hangul for proper document structure recognition.
    """

    root = ET.Element(_q("rdf", "RDF"))

    about_attr = {f"{{{NS['rdf']}}}about": ""}
    resource_header = {f"{{{NS['rdf']}}}resource": "Contents/header.xml"}
    resource_section = {f"{{{NS['rdf']}}}resource": "Contents/section0.xml"}

    desc_root = ET.SubElement(root, _q("rdf", "Description"), about_attr.copy())
    ET.SubElement(desc_root, _q("pkg", "hasPart"), resource_header.copy())

    desc_header = ET.SubElement(root, _q("rdf", "Description"), {f"{{{NS['rdf']}}}about": "Contents/header.xml"})
    ET.SubElement(desc_header, _q("rdf", "type"), {
        f"{{{NS['rdf']}}}resource": f"{NS['pkg']}HeaderFile"
    })

    desc_root_section = ET.SubElement(root, _q("rdf", "Description"), about_attr.copy())
    ET.SubElement(desc_root_section, _q("pkg", "hasPart"), resource_section.copy())

    desc_section = ET.SubElement(root, _q("rdf", "Description"), {f"{{{NS['rdf']}}}about": "Contents/section0.xml"})
    ET.SubElement(desc_section, _q("rdf", "type"), {
        f"{{{NS['rdf']}}}resource": f"{NS['pkg']}SectionFile"
    })

    desc_type = ET.SubElement(root, _q("rdf", "Description"), about_attr.copy())
    ET.SubElement(desc_type, _q("rdf", "type"), {
        f"{{{NS['rdf']}}}resource": f"{NS['pkg']}Document"
    })

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)
