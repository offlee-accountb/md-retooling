#!/usr/bin/env python3
"""HWPX 템플릿 주입 파이프라인.

Vision(수동/API) + slot_detector 하이브리드 방식으로
빈 양식에 비즈니스 데이터를 주입한다.

Usage:
  # 수동 모드: Vision 출력을 직접 붙여넣기
  python pipeline.py template.hwpx --manual vision_output.txt

  # 텍스트 모드: slot_detector + 비즈니스 데이터로 프롬프트 생성
  python pipeline.py template.hwpx --prompt business_data.txt

  # 주입 실행: 생성된 JSON으로 주입
  python pipeline.py template.hwpx --inject data.json -o output.hwpx
"""

import json
import re
import sys
from pathlib import Path

# 같은 디렉토리의 모듈 import
sys.path.insert(0, str(Path(__file__).parent.parent))
from converter.slot_detector import generate_llm_context, detect_slots, detect_paragraph_slots
from converter.validate_injection import validate_json_file

# ---------------------------------------------------------------------------
# Vision 출력 파서
# ---------------------------------------------------------------------------

def parse_vision_output(text: str) -> list[dict]:
    """Flash 3 Vision의 자연어 출력을 파싱하여 구조화된 매핑 리스트로 변환.

    입력 형식 (예시):
      [붙임1] 파일명
      1. 섹션 > 필드명 → 값
      체크박스 설명 → 동의함 ☑
      날짜 (2025년 월 일) → 2025년 6월 15일

    반환: [{"field": "기업명", "value": "...", "context": "...", "file": "붙임1", "is_checkbox": False}, ...]
    """
    results = []
    current_file = ""

    for line in text.strip().split("\n"):
        line = line.strip()
        if not line:
            continue

        # 파일 헤더: [붙임1] ...
        file_match = re.match(r'^\[(.+?)\]', line)
        if file_match and '→' not in line:
            current_file = file_match.group(1)
            continue

        # 필드 → 값 매핑
        if '→' not in line:
            continue

        parts = line.split('→', 1)
        if len(parts) != 2:
            continue

        field_desc = parts[0].strip()
        value = parts[1].strip()

        # 번호 제거: "1. " "1) " 등
        field_desc = re.sub(r'^\d+[\.\)]\s*', '', field_desc)

        # 컨텍스트 추출: "섹션 > 필드명" → context="섹션", field="필드명"
        context = ""
        field = field_desc
        if '>' in field_desc:
            parts_ctx = field_desc.rsplit('>', 1)
            context = parts_ctx[0].strip()
            field = parts_ctx[1].strip()

        # 괄호 안 원본 형식 제거: "날짜 (2025년 월 일)" → field="날짜"
        field_clean = re.sub(r'\s*\(.+?\)\s*$', '', field).strip()

        # 체크박스 판단
        is_checkbox = bool(re.search(r'[☑☐✓✗]|체크|동의함|동의하지', value))

        results.append({
            "file": current_file,
            "field": field_clean or field,
            "field_full": field,
            "value": value,
            "context": context,
            "is_checkbox": is_checkbox,
        })

    return results


# ---------------------------------------------------------------------------
# Vision 매핑 + slot_detector 좌표 매칭
# ---------------------------------------------------------------------------

# 키워드 매칭용: 비전 필드명 → slot_detector 라벨 키워드
KEYWORD_ALIASES = {
    "기업체명": ["기업명", "기업체명", "회사명", "상호"],
    "기업명": ["기업명", "기업체명", "회사명", "상호"],
    "대표자": ["대표자", "대표이사"],
    "대표이사": ["대표자", "대표이사"],
    "설립일자": ["설립일자", "설립"],
    "사업자등록번호": ["사업자등록번호", "사업자번호"],
    "사업자번호": ["사업자등록번호", "사업자번호"],
    "주소": ["주소"],
    "부서명": ["부서명", "부서"],
    "직위": ["직위", "직  위"],
    "성명": ["성명", "성  명", "이름"],
    "휴대폰": ["휴대폰", "핸드폰", "모바일"],
    "전화": ["전화", "전  화", "연락처"],
    "이메일": ["이메일", "E-mail", "email"],
    "연락처": ["연락처", "전화", "휴대폰"],
    "법인번호": ["법인번호", "법인등록번호"],
    "진단 유형": ["기본진단", "심화진단", "진단"],
    "진단유형": ["기본진단", "심화진단", "진단"],
    "신청자": ["신청자", "신  청  자", "신청"],
    "신청기업명": ["신청기업명", "신청기업"],
    "귀중": ["귀중", "귀 중"],
}


def _normalize(text: str) -> str:
    """비교용 정규화: 공백 제거, 소문자."""
    return re.sub(r'\s+', '', text).lower()


