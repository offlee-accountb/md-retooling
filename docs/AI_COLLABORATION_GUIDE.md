# AI 협업 가이드

> 여러 AI 도구(GitHub Copilot, Claude Code, Codex)가 협업할 때 따라야 할 핵심 규칙
> 
> **목적:** 일관성 유지, 컨텍스트 손실 방지, 효율적 인수인계

---

## 1. 언어 원칙

- **문서/주석/커밋:** 한국어
- **코드 식별자:** 영어 (PEP 8)
- **AI 응답:** 한국어 + 영어 식별자

---

## 2. Git 워크플로우

### 브랜치 규칙
```
feature/<기능>    # 새 기능
fix/<버그>        # 버그 수정
phase<N>/<작업>   # Phase별 작업
```

- **main 직접 푸시 금지**
- **PR은 Draft 시작**
- **Squash 머지 권장**

### 커밋 메시지
```
타입: 한 줄 요약

- 핵심 변경 1
- 핵심 변경 2

도구: [AI명] | Phase: N | 파일: [목록]
```

**타입:** `feat`, `fix`, `refactor`, `docs`, `test`, `chore`

---

## 3. 문서 체계 (SSOT)

### 필수 읽기 순서
1. `ARCHITECTURE.md` - 시스템 설계 (항상 먼저)
2. `RECENT_CHANGES.md` - 최근 5-10개 변경
3. `FULL_CHANGELOG.md` - Phase별 전체 이력 (필요시)

### 작업 후 업데이트
```markdown
## YYYY-MM-DD
- **도구:** [AI명]
- **작업:** [요약]
- **파일:** [목록]
- **내용:** [핵심 변경사항]
```

**규칙:**
- 작업 완료 후 즉시 `RECENT_CHANGES.md` 업데이트
- Phase 완료 시 `FULL_CHANGELOG.md` 동기화
- 새 모듈 완성 시 `README.md` 작성

---

## 4. AI 인수인계 프로토콜

### 작업 시작 전 (필수)
- [ ] `ARCHITECTURE.md` 읽기
- [ ] `RECENT_CHANGES.md` 확인
- [ ] 현재 Phase 파악
- [ ] 이전 AI 참고사항 확인

### 작업 완료 후 (필수)
**Phase 진행 중:**
```markdown
## YYYY-MM-DD
- **도구:** GitHub Copilot
- **작업:** MD 파서 완성
- **파일:** converter/md_parser.py
- **내용:** 헤딩/리스트 파싱 구현
```

**Phase 완료 시 추가:**
```markdown
## Phase N 완료
- **완성 기능:** [체크리스트]
- **주요 API:**
  ```python
  from module import function
  result = function(args)
  ```
- **다음 작업자 참고:** [주의사항]
```

### AI 전환 체크리스트
넘기는 AI:
- [ ] `RECENT_CHANGES.md` 상세 작성
- [ ] 주요 API 사용법 문서화
- [ ] 다음 작업자 참고사항 명시

받는 AI:
- [ ] 문서 3개 읽기 (Architecture, Recent, Full)
- [ ] 이전 작업 코드 리뷰
- [ ] 사용법 이해 후 시작

---

## 5. 파일 관리

### 디렉토리 규칙
```
document-automation/
├── tools/              # Phase 0
├── converter/          # Phase 1
├── validator/          # Phase 1
├── template_automation/# Phase 2.5
├── docs/               # 모든 문서
│   ├── ARCHITECTURE.md
│   ├── RECENT_CHANGES.md
│   ├── FULL_CHANGELOG.md
│   ├── AI_COLLABORATION_GUIDE.md
│   └── hwpx_spec.md
└── tests/
    ├── unit/           # 단위 테스트 코드
    ├── integration/    # 통합 테스트
    └── fixtures/       # 샘플 파일
        ├── input/
        ├── output/
        └── hwpx_samples/
```

### 생성 파일
- 임시 출력: `/tmp/` 또는 `output/` (Git 제외)
- 테스트 고정: `tests/fixtures/output/`

---

## 6. 코드 표준

### 함수 작성
```python
def function_name(arg1: str, arg2: int = 0) -> str:
    """
    함수 설명
    
    Args:
        arg1: 설명
        arg2: 설명 (기본값)
        
    Returns:
        반환값 설명
        
    Raises:
        ErrorType: 에러 조건
    """
    # 구현
```

### 금지 사항
- ❌ main 브랜치 직접 푸시
- ❌ `.env` 파일 커밋
- ❌ API 키 하드코딩
- ❌ `try-except-pass` 남발
- ❌ `# type: ignore` 남발

### 권장 사항
- ✅ 타입 힌트 + Docstring
- ✅ 단위 테스트 작성
- ✅ 설정은 `config.json`
- ✅ 복잡한 로직은 주석

---

## 7. CI/검증 (Phase별)

**Phase 0-1:** 수동 검증  
**Phase 2:** 린트(ruff, black) 도입  
**Phase 3+:** CI/CD 파이프라인

### 원칙
- 변경된 파일만 검사
- 신규 코드는 경고 0 강제
- 기존 부채는 점진적 개선

---

## 8. 특수 상황

### 긴 파일 (4,000줄+)
- 전체 읽지 말고 필요 부분만
- `grep`/`ripgrep`로 검색
- 250라인 단위 분할

### 에러 발생
1. 전체 스택트레이스 제공
2. 관련 코드만 첨부
3. "수정해줘" + 에러 로그

### 설계 변경
1. 사용자와 논의
2. `ARCHITECTURE.md` 수정
3. 영향받는 코드 리팩토링
4. `RECENT_CHANGES.md`에 명시

---

## 9. 참고

### 내부 문서
- `ARCHITECTURE.md` - 시스템 설계
- `RECENT_CHANGES.md` - 최근 변경
- `FULL_CHANGELOG.md` - 전체 이력

### 외부 자료
- [PEP 8](https://pep8.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

**2024-11-12 초안 작성 (Claude)**
