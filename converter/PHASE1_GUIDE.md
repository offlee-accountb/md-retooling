# Phase 1 변환 가이드

> MD → HWPX 변환기 개발 상세 가이드
>
> **목표:** 마크다운 파일을 정부 공문서 양식의 HWPX로 변환

---

## Phase 1 목표 & 성공 기준

### 최종 산출물 (Phase 1)

**Input:** `converter/sample_input.md` (마크다운 파일)  
**Output:** `converter/test_inputmodel.hwpx`와 사람이 보기에는 **동일한 양식**의 HWPX 파일  
**범위:** 단일 양식만 구현 (공문서 기본 양식)

### 성공 기준

- [ ] `sample_input.md` → HWPX 변환이 에러 없이 완료된다.
- [ ] 출력 HWPX를 한글에서 열었을 때 문서가 **정상적으로 열린다.**
- [ ] 육안으로 보았을 때 `test_inputmodel.hwpx`와 **동일한 구조/레이아웃**을 가진다.
- [ ] 내용 구조와 스타일이 `converter/style_textbook.md`에 정의된 규칙을 **위반하지 않는다.**

---

## 개발 접근 방법

### ⚠️ 중요: LLM+예제만으로는 부족

- LLM의 내장 지식이나 인터넷 예제만으로는 **HWPX를 한글이 인정하는 수준까지 맞추기 어렵다.**
- 특히 header.xml, 스타일 정의, 패키지 메타 구조까지 맞추지 않으면 **한글에서 파일이 깨지거나, 열리지 않을 수 있다.**

### 📚 3가지 정보 계층

1. **표준 스펙 (최종 기준)**
   - 위치: `docs/hwpx_spec.md` (+ 이를 청킹한 데이터)
   - 역할: KS X 6101 기반 정식 규격. **최종 판단 기준**.
   - 활용: `tools/spec_search.py`로 필요한 섹션 검색 후, 해당 부분을 읽고 구현.

2. **개발자 가이드/핸드북 (실무 요약)**
   - 예: `converter/hwpxparshingguide.md`
   - 역할: header.xml의 `refList`, `charPr/paraPr/fontfaces` 구조와 section의 ID 참조 흐름 같은 **구현 관점 설명**.
   - 활용: 데이터 모델과 ID 매핑을 이해하고, code 구조를 설계할 때 참고.

3. **실제 예제 파일 (제품 구현)**
   - 위치: `converter/test_inputmodel.hwpx`, `converter/test_minimal_manual.hwpx`
   - 역할: 한글이 실제로 생성한 HWPX. **제품이 실제로 허용하는 조합**의 샘플.
   - 활용: `unzip`으로 내부 XML을 확인하면서, 최소 구조와 스타일 패턴을 역추적.

### ✅ 전략: 표준 우선 + 예제 참고 + 가이드 보조

- 표준이 최종 기준, 예제와 가이드는 **현실적인 힌트**.
- 세 자료가 충돌하면 **표준을 우선**하고, 예제/가이드는 구현 편의를 위한 참고로 사용.

### `spec_search.py` 사용 패턴

```bash
# 예시: 줄간격, 문단 속성, header.xml 구조 검색
python tools/spec_search.py "줄간격 line spacing"
python tools/spec_search.py "paraProperties 문단 속성"
python tools/spec_search.py "header.xml refList charProperties paraProperties"
```

검색 결과에서 **섹션 번호/제목**을 보고, 실제 스펙 문단을 읽은 뒤 구현에 반영한다.

---

## 현재 코드 구조 & 역할

```text
converter/
├── md_to_hwpx.py          # Phase1 변환기 메인 (MD → HWPX 스켈레톤)
├── sample_input.md        # 테스트용 입력 파일
├── style_textbook.md      # 정부 양식 스타일 정의
├── PHASE1_INPUT_FORMAT.md # 입력 마크다운 포맷/규칙 정리
├── PHASE1_GUIDE.md        # 이 문서 (개발 가이드)
├── hwpxparshingguide.md   # 개발자용 HWPX 파싱/구조 가이드
├── TROUBLESHOOTING.md     # 해결된 문제 기록
└── CURRENT_ISSUES.md      # 진행중인 이슈
```

