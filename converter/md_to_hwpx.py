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
    BlockType.TITLE: "0",      # will later map to title paraPr
    BlockType.SUBTITLE: "0",
    BlockType.BODY: "0",
    BlockType.DESC2: "0",
    BlockType.DESC3: "0",
    BlockType.EMPHASIS: "0",
    BlockType.PLAIN: "0",
}

CHAR_STYLE_MAP = {
    BlockType.TITLE: "0",
    BlockType.SUBTITLE: "0",
    BlockType.BODY: "0",
    BlockType.DESC2: "0",
    BlockType.DESC3: "0",
    BlockType.EMPHASIS: "0",
    BlockType.PLAIN: "0",
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

    # fontfaces: HANGUL에 맑은 고딕 하나만 정의
    fontfaces = ET.SubElement(ref_list, _q("hh", "fontfaces"), {"itemCnt": "1"})
    ff_hangul = ET.SubElement(fontfaces, _q("hh", "fontface"), {"lang": "HANGUL", "fontCnt": "1"})
    font0 = ET.SubElement(
        ff_hangul,
        _q("hh", "font"),
        {"id": "0", "face": "맑은 고딕", "type": "TTF", "isEmbedded": "0"},
    )
    ET.SubElement(
        font0,
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

    # borderFills: 단순 기본 borderFill 하나
    border_fills = ET.SubElement(ref_list, _q("hh", "borderFills"), {"itemCnt": "1"})
    ET.SubElement(
        border_fills,
        _q("hh", "borderFill"),
        {
            "id": "1",
            "threeD": "0",
            "shadow": "0",
            "centerLine": "NONE",
            "breakCellSeparateLine": "0",
        },
    )

    # charProperties: 본문용 하나 (id 0), fontRef 0 사용
    char_props = ET.SubElement(ref_list, _q("hh", "charProperties"), {"itemCnt": "1"})
    char0 = ET.SubElement(
        char_props,
        _q("hh", "charPr"),
        {
            "id": "0",
            "height": "1000",
            "textColor": "#000000",
            "shadeColor": "none",
            "useFontSpace": "0",
            "useKerning": "0",
            "symMark": "NONE",
            "borderFillIDRef": "1",
        },
    )
    ET.SubElement(
        char0,
        _q("hh", "fontRef"),
        {"hangul": "0", "latin": "0", "hanja": "0", "japanese": "0", "other": "0", "symbol": "0", "user": "0"},
    )
    ET.SubElement(
        char0,
        _q("hh", "ratio"),
        {"hangul": "100", "latin": "100", "hanja": "100", "japanese": "100", "other": "100", "symbol": "100", "user": "100"},
    )
    ET.SubElement(
        char0,
        _q("hh", "spacing"),
        {"hangul": "0", "latin": "0", "hanja": "0", "japanese": "0", "other": "0", "symbol": "0", "user": "0"},
    )
    ET.SubElement(
        char0,
        _q("hh", "relSz"),
        {"hangul": "100", "latin": "100", "hanja": "100", "japanese": "100", "other": "100", "symbol": "100", "user": "100"},
    )
    ET.SubElement(
        char0,
        _q("hh", "offset"),
        {"hangul": "0", "latin": "0", "hanja": "0", "japanese": "0", "other": "0", "symbol": "0", "user": "0"},
    )
    ET.SubElement(
        char0,
        _q("hh", "underline"),
        {"type": "NONE", "shape": "SOLID", "color": "#000000"},
    )
    ET.SubElement(char0, _q("hh", "strikeout"), {"shape": "NONE", "color": "#000000"})
    ET.SubElement(char0, _q("hh", "outline"), {"type": "NONE"})
    ET.SubElement(
        char0,
        _q("hh", "shadow"),
        {"type": "NONE", "color": "#B2B2B2", "offsetX": "10", "offsetY": "10"},
    )

    # tabProperties: 기본 하나
    tab_props = ET.SubElement(ref_list, _q("hh", "tabProperties"), {"itemCnt": "1"})
    ET.SubElement(tab_props, _q("hh", "tabPr"), {"id": "0", "autoTabLeft": "0", "autoTabRight": "0"})

    # paraProperties: 기본 문단 하나 (id 0)
    para_props = ET.SubElement(ref_list, _q("hh", "paraProperties"), {"itemCnt": "1"})
    para0 = ET.SubElement(
        para_props,
        _q("hh", "paraPr"),
        {
            "id": "0",
            "tabPrIDRef": "0",
            "condense": "0",
            "fontLineHeight": "0",
            "snapToGrid": "1",
            "suppressLineNumbers": "0",
            "checked": "0",
        },
    )
    ET.SubElement(para0, _q("hh", "align"), {"horizontal": "JUSTIFY", "vertical": "BASELINE"})
    ET.SubElement(para0, _q("hh", "heading"), {"type": "NONE", "idRef": "0", "level": "0"})
    ET.SubElement(
        para0,
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
    ET.SubElement(para0, _q("hh", "autoSpacing"), {"eAsianEng": "0", "eAsianNum": "0"})
    # margin + lineSpacing: 기본 160% 한 줄 간격
    margin = ET.SubElement(para0, _q("hh", "margin"))
    ET.SubElement(margin, _q("hc", "intent"), {"value": "0", "unit": "HWPUNIT"})
    ET.SubElement(margin, _q("hc", "left"), {"value": "0", "unit": "HWPUNIT"})
    ET.SubElement(margin, _q("hc", "right"), {"value": "0", "unit": "HWPUNIT"})
    ET.SubElement(margin, _q("hc", "prev"), {"value": "0", "unit": "HWPUNIT"})
    ET.SubElement(margin, _q("hc", "next"), {"value": "0", "unit": "HWPUNIT"})
    ET.SubElement(para0, _q("hh", "lineSpacing"), {"type": "PERCENT", "value": "160", "unit": "HWPUNIT"})
    ET.SubElement(
        para0,
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

    # styles: 바탕글 하나 (id 0)
    styles = ET.SubElement(ref_list, _q("hh", "styles"), {"itemCnt": "1"})
    ET.SubElement(
        styles,
        _q("hh", "style"),
        {
            "id": "0",
            "type": "PARA",
            "name": "바탕글",
            "engName": "Normal",
            "paraPrIDRef": "0",
            "charPrIDRef": "0",
            "nextStyleIDRef": "0",
            "langID": "1042",
            "lockForm": "0",
        },
    )

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

    for idx, block in enumerate(text_blocks):
        para_id = PARA_STYLE_MAP.get(block.type, "0")
        p = ET.SubElement(
            root,
            _q("hp", "p"),
            {
                "id": str(idx),
                "paraPrIDRef": para_id,
                "styleIDRef": "0",
                "pageBreak": "0",
                "columnBreak": "0",
                "merged": "0",
            },
        )

        # 첫 문단에만 secPr/페이지 설정 포함
        if idx == 0:
            char_id_for_sec = CHAR_STYLE_MAP.get(block.type, "0")
            run_sec = ET.SubElement(p, _q("hp", "run"), {"charPrIDRef": char_id_for_sec})
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
            ET.SubElement(
                page_pr,
                _q("hp", "margin"),
                {
                    "header": "4252",
                    "footer": "4252",
                    "gutter": "0",
                    "left": "8504",
                    "right": "8504",
                    "top": "5668",
                    "bottom": "4252",
                },
            )

        # 실제 텍스트 run
        char_id = CHAR_STYLE_MAP.get(block.type, "0")
        run = ET.SubElement(p, _q("hp", "run"), {"charPrIDRef": char_id})
        t = ET.SubElement(run, _q("hp", "t"))
        t.text = block.text

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_content_hpf(title: str) -> bytes:
    """Build minimal Contents/content.hpf (opf:package)."""

    root = ET.Element(
        _q("opf", "package"),
        {
            "version": "",
            "unique-identifier": "",
            "id": "",
        },
    )

    metadata = ET.SubElement(root, _q("opf", "metadata"))
    title_el = ET.SubElement(metadata, _q("opf", "title"))
    title_el.text = title or "Untitled"
    lang_el = ET.SubElement(metadata, _q("opf", "language"))
    lang_el.text = "ko"

    manifest = ET.SubElement(root, _q("opf", "manifest"))
    ET.SubElement(
        manifest,
        _q("opf", "item"),
        {"id": "section0", "href": "Contents/section0.xml", "media-type": "application/xml"},
    )

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_container_xml() -> bytes:
    """Build META-INF/container.xml pointing to Contents/content.hpf."""

    root = ET.Element(_q("ocf", "container"))
    root.set("xmlns:hpf", NS["hpf"])
    rootfiles = ET.SubElement(root, _q("ocf", "rootfiles"))
    ET.SubElement(
        rootfiles,
        _q("ocf", "rootfile"),
        {
            "full-path": "Contents/content.hpf",
            "media-type": "application/hwpml-package+xml",
        },
    )
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_version_xml() -> bytes:
    """Build a minimal version.xml (HCFVersion)."""

    hv_ns = "http://www.hancom.co.kr/hwpml/2011/version"
    root = ET.Element(
        f"{{{hv_ns}}}HCFVersion",
        {
            "tagetApplication": "WORDPROCESSOR",
            "major": "5",
            "minor": "0",
        },
    )
    root.set("xmlns:hv", hv_ns)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def build_settings_xml() -> bytes:
    """Build a minimal settings.xml stub.

    For now, we generate a tiny valid shell; details can be filled later
    if Hangul requires them for advanced behavior.
    """

    root = ET.Element(_q("ha", "HWPApplicationSetting"))
    root.set("xmlns:config", "urn:oasis:names:tc:opendocument:xmlns:config:1.0")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


# ---------------------------------------------------------------------------
# Writing .hwpx container (realistic minimal package)
# ---------------------------------------------------------------------------


def write_hwpx(blocks: List[Block], output_path: Path) -> None:
    """Write a minimal but more realistic HWPX (ZIP) container.

    Files we include:
    - mimetype
    - version.xml
    - settings.xml
    - META-INF/container.xml
    - Contents/content.hpf
    - Contents/section0.xml
    """

    output_path = output_path.with_suffix(".hwpx")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    section0_bytes = build_section0_xml(blocks)
    content_hpf_bytes = build_content_hpf(title=blocks[0].text if blocks else "")
    container_bytes = build_container_xml()
    version_bytes = build_version_xml()
    settings_bytes = build_settings_xml()
    header_bytes = build_header_xml()

    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("mimetype", "application/haansofthwp")
        zf.writestr("version.xml", version_bytes)
        zf.writestr("settings.xml", settings_bytes)
        zf.writestr("META-INF/container.xml", container_bytes)
        zf.writestr("Contents/content.hpf", content_hpf_bytes)
        zf.writestr("Contents/section0.xml", section0_bytes)
        zf.writestr("Contents/header.xml", header_bytes)


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
