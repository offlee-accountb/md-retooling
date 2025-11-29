# HWPX Injector

템플릿 HWPX에 데이터를 주입하는 통합 도구

## 구조

```
injector/
├── template_analyzer.py   # 템플릿 분석기 (타입 감지, 필드 추출)
├── unified_injector.py    # 통합 주입기 (3가지 모드 지원)
├── exp_inject.py          # 기존 POC (참고용)
└── README.md
```

## 사용법

### 1. 템플릿 분석

```bash
cd injector
python template_analyzer.py ../input/test_templates/tier1_1_body_only.hwpx
```

또는 unified_injector로:
```bash
python unified_injector.py ../input/test_templates/tier1_1_body_only.hwpx --analyze
```

### 2. 데이터 주입

```bash
python unified_injector.py \
  ../input/test_templates/tier1_1_body_only.hwpx \
  --data ../input/test_data/tier1_data.json \
  --output ../output/tier1_result.hwpx
```

## 지원 모드

### Mode 1: Placeholder ({{KEY}})
```json
{"TITLE": "문서 제목", "NAME": "홍길동"}
```

### Mode 2: 정부 양식 (name 속성)
```json
{"STSU_MAST*BUSI_NM": "데이터인프라구축"}
```

### Mode 3: 좌표 기반
```json
{
  "tables": {
    "0": {
      "1,2": "값1",
      "2,3": "값2"
    }
  }
}
```

### 혼합 사용 가능
```json
{
  "TITLE": "제목",
  "STSU_MAST*BUSI_NM": "사업명",
  "tables": {"0": {"1,0": "셀값"}}
}
```

## 테스트 파일

### Tier 1 (기초)
- `tier1_1_body_only.hwpx`: 본문에 {{TITLE}}, {{NAME}}, {{DATE}} 만
- `tier1_2_table_simple.hwpx`: 표 안에 {{A}}, {{B}}, {{C}}

### Tier 2 (복합)
- `tier2_1_mixed.hwpx`: 본문 + 표 혼합
- `tier2_2_no_tags.hwpx`: 태깅 없는 표 (좌표 기반 테스트)

### Tier 3 (실전)
- `tier3_1_gov_form.hwpx`: 정부 양식 (name 속성)
- `tier3_2_full_complex.hwpx`: (1-2) 수준 초복합

## 테스트 데이터

- `input/test_data/tier1_data.json` - Tier 1용
- `input/test_data/tier2_data.json` - Tier 2용 (좌표 포함)
- `input/test_data/tier3_gov_data.json` - 정부 양식용
