# 📋 MD→HWPX 웹 버전 (순수 JavaScript) 구현 계획

> Python `md_to_hwpx.py` (4,236줄) + `template_loader.py` (604줄)을
> 순수 JavaScript로 변환하여 **HTML 파일 1개**로 만드는 계획

---

## 최종 목표

```
MD변환기.html (단일 파일)
├── [내장] JSZip 라이브러리 (~30KB minified)
├── [내장] 스타일 설정 (core_styles.yaml → JS 객체)
├── [내장] 마크다운 파서
├── [내장] HWPX XML 생성기
├── [내장] ZIP 패키징
└── [내장] 웹 UI (드래그&드롭)
```

---

## 단계별 구현 계획

### Phase 1: 기반 구조 (파일: `MD변환기.html`)
- [ ] HTML 껍데기 + UI (기존 run_web.py의 HTML_PAGE 재사용)
- [ ] JSZip 라이브러리 CDN → 인라인 임베딩
- [ ] `core_styles.yaml` → JavaScript 객체로 변환
- [ ] 상수/설정값 매핑 (Python 30~286줄 → JS)
- [ ] 테스트: HTML 열리고 UI 동작 확인

### Phase 2: 마크다운 파서 (`parse_md_lines` 변환)
- [ ] BlockType enum → JS 상수
- [ ] Block, TableBlock, ProcessBlock 등 데이터 모델 → JS class
- [ ] `parse_md_lines()` 변환 (Python 626~900줄)
  - `_parse_table_block()` — 표 파싱
  - `_parse_summary_block()` — 요약표 파싱
  - `_parse_process_block()` — 프로세스 흐름도 파싱
  - `_parse_diagram_block()` — 도식도 파싱
  - 일반 블록 분류 (제목, 소제목, 본문 등)
- [ ] 테스트: sample.md 파싱 → 콘솔에 블록 구조 출력

### Phase 3: XML 생성 - 기본 구조
- [ ] XML 네임스페이스/헬퍼 (`_q()`, NS 상수 등)
- [ ] `build_header_xml()` (Python 2934~3780줄, 846줄) ← **최대 덩어리**
  - 폰트 정의 (`_add_font`, `add_fontface`)
  - 테두리/채우기 (`add_border_fill`, `add_border_fill_custom`)
  - 글자 속성 (`add_char_pr`)
  - 문단 속성 (`add_para_pr`)
  - 스타일 정의 (`add_style`)
- [ ] `build_content_hpf()` — 매니페스트
- [ ] `build_container_xml()` — 컨테이너
- [ ] `build_version_xml()` — 버전
- [ ] `build_settings_xml()` — 설정
- [ ] `build_manifest_xml()` — ODF 매니페스트
- [ ] `build_container_rdf()` — RDF 메타데이터
- [ ] 테스트: 빈 문서 HWPX 생성 → 한글에서 열리는지 확인

### Phase 4: XML 생성 - 본문 콘텐츠
- [ ] `build_section0_xml()` — 메인 섹션 빌더 (Python 3783~3931줄)
- [ ] `_attach_secpr()` — 섹션/페이지 설정 (1082~1219줄)
- [ ] `_append_header_footer_ctrl()` — 머리말/꼬리말 (1222~1374줄)
- [ ] 기본 문단 생성 (제목/소제목/본문/DESC2/DESC3)
- [ ] `_append_title_table()` — 주제목 상자 (1442~1555줄)
- [ ] `_append_emphasis_table()` — 강조 상자 (1558~1638줄)
- [ ] Bold 텍스트 처리 (`_split_bold_segments`, `_append_text_with_bold`)
- [ ] 테스트: 기본 텍스트 문서 변환 확인

### Phase 5: XML 생성 - 표/프로세스/도식도
- [ ] `_compute_col_widths()` — 열 너비 자동 계산 (1800~1870줄)
- [ ] `_fit_cell_text()` — 텍스트 피팅 (1761~1797줄)
- [ ] `_append_markdown_table()` — 일반 표 렌더링 (1873~2144줄)
- [ ] `_append_summary_table()` — 요약표 렌더링 (2147~2312줄)
- [ ] `_append_process_table()` — 프로세스 흐름도 (2316~2586줄)
- [ ] `_append_diagram_table()` — 도식도 (2589~2885줄)
- [ ] 테스트: sample.md 전체 변환 → 한글에서 동일 결과 확인

