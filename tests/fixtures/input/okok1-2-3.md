복원된 텍스트 파일
fieldid 필드 개체 ID
표 132—fieldBegin 하위 요소
하위 요소 이름	설명
parameters	필드 동작에 필요한 인자들
subList	내용 수정 필드에서 사용됨
metaTag	메타태그 관련 정보
예제 71. fieldBegin 예
code
Xml
<hp:fieldBegin id="B179516910r" type="CLICK_HERE" name="editable" dirty="true" zorder="0"
fieldId="627272811">
    <hp:parameters count="3" name="">
        <hp:integerParam name="Prop">9</hp:integerParam>
        <hp:stringParam name="Command" xml:space="preserve">Clickhere:set:66:Direction:wstring:23:이곳을 마우스로 누르고 내용을 입력하세요.;HelpState:wstring:0:</hp:stringParam>
        <hp:stringParam name="Direction">이곳을 마우스로 누르고 내용을 입력하세요.</hp:stringParam>
    </hp:parameters>
    <hp:metaTag name=""></hp:metaTag>
</hp:fieldBegin>
10.7.2.2 CLICK_HERE
누름틀은 문서마당을 불러왔을 때 화면에 불린 문서마당의 빈 곳을 채워 넣을 안내문과 안내문에 대한 간단한 메모 내용을 입력하는 기능이다.
10.7.2.2.1 필요한 인자들
표 133— CLICK_HERE 요소
| 인자 이름 | 인자 형식 | 설명 |
| :---------- | :----------- | :------------- |
| Direction | stringParam | 안내문 문자열 |
| HelpState | stringParam | 안내문 도움말 |
예제 72. CLICK_HERE 예
code
Xml
<fieldBegin id="fb0r" type="CLICK_HERE" name="Title" editable="true" dirty="false">
    <parameters count="2">
        <stringParam name="Direction">이 곳에 내용 입력!</stringParam>
        <stringParam name="HelpState"></stringParam>
    </parameters>
</fieldBegin>
10.7.2.3 HYPERLINK
10.7.2.3.1 HYPERLINK
하이퍼링크는 문서의 특정한 위치에 현재 문서나 다른 문서, 웹 페이지, 전자우편 주소 등을 연결하여 쉽게 참조하거나 이동할 수 있게 해 주는 기능이다.
문서 내에서 그룹 객체를 사용할 경우 하이퍼링크 종류를 결정할 수 없는 경우가 발생할 수 있다. 각 개별 객체별로 하이퍼링크를 사용하고, 이 객체들을 하나의 그룹으로 묶을 경우 그룹 객체가 생성된다. 이때 생성된 그룹 객체는 그룹 내 객체들이 모두 같은 내용의 하이퍼링크 설정을 가지고 있지 않다면 하이퍼링크 종류, 하이퍼링크 대상, 문서창 옵션 등을 결정할 수 없게 된다. 이런 경우 그룹 객체의 하이퍼링크 설정은 HWPHYPERLINK_TYPE_DONTCARE, HWPHYPERLINK_TARGET_DOCUMENT_DONTCARE, HWPHYPERLINK_JUMP_DONTCARE의 값을 가져야 한다.
10.7.2.3.2 필요한 인자들
표 134—HYPERLINK 요소
| 인자 이름 | 인자 형식 | 설명 |
| :----------- | :------------ | :--------------------------------------------------------- |
| Path | stringParam | 링크 경로 |
| Category | stringParam | 하이퍼링크의 종류 |
| TargetType | stringParam | 하이퍼링크의 종류가 한글 문서인 경우, 한글 문서에서 대상의 종류 |
| DocOpenType | stringParam | 이동 시 문서창 옵션 |
하이퍼링크의 종류
표 135— 하이퍼링크 종류
| 하이퍼링크 종류 | 설명 |
| :---------------------------------- | :------------------------------------------------------------------------- |
| HWPHYPERLINK_TYPE_DONTCARE | 여러 개의 개체가 묶여진 그룹 객체 설정에서 하이퍼링크 종류가 다른 경우. |
| HWPHYPERLINK_TYPE_HWP | HWP 문서 내부의 책갈피 |
| HWPHYPERLINK_TYPE_URL | 웹 주소 |
| HWPHYPERLINK_TYPE_EMAIL | 메일 주소 |
| HWPHYPERLINK_TYPE_EXT | 외부 애플리케이션 문서 |
HWP 문서에서 대상의 종류
표 136 — 대상의 종류
| HWP 문서에서 대상의 종류 | 설명 |
| :------------------------------------------- | :------------------------------------------------------------------- |
| HWPHYPERLINK_TARGET_DOCUMENT_DONTCARE | 동일 그룹 객체 내의 개별 객체들의 하이퍼링크 설정에서 연결 문서가 다른 경우. |
| HWPHYPERLINK_TARGET_OBJECT_DONTCARE | 동일 그룹 객체 내의 개별 객체들의 하이퍼링크 설정에서 책갈피 내용이 다른 경우. |
| HWPHYPERLINK_TARGET_BOOKMARK | 책갈피 |
| HWPHYPERLINK_TARGET_OUTLINE | 개요 |
| HWPHYPERLINK_TARGET_TABLE | 표 |
| HWPHYPERLINK_TARGET_FIGURE | 그림, 그리기 객체 |
| HWPHYPERLINK_TARGET_EQUATION | 수식 |
| HWPHYPERLINK_TARGET_HYPERLINK | 하이퍼링크 |
이동 시 문서창 옵션
표 137— 문서창 옵션
| 이동 시 문서창 옵션 종류 | 설명 |
| :------------------------------ | :---------------------------------------------------------------- |
| HWPHYPERLINK_JUMP_DONTCARE | 동일 그룹 객체 내의 개별 객체들의 하이퍼링크 설정에서 문서창 옵션 종류가 다른 경우. |
| HWPHYPERLINK_JUMP_CURRENTTAB | 현재 문서 탭에서 열기 |
| HWPHYPERLINK_JUMP_NEWTAB | 새로운 문서 탭에서 열기 |
| HWPHYPERLINK_JUMP_NEWWINDOW | 새로운 문서 창에서 열기 |
예제 73. HYPERLINK 예
code
Xml
<fieldBegin id="fb02" type="HYPERLINK" editable="false" dirty="false">
    <parameters count="4">
        <stringParam name="Path">http://www.hancom.co.kr</stringParam>
        <stringParam name="Category">HWPHYPERLINK_TYPE_URL</stringParam>
        <stringParam name="TargetType">HWPHYPERLINK_TARGET_DOCUMENT_DONTCARE</stringParam>
        <stringParam name="DocOpenType">HWPHYPERLINK_JUMP_NEWTAB</stringParam>
    </parameters>