### `md_to_hwpx.py` 개요

- 입력: `sample_input.md` 스타일의 특수 규칙 기반 Markdown
- 중간 표현: `BlockType` enum과 `Block` dataclass를 사용한 **논리 블록 리스트**
- 출력: HWPX 패키지 스켈레톤 (`.hwpx` ZIP)
    - `Contents/section0.xml` : `hs:sec` 루트, 여러 `hp:p` / `hp:run` / `hp:t`
    - `Contents/content.hpf`  : 문서 메타데이터 + section0 참조
    - `META-INF/container.xml`: OCF 컨테이너 정의
    - `version.xml`, `settings.xml` 등 최소 부속 파일

현재는 **paraPr/charPr/style 정의 없이 텍스트만 있는 스켈레톤**이므로, HWP에서 파일이 열리지 않을 수 있다. Phase1의 핵심 과제는 이 구조를 **실제 한글이 열어주는 수준까지** 끌어올리는 것.

---

## 핵심 문서 4종

### 1. PHASE1_GUIDE.md (이 문서)

- Phase1 목표 및 전체 방향
- 개발 가이드라인
- 남은 과제 정리

### 2. TROUBLESHOOTING.md

**목적:** 해결된 문제 아카이브

**작성 시점:** 문제 **해결 완료** 후

**형식:**

```markdown
## [날짜] 문제: 간단한 제목

### 증상

- 어떤 문제가 발생했는가
- 에러 메시지, 현상

### 원인

- 왜 발생했는가
- 근본 원인

### 해결 방법

- 어떻게 해결했는가
- 적용한 코드/설정

### 참고

- 사용한 표준 스펙 위치
- 관련 문서
```

**활용:**

- 다음 양식 개발 시 참고
- 유사 문제 빠른 해결
- AI 학습 자료

### 3. CURRENT_ISSUES.md

**목적:** 진행중인 이슈 공유 (AI 간 인수인계)

**작성 시점:** 문제 발생 ~ 해결 전

**형식:**

```markdown
## [진행중] 이슈 제목

### 상황

- 현재 상태
- 시도한 방법들

### 다음 AI에게

- 시도해볼 만한 접근
- 참고할 스펙 위치
- 주의사항

### 히스토리

- YYYY-MM-DD: Claude - XXX 시도, 실패
- YYYY-MM-DD: Copilot - YYY 시도, 부분 성공
```

**활용:**

- AI 전환 시 컨텍스트 유지
- 중복 시도 방지
- 해결 후 TROUBLESHOOTING.md로 이동

### 4. PHASE1_INPUT_FORMAT.md

**목적:**

- 사람이 `sample_input.md` 스타일로 문서를 작성할 때 따라야 할 **입력 규칙의 단일 출처**

**내용 요약:**

- 문서 전역 설정: 용지, 여백, 줄 격자 등 (HWPX의 `secPr`와 앞으로 연결 예정)
- 라인 타입별 정의:
   - `<주제목>` / `□` / `◦` / `-` / `*` / `<강조>` 등 기호와 들여쓰기 규칙
   - 각 패턴의 논리적 역할 (주제목, 소제목, 본문, 설명 2단계/3단계, 강조 등)
   - 최종 HWP 스타일 맵핑 방향 (예: 제목 박스, 본문 스타일, 설명 스타일)

**활용:**

- MD 파서(`parse_md_lines`)의 입력 스펙으로 사용
- 향후 validator가 "입력 규칙 위반"을 검출할 때 기준으로 사용

---

## 개발 워크플로우

### 정상 흐름

```
1. 기능 구현 시작
2. 문제 발생
3. spec_search.py로 표준 검색
4. 스펙 기반 해결
5. 테스트 통과
6. (필요시) TROUBLESHOOTING.md 기록
```

### AI 전환 필요 시

```
1. CURRENT_ISSUES.md 작성
   - 현재 상황
   - 시도한 것들
   - 다음 접근 방향

2. RECENT_CHANGES.md 업데이트
   - 어디까지 진행했는지

3. 다음 AI가 시작
   - CURRENT_ISSUES.md 읽기
   - 이어서 작업

4. 해결 시
   - CURRENT_ISSUES.md → TROUBLESHOOTING.md 이동
   - CURRENT_ISSUES.md 삭제 또는 [해결됨] 표시
```

