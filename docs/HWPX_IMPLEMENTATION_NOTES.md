# HWPX 구현 참고사항 (Implementation Notes)

> **⚠️ 중요**: 이 문서는 실험을 통해 발견된 HWPX 규칙들입니다.
> 공식 표준(`hwpx_spec.md`)에 명시되지 않았지만, 실제 구현 시 반드시 지켜야 하는 사항들.
> 새로운 발견이 있으면 계속 추가됩니다.

---

# 1. charPr (글자 속성)

## 핵심 규칙 요약

### ✅ 반드시 지켜야 할 것

1. **charPr ID는 0부터 연속으로 사용** (0, 1, 2, 3, ...)
2. **연속 ID는 최소 40개까지 안전하게 작동** (exp7에서 확인)
3. **charPr 내부 순서**: `underline` → `strikeout` (이 순서 필수)
4. **strikeout 속성**: `shape="NONE"` (type 속성 없음!)
5. **section0.xml 첫 문단에 완전한 `<hp:secPr>` 필수** (빈 태그 금지)

### ❌ 하지 말아야 할 것

1. **불연속 ID 사용 금지** (예: 0, 1, 2, 4, 6, 8, 10)
   - 마지막 2~3개 ID가 적용되지 않음
2. **strikeout → underline 순서 금지** (파일 손상)
3. **`strikeout type="NONE"`** (잘못된 속성, shape만 사용)
4. **빈 `<hp:secPr />` 태그** (파일 손상)

---

## 실험 결과 테이블

| 실험 | ID 패턴 | 결과 | 비고 |
|------|---------|------|------|
| exp7 | 연속 0~39 (40개) | ✅ 모두 적용 | 성공 |
| exp14 | 연속 1~30 (30개) | ✅ 모두 적용 | 성공 |
| exp14 | 불연속 0,1,2,4,6,8,10 | ❌ 8,10 미적용 | 실패 |
| exp9 | 불연속 1~11,13~15 | ❌ 14,15 미적용 | 실패 |
| exp10 | 불연속 1~16,18~20 | ❌ 18~20 미적용 | 실패 |
| exp11~14 초기 | - | ❌ 파일 손상 | 구조 오류 |

---

## charPr 올바른 구조

```xml
<hh:charPr id="0" height="1000" textColor="#000000" ...>
    <hh:fontRef hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>
    <hh:ratio hangul="100" latin="100" hanja="100" japanese="100" other="100" symbol="100" user="100"/>
    <hh:spacing hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>
    <hh:relSz hangul="100" latin="100" hanja="100" japanese="100" other="100" symbol="100" user="100"/>
    <hh:offset hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>
    <hh:underline type="NONE" shape="SOLID" color="#000000"/>     <!-- ← 순서 1 -->
    <hh:strikeout shape="NONE" color="#000000"/>                  <!-- ← 순서 2, type 없음! -->
    <hh:outline type="NONE"/>
    <hh:shadow type="NONE" color="#B2B2B2" offsetX="10" offsetY="10"/>
</hh:charPr>
```

### 잘못된 구조 (파일 손상됨)

```xml
<!-- ❌ 잘못됨: strikeout이 먼저, type 속성 있음 -->
<hh:strikeout type="NONE" shape="SOLID" color="#000000"/>
<hh:underline type="NONE" shape="SOLID" color="#000000"/>
```

---

## section0.xml secPr 규칙

첫 번째 문단에 **완전한 `<hp:secPr>` 태그**가 필요합니다.

### ✅ 올바른 구조

