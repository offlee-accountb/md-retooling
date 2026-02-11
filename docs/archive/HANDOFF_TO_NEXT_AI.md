# AI 인수인계 문서 (Handoff Document)

**작성일:** 2025-11-15
**이전 담당 AI:** Claude (Anthropic)
**상태:** HWPX 파일 생성 성공, 하지만 한글 프로그램에서 **여전히 열리지 않음**

---

## 🎯 현재 프로젝트 목표

**Markdown → HWPX 변환기 개발** (Phase 1)

- 입력: `converter/sample_input.md` (특수 규칙 기반 마크다운)
- 출력: 한글(HWP) 프로그램에서 열리는 HWPX 파일
- 목표 양식: 정부 공문서 기본 양식 (`converter/test_inputmodel.hwpx` 참조)

---

## 📂 프로젝트 구조 개요

```
madenew1/
├── converter/                          # 메인 작업 디렉토리
│   ├── md_to_hwpx.py                  # 🔴 현재 변환기 (문제 있음)
│   ├── sample_input.md                # 테스트 입력 파일
│   ├── style_textbook.md              # 정부 양식 스타일 정의
│   ├── test_inputmodel.hwpx           # ✅ 정상 동작하는 참조 파일
│   ├── test_minimal_manual.hwpx       # ✅ 최소 구조 참조 파일
│   │
│   ├── PHASE1_GUIDE.md                # 📘 개발 가이드 (필독)
│   ├── PHASE1_INPUT_FORMAT.md         # 입력 MD 규칙 정의
│   ├── hwpxparshingguide.md           # HWPX 파싱 가이드
│   ├── CURRENT_ISSUES.md              # 🚨 진행중인 이슈
│   ├── TROUBLESHOOTING.md             # 해결된 문제 기록
│   └── EXTERNAL_LLM_REQUEST.md        # 외부 LLM 요청 템플릿
│
├── docs/
│   ├── hwpx_spec.md                   # HWPX 표준 스펙 (KS X 6101)
│   ├── ARCHITECTURE.md                # 전체 시스템 설계
│   └── AI_COLLABORATION_GUIDE.md      # AI 협업 가이드
│
├── tools/
│   └── spec_search.py                 # HWPX 스펙 검색 도구
│
├── output/                            # 생성된 HWPX 파일들
│   ├── test_final.hwpx               # 🔴 최신 생성 파일 (열리지 않음)
│   ├── test_fixed3.hwpx              # 이전 시도
│   └── test_fixed2.hwpx              # 이전 시도
│
└── old handoff/
    └── md_to_hwpx_old.py             # ✅ 이전 성공 버전 (참고용)
```

---

## 🚨 현재 문제 상황

### 증상

`md_to_hwpx.py`로 생성한 HWPX 파일을 한글 프로그램에서 열면:
- "문서 변환코드를 선택하라"는 오류 메시지
- 파일 내용이 깨져서 바이너리 데이터처럼 출력됨

### 생성 명령어

```bash
python3 converter/md_to_hwpx.py converter/sample_input.md output/test_final
```

### 시도한 해결 방법 (모두 실패)

1. ✅ **필수 패키지 파일 추가**
   - `META-INF/manifest.xml` 추가
   - `META-INF/container.rdf` 추가
   - `content.hpf`에 manifest/spine 섹션 추가
   - 결과: 여전히 안 열림

2. ✅ **XML namespace prefix 수정**
   - `ns0:` → `ocf:`, `hv:` 등 정확한 prefix 사용
   - `ET.register_namespace()` 활용
   - 결과: namespace는 올바르나 여전히 안 열림

3. ✅ **header.xml 구조 개선** (이전 성공 버전 참고)
   - fontfaces: 7개 언어 전부 정의 (HANGUL, LATIN, HANJA, JAPANESE, OTHER, SYMBOL, USER)
   - borderFills: 2개 정의 (fillBrush 포함)
   - tabProperties: 3개 정의
   - numberings: 10개 레벨 paraHead 정의
   - 결과: 구조는 참조 파일과 유사하나 여전히 안 열림

