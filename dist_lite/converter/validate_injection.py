#!/usr/bin/env python3
"""template_injector용 JSON 검증기.

LLM이 생성한 injection JSON을 실행 전에 검증한다.
필수 키 확인, 타입 유효성, 좌표 범위 등을 체크.
"""

import json
import sys
from pathlib import Path

# 유효한 injection 타입
VALID_TYPES = {
    "cell", "t_element", "text_replace",
    "checkbox", "paragraph",
    "para_t_element", "para_text_replace",
}

# 타입별 필수 키
REQUIRED_KEYS = {
    "cell": ["table_idx", "row_idx", "cell_idx", "value"],
    "t_element": ["table_idx", "row_idx", "cell_idx", "t_idx", "value"],
    "text_replace": ["find", "replace"],  # + table_idx/row_idx/cell_idx 또는 para_idx
    "checkbox": ["table_idx", "row_idx", "cell_idx"],
    "paragraph": ["para_idx", "value"],
    "para_t_element": ["para_idx", "t_idx", "value"],
    "para_text_replace": ["para_idx", "find", "replace"],
}


def validate_injection(inj: dict, idx: int) -> list[str]:
    """단일 injection 항목을 검증한다. 에러 메시지 리스트 반환."""
    errors = []

    # type 확인
    inj_type = inj.get("type")
    if not inj_type:
        errors.append(f"[{idx}] 'type' 누락")
        return errors
    if inj_type not in VALID_TYPES:
        errors.append(f"[{idx}] 유효하지 않은 type: '{inj_type}' (유효: {VALID_TYPES})")
        return errors

    # 필수 키 확인
    required = REQUIRED_KEYS.get(inj_type, [])
    for key in required:
        if key not in inj:
            # text_replace는 table_idx 또는 para_idx 둘 중 하나
            if inj_type == "text_replace" and key in ("table_idx", "row_idx", "cell_idx"):
                if "para_idx" not in inj:
                    errors.append(f"[{idx}] text_replace는 table_idx+row_idx+cell_idx 또는 para_idx 필요")
            else:
                errors.append(f"[{idx}] 필수 키 누락: '{key}' (type={inj_type})")

    # 좌표 타입 확인
    for key in ["table_idx", "row_idx", "cell_idx", "t_idx", "para_idx"]:
        if key in inj and not isinstance(inj[key], int):
            errors.append(f"[{idx}] '{key}'는 정수여야 함, got: {type(inj[key]).__name__}")

    # value/find/replace 타입 확인
    for key in ["value", "find", "replace"]:
        if key in inj and not isinstance(inj[key], str):
            errors.append(f"[{idx}] '{key}'는 문자열이어야 함, got: {type(inj[key]).__name__}")

    # checkbox의 checked
    if inj_type == "checkbox":
        if "checked" in inj and not isinstance(inj["checked"], bool):
            errors.append(f"[{idx}] 'checked'는 bool이어야 함")

    # text_replace의 find가 비어있지 않은지
    if inj_type in ("text_replace", "para_text_replace"):
        find_val = inj.get("find", "")
        if isinstance(find_val, str) and len(find_val.strip()) == 0:
            errors.append(f"[{idx}] 'find' 값이 비어있음")

    # value에 placeholder가 남아있지 않은지
    for key in ["value", "replace"]:
        val = inj.get(key, "")
        if isinstance(val, str) and "{{" in val and "}}" in val:
            errors.append(f"[{idx}] '{key}'에 미교체 placeholder 남아있음: '{val}'")

    return errors


def validate_json_file(json_path: Path) -> tuple[bool, list[str]]:
    """injection JSON 파일 전체를 검증한다."""
    errors = []

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"JSON 파싱 실패: {e}"]

    if "injections" not in data:
        return False, ["'injections' 키가 없음"]

    injections = data["injections"]
    if not isinstance(injections, list):
        return False, ["'injections'는 배열이어야 함"]

    if len(injections) == 0:
        errors.append("[warn] injections 배열이 비어있음")

    for idx, inj in enumerate(injections):
        errs = validate_injection(inj, idx)
        errors.extend(errs)

    is_valid = not any(e for e in errors if not e.startswith("[warn]"))
    return is_valid, errors


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_injection.py <data.json>")
        return 1

    json_path = Path(sys.argv[1])
    if not json_path.exists():
        print(f"❌ 파일 없음: {json_path}")
        return 1

    is_valid, errors = validate_json_file(json_path)

    print(f"📋 Validating: {json_path.name}")
    print(f"{'='*50}")

    if errors:
        for e in errors:
            icon = "⚠️" if e.startswith("[warn]") else "❌"
            print(f"  {icon} {e}")
    else:
        print("  ✅ 모든 검증 통과")

    print(f"{'='*50}")
    total = len(json.loads(json_path.read_text())["injections"])
    print(f"Result: {'✅ VALID' if is_valid else '❌ INVALID'} ({total} injections)")
    return 0 if is_valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
