
다음은 요청하신 KS X 6101 표준 문서의 OCR 결과물을 수정한 내용입니다.
8.3 파일 형식 버전 식별
리딩 시스템이 OWPML 문서를 제대로 처리하기 위해서는 파일 형식 외에도 파일 형식에 대한 버전 식별이 필요하다. 가령 같은 OWPML 문서 파일 형식이라도 2.x의 구조와 3.x의 구조가 크게 다를 수 있고, 리딩 시스템이 2.x까지만을 지원한다고 하면 3.x의 문서 파일은 사용자를 위한 처리를 해야 한다. 이를 위해서는 파일 형식 버전 정보를 컨테이너의 특정 파일에 기록해야 한다.
OWPML 부합화된 OCF 컨테이너는 최상위 디렉터리의 직접 자식으로서 version.xml을 가지고 있어야 하며, 이 version.xml 파일 안에는 파일 형식에 대한 버전을 기록하고 있어야 한다. 다음은 version.xml에 대한 XML 스키마이다.
그림 2 — version.xml 파일의 XML 스키마
version.xml 스키마는 "http://www.owpml.org/owpml/2024/version" 네임스페이스를 사용한다.
파일 형식 버전은 아래와 같다:
major: 문서 형식의 구조가 완전히 바뀌는 것을 나타낸다. 값이 다르면 구버전과 호환이 불가능하다.
minor: 큰 구조는 동일하나, 큰 변화가 있는 것을 나타낸다. 값이 다르면 구버전과 호환이 불가능하다.
micro: 구조는 동일하나, 하위 요소가 추가되었거나, 하위 버전에서 호환되지 않는 정보가 추가된 것을 나타낸다. 숫자가 달라도 구버전과 호환이 가능하다.
buildNumber: 하위 요소에 정보 등이 추가된 것을 나타낸다. 숫자가 달라도 구버전과 호환이 가능하다.
version.xml 파일은 암호화 및 압축을 하지 않아야 한다.
code
Xml
<hv:HCFVersion xmlns:hv="http://www.owpml.org/owpml/2024/version" targetApplication="WORDPROCESSOR" major="5" minor="1" micro="0" buildNumber="1" xmlVersion="1.2" application="Hancom Office Hangul" appVersion="11.0.0.2129 WIN32LEWindows_r"/>
8.4 OPF OWPML 프로파일
8.4.1 OPF 도입
OWPML은 기본 OPF 스펙에서 몇 가지 요소를 추가해서 사용한다. OWPML 도입 내용은 다음과 같다.
8.4.2 OPF 적용 요소
<package> - <manifest> - <item>의 속성 추가 사항은 아래 그림 3과 같다.
OPF의 manifest 정보만으로는 OWPML에서 사용하기에 부족하다. 이에 따라 @isEmbedded 속성과 @sub-path 속성을 추가하였다. 두 속성은 OWPML 부합화된 OPF에서는 반드시 사용되어야 하는 필수 속성으로, @isEmbedded 속성은 선언된 리소스가 컨테이너 내에 포함되어 있는지를 나타내기 위한 속성이며, @sub-path 속성은 컨테이너 내에서 찾을 수 없는 리소스를 외부에서 찾기 위한 경로를 지정하는 속성이다.
8.4.3 Metadata profile
Metadata 요소는 하위 요소로 문서 내용에 대한 메타데이터를 가지고 있어야 한다. 메타데이터는 DublinCore 메타데이터 표준을 사용할 수 있다.
관련 URL: http://dublincore.org/
표 10 — metadata 형식
설명	바이너리 형식에서의 이름	새 파일 형식에서의 이름
제목	DocInfo의 HwpSummaryInformation	<dc:title>
주제	DocInfo의 HwpSummaryInformation	<dc:subject>
지은이	DocInfo의 HwpSummaryInformation	<dc:creator>
작성된 시각	DocInfo의 HwpSummaryInformation	<meta name="CreateDate">
수정된 시각		<meta name="ModifiedDate">
키워드	DocInfo의 HwpSummaryInformation	<meta name="Keywords">
기타 정보	DocInfo의 HwpSummaryInformation	<dc:description>
작성 회사 (출판사)		<dc:publisher>
언어		<dc:language>
예 4 — metadata의 예
code
Xml
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>예제 문서</dc:title>
    <dc:creator>오피스요소기술팀</dc:creator>
    <dc:publisher>한글과컴퓨터</dc:publisher>
    <dc:language xsi:type="dcterms:RFC3066">ko</dc:language>
    <dc:description>예시에 대한 요약 정보. 기존 comments에 해당.</dc:description>
    <meta content="text" name="CreatedDate">2010-12-14T14:01:00Z</meta>
    <meta content="text" name="ModifiedDate">2010-12-14T14:01:00Z</meta>
    <meta content="text" name="Keywords">키워드 예제</meta>
