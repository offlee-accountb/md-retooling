"""MD → HWPX 변환기 설정/상수.

YAML 기반 스타일 로딩, BlockType → 스타일 ID 매핑,
HWPX 치수 상수, NS/네임스페이스, _q 헬퍼.
"""
from __future__ import annotations

import sys
from pathlib import Path
import xml.etree.ElementTree as ET

from converter.models import BlockType

# Ensure project root is in sys.path
_PROJECT_ROOT = str(Path(__file__).parent.parent)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from validator.template_loader import load_style_config, StyleConfig


# ---------------------------------------------------------------------------
# Load style configuration (YAML-based)
# ---------------------------------------------------------------------------

_DEFAULT_STYLE_PATH = Path(__file__).parent.parent / "templates" / "core_styles.yaml"


def _load_config() -> StyleConfig:
    """Load style configuration from YAML."""
    if _DEFAULT_STYLE_PATH.exists():
        return load_style_config(_DEFAULT_STYLE_PATH)
    from validator.template_loader import StyleConfig
    return StyleConfig(version="1.0", template_id="fallback", description="Hardcoded fallback")


CONFIG: StyleConfig = _load_config()


# ---------------------------------------------------------------------------
# Style mapping layer (logical BlockType → paraPr/charPr IDs)
# ---------------------------------------------------------------------------


def _build_style_maps() -> tuple:
    """CONFIG에서 PARA_STYLE_MAP, RUN_CHAR_OVERRIDE_MAP, STYLE_ID_MAP 생성.

    **스타일 통일 전략**:
    일반 텍스트 문단(SUBTITLE, BODY, DESC2, DESC3, PLAIN)은 모두 BODY의
    styleIDRef / paraPrIDRef를 공유한다.
    TITLE과 EMPHASIS는 표 안에서 렌더링되므로 별도 styleIDRef 유지 가능.
    시각적 차이(폰트, 크기)는 charPrIDRef(run 레벨)로만 제어한다.
    """
    block_to_yaml = {
        BlockType.TITLE: "title",
        BlockType.SUBTITLE: "subtitle",
        BlockType.BODY: "body",
        BlockType.DESC2: "desc2",
        BlockType.DESC3: "desc3",
        BlockType.EMPHASIS: "emphasis",
        BlockType.PLAIN: "plain",
    }

    para_map = {}
    char_map = {}
    style_map = {}

    for block_type, yaml_key in block_to_yaml.items():
        style = CONFIG.get_style(yaml_key)
        if style:
            para_map[block_type] = str(style.para_pr_id)
            char_map[block_type] = str(style.char_pr_id)
            style_map[block_type] = str(style.style_id)
        else:
            para_map[block_type] = "0"
            char_map[block_type] = "0"
            style_map[block_type] = "0"

    # 스타일 통일: 일반 텍스트 문단은 BODY 기준으로 통일
    body_style = CONFIG.get_style("body")
    if body_style:
        unified_style_id = str(body_style.style_id)
        unified_para_id = str(body_style.para_pr_id)
        for bt in (BlockType.SUBTITLE, BlockType.BODY, BlockType.DESC2,
                    BlockType.DESC3, BlockType.PLAIN):
            style_map[bt] = unified_style_id
            para_map[bt] = unified_para_id

    return para_map, char_map, style_map


PARA_STYLE_MAP, RUN_CHAR_OVERRIDE_MAP, STYLE_ID_MAP = _build_style_maps()

INLINE_BOLD_CHAR_ID = RUN_CHAR_OVERRIDE_MAP[BlockType.EMPHASIS]


# ---------------------------------------------------------------------------
# Config-driven constants
# ---------------------------------------------------------------------------

HWPUNITS_PER_MM = CONFIG.hwp_per_mm

# Page dimensions
PAGE_WIDTH_MM = CONFIG.page.width_mm
PAGE_HEIGHT_MM = CONFIG.page.height_mm
PAGE_WIDTH_HWP = str(CONFIG.page.width_hwp)
PAGE_HEIGHT_HWP = str(CONFIG.page.height_hwp)

# Page margins
MARGIN_TOP_MM = CONFIG.page.margins_mm.get("top", 15.0)
MARGIN_BOTTOM_MM = CONFIG.page.margins_mm.get("bottom", 15.0)
MARGIN_LEFT_MM = CONFIG.page.margins_mm.get("left", 20.0)
MARGIN_RIGHT_MM = CONFIG.page.margins_mm.get("right", 20.0)
MARGIN_HEADER_MM = CONFIG.page.margins_mm.get("header", 10.0)
MARGIN_FOOTER_MM = CONFIG.page.margins_mm.get("footer", 10.0)
PAGE_BORDER_OFFSET_MM = CONFIG.page.border_offset_mm

# Table dimensions
TABLE_WIDTH_HWP = str(CONFIG.tables.width_hwp) if CONFIG.tables else "48189"
TITLE_BODY_HEIGHT_HWP = "3174"
ONE_PT_HWP = str(int(round((25.4 / 72) * HWPUNITS_PER_MM)))
TITLE_TABLE_ROW_HEIGHTS = (ONE_PT_HWP, TITLE_BODY_HEIGHT_HWP, ONE_PT_HWP)
EMPH_TABLE_HEIGHT_HWP = "2632"

