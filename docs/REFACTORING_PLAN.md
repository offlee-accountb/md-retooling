# MD → HWPX 변환기 리팩토링 계획서

> **작업 브랜치**: `feat/vision-hybrid-pipeline`
> **안정 백업**: `complete-1-pre-refactor` (태그: `v1.0-pre-refactor`)
> **작성일**: 2026-03-01

---

## 1. 현재 상태 분석

### 1.1 파일 크기
- `converter/md_to_hwpx.py` — **4,308줄**, 173KB
- 단일 파일에 설정/파서/렌더러/빌더/CLI가 모두 포함

### 1.2 코드 영역 분포 (줄 번호 기준)

| 영역 | 범위 | 줄 수 | 주요 내용 |
| --- | --- | ---: | --- |
| **설정/상수** | 1-304 | ~300 | YAML 로드, BlockType enum, 스타일 매핑, 상수 |
| **Base64 미리보기** | 305-637 | ~330 | `PREVIEW_PNG_BASE64` (인라인 이미지 데이터) |
| **파서** | 638-936 | ~300 | `parse_md_lines()` + 특수 블록 파서 |
| **인라인 처리** | 937-1025 | ~90 | Bold 분리, 미리보기 텍스트 |
| **메타데이터/유틸** | 1026-1240 | ~215 | 날짜 형식, 문서제목 추출, secPr 조립 |
| **머리말/꼬리말** | 1243-1400 | ~160 | 헤더/푸터 컨트롤 |
| **제목/강조 테이블** | 1403-1664 | ~260 | `_append_title_table`, `_append_emphasis_table` |
| **열 너비/텍스트 피팅** | 1665-1896 | ~230 | 시각적 너비 측정, 자간 조정 |
| **마크다운 표** | 1899-2170 | ~270 | `_append_markdown_table` |
| **요약표** | 2173-2338 | ~165 | `_append_summary_table` |
| **프로세스 흐름도** | 2342-2612 | ~270 | `_append_process_table` |
| **도식도** | 2615-2948 | ~330 | `_append_diagram_table` |
| **XML 빌더** | 2950-4223 | ~1270 | NS 정의, `build_header_xml`, `build_section0_xml`, `build_content_hpf` 등 |
| **HWPX 패키징/CLI** | 4224-4308 | ~85 | `write_hwpx`, `convert_md_to_hwpx`, `main` |

### 1.3 두 복사본 차이
- `converter/md_to_hwpx.py` vs `dist_lite/converter/md_to_hwpx.py`
- **차이점**: PyInstaller 호환 경로 설정 (`sys._MEIPASS`) 부분만 다름 (4줄)
- 나머지 로직은 **완전히 동일**

---

## 2. 리팩토링 목표

### 2.1 핵심 목표
1. **단일 4,300줄 파일** → **7~8개의 모듈**로 분리
2. 각 모듈의 **단일 책임 원칙** 준수
3. **기능 동일성 유지** — 리팩토링 전후 변환 결과가 바이트 단위로 같아야 함
4. `converter/` 와 `dist_lite/converter/` 의 **동기화 유지**

### 2.2 비목표 (이번에 하지 않는 것)
- 새로운 기능 추가 ❌
- 스타일/레이아웃 변경 ❌
- 성능 최적화 ❌
- 테스트 프레임워크 도입 ❌ (향후 과제)

---

## 3. 목표 모듈 구조

```
converter/
├── __init__.py               ← 패키지 초기화
├── config.py                 ← 설정/상수 (YAML 로드, BlockType, 스타일 매핑)
├── models.py                 ← 데이터 모델 (Block, TableBlock, DiagramBlock 등)
├── parser.py                 ← MD 파서 (parse_md_lines + 특수 블록 파서)
├── renderers/
│   ├── __init__.py
│   ├── inline.py             ← 인라인 처리 (Bold 분리, 텍스트 유틸)
│   ├── tables.py             ← 표 렌더러 (마크다운표, 제목표, 강조표, 요약표)
│   ├── process_diagram.py    ← 프로세스 흐름도 + 도식도
│   └── text_fitting.py       ← 열 너비 계산, 텍스트 피팅
├── xml_builder.py            ← XML 빌더 (header.xml, section0.xml 등)
├── hwpx_writer.py            ← HWPX 패키징 (ZIP 조립)
├── metadata.py               ← 문서 메타데이터, 날짜, secPr, 헤더/푸터
├── preview_data.py           ← PREVIEW_PNG_BASE64 (큰 상수 분리)
└── cli.py                    ← CLI 엔트리포인트 (main, convert_md_to_hwpx)
```

