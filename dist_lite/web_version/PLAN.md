# 📋 MD→HWPX 웹 버전 (순수 JavaScript) 구현 계획

> **Updated 2026-03-01** — 점진적 검증 전략(빈 문서 → 텍스트 → 표 → 도식도)으로 변경
>
> Python `converter/` 패키지(10개 모듈, 4,483줄)를
> 순수 JavaScript로 변환하여 **HTML 파일 1개**로 만드는 계획

---

## 핵심 설계 원칙

### 🎯 "매 Phase마다 한글에서 열어본다"

AI가 코드를 작성할 수는 있지만, **한글(HWP/HWPX)에서 실제로 열었을 때
글꼴이 맞는지, 표가 깨지는지, 여백이 맞는지는 사람이 직접 봐야 한다.**

따라서:
- ❌ 모든 모듈을 만든 뒤 마지막에 통합 테스트 (위험)
- ✅ **빈 문서부터 동작시키고, 매 단계 기능을 추가하며 한글 확인** (안전)

```
Phase 1 → 빈 HWPX 생성          → 한글에서 열림? ✅
Phase 2 → 텍스트만 있는 HWPX     → 제목/소제목/본문 맞음? ✅
Phase 3 → 표 포함 HWPX          → 표/강조/요약표 맞음? ✅
Phase 4 → 프로세스/도식도 포함    → 흐름도/도식도 맞음? ✅
Phase 5 → UI + 패키징           → 웹에서 드래그앤드롭 동작? ✅
```

---

## 최종 목표

```
MD변환기.html (단일 파일, 서버 불필요)
├── [인라인] JSZip (~30KB minified)
├── JS 엔진 (Python 1:1 대응)
│   ├── models       ← converter/models.py
│   ├── config       ← converter/config.py
│   ├── parser       ← converter/parser.py
│   ├── inline       ← renderers/inline.py
│   ├── textFitting  ← renderers/text_fitting.py
│   ├── tables       ← renderers/tables.py
│   ├── processDiag  ← renderers/process_diagram.py
│   ├── xmlBuilder   ← converter/xml_builder.py
│   └── converter    ← converter/md_to_hwpx.py
├── 미리보기 PNG (base64 인라인)
└── 웹 UI (드래그&드롭)
```

---

## 단계별 구현 계획 (점진적 확장)

---

### Phase 1: 빈 문서 HWPX 생성 (Day 1-2)

**목표**: JS로 빈 HWPX 파일을 만들어 **한글에서 열리는지 확인**

```
포함 모듈:
├── models     — BlockType, Block, DocumentMetadata (최소)
├── config     — NS, q(), mmToHwp(), 상수, attachSecPr()
├── xmlBuilder — 전체 XML 빌더 (이것이 핵심)
│   ├── buildHeaderXml()     ← 846줄, 가장 큰 부분
│   ├── buildSection0Xml()   ← 최소: 빈 문단 1개만
│   ├── buildContentHpf()
│   ├── buildContainerXml()
│   ├── buildVersionXml()
│   ├── buildSettingsXml()
│   ├── buildManifestXml()
│   └── buildContainerRdf()
├── converter  — writeHwpx() (JSZip으로 ZIP 패키징)
└── previewData — PREVIEW_PNG base64
```

**XML 생성 전략**: 문자열 템플릿

```javascript
// Python ET.SubElement 패턴 대신 문자열 조합
function buildVersionXml() {
  return `<?xml version="1.0" encoding="UTF-8"?>
<hv:HCFVersion xmlns:hv="http://www.hancom.co.kr/hwpml/2011/version"
  Major="1" Minor="4" Micro="0" BuildNumber="22"/>`;
}
```

**테스트 방법**:
```
1. 브라우저 콘솔에서 convertMdToHwpx("") 실행
2. .hwpx 다운로드
3. 한글에서 열기 → 빈 페이지가 보이면 성공 ✅
```

**이 Phase가 가장 중요** — 여기서 header.xml(폰트/스타일/테두리)이 맞으면,
이후 Phase는 section0.xml에 문단을 추가하는 것뿐이라 상대적으로 안전.

**리스크 집중 지점**:
- borderFill 42개 정의 (반복 패턴 → 헬퍼 함수로 생성)
- charPr 32개 정의 (반복 패턴)
- paraPr ~20개 정의
- 네임스페이스 선언 누락 시 한글이 거부

