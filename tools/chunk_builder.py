#!/usr/bin/env python3
"""
Builds section-level chunks from docs/hwpx_spec.md.
Prefer parsing the Markdown directly to avoid stale indexes. If an index JSON
exists, it is ignored by default to ensure accuracy.

Outputs:
- tools/chunks/sections.jsonl  # one JSON per line (chunk)
- tools/chunks/chunks.meta.json

Usage:
  python tools/chunk_builder.py [--spec docs/hwpx_spec.md] [--out tools/chunks]
  # optional: --use-index to use docs/hwpx_spec.index.json if trustworthy
"""
from __future__ import annotations
import argparse, json, os, sys, re
from pathlib import Path


def load_text(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return text.splitlines()


def cut_lines(lines: list[str], start_line: int, end_line: int) -> str:
    # Lines in index are 1-based; slice is inclusive
    start = max(1, start_line)
    end = min(len(lines), end_line)
    return "\n".join(lines[start - 1 : end]) + "\n"


def _extract_sections_from_md(spec_path: Path) -> list[dict]:
    text = spec_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    # Precompute char offsets per line start (1-based lines)
    char_offsets = [0]
    acc = 0
    for ln in lines:
        char_offsets.append(acc)
        acc += len(ln) + 1

    source_re = re.compile(r'^##\s+Source:\s+(.+)$')
    source_at_line: dict[int, str] = {}
    for i, l in enumerate(lines, start=1):
        m = source_re.match(l)
        if m:
            source_at_line[i] = m.group(1).strip()
    sorted_source_lines = sorted(source_at_line.keys())

    def source_for(line_no: int) -> str | None:
        src = None
        for ln in sorted_source_lines:
            if ln <= line_no:
                src = source_at_line[ln]
            else:
                break
        return src

    anchor_re = re.compile(r'^<a name="(s-[A-Za-z0-9\-]+)"></a>$')
    elem_anchor_re = re.compile(r'^<a name="([A-Za-z0-9\-]+)"></a>$')
    num_heading_re = re.compile(r'^(\d+(?:\.\d+)+)\s+(.+)$')

    sections: list[dict] = []
    # Gather indices of all s- anchors
    s_anchor_lines = [i for i, l in enumerate(lines, start=1) if anchor_re.match(l)]
    for idx, i in enumerate(s_anchor_lines):
        # Find heading line: skip blank and any anchor lines
        j = i + 1
        while j <= len(lines):
            lj = lines[j - 1]
            if lj.strip() == "":
                j += 1
                continue
            if elem_anchor_re.match(lj):
                j += 1
                continue
            break
        if j > len(lines):
            continue
        hm = num_heading_re.match(lines[j - 1])
        if not hm:
            # Not a numbered section
            continue
        number, title = hm.group(1), hm.group(2).strip()
        # Determine end_line as line before next s- anchor or EOF
        end_line = len(lines)
        if idx + 1 < len(s_anchor_lines):
            end_line = s_anchor_lines[idx + 1] - 1
        start_line = j
        start_char = char_offsets[start_line]
        end_char = char_offsets[end_line] + len(lines[end_line - 1])
        anchor = anchor_re.match(lines[i - 1]).group(1)  # type: ignore
        sections.append({
            "anchor": anchor,
            "number": number,
            "title": title,
            "source_file": source_for(start_line),
            "start_line": start_line,
            "end_line": end_line,
            "start_char": start_char,
            "end_char": end_char,
            "length_lines": end_line - start_line + 1,
            "length_chars": end_char - start_char,
        })
    return sections


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", default="docs/hwpx_spec.md")
    parser.add_argument("--out", default="tools/chunks")
    parser.add_argument("--use-index", action="store_true", help="기존 index JSON을 신뢰하여 사용할 경우 지정")
    args = parser.parse_args()

    spec_path = Path(args.spec)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not spec_path.exists():
        print(f"spec file not found: {spec_path}", file=sys.stderr)
        return 2
    # Build sections directly from Markdown unless --use-index is set
    if args.use_index:
        index_path = Path("docs/hwpx_spec.index.json")
        if not index_path.exists():
            print(f"index json not found: {index_path}", file=sys.stderr)
            return 2
        meta = json.loads(index_path.read_text(encoding="utf-8"))
        sections = meta.get("sections", [])
        # Sort by start_line
        sections.sort(key=lambda s: (s.get("start_line", 0), s.get("end_line", 0)))
        lines = load_text(spec_path)
    else:
        sections = _extract_sections_from_md(spec_path)
        lines = load_text(spec_path)

    jsonl_path = out_dir / "sections.jsonl"
    written = 0
    with jsonl_path.open("w", encoding="utf-8") as w:
        for sec in sections:
            anchor = sec.get("anchor")
            number = sec.get("number")
            title = sec.get("title")
            src = sec.get("source_file")
            sline = int(sec.get("start_line", 0))
            eline = int(sec.get("end_line", 0))
            text = cut_lines(lines, sline, eline)
            chunk = {
                "id": anchor or f"s-{sline}-{eline}",
                "anchor": anchor,
                "number": number,
                "title": title,
                "source_file": src,
                "start_line": sline,
                "end_line": eline,
                "text": text,
            }
            w.write(json.dumps(chunk, ensure_ascii=False) + "\n")
            written += 1

    meta_out = {
        "document": str(spec_path),
        "chunks": str(jsonl_path),
        "count": written,
        "source": "md" if not args.use_index else "index-json",
    }
    (out_dir / "chunks.meta.json").write_text(
        json.dumps(meta_out, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"chunks: {written} -> {jsonl_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