</metadata>
9. Header XML 스키마
9.1 네임스페이스
Header XML은 기본적으로 "http://www.owpml.org/owpml/2024/head"를 기본 네임스페이스로 사용한다. 기본 네임스페이스의 접두어(prefix)는 기본적으로 'hh'를 사용한다. 잘못된 사용을 줄이기 위해서 'hh'를 기본 네임스페이스("http://www.owpml.org/owpml/2024/head") 이외의 네임스페이스에 사용하지 않을 것을 권고한다.
9.2.1 헤더 구조
<head> 요소는 header.xml 파일에서 최상위 요소로서, 문서 내용에 관련된 모든 설정을 하위 요소로 가지고 있다. <head> 요소는 네 개의 하위 요소를 가질 수 있다. 각 하위 요소에 대한 설명은 다음에 오는 항들에서 자세하게 설명한다.
표 11 — head version
속성 이름	설명
version	OWPML Header XML의 버전. 이 문서 기준으로 현재 버전은 1.0이다.
표 12 — head 속성
하위 요소 이름	설명
beginNum	문서 내에서 각종 객체들의 시작 번호 정보를 가지고 있는 요소
refList	본문에서 사용될 각종 데이터에 대한 맵핑 정보를 가지고 있는 요소
forbiddenWordList	금칙 문자 목록을 가지고 있는 요소
compatibleDocument	문서 호환성 설정
trackchangeConfig	변경 추적 정보와 암호 정보를 가지고 있는 요소
docOption	연결 표시 정보와 저작권 관련 정보를 가지고 있는 요소
metaTag	메타태그 정보들을 가지고 있는 요소
9.2.2 beginNum 요소
<beginNum> 요소는 문서 내에서 사용되는 각종 객체들의 번호의 시작 숫자를 설정하기 위한 요소이다. 기본적으로 시작 번호는 1에서 시작되며, 사용자 설정에 의해서 1 이외의 번호에서 시작할 수 있게 된다. 시작 번호를 재정의할 수 있는 객체에는 '쪽 번호', '각주', '미주', '그림', '표', '수식' 등이 있다.
그림 6 — <beginNum>의 구조
표 13 — beginNum 속성
속성 이름	설명
page	페이지 시작 번호
footnote	각주 시작 번호
endnote	미주 시작 번호
pic	그림 시작 번호
tbl	표 시작 번호
equation	수식 시작 번호
예 5 — beginNum 예
code
Xml
<hh:beginNum page="1" footnote="1" endnote="1" pic="1" tbl="1" equation="1"/>```

#### 9.2.3 refList 요소

`<refList>` 요소는 본문에서 사용되는 각종 설정 데이터를 가지고 있는 요소이다. `<refList>` 요소는 header XML에서 대부분의 설정 정보를 가지고 있다. 하위 요소에 대한 자세한 설명은 9.3에서 서술한다.

**표 14 — refList 요소**

| 하위 요소 이름 | 설명 |
| :--- | :--- |
| fontfaces | 글꼴 정보 목록 |
| borderFills | 테두리/배경 목록 |
| charProperties | 글자 모양 목록 |
| tabProperties | 탭 설정 목록 |
| numberings | 번호 문단 모양 목록 |
| bullets | 글머리표 문단 모양 목록 |
| paraProperties | 문단 모양 목록 |
| styles | 스타일 목록 |
| memoProperties | 메모 모양 목록 |
| trackChanges | 변경 추적 정보 목록 |
| trackChangeAuthors | 변경 추적 검토자 목록 |

#### 9.2.4 forbiddenWordList 요소

`<forbiddenWordList>` 요소는 금칙 문자의 목록이다.

**그림 8 — `<forbiddenWordList>`의 구조**

**표 15 — forbiddenWordList 속성**

| 속성 이름 | 설명 |
| :--- | :--- |
| itemCnt | 금칙 문자의 개수 |

`<forbiddenWord>` 자식 요소는 요소 값으로 금칙 문자열을 가지는 단순 형식의 요소이다. 다음은 `<forbiddenWordList>` 요소의 예시이다.

**예 7 — forbiddenWordList 예**

```xml
<forbiddenWordList itemCnt="2">
    <forbiddenWord>d</forbiddenWord>
    <forbiddenWord>f</forbiddenWord>
