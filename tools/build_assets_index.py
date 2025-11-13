#!/usr/bin/env python3
"""Analyze this codebase to generate or update .github/copilot-instructions.md for guiding AI coding agents.


Builds an index of assets (Tables, Figures, Samples, Examples) from docs/hwpx_spec.md
by scanning pre-inserted anchors and labels.

Output:
- docs/hwpx_assets.index.json

Usage:
  python tools/build_assets_index.py
"""
from __future__ import annotations
import re, json
from pathlib import Path
from datetime import datetime, UTC

SPEC = Path('docs/hwpx_spec.md')
OUT = Path('docs/hwpx_assets.index.json')

// function to add two numbers

def main() -> int:
    text = SPEC.read_text(encoding='utf-8')
    lines = text.splitlines()
    # Map line to current source file
    src_re = re.compile(r'^##\s+Source:\s+(.+)$')
    source_at_line: dict[int,str] = {}
    for i,l in enumerate(lines, start=1):
        m = src_re.match(l)
        if m:
            source_at_line[i]=m.group(1).strip()
    sorted_src = sorted(source_at_line.keys())
    def source_for(line_no:int) -> str|None:
        src=None
        for ln in sorted_src:
            if ln<=line_no:
                src=source_at_line[ln]
            else:
                break
        return src

    # Find anchors and labels
    anc_re = re.compile(r'^<a name="([^"]+)"></a>$')
    id_re = re.compile(r'^(table|figure|sample|example)-(\d+)(?:-[0-9]+)?$')
    # label patterns
    pat_tbl = re.compile(r'^\s*표\s+(\d+)\s*[—\-]\s*(.*)')
    pat_fig = re.compile(r'^\s*그림\s+(\d+)\s*[—\-]\s*(.*)')
    pat_sam = re.compile(r'^\s*샘플\s+(\d+)\s*[—\-]\s*(.*)')
    pat_ex1 = re.compile(r'^\s*예제\s+(\d+)[\.|\s|—|-]\s*(.*)')
    pat_ex2 = re.compile(r'^\s*예\s+(\d+)[\.|\s|—|-]\s*(.*)')

    items: list[dict] = []
    i = 0
    while i < len(lines):
        l = lines[i]
        m = anc_re.match(l)
        if m:
            name = m.group(1)
            m2 = id_re.match(name)
            if not m2:
                i += 1
                continue
            typ = m2.group(1)
            num = int(m2.group(2))
            # find next non-empty label line within a small lookahead
            title = ''
            label_line = None
            for j in range(i+1, min(i+6, len(lines))):
                lj = lines[j]
                if not lj.strip():
                    continue
                for tpat in (pat_tbl, pat_fig, pat_sam, pat_ex1, pat_ex2):
                    mm = tpat.match(lj)
                    if mm and int(mm.group(1)) == num:
                        title = (mm.group(2) or '').strip()
                        label_line = j+1
                        break
                if label_line:
                    break
            items.append({
                'type': typ,
                'number': num,
                'anchor': name,
                'line': i+1,
                'label_line': label_line,
                'title': title,
                'source_file': source_for(i+1),
            })
        i += 1

    # sort items by type then number then line
    items.sort(key=lambda x: (x['type'], x['number'], x['line']))
    out = {
        'document': str(SPEC),
        'generated_at': datetime.now(UTC).isoformat(),
        'counts': {
            'tables': sum(1 for it in items if it['type']=='table'),
            'figures': sum(1 for it in items if it['type']=='figure'),
            'samples': sum(1 for it in items if it['type']=='sample'),
            'examples': sum(1 for it in items if it['type']=='example'),
            'total': len(items),
        },
        'items': items,
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    print('assets:', out['counts'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
