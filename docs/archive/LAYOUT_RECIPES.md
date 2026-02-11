# HWPX Layout Recipes (Phase 1)

Phase 1에서 주제목·강조 표 같은 고정 규격을 반복 구현하면서 얻은 경험치를 정리했습니다. 새로운 LLM 에이전트나 향후 윈도우에서도 동일한 스타일을 빠르게 재현할 수 있도록 레시피 방식으로 문서화합니다.

도구 버전: `converter/md_to_hwpx.py` 기준 (`output/test_run.hwpx` 확인 완료)

---

## 1. 페이지/섹션 공통 설정

- `landscape="WIDELY"` + `width="59528"` + `height="84186"` → A4 세로
- 여백: 좌/우 20 mm, 상/하 15 mm, 머리말/꼬리말 10 mm (`mm_to_hwp` 참고)
- `secPr`에 다음 요소를 반드시 포함
  - `hp:grid`, `hp:startNum`, `hp:visibility`, `hp:lineNumberShape`
  - `hp:footNotePr`, `hp:endNotePr`
  - `hp:pageBorderFill` ×3 (BOTH/EVEN/ODD)
  - `hp:ctrl/hp:colPr` (단일 칼럼)
- `build_section0_xml()`에서 첫 문단 run에 `_attach_secpr()` 호출로 위 내용을 주입

## 2. CharPr / ParaPr / Style ID 매핑

| BlockType              | ParaPr ID | CharPr ID | Style ID | 비고                           |
|------------------------|-----------|-----------|----------|--------------------------------|
| 주제목 (`<주제목>`)    | 1         | 5         | 1        | HY헤드라인M 15 pt Bold         |
| 소제목 (`□`)           | 2         | 6         | 2        | HY헤드라인M 15 pt              |
| 본문 (`◦`)            | 3         | 0         | 3        | 휴먼명조 15 pt                 |
| 설명2 (`   -`)        | 4         | 0         | 4        | 휴먼명조 공유                  |
| 설명3 (`    *`)       | 5         | 7         | 5        | 맑은 고딕 12 pt               |
| 강조 (`<강조>`, `◈`)  | 6         | 8         | 6        | 휴먼명조 15 pt Bold            |
| 표 1/3행 filler       | -         | 9         | -        | 맑은 고딕 1 pt (ID 9)          |
| spacer (줄간 확보)    | -         | 1~4       | -        | 10/8/6/4 pt 맑은 고딕          |

> **주의**: Hangul은 paraPr=바탕글(paraPrIDRef=0)일 때 run-level `charPrID > 8`을 무시합니다. 의도적으로 필요한 경우 paraPr를 분리하거나 0~8 범위 내에서 재배치하세요.

## 3. BorderFill ID 규칙

| ID | 설명                    | 색상                                   |
|----|------------------------|----------------------------------------|
| 1  | 기본 (투명)            | 없음                                   |
| 2  | 기본 + winBrush        | `faceColor=none`, hatch `#999999`      |
| 3  | 표 외곽선              | 없음                                   |
| 4  | 주제목 2행 (본문 셀)   | 없음 (테두리만)                       |
| 5  | 주제목 1·3행 배경      | `#EBDEF1` + hatch `#999999`           |
| 6  | 강조 박스 배경         | `#CDF2E4` + hatch `#999999`           |

## 4. 주제목 표 (TITLE_TABLE)

구조: `hp:p → hp:run → hp:tbl`  
수치 비교: `test_inputmodel.hwpx` 참조

| 항목           | 값 / 설명                                                   |
|----------------|-------------------------------------------------------------|
| `rowCnt`       | 3                                                           |
| `colCnt`       | 1                                                           |
| `hp:sz.height` | `TITLE_ROW1 (1 pt) + BODY (3174) + TITLE_ROW3 (1 pt)`       |
| `hp:pos`       | treatAsChar=0, flowWithText=1, vertRelTo=PARA, horzRelTo=COLUMN |
| `outMargin`    | 283 (좌/우/상/하)                                           |
| `inMargin`     | 510 (좌/우), 141 (상/하)                                    |

행별 설정:

| 행 | 텍스트      | paraPr/charPr      | cellSz.height | cellMargin | borderFill |
|----|-------------|--------------------|---------------|------------|-----------|
| 1  | `" "`       | `charPrID=9` (1 pt)| `ONE_PT_HWP`  | 0/0/0/0    | 5         |
| 2  | 실제 제목   | para=1, char=5     | 3174          | 1417/141/… | 4         |
| 3  | `" "`       | `charPrID=9`       | `ONE_PT_HWP`  | 0/0/0/0    | 5         |