</forbiddenWordList>
9.2.5 compatibleDocument 요소
<compatibleDocument> 요소는 이 문서가 다른 형태의 문서 형식으로 저장될 때 사용되는 정보들을 가지고 있다.
그림 9 — <compatibleDocument>의 구조
표 16 — compatibleDocument 속성
속성 이름	설명
targetProgram	대상 프로그램
예 8 — compatibleDocument 예
code
Xml
<hh:compatibleDocument targetProgram="HWP201X">
    <hh:layoutCompatibility/>
</hh:compatibleDocument>
9.2.5.2 layoutcompatibility 요소
<layoutCompatibility> 요소는 HWP 문서를 다른 형식의 문서로 변환시킬 때 필요한 설정 정보이다. 즉, HWP 문서를 OOXML 워드 문서로 변환할 때 HWP 문서에서는 지원되지만 OOXML 워드 문서에서는 지원되지 않는 설정 등을 어떤 방식으로 변환시킬 것인지에 대한 설정 값이다.
표 17 — layoutcompatibility 요소
하위 요소 이름	설명
applyFontWeightToBold	진하게 글자에 글꼴의 너비를 적용함.
useInnertJnderline	밑줄 위치를 글자 영역의 안쪽으로 그음.
fixedUndertneWidth	밑줄, 취소선 두께에 글자 크기를 반영하지 않음.
doNotApplyStrikeoutWithUnderline	밑줄과 함께 실선 취소선을 적용하지 않음.
useLowercaseStrikeout	취소선을 영문 소문자 기준으로 그음.
extendLineheightToOffset	글자 위치와 강조점에 의한 영역까지 줄 높이를 확장함.
applyFontspaceToLatin	라틴어 사이의 빈칸에 글꼴에 어울리는 빈칸을 적용함.
treatQuotationAsLatin	인용 부호를 글꼴에 어울리는 빈칸에서 라틴어로 취급함.
doNotApplyDiacSymMarkOfNoneAndSix	강조점의 [없음]과 6개 외의 항목을 적용하지 않음.
doNotAlignWhitespaceOnRight	줄의 가장 오른쪽 빈칸을 다음 줄로 넘기지 않음.
doNotAdjustWordInJustify	양쪽 정렬에서 단어의 문자 간 간격을 보정하지 않음.
baseCharUnitOnEAsian	글자 단위를 바탕글 스타일의 한글 크기를 기준으로 적용함.
baseCharUnitOnIndentOnFirstChar	들여쓰기/내어쓰기의 글자 단위를 문단 첫 글자의 크기를 기준으로 적용함.
adjustLineheightToFont	기본 줄 높이를 글꼴에 맞춰서 조정함.
adjustBaselinelnFixedLinespacing	줄 간격이 [고정값]에서 기준선을 세로 정렬에 따라 조정함.
applyPrevspacingBeneathObject	개체 아래 문단의 위 간격을 개체 기준으로 적용함.
applyNextspacingOfLastPara	마지막 문단의 아래 간격을 영역에 포함하여 확장함.
applyAtLeastToPercent100Pct	줄 간격의 [최소]를 [글자에 따라]에서 100%로 적용함.
doNotApplyAutoSpaceEAsianEng	한글과 영어 간격에 자동 조절을 적용하지 않음.
doNotApplyAutoSpaceEAsianNum	한글과 숫자 간격에 자동 조절을 적용하지 않음.
adjustParaBorderfillToSpacing	문단 테두리/배경 영역을 문단 여백과 위, 아래 간격을 제외하고 줄 간격에만 적용함.
connectParaBorderfillOfEqualBorder	문단 테두리가 같은 문단의 문단 테두리/배경을 연결함.
adjustParaBorderOffsetWithBorder	문단 테두리/배경의 간격을 테두리 설정 시에 적용함.
extendUneheightToParaBorderOffset	문단 테두리의 굵기와 간격의 영역까지 줄 높이를 확장함.
applyParaBorderToOutside	문단 테두리를 지정된 영역의 바깥쪽으로 적용함.
applyMinColumnWidthTo1mm	단 영역의 최소 폭을 1mm로 적용함.
applyTabPosBasedOnSegment	탭 위치를 개체에 의해 재배치된 영역을 기준으로 적용함.
breakTabOverline	줄 영역을 넘어선 탭을 다음 줄로 넘김.
adjustVertPosOfLine	줄 간격에 따라 줄의 위치를 조정함.
doNotApplyWhiteSpaceHeight	white space 문자의 글자 크기를 줄 높이에 반영하지 않음.
doNotAlignLastPeriod	줄의 마지막 마침표를 다음 줄로 넘기지 않음.
doNotAlignLastForbidden	줄의 마지막 금칙 문자를 다음 줄로 넘기지 않음.
baseLineSpacingOnLineGrid	줄 격자의 간격을 줄 간격의 기준으로 적용함.
applyCharSpacingToCharGrid	글자 격자의 간격을 글자에 따른 자간으로 적용함.
doNotApplyGridInHeaderFooter	머리말, 꼬리말에 줄/글자 격자를 적용하지 않음.
applyExtendHeaderFooterEachSection	본문 영역으로 확장되는 구역 단위 머리말, 꼬리말을 적용함.
doNotApplyLinegridAtNoLinespacing	줄 간격이 없으면 줄 격자의 간격을 적용하지 않음.
doNotApplyImageEffect	그림 효과를 적용하지 않음.
doNotApplyShapeComment	개체 설명문 적용하지 않음.
doNotAdjustEmptyAnchorLine	조판 부호만 있는 빈 줄에 개체 배치를 조정하지 않음.
overlapBothAllowOverlap	개체 두 개가 서로 겹침 허용인 경우에만 서로 겹침.
doNotApplyVertOffsetOfForward	조판 부호 다음 쪽으로 넘겨진 개체에 세로 위치를 적용하지 않음.
extendVertLimitToPageMargins	문단 기준 개체의 세로 위치를 종이 영역까지 확장함.
doNotHoldAnchorOfTable	문단 기준 표의 조판 부호는 쪽 넘김을 방지하지 않음.
doNotFormattingAtBeneathAnchor	문단과 조판 부호 다음 쪽으로 넘겨진 개체 사이 영역에 문단을 배치하지 않음.
adjustBaselineOfObjectToBottom	글자처럼 취급한 개체의 기준선을 개체 아래쪽으로 조정함.
doNotApplyExtensionCharPr	글자 겹치기의 확장 기능을 적용하지 않음.
9.2.6 trackChangeConfig 요소
<trackChangeConfig>는 변경 추적에 대한 상태 정보와 암호 정보를 가지고 있다.
표 18 — trackChangeConfig 요소
속성 이름	설명
flags	변경 추적 상태 정보
표 19 — flag 값
flag 값	설명
0x00000001	변경 추적 상태
0x00000002	변경 추적 원본
0x00000004	변경 내용 안보기
0x00000008	변경 추적 문장 부호 표시
0x00000010	변경 추적 서식 표시
0x00000020	변경 추적 삽입/삭제 표시
<config-item-set> 요소는 변경 추적 암호 정보를 갖고 있는 요소이다.
예 9 — config-item-set
code
Xml
<config:config-item-set name="TrackChangePasswordInfo">
    <config:config-item name="algorithm-name" type="string">PBKDF2</config:config-item>
    <config:config-item name="salt" type="base64Binary">nsJ</config:config-item>
    <config:config-item name="iteration-count" type="int">1024</config:config-item>