```xml
<hp:p id="0" paraPrIDRef="0" styleIDRef="0" pageBreak="false" columnBreak="false" merged="false">
    <hp:run charPrIDRef="0">
        <hp:secPr id="0" textDirection="HORIZONTAL" spaceColumns="1134" 
                  tabStop="8000" outlineShapeIDRef="1" memoShapeIDRef="0" 
                  textVerticalWidthHead="false" masterPageCnt="0">
            <hp:grid lineGrid="0" charGrid="0" wonggojiFormat="false"/>
            <hp:startNum pageStartsOn="BOTH" page="0" pic="0" tbl="0" equation="0"/>
            <hp:pagePr landscape="NARROWLY" width="59528" height="84186" gutterType="LEFT_ONLY">
                <hp:margin header="4252" footer="4252" gutter="0" 
                          left="8504" right="8504" top="5668" bottom="4252"/>
            </hp:pagePr>
            <hp:footNotePr>...</hp:footNotePr>
            <hp:endNotePr>...</hp:endNotePr>
        </hp:secPr>
        <hp:t>텍스트</hp:t>
    </hp:run>
</hp:p>
```

### ❌ 잘못된 구조 (파일 손상)

```xml
<!-- 빈 secPr 태그 - 파일 안 열림 -->
<hp:p>
    <hp:run>
        <hp:secPr />
        <hp:t>텍스트</hp:t>
    </hp:run>
</hp:p>
```

---

## 권장 작업 순서

1. **템플릿 파일에서 시작**
   - `(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx` 권장
   
2. **header.xml 수정**
   - `fontfaces` 교체
   - `charProperties` 교체 (charPr ID 연속 확인!)
   - `paraProperties` 교체
   - `styles` 교체

3. **section0.xml 생성**
   - 첫 문단에 완전한 `secPr` 포함
   - 각 문단의 `charPrIDRef`가 유효한 charPr ID 참조하는지 확인

---

## 파일 손상 디버깅 체크리스트

파일이 열리지 않을 때:

- [ ] charPr 내 `underline` → `strikeout` 순서 확인
- [ ] `strikeout`에 `type` 속성 없는지 확인 (`shape`만 있어야 함)
- [ ] section0.xml 첫 문단에 완전한 `secPr` 있는지 확인
- [ ] charPr ID가 연속인지 확인 (0, 1, 2, 3, ...)
- [ ] 모든 `charPrIDRef`가 존재하는 charPr ID를 참조하는지 확인

---

---

# 2. paraPr (문단 속성)

## 핵심 규칙

- **paraPr ID도 0부터 연속으로 사용** (charPr과 동일)
- 연속 ID 30개까지 확인됨 (exp15)
- **불연속 ID 사용 금지** - 건너뛴 ID 이후는 전부 미적용

## 실험 결과 (exp15)

| ID 패턴 | 결과 |
|---------|------|
| 연속 0~29 (30개) | ✅ 모두 적용 |
| 0,1,2,3,4,5,7,9 | ✅ 적용 |
| 0,1,2,3,4,5,7,9,11,13,15 | ❌ 11,13,15 미적용 |
| 0,1,2,3,4,5,10,11,12 | ❌ 10,11,12 미적용 |

**결론:** 중간에 ID를 건너뛰면, 건너뛴 지점 이후의 ID는 적용되지 않음.

---

# 3. 공통 주의사항: 배열 인덱스 vs ID 혼동 방지

## ⚠️ 이 실수가 반복됨! (exp16에서 2회 발생)

HWPX에서 가장 흔한 실수: **배열의 순서(index)**와 **XML의 id 속성**을 혼동하는 것.

### 문제 상황 예시

```python
BORDERFILL_IDS = [0, 1, 2, 3, 4, 5]  # 테스트할 ID 목록
COLORS = [("none", "없음"), ("#FF0000", "빨강"), ("#FF8000", "주황"), ...]

for i, bid in enumerate(BORDERFILL_IDS):
    color = COLORS[i]  # ❌ 잘못됨! i=0일 때 COLORS[0]="없음"
    # bid=1일 때 i=1이지만, COLORS[1]="빨강"...
    # 매핑이 어긋남!
```

### 결과

- 텍스트: `[borderFill ID=1] 빨강` 
- 실제 배경: **흰색** (한 칸 밀림)