# 행 높이 자동 계산 상수
TABLE_LINE_HEIGHT_HWP = 1500
TABLE_MIN_ROW_HEIGHT_HWP = 1800
TABLE_ROW_PADDING_HWP = 400
EMPH_TABLE_ROW_HEIGHT = "521"
TITLE_TABLE_SPACER_CHAR_ID = "9"

# Header/Footer 전용 스타일 ID
def _get_header_footer_ids():
    """머리말/꼬리말 스타일 ID를 CONFIG에서 가져온다."""
    hdr = CONFIG.get_style("header")
    ftr = CONFIG.get_style("footer")
    return {
        "header_para": str(hdr.para_pr_id) if hdr else "12",
        "header_char": str(hdr.char_pr_id) if hdr else "10",
        "header_style": str(hdr.style_id) if hdr else "12",
        "footer_para": str(ftr.para_pr_id) if ftr else "13",
        "footer_char": str(ftr.char_pr_id) if ftr else "10",
        "footer_style": str(ftr.style_id) if ftr else "13",
    }

_HF_IDS = _get_header_footer_ids()
HEADER_PARA_ID = _HF_IDS["header_para"]
FOOTER_PARA_ID = _HF_IDS["footer_para"]
HEADER_CHAR_ID = _HF_IDS["header_char"]
FOOTER_CHAR_ID = _HF_IDS["footer_char"]
HEADER_STYLE_ID = _HF_IDS["header_style"]
FOOTER_STYLE_ID = _HF_IDS["footer_style"]

# Table-specific style IDs
TABLE_TITLE_PARA_ID = "14"
TABLE_HEADER_PARA_ID = "15"
TABLE_BODY_PARA_ID = "16"
SUMMARY_TABLE_PARA_ID = "17"
SUMMARY_BODY_PARA_ID = "18"
SUMMARY_DESC_PARA_ID = "19"
TABLE_TITLE_STYLE_ID = "14"
TABLE_HEADER_STYLE_ID = "15"
TABLE_BODY_STYLE_ID = "16"
SUMMARY_BODY_STYLE_ID = "17"
SUMMARY_DESC_STYLE_ID = "18"
TABLE_BODY_CHAR_ID = "11"
TABLE_HEADER_CHAR_ID = "12"

# Dedicated borderFill IDs
TITLE_TABLE_SPACER_BORDER_ID = "34"
TITLE_TABLE_BODY_BORDER_ID = "35"
EMPH_TABLE_BORDER_ID = "36"
SUMMARY_TABLE_BORDER_ID = "37"
PROCESS_STEP_BORDER_ID = "3"
PROCESS_ARROW_BORDER_ID = "1"
PROCESS_TITLE_BORDER_ID = "41"
PROCESS_DESC_BORDER_ID = "42"

# Spacer paragraph mapping
def _build_spacer_char_map():
    """CONFIG.spacers에서 SPACER_CHAR_MAP 생성."""
    block_to_yaml = {
        BlockType.SUBTITLE: "subtitle",
        BlockType.BODY: "body",
        BlockType.DESC2: "desc2",
        BlockType.DESC3: "desc3",
    }
    result = {}
    for block_type, yaml_key in block_to_yaml.items():
        spacer = CONFIG.spacers.get(yaml_key)
        if spacer:
            result[block_type] = str(spacer.char_pr_id)
    return result

SPACER_CHAR_MAP = _build_spacer_char_map()

SPACER_MARKER_MAP = {
    BlockType.SUBTITLE: " ",
    BlockType.BODY: " ",
    BlockType.DESC2: " ",
    BlockType.DESC3: " ",
}


# ---------------------------------------------------------------------------
# XML Namespaces + _q helper
# ---------------------------------------------------------------------------

NS = {
    "ha": "http://www.hancom.co.kr/hwpml/2011/app",
    "hp": "http://www.hancom.co.kr/hwpml/2011/paragraph",
    "hp10": "http://www.hancom.co.kr/hwpml/2016/paragraph",
    "hs": "http://www.hancom.co.kr/hwpml/2011/section",
    "hc": "http://www.hancom.co.kr/hwpml/2011/core",
    "hh": "http://www.hancom.co.kr/hwpml/2011/head",
    "hhs": "http://www.hancom.co.kr/hwpml/2011/history",
    "hm": "http://www.hancom.co.kr/hwpml/2011/master-page",
    "hpf": "http://www.hancom.co.kr/schema/2011/hpf",
    "hwpunitchar": "http://www.hancom.co.kr/hwpml/2016/HwpUnitChar",
    "ooxmlchart": "http://www.hancom.co.kr/hwpml/2016/ooxmlchart",
    "dc": "http://purl.org/dc/elements/1.1/",
    "opf": "http://www.idpf.org/2007/opf/",
    "epub": "http://www.idpf.org/2007/ops",
    "config": "urn:oasis:names:tc:opendocument:xmlns:config:1.0",
    "ocf": "urn:oasis:names:tc:opendocument:xmlns:container",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "pkg": "http://www.hancom.co.kr/hwpml/2016/meta/pkg#",
}

