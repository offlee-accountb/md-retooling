#!/usr/bin/env python3
"""리팩토링된 converter 모듈들을 dist_lite용 단일 파일로 합칩니다.

출력: dist_lite/converter/md_to_hwpx.py
"""
import re
from pathlib import Path

ROOT = Path("/home/d997/new md retooling")
SRC = ROOT / "converter"
DST = ROOT / "dist_lite" / "converter" / "md_to_hwpx.py"

# 합칠 모듈 순서 (의존 순서)
MODULES = [
    SRC / "models.py",
    SRC / "preview_data.py",
    SRC / "config.py",
    SRC / "renderers" / "inline.py",
    SRC / "renderers" / "text_fitting.py",
    SRC / "renderers" / "tables.py",
    SRC / "renderers" / "process_diagram.py",
    SRC / "parser.py",
    SRC / "xml_builder.py",
    SRC / "md_to_hwpx.py",
]

# 제거할 import 패턴 (converter 내부 import)
INTERNAL_IMPORT_RE = re.compile(
    r"^from converter\.\S+\s+import\s+.*$"
    r"|^from converter\s+import\s+.*$"
    r"|^import converter\.\S+"
)

# 모듈 docstring 추출 후 제거용
DOCSTRING_RE = re.compile(r'^("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', re.MULTILINE)


def strip_internal_imports(src: str) -> str:
    """converter.* 내부 import 제거."""
    lines = src.split("\n")
    result = []
    skip_continuation = False
    for line in lines:
        stripped = line.strip()
        # 멀티라인 import 처리
        if skip_continuation:
            if stripped.endswith(")"):
                skip_continuation = False
            continue

        if INTERNAL_IMPORT_RE.match(stripped):
            if "(" in stripped and ")" not in stripped:
                skip_continuation = True
            continue
        result.append(line)
    return "\n".join(result)


def strip_module_boilerplate(src: str, module_name: str) -> str:
    """모듈별 docstring, __future__ import, 중복 stdlib import 등 제거."""
    lines = src.split("\n")
    result = []
    in_docstring = False
    docstring_done = False

    for line in lines:
        stripped = line.strip()

        # 모듈 맨 처음 docstring 건너뛰기
        if not docstring_done:
            if stripped.startswith('"""') or stripped.startswith("'''"):
                if in_docstring:
                    in_docstring = False
                    docstring_done = True
                    continue
                elif stripped.count('"""') >= 2 or stripped.count("'''") >= 2:
                    docstring_done = True
                    continue
                else:
                    in_docstring = True
                    continue
            elif in_docstring:
                continue
            elif stripped.startswith("#!") or stripped == "":
                continue
            else:
                docstring_done = True

        # __future__ import 건너뛰기
        if stripped.startswith("from __future__"):
            continue

        # sys.path 조작 건너뛰기
        if "_PROJECT_ROOT" in stripped or "sys.path.insert" in stripped:
            continue
        if "Path(__file__).parent.parent" in stripped and "_PROJECT_ROOT" in stripped:
            continue

        result.append(line)

    return "\n".join(result)


# 메인 헤더 (단일 파일 출력용)
HEADER = '''#!/usr/bin/env python3
"""MD → HWPX 변환기 (dist_lite 단일 파일 배포판).

이 파일은 converter/ 패키지의 모든 모듈을 하나로 합친 것입니다.
자동 생성: build_dist_lite.py

모듈 구성:
- models          : 데이터 모델 (BlockType, Block, ...)
- preview_data    : 미리보기 PNG 데이터
- config          : 설정/상수/NS/_q
- renderers       : 인라인, 텍스트 피팅, 표, 프로세스/도식도
- parser          : MD 파싱
- xml_builder     : XML 빌더 (header.xml, section0.xml, ...)
- md_to_hwpx      : ZIP 패키징 + CLI
"""
from __future__ import annotations

import argparse
import base64
import getpass
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum, auto
from pathlib import Path
from typing import Iterable, List, Optional, TYPE_CHECKING

# Ensure project root is in sys.path
_PROJECT_ROOT = str(Path(__file__).parent.parent)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from validator.template_loader import load_style_config, StyleConfig

'''

# 이미 포함된 stdlib import을 제거
STDLIB_IMPORTS = {
    "import argparse", "import base64", "import getpass", "import re",
    "import sys", "import xml.etree.ElementTree as ET", "import zipfile",
    "from dataclasses import dataclass", "from dataclasses import dataclass, field",
    "from datetime import datetime, timezone", "from enum import Enum, auto",
    "from pathlib import Path", "from typing import",
    "import xml.etree.ElementTree", "from validator.template_loader import",
}


def strip_stdlib_imports(src: str) -> str:
    """헤더에 이미 포함된 stdlib import 제거."""
    lines = src.split("\n")
    result = []
    for line in lines:
        stripped = line.strip()
        skip = False
        for pattern in STDLIB_IMPORTS:
            if stripped.startswith(pattern):
                skip = True
                break
        if not skip:
            result.append(line)
    return "\n".join(result)


def build():
    parts = [HEADER]

    for mod_path in MODULES:
        mod_name = mod_path.stem
        src = mod_path.read_text(encoding="utf-8")

        # 1) 내부 import 제거
        src = strip_internal_imports(src)
        # 2) 모듈 boilerplate 제거
        src = strip_module_boilerplate(src, mod_name)
        # 3) 중복 stdlib import 제거
        src = strip_stdlib_imports(src)

        # 섹션 구분자 추가
        separator = f"\n\n# {'=' * 72}\n# Module: {mod_name}\n# {'=' * 72}\n\n"
        parts.append(separator)
        parts.append(src.strip())
        parts.append("\n")

    output = "\n".join(parts)

    # 연속 빈 줄 정리 (3줄 이상 → 2줄)
    output = re.sub(r"\n{4,}", "\n\n\n", output)

    DST.write_text(output, encoding="utf-8")
    line_count = output.count("\n") + 1
    print(f"dist_lite md_to_hwpx.py: {line_count} lines, {len(output)} bytes")


if __name__ == "__main__":
    build()
