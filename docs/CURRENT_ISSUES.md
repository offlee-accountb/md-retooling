# CURRENT_ISSUES

> 이 파일은 Phase 1.x/1.5 진행 중 발견된 열린 이슈를 요약합니다.

## 2025-11-18 – Phase 1.5 Header/Footer 패턴

### 현상

- `converter/md_to_hwpx.py`에서 Tier1 샘플을 기준으로 머리말/꼬리말 HWPX 구조를 구현했으나, 실제 한글(HWP) 표시 결과가 기대와 다름.
- 테스트 대상: `converter/sample_input.md` → `output/test_final.hwpx`.
- 한글에서 열었을 때 관측한 결과:
  - 머리말: **화면 상에 노출되지 않음** (section0.xml에는 header ctrl 구조가 있음).
  - 꼬리말: 내용(`"꼬리말 테스트"`)은 보이지만, **정렬 없음 + 휴먼명조 15pt 정도로 표시**.

### 구현 상태 (2025-11-18 기준)

- Tier1 `(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx`의 `Contents/section0.xml`을 역공학하여 다음 패턴을 맞춤:
  - 머리말(header):
    - 위치: 첫 문단(`hp:p id="0"`) 안, 제목 테이블(`hp:tbl`)이 들어있는 `hp:run` 바로 뒤에 `hp:ctrl/hp:header` 삽입.
    - 구조: `hp:header@id="1" applyPageType="BOTH"` → `hp:subList` → `hp:p id="0"` → `hp:run` → `hp:t`(탭 + 텍스트).
    - 코드: `_append_header_footer_ctrl`에서 header용 `hp:p`에 `paraPrIDRef="8"`, `styleIDRef="0"`를 사용.
  - 꼬리말(footer):
    - 위치: 첫 SUBTITLE 문단(`paraPrIDRef == PARA_STYLE_MAP[BlockType.SUBTITLE]`) 안의 선행 run으로 `hp:run/hp:ctrl/hp:footer` 삽입.
    - 구조: `hp:footer@id="3" applyPageType="BOTH"` → `hp:subList` → `hp:p id="0"` → `hp:run` → `hp:t`(꼬리말 텍스트).
    - 코드: footer용 `hp:p`에 `paraPrIDRef="9"`, `styleIDRef="0"`를 사용.
- `build_section0_xml`의 말미에서:
  - `_build_header_footer_text(doc_meta)`로 헤더/푸터 텍스트 생성.
  - `_append_header_footer_ctrl(root, header_text, footer_text)`를 `try/except`로 호출하여 section0 완성 후 ctrl 주입.

### 원인(의심)

- **스타일/paraPr 정의 불일치 가능성**
  - Tier1 샘플의 `header.xml`과 현재 변환기가 사용하는 `header.xml`의 paraPr/charPr 및 style 정의가 다름.
  - `paraPrIDRef="8"`, `"9"`가 머리말/꼬리말용 오른쪽 정렬 스타일로 정의되어 있지 않을 수 있음.
- **머리말 표시 옵션/뷰 모드 차이 가능성** (사용자 환경 요인)
  - section0.xml에는 `hp:header`가 존재하지만, 한글 UI에서 머리말/꼬리말 숨기기 옵션/보기 모드에 따라 비가시적일 수 있음.
- **오른쪽 정렬 구현 방식 차이**
  - 탭 + paraPr 조합만으로는 실제 기관 양식과 동일한 위치/폰트/정렬을 재현하지 못한 상황.

### 영향 범위

- 현재 Tier0/Tier1 샘플을 변환했을 때:
  - 문서는 정상 오픈.
  - 본문/제목/강조 테이블 등 기존 Phase 1.5 기능은 정상 작동.
  - 머리말/꼬리말은 **구조적으로 존재하지만, 시각적 스타일이 스타일북 요구와 다름**.
- 상위 Phase(표 템플릿, 요약표 등) 작업에 앞서, 머리말/꼬리말 스타일 정의를 보수해야 함.

### To-Do / Next Steps

1. Tier1 with_header 샘플의 `header.xml`과 현재 변환기의 `header.xml`을 diff 비교.
   - 특히 paraPr id="8", id="9" 및 관련 charPr, style 정의를 검토.
   - 필요 시 header/footer 전용 paraPr/charPr를 별도로 정의하고, 변환기에서 해당 ID를 사용하도록 수정.
