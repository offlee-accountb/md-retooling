# Current Issues - 진행중인 이슈

> Phase 1 개발 중 **현재 해결 중인** 문제들
>
> **목적:** AI 간 인수인계, 컨텍스트 유지, 중복 시도 방지

---

## ⚠️ 중요

이 파일은 **진행중인 이슈만** 기록합니다.

**해결되면:**

1. 내용을 `TROUBLESHOOTING.md`로 이동
2. 이 파일에서 삭제 또는 [해결됨] 표시

---

## 작성 규칙

### 형식

```markdown
## [진행중] 이슈 제목

**우선순위:** High / Medium / Low  
**담당 AI:** 마지막으로 작업한 AI 이름

### 상황

- 현재 어떤 상태인가
- 어디까지 진행됐는가

### 시도한 방법들

1. [AI명 - 날짜] 방법1 → 결과
2. [AI명 - 날짜] 방법2 → 결과

### 다음 AI에게

- 시도해볼 접근
- 참고할 스펙 위치
- 주의사항

### 관련 파일

- 영향받는 파일들
```

---

## 진행중인 이슈

---

## [진행중] 2025-11-28 – 표 색상/테두리 미적용 (대제목/강조/요약)

**우선순위:** High  
**담당 AI:** GitHub Copilot (2025-11-27~28)

### 증상

- 대제목 표 1,3행: 연보라 배경(`#EBDEF1`) 없음
- 강조 표: 연두 배경(`#CDF2E4`) 없음
- 요약표: 점선 테두리 아닌 실선 또는 선 없음
- **stylebook 정의대로 색상/테두리가 출력에 반영되지 않음**

### 분석 과정

#### 1차 시도: `add_border_fill_custom()` 호출 수정

- **가설**: `fill_brush`만 전달하고 `borders` 누락
- **수정**: ID 101-104에 `borders` + `fill_brush` 둘 다 전달
- **결과**: ❌ 변화 없음

```python
# 수정한 코드 (라인 ~2274-2312)
add_border_fill_custom(
    101,
    borders={
        "left": ("SOLID", "0.12 mm"),
        "right": ("SOLID", "0.12 mm"),
        "top": ("SOLID", "0.12 mm"),
        "bottom": ("SOLID", "0.12 mm"),
    },
    fill_brush={"faceColor": "#EBDEF1", "hatchColor": "#999999", "alpha": "0"},
)
# ID 102, 103, 104도 동일하게 수정
```

#### 2차 시도: `<tbl>` 태그의 borderFillIDRef 수정

- **가설**: 테이블 셀(`<tc>`)은 ID 101-104를 참조하지만, `<tbl>` 태그 자체는 `"3"`을 참조
- **발견**:
  | 테이블 | `<tbl>` borderFillIDRef | `<tc>` borderFillIDRef |
  |--------|------------------------|------------------------|
  | 대제목 | "3" ❌ | 101, 102 ✅ |
  | 강조 | "3" ❌ | 103 ✅ |
  | 요약 | "104" ✅ | 104 ✅ |
- **수정 위치**:
  - 라인 1311: 대제목 `<tbl>` → `TITLE_TABLE_SPACER_BORDER_ID` (101)
  - 라인 1427: 강조 `<tbl>` → `EMPH_TABLE_BORDER_ID` (103)
- **결과**: ❌ 변화 없음

### 현재 상태

- header.xml에 borderFill ID 101-104 정의 **존재함** (확인 완료)
- 테이블 함수에서 `<tc>` 태그에 올바른 borderFillIDRef **사용함**
- `<tbl>` 태그의 borderFillIDRef도 **수정 완료**
- **그러나 출력에 색상/테두리가 여전히 반영되지 않음**

### 미확인 사항 (다음 AI에게)

1. **header.xml과 section0.xml의 참조 관계**
   - borderFill ID가 header.xml에 정의되어 있어도, section0.xml에서 참조 시 ID 매핑이 다를 수 있음?
2. **HWPX 표준 스펙 확인 필요**
   - `<tbl borderFillIDRef>`와 `<tc borderFillIDRef>` 중 어느 것이 우선하는지?
   - borderFill의 `<hc:fillBrush>` 구조가 올바른지?
