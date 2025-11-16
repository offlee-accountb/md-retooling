# Phase 1.5 가이드 (YAML 기반 Validator)

> Option B 실행 가이드: YAML 스키마를 단일 소스로 삼아 변환기와 검증기를 묶는 Phase 1.5 워크플로우
>
> **목표:** 최대 8개 필드의 공문서 양식을 YAML로 기술하고, 변환기 출력(HWPX)이 해당 스키마와 일치하는지 자동 검증

---

## Phase 1.5 목표 & 성공 기준

### 최종 산출물
- **구성 파일:** `templates/phase1_5_sample.yaml` (최대 8개 블록 정의)
- **입력 데이터:** `tests/fixtures/input/*.md` (기존 Phase 1 입력 재사용)
- **검증 파이프라인:** `validator/phase1_5_validator.py` + `validator/cli.py`
- **결과물:**
  - 변환된 HWPX (`output/*.hwpx`)
  - 검증 리포트 (`output/*.report.json` 또는 CLI stdout)

### 성공 기준
- [ ] YAML 스키마만 수정하면 변환기/검증기 모두 새로운 요구사항을 공유한다.
- [ ] `python validator/cli.py templates/phase1_5_sample.yaml output/sample.hwpx` 실행 시 구조/스타일 diff가 출력된다.
- [ ] 실패 리포트에 최소한 다음 정보가 포함된다: `block_id`, `expected`, `actual`, `severity`.
- [ ] `tests/integration/phase1_5_pipeline.py` (추가 예정)에서 end-to-end 흐름이 통과한다.

---

## 산출물 & 디렉터리 구조

```text
converter/
├── PHASE1_5_GUIDE.md        # 이 문서
├── PHASE1_GUIDE.md          # Phase 1 레거시 가이드
└── md_to_hwpx.py            # 변환기 (재사용)

templates/
└── phase1_5_sample.yaml     # Phase 1.5 기본 스키마 (최대 8개 블록)

validator/
├── cli.py                   # CLI 엔트리포인트 (Phase 1.5)
├── phase1_5_validator.py    # YAML ↔ HWPX 비교 로직
└── report_writer.py         # JSON/텍스트 리포트 유틸 (선택)

tests/
└── fixtures/
    ├── input/               # 입력 MD 샘플
    ├── output/              # 승인된 HWPX 샘플
    └── hwpx_samples/        # 비교용 HWPX (선택)
```

---

## 워크플로우 개요

1. **YAML 스키마 작성**
   - 문단/표/제목 등 최대 8개 블록을 `templates/phase1_5_sample.yaml`에 정의
   - 각 블록은 `type`, `id`, `text`, `style`, `constraints` 등을 가짐
2. **MD → HWPX 변환**
   - `python converter/md_to_hwpx.py --input tests/fixtures/input/okok1-1-1.md --output output/okok1-1-1.hwpx`
   - 변환기는 아직 Phase 1 로직을 사용하되, YAML의 `id`와 `style`을 참고하도록 점진 개선
3. **Validator 실행**
   - `python validator/cli.py templates/phase1_5_sample.yaml output/okok1-1-1.hwpx`
   - 파서는 HWPX XML을 열어 YAML과 비교, mismatch를 누적
4. **리포트 확인**
   - CLI stdout 또는 `--report output/okok1-1-1.report.json` 옵션으로 상세 결과 저장
   - 실패 항목은 `CURRENT_ISSUES.md`에 링크

---

## YAML 스키마 설계 원칙

| 항목            | 설명 |
|-----------------|------|
| `meta`          | 양식 이름, 버전, 작성자 정보 |
| `document`      | 용지, 여백, 기본 스타일 (Phase 1 값 재사용)|
| `blocks[]`      | 순서가 보장된 최대 8개 블록 (제목, 본문, 표, 서명 등)|
| `blocks[].type` | `title`, `body`, `table`, `note`, `signature` 등 확장 가능 |
| `blocks[].id`   | validator가 diff를 표시할 때 사용할 고유 키 |
| `blocks[].text` | 예상 문자열 (정확 일치 또는 정규식) |
| `blocks[].style`| `font`, `size`, `bold`, `align`, `line_spacing`, `border`, `padding` 등 |
| `blocks[].constraints` | 필수 여부, 반복 허용 여부, 열 수 등 |