---

## 📊 파일 비교 분석 결과

### ✅ 정상 동작하는 파일들

**test_inputmodel.hwpx** (복잡한 예제):
```
mimetype
version.xml
settings.xml
META-INF/manifest.xml
META-INF/container.xml
META-INF/container.rdf
Contents/header.xml       (복잡, 많은 스타일)
Contents/section0.xml     (본문 내용)
Contents/content.hpf
Preview/PrvImage.png
Preview/PrvText.txt
```

**test_minimal_manual.hwpx** (최소 예제):
```
mimetype
version.xml
settings.xml
META-INF/manifest.xml
META-INF/container.xml
META-INF/container.rdf
Contents/header.xml       (단순, 최소 스타일)
Contents/section0.xml     (간단한 텍스트)
Contents/content.hpf
Preview/PrvImage.png
Preview/PrvText.txt
```

### 🔴 현재 생성 파일 (test_final.hwpx)

```
mimetype
version.xml              ✅ 속성 완전
settings.xml             ✅ CaretPosition 포함
META-INF/manifest.xml    ✅ 추가됨
META-INF/container.xml   ✅ container.rdf 참조 포함
META-INF/container.rdf   ✅ 추가됨
Contents/header.xml      ✅ 7개 언어, tabPr, numberings 포함
Contents/section0.xml    ⚠️ 많은 문단 (sample_input.md 전체)
Contents/content.hpf     ✅ manifest/spine 포함
```

**Preview 파일 없음** (선택사항이므로 문제 아님)

---

## 🔍 의심되는 원인

### 1. section0.xml 내부 구조 문제 (가능성 높음)

현재 `build_section0_xml()` 함수는:
- 모든 MD 블록을 단순 `<hp:p>` 문단으로 변환
- 첫 문단에만 `<hp:secPr>` (페이지 설정) 포함
- **표(table) 구조 없음**

하지만 `style_textbook.md`에 따르면:
- `<주제목>`과 `<강조>`는 **표 안에** 들어가야 함
- 소제목/본문/설명 앞에는 **여백 확보용 빈 줄** 필요

**⚠️ 표 구조 미구현이 핵심 문제일 가능성**

### 2. header.xml의 미세한 차이

참조 파일(`test_minimal_manual.hwpx`)과 비교:
- ✅ fontfaces 구조 유사 (7개 언어)
- ✅ borderFills 구조 유사
- ✅ charPr/paraPr 기본 구조 유사
- ⚠️ **charPr/paraPr 개수 차이**
  - 참조: charPr 8개, paraPr 20개
  - 현재: charPr 1개, paraPr 1개

### 3. 파일 간 ID 참조 불일치 (가능성 낮음)

현재 ID 참조:
- `section0.xml`의 `paraPrIDRef="0"` → `header.xml`의 `paraPr id="0"` ✅
- `section0.xml`의 `charPrIDRef="0"` → `header.xml`의 `charPr id="0"` ✅
- `charPr`의 `borderFillIDRef="2"` → `borderFill id="2"` ✅

**일관성은 있으나, 더 많은 스타일 정의 필요할 수 있음**

---

## 📚 핵심 참고 문서

### 반드시 읽어야 할 문서 (순서대로)

1. **docs/AI_COLLABORATION_GUIDE.md**
   - AI 협업 규칙
   - 문서 관리 방법

2. **converter/PHASE1_GUIDE.md**
   - Phase 1 목표 및 전략
   - 개발 접근 방법
   - 3가지 정보 계층 (표준 스펙, 개발자 가이드, 예제 파일)

3. **converter/CURRENT_ISSUES.md**
   - 🚨 현재 진행중인 이슈 상세
   - 시도한 방법들
   - 다음 AI를 위한 접근 방향

