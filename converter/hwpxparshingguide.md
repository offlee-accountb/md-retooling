# HWPX 포맷 파싱 가이드

## 개요
이 문서는 HWPX 문서 포맷의 내부 구조를 이해하고, Python을 통해 문서 데이터를 추출하여 객체로 구조화하는 방법을 설명합니다.

## 기본 정보
- HWPX는 ZIP 기반 XML 파일 형식
- KS X 6101 표준 문서 참조
- Python 내장 라이브러리만 사용 (zipfile, xml.etree.ElementTree)

## 사용 라이브러리

```python
import zipfile
import xml.etree.ElementTree as ET
```

## 데이터 모델 구조

### CaretPosition (커서 위치)
```python
@dataclass
class CaretPosition:
    list_id: int
    paragraph_id: int
    char_pos: int
```

### Document (문서 메타정보)
```python
@dataclass
class Document:
    sectionCount: int = 0
    pageStartNum: int = 0
    footnoteStartNum: int = 0
    endnoteStartNum: int = 0
    pictureStartNum: int = 0
    tableStartNum: int = 0
    equationStartNum: int = 0
    caretPos: CaretPosition = field(default_factory=lambda: CaretPosition(0, 0, 0))
    binaryDataCount: int = 0
    hangulFontDataCount: int = 0
    englishFontDataCount: int = 0
```

### FontData (글꼴 정보)
```python
@dataclass
class FontData:
    fontID: int = 0
    fontFace: str = ""
```

### CharShape (글자 모양)
```python
@dataclass
class CharShape:
    charShapeID: int = 0
    faceID: tuple = field(default_factory=lambda: (0,)*7)
    textColor: dict[str, int] = field(default_factory=lambda: {'r': 0, 'g': 0, 'b': 0})
```

### ParaShape (문단 모양)
```python
@dataclass
class ParaShape:
    paraShapeID: int = 0
    horizontalAlign: str = ''
```

## 데이터 추출 프로세스

### 1. ZIP 파일 읽기
```python
@classmethod
def read_hwpx_document(cls, file_path: str) -> bool:
    zipf = zipfile.ZipFile(file_path, 'r')
    # 이후 처리...
```

### 2. XML Namespace 추출
문서 버전에 따라 Namespace가 달라질 수 있으므로 추출 필요

```python
def extract_namespaces(xml_str):
    events = ('start-ns',)
    namespaces = {}
    for _, elem in ET.iterparse(xml_str, events):
        prefix, uri = elem
        namespaces[prefix] = uri
    return namespaces
```

### 3. Contents/header.xml 파일 분석

#### 파일 읽기
```python
@classmethod
def read_header(cls, zipf:zipfile) -> bool:
    # Contents/header.xml 파일 존재 확인
    if XML_FILENAME_HEADER not in zipf.namelist():
        return False
    
    # Namespace 추출
    ns = extract_namespaces(BytesIO(zipf.read(XML_FILENAME_HEADER)))
    if ns == None:
        return False
    
    # XML 파싱
    xml_header = zipf.open(XML_FILENAME_HEADER)
    header = ET.parse(xml_header).getroot()
```

#### header.xml 구조
- **head 요소**: 최상위 요소, secCnt 속성으로 구역 수 포함
- **beginNum**: 각종 객체의 시작 번호
- **refList**: 본문에서 사용될 데이터 맵핑 정보
- **forbiddenWordList**: 금칙 문자 목록
- **compatibleDocument**: 호환성 설정
- **trackchangeConfig**: 변경 추적 정보
- **docOption**: 연결 문서 및 저작권 정보
- **metaTag**: 메타태그 정보

### 4. beginNum 요소 추출

#### beginNum 속성 의미
- page: 페이지 시작 번호
- footnote: 각주 시작 번호
- endnote: 미주 시작 번호
- pic: 그림 시작 번호
- tbl: 표 시작 번호
- equation: 수식 시작 번호

#### 코드 예시
```python
# 구역 정보
cls.sectionCount = header.get('secCnt')

# 시작 번호 추출
begin_num = header.find('hh:beginNum', ns)
cls.pageStartNum = begin_num.get('page')
cls.footnoteStartNum = begin_num.get('footnote')
cls.endnoteStartNum = begin_num.get('endnote')
cls.pictureStartNum = begin_num.get('pic')
cls.tableStartNum = begin_num.get('tbl')
cls.equationStartNum = begin_num.get('equation')
```

### 5. refList 요소 분석

#### refList 하위 요소
- **fontfaces**: 글꼴 정보 목록
- **borderFills**: 테두리/배경/채우기 정보
- **charProperties**: 글자 모양 목록
- **tabProperties**: 탭 정의 목록
- **numberings**: 번호 문단 모양 목록
- **bullets**: 글머리표 문단 모양 목록
- **paraProperties**: 문단 모양 목록
- **styles**: 스타일 목록
- **memoProperties**: 메모 모양 목록
- **trackChanges**: 변경 추적 정보 목록
- **trackChangeAuthors**: 변경 추적 검토자 목록

### 6. 글꼴(fontfaces) 정보 추출

#### fontface 구조
```xml
<hh:fontface lang="HANGUL" fontCnt="2">
    <hh:font id="0" face="함초롬돋움" type="TTF" isEmbedded="0">
        <hh:typeInfo familyType="FCAT_GOTHIC" weight="6" proportion="4" 
                     contrast="0" strokeVariation="1" armStyle="1" 
                     letterform="1" midline="1" xHeight="1"/>
    </hh:font>
</hh:fontface>
```