</fieldBegin>
10.7.2.4 BOOKMARK
10.7.2.4.1 BOOKMARK
두꺼운 책을 읽을 때 책의 중간에 책갈피를 꽂아 두고 필요할 때마다 펼쳐 보면 편리하듯이, [책갈피] 기능은 문서를 편집하는 도중에 본문의 여러 곳에 표시를 해 두었다가 현재 커서의 위치에 상관없이 표시해 둔 곳으로 커서를 곧바로 이동시키는 기능이다.
10.7.2.4.2 XML 예
예제 74. BOOKMARK 예
code
Xml
<fieldBegin id="fb03" type="BOOKMARK" name="txt0r" editable="false" dirty="false"/>
10.7.2.5 FORMULA
10.7.2.5.1 FORMULA
표 계산식은 표에서 덧셈, 뺄셈, 곱셈, 나눗셈 등 간단한 사칙연산은 물론 sum과 avg와 같은 함수를 사용하여 자동으로 계산하는 기능이다.
10.7.2.5.2 필요한 인자들
표 138— FORMULA 요소
| 인자 이름 | 인자 형식 | 설명 |
| :------------------ | :---------- | :--------------------- |
| FunctionName | stringParam | 계산식 함수 이름 |
| FunctionArguments | listParam | 계산식에 필요한 인자들 |
| ResultFormat | stringParam | 결과 출력 형식 |
| LastResult | stringParam | 마지막으로 계산된 결과 |
함수 목록
표 139—FORMULA 함수 목록
| 함수 종류 | 설명 |
| :--------- | :----------------------------------------- |
| SUM | 지정한 범위의 셀들에 대한 합계 계산 |
| AVG | 지정한 범위의 셀들에 대한 평균값 계산 |
| PRODUCT | 지정한 범위의 셀들에 대한 곱셈 계산 |
| MIN | 지정한 범위의 셀들 중 최소값을 찾음. |
| MAX | 지정한 범위의 셀들 중 최대값을 찾음. |
| COUNT | 지정한 범위의 셀들에 대해 공백이 아닌 셀의 수를 계산 |
| ROUND | 하나의 셀에 대하여 지정한 자릿수에서 반올림 |
| MOD | 두 개의 셀에 대한 나눗셈의 나머지 계산 |
| SQRT | 하나의 셀에 대한 양의 제곱근을 계산 |
| DEGTORAD | 하나의 셀에 대한 도(일반각)를 라디안(호도법)으로 변환 |
| RADTODEG | 하나의 셀에 대한 라디안(호도법)을 도(일반각)로 변환 |
| COS | 하나의 셀에 대한 코사인 값 계산 |
| SIN | 하나의 셀에 대한 사인 값 계산 |
| TAN | 하나의 셀에 대한 탄젠트 값 계산 |
| ACOS | 하나의 셀에 대한 아크 코사인 값 계산 |
| ASIN | 하나의 셀에 대한 아크 사인 값 계산 |
| ATAN | 하나의 셀에 대한 아크 탄젠트 값 계산 |
| ABS | 하나의 셀에 대한 절대값을 계산 |
| INT | 하나의 셀에 대하여 소수점을 무시하고 정수 값만을 계산 |
| SIGN | 하나의 셀에 대하여 양수 값이면 1, 0이면 0, 음수 값이면 -1로 계산 |
| CEILING | 하나의 셀에 대하여 크거나 같은 최소 정수를 계산 |
| FLOOR | 하나의 셀에 대하여 작거나 같은 최대 정수를 계산 |
| EXP | 하나의 셀에 대한 자연 지수 e의 거듭 제곱 값을 계산 |
| LN | 하나의 셀에 대한 자연 로그 값(밑이 자연 지수 e인 로그 값)을 계산 |
| LOG | 하나의 셀에 대한 상용 로그 값(밑이 10인 로그 값)을 계산 |
함수 인자
표 140 — FORMULA 함수 인자
| 함수 인자 형태 | 설명 |
| :------------- | :--------------------------------------------------------- |
| LEFT | 현재 셀 왼쪽의 모든 셀 |
| RIGHT | 현재 셀 오른쪽의 모든 셀 |
| ABOVE | 현재 셀 위쪽의 모든 셀 |
| BELOW | 현재 셀 아래쪽의 모든 셀 |
| 셀 주소 | A1, B2 등. 셀 주소와 LEFT, RIGHT, ABOVE, BELOW는 혼합해서 사용할 수 없음 |
셀 번호
커서를 움직여서 셀과 셀 사이를 이동하면 상황 선에 A1, A2, A3...과 같이 현재 커서가 놓여있는 셀의 이름이 표시된다. 즉 가로로는 A, B, C, D, E...의 순서로 이름이 정해지고, 세로로는 1, 2, 3, 4, 5...와 같은 순서로 이름이 정해진다.
표 141 — 셀 번호
| A1 | B1 | C1 | D1 | E1 |
| :-- | :-- | :-- | :-- | :-- |
| A2 | B2 | C2 | D2 | E2 |
| A3 | B3 | C3 | D3 | E3 |
| A4 | B4 | C4 | D4 | E4 |
| A5 | B5 | C5 | D5 | E5 |
결과 출력 형식
표 142— 결과 출력 형식
| 결과 출력 형식 | 설명 |
| :------------- | :----------------------- |
| %g | 기본 형식 |
| %.0f | 정수형 |
| %.1f | 소수점 이하 1자리까지만 표시 |
| %.2f | 소수점 이하 2자리까지만 표시 |
| %.3f | 소수점 이하 3자리까지만 표시 |
| %.4f | 소수점 이하 4자리까지만 표시 |
10.7.2.5.3 XML 예
예제 75. FORMULA 예
code
Xml
<fieldBegin id="fb04" type="FORMULA" editable="false" dirty="false">
    <parameters count="4">
        <stringParam name="FunctionName">SUM</stringParam>
        <listParam name="FunctionArguments" cnt="1">
            <stringParam>LEFT</stringParam>
        </listParam>
        <stringParam name="ResultFormat">%g</stringParam>
        <stringParam name="LastResult">77</stringParam>
    </parameters>
</fieldBegin>
10.7.2.6 DATE 및 DOC_DATE
날짜/시간 표시. DATE 형식은 하위 호환성을 위해 남겨둔 형식이다. DATE 형식은 되도록 사용하지 않는 것을 권고한다.
10.7.2.6.1 필요한 인자들
표 143—DATE 요소
| 인자 이름 | 인자 형식 | 설명 |
| :---------- | :---------- | :----------------- |
| DateNation | stringParam | 국가 코드 |
| DateFormat | stringParam | 날짜/시간 표시 형식|
국가 코드
국가 코드는 기본적으로 ISO 국가 코드 표기법(ISO 3166-1 alpha-3)을 따른다. 단 모든 국가를 지원하지 않고 다음의 다섯 개 국가의 날짜/시간 형태만을 지원한다.
표 144— 국가 코드
| 국가 코드 | 설명 |
| :-------- | :------- |
| KOR | 대한민국 |
| USA | 미국 |
| JPN | 일본 |
| CHN | 중국 |
| TWN | 대만 |
날짜/시간 표시 형식
날짜/시간 표시 형식은 기본적으로 ISO 날짜/시각 표기법(KS X ISO 8601 참조)을 따른다. 단, ISO 날짜/시각 표기법에서 지원하지 않는 표시 형식은 확장해서 사용한다. ISO 날짜/시각 표기법의 자세한 내용은 표준을 참조한다. 이 문서에서는 표준의 간략한 내용과 확장한 내용만을 설명한다.
표 145— 날짜/시간 표시 기호
| 날짜/시간 표시 기호 | 설명 |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Y | 년(year) 요소를 표현 |
| M | 월(month) 요소를 표현. M으로 표기된 경우 1과 같이 한 자리 수로 표현, MM으로 표현된 경우 01과 같이 2자리 수로 표현, MMM으로 표현된 경우 Jan과 같이 축약된 영어식 표현, MMMM인 경우 January와 같이 영어 전체 단어로 표현 |
| D | 일(day) 요소를 표현 |
| W | 주(week) 요소를 표현. 해당 년도에서 몇 번째 주인지 숫자로 표현. ex) 금주는 W번째 주이다. -> 금주는 16번째 주이다. |
| h | 시(hour) 요소를 표현 (24시간제, 0-23) |
| m | 분(minute) 요소를 표현 |
| s | 초(second) 요소를 표현 |
| n | 0 또는 양의 정수를 표현 |
| ± | [+] 또는 [-] |
| E | 확장 요소. 요일(day of the week) 요소를 표현. 국가 코드에 따라서 표현이 다름. 대한민국의 경우 월/화/수/목/금/토/일, 미국의 경우 Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday, 일본/중국/대만의 경우 月/火/水/木/金/土/日로 표현 |
| b | 확장 요소. 요일의 서수 요소를 표현. 월요일을 1을 기준으로 토요일은 6, 일요일은 7 |
| B | 확장 요소. 요일의 서수 요소를 표현. 대한민국/미국의 경우 숫자(1-7)로, 일본/중국/대만의 경우 한자(一-七)로 표현 |
| a | 확장 요소. 오전/오후 요소를 표현. 국가 코드에 따라서 표현이 다름. 대한민국의 경우 오전/오후, 미국의 경우 AM/PM, 일본의 경우 午前/午後, 중국/대만의 경우 上午/下午로 표현 |
| A | 확장 요소. A.M./P.M. 요소를 표현. 국가 코드에 상관없이 A.M./P.M. 중 하나로 표현 |
| I | 확장 요소. 연호/국력 요소를 표현. 일본의 경우 H, 대만의 경우 M, 그 외의 지역은 해당 요소는 무시 |
| L | 확장 요소. 연호/국력의 연도 요소를 표현. 일본/대만의 경우 각 국가의 연호/국력에 맞는 연도가 표시되고, 그 외의 지역은 Y 요소와 동일하게 표현 |
| k | 확장 요소. 시(hour) 요소를 표현 (12시간제, 1-12) |
날짜/시간 표시 예
YYYY-MM-DD hh:mm:ss -> 2011-01-01 01:00:00
YYYY년 M월 D일 E요일 -> 2011년 1월 1일 토요일
a k:mm -> 오전 1:00
YYYY年 M月 D日 (B) -> 2011年 1月 1日 (六)
MMMM D, YYYY -> January 1, 2011
IL年 M月 D日 -> 平成 23年 1月 1日
예제 76. DOC_DATE 예
code
Xml
<fieldBegin id="fb05" type="DOC_DATE" editable="false" dirty="false">
    <parameters count="2">
        <stringParam name="DateNation">KOR</stringParam>
        <stringParam name="DateFormat">YYYY-MM-DD hh:mm:ss</stringParam>
    </parameters>
