# Troubleshooting - 해결된 문제 기록

> Phase 1 개발 중 발생한 문제와 해결 방법 아카이브
> 
> **목적:** 유사 문제 재발 시 빠른 해결, 다음 양식 개발 시 참고

---

## 작성 규칙

### 형식
```markdown
## [YYYY-MM-DD] 문제: 간단한 제목

### 증상
- 어떤 문제가 발생했는가
- 에러 메시지, 현상

### 원인
- 왜 발생했는가

### 해결 방법
- 어떻게 해결했는가
- 코드/설정

### 참고
- 표준 스펙 위치
- 관련 이슈
```

### 작성 시점
- ✅ 문제 **해결 완료** 후
- ❌ 해결 중에는 `CURRENT_ISSUES.md` 사용

---

## 해결된 문제들

<!-- 
아래부터 해결된 문제 기록
최신이 위로
-->

## [2025-11-17] 문제: 주제목/강조 표 규격이 스타일 문서와 다름

### 증상
- 주제목 표의 1/3행이 10pt 높이로 표시되어 상단·하단 여백이 두꺼워짐.
- 강조 박스 배경색이 스타일 문서의 #CDF2E4 대신 연노랑(#FFF7CC)으로 출력됨.
- 전체적으로 폰트 매핑이 흔들리면서 다른 영역에서 의도치 않은 글꼴 크기가 나타남.

### 원인
- 표의 1·3행을 비워두면 Hangul이 해당 셀의 run을 자동 삽입하면서 charPr ID 0(본문 15pt)을 재사용해 높이가 늘어남.
- `borderFill` ID 6이 연노랑으로 정의되어 있어 강조 표가 항상 #FFF7CC로 채워짐.
- charPr 슬롯을 임시로 재배치하면서 주제목/강조와 spacer가 ID를 공유해 버렸고, Hangul의 “charPr ID ≤8” 제약 때문에 폰트가 뒤섞임.

### 해결 방법
1. `char_defs`에 1pt 전용 charPr(ID 9) 추가 후 주제목 표 1/3행에서 해당 ID와 공백 한 글자를 강제로 넣어 셀 높이를 1pt로 고정.
2. 주제목 표 셀 마진을 0으로 맞춰 배경 블록만 남도록 조정하고, 가운데 행은 기존 HY 15pt ID로 유지.
3. `borderFill` ID 6을 #CDF2E4 로 수정해 강조 표가 스타일 문서와 동일한 색상을 사용하도록 변경.
4. 표 주변 spacer는 기존 4pt ID를 계속 쓰고, 일반 문단에 쓰이는 charPr ID 5–8은 원래 매핑(주제목, 소제목, 설명3, 강조)으로 되돌려 전체 폰트가 안정적으로 적용되도록 함.
5. 수정 후 `output/test_run.hwpx`를 한글에서 열어 표 규격과 배경색이 정확하게 나오는지 확인.

### 참고
- 관련 코드: `converter/md_to_hwpx.py` (char_defs, TITLE_TABLE_ROW_HEIGHTS, `_append_title_table`, borderFills)
- 테스트 파일: `output/test_run.hwpx`

## [2025-11-17] 문제: 한글에서 용지가 “사용자 정의/가로”로 표시됨

### 증상
- `style_textbook` 대로 A4 세로 문서를 만들었는데, 한글 UI에서는 “용지 종류: 사용자 정의”, “용지 방향: 가로”로 표기됨.
- 줄 여백은 정상 적용되었으나, 페이지 설정이 뒤틀려 추가 편집 시 예상치 못한 레이아웃이 나옴.

### 원인
- `section0.xml`의 `<hp:pagePr>` 너비/높이를 mm→HWPUNIT으로 변환하면서 반올림(283.46…)을 사용해 Hangul이 내부 템플릿과 다른 값을 기록함. 이때 문서를 “사용자 정의”로 분류.
- `landscape` 속성을 NARROWLY로 두면 Hangul이 자체적으로 회전을 시도하면서 뷰어에서 가로처럼 보이는 버그가 재현됨.