구현 함수: `_append_title_table()`  
모든 표는 `table_id`를 증가시키며 zOrder와 id가 동일하도록 유지.

## 5. 강조 박스 (EMPHASIS_TABLE)

구조: `hp:p → hp:run → hp:tbl` (rowCnt=1)

| 항목           | 값 / 설명                                     |
|----------------|-----------------------------------------------|
| `hp:sz.height` | 2632                                          |
| `cellMargin`   | 566 (좌/우/상/하)                             |
| `borderFill`   | 6 (`#CDF2E4`)                                 |
| 셀 텍스트      | `◈ {block.text}`                              |
| para/char      | para=6, char=8 (휴먼명조 Bold 15 pt)          |

## 6. Spacer 규칙

| 대상             | charPr | 내용   | 넣는 위치                          |
|------------------|--------|--------|-----------------------------------|
| 소제목 전 spacer | ID 1   | `" "`  | Run 하나 (secPr 없음)             |
| 본문 전 spacer   | ID 2   | `" "`  | 동일                               |
| 설명2 전 spacer  | ID 3   | `" "`  |                                   |
| 설명3 전 spacer  | ID 4   | `" "`  |                                   |

`SPACER_MARKER_MAP` 텍스트는 `" "`로 통일 (과거 `↕10↕` 제거).

## 7. Inline Bold

`_append_text_with_bold()`는 `**강조**` 패턴을 탐지해 charPr ID 8 (강조) run을 삽입함.  
주의: 빈 문자열일 경우 조용히 반환하도록 업데이트됐으니, filler 행에서도 문제 없음.

## 8. 본문/설명 들여쓰기 & 줄 간격 가이드

- **행걸이(hanging indent)는 `margin.intent`만 사용**하고 `margin.left/right`는 0으로 둡니다. Hangul은 `left` 값이 존재하면 전체 문단을 이동시키므로, 의도치 않은 좌측 여백이 생깁니다.
- BlockType별 권장 intent (pt 단위 → HWPUNIT = pt×100):

| BlockType | paraPr ID | 표시 | intent (pt) | intent (HWPUNIT) |
|-----------|-----------|------|-------------|------------------|
| BODY (`◦`) | 9         | 내용 | 30 pt       | -3000            |
| DESC2 (`   -`) | 8     | 설명2| 37.5 pt     | -3750            |
| DESC3 (`    *`) | 10   | 설명3| 35 pt       | -3500            |

- intent 값은 음수로 설정하여 “첫 줄만 왼쪽으로 튀어나오고 나머지 줄은 기본 여백을 유지”하도록 합니다.
- 줄 간격 기본값: BODY/DESC2/DESC3 모두 `lineSpacing type="PERCENT" value="160"`. DESC3도 LEFT 정렬을 유지해 한글이 임의로 CENTER로 바꾸지 않도록 합니다.
- 들여쓰기/간격을 재조정할 때의 절차:
  1. `converter/md_to_hwpx.py` 의 `para_defs`에서 대상 paraPr의 `margin.intent`를 수정합니다.
  2. `output/*.hwpx`를 재생성하고 `Contents/header.xml`에서 해당 paraPr의 `intent`와 `left`가 정확히 기록됐는지 확인합니다.
  3. 필요 시 한글에서 문서를 열어 Shift+Tab 기준 위치와 동일한지 확인합니다. (권장값: 내용 30 pt, 설명2 37.5 pt, 설명3 35 pt)

- 추후 `hp:linesegarray`/`hp:lineseg`에 `flags=1441792`를 직접 넣으면 한글이 줄 영역을 재작성하지 않으므로, 문단 편집 시에도 들여쓰기가 유지됩니다.

---

## 향후 확장 아이디어

1. **HWpx → Recipe 자동화**: `test_minimal_manual.hwpx` 등 검증된 샘플을 파싱하고 JSON으로 변환하는 스크립트를 만들어 `_append_*` 헬퍼들의 파라미터로 자동 치환.
2. **템플릿 라이브러리화**: `_append_title_table` / `_append_emphasis_table` 같은 함수들을 별도 모듈로 분리해 재사용성과 테스트를 높임.
3. **문서화 지속**: 새로운 양식을 추가할 때마다 본 문서에 “레이아웃 레시피” 섹션을 확장해 다른 LLM/엔지니어가 즉시 참조 가능하게 유지.

---

## 참고 파일

- `converter/md_to_hwpx.py` – 구현 소스
- `converter/test_inputmodel.hwpx` – 레퍼런스 예시
- `output/test_run.hwpx` – 현재 규격이 적용된 산출물
- `converter/TROUBLESHOOTING.md` – 문제/해결 이력

필요시 레시피 항목을 자유롭게 추가/수정해주세요.