4. **converter/hwpxparshingguide.md**
   - HWPX 파일 구조 설명
   - ID 참조 체계 (header.xml ↔ section0.xml)
   - fontfaces, charPr, paraPr 관계

5. **converter/PHASE1_INPUT_FORMAT.md**
   - 입력 MD 규칙
   - 블록 타입별 정의 (주제목, 소제목, 본문, 설명, 강조)

### 참고 도구

- **tools/spec_search.py**: HWPX 스펙 검색
  ```bash
  python3 tools/spec_search.py "table 표 구조"
  python3 tools/spec_search.py "charPr paraPr"
  ```

- **HWPX 파일 분석**:
  ```bash
  # 정상 파일 분석
  unzip -q converter/test_minimal_manual.hwpx -d /tmp/minimal
  cat /tmp/minimal/Contents/header.xml | python3 -m xml.dom.minidom

  # 생성 파일 분석
  unzip -q output/test_final.hwpx -d /tmp/final
  diff /tmp/minimal/Contents/header.xml /tmp/final/Contents/header.xml
  ```

---

## 🎯 권장 접근 방법

### Option A: 점진적 수정 (추천)

1. **test_minimal_manual.hwpx 완전 복제**
   - 텍스트를 "테스트입니다" 하나만 출력하도록 최소화
   - 한글에서 열리는 것 확인
   - 점차 기능 추가

2. **표(table) 구조 구현**
   - `<주제목>` → 3행 1열 표 변환
   - `<강조>` → 1행 1열 표 변환
   - 참조: `style_textbook.md` 스타일 규칙

3. **여백 줄 추가**
   - 소제목/본문/설명 앞에 작은 폰트 공백 줄 삽입

4. **스타일 확장**
   - charPr/paraPr 개수 늘리기
   - 블록 타입별 스타일 매핑

### Option B: 이전 성공 버전 활용

`old handoff/md_to_hwpx_old.py`를 분석:
- 이 버전은 **실제로 한글에서 열렸던** 코드
- header.xml 생성 로직 참조 (L850-1100)
- 표 구조 생성 로직 확인

현재 코드와 통합:
- 이전 버전의 header.xml 생성 방식 차용
- 현재 버전의 깔끔한 구조 유지

### Option C: 외부 LLM 활용

`converter/EXTERNAL_LLM_REQUEST.md` 사용:
- 다른 LLM에게 "최소 동작 HWPX" 샘플 요청
- 받은 샘플을 `converter/minimal_reference.hwpx`로 저장
- 구조 분석 후 코드 수정

---

## 🔧 핵심 코드 위치

### md_to_hwpx.py 주요 함수

- **Line 176-404**: `build_header_xml()`
  - fontfaces (7개 언어)
  - borderFills (2개)
  - charProperties (1개) ← **확장 필요**
  - tabProperties (3개)
  - numberings (10 레벨)
  - paraProperties (1개) ← **확장 필요**
  - styles (1개)

- **Line 407-520**: `build_section0_xml(blocks)`
  - ⚠️ **표 구조 미구현**
  - 모든 블록을 `<hp:p>` 문단으로만 변환
  - 첫 문단에 secPr/pagePr 포함

- **Line 522-572**: 기타 빌더 함수들
  - `build_content_hpf()`
  - `build_container_xml()`
  - `build_container_rdf()`
  - `build_manifest_xml()`
  - `build_version_xml()`
  - `build_settings_xml()`

- **Line 718-763**: `write_hwpx(blocks, output_path)`
  - ZIP 패키징
  - 파일 순서: mimetype (uncompressed) → 나머지

---

## ✅ 검증 방법

### 1. 파일 구조 확인

```bash
unzip -l output/test_final.hwpx
```

### 2. XML 유효성 확인