### 올바른 해결책

**ID를 직접 인덱스로 사용**:

```python
for i, bid in enumerate(BORDERFILL_IDS):
    color = COLORS[bid]  # ✅ bid 자체를 인덱스로!
    # bid=1이면 COLORS[1]="빨강" → 정확히 매핑
```

### 체크리스트

코드 작성 시 반드시 확인:

- [ ] `COLORS[i]` vs `COLORS[bid]` - 어느 것을 써야 하나?
- [ ] `paraPrIDRef`가 올바른 `paraPr id`를 가리키는가?
- [ ] `borderFillIDRef`가 올바른 `borderFill id`를 가리키는가?
- [ ] **테스트 문단의 라벨 텍스트**와 **실제 적용된 스타일**이 일치하는가?

### 디버깅 팁

색상이 "한 칸씩 밀렸다"면:
1. 배열 인덱스(`i`)와 ID(`bid`)를 혼동했을 가능성 높음
2. 라벨에 표시된 ID와 실제 참조 ID가 다른지 확인
3. `pageBorderFill`, 제목 문단 등 **다른 요소가 ID를 가져가지 않았는지** 확인

---

# 4. borderFill (테두리/배경)

## 핵심 규칙

### ✅ 반드시 지켜야 할 것

1. **borderFill ID는 1부터 시작** (0은 한글이 무시함)
2. **ID 1은 반드시 "색없음"** (`fillBrush` 태그 생략)
3. **연속 ID 사용** (1, 2, 3, 4, ... 20개 확인됨)
4. **네임스페이스**: `hc:fillBrush`, `hc:winBrush` 사용 (hh: 아님!)

### ❌ 하지 말아야 할 것

1. **ID 0 사용 금지** - 한글이 무시함
2. **ID 1에 색상 넣기 금지** - 모든 기본 텍스트/배경이 그 색으로 됨
3. **불연속 ID** - charPr/paraPr과 동일하게 문제 발생 예상

---

## borderFill 구조

### 색없음 (ID 1 - 기본값)

```xml
<hh:borderFill id="1" threeD="0" shadow="0" centerLine="NONE" breakCellSeparateLine="0">
    <hh:slash type="NONE" Crooked="0" isCounter="0"/>
    <hh:backSlash type="NONE" Crooked="0" isCounter="0"/>
    <hh:leftBorder type="NONE" width="0.1 mm" color="#000000"/>
    <hh:rightBorder type="NONE" width="0.1 mm" color="#000000"/>
    <hh:topBorder type="NONE" width="0.1 mm" color="#000000"/>
    <hh:bottomBorder type="NONE" width="0.1 mm" color="#000000"/>
    <hh:diagonal type="SOLID" width="0.1 mm" color="#000000"/>
    <!-- ⚠️ fillBrush 태그 없음 = 색없음 -->
</hh:borderFill>
```

### 색있음 (ID 2 이상)

```xml
<hh:borderFill id="2" threeD="0" shadow="0" centerLine="NONE" breakCellSeparateLine="0">
    <hh:slash type="NONE" Crooked="0" isCounter="0"/>
    <hh:backSlash type="NONE" Crooked="0" isCounter="0"/>
    <hh:leftBorder type="NONE" width="0.1 mm" color="#000000"/>
    <hh:rightBorder type="NONE" width="0.1 mm" color="#000000"/>
    <hh:topBorder type="NONE" width="0.1 mm" color="#000000"/>
    <hh:bottomBorder type="NONE" width="0.1 mm" color="#000000"/>
    <hh:diagonal type="SOLID" width="0.1 mm" color="#000000"/>
    <!-- ⚠️ hc: 네임스페이스 필수! (hh: 아님) -->
    <hc:fillBrush>
        <hc:winBrush faceColor="#FF0000" hatchColor="#000000" alpha="0"/>
    </hc:fillBrush>
</hh:borderFill>
```

---

## 참조 방법