def match_vision_to_slots(vision_mappings: list[dict], slots: dict) -> dict:
    """Vision 매핑과 slot_detector 슬롯을 매칭하여 injection JSON 생성.

    Returns: {
        "matched": [injection_dict, ...],
        "unmatched_vision": [vision_item, ...],
        "unmatched_slots": [slot_item, ...],
    }
    """
    slot_list = slots["slots"]
    matched = []
    used_slot_ids = set()
    unmatched_vision = []

    for vm in vision_mappings:
        field_norm = _normalize(vm["field"])
        value = vm["value"]

        # 키워드 후보
        keywords = KEYWORD_ALIASES.get(vm["field"], [vm["field"]])
        keywords_norm = [_normalize(k) for k in keywords]

        best_slot = None
        best_score = 0

        for slot in slot_list:
            if slot["slot_id"] in used_slot_ids:
                continue

            slot_loc = slot.get("location", "")
            slot_loc_norm = _normalize(slot_loc)
            slot_type = slot["slot_type"]
            slot_orig = _normalize(slot.get("original_text", ""))

            score = 0

            # 키워드 매칭
            for kw_norm in keywords_norm:
                if kw_norm in slot_loc_norm:
                    score += 10
                    break
                if kw_norm in slot_orig:
                    score += 5
                    break

            # 필드명 자체가 슬롯 위치에 포함되는지 (부분 매칭)
            if score == 0 and field_norm and len(field_norm) >= 2:
                if field_norm in slot_loc_norm or field_norm in slot_orig:
                    score += 7

            # 체크박스 매칭 — Vision의 값에 있는 키워드로도 매칭
            if vm["is_checkbox"] and slot_type == "checkbox":
                score += 3
                # Vision 값 안의 키워드가 슬롯에 있는지
                value_norm = _normalize(vm["value"])
                if any(_normalize(kw) in slot_orig for kw in ["기본진단", "심화진단", "동의"]):
                    if any(_normalize(kw) in value_norm for kw in ["기본진단", "동의함"]):
                        score += 8
            elif vm["is_checkbox"] and slot_type != "checkbox":
                score -= 5

            # 날짜 매칭
            if any(k in vm["field"] for k in ["날짜", "일자"]) and slot_type == "date":
                score += 8

            # label_empty 매칭 (신청기업명, 신청자 등)
            if slot_type == "label_empty":
                for kw_norm in keywords_norm:
                    if kw_norm in slot_orig:
                        score += 8
                        break

            if score > best_score:
                best_score = score
                best_slot = slot

        if best_slot and best_score >= 5:
            used_slot_ids.add(best_slot["slot_id"])
            inj = _build_injection(best_slot, vm)
            if inj:
                matched.append(inj)
        else:
            unmatched_vision.append(vm)

    unmatched_slots = [s for s in slot_list if s["slot_id"] not in used_slot_ids]

    return {
        "matched": matched,
        "unmatched_vision": unmatched_vision,
        "unmatched_slots": unmatched_slots,
    }


def _build_injection(slot: dict, vision: dict) -> dict | None:
    """매칭된 슬롯+비전으로 injection 항목을 생성."""
    template = slot["injection_template"]
    inj = dict(template)  # copy

    value = vision["value"]

    if inj["type"] == "checkbox":
        # "동의함 ☑" / "☑ 기본진단" → checked
        inj["checked"] = bool(re.search(r'[☑✓]|동의함|체크', value))
        # placeholder 제거
        inj.pop("value", None)
    elif inj["type"] in ("text_replace", "para_text_replace"):
        # find는 원본 유지, replace에 값 삽입
        find_text = inj.get("find", "")
        orig = slot.get("original_text", "")

        if ":" in orig or "：" in orig:
            # "신청기업명 :" → "신청기업명 : 값"
            inj["replace"] = f"{orig} {value}"
        elif re.search(r'ㅇ{2,}', orig):
            # "ㅇㅇㅇ" → 실제 값, (인) 유지
            replaced = re.sub(r'ㅇ{2,}', value.split('(')[0].strip(), orig)
            inj["replace"] = replaced
        elif re.search(r'년\s+월\s+일', orig) or re.search(r'20\s+\.', orig):
            # 날짜 교체
            inj["replace"] = value
        else:
            inj["replace"] = value
    elif inj["type"] in ("cell", "t_element", "para_t_element"):
        inj["value"] = value
    else:
        inj["value"] = value

    # placeholder 제거
    if inj.get("value") == "{{여기에_값}}":
        inj["value"] = value

    return inj


# ---------------------------------------------------------------------------
# 프롬프트 생성
# ---------------------------------------------------------------------------

