"""Utilities for loading and validating Phase 1.5 YAML templates."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Tuple

import yaml


class TemplateValidationError(Exception):
    """Raised when the YAML template is missing required fields or invalid."""


# =============================================================================
# Validation Template Models (기존)
# =============================================================================

@dataclass
class TemplateMetadata:
    template_id: str
    version: str | None
    max_blocks: int | None


@dataclass
class TemplateModel:
    meta: TemplateMetadata
    document: Dict[str, Any]
    blocks: List[Dict[str, Any]]
    style_defaults: Dict[str, Any]
    raw: Dict[str, Any]


# =============================================================================
# Style Config Models (신규 - HWPX 변환용)
# =============================================================================

@dataclass
class PageConfig:
    """페이지 설정."""
    size: str = "A4"
    width_mm: float = 210.0
    height_mm: float = 297.0
    width_hwp: int = 59528
    height_hwp: int = 84186
    margins_mm: Dict[str, float] = field(default_factory=lambda: {
        "top": 15.0, "bottom": 15.0, "left": 20.0, "right": 20.0,
        "header": 10.0, "footer": 10.0, "gutter": 0
    })
    border_offset_mm: float = 5.0


@dataclass
class FontDef:
    """폰트 정의."""
    id: int
    name: str
    type: str = "TTF"
    family_type: str = "FCAT_GOTHIC"
    usage: List[str] = field(default_factory=list)


@dataclass
class CharProperty:
    """글자 속성 (charPr)."""
    id: int
    name: str
    font_id: int
    height_pt: int
    bold: bool = False
    text_color: str = "#000000"
    
    @property
    def height_hwp(self) -> int:
        """HWP 단위 높이 (pt × 100)."""
        return self.height_pt * 100


@dataclass
class ParaProperty:
    """문단 속성 (paraPr)."""
    id: int
    name: str
    align: str  # JUSTIFY, LEFT, CENTER, RIGHT
    line_spacing_pct: int
    indent_hwp: int = 0
    font_line_height: bool = False
    snap_to_grid: bool = True


@dataclass
class StyleMapping:
    """블록 타입별 스타일 매핑."""
    style_id: int
    para_pr_id: int
    char_pr_id: int
    name_ko: str
    name_en: str


@dataclass
class SpacerDef:
    """Spacer 정의."""
    char_pr_id: int
    height_pt: int


@dataclass
class TableBorders:
    """테이블 테두리 ID 세트."""
    header: Tuple[int, int, int]      # (first_col, mid_cols, last_col)
    body_top: Tuple[int, int, int]
    body_middle: Tuple[int, int, int]
    body_bottom: Tuple[int, int, int]


@dataclass
class TableStyles:
    """테이블 스타일 ID."""
    title_para_id: int
    header_para_id: int
    body_para_id: int
    header_char_id: int
    body_char_id: int
    header_style_id: int
    body_style_id: int


@dataclass
class TableConfig:
    """테이블 설정."""
    width_hwp: int = 48189
    cell_margin_mm: Dict[str, float] = field(default_factory=lambda: {
        "left": 1.8, "right": 1.8, "top": 0.5, "bottom": 0.5
    })
    out_margin_hwp: int = 283
    styles: Optional[TableStyles] = None
    borders: Optional[TableBorders] = None


@dataclass
class BorderFillDef:
    """테두리/채우기 정의."""
    id: int
    name: str
    borders: Optional[Dict[str, Tuple[str, str]]] = None  # {edge: (type, width)}
    fill: Optional[Dict[str, str]] = None  # {face_color, hatch_color}


@dataclass
class DocumentMode:
    """문서 모드 설정."""
    style_mode: str = "stylebook"  # "stylebook" | "normal"
    use_line_spacers: bool = True


@dataclass
class StyleConfig:
    """HWPX 스타일 설정 전체."""
    version: str
    template_id: str
    description: str
    
    # 문서 모드
    document_mode: DocumentMode = field(default_factory=DocumentMode)
    
    # 단위
    hwp_per_mm: float = 283.464566929
    hwp_per_pt: float = 100.0
    
    # 섹션별 설정
    page: PageConfig = field(default_factory=PageConfig)
    fonts: List[FontDef] = field(default_factory=list)
    char_properties: List[CharProperty] = field(default_factory=list)
    para_properties: List[ParaProperty] = field(default_factory=list)
    styles: Dict[str, StyleMapping] = field(default_factory=dict)
    spacers: Dict[str, SpacerDef] = field(default_factory=dict)
    tables: TableConfig = field(default_factory=TableConfig)
    border_fills: List[BorderFillDef] = field(default_factory=list)
    
    # Raw data for extension
    raw: Dict[str, Any] = field(default_factory=dict)
    
    # === Helper methods ===
    
    def get_char_pr(self, char_id: int) -> Optional[CharProperty]:
        """ID로 CharProperty 조회."""
        for cp in self.char_properties:
            if cp.id == char_id:
                return cp
        return None
    
    def get_para_pr(self, para_id: int) -> Optional[ParaProperty]:
        """ID로 ParaProperty 조회."""
        for pp in self.para_properties:
            if pp.id == para_id:
                return pp
        return None
    
    def get_font(self, font_id: int) -> Optional[FontDef]:
        """ID로 Font 조회."""
        for f in self.fonts:
            if f.id == font_id:
                return f
        return None
    
    def get_style(self, block_type: str) -> Optional[StyleMapping]:
        """블록 타입명으로 StyleMapping 조회."""
        return self.styles.get(block_type.lower())
    
    def get_border_fill(self, bf_id: int) -> Optional[BorderFillDef]:
        """ID로 BorderFill 조회."""
        for bf in self.border_fills:
            if bf.id == bf_id:
                return bf
        return None
    
    def mm_to_hwp(self, mm: float) -> int:
        """mm를 HWP 단위로 변환."""
        return int(mm * self.hwp_per_mm)
    
    def pt_to_hwp(self, pt: float) -> int:
        """pt를 HWP 단위로 변환."""
        return int(pt * self.hwp_per_pt)


def load_style_config(path: Path | str) -> StyleConfig:
    """스타일 설정 YAML 파일 로드.
    
    Args:
        path: YAML 파일 경로
        
    Returns:
        StyleConfig: 파싱된 스타일 설정
        
    Raises:
        FileNotFoundError: 파일 없음
        TemplateValidationError: YAML 파싱 또는 검증 실패
    """
    if isinstance(path, str):
        path = Path(path)
    
    if not path.exists():
        raise FileNotFoundError(f"Style config not found: {path}")
    
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise TemplateValidationError(f"Failed to read config: {exc}") from exc
    
    try:
        data = yaml.safe_load(content) or {}
    except yaml.YAMLError as exc:
        raise TemplateValidationError(f"YAML parsing failed: {exc}") from exc
    
    # 메타데이터
    version = data.get("version", "1.0")
    template_id = data.get("template_id", "default")
    description = data.get("description", "")
    
    # 문서 모드
    doc_mode_data = data.get("document_mode", {})
    document_mode = DocumentMode(
        style_mode=doc_mode_data.get("style_mode", "stylebook"),
        use_line_spacers=doc_mode_data.get("use_line_spacers", True),
    )
    
    # 단위
    units = data.get("units", {})
    hwp_per_mm = units.get("hwp_per_mm", 283.464566929)
    hwp_per_pt = units.get("hwp_per_pt", 100.0)
    
    # 페이지 설정
    page_data = data.get("page", {})
    page = PageConfig(
        size=page_data.get("size", "A4"),
        width_mm=page_data.get("width_mm", 210.0),
        height_mm=page_data.get("height_mm", 297.0),
        width_hwp=page_data.get("width_hwp", 59528),
        height_hwp=page_data.get("height_hwp", 84186),
        margins_mm=page_data.get("margins_mm", PageConfig().margins_mm),
        border_offset_mm=page_data.get("border_offset_mm", 5.0),
    )
    
    # 폰트
    fonts = []
    for f in data.get("fonts", []):
        fonts.append(FontDef(
            id=f["id"],
            name=f["name"],
            type=f.get("type", "TTF"),
            family_type=f.get("family_type", "FCAT_GOTHIC"),
            usage=f.get("usage", []),
        ))
    
    # 글자 속성
    char_properties = []
    for cp in data.get("char_properties", []):
        char_properties.append(CharProperty(
            id=cp["id"],
            name=cp["name"],
            font_id=cp["font_id"],
            height_pt=cp["height_pt"],
            bold=cp.get("bold", False),
            text_color=cp.get("text_color", "#000000"),
        ))
    
    # 문단 속성
    para_properties = []
    for pp in data.get("para_properties", []):
        para_properties.append(ParaProperty(
            id=pp["id"],
            name=pp["name"],
            align=pp["align"],
            line_spacing_pct=pp["line_spacing_pct"],
            indent_hwp=pp.get("indent_hwp", 0),
            font_line_height=pp.get("font_line_height", False),
            snap_to_grid=pp.get("snap_to_grid", True),
        ))
    
    # 스타일 매핑
    styles = {}
    for key, s in data.get("styles", {}).items():
        styles[key] = StyleMapping(
            style_id=s["style_id"],
            para_pr_id=s["para_pr_id"],
            char_pr_id=s["char_pr_id"],
            name_ko=s.get("name_ko", key),
            name_en=s.get("name_en", key),
        )
    
    # Spacer
    spacers = {}
    for key, sp in data.get("spacers", {}).items():
        spacers[key] = SpacerDef(
            char_pr_id=sp["char_pr_id"],
            height_pt=sp["height_pt"],
        )
    
    # 테이블 설정
    tables_data = data.get("tables", {})
    default_tbl = tables_data.get("default", {})
    styles_tbl = tables_data.get("styles", {})
    borders_tbl = tables_data.get("borders", {})
    
    table_styles = None
    if styles_tbl:
        table_styles = TableStyles(
            title_para_id=styles_tbl.get("title_para_id", 14),
            header_para_id=styles_tbl.get("header_para_id", 15),
            body_para_id=styles_tbl.get("body_para_id", 16),
            header_char_id=styles_tbl.get("header_char_id", 12),
            body_char_id=styles_tbl.get("body_char_id", 11),
            header_style_id=styles_tbl.get("header_style_id", 15),
            body_style_id=styles_tbl.get("body_style_id", 16),
        )
    
    table_borders = None
    if borders_tbl:
        table_borders = TableBorders(
            header=tuple(borders_tbl.get("header", [12, 13, 14])),
            body_top=tuple(borders_tbl.get("body_top", [9, 10, 11])),
            body_middle=tuple(borders_tbl.get("body_middle", [4, 3, 5])),
            body_bottom=tuple(borders_tbl.get("body_bottom", [6, 7, 8])),
        )
    
    tables = TableConfig(
        width_hwp=default_tbl.get("width_hwp", 48189),
        cell_margin_mm=default_tbl.get("cell_margin_mm", TableConfig().cell_margin_mm),
        out_margin_hwp=default_tbl.get("out_margin_hwp", 283),
        styles=table_styles,
        borders=table_borders,
    )
    
    # BorderFill
    border_fills = []
    for bf in data.get("border_fills", []):
        borders = None
        if bf.get("borders"):
            borders = {}
            for edge, spec in bf["borders"].items():
                if isinstance(spec, list) and len(spec) == 2:
                    borders[edge] = (spec[0], spec[1])
        
        fill = bf.get("fill")
        border_fills.append(BorderFillDef(
            id=bf["id"],
            name=bf["name"],
            borders=borders,
            fill=fill,
        ))
    
    return StyleConfig(
        version=version,
        template_id=template_id,
        description=description,
        document_mode=document_mode,
        hwp_per_mm=hwp_per_mm,
        hwp_per_pt=hwp_per_pt,
        page=page,
        fonts=fonts,
        char_properties=char_properties,
        para_properties=para_properties,
        styles=styles,
        spacers=spacers,
        tables=tables,
        border_fills=border_fills,
        raw=data,
    )


# =============================================================================
# 기존 Validation Functions (유지)
# =============================================================================


def _ensure_dict(node: Any, context: str) -> Dict[str, Any]:
    if not isinstance(node, dict):
        raise TemplateValidationError(f"{context} must be a mapping")
    return node


STYLE_FIELD_TYPES: Mapping[str, tuple[type, ...] | type] = {
    "font": str,
    "font_size": (int, float),
    "line_spacing": int,
    "align": str,
    "bold": bool,
    "italic": bool,
    "underline": bool,
    "indent_pt": (int, float),
    "spacing_before": (int, float),
    "spacing_after": (int, float),
    "shading": str,
    "border": str,
    "border_width_pt": (int, float),
    "padding_pt": (int, float),
}

TEXT_MATCH_TYPES = {"exact", "contains", "regex"}


def _validate_style(
    style: Dict[str, Any] | None,
    context: str,
    defaults: Dict[str, Any] | None,
) -> Dict[str, Any]:
    if style is None:
        return dict(defaults or {})
    style_dict = _ensure_dict(style, context)
    for key, value in style_dict.items():
        expected = STYLE_FIELD_TYPES.get(key)
        if expected is None:
            # Allow forward-compatible custom fields by skipping type checks
            continue
        if not isinstance(value, expected):
            raise TemplateValidationError(
                f"{context}.{key} must be of type {expected} (got {type(value)})"
            )
    merged = dict(defaults or {})
    merged.update(style_dict)
    return merged


def _validate_text_block(block: Dict[str, Any], ctx: str) -> None:
    text = block.get("text")
    text_ctx = f"{ctx}.text"
    text_dict = _ensure_dict(text, text_ctx)
    match = text_dict.get("match", "exact")
    if match not in TEXT_MATCH_TYPES:
        raise TemplateValidationError(
            f"{text_ctx}.match must be one of {sorted(TEXT_MATCH_TYPES)}"
        )
    value = text_dict.get("value")
    if not isinstance(value, str) or not value:
        raise TemplateValidationError(f"{text_ctx}.value must be a non-empty string")


def _validate_table_block(block: Dict[str, Any], ctx: str) -> None:
    table = _ensure_dict(block.get("table"), f"{ctx}.table")
    rows = table.get("rows")
    cols = table.get("cols")
    if not isinstance(rows, int) or rows <= 0:
        raise TemplateValidationError(f"{ctx}.table.rows must be a positive integer")
    if not isinstance(cols, int) or cols <= 0:
        raise TemplateValidationError(f"{ctx}.table.cols must be a positive integer")
    cells = table.get("cells", [])
    if cells is None:
        return
    if not isinstance(cells, list):
        raise TemplateValidationError(f"{ctx}.table.cells must be a list")
    for idx, cell in enumerate(cells, start=1):
        cell_ctx = f"{ctx}.table.cells[{idx}]"
        cell_dict = _ensure_dict(cell, cell_ctx)
        row = cell_dict.get("row")
        col = cell_dict.get("col")
        if not isinstance(row, int) or not (1 <= row <= rows):
            raise TemplateValidationError(
                f"{cell_ctx}.row must be between 1 and {rows} (got {row})"
            )
        if not isinstance(col, int) or not (1 <= col <= cols):
            raise TemplateValidationError(
                f"{cell_ctx}.col must be between 1 and {cols} (got {col})"
            )
        text = cell_dict.get("text")
        if text is not None and not isinstance(text, str):
            raise TemplateValidationError(f"{cell_ctx}.text must be a string if provided")


def _validate_list_block(block: Dict[str, Any], ctx: str) -> None:
    list_cfg = _ensure_dict(block.get("list"), f"{ctx}.list")
    marker = list_cfg.get("marker")
    if marker is not None and not isinstance(marker, str):
        raise TemplateValidationError(f"{ctx}.list.marker must be a string")
    min_items = list_cfg.get("min_items")
    max_items = list_cfg.get("max_items")
    if min_items is not None and (not isinstance(min_items, int) or min_items < 0):
        raise TemplateValidationError(f"{ctx}.list.min_items must be >= 0")
    if max_items is not None and (not isinstance(max_items, int) or max_items < 0):
        raise TemplateValidationError(f"{ctx}.list.max_items must be >= 0")
    if min_items is not None and max_items is not None and min_items > max_items:
        raise TemplateValidationError(
            f"{ctx}.list.min_items must be <= max_items (got {min_items}>{max_items})"
        )


def _validate_constraints(block: Dict[str, Any], ctx: str) -> None:
    constraints = block.get("constraints")
    if constraints is None:
        return
    constraint_dict = _ensure_dict(constraints, f"{ctx}.constraints")
    for key in ("required", "repeatable"):
        value = constraint_dict.get(key)
        if value is not None and not isinstance(value, bool):
            raise TemplateValidationError(f"{ctx}.constraints.{key} must be boolean")


def load_template(path: Path) -> TemplateModel:
    """Parse YAML file, enforce schema invariants, and return structured data."""
    if not path.exists():
        raise FileNotFoundError(f"Template file not found: {path}")
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise TemplateValidationError(f"Failed to read template: {exc}") from exc

    try:
        data = yaml.safe_load(content) or {}
    except yaml.YAMLError as exc:
        raise TemplateValidationError(f"YAML parsing failed: {exc}") from exc

    root = _ensure_dict(data, "Template root")
    meta_dict = _ensure_dict(root.get("meta", {}), "meta")
    document = _ensure_dict(root.get("document", {}), "document")
    defaults = document.get("defaults")
    if defaults is not None:
        defaults = _ensure_dict(defaults, "document.defaults")
    style_defaults = _validate_style(defaults, "document.defaults", None)

    template_id = meta_dict.get("template_id")
    if not isinstance(template_id, str) or not template_id.strip():
        raise TemplateValidationError("meta.template_id must be a non-empty string")
    version = meta_dict.get("version")
    max_blocks = meta_dict.get("max_blocks")
    if max_blocks is not None:
        if not isinstance(max_blocks, int) or max_blocks <= 0:
            raise TemplateValidationError("meta.max_blocks must be a positive integer")

    blocks = root.get("blocks")
    if blocks is None:
        raise TemplateValidationError("Template must define a 'blocks' list")
    if not isinstance(blocks, list):
        raise TemplateValidationError("'blocks' must be a list")

    block_count_limit = max_blocks or 8
    if len(blocks) > block_count_limit:
        raise TemplateValidationError(
            f"blocks count ({len(blocks)}) exceeds allowed maximum ({block_count_limit})"
        )

    block_validators = {
        "table": _validate_table_block,
        "list": _validate_list_block,
    }

    for idx, block in enumerate(blocks, start=1):
        block_ctx = f"blocks[{idx}]"
        block_dict = _ensure_dict(block, block_ctx)
        block_id = block_dict.get("id")
        if not isinstance(block_id, str) or not block_id.strip():
            raise TemplateValidationError(f"{block_ctx}.id must be a non-empty string")
        block_type = block_dict.get("type")
        if not isinstance(block_type, str) or not block_type.strip():
            raise TemplateValidationError(f"{block_ctx}.type must be a non-empty string")
        source = block_dict.get("source")
        if source is not None and not isinstance(source, str):
            raise TemplateValidationError(f"{block_ctx}.source must be a string if provided")

        # Type-specific validation
        validator = block_validators.get(block_type, _validate_text_block)
        validator(block_dict, block_ctx)
        _validate_constraints(block_dict, block_ctx)
        resolved_style = _validate_style(
            block_dict.get("style"), f"{block_ctx}.style", style_defaults
        )
        block_dict.setdefault("style", resolved_style)
        block_dict["style_resolved"] = resolved_style

    meta = TemplateMetadata(
        template_id=template_id,
        version=version,
        max_blocks=max_blocks,
    )
    return TemplateModel(
        meta=meta,
        document=document,
        blocks=blocks,
        style_defaults=style_defaults,
        raw=root,
    )