</fieldBegin>
10.7.2.7 SUMMARY
10.7.2.7.1 Summary
문서 요약 정보는 현재 문서에 대한 제목, 주제, 지은이, 중심 낱말(키워드), 저자, 입력자, 교정자, 내용 요약, 주의사항 등을 간단히 기록할 수 있는 기능이다.
10.7.2.7.2 필요한 인자들
표 147—SUMMARY 요소
| 인자 이름 | 인자 형식 | 설명 |
| :-------- | :---------- | :----------------- |
| Property | stringParam | 문서 요약 정보 속성 |
문서 요약 정보 속성
표 148— 문서 요약 요소
| 속성 | 설명 |
| :------------ | :----------------------- |
| $title | 문서 제목 |
| $subject | 문서 주제 |
| $author | 문서 저자 |
| $keywords | 문서 키워드 |
| $comments | 문서 주석 |
| $lastAuthor | 문서 마지막 수정한 사람 |
| $revNumber | 문서 이력 번호 |
| $lastPrinted | 문서가 마지막으로 출력된 시각 |
| $createDate | 문서가 생성된 시각 |
| $lastSaveDate | 문서가 마지막으로 저장된 시각 |
| $pageCount | 문서 페이지 수 |
| $wordCount | 문서 단어 수 |
| $charCount | 문서 글자 수 |
10.7.2.7.3 XML 예
예제 77. SUMMARY 예
code
Xml
<fieldBegin id="fb06" type="SUMMARY" editable="false" dirty="false">
    <parameters count="1">
        <stringParam name="Property">$title</stringParam>
    </parameters>
</fieldBegin>
10.7.2.8 USER_INFO
10.7.2.8.1 USER_INFO
사용자 정보는 현재 문서의 작성자에 대한 이름, 회사명, 전화번호 등을 간단히 기록할 수 있는 기능이다.
10.7.2.8.2 필요한 인자들
표 149— USER_INFO 요소
| 인자 이름 | 인자 형식 | 설명 |
| :-------- | :---------- | :--------------- |
| Category | stringParam | 사용자 정보 항목 |
사용자 정보 항목
표 150— 사용자 정보 항목
| 항목 | 설명 |
| :---------------- | :----------------- |
| $UserName | 사용자 이름 |
| $Company | 회사 이름 |
| $Department | 부서 이름 |
| $Position | 직책 이름 |
| $OfficeTelephone | 회사 전화번호 |
| $Fax | 팩스 번호 |
| $HomeTelephone | 집 전화번호 |
| $Mobilephone | 핸드폰 번호 |
| $UMS1 | UMS 번호 1 |
| $UMS2 | UMS 번호 2 |
| $Homepage | 홈페이지 주소 |
| $Email1 | 전자우편 주소 1 |
| $Email2 | 전자우편 주소 2 |
| $Email3 | 전자우편 주소 3 |
| $OfficeZipcode | 회사 우편번호 |
| $OfficeAddress | 회사 주소 |
| $HomeZipcode | 집 우편번호 |
| $HomeAddress | 집 주소 |
| $Etc | 기타 |
| $UserDefineName | 사용자 정의 아이템 이름 |
| $UserDefineValue | 사용자 정의 아이템 값 |
10.7.2.8.3 XML 예
예제 78. USER_INFO 예
code
Xml
<fieldBegin id="fb07" type="USER_INFO" editable="false" dirty="false">
    <parameters count="1">
        <stringParam name="Category">$UserName</stringParam>
    </parameters>
</fieldBegin>
10.7.2.9 PATH
10.7.2.9.1 Path
현재 문서의 물리적인 파일 경로를 문서에 표시해 주는 기능이다.
10.7.2.9.2 필요한 인자들
표 151 —PATH 요소
| 인자 이름 | 인자 형식 | 설명 |
| :-------- | :---------- | :------------- |
| Format | stringParam | 파일 경로 형식 |
파일 경로 형식
(주: OCR된 문서에서 표 152의 내용이 유실되었습니다.)
10.7.2.9.3 XML 예
예제 79. PATH 예
code
Xml
<fieldBegin id="fb07" type="PATH" editable="false" dirty="false">
    <parameters count="1">
        <stringParam name="Format">$P$F</stringParam>
    </parameters>
</fieldBegin>
10.7.2.10 CROSSREF
10.7.2.10.1 CROSSREF
상호 참조는 다른 곳의 그림, 표 등을 현재의 본문에서 항상 참조할 수 있도록 그 위치를 표시해 주는 기능이다.
10.7.2.10.2 필요한 인자들
표 153— CROSSREF 요소
| 인자 이름 | 인자 형식 | 설명 |
| :------------- | :------------ | :--------------------------------------------------------------------- |
| RefPath | stringParam | 참조 경로 |
| RefType | stringParam | 참조 대상 종류 |
| RefContentType | stringParam | 참조 내용 |
| RefHyperLink | booleanParam | 하이퍼링크 여부 |
| RefOpenType | stringParam | 하이퍼링크 이동 시 문서창 열기 옵션. 참조 경로가 현재 문서가 아닌 외부 문서일 경우에만 사용됨 (HYPERLINK의 '이동 시 문서창 옵션' 참조) |
참조 경로 형식
참조 경로는 기본적으로 다음과 같은 형식을 가진다.
책갈피 상호 참조의 경우, 예외로 {참조 대상의 ID} 대신에 {책갈피 이름}을 사용한다.
참조 대상이 있는 문서가 현재 문서인 경우 {문서의 파일 경로}는 생략된다.
표 154— 참조 경로 형식
| 구분 | 형식 |
| :--------------- | :--------------------------------- |
| 외부 문서 참조인 경우 | {문서의 파일 경로}?{참조 대상의 ID 또는 책갈피 이름} |
| 현재 문서 참조인 경우 | ?{참조 대상의 ID 또는 책갈피 이름} |
참조 대상 종류
표 155— 참조 대상 종류
| 참조 대상 종류 | 설명 |
| :---------------- | :------- |
| TARGET_TABLE | 표 |
| TARGET_PICTURE | 그림 |
| TARGET_EQUATION | 수식 |
| TARGET_FOOTNOTE | 각주 |
| TARGET_ENDNOTE | 미주 |
| TARGET_OUTLINE | 개요 |
| TARGET_BOOKMARK | 책갈피 |
참조 내용
표 156— 참조 내용
| 참조 내용 | 설명 |
| :------------------- | :------------------------------------------------------------------- |
| OBJECT_TYPE_PAGE | 참조 대상이 있는 쪽 번호 |
| OBJECT_TYPE_NUMBER | 참조 대상의 번호 |
| OBJECT_TYPE_CONTENTS | 참조 대상의 캡션 내용 또는 책갈피의 경우 책갈피 내용. 미주/각주의 경우 해당 형식을 사용할 수 없음 |
| OBJECT_TYPE_UPDOWNPOS| 현재 위치 기준으로 참조 대상이 있는 위치 (위/아래) |
10.7.2.10.3 XML 예
예제 80. CROSSREF 예
code
Xml
<fieldBegin id="fb10" type="CROSSREF" editable="false" dirty="false">
    <parameters count="5">
        <stringParam name="RefPath">?Table8</stringParam>
        <stringParam name="RefType">TARGET_TABLE</stringParam>
        <stringParam name="RefContentType">OBJECT_TYPE_NUMBER</stringParam>
        <booleanParam name="RefHyperLink">true</booleanParam>
        <stringParam name="RefOpenType">HWPHYPERLINK_JUMP_DONTCARE</stringParam>
    </parameters>
