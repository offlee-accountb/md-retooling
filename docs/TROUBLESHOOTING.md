# TROUBLESHOOTING

> 변환기/검증기 사용 중 자주 발생하는 문제와 우회 방법을 정리합니다.

---

## 머리말/꼬리말이 보이지 않거나 정렬이 이상할 때 (Phase 1.5)

### 증상
- 입력: `converter/sample_input.md` → 출력: `output/test_final.hwpx`.
- 한글에서 열었을 때:
  - 머리말: 문서 상단에 아무 것도 보이지 않음.
  - 꼬리말: 텍스트(`"꼬리말 테스트"`)는 보이지만, 정렬이 "없음"으로 잡혀 있고, 폰트가 휴먼명조 15pt 근처로 표시됨.

### 내부 구조 확인 결과
- `unzip -p output/test_final.hwpx Contents/section0.xml`로 확인 시:
  - 머리말:
    - `hp:p id="0"` (제목 테이블이 있는 문단)의 `hp:run` 안에 `hp:tbl` 뒤에 다음과 같은 ctrl이 존재:
      ```xml
      <hp:ctrl>
        <hp:header id="1" applyPageType="BOTH">
          <hp:subList ... textWidth="48189" textHeight="2834">
            <hp:p id="0" paraPrIDRef="8" styleIDRef="0" ...>
              <hp:run charPrIDRef="0">
                <hp:t>
                  <hp:tab width="39188" leader="0" type="2" />
                </hp:t>
                추진단 자료 스타일 보고서 - ...
              </hp:run>
            </hp:p>
          </hp:subList>
        </hp:header>
      </hp:ctrl>
      ```
    - 즉, XML 상으로는 머리말 구조가 존재하며, 탭 + 텍스트 패턴도 들어가 있음.
  - 꼬리말:
    - 첫 SUBTITLE 문단(`paraPrIDRef="2"`) 안에 다음과 같은 ctrl이 존재:
      ```xml
      <hp:run ...>
        <hp:ctrl>
          <hp:footer id="3" applyPageType="BOTH">
            <hp:subList ... textWidth="48189" textHeight="2834">
              <hp:p id="0" paraPrIDRef="9" styleIDRef="0" ...>
                <hp:run charPrIDRef="0">
                  <hp:t>꼬리말 테스트</hp:t>
                </hp:run>
              </hp:p>
            </hp:subList>
          </hp:footer>
        </hp:ctrl>
      </hp:run>
      ```
    - 구조적으로는 Tier1 with_header 샘플과 동일한 위치/패턴을 따르고 있음.

### 가능한 원인
1. **`header.xml` 스타일 정의 불일치**
   - 변환기가 사용하는 `header.xml`에서:
     - `paraPr id="8"`, `id="9"`가 실제로 오른쪽 정렬 + 기관 요구 폰트(예: 바탕글 11pt)가 아닌, 기본/실험용 스타일로 정의되어 있을 수 있음.
   - Tier1 with_header 샘플의 `header.xml`과 비교했을 때:
     - 머리말/꼬리말용 paraPr/charPr의 정렬, 폰트, 크기 설정이 다를 가능성이 큼.

2. **한글 UI의 머리말/꼬리말 보기 옵션**
   - 한글 상단/하단에 머리말/꼬리말이 표시되지 않는 경우:
     - "보기" 탭 또는 페이지 레이아웃에서 머리말/꼬리말 표시 옵션이 꺼져 있을 수 있음.
   - 다만, 이 경우에도 꼬리말 텍스트는 보인다는 점에서, 스타일 정의 문제와 복합적으로 얽혀 있을 수 있음.

3. **오른쪽 정렬 구현 방식 차이**
   - 현재 구현은 "오른쪽 정렬 스타일 + 탭" 패턴을 Tier1 XML에서 그대로 모사했지만,
   - 실제 기관 문서에서는 paraPr/charPr, 탭 스톱, 마진 조합이 다르게 구성되어 있을 수 있음.

### 디버깅/우회 절차

#### 1단계: XML 구조 확인 (이미 완료된 절차)
```bash
cd /home/<user>/madenew1
unzip -p output/test_final.hwpx Contents/section0.xml | sed -n '1,120p'
```
- 머리말/꼬리말 `hp:header`/`hp:footer` 존재 여부와 `paraPrIDRef`/`charPrIDRef` 값을 확인.

#### 2단계: 스타일 정의 비교
1. Tier1 with_header 샘플에서 `header.xml` 추출:
   ```bash
   unzip -p validator/tier_test/tier1/with_header.hwpx Contents/header.xml > /tmp/header_with.xml
   ```
2. 현재 변환기가 사용하는 `header.xml` 추출:
   ```bash
   unzip -p output/test_final.hwpx Contents/header.xml > /tmp/header_current.xml
   ```
3. diff 비교:
   ```bash
   diff -u /tmp/header_with.xml /tmp/header_current.xml | less
   ```
