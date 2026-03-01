#!/usr/bin/env python3
"""MD → HWPX 변환기 (thin orchestrator).

모든 핵심 로직은 하위 모듈로 분리됨:
- converter.models        : 데이터 모델
- converter.config        : 설정/상수/NS/_q
- converter.parser        : MD 파싱
- converter.renderers.*   : 렌더링 (inline, text_fitting, tables, process_diagram)
- converter.xml_builder   : XML 빌더 (header.xml, section0.xml, ...)
- converter.preview_data  : 미리보기 이미지 데이터

이 파일은 write_hwpx (ZIP 패키징) + CLI 진입점만 담당한다.
"""
from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path
from typing import List

# Ensure project root is in sys.path (for CLI: python converter/md_to_hwpx.py)
_PROJECT_ROOT = str(Path(__file__).parent.parent)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from converter.models import Block
from converter.parser import parse_md_lines
from converter.preview_data import PREVIEW_PNG_BYTES
from converter.renderers.inline import _build_preview_text
from converter.xml_builder import (
    build_header_xml, build_section0_xml, build_content_hpf,
    build_container_xml, build_version_xml, build_settings_xml,
    build_manifest_xml, build_container_rdf,
    _build_document_metadata,
)


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

    metadata = _build_document_metadata(blocks)

    # Build all XML files
    header_bytes = build_header_xml()
    section0_bytes = build_section0_xml(blocks, metadata)
    content_hpf_bytes = build_content_hpf(doc_meta=metadata)
    container_bytes = build_container_xml()
    container_rdf_bytes = build_container_rdf()
    manifest_bytes = build_manifest_xml()
    version_bytes = build_version_xml()
    settings_bytes = build_settings_xml()
    preview_text_bytes = _build_preview_text(blocks, metadata.title).encode("utf-8")

    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        # mimetype must be first and uncompressed (per OCF spec)
        zf.writestr("mimetype", "application/hwp+zip", compress_type=zipfile.ZIP_STORED)

        # Version and settings
        zf.writestr("version.xml", version_bytes)
        zf.writestr("settings.xml", settings_bytes)

        # Preview assets
        zf.writestr("Preview/PrvText.txt", preview_text_bytes)
        zf.writestr("Preview/PrvImage.png", PREVIEW_PNG_BYTES)

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
