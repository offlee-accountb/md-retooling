# Document Automation System (Phase 1.5)

공공기관 공문서 자동 생성 시스템입니다. Markdown 텍스트를 표준화된 HWPX 포맷으로 변환합니다.

## 현재 구현 상태

### ✅ Phase 0: HWPX 스펙 검색 시스템
- `tools/chunk_builder.py` – HWPX 스펙 문서를 섹션 단위로 분할
- `tools/spec_search.py` – BM25 기반 키워드 검색

### ✅ Phase 1: Markdown → HWPX 변환기
- `converter/md_to_hwpx.py` – 핵심 변환 엔진
- 지원 기능: 제목, 본문, 굵게, 들여쓰기, 표, 페이지 설정
- 최근 개선: 표 기반 제목/강조 블록, 정확한 스타일 사양, 들여쓰기 수정

### 🔧 Phase 1.5: 검증 및 테스트 (진행 중)
- `validator/phase1_5_validator.py` – HWPX 출력 검증
- `validator/template_loader.py` – 템플릿 로딩 및 관리
- `tests/` – 단위 및 통합 테스트

자세한 로드맵은 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)를 참조하세요.

---

## 요구 사항
- Python 3.11 이상
- 의존성: PyYAML, lxml, pytest

### 설치 방법
```bash
# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

---

## 빠른 시작

### 1. Markdown → HWPX 변환
```bash
# 기본 사용법
python3 converter/md_to_hwpx.py input.md output.hwpx

# 예제 실행
python3 converter/md_to_hwpx.py converter/sample_input.md output/test.hwpx
```

변환기가 지원하는 Markdown 문법:
- `# 제목1`, `## 제목2`, `### 제목3` - 각 레벨에 맞는 스타일 적용
- `**굵게**` - 인라인 굵게 처리
- `들여쓰기` - 문단 들여쓰기 (네거티브 intent 값 사용)
- 표 - 제목 블록 및 강조 블록으로 변환

### 2. HWPX 스펙 검색
```bash
# 스펙 문서 청크 생성
python3 tools/chunk_builder.py --spec docs/hwpx_spec.md --out tools/chunks

# 키워드 검색
python3 tools/spec_search.py "줄간격 line-spacing" -k 5 --compact 1
```

### 3. HWPX 검증
```bash
# 생성된 HWPX 파일 검증
python3 validator/cli.py output/test.hwpx
```

### 4. 테스트 실행
```bash
# 모든 테스트 실행
pytest

# 특정 테스트만 실행
pytest tests/unit/test_template_loader.py
```

---

## 디렉터리 구조
```
.
├── README.md              # 이 문서
├── requirements.txt       # Python 의존성
├── docs/
│   ├── ARCHITECTURE.md    # 전체 로드맵 및 아키텍처
│   ├── hwpx_spec.md       # HWPX 표준 스펙 문서
│   └── TROUBLESHOOTING.md # 문제 해결 가이드
├── converter/
│   ├── md_to_hwpx.py      # 🔥 Markdown → HWPX 변환 엔진
│   ├── PHASE1_GUIDE.md    # Phase 1 가이드
│   ├── PHASE1_5_GUIDE.md  # Phase 1.5 가이드
│   └── sample_input.md    # 예제 입력 파일
├── validator/
│   ├── cli.py             # 검증 CLI 인터페이스
│   ├── phase1_5_validator.py  # HWPX 검증 로직
│   └── template_loader.py # 템플릿 로더
├── templates/             # HWPX 템플릿 파일
├── tools/
│   ├── chunk_builder.py   # 스펙 문서 청크 생성
│   ├── spec_search.py     # 스펙 검색 도구
│   └── chunks/            # 생성된 청크 데이터
├── tests/
│   ├── unit/              # 단위 테스트
│   ├── integration/       # 통합 테스트
│   └── fixtures/          # 테스트 픽스처
└── output/                # 생성된 HWPX 파일
```

---

## 주요 기능 체크리스트

### Phase 0: 스펙 검색 시스템
- [x] HWPX 스펙 문서 청크 생성
- [x] BM25 기반 키워드 검색
- [x] JSON 출력 지원

### Phase 1: Markdown → HWPX 변환
- [x] 기본 문단 변환
- [x] 제목 레벨 (H1, H2, H3) 지원
- [x] 인라인 굵게 처리
- [x] 문단 들여쓰기 (네거티브 intent)
- [x] 표 기반 블록 (제목/강조)
- [x] 페이지 설정 및 섹션 속성
- [x] CharPr ID 제약 (0-8 범위)

### Phase 1.5: 검증 및 테스트
- [x] HWPX 구조 검증기
- [x] 템플릿 로더
- [x] 단위 테스트 프레임워크
- [ ] 통합 테스트 완성
- [ ] 전체 스모크 테스트

---

## 알려진 이슈 및 제약사항

현재 알려진 문제는 [converter/CURRENT_ISSUES.md](converter/CURRENT_ISSUES.md)를 참조하세요.

주요 제약사항:
- CharPr ID는 0-8 범위로 제한 (한글 호환성)
- 복잡한 중첩 구조는 아직 미지원
- 이미지 삽입 기능 미구현

## 문제 해결

문제가 발생하면:
1. [converter/TROUBLESHOOTING.md](converter/TROUBLESHOOTING.md) 확인
2. `output/` 디렉토리의 생성된 HWPX 파일을 한글에서 열어 확인
3. 검증기로 구조 검사: `python3 validator/cli.py output/파일.hwpx`

---

## 다음 단계

### Phase 2: 고급 기능
- 이미지 삽입
- 각주 및 미주
- 목차 자동 생성
- 복잡한 표 지원

### Phase 2.5: 자동화
- LLM API 연동
- 템플릿 자동 선택
- 배치 변환

자세한 내용은 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)를 참조하세요.

---

## 기여 및 라이선스

이 프로젝트는 공공기관 문서 자동화를 위한 내부 도구입니다.
