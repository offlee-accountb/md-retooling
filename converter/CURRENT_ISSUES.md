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

## [진행중] Spacer 줄(라인스페이서) 폰트/크기 미스매치

**우선순위:** Medium  
**담당 AI:** Codex (2025-11-15)

### 상황
- style_textbook 규칙에 따라 spacer(소제목/본문/설명2/설명3 사이 공백 줄)를 각각 10/8/6/4pt 맑은 고딕으로 넣어야 하지만,
  - 한글에서 실제로 확인해보면 여전히 기본 바탕글(한컴바탕 10pt)에 가까운 값으로 표시됨.
  - spacer 문단이 바탕글 스타일로 보이면서 폰트 크기만 반영되지 않거나, 특정 줄만 잘못된 크기를 사용.
- `<hp:linesegarray>`는 쓰지 않기로 했으며, 순수하게 run의 charPr 높이만으로 줄간격을 제어해야 한다는 추가 요구 있음.

### 시도한 방법들
1. [Codex - 11/15] spacer용 paraPr/style을 따로 정의 → **한글에서 기본 스타일로 덮여 보임**
2. [Codex - 11/15] spacer 문단을 바탕글 스타일로 통일하고 run에만 charPr 10~13 (맑은고딕 10/8/6/4pt) 적용 → **한글 결과에서 여전히 4/15/10/10pt로 관측됨**

### 다음 AI에게
- `output/test_styled6.hwpx`를 한글에서 열어 spacer 줄의 실제 폰트/높이가 어떻게 결정되는지 다시 확인.
- 한글이 run-level charPr보다 paraPr/style 레벨의 값을 우선시한다면:
  1. spacer run에 텍스트 대신 `<hp:ctrl>` 또는 빈 cell/table을 써서 강제 높이 지정,
  2. 또는 paraPr margin/lineSpacing을 직접 조정해 여백을 확보하는 쪽으로 설계 변경.
- `<hp:linesegarray>` 없이 run만으로 줄 높이를 정확히 제어하는 사례가 있는지 `test_inputmodel.hwpx`나 스타일북에서 추가 사례 조사 필요.

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