</config:config-item-set>
9.2.7 docOption 요소
<docOption>은 연결 문서 정보와 저작권 관련 정보를 가지고 있는 요소이다.
표 20 — docOption 요소
하위 요소 이름	설명
linkinfo	연결 문서 정보
licensemark	저작권 관련 정보
<linkinfo>는 연결 문서 정보를 가지고 있는 요소이다.
표 21 — linkinfo 요소
속성 이름	설명
path	연결된 문서의 경로
pageInherit	연결 인쇄 시 쪽 번호 잇기 여부
footnoteInherit	연결 인쇄 시 각주 번호 잇기 여부
<licensemark>는 저작권 관련 정보를 가지고 있는 요소이다.
표 22 — licensemark 요소
속성 이름	설명
flag	저작권 제한 정보
lang	국가 코드
표 23 — flag 값
flag 값	설명
0x00000001	상업적 이용 제한
0x00000002	변경 제한
0x00000004	동일 조건하에 복제 허가
9.2.8 metaTag 요소
<metaTag>은 메타 태그에 대한 정보를 가지고 있는 요소이다. jsonobject 형식으로 표현된다.
예 10 — metaTag 예
code
Xml
<!--fieldBegin 요소의 metaTag-->
<hp:fieldBegin id="1795169102" type="CLICK_HERE" name="" editable="true" dirty="true" zorder="-1" fieldid="-62727281">
    <hp:parameters entry="3" name="">
        <hp:integerParam name="Prop">9</hp:integerParam>
        <hp:stringParam name="Command" xml:space="preserve">clickhere:set:66:Direction:wstring:23:이곳을 마우스로 누르고 내용을 입력하세요. HelpState:wstring:0: </hp:stringParam>
        <hp:stringParam name="_Direction_">이곳을 마우스로 누르고 내용을 입력하세요.</hp:stringParam>
    </hp:parameters>
    <hp:metaTag>{"name":"#이름"}</hp:metaTag>
