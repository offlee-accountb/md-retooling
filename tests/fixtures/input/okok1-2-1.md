10.7.2.2 CLICK_HERE
누름틀은 문서마당을 불러왔을 때 화면에 표시된 문서마당의 빈 곳을 채워 넣을 안내문과 안내문에 대한 간단한 메모 내용을 입력하는 기능이다.
10.7.2.2.1 필요한 인자들
표 133 — CLICK_HERE 요소
인자 이름	인자 형식	설명
Direction	stringParam	안내문 문자열
HelpState	stringParam	안내문 도움말
샘플 72 — CLICK_HERE 예
code
Xml
<fieldBegin id="fb01" type="CLICK_HERE" name="title" editable="true" dirty="false">
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
표 134 — HYPERLINK 요소
인자 이름	인자 형식	설명
Path	stringParam	링크 경로
Category	stringParam	하이퍼링크의 종류
TargetType	stringParam	하이퍼링크의 종류가 한글 문서인 경우, 한글 문서에서 대상의 종류
DocOpenType	stringParam	이동 시 문서창 옵션
하이퍼링크의 종류
표 135 — 하이퍼링크 종류
| 하이퍼링크 종류 | 설명 |
| :--- | :--- |
| HWPHYPERLINK_TYPE_DONTCARE | 여러 개체가 섞여 그룹으로 지정된 설정에서 하이퍼링크 종류가 다른 경우 |
| HWPHYPERLINK_TYPE_HWP | HWP 문서 내부의 책갈피 |
| HWPHYPERLINK_TYPE_URL | 웹 주소 |
| HWPHYPERLINK_TYPE_EMAIL | 메일 주소 |
| HWPHYPERLINK_TYPE_EXT | 외부 애플리케이션 문서 |
HWP 문서에서 대상의 종류
표 136 — 대상의 종류
| HWP 문서에서 대상의 종류 | 설명 |
| :--- | :--- |
| HWPHYPERLINK_TARGET_DOCUMENT_DONTCARE | 동일 그룹 객체 내의 개별 객체들의 하이퍼링크 설정에서 연결 문서가 다른 경우 |
| HWPHYPERLINK_TARGET_OBJECT_DONTCARE | 동일 그룹 객체 내의 개별 객체들의 하이퍼링크 설정에서 참조 내용이 다른 경우 |
| HWPHYPERLINK_TARGET_BOOKMARK | 책갈피 |
| HWPHYPERLINK_TARGET_OUTLINE | 개요 |
| HWPHYPERLINK_TARGET_TABLE | 표 |
| HWPHYPERLINK_TARGET_FIGURE | 그림, 그리기 객체 |
| HWPHYPERLINK_TARGET_EQUATION | 수식 |
| HWPHYPERLINK_TARGET_HYPERLINK | 하이퍼링크 |
이동 시 문서창 옵션
표 137 — 문서창 옵션
| 이동 시 문서창 옵션 종류 | 설명 |
| :--- | :--- |
| HWPHYPERLINK_JUMP_DONTCARE | 동일 그룹 객체 내의 개별 객체들의 하이퍼링크 설정에서 문서창 옵션 종류가 다른 경우 |
| HWPHYPERLINK_JUMP_CURRENTTAB | 현재 문서 탭에서 열기 |
| HWPHYPERLINK_JUMP_NEWTAB | 새로운 문서 탭에서 열기 |
| HWPHYPERLINK_JUMP_NEWWINDOW | 새로운 문서 창에서 열기 |
샘플 73 — HYPERLINK 예
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
두꺼운 책을 읽을 때 책의 중간에 책갈피를 꽂아 두고 필요할 때마다 쉽게 펴보듯이, [책갈피] 기능은 문서를 편집하는 도중에 본문의 여러 곳에 표시를 해 두었다가 현재 커서의 위치에 상관없이 표시해 둔 곳으로 커서를 곧바로 이동시키는 기능이다.
10.7.2.4.2 XML 예
샘플 74 — BOOKMARK 예
code
Xml
<fieldBegin id="fb03" type="BOOKMARK" name="txn01" editable="false" dirty="false"/>
10.7.2.5 FORMULA
10.7.2.5.1 FORMULA
표 계산식은 표에서 덧셈, 뺄셈, 곱셈, 나눗셈과 같은 사칙연산은 물론 sum과 avg와 같은 간단한 함수를 이용하여 계산하는 기능이다.
10.7.2.5.2 필요한 인자들
표 138 — FORMULA 요소
인자 이름	인자 형식	설명
FunctionName	stringParam	계산식 함수 이름
FunctionArguments	listParam	계산식에 필요한 인자들
ResultFormat	stringParam	결과 출력 형식
LastResult	stringParam	마지막으로 계산된 결과
함수 목록
표 139 — FORMULA 함수 목록
| 함수 종류 | 설명 |
| :--- | :--- |
| SUM | 지정한 범위의 셀들에 대한 합을 계산 |
| AVG | 지정한 범위의 셀들에 대한 평균을 계산 |
| PRODUCT | 지정한 범위의 셀들에 대한 곱을 계산 |
| MIN | 지정한 범위의 셀들 중 최소값을 찾음 |
| MAX | 지정한 범위의 셀들 중 최대값을 찾음 |
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
| ABS | 하나의 셀에 대한 절댓값을 계산 |
| INT | 하나의 셀에 대하여 소수점을 무시하고 정수 값만을 계산 |
| SIGN | 하나의 셀에 대하여 양수 값이면 1, 0이면 0, 음수 값이면 -1을 계산 |
| CEILING | 하나의 셀에 대하여 크거나 같은 최소 정수를 계산 |
| FLOOR | 하나의 셀에 대하여 작거나 같은 최대 정수를 계산 |
| EXP | 하나의 셀에 대한 자연 지수 e의 거듭 제곱 값을 계산 |
| LN | 하나의 셀에 대한 자연 로그 값(밑이 자연 지수 e인 로그 값)을 계산 |
| LOG | 하나의 셀에 대한 상용 로그 값(밑이 10인 로그 값)을 계산 |
함수 인자
표 140 — FORMULA 함수 인자
| 함수 인자 형태 | 설명 |
| :--- | :--- |
| LEFT | 현재 셀 왼쪽의 모든 셀 |
| RIGHT | 현재 셀 오른쪽의 모든 셀 |
| ABOVE | 현재 셀 위쪽의 모든 셀 |
| BELOW | 현재 셀 아래쪽의 모든 셀 |
| 셀 주소 | A1, B2 등과 같은 셀의 주소. 셀 주소와 LEFT, RIGHT, ABOVE, BELOW는 혼합해서 사용할 수 없음 |
결과 출력 형식
표 142 — 결과 출력 형식
| 결과 출력 형식 | 설명 |
| :--- | :--- |
| %g | 기본 형식 |
| %.0f | 정수형 |
| %.1f | 소수점 이하 1자리까지만 표시 |
| %.2f | 소수점 이하 2자리까지만 표시 |
| %.3f | 소수점 이하 3자리까지만 표시 |
| %.4f | 소수점 이하 4자리까지만 표시 |
10.7.2.5.3 XML 예
샘플 75 — FORMULA 예
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
표 143 — DATE 요소
인자 이름	인자 형식	설명
DateNation	stringParam	국가 코드
DateFormat	stringParam	날짜/시간 표시 형식
국가 코드
표 144 — 국가 코드
| 국가 코드 | 설명 |
| :--- | :--- |
| KOR | 대한민국 |
| USA | 미국 |
| JPN | 일본 |
| CHN | 중국 |
| TWN | 대만 |
날짜/시간 표시 기호
표 145 — 날짜/시간 표시 기호
| 날짜/시간 표시 기호 | 설명 |
| :--- | :--- |
| Y | 연(year) 요소를 표현 |
| M | 월(month) 요소를 표현 (M: 1, MM: 01, MMM: Jan, MMMM: January) |
| D | 일(day) 요소를 표현 |
| W | 주(week) 요소를 표현 (해당 연도에서 몇 번째 주인지 숫자로 표현) |
| h | 시(hour) 요소를 표현 (24시간제, 0-23) |
| m | 분(minute) 요소를 표현 |
| s | 초(second) 요소를 표현 |
| E | 확장 요소, 요일(day of the week) 요소를 표현. 국가 코드에 따라 다름 (예: 월/화/수...) |
| b | 확장 요소, 요일의 서수 요소를 표현 (월요일=1, ..., 일요일=7) |
| B | 확장 요소, 요일의 서수 요소를 표현 (한국/미국: 숫자(17), 일본/중국/대만: 한자(一七)) |
| a | 확장 요소, 오전/오후 요소를 표현 (예: 오전/오후, AM/PM) |
| A | 확장 요소, A.M./P.M. 요소를 표현 (국가 코드에 상관없이 A.M./P.M.으로 표현) |
| I | 확장 요소, 연호/국력 요소를 표현 (일본: 平成, 대만: 民國) |
| L | 확장 요소, 연호/국력의 연도 요소를 표현 |
| k | 확장 요소, 시(hour) 요소를 표현 (12시간제, 1-12) |
샘플 76 — DOC_DATE 예
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
표 147 — SUMMARY 요소
인자 이름	인자 형식	설명
Property	stringParam	문서 요약 정보 속성
문서 요약 정보 속성
표 148 — 문서 요약 요소
| 속성 | 설명 |
| :--- | :--- |
| $title | 문서 제목 |
| $subject | 문서 주제 |
| $author | 문서 저자 |
| $keywords | 문서 키워드 |
| $comments | 문서 주석 |
| $lastAuthor | 문서를 마지막으로 수정한 사람 |
| $revNumber | 문서 이력 번호 |
| $lastPrinted | 문서가 마지막으로 출력된 시각 |
| $createDate | 문서가 생성된 시각 |
| $lastSaveDate | 문서가 마지막으로 저장된 시각 |
| $pageCount | 문서 페이지 수 |
| $wordCount | 문서 단어 수 |
| $charCount | 문서 글자 수 |
10.7.2.7.3 XML 예
샘플 77 — SUMMARY 예
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
표 149 — USER_INFO 요소
인자 이름	인자 형식	설명
Category	stringParam	사용자 정보 항목
사용자 정보 항목
표 150 — 사용자 정보 항목
| 항목 | 설명 |
| :--- | :--- |
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
샘플 78 — USER_INFO 예
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
표 151 — PATH 요소
인자 이름	인자 형식	설명
Format	stringParam	파일 경로 형식
파일 경로 형식
표 152 — 파일 경로 형식
| 형식 | 설명 |
| :--- | :--- |
| $P | 경로만 |
| $F | 파일 이름만 |
| 
P
P
F | 경로와 파일 이름 |
10.7.2.9.3 XML 예
샘플 79 — PATH 예
code
Xml
<fieldBegin id="fb08" type="PATH" editable="false" dirty="false">
    <parameters count="1">
        <stringParam name="Format">$P$F</stringParam>
    </parameters>
