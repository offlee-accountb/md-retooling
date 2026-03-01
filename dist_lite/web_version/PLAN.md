# 📋 MD→HWPX 웹 버전 (순수 JavaScript) 구현 계획

> **Updated 2026-03-01** — Python 모듈화 리팩토링 완료(Phase 1-6) 후 갱신
>
> Python `converter/` 패키지(10개 모듈, 4,483줄)를
> 순수 JavaScript로 변환하여 **HTML 파일 1개**로 만드는 계획

---

## 최종 목표

```
MD변환기.html (단일 파일, 서버 불필요)
├── [인라인] JSZip (~30KB minified)
├── JS 모듈 (Python 1:1 대응)
│   ├── models.js         ← converter/models.py        (92줄)
│   ├── config.js         ← converter/config.py         (390줄)
│   ├── parser.js         ← converter/parser.py          (307줄)
│   ├── inline.js         ← renderers/inline.py          (120줄)
│   ├── textFitting.js    ← renderers/text_fitting.py    (242줄)
│   ├── tables.js         ← renderers/tables.py          (743줄)
│   ├── processDiagram.js ← renderers/process_diagram.py (636줄)
│   ├── xmlBuilder.js     ← converter/xml_builder.py     (1,497줄)
│   └── converter.js      ← converter/md_to_hwpx.py      (121줄)
├── 미리보기 PNG (base64 인라인)
└── 웹 UI (드래그&드롭, 기존 run_web.py HTML 재사용)
```

**핵심 차이**: 서버 불필요. 브라우저에서 `.md` 읽기 → JS로 변환 → JSZip으로 `.hwpx` 생성 → 다운로드.

---

## Python → JavaScript 모듈 매핑

### 소스 구조 대응표

| # | Python 모듈 | JS 섹션 | 줄 수 | 변환 난이도 | 비고 |
|---|---|---|---|---|---|
| 1 | `models.py` | `models.js` | 92 | ⭐ 쉬움 | dataclass → JS class |
| 2 | `config.py` | `config.js` | 390 | ⭐⭐ 중간 | YAML 로딩 → JS 객체 리터럴 |
| 3 | `preview_data.py` | (인라인 상수) | 335 | ⭐ 쉬움 | base64 문자열 복사 |
| 4 | `renderers/inline.py` | `inline.js` | 120 | ⭐ 쉬움 | 정규식 + 문자열 처리 |
| 5 | `renderers/text_fitting.py` | `textFitting.js` | 242 | ⭐⭐ 중간 | 순수 계산 로직 |
| 6 | `renderers/tables.py` | `tables.js` | 743 | ⭐⭐⭐ 어려움 | XML DOM 조작 |
| 7 | `renderers/process_diagram.py` | `processDiagram.js` | 636 | ⭐⭐⭐ 어려움 | XML DOM 조작 |
| 8 | `parser.py` | `parser.js` | 307 | ⭐⭐ 중간 | 정규식 + 상태 머신 |
| 9 | `xml_builder.py` | `xmlBuilder.js` | 1,497 | ⭐⭐⭐⭐ 최대 | 846줄 header + 메타 |
| 10 | `md_to_hwpx.py` | `converter.js` | 121 | ⭐ 쉬움 | ZIP 패키징 (JSZip) |
| | **합계** | | **4,483** | | |

---

## 단계별 구현 계획

### Phase 1: 기반 구조 + 설정 (Day 1)

**목표**: HTML 껍데기, JS 모듈 구조, 설정/상수 변환

```
작업:
├── HTML_PAGE (run_web.py에서 복사 + 오프라인 변환 로직 교체)
├── JSZip CDN → <script> 인라인 임베딩
├── models.py → models.js
│   ├── BlockType enum → const BlockType = { TITLE: 'TITLE', ... }
│   ├── Block class → class Block { constructor(...) {} }
│   ├── TableBlock, ProcessBlock, DiagramBlock 등
│   └── DocumentMetadata class
├── config.py → config.js
│   ├── core_styles.yaml → JS 객체 리터럴 (YAML 파서 불필요)
│   ├── _build_style_maps() → buildStyleMaps()
│   ├── 모든 상수 (PAGE_WIDTH_HWP, TABLE_WIDTH_HWP, ...)
│   ├── NS 네임스페이스 → const NS = { ... }
│   ├── _q() → q(prefix, tag)
│   ├── mm_to_hwp() → mmToHwp()
│   └── _attach_secpr() → attachSecPr()
└── preview_data.py → PREVIEW_PNG_BASE64 상수 (그대로 복사)
```

**테스트**: HTML 열기 → 콘솔에서 `BlockType.TITLE`, `q('hp','p')` 동작 확인

---

### Phase 2: 파서 + 인라인 (Day 2)

