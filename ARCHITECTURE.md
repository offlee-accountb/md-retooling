# Document Automation System - Architecture

## Phase 0: 개발 환경 준비 (필수 선행)

### HWPX 스펙 검색 시스템
**문제:**
- HWPX 표준 문서: 약 40만자 (400페이지)
- AI 코딩 에이전트의 컨텍스트 윈도우 + 입출력 토큰 한계
- 전체 문서를 한번에 참조 불가능 (4만자도 제대로 참고 못함)

**해결:**
- 간이 RAG 시스템 구축
  * hwpx_spec.md를 청크 단위로 분할
  * 키워드 검색 또는 간단한 임베딩
  * 필요한 부분만 추출하여 AI에게 전달

**구현:**
```
tools/
├── spec_search.py      # 검색 메인 로직
├── chunk_builder.py    # 스펩 문서 분할
└── chunks/             # 분할된 데이터 저장
```

**사용 예시:**
```bash
# 줄간격 관련 스펙 찾기
python tools/spec_search.py "줄간격 line-spacing"

# 결과를 AI에게 전달하여 코딩
```

---

## 프로젝트 목표
공공기관 공문서 자동 생성 시스템
- Input: 텍스트 파일 (PDF, Word, MD 등)
- Process: LLM 가공 → 부처 형식 마크다운
- Output: 규격화된 HWPX 문서

## 시스템 흐름도
```
[텍스트 입력] 
    ↓
[텍스트 추출] (후순위, 기존 툴 활용)
    ↓
[LLM 가공] (장기, 수동/자동 옵션)
    ↓
[마크다운 생성/수정]
    ↓
[MD → HWPX 변환] ⭐ 최우선
    ↓
[HWPX 출력]
    ↕
[HWPX 검증 툴] ⭐ 필수 보조
```

## MVP 개발 우선순위

### Phase 0: 개발 환경 (선행 필수)
- HWPX 스펙 검색 시스템
- 코딩 에이전트가 표준 문서 참조 가능하게

### Phase 1: 핵심 변환 엔진 (최우선)
1. **MD → HWPX 변환기**
   - 목표: 마크다운 → 한글 문서 변환
   - 조정 가능: 줄간격, 양식, 폰트, 제목 스타일
   - 지속적 개선 필요
   
2. **HWPX 검증 툴**
   - HWPX 파일 구조 시각화
   - VS Code에서 확인 가능
   - 주석/설명 자동 추가
   - 실시간 피드백

### Phase 2: 자동화 (장기)
3. **LLM API 연동**
   - Claude/GPT API 연동
   - 텍스트 → MD 자동 생성
   - 수동 입력과 선택 가능

### Phase 2.5: 템플릿 반자동화 (초장기)
4. **템플릿 리버스 엔지니어링 툴**
   - 목표: 새 양식 추가 시간 단축 (3주 → 3일)
   - HWPX 샘플 → 구조 자동 분석
   - 변수 패턴 자동 탐지 ("___", "OOO" 등)
   - 템플릿 JSON 자동 생성
   - 변환 코드 80% 자동 생성
   - 사람이 20%만 미세 조정

### Phase 4: 확장 (후순위)
5. **텍스트 추출**
   - PDF OCR
   - Word 파싱
   - 기존 툴 활용 검토

6. **웹 서비스화**
   - HTML 프론트엔드
   - 유료 결제 시스템

## 기술 스택

### Backend
- Python 3.11+
- FastAPI
- HWPX 처리: XML 직접 조작 (국가 표준 준수)

### 보조 툴
- HWPX 스펙 검색 시스템 (RAG 기반)
- VS Code Extension (HWPX 뷰어) 또는 독립 스크립트

### 향후 추가
- Anthropic/OpenAI API
- 프론트엔드: React (TBD)

## 핵심 컴포넌트 상세

### MD → HWPX 변환기

**입력 스펙:**
```python
def convert_md_to_hwpx(
    md_file: str,           # 마크다운 파일 경로
    output: str,            # 출력 HWPX 경로
    style_config: dict = None  # 양식 설정 (선택)
) -> str:
    """
    마크다운을 HWPX로 변환
    
    Returns: 생성된 HWPX 파일 경로
    Raises: ConversionError
    """
```

**스타일 설정 예시:**
```json
{
  "h1": {
    "font": "맑은 고딕",
    "size": 18,
    "bold": true,
    "align": "center"
  },
  "h2": {
    "font": "맑은 고딕", 
    "size": 14,
    "bold": true,
    "align": "left"
  },
  "body": {
    "font": "바탕",
    "size": 11,
    "line_spacing": 160,
    "align": "justify"
  }
}
```