</fieldBegin>
10.7.2.11 MAILMERGE
10.7.2.11.1 MAILMERGE
메일 머지는 여러 사람의 이름, 주소 등이 들어 있는 '데이터 파일(data file)'과 '서식 파일(form letter)'을 결합(merging)함으로써, 이름이나 직책, 주소 부분 등만 다르고 나머지 내용이 같은 수십, 수백 통의 편지지를 한꺼번에 만드는 기능이다.
10.7.2.11.2 필요한 인자들
표 157-MAILMERGE 요소
| 인자 이름 | 인자 형식 | 설명 |
| :--------- | :---------- | :----------------------------------------------------- |
| FieldType | stringParam | 필드 형식. WAB, USER_DEFINE 중 하나의 값을 가질 수 있음 |
| FieldValue | stringParam | 필드 엔트리 이름 |
필드 엔트리 이름
필드 형식이 USER_DEFINE인 경우 별도의 정해진 이름 규칙은 없다.
필드 형식이 WAB인 경우에는 다음의 이름만을 사용해야 한다.
표 158— 필드 엔트리 이름
| 참조 대상 종류 | 설명 |
| :------------------------------- | :-------------------------------------- |
| ENTRYID | Windows Address Book의 각 엔트리의 고유 아이디 |
| OBJECT_TYPE | 엔트리 객체 형식 |
| DISPLAY_NAME | 사용자 표시 이름 |
| SURNAME | 사용자 성 |
| GIVEN_NAME | 사용자 이름 |
| NICKNAME | 사용자 애칭 |
| TITLE | 직함 |
| COMPANY_NAME | 회사 이름 |
| DEPARTMENT_NAME | 부서 이름 |
| SPOUSE_NAME | 배우자 이름 |
| MOBILE_TELEPHONE_NUMBER | 휴대폰 번호 |
| PAGER_TELEPHONE_NUMBER | 호출기 번호 |
| EMAIL_ADDRESS | 전자우편 주소 |
| HOME_ADDRESS_COUNTRY | 집 주소 국가/지역 |
| HOME_ADDRESS_STATE_OR_PROVINCE | 집 주소 시/도 |
| HOME_ADDRESS_CITY | 집 주소 구/군/시 |
| HOME_ADDRESS_STREET | 집 주소 나머지 |
| HOME_TELEPHONE_NUMBER | 집 전화번호 |
| HOME_FAX_NUMBER | 집 팩스 번호 |
| HOME_ADDRESS_POSTAL_CODE | 집 주소 우편 번호 |
| BUSINESS_ADDRESS_COUNTRY | 직장 주소 국가/지역 |
| BUSINESS_ADDRESS_STATE_OR_PROVINCE| 직장 주소 시/도 |
| BUSINESS_ADDRESS_CITY | 직장 주소 구/군/시 |
| BUSINESS_ADDRESS_STREET | 직장 주소 나머지 |
| BUSINESS_TELEPHONE_NUMBER | 직장 전화 번호 |
| BUSINESS_FAX_NUMBER | 직장 팩스 번호 |
| BUSINESS_ADDRESS_POSTAL_CODE | 직장 주소 우편 번호 |
10.7.2.11.3 XML 예
예제 81. MAILMERGE 예
code
Xml
<fieldBegin id="fb11" type="MAILMERGE" editable="false" dirty="false">
    <parameters count="2">
        <stringParam name="FieldType">WAB</stringParam>
        <stringParam name="FieldValue">SURNAME</stringParam>
    </parameters>
</fieldBegin>
10.7.2.12 MEMO
10.7.2.12.1 MEMO
메모는 현재 편집 중인 문서에서 특정 단어나 블록으로 설정한 문자열에 대한 간단한 추가 내용을 기록하는 기능이다.
10.7.2.12.2 필요한 인자들
표 159—MEMO 요소
| 인자 이름 | 인자 형식 | 설명 |
| :------------- | :------------ | :--------------------------------------------- |
| ID | stringParam | 메모를 식별하기 위한 아이디 |
| Number | integerParam | 메모 번호 |
| CreateDateTime | stringParam | 메모 작성 시각. KS X ISO 8601에 따라 'YYYY-MM-DD hh:mm:ss' 형식 사용 |
| Author | stringParam | 메모 작성자 |
| MemoShapeIDRef | stringParam | 메모 모양 속성 정보 아이디 참조값 |
10.7.2.12.3 XML 예
예제 82. MEMO 예
code
Xml
<fieldBegin id="fb11" type="MEMO" editable="true" dirty="true">
    <parameters count="5">
        <stringParam name="ID">memo1</stringParam>
        <integerParam name="Number">1</integerParam>
        <stringParam name="CreateDateTime">2011-01-01 10:00:00</stringParam>
        <stringParam name="Author">hancom</stringParam>
        <stringParam name="MemoShapeID">memoShape3</stringParam>
    </parameters>
    <subList ...>
        ...
        <t>
            <char>메모 내용</char>
        </t>
        ...
    </subList>
</fieldBegin>
(subList의 상세 내용은 생략)
10.7.2.13 PROOFREADING_MARKS
10.7.2.13.1 PROOFREADING_MARKS
교정 부호는 맞춤법, 띄어쓰기, 글자 크기, 문장 부호, 줄바꿈, 오자, 탈자, 어색한 표현 등을 바로잡기 위하여 특정 부호를 문서 내에 삽입하는 기능이다.
10.7.2.13.2 필요한 인자들
교정 부호 종류가 '메모 고침'인 경우 MEMO 형식에서 사용되는 인자들을 사용한다. 즉, Type, ID, Number, CreateDateTime, Author, MemoShapeIDRef 인자들을 사용한다. Type을 제외한 나머지 인자들에 대한 자세한 설명은 10.7.2.12를 참조한다.
교정 부호 종류가 '자료 연결'인 경우 HYPERLINK 형식에서 사용되는 인자들을 사용한다. 즉, Type, Path, Category, TargetType, DocOpenType 인자들이 사용된다. Type을 제외한 나머지 인자들에 대한 자세한 설명은 10.7.2.3을 참조한다.
표 160 — PROOFREADING_MARKS 요소
| 인자 이름 | 인자 형식 | 설명 |
| :------------------- | :----------- | :----------------------------------------------------------------- |
| Type | stringParam | 교정 부호 종류 |
| ProofreadingContents | stringParam | 교정 내용. 넣음표, 부호 넣음표, 고침표에서 사용됨 |
| MovingMargin | integerParam | 자리 옮김 여백. 오른/왼자리 옮김표에서 사용됨 |
| MovingStart | integerParam | 자리 옮김 시작위치. 오른/왼자리 옮김표에서 사용됨 |
| SplitType | stringParam | '자리 바꿈 나눔표'인지 '줄 서로 바꿈 나눔표'인지 여부. 자리/줄 서로 바꿈 나눔표에서 사용됨 |
교정 부호 종류
표 161 — 교정 부호 종류
| 참조 내용 | 설명 |
| :---------------- | :------------- |
| WORD_SPACING | 띄움표 |
| CONTENT_INSERT | 넣음표 |
| SIGN_INSERT | 부호 넣음표 |
| LINE_SPLIT | 줄 나눔표 |
| LINE_SPACE | 줄 비움표 |
| MEMO_CHANGE | 메모 고침 |
| SIMPLE_CHANGE | 고침표 |
| CLIPPING | 뺌표 |
| DELETE | 지움표 |
| ATTACH | 붙임표 |
| LINE_ATTACH | 줄 붙임표 |
| LINE_LINK | 줄 이음표 |
| SAWTOOTH | 톱니표 |
| THINKING | 생각표 |
| PRAISE | 칭찬표 |
| LINE | 줄표 |
| POSITION_TRANSFER | 자리 바꿈표 |
| LINE_TRANSFER | 줄 서로 바꿈표 |
| TRANSFER_SPLIT | 바꿈 나눔표 |
| RIGHT_MOVE | 오른자리 옮김표|
| LEFT_MOVE | 왼자리 옮김표 |
| LINK_DATA | 자료 연결 |
SplitType
표 162—SplitType 요소
| 참조 내용 | 설명 |
| :-------- | :--------------------- |
| POSITION | 자리 바꿈 나눔표를 지칭|
| LINE | 줄 서로 바꿈 나눔표를 지칭 |
10.7.2.13.3 XML 예
예제 83. PROOFREADING_MARKS 예
code
Xml
<fieldBegin id="fb12" type="PROOFREADING_MARKS" editable="false" dirty="true">
    <parameters count="2">
        <stringParam name="Type">SIMPLE_CHANGE</stringParam>
        <stringParam name="ProofreadingContents">고칠 내용</stringParam>
    </parameters>