**목표**: MD 텍스트 → Block 배열 변환

```
작업:
├── inline.js
│   ├── BOLD_PATTERN → /\*\*(.*?)\*\*/g
│   ├── splitBoldSegments(text)
│   ├── stripBoldMarkup(text)
│   ├── formatBlockPreviewText(block)
│   └── buildPreviewText(blocks, title)
├── parser.js
│   ├── parseMdLines(lines) — 메인 파서
│   ├── parseTableBlock() — <표 제목:> 파싱
│   ├── parseSummaryBlock() — <요약표:> 파싱
│   ├── parseProcessBlock() — <프로세스:> 파싱
│   └── parseDiagramBlock() — <도식도:> 파싱
└── 테스트 콘솔 출력
```

**테스트**: `STANDARD_TEST.md` 텍스트를 textarea에 붙여넣기 → `parseMdLines()` → 블록 구조 콘솔 출력

---

### Phase 3: XML 생성 핵심 (Day 3-4) ← **최대 작업량**

**목표**: header.xml, section0.xml 등 XML 생성

```
작업:
├── XML 생성 전략 결정
│   ├── 방법 A: 문자열 템플릿 리터럴 (추천 — 구조 고정적)
│   └── 방법 B: DOM API (document.createElementNS) → 불필요하게 복잡
│
├── xmlBuilder.js (1,497줄 → 예상 ~1,200줄 JS)
│   ├── 메타데이터 유틸
│   │   ├── formatLocalizedDatetime()
│   │   ├── isoformatUtc()
│   │   ├── extractDocTitle()
│   │   ├── buildHeaderFooterText()
│   │   └── buildDocumentMetadata()
│   │
│   ├── buildHeaderXml() ← 846줄, 최대 덩어리
│   │   ├── fontfaces (7개 언어 × 3개 글꼴)
│   │   ├── borderFills (42개) ← 대부분 데이터, 반복 패턴
│   │   ├── charProperties (32개) ← 반복 패턴
│   │   ├── paraProperties (~20개) ← 반복 패턴
│   │   └── styles (~19개)
│   │
│   ├── appendHeaderFooterCtrl()
│   ├── buildSection0Xml(blocks, docMeta) ← 본문 문단 생성
│   ├── buildContentHpf(docMeta)
│   ├── buildContainerXml()
│   ├── buildVersionXml()
│   ├── buildSettingsXml()
│   ├── buildManifestXml()
│   └── buildContainerRdf()
│
└── appendTextWithBold()/appendTextWithBoldCustom() → inline.js에 추가
```

**핵심 전략 — `build_header_xml` 단순화**:
```javascript
// Python: ET.SubElement + 속성 딕셔너리 → 복잡한 DOM 조작
// JS: 문자열 템플릿으로 직접 생성 (훨씬 간결)

function buildBorderFill(id, borders, fillBrush) {
  const edges = ['left','right','top','bottom'].map(side => {
    const [type, width] = borders?.[side] || ['NONE', '0.1 mm'];
    return `<hh:${side}Border type="${type}" width="${width}" color="#000000"/>`;
  }).join('\n');

  const fill = fillBrush
    ? `<hc:fillBrush><hc:winBrush ${Object.entries(fillBrush).map(([k,v])=>`${k}="${v}"`).join(' ')}/></hc:fillBrush>`
    : '';

  return `<hh:borderFill id="${id}" threeD="0" shadow="0" centerLine="NONE" breakCellSeparateLine="0">
    <hh:slash type="NONE" Crooked="0" isCounter="0"/>
    <hh:backSlash type="NONE" Crooked="0" isCounter="0"/>
    ${edges}
    <hh:diagonal type="SOLID" width="0.1 mm" color="#000000"/>
    ${fill}
  </hh:borderFill>`;
}
```

**테스트**: 빈 Block 배열 → HWPX 생성 → 한글에서 열리는지 확인

---

### Phase 4: 렌더러 — 표/문단 (Day 5-6)

**목표**: 제목표, 강조표, 일반표, 요약표 렌더링

```
작업:
├── textFitting.js
│   ├── TABLE_FIT_CHAR_IDS, FIT_CANDIDATES
│   ├── visualTextWidth(text)
│   ├── estimateLineCount(text, width, fontSize)
│   ├── fitCellText(text, colWidthHwp, ...)
│   └── computeColWidths(rows, totalWidth)
│
├── tables.js
│   ├── createTableRow(tbl, { height, cells })
│   ├── appendTitleTable(root, block, ...)
│   ├── appendEmphasisTable(root, block, ...)
│   ├── appendMarkdownTable(root, tableBlock, ...) ← 270줄
│   └── appendSummaryTable(root, summaryBlock, ...) ← 165줄
│
└── inline.js 보강
    ├── appendTextWithBold(paragraph, charId, text)
    └── appendTextWithBoldCustom(paragraph, charId, text, boldCharId)
```

