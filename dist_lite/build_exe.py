#!/usr/bin/env python3
"""dist_lite를 하나의 실행 파일(.exe)로 빌드하는 스크립트.

사용법:
    cd dist_lite
    python build_exe.py

결과:
    dist/MD변환기.exe  (Windows)
    dist/MD변환기      (Linux/Mac)
"""

import os
import sys
import subprocess

# ── 1) PyInstaller 자동 설치 ──────────────────────────────────────
try:
    import PyInstaller.__main__
except ImportError:
    print("⏳ PyInstaller가 없습니다. 자동 설치 중...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    import PyInstaller.__main__

try:
    import yaml  # noqa: F401
except ImportError:
    print("⏳ PyYAML이 없습니다. 자동 설치 중...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyYAML"])

from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

# ── 2) OS별 --add-data 구분자 ─────────────────────────────────────
#    Windows: "소스;대상"   /   Linux·Mac: "소스:대상"
SEP = ";" if os.name == "nt" else ":"


def _add(src: str, dst: str) -> list:
    """--add-data 인자 한 쌍을 OS에 맞게 생성."""
    return ["--add-data", f"{SCRIPT_DIR / src}{SEP}{dst}"]


def build():
    args = [
        str(SCRIPT_DIR / "run_web.py"),
        "--onefile",                          # 단일 파일로 묶기
        "--name", "MD변환기",                  # 실행 파일 이름
        "--noconfirm",                        # 기존 빌드 덮어쓰기
        "--clean",                            # 캐시 정리
        # 데이터 파일 포함
        *_add("templates",           "templates"),
        *_add("converter",           "converter"),
        *_add("validator",           "validator"),
        *_add("예시",                 "예시"),
        *_add("마크다운_작성가이드.md",  "."),
        *_add("README.md",           "."),
        # 숨겨진 import
        "--hidden-import", "yaml",
        "--hidden-import", "converter",
        "--hidden-import", "converter.md_to_hwpx",
        "--hidden-import", "validator",
        "--hidden-import", "validator.template_loader",
        # 콘솔 표시 (서버 로그를 보여줌)
        "--console",
        # 작업 디렉토리
        "--distpath", str(SCRIPT_DIR / "dist"),
        "--workpath", str(SCRIPT_DIR / "build"),
        "--specpath", str(SCRIPT_DIR),
    ]

    print("🔨 빌드를 시작합니다...")
    print()
    PyInstaller.__main__.run(args)

    exe_name = "MD변환기.exe" if os.name == "nt" else "MD변환기"
    exe_path = SCRIPT_DIR / "dist" / exe_name

    print()
    print("=" * 60)
    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print(f"✅ 빌드 완료!  ({size_mb:.1f} MB)")
        print(f"   파일: {exe_path}")
        print()
        print("   이 파일 하나만 배포하면 됩니다.")
        print("   사용법: 더블클릭하면 브라우저가 자동으로 열립니다.")
    else:
        print("❌ 빌드 실패! 위의 에러 메시지를 확인하세요.")
    print("=" * 60)


if __name__ == "__main__":
    build()