---

### Phase 2: 텍스트 문단 렌더링 (Day 3)

**목표**: 제목/소제목/본문/설명 등 **텍스트 블록**을 렌더링

```
추가 모듈:
├── parser     — parseMdLines() (전체 파서)
├── inline     — splitBoldSegments(), stripBoldMarkup(),
│                appendTextWithBold(), buildPreviewText()
└── xmlBuilder 보강
    ├── buildSection0Xml() 업그레이드
    │   ├── 일반 문단 (SUBTITLE, BODY, DESC2, DESC3, PLAIN)
    │   ├── Bold 텍스트 처리 (**굵게**)
    │   ├── 스페이서 문단 (블록 간 간격)
    │   └── 머리말/꼬리말 (appendHeaderFooterCtrl)
    └── buildDocumentMetadata()
```

**테스트 방법**:
```
1. 간단한 MD 텍스트로 변환:
   <주제목>테스트 문서

   □ 소제목입니다
   ◦ 본문 내용
   - 설명 레벨2

2. .hwpx 다운로드 → 한글에서 열기
3. 확인사항:
   - 제목이 표 안에 잘 나오는가?
   - 소제목/본문/설명의 글꼴과 크기가 맞는가?
   - Bold 텍스트(**굵게**)가 적용되는가?
   - 머리말/꼬리말이 보이는가?
```

---

### Phase 3: 표 렌더링 (Day 4-5)

**목표**: 마크다운 표, 제목표, 강조표, 요약표 렌더링

```
추가 모듈:
├── textFitting — visualTextWidth(), fitCellText(), computeColWidths()
└── tables      — createTableRow(), appendTitleTable(),
                  appendEmphasisTable(), appendMarkdownTable(),
                  appendSummaryTable()
```

**테스트 방법**:
```
1. STANDARD_TEST.md로 변환
2. .hwpx 다운로드 → 한글에서 열기
3. 확인사항:
   - 표 테두리가 정상인가?
   - 열 너비가 자동 조절되는가?
   - 헤더 행 배경색(연보라)이 맞는가?
   - 강조 상자(연두 배경)가 맞는가?
4. Python 출력과 나란히 비교
```

---

### Phase 4: 프로세스/도식도 렌더링 (Day 6)

**목표**: 프로세스 흐름도, 도식도 블록 렌더링

```
추가 모듈:
└── processDiagram — appendProcessTable(), appendDiagramTable()
```

**테스트 방법**:
```
1. test_diagram.md로 변환
2. .hwpx 다운로드 → 한글에서 열기
3. 확인사항:
   - 프로세스 단계 (제목행 파란배경 + 설명행 흰배경)
   - 화살표(→)가 2행 병합 셀에 맞는가?
   - 도식도 ↔ 좌우 배치가 정상인가?
   - ↓ 화살표 연결이 맞는가?
4. Python 출력과 나란히 비교
```

---

### Phase 5: UI + 단일 HTML 패키징 (Day 7)

**목표**: 웹 UI 연결, 최종 단일 HTML 파일 생성

```
작업:
├── UI (기존 run_web.py HTML 재사용)
│   ├── 드래그&드롭 → FileReader로 .md 읽기
│   ├── convertMdToHwpx(mdText) 호출 (서버 통신 제거)
│   ├── Blob → 자동 다운로드
│   └── 진행상태/에러 표시
│
├── 단일 파일 패키징
│   ├── JSZip minified 인라인 삽입
│   ├── PREVIEW_PNG base64 인라인
│   └── 모든 JS 모듈 → <script> 블록 하나로 연결
│
└── 최종 테스트
    ├── STANDARD_TEST.md → Python 출력과 한글에서 비교
    ├── test_diagram.md → Python 출력과 한글에서 비교
    ├── 실제 업무 문서 변환 테스트
    └── 파일 이름에 한글이 포함된 경우
```

---

## Python → JavaScript 모듈 매핑

### 소스 구조 대응표