</fieldBegin>
10.7.2.14 PRIVATEINFO
10.7.2.14.1 PRIVATEINFO 요소
개인 정보 보호는 현재 화면에서 편집하고 있는 문서 내용 중 사용자가 블록으로 지정한 영역을 암호를 걸어 사용자가 선택한 글자표로 변경하는 기능이다.
10.7.2.14.2 필요한 인자들
표 163— PRIVATEINFO 요소
| 인자 이름 | 인자 형식 | 설명 |
| :------------- | :----------- | :---------------------------------- |
| EncryptMode | stringParam | 암호화 방식 |
| EncryptLength | integerParam | 암호화된 결과의 길이 |
| DecryptLength | integerParam | 복호화한 후의 길이 |
| EncryptString | stringParam | 암호화된 결과를 BASE64로 인코딩한 문자열 |
| MarkChar | stringParam | 암호화된 문자열 대신에 화면에 표시될 문자 |
| Pattern | stringParam | Pattern |
| Type | stringParam | Type |
암호화 방식
표 164— 암호화 방식
| 참조 내용 | 설명 |
| :-------- | :---------------------------------- |
| AES | AES(Advanced Encryption Standard) |
(문서의 흐름상 METADATA, CITATION, BIBLIOGRAPHY 등이 이어지나, 제공된 OCR 텍스트는 순서가 일부 섞여 있습니다. 제공된 텍스트 순서대로 복원합니다.)
예제 85 METADATA 예```xml
<fieldBegin id="fb13" type="METADATA" editable="false" dirty="true">
<parameters count="4">
<stringParam name="ID">103e9eab2c70</stringParam>
<stringParam name="Property">http://www.w3.org/2002/12/cal/cal#dtstart</stringParam>
<stringParam name="Content">2007-09-16T16:00:00-05:00</stringParam>
<stringParam name="Datatype">xsd:dateTime</stringParam>
</parameters>
</fieldBegin>
code
Code
#### **10.7.2.16 CITATION**

**10.7.2.16.1 CITATION**
인용은 연구논문이나 다른 여타의 원본을 인용해야 하는 문서를 작성할 때 사용하는 기능이다. 인용은 다양한 형식의 인용 스타일을 선택하여 적용할 수 있다.

**10.7.2.16.2 필요한 인자**

표 166— CITATION 요소
| 인자 이름 | 인자 형식   | 설명                   |
| :-------- | :---------- | :--------------------- |
| GUID      | stringParam | 인용 고유 번호         |
| Result    | stringParam | 스타일이 적용된 인용 문자열 |

**10.7.2.16.3 XML 예**

예제 86. CITATION 예
```xml
<fieldBegin id="fb13" type="CITATION" editable="false" dirty="true">
    <parameters count="2">
        <stringParam name="GUID">A25C5BE1-391C-4088-9E2C-3E0C521730F1</stringParam>
        <stringParam name="Result">(나연_작가_퍼스트공연_작가_라스트, ... 1948)</stringParam>
    </parameters>
</fieldBegin>
10.7.2.17 BIBLIOGRAPHY
'참고문헌'은 참조한 원본에 대한 출처 정보를 적는 기능이다. 다양한 스타일을 선택하거나 다른 참고문헌 스타일을 적용할 수 있다. 참고문헌에 대한 xml 데이터는 OOXML의 형식을 사용하며 Custom/Bibliography.xml에 기입된다. 해당 데이터는 참고문헌 스타일에 의해 표현된다.
10.7.2.17.1 필요한 인자들
표 167—BIBLIOGRAPHY 요소
| 인자 이름 | 인자 형식 | 설명 |
| :------------ | :---------- | :--------------- |
| StyleName | stringParam | 참고문헌 스타일 |
| StyleVersion | stringParam | 참고문헌 스타일 버전 |
10.7.2.17.2 XML 예
예제 87. BIBLIOGRAPHY 예
code
Xml
<fieldBegin id="fb13" type="BIBLIOGRAPHY" editable="false" dirty="true">
    <parameters count="2">
        <stringParam name="StyleName">APA</stringParam>
        <stringParam name="StyleVersion">6</stringParam>
    </parameters>
</fieldBegin>
10.7.2.18 METATAG
메타태그는 본문의 메타 정보를 ...
예제 88. METATAG 예
code
Xml
<fieldBegin id="fb13" type="METATAG" editable="false" dirty="true" zorder="7">
    <hp:metaTag name="#내 화면"/>
</fieldBegin>
10.7.3 fieldEnd 요소
<fieldBegin> 요소와 쌍을 이루는 요소이다.
표 168 —fieldEnd 요소
| 속성 이름 | 설명 |
| :---------- | :--------------- |
| beginIDRef | 시작 아이디 참조값 |
| fieldId | 필드 개체 아이디 |
예제 89. fieldEnd 예
code
Xml
<hp:fieldEnd beginIDRef="1790845288" fieldId="623209829"/>
10.7.4 bookmark 요소
필드에서 사용되는 책갈피와는 다른 구조를 가지는 책갈피를 표현하기 위한 요소이다. 필드의 책갈피는 지정된 구역에 책갈피 표시를 하지만, <bookmark> 요소를 사용한 책갈피는 지정된 구역을 가지지 않고 단순히 지정된 위치에 책갈피 표시를 한다.
표 169 — bookmark 요소
| 속성 이름 | 설명 |
| :-------- | :--------- |
| name | 책갈피 이름 |
예제 90. bookmark 예
code
Xml
<hp:bookmark name="책갈피"/>
10.7.5 머리말/꼬리말 요소 형식
표 170—HeaderFooterType 요소
| 속성 이름 | 설명 |
| :------------ | :----------------------------------------- |
| id | 머리말/꼬리말을 식별하기 위한 아이디 |
| applyPageType | 머리말/꼬리말이 적용될 페이지 형식. BOTH: 양쪽, EVEN: 짝수쪽, ODD: 홀수쪽 |
표 171 — HeaderFooterType 하위 요소
| 하위 요소 이름 | 설명 |
| :------------- | :------------- |
| subList | 머리말/꼬리말 내용 |
예제 91. HeaderFooterType 예
code
Xml
<hp:footer id="-9" applyPageType="BOTH">
    <hp:subList ...>
        ...
        <hp:run charPrIDRef="7">
            ...
            <hp:ctrl>
                <hp:fieldBegin id="1790879954" type="PATH" name="" editable="0" dirty="0" zorder="7" fieldId="-628121972" metaTag="">
                    <hp:parameters cnt="3" name="">
                        <hp:integerParam name="Prop">8</hp:integerParam>
                        <hp:stringParam name="Command">$F</hp:stringParam>
                        <hp:stringParam name="Format">$F</hp:stringParam>
                    </hp:parameters>
                </hp:fieldBegin>
            </hp:ctrl>
            <hp:t>테스트 문서입니다.owpml</hp:t>
            <hp:ctrl>
                <hp:fieldEnd beginIDRef="1790879954" fieldId="-628121971"/>
            </hp:ctrl>
            ...
        </hp:run>
        ...
    </hp:subList>
</hp:footer>
(XML 일부 내용 생략)
10.7.6 각주/미주 요소 형식
각주 및 미주를 표현하기 위한 요소 형식이다.
표 172—NoteType 요소
| 속성 이름 | 설명 |
| :-------- | :----------------------------- |
| id | 각주/미주를 식별하기 위한 아이디 |
표 173 — NoteType 하위 요소
| 하위 요소 이름 | 설명 |
| :------------- | :--------- |
| subList | 각주/미주 내용 |
예제 92. NoteType 예```xml
<hp:footNote instId="183252349">
<hp:subList id="..." textDirection="HORIZONTAL" lineWrap="BREAK" vertAlign="TOP" ...>
<hp:p id="0" paraPrIDRef="10" styleIDRef="14" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="8">
hp:ctrl
<hp:autoNum num="1" numType="FOOTNOTE">
<hp:autoNumFormat type="DIGIT" userChar="" prefixChar="" suffixChar=")" supscript="0"/>
</hp:autoNum>
</hp:ctrl>
hp:t </hp:t>
</hp:run>
</hp:p>
</hp:subList>
</hp:footNote>
code
Code
#### **10.7.7 자동/새 번호 요소 형식**
자동 번호 및 새 번호를 표현하기 위한 요소 형식이다.

표 174 — AutoNumNewNumType 요소
| 속성 이름 | 설명     |
| :-------- | :------- |
| num       | 번호     |
| numType   | 번호의 종류 |

표 175 — AutoNumNewNumType 하위 요소
*(주: OCR된 문서에서 표 175의 내용이 유실되었습니다.)*

예제 93. AutoNumNewNumType 예
```xml
<hp:autoNum num="1" numType="PAGE">
    <hp:autoNumFormat type="DIGIT" userChar="" prefixChar="" suffixChar="" supscript="0"/>