**테스트**: `STANDARD_TEST.md` → Python 출력과 XML byte-diff 비교

---

### Phase 5: 렌더러 — 프로세스/도식도 (Day 7)

**목표**: 프로세스 흐름도, 도식도 렌더링

```
작업:
├── processDiagram.js
│   ├── appendProcessTable(root, processBlock, ...) ← 270줄
│   │   ├── 단계별 셀 (제목행 + 설명행)
│   │   ├── 화살표 셀 (→)
│   │   └── 2행 머지
│   │
│   └── appendDiagramTable(root, diagramBlock, ...) ← 300줄
│       ├── 박스 셀 (제목 + 설명)
│       ├── 연결 화살표 (↓, ↔)
│       └── 좌우 배치 (↔ 시)
│
└── 테스트: test_diagram.md 변환 확인
```

---

### Phase 6: 통합 + 단일 HTML 패키징 (Day 8)

**목표**: 모든 모듈 통합, 단일 HTML 파일로 배포

```
작업:
├── converter.js — ZIP 패키징
│   ├── writeHwpx(blocks) → JSZip 사용
│   │   ├── mimetype (ZIP_STORED)
│   │   ├── version.xml, settings.xml
│   │   ├── Preview/PrvText.txt, PrvImage.png
│   │   ├── META-INF/manifest.xml, container.xml, container.rdf
│   │   └── Contents/header.xml, section0.xml, content.hpf
│   └── convertMdToHwpx(mdText) → Blob
│
├── UI 연결
│   ├── 파일 드래그&드롭 (기존 run_web.py HTML 재사용)
│   ├── FileReader로 .md 읽기
│   ├── convertMdToHwpx() 호출
│   ├── Blob → 자동 다운로드
│   └── 진행상태 표시
│
├── 단일 파일 패키징
│   ├── JSZip minified 인라인 삽입
│   ├── PREVIEW_PNG base64 인라인
│   └── 모든 JS 모듈 → <script> 블록 하나로 연결
│
└── 최종 테스트
    ├── STANDARD_TEST.md → Python 출력과 diff
    ├── test_diagram.md → Python 출력과 diff
    └── 실제 업무 문서 테스트
```

---

## 함수 매핑표 (Python → JavaScript)

| Python 모듈 | Python 함수 | JS 함수 | 비고 |
|---|---|---|---|
| **models** | `BlockType` (Enum) | `BlockType` (const obj) | |
| | `Block` (dataclass) | `class Block` | |
| | `TableBlock` | `class TableBlock` | |
| | `DocumentMetadata` | `class DocumentMetadata` | |
| **config** | `_load_config()` | (제거) | JS 객체 직접 사용 |
| | `_build_style_maps()` | `buildStyleMaps()` | |
| | `_q(prefix, tag)` | `q(prefix, tag)` | |
| | `mm_to_hwp(mm)` | `mmToHwp(mm)` | |
| | `_attach_secpr(run)` | `attachSecPr()` | 문자열 반환 |
| **inline** | `_split_bold_segments()` | `splitBoldSegments()` | |
| | `_strip_bold_markup()` | `stripBoldMarkup()` | |
| | `_append_text_with_bold()` | `appendTextWithBold()` | |
| | `_build_preview_text()` | `buildPreviewText()` | |
| **text_fitting** | `_visual_text_width()` | `visualTextWidth()` | |
| | `_estimate_line_count()` | `estimateLineCount()` | |
| | `_fit_cell_text()` | `fitCellText()` | |
| | `_compute_col_widths()` | `computeColWidths()` | |
| **tables** | `_create_table_row()` | `createTableRow()` | |
| | `_append_title_table()` | `appendTitleTable()` | |
| | `_append_emphasis_table()` | `appendEmphasisTable()` | |
| | `_append_markdown_table()` | `appendMarkdownTable()` | |
| | `_append_summary_table()` | `appendSummaryTable()` | |
| **process_diagram** | `_append_process_table()` | `appendProcessTable()` | |
| | `_append_diagram_table()` | `appendDiagramTable()` | |
| **parser** | `parse_md_lines()` | `parseMdLines()` | |
| **xml_builder** | `build_header_xml()` | `buildHeaderXml()` | 문자열 반환 |
| | `build_section0_xml()` | `buildSection0Xml()` | 문자열 반환 |
| | `build_content_hpf()` | `buildContentHpf()` | |
| | `build_container_xml()` | `buildContainerXml()` | |
| | `build_version_xml()` | `buildVersionXml()` | |
| | `build_settings_xml()` | `buildSettingsXml()` | |
| | `build_manifest_xml()` | `buildManifestXml()` | |
| | `build_container_rdf()` | `buildContainerRdf()` | |
| | `_build_document_metadata()` | `buildDocumentMetadata()` | |
| **md_to_hwpx** | `write_hwpx()` | `writeHwpx()` | JSZip |
| | `convert_md_to_hwpx()` | `convertMdToHwpx()` | |