</fieldBegin>
10.7.2.10 CROSSREF
10.7.2.10.1 CROSSREF
상호 참조는 다른 곳의 그림, 표 등을 현재의 본문에서 항상 참조할 수 있도록 그 위치를 표시해 주는 기능이다.
10.7.2.10.2 필요한 인자들
표 153 — CROSSREF 요소
인자 이름	인자 형식	설명
RefPath	stringParam	참조 경로
RefType	stringParam	참조 대상 종류
RefContentType	stringParam	참조 내용
RefHyperlink	booleanParam	하이퍼링크 여부
RefOpenType	stringParam	하이퍼링크 이동 시 문서창 열기 옵션. HYPERLINK의 '이동 시 문서창 옵션' 참조
참조 대상 종류
표 155 — 참조 대상 종류
| 참조 대상 종류 | 설명 |
| :--- | :--- |
| TARGET_TABLE | 표 |
| TARGET_PICTURE | 그림 |
| TARGET_EQUATION | 수식 |
| TARGET_FOOTNOTE | 각주 |
| TARGET_ENDNOTE | 미주 |
| TARGET_OUTLINE | 개요 |
| TARGET_BOOKMARK | 책갈피 |
참조 내용
표 156 — 참조 내용
| 참조 내용 | 설명 |
| :--- | :--- |
| OBJECT_TYPE_PAGE | 참조 대상이 있는 쪽 번호 |
| OBJECT_TYPE_NUMBER | 참조 대상의 번호 |
| OBJECT_TYPE_CONTENTS | 참조 대상의 캡션 내용 또는 책갈피의 경우 책갈피 내용 |
| OBJECT_TYPE_UPDOWNPOS | 현재 위치 기준으로 참조 대상이 있는 위치 (위/아래) |
10.7.2.10.3 XML 예
샘플 80 — CROSSREF 예
code
Xml
<fieldBegin id="fb09" type="CROSSREF" editable="false" dirty="false">
    <parameters count="5">
        <stringParam name="RefPath">?table_id</stringParam>
        <stringParam name="RefType">TARGET_TABLE</stringParam>
        <stringParam name="RefContentType">OBJECT_TYPE_NUMBER</stringParam>
        <booleanParam name="RefHyperlink">true</booleanParam>
        <stringParam name="RefOpenType">HWPHYPERLINK_JUMP_DONTCARE</stringParam>
    </parameters>