</hp:autoNum>
10.7.8 pageNumCtrl 요소
쪽 번호를 홀수쪽, 짝수쪽 또는 양쪽 모두에 표시할지를 설정하기 위한 요소이다.
표 176 — pageNumCtrl 요소
| 속성 이름 | 설명 |
| :------------ | :--------- |
| pageStartsOn | 홀/짝수 구분 |
10.7.9 pageHiding 요소
현재 구역 내에서 감추어야 할 것들을 설정하기 위한 요소이다.
표 177 — pageHiding 요소
| 속성 이름 | 설명 |
| :------------- | :--------------- |
| hideHeader | 머리말 감추기 여부 |
| hideFooter | 꼬리말 감추기 여부 |
| hideMasterPage | 바탕쪽 감추기 여부 |
| hideBorder | 테두리 감추기 여부 |
| hideFill | 배경 감추기 여부 |
| hidePageNum | 쪽 번호 감추기 여부|
예제 94. pageHiding 예
code
Xml
<hp:pageHiding hideHeader="0" hideFooter="0" hideMasterPage="0" hideBorder="0" hideFill="0" hidePageNum="0"/>
10.7.10 pageNum 요소
쪽 번호의 위치 및 모양을 설정하기 위한 요소이다.
표 178 — pageNum 요소
| 속성 이름 | 설명 |
| :--------- | :--------- |
| pos | 번호 위치 |
| formatType | 번호 모양 종류 |
| sideChar | 줄표 넣기 |
예제 95. pageNum 예
code
Xml
<hp:pageNum pos="BOTTOM_CENTER" formatType="DIGIT" sideChar="-"/>
10.7.11 indexmark 요소
<indexmark>는 찾아보기(Index, 색인)와 관련된 정보를 갖고 있는 요소이다.
표 179 —indexmark 요소
| 하위 요소 이름 | 설명 |
| :------------- | :---------------------------------------------------------------------- |
| firstKey | 찾아보기에 사용할 첫 번째 키워드. 요소의 값으로 키워드 문자열을 가짐. |
| secondKey | 찾아보기에 사용할 두 번째 키워드. 요소의 값으로 키워드 문자열을 가짐. |
예제 96. indexmark 예
code
Xml
<hp:indexmark>
    <hp:firstKey>aa</hp:firstKey>
    <hp:secondKey>aa</hp:secondKey>
</hp:indexmark>
10.7.12 hiddenComment 요소
<hiddenComment>는 숨은 설명을...
표 180 — hiddenComment 요소
| 하위 요소 이름 | 설명 |
| :------------- | :--------------- |
| subList | 숨은 설명 내용 (10.1.1 참조) |
예제 97. hiddenComment 예
code
Xml
<hp:hiddenComment>
    <hp:subList ...>
        <hp:p ...>
            <hp:run charPrIDRef="6">
                <hp:t>
                    <hp:insertBegin id="55" TcId="19"/>
                    숨은 설명입니다.
                    <hp:insertEnd id="55" TcId="19" paraend="0"/>
                </hp:t>
            </hp:run>
            ...
        </hp:p>
    </hp:subList>
</hp:hiddenComment>
(10.8.1) t 요소
표 182 — t 하위 요소
| 하위 요소 이름 | 설명 |
| :-------------- | :---------------------------------- |
| {요소 값} | 글자 |
| markpenBegin | 형광펜 시작 |
| markpenEnd | 형광펜 끝 |
| titleMark | 제목 차례 표시 |
| tab | 탭. 하위 속성 있음. |
| lineBreak | 강제 줄 나눔 |
| hyphen | 하이픈 |
| nbSpace | 묶음 빈칸 |
| fwSpace | 고정폭 빈칸 |
| insertBegin | 변경 추적 삽입 시작지점 |
| insertEnd | 변경 추적 삽입 끝지점 |
| deleteBegin | 변경 추적 삭제 시작지점 |
| deleteEnd | 변경 추적 삭제 끝지점 |
10.8.2 markpenBegin 요소
형광펜 색상 정보를 담고 있는 요소이다.
표 183 —markpenBegin 요소
| 속성 이름 | 설명 |
| :--------- | :--------- |
| beginColor | 형광펜 색상 |
예제 98. markpenBegin 예
code
Xml
<hp:markpenBegin color="#FFFF0000"/>
sampletext
<hp:markpenEnd/>
(10.8.3 titleMark 요소)
(주: 문서 번호는 유실되었으나 표 182의 내용에 근거하여 복원)
표 184 —titleMark 요소
| 속성 이름 | 설명 |
| :-------- | :------------------------------------------ |
| ignore | 제목 차례 표시 여부. true: 차례 만들기 무시 |
10.8.4 tab 요소
표 185— tab 요소
| 속성 이름 | 설명 |
| :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| width | 탭의 간격 |
| leader | 탭의 채움모양 (LineType 참조) |
| type | 탭 종류. LEFT: 왼쪽 정렬 탭, RIGHT: 오른쪽 정렬 탭, CENTER: 가운데 정렬 탭, DECIMAL: 소수점 정렬 탭 |
예제 99. tab 예
code
Xml
<hp:tab width="31188" leader="0" type="2"/>
10.8.5 변경 추적 요소 형식
<insertBegin>, <insertEnd>, <deleteBegin>, <deleteEnd> 요소는 [TrackChangeTag] 형식을 기본으로 하며, [TrackChangeTag]는 변경 추적 정보를 정의한 형식이다.
표 186 —TrackChangeTag 요소
| 속성 이름 | 설명 |
| :-------- | :----------------------- |
| id | 변경 추적을 식별하기 위한 아이디 |
| TcId | 변경 추적 아이디 참조값 |
| paraend | 문단 끝 포함 여부 |
예제 100. TrackChangeTag 예
code
Xml
<hp:run charPrIDRef="1">
    <hp:t>
        프로그램입니다.
        <hp:insertBegin id="1" TcId="7"/>
        <hp:insertEnd id="1" TcId="7" paraend="1"/>
    </hp:t>