</hp:fieldBegin>

<!--tbl 요소의 metaTag-->
<hp:tbl id="1793424928" zOrder="0" numberingTypes="TABLE" textWrap="TOP_AND_BOTTOM" textFlow="BOTH_SIDES" lock="false" dropcapstyle="None" pageBreak="CELL" repeatHeader="true" rowCnt="2" colCnt="1" cellSpacing="0" borderFillIDRef="3" noAdjust="false">
    <hp:tc name="" header="false" hasMargin="false" protect="false" editable="false" dirty="false" borderFillIDRef="3">
        <hp:subList id="" textDirection="HORIZONTAL" lineWrap="BREAK" vertAlign="CENTER" linkListIDRef="0" linkListNextIDRef="0" textWidth="0" textHeight="0" hasTextRef="false" hasNumRef="false" metatag="{&quot;name&quot;:&quot;#이름&quot;}">
        </hp:subList>
    </hp:tc>
</hp:tbl>
9.3 문서 설정 정보
9.3.1 문서 설정
문서 설정 정보는 문서 내에서 사용되는 각종 글꼴 정보, 글자 모양 정보, 테두리/배경 정보와 같이 문서의 레이아웃 설정 및 모양 설정을 가지고 있다.
9.3.2 fontfaces 요소
문서 내에서 글꼴 정보는 반드시 1개 이상 정의되어 있어야 한다. 내용이 없는 문서라도 기본 글꼴 정보는 정의되어 있어야 한다. 속성 @itemCnt의 값은 1 이상(positiveInteger)으로 제한되어 있으며, 자식 요소인 <fontface> 요소의 개수 한정자 역시 1 이상으로 정의되어 있다.
표 24 — fontfaces 요소
속성 이름	설명
itemCnt	글꼴 정보의 개수
예 11 — fontfaces 예
code
Xml
<hh:fontfaces itemCnt="1">
    <hh:fontface lang="HANGUL" fontCnt="1">
        <hh:font id="0" face="바탕" type="TTF" isEmbedded="false">
            <hh:typeinfo familyType="FCAT_GOTHIC" weight="6" proportion="4" contrast="0" strokeVariation="1" armStyle="1" letterform="1" midline="1" xHeight="1"/>
        </hh:font>
    </hh:fontface>