### 3.1 모듈별 상세

#### `config.py` (~150줄)
- `_load_config()` + `CONFIG` 글로벌
- `_build_style_maps()` → `PARA_STYLE_MAP`, `RUN_CHAR_OVERRIDE_MAP`, `STYLE_ID_MAP`
- `_build_spacer_char_map()` → `SPACER_CHAR_MAP`, `SPACER_MARKER_MAP`
- `_get_header_footer_ids()` → 각종 상수
- 치수 상수 (TABLE_WIDTH_HWPUNIT, ONE_PT_HWP 등)
- `NS` 딕셔너리, `_q()` 헬퍼, `ET.register_namespace` 호출

#### `models.py` (~80줄)
- `BlockType` enum
- `Block`, `TableBlock`, `SummaryTableBlock`, `ProcessBlock`
- `DiagramBox`, `DiagramBlock`
- `DocumentMetadata`

#### `parser.py` (~300줄)
- `parse_md_lines()` 함수 전체
- 내부 헬퍼: `_normalize_line`, `_parse_table_block`, `_parse_summary_block`, `_parse_process_block`, `_parse_diagram_block`

#### `renderers/inline.py` (~100줄)
- `BOLD_PATTERN`
- `_split_bold_segments()`
- `_append_text_with_bold()`, `_append_text_with_bold_custom()`
- `_strip_bold_markup()`
- `_format_block_preview_text()`, `_build_preview_text()`

#### `renderers/text_fitting.py` (~200줄)
- `_visual_text_width()`
- `_estimate_line_count()`
- `_fit_cell_text()`
- `_compute_col_widths()`
- 피팅 상수 (`FIT_CANDIDATES`, `CHAR_WIDTH_HWP` 등)

#### `renderers/tables.py` (~700줄)
- `_create_table_row()` — 공용 행 생성
- `_append_title_table()`
- `_append_emphasis_table()`
- `_append_markdown_table()` + 내부 헬퍼
- `_append_summary_table()`

#### `renderers/process_diagram.py` (~600줄)
- `_append_process_table()` + 내부 헬퍼 (`_get_circled`, `_make_cell`)
- `_append_diagram_table()` + 내부 헬퍼 (`_add_diagram_cell`)

#### `xml_builder.py` (~900줄)
- `build_header_xml()` + 모든 내부 헬퍼
  - `_add_font`, `add_fontface`, `add_border_fill`, `add_border_fill_custom`
  - `add_char_pr`, `add_para_pr`, `add_style`
- 관련 border_fill 관련 상수

#### `metadata.py` (~400줄)
- `_format_localized_datetime()`, `_isoformat_utc()`, `_safe_get_username()`
- `_extract_doc_title()`, `_build_header_footer_text()`
- `_build_document_metadata()`
- `_attach_secpr()`
- `_append_header_footer_ctrl()`

#### `hwpx_writer.py` (~200줄)
- `build_section0_xml()` — 블록 리스트를 섹션으로 조립
- `build_content_hpf()`
- `build_container_xml()`, `build_version_xml()`, `build_settings_xml()`
- `build_manifest_xml()`, `build_container_rdf()`
- `write_hwpx()`

#### `preview_data.py` (~340줄)
- `PREVIEW_PNG_BASE64` 상수만 분리 (330줄의 Base64 문자열)
- `PREVIEW_PNG_BYTES`

#### `cli.py` (~30줄)
- `convert_md_to_hwpx()`
- `main()`
- `if __name__ == "__main__"` 블록

#### `md_to_hwpx.py` (유지 — 호환성 레이어)
- 기존 `python converter/md_to_hwpx.py` 명령이 그대로 동작하도록
- 내부적으로 `from converter.cli import main` 후 위임
- 또는 모든 public API를 re-export

---

## 4. 리팩토링 단계 (Phase별)