</hp:run>
10.9 기본 도형 객체
10.9.1 도형 객체
기본 도형 객체는 표, 그림, 수식, 컨테이너와 같은 문서 내에서 텍스트 이외의 기본적인 객체들을 뜻한다. 기본 도형 객체들은 [AbstractShapeObjectType]을 기본 형식(base type)으로 가진다.
10.9.2 AbstractShapeObjectType
10.9.2.1 AbstractShapeObjectType
[AbstractShapeObjectType]은 기본 도형 객체들의 공통된 속성을 정의한 형식이다. 기본 도형 객체들은 [AbstractShapeObjectType]을 기본 형식으로 가지고 추가적으로 필요한 속성이나 요소를 확장해서 사용한다. [AbstractShapeObjectType]은 추상 형식이므로 이것만으로는 XML 요소를 생성할 수 없다.
표 187 — AbstractShapeObjectType 요소
| 속성 이름 | 설명 |
| :------------ | :-------------------------------------------------------------------------------------------------- |
| id | 객체를 식별하기 위한 아이디 |
| zOrder | z-order |
| numberingType | |
| textWrap | ... 하위 요소 pos의 속성 중 treatAsChar가 'false'일 때에만 사용. |
| textFlow | 오브젝트의 좌우 어느 쪽에 글을 배치할지 정하는 옵션. textWrap 속성이 "SQUARE" 또는 "TIGHT" 또는 "THROUGH"일 때에만 사용. |
| lock | 객체 선택 가능 여부 |
| dropcapStyle | 첫 글자 장식 스타일. None: 없음, DoubleLine: 2줄, TripleLine: 3줄, Margin: 여백 |
표 188 — AbstractShapeObjectType 하위 요소
| 하위 요소 이름 | 설명 |
| :------------- | :----------------- |
| sz | 크기 정보 |
| pos | 위치 정보 |
| outMargin | 바깥 여백 |
| caption | 캡션 |
| shapeComment | ... |
| metaTag | 메타태그 관련 정보 |
예제 101. AbstractShapeObjectType 예
code
Xml
<hp:rect id="1790879982" zOrder="1" numberingType="PICTURE" textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="0" dropcapStyle="None">
10.9.2.2 객체 크기 정보
객체들의 크기 정보를 가지고 있는 요소이다.
(주: OCR된 문서에서 sz 요소에 대한 설명이 누락되었습니다.)
10.9.2.3 객체 위치 정보
표 190 —pos 요소
| 속성 이름 | 설명 |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| treatAsChar | 글자처럼 취급 여부 |
| affectLSpacing | 줄 간격에 영향을 줄지 여부. treatAsChar가 true일 때만 의미 있음. |
| flowWithText | 오브젝트의 세로 위치를 본문 영역으로 제한할지 여부. 하위 요소 RelativeTo의 속성 중 vertical이 'PARA'일 때에만 사용. |
| allowOverlap | 다른 오브젝트와 겹치는 것을 허용할지 여부. treatAsChar 속성이 'false'일 때에만 사용. flowWithText 속성이 'true'이면 무조건 'false'로 간주함. |
| holdAnchorAndSO | 객체와 조판부호를 항상 같은 쪽에 놓을지 여부 |
| vertRelTo | 세로 위치의 기준. treatAsChar 속성이 'false'일 때에만 사용. |
| horzRelTo | 가로 위치의 기준. treatAsChar 속성이 'false'일 때에만 사용. |
| vertAlign | vertRelTo에 대한 상대적인 배치 방식. vertRelTo의 값에 따라 가능한 범위가 제한됨. TOP/CENTER/BOTTOM (vertRelTo="PAPER/PAGE/PARA"), INSIDE/OUTSIDE (vertRelTo="PAPER/PAGE") |
| horzAlign | horzRelTo에 대한 상대적인 배치 방식. |
| vertOffset | vertRelTo와 vertAlign을 기준으로 한 상대적인 오프셋 값. 단위는 HWPUNIT. |
| horzOffset | horzRelTo와 horzAlign을 기준으로 한 상대적인 오프셋 값. 단위는 HWPUNIT. |
예제 102. pos 예
code
Xml
<hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="0" allowOverlap="1" holdAnchorAndSO="0" vertRelTo="PAPER" horzRelTo="PAPER" vertAlign="TOP" horzAlign="LEFT" vertOffset="9579" horzOffset="9827"/>
10.9.2.4 객체 바깥 여백
<outMargin> 요소는 [MarginAttributeGroup]을 속성으로 포함한다. [MarginAttributeGroup]은 10.6.6.2를 참조한다.
표 191—outMargin 요소
| 속성 이름 | 설명 |
| :-------------------- | :------------- |
| [MarginAttributeGroup]| 10.6.6.2 참조 |
예제 103. outMargin 예
code
Xml
<hp:outMargin left="0" right="0" top="0" bottom="0"/>
10.9.2.5 캡션
<caption> 요소는 하위 요소로 <subList> 요소를 가진다. <subList> 요소는 11.1.2를 참조한다.
표 192 — caption 요소
| 속성 이름 | 설명 |
| :-------- | :----------------------------- |
| side | ... |
| fullSize | 캡션 폭에 마진을 포함할지 여부 |
| width | 캡션 폭 |
| gap | 캡션과 틀 사이의 간격 |
| lastWidth | 텍스트 최대 길이 (=객체의 폭) |
표 193 — caption 하위 요소
| 하위 요소 이름 | 설명 |
| :------------- | :------------------- |
| subList | 캡션 내용 (11.1.2 참조) |
예제 104. caption 예
code
Xml
<hp:caption side="BOTTOM" fullSz="0" width="8504" gap="850" lastWidth="10000">
    <hp:subList ...>
        <hp:p ...>
            <hp:run charPrIDRef="0">
                <hp:t>그림 </hp:t>
                <hp:ctrl>
                    <hp:autoNum num="1" numType="PICTURE">
                        <hp:autoNumFormat type="DIGIT" userChar="" prefixChar="" suffixChar="" supscript="0"/>
                    </hp:autoNum>
                </hp:ctrl>
                <hp:t> </hp:t>
            </hp:run>
        </hp:p>
    </hp:subList>
</hp:caption>
10.9.3 tbl 요소
10.9.3.1 tbl
<tbl> 요소는 표에 관한 정보를 가지고 있는 요소로 [AbstractShapeObjectType]을 상속받는다. [AbstractShapeObjectType]의 자세한 내용은 10.9.2를 참조한다.
표 194_tbl 요소
| 속성 이름 | 설명 |
| :-------------- | :--------------------------------------------------------------------- |
| pageBreak | 표가 페이지 경계에서 나뉘는 방식. TABLE: 표는 나뉘지만 셀은 나뉘지 않음. CELL: 셀 내의 텍스트도 나뉨. NONE: 나뉘지 않음. |
| repeatHeader | 표가 나뉘었을 경우, 제목 행을 나뉜 페이지에서도 반복할지 여부 |
| rowCnt | 표의 행 개수 |
| colCnt | 표의 열 개수 |
| cellSpacing | 셀 간격. 단위는 HWPUNIT. |
| borderFillIDRef | 테두리/배경 아이디 참조값 |
| noAdjust | 셀 너비/높이 값의 최소 단위(1pt) 보정 여부 |
표 195 —tbl 하위 요소
| 하위 요소 이름 | 설명 |
| :------------- | :----------- |
| inMargin | 안쪽 여백 |
| cellzoneList | 셀존 목록 |
| tr | 행 |
| label | 레이블 |
예제 105. tbl 예
code
Xml
<hp:tbl id="1811647054" zOrder="0" numberingType="TABLE" textWrap="TOP_AND_BOTTOM" textFlow="BOTH_SIDES" lock="0" dropcapStyle="None" pageBreak="CELL" repeatHeader="1" rowCnt="5" colCnt="5" cellSpacing="0" borderFillIDRef="3" noAdjust="0">
    <hp:sz width="41950" widthRelTo="ABSOLUTE" height="6410" heightRelTo="ABSOLUTE" protect="0"/>
    <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="COLUMN" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/>
    <hp:outMargin left="283" right="283" top="283" bottom="283"/>
    <hp:inMargin left="510" right="510" top="141" bottom="141"/>
    ...