VISION_PROMPT_TEMPLATE = """첨부된 이미지는 한국 정부 공문서 양식(HWPX)입니다. 빈 양식(아직 작성 안 된 상태)입니다.

## 요청

양식 이미지를 보고:
1. **비어있는 입력 필드**를 모두 찾아주세요 (빈 칸, 날짜, 체크박스, 밑줄, ㅇㅇㅇ 등)
2. 각 필드의 **위치**와 **용도**를 설명해주세요
3. 아래 비즈니스 데이터를 사용하여, 각 필드에 **어떤 값을 넣어야 하는지** 매핑해주세요

## 비즈니스 데이터
{business_data}

## 출력 형식

반드시 아래 형식으로 출력하세요 (파싱에 사용됩니다):

```
[파일명]
섹션 > 필드명 → 값
다른 필드명 → 값
체크박스 필드 → 동의함 ☑
날짜 필드 → 2025년 6월 15일
```

**중요**:
- 모든 빈 칸을 빠짐없이 찾으세요
- 체크박스는 어느 것을 체크해야 하는지 명시하세요
- 날짜는 원본 양식의 형식을 따르세요
- "(인)" "(서명)" 표시는 유지하세요
"""


def generate_vision_prompt(business_data: str) -> str:
    """Vision LLM에게 전달할 프롬프트 생성."""
    return VISION_PROMPT_TEMPLATE.format(business_data=business_data)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(description="HWPX 템플릿 주입 파이프라인")
    parser.add_argument("hwpx", help="HWPX 템플릿 파일 경로")
    parser.add_argument("--manual", metavar="FILE",
                        help="Vision 출력 텍스트 파일 (수동 모드)")
    parser.add_argument("--prompt", metavar="FILE",
                        help="비즈니스 데이터 파일 → Vision 프롬프트 생성")
    parser.add_argument("--inject", metavar="FILE",
                        help="injection JSON으로 바로 주입")
    parser.add_argument("-o", "--output", default=None,
                        help="출력 HWPX 경로")
    parser.add_argument("--section", default="Contents/section0.xml",
                        help="섹션 파일 (기본: Contents/section0.xml)")

    args = parser.parse_args()
    hwpx_path = Path(args.hwpx)

    # --- 모드 1: Vision 프롬프트 생성 ---
    if args.prompt:
        biz_data = Path(args.prompt).read_text(encoding="utf-8")
        prompt = generate_vision_prompt(biz_data)
        print(prompt)
        print("\n" + "=" * 60)
        print("⬆️  위 프롬프트 + 양식 이미지를 Flash 3에 붙여넣으세요.")
        print("   결과를 텍스트 파일로 저장한 후:")
        print(f"   python pipeline.py {hwpx_path} --manual <결과파일.txt>")
        return 0

    # --- 모드 2: 수동 Vision 출력 → injection JSON 생성 ---
    if args.manual:
        vision_text = Path(args.manual).read_text(encoding="utf-8")

        # 1) Vision 파싱
        mappings = parse_vision_output(vision_text)
        print(f"📋 Vision 출력 파싱: {len(mappings)}개 필드 발견")

        # 2) slot_detector
        ctx = generate_llm_context(hwpx_path, args.section)
        print(f"🔍 slot_detector: {ctx['total_slots']}개 슬롯 탐지")

        # 3) 매칭
        result = match_vision_to_slots(mappings, ctx)
        print(f"✅ 매칭 성공: {len(result['matched'])}개")
        if result["unmatched_vision"]:
            print(f"⚠️  Vision에서 찾았지만 좌표 매칭 실패: {len(result['unmatched_vision'])}개")
            for uv in result["unmatched_vision"]:
                print(f"    → {uv['field']}: {uv['value'][:30]}")
        if result["unmatched_slots"]:
            print(f"ℹ️  slot_detector 슬롯 중 미사용: {len(result['unmatched_slots'])}개")

        # 4) JSON 출력
        output_data = {
            "description": f"{hwpx_path.name} — Vision 하이브리드 주입",
            "injections": result["matched"],
        }
        json_path = hwpx_path.with_suffix('.auto.json')
        if args.output:
            json_path = Path(args.output).with_suffix('.json')

        json_path.write_text(
            json.dumps(output_data, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        print(f"\n💾 injection JSON 저장: {json_path}")

        # 5) 검증
        is_valid, errors = validate_json_file(json_path)
        if is_valid:
            print(f"✅ 검증 통과 ({len(result['matched'])}개 injections)")
        else:
            print("❌ 검증 실패:")
            for e in errors:
                print(f"  {e}")

        return 0

    # --- 모드 3: 바로 주입 ---
    if args.inject:
        from converter.template_injector import inject_into_hwpx
        output_path = args.output or str(hwpx_path).replace('.hwpx', '_filled.hwpx')
        inject_into_hwpx(str(hwpx_path), args.inject, output_path)
        return 0

    # --- 기본: slot_detector JSON 출력 ---
    ctx = generate_llm_context(hwpx_path, args.section)
    print(json.dumps(ctx, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
