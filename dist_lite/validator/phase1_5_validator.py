"""YAML-driven validator for Phase 1.5."""
from __future__ import annotations

import json
import re
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    from .template_loader import TemplateModel, load_template
except ImportError:  # pragma: no cover - allows running cli.py directly
    from template_loader import TemplateModel, load_template  # type: ignore


class HwpxParseError(Exception):
    """Raised when the HWPX package cannot be read or parsed."""


@dataclass
class Finding:
    block_id: str
    severity: str
    field: str
    expected: str
    actual: str
    hint: str | None = None


@dataclass
class ValidationReport:
    template: str
    hwpx: str
    summary: Dict[str, int]
    findings: List[Finding] = field(default_factory=list)

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2)

    def to_text(self) -> str:
        parts = [f"Template: {self.template}", f"HWPX: {self.hwpx}"]
        summary_str = ", ".join(f"{k}={v}" for k, v in self.summary.items())
        parts.append(f"Summary: {summary_str}")
        if not self.findings:
            parts.append("No findings.")
            return "\n".join(parts)
        parts.append("Findings:")
        for item in self.findings:
            hint_text = f" hint={item.hint}" if item.hint else ""
            parts.append(
                f"  - [{item.severity.upper()}] {item.block_id}::{item.field} "
                f"expected='{item.expected}' actual='{item.actual}'{hint_text}"
            )
        return "\n".join(parts)


@dataclass
class TableData:
    rows: int
    cols: int
    cells: Dict[Tuple[int, int], str]

    def get_text(self, row: int, col: int) -> str:
        return self.cells.get((row, col), "")


@dataclass
class DocumentBlock:
    kind: str  # 'paragraph' or 'table'
    text: Optional[str] = None
    table: Optional[TableData] = None
    attrs: Dict[str, Optional[str]] | None = None


NS = {
    "hp": "http://www.hancom.co.kr/hwpml/2011/paragraph",
    "hs": "http://www.hancom.co.kr/hwpml/2011/section",
    "hh": "http://www.hancom.co.kr/hwpml/2011/head",
}


def _q(prefix: str, tag: str) -> str:
    return f"{{{NS[prefix]}}}{tag}"


class HwpxDocument:
    """Utility wrapper for reading sections from a HWPX package."""

    def __init__(self, hwpx_path: Path):
        self.hwpx_path = Path(hwpx_path)
        if not self.hwpx_path.exists():
            raise HwpxParseError(f"HWPX file not found: {hwpx_path}")
        try:
            with zipfile.ZipFile(self.hwpx_path) as zf:
                section_bytes = zf.read("Contents/section0.xml")
        except KeyError as exc:
            raise HwpxParseError("HWPX is missing Contents/section0.xml") from exc
        except zipfile.BadZipFile as exc:
            raise HwpxParseError("Invalid HWPX zip container") from exc

        sanitized = self._dedupe_xmlns(section_bytes.decode("utf-8"))
        try:
            self.section_root = ET.fromstring(sanitized)
        except ET.ParseError as exc:
            raise HwpxParseError(f"section0.xml parsing failed: {exc}") from exc
        self.blocks = self._extract_blocks()

    @staticmethod
    def _dedupe_xmlns(xml_text: str) -> str:
        pattern = re.compile(r"(\s+xmlns(?::[A-Za-z0-9_]+)?=\"[^\"]*\")")
        seen: set[str] = set()

        def replacer(match: re.Match[str]) -> str:
            attr = match.group(1)
            key = attr.split("=")[0].strip()
            if key in seen:
                return ""
            seen.add(key)
            return attr

        return pattern.sub(replacer, xml_text, count=0)

    def _extract_blocks(self) -> List[DocumentBlock]:
        blocks: List[DocumentBlock] = []
        for p in self.section_root.findall(_q("hp", "p")):
            para_attrs = {
                "paraPrIDRef": p.get("paraPrIDRef"),
                "styleIDRef": p.get("styleIDRef"),
            }
            char_attr = self._find_char_pr(p)
            if char_attr:
                para_attrs["charPrIDRef"] = char_attr
            table_el = p.find(f".//{_q('hp', 'tbl')}")
            if table_el is not None:
                table = self._parse_table(table_el)
                blocks.append(
                    DocumentBlock(
                        kind="table",
                        table=table,
                        attrs=para_attrs,
                    )
                )
            else:
                text = self._extract_text(p)
                blocks.append(
                    DocumentBlock(
                        kind="paragraph",
                        text=text,
                        attrs=para_attrs,
                    )
                )
        return blocks

    @staticmethod
    def _find_char_pr(p: ET.Element) -> Optional[str]:
        run = p.find(_q("hp", "run"))
        if run is not None and run.get("charPrIDRef"):
            return run.get("charPrIDRef")
        return None

    @staticmethod
    def _extract_text(p: ET.Element) -> str:
        fragments = []
        for t in p.findall(f".//{_q('hp', 't')}"):
            if t.text:
                fragments.append(t.text)
        return "".join(fragments)

    def _parse_table(self, tbl: ET.Element) -> TableData:
        cells: Dict[Tuple[int, int], str] = {}
        rows = tbl.findall(f".//{_q('hp', 'tr')}")
        row_cnt = len(rows)
        col_cnt = 0
        for row_idx, tr in enumerate(rows, start=1):
            cols = tr.findall(f".//{_q('hp', 'tc')}")
            col_cnt = max(col_cnt, len(cols))
            for col_idx, tc in enumerate(cols, start=1):
                text = self._extract_text(tc)
                cells[(row_idx, col_idx)] = text
        return TableData(rows=row_cnt, cols=col_cnt, cells=cells)