</hp:tbl>
10.9.3.2 inMargin 요소
<inMargin> 요소는 안쪽 여백 정보로 [MarginAttributeGroup] 속성을 포함한다. [MarginAttributeGroup]은 10.6.6.2를 참조한다.
표 196 —inMargin 요소
| 속성 이름 | 설명 |
| :-------------------- | :------------- |
| [MarginAttributeGroup]| 10.6.6.2 참조 |
예제 106. inMargin 예
code
Xml
<hp:inMargin left="510" right="510" top="141" bottom="141"/>
10.9.3.3 cellzoneList 요소
10.9.3.3.1 cellzoneList
표는 표 전체 또는 표 부분적으로 배경색 및 테두리와 같은 속성을 줄 때, 영역을 지정하기 위해서 <cellzone> 요소를 사용한다.
표 197 —cellzoneList 하위 요소
| 하위 요소 이름 | 설명 |
| :------------- | :----- |
| cellzone | 셀존 |
10.9.3.3.2 cellzone 요소
Cell zone은 표에서 스타일 및 모양이 적용되는 단위이다.
표 198 — cellzone 요소
| 속성 이름 | 설명 |
| :-------------- | :--------------------------------- |
| startRowAddr | 셀존 row의 시작 주소 (0부터 시작) |
| startColAddr | 셀존 column의 시작 주소 (0부터 시작) |
| endRowAddr | 셀존 row의 끝 주소 (0부터 시작) |
| endColAddr | 셀존 column의 끝 주소 (0부터 시작) |
| borderFillIDRef | 테두리/배경 아이디 참조값 |
10.9.3.4 tr 요소
표에서 하나의 행을 표현한다.
(주: OCR된 문서에서 tc 요소에 대한 설명이 tr 요소 설명에 포함되어 있습니다. 분리하여 정리합니다.)
tc 요소 (셀)
표 201— tc 요소
| 속성 이름 | 설명 |
| :-------------- | :-------------------------- |
| name | ... |
| header | 제목 셀 여부 |
| hasMargin | ... |
| protect | 셀 보호 여부 |
| editable | 편집 가능 여부 |
| dirty | ... |
| borderFillIDRef | 테두리/배경 아이디 참조값 |
| cellAddr | 셀 주소 |
| cellSpan | 셀 병합 정보 |
| cellSz | 셀 크기 |
| cellMargin | 셀 여백 |
예제 108. tc 예```xml
<hp:tc name="" header="0" hasMargin="0" protect="0" editable="0" dirty="0" borderFillIDRef="4">
<hp:subList ...> ... </hp:subList>
<hp:cellAddr colAddr="4" rowAddr="0"/>
<hp:cellSpan colSpan="1" rowSpan="1"/>
<hp:cellSz width="8390" height="282"/>
<hp:cellMargin left="510" right="510" top="141" bottom="141"/>
</hp:tc>
code
Code
*   **셀 주소**

표 202 —cellAddr 요소
| 속성 이름 | 설명                                                   |
| :-------- | :----------------------------------------------------- |
| colAddr   | 셀의 열 주소. 0부터 시작하며 오른쪽으로 1씩 증가.      |
| rowAddr   | 셀의 행 주소. 0부터 시작하며 아래쪽으로 1씩 증가.      |

예제 109. cellAddr 예
```xml
<hp:cellAddr colAddr="3" rowAddr="0"/>
셀 병합 정보
표 203 —cellSpan 요소
| 속성 이름 | 설명 |
| :-------- | :--------- |
| colSpan | 열 병합 개수 |
| rowSpan | 행 병합 개수 |
예제 110. cellSpan 예
code
Xml
<hp:cellSpan colSpan="1" rowSpan="1"/>
셀 크기
표 204 — cellSz 요소
| 하위 요소 이름 | 설명 |
| :------------- | :--------------------- |
| width | 셀의 폭. 단위는 HWPUNIT. |
| height | 셀의 높이. 단위는 HWPUNIT. |
예제 111. cellSz 예
code
Xml
<hp:cellSz width="8390" height="282"/>
셀 여백
표 205—cellMargin 요소
| 속성 이름 | 설명 |
| :-------------------- | :------------- |
| [MarginAttributeGroup]| 10.6.6.2 참조 |
예제 112. cellMargin 예
code
Xml
<hp:cellMargin left="510" right="510" top="141" bottom="141"/>
10.9.3.5 Label 요소
표 206 —label 요소
| 속성 이름 | 설명 |
| :----------- | :------------- |
| topmargin | 용지 위쪽 여백 |
| leftmargin | 용지 왼쪽 여백 |
| boxwidth | 이름표 폭 |
| boxlength | 이름표 길이 |
| boxmarginhor | 이름표 좌우 여백 |
| boxmarginver | 이름표 상하 여백 |
| labelcols | 이름표 열의 개수 |
| labelrows | 이름표 행의 개수 |
| landscape | 용지 방향 |
| pagewidth | 문서의 폭 |
| pageheight | 문서의 길이 |
예제 113. label 예
code
Xml
<hp:label topmargin="1332" leftmargin="1532" boxwidth="56692" boxlength="81936" boxmarginhor="0" boxmarginver="0" labelcols="1" labelrows="1" landscape="WIDELY" pagewidth="59528" pageheight="84188"/>```

#### **10.9.4 equation 요소**
`<equation>` 요소는 [AbstractShapeObjectType]을 상속받는다. [AbstractShapeObjectType]의 자세한 내용은 10.9.2를 참조한다.

표 207 — equation 요소
| 속성 이름   | 설명                                   |
| :---------- | :------------------------------------- |
| version     | ...                                    |
| baseLine    | 수식이 그려질 기본 선                  |
| textColor   | 수식 글자 색                           |
| baseUnit    | 수식의 글자 크기. 단위는 HWPUNIT.      |
| lineMode    | 수식이 차지하는 범위                   |
| font        | 수식 폰트. Default font: 'HYhwpEQ' |

표 208 — equation 하위 요소
| 하위 요소 이름 | 설명                                       |
| :------------- | :----------------------------------------- |
| script         | 수식 내용. 자세한 내용은 부속서의 수식 스크립트 참조 |

예제 114. equation 예
```xml
<hp:equation id="1806018078" zOrder="2" numberingType="EQUATION" textWrap="TOP_AND_BOTTOM" textFlow="BOTH_SIDES" lock="0" dropcapStyle="None" version="Equation Version 60" baseLine="66" textColor="#000000" baseUnit="1000" lineMode="CHAR" font="HancomEQN">
(10.9.5) AbstractShapeComponentType
(주: 문서 번호는 유실되었으나 내용의 흐름에 따라 10.9.5로 복원)
표 209 — AbstractShapeComponentType 요소
| 속성 이름 | 설명 |
| :----------- | :--------------- |
| href | 하이퍼링크 속성 |
| groupLevel | ... |
| instid | 객체 아이디 |
표 210 — AbstractShapeComponentType 하위 요소
| 하위 요소 이름 | 설명 |
| :------------- | :----------------------------- |
| offset | 객체가 속한 그룹 내에서의 오프셋 정보 |
| orgSz | 객체 생성 시 최초 크기 |
| curSz | 객체의 현재 크기 |
| flip | 객체가 뒤집어진 상태인지 여부 |
| rotationInfo | 객체 회전 정보 |
| renderingInfo | 객체 렌더링 정보 |
예제 115. AbstractShapeComponentType 예
code
Xml
<hp:rect id="1833429566" zOrder="3" numberingType="PICTURE" textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="0" dropcapStyle="None" href="" groupLevel="0" instid="752...43" ratio="0">
    <hp:offset x="0" y="0"/>
    <hp:orgSz width="16800" height="12825"/>
    <hp:curSz width="16800" height="12825"/>
    <hp:flip horizontal="0" vertical="0"/>
    <hp:rotationInfo angle="0" centerX="8400" centerY="6412" rotateimage="1"/>
    <hp:renderingInfo>
        <hp:transMatrix e1="..." e2="..." e3="..." e4="..." e5="..." e6="..."/>
        <hp:scaMatrix e1="..." e2="..." e3="..." e4="..." e5="..." e6="..."/>
        <hp:rotMatrix e1="..." e2="..." e3="..." e4="..." e5="..." e6="..."/>
    </hp:renderingInfo>
</hp:rect>
(행렬 값은 생략)
10.9.5.2 객체가 속한 그룹 내에서의 오프셋 정보
그룹 객체 내에서 개별 객체들의 그룹 내 상대 위치 정보를 가지고 있는 요소이다.
표 211 — offset 요소
| 속성 이름 | 설명 |
| :-------- | :------------------------------- |
| x | 객체가 속한 그룹 내에서의 x offset |
| y | 객체가 속한 그룹 내에서의 y offset |
예제 116. offset 예
code
Xml
<hp:offset x="0" y="0"/>
10.9.5.3 객체 생성 시 최초 크기
객체 생성 시 최초 크기 정보를 가지고 있는 요소이다.
표 212 —orgSz 요소
| 속성 이름 | 설명 |
| :-------- | :----------------------------------- |
| width | 객체 생성 시 최초 폭. 단위는 HWPUNIT. |
| height | 객체 생성 시 최초 높이. 단위는 HWPUNIT. |
예제 117. orgSz 예
code
Xml
<hp:orgSz width="16800" height="12825"/>
10.9.5.4 객체의 현재 크기
객체의 현재 크기 정보를 가지고 있는 요소이다.
표 213 —curSz 요소
| 속성 이름 | 설명 |
| :-------- | :------------------------------- |
| width | 객체의 현재 폭. 단위는 HWPUNIT. |
| height | 객체의 현재 높이. 단위는 HWPUNIT. |
예제 118. curSz 예
code
Xml
<hp:curSz width="12500" height="5000"/>
10.9.5.5 객체가 뒤집어진 상태인지 여부
객체의 반전 여부 정보를...
표 214 —flip 요소
| 속성 이름 | 설명 |
| :--------- | :------------------------- |
| horizontal | 좌우로 뒤집어진 상태인지 여부 |
| vertical | 상하로 뒤집어진 상태인지 여부 |
예제 119. flip 예
code
Xml
<hp:flip horizontal="1" vertical="1"/>
10.9.5.6 객체 회전 정보
객체의 회전 정보를 가지고 있는 요소이다.
표 215—rotationInfo 요소
| 속성 이름 | 설명 |
| :---------- | :------------- |
| angle | 회전각 |
| centerX | 회전 중심의 x 좌표 |
| centerY | 회전 중심의 y 좌표 |
| rotateimage | 이미지 회전 여부 |
예제 120. rotationinfo 예
code
Xml
<hp:rotationInfo angle="0" centerX="6250" centerY="2500" rotateimage="1"/>
10.9.5.7 객체 렌더링 정보
10.9.5.7.1 객체 렌더링
객체 렌더링 시 필요한, 변환 행렬, 확대/축소 행렬, 회전 행렬을 가지고 있는 요소이다.