3. **실제 출력 파일 검증**

   - 생성된 hwpx를 unzip하여 header.xml의 borderFill 101-104 정의 확인
   - section0.xml에서 `<tc borderFillIDRef="101">` 등이 실제로 존재하는지 확인

4. **참조용 정상 파일과 비교**
   - `validator/tier_test_inputmodel/(2-1)test_inputmodel.hwpx`의 구조와 비교
   - 정상 작동하는 표가 어떤 borderFill 구조를 사용하는지

### 시도할 수 있는 접근

1. **출력 hwpx 직접 분석**: unzip 후 header.xml, section0.xml 비교
2. **정상 inputmodel과 diff**: 색상이 올바르게 적용된 파일과 구조 비교
3. **fillBrush 구조 확인**: `<hc:winBrush>` 대신 다른 요소가 필요할 수 있음
4. **borderFill ID 범위 확인**: 한글에서 특정 ID 범위만 인식할 가능성

### 관련 파일

- `converter/md_to_hwpx.py`:
  - 라인 212-215: 상수 정의 (TITLE_TABLE_SPACER_BORDER_ID 등)
  - 라인 1274-1389: `_append_title_table()` 함수
  - 라인 1391-1470: `_append_emphasis_table()` 함수
  - 라인 1709-1870: `_append_summary_table()` 함수
  - 라인 2029-2065: `add_border_fill_custom()` 함수 정의
  - 라인 2272-2315: borderFill ID 101-104 정의
- `converter/style_textbook.md`: stylebook 색상 정의
- `validator/tier_test_inputmodel/(2-1)test_inputmodel.hwpx`: 참조용 정상 파일

---

## [진행중] Phase1.5 Validator가 실제 문서와 불일치 리포트 다수 발생

**우선순위:** High  
**담당 AI:** GitHub Copilot (2025-11-16)

### 상황

- `validator/cli.py templates/phase1_5_sample.yaml output/test_final.hwpx --format text` 실행 시 7개의 ERROR가 연속적으로 발생.
- 증상: YAML 템플릿은 8개 미만 블록(제목/메타 표/요약/불릿/노트/결재 표/서명)을 기대하나, 실제 `output/test_final.hwpx`는 Phase1 변환기의 기본 보고서 텍스트라 구조가 완전히 다름.
- 현재 validator 로직은 table/list/text 순서를 엄격 비교하기 때문에 실제 문서가 기대 템플릿과 다르면 모든 블록이 실패 처리됨.

### 시도한 방법들

1. [Copilot - 11/16] Phase1.5 validator 코어 구현 (`validator/phase1_5_validator.py`) 및 CLI 연동 → 정상적으로 HWPX를 열어 diff 출력하지만, 템플릿과 내용이 달라 모든 블록이 실패됨.
2. [Copilot - 11/16] section0.xml 파싱 시 중복 namespace 제거 및 spacer 문단 건너뛰기 로직 추가 → XML 파싱 오류 해결, 텍스트/테이블 비교까지 수행됨.

### 다음 AI에게

- 템플릿을 실제 Phase1 출력과 맞춰 업데이트하거나, validator에서 BlockType 매핑(예: 제목 테이블 → 실제 표 구조) 규칙을 도입해야 함.
- HWPX 문서 파싱 시 paraPrIDRef/charPrIDRef 기반으로 BlockType을 추정하는 로직이 아직 없음. 이를 도입하면 템플릿에 현재 BlockType 대신 스타일 기준 규칙을 쓸 수 있음.
- 리스트(`bullet_section`)는 현재 “marker로 시작하는 연속 문단”만 감지하므로, Phase1 출력에 맞춰 marker/정규식 조건을 재설계 필요.
- 참고 파일: `validator/phase1_5_validator.py`, `templates/phase1_5_sample.yaml`, `output/test_final.hwpx`.

### 관련 파일

- `validator/phase1_5_validator.py`
- `validator/cli.py`
- `templates/phase1_5_sample.yaml`
- `output/test_final.hwpx`

## [해결됨] Spacer 줄(라인스페이서) 폰트/크기 미스매치

**우선순위:** Medium  
**담당 AI:** Codex (2025-11-17)