| # | Python 모듈 | 줄 수 | JS 도입 Phase | 변환 난이도 |
|---|---|---|---|---|
| 1 | `models.py` | 92 | Phase 1 | ⭐ 쉬움 |
| 2 | `config.py` | 390 | Phase 1 | ⭐⭐ 중간 |
| 3 | `preview_data.py` | 335 | Phase 1 | ⭐ 쉬움 (복사) |
| 4 | `xml_builder.py` | 1,497 | Phase 1~2 | ⭐⭐⭐⭐ 최대 |
| 5 | `md_to_hwpx.py` | 121 | Phase 1 | ⭐ 쉬움 |
| 6 | `parser.py` | 307 | Phase 2 | ⭐⭐ 중간 |
| 7 | `renderers/inline.py` | 120 | Phase 2 | ⭐ 쉬움 |
| 8 | `renderers/text_fitting.py` | 242 | Phase 3 | ⭐⭐ 중간 |
| 9 | `renderers/tables.py` | 743 | Phase 3 | ⭐⭐⭐ 어려움 |
| 10 | `renderers/process_diagram.py` | 636 | Phase 4 | ⭐⭐⭐ 어려움 |

### 함수 매핑표

| Python 함수 | JS 함수 | Phase |
|---|---|---|
| `BlockType` (Enum) | `BlockType` (const) | 1 |
| `Block` (dataclass) | `class Block` | 1 |
| `_q(prefix, tag)` | `q(prefix, tag)` | 1 |
| `mm_to_hwp(mm)` | `mmToHwp(mm)` | 1 |
| `_attach_secpr()` | `attachSecPr()` | 1 |
| `build_header_xml()` | `buildHeaderXml()` | 1 |
| `build_section0_xml()` | `buildSection0Xml()` | 1→2 |
| `build_content_hpf()` | `buildContentHpf()` | 1 |
| `build_*_xml()` (5개) | `build*Xml()` | 1 |
| `write_hwpx()` | `writeHwpx()` | 1 |
| `parse_md_lines()` | `parseMdLines()` | 2 |
| `_split_bold_segments()` | `splitBoldSegments()` | 2 |
| `_append_text_with_bold()` | `appendTextWithBold()` | 2 |
| `_build_preview_text()` | `buildPreviewText()` | 2 |
| `_visual_text_width()` | `visualTextWidth()` | 3 |
| `_fit_cell_text()` | `fitCellText()` | 3 |
| `_compute_col_widths()` | `computeColWidths()` | 3 |
| `_create_table_row()` | `createTableRow()` | 3 |
| `_append_title_table()` | `appendTitleTable()` | 3 |
| `_append_markdown_table()` | `appendMarkdownTable()` | 3 |
| `_append_summary_table()` | `appendSummaryTable()` | 3 |
| `_append_process_table()` | `appendProcessTable()` | 4 |
| `_append_diagram_table()` | `appendDiagramTable()` | 4 |

---

## 기술 결정사항

### XML 생성: 문자열 템플릿 ✅

```javascript
// 이유: HWPX XML은 구조가 고정적 → 문자열이 가장 단순
// Python ET.SubElement(parent, tag, attribs) 패턴을
// JS 문자열 조합으로 1:1 변환

function buildBorderFill(id, borders = {}, fillBrush = null) {
  const edge = (side) => {
    const [type, width] = borders[side] || ['NONE', '0.1 mm'];
    return `<hh:${side}Border type="${type}" width="${width}" color="#000000"/>`;
  };
  const fill = fillBrush
    ? `<hc:fillBrush><hc:winBrush ${
        Object.entries(fillBrush).map(([k,v]) => `${k}="${v}"`).join(' ')
      }/></hc:fillBrush>`
    : '';

  return `<hh:borderFill id="${id}" threeD="0" shadow="0"
    centerLine="NONE" breakCellSeparateLine="0">
  <hh:slash type="NONE" Crooked="0" isCounter="0"/>
  <hh:backSlash type="NONE" Crooked="0" isCounter="0"/>
  ${edge('left')}${edge('right')}${edge('top')}${edge('bottom')}
  <hh:diagonal type="SOLID" width="0.1 mm" color="#000000"/>
  ${fill}
</hh:borderFill>`;
}
```

### ZIP: JSZip v3 (MIT) ✅

```javascript
const zip = new JSZip();
zip.file("mimetype", "application/hwp+zip", { compression: "STORE" });
zip.file("Contents/header.xml", headerXml);
const blob = await zip.generateAsync({ type: "blob" });
```

### 스타일 설정: JS 직접 정의 ✅