# Register all namespace prefixes
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

ET.register_namespace("hv", "http://www.hancom.co.kr/hwpml/2011/version")
ET.register_namespace("odf", "urn:oasis:names:tc:opendocument:xmlns:manifest:1.0")


def _q(prefix: str, tag: str) -> str:
    """Qualified tag helper: _q("hp", "p") → '{ns}p'."""
    return f"{{{NS[prefix]}}}{tag}"


def mm_to_hwp(mm: float) -> str:
    """Convert millimeters to Hangul internal HWPUNIT."""
    return str(int(mm * HWPUNITS_PER_MM))


# ---------------------------------------------------------------------------
# Section properties (secPr) — used by renderers and xml_builder
# ---------------------------------------------------------------------------


def _attach_secpr(run: ET.Element) -> None:
    sec_pr = ET.SubElement(
        run,
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
        {
            "landscape": "WIDELY",
            "width": PAGE_WIDTH_HWP,
            "height": PAGE_HEIGHT_HWP,
            "gutterType": "LEFT_ONLY",
        },
    )
    ET.SubElement(
        page_pr,
        _q("hp", "margin"),
        {
            "header": mm_to_hwp(MARGIN_HEADER_MM),
            "footer": mm_to_hwp(MARGIN_FOOTER_MM),
            "gutter": "0",
            "left": mm_to_hwp(MARGIN_LEFT_MM),
            "right": mm_to_hwp(MARGIN_RIGHT_MM),
            "top": mm_to_hwp(MARGIN_TOP_MM),
            "bottom": mm_to_hwp(MARGIN_BOTTOM_MM),
        },
    )
    footnote_pr = ET.SubElement(sec_pr, _q("hp", "footNotePr"))
    ET.SubElement(
        footnote_pr,
        _q("hp", "autoNumFormat"),
        {"type": "DIGIT", "userChar": "", "prefixChar": "", "suffixChar": ")", "supsript": "0"},
    )
    ET.SubElement(
        footnote_pr,
        _q("hp", "noteLine"),
        {"length": "-1", "type": "SOLID", "width": "0.12 mm", "color": "#000000"},
    )
    ET.SubElement(
        footnote_pr,
        _q("hp", "noteSpacing"),
        {"betweenNotes": "283", "belowLine": "567", "aboveLine": "850"},
    )
    ET.SubElement(footnote_pr, _q("hp", "numbering"), {"type": "CONTINUOUS", "newNum": "1"})
    ET.SubElement(
        footnote_pr,
        _q("hp", "placement"),
        {"place": "EACH_COLUMN", "beneathText": "0"},
    )
    endnote_pr = ET.SubElement(sec_pr, _q("hp", "endNotePr"))
    ET.SubElement(
        endnote_pr,
        _q("hp", "autoNumFormat"),
        {"type": "DIGIT", "userChar": "", "prefixChar": "", "suffixChar": ")", "supsript": "0"},
    )
    ET.SubElement(
        endnote_pr,
        _q("hp", "noteLine"),
        {"length": "14692344", "type": "SOLID", "width": "0.12 mm", "color": "#000000"},
    )
    ET.SubElement(
        endnote_pr,
        _q("hp", "noteSpacing"),
        {"betweenNotes": "0", "belowLine": "567", "aboveLine": "850"},
    )
    ET.SubElement(endnote_pr, _q("hp", "numbering"), {"type": "CONTINUOUS", "newNum": "1"})
    ET.SubElement(
        endnote_pr,
        _q("hp", "placement"),
        {"place": "END_OF_DOCUMENT", "beneathText": "0"},
    )
    for border_type in ("BOTH", "EVEN", "ODD"):
        page_border = ET.SubElement(
            sec_pr,
            _q("hp", "pageBorderFill"),
            {
                "type": border_type,
                "borderFillIDRef": "1",
                "textBorder": "PAPER",
                "headerInside": "0",
                "footerInside": "0",
                "fillArea": "PAPER",
            },
        )
        ET.SubElement(
            page_border,
            _q("hp", "offset"),
            {
                "left": mm_to_hwp(PAGE_BORDER_OFFSET_MM),
                "right": mm_to_hwp(PAGE_BORDER_OFFSET_MM),
                "top": mm_to_hwp(PAGE_BORDER_OFFSET_MM),
                "bottom": mm_to_hwp(PAGE_BORDER_OFFSET_MM),
            },
        )
    ctrl = ET.SubElement(run, _q("hp", "ctrl"))
    ET.SubElement(
        ctrl,
        _q("hp", "colPr"),
        {"id": "", "type": "NEWSPAPER", "layout": "LEFT", "colCount": "1", "sameSz": "1", "sameGap": "0"},
    )
