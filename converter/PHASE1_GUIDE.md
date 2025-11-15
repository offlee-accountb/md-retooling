# Phase 1 변환 가이드

> MD → HWPX 변환기 개발 상세 가이드
>
> **목표:** 마크다운 파일을 정부 공문서 양식의 HWPX로 변환

---

## MVP 목표

### 최종 산출물

**Input:** `sample_input.md` (마크다운 파일)  
**Output:** 정부 공문서 양식의 HWPX 파일  
**범위:** 단일 양식만 구현 (공문서 기본 양식)

### 성공 기준

- [ ] `sample_input.md` → HWPX 변환 성공
- [ ] 정부 양식 규격 준수
- [ ] 육안 검증 통과 (한글 프로그램에서 확인)

---

## 개발 접근 방법

### ⚠️ 중요: LLM 지식만으로는 부족

토이프로젝트 경험상, AI가 가진 HWPX 지식만으로는 **요구 수준의 품질이 나오지 않음**.

### ✅ 해결책: HWPX 표준 문서 활용

- **위치:** `tools/` 폴더
- **내용:** HWPX 100% 구현 표준 (40-60만자)
- **활용:** RAG 방식 검색 시스템 사용
- **방법:**

  ```bash
  # 필요한 스펙 검색
  python tools/spec_search.py "줄간격"
  python tools/spec_search.py "문단 스타일"

  # 결과를 AI에게 제공하여 구현
  ```

### 개발 흐름

```
문제 발생
    ↓
tools/spec_search.py로 표준 검색
    ↓
관련 스펙 확인
    ↓
스펙 기반으로 구현
    ↓
테스트
```

---

## 프로젝트 구조

```
converter/
├── md_parser.py           # 마크다운 파싱
├── hwpx_generator.py      # HWPX 생성
├── style_textbook.md      # 정부 양식 스타일 정의
├── sample_input.md        # 테스트용 입력 파일
├── PHASE1_GUIDE.md        # 이 문서
├── TROUBLESHOOTING.md     # 해결된 문제 기록
└── CURRENT_ISSUES.md      # 진행중인 이슈
```

---

## 핵심 문서 3종

### 1. PHASE1_GUIDE.md (이 문서)

- MVP 목표 및 전체 방향
- 개발 가이드라인
- 장기 확장 계획

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

## 장기 확장 계획

### MVP 이후 추가 기능

MVP 완료 후 단계적으로 추가:

- [ ] 다양한 제목 레벨 (h3, h4, h5)
- [ ] 리스트 처리 (순서, 비순서)
- [ ] 표(table) 변환
- [ ] 이미지 삽입
- [ ] 각주/미주
- [ ] 페이지 번호
- [ ] 머리말/꼬리말

**원칙:**

- MVP 검증 후 확장
- 각 기능마다 표준 스펙 확인
- TROUBLESHOOTING.md에 경험 축적

---

## 참고 자료

### 내부 문서

- `tools/spec_search.py` - HWPX 표준 검색
- `docs/hwpx_spec.md` - 전체 표준 문서
- `validator/toy_project/` - 토이프로젝트 참고 (예정)

### 관련 Phase 문서

- `ARCHITECTURE.md` - 전체 시스템 설계
- `RECENT_CHANGES.md` - 최근 변경사항
- `FULL_CHANGELOG.md` - Phase별 이력

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