### 해결 방법
1. Hangul이 사용하는 정확한 HWPUNIT 값을 `test_minimal_manual.hwpx`에서 추출해 상수(`59528×84186`)로 정의하고, mm 변환 함수는 내림(`int(mm * 283.464566929)`)으로 맞춤.
2. `hp:pagePr`에 `landscape="WIDELY"`를 지정해 세로 레이아웃을 확정하고, 여백/머리말/꼬리말도 동일한 단위로 기록.
3. footnote/endnote/pageBorderFill/colPr 등 템플릿과 동일한 섹션 메타데이터를 추가하여 Hangul이 문서를 표준 A4로 인식하도록 맞춤.
4. 수정 후 `output/test_run.hwpx`를 한글에서 열어 “용지: A4, 방향: 세로, 여백: 20/20/15/15 + 10mm”로 표시되는지 확인.

### 참고
- 관련 파일: `converter/md_to_hwpx.py` (`mm_to_hwp`, `PAGE_*` 상수, `build_section0_xml` 내 `hp:pagePr`/footnote/colPr 추가)
- 비교 기준: `converter/test_minimal_manual.hwpx` 의 `Contents/section0.xml`

## [2025-11-17] 문제: 스타일 텍스트가 기본 바탕글 폰트로 돌아감

### 증상
- spacer 줄은 정상 높이를 유지하지만 주제목/소제목/본문/설명 계열 텍스트가 모두 기본 바탕글 폰트(맑은 고딕 10pt)로 표시됨.
- charPr ID 5~11에 매핑된 스타일이 존재함에도 한글에서 열면 폰트/크기 차이가 사라지고 기본 서식으로 fallback.

### 원인
- Hangul은 **동일한 paraPr(바탕글)**를 공유하는 문단에서 run-level charPr ID가 8을 초과하면 height/폰트를 무시하고 기본값으로 되돌리는 제약이 있음.
- RUN_CHAR_OVERRIDE_MAP을 제거하고 styleIDRef만으로 charPr을 참조했을 때, 한글이 해당 스타일의 charPr ID(9+)를 동일한 제약으로 취급하며 무시.
- header.xml의 charPr 정의도 0/1/2 외 ID에 대해 Hangul이 fallback 하면서 stile_textbook 요구사항이 깨짐.

### 해결 방법
1. `converter/md_to_hwpx.py`에서 RUN_CHAR_OVERRIDE_MAP을 재도입하여 각 BlockType이 **ID 0~8 범위**만 사용하도록 지정 (본문/설명2=0, 주제목=5, 소제목=6, 설명3=7, 강조=8 등).
2. `build_header_xml()`의 char_defs 테이블을 ID 0~8까지만 남기고 각 스타일의 폰트/크기를 해당 ID에 재배치. Spacer용 1~4는 유지, 텍스트 스타일은 5~8에 할당.
3. style_defs 및 STYLE_ID_MAP, RUN_CHAR_OVERRIDE_MAP이 동일한 charPr ID를 가리키도록 업데이트.
4. 한글에서 `output/test_run.hwpx` 확인 시 모든 스타일이 명세대로 출력되는지 검증.

### 참고
- 관련 이슈: `converter/CURRENT_ISSUES.md` – “Spacer 줄(라인스페이서) 폰트/크기 미스매치”
- 수정 라인: `converter/md_to_hwpx.py` (RUN_CHAR_OVERRIDE_MAP, char_defs, style_defs, section0 run 생성부)

## [2025-11-15] 문제: charPr ID 9 이상이 무시되어 줄 높이가 틀어짐

### 증상
- spacer 줄을 10/8/6/4pt로 세팅했음에도 한글에서 4/15/10/10pt처럼 기본 바탕글 값으로 표시됨.
- charPr ID를 9, 10, 11 등으로 부여한 일반 본문 스타일도 동일하게 폰트 크기와 줄 높이가 무시됨.