### paraPr에서 배경색 참조

```xml
<hh:paraPr id="0" ...>
    ...
    <hh:border borderFillIDRef="2" offsetLeft="283" offsetRight="283" 
               offsetTop="283" offsetBottom="283" connect="0" ignoreMargin="0"/>
</hh:paraPr>
```

### 페이지 배경 (색없음으로 설정)

```xml
<hp:pageBorderFill type="BOTH" borderFillIDRef="0" textBorder="PAPER" ...>
    <!-- borderFillIDRef="0"으로 페이지 배경 없음 -->
</hp:pageBorderFill>
```

---

## 실험 결과 (exp16)

| 테스트 | 결과 | 비고 |
|--------|------|------|
| ID 0~20 연속 | ❌ ID 0 무시됨, 전체 빨강 | 0-based 실패 |
| ID 1~20 연속, ID 1=흰색 | ⚠️ 동작하지만 음영색 흰색 | 차선책 |
| ID 1~20 연속, ID 1=색없음 | ✅ 완벽 | 권장 |

---

## 자동 생성 시 권장 패턴

```python
def build_borderfill(bid: int, color: str = None) -> str:
    """
    borderFill 생성
    - bid: 1부터 시작 (0 사용 금지)
    - color: None이면 색없음, "#RRGGBB" 형식이면 해당 색
    """
    base = f'''<hh:borderFill id="{bid}" threeD="0" shadow="0" centerLine="NONE" breakCellSeparateLine="0">
<hh:slash type="NONE" Crooked="0" isCounter="0"/>
<hh:backSlash type="NONE" Crooked="0" isCounter="0"/>
<hh:leftBorder type="NONE" width="0.1 mm" color="#000000"/>
<hh:rightBorder type="NONE" width="0.1 mm" color="#000000"/>
<hh:topBorder type="NONE" width="0.1 mm" color="#000000"/>
<hh:bottomBorder type="NONE" width="0.1 mm" color="#000000"/>
<hh:diagonal type="SOLID" width="0.1 mm" color="#000000"/>'''
    
    if color:
        # 색있음 - fillBrush 추가 (hc: 네임스페이스!)
        base += f'''<hc:fillBrush><hc:winBrush faceColor="{color}" hatchColor="#000000" alpha="0"/></hc:fillBrush>'''
    
    base += '''</hh:borderFill>'''
    return base

# 사용 예:
borderfills = [
    build_borderfill(1),              # ID 1 = 색없음 (필수!)
    build_borderfill(2, "#FF0000"),   # ID 2 = 빨강
    build_borderfill(3, "#00FF00"),   # ID 3 = 초록
    # ...
]
```

---

# 5. YAML 기반 스타일 관리

## 핵심 아키텍처

모든 스타일 정의는 `templates/core_styles.yaml`에서 중앙 관리됩니다.
하드코딩 대신 YAML에서 동적으로 로드하여 유지보수성을 높였습니다.

### YAML → Converter 흐름

```
templates/core_styles.yaml
         │
         ▼
validator/template_loader.py
         │ StyleConfig 데이터클래스로 파싱
         ▼
CONFIG 전역 객체
         │
         ├──→ CONFIG.fonts          (폰트 정의)
         ├──→ CONFIG.char_styles    (charPr 정의)
         ├──→ CONFIG.para_styles    (paraPr 정의)
         ├──→ CONFIG.styles         (스타일 정의)
         ├──→ CONFIG.border_fills   (borderFill 정의)
         └──→ CONFIG.document_mode  (문서 모드 설정)
                  │
                  ├──→ style_mode: "stylebook" | "normal"
                  └──→ use_line_spacers: true | false
```

### YAML 기반으로 전환된 영역