</fieldBegin>
10.7.2.11 MAILMERGE
10.7.2.11.1 MAILMERGE
메일 머지는 여러 사람의 이름, 주소 등이 들어 있는 '데이터 파일(data file)'과 '서식 파일(form letter)'을 합침(merging)으로써, 이름이나 직책, 주소 부분 등만 다르고 나머지 내용이 같은 수십, 수백 통의 편지지를 한꺼번에 만드는 기능이다.
10.7.2.11.2 필요한 인자들
표 157 — MAILMERGE 요소
인자 이름	인자 형식	설명
FieldType	stringParam	필드 형식. WAB, USER_DEFINE 중 하나의 값을 가질 수 있음
FieldValue	stringParam	필드 엔트리 이름
10.7.2.11.3 XML 예
샘플 81 — MAILMERGE 예
code
Xml
<fieldBegin id="fb10" type="MAILMERGE" editable="false" dirty="false">
    <parameters count="2">
        <stringParam name="FieldType">WAB</stringParam>
        <stringParam name="FieldValue">SURNAME</stringParam>
    </parameters>
</fieldBegin>
10.7.2.12 MEMO
10.7.2.12.1 MEMO
메모는 현재 편집 중인 문서에서 특정 단어나 블록으로 설정한 문자열에 대한 간단한 추가 내용을 기록하는 기능이다.
10.7.2.12.2 필요한 인자들
표 159 — MEMO 요소
인자 이름	인자 형식	설명
ID	stringParam	메모를 식별하기 위한 아이디
Number	integerParam	메모 번호
CreateDateTime	stringParam	메모 작성 시각. KS X ISO 8601에 따라 'YYYY-MM-DD hh:mm:ss' 형식 사용
Author	stringParam	메모 작성자
MemoShapeIDRef	stringParam	메모 모양 속성 정보 아이디 참조값
10.7.2.12.3 XML 예
샘플 82 — MEMO 예
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
    <subList>
        <!-- 메모 내용 -->
        <p>
            <run>
                <t>메모 내용</t>
            </run>
        </p>
    </subList>
