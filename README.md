# Document Automation System (Phase 0)

Phase 0는 HWPX 표준 문서를 AI/사람이 빠르게 참조할 수 있도록 **간이 RAG 파이프라인**을 준비하는 단계입니다. 현재 레포지토리는 다음 두 가지 툴을 중심으로 구성됩니다.

1. `tools/chunk_builder.py` – `docs/hwpx_spec.md`를 섹션 단위로 분할하여 JSONL 청크를 생성합니다.
2. `tools/spec_search.py` – 생성된 청크를 대상으로 BM25 기반 키워드 검색을 수행합니다.

`ARCHITECTURE.md`에는 Phase 0~2.5까지의 전체 로드맵이 정리되어 있습니다. 본 README는 Phase 0 재현 방법에 초점을 맞춥니다.

---

## 요구 사항
- Python 3.11 이상 (표준 라이브러리만 사용)
- (선택) 가상환경: `python -m venv .venv && source .venv/bin/activate`

필요 시 아래 명령으로 의존성을 설치할 수 있습니다.

```bash
pip install -r requirements.txt
```

현재 Phase 0 도구는 추가 패키지 없이 동작하지만, 이후 Markdown 파서·XML 라이브러리를 도입할 경우 해당 파일을 갱신하십시오.

---

## 빠른 시작
1. **레포지토리 클론 후 루트로 이동**
   ```bash
   git clone <repo-url>
   cd md-retooling
   ```
2. **(선택) 가상환경 활성화 및 의존성 설치**
3. **아래 순서대로 Phase 0 파이프라인을 실행**

### 1) HWPX 스펙 청크 재생성
```bash
python3 tools/chunk_builder.py --spec docs/hwpx_spec.md --out tools/chunks
```
- `tools/chunks/sections.jsonl`: 섹션별 텍스트와 메타데이터
- `tools/chunks/chunks.meta.json`: 빌드 정보 요약

### 2) 키워드 검색
```bash
python3 tools/spec_search.py "줄간격 line-spacing" -k 5 --compact 1
```
- `--compact` 옵션은 히트 근처 몇 줄만 압축 출력합니다.
- `--json`을 지정하면 구조화된 결과를 반환하므로 LLM 프롬프트 작성에 활용하기 쉽습니다.

### 3) Phase 0 스모크 테스트 (선택)
청크 재생성 + 샘플 검색을 자동화한 스크립트를 제공합니다.
```bash
python3 tools/phase0_smoke_test.py
```
- 청크 파일 존재 여부 → 필요 시 자동 재빌드
- 대표 쿼리로 `spec_search.py` 실행
- 결과 요약과 함께 종료 코드로 성공/실패 여부를 전달

---

## 디렉터리 구조
```
.
├── ARCHITECTURE.md        # 전체 로드맵 및 컴포넌트 상세
├── README.md              # (현재 문서) Phase 0 가이드
├── docs/
│   └── hwpx_spec.md       # 통합된 HWPX 스펙 (원본 조각은 루트 okok*.md)
├── tools/
│   ├── chunk_builder.py   # 스펙 → 섹션 청크 생성
│   ├── spec_search.py     # BM25 기반 검색
│   ├── phase0_smoke_test.py (추가됨)
│   └── chunks/            # sections.jsonl + meta
└── ...
```

---

## Phase 0 완료 체크리스트
- [x] `docs/hwpx_spec.md` 최신 상태 유지
- [x] `tools/chunks/sections.jsonl` 재빌드 가능
- [x] `tools/spec_search.py`로 스펙 검색 가능
- [ ] README/requirements 최신화 (본 문서로 충족)
- [ ] 스모크 테스트 통과 (추가 스크립트 활용)

체크리스트를 충족한 후 Phase 1(MD→HWPX 변환기, HWPX 검증 툴)로 진입하는 것을 권장합니다.

---

## 자주 묻는 질문
### Q. 스펙에 새 버전이 릴리스되면?
1. `docs/hwpx_spec.md`를 교체합니다.
2. `python3 tools/chunk_builder.py ...`를 다시 실행합니다.
3. 필요시 `tools/hwpx_terms.alias.json` 등 보조 데이터도 갱신합니다.

### Q. LLM 프롬프트에 어떻게 사용하나요?
1. 위 검색 결과에서 필요한 섹션의 `anchor`, `text`를 복사합니다.
2. LLM에게 "다음 HWPX 스펙을 참고하여 ..."와 같이 전달합니다.
3. Phase 1 변환기가 준비되면 해당 코드와 연계됩니다.

---

## 다음 단계
- Phase 1 진입 전: 간단한 MD→HWPX 변환 PoC 및 테스트 설계
- Phase 1: 변환기 + 검증기 기본 기능 구현
- Phase 2 이후: LLM API 연동, 템플릿 자동화 등 `ARCHITECTURE.md` 참고
