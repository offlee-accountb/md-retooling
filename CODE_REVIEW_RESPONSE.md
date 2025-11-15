# 코드 리뷰 답변

## 프로젝트 개요
MD 파일을 HWPX(한글 문서)로 변환하는 자동화 시스템. 현재 Phase 0(HWPX 스펙 검색 시스템)이 구현되어 있음.

---

## 주요 발견 사항

### 1. 심각도: 높음 ⚠️

#### `build_assets_index.py:22` - 잘못된 주석
```python
// function to add two numbers
```
**문제점:**
- Python 코드에 C++ 스타일 주석 사용
- 주석 내용이 실제 코드와 전혀 무관함
- 테스트 코드나 실수로 남겨진 것으로 보임

**권장 조치:**
```python
# 제거 또는 적절한 Python 주석으로 교체
```

---

### 2. 심각도: 중간 ⚠️

#### `spec_search.py` - import 구문 위치
**문제점:**
- Line 148, 321: `import math`가 함수 내부에 있음
- PEP 8 권장사항 위반 (모듈은 파일 상단에서 import)

**현재:**
```python
def bm25_score_doc(...):
    ...
    import math  # Line 148
    idf = math.log(1.0 + idf)
```

**권장:**
```python
# 파일 상단 (Line 19-22 근처)
from __future__ import annotations
import argparse, json, os, re, sys
import math  # 여기에 추가
from pathlib import Path
```

#### 타입 힌트 일관성
**문제점:**
- Line 77: `list[str]` (소문자)
- Line 22: `List[str]` (대문자)
- 혼용으로 인한 일관성 부족

**권장:**
- Python 3.9+ 사용 시 소문자 `list[str]` 통일 (더 현대적)
- 또는 `List[str]` 통일 + `from typing import List` 명시

---

### 3. 심각도: 낮음 ℹ️

#### `spec_search.py:256` - main() 함수 길이
**문제점:**
- main() 함수가 164줄 (Line 256-420)로 너무 김
- 단일 책임 원칙 위반

**권장:**
- 검색 로직, 재랭킹 로직, 출력 로직을 별도 함수로 분리
```python
def search_chunks(chunks, query, aliases, args): ...
def rerank_results(scored, terms, args): ...
def output_results(results, terms, args): ...
```

#### `build_assets_index.py:74-80` - 반복 코드
**문제점:**
```python
for tpat in (pat_tbl, pat_fig, pat_sam, pat_ex1, pat_ex2):
    mm = tpat.match(lj)
    if mm and int(mm.group(1)) == num:
        title = (mm.group(2) or '').strip()
        label_line = j+1
        break
```
- 패턴 매칭이 단순 반복됨

**권장:**
```python
PATTERNS = {
    'table': re.compile(r'^\s*표\s+(\d+)\s*[—\-]\s*(.*)'),
    'figure': re.compile(r'^\s*그림\s+(\d+)\s*[—\-]\s*(.*)'),
    # ...
}
```

---

## 코드 품질 평가

### 강점 ✅
1. **spec_search.py**
   - BM25 + TF-IDF 조합으로 정교한 검색 구현
   - 한글/영어 동의어 처리 우수
   - CamelCase 자동 변형 처리 (lineSpacing → line-spacing)
   - 재랭킹 옵션으로 정확도 향상 가능

2. **chunk_builder.py**
   - Markdown 직접 파싱으로 데이터 신선도 보장
   - 라인/문자 오프셋 정밀 계산
   - 소스 파일 추적 기능

3. **전반적**
   - 유니코드 처리가 잘 되어 있음
   - 문서화 (docstring)가 명확함
   - 타입 힌트 사용으로 가독성 높음

### 개선 필요 ⚠️
1. **에러 처리 부족**
   - 파일 I/O 시 예외 처리 없음
   - JSON 파싱 실패 시 대응 없음

2. **테스트 코드 없음**
   - `tests/` 폴더에 실제 테스트 없음 (ARCHITECTURE.md에는 명시됨)

3. **로깅 부재**
   - 디버깅을 위한 로깅 메커니즘 없음
   - `print()` 대신 `logging` 모듈 사용 권장

---

## 우선순위 조치 항목

### 즉시 수정 (P0)
1. ✅ `build_assets_index.py:22` 잘못된 주석 제거
2. ✅ `spec_search.py` import 구문을 파일 상단으로 이동

### 단기 개선 (P1)
3. 타입 힌트 일관성 통일 (`list[str]` vs `List[str]`)
4. 에러 처리 추가 (try-except for file I/O)
5. main() 함수 리팩토링 (검색/출력 로직 분리)

### 중기 개선 (P2)
6. 단위 테스트 작성 (`tests/unit/`)
7. `logging` 모듈 도입
8. 정규표현식에 주석 추가 (가독성)

---

## 아키텍처 코멘트

### 현재 설계 평가
- **RAG 검색 시스템**: 40만자 문서를 청크 단위로 처리하는 전략은 적절함
- **BM25 선택**: TF-IDF보다 문서 길이 정규화가 우수하여 좋은 선택
- **동의어 확장**: 한글/영어 혼용 환경에 최적화됨

### 향후 고려사항
1. **벡터 임베딩**: 현재는 키워드 기반, 향후 의미 기반 검색 추가 검토
2. **캐싱**: 검색 결과 캐싱으로 성능 향상 가능
3. **인덱스 업데이트**: `hwpx_spec.md` 변경 시 자동 재인덱싱 필요

---

## 보안/성능 체크

### 보안
- ✅ 사용자 입력 검증 (argparse)
- ✅ 경로 조작 공격 방어 (Path 사용)
- ⚠️ 정규표현식 ReDoS 가능성 (복잡한 패턴에서)

### 성능
- ✅ 메모리: JSONL 스트리밍 방식 (한 줄씩 처리)
- ✅ 검색 속도: BM25 인메모리 인덱스로 충분히 빠름
- ⚠️ 큰 문서: `docs/hwpx_spec.md`가 더 커지면 청크 크기 조정 필요

---

## 종합 의견

**전체 평가: B+ (양호)**

프로젝트 초기 단계(Phase 0)로서 핵심 기능은 잘 구현되어 있음. 몇 가지 사소한 코드 스타일 문제와 누락된 에러 처리가 있으나, 전반적인 설계와 구현 품질은 우수함.

**즉시 조치 필요 항목:**
1. `build_assets_index.py:22` 잘못된 주석 제거
2. import 구문 위치 정리

**다음 단계 권장사항:**
1. 단위 테스트 작성으로 코드 안정성 확보
2. Phase 1(MD → HWPX 변환기) 진행 전 현재 코드 리팩토링
3. 에러 처리 및 로깅 강화

---

## 메타데이터

- **검토 일자**: 2025-11-15
- **검토 범위**: `tools/*.py`, `ARCHITECTURE.md`
- **코드 라인 수**: ~600 LOC
- **발견된 이슈**: 8개 (높음 1, 중간 3, 낮음 4)
