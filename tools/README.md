# Phase 0: HWPX 스펙 검색 시스템

> AI 코딩 에이전트가 40만자 규모의 HWPX 표준 문서를 효율적으로 참조할 수 있도록 하는 RAG 기반 검색 시스템

## 개요

HWPX 표준 문서는 약 40만자(400페이지) 규모로, AI 에이전트의 컨텍스트 윈도우 한계로 인해 전체 문서를 한번에 참조할 수 없습니다. 이 도구들은 문서를 청크 단위로 분할하고 키워드 검색을 통해 필요한 부분만 추출하여 AI에게 전달합니다.

## 파일 구조

```
tools/
├── README.md              # 이 문서
├── spec_search.py         # 검색 메인 로직 (BM25 + 동의어 + TF-IDF)
├── chunk_builder.py       # 스펙 문서 분할
├── build_assets_index.py  # 표/그림/예제 인덱스 생성
├── phase0_smoke_test.py   # Phase 0 통합 테스트
└── chunks/                # 분할된 데이터 저장
    ├── sections.jsonl     # 섹션별 청크 (340개)
    └── chunks.meta.json   # 메타데이터
```

## 핵심 도구

### 1. spec_search.py - HWPX 스펙 검색기

**기능:**
- BM25 알고리즘 기반 키워드 검색
- 동의어 확장 (camelCase, hyphen, 공백 변형)
- TF-IDF 문장 단위 재정렬 (선택)
- 컨텍스트 윈도우 압축 (필요한 문장만 추출)
- 앵커 기반 섹션 부스팅

**사용법:**
```bash
# 기본 검색 (Top 5)
python tools/spec_search.py "줄간격 line-spacing"

# 결과 수 지정 + JSON 출력
python tools/spec_search.py "paraPr 문단 모양" -k 3 --json

# 문장 압축 (윈도우 크기 2) + 자동 K 조정
python tools/spec_search.py "lineSpacing" --compact 2 --auto-k

# TF-IDF 재정렬 (상위 12개 중 문장 유사도로 재순위)
python tools/spec_search.py "필드 fieldBegin" --rerank-top 12 --compact 1
```

**옵션:**
- `-k N` - 반환할 결과 수 (기본: 5)
- `--json` - JSON 형식 출력
- `--auto-k` - 스코어 격차가 크면 자동으로 K 축소
- `--compact N` - 키워드 주변 N줄만 추출 (0=비활성)
- `--rerank-top N` - 상위 N개를 TF-IDF로 재정렬

**데이터 소스:**
- `docs/hwpx_spec.md` - 원본 스펙 문서
- `docs/hwpx_spec.index.json` - 섹션 경계 정보
- `docs/hwpx_terms.alias.json` - 용어 동의어 맵
- `tools/chunks/sections.jsonl` - 분할된 청크 (chunk_builder로 생성)

### 2. chunk_builder.py - 청크 빌더

**기능:**
- Markdown 직접 파싱으로 섹션 자동 추출
- 앵커 기반 섹션 분할 (`<a name="s-xxx">`)
- 번호 있는 헤딩 탐지 (`9.3.8.2 paraPr 요소`)
- 소스 파일 추적 (`## Source: okok1-1-1.md`)

**사용법:**
```bash
# 기본 실행 (Markdown 직접 파싱)
python tools/chunk_builder.py

# 특정 스펙 파일 지정
python tools/chunk_builder.py --spec docs/hwpx_spec.md --out tools/chunks

# 기존 index.json 사용 (옵션, 비권장)
python tools/chunk_builder.py --use-index
```

**출력:**
- `tools/chunks/sections.jsonl` - 섹션별 청크 (현재 340개)
- `tools/chunks/chunks.meta.json` - 메타데이터

**청크 포맷:**
```json
{
  "id": "s-para-paraPr",
  "anchor": "s-para-paraPr",
  "number": "9.3.8.2",
  "title": "paraPr 요소",
  "source_file": "okok1-1-3.md",
  "start_line": 1234,
  "end_line": 1289,
  "text": "9.3.8.2 paraPr 요소\n..."
}
```

### 3. build_assets_index.py - 에셋 인덱서

**기능:**
- 표, 그림, 샘플, 예제 자동 인덱싱
- 앵커와 라벨 매칭 (`<a name="table-123">` + `표 123 — 제목`)

**사용법:**
```bash
python tools/build_assets_index.py
```

**출력:**
- `docs/hwpx_assets.index.json` - 에셋 인덱스