---

## Phase 1 남은 과제

### 1. 한글에서 열리는 최소 HWPX 구조 정리

- `converter/test_minimal_manual.hwpx`와 `converter/test_inputmodel.hwpx`를 기준으로 **한글이 실제로 열어주는 최소 구조**를 요약한다.
- 특히 다음을 집중 분석:
   - `Contents/header.xml`의 `hh:head` / `refList` / `charPr` / `paraPr` / `fontfaces` 구조
   - `hp:p@paraPrIDRef` ↔ `paraPr@id`, `hp:run@charPrIDRef` ↔ `charPr@id`, `charPr@fontRef` ↔ `font@id` 관계
   - `hp:secPr`(페이지/여백/줄격자)와 기본 제목/본문에 필요한 요소

### 2. `md_to_hwpx.py`에 header/styling 최소 정의 추가

- `header.xml` 생성 로직 추가 (초판)
   - 최소한의 fontfaces, charPr, paraPr, style 정의
   - `section0.xml`이 참조하는 ID들과 일관성 유지
- `section0.xml`의 `paraPrIDRef` / `charPrIDRef`를 header 정의와 연결
- 목표: **아주 단순한 텍스트만이라도 한글에서 열리는 HWPX**를 먼저 만든 뒤, 점차 `style_textbook.md`에 맞게 스타일을 확장.

### 3. Validator 설계 초안

- 별도 모듈(예: `validator/phase1_validator.py`)에서 다음을 체크:
   - ZIP 구조 및 필수 파일 존재 여부 (version.xml, header.xml, section0.xml, content.hpf, META-INF/container.xml 등)
   - header.xml ↔ section0.xml 사이의 ID 참조 일관성
   - `style_textbook.md` / `PHASE1_INPUT_FORMAT.md`에서 정의한 스타일 규칙 위반 여부
- 초기에는 **구조/ID 일관성 검사**만 구현하고, 이후 점차 스타일 세부 규칙을 추가.

### 4. 장기 확장 (Phase 1 이후)

- [ ] 다양한 제목 레벨 (추가 양식, h3/h4/h5 수준)
- [ ] 리스트 처리 (순서, 비순서)
- [ ] 표(table) 변환
- [ ] 이미지 삽입
- [ ] 각주/미주
- [ ] 페이지 번호
- [ ] 머리말/꼬리말

**원칙:**

- Phase 1에서 "기본 양식 하나를 끝까지" 밀어붙인 뒤 확장한다.
- 각 기능마다 **스펙 + 예제 + 가이드**를 함께 참고한다.
- 중요한 문제/결정은 `TROUBLESHOOTING.md`와 `CURRENT_ISSUES.md`에 반드시 남긴다.

---

## 참고 자료

### 내부 문서

- `tools/spec_search.py` - HWPX 표준 검색 도구
- `docs/hwpx_spec.md` - 전체 표준 문서 (Phase0에서 청킹/색인됨)
- `converter/hwpxparshingguide.md` - 개발자용 파싱/구조 가이드
- `converter/PHASE1_INPUT_FORMAT.md` - 입력 마크다운 규칙 정의

### 관련 Phase 문서

- `docs/ARCHITECTURE.md` - 전체 시스템 설계
- (있다면) `RECENT_CHANGES.md` - 최근 변경사항
- (있다면) `FULL_CHANGELOG.md` - Phase별 이력

---

## 개발 시작 전 체크리스트

- [ ] `ARCHITECTURE.md` 읽음
- [ ] `RECENT_CHANGES.md` 확인
- [ ] `tools/spec_search.py` 사용법 이해
- [ ] `sample_input.md` 준비됨
- [ ] HWPX 표준 문서 위치 확인
- [ ] `CURRENT_ISSUES.md` 확인 (기존 이슈 있는지)

---

**2024-11-12 초안 작성**  
**2025-11-15 Phase1 진행 상황 반영 업데이트**