추가 규칙:
- YAML은 Phase 1 입력 규칙(예: `<주제목>`, `□ 항목`)과 매핑이 분명해야 한다.
- 필드가 8개를 초과하면 별도 템플릿으로 분리한다 (Phase 1.5 스코프 유지).
- 문자열 비교는 기본적으로 trim + normalize-space 후 수행. 필요시 `match: regex` 옵션을 둔다.

---

## Validator 구성 요소

### `validator/cli.py`
- `argparse` 기반 CLI
- 인자: `--template`, `--hwpx`, `--report`, `--fail-on warn|error`
- 흐름: 템플릿 로딩 → HWPX 파싱 → `Phase15Validator` 호출 → 리포트 출력

### `phase1_5_validator.py`
- 책임 분리:
  1. `YamlTemplate` 데이터클래스: 로딩 및 유효성 검사
  2. `HwpxDocument` 래퍼: section0.xml, header.xml을 객체 형태로 노출
  3. `Phase15Validator`: 각 블록 비교, diff 생성
- 필수 체크 항목:
  - 블록 순서: YAML 배열 순서와 HWPX 문단 순서가 일치하는가
  - 텍스트: exact/regex 옵션에 따라 비교
  - 스타일: charPr/paraPr ID 참조가 YAML style 요구와 일치하는가
  - 표: 행/열 수, border 스타일, 셀 텍스트

### 리포트 포맷
```json
{
  "template": "phase1_5_sample.yaml",
  "hwpx": "output/okok1-1-1.hwpx",
  "summary": {"passed": 6, "failed": 2},
  "findings": [
    {
      "block_id": "title_main",
      "severity": "error",
      "field": "text",
      "expected": "<주제목> 사업 개요",
      "actual": "<주제목> 사업 개요(안)",
      "hint": "마크다운 입력 또는 스타일 레시피 확인"
    }
  ]
}
```

---

## 테스트 전략

1. **단위 테스트** (`tests/unit/`)
   - YAML 로더, HWPX 파서, 스타일 비교 함수 각각 검증
2. **통합 테스트** (`tests/integration/phase1_5_pipeline.py`)
   - MD → HWPX → Validator 전체 흐름 실행
3. **회귀 샘플** (`tests/fixtures/hwpx_samples/`)
   - 이전에 통과한 HWPX를 보관하고, 스키마 업데이트 시 diff 비교
4. **CI Hook (선택)**
   - `phase0_smoke_test.py` 이후 `validator/cli.py` 실행을 추가하여 회귀 차단

## Tier 테스트 추적 (Option B)
- Tier별 샘플과 실행 로그는 `docs/phase1.5_tiers.md` 한 곳에서만 관리한다. 필요 시 전체 파일을 보관/폐기하여 Option B 작업 흔적을 일괄 정리할 수 있다.
- 사용자(또는 차기 에이전트)가 제공하는 샘플은 `validator/tier_test/tier0~tier3/`에 넣고, 검증 후 결과를 같은 문서의 Run Log에 자유 형식으로 기록한다.
- `docs/ARCHITECTURE.md`에는 1~2줄 수준의 Option B 요약만 유지하고, 세부 진행 상황은 반드시 위 전용 문서에 적는다.

---

## 운영 노트

- **스키마 변경 절차**
  1. `templates/*.yaml` 수정
  2. `tests/fixtures/input/*.md`에 대응되는 예제 업데이트
  3. 변환기/validator 통합 테스트 실행
  4. `CURRENT_ISSUES.md`에 주요 변경 기록

- **디버깅 팁**
  - HWPX는 ZIP이므로 `unzip -p output/foo.hwpx Contents/section0.xml | xmllint --format -` 으로 즉시 확인
  - YAML ↔ HWPX 매핑 표를 `docs/LAYOUT_RECIPES.md`에 추가하여 다음 에이전트와 공유

- **Phase 2.x로 확장 시**
  - YAML 스키마를 JSON Schema로 정식 정의 → VS Code 자동 완성 제공
  - Validator를 FastAPI로 감싸 REST API 제공
  - LLM(Phase 2)에서 생성된 MD를 바로 Phase 1.5 파이프라인으로 흘려 품질 확인

---

**2025-02-15 초안 작성 (Option B 합의 반영)**