class DocumentIterator:
    """Consumes DocumentBlocks while skipping spacer paragraphs and reordering tables."""

    TITLE_TABLE_STYLE = {"1", "6"}
    BULLET_CHARS = {"2", "3", "4"}

    def __init__(self, blocks: List[DocumentBlock]):
        self.blocks = blocks
        self.index = 0

    def _skip_blank(self, idx: int) -> int:
        while idx < len(self.blocks):
            block = self.blocks[idx]
            if block.kind == "paragraph":
                if not (block.text or "").strip():
                    idx += 1
                    continue
            break
        return idx

    def _reorder_if_title_table(self, idx: int) -> int:
        if idx <= 0 or idx >= len(self.blocks):
            return idx
        block = self.blocks[idx]
        if block.kind != "table":
            return idx
        style_id = block.attrs.get("styleIDRef") if block.attrs else None
        if style_id in self.TITLE_TABLE_STYLE:
            prev_idx = idx - 1
            self.blocks[prev_idx], self.blocks[idx] = self.blocks[idx], self.blocks[prev_idx]
            return prev_idx
        return idx

    def peek(self) -> Optional[DocumentBlock]:
        idx = self._skip_blank(self.index)
        idx = self._reorder_if_title_table(idx)
        if idx >= len(self.blocks):
            return None
        return self.blocks[idx]

    def consume(self) -> Optional[DocumentBlock]:
        idx = self._skip_blank(self.index)
        idx = self._reorder_if_title_table(idx)
        if idx >= len(self.blocks):
            return None
        block = self.blocks[idx]
        self.index = idx + 1
        return block

    def collect_list(self, marker: Optional[str]) -> List[DocumentBlock]:
        items: List[DocumentBlock] = []
        while True:
            idx = self._skip_blank(self.index)
            if idx >= len(self.blocks):
                break
            block = self.blocks[idx]
            if block.kind != "paragraph":
                break
            text = (block.text or "").strip()
            char_id = (block.attrs or {}).get("charPrIDRef")
            is_bullet = char_id in self.BULLET_CHARS
            if marker:
                if marker == "-" and not (text.startswith("-") or is_bullet):
                    break
                if marker != "-" and not text.startswith(marker):
                    break
            elif not is_bullet:
                break
            items.append(block)
            self.index = idx + 1
        return items