**통계 예시:**
```json
{
  "counts": {
    "tables": 250,
    "figures": 45,
    "samples": 30,
    "examples": 15,
    "total": 340
  }
}
```

### 4. phase0_smoke_test.py - 통합 테스트

**기능:**
- Phase 0 전체 워크플로우 검증
- 청크 빌드 자동화 (필요시 or 강제)
- 샘플 검색 실행

**사용법:**
```bash
# 기본 테스트 (줄간격 검색, Top 3)
python tools/phase0_smoke_test.py

# 커스텀 쿼리
python tools/phase0_smoke_test.py --query "paraPr fontLineHeight" -k 5

# 청크 강제 재생성
python tools/phase0_smoke_test.py --force-rebuild
```

## 워크플로우

### 1. 초기 설정 (최초 1회)
```bash
# 청크 생성
python tools/chunk_builder.py

# 에셋 인덱스 생성 (선택)
python tools/build_assets_index.py

# 테스트 실행
python tools/phase0_smoke_test.py
```

### 2. AI 에이전트 작업 시
```bash
# 필요한 스펙 부분 검색
python tools/spec_search.py "찾고싶은 키워드" -k 3 --compact 1

# 결과를 AI 에게 전달하여 코딩
```

### 3. 스펙 문서 업데이트 시
```bash
# 청크 재생성
python tools/chunk_builder.py

# 자동 감지 테스트
python tools/phase0_smoke_test.py  # 자동으로 재빌드 감지
```

## 검색 팁

### 키워드 선정
- **한영 혼용 가능**: `"줄간격 line-spacing"`
- **camelCase 자동 확장**: `lineSpacing` → `line spacing`, `line-spacing`, `linespacing`
- **동의어 자동 포함**: `hwpx_terms.alias.json`에 정의된 용어 그룹

### 결과 품질 향상
```bash
# 기본 검색 (넓게)
python tools/spec_search.py "paraPr" -k 10

# 정밀 검색 (문장 재정렬 + 압축)
python tools/spec_search.py "paraPr fontLineHeight" --rerank-top 15 --compact 2 -k 3

# 자동 필터링 (스코어 격차 큰 경우 Top 2만)
python tools/spec_search.py "lineSpacing" --auto-k
```

## 데이터 파일 설명

### `tools/chunks/sections.jsonl`
- 섹션별로 1줄씩 JSON 저장 (JSONL 포맷)
- 현재 340개 섹션
- 파일 크기: ~2MB

### `docs/hwpx_spec.index.json`
- 섹션 경계 메타데이터
- `chunk_builder.py --use-index`로 활용 가능 (비권장, Markdown 직접 파싱 우선)

### `docs/hwpx_terms.alias.json`
- 용어 동의어 그룹
- 예: `lineSpacing` ↔ `line-spacing` ↔ `줄간격`

## 문제 해결

### "chunks 파일이 없습니다" 에러
```bash
python tools/chunk_builder.py
```

### 검색 결과 없음
1. 키워드를 단순화 (예: `"문단모양"` → `"paraPr"`)
2. `-k` 값을 늘려서 확인 (예: `-k 20`)
3. 동의어 확인: `docs/hwpx_terms.alias.json`

### 청크가 오래됨
```bash
# 스펙 파일 수정 후 재생성
python tools/chunk_builder.py

# 또는 smoke test로 자동 감지
python tools/phase0_smoke_test.py
```

## 성능 특성

- **청크 빌드**: ~1-2초 (340개 섹션)
- **검색 속도**: ~100-200ms (BM25)
- **재정렬 추가**: ~50-100ms (TF-IDF)
- **메모리**: ~10MB (인덱스 로드)

## 다음 단계 (Phase 1)

이 검색 시스템을 활용하여:
1. **MD → HWPX 변환기** 개발
   - 스펙 검색으로 필요한 XML 구조 찾기
   - 예: `python tools/spec_search.py "paraPr lineSpacing"`
2. **HWPX 검증 툴** 개발
   - 생성된 HWPX와 스펙 대조

## 참고 문서

- [ARCHITECTURE.md](../docs/ARCHITECTURE.md) - 전체 시스템 설계
- [AI_COLLABORATION_GUIDE.md](../docs/AI_COLLABORATION_GUIDE.md) - AI 협업 규칙
- [hwpx_spec.md](../docs/hwpx_spec.md) - HWPX 표준 문서 (40만자)
