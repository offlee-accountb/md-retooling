"""Unit tests for validator.template_loader."""
from __future__ import annotations

import textwrap

import pytest
import yaml

from validator.template_loader import (
    TemplateValidationError,
    load_template,
)


def _write_yaml(tmp_path, data) -> str:
    path = tmp_path / "template.yaml"
    yaml_text = yaml.safe_dump(data, sort_keys=False)
    path.write_text(yaml_text, encoding="utf-8")
    return path


def _base_meta_document() -> dict:
    return {
        "meta": {
            "template_id": "unit-test-template",
            "max_blocks": 8,
        },
        "document": {
            "defaults": {
                "font": "Malgun Gothic",
                "font_size": 11,
                "line_spacing": 160,
            }
        },
    }


def test_text_block_requires_text_mapping(tmp_path):
    data = _base_meta_document()
    data["blocks"] = [
        {
            "id": "title_main",
            "type": "title",
            "style": {"font_size": 18},
        }
    ]
    path = _write_yaml(tmp_path, data)

    with pytest.raises(TemplateValidationError) as exc:
        load_template(path)

    assert "blocks[1].text" in str(exc.value)


def test_table_block_rejects_out_of_range_cell(tmp_path):
    data = _base_meta_document()
    data["blocks"] = [
        {
            "id": "meta_table",
            "type": "table",
            "table": {
                "rows": 2,
                "cols": 2,
                "cells": [
                    {"row": 3, "col": 1, "text": "Oops"},
                ],
            },
        }
    ]
    path = _write_yaml(tmp_path, data)

    with pytest.raises(TemplateValidationError) as exc:
        load_template(path)

    assert "row must be between 1 and 2" in str(exc.value)


def test_blocks_over_limit_raise(tmp_path):
    data = _base_meta_document()
    blocks = []
    for idx in range(9):
        blocks.append(
            {
                "id": f"block_{idx}",
                "type": "body",
                "text": {"match": "exact", "value": f"Item {idx}"},
            }
        )
    data["blocks"] = blocks
    path = _write_yaml(tmp_path, data)

    with pytest.raises(TemplateValidationError) as exc:
        load_template(path)

    assert "exceeds allowed maximum" in str(exc.value)


def test_style_defaults_merge_into_blocks(tmp_path):
    data = _base_meta_document()
    data["blocks"] = [
        {
            "id": "body_1",
            "type": "body",
            "text": {"match": "exact", "value": "Body text"},
            "style": {"font_size": 14},
        }
    ]
    path = _write_yaml(tmp_path, data)

    template = load_template(path)

    style = template.blocks[0]["style_resolved"]
    assert style["font"] == "Malgun Gothic"
    assert style["font_size"] == 14
    assert template.style_defaults["line_spacing"] == 160