</fieldBegin>
10.7.2.13 PROOFREADING_MARKS
10.7.2.13.1 PROOFREADING_MARKS
교정 부호는 맞춤법, 띄어쓰기, 글자 크기, 문장 부호, 줄바꿈, 오자, 탈자, 어색한 표현 등을 바로잡기 위하여 특정 부호를 문서 내에 삽입하는 기능이다.
10.7.2.13.2 필요한 인자들
표 160 — PROOFREADING_MARKS 요소
인자 이름	인자 형식	설명
Type	stringParam	교정 부호 종류
ProofreadingContents	stringParam	교정 내용. 넣음표, 부호 넣음표, 고침표에서 사용됨
MovingMargin	integerParam	자리 옮김 여백. 오른/왼자리 옮김표에서 사용됨
MovingStart	integerParam	자리 옮김 시작위치. 오른/왼자리 옮김표에서 사용됨
SplitType	stringParam	'자리 바꿈 나눔표'인지 '줄 서로 바꿈 나눔표'인지 여부
10.7.2.13.3 XML 예
샘플 83 — PROOFREADING_MARKS 예
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
개인 정보 보호는 현재 화면에서 편집하고 있는 문서 내용 중 사용자가 블록으로 지정한 영역을 암호를 걸어 사용자가 선택한 문자로 변경하는 기능이다.
10.7.2.14.2 필요한 인자들
표 163 — PRIVATEINFO 요소
인자 이름	인자 형식	설명
EncryptMode	stringParam	암호화 방식
EncryptLength	integerParam	암호화된 결과의 길이
DecryptLength	integerParam	복호화한 후의 길이
EncryptString	stringParam	암호화된 결과를 BASE64로 인코딩한 문자열
MarkChar	stringParam	암호화 전 문자열 대신에 화면에 표시될 문자
Pattern	stringParam	Pattern
Type	stringParam	Type
10.7.2.16 CITATION
10.7.2.16.1 CITATION
인용은 연구논문이나 다른 여타의 원본을 인용해야 하는 문서를 작성할 때 사용하는 기능이다. 인용은 다양한 형식의 인용 스타일을 선택하여 적용할 수 있다.
10.7.2.16.2 필요한 인자들
표 166 — CITATION 요소
인자 이름	인자 형식	설명
GUID	stringParam	인용 고유 번호
Result	stringParam	스타일이 적용된 인용 문자열
10.7.2.16.3 XML 예
샘플 86 — CITATION 예
code
Xml
<fieldBegin id="fb13" type="CITATION" editable="false" dirty="true">
    <parameters count="2">
        <stringParam name="GUID">A25C5BE1-391C-4088-9E2C-3E0C521730F1</stringParam>
        <stringParam name="Result">(나연, 1948)</stringParam>
    </parameters>
</fieldBegin>
10.7.2.17 BIBLIOGRAPHY
참고문헌은 참조한 원본에 대한 출처 정보를 적는 기능이다. 다양한 참고문헌 스타일을 적용할 수 있다.
10.7.2.17.1 필요한 인자들
표 167 — BIBLIOGRAPHY 요소
인자 이름	인자 형식	설명
StyleName	stringParam	참고문헌 스타일
StyleVersion	stringParam	참고문헌 스타일 버전
10.7.2.17.2 XML 예
샘플 87 — BIBLIOGRAPHY 예
code
Xml
<fieldBegin id="fb14" type="BIBLIOGRAPHY" editable="false" dirty="true">
    <parameters count="2">
        <stringParam name="StyleName">APA</stringParam>
        <stringParam name="StyleVersion">6</stringParam>
    </parameters>
</fieldBegin>
10.7.3 fieldEnd 요소
<fieldBegin> 요소와 쌍을 이루는 요소이다.
표 168 — fieldEnd 요소
속성 이름	설명
beginIDRef	시작 아이디 참조값
fieldid	필드 개체 아이디
샘플 89 — fieldEnd 예
code
Xml
<hp:fieldEnd beginIDRef="1790845288" fieldid="-623209829"/>