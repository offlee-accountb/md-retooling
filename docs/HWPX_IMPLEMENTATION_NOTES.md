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

# 5. 추후 추가 예정

---

## 관련 문서

- `docs/hwpx_spec.md` - HWPX 공식 표준 (수정 금지)
- `docs/TROUBLESHOOTING.md` - 일반 트러블슈팅
- `docs/ARCHITECTURE.md` - 시스템 설계
- `converter/HANDOFF_TO_NEXT_AI.md` - AI 핸드오프 가이드

---

*마지막 업데이트: 2024년 11월 - exp16 borderFill 실험 추가*