```bash
unzip -q output/test_final.hwpx -d /tmp/test
python3 -m xml.dom.minidom /tmp/test/Contents/header.xml > /dev/null
echo $?  # 0이면 valid XML
```

### 3. 참조 파일과 비교

```bash
# header.xml 비교
diff <(unzip -p converter/test_minimal_manual.hwpx Contents/header.xml) \
     <(unzip -p output/test_final.hwpx Contents/header.xml)
```

### 4. 한글 프로그램 테스트

- 파일을 한글에서 직접 열어보기
- 열리지 않으면: 에러 메시지 확인
- 열리면: 내용 표시 여부 확인

---

## 📝 작업 기록 규칙

### CURRENT_ISSUES.md 업데이트

문제 해결 시도할 때마다:
```markdown
### 시도한 방법들

3. [Your AI Name - 11/15] 방법 설명 → 결과
```

### TROUBLESHOOTING.md 기록

문제 **해결 완료** 시:
```markdown
## [2025-11-15] 문제: 간단한 제목

### 증상
...

### 원인
...

### 해결 방법
...
```

---

## 🎓 학습 자료

### HWPX 구조 이해

1. ZIP 파일 구조
2. header.xml (스타일 정의)
3. section0.xml (본문 내용)
4. ID 참조 체계

**hwpxparshingguide.md** 참조

### 표(table) 구조 구현

HWPX에서 표는 `<hp:tbl>` 요소로 구현:
```xml
<hp:tbl>
  <hp:tr>
    <hp:tc>
      <hp:p>...</hp:p>
    </hp:tc>
  </hp:tr>
</hp:tbl>
```

**spec_search.py로 검색:**
```bash
python3 tools/spec_search.py "tbl table 표"
```

---

## 🚀 시작하기

### Step 1: 상황 파악 (15분)

1. 이 문서 읽기
2. `converter/CURRENT_ISSUES.md` 읽기
3. `converter/PHASE1_GUIDE.md` 훑어보기

### Step 2: 분석 (30분)

```bash
# 정상 파일 구조 확인
unzip -q converter/test_minimal_manual.hwpx -d /tmp/minimal
cat /tmp/minimal/Contents/section0.xml

# 현재 생성 파일 확인
unzip -q output/test_final.hwpx -d /tmp/final
diff -u /tmp/minimal/Contents/section0.xml /tmp/final/Contents/section0.xml
```

### Step 3: 수정 시도

Option A, B, C 중 선택하여 진행

---

## 💡 힌트

### 핵심 의심 포인트

1. **section0.xml의 표 구조 누락**
   - `style_textbook.md`: 주제목/강조는 표로 구현
   - 현재 코드: 모든 블록을 단순 문단으로만 처리

2. **charPr/paraPr 개수 부족**
   - 참조 파일: 다양한 스타일 (8개 이상)
   - 현재: 기본 스타일 1개만

3. **여백 줄 미구현**
   - `style_textbook.md`: 각 블록 앞에 작은 폰트 공백
   - 현재: 여백 줄 없음

### 디버깅 팁

```bash
# section0.xml에 표가 있는지 확인
unzip -p output/test_final.hwpx Contents/section0.xml | grep "<hp:tbl"

# charPr 개수 확인
unzip -p output/test_final.hwpx Contents/header.xml | grep -o '<hh:charPr' | wc -l

# ID 참조 일관성 확인
unzip -p output/test_final.hwpx Contents/section0.xml | grep -o 'charPrIDRef="[^"]*"' | sort -u
unzip -p output/test_final.hwpx Contents/header.xml | grep -o '<hh:charPr id="[^"]*"'
```

---

## 📞 추가 정보

- Git 브랜치: `phase0/docs-smoke-test`
- 최근 커밋들 확인: `git log --oneline -10`
- 변경된 파일들: `git status`

**행운을 빕니다! 🍀**

이 문제를 해결하면 Phase 1의 가장 큰 장벽을 넘는 것입니다.
