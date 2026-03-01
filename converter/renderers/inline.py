"""인라인 텍스트 처리: Bold 분리, 미리보기 텍스트, XML run 생성.

BOLD_PATTERN, _split_bold_segments, _strip_bold_markup,
_append_text_with_bold, _append_text_with_bold_custom,
_format_block_preview_text, _build_preview_text
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from typing import List, Optional

from converter.models import BlockType, Block
from converter.config import _q, INLINE_BOLD_CHAR_ID


# ---------------------------------------------------------------------------
# Bold 패턴 및 세그먼트 분리
# ---------------------------------------------------------------------------

BOLD_PATTERN = re.compile(r"\*\*(.+?)\*\*")


def _split_bold_segments(text: str) -> List[tuple[str, bool]]:
    segments: List[tuple[str, bool]] = []
    last = 0
    for match in BOLD_PATTERN.finditer(text):
        start, end = match.span()
        if start > last:
            segments.append((text[last:start], False))
        segments.append((match.group(1), True))
        last = end
    if last < len(text):
        segments.append((text[last:], False))
    if not segments and text:
        segments.append((text, False))
    return segments


def _strip_bold_markup(text: str) -> str:
    if not text:
        return ""
    return BOLD_PATTERN.sub(lambda match: match.group(1), text)


# ---------------------------------------------------------------------------
# XML run 생성 (Bold 지원)
# ---------------------------------------------------------------------------


def _append_text_with_bold(
    paragraph: ET.Element, base_char_id: str | None, full_text: str
) -> None:
    _append_text_with_bold_custom(paragraph, base_char_id, full_text, INLINE_BOLD_CHAR_ID)


def _append_text_with_bold_custom(
    paragraph: ET.Element, base_char_id: str | None, full_text: str, bold_char_id: str
) -> None:
    if full_text is None:
        return
    if not full_text:
        return
    segments = _split_bold_segments(full_text)
    if not segments:
        segments = [(full_text, False)]
    for seg_text, is_bold in segments:
        if not seg_text:
            continue
        run_attrs = {}
        if is_bold:
            run_attrs["charPrIDRef"] = bold_char_id
        elif base_char_id is not None:
            run_attrs["charPrIDRef"] = base_char_id
        run = ET.SubElement(paragraph, _q("hp", "run"), run_attrs)
        t = ET.SubElement(run, _q("hp", "t"))
        t.text = seg_text


# ---------------------------------------------------------------------------
# 미리보기 텍스트 생성
# ---------------------------------------------------------------------------


def _format_block_preview_text(block: Block) -> Optional[str]:
    if not block.text:
        return None
    if block.type in (BlockType.TABLE, BlockType.SUMMARY_TABLE, BlockType.PROCESS, BlockType.DIAGRAM):
        return None
    if block.type == BlockType.TITLE:
        return None
    cleaned = _strip_bold_markup(block.text).strip()
    if not cleaned:
        return None
    if block.type == BlockType.SUBTITLE:
        return f"□ {cleaned}"
    if block.type == BlockType.BODY:
        return f" ◦ {cleaned}"
    if block.type == BlockType.DESC2:
        return f"   - {cleaned}"
    if block.type == BlockType.DESC3:
        return f"    * {cleaned}"
    if block.type == BlockType.EMPHASIS:
        return f"◈ {cleaned}"
    return cleaned


def _build_preview_text(blocks: List[Block], title: str) -> str:
    safe_title = title.strip() or "Untitled"
    lines = ["< >", f"<{safe_title}>", "< >", ""]
    for block in blocks:
        preview_line = _format_block_preview_text(block)
        if preview_line is None:
            continue
        lines.append(preview_line)
        lines.append("")
    preview = "\n".join(lines).rstrip()
    if not preview.endswith("\n"):
        preview += "\n"
    return preview