#### fontface 속성
- lang: 언어 (HANGUL, LATIN, HANJA, JAPANESE, OTHER, SYMBOL, USER)
- fontCnt: 글꼴 개수

#### font 요소 속성
- id: 글꼴 ID
- face: 글꼴 이름
- type: 글꼴 타입 (TTF 등)
- isEmbedded: 임베딩 여부

### 7. 글자 모양(charProperties) 추출

#### charPr 요소 구조
run 요소의 charPrIDRef가 charPr의 id와 연결되어 글자 속성 정의

#### charPr 속성
- id: 글자 모양 ID
- textColor: 글자 색상 (RGB)

#### charPr 하위 요소
- fontRef: 언어별 글꼴 참조 ID

#### 코드 예시
```python
def _read_header(self) -> bool:
    # 글자 모양 정보 추출
    char_shape_list = ref_list.find('hh:charProperties', ns)
    for char_pr in char_shape_list.findall('hh:charPr', ns):
        char_shape = self._read_char_shape(char_pr, ns)
        if char_shape:
            doc.shapeManager.charshapeList.append(char_shape)

def _read_char_shape(self, char_pr:ET.Element, ns:dict) -> CharShape:
    char_shape = CharShape()
    
    # 속성 추출
    char_shape.charShapeID = int(char_pr.get('id'))
    char_shape.textColor = self.hex_to_rgb(char_pr.get('textColor'))
    
    # 하위 요소 추출
    char_shape.faceID = self.lang_data_to_int_tuple(char_pr.find('hh:fontRef', ns))
    
    return char_shape
```

### 8. 문단 모양(paraProperties) 추출

#### paraPr 요소 구조
p 요소의 paraPrIDRef가 paraPr의 id와 연결되어 문단 속성 정의

#### paraPr 속성
- id: 문단 모양 ID

#### paraPr 하위 요소
- align: 문단 정렬 (horizontal, vertical)

#### 코드 예시
```python
def _read_para_shape(self, para_pr:ET.Element, ns:dict) -> ParaShape:
    para_shape = ParaShape()
    
    para_shape.paraShapeID = int(para_pr.get('id'))
    
    align = para_pr.find('hh:align', ns)
    para_shape.horizontalAlign = align.get('horizontal')
    para_shape.verticalAlign = align.get('vertical')
    
    return para_shape
```

## 본문 데이터와 서식 연결

### section.xml 구조 예시
```xml
<hs:sec>
    <hp:p paraPrIDRef="20">
        <hp:run charPrIDRef="7">
            <hp:t>한글</hp:t>
        </hp:run>
        <hp:run charPrIDRef="0">
            <hp:t>과</hp:t>
        </hp:run>
        <hp:run charPrIDRef="8">
            <hp:t>컴퓨터</hp:t>
        </hp:run>
    </hp:p>
</hs:sec>
```

### 데이터 연결 흐름
1. **p 요소**: paraPrIDRef="20" → header.xml의 paraPr id="20"과 매칭
2. **run 요소**: charPrIDRef="7" → header.xml의 charPr id="7"과 매칭
3. **charPr**: fontRef hangul="0" → fontface의 font id="0"과 매칭

### 연결 예시
```
문단 (p)
├─ paraPrIDRef="20"
│  └─ header.xml: <hh:paraPr id="20">
│     └─ align horizontal="CENTER"
│
└─ run elements
   ├─ "한글" (charPrIDRef="7")
   │  └─ header.xml: <hh:charPr id="7" textColor="#6182D6">
   │     └─ fontRef hangul="2" → font id="2"
   │
   ├─ "과" (charPrIDRef="0")
   │  └─ header.xml: <hh:charPr id="0">
   │     └─ fontRef hangul="0" → font id="0" face="맑은 고딕"
   │
   └─ "컴퓨터" (charPrIDRef="8")
      └─ header.xml: <hh:charPr id="8">
```

## 주요 파일 구조

### HWPX 내부 파일 목록
- Contents/content.hpf: 패키징 정보
- Contents/header.xml: 문서 메타정보 및 서식 정보
- Contents/section.xml: 본문 내용
- metadata.xml: 문서 메타데이터
- settings.xml: 문서 설정

## 중요 참조사항

### XML Namespace
문서 버전에 따라 다를 수 있으므로 반드시 extract_namespaces로 추출하여 사용

### ID 참조 체계
- paraPrIDRef → paraPr id: 문단 모양 연결
- charPrIDRef → charPr id: 글자 모양 연결
- fontRef 언어별 ID → font id: 글꼴 연결

### 표준 문서 참조
- KS X 6101 표준 문서에서 상세 스키마 확인 가능
- e-나라표준인증에서 표준 문서 열람 가능

## 요약
HWPX 파싱의 핵심은:
1. ZIP 파일로 압축된 XML 파일들을 추출
2. header.xml에서 서식 정보 추출 (글꼴, 글자모양, 문단모양)
3. section.xml에서 본문 내용 추출
4. ID 참조를 통해 본문과 서식 연결
5. Python 객체로 구조화하여 활용

## Phase 1.5 추가 메모
- 머리말/꼬리말: `section0.xml`의 `hp:header`/`hp:footer` ctrl에서 `paraPrIDRef`/`charPrIDRef`가 header.xml 정의와 일치하는지 확인(현행 8/9가 기관 스타일과 다를 수 있음).
- 표 테두리: header.xml에 borderFill 7~18(헤더 배경 + DOUBLE_SLIM 조합)이 정의되어 있으므로, 셀의 `borderFillIDRef`를 파싱할 때 해당 ID 맵과 함께 비교하면 스타일 diff를 추적하기 쉽다.