```javascript
const CONFIG = {
  hwpPerMm: 283.46,
  page: { widthMm: 210, heightMm: 297, ... },
  styles: {
    title: { styleId: 14, paraPrId: 14, charPrId: 5 },
    body:  { styleId: 5,  paraPrId: 5,  charPrId: 0 },
  },
};
```

---

## 검증 체크리스트

### Phase 1 검증 (빈 문서)
- [ ] .hwpx가 생성되는가?
- [ ] 한글에서 오류 없이 열리는가?
- [ ] 빈 페이지가 표시되는가?
- [ ] 페이지 크기/여백이 Python 출력과 동일한가?

### Phase 2 검증 (텍스트)
- [ ] <주제목>이 표 안에 렌더링되는가?
- [ ] □ 소제목의 글꼴/크기가 맞는가?
- [ ] ◦ 본문의 글꼴/크기가 맞는가?
- [ ] **굵게** 텍스트가 적용되는가?
- [ ] 머리말/꼬리말이 표시되는가?
- [ ] 블록 간 간격(스페이서)이 맞는가?

### Phase 3 검증 (표)
- [ ] 표 테두리 스타일이 맞는가?
- [ ] 헤더 행 배경색(연보라)이 맞는가?
- [ ] 열 너비가 자동 조절되는가?
- [ ] 텍스트 피팅(자간/폰트 축소)이 동작하는가?
- [ ] 강조 상자(연두 배경)가 맞는가?
- [ ] 요약표가 맞는가?

### Phase 4 검증 (프로세스/도식도)
- [ ] 프로세스 단계 배경색(파란/흰)이 맞는가?
- [ ] 화살표(→) 셀이 2행 병합되는가?
- [ ] 도식도 ↔ 좌우 배치가 정상인가?
- [ ] ↓ 화살표 연결이 맞는가?

### Phase 5 검증 (최종)
- [ ] 웹에서 .md 파일 드래그앤드롭이 동작하는가?
- [ ] STANDARD_TEST.md 변환 결과가 Python과 동일한가?
- [ ] test_diagram.md 변환 결과가 Python과 동일한가?
- [ ] 실제 업무 문서가 정상 변환되는가?

---

## 리스크 & 완화 방안

| 리스크 | 확률 | 영향 | 완화 |
|---|---|---|---|
| header.xml 속성 누락 → 한글 거부 | 중간 | 높음 | **Phase 1에서 빈 문서로 즉시 검증** |
| 네임스페이스 오타 | 중간 | 높음 | Python XML 출력과 diff 비교 |
| borderFill/charPr 반복 변환 실수 | 중간 | 중간 | 헬퍼 함수로 패턴 추출 |
| 한글 텍스트 인코딩 | 낮음 | 중간 | JS UTF-8 네이티브 |
| JSZip mimetype 순서 | 중간 | 높음 | 첫 파일로 STORE 등록 |
| 표 렌더링 미세 차이 | 높음 | 낮음 | Phase 3에서 조기 발견 |

---

## 예상 일정

| Phase | 작업 | 일수 | 검증 |
|---|---|---|---|
| 1 | 빈 문서 HWPX 생성 | 2일 | 한글에서 열기 ✅ |
| 2 | 텍스트 문단 렌더링 | 1일 | 한글에서 확인 ✅ |
| 3 | 표 렌더링 | 2일 | 한글에서 확인 ✅ |
| 4 | 프로세스/도식도 | 1일 | 한글에서 확인 ✅ |
| 5 | UI + 단일 HTML | 1일 | 웹 동작 확인 ✅ |
| | **총 7일** | | **매 단계 한글 검증** |

---

## 파일 구조

```
dist_lite/web_version/
├── PLAN.md              ← 이 문서
├── MD변환기.html         ← 최종 산출물 (단일 파일)
└── dev/                 ← 개발용 (완성 후 merge)
    ├── index.html       ← 테스트 UI (콘솔 + 다운로드 버튼)
    ├── models.js        ← Phase 1
    ├── config.js        ← Phase 1
    ├── previewData.js   ← Phase 1
    ├── xmlBuilder.js    ← Phase 1~2
    ├── converter.js     ← Phase 1
    ├── parser.js        ← Phase 2
    ├── inline.js        ← Phase 2
    ├── textFitting.js   ← Phase 3
    ├── tables.js        ← Phase 3
    └── processDiagram.js ← Phase 4
```