---

## 기술 결정사항

### XML 생성: 문자열 템플릿 방식 ✅

```
이유:
1. HWPX XML 구조는 고정적 (동적 DOM 조작 불필요)
2. Python ET.SubElement 패턴 → 문자열이 1:1 대응으로 더 단순
3. 디버깅 용이 (생성된 XML을 그대로 볼 수 있음)
4. 성능 우수 (DOM 파싱 없음)

단점:
- 특수문자 이스케이프 주의 (< > & " → &lt; &gt; &amp; &quot;)
- 들여쓰기 관리 필요
```

### ZIP: JSZip (v3, MIT) ✅

```javascript
const zip = new JSZip();
zip.file("mimetype", "application/hwp+zip", { compression: "STORE" });
zip.file("Contents/header.xml", headerXml);
// ...
const blob = await zip.generateAsync({ type: "blob" });
```

### 스타일 설정: JS 직접 정의 ✅

```javascript
// core_styles.yaml 내용을 JS 객체로 하드코딩
const CONFIG = {
  hwpPerMm: 283.46,
  page: { widthMm: 210, heightMm: 297, ... },
  styles: {
    title: { styleId: 14, paraPrId: 14, charPrId: 5 },
    body:  { styleId: 5,  paraPrId: 5,  charPrId: 0 },
    // ...
  },
  spacers: { ... },
};
```

---

## 검증 전략

### Byte-level 비교

```bash
# 1) Python으로 변환
python converter/md_to_hwpx.py samples/STANDARD_TEST.md /tmp/py_output.hwpx

# 2) JS 웹버전으로 변환 → JS출력.hwpx

# 3) ZIP 풀어서 XML 비교
unzip -o /tmp/py_output.hwpx -d /tmp/py_xml
unzip -o /tmp/js_output.hwpx -d /tmp/js_xml
diff -r /tmp/py_xml /tmp/js_xml
```

### 단계별 스냅샷 비교

각 Phase 완료 시:
1. 해당 모듈의 JS 출력과 Python 출력을 비교
2. Phase 3 이후 — 빈 문서 HWPX → 한글 오픈 테스트
3. Phase 4 이후 — STANDARD_TEST 전체 비교
4. Phase 6 — 실 업무 문서로 최종 검증

---

## 리스크 & 완화 방안

| 리스크 | 확률 | 영향 | 완화 |
|---|---|---|---|
| XML 속성 오타/누락 → 한글 오류 | 중간 | 높음 | Python 출력과 byte-diff 비교 |
| `buildHeaderXml` 대규모 변환 실수 | 중간 | 높음 | 반복 패턴을 헬퍼 함수로 추출 |
| 한글 텍스트 인코딩 | 낮음 | 중간 | JS 네이티브 Unicode, UTF-8 출력 |
| 큰 파일 메모리 | 낮음 | 낮음 | 일반 보고서 기준 문제 없음 |
| JSZip mimetype 순서 | 중간 | 높음 | `compression: "STORE"` + 첫 파일 등록 |

---

## 예상 일정

| Phase | 일수 | 누적 | 설명 |
|---|---|---|---|
| 1 기반+설정 | 1일 | 1일 | HTML, models, config, preview |
| 2 파서+인라인 | 1일 | 2일 | parser, inline |
| 3 XML 핵심 | 2일 | 4일 | xmlBuilder (최대 작업) |
| 4 표 렌더러 | 2일 | 6일 | textFitting, tables, inline 보강 |
| 5 프로세스/도식도 | 1일 | 7일 | processDiagram |
| 6 통합+패키징 | 1일 | 8일 | converter, UI, 단일 HTML |
| | **총 8일** | | |

---

## 파일 구조 (개발 중)

```
dist_lite/web_version/
├── PLAN.md              ← 이 문서
├── MD변환기.html         ← 최종 산출물 (단일 파일)
└── dev/                 ← 개발용 분리 파일 (완성 후 merge)
    ├── index.html       ← UI + 모듈 로딩
    ├── models.js
    ├── config.js
    ├── parser.js
    ├── inline.js
    ├── textFitting.js
    ├── tables.js
    ├── processDiagram.js
    ├── xmlBuilder.js
    └── converter.js
```

개발 중에는 `dev/` 안에서 ES 모듈(`import/export`)로 작업하고,
최종 배포 시 하나의 `MD변환기.html`로 합침.
