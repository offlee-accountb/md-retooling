9.3.8.2 paraPr 요소
9.3.8.2.1 paraPr 일반 항목
문단 모양 정보는 문단 내 정렬, 문단 테두리 등 문단을 표현할 때 필요한 각종 설정 정보를 가지고 있는 요소이다.
fontLineHeight: 글자에 어울리는 줄 높이 사용 여부
snapToGrid: 편집 용지의 줄 격자 사용 여부
suppressLineNumbers: 줄 번호 건너뜀 사용 여부
checked: 선택 글머리표 여부
textDir: 문단 방향 정보 (RTL: 오른쪽에서 왼쪽, LTR: 왼쪽에서 오른쪽)
표 75 — paraPr 하위 요소
하위 요소 이름	설명
align	문단 내 정렬 설정
heading	문단 머리 번호/글머리표 설정
breakSetting	문단 줄 나눔 설정
margin	문단 여백 설정
lineSpacing	줄 간격 설정
border	문단 테두리 설정
autoSpacing	문단 자동 간격 조절 설정
9.3.8.2.2 align 요소
문단 내 정렬 방식을 표현하기 위한 요소이다.
그림 51 — <align>의 구조
샘플 35 — align 예
<hh:align horizontal="JUSTIFY" vertical="BASELINE"/>
9.3.8.2.3 heading 요소
문단 머리 모양 설정 정보를 가지고 있는 요소이다.
그림 52 — <heading>의 구조
표 77 — heading 요소
속성 이름	설명
type	문단 머리 모양 종류 (NONE: 없음, OUTLINE: 개요, NUMBER: 번호, BULLET: 글머리표)
idRef	문단 머리 번호/글머리표 모양 아이디 참조값
level	문단 단계
샘플 36 — heading 예
<hh:heading type="NUMBER" idRef="2" level="1"/>
9.3.8.2.4 breakSetting 요소
문단의 줄 나눔 설정 정보를 가지고 있는 요소이다.
그림 53 — <breakSetting>의 구조
표 78 — breakSetting 요소
속성 이름	설명
breakLatinWord	라틴 문자의 나눔 단위
breakNonLatinWord	라틴 문자 이외의 문자의 줄 나눔 단위
widowOrphan	외톨이줄 보호 여부
keepWithNext	다음 문단과 함께 여부
keepLines	문단 보호 여부
pageBreakBefore	문단 앞에서 항상 쪽 나눔 여부
lineWrap	한 줄로 입력 사용 시의 형식
샘플 37 - breakSetting 예
<hh:breakSetting breakLatinWord="KEEP_WORD" breakNonLatinWord="KEEP_WORD" widowOrphan="0" keepWithNext="0" keepLines="0" pageBreakBefore="0" lineWrap="BREAK"/>
9.3.8.2.5 margin 요소
문단의 여백 정보를 가지고 있는 요소이다.
그림 54 — <margin>의 구조
표 79 — margin 요소
속성 이름	설명
indent	들여쓰기/내어쓰기 값. 단위는 HWPUNIT.
left	왼쪽 여백. 단위는 HWPUNIT.
right	오른쪽 여백. 단위는 HWPUNIT.
prev	문단 위 간격. 단위는 HWPUNIT.
next	문단 아래 간격. 단위는 HWPUNIT.
샘플 38 - margin 예
<hh:margin indent="0" left="0" right="0" prev="0" next="0"/>
9.3.8.2.6 lineSpacing 요소
문단의 줄 간격 정보를 가지고 있는 요소이다.
그림 55 - <lineSpacing>의 구조
표 80 — lineSpacing 요소
속성 이름	설명
type	줄 간격 종류
value	줄 간격 값. type이 PERCENT이면 0% ~ 500% 사이의 값.
unit	줄 간격 값의 단위.
샘플 39 — lineSpacing 예
<hh:lineSpacing type="PERCENT" value="160" unit="HWPUNIT"/>
9.3.8.2.7 border 요소
문단의 테두리 설정 정보를 가지고 있는 요소이다.
그림 56 — <border>의 구조
표 81 — border 요소
속성 이름	설명
borderFillIDRef	테두리/배경 모양 아이디 참조값
offsetLeft	문단 테두리 왼쪽 간격. 단위는 HWPUNIT.
offsetRight	문단 테두리 오른쪽 간격. 단위는 HWPUNIT.
offsetTop	문단 테두리 위쪽 간격. 단위는 HWPUNIT.
offsetBottom	문단 테두리 아래쪽 간격. 단위는 HWPUNIT.
connect	문단 테두리 연결 여부
ignoreMargin	문단 테두리 여백 무시 여부
샘플 40 — border 예
<hh:border borderFillIDRef="1" offsetLeft="0" offsetRight="0" offsetTop="0" offsetBottom="0" connect="0" ignoreMargin="0"/>
9.3.8.2.8 autoSpacing 요소
문단 내에서 한글, 영어, 숫자 사이의 간격에 대한 자동 조절 설정 정보를 가지고 있는 요소이다.
그림 57 — <autoSpacing>의 구조
표 82 — autoSpacing 요소
속성 이름	설명
eAsianEng	한글과 영어 간격을 자동 조절 여부
eAsianNum	한글과 숫자 간격을 자동 조절 여부
샘플 41 — autoSpacing 예
<hh:autoSpacing eAsianEng="0" eAsianNum="0"/>
9.3.9 styles 요소
9.3.9.1 styles
스타일 정보 목록을 가지고 있는 요소이다.
그림 58 — <styles>의 구조
표 83 — styles 요소
속성 이름	설명
itemCnt	스타일 정보의 개수
표 84 — styles 하위 요소
하위 요소 이름	설명
style	스타일 정보
샘플 42 — styles 예
code
Xml
<hh:styles itemCnt="21">
    <hh:style id="0" type="PARA" name="바탕글" engName="Normal" paraPrIDRef="0" charPrIDRef="0" nextStyleIDRef="0" langID="1042" lockForm="0"/>
    <hh:style id="1" type="PARA" name="본문" engName="Body" paraPrIDRef="1" charPrIDRef="0" nextStyleIDRef="1" langID="1042" lockForm="0"/>
    <hh:style id="2" type="PARA" name="개요 1" engName="Outline 1" paraPrIDRef="2" charPrIDRef="0" nextStyleIDRef="2" langID="1042" lockForm="0"/>
    <hh:style id="3" type="PARA" name="개요 2" engName="Outline 2" paraPrIDRef="3" charPrIDRef="1" nextStyleIDRef="3" langID="1042" lockForm="0"/>
    <hh:style id="4" type="PARA" name="개요 3" engName="Outline 3" paraPrIDRef="4" charPrIDRef="0" nextStyleIDRef="4" langID="1042" lockForm="0"/>
    <hh:style id="5" type="PARA" name="개요 4" engName="Outline 4" paraPrIDRef="5" charPrIDRef="0" nextStyleIDRef="5" langID="1042" lockForm="0"/>
    <hh:style id="6" type="PARA" name="개요 5" engName="Outline 5" paraPrIDRef="6" charPrIDRef="0" nextStyleIDRef="6" langID="1042" lockForm="0"/>
    <hh:style id="7" type="PARA" name="개요 6" engName="Outline 6" paraPrIDRef="7" charPrIDRef="0" nextStyleIDRef="7" langID="1042" lockForm="0"/>
    <hh:style id="8" type="PARA" name="개요 7" engName="Outline 7" paraPrIDRef="8" charPrIDRef="0" nextStyleIDRef="8" langID="1042" lockForm="0"/>
    <hh:style id="9" type="PARA" name="개요 8" engName="Outline 8" paraPrIDRef="9" charPrIDRef="0" nextStyleIDRef="9" langID="1042" lockForm="0"/>
    <hh:style id="10" type="PARA" name="개요 9" engName="Outline 9" paraPrIDRef="10" charPrIDRef="0" nextStyleIDRef="10" langID="1042" lockForm="0"/>
    <hh:style id="11" type="PARA" name="개요 10" engName="Outline 10" paraPrIDRef="11" charPrIDRef="0" nextStyleIDRef="11" langID="1042" lockForm="0"/>
    <hh:style id="12" type="CHAR" name="쪽 번호" engName="Page Number" paraPrIDRef="0" charPrIDRef="0" nextStyleIDRef="0" langID="1042" lockForm="0"/>
    <hh:style id="13" type="PARA" name="머리말" engName="Header" paraPrIDRef="9" charPrIDRef="1" nextStyleIDRef="13" langID="1042" lockForm="0"/>
    <hh:style id="14" type="PARA" name="각주" engName="Footnote" paraPrIDRef="10" charPrIDRef="1" nextStyleIDRef="14" langID="1042" lockForm="0"/>
    <hh:style id="15" type="PARA" name="미주" engName="Endnote" paraPrIDRef="10" charPrIDRef="2" nextStyleIDRef="15" langID="1042" lockForm="0"/>
    <hh:style id="16" type="PARA" name="메모" engName="Memo" paraPrIDRef="11" charPrIDRef="3" nextStyleIDRef="16" langID="1042" lockForm="0"/>
    <hh:style id="17" type="PARA" name="차례 제목" engName="TOC Heading" paraPrIDRef="12" charPrIDRef="4" nextStyleIDRef="17" langID="1042" lockForm="0"/>
    <hh:style id="18" type="PARA" name="차례 1" engName="TOC 1" paraPrIDRef="13" charPrIDRef="5" nextStyleIDRef="18" langID="1042" lockForm="0"/>
    <hh:style id="19" type="PARA" name="차례 2" engName="TOC 2" paraPrIDRef="14" charPrIDRef="5" nextStyleIDRef="19" langID="1042" lockForm="0"/>
    <hh:style id="20" type="PARA" name="차례 3" engName="TOC 3" paraPrIDRef="15" charPrIDRef="5" nextStyleIDRef="20" langID="1042" lockForm="0"/>