4. 특히 다음 항목을 집중 확인:
   - `paraPr id="8"`, `paraPr id="9"`의 `align`, `lineSpacing`, `fontRef` 설정.
   - 머리말/꼬리말 전용 style(`hh:style`)이 있는지 여부.

#### 3단계: 임시 우회 (수동 편집)
- 문제를 재현/확인하기 위해, 한글에서 직접 스타일을 수정:
  1. `output/test_final.hwpx`를 한글에서 열기.
  2. 머리말/꼬리말 편집 모드로 들어가, 해당 문단을 선택 후 원하는 정렬/폰트로 변경.
  3. 저장 후 다시 `header.xml`을 추출하여, 한글이 실제로 어떤 paraPr/charPr를 사용하는지 확인.
- 이 정보를 바탕으로 변환기 쪽 `header.xml`에 동일한 paraPr/charPr 정의를 추가하고, `paraPrIDRef`/`charPrIDRef`를 그 ID로 맞추면 된다.

#### 4단계: 변환기 수정 방향 (가이드)
- 변환기 코드(`converter/md_to_hwpx.py`):
  - `_append_header_footer_ctrl`에서 현재는 상수 `"8"`, `"9"`를 paraPrIDRef로 사용 중.
  - 추후에는:
    - `HEADER_PARA_ID`, `FOOTER_PARA_ID` 상수를 별도 정의.
    - 이 값이 실제 `header.xml`에 존재하는지 검증하거나,
    - 존재하지 않을 경우 graceful fallback (예: PLAIN 스타일로 생성 + 로그 경고) 도입.
- 스타일 파일(`header.xml`):
  - Tier1 with_header 샘플의 머리말/꼬리말 paraPr/charPr 블록을 그대로 가져와 현재 변환기용 `header.xml`에 병합.

### 요약
- **문제 본질:** 머리말/꼬리말 XML 구조는 이미 Tier1 샘플과 거의 동일하게 생성되고 있지만, 한글에서 보이는 정렬/폰트는 `header.xml`의 스타일 정의 차이 때문에 기관 요구와 다름.
- **현재 상태:** 구조는 안정, 스타일 튜닝(paraPr/charPr 정의 동기화)이 남아 있는 상태.
- **권장 조치:** Tier1 샘플의 머리말/꼬리말 스타일 정의를 현재 변환기 `header.xml`에 반영하고, 관련 ID를 상수로 관리하여 추후 양식 추가 시 재사용 가능하게 설계.

---

(이 섹션은 GitHub Copilot가 2025-11-18 기준 머리말/꼬리말 관련 트러블슈팅 상황을 정리한 것입니다.)

## 표 헤더/본문 보더·색상 어긋날 때 (Phase 1.5)

### 증상
- 헤더 행 배경(연보라) 누락, 이중실선이 일부 셀에만 적용.
- 오른쪽 열 상/하 보더가 다른 열과 다르게 얇은 실선 혹은 없음으로 표시.
- 중간 행 하단이 모두 굵은 실선으로 깔리거나 마지막 행만 얇은 실선으로 남는 등 행·열별 보더 불일치.

### 확인 포인트
1. `Contents/header.xml`의 borderFill 정의:
   - Tier1 샘플 기준 double-slim 세트: id 12~17 (위 DOUBLE_SLIM 0.5mm, 좌·우 0.12mm 조합).
   - 헤더 배경용 id 7(연보라 + top SOLID 0.12 / bottom DOUBLE 0.5 / 좌·우 없음).
2. `Contents/section0.xml`에서 테이블 셀별 borderFillIDRef:
   - 헤더: 좌/중/우 = 12/13/14, 본문 중간행: 15/16/17, 마지막행: 8(얇은 실선).
3. 마크다운 표 제목 뒤에 빈 줄이 있는지 여부 (빈 줄이 있으면 과거 버전에서 표 감지 실패 가능).

### 수정/우회 절차
1. Tier1 샘플(`validator/tier_test_inputmodel/(2-1)test_inputmodel.hwpx`)과 현재 산출물의 `header.xml`을 diff해 12~17 정의가 동일한지 확인.
2. `section0.xml`에서 표 헤더/본문 각 셀의 `borderFillIDRef`를 행·열별로 점검:
   - 헤더 행: 좌 12, 중 13, 우 14
   - 본문 중간행: 좌 15, 중 16, 우 17
   - 마지막 행: 8
3. 필요 시 새로운 borderFill ID(19+)를 추가해 오른쪽 열 전용/마지막 행 전용 테두리를 분리하고, `_append_markdown_table`의 매핑을 조정.
4. 헤더 배경이 사라지면 id 7을 헤더 행에 강제 적용하거나, 테이블 전체 borderFill이 덮어쓰지 않는지 확인.

### 참고
- 최신 파서는 `<표 제목 : ...>` 뒤의 빈 줄을 건너뛰고 파이프로 시작하는 줄을 표로 인식함. 탭은 스페이스로 자동 치환됨.