### HWPX 검증 툴

**기능:**
```python
def validate_hwpx(hwpx_file: str) -> dict:
    """
    HWPX 파일 구조 분석 및 시각화
    
    Returns: {
        "structure": [...],     # XML 트리 구조
        "styles": {...},        # 스타일 정보
        "content_preview": "..."  # 내용 미리보기
    }
    """
```

**출력 예시:**
```
=== HWPX 구조 분석 ===
제목1 (18pt, 굵게, 가운데): "보고서 제목"
제목2 (14pt, 굵게, 왼쪽): "1. 개요"
본문 (11pt, 160%, 양쪽): "본문 내용입니다."
```

### 템플릿 자동화 툴 (Phase 2.5)

**목표:**
- 새 양식 추가 시간 단축: 3주 → 3일
- 반복 작업 80% 자동화

**핵심 기능:**

1. **HWPX 구조 분석기**
```python
def analyze_hwpx_template(hwpx_file: str) -> dict:
    """
    샘플 HWPX에서 구조 자동 추출
    
    Returns: {
        "template_name": "비자발급서",
        "structure": [...],      # 문서 구조
        "variables": [...],      # 채워야 할 변수들
        "styles": {...}          # 스타일 정보
    }
    """
```

2. **변수 자동 탐지**
   - 패턴 인식: "___", "OOO", "[ ]", "____년 __월"
   - 라벨 추출: "성명:", "생년월일:" 등
   - 변수명 자동 생성: {{name}}, {{birth_date}}

3. **템플릿 JSON 생성**
```json
{
  "template_name": "비자발급서",
  "structure": [
    {
      "type": "title",
      "content": "비자 발급 신청서",
      "style": {"size": 18, "bold": true}
    },
    {
      "type": "field",
      "label": "성명",
      "variable": "{{name}}",
      "required": true
    }
  ]
}
```

4. **변환 코드 자동 생성**
```python
def generate_converter_code(template_json: dict) -> str:
    """
    템플릿 JSON → Python 변환 코드 (80% 완성)
    
    자동 생성:
    - 기본 구조
    - 변수 매핑
    - 스타일 적용
    
    수동 작업 필요 (TODO 주석으로 표시):
    - 특수 로직 (날짜 포맷, 계산식)
    - 복잡한 조건문
    - 검증 규칙
    """
```

**작업 흐름:**
```
샘플 HWPX (비자발급서.hwpx)
    ↓
[자동] 구조 분석
    ↓
[자동] 템플릿 JSON 생성
    ↓
[자동] 변환 코드 80% 생성
    ↓
[수동] 미세 조정 20%
    ↓
새 변환기 완성
```

**예상 효과:**
- 수동 개발: 분석(1주) + 구현(1.5주) + 테스트(0.5주) = **3주**
- 반자동: 분석(자동) + 코드생성(자동) + 조정(2일) + 테스트(1일) = **3일**

## 데이터 흐름

### 현재 MVP
```
MD 파일 (수동 작성)
    ↓
변환 엔진
    ↓
HWPX 파일
    ↓
검증 툴로 확인
    ↓
피드백 → 변환 로직 개선
```

### 향후 확장
```
텍스트 입력
    ↓
LLM API (선택적)
    ↓
MD 파일 (자동 or 수동)
    ↓
변환 엔진
    ↓
HWPX 파일
```

## 프로젝트 구조
```
document-automation/
├── tools/                  # Phase 0
│   ├── spec_search.py     # HWPX 스펙 검색
│   ├── chunk_builder.py   # 문서 분할
│   └── chunks/            # 분할된 스펙 데이터
│
├── converter/              # Phase 1
│   ├── md_parser.py
│   ├── hwpx_generator.py
│   └── styles.py
│
├── validator/              # Phase 1
│   ├── hwpx_reader.py
│   └── visualizer.py
│
├── template_automation/    # Phase 2.5 (초장기)
│   ├── template_analyzer.py   # HWPX → JSON 분석
│   ├── code_generator.py      # JSON → Python 코드 생성
│   └── generated_templates/   # 자동 생성된 템플릿들
│
├── docs/
│   ├── hwpx_spec.md           # 40만자 표준 문서
│   ├── RECENT_CHANGES.md      # 최근 변경사항 (5-10개)
│   └── FULL_CHANGELOG.md      # 전체 변경 이력
│
├── templates/
│   └── government_format.json
│
└── tests/
    ├── unit/                   # 단위 테스트
    │   ├── test_converter.py
    │   ├── test_parser.py
    │   └── test_validator.py
    ├── integration/            # 통합 테스트
    │   └── test_end_to_end.py
    └── fixtures/               # 테스트 샘플 파일들
        ├── input/              # 입력 샘플 (MD, 텍스트)
        │   ├── sample1.md
        │   └── sample2.md
        ├── output/             # 예상 출력 (HWPX)
        │   ├── expected1.hwpx
        │   └── expected2.hwpx
        └── hwpx_samples/       # 분석용 HWPX 샘플
            ├── 비자발급서.hwpx
            └── 공문서양식.hwpx
```