</hh:styles>
9.3.9.2 style 요소
스타일은 자주 사용하는 글자 모양이나 문단 모양을 미리 정해 놓고서 이를 사용할 수 있게 해주는 기능이다. <style> 요소는 설정된 스타일 기능을 표현하기 위한 요소이다.
그림 59 — <style>의 구조
표 85 — style 요소
속성 이름	설명
id	스타일 정보를 구별하기 위한 아이디
type	스타일 종류 (PARA: 문단 스타일, CHAR: 글자 스타일)
name	스타일의 로컬 이름. 한글 윈도에서는 한글 스타일 이름.
engName	스타일의 영문 이름
paraPrIDRef	문단 모양 아이디 참조값. 스타일의 종류가 문단인 경우 반드시 지정해야 함.
charPrIDRef	글자 모양 아이디 참조값. 스타일의 종류가 글자인 경우 반드시 지정해야 함.
nextStyleIDRef	다음 스타일 아이디 참조값. 문단 스타일에서 사용자가 리턴 키를 입력하여 다음 문단으로 이동하였을 때 적용될 문단 스타일을 지정함.
langID	언어 아이디 (http://www.w3.org/WAI/ER/IG/ert/iso639.htm 참조)
lockForm	양식 모드에서 style 보호하기 여부
9.3.10 memoProperties 요소
9.3.10.1 memoProperties
메모 모양에 대한 목록을 가지고 있는 요소이다.
그림 60 — <memoProperties>의 구조
표 86 — memoProperties 요소
속성 이름	설명
itemCnt	메모 모양 정보의 개수
표 87 — memoProperties 하위 요소
하위 요소 이름	설명
memoPr	메모 모양 정보
샘플 43 — memoProperties 예
code
Xml
<hh:memoProperties itemCnt="1">
    <hh:memoPr id="1" width="15590" lineWidth="1" lineType="SOLID" lineColor="#B6D7AE" fillColor="#F0FFE9" activeColor="#CFF1C1" memoType="NORMAL"/>
</hh:memoProperties>
9.3.10.2 memoPr 요소
메모는 문서 작성 또는 수정 중 간략한 내용을 기록해 둘 수 있는 기능이다. <memoPr> 요소는 실제 메모 내용을 담고 있는 것이 아니라, 화면에 표시될 메모의 모양 정보를 가지고 있는 요소이다. 즉, 메모 선의 색, 메모의 색 등 화면 표시를 위한 설정값을 담고 있다.
그림 61 — <memoPr>의 구조
표 88 — memoPr 요소
속성 이름	설명
id	메모 모양 정보를 구별하기 위한 아이디
width	메모가 보이는 넓이
lineType	메모의 선 종류
lineColor	메모의 선 색
fillColor	메모의 색
activeColor	메모가 활성화되었을 때의 색
memoType	메모 변경 추적을 위한 속성
lineWidth	메모의 라인 두께
9.3.11 trackChanges 요소
9.3.11.1 trackChanges
변경 추적 정보 목록을 가지고 있는 요소이다.
표 89 — trackChanges 요소
속성 이름	설명
itemCnt	변경 추적의 개수
표 90 — trackChanges 하위 요소
하위 요소 이름	설명
trackChange	변경 추적 정보
샘플 44 — trackChanges 예
code
Xml
<hh:trackChanges itemCnt="5">
    <hh:trackChange type="Insert" date="2021-10-15T01:08:00Z" authorID="1" hide="0" id="1"/>
    <hh:trackChange type="Insert" date="2021-10-15T01:47:00Z" authorID="1" hide="0" id="2"/>
    <hh:trackChange type="ParaShape" date="2021-10-15T01:47:00Z" authorID="1" hide="0" id="3" paraShapeID="17"/>
    <hh:trackChange type="Delete" date="2021-10-15T01:51:00Z" authorID="1" hide="0" id="4"/>
    <hh:trackChange type="ParaShape" date="2021-10-15T01:51:00Z" authorID="1" hide="0" id="5" paraShapeID="20"/>
</hh:trackChanges>
9.3.11.2 trackChange 요소
변경 추적 정보를 가지고 있는 요소이다.
그림 63 — <trackChange>의 구조
표 91 — trackChange 요소
속성 이름	설명
type	변경 추적의 종류 (UnKnown: 없음, Insert: 삽입, Delete: 삭제, CharShape: 글자 서식 변경, ParaShape: 문단 서식 변경)
date	변경 추적 시간 (%04d-%02d-%02dT%02d:%02d:%02dZ: 년,월,일,시,분,초)
authorID	변경 추적 검토자를 구별하기 위한 아이디
charShapeID	변경 추적 글자의 서식 정보
paraShapeID	변경 추적 문단의 서식 정보
hide	변경 추적 화면 표시 여부
id	변경 추적 적용 문서 구별 아이디
9.3.12 trackChangeAuthors 요소
9.3.12.1 trackChangeAuthors 일반 항목
변경 추적 검토자 목록을 가지고 있는 요소이다.
그림 64 — <trackChangeAuthors>의 구조
표 92 — trackChangeAuthors 요소
속성 이름	설명
itemCnt	변경 추적 검토자 수
표 93 — trackChangeAuthors 하위 요소
하위 요소 이름	설명
trackChangeAuthor	변경 추적 검토자
샘플 45 — trackChangeAuthors 예
code
Xml
<hh:trackChangeAuthors itemCnt="1">
    <hh:trackChangeAuthor name="hancom" mark="1" id="1"/>
</hh:trackChangeAuthors>
9.3.12.2 trackChangeAuthor 요소
변경 추적 검토자 정보를 가지고 있는 요소이다.
그림 65 — <trackChangeAuthor>의 구조
표 94 — trackChangeAuthor 요소
속성 이름	설명
name	검토자 이름
mark	검토 표시 여부
color	지정 시 색상
id	검토자를 구별하기 위한 아이디
샘플 46 — trackChangeAuthor 예
code
Xml
<hh:trackChangeAuthors itemCnt="1">
    <hh:trackChangeAuthor name="hancom" mark="1" id="1"/>
</hh:trackChangeAuthors>
10. 본문 XML 스키마
10.1 네임스페이스
Body XML은 기본적으로 "http://www.owpml.org/owpml/2024/body"를 기본 네임스페이스로 사용한다. 기본 네임스페이스의 접두어(prefix)는 기본적으로 "hp"를 사용한다. 잘못된 사용을 막기 위해서 "hp"를 기본 네임스페이스("http://www.owpml.org/owpml/2024/body") 이외의 네임스페이스에 사용하지 않는 것을 권고한다.
10.2 본문 개요
그림 66 — 논리적 구조
본문의 논리적인 구조는 ‘본문-구역-문단’이다. 위의 그림은 논리적인 구조를 도식화한 그림이다. 본문은 구역들의 목록으로 구성된다. 이 문서에서 서술하는 규격에서는 본문(Body)이 따로 존재하지 않고, 각 구역(Section)이 개별 파일로 저장된다. 구역은 반드시 한 개 이상 존재해야 하며, 한 구역은 반드시 한 개 이상의 문단을 가지고 있어야 한다. 표나 상자 같은 특수한 경우, 문단은 다시 문단 목록을 가지고 있을 수 있다. 이 경우 문단은 여러 개의 문단 목록을 자식 요소로서 가지고 있을 수 있다. 문단은 실제 문서 내용이 가지고 있는 단위로, 단순 텍스트뿐만 아니라 표, 그림, 그리기 객체 등 멀티미디어 요소를 가질 수 있다.
10.3 sec 요소
<sec> 요소는 구역을 나타낸다. 내부적으로 구역에 대한 설정 정보를 가지며, 이에 대한 자세한 내용은 10.6을 참조한다.
표 95 — sec 요소
하위 요소 이름	설명
p	문단
10.4 p 요소
<p> 요소는 HWP 문서에서 내용 표현을 위한 기본 단위이며 문단을 나타낸다.
그림 68 — <p>의 구조
표 96 — p 요소
속성 이름	설명
id	문단을 식별하기 위한 아이디
paraPrIDRef	문단 모양 아이디 참조값
styleIDRef	스타일 아이디 참조값
pageBreak	쪽 나눔 여부
columnBreak	단 나눔 여부
merged	문단 병합 여부
paraTcId	문단 번호 변경 추적 아이디
표 97 — p 하위 요소
하위 요소 이름	설명
run	글자 속성 컨테이너
metaTag	메타태그 관련 정보
샘플 47 — p 예
code
Xml
<hp:p id="3121190098" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
    <hp:run charPrIDRef="0">
        <hp:t>샘플 문서</hp:t>
    </hp:run>
</hp:p>
10.5 run 요소
run은 글자 속성 컨테이너를 의미한다. 하나 혹은 여러 개의 글자가 가지고 있는 동일한 속성을 나타낸다. 문서의 모든 콘텐츠와 내용 관련 요소들은 <run> 요소로 묶여서 구성된다. <run> 요소는 크게 두 가지 형태의 자식 요소를 가진다. 하나는 구역, 단, 문단의 제어에 관련된 요소들을 가지는 <ctrl> 요소와, 다른 하나는 문자열, 표, 그림 등의 실제 내용을 가지는 요소이다.
그림 69 — <run>의 구조
표 98 — run 요소
속성 이름	설명
charPrIDRef	글자 모양 설정 아이디 참조값
표 99 — run 하위 요소
하위 요소 이름	설명
secPr	구역 설정 정보
ctrl	문단 제어 정보
t	텍스트 문자열
tbl	표
pic	그림
container	묶음 객체
ole	OLE
equation	수식
line	선
rect	사각형
ellipse	타원
arc	호
polygon	다각형
curve	곡선
connectLine	연결선
textart	글맵시
compose	글자 겹침
dutmal	덧말
btn	버튼
radioBtn	라디오 버튼
checkBtn	체크 버튼
comboBox	콤보 박스
edit	에디트
listBox	리스트 박스
scrollBar	스크롤바
video	비디오
chart	차트
10.6 secPr 요소
구역(Section)은 콘텐츠의 영역을 구분 짓는 가장 큰 단위이다. <secPr> 요소는 구역 내에서의 각종 설정 정보를 가지고 있는 요소이다.
그림 70 — <secPr>의 구조
표 100 — secPr 요소
속성 이름	설명
id	구역 정의를 식별하기 위한 아이디
textDirection	구역 내 텍스트 방향
spaceColumns	동일한 페이지에서 서로 다른 단 사이의 간격
tabStop	기본 탭 간격
tabStopVal	기본 탭 간격 (1.31 이후 버전)
tabStopUnit	기본 탭 간격 단위 (1.31 이후 버전)
outlineShapeIDRef	개요 번호 모양 아이디 참조값
memoShapeIDRef	메모 모양 아이디 참조값
textVerticalWidthHead	머리말/꼬리말 세로 쓰기 여부
masterPageCnt	구역 내에서 정의된 바탕쪽 설정의 개수
표 101 — secPr 하위 요소
하위 요소 이름	설명
startNum	구역 내 각 객체의 시작 번호 정보
grid	줄맞춤 정보
visibility	감추기/보여주기 정보
lineNumberShape	줄 번호 정보
pagePr	용지 설정 정보
footNotePr	각주 모양 정보
endNotePr	미주 모양 정보
pageBorderFill	쪽 테두리/배경 정보
masterPage	바탕쪽 설정 정보
presentation	프레젠테이션 정보
샘플 48 — secPr 예
code
Xml
<hp:secPr id="0" textDirection="HORIZONTAL" spaceColumns="1134" tabStop="8000" tabStopVal="4000" tabStopUnit="HWPUNIT" outlineShapeIDRef="1" memoShapeIDRef="0" textVerticalWidthHead="0" masterPageCnt="0">
    <hp:grid lineGrid="0" charGrid="0" wonggojiFormat="0"/>
    <hp:startNum pageStartsOn="BOTH" page="0" pic="0" tbl="0" equation="0"/>
    <hp:visibility hideFirstHeader="0" hideFirstFooter="0" hideFirstMasterPage="0" border="SHOW_ALL" fill="SHOW_ALL" hideFirstPageNum="0" hideFirstEmptyLine="0" showLineNumber="0"/>
    <hp:lineNumberShape restartType="0" countBy="0" distance="0" startNumber="0"/>
</hp:secPr>
구역 내에서 각종 시작 번호들에 대한 설정을 가지고 있는 요소이다.
그림 71 — <startNum>의 구조
표 102 — startNum 요소
속성 이름	설명
pageStartsOn	구역 나눔으로 새 페이지가 생길 때 페이지 번호 적용 유형
page	쪽 시작 번호. 값이 0이면 앞 구역에 이어서 번호를 매기고, 1 이상이면 임의의 번호로 시작.
pic	그림 시작 번호. 값이 0이면 앞 구역에 이어서 번호를 매기고, 1 이상이면 임의의 번호로 시작.
tbl	표 시작 번호. 값이 0이면 앞 구역에 이어서 번호를 매기고, 1 이상이면 임의의 번호로 시작.
equation	수식 시작 번호. 값이 0이면 앞 구역에 이어서 번호를 매기고, 1 이상이면 임의의 번호로 시작.
샘플 49 — startNum 예
<hp:startNum pageStartsOn="BOTH" page="0" pic="0" tbl="0" equation="0"/>
구역 내의 줄맞춤 설정 정보를 표현하기 위한 요소이다.
그림 72 — <grid>의 구조
표 103 — grid 요소
속성 이름	설명
lineGrid	세로로 줄맞춤을 할지 여부
charGrid	가로로 줄맞춤을 할지 여부
wonggojiFormat	원고지 형식 사용 여부
샘플 50 — grid 예
<hp:grid lineGrid="0" charGrid="0" wonggojiFormat="0"/>
구역 내의 각 요소들에 대한 보여주기/감추기 설정 정보를 표현하기 위한 요소이다.
그림 73 — <visibility>의 구조
표 104 — visibility 요소
속성 이름	설명
hideFirstHeader	첫 쪽에만 머리말 감추기 여부
hideFirstFooter	첫 쪽에만 꼬리말 감추기 여부
hideFirstMasterPage	첫 쪽에만 바탕쪽 감추기 여부
border	테두리 감추기/보여주기 여부 (첫 쪽에만 감추기, 첫 쪽에만 보여주기, 모두 보여주기)
fill	배경 감추기/보여주기 여부 (첫 쪽에만 감추기, 첫 쪽에만 보여주기, 모두 보여주기)
hideFirstPageNum	첫 쪽에만 쪽번호 감추기 여부
hideFirstEmptyLine	첫 쪽에만 빈 줄 감추기 여부
showLineNumber	줄 번호 표시 여부
샘플 51 — visibility 예
<hp:visibility hideFirstHeader="0" hideFirstFooter="0" hideFirstMasterPage="0" border="SHOW_ALL" fill="SHOW_ALL" hideFirstPageNum="0" hideFirstEmptyLine="0" showLineNumber="0"/>
구역 내의 줄 번호 정보를 표현하기 위한 요소이다.
그림 74 — <lineNumberShape>의 구조
표 105 — lineNumberShape 요소
속성 이름	설명
restartType	줄 번호 방식
countBy	줄 번호 표시 간격
distance	본문과의 줄 번호 위치
startNumber	줄 번호 시작 번호
샘플 52 — lineNumberShape 예
<hp:lineNumberShape restartType="0" countBy="1" distance="2834" startNumber="1"/>
구역 내의 용지 설정 정보를 표현하기 위한 요소이다.
그림 75 — <pagePr>의 구조
표 106 — pagePr 요소
속성 이름	설명
landscape	용지 방향
width	용지 가로 크기. 단위는 HWPUNIT.
height	용지 세로 크기. 단위는 HWPUNIT.
gutterType	제본 방식 (LEFT_ONLY: 왼쪽, LEFT_RIGHT: 맞쪽, TOP_BOTTOM: 위쪽)
표 107 — pagePr 하위 요소
하위 요소 이름	설명
margin	여백 정보
샘플 53 — pagePr 예
code
Xml
<hp:pagePr landscape="WIDELY" width="59528" height="84186" gutterType="LEFT_ONLY">
    <hp:margin header="4252" footer="4252" gutter="0" left="8504" right="8504" top="5668" bottom="4252"/>
</hp:pagePr>
(MarginAttributeGroup)은 여백 정보를 표현할 때 공통적으로 사용되는 속성들을 모은 형식이다. [MarginAttributeGroup]은 <margin> 요소, <outMargin> 요소 등에서 사용된다.
그림 76 — [MarginAttributeGroup]의 구조
표 108 — MarginAttributeGroup 요소
속성 이름	설명
left	왼쪽 여백. 단위는 HWPUNIT.
right	오른쪽 여백. 단위는 HWPUNIT.
top	위쪽 여백. 단위는 HWPUNIT.
bottom	아래쪽 여백. 단위는 HWPUNIT.
<margin> 요소는 속성 그룹 (MarginAttributeGroup)을 포함한다. (MarginAttributeGroup)은 10.6.6.2를 참조한다.
그림 77 — <margin>의 구조
표 109 — margin 요소
속성 이름	설명
(MarginAttributeGroup)	10.6.6.2 참조
header	머리말 여백. 단위는 HWPUNIT.
footer	꼬리말 여백. 단위는 HWPUNIT.
gutter	제본 여백. 단위는 HWPUNIT.
샘플 54 - margin 예
<hp:margin header="4252" footer="4252" gutter="0" left="8504" right="8504" top="5668" bottom="4252"/>
각주 모양 정보를 가지고 있는 요소이다.
그림 78 — <footNotePr>의 구조
표 110 — footNotePr 요소
하위 요소 이름	설명
autoNumFormat	자동 번호 매김 모양 정보
noteLine	구분선 모양 정보
noteSpacing	여백 정보
numbering	번호 매김 형식
placement	위치 정보
샘플 55 — footNotePr 예
code
Xml
<hp:footNotePr>
    <hp:autoNumFormat type="DIGIT" userChar="" prefixChar="" suffixChar=")" supscript="1"/>
    <hp:noteLine length="5cm" type="SOLID" width="0.12mm" color="#000000"/>
    <hp:noteSpacing betweenNotes="283" belowLine="567" aboveLine="850"/>
    <hp:numbering type="CONTINUOUS" newNum="1"/>
    <hp:placement place="EACH_COLUMN" beneathText="0"/>
</hp:footNotePr>
각주/미주 내에서 사용되는 자동 번호 매김 모양 정보를 가지고 있는 요소이다.
그림 79 — <autoNumFormat>의 구조
표 111 — autoNumFormat 요소
속성 이름	설명
type	번호 모양 종류
userChar	사용자 정의 기호. type이 USER_CHAR로 설정된 경우, 번호 모양으로 사용될 사용자 정의 글자.
prefixChar	앞 장식 문자
suffixChar	뒤 장식 문자
supscript	각주/미주 내용 중 번호 코드의 모양을 위첨자 형식으로 할지 여부
샘플 56 — autoNumFormat 예
<hp:autoNumFormat type="DIGIT" userChar="" prefixChar="" suffixChar=")" supscript="0"/>
각주/미주 내에서 사용되는 구분선 모양 정보를 가지고 있는 요소이다.
표 112 — noteLine 요소
속성 이름	설명
length	구분선 길이 (0(구분선 없음), 5cm, 2cm, Column/3(단 크기의 1/3), Column(단 크기), 그 외 (HWPUNIT 단위의 사용자 지정 길이))
type	구분선 종류
width	구분선 굵기. 단위는 mm.
color	구분선 색
각주/미주 내에서 사용되는 여백 정보를 가지고 있는 요소이다.
그림 81 — <noteSpacing>의 구조
표 113 — noteSpacing 요소
속성 이름	설명
betweenNotes	주석 사이의 여백
belowLine	구분선 아래 여백
aboveLine	구분선 위 여백
샘플 57 — noteSpacing 예
<hp:noteSpacing betweenNotes="283" belowLine="567" aboveLine="850"/>
<footNotePr> 요소의 <numbering> 요소와 <endNotePr> 요소의 <numbering> 요소는 구조상 동일하다. 하지만 속성에서 허용되는 값의 범위가 다르다. <footNotePr> 요소의 <numbering> 요소의 경우 속성 @type이 가질 수 있는 값의 범위는 CONTINUOUS, ON_SECTION, ON_PAGE이다. <endNotePr> 요소의 <numbering> 요소의 경우 속성 @type이 가질 수 있는 값의 범위는 CONTINUOUS, ON_SECTION이다.
그림 82 — <numbering>의 구조
표 114 — numbering 요소
속성 이름	설명
type	번호 매기기 형식
newNum	시작 번호. type이 ON_SECTION일 때에만 사용됨.
샘플 58 — numbering 예
<hp:numbering type="CONTINUOUS" newNum="1"/>
<footNotePr> 요소의 <placement> 요소와 <endNotePr> 요소의 <placement> 요소는 구조상 동일하다. 하지만 속성에서 허용되는 값의 범위가 다르다. <footNotePr> 요소의 <placement> 요소의 경우 속성 @place에서 가질 수 있는 값의 범위는 EACH_COLUMN, MERGED_COLUMN, RIGHT_MOST_COLUMN이다. <endNotePr> 요소의 <placement> 요소의 경우 속성 @place에서 가질 수 있는 값의 범위는 END_OF_DOCUMENT, END_OF_SECTION이다.
그림 83 — <placement>의 구조
표 115 — placement 요소
속성 이름	설명
place	한 페이지 내에서 각주를 다단에 어떻게 위치시킬지에 대한 설정
beneathText	텍스트에 이어 바로 출력할지 여부
샘플 59 — placement 예
<hp:placement place="EACH_COLUMN" beneathText="0"/>
미주 모양 정보를 가지고 있는 요소이다.
그림 84 — <endNotePr>의 구조
표 116 — endNotePr 요소
하위 요소 이름	설명
autoNumFormat	자동 번호 매김 모양 정보
noteLine	구분선 모양 정보
noteSpacing	여백 정보
numbering	번호 매김 형식
placement	위치 정보
샘플 60 — endNotePr 예
code
Xml
<hp:endNotePr>
    <hp:autoNumFormat type="DIGIT" userChar="" prefixChar="" suffixChar=")" supscript="1"/>
    <hp:noteLine length="14692344" type="SOLID" width="0.12mm" color="#000000"/>
    <hp:noteSpacing betweenNotes="0" belowLine="567" aboveLine="850"/>
    <hp:numbering type="CONTINUOUS" newNum="1"/>
    <hp:placement place="END_OF_DOCUMENT" beneathText="0"/>
</hp:endNotePr>
<footNotePr> 요소의 <numbering> 요소와 <endNotePr> 요소의 <numbering> 요소는 구조상 동일하다. 하지만 속성에서 허용되는 값의 범위가 다르다. <footNotePr> 요소의 <numbering> 요소의 경우 속성 @type이 가질 수 있는 값의 범위는 CONTINUOUS, ON_SECTION, ON_PAGE이다. <endNotePr> 요소의 <numbering> 요소의 경우 속성 @type이 가질 수 있는 값의 범위는 CONTINUOUS, ON_SECTION이다.
그림 85 — <numbering>의 구조
표 117 — numbering 요소
속성 이름	설명
type	번호 매기기 형식
newNum	시작 번호. type이 ON_SECTION일 때에만 사용됨.
샘플 61 — numbering 예
<hp:numbering type="CONTINUOUS" newNum="1"/>
<footNotePr> 요소의 <placement> 요소와 <endNotePr> 요소의 <placement> 요소는 구조상 동일하다. 하지만 속성에서 허용되는 값의 범위가 다르다. <footNotePr> 요소의 <placement> 요소의 경우 속성 @place에서 가질 수 있는 값의 범위는 EACH_COLUMN, MERGED_COLUMN, RIGHT_MOST_COLUMN이다. <endNotePr> 요소의 <placement> 요소의 경우 속성 @place에서 가질 수 있는 값의 범위는 END_OF_DOCUMENT, END_OF_SECTION이다.
그림 86 — <placement>의 구조
표 118 — placement 요소
속성 이름	설명
place	한 페이지 내에서 미주를 다단에 어떻게 위치시킬지에 대한 설정
beneathText	텍스트에 이어 바로 출력할지 여부
샘플 62 — placement 예
<hp:placement place="END_OF_DOCUMENT" beneathText="0"/>
<pageBorderFill>은 구역 내에서 사용되는 테두리/배경 설정 정보를 가지고 있는 요소이다.
그림 87 — <pageBorderFill>의 구조
표 119 — pageBorderFill 요소
속성 이름	설명
type	쪽 테두리 종류
borderFillIDRef	테두리/배경 정보 아이디 참조값
textBorder	쪽 테두리 위치 기준
headerInside	머리말 포함 여부
footerInside	꼬리말 포함 여부
fillArea	채움 영역
표 120 — pageBorderFill 하위 요소
하위 요소 이름	설명
offset	테두리/배경 위치 정보
샘플 63 — pageBorderFill 예
code
Xml
<hp:pageBorderFill type="BOTH" borderFillIDRef="1" textBorder="PAPER" headerInside="1" footerInside="1" fillArea="PAPER">
    <hp:offset left="1417" right="1417" top="1417" bottom="1417"/>
</hp:pageBorderFill>
구역 내에서 사용되는 테두리/배경에 대한 위치 정보를 가지고 있는 요소이다.
그림 88 — <offset>의 구조
표 121 — offset 요소
속성 이름	설명
left	왼쪽 간격. 단위는 HWPUNIT.
right	오른쪽 간격. 단위는 HWPUNIT.
top	위쪽 간격. 단위는 HWPUNIT.
bottom	아래쪽 간격. 단위는 HWPUNIT.
샘플 64 — offset 예
<hp:offset left="1417" right="1417" top="1417" bottom="1417"/>
<masterPage> 요소는 바탕쪽 스키마에서 설정된 정보를 참조한다. 한 섹션 내에서 바탕쪽은 여러 개가 올 수 있다.
그림 89 — <masterPage>의 구조
표 122 — masterPage 요소
속성 이름	설명
idRef	바탕쪽 설정 정보 아이디 참조값
샘플 65 — masterPage 예
<hp:masterPage idRef="masterpage1"/>
문서의 프레젠테이션 설정 정보를 갖고 있는 요소이다.
표 123 — presentation 요소
속성 이름	설명
effect	화면 전환 효과
soundIDRef	효과음 바이너리 데이터에 대한 아이디 참조값
invertText	글자색 반전 효과 여부
autoShow	자동 시연 여부
showTime	화면 전환 시간 (초 단위)
applyTo	적용범위 (PRAT_WHOLE_DOCUMENT: 문서 전체, PRAT_NEWSECTION: 현재 위치부터 새 구역)
표 124 — presentation 하위 요소
하위 요소 이름	설명
fillBrush	채우기 정보
샘플 66 — presentation 예
code
Xml
<hp:presentation effect="OVER_LEFT" soundIDRef="" invertText="0" autoShow="0" showTime="0" applyTo="WholeDoc">
    <hp:fillBrush>
        <hc:winBrush faceColor="#FF6600" hatchColor="#FFFFFF"/>
    </hp:fillBrush>
</hp:presentation>
PRE_MOVE_UP: 위로 가리기
PRE_MOVE_DOWN: 아래로 가리기
PRE_RANDOM: 임의 선택
10.7 Ctrl 요소
<ctrl> 요소는 콘텐츠에서 본문 내 제어 관련 요소들을 모은 요소이다.
그림 91 — <ctrl>의 구조
표 126 — Ctrl 요소
하위 요소 이름	설명
colPr	단 설정 정보
fieldBegin	필드 시작
fieldEnd	필드 끝
bookmark	책갈피
header	머리말 (10.7.5 머리말/꼬리말 요소 형식 참조)
footer	꼬리말 (10.7.5 머리말/꼬리말 요소 형식 참조)
footNote	각주 (10.7.6 각주/미주 요소 형식 참조)
endNote	미주 (10.7.6 각주/미주 요소 형식 참조)
autoNum	자동 번호
newNum	새 번호
pageNumCtrl	홀/짝수 조정
pageHiding	감추기
pageNum	쪽번호 위치
indexmark	찾아보기 표식
hiddenComment	숨은 설명
샘플 67 — Ctrl 예
code
Xml
<hp:ctrl>
    <hp:colPr id="0" type="NEWSPAPER" layout="LEFT" colCount="1" sameSz="1" sameGap="0"/>
</hp:ctrl>
10.7.1 colPr 요소
단 설정 정보들을 가지고 있는 요소이다.
그림 92 — <colPr>의 구조
표 127 — colPr 요소
속성 이름	설명
id	단 설정 정보를 구별하기 위한 아이디
type	단 종류
layout	단 방향 지정
colCount	단 개수
sameSz	단 너비를 동일하게 지정할지 여부 (true이면 동일한 너비, false이면 각기 다른 너비)
sameGap	단 사이 간격을 동일하게 지정했을 경우에만 사용됨
표 128 — colPr 하위 요소
하위 요소 이름	설명
colLine	단 구분선
colSz	단 사이 간격. 단 너비를 각기 다르게 지정했을 경우에만 사용됨.
샘플 68 — colPr 예
code
Xml
<hp:ctrl>
    <hp:colPr id="0" type="NEWSPAPER" layout="LEFT" colCount="1" sameSz="1" sameGap="0"/>
</hp:ctrl>
단 사이의 구분선 설정 정보를 가지고 있는 요소이다.
표 129 — colLine 요소
속성 이름	설명
type	구분선 종류
width	구분선 굵기
color	구분선 색
샘플 69 — colLine 예
code
Xml
<hp:colPr id="0" type="NEWSPAPER" layout="LEFT" colCount="2" sameSz="1" sameGap="14174">
    <hp:colLine type="DOUBLE_SLIM" width="0.7mm" color="#3A3C84"/>
</hp:colPr>
<colPr>의 속성 중 @sameSz 속성이 false(각기 다른 단 사이 간격을 가짐)로 설정되었을 때에만 사용되는 요소이다.
그림 94 — <colSz>의 구조
표 130 — colSz 요소
속성 이름	설명
width	단의 크기
gap	단 사이 간격
샘플 70 — colSz 예
code
Xml
<hp:colPr id="0" type="NEWSPAPER" layout="LEFT" colCount="2" sameSz="0" sameGap="2268">
    <hp:colLine type="DOUBLE_SLIM" width="0.7mm" color="#3A3C84"/>
    <hp:colSz width="20090" gap="1740"/>
    <hp:colSz width="10924" gap="0"/>
</hp:colPr>
10.7.2 fieldBegin 요소
메모, 외부 연결, 북마크 등 문서 내에서 부가적인 기능을 표현하기 위한 요소이다.
표 131 — fieldBegin 요소
속성 이름	설명
id	필드 시작을 구별하기 위한 아이디
type	필드 종류
name	필드 이름
editable	읽기 전용 상태에서도 수정 가능한지 여부
fieldid	필드 객체 ID