| 영역 | 이전 방식 | 현재 방식 | 비고 |
|------|----------|----------|------|
| fonts | 하드코딩 리스트 | `CONFIG.fonts` | 폰트명, 타입 등 |
| charProperties | `char_defs` 딕셔너리 | `CONFIG.char_styles` | 연속 ID 자동 보장 |
| paraProperties | `para_defs` 딕셔너리 | `CONFIG.para_styles` | 중복 ID 문제 해결 |
| styles | `style_defs` 리스트 | `CONFIG.styles` | 19개 스타일 정의 |
| borderFills | `BORDER_FILLS` 리스트 | `CONFIG.border_fills` | ID 1=색없음 규칙 준수 |

### 장점

1. **단일 소스**: 모든 스타일이 한 파일에서 관리됨
2. **검증 용이**: YAML 포맷으로 휴먼리더블
3. **확장 용이**: 새 스타일 추가 시 YAML만 수정
4. **ID 연속성 보장**: 배열 순서대로 ID 할당

### 주의사항

⚠️ YAML 수정 시 반드시 확인:
- charPr/paraPr ID는 배열 순서대로 0, 1, 2, 3... 할당됨
- borderFill ID는 배열 순서대로 1, 2, 3, 4... 할당됨 (0 아님!)
- style ID는 YAML에 명시된 `id` 필드 사용

---

# 6. 레이아웃 레시피 (Layout Recipes)

Phase 1에서 주제목·강조 표 같은 고정 규격을 반복 구현하면서 얻은 경험치입니다.

## 6.1 페이지/섹션 공통 설정

- `landscape="WIDELY"` + `width="59528"` + `height="84186"` → A4 세로
- 여백: 좌/우 20 mm, 상/하 15 mm, 머리말/꼬리말 10 mm
- `secPr`에 반드시 포함할 요소:
  - `hp:grid`, `hp:startNum`, `hp:visibility`, `hp:lineNumberShape`
  - `hp:footNotePr`, `hp:endNotePr`
  - `hp:pageBorderFill` ×3 (BOTH/EVEN/ODD)
  - `hp:ctrl/hp:colPr` (단일 칼럼)

## 6.2 표 스타일링 구조

### borderFill ID 전략

기존 palette ID (1-33) 다음부터 순차적으로 부여: 34, 35, 36, 37...

⚠️ **절대 큰 값으로 점프하지 말 것** (예: 101+) — 일부 환경에서 인식 안 됨

### 현재 사용 중인 커스텀 borderFill ID

| ID  | 상수명                        | 용도         | 테두리      | 배경색           |
| --- | ----------------------------- | ------------ | ----------- | ---------------- |
| 34  | TITLE_TABLE_SPACER_BORDER_ID  | 대제목 1,3행 | NONE        | #EBDEF1 (연보라) |
| 35  | TITLE_TABLE_BODY_BORDER_ID    | 대제목 본문  | NONE        | 없음             |
| 36  | EMPH_TABLE_BORDER_ID          | 강조 표      | SOLID 0.12mm| #CDF2E4 (연두)   |
| 37  | SUMMARY_TABLE_BORDER_ID       | 요약표       | DOT 0.12mm  | 없음             |

### 표 XML 구조

```xml
<!-- 표 외곽 (container) -->
<hp:tbl borderFillIDRef="3">  <!-- SOLID 외곽선 -->
  <hp:tr>
    <!-- 각 셀 (cell-level 배경/테두리) -->
    <hp:tc borderFillIDRef="34">  <!-- 연보라 배경 -->
      ...
    </hp:tc>
  </hp:tr>
</hp:tbl>
```

### HWPX LineType2 유효 값

- `NONE`, `SOLID`, `DOT`, `DASH`, `DASH_DOT`, `DASH_DOT_DOT`, `LONG_DASH`
- `CIRCLE`, `DOUBLE_SLIM`, `SLIM_THICK`, `THICK_SLIM`, `SLIM_THICK_SLIM`
- ⚠️ `DOTTED`는 유효하지 않음! 반드시 `DOT` 사용

## 6.3 주제목 표 (TITLE_TABLE)

