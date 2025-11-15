#!/usr/bin/env python3
"""Phase1: Minimal MD → HWPX converter skeleton.

Goal (MVP):
- Read `sample_input.md`-style markdown.
- Parse lines into typed blocks (TITLE, SUBTITLE, BODY, DESC2, DESC3, EMPHASIS, PLAIN).
- Build an in-memory HWPX-like XML tree (single section, simple run/para structure).
- Save to `.hwpx` file (ZIP container with minimal XMLs).

NOTE:
- This is a skeleton: XML structure is intentionally simple and will be
  refined against the HWPX spec using `tools/spec_search.py`.
- For now we only guarantee that the output is a well-formed ZIP+XML file.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
from typing import Iterable, List
import argparse
import zipfile
import xml.etree.ElementTree as ET

# ---------------------------------------------------------------------------
# Data model for parsed markdown
# ---------------------------------------------------------------------------


class BlockType(Enum):
    TITLE = auto()       # <주제목>
    SUBTITLE = auto()    # □
    BODY = auto()        # ◦
    DESC2 = auto()       # - (3 spaces)
    DESC3 = auto()       # * (4 spaces)
    EMPHASIS = auto()    # <강조>
    PLAIN = auto()       # fallback / other


@dataclass
class Block:
    type: BlockType
    raw: str            # original line
    text: str           # content without leading markers


# ---------------------------------------------------------------------------
# Style mapping layer (logical BlockType → paraPr/charPr IDs)
# ---------------------------------------------------------------------------


# NOTE:
# - IDs here MUST correspond to definitions in header.xml.
# - For now header.xml only defines paraPr id="0" and charPr id="0".
# - We still keep the mapping table so that later we can extend header.xml
#   and just update these maps without touching the rest of the code.

PARA_STYLE_MAP = {
    # NOTE: IDs must match paraPr definitions in header.xml
    BlockType.TITLE: "1",
    BlockType.SUBTITLE: "2",
    BlockType.BODY: "3",
    BlockType.DESC2: "4",
    BlockType.DESC3: "5",
    BlockType.EMPHASIS: "6",
    BlockType.PLAIN: "0",
}

# Hangul only honors run-level charPr IDs ≤8 when the paragraph shares the 바탕글
# paraPr. Keep explicit IDs for each logical block so we never emit 9+; spacer runs
# still use 1~4 via SPACER_CHAR_MAP.
RUN_CHAR_OVERRIDE_MAP = {
    BlockType.TITLE: "5",
    BlockType.SUBTITLE: "6",
    BlockType.BODY: "0",
    BlockType.DESC2: "0",
    BlockType.DESC3: "7",
    BlockType.EMPHASIS: "8",
    BlockType.PLAIN: "0",
}

# StyleID mapping (p@styleIDRef → hh:style@id in header.xml)
STYLE_ID_MAP = {
    BlockType.TITLE: "1",
    BlockType.SUBTITLE: "2",
    BlockType.BODY: "3",
    BlockType.DESC2: "4",
    BlockType.DESC3: "5",
    BlockType.EMPHASIS: "6",
    BlockType.PLAIN: "0",
}

# Spacer paragraph mapping: certain BlockType 앞에 여백용 문단 삽입
SPACER_CHAR_MAP = {
    # 휴먼명조 계열 spacer (test_inputmodel 기반)
    # NOTE: spacer charPr IDs intentionally kept in 1~4 so Hangul honors their heights
    BlockType.SUBTITLE: "1",   # 10pt
    BlockType.BODY: "2",      # 8pt
    BlockType.DESC2: "3",     # 6pt
    BlockType.DESC3: "4",     # 4pt
}

# Spacer marker text: ↕(size)↕ so later manual/auto replace is easy
SPACER_MARKER_MAP = {
    BlockType.SUBTITLE: "↕10↕",
    BlockType.BODY: "↕8↕",
    BlockType.DESC2: "↕6↕",
    BlockType.DESC3: "↕4↕",
}


# ---------------------------------------------------------------------------
# Parsing `sample_input.md`-style markdown into blocks
# ---------------------------------------------------------------------------


def parse_md_lines(lines: Iterable[str]) -> List[Block]:
    blocks: List[Block] = []

    for line in lines:
        # Preserve original line, but strip trailing newline for processing
        original = line.rstrip("\n")
        stripped = original.lstrip(" ")
        leading_spaces = len(original) - len(stripped)

        if not stripped:
            # Empty line → we can keep as PLAIN (or skip). For now keep.
            blocks.append(Block(BlockType.PLAIN, original, ""))
            continue

        # Title: <주제목> 텍스트
        if stripped.startswith("<주제목>"):
            text = stripped[len("<주제목>") :].strip()
            blocks.append(Block(BlockType.TITLE, original, text))
            continue

        # Emphasis: <강조> 텍스트
        if stripped.startswith("<강조>"):
            text = stripped[len("<강조>") :].strip()
            blocks.append(Block(BlockType.EMPHASIS, original, text))
            continue

        # Subtitle: starts with □ (no strict space requirement, rely on char)
        if stripped.startswith("□"):
            text = stripped[len("□") :].strip()
            blocks.append(Block(BlockType.SUBTITLE, original, text))
            continue

        # Body: one leading space then ◦
        if leading_spaces == 1 and stripped.startswith("◦"):
            text = stripped[len("◦") :].strip()
            blocks.append(Block(BlockType.BODY, original, text))
            continue

        # Desc2: three spaces then -
        if leading_spaces == 3 and stripped.startswith("-"):
            text = stripped[len("-") :].strip()
            blocks.append(Block(BlockType.DESC2, original, text))
            continue

        # Desc3: four spaces then *
        if leading_spaces == 4 and stripped.startswith("*"):
            text = stripped[len("*") :].strip()
            blocks.append(Block(BlockType.DESC3, original, text))
            continue

        # Fallback: plain text
        blocks.append(Block(BlockType.PLAIN, original, stripped))

    return blocks


NS = {
    "ha": "http://www.hancom.co.kr/hwpml/2011/app",
    "hp": "http://www.hancom.co.kr/hwpml/2011/paragraph",
    "hs": "http://www.hancom.co.kr/hwpml/2011/section",
    "hc": "http://www.hancom.co.kr/hwpml/2011/core",
    "hh": "http://www.hancom.co.kr/hwpml/2011/head",
    "hhs": "http://www.hancom.co.kr/hwpml/2011/history",
    "hm": "http://www.hancom.co.kr/hwpml/2011/master-page",
    "hpf": "http://www.hancom.co.kr/schema/2011/hpf",
    "dc": "http://purl.org/dc/elements/1.1/",
    "opf": "http://www.idpf.org/2007/opf/",
    "ocf": "urn:oasis:names:tc:opendocument:xmlns:container",
}

# Register all namespace prefixes to avoid ns0, ns1, etc.
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

# Additional namespaces
ET.register_namespace("hv", "http://www.hancom.co.kr/hwpml/2011/version")
ET.register_namespace("odf", "urn:oasis:names:tc:opendocument:xmlns:manifest:1.0")
ET.register_namespace("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
ET.register_namespace("config", "urn:oasis:names:tc:opendocument:xmlns:config:1.0")


def _q(prefix: str, tag: str) -> str:
    """Qualified tag helper: _q("hp", "p") → '{ns}p'."""

    return f"{{{NS[prefix]}}}{tag}"


# ---------------------------------------------------------------------------
# Minimal HWPX XML builders (header.xml, section0.xml, content.hpf, container)
# ---------------------------------------------------------------------------


def build_header_xml() -> bytes:
    """Build a minimal header.xml similar to test_minimal_manual.hwpx.

    이 버전은 "테스트입니다" 한 줄 출력에 필요한 정도로만 축소한 헤더입니다.
    - fontfaces: 맑은 고딕 하나만 실질적으로 사용 (id 0)
    - charPr: 본문용 하나 (id 0)
    - paraPr: 기본 문단 하나 (id 0)
    - style: 바탕글 하나 (id 0)
    """

    head = ET.Element(
        _q("hh", "head"),
        {
            "version": "1.4",
            "secCnt": "1",
            "xmlns:ha": NS["ha"],
            "xmlns:hp": NS["hp"],
            "xmlns:hs": NS["hs"],
            "xmlns:hc": NS["hc"],
            "xmlns:hh": NS["hh"],
            "xmlns:hhs": NS["hhs"],
            "xmlns:hm": NS["hm"],
            "xmlns:hpf": NS["hpf"],
            "xmlns:dc": NS["dc"],
            "xmlns:opf": NS["opf"],
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

    # borderFills: 최소 2개 필요 (참조 파일 기준)
    border_fills = ET.SubElement(ref_list, _q("hh", "borderFills"), {"itemCnt": "2"})

    # borderFill id="1" - 기본
    bf1 = ET.SubElement(border_fills, _q("hh", "borderFill"), {
        "id": "1",
        "threeD": "0",
        "shadow": "0",
        "centerLine": "NONE",
        "breakCellSeparateLine": "0",
    })
    ET.SubElement(bf1, _q("hh", "slash"), {"type": "NONE", "Crooked": "0", "isCounter": "0"})
    ET.SubElement(bf1, _q("hh", "backSlash"), {"type": "NONE", "Crooked": "0", "isCounter": "0"})
    ET.SubElement(bf1, _q("hh", "leftBorder"), {"type": "NONE", "width": "0.1 mm", "color": "#000000"})
    ET.SubElement(bf1, _q("hh", "rightBorder"), {"type": "NONE", "width": "0.1 mm", "color": "#000000"})
    ET.SubElement(bf1, _q("hh", "topBorder"), {"type": "NONE", "width": "0.1 mm", "color": "#000000"})
    ET.SubElement(bf1, _q("hh", "bottomBorder"), {"type": "NONE", "width": "0.1 mm", "color": "#000000"})
    ET.SubElement(bf1, _q("hh", "diagonal"), {"type": "SOLID", "width": "0.1 mm", "color": "#000000"})

    # borderFill id="2" - fillBrush 포함
    bf2 = ET.SubElement(border_fills, _q("hh", "borderFill"), {
        "id": "2",
        "threeD": "0",
        "shadow": "0",
        "centerLine": "NONE",
        "breakCellSeparateLine": "0",
    })
    ET.SubElement(bf2, _q("hh", "slash"), {"type": "NONE", "Crooked": "0", "isCounter": "0"})
    ET.SubElement(bf2, _q("hh", "backSlash"), {"type": "NONE", "Crooked": "0", "isCounter": "0"})
    ET.SubElement(bf2, _q("hh", "leftBorder"), {"type": "NONE", "width": "0.1 mm", "color": "#000000"})
    ET.SubElement(bf2, _q("hh", "rightBorder"), {"type": "NONE", "width": "0.1 mm", "color": "#000000"})
    ET.SubElement(bf2, _q("hh", "topBorder"), {"type": "NONE", "width": "0.1 mm", "color": "#000000"})
    ET.SubElement(bf2, _q("hh", "bottomBorder"), {"type": "NONE", "width": "0.1 mm", "color": "#000000"})
    ET.SubElement(bf2, _q("hh", "diagonal"), {"type": "SOLID", "width": "0.1 mm", "color": "#000000"})
    fillBrush = ET.SubElement(bf2, _q("hc", "fillBrush"))
    ET.SubElement(fillBrush, _q("hc", "winBrush"), {"faceColor": "none", "hatchColor": "#999999", "alpha": "0"})

    # charProperties: 글자 모양 정의 (style_textbook 기준)
    char_props = ET.SubElement(ref_list, _q("hh", "charProperties"), {"itemCnt": "0"})

    def add_char_pr(char_id: int, height: int, hangul_font_id: int, *, bold: bool = False) -> None:
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
        ET.SubElement(
            char,
            _q("hh", "spacing"),
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

    char_defs = [
        # Base/body text (휴먼명조 15pt) lives at ID 0 so the 바탕글 fallback is safe.
        (0, 1500, 1, False),
        # Spacer charPr (line-height 확보용, Hangul-safe IDs 1~4)
        (1, 1000, 2, False),   # 소제목 spacer 맑은고딕 10pt
        (2, 800, 2, False),    # 본문 spacer 맑은고딕 8pt
        (3, 600, 2, False),    # 설명2 spacer 맑은고딕 6pt
        (4, 400, 2, False),    # 설명3 spacer 맑은고딕 4pt
        # 본문 계열 스타일 (ID ≤ 8만 사용)
        (5, 1500, 0, True),    # 주제목 HY 15pt Bold
        (6, 1500, 0, False),   # 소제목 HY 15pt
        (7, 1200, 2, False),   # 설명3 맑은고딕 12pt
        (8, 1500, 1, True),    # 강조 휴먼 15pt Bold
    ]
    for cid, height, font_id, is_bold in char_defs:
        add_char_pr(cid, height, font_id, bold=is_bold)
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
        ET.SubElement(margin_el, _q("hc", "intent"), {"value": "0", "unit": "HWPUNIT"})
        ET.SubElement(margin_el, _q("hc", "left"), {"value": "0", "unit": "HWPUNIT"})
        ET.SubElement(margin_el, _q("hc", "right"), {"value": "0", "unit": "HWPUNIT"})
        ET.SubElement(margin_el, _q("hc", "prev"), {"value": "0", "unit": "HWPUNIT"})
        ET.SubElement(margin_el, _q("hc", "next"), {"value": "0", "unit": "HWPUNIT"})
        ET.SubElement(
            para,
            _q("hh", "lineSpacing"),
            {"type": "PERCENT", "value": str(line_spacing_value), "unit": "PERCENT"},
        )
        ET.SubElement(
            para,
            _q("hh", "border"),
            {
                "borderFillIDRef": "1",
                "offsetLeft": "0",
                "offsetRight": "0",
                "offsetTop": "0",
                "offsetBottom": "0",
                "connect": "0",
                "ignoreMargin": "0",
            },
        )

    para_defs = [
        (0, "JUSTIFY", 100, {"font_line_height": "1", "snap_to_grid": "0"}),
        (1, "CENTER", 130, {}),
        (2, "LEFT", 160, {}),
        (3, "LEFT", 160, {}),
        (4, "LEFT", 160, {}),
        (5, "LEFT", 160, {}),
        (6, "CENTER", 130, {}),
        # 예비 paraPr 5종 (Option A 대비)
        (7, "LEFT", 150, {"font_line_height": "0", "snap_to_grid": "1"}),
        (8, "LEFT", 140, {"font_line_height": "0", "snap_to_grid": "1"}),
        (9, "JUSTIFY", 130, {"font_line_height": "0", "snap_to_grid": "0"}),
        (10, "CENTER", 120, {"font_line_height": "0", "snap_to_grid": "1"}),
        (11, "LEFT", 135, {"font_line_height": "0", "snap_to_grid": "1"}),
    ]
    for pid, align, spacing, extra in para_defs:
        add_para_pr(
            pid,
            align,
            spacing,
            font_line_height=extra.get("font_line_height", "0"),
            snap_to_grid=extra.get("snap_to_grid", "1"),
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
        (3, "본문", "Body", 3, 0),
        (4, "설명2", "Desc2", 4, 0),
        (5, "설명3", "Desc3", 5, 7),
        (6, "강조", "Emphasis", 6, 8),
        (7, "예비제목", "ReserveHeading", 7, 5),
        (8, "예비본문A", "ReserveBodyA", 8, 0),
        (9, "예비본문B", "ReserveBodyB", 9, 7),
        (10, "예비캡션", "ReserveCaption", 10, 7),
        (11, "예비강조", "ReserveEmphasis", 11, 8),
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


def build_section0_xml(blocks: List[Block]) -> bytes:
    """Build section0.xml with hs:sec root and one or more hp:p.

    - paraPrIDRef="0", styleIDRef="0" → header.xml의 paraPr/style과 연결
    - charPrIDRef="0" → header.xml의 charPr과 연결
    - 첫 문단에는 페이지/섹션 설정을 위한 hp:secPr를 포함 (test_minimal_manual 패턴 차용)
    """

    root = ET.Element(
        _q("hs", "sec"),
        {
            "xmlns:ha": NS["ha"],
            "xmlns:hp": NS["hp"],
            "xmlns:hs": NS["hs"],
            "xmlns:hc": NS["hc"],
            "xmlns:hh": NS["hh"],
            "xmlns:hhs": NS["hhs"],
            "xmlns:hm": NS["hm"],
            "xmlns:hpf": NS["hpf"],
            "xmlns:dc": NS["dc"],
            "xmlns:opf": NS["opf"],
        },
    )

    # 텍스트가 하나도 없으면 빈 문단 하나라도 만들어 둔다.
    text_blocks = [b for b in blocks if b.text]
    if not text_blocks:
        text_blocks = [Block(BlockType.PLAIN, "", "테스트입니다")]  # fallback

    p_id = 0
    secpr_attached = False

    for block in text_blocks:
        # 1) 필요하면 spacer 문단 추가
        spacer_char_id = SPACER_CHAR_MAP.get(block.type)
        if spacer_char_id is not None:
            spacer_marker = SPACER_MARKER_MAP.get(block.type, "↕↕")
            p = ET.SubElement(
                root,
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
            # spacer에는 secPr를 붙이지 않는다
            run_sp = ET.SubElement(p, _q("hp", "run"), {"charPrIDRef": spacer_char_id})
            t_sp = ET.SubElement(run_sp, _q("hp", "t"))
            t_sp.text = spacer_marker
            p_id += 1

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
            sec_pr = ET.SubElement(
                run_sec,
                _q("hp", "secPr"),
                {
                    "id": "",
                    "textDirection": "HORIZONTAL",
                    "spaceColumns": "1134",
                    "tabStop": "8000",
                    "tabStopVal": "4000",
                    "tabStopUnit": "HWPUNIT",
                    "outlineShapeIDRef": "1",
                    "memoShapeIDRef": "0",
                    "textVerticalWidthHead": "0",
                    "masterPageCnt": "0",
                },
            )
            ET.SubElement(sec_pr, _q("hp", "grid"), {"lineGrid": "0", "charGrid": "0", "wonggojiFormat": "0"})
            ET.SubElement(
                sec_pr,
                _q("hp", "startNum"),
                {"pageStartsOn": "BOTH", "page": "0", "pic": "0", "tbl": "0", "equation": "0"},
            )
            ET.SubElement(
                sec_pr,
                _q("hp", "visibility"),
                {
                    "hideFirstHeader": "0",
                    "hideFirstFooter": "0",
                    "hideFirstMasterPage": "0",
                    "border": "SHOW_ALL",
                    "fill": "SHOW_ALL",
                    "hideFirstPageNum": "0",
                    "hideFirstEmptyLine": "0",
                    "showLineNumber": "0",
                },
            )
            ET.SubElement(
                sec_pr,
                _q("hp", "lineNumberShape"),
                {"restartType": "0", "countBy": "0", "distance": "0", "startNumber": "0"},
            )
            page_pr = ET.SubElement(
                sec_pr,
                _q("hp", "pagePr"),
                {"landscape": "WIDELY", "width": "59528", "height": "84186", "gutterType": "LEFT_ONLY"},
            )
            # 페이지 여백: PHASE1_INPUT_FORMAT (A4, 위/아래 15mm, 좌/우 20mm, 머리말/꼬리말 10mm)
            # test_inputmodel.hwpx의 수치를 그대로 사용
            ET.SubElement(
                page_pr,
                _q("hp", "margin"),
                {
                    "header": "2834",
                    "footer": "2834",
                    "gutter": "0",
                    "left": "5669",
                    "right": "5669",
                    "top": "4251",
                    "bottom": "4252",
                },
            )
            secpr_attached = True

        # 실제 텍스트 run
        char_id = RUN_CHAR_OVERRIDE_MAP.get(block.type)
        run_attrs = {}
        if char_id is not None:
            run_attrs["charPrIDRef"] = char_id
        run = ET.SubElement(p, _q("hp", "run"), run_attrs)
        t = ET.SubElement(run, _q("hp", "t"))

        # BlockType에 따라 머리 기호 복원
        if block.type == BlockType.SUBTITLE:
            t.text = f"□ {block.text}"
        elif block.type == BlockType.BODY:
            t.text = f"◦ {block.text}"
        elif block.type == BlockType.DESC2:
            t.text = f"   - {block.text}"
        elif block.type == BlockType.DESC3:
            t.text = f"    * {block.text}"
        elif block.type == BlockType.EMPHASIS:
            t.text = f"◈ {block.text}"
        else:
            t.text = block.text

        p_id += 1

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_content_hpf(title: str) -> bytes:
    """Build Contents/content.hpf (opf:package) with manifest and spine.

    Based on test_inputmodel.hwpx structure.
    """

    root = ET.Element(
        _q("opf", "package"),
        {
            "version": "",
            "unique-identifier": "",
            "id": "",
        },
    )

    # Add all necessary namespaces
    for prefix, uri in NS.items():
        root.set(f"xmlns:{prefix}", uri)

    # Metadata
    metadata = ET.SubElement(root, _q("opf", "metadata"))
    title_el = ET.SubElement(metadata, _q("opf", "title"))
    title_el.text = title or "Untitled"
    lang_el = ET.SubElement(metadata, _q("opf", "language"))
    lang_el.text = "ko"

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
    ET.SubElement(spine, _q("opf", "itemref"), {"idref": "section0", "linear": "yes"})

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

    rdf_ns = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    pkg_ns = "http://www.hancom.co.kr/hwpml/2016/meta/pkg#"

    root = ET.Element(f"{{{rdf_ns}}}RDF")
    root.set("xmlns:rdf", rdf_ns)

    # Document root description
    desc_root = ET.SubElement(root, f"{{{rdf_ns}}}Description", {"rdf:about": ""})
    ET.SubElement(desc_root, f"{{{pkg_ns}}}hasPart", {
        "xmlns:ns0": pkg_ns,
        "rdf:resource": "Contents/header.xml"
    })

    # Header file description
    desc_header = ET.SubElement(root, f"{{{rdf_ns}}}Description", {"rdf:about": "Contents/header.xml"})
    ET.SubElement(desc_header, f"{{{rdf_ns}}}type", {
        "rdf:resource": f"{pkg_ns}HeaderFile"
    })

    # Document root has section
    desc_root2 = ET.SubElement(root, f"{{{rdf_ns}}}Description", {"rdf:about": ""})
    ET.SubElement(desc_root2, f"{{{pkg_ns}}}hasPart", {
        "xmlns:ns0": pkg_ns,
        "rdf:resource": "Contents/section0.xml"
    })

    # Section file description
    desc_section = ET.SubElement(root, f"{{{rdf_ns}}}Description", {"rdf:about": "Contents/section0.xml"})
    ET.SubElement(desc_section, f"{{{rdf_ns}}}type", {
        "rdf:resource": f"{pkg_ns}SectionFile"
    })

    # Document type description
    desc_type = ET.SubElement(root, f"{{{rdf_ns}}}Description", {"rdf:about": ""})
    ET.SubElement(desc_type, f"{{{rdf_ns}}}type", {
        "rdf:resource": f"{pkg_ns}Document"
    })

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


# ---------------------------------------------------------------------------
# Writing .hwpx container (realistic minimal package)
# ---------------------------------------------------------------------------


def write_hwpx(blocks: List[Block], output_path: Path) -> None:
    """Write a complete HWPX (ZIP) container with all required files.

    Files included (based on test_inputmodel.hwpx structure):
    - mimetype
    - version.xml
    - settings.xml
    - META-INF/manifest.xml (NEW - required)
    - META-INF/container.xml
    - META-INF/container.rdf (NEW - required)
    - Contents/header.xml
    - Contents/section0.xml
    - Contents/content.hpf
    """

    output_path = output_path.with_suffix(".hwpx")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Build all XML files
    header_bytes = build_header_xml()
    section0_bytes = build_section0_xml(blocks)
    content_hpf_bytes = build_content_hpf(title=blocks[0].text if blocks else "")
    container_bytes = build_container_xml()
    container_rdf_bytes = build_container_rdf()
    manifest_bytes = build_manifest_xml()
    version_bytes = build_version_xml()
    settings_bytes = build_settings_xml()

    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        # mimetype must be first and uncompressed (per OCF spec)
        zf.writestr("mimetype", "application/hwp+zip", compress_type=zipfile.ZIP_STORED)

        # Version and settings
        zf.writestr("version.xml", version_bytes)
        zf.writestr("settings.xml", settings_bytes)

        # META-INF files (all required)
        zf.writestr("META-INF/manifest.xml", manifest_bytes)
        zf.writestr("META-INF/container.xml", container_bytes)
        zf.writestr("META-INF/container.rdf", container_rdf_bytes)

        # Contents files
        zf.writestr("Contents/header.xml", header_bytes)
        zf.writestr("Contents/section0.xml", section0_bytes)
        zf.writestr("Contents/content.hpf", content_hpf_bytes)


# ---------------------------------------------------------------------------
# High-level conversion API & CLI entrypoint
# ---------------------------------------------------------------------------


def convert_md_to_hwpx(input_md_path: Path, output_hwpx_path: Path) -> None:
    lines = input_md_path.read_text(encoding="utf-8").splitlines(True)
    blocks = parse_md_lines(lines)
    write_hwpx(blocks, output_hwpx_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Phase1 MD → HWPX converter (skeleton)")
    parser.add_argument("input_md", type=Path, help="Input markdown file (e.g., converter/sample_input.md)")
    parser.add_argument("output_hwpx", type=Path, help="Output HWPX file path (without .hwpx suffix also ok)")
    args = parser.parse_args()

    convert_md_to_hwpx(args.input_md, args.output_hwpx)
    print(f"[ok] Converted {args.input_md} → {args.output_hwpx.with_suffix('.hwpx')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