### 원인
- 한글이 **바탕글 paraPr(paraPrIDRef=0)**에서 run-level charPr를 해석할 때 ID 0~8 범위까지만 라인 높이에 반영하고, 그 이상 ID는 기본값으로 되돌리는 제약이 존재.
- spacer/본문 모두 paraPr 0을 공유하고 있었기 때문에, ID 9 이상을 사용하면 항상 fallback이 발생함.

### 해결 방법
1. spacer 전용 charPr를 1~4 범위로 재배치하여 10/8/6/4pt가 정확히 나오도록 수정.
2. 본문/설명/강조용 charPr도 6~8 범위 안에 최대한 배치하고, 추가 스타일이 필요하면 **새 paraPr/style을 만들어 그 문단에서만 높은 ID를 쓰도록** 설계해야 함.
3. `converter/md_to_hwpx.py`에서 charPr ID를 정의할 때 “바탕글 공유 영역(0~8)”과 “개별 스타일 영역(9+)”을 명시적으로 구분하도록 주석을 추가.
4. [2025-11-15 추가] `output/test_styled8.hwpx` 점검 결과, 스타일 ID 1~6(본문 charPr 8)은 요구사항과 일치하지만 예비 스타일 7/9/10/11은 다른 paraPr/charPr 세팅으로 인해 명령과 다른 폰트·정렬·pt가 적용됨. 예비 스타일 사용 시 문건에 혼선이 있는지 추가 검증 필요.

### 참고
- 테스트 파일: `output/test_styled6.hwpx` (spacer 1~4 성공, 9 이후 실패 사례 포함)
- 관련 이슈: `CURRENT_ISSUES.md` 항목 “Spacer 줄(라인스페이서) 폰트/크기 미스매치”

## [2025-11-15] 문제: 생성한 HWPX가 한글에서 열리지 않음

### 증상
- `md_to_hwpx.py`로 만든 문서를 한글에서 열면 “문서 변환코드를 선택하라”는 오류가 뜨고, 내용이 깨진 바이너리처럼 보임.

### 원인
- OCF/HWPX 패키지 구성요소가 빠져 있었음.
  - `META-INF/manifest.xml`, `META-INF/container.rdf`, `contents/content.hpf`의 spine 등이 누락.
  - `version.xml` 속성도 최소값만 들어 있어서 Hancom 뷰어가 패키지를 인정하지 못함.

### 해결 방법
1. `test_inputmodel.hwpx`, `test_minimal_manual.hwpx`를 비교 분석해 필수 파일/속성을 정리.
2. `md_to_hwpx.py`에 다음 빌더를 추가/수정:
   - `build_manifest_xml()`, `build_container_rdf()`, `build_container_xml()` (rootfile 2개 등록).
   - `build_content_hpf()`에서 manifest/spine/metadata를 표준대로 생성.
   - `build_version_xml()` 속성 보완.
3. `write_hwpx()`에서 누락된 XML을 ZIP에 포함하고, `mimetype`를 `application/hwp+zip`으로 수정.
4. 새로 생성한 `output/test_styled?.hwpx`를 한글에서 열어 정상 동작 확인.

### 참고
- 관련 이슈: `converter/CURRENT_ISSUES.md` (2025-11-15 이전 기록)
- 스펙 링크: `docs/hwpx_spec.md`
- 비교용 샘플: `converter/test_inputmodel.hwpx`

---

<!-- 예시 (실제 문제 발생 시 이 예시 삭제)

## [2024-11-15] 문제: 줄간격이 140%로 나옴

### 증상
- 설정은 160%인데 생성된 HWPX에서 140%로 표시
- 한글 프로그램에서 확인 시 줄간격 틀림

### 원인
- HWPX 표준에서 줄간격은 비율이 아닌 절대값 사용
- 160% = 1.6이 아니라 특정 단위 값 필요

### 해결 방법
```python
# Before (잘못된 방법)
line_spacing = 1.6

# After (올바른 방법)
line_spacing = 160  # 단위: %를 의미하는 정수값
```

### 참고
- 표준 스펙: `docs/hwpx_spec.md` 섹션 3.2.4
- 검색: `python tools/spec_search.py "줄간격 line-spacing"`

-->