구조: `hp:p → hp:run → hp:tbl` (rowCnt=3, colCnt=1)

| 항목           | 값 / 설명                                                   |
|----------------|-------------------------------------------------------------|
| `hp:sz.height` | `TITLE_ROW1 (1 pt) + BODY (3174) + TITLE_ROW3 (1 pt)`       |
| `hp:pos`       | treatAsChar=0, flowWithText=1, vertRelTo=PARA, horzRelTo=COLUMN |
| `outMargin`    | 283 (좌/우/상/하)                                           |
| `inMargin`     | 510 (좌/우), 141 (상/하)                                    |

| 행 | 텍스트      | charPr     | cellSz.height | borderFill |
|----|-------------|------------|---------------|------------|
| 1  | `" "`       | 1 pt 폰트  | ONE_PT_HWP    | 5 (연보라) |
| 2  | 실제 제목   | 15 pt Bold | 3174          | 4 (투명)   |
| 3  | `" "`       | 1 pt 폰트  | ONE_PT_HWP    | 5 (연보라) |

## 6.4 강조 박스 (EMPHASIS_TABLE)

구조: `hp:p → hp:run → hp:tbl` (rowCnt=1)

| 항목           | 값 / 설명                                     |
|----------------|-----------------------------------------------|
| `hp:sz.height` | 2632                                          |
| `cellMargin`   | 566 (좌/우/상/하)                             |
| `borderFill`   | 6 (`#CDF2E4` 연두)                            |
| 셀 텍스트      | `◈ {block.text}`                              |

## 6.5 들여쓰기 & 줄 간격

### 핵심 규칙

- **행걸이(hanging indent)는 `margin.intent`만 사용**
- `margin.left/right`는 0으로 유지 (Hangul이 전체 문단을 이동시킴)
- intent 값은 음수 = "첫 줄만 왼쪽으로 튀어나옴"

### BlockType별 권장 intent

| BlockType | 표시 | intent (pt) | intent (HWPUNIT) |
|-----------|------|-------------|------------------|
| BODY (`◦`) | 내용 | 30 pt       | -3000            |
| DESC2 (`-`) | 설명2| 37.5 pt     | -3750            |
| DESC3 (`*`) | 설명3| 35 pt       | -3500            |

### 줄 간격

- 기본값: `lineSpacing type="PERCENT" value="160"`
- DESC3도 LEFT 정렬 유지 (CENTER 자동 전환 방지)

## 6.6 Spacer 규칙

| 대상             | charPr | 내용   |
|------------------|--------|--------|
| 소제목 전 spacer | ID 1   | `" "`  |
| 본문 전 spacer   | ID 2   | `" "`  |
| 설명2 전 spacer  | ID 3   | `" "`  |
| 설명3 전 spacer  | ID 4   | `" "`  |

> `use_line_spacers: false` 설정 시 스페이서 삽입 생략

## 6.7 Inline Bold

`**강조**` 패턴을 탐지해 강조용 charPr run을 삽입.
빈 문자열일 경우 조용히 반환.

---

# 7. linesegarray (줄 레이아웃 캐시)

## 개요

`<hp:linesegarray>`는 문단 내 각 줄의 레이아웃 정보를 담는 **캐시 데이터**입니다.
한글이 파일을 열 때 자동으로 계산하므로, **텍스트 주입 시 반드시 제거**해야 합니다.

## 문제 상황

기존 HWPX 템플릿에 텍스트를 주입하면 **긴 텍스트가 자동 줄바꿈되지 않는** 현상 발생.

### 원인