### 상황

- style_textbook 규칙에 따라 spacer(소제목/본문/설명2/설명3 사이 공백 줄)를 각각 10/8/6/4pt 맑은 고딕으로 넣어야 함.
- 2025-11-15 분석 결과: **바탕글 문단에서 run-level charPr ID가 0~8 범위를 벗어나면 한글이 높이를 무시**하고 기본값으로 되돌린다.
  - spacer ID를 1~4로 낮추면 정확히 10/8/6/4pt로 표시되는 것이 확인됨.
  - 본문/설명 스타일을 위해 6 이상 ID를 사용했더니 9번 이후부터 다시 fallback 증상이 반복됨.
- `<hp:linesegarray>`는 쓰지 않기로 했으며, 순수하게 run의 charPr/paraPr 조합으로 줄간격을 제어해야 한다는 요구 그대로 유지.
- `output/test_styled8.hwpx` 기준: **스타일 ID 1~6(본문은 charPr 8)만 요구사항을 정확히 준수**하고 있으며, 예비 스타일 7/9/10/11은 현재 폰트·정렬·pt값이 사양과 다름. 예비 스타일이 잘못 쓰이지 않도록 추가 가이드 필요.

### 시도한 방법들

1. [Codex - 11/15] spacer용 paraPr/style을 따로 정의 → **한글에서 기본 스타일로 덮여 보임**
2. [Codex - 11/15] spacer 문단을 바탕글 스타일로 통일하고 run에만 charPr 10~13 (맑은고딕 10/8/6/4pt) 적용 → **한글 결과에서 여전히 4/15/10/10pt로 관측됨**
3. [Codex - 11/15] spacer charPr ID를 1~4로 낮춰 재배치 → **한글에서 정확히 10/8/6/4pt로 동작**
4. [Codex - 11/15] 일반 텍스트 charPr를 6~12로 이동 → **ID 9 이후 다시 fallback 발생 (문제 재현)**
5. [Codex - 11/15] 문단 run-level charPr를 제거하고 styleIDRef→header의 charPr에 의존하도록 수정 → **HWP에서 검증 필요 (style 경유 시 charPr ID 제한이 풀리는지 확인 예정)**
6. [Codex - 11/17] charPr ID 0~8 범위만 재사용하도록 header.xml/런 매핑 재배치 (본문/설명2=0, 주제목=5, 소제목=6, 설명3=7, 강조=8) 및 RUN_CHAR_OVERRIDE_MAP 복구 → **Hangul에서 spacer/본문/제목 모두 의도대로 표시됨 (확인 완료)**

### 다음 AI에게

- Hangul 0~8 제약을 준수하는 한 추가 작업 불필요. 새 스타일이 필요하면 charPr ID 0~8 범위에서 재배치하거나 전용 paraPr를 도입해야 함.
- `converter/TROUBLESHOOTING.md`에 해결 기록 남김. 추가 재현 시 해당 문서를 참고.
- 참고: `output/test_styled6.hwpx`, `output/test_run.hwpx`

### 관련 파일

- `converter/md_to_hwpx.py` (`build_header_xml`, `build_section0_xml`)
- 출력 예시: `output/test_styled6.hwpx`

<!-- 예시 형식 (실제 이슈 발생 시 참고)

## [진행중] 제목 스타일이 적용 안됨

**우선순위:** High
**담당 AI:** GitHub Copilot (2024-11-15)

### 상황
- h1 제목을 18pt 굵게로 설정했으나 실제 HWPX에서 12pt로 나옴
- h2는 정상 작동

### 시도한 방법들
1. [Copilot - 11/15] styles.py에서 크기 직접 지정 → 실패
2. [Copilot - 11/15] HWPX XML에서 직접 수정 → 부분 성공 (굵기만)

### 다음 AI에게
- 표준 스펙 3.1.2 "제목 스타일" 섹션 참고 필요
- CharShape과 ParaShape 두 곳 모두 설정해야 할 가능성
- 검색: `python tools/spec_search.py "제목 heading style"`

### 관련 파일
- `converter/hwpx_generator.py` (L45-67)
- `converter/styles.py` (L12-24)

-->
