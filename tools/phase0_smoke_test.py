#!/usr/bin/env python3
"""Phase 0 end-to-end smoke test.

Steps
1. Check docs/hwpx_spec.md exists.
2. Rebuild tools/chunks/sections.jsonl if missing, stale, or --force-rebuild given.
3. Run tools/spec_search.py with a representative query.

Exit code 0 means both chunk build (when applicable) and search completed.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    """Run command and stream output; raise if it fails."""
    print(f"[cmd] {' '.join(cmd)}")
    return subprocess.run(cmd, cwd=str(cwd), check=True, text=True)

def needs_rebuild(spec: Path, sections: Path) -> bool:
    if not sections.exists():
        return True
    return spec.stat().st_mtime > sections.stat().st_mtime

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", default="줄간격 line-spacing", help="검색 키워드")
    parser.add_argument("-k", type=int, default=3, help="검색 결과 수")
    parser.add_argument("--compact", type=int, default=1, help="spec_search --compact 값")
    parser.add_argument("--force-rebuild", action="store_true", help="항상 청크 재생성")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    docs = root / "docs"
    tools_dir = root / "tools"
    spec = docs / "hwpx_spec.md"
    sections = tools_dir / "chunks" / "sections.jsonl"

    if not spec.exists():
        print(f"[error] Spec not found: {spec}")
        return 1

    chunk_cmd = [
        sys.executable,
        str(tools_dir / "chunk_builder.py"),
        "--spec",
        str(spec),
        "--out",
        str(tools_dir / "chunks"),
    ]

    if args.force_rebuild or needs_rebuild(spec, sections):
        print("[info] Running chunk builder…")
        run(chunk_cmd, root)
    else:
        print("[info] Existing sections.jsonl is up to date.")

    search_cmd = [
        sys.executable,
        str(tools_dir / "spec_search.py"),
        args.query,
        "-k",
        str(args.k),
        "--compact",
        str(args.compact),
    ]
    print("[info] Running sample search…")
    run(search_cmd, root)
    print("[ok] Phase 0 smoke test completed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
