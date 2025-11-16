"""Utilities for loading and validating Phase 1.5 YAML templates."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Mapping

import yaml


class TemplateValidationError(Exception):
    """Raised when the YAML template is missing required fields or invalid."""


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