### Phase 0: 준비 (현재 완료)
- [x] 안정 브랜치 `complete-1-pre-refactor` 푸쉬
- [x] 태그 `v1.0-pre-refactor` 생성
- [x] 3개 변환 테스트 통과 확인
- [x] 두 복사본의 차이 확인 (PyInstaller 경로만)

### Phase 1: 데이터 모델 + 상수 분리
1. `models.py` 생성 — BlockType, Block, TableBlock 등 데이터클래스 추출
2. `preview_data.py` 생성 — PREVIEW_PNG_BASE64 이동
3. `config.py` 생성 — 설정 로딩, 스타일 매핑, 상수
4. `md_to_hwpx.py`에서 import로 대체
5. **회귀 테스트** (3개 파일)

### Phase 2: 파서 분리
1. `parser.py` 생성 — `parse_md_lines()` 전체 이동
2. `md_to_hwpx.py`에서 import로 대체  
3. **회귀 테스트**

### Phase 3: 인라인 + 텍스트 피팅 분리
1. `renderers/__init__.py` 생성
2. `renderers/inline.py` 생성 — Bold 관련 함수
3. `renderers/text_fitting.py` 생성 — 열 너비, 피팅
4. **회귀 테스트**

### Phase 4: 렌더러 분리
1. `renderers/tables.py` 생성 — 표 렌더러들
2. `renderers/process_diagram.py` 생성 — 프로세스 + 도식도
3. **회귀 테스트**

### Phase 5: XML 빌더 + 메타데이터 분리
1. `metadata.py` 생성
2. `xml_builder.py` 생성 — `build_header_xml` 등
3. `hwpx_writer.py` 생성 — 패키징 로직
4. **회귀 테스트**

### Phase 6: CLI + 호환성 레이어 + dist_lite 동기화
1. `cli.py` 생성
2. `md_to_hwpx.py`를 호환성 레이어로 최소화
3. `dist_lite/converter/` 에 동일 구조 복사
4. dist_lite용 PyInstaller 경로 패치 적용
5. **최종 회귀 테스트** (3개 파일 × 2 경로)

---

## 5. 테스트 전략

### 매 Phase마다 실행
```bash
source .venv/bin/activate
python converter/md_to_hwpx.py samples/STANDARD_TEST.md output/STANDARD_TEST.hwpx
python converter/md_to_hwpx.py samples/test_diagram.md output/test_diagram.hwpx
python dist_lite/converter/md_to_hwpx.py samples/STANDARD_TEST.md output/STANDARD_TEST_lite.hwpx
```

### 결과 검증
- 변환 성공 (exit code 0)
- 출력 파일 생성 확인
- (가능하면) XML 내용 비교 — ZIP 내부 `Contents/section0.xml` 바이너리 diff

---

## 6. 주의사항

1. **순환 import 방지**: `config.py`가 가장 하위이고, 다른 모듈은 config만 import
   ```
   config.py, models.py  (의존성 없음)
        ↑
   parser.py             (models, config)
        ↑
   renderers/*           (models, config)
        ↑
   xml_builder.py        (config)
        ↑
   metadata.py           (models, config)
        ↑
   hwpx_writer.py        (모든 모듈)
        ↑
   cli.py                (hwpx_writer)
   ```

2. **내부 함수 → 모듈 함수 변환**: `parse_md_lines()` 안의 nested 함수들은 모듈 레벨 private 함수로 승격
   - 예: `parse_md_lines._parse_table_block()` → `_parse_table_block()`

3. **글로벌 상수 접근**: `CONFIG`, `PARA_STYLE_MAP` 등은 `config.py`에서 export
   - 다른 모듈에서 `from converter.config import CONFIG, PARA_STYLE_MAP` 사용

4. **dist_lite 동기화**: Phase 6에서 일괄 동기화 (중간에는 converter/만 수정)

---

## 7. 추진 여부 확인

리팩토링을 진행할까요? 진행 시 **Phase 1부터 순차적으로** 하나씩 완료하며, 매 Phase마다 회귀 테스트를 수행합니다.

선택지:
- **A) 전체 리팩토링 진행** — Phase 1~6 순차 실행
- **B) Phase 1만 먼저** — 데이터 모델/상수 분리 후 상태 확인
- **C) 계획 수정** — 모듈 구조나 Phase 순서 변경
- **D) 보류** — 다른 작업 우선