</hh:fontfaces>
글꼴 정보는 언어별로 정의된다. 현재 이 문서에서 지원되고 있는 언어 형식으로는 [한글, 라틴, 한자, 일어, 기타, 심볼, 사용자]가 있다. [한글, 라틴, 한자, 일어, 심볼] 언어 형식의 구분은 Unicode 4.0을 참고한다. [기타] 언어 형식의 구분은 RTL(Right to Left) 표기방식의 언어이며 [사용자] 언어 형식의 구분은 PUA(Private Unicode Area) 영역을 말한다.
표 25 — fontface 요소
속성 이름	설명
lang	글꼴이 적용될 언어 유형
fontCnt	글꼴의 개수
HWP 문서 스키마는 내장 글꼴을 지원한다. 글꼴이 내장된 경우, 글꼴 데이터 파일은 다른 바이너리 파일과 마찬가지로 컨테이너 내에 바이너리 형태로 포함이 되고 manifest에 해당 정보를 기록한다. <font> 엘리먼트에서는 manifest에 정의된 정보를 참조해서 내장된 글꼴에 접근하게 된다.
표 26 — font 요소
속성 이름	설명
id	글꼴을 식별하기 위한 아이디
face	글꼴의 이름
type	글꼴의 유형
isEmbedded	글꼴 파일이 문서 컨테이너 내에 포함되었는지 여부
binaryItemIDRef	글꼴 파일이 문서 컨테이너 내에 포함된 경우 해당 글꼴 파일을 지정하기 위한 ID 참조 값
표 27 — font 하위 요소
하위 요소 이름	설명
substFont	대체 글꼴
typeinfo	글꼴 유형 정보
substFont 요소
애플리케이션에서는 <font> 요소에서 정의된 글꼴이 없는 경우 가장 먼저 <substFont> 요소에 정의된 글꼴을 사용해야 한다. 대체 글꼴마저 없는 경우 시스템 기본 글꼴을 사용하는 것을 권고한다.
표 28 — substFont 요소
속성 이름	설명
face	대체 글꼴의 이름
type	글꼴의 유형
isEmbedded	글꼴 파일이 문서 컨테이너 내에 포함되었는지 여부
binaryItemIDRef	글꼴 파일이 문서 컨테이너 내에 포함된 경우 해당 글꼴 파일을 지정하기 위한 ID 참조 값
typeinfo 요소
글꼴의 유형 설정을 표현하기 위한 요소이다.
표 29 — typeinfo 속성
속성 이름	설명
familyType	글꼴 계열
serifStyle	세리프 유형
weight	굵기
proportion	비례
contrast	대조
strokeVariation	스트로크 편차
armStyle	자획 유형
letterform	글자형
midline	중간선
xHeight	x-높이
9.3.3 borderFills 요소
한 문서 내에서는 다양한 테두리/배경 정보들이 사용되는데 이런 테두리/배경 정보를 목록 형태로 가지고 있는 요소이다.
표 30 — borderFills 요소
속성 이름	설명
itemCnt	테두리/배경/채우기 정보의 개수
표 32 — borderFill 요소
속성 이름	설명
id	테두리/배경/채우기 정보를 구별하기 위한 아이디
threeD	3D 효과의 사용 여부
shadow	그림자 효과의 사용 여부
centerline	중심선 종류
breakCellSeparateLine	자동으로 나뉜 표의 경계선 생성 여부
표 33 — borderFill 하위 요소
하위 요소 이름	설명
slash	slash 대각선 모양 설정 (9.3.3.2.2 참조)
backSlash	backSlash 대각선 모양 설정 (9.3.3.2.2 참조)
leftBorder	왼쪽 테두리 (9.3.3.2.3 참조)
rightBorder	오른쪽 테두리 (9.3.3.2.3 참조)
topBorder	위쪽 테두리 (9.3.3.2.3 참조)
bottomBorder	아래쪽 테두리 (9.3.3.2.3 참조)
diagonal	대각선 (9.3.3.2.3 참조)
fillBrush	채우기 정보
테두리/배경 설정 중, 대각선의 정보를 담기 위한 요소이다.
표 34 — SlashType 요소
속성 이름	설명
type	Slash/BackSlash의 모양 (NONE, CENTER, CENTER_BELOW, CENTER_ABOVE, ALL)
Crooked	꺾인 대각선 여부
isCounter	slash/backSlash 대각선의 역방향 여부
<leftBorder>, <rightBorder>, <topBorder>, <bottomBorder>, <diagonal>은 모두 같은 형식을 가진다.
표 35 — BorderType 요소
속성 이름	설명
type	테두리선의 종류
width	테두리선의 굵기 (단위: mm)
color	테두리선의 색상
winBrush 요소
면 채우기 정보를 표현하기 위한 요소이다. 면 채우기 정보에는 면 색, 무늬 색, 무늬 종류, 투명도 등이 있다.
표 37 — winBrush 요소
속성 이름	설명
faceColor	면 색
hatchColor	무늬 색
hatchStyle	무늬 종류
alpha	투명도
gradation 요소
한 색상에서 다른 색상으로 점진적 또는 단계적으로 변화하는 기법을 표현하기 위한 요소이다.
표 38 — gradation 요소
속성 이름	설명
type	그러데이션 유형
angle	그러데이션 각도
centerX	가로 중심 (X 좌표)
centerY	세로 중심 (Y 좌표)
step	변경 정도
colorNum	색 수
stepCenter	변경 정도의 중심
alpha	투명도
imgBrush 요소
그림으로 채우기 정보를 표현하기 위한 요소이다.
표 43 — img 요소
속성 이름	설명
bright	그림의 밝기
contrast	그림의 명암
effect	그림의 추가 효과 (REAL_PIC, GRAY_SCALE, BLACK_WHITE)
binaryItemIDRef	BinDataItem 요소의 아이디 참조값
alpha	투명도
9.3.4 charProperties 요소
콘텐츠 내에서 글자 모양 정보는 반드시 한 개 이상 정의되어 있어야 한다.
표 44 — charProperties 요소
속성 이름	설명
itemCnt	글자 모양 정보의 개수
글자 모양 설정 정보를 표현하기 위한 요소이다.
표 46 — charPr 요소
속성 이름	설명
id	글자 모양 정보를 구별하기 위한 아이디
height	글자 크기 (단위: HWPUNIT)
textColor	글자 색
shadeColor	음영 색
useFontSpace	글꼴에 어울리는 빈칸 사용 여부
useKerning	커닝 사용 여부
symMark	강조점 종류
borderFillIDRef	글자 테두리 기능에 대한 아이디 참조
표 47 — charPr 하위 요소
하위 요소 이름	설명
fontRef	언어별 글꼴 참조
ratio	언어별 장평 (%)
spacing	언어별 자간 (%)
relSz	언어별 상대 크기 (%)
offset	언어별 오프셋 (%)
italic	기울임
bold	진하게
underline	밑줄
strikeout	취소선
outline	외곽선
shadow	그림자
emboss	양각
engrave	음각
supscript	위첨자
subscript	아래첨자
표 48 — symMark 유니코드 값
속성 값	유니코드 값	속성 값	유니코드 값
NONE	없음	GRAVE ACCENT	0x0300
DOT ABOVE	0x0307	ACUTE ACCENT	0x0301
RING ABOVE	0x030A	CIRCUMFLEX	0x0302
TILDE	0x030C	MACRON	0x0304
CARON	0x0303	HOOK ABOVE	0x0309
SIDE	0x302E	DOT BELOW	0x0323
COLON	0x302F		
각 언어별 글자에서 참조하는 글꼴에 대한 정보를 가지고 있는 요소이다.
표 49 — fontRef 요소
속성 이름	설명
hangul	한글 글자에서 사용될 글꼴의 아이디 참조값
latin	라틴 글자에서 사용될 글꼴의 아이디 참조값
hanja	한자 글자에서 사용될 글꼴의 아이디 참조값
japanese	일본어 글자에서 사용될 글꼴의 아이디 참조값
other	기타 글자에서 사용될 글꼴의 아이디 참조값
symbol	심볼 글자에서 사용될 글꼴의 아이디 참조값
user	사용자 글자에서 사용될 글꼴의 아이디 참조값
글자 속성 중 밑줄을 표현하기 위한 요소이다.
표 54 — underline 요소
속성 이름	설명
type	밑줄의 종류 (BOTTOM, CENTER, TOP)
shape	밑줄의 모양
color	밑줄의 색
글자 속성 중 취소선을 표현하기 위한 요소이다.
표 55 — strikeout 요소
속성 이름	설명
shape	취소선의 모양
color	취소선의 색
글자 속성 중 외곽선을 표현하기 위한 요소이다.
표 56 — outline 요소
속성 이름	설명
type	외곽선의 종류
글자 속성 중 그림자를 표현하기 위한 요소이다.
표 57 — shadow 요소
속성 이름	설명
type	그림자의 종류 (NONE, DROP, CONTINUOUS)
color	그림자의 색
offsetX	그림자 간격 X (%)
offsetY	그림자 간격 Y (%)
9.3.5 tabProperties 요소
탭 정보 목록을 가지고 있는 요소이다.
표 58 — tabProperties 요소
속성 이름	설명
itemCnt	탭 정보의 개수
표 60 — tabPr 요소
속성 이름	설명
id	탭 정보를 구별하기 위한 아이디
autoTabLeft	문단 왼쪽 끝 자동 탭 여부 (내어쓰기용)
autoTabRight	문단 오른쪽 끝 자동 탭 여부
탭의 모양 및 위치 정보 등을 표현하기 위한 요소이다.
9.3.6 numberings 요소
문단 번호 모양 정보 목록을 가지고 있는 요소이다.
표 63 — numberings 요소
속성 이름	설명
itemCnt	문단 번호 모양 정보의 개수
각 번호/글머리표 문단 머리의 정보이다.
표 67 — paraHead 요소
속성 이름	설명
start	사용자 지정 문단 시작번호
level	번호/글머리표의 수준
align	문단의 정렬 종류 (LEFT, RIGHT, CENTER)
useInstWidth	번호 너비를 실제 인스턴스 문자열의 너비에 맞출지 여부
autoIndent	자동 내어쓰기 여부
widthAdjust	번호 너비 보정 값 (단위: HWPUNIT)
textOffsetType	수준별 본문과의 거리 단위 종류 (PERCENT, HWPUNIT)
textOffset	수준별 본문과의 거리
numFormat	번호 형식
charPrIDRef	글자 모양 아이디 참조값
checkable	확인용 글머리표 여부
9.3.7 bullets 요소
글머리표 문단 모양 정보 목록을 가지고 있는 요소이다.
표 68 — bullets 요소
속성 이름	설명
bulletCount	글머리표 문단 모양 정보의 개수
글머리표 문단 모양 정보를 사용하면 문단의 머리에 번호 대신 글머리표 또는 그림 글머리표를 삽입할 수 있다.
표 70 — bullet 요소
속성 이름	설명
id	글머리표 문단 모양을 구별하기 위한 아이디
char	글머리표 문자
checkedChar	선택 글머리표 문자
useImg	글머리표 문자 대신 글머리표 그림을 사용할지 여부
9.3.8 paraProperties 요소
문단 모양 정보 목록을 가지고 있는 요소입니다.
하위 요소 이름	설명
paraPr	문단 모양 정보
예 34 — paraProperties 예
code
Xml
<hh:paraProperties itemCnt="2">
    <hh:paraPr id="0" tabPrIDRef="0" condense="0" fontLineHeight="false" snapToGrid="true" suppressLineNumbers="false" checked="false" textDir="LTR">
        <hh:align horizontal="JUSTIFY" vertical="BASELINE"/>
        <hh:heading type="NONE" idRef="0" level="0"/>
        <hh:breakSetting breakLatinWord="KEEP_WORD" breakNonLatinWord="KEEP_WORD" widowOrphan="true" keepWithNext="false" keepLines="false" pageBreakBefore="false" lineWrap="BREAK"/>
        <hh:autoSpacing eAsianEng="false" eAsianNum="false"/>
        <hh:margin>
            <hh:intent value="0" unit="HWPUNIT"/>
            <hh:left value="0" unit="HWPUNIT"/>
            <hh:right value="0" unit="HWPUNIT"/>
            <hh:prev value="0" unit="HWPUNIT"/>
            <hh:next value="0" unit="HWPUNIT"/>
        </hh:margin>
        <hh:lineSpacing type="PERCENT" value="160" unit="HWPUNIT"/>
        <hh:border borderFillIDRef="2" offsetLeft="0" offsetRight="0" offsetTop="0" offsetBottom="0" connect="true" ignoreMargin="false"/>
    </hh:paraPr>
</hh:paraProperties>```

---