## 개발 로드맵

**Week 0: 준비**
- HWPX 스펙 검색 시스템 구축
- 청크 분할 및 인덱싱
- 검색 테스트

**Week 1-2: 기본 변환**
- 간단한 MD → HWPX 프로토타입
- 기본 텍스트만 (제목, 본문)
- 스펙 참조하며 XML 구조 구현

**Week 3-4: 양식 정교화**
- 줄간격, 폰트 조정
- 부처 양식 적용
- 스펙 검색으로 세부 사항 확인

**Week 5-6: 검증 툴**
- HWPX 구조 파서
- 시각화 스크립트

**Week 7+: 반복 개선**
- 실제 공문서로 테스트
- 피드백 반영
- 양식 미세 조정

**Phase 2.5 이후 (초장기):**
- 3개 양식에서 패턴 발견
- 템플릿 분석기 개발
- 코드 생성기 개발
- 새 양식 추가 시간: 3주 → 3일

## 핵심 요구사항

### MD → HWPX 변환기
- 부처 공문서 양식 준수
- 세밀한 조정 가능
  - 줄간격
  - 폰트 (명조/돋움)
  - 제목 레벨별 스타일
  - 여백, 들여쓰기
- 이미지/표 삽입 지원
- **국가 표준 HWPX 스펙 100% 준수**

### HWPX 검증 툴
- HWPX 내부 구조 표시
- XML 트리 시각화
- 스타일 정보 확인
- MD 역변환 (선택)

## 제약사항

### AI 코딩 에이전트
- 컨텍스트 윈도우 제한
- 입출력 토큰 한계
- 4만자 이상은 제대로 참조 불가
- → RAG 방식 검색 필수

### HWPX 포맷
- ZIP 압축된 XML 파일 집합
- 국가 표준 문서 (400p) 준수 필요
- Python 직접 지원 라이브러리 부족
- XML 직접 생성 방식 채택

## 참고 자료
- `docs/hwpx_spec.md` - HWPX 표준 통합본(원문 전체 포함, 고유 앵커/Global Index 포함)
- `docs/hwpx_spec.index.json` - 섹션 청킹 메타(라인/문자 오프셋, 원본 파일 매핑)
- `docs/hwpx_terms.alias.json` - 용어 동의어 사전(KR/EN/스키마명 → 대표 앵커)
- RAG 검색 시스템을 통해 필요 부분만 참조

## AI 협업 및 파일 관리

### 변경 이력 관리
- `docs/RECENT_CHANGES.md` - 최근 5-10개 변경사항 (AI가 매번 참조)
- `docs/FULL_CHANGELOG.md` - 전체 변경 이력 (필요시 참조)

**운영 방식:**
- 작업 완료 후 RECENT_CHANGES.md 업데이트
- 10개 초과 시 오래된 항목은 FULL_CHANGELOG.md로 이동
- AI 작업 시작 전 RECENT_CHANGES.md 필수 확인

### 파일 관리 규칙

**테스트 파일:**
- `tests/unit/` - 단위 테스트 코드만
- `tests/integration/` - 통합 테스트 코드만
- `tests/fixtures/` - 모든 샘플 파일 (코드 아님)
  * `input/` - 입력 샘플
  * `output/` - 예상 출력
  * `hwpx_samples/` - 분석용 실제 HWPX

**생성된 파일:**
- 개발 중 생성되는 임시 HWPX는 `output/` 또는 `/tmp/`
- Git에 커밋하지 않음 (.gitignore 설정)

**문서:**
- 모든 문서는 `docs/` 폴더
- 스펙, 가이드, 변경 이력 통합 관리