2. 머리말 표시 여부/옵션 검증.
   - 동일 HWPX를 다른 PC/설치 환경에서 열어 머리말 노출 여부 확인.
   - (선택) 머리말 내부 텍스트에 눈에 띄는 테스트 문자열을 넣어 실제 렌더링 여부를 재확인.
3. 꼬리말 정렬/폰트 검증.
   - 꼬리말 문단이 실제로 어떤 paraPr/charPr를 물고 있는지 한글 스타일 창으로 확인.
   - 휴먼명조 15pt로 표시되는 원인이 header.xml 기본 스타일 때문인지 확인 후, 기관 스타일(예: 바탕글 11pt)로 맞추는 paraPr/charPr 정의 추가.
4. 문서화/테스트 연계.
   - 위 수정이 끝나면 Tier0/Tier1 샘플을 다시 변환하여, validator Tier 테스트 + 수동 눈검 검증 절차를 정리.
   - 머리말/꼬리말 관련 회귀 테스트 케이스를 `tests/fixtures`에 추가하는 것을 고려.

---

(이 섹션은 GitHub Copilot가 2025-11-18 기준 상태를 요약한 것입니다. 이후 수정 시 날짜/상태를 갱신해 주세요.)

## [해결됨] 2025-11-27 – Phase 1.5 표 색상/테두리 수정 완료

### 해결된 문제

1. **대제목 표 1,3행**: 연보라 배경(#EBDEF1) + 0.12mm 실선 테두리 적용
2. **대제목 표 본문(2행)**: 0.12mm 실선 테두리 (배경 없음)
3. **강조 표**: 연두 배경(#CDF2E4) + 0.4mm 실선 테두리 적용
4. **요약표**: 점선(DOTTED) 0.12mm 테두리 적용
5. **꼬리말**: 하드코딩된 "꼬리말 테스트" → 빈 문자열로 변경

### 수정 내용

- `converter/md_to_hwpx.py`의 `add_border_fill_custom()` 호출부 수정
  - ID 101: `borders` 파라미터 추가 (SOLID 0.12mm) + 연보라 fillBrush
  - ID 102: `borders` 파라미터 추가 (SOLID 0.12mm)
  - ID 103: `borders` 파라미터 추가 (SOLID 0.4mm) + 연두 fillBrush
  - ID 104: 점선 두께 0.5mm → 0.12mm로 수정
- `_build_header_footer_text()`: 꼬리말 하드코딩 제거

### 주의사항 (AI 인수인계)

- borderFill 정의 시 `borders` 파라미터를 누락하면 테두리가 NONE으로 설정됨
- `fill_brush`만 있으면 배경색만 적용되고 테두리는 없음
- 둘 다 필요하면 반드시 두 파라미터 모두 명시할 것

---

## [해결됨] 2025-11-20 – Phase 1.5 표 보더/이중실선 불일치

### 현상

- 표 헤더/본문 보더가 스타일북·Tier1 샘플과 다르게 렌더링됨.
- 헤더 배경(연보라) 누락, 오른쪽 열의 상/하 보더가 다른 행과 다름.
- 중간 행 하단이 모두 굵은 실선으로 깔리거나, 마지막 행 얇은 실선만 남는 등 행·열별 보더 매핑이 일관되지 않음.

### 구현 상태

- `converter/md_to_hwpx.py`에서 double-slim 테두리를 위해 borderFill 12~17을 정의하고, 헤더/중간행/마지막행에서 셀 좌·우 위치에 따라 ID를 매핑하도록 수정함.
- 표 파서는 `<표 제목 : ...>` 뒤의 빈 줄을 건너뛰도록 보완했으며, 마커(◦/-,\*, bullet 변형)를 관용적으로 인식하도록 확장됨.
- **2025-11-27 해결됨**: borderFill ID 101~104에 올바른 borders/fillBrush 정의 적용.

### 해결 방법

- `add_border_fill_custom()` 호출 시 `borders` 딕셔너리를 명시적으로 전달
- 대제목/강조/요약표 각각의 borderFill ID에 스타일북 요구사항 반영