### Phase 6: 통합/패키징/최종테스트
- [ ] `write_hwpx()` — ZIP 패키징 (JSZip 사용)
- [ ] `convert_md_to_hwpx()` — 전체 파이프라인 연결
- [ ] 웹 UI 연결 (파일 업로드 → 변환 → 다운로드)
- [ ] 전체 테스트 (sample.md + 실제 문서)
- [ ] 파일 크기 최적화 (JSZip 인라인)

---

## 함수 매핑표 (Python → JavaScript)

| Python 함수 | JS 함수 | 줄 수 | 난이도 |
|---|---|---|---|
| `_load_config()` | (삭제, JS 객체 직접 사용) | ~10 | - |
| `_build_style_maps()` | `buildStyleMaps()` | ~30 | 쉬움 |
| `parse_md_lines()` | `parseMdLines()` | ~280 | 중간 |
| `_split_bold_segments()` | `splitBoldSegments()` | ~15 | 쉬움 |
| `_append_text_with_bold()` | `appendTextWithBold()` | ~25 | 쉬움 |
| `_visual_text_width()` | `visualTextWidth()` | ~25 | 쉬움 |
| `_estimate_line_count()` | `estimateLineCount()` | ~50 | 중간 |
| `_fit_cell_text()` | `fitCellText()` | ~40 | 중간 |
| `_compute_col_widths()` | `computeColWidths()` | ~70 | 중간 |
| `_attach_secpr()` | `attachSecPr()` | ~140 | 중간 |
| `_append_header_footer_ctrl()` | `appendHeaderFooterCtrl()` | ~150 | 중간 |
| `_create_table_row()` | `createTableRow()` | ~60 | 중간 |
| `_append_title_table()` | `appendTitleTable()` | ~110 | 중간 |
| `_append_emphasis_table()` | `appendEmphasisTable()` | ~80 | 중간 |
| `_append_markdown_table()` | `appendMarkdownTable()` | ~270 | **어려움** |
| `_append_summary_table()` | `appendSummaryTable()` | ~165 | 중간 |
| `_append_process_table()` | `appendProcessTable()` | ~270 | **어려움** |
| `_append_diagram_table()` | `appendDiagramTable()` | ~300 | **어려움** |
| `build_header_xml()` | `buildHeaderXml()` | ~846 | **최대** |
| `build_section0_xml()` | `buildSection0Xml()` | ~150 | 중간 |
| `build_content_hpf()` | `buildContentHpf()` | ~80 | 쉬움 |
| `build_container_xml()` | `buildContainerXml()` | ~40 | 쉬움 |
| `build_version_xml()` | `buildVersionXml()` | ~22 | 쉬움 |
| `build_settings_xml()` | `buildSettingsXml()` | ~16 | 쉬움 |
| `build_manifest_xml()` | `buildManifestXml()` | ~11 | 쉬움 |
| `build_container_rdf()` | `buildContainerRdf()` | ~34 | 쉬움 |
| `write_hwpx()` | `writeHwpx()` | ~50 | 쉬움 (JSZip) |

---

## 기술 결정사항

### XML 생성 방식
- Python: `xml.etree.ElementTree` (DOM 조작 후 직렬화)
- **JS: 문자열 템플릿 리터럴로 직접 생성** (DOM 불필요, 더 직관적)
  - HWPX XML은 구조가 고정적이라 문자열이 더 효율적

### ZIP 생성
- Python: `zipfile.ZipFile`
- **JS: `JSZip` 라이브러리** (MIT 라이선스, ~30KB)

### 스타일 설정
- Python: `core_styles.yaml` → `template_loader.py` → `StyleConfig` 객체
- **JS: YAML 내용을 JS 객체 리터럴로 직접 변환** (YAML 파서 불필요)

---

## 리스크 & 완화 방안

| 리스크 | 확률 | 완화 |
|---|---|---|
| XML 속성 오타/누락 → 한글 오류 | 중간 | Python 출력과 byte-diff 비교 |
| `build_header_xml` 846줄 변환 실수 | 중간 | 문자열 템플릿으로 단순화 |
| 한글 인코딩 문제 | 낮음 | JS는 네이티브 Unicode |
| 큰 파일 변환 시 브라우저 메모리 | 낮음 | 일반 보고서 수준이면 문제 없음 |