def normalize_text(text: str, collapse: bool = True) -> str:
    base = text.strip()
    if collapse:
        base = re.sub(r"\s+", " ", base)
    return base


def is_placeholder(value: str) -> bool:
    return value.startswith("{{") and value.endswith("}}")


class Phase15Validator:
    """Validates a converted HWPX document against a YAML template."""

    TEXT_TYPES = {
        "title",
        "body",
        "note",
        "signature",
        "subtitle",
        "paragraph",
        "text",
        "plain",
    }

    def __init__(self, template_path: Path):
        self.template_path = template_path
        self.template_model: TemplateModel = load_template(template_path)

    def validate(self, hwpx_path: Path) -> ValidationReport:
        document = HwpxDocument(hwpx_path)
        iterator = DocumentIterator(document.blocks)
        findings: List[Finding] = []
        error_blocks: set[str] = set()

        for block_cfg in self.template_model.blocks:
            block_id = block_cfg.get("id", "unknown")
            block_type = block_cfg.get("type", "body")
            constraints = block_cfg.get("constraints", {}) or {}
            required = constraints.get("required", True)

            if block_type == "table":
                doc_block = iterator.consume()
                if doc_block is None:
                    findings.append(
                        Finding(
                            block_id,
                            "error" if required else "warn",
                            "structure",
                            "Table block present",
                            "Document ended before table",
                            "Add missing table block or update template",
                        )
                    )
                    if required:
                        error_blocks.add(block_id)
                    continue
                if doc_block.kind != "table":
                    findings.append(
                        Finding(
                            block_id,
                            "error" if required else "warn",
                            "structure",
                            "Table block",
                            f"Saw {doc_block.kind}",
                            "Ensure table order matches template",
                        )
                    )
                    if required:
                        error_blocks.add(block_id)
                    continue
                table_findings = self._compare_table(block_cfg, doc_block.table or TableData(0, 0, {}), block_id)
                findings.extend(table_findings)
                if any(f.severity == "error" for f in table_findings):
                    error_blocks.add(block_id)
            elif block_type == "list":
                marker = block_cfg.get("source")
                list_items = iterator.collect_list(marker)
                list_findings = self._compare_list(block_cfg, list_items, block_id)
                findings.extend(list_findings)
                if any(f.severity == "error" for f in list_findings):
                    error_blocks.add(block_id)
            else:
                doc_block = iterator.consume()
                if doc_block is None:
                    findings.append(
                        Finding(
                            block_id,
                            "error" if required else "warn",
                            "structure",
                            "Text block present",
                            "Document ended",
                            "Add missing paragraph or update template",
                        )
                    )
                    if required:
                        error_blocks.add(block_id)
                    continue
                if doc_block.kind != "paragraph":
                    findings.append(
                        Finding(
                            block_id,
                            "error" if required else "warn",
                            "structure",
                            "Paragraph block",
                            f"Saw {doc_block.kind}",
                            "Order mismatch (paragraph expected)",
                        )
                    )
                    if required:
                        error_blocks.add(block_id)
                    continue
                text_findings = self._compare_text(block_cfg, doc_block.text or "", block_id)
                findings.extend(text_findings)
                if any(f.severity == "error" for f in text_findings):
                    error_blocks.add(block_id)

        total_blocks = len(self.template_model.blocks)
        failed_blocks = len(error_blocks)
        summary = {
            "blocks": total_blocks,
            "passed": total_blocks - failed_blocks,
            "failed": failed_blocks,
            "issues": len(findings),
        }
        template_label = f"{self.template_model.meta.template_id} ({self.template_path})"
        return ValidationReport(
            template=template_label,
            hwpx=str(hwpx_path),
            summary=summary,
            findings=findings,
        )

    def _compare_text(self, block_cfg: Dict, actual_text: str, block_id: str) -> List[Finding]:
        findings: List[Finding] = []
        text_cfg = block_cfg.get("text") or {}
        expected_value = text_cfg.get("value", "")
        match_type = text_cfg.get("match", "exact")
        collapse = text_cfg.get("normalize", True)
        if block_cfg.get("type") == "title":
            prefix = block_cfg.get("source") or ""
            if prefix and actual_text.startswith(prefix):
                actual_text = actual_text[len(prefix) :].strip()
        normalized_actual = normalize_text(actual_text, collapse=collapse)
        normalized_expected = normalize_text(expected_value, collapse=collapse)

        if match_type == "exact" and normalized_actual != normalized_expected:
            findings.append(
                Finding(
                    block_id,
                    "error",
                    "text",
                    normalized_expected,
                    normalized_actual,
                    "Text differs from template",
                )
            )
        elif match_type == "contains" and normalized_expected not in normalized_actual:
            findings.append(
                Finding(
                    block_id,
                    "error",
                    "text",
                    f"Contains {normalized_expected}",
                    normalized_actual,
                    "Expected substring missing",
                )
            )
        elif match_type == "regex":
            if not re.search(expected_value, normalized_actual):
                findings.append(
                    Finding(
                        block_id,
                        "error",
                        "text",
                        expected_value,
                        normalized_actual,
                        "Regex did not match",
                    )
                )
        return findings

    def _compare_table(self, block_cfg: Dict, table: TableData, block_id: str) -> List[Finding]:
        findings: List[Finding] = []
        table_cfg = block_cfg.get("table") or {}
        expected_rows = table_cfg.get("rows")
        expected_cols = table_cfg.get("cols")
        if expected_rows and table.rows != expected_rows:
            findings.append(
                Finding(
                    block_id,
                    "error",
                    "table.rows",
                    str(expected_rows),
                    str(table.rows),
                    "Row count mismatch",
                )
            )
        if expected_cols and table.cols != expected_cols:
            findings.append(
                Finding(
                    block_id,
                    "error",
                    "table.cols",
                    str(expected_cols),
                    str(table.cols),
                    "Column count mismatch",
                )
            )
        for cell in table_cfg.get("cells", []) or []:
            row = cell.get("row")
            col = cell.get("col")
            expected_text = cell.get("text", "")
            actual_text = table.get_text(row, col)
            if not expected_text:
                continue
            if is_placeholder(expected_text):
                if not actual_text.strip():
                    findings.append(
                        Finding(
                            block_id,
                            "warn",
                            f"table.cell({row},{col})",
                            "Non-empty value",
                            "",
                            "Populate placeholder cell",
                        )
                    )
                continue
            norm_expected = normalize_text(expected_text)
            norm_actual = normalize_text(actual_text)
            if norm_expected != norm_actual:
                findings.append(
                    Finding(
                        block_id,
                        "error",
                        f"table.cell({row},{col})",
                        norm_expected,
                        norm_actual,
                        "Cell text mismatch",
                    )
                )
        return findings

    def _compare_list(
        self,
        block_cfg: Dict,
        list_items: List[DocumentBlock],
        block_id: str,
    ) -> List[Finding]:
        findings: List[Finding] = []
        list_cfg = block_cfg.get("list") or {}
        min_items = list_cfg.get("min_items", 1)
        max_items = list_cfg.get("max_items")
        normalize_flag = list_cfg.get("normalize_whitespace", False)

        count = len(list_items)
        if count < min_items:
            findings.append(
                Finding(
                    block_id,
                    "error",
                    "list.count",
                    f">= {min_items}",
                    str(count),
                    "Too few list items",
                )
            )
        if max_items is not None and count > max_items:
            findings.append(
                Finding(
                    block_id,
                    "error",
                    "list.count",
                    f"<= {max_items}",
                    str(count),
                    "Too many list items",
                )
            )

        marker = block_cfg.get("source")
        for item in list_items:
            text = item.text or ""
            normalized = normalize_text(text) if normalize_flag else text.strip()
            if marker and not normalized.startswith(marker):
                findings.append(
                    Finding(
                        block_id,
                        "warn",
                        "list.marker",
                        f"Starts with {marker}",
                        normalized,
                        "Unexpected list marker",
                    )
                )
        return findings