```xml
<!-- 원본 템플릿: 짧은 텍스트 → lineseg 1개 -->
<hp:p id="7">
    <hp:run><hp:t>(추진 배경)</hp:t></hp:run>
    <hp:linesegarray>
        <hp:lineseg textpos="0" vertpos="10802" ... flags="393216"/>
    </hp:linesegarray>
</hp:p>

<!-- 주입 후: 긴 텍스트인데 lineseg는 여전히 1개 → 줄바꿈 안 됨 -->
<hp:p id="7">
    <hp:run><hp:t>(추진 배경) 중소기업의 스마트공장 도입 시 기술 검증 및 실증 환경 부족 문제 해소하고...</hp:t></hp:run>
    <hp:linesegarray>
        <hp:lineseg textpos="0" vertpos="10802" ... flags="393216"/>  <!-- 여전히 1개! -->
    </hp:linesegarray>
</hp:p>
```

### lineseg 구조 분석

| 속성 | 설명 |
|------|------|
| `textpos` | 해당 줄의 시작 문자 인덱스 (0, 41, 84, ...) |
| `vertpos` | 세로 위치 (HWPUNIT) |
| `vertsize` | 줄 높이 |
| `horzsize` | 가로 크기 (페이지 너비) |
| `flags` | 첫 줄=`0x60000` (393216), 이후 줄=`0x160000` (1441792) |

정상적인 긴 텍스트:
```xml
<!-- 72자 텍스트 → lineseg 2개 -->
<hp:linesegarray>
    <hp:lineseg textpos="0" ... flags="393216"/>   <!-- 첫 줄 -->
    <hp:lineseg textpos="41" ... flags="1441792"/> <!-- 둘째 줄 -->
</hp:linesegarray>
```

## 해결 방법

### ✅ 권장: linesegarray 완전 제거

```python
import re

LINESEGARRAY_PATTERN = re.compile(
    r'<hp:linesegarray[^>]*>.*?</hp:linesegarray>', 
    re.DOTALL
)

def remove_linesegarray(xml_content: str) -> str:
    """linesegarray 제거 - 한글이 자동 재계산"""
    return LINESEGARRAY_PATTERN.sub('', xml_content)
```

### 결과

- `linesegarray` 없는 파일을 한글에서 열면 자동으로 레이아웃 재계산
- 긴 텍스트도 정상적으로 자동 줄바꿈됨

## 적용 위치

| 파일 | 함수 | 설명 |
|------|------|------|
| `injector/keyword_injector.py` | `_process_section()` | 키워드 주입 시 제거 |
| `injector/unified_injector.py` | `_process_section()` | 통합 주입 시 제거 |
| `converter/md_to_hwpx.py` | - | 직접 생성 시 linesegarray 미포함 |

## 주의사항

### 가끔 줄바꿈이 안 되는 경우

| 가능성 | 설명 | 확인 방법 |
|--------|------|----------|
| 일부 섹션만 제거됨 | section0.xml 외 다른 섹션 | 모든 section*.xml 처리 |
| 표 내부 셀 | `<hp:tc>` 안의 linesegarray | 표 셀 내부도 제거 필요 |
| 머리말/꼬리말 | masterPage.xml 내부 | masterPage도 처리 필요 |
| 텍스트박스 | `<hp:textart>` 등 특수 요소 | 해당 요소 내부 확인 |

### 제거 시 안전성

- 한글 2020 이상에서 테스트 완료
- 파일 손상 없음
- 저장 시 한글이 자동으로 linesegarray 재생성

## 관련 이슈

- `docs/TROUBLESHOOTING.md` 참고: "향후 과제: linesegarray flags 직접 제어"
- `docs/CURRENT_ISSUES.md` 참고: "linesegarray는 쓰지 않기로 함"

---

# 8. 추후 추가 예정

---

## 관련 문서

- `docs/hwpx_spec.md` - HWPX 공식 표준 (수정 금지)
- `docs/TROUBLESHOOTING.md` - 일반 트러블슈팅
- `docs/ARCHITECTURE.md` - 시스템 설계
- `converter/HANDOFF_TO_NEXT_AI.md` - AI 핸드오프 가이드

---

*마지막 업데이트: 2025년 1월 - YAML 기반 스타일 관리, Document Mode 추가*
