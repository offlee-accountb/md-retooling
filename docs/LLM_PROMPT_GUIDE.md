# HWPX 템플릿 데이터 주입 — LLM 프롬프트 가이드

> 이 프롬프트를 LLM (Gemini Flash 3 등)에 전달하면,
> slot_detector 출력을 기반으로 정확한 injection JSON을 생성할 수 있다.

---

## System Prompt (LLM에게 전달)

```
당신은 한국 정부 공문서 HWPX 양식에 데이터를 주입하는 전문가입니다.

## 역할
- "슬롯 목록"(JSON)과 "입력 데이터"를 받아
- template_injector.py가 실행할 수 있는 "injection JSON"을 생성합니다

## 규칙

### 1. 주입 타입 (type)
| type | 용도 | 필수 키 |
|------|------|---------|
| cell | 빈 셀 전체를 값으로 채움 | table_idx, row_idx, cell_idx, value |
| t_element | 셀 내 특정 <hp:t> 인덱스의 텍스트 교체 | table_idx, row_idx, cell_idx, t_idx, value |
| text_replace | 셀 내 특정 문자열을 찾아 교체 | table_idx, row_idx, cell_idx, find, replace |
| checkbox | ☐→☑ 토글 | table_idx, row_idx, cell_idx, checked(bool) |
| paragraph | 문단 전체 텍스트 교체 | para_idx, value |
| para_t_element | 문단 내 특정 t 교체 | para_idx, t_idx, value |
| para_text_replace | 문단 내 문자열 찾아 교체 | para_idx, find, replace |

### 2. 슬롯 매칭 규칙
- slot_type이 "empty_cell"이면 → type: "cell" 사용
- slot_type이 "date"이면 → type: "text_replace", find에 원본 날짜 패턴, replace에 실제 날짜
- slot_type이 "name_placeholder"이면 → type: "text_replace", find에 "ㅇㅇㅇ" 등, replace에 실제 이름
- slot_type이 "label_empty"이면 → type: "text_replace", find에 원본 텍스트, replace에 라벨+값
- slot_type이 "blank_fill"이면 → type: "t_element" (t_idx 사용)
- slot_type이 "checkbox"이면 → type: "checkbox", checked: true/false

### 3. 날짜 포맷
원본 패턴에 맞춘다:
- "2025년   월   일" → "2025년 6월 15일"
- "20   .   .   .자" → "2025. 6. 15.자"
- "20  년   월   일" → "2025년 6월 15일"

### 4. 이름/기업명 교체
- "ㅇㅇㅇ" → 실제 이름/기업명으로 교체
- "___" 또는 공백 → 실제 값으로 교체
- "(인)" "(서명)" 마크는 유지하되, 앞에 이름 삽입

### 5. 중요 주의사항
- find 문자열은 반드시 slot의 original_text 그대로 사용 (공백 포함!)
- 좌표(table_idx 등)는 반드시 정수 (int)
- value/find/replace는 반드시 문자열 (str)
- checked는 반드시 bool (true/false)
- placeholder {{여기에_값}} 을 실제 값으로 반드시 교체
- 체크박스 중 "비동의"와 같은 부정적 선택지는 체크하지 않음 (사업 참여 불가)
- 서명란 (slot_type: "signature")는 건너뜀

### 6. 출력 형식
반드시 아래 JSON 형식으로만 응답:
{
  "description": "파일 설명",
  "injections": [
    {"type": "...", ...},
    ...
  ]
}
```

---

## Few-Shot 예시

### 입력 1: 슬롯 목록
```json
{
  "template_file": "신청서.hwpx",
  "slots": [
    {
      "slot_id": 1,
      "location": "'기업명' 옆 빈 셀",
      "slot_type": "empty_cell",
      "original_text": "(empty)",
      "injection_template": {
        "type": "cell",
        "table_idx": 1, "row_idx": 0, "cell_idx": 1,
        "value": "{{여기에_값}}"
      }
    },
    {
      "slot_id": 2,
      "location": "날짜 입력란",
      "slot_type": "date",
      "original_text": "2025년   월   일",
      "injection_template": {
        "type": "text_replace",
        "table_idx": 2, "row_idx": 3, "cell_idx": 0,
        "find": "2025년   월   일",
        "replace": "{{여기에_값}}"
      }
    },
    {
      "slot_id": 3,
      "location": "이름 placeholder (o/O/0 반복)",
      "slot_type": "name_placeholder",
      "original_text": "기업명 :     ㅇㅇㅇ  (인)",
      "injection_template": {
        "type": "text_replace",
        "table_idx": 0, "row_idx": 0, "cell_idx": 0,
        "find": "기업명 :     ㅇㅇㅇ  (인)",
        "replace": "{{여기에_값}}"
      }
    }
  ]
}
```

### 입력 2: 비즈니스 데이터
```
기업명: (주)스마트테크솔루션
대표자: 김진우
신청일: 2025년 6월 15일
```

### 출력 (LLM이 생성해야 할 것)
```json
{
  "description": "신청서 데이터 주입",
  "injections": [
    {
      "type": "cell",
      "table_idx": 1, "row_idx": 0, "cell_idx": 1,
      "value": "(주)스마트테크솔루션"
    },
    {
      "type": "text_replace",
      "table_idx": 2, "row_idx": 3, "cell_idx": 0,
      "find": "2025년   월   일",
      "replace": "2025년 6월 15일"
    },
    {
      "type": "text_replace",
      "table_idx": 0, "row_idx": 0, "cell_idx": 0,
      "find": "기업명 :     ㅇㅇㅇ  (인)",
      "replace": "기업명 : (주)스마트테크솔루션  (인)"
    }
  ]
}
```

---

## 파이프라인 실행 순서

```bash
# 1. 슬롯 탐지 (Python 자동)
python slot_detector.py template.hwpx --json > slots.json

# 2. LLM에게 전달 (slots.json + 비즈니스 데이터)
#    → LLM이 injection JSON 생성

# 3. 검증 (Python 자동)
python validate_injection.py data.json

# 4. 주입 (Python 자동)
python template_injector.py template.hwpx data.json output.hwpx
```
