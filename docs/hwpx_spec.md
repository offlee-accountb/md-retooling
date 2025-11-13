# HWPX Specification – Full Consolidation

본 문서는 아래 원본 조각을 손실 없이 순서대로 통합한 문서입니다.
원본 파일: okok1-1-1.md okok1-1-2.md okok1-1-3.md okok1-2-1.md okok1-2-2.md okok1-2-3.md okok1-3.md okok1-4.md

목차(파일별):
- [okok1-1-1.md](#source-okok111.md)
- [okok1-1-2.md](#source-okok112.md)
- [okok1-1-3.md](#source-okok113.md)
- [okok1-2-1.md](#source-okok121.md)
- [okok1-2-2.md](#source-okok122.md)
- [okok1-2-3.md](#source-okok123.md)
- [okok1-3.md](#source-okok13.md)
- [okok1-4.md](#source-okok14.md)

## Global Index (Sections)
- 3.1 HWP(Hangeul Word-Processor) 문서: 1989년 이후 (주)한글과컴퓨터에서 개발한 한글 워드프로세서 프로그램으로 생성되는 바이너리 형식의 전자문서 (#s-3-1-HWPHangeul)
- 3.2 IDPF(International Digital Publishing Forum): 국제 디지털 출판 포럼. 전자 출판 산업의 표준을 수립하기 위해 성립된 디지털 출판 산업을 위한 무역 및 표준 협회 (#s-3-2-IDPFInternational)
- 3.3 OCF(Open Container Format): IDPF(3.2)에서 정의한 전자책을 위한 포맷 중의 하나인 컨테이너 포맷 (#s-3-3-OCFOpen)
- 3.4 EPUB Publication: ISO/IEC 23736 표준에서 정의하는 전자책의 논리적 구조 정보를 표현하는 표준 (#s-3-4-EPUB)
- 3.5 OPS(Open Publication Structure): IDPF(3.2)에서 정의한 전자책을 위한 공개 출판 구조 포맷 (#s-3-5-OPSOpen)
- 3.6 OPF(Open Packaging Format): IDPF(3.2)에서 정의한 전자책을 위한 공개 패키징 포맷 (#s-3-6-OPFOpen)
- 3.7 EPUB Content documents: 전자책의 콘텐츠 표현을 위한 표준 (#s-3-7-EPUB)
- 3.8 OWPML(Open Word-Processor Markup Language): 이 표준에서 정의하는 개방형 워드프로세서 문서 형식 (#s-3-8-OWPMLOpen)
- 3.9 대체(fall-back): 동일한 콘텐츠를 표현하는 다른 미디어 형식의 파일을 연결된 정보를 통해 찾아가는 방식으로, 해당 리딩 시스템(3.12)이 처리할 수 있는 파일을 찾는 행위 (#s-3-9-fall-back)
- 3.10 ZIP: 번들링(bundling)과 압축에 대한 파일 포맷 (#s-3-10-ZIP)
- 3.11 XML 네임스페이스: XML 요소의 이름과 속성의 고유한 URI 형식 식별자 (#s-3-11-XML)
- 3.12 리딩 시스템(reading system): OWPML(3.8) 문서를 읽고, 편집할 수 있는 애플리케이션 또는 시스템 (#s-3-12-reading)
- 3.13 SP 그룹(significant property group): 텍스트 문서 구성 요소 정의 항목에 대한 용어 정의 및 그룹화 (#s-3-13-SP)
- 3.14 각주(footnote): 본문 내용에 대한 보충 자료를 구체적으로 제시하거나, 인용한 자료의 출처 등을 밝히는 현재 쪽의 맨 끝부분에 놓이는 주석 (#s-3-14-footnote)
- 3.15 강조점: 문자열을 강조하는 목적으로 현재 글자의 위, 아래 또는 글자 사이에 찍는 점 (#s-3-15-sec)
- 3.16 개요: 본문의 내용을 간결하게 추려낸 주된 글 내용 (#s-3-16-sec)
- 3.17 개체: 텍스트, 도형(3.32), 그림, 글상자(3.25), 수식(3.45), 표, 글맵시, 소리, 플래시 등의 독립된 기능을 하는 단위 (#s-3-17-sec)
- 3.18 격자: 한 쪽에 들어갈 수 있는 줄 수를 제한하기 위한 표준 줄 간격 (#s-3-18-sec)
- 3.19 계산식: 표(3.64)에서 덧셈, 뺄셈, 곱셈, 나눗셈의 간단한 사칙연산 및 avg와 같은 통계 함수와 sum(left) 등과 같은 left, right, below, above의 범위 지정자로 구성된 식 (#s-3-19-avg)
- 3.20 교정 부호: 맞춤법, 띄어쓰기, 글자 크기, 문장 부호, 줄 바꾸기 등을 바로잡기 위하여 문서에 표시된 부호 (#s-3-20-sec)
- 3.21 구역: HWP 문서에서 본문의 영역을 구분 짓는 단위 (#s-3-21-HWP)
- 3.22 글꼴: 글씨를 써 놓은 모양. 글씨체의 종류를 나타내며, 대표적인 글꼴로는 바탕체, 궁서체, 돋움체 같은 것들이 있다. (#s-3-22-sec)
- 3.23 글맵시: 글자를 구부리거나 글자에 외곽선, 면 채우기(3.59), 그림자, 회전 등의 효과를 주어 문자를 꾸미는 기능 (#s-3-23-sec)
- 3.24 글머리표: 여러 개의 항목을 나열할 때 문단(3.36)의 머리에 불릿(bullet) 모양을 붙여서 입력하는 기능 (#s-3-24-bullet)
- 3.25 글상자: 문서에 위치와 크기 조절, 개체(3.17) 안의 채우기(3.42) 효과, 테두리의 모양과 색깔 바꾸기 등을 자유자재로 설정하여 글을 담는 상자 (#s-3-25-sec)
- 3.26 글자 격자: 한 줄에 들어갈 수 있는 글자의 수를 제한하기 위한 표준 글자 간격 (#s-3-26-sec)
- 3.27 글자 모양: 글자 색 바꾸기, 기울임, 진하게, 밑줄, 취소선(3.61), 그림자, 양각, 음각, 외곽선, 첨자 등의 다양한 글자의 속성 (#s-3-27-sec)
- 3.28 글자 스타일: 글자를 꾸미기 위해 글꼴(3.22), 글자 크기 등의 글자 모양(3.27)만을 미리 지정한 하나의 형식 (#s-3-28-sec)
- 3.29 글자 위치: 글자의 기준선을 기준으로 위나 아래 위치 (#s-3-29-sec)
- 3.30 다단: 신문이나 회보, 찾아보기 등을 만들 때 읽기 쉽도록 한 쪽을 여러 개로 나눌 때 쓰는 것 (#s-3-30-sec)
- 3.31 덧말: 본문의 아래나 또는 위에 넣는 보충 설명 (#s-3-31-sec)
- 3.32 도형: 직선, 직사각형, 타원, 호, 다각형, 곡선, 자유선, 개체(3.17) 연결선, 글상자(3.25) 등 문서에 삽입하고 편집할 수 있는 개체(3.17) (#s-3-32-sec)
- 3.33 머리말(header): 문서의 한 쪽의 맨 위에 한두 줄의 내용이 쪽마다 고정적으로 반복되는 것 (#s-3-33-header)
- 3.34 꼬리말(footer): 문서의 한 쪽의 맨 아래에 한두 줄의 내용이 쪽마다 고정적으로 반복되는 것 (#s-3-34-footer)
- 3.35 메모(memo): 현재 입력 중인 문서에서 특정 단어나 블록으로 설정한 문자열에 대해 편집자 기준으로 오른편에 글상자(3.25)가 실행되어 추가 내용을 입력하는 기능 (#s-3-35-memo)
- 3.36 문단: 여러 문장이 이어지다가 문맥에 따라 줄이 바뀌는 부분 (#s-3-36-sec)
- 3.37 미주(endnote): 본문 내용에 대한 보충 자료를 구체적으로 제시하거나 인용한 자료의 출처 등을 밝히는 현재 구역(3.21)의 맨 끝부분에 놓이는 주석 (#s-3-37-endnote)
- 3.38 바탕글 스타일: 문서의 기본 문단(3.36) 스타일 (#s-3-38-sec)
- 3.39 바탕쪽: 문서 전체 쪽에 공통으로 적용되는 모양 (#s-3-39-sec)
- 3.40 상호 참조: 다른 쪽의 그림, 표(3.64) 등을 본문에서 항상 참조할 수 있도록 그 위치를 표시해 주는 기능 (#s-3-40-sec)
- 3.41 색인(index): 책이나 학술서, 연구 대상이 된 서적의 내용 중에서 중요한 항목, 술어, 인명, 지명 등을 뽑아 본문 어느 쪽에 위치하는지 바로 찾아볼 수 있도록 쪽 번호와 함께 별도로 배열하여 놓은 목록 (#s-3-41-index)
- 3.42 선택 글자 보호: 현재 화면에서 편집하고 있는 문서 내용 중 사용자가 블록으로 지정한 영역에 암호를 걸어 사용자가 선택한 문자로 변경하여 개인 정보를 보호하는 기능 (#s-3-42-sec)
- 3.43 세로 정렬: 줄 안에서 각 글자의 위치를 세로로 정렬할 때 글자의 위쪽, 가운데, 아래쪽을 정하여 정렬하는 것 (#s-3-43-sec)
- 3.44 가로 정렬: 줄 안에서 각 글자의 위치를 가로로 정렬할 때 글자의 왼쪽, 가운데, 오른쪽을 정하여 정렬하는 것 (#s-3-44-sec)
- 3.45 수식: 수 또는 양을 나타내는 숫자나 문자를 연산 기호로 연결한 식과 수식(3.45)을 명령어를 이용하여 작성한 것 (#s-3-45-sec)
- 3.46 숨은 설명(hidden comment): 실제 문서의 내용에는 포함되지 않으면서, 파일을 편집하는 사람에게 필요한 메모(3.35)나 주의사항 등을 기록한 것 (#s-3-46-hidden)
- 3.47 스크립트(script): 이벤트 속성 또는 양식 개체(3.50)의 이벤트 내용을 실행시키게 하는 것 (#s-3-47-script)
- 3.48 스타일(style): 글꼴(3.22), 크기, 장평(3.54), 자간(3.53), 왼쪽 여백, 오른쪽 여백, 첫 줄, 정렬 방식, 줄 간격(3.57), 문단(3.36) 종류와 같은 문서의 전체적인 꾸밈 정보 (#s-3-48-style)
- 3.49 시작 번호: 문서 내에서 사용되는 각종 개체들의 번호의 시작 숫자 (#s-3-49-sec)
- 3.50 양식 개체: 편집 화면에 넣을 수 있는 명령 단추, 선택 상자, 콤보 상자, 라디오 단추, 입력 상자의 개체(3.17) (#s-3-50-sec)
- 3.51 용지 방향: 편집 용지를 좁게 쓸 것인가 넓게 쓸 것인가에 대한 방향 정의 (#s-3-51-sec)
- 3.52 용지 여백: 선택한 용지 설정에서 본문, 머리말(3.33), 꼬리말(3.34), 각주(3.14) 영역을 제외한 편집 용지상의 나머지 상하좌우 여백 (#s-3-52-sec)
- 3.53 자간: 글자와 글자 사이의 간격 (#s-3-53-sec)
- 3.54 장평: 글자의 가로/세로 비율. 글자의 세로 길이는 그대로 유지하면서 글자의 가로 폭을 줄이거나 늘리는 것 (#s-3-54-sec)
- 3.55 조판 부호: 편집 과정에서 사용자가 내리는 명령을 문서에 기록하여 나타내는 부호 (#s-3-55-sec)
- 3.56 주석(comment): 각주(3.14), 미주(3.37), 숨은 설명의 통칭 (#s-3-56-comment)
- 3.57 줄 간격: 지금 줄의 맨 위부터 다음 줄의 맨 위까지의 간격 (#s-3-57-sec)
- 3.58 차례: 책이나 글 따위에서 따로 적어 놓은 항목 (#s-3-58-sec)
- 3.59 채우기: 문서에서 표현되는 모든 개체의 면을 지정된 색과 지정된 패턴으로 채우는 기능 (#s-3-59-sec)
- 3.60 책갈피(bookmark): 문서를 편집하는 도중에 본문의 임의의 곳에 표시를 해 두었다가 현재 커서의 위치에 상관없이 표시해 둔 곳으로 커서를 곧바로 이동시키는 기능 (#s-3-60-bookmark)
- 3.61 취소선(strikeout): 선택한 단어나 블록 지정한 부분에 다양한 선과 모양으로 취소를 의미하는 선 (#s-3-61-strikeout)
- 3.62 캡션(caption): 본문에 들어가는 그림, 표(3.64), 그리기 개체(3.17), 수식(3.45)에 필요에 따라 번호와 제목, 간단한 설명을 붙이는 것 (#s-3-62-caption)
- 3.63 편집 용지: 어떤 크기의 용지에 편집할 것인지, 용지 방향(3.51), 용지 여백(3.52) 등에 대한 설정 (#s-3-63-sec)
- 3.64 표(table): 문서를 만들면서 복잡한 내용이나 수치 자료를 일목요연하게 정리하고자 할 때 이용하는 것 (#s-3-64-table)
- 3.65 하이퍼링크(hyperlink): 문서의 특정한 위치에 현재 문서나 다른 문서, 웹 페이지, 전자 우편 주소 등을 연결하여 쉽게 참조하거나 이동할 수 있게 해 주는 것 (#s-3-65-hyperlink)
- 3.66 전자서명: 문서에 디지털 서명을 하는 기능 (#s-3-66-sec)
- 3.67 변경 추적: 문서의 추가, 삭제, 서식 변경사항과 같은 수정내역을 기록하여 변경된 내용을 확인할 수 있는 기능 (#s-3-67-sec)
- 3.68 절대단위: 문서 내 다양한 수치를 나타내는 단위로, 물리적인 고정 값과 연관된 값을 나타내는 단위 (#s-3-68-sec)
- 3.69 상대단위: 문서 내 다양한 수치를 나타내는 단위로, 기준으로부터 상대적인 크기를 값으로 나타내는 단위 (#s-3-69-sec)
- 4.1 일반사항 (#s-4-1-sec)
- 4.2 OWPML XML 콘텐츠 문서의 조건 (#s-4-2-OWPML)
- 4.3 리딩 시스템의 적합성 (#s-4-3-sec)
- 4.4 OWPML 문서 호환성 및 적합성 조건 (#s-4-4-OWPML)
- 5.1 XML과의 관계 (#s-5-1-XML)
- 5.2 XML 네임스페이스와의 관계 (#s-5-2-XML)
- 5.3 유니코드와의 관계 (#s-5-3-sec)
- 5.4 MIME 미디어 유형 (#s-5-4-MIME)
- 7.1 기본 형식 (#s-7-1-sec)
- 7.2 단위 (#s-7-2-sec)
- 7.2.1 상대단위 (#s-7-2-1-sec)
- 7.2.2 절대단위 (#s-7-2-2-sec)
- 7.2.3 HWPUNIT (#s-7-2-3-HWPUNIT)
- 7.2.4 HWPUNIT과 다른 단위와의 관계 (#s-7-2-4-HWPUNIT)
- 7.2.5 기타 단위 표현 (#s-7-2-5-sec)
- 7.3 OWPML의 기본 자료 형식 (#s-7-3-OWPML)
- 7.4 OWPML의 색상 표현 (#s-7-4-OWPML)
- 8.1 OCF (#s-8-1-OCF)
- 8.2 OCF OWPML 프로파일 (#s-8-2-OCF)
- 8.3 파일 형식 버전 식별 (#s-8-3-sec)
- 8.4 OPF OWPML 프로파일 (#s-8-4-OPF)
- 8.4.1 OPF 도입 (#s-8-4-1-OPF)
- 8.4.2 OPF 적용 요소 (#s-8-4-2-OPF)
- 8.4.3 Metadata profile (#s-8-4-3-Metadata)
- 9.1 네임스페이스 (#s-9-1-sec)
- 9.2.1 헤더 구조 (#s-9-2-1-sec)
- 9.2.2 beginNum 요소 (#s-9-2-2-beginNum)
- 9.2.5 compatibleDocument 요소 (#s-9-2-5-compatibleDocument)
- 9.2.5.2 layoutcompatibility 요소 (#s-9-2-5-2-layoutcompatibility)
- 9.2.6 trackChangeConfig 요소 (#s-9-2-6-trackChangeConfig)
- 9.2.7 docOption 요소 (#s-9-2-7-docOption)
- 9.2.8 metaTag 요소 (#s-9-2-8-metaTag)
- 9.3 문서 설정 정보 (#s-9-3-sec)
- 9.3.1 문서 설정 (#s-9-3-1-sec)
- 9.3.2 fontfaces 요소 (#s-9-3-2-fontfaces)
- 9.3.3 borderFills 요소 (#s-9-3-3-borderFills)
- 9.3.4 charProperties 요소 (#s-9-3-4-charProperties)
- 9.3.5 tabProperties 요소 (#s-9-3-5-tabProperties)
- 9.3.6 numberings 요소 (#s-9-3-6-numberings)
- 9.3.7 bullets 요소 (#s-9-3-7-bullets)
- 9.3.8 paraProperties 요소 (#s-9-3-8-paraProperties)
- 9.3.8.2 paraPr 요소 (#s-9-3-8-2-paraPr)
- 9.3.8.2.1 paraPr 일반 항목 (#s-9-3-8-2-1-paraPr)
- 9.3.8.2.2 align 요소 (#s-9-3-8-2-2-align)
- 9.3.8.2.3 heading 요소 (#s-9-3-8-2-3-heading)
- 9.3.8.2.4 breakSetting 요소 (#s-9-3-8-2-4-breakSetting)
- 9.3.8.2.5 margin 요소 (#s-9-3-8-2-5-margin)
- 9.3.8.2.6 lineSpacing 요소 (#s-9-3-8-2-6-lineSpacing)
- 9.3.8.2.7 border 요소 (#s-9-3-8-2-7-border)
- 9.3.8.2.8 autoSpacing 요소 (#s-9-3-8-2-8-autoSpacing)
- 9.3.9 styles 요소 (#s-9-3-9-styles)
- 9.3.9.1 styles (#s-9-3-9-1-styles)
- 9.3.9.2 style 요소 (#s-9-3-9-2-style)
- 9.3.10 memoProperties 요소 (#s-9-3-10-memoProperties)
- 9.3.10.1 memoProperties (#s-9-3-10-1-memoProperties)
- 9.3.10.2 memoPr 요소 (#s-9-3-10-2-memoPr)
- 9.3.11 trackChanges 요소 (#s-9-3-11-trackChanges)
- 9.3.11.1 trackChanges (#s-9-3-11-1-trackChanges)
- 9.3.11.2 trackChange 요소 (#s-9-3-11-2-trackChange)
- 9.3.12 trackChangeAuthors 요소 (#s-9-3-12-trackChangeAuthors)
- 9.3.12.1 trackChangeAuthors 일반 항목 (#s-9-3-12-1-trackChangeAuthors)
- 9.3.12.2 trackChangeAuthor 요소 (#s-9-3-12-2-trackChangeAuthor)
- 10.1 네임스페이스 (#s-10-1-sec)
- 10.2 본문 개요 (#s-10-2-sec)
- 10.3 sec 요소 (#s-10-3-sec)
- 10.4 p 요소 (#s-10-4-p)
- 10.5 run 요소 (#s-10-5-run)
- 10.6 secPr 요소 (#s-10-6-secPr)
- 10.7 Ctrl 요소 (#s-10-7-Ctrl)
- 10.7.1 colPr 요소 (#s-10-7-1-colPr)
- 10.7.2 fieldBegin 요소 (#s-10-7-2-fieldBegin)
- 10.7.2.2 CLICK_HERE (#s-10-7-2-2-CLICK_HERE)
- 10.7.2.2.1 필요한 인자들 (#s-10-7-2-2-1-sec)
- 10.7.2.3 HYPERLINK (#s-10-7-2-3-HYPERLINK)
- 10.7.2.3.1 HYPERLINK (#s-10-7-2-3-1-HYPERLINK)
- 10.7.2.3.2 필요한 인자들 (#s-10-7-2-3-2-sec)
- 10.7.2.4 BOOKMARK (#s-10-7-2-4-BOOKMARK)
- 10.7.2.4.1 BOOKMARK (#s-10-7-2-4-1-BOOKMARK)
- 10.7.2.4.2 XML 예 (#s-10-7-2-4-2-XML)
- 10.7.2.5 FORMULA (#s-10-7-2-5-FORMULA)
- 10.7.2.5.1 FORMULA (#s-10-7-2-5-1-FORMULA)
- 10.7.2.5.2 필요한 인자들 (#s-10-7-2-5-2-sec)
- 10.7.2.5.3 XML 예 (#s-10-7-2-5-3-XML)
- 10.7.2.6 DATE 및 DOC_DATE (#s-10-7-2-6-DATE)
- 10.7.2.6.1 필요한 인자들 (#s-10-7-2-6-1-sec)
- 10.7.2.7 SUMMARY (#s-10-7-2-7-SUMMARY)
- 10.7.2.7.1 Summary (#s-10-7-2-7-1-Summary)
- 10.7.2.7.2 필요한 인자들 (#s-10-7-2-7-2-sec)
- 10.7.2.7.3 XML 예 (#s-10-7-2-7-3-XML)
- 10.7.2.8 USER_INFO (#s-10-7-2-8-USER_INFO)
- 10.7.2.8.1 USER_INFO (#s-10-7-2-8-1-USER_INFO)
- 10.7.2.8.2 필요한 인자들 (#s-10-7-2-8-2-sec)
- 10.7.2.8.3 XML 예 (#s-10-7-2-8-3-XML)
- 10.7.2.9 PATH (#s-10-7-2-9-PATH)
- 10.7.2.9.1 Path (#s-10-7-2-9-1-Path)
- 10.7.2.9.2 필요한 인자들 (#s-10-7-2-9-2-sec)
- 10.7.2.9.3 XML 예 (#s-10-7-2-9-3-XML)
- 10.7.2.10 CROSSREF (#s-10-7-2-10-CROSSREF)
- 10.7.2.10.1 CROSSREF (#s-10-7-2-10-1-CROSSREF)
- 10.7.2.10.2 필요한 인자들 (#s-10-7-2-10-2-sec)
- 10.7.2.10.3 XML 예 (#s-10-7-2-10-3-XML)
- 10.7.2.11 MAILMERGE (#s-10-7-2-11-MAILMERGE)
- 10.7.2.11.1 MAILMERGE (#s-10-7-2-11-1-MAILMERGE)
- 10.7.2.11.2 필요한 인자들 (#s-10-7-2-11-2-sec)
- 10.7.2.11.3 XML 예 (#s-10-7-2-11-3-XML)
- 10.7.2.12 MEMO (#s-10-7-2-12-MEMO)
- 10.7.2.12.1 MEMO (#s-10-7-2-12-1-MEMO)
- 10.7.2.12.2 필요한 인자들 (#s-10-7-2-12-2-sec)
- 10.7.2.12.3 XML 예 (#s-10-7-2-12-3-XML)
- 10.7.2.13 PROOFREADING_MARKS (#s-10-7-2-13-PROOFREADING_MARKS)
- 10.7.2.13.1 PROOFREADING_MARKS (#s-10-7-2-13-1-PROOFREADING_MARKS)
- 10.7.2.13.2 필요한 인자들 (#s-10-7-2-13-2-sec)
- 10.7.2.13.3 XML 예 (#s-10-7-2-13-3-XML)
- 10.7.2.14 PRIVATEINFO (#s-10-7-2-14-PRIVATEINFO)
- 10.7.2.14.1 PRIVATEINFO 요소 (#s-10-7-2-14-1-PRIVATEINFO)
- 10.7.2.14.2 필요한 인자들 (#s-10-7-2-14-2-sec)
- 10.7.2.16 CITATION (#s-10-7-2-16-CITATION)
- 10.7.2.16.1 CITATION (#s-10-7-2-16-1-CITATION)
- 10.7.2.16.2 필요한 인자들 (#s-10-7-2-16-2-sec)
- 10.7.2.16.3 XML 예 (#s-10-7-2-16-3-XML)
- 10.7.2.17 BIBLIOGRAPHY (#s-10-7-2-17-BIBLIOGRAPHY)
- 10.7.2.17.1 필요한 인자들 (#s-10-7-2-17-1-sec)
- 10.7.2.17.2 XML 예 (#s-10-7-2-17-2-XML)
- 10.7.3 fieldEnd 요소 (#s-10-7-3-fieldEnd)
- 10.9.5.7.1 renderinginfo 요소 (#s-10-9-5-7-1-renderinginfo)
- 10.9.5.7.2 행렬 요소 형식 (#s-10-9-5-7-2-sec)
- 10.9.6 pic 요소 (#s-10-9-6-pic)
- 10.9.6.1 pic (#s-10-9-6-1-pic)
- 10.9.6.2 테두리선 모양 (#s-10-9-6-2-sec)
- 10.9.6.3 이미지 좌표 정보 (#s-10-9-6-3-sec)
- 10.9.6.3.1 이미지 좌표 (#s-10-9-6-3-1-sec)
- 10.9.6.3.2 점 요소 형식 (#s-10-9-6-3-2-sec)
- 10.9.6.4 이미지 자르기 정보 (#s-10-9-6-4-sec)
- 10.9.6.5 이미지 효과 정보 (#s-10-9-6-5-sec)
- 10.9.6.5.1 이미지 효과 (#s-10-9-6-5-1-sec)
- 10.9.6.5.2 그림자 효과 (#s-10-9-6-5-2-sec)
- 10.9.6.5.4 부드러운 가장자리 효과 (#s-10-9-6-5-4-sec)
- 10.9.6.5.5 반사 효과 (#s-10-9-6-5-5-sec)
- 10.9.6.6 이미지 원본 정보 (#s-10-9-6-6-sec)
- 10.9.7 ole 요소 (#s-10-9-7-ole)
- 10.9.7.1 ole (#s-10-9-7-1-ole)
- 10.9.7.2 extent 요소 (#s-10-9-7-2-extent)
- 10.9.8 container 요소 (#s-10-9-8-container)
- 10.9.9 chart 요소 (#s-10-9-9-chart)
- 10.10 그리기 객체 (#s-10-10-sec)
- 10.10.1 그리기 객체 (#s-10-10-1-sec)
- 10.10.2 AbstractDrawingObjectType (#s-10-10-2-AbstractDrawingObjectType)
- 10.10.2.1 AbstractDrawingObjectType (#s-10-10-2-1-AbstractDrawingObjectType)
- 10.10.2.2 채우기 정보 (#s-10-10-2-2-sec)
- 10.10.2.2.1 채우기 (#s-10-10-2-2-1-sec)
- 10.10.2.2.2 면 채우기 정보 (#s-10-10-2-2-2-sec)
- 10.10.2.2.3 그러데이션 효과 (#s-10-10-2-2-3-sec)
- 10.10.2.2.4 그림으로 채우기 정보 (#s-10-10-2-2-4-sec)
- 10.10.2.3 그리기 객체 글상자용 텍스트 (#s-10-10-2-3-sec)
- 10.10.2.3.2 글상자 텍스트 여백 (#s-10-10-2-3-2-sec)
- 10.10.2.4 그리기 객체의 그림자 정보 (#s-10-10-2-4-sec)
- 10.10.3 그리기 객체 — 선 (#s-10-10-3-sec)
- 10.10.4 그리기 객체 — 사각형 (#s-10-10-4-sec)
- 10.10.5 그리기 객체 — 타원 (#s-10-10-5-sec)
- 10.10.7 그리기 객체 — 다각형 (#s-10-10-7-sec)
- 10.10.8 그리기 객체 — 곡선 (#s-10-10-8-sec)
- 10.10.8.1 곡선 (#s-10-10-8-1-sec)
- 10.10.8.2 곡선 세그먼트 (#s-10-10-8-2-sec)
- 10.10.9 그리기 객체 — 연결선 (#s-10-10-9-sec)
- 10.10.9.1 연결선 (#s-10-10-9-1-sec)
- 10.10.9.2 연결선 연결점 정보 (#s-10-10-9-2-sec)
- 10.10.9.3 연결선 조절점 정보 (#s-10-10-9-3-sec)
- 10.11 양식 객체 (#s-10-11-sec)
- 10.11.1 AbstractFormObjectType (#s-10-11-1-AbstractFormObjectType)
- 10.11.1.1 AbstractFormObjectType (#s-10-11-1-1-AbstractFormObjectType)
- 10.11.1.2 양식 객체의 글자 속성 (#s-10-11-1-2-sec)
- 10.11.2 AbstractButtonObjectType (#s-10-11-2-AbstractButtonObjectType)
- 10.7.2.18 METATAG (#s-10-7-2-18-METATAG)
- 10.7.4 bookmark 요소 (#s-10-7-4-bookmark)
- 10.7.5 머리말/꼬리말 요소 형식 (#s-10-7-5-sec)
- 10.7.6 각주/미주 요소 형식 (#s-10-7-6-sec)
- 10.7.8 pageNumCtrl 요소 (#s-10-7-8-pageNumCtrl)
- 10.7.9 pageHiding 요소 (#s-10-7-9-pageHiding)
- 10.7.10 pageNum 요소 (#s-10-7-10-pageNum)
- 10.7.11 indexmark 요소 (#s-10-7-11-indexmark)
- 10.7.12 hiddenComment 요소 (#s-10-7-12-hiddenComment)
- 10.8.2 markpenBegin 요소 (#s-10-8-2-markpenBegin)
- 10.8.4 tab 요소 (#s-10-8-4-tab)
- 10.8.5 변경 추적 요소 형식 (#s-10-8-5-sec)
- 10.9 기본 도형 객체 (#s-10-9-sec)
- 10.9.1 도형 객체 (#s-10-9-1-sec)
- 10.9.2 AbstractShapeObjectType (#s-10-9-2-AbstractShapeObjectType)
- 10.9.2.1 AbstractShapeObjectType (#s-10-9-2-1-AbstractShapeObjectType)
- 10.9.2.2 객체 크기 정보 (#s-10-9-2-2-sec)
- 10.9.2.3 객체 위치 정보 (#s-10-9-2-3-sec)
- 10.9.2.4 객체 바깥 여백 (#s-10-9-2-4-sec)
- 10.9.2.5 캡션 (#s-10-9-2-5-sec)
- 10.9.3 tbl 요소 (#s-10-9-3-tbl)
- 10.9.3.1 tbl (#s-10-9-3-1-tbl)
- 10.9.3.2 inMargin 요소 (#s-10-9-3-2-inMargin)
- 10.9.3.3 cellzoneList 요소 (#s-10-9-3-3-cellzoneList)
- 10.9.3.3.1 cellzoneList (#s-10-9-3-3-1-cellzoneList)
- 10.9.3.3.2 cellzone 요소 (#s-10-9-3-3-2-cellzone)
- 10.9.3.4 tr 요소 (#s-10-9-3-4-tr)
- 10.9.3.5 Label 요소 (#s-10-9-3-5-Label)
- 10.9.5.2 객체가 속한 그룹 내에서의 오프셋 정보 (#s-10-9-5-2-sec)
- 10.9.5.3 객체 생성 시 최초 크기 (#s-10-9-5-3-sec)
- 10.9.5.4 객체의 현재 크기 (#s-10-9-5-4-sec)
- 10.9.5.5 객체가 뒤집어진 상태인지 여부 (#s-10-9-5-5-sec)
- 10.9.5.6 객체 회전 정보 (#s-10-9-5-6-sec)
- 10.9.5.7 객체 렌더링 정보 (#s-10-9-5-7-sec)
- 10.9.5.7.1 객체 렌더링 (#s-10-9-5-7-1-sec)
- 16.2 Signature의 요소 (#s-16-2-Signature)
- 16.2.1 Signature의 구조 (#s-16-2-1-Signature)
- 16.2.2 ds:SignedInfo의 요소 (#s-16-2-2-dsSignedInfo)
- 16.2.3 ds:KeyInfo의 요소 (#s-16-2-3-dsKeyInfo)
- 16.2.4 ds:Object의 요소 (#s-16-2-4-dsObject)
- 16.3 XML 예 (#s-16-3-XML)
- 17.1 하위 호환성 (#s-17-1-sec)
- 17.2 switch 요소 (#s-17-2-switch)
- 17.2.1 switch (#s-17-2-1-switch)
- 17.2.2 case 요소 (#s-17-2-2-case)
- 17.2.3 default 요소 (#s-17-2-3-default)
- 17.3 XML 예 (#s-17-3-XML)
- 1.1 수식 버전 (#s-1-1-sec)
- 1.2 항의 구분 및 인식 (#s-1-2-sec)
- 1.3 수식에 쓰이는 글씨체 (#s-1-3-sec)
- 1.3.1 예제 (#s-1-3-1-sec)
- 1.3.1.1 기본 (#s-1-3-1-1-sec)
- 1.3.1.2 로만체 - 이탤릭체 (#s-1-3-1-2-sec)
- 1.3.1.3 볼드체 (#s-1-3-1-3-sec)
- 1.4 White Space 표현 (#s-1-4-White)
- 1.4.1 공백 및 줄바꿈 (#s-1-4-1-sec)
- 1.4.2 세로 칸 맞춤(&) (#s-1-4-2-sec)
- 1.5 예약어 및 명령어 (#s-1-5-sec)
- 1.5.1 따옴표(") (#s-1-5-1-sec)
- 1.5.2 분수 (OVER) (#s-1-5-2-OVER)
- 1.5.6 위 아래 (ATOP) (#s-1-5-6-ATOP)
- 1.5.9 제곱근 (SQRT) (#s-1-5-9-SQRT)
- 1.5.10 LEFT, RIGHT (#s-1-5-10-LEFT)
- 1.5.11 BIGG 기호 (#s-1-5-11-BIGG)
- 1.5.12 적분 (INT, OINT) (#s-1-5-12-INT)
- 1.5.13 극한 (lim, Lim) (#s-1-5-13-lim)
- 1.5.14 합 (SUM) (#s-1-5-14-SUM)
- 1.5.15 합집합 (UNION), 교집합 (INTER), 곱집합 (PROD) (#s-1-5-15-UNION)
- 1.5.16 상호관계 (REL) (#s-1-5-16-REL)
- 1.5.17 BUILDREL (#s-1-5-17-BUILDREL)
- 1.5.18 세로 쌓기 (PILE, LPILE, RPILE) (#s-1-5-18-PILE)
- 1.5.19 경우 (CASES) (#s-1-5-19-CASES)
- 1.5.20 조합 (CHOOSE, BINOM) (#s-1-5-20-CHOOSE)
- 1.5.21 행렬 (MATRIX, PMATRIX, BMATRIX, DMATRIX) (#s-1-5-21-MATRIX)
- 1.5.22 밑줄(UNDERLINE), 윗줄(OVERLINE) (#s-1-5-22-UNDERLINE)
- 1.5.23 왼쪽 아래첨자 (LSUB) (#s-1-5-23-LSUB)
- 1.5.24 왼쪽 위첨자 (LSUP) (#s-1-5-24-LSUP)
- 1.5.25 최소공배수/최대공약수 함수 (LADDER) (#s-1-5-25-LADDER)
- 1.5.26 2진수 변환 함수 (SLADDER) (#s-1-5-26-SLADDER)
- 1.5.27 거꾸로 나눗셈 (LONGDIV) (#s-1-5-27-LONGDIV)
- 1.5.28 색상 (COLOR) (#s-1-5-28-COLOR)
- 1.5.29 글자장식 (#s-1-5-29-sec)
- 1.5.30 부정 (NOT) (#s-1-5-30-NOT)
- 1.5.31 그리스 문자 (#s-1-5-31-sec)
- 1.5.32 괄호 (#s-1-5-32-sec)
- 1.5.33 적분 기호 (#s-1-5-33-sec)
- 1.5.34 합, 관계, 집합 기호 (#s-1-5-34-sec)
- 1.5.35 화살표 (#s-1-5-35-sec)
- 1.5.36 연산/논리 기호 (#s-1-5-36-sec)
- 1.5.37 기타기호 (#s-1-5-37-sec)
- 1.1 제정의 취지 (#s-1-1-sec)
- 1.2 제정의 경위 (#s-1-2-sec)
- 2.1 개정의 취지 (#s-2-1-sec)
- 2.2 개정의 경위 (#s-2-2-sec)
- 2.3 주요 개정 내역 (#s-2-3-sec)
- 2.3.1 적용범위 (#s-2-3-1-sec)
- 2.3.2 자구 수정 (#s-2-3-2-sec)
- 2.3.3 추가항목 (#s-2-3-3-sec)
- 2.3.4 KS A 0001:2015 반영 (#s-2-3-4-KS)
- 3.1 개정의 취지 (#s-3-1-sec)
- 3.2 개정의 경위 (#s-3-2-sec)
- 3.3 주요 개정 내용 (#s-3-3-sec)
- 3.3.1 적용범위 (#s-3-3-1-sec)
- 3.3.2 자구 수정 (#s-3-3-2-sec)
- 3.3.3 추가항목 (#s-3-3-3-sec)
- 3.3.4 KS A 0001:2023 반영 (#s-3-3-4-KS)




## Elements TOC
- bookmark (책갈피) (#hp-bookmark)
- HCFVersion (버전 정의) (#hv-HCFVersion)
- charPr (글자 속성) (#hp-charPr)
- tabProperties (탭 정보 목록) (#hp-tabProperties)
- tabPr (탭 정의) (#hp-tabPr)
- numberings (문단 번호 목록) (#hp-numberings)
- paraHead (머리설정) (#hp-paraHead)
- bullets (글머리표 목록) (#hp-bullets)
- paraPr (문단 모양) (#hp-paraPr)
- align (정렬) (#hp-align)
- heading (머리번호/글머리표) (#hp-heading)
- breakSetting (줄 나눔) (#hp-breakSetting)
- margin (문단 여백) (#hp-margin)
- lineSpacing (줄 간격) (#hp-lineSpacing)
- border (문단 테두리) (#hp-border)
- autoSpacing (자동 간격) (#hp-autoSpacing)
- p (문단) (#hp-p)
- run (런/문자 컨테이너) (#hp-run)
- secPr (구역 설정) (#hp-secPr)
- pagePr (쪽/용지 설정) (#hp-pagePr)
- footNotePr (각주 설정) (#hp-footNotePr)
- endNotePr (미주 설정) (#hp-endNotePr)
- masterPage (바탕쪽) (#hp-masterPage)
- tbl (표) (#hp-tbl)
- doNotApplyHyperlink (하이퍼링크 제외) (#hp-doNotApplyHyperlink)


## Assets TOC
- Examples:
  - example 4: — metadata의 예 (#example-4)
  - example 5: — beginNum 예 (#example-5)
  - example 71: fieldBegin 예 (#example-71)
  - example 72: CLICK_HERE 예 (#example-72)
  - example 73: HYPERLINK 예 (#example-73)
  - example 74: BOOKMARK 예 (#example-74)
  - example 75: FORMULA 예 (#example-75)
  - example 76: DOC_DATE 예 (#example-76)
  - example 77: SUMMARY 예 (#example-77)
  - example 78: USER_INFO 예 (#example-78)
  - example 79: PATH 예 (#example-79)
  - example 80: CROSSREF 예 (#example-80)
  - example 81: MAILMERGE 예 (#example-81)
  - example 82: MEMO 예 (#example-82)
  - example 83: PROOFREADING_MARKS 예 (#example-83)
  - example 85: METADATA 예```xml (#example-85)
  - example 86: CITATION 예 (#example-86)
  - example 94: pageHiding 예 (#example-94)
  - example 95: pageNum 예 (#example-95)
  - example 96: indexmark 예 (#example-96)
  - example 97: hiddenComment 예 (#example-97)
  - example 98: markpenBegin 예 (#example-98)
  - example 99: tab 예 (#example-99)
  - example 100: TrackChangeTag 예 (#example-100)
  - example 101: AbstractShapeObjectType 예 (#example-101)
  - example 102: pos 예 (#example-102)
  - example 103: outMargin 예 (#example-103)
  - example 104: caption 예 (#example-104)
  - example 105: tbl 예 (#example-105)
  - example 106: inMargin 예 (#example-106)
  - example 108: tc 예```xml (#example-108)
  - example 109: cellAddr 예 (#example-109)
  - example 115: AbstractShapeComponentType 예 (#example-115)
  - example 116: offset 예 (#example-116)
  - example 117: orgSz 예 (#example-117)
  - example 118: curSz 예 (#example-118)
  - example 119: flip 예 (#example-119)
  - example 120: rotationinfo 예 (#example-120)
- Figures:
  - figure 2: version.xml 파일의 XML 스키마 (#figure-2)
  - figure 6: <beginNum>의 구조 (#figure-6)
  - figure 148: <softEdge>의 구조 (#figure-148)
  - figure 149: <reflection>의 구조 (#figure-149)
  - figure 150: <alpha>의 구조 (#figure-150)
  - figure 169: <polygon>의 구조 (#figure-169)
  - figure 173: [ConnectPointType]의 구조 (#figure-173)
  - figure 175: <formCharPr>의 구조 (#figure-175)
  - figure 211: ds:SignatureMethod의 구조 (#figure-211)
  - figure 212: <switch>의 구조 (#figure-212)
- Samples:
  - sample 180: SignatureMethod 예 (#sample-180)
  - sample 181: switch 예 (#sample-181)
- Tables:
  - table 1: MIME 미디어 유형 (#table-1)
  - table 2: HWPValue 형식 (#table-2)
  - table 9: 색상 형식 (#table-9)
  - table 10: metadata 형식 (#table-10)
  - table 11: head version (#table-11)
  - table 12: head 속성 (#table-12)
  - table 13: beginNum 속성 (#table-13)
  - table 132: fieldBegin 하위 요소 (#table-132)
  - table 133: CLICK_HERE 요소 (#table-133)
  - table 134: HYPERLINK 요소 (#table-134)
  - table 135: 하이퍼링크 종류 (#table-135)
  - table 136: 대상의 종류 (#table-136)
  - table 137: 문서창 옵션 (#table-137)
  - table 138: FORMULA 요소 (#table-138)
  - table 139: FORMULA 함수 목록 (#table-139)
  - table 140: FORMULA 함수 인자 (#table-140)
  - table 141: 셀 번호 (#table-141)
  - table 142: 결과 출력 형식 (#table-142)
  - table 143: DATE 요소 (#table-143)
  - table 144: 국가 코드 (#table-144)
  - table 145: 날짜/시간 표시 기호 (#table-145)
  - table 147: SUMMARY 요소 (#table-147)
  - table 148: 문서 요약 요소 (#table-148)
  - table 149: USER_INFO 요소 (#table-149)
  - table 150: 사용자 정보 항목 (#table-150)
  - table 151: PATH 요소 (#table-151)
  - table 153: CROSSREF 요소 (#table-153)
  - table 154: 참조 경로 형식 (#table-154)
  - table 155: 참조 대상 종류 (#table-155)
  - table 156: 참조 내용 (#table-156)
  - table 157: MAILMERGE 요소 (#table-157)
  - table 158: 필드 엔트리 이름 (#table-158)
  - table 159: MEMO 요소 (#table-159)
  - table 160: PROOFREADING_MARKS 요소 (#table-160)
  - table 161: 교정 부호 종류 (#table-161)
  - table 162: SplitType 요소 (#table-162)
  - table 163: PRIVATEINFO 요소 (#table-163)
  - table 164: 암호화 방식 (#table-164)
  - table 166: CITATION 요소 (#table-166)
  - table 176: pageNumCtrl 요소 (#table-176)
  - table 177: pageHiding 요소 (#table-177)
  - table 178: pageNum 요소 (#table-178)
  - table 179: indexmark 요소 (#table-179)
  - table 180: hiddenComment 요소 (#table-180)
  - table 182: t 하위 요소 (#table-182)
  - table 183: markpenBegin 요소 (#table-183)
  - table 184: titleMark 요소 (#table-184)
  - table 185: tab 요소 (#table-185)
  - table 186: TrackChangeTag 요소 (#table-186)
  - table 187: AbstractShapeObjectType 요소 (#table-187)
  - table 188: AbstractShapeObjectType 하위 요소 (#table-188)
  - table 190: pos 요소 (#table-190)
  - table 191: outMargin 요소 (#table-191)
  - table 192: caption 요소 (#table-192)
  - table 193: caption 하위 요소 (#table-193)
  - table 195: tbl 하위 요소 (#table-195)
  - table 196: inMargin 요소 (#table-196)
  - table 197: cellzoneList 하위 요소 (#table-197)
  - table 198: cellzone 요소 (#table-198)
  - table 201: tc 요소 (#table-201)
  - table 202: cellAddr 요소 (#table-202)
  - table 209: AbstractShapeComponentType 요소 (#table-209)
  - table 210: AbstractShapeComponentType 하위 요소 (#table-210)
  - table 211: offset 요소 (#table-211)
  - table 212: orgSz 요소 (#table-212)
  - table 213: curSz 요소 (#table-213)
  - table 214: flip 요소 (#table-214)
  - table 215: rotationInfo 요소 (#table-215)
  - table 236: softEdge 요소 (#table-236)
  - table 237: reflection 요소 (#table-237)
  - table 238: reflection 하위 요소 (#table-238)
  - table 239: alpha 요소 (#table-239)
  - table 267: polygon 요소 (#table-267)
  - table 268: curve 요소 (#table-268)
  - table 269: seg 요소 (#table-269)
  - table 270: connectLine 요소 (#table-270)
  - table 271: connectLine 하위 요소 (#table-271)
  - table 272: ConnectPointType 요소 (#table-272)
  - table 273: ConnectControlPointType 속성 (#table-273)
  - table 274: type 값 (#table-274)
  - table 275: AbstractFormObjectType 요소 (#table-275)
  - table 276: AbstractFormObjectType 하위 요소 (#table-276)
  - table 277: formCharPr 요소 (#table-277)
  - table 323: Signature 요소 (#table-323)
  - table 325: ds:SignatureMethod 요소 (#table-325)
  - table 326: ds:SignatureMethod 하위 요소 (#table-326)
  - table 327: switch 요소 (#table-327)
  - table 328: case 요소 (#table-328)

---

## Source: okok1-1-1.md
<a name="source-okok111.md"></a>

정상 텍스트로 복원된 전체 파일
한국산업표준 KS X 6101:2024
개방형 워드프로세서 마크업 언어(OWPML) 문서 구조
Open Word Processor Markup Language(OWPML) document structure
개정일: 2024년 10월 30일
제정일: 2011년 12월 30일
머리말
이 표준은 「산업표준화법」 관련 규정에 따라 산업표준심의회의 심의를 거쳐 개정한 한국산업표준이다. 이에 따라 KS X 6101:2018은 개정되어 이 표준으로 바뀌었다.
이 표준의 내용 일부 또는 전부는 저작권법에 따른 보호 대상이 되는 저작물이 될 수 있다.
이 표준의 내용 일부 또는 전부가 ISO·IEC 등에서 제정한 표준을 참고하여 제정 또는 개정된 경우, 해당 표준의 저작권을 보유하고 있는 ISO·IEC 등의 저작권 보호 규정 등에 따라 보호되어야 한다.
이 표준의 일부가 기술적 성질을 가진 특허권, 출원공개 이후의 특허출원, 실용신안권 또는 출원공개 후의 실용신안등록출원에 저촉될 가능성이 있다는 것에 주의를 환기한다. 관계 중앙행정기관의 장과 산업표준심의회는 이러한 기술적 성질을 가진 특허권, 출원공개 이후의 특허출원, 실용신안권 또는 출원공개 후의 실용신안등록출원에 관계되는 확인에 대하여 책임을 지지 않는다.
개요
이 표준은 2018년 1차 개정이 실시되었지만, 그 후의 개방형 텍스트 문서 관련 기술의 변화와 다양한 추가사항 및 기계 가독성을 높일 수 있는 구조를 포함하는 개방형 텍스트 문서 포맷 시장에 대응하고, 이전 버전에 포함된 스키마 오류를 바로잡고, OWPML 개방형 텍스트 문서 규격을 활용하고자 하는 많은 개발자들에게 보다 상세한 기술적 정보를 제공하여 활용도를 높이기 위하여 개정하였다.
이 표준은 공공 및 민간에서 국내 문서 형식으로 사용되고 있는 HWP 형식의 바이너리 문서 파일에 대한 개방성, 호환성, 보존성을 확보하기 위해 바이너리 포맷보다 개방성과 기술적 해석이 용이한 XML 기반의 패키지 포맷으로 제정되었다. 특히 공공 부문의 경우 업무를 위해 작성된 많은 문서, 공공 영역에서 배포되는 다양한 서식이 HWP 바이너리 또는 개방형 포맷인 HWPX 형식으로 작성되어 처리되고 있으며, XML 기반의 개방형 문서 형식이 아닌 바이너리(HWP 바이너리 문서 형식은 해당 개발사에서 개방성 확보를 위해 공개함) 문서 형식의 사용으로 인해서 기간 시스템 간의 연동 등 다양한 문제가 발생할 수 있다. 또한, 기존에 생성된 다양한 버전의 HWP 바이너리 문서가 기술적 변화로 인해서 문서 및 콘텐츠에 대한 열람, 편집을 보장할 수 없는 경우도 발생할 수 있다. 이에 개방적이며 기존 HWP 바이너리 형식의 문서에 대해 100% 호환성을 제공하고, 문서의 장기 보존에 대한 대비를 위한 기반을 마련하여, 한국의 문서 편집 문화를 잘 표현할 수 있도록 XML 기반의 개방형 문서 표준의 필요에 의해 제정되었다.
이 개방형 표준을 제정함으로써 어느 편집기에서나 HWP 문서 포맷을 지원하도록 처리하는 기술을 개발할 수 있다. 이 표준의 기반이 된 HWPML(Hangeul Word Processor Markup Language)은 1998년에 국내 소프트웨어 업체에서 개발되어 20여 년간 문서 작성, 유통 등 다양하게 사용되어 왔다. 그러나 문서 구성에 필요한 리소스가 분리되지 않고, 일부 의미가 모호하게 정의되어 있으며, DRM 등 기존 표준을 적용하기 어려운 문제가 있어, 이러한 문제점을 개선하고 발전시켜 제정한 형식이 이 표준이다.
특히, OWPML 문서 규격이 달성하고자 하는 목표는 다음과 같다.
워드프로세서 콘텐츠 생성자에게 콘텐츠 생성에 필요한 기술 요소를 제공함으로써 생성된 콘텐츠가 다양한 리딩 시스템(Reading system) 및 콘텐츠 생성 도구에서 생성자의 의도대로 올바르게 표현되고 재수정 될 수 있도록 한다.
기존의 HWP 문서와의 호환성을 반영한다.
콘텐츠 생성 및 표현 방식의 표준을 정의함으로써 HWP 문서의 유통 및 마이그레이션을 지원하고, 기술독립적 환경을 구축한다.
OWPML의 개방성을 높이고 정보 제공의 정확성을 높인다.
기술의 변화에 대비하여 텍스트 형식의 문서의 내용 및 맥락 정보를 장기간 보존할 수 있도록 한다.
이 표준에서 정의하는 형식은 문서 내용에 대한 구조적 정보를 표현하는 XML 기반의 문서 형식과 이에 필요한 공유 리소스들 간의 논리적인 구조 정보, 그리고 이러한 요소들을 하나의 물리적인 파일로 패키징할 수 있는 논리적인 컨테이너 및 물리적 패키징 개념을 도입하였다. 이러한 구성으로 인해서 소프트웨어 편집기에서 OWPML 문서 작성 및 표현 기술 개발 시 필요한 콘텐츠만을 선별적으로 메모리에 적재하여 사용할 수 있는 유연한 문서 파일 형식으로 개발되었다.
또한 W3C XML 암호화 방식과 전자서명 방식 등 기존 표준을 도입하여 보다 신뢰성 있고 개방적인 문서 형식으로 발전하였다.
이 표준은 문서처리기준 및 처리언어(JTC 1/SC 34) 전문위원회에서 표준의 내용 및 방향에 대한 검토 및 바이너리 형식과의 연계성을 검증하는 절차를 거쳐 개발되었다. 표준 제정을 통하여 문서의 마이그레이션, 변환 등에 있어 기술적인 장벽을 제거하고, 문서의 장기보존 시에 발생될 수 있는 기술의 변화 등에도 유연하게 대비할 수 있어 다양한 활용의 기회가 생겼다고 할 수 있다.
1. 적용범위
이 표준에서 규정하고 있는 개방형 워드프로세서 마크업 언어 OWPML(Open Word-Processor Markup Language)은 개방형 문서 형식으로 텍스트 유형의 콘텐츠 표현에 관한 표준이다. 또한 XML 기반의 개방된 형식으로 바이너리 형식의 HWP 문서를 정확하게 기술하기 위해 2018년 1차 개정되었으며, 문서 요소를 추가하고 각각 기존 문서 요소에 상세한 설명과 예제를 추가하여 수요자의 이해를 돕고 문서의 하위 호환성과 사용자의 확장성을 지원하고자 2차 개정되었다.
이 표준은
개방형 텍스트 문서를 표현하는 방식에 대하여
바이너리 HWP 문서 포맷을 100% 호환할 수 있는 문서 규격에 대하여
하위 호환성 증가 방안에 대하여
문서의 메타데이터 추가 및 확장성을 제공하는 방식에 대하여 규정한다.
이 표준은 OWPML(HWPX) 개방형 문서를 생성, 처리 등의 작업을 수행하는 IT 개발자를 위해 필요하며, 기타 OWPML 문서와 OOXML, ODF 등 개방형 문서와의 호환 기술을 개발하는 개발사가 이 표준의 수요자가 된다.
2. 인용표준
다음의 인용표준은 전체 또는 부분적으로 이 표준의 적용을 위해 필수적이다. 발행연도가 표기된 인용표준은 인용된 판만을 적용하며, 발행연도가 표기되지 않은 인용표준은 최신판(모든 추록을 포함)을 적용한다.
KS X ISO 8601: 데이터 요소 및 교환 포맷 — 정보교환 — 날짜 및 시각의 표기
ISO 3166-1: Codes for the representation of names of countries and their subdivisions — Part 1: Country codes
ISO/IEC 26300-1:2015: Open Document Format for Office Applications (OpenDocument) v1.2 - Part 1: OpenDocument Schema
ISO/IEC 26300-3:2015: Open Document Format for Office Applications (OpenDocument) v1.2 - Part 3: Packages
XML 1.1: W3C(The World Wide Web Consortium) Extensible Markup Language(XML) 1.1(Second Edition) 2006
CSS Values and Units Module Level 3: W3C Candidate Recommendation, 01 December 2022
Namespaces in XML 1.1: W3C(The World Wide Web Consortium), Namespaces in XML 1.1 (Second Edition) 2006
Unicode 4.0: The Unicode Consortium, The Unicode Standard, Version 4.0.0
XML-Signature Syntax and Processing Version 1.1: W3C Recommendation 11 April 2013
XML Encryption Syntax and Processing Version 1.1: W3C Recommendation 11 April 2013
MIME MEDIA TYPE: IANA(Internet Assigned Numbers Authority), MIME MEDIA TYPE
3. 용어와 정의
이 표준의 목적을 위하여 다음의 용어와 정의를 적용한다.
<a name="s-3-1-HWPHangeul"></a>
3.1 HWP(Hangeul Word-Processor) 문서: 1989년 이후 (주)한글과컴퓨터에서 개발한 한글 워드프로세서 프로그램으로 생성되는 바이너리 형식의 전자문서
<a name="s-3-2-IDPFInternational"></a>
3.2 IDPF(International Digital Publishing Forum): 국제 디지털 출판 포럼. 전자 출판 산업의 표준을 수립하기 위해 성립된 디지털 출판 산업을 위한 무역 및 표준 협회
<a name="s-3-3-OCFOpen"></a>
3.3 OCF(Open Container Format): IDPF(3.2)에서 정의한 전자책을 위한 포맷 중의 하나인 컨테이너 포맷
<a name="s-3-4-EPUB"></a>
3.4 EPUB Publication: ISO/IEC 23736 표준에서 정의하는 전자책의 논리적 구조 정보를 표현하는 표준
<a name="s-3-5-OPSOpen"></a>
3.5 OPS(Open Publication Structure): IDPF(3.2)에서 정의한 전자책을 위한 공개 출판 구조 포맷
<a name="s-3-6-OPFOpen"></a>
3.6 OPF(Open Packaging Format): IDPF(3.2)에서 정의한 전자책을 위한 공개 패키징 포맷
<a name="s-3-7-EPUB"></a>
3.7 EPUB Content documents: 전자책의 콘텐츠 표현을 위한 표준
<a name="s-3-8-OWPMLOpen"></a>
3.8 OWPML(Open Word-Processor Markup Language): 이 표준에서 정의하는 개방형 워드프로세서 문서 형식
<a name="s-3-9-fall-back"></a>
3.9 대체(fall-back): 동일한 콘텐츠를 표현하는 다른 미디어 형식의 파일을 연결된 정보를 통해 찾아가는 방식으로, 해당 리딩 시스템(3.12)이 처리할 수 있는 파일을 찾는 행위
<a name="s-3-10-ZIP"></a>
3.10 ZIP: 번들링(bundling)과 압축에 대한 파일 포맷
<a name="s-3-11-XML"></a>
3.11 XML 네임스페이스: XML 요소의 이름과 속성의 고유한 URI 형식 식별자
<a name="s-3-12-reading"></a>
3.12 리딩 시스템(reading system): OWPML(3.8) 문서를 읽고, 편집할 수 있는 애플리케이션 또는 시스템
<a name="s-3-13-SP"></a>
3.13 SP 그룹(significant property group): 텍스트 문서 구성 요소 정의 항목에 대한 용어 정의 및 그룹화
<a name="s-3-14-footnote"></a>
3.14 각주(footnote): 본문 내용에 대한 보충 자료를 구체적으로 제시하거나, 인용한 자료의 출처 등을 밝히는 현재 쪽의 맨 끝부분에 놓이는 주석
<a name="s-3-15-sec"></a>
3.15 강조점: 문자열을 강조하는 목적으로 현재 글자의 위, 아래 또는 글자 사이에 찍는 점
<a name="s-3-16-sec"></a>
3.16 개요: 본문의 내용을 간결하게 추려낸 주된 글 내용
<a name="s-3-17-sec"></a>
3.17 개체: 텍스트, 도형(3.32), 그림, 글상자(3.25), 수식(3.45), 표, 글맵시, 소리, 플래시 등의 독립된 기능을 하는 단위
<a name="s-3-18-sec"></a>
3.18 격자: 한 쪽에 들어갈 수 있는 줄 수를 제한하기 위한 표준 줄 간격
<a name="s-3-19-avg"></a>
3.19 계산식: 표(3.64)에서 덧셈, 뺄셈, 곱셈, 나눗셈의 간단한 사칙연산 및 avg와 같은 통계 함수와 sum(left) 등과 같은 left, right, below, above의 범위 지정자로 구성된 식
<a name="s-3-20-sec"></a>
3.20 교정 부호: 맞춤법, 띄어쓰기, 글자 크기, 문장 부호, 줄 바꾸기 등을 바로잡기 위하여 문서에 표시된 부호
<a name="s-3-21-HWP"></a>
3.21 구역: HWP 문서에서 본문의 영역을 구분 짓는 단위
<a name="s-3-22-sec"></a>
3.22 글꼴: 글씨를 써 놓은 모양. 글씨체의 종류를 나타내며, 대표적인 글꼴로는 바탕체, 궁서체, 돋움체 같은 것들이 있다.
<a name="s-3-23-sec"></a>
3.23 글맵시: 글자를 구부리거나 글자에 외곽선, 면 채우기(3.59), 그림자, 회전 등의 효과를 주어 문자를 꾸미는 기능
<a name="s-3-24-bullet"></a>
3.24 글머리표: 여러 개의 항목을 나열할 때 문단(3.36)의 머리에 불릿(bullet) 모양을 붙여서 입력하는 기능
<a name="s-3-25-sec"></a>
3.25 글상자: 문서에 위치와 크기 조절, 개체(3.17) 안의 채우기(3.42) 효과, 테두리의 모양과 색깔 바꾸기 등을 자유자재로 설정하여 글을 담는 상자
<a name="s-3-26-sec"></a>
3.26 글자 격자: 한 줄에 들어갈 수 있는 글자의 수를 제한하기 위한 표준 글자 간격
<a name="s-3-27-sec"></a>
3.27 글자 모양: 글자 색 바꾸기, 기울임, 진하게, 밑줄, 취소선(3.61), 그림자, 양각, 음각, 외곽선, 첨자 등의 다양한 글자의 속성
<a name="s-3-28-sec"></a>
3.28 글자 스타일: 글자를 꾸미기 위해 글꼴(3.22), 글자 크기 등의 글자 모양(3.27)만을 미리 지정한 하나의 형식
<a name="s-3-29-sec"></a>
3.29 글자 위치: 글자의 기준선을 기준으로 위나 아래 위치
<a name="s-3-30-sec"></a>
3.30 다단: 신문이나 회보, 찾아보기 등을 만들 때 읽기 쉽도록 한 쪽을 여러 개로 나눌 때 쓰는 것
<a name="s-3-31-sec"></a>
3.31 덧말: 본문의 아래나 또는 위에 넣는 보충 설명
<a name="s-3-32-sec"></a>
3.32 도형: 직선, 직사각형, 타원, 호, 다각형, 곡선, 자유선, 개체(3.17) 연결선, 글상자(3.25) 등 문서에 삽입하고 편집할 수 있는 개체(3.17)
<a name="s-3-33-header"></a>
3.33 머리말(header): 문서의 한 쪽의 맨 위에 한두 줄의 내용이 쪽마다 고정적으로 반복되는 것
<a name="s-3-34-footer"></a>
3.34 꼬리말(footer): 문서의 한 쪽의 맨 아래에 한두 줄의 내용이 쪽마다 고정적으로 반복되는 것
<a name="s-3-35-memo"></a>
3.35 메모(memo): 현재 입력 중인 문서에서 특정 단어나 블록으로 설정한 문자열에 대해 편집자 기준으로 오른편에 글상자(3.25)가 실행되어 추가 내용을 입력하는 기능
<a name="s-3-36-sec"></a>
3.36 문단: 여러 문장이 이어지다가 문맥에 따라 줄이 바뀌는 부분
<a name="s-3-37-endnote"></a>
3.37 미주(endnote): 본문 내용에 대한 보충 자료를 구체적으로 제시하거나 인용한 자료의 출처 등을 밝히는 현재 구역(3.21)의 맨 끝부분에 놓이는 주석
<a name="s-3-38-sec"></a>
3.38 바탕글 스타일: 문서의 기본 문단(3.36) 스타일
<a name="s-3-39-sec"></a>
3.39 바탕쪽: 문서 전체 쪽에 공통으로 적용되는 모양
<a name="s-3-40-sec"></a>
3.40 상호 참조: 다른 쪽의 그림, 표(3.64) 등을 본문에서 항상 참조할 수 있도록 그 위치를 표시해 주는 기능
<a name="s-3-41-index"></a>
3.41 색인(index): 책이나 학술서, 연구 대상이 된 서적의 내용 중에서 중요한 항목, 술어, 인명, 지명 등을 뽑아 본문 어느 쪽에 위치하는지 바로 찾아볼 수 있도록 쪽 번호와 함께 별도로 배열하여 놓은 목록
<a name="s-3-42-sec"></a>
3.42 선택 글자 보호: 현재 화면에서 편집하고 있는 문서 내용 중 사용자가 블록으로 지정한 영역에 암호를 걸어 사용자가 선택한 문자로 변경하여 개인 정보를 보호하는 기능
<a name="s-3-43-sec"></a>
3.43 세로 정렬: 줄 안에서 각 글자의 위치를 세로로 정렬할 때 글자의 위쪽, 가운데, 아래쪽을 정하여 정렬하는 것
<a name="s-3-44-sec"></a>
3.44 가로 정렬: 줄 안에서 각 글자의 위치를 가로로 정렬할 때 글자의 왼쪽, 가운데, 오른쪽을 정하여 정렬하는 것
<a name="s-3-45-sec"></a>
3.45 수식: 수 또는 양을 나타내는 숫자나 문자를 연산 기호로 연결한 식과 수식(3.45)을 명령어를 이용하여 작성한 것
<a name="s-3-46-hidden"></a>
3.46 숨은 설명(hidden comment): 실제 문서의 내용에는 포함되지 않으면서, 파일을 편집하는 사람에게 필요한 메모(3.35)나 주의사항 등을 기록한 것
<a name="s-3-47-script"></a>
3.47 스크립트(script): 이벤트 속성 또는 양식 개체(3.50)의 이벤트 내용을 실행시키게 하는 것
<a name="s-3-48-style"></a>
3.48 스타일(style): 글꼴(3.22), 크기, 장평(3.54), 자간(3.53), 왼쪽 여백, 오른쪽 여백, 첫 줄, 정렬 방식, 줄 간격(3.57), 문단(3.36) 종류와 같은 문서의 전체적인 꾸밈 정보
<a name="s-3-49-sec"></a>
3.49 시작 번호: 문서 내에서 사용되는 각종 개체들의 번호의 시작 숫자
<a name="s-3-50-sec"></a>
3.50 양식 개체: 편집 화면에 넣을 수 있는 명령 단추, 선택 상자, 콤보 상자, 라디오 단추, 입력 상자의 개체(3.17)
<a name="s-3-51-sec"></a>
3.51 용지 방향: 편집 용지를 좁게 쓸 것인가 넓게 쓸 것인가에 대한 방향 정의
<a name="s-3-52-sec"></a>
3.52 용지 여백: 선택한 용지 설정에서 본문, 머리말(3.33), 꼬리말(3.34), 각주(3.14) 영역을 제외한 편집 용지상의 나머지 상하좌우 여백
<a name="s-3-53-sec"></a>
3.53 자간: 글자와 글자 사이의 간격
<a name="s-3-54-sec"></a>
3.54 장평: 글자의 가로/세로 비율. 글자의 세로 길이는 그대로 유지하면서 글자의 가로 폭을 줄이거나 늘리는 것
<a name="s-3-55-sec"></a>
3.55 조판 부호: 편집 과정에서 사용자가 내리는 명령을 문서에 기록하여 나타내는 부호
<a name="s-3-56-comment"></a>
3.56 주석(comment): 각주(3.14), 미주(3.37), 숨은 설명의 통칭
<a name="s-3-57-sec"></a>
3.57 줄 간격: 지금 줄의 맨 위부터 다음 줄의 맨 위까지의 간격
<a name="s-3-58-sec"></a>
3.58 차례: 책이나 글 따위에서 따로 적어 놓은 항목
<a name="s-3-59-sec"></a>
3.59 채우기: 문서에서 표현되는 모든 개체의 면을 지정된 색과 지정된 패턴으로 채우는 기능
<a name="s-3-60-bookmark"></a>
<a name="hp-bookmark"></a>
3.60 책갈피(bookmark): 문서를 편집하는 도중에 본문의 임의의 곳에 표시를 해 두었다가 현재 커서의 위치에 상관없이 표시해 둔 곳으로 커서를 곧바로 이동시키는 기능
<a name="s-3-61-strikeout"></a>
3.61 취소선(strikeout): 선택한 단어나 블록 지정한 부분에 다양한 선과 모양으로 취소를 의미하는 선
<a name="s-3-62-caption"></a>
3.62 캡션(caption): 본문에 들어가는 그림, 표(3.64), 그리기 개체(3.17), 수식(3.45)에 필요에 따라 번호와 제목, 간단한 설명을 붙이는 것
<a name="s-3-63-sec"></a>
3.63 편집 용지: 어떤 크기의 용지에 편집할 것인지, 용지 방향(3.51), 용지 여백(3.52) 등에 대한 설정
<a name="s-3-64-table"></a>
3.64 표(table): 문서를 만들면서 복잡한 내용이나 수치 자료를 일목요연하게 정리하고자 할 때 이용하는 것
<a name="s-3-65-hyperlink"></a>
3.65 하이퍼링크(hyperlink): 문서의 특정한 위치에 현재 문서나 다른 문서, 웹 페이지, 전자 우편 주소 등을 연결하여 쉽게 참조하거나 이동할 수 있게 해 주는 것
<a name="s-3-66-sec"></a>
3.66 전자서명: 문서에 디지털 서명을 하는 기능
<a name="s-3-67-sec"></a>
3.67 변경 추적: 문서의 추가, 삭제, 서식 변경사항과 같은 수정내역을 기록하여 변경된 내용을 확인할 수 있는 기능
<a name="s-3-68-sec"></a>
3.68 절대단위: 문서 내 다양한 수치를 나타내는 단위로, 물리적인 고정 값과 연관된 값을 나타내는 단위
<a name="s-3-69-sec"></a>
3.69 상대단위: 문서 내 다양한 수치를 나타내는 단위로, 기준으로부터 상대적인 크기를 값으로 나타내는 단위
4. 적합성
<a name="s-4-1-sec"></a>
4.1 일반사항
이 표준에 따라 생성된 OWPML(HWPX) 문서는 표준 적합성을 평가할 수 있다. 또한 OWPML 표준 문서 형식을 해석하여 편집 문서로 읽을 수 있는 리딩 시스템에 대해서도 성능이나 호환성 평가를 수행할 필요가 있다. 이 경우 아래 세부 사항에 따라 평가할 수 있다.
<a name="s-4-2-OWPML"></a>
4.2 OWPML XML 콘텐츠 문서의 조건
이 표준에서 정의하는 콘텐츠 문서는 다음 조건을 만족해야 한다.
OWPML에 포함된 XML 문서는 이 표준에서 정의한 스키마를 만족하는 유효한(valid) XML 문서여야 한다.
모든 XML 문서의 기본 인코딩 형식은 UTF-8을 사용해야 한다.
모든 XML 문서의 MIMETYPE은 application/xml 미디어 유형을 지녀야 한다.
<a name="s-4-3-sec"></a>
4.3 리딩 시스템의 적합성
이 표준은 리딩 시스템에 대해 한 단계의 적합성만을 정의한다. 리딩 시스템은 다음과 같이 문서를 처리할 때에만 적합성을 인정받을 수 있다.
OWPML 콘텐츠 문서를 처리할 때 리딩 시스템은 반드시 다음 조건을 충족해야 한다.
정형성(well-formedness)과 오류의 처리 등을 포함한 XML 1.1 규격의 원칙에 따라 XML을 처리해야 한다.
대체(fall-back) 부재 시, 지원되지 않는 미디어 유형의 <img> 또는 object 요소를 무시하고 문서를 표현하는 단계(렌더링)를 수행하지 않아야 한다.
‘XML 네임스페이스와의 관계’에서 정의된 것과 같이, 적합한 네임스페이스 규칙의 존재를 존중해야 한다.
<a name="s-4-4-OWPML"></a>
4.4 OWPML 문서 호환성 및 적합성 조건
이 표준은 텍스트형 문서에 대한 개방형 포맷으로 다양한 텍스트형 문서와의 호환성 및 본 표준에 대한 적합성을 판단하는 데 보다 명확한 기준을 제시하기 위해 문서 내 지원되는 콘텐츠 요소를 SP(Significant Property)로 구분하여 호환성 및 적합성을 4단계로 나누어 정의한다.
레벨 0 (Level 0): SP0 그룹의 콘텐츠 요소가 지원 대상에 포함되어야 한다. (용어정의 3.13 - 3.18 항목)
레벨 1 (Level 1): SP1 그룹의 콘텐츠 요소가 지원 대상에 포함되어야 한다. (용어정의 3.19 - 3.24 항목)
레벨 2 (Level 2): 레벨 1 단계를 지원하고 SP2 그룹의 콘텐츠 요소가 지원 대상에 포함되어야 한다. (용어정의 3.25 - 3.43 항목)
레벨 3 (Level 3): 레벨 1, 2 단계를 지원하고 SP3 그룹의 콘텐츠 요소가 지원 대상에 포함되어야 한다. (용어정의 3.44 - 3.64 항목)
SP 그룹	SP0 항목	SP1 항목	SP2 항목	SP3 항목
문서 요소	3.13-3.18	3.19-3.24	3.25-3.43	3.44-3.64
5. 다른 기술 표준과의 관계
이 표준과 관련되거나 포함되는 기술 표준과의 관계를 설명한다.
<a name="s-5-1-XML"></a>
5.1 XML과의 관계
이 표준은 XML을 기반으로 한다. 이는 XML의 일관성과 단순성 때문이며, XML 문서는 앞으로 등장할 새로운 기술에 잘 적응할 것으로 기대되기 때문이다. 또한 XML 기반 문서의 논리적 구조를 설정하는 문법 정의를 위한 정형화된 규칙을 제공하며, 이는 기술 구현자들의 업무 시간과 비용을 절감시키고 시스템 간 호환성을 높이는 이점이 있다. 또한, XML은 확장이 가능하다. 즉, XML은 특정 문서유형이나 특정 유형의 요소 집합에 독점적이지 않아 문서의 일부분을 보다 직접적으로 추가할 수 있는 문서 마크업을 활성화하여 자동 포맷팅 등의 컴퓨터 처리작업을 통해 수정할 수 있도록 한다.
XML 1.1에 정의된 대로 리딩 시스템은 반드시 XML 프로세서이어야 한다. 모든 OWPML 콘텐츠 문서들은 반드시 해당 스키마에 따라 유효한 XML 문서이어야 한다.
<a name="s-5-2-XML"></a>
5.2 XML 네임스페이스와의 관계
리딩 시스템은 반드시 http://www.w3.org/TR/xml-names11/의 XML 네임스페이스 권고사항에 따라 XML 네임스페이스를 처리해야 한다.
네임스페이스 접두어는 각기 다른 XML 어휘에서 따온 동일한 명칭을 구분해야 한다. XML 문서의 XML 네임스페이스 선언은 고유한 네임스페이스 접두어를 고유한 URI에 연계시킨다. 이 접두어는 문서의 요소 이름이나 속성 이름에 사용될 수 있다. 반면, XML 문서 내의 네임스페이스 선언은 URI를 기본 네임스페이스로 식별하여 네임스페이스 접두어를 가지지 못한 요소들에 적용된다. OWPML 문서는 아래와 같은 형식으로 네임스페이스를 선언하여 활용하며, 본 표준의 개정 수준에 따라 네임스페이스는 변경하여 문서의 버전을 확인하는 데 활용될 수 있다.
보기:
code
Xml
xmlns:hh="http://www.owpml.org/owpml/2024/head"
xmlns:hb="http://www.owpml.org/owpml/2024/body"
xmlns:hp="http://www.owpml.org/owpml/2024/paragraph"
xmlns:hc="http://www.owpml.org/owpml/2024/core"
xmlns:hv="http://www.owpml.org/owpml/2024/version"
xmlns:hm="http://www.owpml.org/owpml/2024/master-page"
xmlns:hs="http://www.owpml.org/owpml/2024/history"
모든 OWPML 문서의 최상위 요소는 반드시 문서의 네임스페이스를 명확하게 명시해야 한다. OWPML 네임스페이스가 문서에서 사용되는 경우, 반드시 http://www.owpml.org/owpml/2024/head 또는 http://www.owpml.org/owpml/2024/body 등으로 명확히 선언되어야 한다. 네임스페이스 접두어가 사용된 경우, 저자들에게 hh 또는 hb 접두어를 사용하여 이 네임스페이스로 바인딩하고, hh, hb를 다른 네임스페이스의 접두어로 사용하지 않을 것을 권고한다.
보기:
code
Xml
<head xmlns="http://www.owpml.org/owpml/2024/head">
<a name="s-5-3-sec"></a>
5.3 유니코드와의 관계
HWP 문서들은 유니코드에 정의된 것과 같이 UTF-8 인코딩을 사용하여 전체 유니코드 문자 집합을 사용할 수 있다. 유니코드의 사용으로 국제화, 그리고 여러 가지 언어로 문서를 작성하는 일이 쉬워진다. 하지만, 리딩 시스템은 모든 유니코드 문자에 대해 글자(glyph)를 제공하지 않을 수 있다.
리딩 시스템은 반드시 UTF-8 문자를 제대로 파싱(parse)해야 한다. 리딩 시스템은 일부 문자의 표시를 거부할 수 있지만, 표시할 수 없는 문자가 있다는 사실을 반드시 표시해야 한다. 리딩 시스템은 유니코드 문자를 구성하는 바이트(byte)를 개별 문자로 표시해서는 안 된다.
리딩 시스템의 지속적 검색 및 분류작업을 지원하기 위해서, 유니코드 정규화 양식 C(Unicode Normalization Form C, NFC)를 반드시 사용해야 한다. (http://www.w3.org/TR/charmod-norm/ 참조)
<a name="s-5-4-MIME"></a>
5.4 MIME 미디어 유형
이 표준은 모든 리딩 시스템이 반드시 지원하고 HWP 문서 파일이 포함할 수 있는 OWPML 핵심 미디어 유형의 목록을 정의한다. 핵심 미디어 유형 이외의 형식을 추가하는 경우에는 IANA(Internet Assigned Numbers Authority)의 공식 미디어 형식 목록에 따라 표기해야 한다.
OWPML 핵심 미디어 유형은 다음과 같다.
<a name="table-1"></a>
표 1 — MIME 미디어 유형
| MIME 미디어 유형 | 참조 | 기술 |
| :--- | :--- | :--- |
| image/gif | http://www.w3.org/Graphics/GIF/spec-gif89a.txt | 래스터(Raster) 이미지에 사용 |
| image/jpeg | http://www.w3.org/Graphics/JPEG/ | 래스터(Raster) 이미지에 사용 |
| image/png | RFC 2083 | 래스터(Raster) 이미지에 사용 |
| application/xml | http://www.w3.org/TR/xml11/ | 외부 XML 콘텐츠에 사용 |
| application/javascript | http://www.ecma-international.org/publications/standards/Ecma-262.htm | 양식 객체의 스크립트에 사용 |
6. OWPML 스키마 구성
이 표준에서 기술하고 있는 OWPML 문서의 논리적 구조를 정의하는 XML 스키마는 5가지로 구성된다.
첫째는 문서 내에서 사용되는 모든 설정을 가지고 있는 header 스키마이다. header에는 구역에 대한 정의, 금칙 문자, 글꼴, 테두리/배경, 각종 객체에 대한 연결 정보 등이 들어있다.
둘째는 실제 문서 내용이 들어가는 Body 스키마이다. Body에는 사용자가 설정한 문서의 레이아웃대로 문서의 내용만이 저장된다.
셋째는 문서에 공통으로 적용되는 바탕쪽 설정이 들어있는 스키마이다.
넷째는 문서 이력 스키마이다. 문서 이력 정보는 추가/수정되었던 기록을 담고 있다.
다섯째는 패키지 포맷에 대한 정의 스키마로, 콘텐츠의 메타데이터를 담고 있다.
각 XML 스키마에 대한 구체적인 내용 설명은 다음 장부터 설명한다. 각 스키마에 대한 상세한 스키마 정의는 첨부된 [부속서] XML 스키마 문서 5종을 참조한다.
7. 기본 형식 및 단위
<a name="s-7-1-sec"></a>
7.1 기본 형식
OWPML 문서는 리딩 시스템에 따라 다양한 단위로 글자 크기, 문단 간격 등 콘텐츠의 서식을 표현한다. 그러나 OWPML의 내부 논리적 구조 정보를 정의할 때는 한 가지 기본적으로 정해지는 단위가 필요하다. 이 장에서는 XML 스키마를 통해 정의되는 OWPML 문서에서 기본적으로 사용되는 단위(Unit)에 대해서 설명한다. 단위는 기본적으로 절대단위와 상대단위로 나뉘며, 절대 단위는 전자문서의 출력장치(모니터)의 물리적 속성을 아는 경우 효율적이며, 상대 단위는 이기종 간, 플랫폼 간의 호환성을 유지하는 데 편리하게 사용되는 단위이다.
<a name="s-7-2-sec"></a>
7.2 단위
<a name="s-7-2-1-sec"></a>
7.2.1 상대단위
기준이 되는 길이로부터 상대적인 값을 측정하는 길이를 상대 길이라고 하며, 이를 표현하는 단위를 상대단위라고 한다. OWPML 문서를 표현하는 데 절대단위 또는 상대단위를 사용해야 한다. 자세한 사항은 W3C CSS Values and Units Module Level 3 표준을 참고하기 바란다.
<a name="s-7-2-2-sec"></a>
7.2.2 절대단위
절대 길이 단위는 물리적인 측정 장치와 연결되어 있으며 상호 고정되어 있는 단위를 말한다. 이 단위는 cm, mm, pt 등 물리적인 단위로 구성된다. 자세한 사항은 W3C CSS Values and Units Module Level 3 표준을 참고하기 바란다.
<a name="s-7-2-3-HWPUNIT"></a>
7.2.3 HWPUNIT
이 표준에서 정의하는 OWPML 텍스트 형식의 문서는 OOXML, ODF 등 텍스트형 문서를 표현하는 개방형 문서 표준들과의 호환성을 높이기 위해 상호 변환 오차를 최소화할 수 있도록 정의된 HWPUNIT이라는 단위를 사용해야 한다. HWPUNIT은 본 표준 및 바이너리 HWP 문서 형식에서 사용되는 공통 단위이며, 모든 단위가 표시되지 않는 속성 값들은 암묵적으로 단위를 HWPUNIT으로 해석해야 한다. 이 단위 크기에 대한 정의는 다음과 같다.
10 pt = 1000 HWPUNIT
<a name="s-7-2-4-HWPUNIT"></a>
7.2.4 HWPUNIT과 다른 단위와의 관계
HWPUNIT은 CSS의 절대 단위와 아래와 같은 값의 관계를 갖는다.
1 pt = 100 hwpunit
1 mm = 283.456 hwpunit
1 cm = 2834.56 hwpunit
1 inch = 7200 hwpunit
1 pixel = 75 hwpunit
1 char = 500 hwpunit
1 twips = 5 hwpunit
<a name="s-7-2-5-sec"></a>
7.2.5 기타 단위 표현
이 표준에서 HWPUNIT 단위를 사용하는 경우 대부분 암시적으로 단위를 사용한다. 하지만 명시적으로 단위를 기술해야 하는 경우도 있다. 아래는 명시적으로 단위를 기술할 때 사용되는 XML 요소 형식(Complex Type)이다.
<a name="table-2"></a>
표 2 — HWPValue 형식
| 속성 이름 | 설명 |
| :--- | :--- |
| value | 실제 값 |
| unit | 값의 단위 |
속성 unit에 올 수 있는 값은 HWPUNIT, CHAR 등이며, 기본값은 CHAR이다.
예시 1: HWPValue 형식
code
Xml
```xml
<hh:margin>
    <hh:intent value="0" unit="HWPUNIT"/>
    <hh:left value="0" unit="HWPUNIT"/>
    <hh:right value="0" unit="HWPUNIT"/>
    <hh:prev value="0" unit="HWPUNIT"/>
    <hh:next value="1600" unit="HWPUNIT"/>
</hh:margin>
<hh:lineSpacing type="PERCENT" value="160" unit="HWPUNIT"/>
```
<a name="s-7-3-OWPML"></a>
7.3 OWPML의 기본 자료 형식
OWPML에서 사용되는 기본 값들의 형태는 다음 표에 명시되어 있다.
(표 3 ~ 8: 각종 번호, 선 형식 등은 내용이 방대하여 생략되었으나, 원본 문서에 포함되어 있음)
<a name="s-7-4-OWPML"></a>
7.4 OWPML의 색상 표현
OWPML 문서 내의 색상 표현은 16진수(Hex) 형식으로 표현될 수 있다. 이 값은 기본적으로 문자열이며, # 기호를 앞에 붙여 나타낸다.
<a name="table-9"></a>
표 9 — 색상 형식
| 속성 | 설명 |
| :--- | :--- |
| Base Type | xs:string |
| Extend Type| HEX value |
| Pattern | #[0-9A-Fa-f]{6} |
| Example | #01F39B |
8. 컨테이너 및 패키징
<a name="s-8-1-OCF"></a>
8.1 OCF
OWPML 문서는 콘텐츠를 구성하는 여러 파일들을 물리적으로 하나의 파일로 묶기 위해 개방형 컨테이너 포맷인 OCF(Open Container Format) 규격을 기반으로 생성되어야 한다.
<a name="s-8-2-OCF"></a>
8.2 OCF OWPML 프로파일
OWPML은 OCF에서 사용되는 기본 파일 및 디렉터리 외에 추가적인 파일 및 디렉터리를 사용한다. 그 중 version.xml은 필수적으로 사용되어야 하는 파일로써 OWPML 파일 형식에 대한 버전 정보를 가지고 있는 파일이다. 그 외의 디렉터리들은 선택적으로 사용된다.
ZIP Container
mimetype
version.xml
META-INF/
container.xml
manifest.xml (선택)
metadata.xml (선택)
signatures.xml (선택)
encryption.xml (선택)
rights.xml (선택)
Preview/
PrvText.txt
PrvImage.png
Chart/
chart1.xml
Contents/
content.hpf
header.xml
section0.xml
BinData/
img0.jpg
Scripts/
default.js
XMLTemplate/
TemplateSchema.xsd
DocHistory/
VersionLog0.xml
Custom/
Bibliography.xml
<a name="s-8-3-sec"></a>
8.3 파일 형식 버전 식별
OWPML을 준수하는 OCF 컨테이너는 최상위 디렉터리의 직접 자식으로서 version.xml을 가지고 있어야 하며, 이 파일 안에는 파일 형식에 대한 버전을 기록하고 있어야 한다.
major: 문서 형식의 구조가 완전히 바뀌는 것을 나타낸다.
minor: 큰 구조는 동일하나, 큰 변화가 있는 것을 나타낸다.
micro: 구조는 동일하나, 하위 요소가 추가된 것을 나타낸다.
buildNumber: 하위 요소에 정보가 추가된 것을 나타낸다.
예시: version.xml
---

## Source: okok1-1-2.md
<a name="source-okok112.md"></a>


다음은 요청하신 KS X 6101 표준 문서의 OCR 결과물을 수정한 내용입니다.
8.3 파일 형식 버전 식별
리딩 시스템이 OWPML 문서를 제대로 처리하기 위해서는 파일 형식 외에도 파일 형식에 대한 버전 식별이 필요하다. 가령 같은 OWPML 문서 파일 형식이라도 2.x의 구조와 3.x의 구조가 크게 다를 수 있고, 리딩 시스템이 2.x까지만을 지원한다고 하면 3.x의 문서 파일은 사용자를 위한 처리를 해야 한다. 이를 위해서는 파일 형식 버전 정보를 컨테이너의 특정 파일에 기록해야 한다.
OWPML 부합화된 OCF 컨테이너는 최상위 디렉터리의 직접 자식으로서 version.xml을 가지고 있어야 하며, 이 version.xml 파일 안에는 파일 형식에 대한 버전을 기록하고 있어야 한다. 다음은 version.xml에 대한 XML 스키마이다.
<a name="figure-2"></a>
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
<a name="hv-HCFVersion"></a>
<hv:HCFVersion xmlns:hv="http://www.owpml.org/owpml/2024/version" targetApplication="WORDPROCESSOR" major="5" minor="1" micro="0" buildNumber="1" xmlVersion="1.2" application="Hancom Office Hangul" appVersion="11.0.0.2129 WIN32LEWindows_r"/>
<a name="s-8-4-OPF"></a>
8.4 OPF OWPML 프로파일
<a name="s-8-4-1-OPF"></a>
8.4.1 OPF 도입
OWPML은 기본 OPF 스펙에서 몇 가지 요소를 추가해서 사용한다. OWPML 도입 내용은 다음과 같다.
<a name="s-8-4-2-OPF"></a>
8.4.2 OPF 적용 요소
<package> - <manifest> - <item>의 속성 추가 사항은 아래 그림 3과 같다.
OPF의 manifest 정보만으로는 OWPML에서 사용하기에 부족하다. 이에 따라 @isEmbedded 속성과 @sub-path 속성을 추가하였다. 두 속성은 OWPML 부합화된 OPF에서는 반드시 사용되어야 하는 필수 속성으로, @isEmbedded 속성은 선언된 리소스가 컨테이너 내에 포함되어 있는지를 나타내기 위한 속성이며, @sub-path 속성은 컨테이너 내에서 찾을 수 없는 리소스를 외부에서 찾기 위한 경로를 지정하는 속성이다.
<a name="s-8-4-3-Metadata"></a>
8.4.3 Metadata profile
Metadata 요소는 하위 요소로 문서 내용에 대한 메타데이터를 가지고 있어야 한다. 메타데이터는 DublinCore 메타데이터 표준을 사용할 수 있다.
관련 URL: http://dublincore.org/
<a name="table-10"></a>
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
<a name="example-4"></a>
예 4 — metadata의 예
code
Xml
```xml
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
```
9. Header XML 스키마
<a name="s-9-1-sec"></a>
9.1 네임스페이스
Header XML은 기본적으로 "http://www.owpml.org/owpml/2024/head"를 기본 네임스페이스로 사용한다. 기본 네임스페이스의 접두어(prefix)는 기본적으로 'hh'를 사용한다. 잘못된 사용을 줄이기 위해서 'hh'를 기본 네임스페이스("http://www.owpml.org/owpml/2024/head") 이외의 네임스페이스에 사용하지 않을 것을 권고한다.
<a name="s-9-2-1-sec"></a>
9.2.1 헤더 구조
<head> 요소는 header.xml 파일에서 최상위 요소로서, 문서 내용에 관련된 모든 설정을 하위 요소로 가지고 있다. <head> 요소는 네 개의 하위 요소를 가질 수 있다. 각 하위 요소에 대한 설명은 다음에 오는 항들에서 자세하게 설명한다.
<a name="table-11"></a>
표 11 — head version
속성 이름	설명
version	OWPML Header XML의 버전. 이 문서 기준으로 현재 버전은 1.0이다.
<a name="table-12"></a>
표 12 — head 속성
하위 요소 이름	설명
beginNum	문서 내에서 각종 객체들의 시작 번호 정보를 가지고 있는 요소
refList	본문에서 사용될 각종 데이터에 대한 맵핑 정보를 가지고 있는 요소
forbiddenWordList	금칙 문자 목록을 가지고 있는 요소
compatibleDocument	문서 호환성 설정
trackchangeConfig	변경 추적 정보와 암호 정보를 가지고 있는 요소
docOption	연결 표시 정보와 저작권 관련 정보를 가지고 있는 요소
metaTag	메타태그 정보들을 가지고 있는 요소
<a name="s-9-2-2-beginNum"></a>
9.2.2 beginNum 요소
<beginNum> 요소는 문서 내에서 사용되는 각종 객체들의 번호의 시작 숫자를 설정하기 위한 요소이다. 기본적으로 시작 번호는 1에서 시작되며, 사용자 설정에 의해서 1 이외의 번호에서 시작할 수 있게 된다. 시작 번호를 재정의할 수 있는 객체에는 '쪽 번호', '각주', '미주', '그림', '표', '수식' 등이 있다.
<a name="figure-6"></a>
그림 6 — <beginNum>의 구조
<a name="table-13"></a>
표 13 — beginNum 속성
속성 이름	설명
page	페이지 시작 번호
footnote	각주 시작 번호
endnote	미주 시작 번호
pic	그림 시작 번호
tbl	표 시작 번호
equation	수식 시작 번호
<a name="example-5"></a>
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
<a name="s-9-2-5-compatibleDocument"></a>
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
<a name="s-9-2-5-2-layoutcompatibility"></a>
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
<a name="s-9-2-6-trackChangeConfig"></a>
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
<a name="s-9-2-7-docOption"></a>
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
<a name="s-9-2-8-metaTag"></a>
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
<a name="s-9-3-sec"></a>
9.3 문서 설정 정보
<a name="s-9-3-1-sec"></a>
9.3.1 문서 설정
문서 설정 정보는 문서 내에서 사용되는 각종 글꼴 정보, 글자 모양 정보, 테두리/배경 정보와 같이 문서의 레이아웃 설정 및 모양 설정을 가지고 있다.
<a name="s-9-3-2-fontfaces"></a>
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
<a name="s-9-3-3-borderFills"></a>
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
<a name="s-9-3-4-charProperties"></a>
9.3.4 charProperties 요소
콘텐츠 내에서 글자 모양 정보는 반드시 한 개 이상 정의되어 있어야 한다.
표 44 — charProperties 요소
속성 이름	설명
itemCnt	글자 모양 정보의 개수
글자 모양 설정 정보를 표현하기 위한 요소이다.
<a name="hp-charPr"></a>
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
<a name="s-9-3-5-tabProperties"></a>
<a name="hp-tabProperties"></a>
9.3.5 tabProperties 요소
탭 정보 목록을 가지고 있는 요소이다.
표 58 — tabProperties 요소
속성 이름	설명
itemCnt	탭 정보의 개수
<a name="hp-tabPr"></a>
표 60 — tabPr 요소
속성 이름	설명
id	탭 정보를 구별하기 위한 아이디
autoTabLeft	문단 왼쪽 끝 자동 탭 여부 (내어쓰기용)
autoTabRight	문단 오른쪽 끝 자동 탭 여부
탭의 모양 및 위치 정보 등을 표현하기 위한 요소이다.
<a name="s-9-3-6-numberings"></a>
<a name="hp-numberings"></a>
9.3.6 numberings 요소
문단 번호 모양 정보 목록을 가지고 있는 요소이다.
표 63 — numberings 요소
속성 이름	설명
itemCnt	문단 번호 모양 정보의 개수
각 번호/글머리표 문단 머리의 정보이다.
<a name="hp-paraHead"></a>
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
<a name="s-9-3-7-bullets"></a>
<a name="hp-bullets"></a>
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
<a name="s-9-3-8-paraProperties"></a>
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
---

## Source: okok1-1-3.md
<a name="source-okok113.md"></a>

<a name="s-9-3-8-2-paraPr"></a>
<a name="hp-paraPr"></a>
9.3.8.2 paraPr 요소
<a name="s-9-3-8-2-1-paraPr"></a>
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
<a name="s-9-3-8-2-2-align"></a>
<a name="hp-align"></a>
9.3.8.2.2 align 요소
문단 내 정렬 방식을 표현하기 위한 요소이다.
그림 51 — <align>의 구조
샘플 35 — align 예
<hh:align horizontal="JUSTIFY" vertical="BASELINE"/>
<a name="s-9-3-8-2-3-heading"></a>
<a name="hp-heading"></a>
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
<a name="s-9-3-8-2-4-breakSetting"></a>
<a name="hp-breakSetting"></a>
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
<a name="s-9-3-8-2-5-margin"></a>
<a name="hp-margin"></a>
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
<a name="s-9-3-8-2-6-lineSpacing"></a>
<a name="hp-lineSpacing"></a>
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
<a name="s-9-3-8-2-7-border"></a>
<a name="hp-border"></a>
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
<a name="s-9-3-8-2-8-autoSpacing"></a>
<a name="hp-autoSpacing"></a>
9.3.8.2.8 autoSpacing 요소
문단 내에서 한글, 영어, 숫자 사이의 간격에 대한 자동 조절 설정 정보를 가지고 있는 요소이다.
그림 57 — <autoSpacing>의 구조
표 82 — autoSpacing 요소
속성 이름	설명
eAsianEng	한글과 영어 간격을 자동 조절 여부
eAsianNum	한글과 숫자 간격을 자동 조절 여부
샘플 41 — autoSpacing 예
<hh:autoSpacing eAsianEng="0" eAsianNum="0"/>
<a name="s-9-3-9-styles"></a>
9.3.9 styles 요소
<a name="s-9-3-9-1-styles"></a>
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
<a name="s-9-3-9-2-style"></a>
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
<a name="s-9-3-10-memoProperties"></a>
9.3.10 memoProperties 요소
<a name="s-9-3-10-1-memoProperties"></a>
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
<a name="s-9-3-10-2-memoPr"></a>
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
<a name="s-9-3-11-trackChanges"></a>
9.3.11 trackChanges 요소
<a name="s-9-3-11-1-trackChanges"></a>
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
<a name="s-9-3-11-2-trackChange"></a>
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
<a name="s-9-3-12-trackChangeAuthors"></a>
9.3.12 trackChangeAuthors 요소
<a name="s-9-3-12-1-trackChangeAuthors"></a>
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
<a name="s-9-3-12-2-trackChangeAuthor"></a>
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
<a name="s-10-1-sec"></a>
10.1 네임스페이스
Body XML은 기본적으로 "http://www.owpml.org/owpml/2024/body"를 기본 네임스페이스로 사용한다. 기본 네임스페이스의 접두어(prefix)는 기본적으로 "hp"를 사용한다. 잘못된 사용을 막기 위해서 "hp"를 기본 네임스페이스("http://www.owpml.org/owpml/2024/body") 이외의 네임스페이스에 사용하지 않는 것을 권고한다.
<a name="s-10-2-sec"></a>
10.2 본문 개요
그림 66 — 논리적 구조
본문의 논리적인 구조는 ‘본문-구역-문단’이다. 위의 그림은 논리적인 구조를 도식화한 그림이다. 본문은 구역들의 목록으로 구성된다. 이 문서에서 서술하는 규격에서는 본문(Body)이 따로 존재하지 않고, 각 구역(Section)이 개별 파일로 저장된다. 구역은 반드시 한 개 이상 존재해야 하며, 한 구역은 반드시 한 개 이상의 문단을 가지고 있어야 한다. 표나 상자 같은 특수한 경우, 문단은 다시 문단 목록을 가지고 있을 수 있다. 이 경우 문단은 여러 개의 문단 목록을 자식 요소로서 가지고 있을 수 있다. 문단은 실제 문서 내용이 가지고 있는 단위로, 단순 텍스트뿐만 아니라 표, 그림, 그리기 객체 등 멀티미디어 요소를 가질 수 있다.
<a name="s-10-3-sec"></a>
10.3 sec 요소
<sec> 요소는 구역을 나타낸다. 내부적으로 구역에 대한 설정 정보를 가지며, 이에 대한 자세한 내용은 10.6을 참조한다.
표 95 — sec 요소
하위 요소 이름	설명
p	문단
<a name="s-10-4-p"></a>
<a name="hp-p"></a>
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
<a name="s-10-5-run"></a>
<a name="hp-run"></a>
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
<a name="s-10-6-secPr"></a>
<a name="hp-secPr"></a>
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
<a name="hp-pagePr"></a>
pagePr	용지 설정 정보
<a name="hp-footNotePr"></a>
footNotePr	각주 모양 정보
<a name="hp-endNotePr"></a>
endNotePr	미주 모양 정보
pageBorderFill	쪽 테두리/배경 정보
<a name="hp-masterPage"></a>
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
<a name="s-10-7-Ctrl"></a>
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
<a name="s-10-7-1-colPr"></a>
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
<a name="s-10-7-2-fieldBegin"></a>
10.7.2 fieldBegin 요소
메모, 외부 연결, 북마크 등 문서 내에서 부가적인 기능을 표현하기 위한 요소이다.
표 131 — fieldBegin 요소
속성 이름	설명
id	필드 시작을 구별하기 위한 아이디
type	필드 종류
name	필드 이름
editable	읽기 전용 상태에서도 수정 가능한지 여부
fieldid	필드 객체 ID

---

## Source: okok1-2-1.md
<a name="source-okok121.md"></a>

<a name="s-10-7-2-2-CLICK_HERE"></a>
10.7.2.2 CLICK_HERE
누름틀은 문서마당을 불러왔을 때 화면에 표시된 문서마당의 빈 곳을 채워 넣을 안내문과 안내문에 대한 간단한 메모 내용을 입력하는 기능이다.
<a name="s-10-7-2-2-1-sec"></a>
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
<a name="s-10-7-2-3-HYPERLINK"></a>
10.7.2.3 HYPERLINK
<a name="s-10-7-2-3-1-HYPERLINK"></a>
10.7.2.3.1 HYPERLINK
하이퍼링크는 문서의 특정한 위치에 현재 문서나 다른 문서, 웹 페이지, 전자우편 주소 등을 연결하여 쉽게 참조하거나 이동할 수 있게 해 주는 기능이다.
문서 내에서 그룹 객체를 사용할 경우 하이퍼링크 종류를 결정할 수 없는 경우가 발생할 수 있다. 각 개별 객체별로 하이퍼링크를 사용하고, 이 객체들을 하나의 그룹으로 묶을 경우 그룹 객체가 생성된다. 이때 생성된 그룹 객체는 그룹 내 객체들이 모두 같은 내용의 하이퍼링크 설정을 가지고 있지 않다면 하이퍼링크 종류, 하이퍼링크 대상, 문서창 옵션 등을 결정할 수 없게 된다. 이런 경우 그룹 객체의 하이퍼링크 설정은 HWPHYPERLINK_TYPE_DONTCARE, HWPHYPERLINK_TARGET_DOCUMENT_DONTCARE, HWPHYPERLINK_JUMP_DONTCARE의 값을 가져야 한다.
<a name="s-10-7-2-3-2-sec"></a>
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
<a name="s-10-7-2-4-BOOKMARK"></a>
10.7.2.4 BOOKMARK
<a name="s-10-7-2-4-1-BOOKMARK"></a>
10.7.2.4.1 BOOKMARK
두꺼운 책을 읽을 때 책의 중간에 책갈피를 꽂아 두고 필요할 때마다 쉽게 펴보듯이, [책갈피] 기능은 문서를 편집하는 도중에 본문의 여러 곳에 표시를 해 두었다가 현재 커서의 위치에 상관없이 표시해 둔 곳으로 커서를 곧바로 이동시키는 기능이다.
<a name="s-10-7-2-4-2-XML"></a>
10.7.2.4.2 XML 예
샘플 74 — BOOKMARK 예
code
Xml
<fieldBegin id="fb03" type="BOOKMARK" name="txn01" editable="false" dirty="false"/>
<a name="s-10-7-2-5-FORMULA"></a>
10.7.2.5 FORMULA
<a name="s-10-7-2-5-1-FORMULA"></a>
10.7.2.5.1 FORMULA
표 계산식은 표에서 덧셈, 뺄셈, 곱셈, 나눗셈과 같은 사칙연산은 물론 sum과 avg와 같은 간단한 함수를 이용하여 계산하는 기능이다.
<a name="s-10-7-2-5-2-sec"></a>
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
<a name="s-10-7-2-5-3-XML"></a>
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
<a name="s-10-7-2-6-DATE"></a>
10.7.2.6 DATE 및 DOC_DATE
날짜/시간 표시. DATE 형식은 하위 호환성을 위해 남겨둔 형식이다. DATE 형식은 되도록 사용하지 않는 것을 권고한다.
<a name="s-10-7-2-6-1-sec"></a>
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
<a name="s-10-7-2-7-SUMMARY"></a>
10.7.2.7 SUMMARY
<a name="s-10-7-2-7-1-Summary"></a>
10.7.2.7.1 Summary
문서 요약 정보는 현재 문서에 대한 제목, 주제, 지은이, 중심 낱말(키워드), 저자, 입력자, 교정자, 내용 요약, 주의사항 등을 간단히 기록할 수 있는 기능이다.
<a name="s-10-7-2-7-2-sec"></a>
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
<a name="s-10-7-2-7-3-XML"></a>
10.7.2.7.3 XML 예
샘플 77 — SUMMARY 예
code
Xml
<fieldBegin id="fb06" type="SUMMARY" editable="false" dirty="false">
    <parameters count="1">
        <stringParam name="Property">$title</stringParam>
    </parameters>
</fieldBegin>
<a name="s-10-7-2-8-USER_INFO"></a>
10.7.2.8 USER_INFO
<a name="s-10-7-2-8-1-USER_INFO"></a>
10.7.2.8.1 USER_INFO
사용자 정보는 현재 문서의 작성자에 대한 이름, 회사명, 전화번호 등을 간단히 기록할 수 있는 기능이다.
<a name="s-10-7-2-8-2-sec"></a>
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
<a name="s-10-7-2-8-3-XML"></a>
10.7.2.8.3 XML 예
샘플 78 — USER_INFO 예
code
Xml
<fieldBegin id="fb07" type="USER_INFO" editable="false" dirty="false">
    <parameters count="1">
        <stringParam name="Category">$UserName</stringParam>
    </parameters>
</fieldBegin>
<a name="s-10-7-2-9-PATH"></a>
10.7.2.9 PATH
<a name="s-10-7-2-9-1-Path"></a>
10.7.2.9.1 Path
현재 문서의 물리적인 파일 경로를 문서에 표시해 주는 기능이다.
<a name="s-10-7-2-9-2-sec"></a>
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
<a name="s-10-7-2-9-3-XML"></a>
10.7.2.9.3 XML 예
샘플 79 — PATH 예
code
Xml
<fieldBegin id="fb08" type="PATH" editable="false" dirty="false">
    <parameters count="1">
        <stringParam name="Format">$P$F</stringParam>
    </parameters>
</fieldBegin>
<a name="s-10-7-2-10-CROSSREF"></a>
10.7.2.10 CROSSREF
<a name="s-10-7-2-10-1-CROSSREF"></a>
10.7.2.10.1 CROSSREF
상호 참조는 다른 곳의 그림, 표 등을 현재의 본문에서 항상 참조할 수 있도록 그 위치를 표시해 주는 기능이다.
<a name="s-10-7-2-10-2-sec"></a>
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
<a name="s-10-7-2-10-3-XML"></a>
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
<a name="s-10-7-2-11-MAILMERGE"></a>
10.7.2.11 MAILMERGE
<a name="s-10-7-2-11-1-MAILMERGE"></a>
10.7.2.11.1 MAILMERGE
메일 머지는 여러 사람의 이름, 주소 등이 들어 있는 '데이터 파일(data file)'과 '서식 파일(form letter)'을 합침(merging)으로써, 이름이나 직책, 주소 부분 등만 다르고 나머지 내용이 같은 수십, 수백 통의 편지지를 한꺼번에 만드는 기능이다.
<a name="s-10-7-2-11-2-sec"></a>
10.7.2.11.2 필요한 인자들
표 157 — MAILMERGE 요소
인자 이름	인자 형식	설명
FieldType	stringParam	필드 형식. WAB, USER_DEFINE 중 하나의 값을 가질 수 있음
FieldValue	stringParam	필드 엔트리 이름
<a name="s-10-7-2-11-3-XML"></a>
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
<a name="s-10-7-2-12-MEMO"></a>
10.7.2.12 MEMO
<a name="s-10-7-2-12-1-MEMO"></a>
10.7.2.12.1 MEMO
메모는 현재 편집 중인 문서에서 특정 단어나 블록으로 설정한 문자열에 대한 간단한 추가 내용을 기록하는 기능이다.
<a name="s-10-7-2-12-2-sec"></a>
10.7.2.12.2 필요한 인자들
표 159 — MEMO 요소
인자 이름	인자 형식	설명
ID	stringParam	메모를 식별하기 위한 아이디
Number	integerParam	메모 번호
CreateDateTime	stringParam	메모 작성 시각. KS X ISO 8601에 따라 'YYYY-MM-DD hh:mm:ss' 형식 사용
Author	stringParam	메모 작성자
MemoShapeIDRef	stringParam	메모 모양 속성 정보 아이디 참조값
<a name="s-10-7-2-12-3-XML"></a>
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
<a name="s-10-7-2-13-PROOFREADING_MARKS"></a>
10.7.2.13 PROOFREADING_MARKS
<a name="s-10-7-2-13-1-PROOFREADING_MARKS"></a>
10.7.2.13.1 PROOFREADING_MARKS
교정 부호는 맞춤법, 띄어쓰기, 글자 크기, 문장 부호, 줄바꿈, 오자, 탈자, 어색한 표현 등을 바로잡기 위하여 특정 부호를 문서 내에 삽입하는 기능이다.
<a name="s-10-7-2-13-2-sec"></a>
10.7.2.13.2 필요한 인자들
표 160 — PROOFREADING_MARKS 요소
인자 이름	인자 형식	설명
Type	stringParam	교정 부호 종류
ProofreadingContents	stringParam	교정 내용. 넣음표, 부호 넣음표, 고침표에서 사용됨
MovingMargin	integerParam	자리 옮김 여백. 오른/왼자리 옮김표에서 사용됨
MovingStart	integerParam	자리 옮김 시작위치. 오른/왼자리 옮김표에서 사용됨
SplitType	stringParam	'자리 바꿈 나눔표'인지 '줄 서로 바꿈 나눔표'인지 여부
<a name="s-10-7-2-13-3-XML"></a>
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
<a name="s-10-7-2-14-PRIVATEINFO"></a>
10.7.2.14 PRIVATEINFO
<a name="s-10-7-2-14-1-PRIVATEINFO"></a>
10.7.2.14.1 PRIVATEINFO 요소
개인 정보 보호는 현재 화면에서 편집하고 있는 문서 내용 중 사용자가 블록으로 지정한 영역을 암호를 걸어 사용자가 선택한 문자로 변경하는 기능이다.
<a name="s-10-7-2-14-2-sec"></a>
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
<a name="s-10-7-2-16-CITATION"></a>
10.7.2.16 CITATION
<a name="s-10-7-2-16-1-CITATION"></a>
10.7.2.16.1 CITATION
인용은 연구논문이나 다른 여타의 원본을 인용해야 하는 문서를 작성할 때 사용하는 기능이다. 인용은 다양한 형식의 인용 스타일을 선택하여 적용할 수 있다.
<a name="s-10-7-2-16-2-sec"></a>
10.7.2.16.2 필요한 인자들
표 166 — CITATION 요소
인자 이름	인자 형식	설명
GUID	stringParam	인용 고유 번호
Result	stringParam	스타일이 적용된 인용 문자열
<a name="s-10-7-2-16-3-XML"></a>
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
<a name="s-10-7-2-17-BIBLIOGRAPHY"></a>
10.7.2.17 BIBLIOGRAPHY
참고문헌은 참조한 원본에 대한 출처 정보를 적는 기능이다. 다양한 참고문헌 스타일을 적용할 수 있다.
<a name="s-10-7-2-17-1-sec"></a>
10.7.2.17.1 필요한 인자들
표 167 — BIBLIOGRAPHY 요소
인자 이름	인자 형식	설명
StyleName	stringParam	참고문헌 스타일
StyleVersion	stringParam	참고문헌 스타일 버전
<a name="s-10-7-2-17-2-XML"></a>
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
<a name="s-10-7-3-fieldEnd"></a>
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
---

## Source: okok1-2-2.md
<a name="source-okok122.md"></a>

KSX 6101:2024
<a name="s-10-9-5-7-1-renderinginfo"></a>
10.9.5.7.1 renderinginfo 요소
표 216 — renderinginfo 요소
하위 요소 이름	설명
transMatrix	Translation Matrix, 10.9.5.7.2 참조
scaMatrix	Scaling Matrix, 10.9.5.7.2 참조
rotMatrix	Rotation Matrix, 10.9.5.7.2 참조
<a name="s-10-9-5-7-2-sec"></a>
10.9.5.7.2 행렬 요소 형식
[MatrixType]은 행렬을 표현하기 위한 요소 형식이다. 3x3 행렬 요소는 (0,0,1)로 가정하기 때문에 표현하지 않는다.
그림 135 — [MatrixType]의 구조
표 217 — MatrixType 요소
속성 이름	설명
e1	3x3 행렬의 첫 번째 요소 (0,0)
e2	3x3 행렬의 두 번째 요소 (0,1)
e3	3x3 행렬의 세 번째 요소 (0,2)
e4	3x3 행렬의 네 번째 요소 (1,0)
e5	3x3 행렬의 다섯 번째 요소 (1,1)
e6	3x3 행렬의 여섯 번째 요소 (1,2)
실습 121 MatrixType 예
code
Xml
<hp:renderingInfo>
    <hp:transMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
    <hp:scaMatrix e1="0.881959" e2="0" e3="0" e4="0" e5="0.35278"/>
    <hp:rotMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
</hp:renderingInfo>
<a name="s-10-9-6-pic"></a>
10.9.6 pic 요소
<a name="s-10-9-6-1-pic"></a>
10.9.6.1 pic
<pic> 요소는 [AbstractShapeComponentType]을 상속받는다. [AbstractShapeComponentType]의 자세한 내용은 10.9.5를 참조한다.
표 218 — pic 요소
속성 이름	설명
reverse	그림 색상 반전
표 219 — pic 하위 요소
하위 요소 이름	설명
lineShape	테두리선 모양
imgRect	이미지 좌표 정보
imgClip	이미지 자르기 정보
effects	이미지 효과 정보
inMargin	안쪽 여백 정보 10.6.6.2 참조
imgDim	이미지 원본 정보
img	그림 정보
실습 122 pic 예
code
Xml
<hp:pic id="-1790881809" zOrder="2" numberingType="PICTURE" textWrap="SQUARE" textFlow="BOTH_SIDES"
lock="1" dropcapstyle="None" href="" groupLevel="0" instid="717139986" reverse="0">
    <hp:offset x="0" y="0"/>
    <hp:orgSz width="13800" height="15438"/>
    <hp:curSz width="0" height="0"/>
    <hp:flip horizontal="0" vertical="0"/>
    <hp:rotationInfo angle="0" centerX="6900" centerY="7719" rotateimage="1"/>
    <hp:renderinginfo>
        <hp:transMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
        <hp:scaMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
        <hp:rotMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
    </hp:renderinginfo>
    <hp:img binaryItemIDRef="image1" bright="0" contrast="0" effect="REAL_PIC" alpha="0"/>
    <hp:lineShape color="#FF0000" width="33" style="DOT" endCap="FLAT" headStyle="NORMAL" tailStyle="NORMAL"
    headfill="0" tailfill="0" headSz="SMALL_SMALL" tailSz="SMALL_SMALL" outlineStyle="OUTER" alpha="0"/>
    <hp:imgRect>
        <hp:ptO x="0" y="0"/>
        <hp:pt1 x="13800" y="0"/>
        <hp:pt2 x="13800" y="15438"/>
        <hp:pt3 x="0" y="15438"/>
    </hp:imgRect>
    <hp:imgClip left="0" right="45060" top="0" bottom="50400"/>
    <hp:inMargin left="0" right="0" top="0" bottom="0"/>
    <hp:imgDim dimwidth="45060" dimheight="50400"/>
    <hp:effects/>
    <hp:sz width="13800" widthRelTo="ABSOLUTE" height="15438" heightRelTo="ABSOLUTE" protect="0"/>
    <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="1" holdAnchorAndSO="0"
    vertRelTo="PAPER" horzRelTo="PAPER" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="119107"/>
    <hp:outMargin left="0" right="0" top="0" bottom="0"/>
    <hp:shapeComment>그림입니다. 원본 그림의 이름:01_대오버?!.png 원본 그림의 크기: 가로 601pixel, 세로 672pixel</hp:shapeComment>
</hp:pic>
<a name="s-10-9-6-2-sec"></a>
10.9.6.2 테두리선 모양
그림 137 — <lineShape>의 구조
표 220 — lineShape 요소
속성 이름	설명
color	선 색상
width	선 굵기. 단위: HWPUNIT
style	선 종류
endCap	선 끝 모양
headStyle	화살표 시작 모양
tailStyle	화살표 끝 모양
headfill	화살표 시작점 선 색상으로 채우기 여부
tailfill	화살표 끝점 선 색상으로 채우기 여부
headSz	화살표 시작 크기
tailSz	화살표 끝 크기
outlineStyle	테두리선의 형태
alpha	투명도
실습 123 lineShape 예
code
Xml
<hp:lineShape color="#141313" width="6" style="SOLID" endCap="FLAT" headStyle="NORMAL"
tailStyle="NORMAL" headfill="1" tailfill="1" headSz="SMALL_SMALL" tailSz="SMALL_SMALL"
outlineStyle="INNER" alpha="277"/>
<a name="s-10-9-6-3-sec"></a>
10.9.6.3 이미지 좌표 정보
<a name="s-10-9-6-3-1-sec"></a>
10.9.6.3.1 이미지 좌표
그림의 좌표 정보를 가지고 있는 요소이다.
그림 138 — <imgRect>의 구조
표 221 — imgRect 요소
하위 요소 이름	설명
pt0	첫 번째 좌표 10.9.6.3.2 참조
pt1	두 번째 좌표 10.9.6.3.2 참조
pt2	세 번째 좌표 10.9.6.3.2 참조
pt3	네 번째 좌표 10.9.6.3.2 참조
<a name="s-10-9-6-3-2-sec"></a>
10.9.6.3.2 점 요소 형식
좌표 정보를 표현할 때 사용하는 요소로, 2축 좌표계를 사용한다.
표 222 — PointType 요소
속성 이름	설명
x	x 좌표
y	y 좌표
실습 124 PointType 예
code
Xml
<hp:imgRect>
    <hp:ptO x="0" y="0"/>
    <hp:pt1 x="14112" y="0"/>
    <hp:pt2 x="14112" y="7938"/>
    <hp:pt3 x="0" y="7938"/>
</hp:imgRect>
<a name="s-10-9-6-4-sec"></a>
10.9.6.4 이미지 자르기 정보
원본 그림을 기준으로 자를 영역 정보를 가지고 있는 요소이다. 자르기 정보가 설정되면, 그림은 논리적으로 원본 그림에서 해당 영역만큼 잘리게 되고, 화면에서는 남은 영역만 표시된다.
그림 140 — <img>의 구조
표 223 — imgClip 요소
속성 이름	설명
left	왼쪽에서 이미지를 자른 크기
right	오른쪽에서 이미지를 자른 크기
top	위쪽에서 이미지를 자른 크기
bottom	아래쪽에서 이미지를 자른 크기
실습 125 imgClip 예
code
Xml
<hp:imgClip left="0" right="96000" top="0" bottom="54000"/>
<a name="s-10-9-6-5-sec"></a>
10.9.6.5 이미지 효과 정보
<a name="s-10-9-6-5-1-sec"></a>
10.9.6.5.1 이미지 효과
그림에 적용될 효과 정보를 가지고 있는 요소이다.
표 224 — effects 요소
하위 요소 이름	설명
shadow	그림자 효과
glow	네온 효과
softEdge	부드러운 가장자리 효과
reflection	반사 효과
<a name="s-10-9-6-5-2-sec"></a>
10.9.6.5.2 그림자 효과
그림 효과 중 그림자 효과에 대한 설정 정보를 가지고 있는 요소이다.
표 225 — shadow 요소
속성 이름	설명
style	그림자 스타일
alpha	시작 투명도
radius	흐릿한 정도
direction	방향 각도
distance	대상과 그림자 사이의 거리
rotationstyle	도형과 함께 그림자 회전 여부
하위 요소 이름	설명
skew	기울기
scale	확대 비율
effectsColor	그림자 색상
실습 126 shadow 예
code
Xml
<hp:shadow style="OUTSIDE" alpha="?" radius="60" direction="?" distance="100"
alignStyle="CENTER" rotationStyle="0">
    <hp:skew x="15" y="0"/>
    <hp:scale x="1" y="1"/>
    <hp:effectsColor type="RGB" schemeIdx="-1" systemIdx="-1" presetIdx="-1">
        <hp:rgb r="1" g="1" b="1"/>
    </hp:effectsColor>
</hp:shadow>
기울기 각도
기울기 정보를 가지고 있는 요소이다.
그림 143 — <skew>의 구조
표 227 — skew 요소
속성 이름	설명
x	x축 기울기 각도
y	y축 기울기 각도
실습 127 skew 예
code
Xml
<hp:skew x="30" y="0"/>
확대 비율
확대 정보를 가지고 있는 요소이다.
그림 144 — <scale>의 구조
표 228 — scale 요소
속성 이름	설명
x	x축 확대 비율
y	y축 확대 비율
실습 128 scale 예```xml
<hp:scale x="1" y="1.2"/>
code
Code
**색상 정보**
효과에 사용될 색상 정보를 가지고 있는 요소이다.

**표 230 — effectsColor 하위 요소**

| 하위 요소 이름 | 설명 |
| :--- | :--- |
| rgb | RGB 색상 표현 속성으로 r, g, b 세 가지 속성을 가짐. 모두 0 이상의 정수 값을 가짐. 해당 요소의 추가적인 설명은 생략. |
| cmyk | CMYK 색상 표현 속성으로 c, m, y, k 네 가지 속성을 가짐. 모두 0 이상의 정수 값을 가짐. 해당 요소의 추가적인 설명은 생략. |
| scheme | Scheme 색상 표현 속성으로 r, g, b 세 가지 속성을 가짐. 모두 0 이상의 정수 값을 가짐. 해당 요소의 추가적인 설명은 생략. |
| system | System 색상 표현 속성으로 h, s, l 세 가지 속성을 가짐. 모두 0 이상의 정수 값을 가짐. |

**effect 요소**
색상 효과 정보를 가지고 있는 요소이다.

**그림 146 — `<effect>`의 구조**

**표 231 — effect 요소**

| 속성 이름 | 설명 |
| :--- | :--- |
| type | 색상 효과 종류 |
| value | 효과 적용에 필요한 수치 |

**표 232 — 색상 효과 종류 1**

| 색상 효과 구분 | 이름/설명 | 값의 범위 | 기본 값 |
| :--- | :--- | :--- | :--- |
| ALPHA | 투명도. 1.0이면 불투명 | 0.0 ~ 1.0 | 1.0 |
| ALPHA_MOD | 투명도 조정 값. 1.0이면 변화 없음 | 0.0 ~ 1.0 | 1.0 |
| ALPHA_OFF | 투명도 오프셋 | 정수형 | 0 |
| RED | RGB 값 중 red 값 | 0.0 ~ 1.0 | 1.0 |
| RED_MOD | red 조정 값 | 0.0 ~ 1.0 | 1.0 |
| RED_OFF | red 오프셋 | 정수형 | 0 |
| GREEN | RGB 값 중 green 값 | 0.0 ~ 1.0 | 1.0 |
| GREEN_MOD | green 조정 값 | 0.0 ~ 1.0 | 1.0 |
| GREEN_OFF | green 오프셋 | 정수형 | 0 |
| BLUE | RGB 값 중 blue 값 | 0.0 ~ 1.0 | 1.0 |
| BLUE_MOD | blue 조정 값 | 0.0 ~ 1.0 | 1.0 |

**표 233 — 색상 효과 종류 2**

| 색상 효과 구분 | 이름/설명 | 값의 범위 | 기본 값 |
| :--- | :--- | :--- | :--- |
| BLUE_OFF | blue 오프셋 | 정수형 | 0 |
| HUE | HSL 컬러 모델에서 색조(hue) 값 설정 | 0 ~ 359 | |
| HUE_MOD | HSL 컬러 모델에서 색조 값 조정 | 0.0 ~ 1.0 | 1.0 |
| HUE_OFF | HSL 컬러 모델에서 색조 값 오프셋 | -16000 ~ 16000 | 0 |
| SAT | HSL 컬러 모델에서 채도(saturation) 값 설정 | 0.0 ~ 1.0 | |
| SAT_MOD | HSL 컬러 모델에서 채도 값 조정 | 0.0 ~ 1.0 | 1.0 |
| SAT_OFF | 채도 조정 값 오프셋 | | |
| LUM | HSL 컬러 모델에서 명도(luminance) 값 설정 | 0.0 ~ 1.0 | |
| LUM_MOD | HSL 컬러 모델에서 명도 값 조정 | 0.0 ~ 1.0 | 1.0 |
| LUM_OFF | 명도 오프셋 | | 0 |
| SHADE | 현재 색상을 어둡게 함. 1이면 변화 없음 | | 1 |
| TINT | 현재 색상을 밝게 함. 1이면 변화 없음 | | 1 |
| GRAY | Gray scale(회색조) 사용 | 0 또는 1 | |
| COMP | 보색(complementary color) 사용 | 0 또는 1 | |
| GAMMA | 감마(Gamma) 적용 (감마 값 = 1/2.2) | | |
| INV_GAMMA | 역감마(Inverse Gamma) 적용 (감마 값 = 2.2) | | |
| INV | 색상 반전 | | |

**10.9.6.5.3 네온 효과**
네온 효과 정보를 가지고 있는 요소이다.

**그림 147 — `<glow>`의 구조**

**표 234 — glow 요소**

| 속성 이름 | 설명 |
| :--- | :--- |
| alpha | 투명도 |
| radius | 네온 반경. 단위: HWPUNIT |

**표 235 — glow 하위 요소**

| 하위 요소 이름 | 설명 |
| :--- | :--- |
| effectsColor | 네온 색상 10.9.6.5.2.3 참조 |

**실습 130 glow 예**
```xml
```xml
<hp:glow alpha="0.5" radius="1000">
    <hp:effectsColor type="RGB" schemeIdx="-1" systemIdx="-1" presetIdx="-1">
        <hp:rgb r="178" g="178" b="178">
            <hp:effect type="SAT_MOD" value="0.75"/>
        </hp:effectsColor>
    </hp:glow>
```
<a name="s-10-9-6-5-4-sec"></a>
10.9.6.5.4 부드러운 가장자리 효과
부드러운 가장자리 효과 정보를 가지고 있는 요소이다.
<a name="figure-148"></a>
그림 148 — <softEdge>의 구조
<a name="table-236"></a>
표 236 — softEdge 요소
속성 이름	설명
radius	부드러운 가장자리 크기. 단위는 HWPUNIT
실습 131 softEdge 예
code
Xml
<hp:softEdge radius="500"/>
<a name="s-10-9-6-5-5-sec"></a>
10.9.6.5.5 반사 효과
반사 효과 정보를 가지고 있는 요소이다.
<a name="figure-149"></a>
그림 149 — <reflection>의 구조
<a name="table-237"></a>
표 237 — reflection 요소
속성 이름	설명
alignStyle	반사된 그림 위치
radius	흐릿한 정도. 단위: HWPUNIT
direction	반사된 그림 방향 각도
distance	대상과 반사된 그림 사이의 거리. 단위는 HWPUNIT
rotationstyle	도형과 함께 회전할 것인지 여부
fadeDirection	오프셋 방향
<a name="table-238"></a>
표 238 — reflection 하위 요소
하위 요소 이름	설명
skew	기울기 10.9.6.5.2.1 참조
scale	확대 비율 10.9.6.5.2.2 참조
alpha	투명도 설정 10.9.6.5.5.1 참조
pos	위치 설정 10.9.6.5.5.2 참조
실습 132 reflection 예
code
Xml
<hp:reflection alignStyle="BOTTOM_LEFT" radius="50" direction="90" distance="400"
rotationStyle="0" fadeDirection="90">
    <hp:skew x="0" y="0"/>
    <hp:scale x="1" y="0"/>
    <hp:alpha start="0.5" end="0.99"/>
    <hp:pos start="0" end="0.75"/>
</hp:reflection>
투명도 설정
반사 효과 사용 시 투명도 설정 정보를 가지고 있는 요소이다.
<a name="figure-150"></a>
그림 150 — <alpha>의 구조
<a name="table-239"></a>
표 239 — alpha 요소
속성 이름	설명
start	시작 위치 투명도
end	끝 위치 투명도
실습 133 alpha 예
code
Xml
<hp:alpha start="0.5" end="0.99"/>```

**반사 효과 위치 설정**
반사된 영상이 시작될 위치 정보를 가지고 있는 요소이다.

**그림 151 — `<pos>`의 구조**

**표 240 — pos 요소**

| 속성 이름 | 설명 |
| :--- | :--- |
| start | 시작 위치 |
| end | 끝 위치 |

**실습 134 pos 예**
```xml
<hp:pos start="0" end="0.75"/>
<a name="s-10-9-6-6-sec"></a>
10.9.6.6 이미지 원본 정보
원본 그림의 크기 정보를 가지고 있는 요소이다.
표 241 — imgDim 요소
속성 이름	설명
dimwidth	원본 너비
dimheight	원본 높이
실습 135 imgDim 예
code
Xml
<hp:imgDim dimwidth="96000" dimheight="54000"/>
<a name="s-10-9-7-ole"></a>
10.9.7 ole 요소
<a name="s-10-9-7-1-ole"></a>
10.9.7.1 ole
<ole> 요소는 [AbstractShapeComponentType]을 상속받는다. [AbstractShapeComponentType]의 자세한 내용은 10.9.5를 참조한다.
그림 152 — <ole>의 구조
실습 136 ole 예
code
Xml
<hp:ole id="1790881810" zOrder="3" numberingType="PICTURE" textWrap="SQUARE" textFlow="BOTH_SIDES"
lock="0" dropcapstyle="None" href="" groupLevel="0" instid="717139988" objectType="EMBEDDED"
binaryItemIDRef="ole1" hasMoniker="0" drawAspect="CONTENT" eqBaseLine="0">
    <hp:offset x="0" y="0"/>
    <hp:orgSz width="14176" height="14176"/>
    <hp:curSz width="0" height="0"/>
    <hp:flip horizontal="0" vertical="0"/>
    <hp:rotationInfo angle="0" centerX="7088" centerY="7088" rotateimage="1"/>
    <hp:renderingInfo>
        <hp:transMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
        <hp:scaMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
        <hp:rotMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
    </hp:renderingInfo>
    <hp:extent x="14176" y="14176"/>
    <hp:lineShape color="#0000FF" width="133" style="DASH_DOT" endCap="ROUND" headStyle="NORMAL"
    tailStyle="NORMAL" headfill="0" tailfill="0" headSz="SMALL_SMALL" tailSz="SMALL_SMALL"
    outlineStyle="OUTER" alpha="0"/>
    <hp:sz width="14176" widthRelTo="ABSOLUTE" height="14176" heightRelTo="ABSOLUTE" protect="0"/>
    <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0"
    vertRelTo="PARA" horzRelTo="COLUMN" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/>
    <hp:outMargin left="0" right="0" top="0" bottom="0"/>
    <hp:shapeComment>OLE 개체입니다. 개체 형식은 Bitmap Image입니다.</hp:shapeComment>
</hp:ole>
<a name="s-10-9-7-2-extent"></a>
10.9.7.2 extent 요소
OLE 객체의 확장 크기 정보를 가지고 있는 요소이다.
그림 153 — <extent>의 구조
표 244 — extent 요소
속성 이름	설명
x	오브젝트 자체의 extent x 크기
y	오브젝트 자체의 extent y 크기
실습 137 extent 예
code
Xml
<hp:extent x="14176" y="14176"/>
<a name="s-10-9-8-container"></a>
10.9.8 container 요소
<container> 요소는 [AbstractShapeComponentType]을 상속받는다. [AbstractShapeComponentType]의 자세한 내용은 10.9.5를 참조한다.
<container> 요소는 다른 도형 객체를 묶기 위해서 사용되는 객체이다. <container> 요소로 묶을 수 있는 객체에는 컨테이너 객체 자신과, 선, 사각형, 타원, 호, 다각형, 곡선, 연결선과 같은 그리기 객체, 그림, OLE 객체가 있다.
그림 154 — <container>의 구조
실습 138 container 예
code
Xml
<hp:container id="1615476006" zOrder="1" numberingType="PICTURE"
textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href=""
groupLevel="0" instid="541734183">
    <hp:sz width="31160" widthRelTo="ABSOLUTE" height="12660" heightRelTo="ABSOLUTE" protect="0"/>
    <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="0" allowOverlap="1"
    holdAnchorAndSO="0" vertRelTo="PAPER" horzRelTo="PAPER" vertAlign="TOP" horzAlign="LEFT"
    vertOffset="10540" horzOffset="11734"/>
    <hp:outMargin left="0" right="0" top="0" bottom="0"/>
    <hp:caption side="BOTTOM" fullSz="0" width="8504" gap="850" lastWidth="31160">
        <hp:subList id="0" textDirection="HORIZONTAL" lineWrap="BREAK" vertAlign="TOP"
        linkListIDRef="0" linkListNextIDRef="0" textWidth="0" textHeight="0" hasTextRef="0" hasNumRef="0">
            <hp:p id="0" paraPrIDRef="19" styleIDRef="2" pageBreak="0" columnBreak="0" merged="0">
                <hp:run charPrIDRef="7">
                    <hp:t>ShapeCompContainer</hp:t>
                </hp:run>
            </hp:p>
        </hp:subList>
    </hp:caption>
    <hp:shapeComment>묶음 개체입니다.</hp:shapeComment>
    <hp:rect id="2" zOrder="0" numberingType="NONE" textWrap="TOP_AND_BOTTOM"
    textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href="" groupLevel="1" instid="541734179" ratio="20"/>
    <hp:ellipse id="7602208" zOrder="0" numberingType="NONE" textWrap="TOP_AND_BOTTOM"
    textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href="" groupLevel="1" instid="541734181"
    intervalDirty="0" hasArcPr="0" arcType="NORMAL"/>
</hp:container>
<a name="s-10-9-9-chart"></a>
10.9.9 chart 요소
<chart> 요소는 [AbstractShapeObjectType]을 상속받는다. [AbstractShapeObjectType]의 자세한 내용은 10.9.2를 참조한다.
<chartIDRef>: 차트 데이터에 대한 아이디 참조값으로 차트에 대한 xml 데이터는 OOXML의 형식을 사용하며 Chart/chart.xml (8.2 참조)에 기입된다.
그림 155 — <chart>의 구조
표 246 — chart 요소
속성 이름	설명
chartIDRef	차트 데이터에 대한 아이디 참조값
version	차트 버전
실습 139 chart 예
code
Xml
<hp:chart id="-1811647071" zOrder="6" numberingType="PICTURE" textWrap="SQUARE"
textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" chartIDRef="Chart/chart1.xml">
    <hp:sz width="32250" widthRelTo="ABSOLUTE" height="18750" heightRelTo="ABSOLUTE" protect="0"/>
    <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="0"
    holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="COLUMN" vertAlign="TOP" horzAlign="LEFT"
    vertOffset="0" horzOffset="0"/>
    <hp:outMargin left="0" right="0" top="0" bottom="0"/>
</hp:chart>
<a name="s-10-10-sec"></a>
10.10 그리기 객체
<a name="s-10-10-1-sec"></a>
10.10.1 그리기 객체
그리기 객체는 연결선, 사각형, 원 등과 같은 기본 도형 객체보다 더 구체화된 도형 객체이다. 그리기 객체는 기본 도형 객체의 공통 속성을 모두 상속받으며 그리기 객체만을 위한 속성을 추가적으로 더 정의해서 사용한다.
<a name="s-10-10-2-AbstractDrawingObjectType"></a>
10.10.2 AbstractDrawingObjectType
<a name="s-10-10-2-1-AbstractDrawingObjectType"></a>
10.10.2.1 AbstractDrawingObjectType
[AbstractDrawingObjectType]은 그리기 객체의 기본 속성을 정의하고 있는 요소 형식이다. [AbstractDrawingObjectType]은 [AbstractShapeComponentType]을 기본 형식으로 가지고 추가적으로 필요한 속성이나 요소를 확장한다. [AbstractShapeComponentType]의 자세한 내용은 10.9.5를 참조한다.
[AbstractDrawingObjectType]은 추상 형식이므로 [AbstractDrawingObjectType]만으로는 XML 요소를 생성할 수 없다.
그림 156 — [AbstractDrawingObjectType]의 구조
표 247 — AbstractDrawingObjectType 요소
하위 요소 이름	설명
lineShape	그리기 객체의 테두리선 정보 10.9.6.2 참조
fillBrush	그리기 객체의 채우기 정보
drawText	그리기 객체 글상자용 텍스트
shadow	그리기 객체의 그림자 정보
실습 140 AbstractDrawingObjectType 예
code
Xml
<hp:lineShape color="#000000" width="33" style="SOLID" endCap="FLAT" headStyle="NORMAL" tailStyle="NORMAL"
headfill="1" tailfill="1" headSz="MEDIUM_MEDIUM" tailSz="MEDIUM_MEDIUM" outlineStyle="NORMAL" alpha="0"/>
<hp:fillBrush>
    <hc:winBrush faceColor="#FFFFFF" hatchColor="#000000" alpha="0"/>
</hp:fillBrush>
<hp:shadow type="NONE" color="#828282" offsetX="0" offsetY="0" alpha="0"/>
<hp:drawText lastWidth="34260" name="" editable="0"/>
<a name="s-10-10-2-2-sec"></a>
10.10.2.2 채우기 정보
<a name="s-10-10-2-2-1-sec"></a>
10.10.2.2.1 채우기
그리기 객체에서 객체의 면 영역에서 사용된 채우기 효과 정보를 가지고 있는 요소이다.
그림 157 — <fillBrush>의 구조
표 248 — fillBrush 요소
하위 요소 이름	설명
winBrush	면 채우기
gradation	그러데이션 효과
imgBrush	그림으로 채우기
<a name="s-10-10-2-2-2-sec"></a>
10.10.2.2.2 면 채우기 정보
채우기 효과 중 단색 또는 무늬가 입혀진 단색으로 채우는 효과 정보를 가지고 있는 요소이다.
그림 158 — <winBrush>의 구조
표 249 — winBrush 요소
속성 이름	설명
faceColor	면 색상
hatchColor	무늬 색
hatchstyle	무늬 종류
alpha	투명도
<a name="s-10-10-2-2-3-sec"></a>
10.10.2.2.3 그러데이션 효과
한 색상에서 다른 색상으로 점진적 또는 단계적으로 변하는 기법을 표현하기 위한 요소이다.
그림 159 — <gradation>의 구조
표 250 — gradation 요소
속성 이름	설명
type	그러데이션 유형
angle	그러데이션 기울기 (시작각)
centerX	그러데이션 가로 중심 (중심 X 좌표)
centerY	그러데이션 세로 중심 (중심 Y 좌표)
step	그러데이션 번짐 정도 (0-255)
colorNum	그러데이션 색상 수
stepCenter	그러데이션 번짐 정도의 중심 (0-100)
alpha	투명도
표 251 — gradation 하위 요소
하위 요소 이름	설명
color	그러데이션 색상
그러데이션 색상
그러데이션 색상으로 표현하기 위한 요소로, 점진적으로 또는 단계적으로 변화하는 색상 중 시작 색, 또는 끝 색, 중간 단계 색 등을 표현한다.
그림 160 — <color>의 구조
표 252 — color 요소
속성 이름	설명
value	색상값
<a name="s-10-10-2-2-4-sec"></a>
10.10.2.2.4 그림으로 채우기 정보
그림으로 특정 부분을 채울 때 사용되는 요소로, 지정된 그림을 지정된 효과를 사용해서 채운다. 사용할 수 있는 효과에는 '크기에 맞추어', '위로/가운데로/아래로', '바둑판식으로' 등이 있다.
<a name="s-10-10-2-3-sec"></a>
10.10.2.3 그리기 객체 글상자용 텍스트
그리기 객체 안의 또는 지정 영역에 표시되는 글상자 내용을 가지고 있는 요소이다.
표 255 — drawText 요소
속성 이름	설명
lastwidth	라스트 라인의 최대 폭. 단위는 HWPUNIT
name	글상자 이름
editable	편집 가능 여부
표 256 — drawText 하위 요소
하위 요소 이름	설명
textMargin	글상자 텍스트 여백
subList	글상자 텍스트 11.1.2 참조
실습 141 drawText 예
code
Xml
<hp:drawText lastWidth="12540" name="" editable="0">
    <hp:subList id="0" textDirection="HORIZONTAL" lineWrap="BREAK" vertAlign="CENTER"
    linkListIDRef="0" linkListNextIDRef="0" textWidth="0" textHeight="0" hasTextRef="1" hasNumRef="0">
        <hp:p id="0" paraPrIDRef="20" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
            <hp:run charPrIDRef="8">
                <hp:t>Rectangle</hp:t>
            </hp:run>
        </hp:p>
    </hp:subList>
    <hp:textMargin left="283" right="283" top="283" bottom="283"/>
</hp:drawText>
<a name="s-10-10-2-3-2-sec"></a>
10.10.2.3.2 글상자 텍스트 여백
<textMargin> 요소는 [MarginAttributeGroup]을 속성으로 포함한다. [MarginAttributeGroup]은 10.6.6.2를 참조한다.
그림 163 — <textMargin>의 구조
표 257 — textMargin 요소
속성 이름	설명
[MarginAttributeGroup]	10.6.6.2 참조
실습 142 textMargin 예
code
Xml
<hp:textMargin left="283" right="283" top="283" bottom="283"/>
<a name="s-10-10-2-4-sec"></a>
10.10.2.4 그리기 객체의 그림자 정보
그리기 객체에 적용될 그림자 효과 정보를 가지고 있는 요소이다.
그림 164 — <shadow>의 구조
표 258 — shadow 요소
속성 이름	설명
type	그림자 종류
color	그림자 색
offsetX	그림자 간격 X. 단위는 %
offsetY	그림자 간격 Y. 단위는 %
<a name="s-10-10-3-sec"></a>
10.10.3 그리기 객체 — 선
그림 165 — <line>의 구조
표 259 — line 요소
속성 이름	설명
isReverseHV	처음 생성 시 수직선 또는 수평선일 때, 선의 방향이 언제나 오른쪽(위쪽)으로 잡힘으로 인한 현상 때문에 방향을 바로 잡아주기 위한 속성
표 260 — line 하위 요소
하위 요소 이름	설명
startPt	시작점 10.9.6.3.2 참조
endPt	끝점 10.9.6.3.2 참조
실습 144 line 예
code
Xml
<hp:line id="1480891240" zOrder="1" numberingType="PICTURE" textWrap="IN_FRONT_OF_TEXT"
textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href="" groupLevel="0" instid="407149417"
isReverseHV="0">
    <hp:startPt x="0" y="0"/>
    <hp:endPt x="4686" y="9102"/>
</hp:line>
<a name="s-10-10-4-sec"></a>
10.10.4 그리기 객체 — 사각형
<rect> 요소는 [AbstractDrawingObjectType]을 상속받는다. [AbstractDrawingObjectType]의 자세한 내용은 10.10.2를 참조한다.
표 261 — rect 요소
속성 이름	설명
ratio	사각형 모서리 곡률. 단위는 %. 직각은 0, 둥근 모양은 20, 반원은 50 등
표 262 — rect 하위 요소
하위 요소 이름	설명
pt0	첫 번째 좌표 10.9.6.3.2 참조
pt1	두 번째 좌표 10.9.6.3.2 참조
pt2	세 번째 좌표 10.9.6.3.2 참조
pt3	네 번째 좌표 10.9.6.3.2 참조
실습 145 rect 예
code
Xml
<hp:rect id="1480891242" zOrder="2" numberingType="PICTURE" textWrap="IN_FRONT_OF_TEXT"
textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href="" groupLevel="0" instid="407149419"
ratio="0">
    <hp:ptO x="0" y="0"/>
    <hp:pt1 x="12838" y="0"/>
    <hp:pt2 x="12838" y="9306"/>
    <hp:pt3 x="0" y="9306"/>
</hp:rect>
<a name="s-10-10-5-sec"></a>
10.10.5 그리기 객체 — 타원
<ellipse> 요소는 [AbstractDrawingObjectType]을 상속받는다. [AbstractDrawingObjectType]의 자세한 내용은 10.10.2를 참조한다.
표 263 — ellipse 요소
속성 이름	설명
intervalDirty	호(arc)로 바뀌었을 때, interval을 다시 계산해야 할 필요가 있는지 여부. interval: 원 위에 존재하는 두 점 사이의 거리
hasArcProperty	호로 바뀌었는지 여부
arcType	호의 종류. NORMAL: 호, PIE: 부채꼴, CHORD: 활
표 264 — ellipse 하위 요소
하위 요소 이름	설명
center	중심 좌표 10.9.6.3.2 참조
ax1	제1 축 좌표 10.9.6.3.2 참조
ax2	제2 축 좌표 10.9.6.3.2 참조
start1	시작 지점 1 좌표 10.9.6.3.2 참조
end1	끝 지점 1 좌표 10.9.6.3.2 참조
start2	시작 지점 2 좌표 10.9.6.3.2 참조
end2	끝 지점 2 좌표 10.9.6.3.2 참조
실습 146 ellipse 예```xml
<hp:ellipse id="1480891244" zOrder="3" numberingType="PICTURE"
textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href=""
groupLevel="0" instid="407149421" intervalDirty="0" hasArcPr="0" arcType="NORMAL">
<hp:center x="4925" y="3973"/>
<hp:ax1 x="9850" y="3973"/>
<hp:ax2 x="4925" y="0"/>
<hp:start1 x="0" y="-1337540795"/>
<hp:end1 x="-114407252" y="1432413552"/>
<hp:start2 x="-1105998402" y="100663296"/>
<hp:end2 x="393344" y="2"/>
</hp:ellipse>
code
Code
**10.10.6 그리기 객체 — 호**
`<arc>` 요소는 [AbstractDrawingObjectType]을 상속받는다. [AbstractDrawingObjectType]의 자세한 내용은 10.10.2를 참조한다.

**그림 168 — `<arc>`의 구조**

**표 265 — arc 요소**

| 속성 이름 | 설명 |
| :--- | :--- |
| type | 호의 종류. NORMAL: 호, PIE: 부채꼴, CHORD: 활 |

**표 266 — arc 하위 요소**

| 하위 요소 이름 | 설명 |
| :--- | :--- |
| center | 중심 좌표 10.9.6.3.2 참조 |
| ax1 | 제1 축 좌표 10.9.6.3.2 참조 |
| ax2 | 제2 축 좌표 10.9.6.3.2 참조 |

**실습 147 arc 예**
```xml
<hp:arc id="1480891246" zOrder="4" numberingType="PICTURE" textWrap="IN_FRONT_OF_TEXT"
textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href="" groupLevel="0" instid="407149423"
type="NORMAL">
    <hp:center x="0" y="0"/>
    <hp:ax1 x="0" y="9645"/>
    <hp:ax2 x="1417" y="0"/>
</hp:arc>
<a name="s-10-10-7-sec"></a>
10.10.7 그리기 객체 — 다각형
<polygon> 요소는 [AbstractDrawingObjectType]을 상속받는다. [AbstractDrawingObjectType]의 자세한 내용은 10.10.2를 참조한다.
<a name="figure-169"></a>
그림 169 — <polygon>의 구조
<a name="table-267"></a>
표 267 — polygon 요소
하위 요소 이름	설명
pt	다각형 좌표 10.9.6.3.2 참조
실습 148 polygon 예
code
Xml
<hp:polygon id="1480891248" zOrder="5" numberingType="PICTURE"
textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href=""
groupLevel="0" instid="407149425">
    <hp:pt x="326" y="0"/>
    <hp:pt x="0" y="3872"/>
    <hp:pt x="-3329" y="7744"/>
    <hp:pt x="-1154" y="7540"/>
    <hp:pt x="1142" y="-2047"/>
    <hp:pt x="326" y="0"/>
</hp:polygon>
<a name="s-10-10-8-sec"></a>
10.10.8 그리기 객체 — 곡선
<a name="s-10-10-8-1-sec"></a>
10.10.8.1 곡선
<curve> 요소는 [AbstractDrawingObjectType]을 상속받는다. [AbstractDrawingObjectType]의 자세한 내용은 10.10.2를 참조한다.
<a name="table-268"></a>
표 268 — curve 요소
하위 요소 이름	설명
seg	곡선 세그먼트
실습 149 curve 예
code
Xml
<hp:curve id="1480891254" zOrder="6" numberingType="PICTURE"
textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="1" dropcapstyle="None" href=""
groupLevel="0" instid="407149431">
    <hp:seg type="CURVE" x1="?" y1="1485" x2="1429" y2="10859"/>
    <hp:seg type="CURVE" x1="1429" y1="10859" x2="3263" y2="882"/>
    <hp:seg type="CURVE" x1="3263" y1="882" x2="5233" y2="11199"/>
    <hp:seg type="CURVE" x1="5233" y1="11199" x2="5980" y2="910"/>
    <hp:seg type="CURVE" x1="5980" y1="910" x2="274" y2="1485"/>
</hp:curve>
<a name="s-10-10-8-2-sec"></a>
10.10.8.2 곡선 세그먼트
그리기 객체 중 곡선을 표현할 때 곡선의 단위, 곡선의 시작점 및 끝점을 표현하기 위한 요소이다.
<a name="table-269"></a>
표 269 — seg 요소
속성 이름	설명
type	곡선 세그먼트 형식. curve: 곡선, line: 직선
x1	곡선 세그먼트 시작점 X 좌표
y1	곡선 세그먼트 시작점 y 좌표
x2	곡선 세그먼트 끝점 X 좌표
y2	곡선 세그먼트 끝점 y 좌표
실습 150 seg 예
code
Xml
<hp:seg type="CURVE" x1="274" y1="1485" x2="1429" y2="10859"/>
<a name="s-10-10-9-sec"></a>
10.10.9 그리기 객체 — 연결선
<a name="s-10-10-9-1-sec"></a>
10.10.9.1 연결선
<connectLine> 요소는 [AbstractDrawingObjectType]을 상속받는다. [AbstractDrawingObjectType]의 자세한 내용은 10.10.2를 참조한다.
<a name="table-270"></a>
표 270 — connectLine 요소
속성 이름	설명
type	연결선 형식
<a name="table-271"></a>
표 271 — connectLine 하위 요소
하위 요소 이름	설명
startPt	연결선 시작점 정보
endPt	연결선 끝점 정보
controlPoints	연결선 조절점 정보
실습 151 connectLine 예
code
Xml
<hp:connectLine id="1480891256" zOrder="7" numberingType="PICTURE"
textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href=""
groupLevel="0" instid="407149433" type="STRAIGHT_NO_ARROW">
    <hp:startPt x="?" y="4154" subjectIDRef="407149431" subjectIdx="-1"/>
    <hp:endPt x="?" y="0" subjectIDRef="407149427" subjectIdx="2"/>
    <hp:controlPoints>
        <hp:point x="?" y="4144" type="3"/>
        <hp:point x="?" y="0" type="26"/>
    </hp:controlPoints>
</hp:connectLine>
<a name="s-10-10-9-2-sec"></a>
10.10.9.2 연결선 연결점 정보
[ConnectPointType]은 [PointType]을 기본 형식으로 가지고 추가적으로 필요한 속성이나 요소를 확장한다. [PointType]의 자세한 내용은 10.9.6.3.2를 참조한다.
<a name="figure-173"></a>
그림 173 — [ConnectPointType]의 구조
<a name="table-272"></a>
표 272 — ConnectPointType 요소
속성 이름	설명
subjectIDRef	시작/끝 부분과 연결되는 대상의 아이디 참조값
subjectIdx	시작/끝 부분과 연결되는 대상의 연결점 index
실습 152 ConnectPointType 예
code
Xml
```xml
<hp:startPt x="0" y="0" subjectIDRef="0" subjectIdx="0"/>
<hp:endPt x="15402" y="10581" subjectIDRef="1" subjectIdx="0"/>
```
<a name="s-10-10-9-3-sec"></a>
10.10.9.3 연결선 조절점 정보
[ConnectControlPointType]은 [PointType]을 기본 형식으로 가지고 추가적으로 필요한 속성이나 요소를 확장한다.
<a name="table-273"></a>
표 273 — ConnectControlPointType 속성
속성 이름	설명
type	조절점 종류
실습 153 ConnectControlPointType 예
code
Xml
```xml
<hp:controlPoints>
    <hp:point x="-2446" y="0" type="3"/>
    <hp:point x="-2446" y="-2207" type="2"/>
    <hp:point x="0" y="-2207" type="2"/>
    <hp:point x="0" y="-7035" type="26"/>
</hp:controlPoints>
```
<a name="table-274"></a>
표 274 — type 값
type 값	설명
0x00000001	시작점
0x00000002	직선
0x0000001a	끝점
<a name="s-10-11-sec"></a>
10.11 양식 객체
<a name="s-10-11-1-AbstractFormObjectType"></a>
10.11.1 AbstractFormObjectType
<a name="s-10-11-1-1-AbstractFormObjectType"></a>
10.11.1.1 AbstractFormObjectType
[AbstractFormObjectType]은 양식 객체의 공통 속성을 정의한다. [AbstractFormObjectType]은 [AbstractShapeObjectType]을 기본 형식으로 가지고 추가적으로 필요한 속성이나 요소를 확장한다. [AbstractShapeObjectType]의 자세한 내용은 10.9.2를 참조한다.
[AbstractFormObjectType]은 추상 형식이므로 [AbstractFormObjectType]만으로는 XML 요소를 생성할 수 없다.
<a name="table-275"></a>
표 275 — AbstractFormObjectType 요소
속성 이름	설명
name	이름
foreColor	전경색
backColor	배경색
groupName	그룹 이름
tabStop	Tab 키로 객체들을 이동할 때 해당 객체에 멈출 수 있는지 설정하는 속성
editable	편집 가능 여부
tabOrder	Tab 키 이동 순서
enabled	활성화 여부
borderTypeIDRef	테두리 아이디 참조값
drawFrame	프레임 표시 가능 여부
printable	출력 가능 여부
<a name="table-276"></a>
표 276 — AbstractFormObjectType 하위 요소
하위 요소 이름	설명
formCharPr	양식 객체의 글자 속성
실습 154 AbstractFormObjectType 요소
code
Xml
<hp:btn caption="누름 단추" radioGroupName="" triState="0" name="PushButton1" foreColor="#000000"
backColor="#F0F0F0" groupName="" tabStop="1" editable="1" tabOrder="1" enabled="1" borderTypeIDRef="4"
drawFrame="1" printable="1" command="">
    <hp:formCharPr charPrIDRef="1" followContext="0" autoSz="0" wordWrap="0"/>
    <hp:sz width="7087" widthRelTo="ABSOLUTE" height="1964" heightRelTo="ABSOLUTE" protect="0"/>
    <hp:pos treatAsChar="1" affectLSpacing="1" flowWithText="1" allowOverlap="1" holdAnchorAndSO="1"
    vertRelTo="PARA" horzRelTo="PARA" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/>
    <hp:outMargin left="133" right="133" top="133" bottom="133"/>
</hp:btn>
<a name="s-10-11-1-2-sec"></a>
10.11.1.2 양식 객체의 글자 속성
<a name="figure-175"></a>
그림 175 — <formCharPr>의 구조
<a name="table-277"></a>
표 277 — formCharPr 요소
속성 이름	설명
charPrIDRef	글자 모양 아이디 참조값
followContext	양식 객체가 주위의 글자 속성을 따라갈지 여부
autoSize	자동 크기 조절 여부
wordWrap	줄 내림 여부
실습 155 formCharPr 예
code
Xml
<hp:formCharPr charPrIDRef="?" followContext="0" autoSz="0" wordWrap="0"/>
<a name="s-10-11-2-AbstractButtonObjectType"></a>
10.11.2 AbstractButtonObjectType
[AbstractButtonObjectType]은 버튼 양식 객체의 공통 속성을 정의한다. [AbstractButtonObjectType]은 [AbstractFormObjectType]을 기본 형식으로 가지고 추가적으로 필요한 속성이나 요소를 확장한다. [AbstractFormObjectType]의 자세한 내용은 10.11.1을 참조한다.
[AbstractButtonObjectType]은 추상 형식이므로 [AbstractButtonObjectType]만으로는 XML 요소를 생성할 수 없다.
---

## Source: okok1-2-3.md
<a name="source-okok123.md"></a>

복원된 텍스트 파일
fieldid 필드 개체 ID
<a name="table-132"></a>
표 132—fieldBegin 하위 요소
하위 요소 이름	설명
parameters	필드 동작에 필요한 인자들
subList	내용 수정 필드에서 사용됨
metaTag	메타태그 관련 정보
<a name="example-71"></a>
예제 71. fieldBegin 예
code
Xml
<hp:fieldBegin id="B179516910r" type="CLICK_HERE" name="editable" dirty="true" zorder="0"
fieldId="627272811">
    <hp:parameters count="3" name="">
```xml
        <hp:integerParam name="Prop">9</hp:integerParam>
        <hp:stringParam name="Command" xml:space="preserve">Clickhere:set:66:Direction:wstring:23:이곳을 마우스로 누르고 내용을 입력하세요.;HelpState:wstring:0:</hp:stringParam>
        <hp:stringParam name="Direction">이곳을 마우스로 누르고 내용을 입력하세요.</hp:stringParam>
    </hp:parameters>
    <hp:metaTag name=""></hp:metaTag>
</hp:fieldBegin>
```
10.7.2.2 CLICK_HERE
누름틀은 문서마당을 불러왔을 때 화면에 불린 문서마당의 빈 곳을 채워 넣을 안내문과 안내문에 대한 간단한 메모 내용을 입력하는 기능이다.
10.7.2.2.1 필요한 인자들
<a name="table-133"></a>
표 133— CLICK_HERE 요소
| 인자 이름 | 인자 형식 | 설명 |
| :---------- | :----------- | :------------- |
| Direction | stringParam | 안내문 문자열 |
| HelpState | stringParam | 안내문 도움말 |
<a name="example-72"></a>
예제 72. CLICK_HERE 예
code
Xml
```xml
<fieldBegin id="fb0r" type="CLICK_HERE" name="Title" editable="true" dirty="false">
    <parameters count="2">
        <stringParam name="Direction">이 곳에 내용 입력!</stringParam>
        <stringParam name="HelpState"></stringParam>
    </parameters>
</fieldBegin>
```
10.7.2.3 HYPERLINK
10.7.2.3.1 HYPERLINK
하이퍼링크는 문서의 특정한 위치에 현재 문서나 다른 문서, 웹 페이지, 전자우편 주소 등을 연결하여 쉽게 참조하거나 이동할 수 있게 해 주는 기능이다.
문서 내에서 그룹 객체를 사용할 경우 하이퍼링크 종류를 결정할 수 없는 경우가 발생할 수 있다. 각 개별 객체별로 하이퍼링크를 사용하고, 이 객체들을 하나의 그룹으로 묶을 경우 그룹 객체가 생성된다. 이때 생성된 그룹 객체는 그룹 내 객체들이 모두 같은 내용의 하이퍼링크 설정을 가지고 있지 않다면 하이퍼링크 종류, 하이퍼링크 대상, 문서창 옵션 등을 결정할 수 없게 된다. 이런 경우 그룹 객체의 하이퍼링크 설정은 HWPHYPERLINK_TYPE_DONTCARE, HWPHYPERLINK_TARGET_DOCUMENT_DONTCARE, HWPHYPERLINK_JUMP_DONTCARE의 값을 가져야 한다.
10.7.2.3.2 필요한 인자들
<a name="table-134"></a>
표 134—HYPERLINK 요소
| 인자 이름 | 인자 형식 | 설명 |
| :----------- | :------------ | :--------------------------------------------------------- |
| Path | stringParam | 링크 경로 |
| Category | stringParam | 하이퍼링크의 종류 |
| TargetType | stringParam | 하이퍼링크의 종류가 한글 문서인 경우, 한글 문서에서 대상의 종류 |
| DocOpenType | stringParam | 이동 시 문서창 옵션 |
하이퍼링크의 종류
<a name="table-135"></a>
표 135— 하이퍼링크 종류
| 하이퍼링크 종류 | 설명 |
| :---------------------------------- | :------------------------------------------------------------------------- |
| HWPHYPERLINK_TYPE_DONTCARE | 여러 개의 개체가 묶여진 그룹 객체 설정에서 하이퍼링크 종류가 다른 경우. |
| HWPHYPERLINK_TYPE_HWP | HWP 문서 내부의 책갈피 |
| HWPHYPERLINK_TYPE_URL | 웹 주소 |
| HWPHYPERLINK_TYPE_EMAIL | 메일 주소 |
| HWPHYPERLINK_TYPE_EXT | 외부 애플리케이션 문서 |
HWP 문서에서 대상의 종류
<a name="table-136"></a>
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
<a name="table-137"></a>
표 137— 문서창 옵션
| 이동 시 문서창 옵션 종류 | 설명 |
| :------------------------------ | :---------------------------------------------------------------- |
| HWPHYPERLINK_JUMP_DONTCARE | 동일 그룹 객체 내의 개별 객체들의 하이퍼링크 설정에서 문서창 옵션 종류가 다른 경우. |
| HWPHYPERLINK_JUMP_CURRENTTAB | 현재 문서 탭에서 열기 |
| HWPHYPERLINK_JUMP_NEWTAB | 새로운 문서 탭에서 열기 |
| HWPHYPERLINK_JUMP_NEWWINDOW | 새로운 문서 창에서 열기 |
<a name="example-73"></a>
예제 73. HYPERLINK 예
code
Xml
```xml
<fieldBegin id="fb02" type="HYPERLINK" editable="false" dirty="false">
    <parameters count="4">
        <stringParam name="Path">http://www.hancom.co.kr</stringParam>
        <stringParam name="Category">HWPHYPERLINK_TYPE_URL</stringParam>
        <stringParam name="TargetType">HWPHYPERLINK_TARGET_DOCUMENT_DONTCARE</stringParam>
        <stringParam name="DocOpenType">HWPHYPERLINK_JUMP_NEWTAB</stringParam>
    </parameters>
</fieldBegin>
```
10.7.2.4 BOOKMARK
10.7.2.4.1 BOOKMARK
두꺼운 책을 읽을 때 책의 중간에 책갈피를 꽂아 두고 필요할 때마다 펼쳐 보면 편리하듯이, [책갈피] 기능은 문서를 편집하는 도중에 본문의 여러 곳에 표시를 해 두었다가 현재 커서의 위치에 상관없이 표시해 둔 곳으로 커서를 곧바로 이동시키는 기능이다.
10.7.2.4.2 XML 예
<a name="example-74"></a>
예제 74. BOOKMARK 예
code
Xml
<fieldBegin id="fb03" type="BOOKMARK" name="txt0r" editable="false" dirty="false"/>
10.7.2.5 FORMULA
10.7.2.5.1 FORMULA
표 계산식은 표에서 덧셈, 뺄셈, 곱셈, 나눗셈 등 간단한 사칙연산은 물론 sum과 avg와 같은 함수를 사용하여 자동으로 계산하는 기능이다.
10.7.2.5.2 필요한 인자들
<a name="table-138"></a>
표 138— FORMULA 요소
| 인자 이름 | 인자 형식 | 설명 |
| :------------------ | :---------- | :--------------------- |
| FunctionName | stringParam | 계산식 함수 이름 |
| FunctionArguments | listParam | 계산식에 필요한 인자들 |
| ResultFormat | stringParam | 결과 출력 형식 |
| LastResult | stringParam | 마지막으로 계산된 결과 |
함수 목록
<a name="table-139"></a>
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
<a name="table-140"></a>
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
<a name="table-141"></a>
표 141 — 셀 번호
| A1 | B1 | C1 | D1 | E1 |
| :-- | :-- | :-- | :-- | :-- |
| A2 | B2 | C2 | D2 | E2 |
| A3 | B3 | C3 | D3 | E3 |
| A4 | B4 | C4 | D4 | E4 |
| A5 | B5 | C5 | D5 | E5 |
결과 출력 형식
<a name="table-142"></a>
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
<a name="example-75"></a>
예제 75. FORMULA 예
code
Xml
```xml
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
```
10.7.2.6 DATE 및 DOC_DATE
날짜/시간 표시. DATE 형식은 하위 호환성을 위해 남겨둔 형식이다. DATE 형식은 되도록 사용하지 않는 것을 권고한다.
10.7.2.6.1 필요한 인자들
<a name="table-143"></a>
표 143—DATE 요소
| 인자 이름 | 인자 형식 | 설명 |
| :---------- | :---------- | :----------------- |
| DateNation | stringParam | 국가 코드 |
| DateFormat | stringParam | 날짜/시간 표시 형식|
국가 코드
국가 코드는 기본적으로 ISO 국가 코드 표기법(ISO 3166-1 alpha-3)을 따른다. 단 모든 국가를 지원하지 않고 다음의 다섯 개 국가의 날짜/시간 형태만을 지원한다.
<a name="table-144"></a>
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
<a name="table-145"></a>
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
<a name="example-76"></a>
예제 76. DOC_DATE 예
code
Xml
```xml
<fieldBegin id="fb05" type="DOC_DATE" editable="false" dirty="false">
    <parameters count="2">
        <stringParam name="DateNation">KOR</stringParam>
        <stringParam name="DateFormat">YYYY-MM-DD hh:mm:ss</stringParam>
    </parameters>
</fieldBegin>
```
10.7.2.7 SUMMARY
10.7.2.7.1 Summary
문서 요약 정보는 현재 문서에 대한 제목, 주제, 지은이, 중심 낱말(키워드), 저자, 입력자, 교정자, 내용 요약, 주의사항 등을 간단히 기록할 수 있는 기능이다.
10.7.2.7.2 필요한 인자들
<a name="table-147"></a>
표 147—SUMMARY 요소
| 인자 이름 | 인자 형식 | 설명 |
| :-------- | :---------- | :----------------- |
| Property | stringParam | 문서 요약 정보 속성 |
문서 요약 정보 속성
<a name="table-148"></a>
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
<a name="example-77"></a>
예제 77. SUMMARY 예
code
Xml
```xml
<fieldBegin id="fb06" type="SUMMARY" editable="false" dirty="false">
    <parameters count="1">
        <stringParam name="Property">$title</stringParam>
    </parameters>
</fieldBegin>
```
10.7.2.8 USER_INFO
10.7.2.8.1 USER_INFO
사용자 정보는 현재 문서의 작성자에 대한 이름, 회사명, 전화번호 등을 간단히 기록할 수 있는 기능이다.
10.7.2.8.2 필요한 인자들
<a name="table-149"></a>
표 149— USER_INFO 요소
| 인자 이름 | 인자 형식 | 설명 |
| :-------- | :---------- | :--------------- |
| Category | stringParam | 사용자 정보 항목 |
사용자 정보 항목
<a name="table-150"></a>
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
<a name="example-78"></a>
예제 78. USER_INFO 예
code
Xml
```xml
<fieldBegin id="fb07" type="USER_INFO" editable="false" dirty="false">
    <parameters count="1">
        <stringParam name="Category">$UserName</stringParam>
    </parameters>
</fieldBegin>
```
10.7.2.9 PATH
10.7.2.9.1 Path
현재 문서의 물리적인 파일 경로를 문서에 표시해 주는 기능이다.
10.7.2.9.2 필요한 인자들
<a name="table-151"></a>
표 151 —PATH 요소
| 인자 이름 | 인자 형식 | 설명 |
| :-------- | :---------- | :------------- |
| Format | stringParam | 파일 경로 형식 |
파일 경로 형식
(주: OCR된 문서에서 표 152의 내용이 유실되었습니다.)
10.7.2.9.3 XML 예
<a name="example-79"></a>
예제 79. PATH 예
code
Xml
```xml
<fieldBegin id="fb07" type="PATH" editable="false" dirty="false">
    <parameters count="1">
        <stringParam name="Format">$P$F</stringParam>
    </parameters>
</fieldBegin>
```
10.7.2.10 CROSSREF
10.7.2.10.1 CROSSREF
상호 참조는 다른 곳의 그림, 표 등을 현재의 본문에서 항상 참조할 수 있도록 그 위치를 표시해 주는 기능이다.
10.7.2.10.2 필요한 인자들
<a name="table-153"></a>
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
<a name="table-154"></a>
표 154— 참조 경로 형식
| 구분 | 형식 |
| :--------------- | :--------------------------------- |
| 외부 문서 참조인 경우 | {문서의 파일 경로}?{참조 대상의 ID 또는 책갈피 이름} |
| 현재 문서 참조인 경우 | ?{참조 대상의 ID 또는 책갈피 이름} |
참조 대상 종류
<a name="table-155"></a>
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
<a name="table-156"></a>
표 156— 참조 내용
| 참조 내용 | 설명 |
| :------------------- | :------------------------------------------------------------------- |
| OBJECT_TYPE_PAGE | 참조 대상이 있는 쪽 번호 |
| OBJECT_TYPE_NUMBER | 참조 대상의 번호 |
| OBJECT_TYPE_CONTENTS | 참조 대상의 캡션 내용 또는 책갈피의 경우 책갈피 내용. 미주/각주의 경우 해당 형식을 사용할 수 없음 |
| OBJECT_TYPE_UPDOWNPOS| 현재 위치 기준으로 참조 대상이 있는 위치 (위/아래) |
10.7.2.10.3 XML 예
<a name="example-80"></a>
예제 80. CROSSREF 예
code
Xml
```xml
<fieldBegin id="fb10" type="CROSSREF" editable="false" dirty="false">
    <parameters count="5">
        <stringParam name="RefPath">?Table8</stringParam>
        <stringParam name="RefType">TARGET_TABLE</stringParam>
        <stringParam name="RefContentType">OBJECT_TYPE_NUMBER</stringParam>
        <booleanParam name="RefHyperLink">true</booleanParam>
        <stringParam name="RefOpenType">HWPHYPERLINK_JUMP_DONTCARE</stringParam>
    </parameters>
</fieldBegin>
```
10.7.2.11 MAILMERGE
10.7.2.11.1 MAILMERGE
메일 머지는 여러 사람의 이름, 주소 등이 들어 있는 '데이터 파일(data file)'과 '서식 파일(form letter)'을 결합(merging)함으로써, 이름이나 직책, 주소 부분 등만 다르고 나머지 내용이 같은 수십, 수백 통의 편지지를 한꺼번에 만드는 기능이다.
10.7.2.11.2 필요한 인자들
<a name="table-157"></a>
표 157-MAILMERGE 요소
| 인자 이름 | 인자 형식 | 설명 |
| :--------- | :---------- | :----------------------------------------------------- |
| FieldType | stringParam | 필드 형식. WAB, USER_DEFINE 중 하나의 값을 가질 수 있음 |
| FieldValue | stringParam | 필드 엔트리 이름 |
필드 엔트리 이름
필드 형식이 USER_DEFINE인 경우 별도의 정해진 이름 규칙은 없다.
필드 형식이 WAB인 경우에는 다음의 이름만을 사용해야 한다.
<a name="table-158"></a>
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
<a name="example-81"></a>
예제 81. MAILMERGE 예
code
Xml
```xml
<fieldBegin id="fb11" type="MAILMERGE" editable="false" dirty="false">
    <parameters count="2">
        <stringParam name="FieldType">WAB</stringParam>
        <stringParam name="FieldValue">SURNAME</stringParam>
    </parameters>
</fieldBegin>
```
10.7.2.12 MEMO
10.7.2.12.1 MEMO
메모는 현재 편집 중인 문서에서 특정 단어나 블록으로 설정한 문자열에 대한 간단한 추가 내용을 기록하는 기능이다.
10.7.2.12.2 필요한 인자들
<a name="table-159"></a>
표 159—MEMO 요소
| 인자 이름 | 인자 형식 | 설명 |
| :------------- | :------------ | :--------------------------------------------- |
| ID | stringParam | 메모를 식별하기 위한 아이디 |
| Number | integerParam | 메모 번호 |
| CreateDateTime | stringParam | 메모 작성 시각. KS X ISO 8601에 따라 'YYYY-MM-DD hh:mm:ss' 형식 사용 |
| Author | stringParam | 메모 작성자 |
| MemoShapeIDRef | stringParam | 메모 모양 속성 정보 아이디 참조값 |
10.7.2.12.3 XML 예
<a name="example-82"></a>
예제 82. MEMO 예
code
Xml
```xml
<fieldBegin id="fb11" type="MEMO" editable="true" dirty="true">
    <parameters count="5">
        <stringParam name="ID">memo1</stringParam>
        <integerParam name="Number">1</integerParam>
        <stringParam name="CreateDateTime">2011-01-01 10:00:00</stringParam>
        <stringParam name="Author">hancom</stringParam>
        <stringParam name="MemoShapeID">memoShape3</stringParam>
    </parameters>
    <subList ...>
```
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
<a name="table-160"></a>
표 160 — PROOFREADING_MARKS 요소
| 인자 이름 | 인자 형식 | 설명 |
| :------------------- | :----------- | :----------------------------------------------------------------- |
| Type | stringParam | 교정 부호 종류 |
| ProofreadingContents | stringParam | 교정 내용. 넣음표, 부호 넣음표, 고침표에서 사용됨 |
| MovingMargin | integerParam | 자리 옮김 여백. 오른/왼자리 옮김표에서 사용됨 |
| MovingStart | integerParam | 자리 옮김 시작위치. 오른/왼자리 옮김표에서 사용됨 |
| SplitType | stringParam | '자리 바꿈 나눔표'인지 '줄 서로 바꿈 나눔표'인지 여부. 자리/줄 서로 바꿈 나눔표에서 사용됨 |
교정 부호 종류
<a name="table-161"></a>
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
<a name="table-162"></a>
표 162—SplitType 요소
| 참조 내용 | 설명 |
| :-------- | :--------------------- |
| POSITION | 자리 바꿈 나눔표를 지칭|
| LINE | 줄 서로 바꿈 나눔표를 지칭 |
10.7.2.13.3 XML 예
<a name="example-83"></a>
예제 83. PROOFREADING_MARKS 예
code
Xml
```xml
<fieldBegin id="fb12" type="PROOFREADING_MARKS" editable="false" dirty="true">
    <parameters count="2">
        <stringParam name="Type">SIMPLE_CHANGE</stringParam>
        <stringParam name="ProofreadingContents">고칠 내용</stringParam>
    </parameters>
</fieldBegin>
```
10.7.2.14 PRIVATEINFO
10.7.2.14.1 PRIVATEINFO 요소
개인 정보 보호는 현재 화면에서 편집하고 있는 문서 내용 중 사용자가 블록으로 지정한 영역을 암호를 걸어 사용자가 선택한 글자표로 변경하는 기능이다.
10.7.2.14.2 필요한 인자들
<a name="table-163"></a>
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
<a name="table-164"></a>
표 164— 암호화 방식
| 참조 내용 | 설명 |
| :-------- | :---------------------------------- |
| AES | AES(Advanced Encryption Standard) |
(문서의 흐름상 METADATA, CITATION, BIBLIOGRAPHY 등이 이어지나, 제공된 OCR 텍스트는 순서가 일부 섞여 있습니다. 제공된 텍스트 순서대로 복원합니다.)
<a name="example-85"></a>
예제 85 METADATA 예```xml
```xml
<fieldBegin id="fb13" type="METADATA" editable="false" dirty="true">
<parameters count="4">
<stringParam name="ID">103e9eab2c70</stringParam>
<stringParam name="Property">http://www.w3.org/2002/12/cal/cal#dtstart</stringParam>
<stringParam name="Content">2007-09-16T16:00:00-05:00</stringParam>
<stringParam name="Datatype">xsd:dateTime</stringParam>
</parameters>
</fieldBegin>
```
code
Code
#### **10.7.2.16 CITATION**

**10.7.2.16.1 CITATION**
인용은 연구논문이나 다른 여타의 원본을 인용해야 하는 문서를 작성할 때 사용하는 기능이다. 인용은 다양한 형식의 인용 스타일을 선택하여 적용할 수 있다.

**10.7.2.16.2 필요한 인자**

<a name="table-166"></a>
표 166— CITATION 요소
| 인자 이름 | 인자 형식   | 설명                   |
| :-------- | :---------- | :--------------------- |
| GUID      | stringParam | 인용 고유 번호         |
| Result    | stringParam | 스타일이 적용된 인용 문자열 |

**10.7.2.16.3 XML 예**

<a name="example-86"></a>
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
<a name="s-10-7-2-18-METATAG"></a>
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
<a name="s-10-7-4-bookmark"></a>
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
<a name="s-10-7-5-sec"></a>
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
<a name="s-10-7-6-sec"></a>
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
```xml
<hp:autoNum num="1" numType="PAGE">
    <hp:autoNumFormat type="DIGIT" userChar="" prefixChar="" suffixChar="" supscript="0"/>
</hp:autoNum>
```
<a name="s-10-7-8-pageNumCtrl"></a>
10.7.8 pageNumCtrl 요소
쪽 번호를 홀수쪽, 짝수쪽 또는 양쪽 모두에 표시할지를 설정하기 위한 요소이다.
<a name="table-176"></a>
표 176 — pageNumCtrl 요소
| 속성 이름 | 설명 |
| :------------ | :--------- |
| pageStartsOn | 홀/짝수 구분 |
<a name="s-10-7-9-pageHiding"></a>
10.7.9 pageHiding 요소
현재 구역 내에서 감추어야 할 것들을 설정하기 위한 요소이다.
<a name="table-177"></a>
표 177 — pageHiding 요소
| 속성 이름 | 설명 |
| :------------- | :--------------- |
| hideHeader | 머리말 감추기 여부 |
| hideFooter | 꼬리말 감추기 여부 |
| hideMasterPage | 바탕쪽 감추기 여부 |
| hideBorder | 테두리 감추기 여부 |
| hideFill | 배경 감추기 여부 |
| hidePageNum | 쪽 번호 감추기 여부|
<a name="example-94"></a>
예제 94. pageHiding 예
code
Xml
<hp:pageHiding hideHeader="0" hideFooter="0" hideMasterPage="0" hideBorder="0" hideFill="0" hidePageNum="0"/>
<a name="s-10-7-10-pageNum"></a>
10.7.10 pageNum 요소
쪽 번호의 위치 및 모양을 설정하기 위한 요소이다.
<a name="table-178"></a>
표 178 — pageNum 요소
| 속성 이름 | 설명 |
| :--------- | :--------- |
| pos | 번호 위치 |
| formatType | 번호 모양 종류 |
| sideChar | 줄표 넣기 |
<a name="example-95"></a>
예제 95. pageNum 예
code
Xml
<hp:pageNum pos="BOTTOM_CENTER" formatType="DIGIT" sideChar="-"/>
<a name="s-10-7-11-indexmark"></a>
10.7.11 indexmark 요소
<indexmark>는 찾아보기(Index, 색인)와 관련된 정보를 갖고 있는 요소이다.
<a name="table-179"></a>
표 179 —indexmark 요소
| 하위 요소 이름 | 설명 |
| :------------- | :---------------------------------------------------------------------- |
| firstKey | 찾아보기에 사용할 첫 번째 키워드. 요소의 값으로 키워드 문자열을 가짐. |
| secondKey | 찾아보기에 사용할 두 번째 키워드. 요소의 값으로 키워드 문자열을 가짐. |
<a name="example-96"></a>
예제 96. indexmark 예
code
Xml
```xml
<hp:indexmark>
    <hp:firstKey>aa</hp:firstKey>
    <hp:secondKey>aa</hp:secondKey>
</hp:indexmark>
```
<a name="s-10-7-12-hiddenComment"></a>
10.7.12 hiddenComment 요소
<hiddenComment>는 숨은 설명을...
<a name="table-180"></a>
표 180 — hiddenComment 요소
| 하위 요소 이름 | 설명 |
| :------------- | :--------------- |
| subList | 숨은 설명 내용 (10.1.1 참조) |
<a name="example-97"></a>
예제 97. hiddenComment 예
code
Xml
```xml
<hp:hiddenComment>
    <hp:subList ...>
        <hp:p ...>
            <hp:run charPrIDRef="6">
                <hp:t>
                    <hp:insertBegin id="55" TcId="19"/>
```
                    숨은 설명입니다.
                    <hp:insertEnd id="55" TcId="19" paraend="0"/>
                </hp:t>
            </hp:run>
            ...
        </hp:p>
    </hp:subList>
</hp:hiddenComment>
(10.8.1) t 요소
<a name="table-182"></a>
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
<a name="s-10-8-2-markpenBegin"></a>
10.8.2 markpenBegin 요소
형광펜 색상 정보를 담고 있는 요소이다.
<a name="table-183"></a>
표 183 —markpenBegin 요소
| 속성 이름 | 설명 |
| :--------- | :--------- |
| beginColor | 형광펜 색상 |
<a name="example-98"></a>
예제 98. markpenBegin 예
code
Xml
<hp:markpenBegin color="#FFFF0000"/>
sampletext
<hp:markpenEnd/>
(10.8.3 titleMark 요소)
(주: 문서 번호는 유실되었으나 표 182의 내용에 근거하여 복원)
<a name="table-184"></a>
표 184 —titleMark 요소
| 속성 이름 | 설명 |
| :-------- | :------------------------------------------ |
| ignore | 제목 차례 표시 여부. true: 차례 만들기 무시 |
<a name="s-10-8-4-tab"></a>
10.8.4 tab 요소
<a name="table-185"></a>
표 185— tab 요소
| 속성 이름 | 설명 |
| :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| width | 탭의 간격 |
| leader | 탭의 채움모양 (LineType 참조) |
| type | 탭 종류. LEFT: 왼쪽 정렬 탭, RIGHT: 오른쪽 정렬 탭, CENTER: 가운데 정렬 탭, DECIMAL: 소수점 정렬 탭 |
<a name="example-99"></a>
예제 99. tab 예
code
Xml
<hp:tab width="31188" leader="0" type="2"/>
<a name="s-10-8-5-sec"></a>
10.8.5 변경 추적 요소 형식
<insertBegin>, <insertEnd>, <deleteBegin>, <deleteEnd> 요소는 [TrackChangeTag] 형식을 기본으로 하며, [TrackChangeTag]는 변경 추적 정보를 정의한 형식이다.
<a name="table-186"></a>
표 186 —TrackChangeTag 요소
| 속성 이름 | 설명 |
| :-------- | :----------------------- |
| id | 변경 추적을 식별하기 위한 아이디 |
| TcId | 변경 추적 아이디 참조값 |
| paraend | 문단 끝 포함 여부 |
<a name="example-100"></a>
예제 100. TrackChangeTag 예
code
Xml
```xml
<hp:run charPrIDRef="1">
    <hp:t>
```
        프로그램입니다.
        <hp:insertBegin id="1" TcId="7"/>
        <hp:insertEnd id="1" TcId="7" paraend="1"/>
    </hp:t>
</hp:run>
<a name="s-10-9-sec"></a>
10.9 기본 도형 객체
<a name="s-10-9-1-sec"></a>
10.9.1 도형 객체
기본 도형 객체는 표, 그림, 수식, 컨테이너와 같은 문서 내에서 텍스트 이외의 기본적인 객체들을 뜻한다. 기본 도형 객체들은 [AbstractShapeObjectType]을 기본 형식(base type)으로 가진다.
<a name="s-10-9-2-AbstractShapeObjectType"></a>
10.9.2 AbstractShapeObjectType
<a name="s-10-9-2-1-AbstractShapeObjectType"></a>
10.9.2.1 AbstractShapeObjectType
[AbstractShapeObjectType]은 기본 도형 객체들의 공통된 속성을 정의한 형식이다. 기본 도형 객체들은 [AbstractShapeObjectType]을 기본 형식으로 가지고 추가적으로 필요한 속성이나 요소를 확장해서 사용한다. [AbstractShapeObjectType]은 추상 형식이므로 이것만으로는 XML 요소를 생성할 수 없다.
<a name="table-187"></a>
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
<a name="table-188"></a>
표 188 — AbstractShapeObjectType 하위 요소
| 하위 요소 이름 | 설명 |
| :------------- | :----------------- |
| sz | 크기 정보 |
| pos | 위치 정보 |
| outMargin | 바깥 여백 |
| caption | 캡션 |
| shapeComment | ... |
| metaTag | 메타태그 관련 정보 |
<a name="example-101"></a>
예제 101. AbstractShapeObjectType 예
code
Xml
<hp:rect id="1790879982" zOrder="1" numberingType="PICTURE" textWrap="IN_FRONT_OF_TEXT" textFlow="BOTH_SIDES" lock="0" dropcapStyle="None">
<a name="s-10-9-2-2-sec"></a>
10.9.2.2 객체 크기 정보
객체들의 크기 정보를 가지고 있는 요소이다.
(주: OCR된 문서에서 sz 요소에 대한 설명이 누락되었습니다.)
<a name="s-10-9-2-3-sec"></a>
10.9.2.3 객체 위치 정보
<a name="table-190"></a>
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
<a name="example-102"></a>
예제 102. pos 예
code
Xml
<hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="0" allowOverlap="1" holdAnchorAndSO="0" vertRelTo="PAPER" horzRelTo="PAPER" vertAlign="TOP" horzAlign="LEFT" vertOffset="9579" horzOffset="9827"/>
<a name="s-10-9-2-4-sec"></a>
10.9.2.4 객체 바깥 여백
<outMargin> 요소는 [MarginAttributeGroup]을 속성으로 포함한다. [MarginAttributeGroup]은 10.6.6.2를 참조한다.
<a name="table-191"></a>
표 191—outMargin 요소
| 속성 이름 | 설명 |
| :-------------------- | :------------- |
| [MarginAttributeGroup]| 10.6.6.2 참조 |
<a name="example-103"></a>
예제 103. outMargin 예
code
Xml
<hp:outMargin left="0" right="0" top="0" bottom="0"/>
<a name="s-10-9-2-5-sec"></a>
10.9.2.5 캡션
<caption> 요소는 하위 요소로 <subList> 요소를 가진다. <subList> 요소는 11.1.2를 참조한다.
<a name="table-192"></a>
표 192 — caption 요소
| 속성 이름 | 설명 |
| :-------- | :----------------------------- |
| side | ... |
| fullSize | 캡션 폭에 마진을 포함할지 여부 |
| width | 캡션 폭 |
| gap | 캡션과 틀 사이의 간격 |
| lastWidth | 텍스트 최대 길이 (=객체의 폭) |
<a name="table-193"></a>
표 193 — caption 하위 요소
| 하위 요소 이름 | 설명 |
| :------------- | :------------------- |
| subList | 캡션 내용 (11.1.2 참조) |
<a name="example-104"></a>
예제 104. caption 예
code
Xml
```xml
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
```
<a name="s-10-9-3-tbl"></a>
<a name="hp-tbl"></a>
10.9.3 tbl 요소
<a name="s-10-9-3-1-tbl"></a>
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
<a name="table-195"></a>
표 195 —tbl 하위 요소
| 하위 요소 이름 | 설명 |
| :------------- | :----------- |
| inMargin | 안쪽 여백 |
| cellzoneList | 셀존 목록 |
| tr | 행 |
| label | 레이블 |
<a name="example-105"></a>
예제 105. tbl 예
code
Xml
```xml
<hp:tbl id="1811647054" zOrder="0" numberingType="TABLE" textWrap="TOP_AND_BOTTOM" textFlow="BOTH_SIDES" lock="0" dropcapStyle="None" pageBreak="CELL" repeatHeader="1" rowCnt="5" colCnt="5" cellSpacing="0" borderFillIDRef="3" noAdjust="0">
    <hp:sz width="41950" widthRelTo="ABSOLUTE" height="6410" heightRelTo="ABSOLUTE" protect="0"/>
    <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="COLUMN" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/>
    <hp:outMargin left="283" right="283" top="283" bottom="283"/>
    <hp:inMargin left="510" right="510" top="141" bottom="141"/>
```
    ...
</hp:tbl>
<a name="s-10-9-3-2-inMargin"></a>
10.9.3.2 inMargin 요소
<inMargin> 요소는 안쪽 여백 정보로 [MarginAttributeGroup] 속성을 포함한다. [MarginAttributeGroup]은 10.6.6.2를 참조한다.
<a name="table-196"></a>
표 196 —inMargin 요소
| 속성 이름 | 설명 |
| :-------------------- | :------------- |
| [MarginAttributeGroup]| 10.6.6.2 참조 |
<a name="example-106"></a>
예제 106. inMargin 예
code
Xml
<hp:inMargin left="510" right="510" top="141" bottom="141"/>
<a name="s-10-9-3-3-cellzoneList"></a>
10.9.3.3 cellzoneList 요소
<a name="s-10-9-3-3-1-cellzoneList"></a>
10.9.3.3.1 cellzoneList
표는 표 전체 또는 표 부분적으로 배경색 및 테두리와 같은 속성을 줄 때, 영역을 지정하기 위해서 <cellzone> 요소를 사용한다.
<a name="table-197"></a>
표 197 —cellzoneList 하위 요소
| 하위 요소 이름 | 설명 |
| :------------- | :----- |
| cellzone | 셀존 |
<a name="s-10-9-3-3-2-cellzone"></a>
10.9.3.3.2 cellzone 요소
Cell zone은 표에서 스타일 및 모양이 적용되는 단위이다.
<a name="table-198"></a>
표 198 — cellzone 요소
| 속성 이름 | 설명 |
| :-------------- | :--------------------------------- |
| startRowAddr | 셀존 row의 시작 주소 (0부터 시작) |
| startColAddr | 셀존 column의 시작 주소 (0부터 시작) |
| endRowAddr | 셀존 row의 끝 주소 (0부터 시작) |
| endColAddr | 셀존 column의 끝 주소 (0부터 시작) |
| borderFillIDRef | 테두리/배경 아이디 참조값 |
<a name="s-10-9-3-4-tr"></a>
10.9.3.4 tr 요소
표에서 하나의 행을 표현한다.
(주: OCR된 문서에서 tc 요소에 대한 설명이 tr 요소 설명에 포함되어 있습니다. 분리하여 정리합니다.)
tc 요소 (셀)
<a name="table-201"></a>
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
<a name="example-108"></a>
예제 108. tc 예```xml
```xml
<hp:tc name="" header="0" hasMargin="0" protect="0" editable="0" dirty="0" borderFillIDRef="4">
<hp:subList ...> ... </hp:subList>
<hp:cellAddr colAddr="4" rowAddr="0"/>
<hp:cellSpan colSpan="1" rowSpan="1"/>
<hp:cellSz width="8390" height="282"/>
<hp:cellMargin left="510" right="510" top="141" bottom="141"/>
</hp:tc>
```
code
Code
*   **셀 주소**

<a name="table-202"></a>
표 202 —cellAddr 요소
| 속성 이름 | 설명                                                   |
| :-------- | :----------------------------------------------------- |
| colAddr   | 셀의 열 주소. 0부터 시작하며 오른쪽으로 1씩 증가.      |
| rowAddr   | 셀의 행 주소. 0부터 시작하며 아래쪽으로 1씩 증가.      |

<a name="example-109"></a>
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
<a name="s-10-9-3-5-Label"></a>
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
<a name="table-209"></a>
표 209 — AbstractShapeComponentType 요소
| 속성 이름 | 설명 |
| :----------- | :--------------- |
| href | 하이퍼링크 속성 |
| groupLevel | ... |
| instid | 객체 아이디 |
<a name="table-210"></a>
표 210 — AbstractShapeComponentType 하위 요소
| 하위 요소 이름 | 설명 |
| :------------- | :----------------------------- |
| offset | 객체가 속한 그룹 내에서의 오프셋 정보 |
| orgSz | 객체 생성 시 최초 크기 |
| curSz | 객체의 현재 크기 |
| flip | 객체가 뒤집어진 상태인지 여부 |
| rotationInfo | 객체 회전 정보 |
| renderingInfo | 객체 렌더링 정보 |
<a name="example-115"></a>
예제 115. AbstractShapeComponentType 예
code
Xml
```xml
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
```
(행렬 값은 생략)
<a name="s-10-9-5-2-sec"></a>
10.9.5.2 객체가 속한 그룹 내에서의 오프셋 정보
그룹 객체 내에서 개별 객체들의 그룹 내 상대 위치 정보를 가지고 있는 요소이다.
<a name="table-211"></a>
표 211 — offset 요소
| 속성 이름 | 설명 |
| :-------- | :------------------------------- |
| x | 객체가 속한 그룹 내에서의 x offset |
| y | 객체가 속한 그룹 내에서의 y offset |
<a name="example-116"></a>
예제 116. offset 예
code
Xml
<hp:offset x="0" y="0"/>
<a name="s-10-9-5-3-sec"></a>
10.9.5.3 객체 생성 시 최초 크기
객체 생성 시 최초 크기 정보를 가지고 있는 요소이다.
<a name="table-212"></a>
표 212 —orgSz 요소
| 속성 이름 | 설명 |
| :-------- | :----------------------------------- |
| width | 객체 생성 시 최초 폭. 단위는 HWPUNIT. |
| height | 객체 생성 시 최초 높이. 단위는 HWPUNIT. |
<a name="example-117"></a>
예제 117. orgSz 예
code
Xml
<hp:orgSz width="16800" height="12825"/>
<a name="s-10-9-5-4-sec"></a>
10.9.5.4 객체의 현재 크기
객체의 현재 크기 정보를 가지고 있는 요소이다.
<a name="table-213"></a>
표 213 —curSz 요소
| 속성 이름 | 설명 |
| :-------- | :------------------------------- |
| width | 객체의 현재 폭. 단위는 HWPUNIT. |
| height | 객체의 현재 높이. 단위는 HWPUNIT. |
<a name="example-118"></a>
예제 118. curSz 예
code
Xml
<hp:curSz width="12500" height="5000"/>
<a name="s-10-9-5-5-sec"></a>
10.9.5.5 객체가 뒤집어진 상태인지 여부
객체의 반전 여부 정보를...
<a name="table-214"></a>
표 214 —flip 요소
| 속성 이름 | 설명 |
| :--------- | :------------------------- |
| horizontal | 좌우로 뒤집어진 상태인지 여부 |
| vertical | 상하로 뒤집어진 상태인지 여부 |
<a name="example-119"></a>
예제 119. flip 예
code
Xml
<hp:flip horizontal="1" vertical="1"/>
<a name="s-10-9-5-6-sec"></a>
10.9.5.6 객체 회전 정보
객체의 회전 정보를 가지고 있는 요소이다.
<a name="table-215"></a>
표 215—rotationInfo 요소
| 속성 이름 | 설명 |
| :---------- | :------------- |
| angle | 회전각 |
| centerX | 회전 중심의 x 좌표 |
| centerY | 회전 중심의 y 좌표 |
| rotateimage | 이미지 회전 여부 |
<a name="example-120"></a>
예제 120. rotationinfo 예
code
Xml
<hp:rotationInfo angle="0" centerX="6250" centerY="2500" rotateimage="1"/>
<a name="s-10-9-5-7-sec"></a>
10.9.5.7 객체 렌더링 정보
<a name="s-10-9-5-7-1-sec"></a>
10.9.5.7.1 객체 렌더링
객체 렌더링 시 필요한, 변환 행렬, 확대/축소 행렬, 회전 행렬을 가지고 있는 요소이다.
---

## Source: okok1-3.md
<a name="source-okok13.md"></a>

KS X 6101:2024 (전체 복원 및 수정)
<a name="s-16-2-Signature"></a>
16.2 Signature의 요소
<a name="s-16-2-1-Signature"></a>
16.2.1 Signature의 구조
<a name="table-323"></a>
표 323 — Signature 요소
하위 요소 이름	설명
ds:SignedInfo	전자서명에 대한 정규화 알고리즘, 서명(해시) 알고리즘, 전자서명 대상에 대한 링크 정보
ds:SignatureValue	base64 인코딩된 전자서명 값
ds:KeyInfo	전자서명에 사용된 키에 대한 정보
ds:Object	전자서명 대상에 대한 정보
<a name="s-16-2-2-dsSignedInfo"></a>
16.2.2 ds:SignedInfo의 요소
<a name="figure-211"></a>
그림 211 — ds:SignatureMethod의 구조
<a name="table-325"></a>
표 325 — ds:SignatureMethod 요소
속성 이름	설명
URI	전자서명된 원본 문서의 위치
<a name="table-326"></a>
표 326 — ds:SignatureMethod 하위 요소
하위 요소 이름	설명
ds:Transforms	서명에 적용한 순서화된 목록. 정규화, 인코딩/디코딩, 암호화에 대한 식별 정보
ds:DigestMethod	전자서명에 적용된 해시 알고리즘
ds:DigestValue	서명된 전자서명의 실제 값
<a name="s-16-2-3-dsKeyInfo"></a>
16.2.3 ds:KeyInfo의 요소
ds:KeyInfo는 전자서명에 사용된 키에 대한 정보로, 서명을 검증할 수 있도록 공개키를 포함한다. OWPML에서는 공개키로 공인인증서를 사용하며 ds:KeyInfo의 요소 중 ds:X509Data를 사용한다.
<a name="s-16-2-4-dsObject"></a>
16.2.4 ds:Object의 요소
ds:Object는 전자서명의 대상을 명시하기 위한 요소이다.
<a name="s-16-3-XML"></a>
16.3 XML 예
<a name="sample-180"></a>
샘플 180 — SignatureMethod 예
code
Xml
```xml
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
    <ds:SignedInfo>
        <ds:CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
        <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
        <ds:Reference URI="">
            <ds:Transforms>
                <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
            </ds:Transforms>
            <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
            <ds:DigestValue>zGeX...</ds:DigestValue>
        </ds:Reference>
    </ds:SignedInfo>
    <ds:SignatureValue>pOF8Wg==</ds:SignatureValue>
    <ds:KeyInfo>
        <ds:X509Data>
            <ds:X509IssuerSerial>
                <ds:X509IssuerName>...</ds:X509IssuerName>
                <ds:X509SerialNumber>60002</ds:X509SerialNumber>
            </ds:X509IssuerSerial>
            <ds:X509Certificate>lBfv0WUvA==</ds:X509Certificate>
        </ds:X509Data>
    </ds:KeyInfo>
    <ds:Object>
        <ds:Manifest Id="...">
            <ds:Reference URI="...">
                <ds:Transforms>
                    <ds:Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
                </ds:Transforms>
                <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
                <ds:DigestValue>16AOwY...</ds:DigestValue>
            </ds:Reference>
        </ds:Manifest>
    </ds:Object>
</ds:Signature>
```
17 하위 호환성 요소
<a name="s-17-1-sec"></a>
17.1 하위 호환성
하위 호환성 요소는 상위 버전에서 만든 문서를 하위 버전 문서에서 처리하기 위한 구조를 말한다.
<a name="s-17-2-switch"></a>
17.2 switch 요소
<a name="s-17-2-1-switch"></a>
17.2.1 switch
<switch>는 호환이 필요한 구조의 요소 아래 위치할 수 있다. <switch> 아래의 구조는 호환이 되는 구조를 포함한다. <case>의 하위 조건을 만족한다면 하위 구조를 선택하고 그렇지 않을 경우 <default> 하위 구조를 따른다.
<a name="figure-212"></a>
그림 212 — <switch>의 구조
<a name="table-327"></a>
표 327 — switch 요소
하위 요소 이름	설명
case	호환 구조
default	대체 구조
<a name="s-17-2-2-case"></a>
17.2.2 case 요소
<case> 요소는 호환이 필요한 구조의 대체 표현을 포함하고 있다. <case> 요소는 여러 개 올 수 있으며, 향상된 호환을 위하여 최적 렌더링 포맷 순으로 정렬하는 것이 좋다. <case>의 하위 속성인 <required-namespace>를 확인하여 하위 구조를 선택한다.
<a name="table-328"></a>
표 328 — case 요소
속성 이름	설명
required-namespace	호환 조건
<a name="s-17-2-3-default"></a>
17.2.3 default 요소
<default> 요소는 어떤 <case>도 렌더링할 수 없을 때의 기본 호환 구조를 제공한다.
<a name="s-17-3-XML"></a>
17.3 XML 예
<a name="sample-181"></a>
샘플 181 — switch 예
code
Xml
```xml
<hp:run chwpPrIDRef="1">
    <hp:switch>
        <hp:case required-namespace="http://www.hancom.co.kr/hwpml/2016/ooxmlchart">
            <hp:chart id="430597883" zOrder="0" numberingType="PICTURE" textWrap="TIGHT" textFlow="BOTH_SIDES" lock="0" ctrlch="-1" ctrlid="-610494580" dropcapstyle="None" chartIDRef="Chart/chart1.xml">
                <hp:sz width="32250" widthRelTo="ABSOLUTE" height="18750" heightRelTo="ABSOLUTE" protect="0"/>
                <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="COLUMN" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/>
                <hp:outMargin left="0" right="0" top="0" bottom="0"/>
            </hp:chart>
        </hp:case>
        <hp:default>
            <hp:ole id="-143059788" textFlow="BOTH_SIDES" lock="0" href="..." groupLevel="0" instid="0" objectType="UNKNOWN" binaryItemIDRef="ole" hasMoniker="0" drawAspect="CONTENT" eqBaseLine="0">
                <hp:offset x="0" y="0"/>
                <hp:orgSz width="7200" height="7200"/>
                <hp:curSz width="0" height="0"/>
                <hp:flip horizontal="0" vertical="0"/>
                <hp:rotationInfo angle="0" centerX="452816845" centerY="3452816845" rotationangle="-1"/>
                <hp:renderingInfo>
                    <hp:transMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
                    <hp:scaMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
                    <hp:rotMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>
                </hp:renderingInfo>
                <hp:extent width="7200" height="7200"/>
                <hp:lineShape color="#000000" width="0" style="NONE" endCap="ROUND" headStyle="NORMAL" tailStyle="NORMAL" headfill="0" tailfill="0" outlineStyle="NORMAL" alpha="0"/>
                <hp:sz width="32250" widthRelTo="ABSOLUTE" height="18750" heightRelTo="ABSOLUTE" protect="0"/>
                <hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="COLUMN" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/>
                <hp:outMargin left="0" right="0" top="0" bottom="0"/>
            </hp:ole>
        </hp:default>
    </hp:switch>
</hp:run>
```
부속서 A (참고)
A.1 개방성 확보
국내 유통되는 전자 문서 형식의 대다수를 차지하는 국내 사실상(De Facto)의 워드프로세서형 문서의 표준인 HWP 바이너리 포맷을 XML 기반의 OWPML로 표준화함으로써, 바이너리 문서(11년 6월 공개)의 내부 구조를 100% 재표현하여 공공성 및 개방성을 확보하고, 보존성을 높이는 것이 이 표준의 목적이다. 이러한 개방성 확보 및 기술의 오픈 생태계 기반 마련을 통하여 특정 기업의 솔루션에 종속적이지 않은 문서의 생산, 유통 환경에서 기존의 HWP 바이너리 문서의 호환성 및 표현 기술 기반의 개방형, 기술 독립적인 OWPML 개방형 표준을 기존 레거시 포맷을 대신하여 사용할 수 있다. 또한, 국내 워드프로세서형 문서 포맷에 보다 많은 전문가의 참여를 유도하여 문서 형식 자체에 대한 고도화를 추구한다.
A.2 안정성 확보
국가기록원, 공인 전자 문서 보관소 등 다양한 장기 보존 시스템에 저장된 레거시 문서의 장기 보존 안정성을 확보하는 것이 이 표준의 목적이다. 기존 바이너리 포맷의 문서를 표준화된 XML 기반의 문서 형식으로 변환함으로써 문서에 대한 유지 보수 및 관리상의 안정성을 확보할 수 있다.
A.3 경제성 확보
공공 기관의 경우, WTO 협정에 따라 향후 국제 및 국내 표준 문서를 표준 전자 문서로 마이그레이션이 필요하다. OWPML의 표준화를 통해서 다양한 애플리케이션을 통한 기존의 HWP 바이너리 형식 문서를 표준 포맷 형식의 문서로 마이그레이션하는 데 드는 비용이 절감될 수 있다.
A.4 기술 개발 기회의 확대
표준화를 통해 hwp 바이너리 형식과 owpml의 변환을 가능하게 함으로써, 특정 기업의 애플리케이션에 종속적이었던 문서 형식을 이용하여 누구나 다양한 애플리케이션의 개발 및 포맷 형식의 발전을 가져올 수 있다.
부속서 B (XML Schema Definition)
(제공된 OCR 텍스트를 기반으로 XML 스키마 정의를 처음부터 끝까지 복원한 내용입니다.)
code
Xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
```
           xmlns:hc="http://www.hancom.co.kr/hwpml/2011/head"
           targetNamespace="http://www.hancom.co.kr/hwpml/2011/head"
           elementFormDefault="qualified">

<xs:element name="head" type="hc:HWPMLHeadType">
    <xs:annotation>
        <xs:documentation>Root Element</xs:documentation>
    </xs:annotation>
</xs:element>

<xs:complexType name="HWPMLHeadType">
    <xs:sequence>
        <xs:element name="beginNum">
            <xs:annotation>
                <xs:documentation>시작 번호</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="page" type="xs:positiveInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>페이지 시작 번호</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="footnote" type="xs:positiveInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>각주 시작 번호</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="endnote" type="xs:positiveInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>미주 시작 번호</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="pic" type="xs:positiveInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>그림 시작 번호</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="tbl" type="xs:positiveInteger" use="required">
                     <xs:annotation>
                        <xs:documentation>표 시작 번호</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="equation" type="xs:positiveInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>수식 시작 번호</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="refList" type="MappingTableType" minOccurs="1"/>
        <xs:element name="forbiddenWordList" type="ForbiddenWordListType" minOccurs="0"/>
        <xs:element name="compatibleDocument" type="CompatibleDocumentType" minOccurs="0"/>
        <xs:element name="trackchangeConfig">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="trackChangeEncryption" type="hc:KeyEncryptionType" minOccurs="0"/>
                </xs:sequence>
                <xs:attribute name="flags" type="xs:nonNegativeInteger"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="docOption" type="DocOptionType" minOccurs="0"/>
        <xs:element name="metaTag" type="hc:MetaTagType" minOccurs="0"/>
    </xs:sequence>
    <xs:attribute name="version" type="xs:string" use="required"/>
    <xs:attribute name="secCnt" type="xs:nonNegativeInteger" use="required"/>
</xs:complexType>

<xs:complexType name="DocOptionType">
    <xs:sequence>
        <!-- ... DocOptionType의 세부 자식 요소들 ... -->
        <xs:element name="licensemark" minOccurs="0">
            <xs:complexType>
                <xs:attribute name="type" type="xs:unsignedInt" use="required"/>
                <xs:attribute name="flag" type="xs:byte" use="required"/>
                <xs:attribute name="lang" type="xs:byte"/>
            </xs:complexType>
        </xs:element>
    </xs:sequence>
</xs:complexType>

<xs:complexType name="MappingTableType">
    <xs:annotation>
        <xs:documentation>매핑 테이블. 본문에서 사용될 각종 데이터를 가지고 있는 엘리먼트.</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="fontfaces">
            <xs:annotation>
                <xs:documentation>글꼴 리스트.</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="fontface" type="FontfaceType" minOccurs="1" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:positiveInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="borderFills" minOccurs="0">
            <xs:annotation>
                <xs:documentation>테두리/배경/채우기 정보</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="borderFill" type="BorderFillType" minOccurs="0" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:positiveInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>테두리/배경 항목의 개수</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="charProperties">
            <xs:annotation>
                <xs:documentation>글자 모양 정보</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="charPr" type="CharShapeType" minOccurs="1" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:positiveInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="tabProperties" minOccurs="0">
            <xs:annotation>
                <xs:documentation>탭 모양 정보</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="tabPr" type="TabDefType" minOccurs="0" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:nonNegativeInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="numberings" minOccurs="0">
            <xs:annotation>
                <xs:documentation>문단 번호 모양</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="numbering" type="NumberingType" minOccurs="0" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:nonNegativeInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="bullets" minOccurs="0">
            <xs:annotation>
                <xs:documentation>글머리표 문단 모양</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="bullet" type="BulletType" minOccurs="0" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:nonNegativeInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="paraProperties">
            <xs:annotation>
                <xs:documentation>문단 모양</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="paraPr" type="ParaShapeType" maxOccurs="unbounded"/>
                </xs:sequence>
                <xs:attribute name="itemCnt" type="xs:positiveInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="styles">
            <xs:annotation>
                <xs:documentation>스타일</xs:documentation>
            </xs:annotation>
            <!-- ... styles 세부 정의 ... -->
        </xs:element>
    </xs:sequence>
</xs:complexType>

<xs:complexType name="FontfaceType">
    <xs:sequence>
        <xs:element name="font" minOccurs="1" maxOccurs="unbounded">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="typeInfo" minOccurs="0">
                        <xs:annotation>
                            <xs:documentation>글꼴 정보</xs:documentation>
                        </xs:annotation>
                        <xs:complexType>
                            <xs:attribute name="familyType" use="required">
                                <xs:annotation>
                                    <xs:documentation>글꼴 계열</xs:documentation>
                                </xs:annotation>
                                <xs:simpleType>
                                    <xs:restriction base="xs:string">
                                        <xs:enumeration value="FCAT_UNKNOWN"/>
                                        <xs:enumeration value="FCAT_MYUNGJO">
                                            <xs:annotation><xs:documentation>serif</xs:documentation></xs:annotation>
                                        </xs:enumeration>
                                        <xs:enumeration value="FCAT_GOTHIC">
                                            <xs:annotation><xs:documentation>sans-serif</xs:documentation></xs:annotation>
                                        </xs:enumeration>
                                        <xs:enumeration value="FCAT_SSERIF">
                                            <xs:annotation><xs:documentation>monospace</xs:documentation></xs:annotation>
                                        </xs:enumeration>
                                        <xs:enumeration value="FCAT_BRUSHSCRIPT">
                                            <xs:annotation><xs:documentation>cursive</xs:documentation></xs:annotation>
                                        </xs:enumeration>
                                        <xs:enumeration value="FCAT_DECORATIVE">
                                             <xs:annotation><xs:documentation>decorative</xs:documentation></xs:annotation>
                                        </xs:enumeration>
                                        <!-- OCR 불분명한 값들 생략 -->
                                    </xs:restriction>
                                </xs:simpleType>
                            </xs:attribute>
                            <xs:attribute name="serifStyle" type="xs:string">
                                <xs:annotation><xs:documentation>세리프 유형</xs:documentation></xs:annotation>
                            </xs:attribute>
                            <!-- weight, proportion, contrast, strokeVanation, armStyle, letterform, midline, xHeight 등 속성 -->
                        </xs:complexType>
                    </xs:element>
                </xs:sequence>
                <xs:attribute name="id" type="xs:nonNegativeInteger" use="required">
                    <xs:annotation><xs:documentation>글꼴 아이디</xs:documentation></xs:annotation>
                </xs:attribute>
                <xs:attribute name="face" type="xs:string" use="required">
                     <xs:annotation><xs:documentation>글꼴 이름</xs:documentation></xs:annotation>
                </xs:attribute>
                <xs:attribute name="type" use="required">
                    <xs:annotation><xs:documentation>글꼴 유형 (rep: 대표글꼴, ttf: 트루타입글꼴, hft: 한/글전용 글꼴)</xs:documentation></xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="REP"/>
                            <xs:enumeration value="TTF"/>
                            <xs:enumeration value="HFT"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="isEmbedded" type="xs:boolean" default="false"/>
                <xs:attribute name="binaryItemIDRef" type="xs:string"/>
            </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="lang" use="required">
        <xs:annotation><xs:documentation>언어(한글, 영어 등)</xs:documentation></xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="HANGUL"/>
                <xs:enumeration value="LATIN"/>
                <xs:enumeration value="HANJA"/>
                <xs:enumeration value="JAPANESE"/>
                <xs:enumeration value="OTHER"/>
                <xs:enumeration value="SYMBOL"/>
                <xs:enumeration value="USER"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="fontCnt" type="xs:nonNegativeInteger" use="required">
        <xs:annotation><xs:documentation>글꼴의 개수</xs:documentation></xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="BorderFillType">
    <xs:annotation>
        <xs:documentation>테두리/배경/채우기</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="slash" type="SlashType" minOccurs="0"/>
        <xs:element name="backSlash" type="SlashType" minOccurs="0"/>
        <xs:element name="leftBorder" type="BorderType" minOccurs="0">
            <xs:annotation><xs:documentation>왼쪽 테두리</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="rightBorder" type="BorderType" minOccurs="0">
             <xs:annotation><xs:documentation>오른쪽 테두리</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="topBorder" type="BorderType" minOccurs="0">
             <xs:annotation><xs:documentation>위쪽 테두리</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="bottomBorder" type="BorderType" minOccurs="0">
            <xs:annotation><xs:documentation>아래쪽 테두리</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="diagonal" type="BorderType" minOccurs="0">
            <xs:annotation><xs:documentation>대각선</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="fillBrush" type="FillBrushType" minOccurs="0">
            <xs:annotation><xs:documentation>채우기 정보</xs:documentation></xs:annotation>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required">
        <xs:annotation><xs:documentation>테두리/채우기 항목 아이디</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="threeD" type="xs:boolean" default="false"/>
    <xs:attribute name="shadow" type="xs:boolean" default="false">
        <xs:annotation><xs:documentation>그림자 효과 on/off</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="centerLine">
        <xs:annotation><xs:documentation>중심선 종류</xs:documentation></xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="NONE"/>
                <xs:enumeration value="VERTICAL"/>
                <xs:enumeration value="HORIZONTAL"/>
                <xs:enumeration value="CROSS"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="breakCellSeparateLine" type="xs:boolean" default="false">
         <xs:annotation><xs:documentation>페이지 경계에 걸친 표의 선 속성 여부</xs:documentation></xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="SlashType">
    <xs:attribute name="type" use="required">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="NONE"><xs:annotation><xs:documentation>사선 없음</xs:documentation></xs:annotation></xs:enumeration>
                <xs:enumeration value="CENTER"><xs:annotation><xs:documentation>중심선 하나</xs:documentation></xs:annotation></xs:enumeration>
                <xs:enumeration value="CENTER_BELOW"><xs:annotation><xs:documentation>중심선 아래의 사선</xs:documentation></xs:annotation></xs:enumeration>
                <xs:enumeration value="CENTER_ABOVE"><xs:annotation><xs:documentation>중심선 위의 사선</xs:documentation></xs:annotation></xs:enumeration>
                <xs:enumeration value="ALL"><xs:annotation><xs:documentation>중심선, 중심선 아래의 사선, 중심선 위의 사선</xs:documentation></xs:annotation></xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="Crooked" type="xs:boolean" use="required"/>
    <xs:attribute name="isCounter" type="xs:boolean" use="required"/>
</xs:complexType>

<xs:complexType name="BorderType">
    <xs:annotation><xs:documentation>테두리 선</xs:documentation></xs:annotation>
    <xs:attribute name="type" type="hc:LineType2" use="required">
        <xs:annotation><xs:documentation>테두리 선 종류</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="width" type="hc:LineWidth" use="required">
        <xs:annotation><xs:documentation>테두리 선 굵기</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="color" type="hc:RGBColorType" use="required">
        <xs:annotation><xs:documentation>테두리 선 색깔</xs:documentation></xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="CharShapeType">
    <xs:annotation><xs:documentation>글자 모양</xs:documentation></xs:annotation>
    <xs:sequence>
        <xs:element name="fontRef">
            <xs:annotation><xs:documentation>언어별 글꼴. 각 글꼴 타입에 맞는 글꼴 ID. (한글이면 한글글꼴 타입)</xs:documentation></xs:annotation>
            <xs:complexType>
                <xs:attribute name="hangul" type="xs:nonNegativeInteger" use="required"/>
                <xs:attribute name="latin" type="xs:nonNegativeInteger" use="required"/>
                <xs:attribute name="hanja" type="xs:nonNegativeInteger" use="required"/>
                <xs:attribute name="japanese" type="xs:nonNegativeInteger" use="required"/>
                <xs:attribute name="other" type="xs:nonNegativeInteger" use="required"/>
                <xs:attribute name="symbol" type="xs:nonNegativeInteger" use="required"/>
                <xs:attribute name="user" type="xs:nonNegativeInteger" use="required"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="ratio">
            <xs:annotation><xs:documentation>언어별 장평. 단위는 %.</xs:documentation></xs:annotation>
            <xs:complexType>
                 <!-- hangul, latin, hanja, japanese, other, symbol, user 속성. 50-200% -->
            </xs:complexType>
        </xs:element>
        <xs:element name="spacing">
            <xs:annotation><xs:documentation>언어별 자간. 단위는 %.</xs:documentation></xs:annotation>
            <xs:complexType>
                <!-- hangul, latin, hanja, japanese, other, symbol, user 속성. -50-50% -->
            </xs:complexType>
        </xs:element>
        <xs:element name="relSz">
            <xs:annotation><xs:documentation>언어별 글자의 상대 크기. 단위는 %.</xs:documentation></xs:annotation>
            <xs:complexType>
                <!-- hangul, latin, hanja, japanese, other, symbol, user 속성. 10-250% -->
            </xs:complexType>
        </xs:element>
        <xs:element name="offset">
            <xs:annotation><xs:documentation>언어별 오프셋. 단위는 %.</xs:documentation></xs:annotation>
            <xs:complexType>
                <!-- hangul, latin, hanja, japanese, other, symbol, user 속성. -100-100% -->
            </xs:complexType>
        </xs:element>
        <xs:element name="underline" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 밑줄</xs:documentation></xs:annotation>
             <!-- ... underline 세부 정의 ... -->
        </xs:element>
        <xs:element name="strikeout" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 취소선</xs:documentation></xs:annotation>
             <!-- ... strikeout 세부 정의 ... -->
        </xs:element>
        <xs:element name="outline" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 외곽선</xs:documentation></xs:annotation>
             <!-- ... outline 세부 정의 ... -->
        </xs:element>
        <xs:element name="shadow" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 그림자</xs:documentation></xs:annotation>
             <!-- ... shadow 세부 정의 ... -->
        </xs:element>
        <xs:element name="emboss" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 양각</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="engrave" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 음각</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="superscript" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 위 첨자</xs:documentation></xs:annotation>
        </xs:element>
        <xs:element name="subscript" minOccurs="0">
             <xs:annotation><xs:documentation>글자 속성: 아래 첨자</xs:documentation></xs:annotation>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required">
        <xs:annotation><xs:documentation>글자 모양 아이디</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="height" type="xs:integer" default="1000">
        <xs:annotation><xs:documentation>글자 크기 (hwpunit 단위. 10pt = 1000 hwpunit)</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="textColor" type="hc:RGBColorType" default="#000000">
         <xs:annotation><xs:documentation>글자색</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="shadeColor" type="hc:RGBColorType" default="#FFFFFF">
        <xs:annotation><xs:documentation>음영색</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="useFontSpace" type="xs:boolean" default="false">
        <xs:annotation><xs:documentation>글꼴에 어울리는 공백 사용 여부</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="useKerning" type="xs:boolean" default="false">
        <xs:annotation><xs:documentation>커닝 사용 여부</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="symMark" default="NONE">
        <xs:annotation><xs:documentation>강조점</xs:documentation></xs:annotation>
        <!-- ... symMark 세부 enum 정의 ... -->
    </xs:attribute>
    <xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
        <xs:annotation><xs:documentation>테두리/배경 ID</xs:documentation></xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="TabDefType">
    <xs:sequence>
        <xs:element name="tabItem" minOccurs="1" maxOccurs="unbounded">
            <xs:complexType>
                <xs:attribute name="pos" type="xs:integer" use="required">
                    <xs:annotation><xs:documentation>탭의 위치. 단위는 hwpunit</xs:documentation></xs:annotation>
                </xs:attribute>
                <xs:attribute name="type" use="required">
                    <xs:annotation><xs:documentation>탭의 종류</xs:documentation></xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="LEFT"><xs:annotation><xs:documentation>왼쪽</xs:documentation></xs:annotation></xs:enumeration>
                            <xs:enumeration value="RIGHT"><xs:annotation><xs:documentation>오른쪽</xs:documentation></xs:annotation></xs:enumeration>
                            <xs:enumeration value="CENTER"><xs:annotation><xs:documentation>가운데</xs:documentation></xs:annotation></xs:enumeration>
                            <xs:enumeration value="DECIMAL"><xs:annotation><xs:documentation>소수점</xs:documentation></xs:annotation></xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="leader" type="hc:LineType2" use="required">
                    <xs:annotation><xs:documentation>채울 모양 종류</xs:documentation></xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="autoTabLeft" type="xs:boolean" default="false">
        <xs:annotation><xs:documentation>문단 왼쪽 자동 탭 (내어쓰기용 자동 탭)</xs:documentation></xs:annotation>
    </xs:attribute>
    <xs:attribute name="autoTabRight" type="xs:boolean" default="false">
        <xs:annotation><xs:documentation>문단 오른쪽 자동 탭</xs:documentation></xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="NumberingType">
    <xs:annotation><xs:documentation>문단 번호 모양 정보</xs:documentation></xs:annotation>
    <xs:sequence>
        <xs:element name="paraHead" type="ParaHeadType" maxOccurs="unbounded"/>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="start" type="xs:integer" default="1">
        <xs:annotation><xs:documentation>시작 번호</xs:documentation></xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="BulletType">
    <xs:annotation><xs:documentation>글머리표 문단 모양 정보</xs:documentation></xs:annotation>
    <!-- ... BulletType 세부 정의 ... -->
</xs:complexType>

</xs:schema>
<xs:complexType name="BulletType">
    <xs:annotation>
        <xs:documentation>글머리표 문단 모양 정보</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="img" type="hc:ImageType" minOccurs="0"/>
        <xs:element name="paraHead" type="ParaHeadType"/>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="char" type="xs:string" use="required">
        <xs:annotation>
            <xs:documentation>글머리표 문자</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="checkedChar" type="xs:string">
        <xs:annotation>
            <xs:documentation>체크되었을 때의 글머리표 문자</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="useImage" type="xs:boolean" use="required">
        <xs:annotation>
            <xs:documentation>이미지 사용 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="ParaHeadType" mixed="true">
    <xs:annotation>
        <xs:documentation>
            번호/문단머리 정보.
            문자열 내 특정 문자에 제어코드(^, #)를 사용함으로써 해당 수준에서 표시되는 번호 또는 문단 머리의 포맷을 제어한다.
            ^n: n수준 정보를 표시한다. (예: 1.1.1.1.1.1.1)
            ^N: n수준 정보를 표시하며 마지막에 마침표를 하나 더 찍는다. (예: 1.1.1.1.1.1.1.)
            번호(1-7): 해당 수준에 해당하는 숫자 또는 문자 또는 기호를 표시한다.
        </xs:documentation>
    </xs:annotation>
    <xs:attribute name="start" type="xs:unsignedInt" default="1">
        <xs:annotation>
            <xs:documentation>시작 번호</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="level" use="required">
        <xs:annotation>
            <xs:documentation>수준</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:positiveInteger"/>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="align" default="LEFT">
        <xs:annotation>
            <xs:documentation>번호 정렬 방식</xs:documentation>
        </xs:annotation>
        <!-- align 속성의 simpleType 정의 누락되었으나 문맥상 Left, Right, Center 등 포함될 것으로 추정 -->
    </xs:attribute>
    <xs:attribute name="autoIndent" type="xs:boolean" default="true">
        <xs:annotation>
            <xs:documentation>자동 내어쓰기 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="widthAdjust" type="xs:integer" default="0">
        <xs:annotation>
            <xs:documentation>너비 보정 값. 단위는 hwpunit</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="textOffsetType" default="PERCENT">
        <xs:annotation>
            <xs:documentation>본문과의 거리 범위 유형</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="PERCENT"/>
                <xs:enumeration value="HWPUNIT"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="textOffset" type="xs:integer" default="50">
        <xs:annotation>
            <xs:documentation>본문과의 거리</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="numFormat" type="hc:NumberType" default="DIGIT">
        <xs:annotation>
            <xs:documentation>번호 포맷 (글머리표 문단의 경우에는 사용되지 않음)</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>글자 모양 아이디 참조</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="checkChar" type="xs:string">
        <xs:annotation>
            <xs:documentation>체크 글머리 문자</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="ParaShapeType">
    <xs:annotation>
        <xs:documentation>문단 모양 정보</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="align">
            <xs:annotation>
                <xs:documentation>문단 정렬</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="horizontal" use="required">
                    <xs:annotation>
                        <xs:documentation>수평 정렬</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="JUSTIFY">
                                <xs:annotation><xs:documentation>양쪽 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="LEFT">
                                <xs:annotation><xs:documentation>왼쪽 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="RIGHT">
                                <xs:annotation><xs:documentation>오른쪽 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER">
                                <xs:annotation><xs:documentation>가운데 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="DISTRIBUTE">
                                <xs:annotation><xs:documentation>배분 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="DISTRIBUTE_SPACE">
                                <xs:annotation><xs:documentation>나눔 정렬 (공백에만 배분)</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="vertical" use="required">
                    <xs:annotation>
                        <xs:documentation>수직 정렬</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="BASELINE">
                                <xs:annotation><xs:documentation>글자 기준선</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="TOP">
                                <xs:annotation><xs:documentation>위</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER">
                                <xs:annotation><xs:documentation>가운데</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BOTTOM">
                                <xs:annotation><xs:documentation>아래</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="heading">
            <xs:annotation>
                <xs:documentation>문단 머리 번호/글머리표</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="type" use="required">
                    <xs:annotation>
                        <xs:documentation>문단 머리 모양 종류</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="NONE">
                                <xs:annotation><xs:documentation>없음</xs:documentation></xs:annotation>
                            </xs:enumeration>
                             <xs:enumeration value="OUTLINE">
                                <xs:annotation><xs:documentation>개요</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="NUMBER">
                                <xs:annotation><xs:documentation>번호</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BULLET">
                                <xs:annotation><xs:documentation>글머리표</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="idRef" type="xs:nonNegativeInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>번호/글머리표 문단 모양 아이디 참조</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="level" use="required">
                    <xs:annotation>
                        <xs:documentation>수준</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:nonNegativeInteger"/>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="breakSetting">
            <xs:annotation>
                <xs:documentation>줄 나눔 설정</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="breakLatinWord" use="required">
                    <xs:annotation>
                        <xs:documentation>라틴 문자의 줄나눔 단위</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="KEEP_WORD">
                                <xs:annotation><xs:documentation>단어</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="HYPHENATION">
                                <xs:annotation><xs:documentation>하이픈</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BREAK_WORD">
                                <xs:annotation><xs:documentation>글자</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="breakNonLatinWord" use="required">
                    <xs:annotation>
                        <xs:documentation>라틴 문자 이외의 문자의 줄나눔 단위</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                             <xs:enumeration value="KEEP_WORD">
                                <xs:annotation><xs:documentation>단어</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BREAK_WORD">
                                <xs:annotation><xs:documentation>글자</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="widowOrphan" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>고아/미망줄 보호 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="keepWithNext" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>다음 문단과 함께</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="keepLines" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>문단 보호 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="pageBreakBefore" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>문단 앞에서 항상 쪽나눔 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="lineWrap" use="required">
                    <xs:annotation>
                        <xs:documentation>줄바꿈 영역 사용 시의 형식</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                             <xs:enumeration value="BREAK">
                                <xs:annotation><xs:documentation>줄바꿈</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="SQUEEZE">
                                <xs:annotation><xs:documentation>자간을 조정하여 한 줄 유지</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="KEEP">
                                <xs:annotation><xs:documentation>내용에 따라 폭이 늘어남</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="margin">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="intent" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>들여쓰기/내어쓰기. 0보다 크면 들여쓰기, 0이면 보통, 0보다 작으면 내어쓰기.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="left" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>왼쪽 여백. 단위를 표기하지 않으면 hwpunit이고 표기하면 표기한 단위.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="right" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>오른쪽 여백</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="prev" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>문단 간격 위</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="next" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>문단 간격 아래</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
        <xs:element name="lineSpacing">
            <xs:annotation>
                <xs:documentation>줄 간격</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="type" use="required">
                    <xs:annotation>
                        <xs:documentation>줄간격 종류</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="PERCENT">
                                <xs:annotation><xs:documentation>글자에 따라</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="FIXED">
                                <xs:annotation><xs:documentation>고정값</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BETWEEN_LINES">
                                <xs:annotation><xs:documentation>여백만 지정</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="AT_LEAST">
                                <xs:annotation><xs:documentation>최소</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="value" type="xs:integer" use="required">
                    <xs:annotation>
                        <xs:documentation>줄 간격 값. type이 PERCENT이면 0%-500%로 제한</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="unit">
                    <xs:annotation>
                        <xs:documentation>줄 간격 값의 단위</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="CHAR"/>
                            <xs:enumeration value="HWPUNIT"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="border">
            <xs:annotation>
                <xs:documentation>문단 테두리</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
                    <xs:annotation>
                        <xs:documentation>테두리/배경 모양 아이디</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetLeft" type="xs:integer" default="0">
                    <xs:annotation>
                        <xs:documentation>문단 테두리 왼쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetRight" type="xs:integer" default="0">
                     <xs:annotation>
                        <xs:documentation>문단 테두리 오른쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetTop" type="xs:integer" default="0">
                     <xs:annotation>
                        <xs:documentation>문단 테두리 위쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetBottom" type="xs:integer" default="0">
                     <xs:annotation>
                        <xs:documentation>문단 테두리 아래쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="connect" type="xs:boolean" default="false">
                    <xs:annotation>
                        <xs:documentation>문단 테두리 연결 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="ignoreMargin" type="xs:boolean" default="false">
                    <xs:annotation>
                        <xs:documentation>문단 테두리 여백 무시 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="autoSpacing">
            <xs:annotation>
                <xs:documentation>문단 자동 간격 조정 설정</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="eAsianEng" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>아시아/영어 간격을 자동 조절</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="eAsianNum" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>아시아/숫자 간격을 자동 조절</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="tabPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>탭 정의 아이디 참조</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="condense">
        <xs:annotation>
            <xs:documentation>줄 나눔 최소값. 단위는 %</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:minInclusive value="0"/>
                <xs:maxInclusive value="75"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="fontLineHeight" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>글꼴에 어울리는 줄 높이 사용 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="snapToGrid" type="xs:boolean" default="true">
        <xs:annotation>
            <xs:documentation>편집 용지의 줄 격자 사용 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="suppressLineNumbers" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>줄 번호 건너뛰기</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="checked" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>체크 글머리표 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="StyleType">
    <xs:annotation>
        <xs:documentation>스타일 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="type" use="required">
        <xs:annotation>
            <xs:documentation>스타일 타입</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="PARA">
                    <xs:annotation><xs:documentation>문단 스타일</xs:documentation></xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="CHAR">
                    <xs:annotation><xs:documentation>글자 스타일</xs:documentation></xs:annotation>
                </xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="name" type="xs:string" use="required">
        <xs:annotation>
            <xs:documentation>한글 스타일 이름. 한글 윈도우에서는 한글 스타일 이름.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="engName" type="xs:string">
        <xs:annotation>
            <xs:documentation>영문 스타일 이름</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="paraPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>문단 모양 아이디 참조. 스타일의 종류가 문단인 경우 지정해야 함.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>글자 모양 아이디 참조. 스타일의 종류가 글자인 경우 지정해야 함.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="nextStyleIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>다음 스타일 아이디 참조. 문단 스타일에서 사용자가 리턴키를 입력하여 다음 문단으로 이동하였을 때 적용될 문단 스타일을 지정한다.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="langID" type="xs:unsignedShort">
        <xs:annotation>
            <xs:documentation>언어 아이디</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lockForm" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>양식 모드에서 Style 보호하기 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="MemoShapeType">
    <xs:annotation>
        <xs:documentation>메모 모양 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="width" type="xs:nonNegativeInteger" use="required">
        <xs:annotation>
            <xs:documentation>메모가 보이는 너비</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lineWidth" type="xs:string">
        <xs:annotation>
            <xs:documentation>메모의 라인 굵기</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lineType" type="hc:LineType2" use="required">
        <xs:annotation>
            <xs:documentation>메모의 선 종류</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lineColor" type="hc:RGBColorType" use="required">
        <xs:annotation>
            <xs:documentation>메모의 선 색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="fillColor" type="hc:RGBColorType" use="required">
        <xs:annotation>
            <xs:documentation>메모 배경색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="activeColor" type="hc:RGBColorType" use="required">
        <xs:annotation>
            <xs:documentation>메모가 활성화되었을 때 색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="memoType">
        <xs:annotation>
            <xs:documentation>메모 변경 추적을 위한 속성</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="NORMAL"/>
                <xs:enumeration value="USER_INSERT"/>
                <xs:enumeration value="USER_DELETE"/>
                <xs:enumeration value="USER_UPDATE"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="CompatibleDocumentType">
    <xs:annotation>
        <xs:documentation>호환 문서 정보</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="layoutCompatibility">
             <xs:complexType>
                <xs:sequence>
                    <!-- Various boolean flags for compatibility options -->
                    <xs:element name="applyExtensionCharCompose" minOccurs="0"/>
                    <xs:element name="doNotAlignParagraphSpacingAtGrid" minOccurs="0"/>
                    <xs:element name="doNotAdjustWordSpacingInJustify" minOccurs="0"/>
                    <xs:element name="doNotApplyAsiaFontToParagraphLeading" minOccurs="0"/>
                    <xs:element name="doNotAdjustLineSpacingAtFont" minOccurs="0"/>
                    <xs:element name="doNotAdjustBaselineAtFont" minOccurs="0"/>
                    <xs:element name="doNotApplyParagraphLeading" minOccurs="0"/>
                    <xs:element name="doNotAdjustFragmentOfWord" minOccurs="0"/>
                    <xs:element name="adjustBaselineOfAsiaFont" minOccurs="0"/>
                    <xs:element name="doNotAdjustLastLineInJustify" minOccurs="0"/>
                    <xs:element name="doNotAdjustLineSpacingAtGrid" minOccurs="0"/>
                    <xs:element name="doNotAdjustBetweenLines" minOccurs="0"/>
                    <xs:element name="doNotAdjustFirstLineLeadingAtPage" minOccurs="0"/>
                    <xs:element name="doNotAdjustBetweenLinesAtPage" minOccurs="0"/>
                    <xs:element name="doNotBalanceHalfCharAndFullChar" minOccurs="0"/>
                    <xs:element name="doNotApplyUnderlineForSpace" minOccurs="0"/>
                    <xs:element name="doNotApplyBoldToSpace" minOccurs="0"/>
                    <xs:element name="doNotAdjustBlankAtWord" minOccurs="0"/>
                    <xs:element name="doNotAdjustWidthAtUnderline" minOccurs="0"/>
                    <xs:element name="doNotAdjustWidthAtStrike" minOccurs="0"/>
                    <xs:element name="doNotAdjustWidthAtOutline" minOccurs="0"/>
                    <xs:element name="doNotApplyCharSpacingAtLastChar" minOccurs="0"/>
                    <xs:element name="doNotSpreadAtTab" minOccurs="0"/>
                    <xs:element name="doNotAdjustBaselineAtTop" minOccurs="0"/>
                    <xs:element name="doNotAdjustSpacingAtNumber" minOccurs="0"/>
                    <xs:element name="doNotApplySmartTag" minOccurs="0"/>
                    <xs:element name="doNotApplyShapeComment" minOccurs="0"/>
<a name="hp-doNotApplyHyperlink"></a>
                    <xs:element name="doNotApplyHyperlink" minOccurs="0"/>
                    <xs:element name="overlapBothAllowOverlap" minOccurs="0"/>
                    <xs:element name="doNotApplyVertOffsetOfForward" minOccurs="0"/>
                    <xs:element name="extendVertLimitToPageMargins" minOccurs="0"/>
                    <xs:element name="doNotHoldAnchorOfTable" minOccurs="0"/>
                    <xs:element name="doNotFormattingAtBeneathAnchor" minOccurs="0"/>
                    <xs:element name="adjustBaselineOfObjectToBottom" minOccurs="0"/>
                    <xs:element name="doNotApplyExtensionCharCompose" minOccurs="0"/>
                </xs:sequence>
             </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="targetProgram" use="required">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="HWP201X"/>
                <xs:enumeration value="HWP200X"/>
                <xs:enumeration value="MS_WORD"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="TrackChange">
    <xs:annotation>
        <xs:documentation>변경 추적 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="type" type="hc:TrackChangeType"/>
    <xs:attribute name="date" type="xs:dateTime"/>
    <xs:attribute name="authorID" type="xs:nonNegativeInteger"/>
    <xs:attribute name="charShapeID" type="xs:nonNegativeInteger"/>
    <xs:attribute name="paraShapeID" type="xs:nonNegativeInteger"/>
    <xs:attribute name="hide" type="xs:boolean" use="required"/>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
</xs:complexType>

<xs:complexType name="TrackChangeAuthor">
    <xs:annotation>
        <xs:documentation>변경 추적 사용자 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="name" type="xs:string"/>
    <xs:attribute name="mark" type="xs:boolean"/>
    <xs:attribute name="color" type="hc:RGBColorType"/>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
</xs:complexType>

```xml
<!-- 여기서부터는 Body.xml의 스키마 정의로 추정됨 -->
<!-- 파일 시작: Body.xml.xsd -->
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
```
           xmlns:hp="http://www.owpml.org/owpml/2024/paragraph"
           xmlns:hc="http://www.owpml.org/owpml/2024/core"
           targetNamespace="http://www.owpml.org/owpml/2024/paragraph"
           elementFormDefault="qualified">

```xml
    <xs:import namespace="http://www.owpml.org/owpml/2024/core" schemaLocation="HWPMLCore.xsd"/>
    <xs:import namespace="http://www.w3.org/XML/1998/namespace" schemaLocation="http://www.w3.org/2001/xml.xsd"/>
```
    
    <xs:complexType name="SectionType">
        <xs:sequence>
            <xs:element name="p" type="hp:PType" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    
    <xs:complexType name="ParaListType">
        <xs:sequence>
            <xs:element name="p" type="hp:PType" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="textDirection" default="HORIZONTAL">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="HORIZONTAL"/>
                    <xs:enumeration value="VERTICAL"/>
                    <xs:enumeration value="VERTICALALL">
                        <xs:annotation><xs:documentation>영문 눕힘</xs:documentation></xs:annotation>
                    </xs:enumeration>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="lineWrap" default="BREAK">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="BREAK"/>
                    <xs:enumeration value="SQUEEZE"/>
                    <xs:enumeration value="KEEP"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="vertAlign" default="TOP"/>
    </xs:complexType>
    
    <xs:element name="sec" type="hp:SectionDefinitionType">
        <xs:annotation>
            <xs:documentation>HWPML 문서의 구역</xs:documentation>
        </xs:annotation>
    </xs:element>

    <xs:complexType name="PType">
        <xs:choice minOccurs="0" maxOccurs="unbounded">
            <xs:element name="run">
                <xs:complexType>
                    <xs:choice minOccurs="0" maxOccurs="unbounded">
                        <xs:element name="ctrl">
                            <xs:complexType>
                                <xs:choice minOccurs="1" maxOccurs="unbounded">
                                    <xs:element name="colPr" type="hp:ColumnDefType" minOccurs="0"/>
                                    <xs:element name="fieldBegin">
                                        <xs:complexType>
                                            <xs:sequence minOccurs="0">
                                                <xs:element name="parameters" type="hp:ParameterList" minOccurs="0"/>
                                                <xs:element name="subList" type="hp:ParaListType" minOccurs="0"/>
                                                <xs:element name="metaTag" type="hc:MetaTagType" minOccurs="0"/>
                                            </xs:sequence>
                                            <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
                                            <xs:attribute name="type" type="hp:FieldType" use="required"/>
                                            <xs:attribute name="name" type="xs:string"/>
                                            <xs:attribute name="editable" type="xs:boolean" default="true"/>
                                            <xs:attribute name="dirty" type="xs:boolean" default="false"/>
                                            <xs:attribute name="zorder" type="xs:integer"/>
                                            <xs:attribute name="fieldid" type="xs:nonNegativeInteger"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="fieldEnd">
                                        <xs:complexType>
                                            <xs:attribute name="beginIDRef" type="xs:nonNegativeInteger" use="required"/>
                                            <xs:attribute name="fieldid" type="xs:unsignedInt"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="bookmark">
                                        <xs:complexType>
                                            <xs:attribute name="name" type="xs:string"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="header" type="hp:HeaderFooterType"/>
                                    <xs:element name="footer" type="hp:HeaderFooterType"/>
                                    <xs:element name="footNote" type="hp:NoteType"/>
                                    <xs:element name="endNote" type="hp:NoteType"/>
                                    <xs:element name="autoNum" type="hp:AutoNumNewNumType"/>
                                    <xs:element name="newNum" type="hp:AutoNumNewNumType"/>
                                    <xs:element name="pageNumCtrl">
                                        <xs:complexType>
                                            <xs:attribute name="pageStartsOn" default="BOTH">
                                                <xs:simpleType>
                                                    <xs:restriction base="xs:string">
                                                        <xs:enumeration value="BOTH"/>
                                                        <xs:enumeration value="EVEN"/>
                                                        <xs:enumeration value="ODD"/>
                                                    </xs:restriction>
                                                </xs:simpleType>
                                            </xs:attribute>
                                            <!-- ... 기타 pageNumCtrl 속성들 ... -->
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="pageHiding">
                                        <xs:complexType>
                                            <xs:attribute name="hideHeader" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideFooter" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideMasterPage" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideBorder" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideFill" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hidePageNum" type="xs:boolean" default="false"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="pageNum">
                                        <xs:complexType>
                                            <xs:attribute name="pos" default="TOP_LEFT">
                                                <xs:annotation><xs:documentation>쪽 번호 위치</xs:documentation></xs:annotation>
                                                <xs:simpleType>
                                                    <xs:restriction base="xs:string">
                                                        <xs:enumeration value="NONE"/>
                                                        <xs:enumeration value="TOP_LEFT"/>
                                                        <xs:enumeration value="TOP_CENTER"/>
                                                        <xs:enumeration value="TOP_RIGHT"/>
                                                        <xs:enumeration value="BOTTOM_LEFT"/>
                                                        <xs:enumeration value="BOTTOM_CENTER"/>
                                                        <xs:enumeration value="BOTTOM_RIGHT"/>
                                                        <xs:enumeration value="OUTSIDE_TOP"/>
                                                        <xs:enumeration value="OUTSIDE_BOTTOM"/>
                                                        <xs:enumeration value="INSIDE_TOP"/>
                                                        <xs:enumeration value="INSIDE_BOTTOM"/>
                                                    </xs:restriction>
                                                </xs:simpleType>
                                            </xs:attribute>
                                            <xs:attribute name="formatType" type="hc:NumberType" default="DIGIT">
                                                <xs:annotation><xs:documentation>쪽 번호 형식</xs:documentation></xs:annotation>
                                            </xs:attribute>
                                            <xs:attribute name="sideChar" type="xs:string" default="-">
                                                 <xs:annotation><xs:documentation>앞뒤 장식 문자 넣기</xs:documentation></xs:annotation>
                                            </xs:attribute>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="indexmark">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="firstKey"/>
                                                <xs:element name="secondKey"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="hiddenComment">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="subList" type="hp:ParaListType"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:choice>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="t">
                            <!-- ... t(text) element definition ... -->
                        </xs:element>
                        <xs:element name="markpenBegin">
                            <xs:complexType>
                                <xs:attribute name="color" type="hc:RGBColorType"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="markpenEnd" minOccurs="0"/>
                        <xs:element name="titleMark">
                             <xs:complexType>
                                <xs:attribute name="ignore" type="xs:boolean" default="false"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="tab" minOccurs="0">
                             <xs:annotation><xs:documentation>Attribute 'width' 단위는 hwpunit</xs:documentation></xs:annotation>
                             <xs:complexType>
                                <xs:attribute name="width" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="leader" type="hc:LineType2"/>
                                <xs:attribute name="type">
                                    <xs:annotation><xs:documentation>탭의 종류</xs:documentation></xs:annotation>
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="LEFT"><xs:annotation><xs:documentation>왼쪽</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="RIGHT"><xs:annotation><xs:documentation>오른쪽</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="CENTER"><xs:annotation><xs:documentation>가운데</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="DECIMAL"><xs:annotation><xs:documentation>소수점</xs:documentation></xs:annotation></xs:enumeration>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="lineBreak" minOccurs="0"/>
                        <xs:element name="hyphen" minOccurs="0"/>
                        <xs:element name="nbspace" minOccurs="0"/>
                        <xs:element name="fwspace" minOccurs="0"/>
                        <xs:element name="insertBegin" type="hp:TrackChangeTag"/>
                        <xs:element name="insertEnd" type="hp:TrackChangeTag"/>
                        <xs:element name="deleteBegin" type="hp:TrackChangeTag"/>
                        <xs:element name="deleteEnd" type="hp:TrackChangeTag"/>
                        <xs:element name="tbl">
                            <xs:complexType>
                                <xs:attribute name="charStyleIDRef" type="xs:nonNegativeInteger"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="drawing" type="hp:ShapeType"/>
                        <xs:element name="pic" type="hp:PictureType"/>
                        <xs:element name="ole" type="hp:OLEType"/>
                        <xs:element name="container" type="hp:ContainerType"/>
                        <xs:element name="equation" type="hp:EquationType"/>
                        <xs:element name="line" type="hp:LineType"/>
                        <xs:element name="rect" type="hp:RectangleType"/>
                        <xs:element name="ellipse" type="hp:EllipseType"/>
                        <xs:element name="arc" type="hp:ArcType"/>
                        <xs:element name="polygon" type="hp:PolygonType"/>
                        <xs:element name="curve" type="hp:CurveType"/>
                        <xs:element name="connectLine" type="hp:ConnectLineType"/>
                        <xs:element name="textart">
                            <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractDrawingObjectType">
                                        <xs:sequence>
                                            <xs:element name="pt0" type="hc:PointType"/>
                                            <xs:element name="pt1" type="hc:PointType"/>
                                            <xs:element name="pt2" type="hc:PointType"/>
                                            <xs:element name="pt3" type="hc:PointType"/>
                                            <xs:element name="textartPr">
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="shadow" type="hp:ShadowType"/>
                                                    </xs:sequence>
                                                    <xs:attribute name="fontName" type="xs:string"/>
                                                    <xs:attribute name="fontStyle" type="xs:string"/>
                                                    <xs:attribute name="fontType" default="TTF">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="TTF"/>
                                                                <xs:enumeration value="HFT"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="textShape" default="REGULAR">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <!-- REGULAR, PARALLELOGRAM 등 수십 개의 값들 -->
                                                                <xs:enumeration value="REGULAR"/><xs:enumeration value="PARALLELOGRAM"/>
                                                                <xs:enumeration value="INVERTED_PARALLELOGRAM"/><xs:enumeration value="UPWARD_CASCADE"/>
                                                                <xs:enumeration value="DOWNWARD_CASCADE"/><xs:enumeration value="INVERTED_UPWARD_CASCADE"/>
                                                                <xs:enumeration value="INVERTED_DOWNWARD_CASCADE"/><xs:enumeration value="REDUCE_RIGHT"/>
                                                                <xs:enumeration value="REDUCE_LEFT"/><xs:enumeration value="ISOSCELES_TRAPEZOID"/>
                                                                <xs:enumeration value="INVERTED_ISOSCELES_TRAPEZOID"/><xs:enumeration value="TOP_RIBBON_RECTANGLE"/>
                                                                <xs:enumeration value="BOTTOM_RIBBON_RECTANGLE"/><xs:enumeration value="CHEVRON"/>
                                                                <xs:enumeration value="BOW_TIE"/><xs:enumeration value="HEXAGON"/>
                                                                <xs:enumeration value="WAVE1"/><xs:enumeration value="WAVE2"/><xs:enumeration value="WAVE3"/><xs:enumeration value="WAVE4"/>
                                                                <xs:enumeration value="LEFT_TILT_CYLINDER"/><xs:enumeration value="RIGHT_TILT_CYLINDER"/>
                                                                <xs:enumeration value="BOTTOM_WIDE_CYLINDER"/><xs:enumeration value="TOP_WIDE_CYLINDER"/>
                                                                <!-- ... 그 외 다수 값 생략하지 않고 모두 기입 -->
                                                                <xs:enumeration value="THIN_CURVE_UP1"/><xs:enumeration value="THIN_CURVE_UP2"/>
                                                                <xs:enumeration value="THIN_CURVE_DOWN1"/><xs:enumeration value="THIN_CURVE_DOWN2"/>
                                                                <xs:enumeration value="INVERSED_FINGERNAIL"/><xs:enumeration value="FINGERNAIL"/>
                                                                <xs:enumeration value="GINKO_LEAF1"/><xs:enumeration value="GINKO_LEAF2"/>
                                                                <xs:enumeration value="INFLATE_RIGHT"/><xs:enumeration value="INFLATE_LEFT"/>
                                                                <xs:enumeration value="INFLATE_TOP_CONVEX"/><xs:enumeration value="INFLATE_BOTTOM_CONCAVE"/>
                                                                <xs:enumeration value="DEFLATE_TOP1"/><xs:enumeration value="DEFLATE_BOTTOM"/>
                                                                <xs:enumeration value="DEFLATE"/><xs:enumeration value="INFLATE"/>
                                                                <xs:enumeration value="INFLATE_TOP"/><xs:enumeration value="INFLATE_BOTTOM"/>
                                                                <xs:enumeration value="RECTANGLE"/><xs:enumeration value="LEFT_CYLINDER"/>
                                                                <xs:enumeration value="CYLINDER"/><xs:enumeration value="RIGHT_CYLINDER"/>
                                                                <xs:enumeration value="CIRCLE"/><xs:enumeration value="CURVE_DOWN"/>
                                                                <xs:enumeration value="ARCH_UP"/><xs:enumeration value="ARCH_DOWN"/>
                                                                <xs:enumeration value="SINGLE_LINE_CIRCLE1"/><xs:enumeration value="SINGLE_LINE_CIRCLE2"/>
                                                                <xs:enumeration value="TRIPLE_LINE_CIRCLE1"/><xs:enumeration value="TRIPLE_LINE_CIRCLE2"/>
                                                                <xs:enumeration value="DOUBLE_LINE_CIRCLE"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="lineSpacing" default="120">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:nonNegativeInteger">
                                                                <xs:minInclusive value="50"/>
                                                                <xs:maxInclusive value="500"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="charSpacing" default="100">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:nonNegativeInteger">
                                                                <xs:minInclusive value="-50"/>
                                                                <xs:maxInclusive value="500"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="align" default="LEFT">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="LEFT"/>
                                                                <xs:enumeration value="RIGHT"/>
                                                                <xs:enumeration value="CENTER"/>
                                                                <xs:enumeration value="FULL"/>
                                                                <xs:enumeration value="TABLE"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                </xs:complexType>
                                            </xs:element>
                                            <xs:element name="outline">
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="pt" type="hc:PointType" minOccurs="0" maxOccurs="unbounded"/>
                                                    </xs:sequence>
                                                    <xs:attribute name="cnt" type="xs:nonNegativeInteger"/>
                                                </xs:complexType>
                                            </xs:element>
                                        </xs:sequence>
                                        <xs:attribute name="text" type="xs:string"/>
                                    </xs:extension>
                                </xs:complexContent>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="compose">
                            <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="charPr" maxOccurs="unbounded">
                                        <xs:complexType>
                                            <xs:attribute name="prIDRef" type="xs:nonNegativeInteger"/>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:sequence>
                                <xs:attribute name="circleType" default="SHAPE_CIRCLE">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="CHAR"/>
                                            <xs:enumeration value="SHAPE_CIRCLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_CIRCLE"/>
                                            <xs:enumeration value="SHAPE_RECTANGLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_RECTANGLE"/>
                                            <xs:enumeration value="SHAPE_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_LIGHT"/>
                                            <xs:enumeration value="SHAPE_RHOMBUS"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_RHOMBUS"/>
                                            <xs:enumeration value="SHAPE_EMPTY_CIRCULATE_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_THICK_CIRCULATE_TRIANGLE"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="charSz" type="xs:integer">
                                     <xs:annotation><xs:documentation>글자 크기 비율 (%)</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="composeType">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="SPREAD"/>
                                            <xs:enumeration value="OVERLAP"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="charprCnt" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="composeText" type="xs:string"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="dutmal">
                             <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="mainText"/>
                                    <xs:element name="subText"/>
                                </xs:sequence>
                                <xs:attribute name="pos" default="TOP">
                                     <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="TOP"/>
                                            <xs:enumeration value="BOTTOM"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="szRatio" type="xs:positiveInteger"/>
                                <xs:attribute name="option" type="xs:unsignedInt" default="47"/>
                                <xs:attribute name="styleIDRef" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="align" default="CENTER">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="JUSTIFY"/>
                                            <xs:enumeration value="LEFT"/>
                                            <xs:enumeration value="RIGHT"/>
                                            <xs:enumeration value="CENTER"/>
                                            <xs:enumeration value="DISTRIBUTE"/>
                                            <xs:enumeration value="DISTRIBUTE_SPACE"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                             </xs:complexType>
                        </xs:element>
                        <xs:element name="btn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="radioBtn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="checkBtn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="comboBox" type="hp:ComboBoxType"/>
                        <xs:element name="listBox" type="hp:ListBoxType"/>
                        <xs:element name="edit" type="hp:EditType"/>
                        <xs:element name="scrollBar" type="hp:ScrollBarType"/>
                        <xs:element name="video">
                             <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractShapeComponentType">
                                        <xs:attribute name="videoType" use="required">
                                             <xs:annotation><xs:documentation>비디오 종류 (로컬/웹)</xs:documentation></xs:annotation>
                                             <xs:simpleType>
                                                <xs:restriction base="xs:string">
                                                    <xs:enumeration value="LOCAL">
                                                        <xs:annotation><xs:documentation>로컬 컴퓨터의 동영상</xs:documentation></xs:annotation>
                                                    </xs:enumeration>
                                                    <xs:enumeration value="WEB">
                                                        <xs:annotation><xs:documentation>웹 링크 동영상</xs:documentation></xs:annotation>
                                                    </xs:enumeration>
                                                </xs:restriction>
                                            </xs:simpleType>
                                        </xs:attribute>
                                        <xs:attribute name="fileIDRef" type="xs:string" use="optional"/>
                                        <xs:attribute name="imageIDRef" type="xs:string" use="optional"/>
                                        <xs:attribute name="tag" type="xs:string" use="optional"/>
                                    </xs:extension>
                                </xs:complexContent>
                             </xs:complexType>
                        </xs:element>
                        <xs:element name="chart">
                             <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractShapeObjectType">
                                        <xs:attribute name="version" type="xs:float"/>
                                        <xs:attribute name="chartIDRef" type="xs:string"/>
                                    </xs:extension>
                                </xs:complexContent>
                             </xs:complexType>
                        </xs:element>
                    </xs:choice>
                    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger"/>
                    <xs:attribute name="charTcid" type="xs:nonNegativeInteger" use="optional"/>
                </xs:complexType>
            </xs:element>
        </xs:choice>
        <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="paraPrIDRef" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="styleIDRef" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="pageBreak" type="xs:boolean" default="false"/>
        <xs:attribute name="columnBreak" type="xs:boolean" default="false"/>
        <xs:attribute name="merged" type="xs:boolean" default="false"/>
        <xs:attribute name="paraTcid" type="xs:nonNegativeInteger" use="optional"/>
    </xs:complexType>
    
    <xs:complexType name="SectionDefinitionType">
        <xs:sequence>
            <xs:element name="startNum" minOccurs="0">
                <xs:annotation><xs:documentation>시작 번호</xs:documentation></xs:annotation>
                <xs:complexType>
                     <xs:attribute name="pageStartsOn" default="BOTH">
                        <xs:annotation><xs:documentation>구역 나눔을 한 용지가 생길 때 페이지 번호 적용 옵션</xs:documentation></xs:annotation>
                        <xs:simpleType>
                            <xs:restriction base="xs:string">
                                <xs:enumeration value="BOTH"/>
                                <xs:enumeration value="EVEN"/>
                                <xs:enumeration value="ODD"/>
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="page" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>페이지 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="pic" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>그림 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="tbl" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>표 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="equation" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>수식 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="grid" minOccurs="0">
                <xs:annotation><xs:documentation>격자 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                    <xs:attribute name="lineGrid" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>줄 격자. 0이면 현재 글꼴을 한 줄로 함</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="charGrid" type="xs:nonNegativeInteger" default="0">
                         <xs:annotation><xs:documentation>글자 격자. 0이면 현재 글꼴을 한 글자로 함</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="wongojiFormat" type="xs:boolean" default="true">
                        <xs:annotation><xs:documentation>원고지 형식 여부</xs:documentation></xs:annotation>
                    </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="visibility" minOccurs="0">
                 <xs:annotation><xs:documentation>감추기/보여주기 설정</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:attribute name="hideFirstHeader" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 머리말 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstFooter" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 꼬리말 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstMasterPage" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 바탕쪽 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="border" type="hp:VisibilityValue"/>
                     <xs:attribute name="fill" type="hp:VisibilityValue"/>
                     <xs:attribute name="hideFirstPageNum" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 쪽번호 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstEmptyLine" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 빈 줄 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="showLineNumber" type="xs:boolean" default="false">
                         <xs:annotation><xs:documentation>줄 번호 표시 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="lineNumberShape" minOccurs="0">
                <xs:annotation><xs:documentation>줄 번호 모양</xs:documentation></xs:annotation>
                <xs:complexType>
                    <xs:attribute name="restartType" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>줄 번호 방식</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="countBy" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>번호 표시 간격</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="distance" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>본문과 번호 거리</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="startNumber" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>줄 번호 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="pagePr" minOccurs="0">
                <xs:annotation><xs:documentation>용지 설정</xs:documentation></xs:annotation>
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="margin">
                            <xs:complexType>
                                <xs:attributeGroup ref="hc:MarginAttributeGroup"/>
                                <xs:attribute name="header" type="xs:nonNegativeInteger" default="4252">
                                    <xs:annotation><xs:documentation>머리말 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="footer" type="xs:nonNegativeInteger" default="4252">
                                     <xs:annotation><xs:documentation>꼬리말 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="gutter" type="xs:nonNegativeInteger" default="0">
                                     <xs:annotation><xs:documentation>제본 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                    <xs:attribute name="landscape" default="NARROWLY">
                         <xs:annotation><xs:documentation>용지 방향</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                 <xs:enumeration value="WIDELY"/>
                                 <xs:enumeration value="NARROWLY"/>
                             </xs:restriction>
                         </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="width" type="xs:positiveInteger" default="59528">
                         <xs:annotation><xs:documentation>용지 가로 크기. 단위는 HWPUNIT</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="height" type="xs:positiveInteger" default="84188">
                         <xs:annotation><xs:documentation>용지 세로 크기. 단위는 HWPUNIT</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="gutterType" default="LEFT_ONLY">
                         <xs:annotation><xs:documentation>제본 방식</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="LEFT_ONLY"/>
                                <xs:enumeration value="LEFT_RIGHT"/>
                                <xs:enumeration value="TOP_BOTTOM"/>
                             </xs:restriction>
                         </xs:simpleType>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="footNotePr" type="hp:FootNoteShapeType" minOccurs="0">
                 <xs:annotation><xs:documentation>각주 모양</xs:documentation></xs:annotation>
            </xs:element>
            <xs:element name="endNotePr" type="hp:EndNoteShapeType" minOccurs="0">
                 <xs:annotation><xs:documentation>미주 모양</xs:documentation></xs:annotation>
            </xs:element>
            <xs:element name="pageBorderFill" minOccurs="0" maxOccurs="3">
                 <xs:annotation><xs:documentation>쪽 테두리/배경 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:sequence>
                         <xs:element name="offset">
                            <xs:annotation><xs:documentation>테두리/배경 위치</xs:documentation></xs:annotation>
                            <xs:complexType>
                                <xs:attribute name="left" type="xs:nonNegativeInteger" default="1417">
                                    <xs:annotation><xs:documentation>왼쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="right" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>오른쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="top" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>위쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="bottom" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>아래쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                            </xs:complexType>
                         </xs:element>
                     </xs:sequence>
                     <xs:attribute name="type">
                         <xs:annotation><xs:documentation>적용 쪽</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="BOTH"><xs:annotation><xs:documentation>양쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="EVEN"><xs:annotation><xs:documentation>짝수쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="ODD"><xs:annotation><xs:documentation>홀수쪽</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
                        <xs:annotation><xs:documentation>테두리/배경 아이디 참조</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="textBorder">
                        <xs:annotation><xs:documentation>테두리 위치 기준</xs:documentation></xs:annotation>
                        <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="CONTENT"><xs:annotation><xs:documentation>본문 기준</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="PAPER"><xs:annotation><xs:documentation>종이 기준</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="headerInside" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>머리말 포함 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="footerInside" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>꼬리말 포함 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="fillArea">
                         <xs:annotation><xs:documentation>채울 영역</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="PAPER"><xs:annotation><xs:documentation>종이</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="PAGE"><xs:annotation><xs:documentation>쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="BORDER"><xs:annotation><xs:documentation>테두리</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="masterpage" minOccurs="0" maxOccurs="unbounded">
                 <xs:annotation><xs:documentation>바탕쪽 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                    <xs:attribute name="idRef" type="xs:string" use="required"/>
                 </xs:complexType>
            </xs:element>
            <xs:element name="presentation" minOccurs="0">
                 <xs:annotation><xs:documentation>프레젠테이션 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:sequence>
                         <xs:element name="fillBrush" type="hc:FillBrushType" minOccurs="0">
                            <xs:annotation><xs:documentation>배경 정보</xs:documentation></xs:annotation>
                         </xs:element>
                     </xs:sequence>
                     <xs:attribute name="effect">
                         <xs:annotation><xs:documentation>화면 전환 효과</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="none"/><xs:enumeration value="serLen"/><xs:enumeration value="serRight"/>
                                <xs:enumeration value="serUp"/><xs:enumeration value="serDown"/><xs:enumeration value="rectOut"/>
                                <xs:enumeration value="rectIn"/><xs:enumeration value="windLeft"/><xs:enumeration value="windRight"/>
                                <xs:enumeration value="blindUp"/><xs:enumeration value="blindDown"/><xs:enumeration value="curtionHorzOut"/>
                                <xs:enumeration value="curtionHorzIn"/><xs:enumeration value="curtionVertOut"/><xs:enumeration value="curtionVertIn"/>
                                <xs:enumeration value="moveLeft"/><xs:enumeration value="moveRight"/><xs:enumeration value="moveUp"/>
                                <xs:enumeration value="moveDown"/><xs:enumeration value="random"/>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="soundIDRef">
                         <xs:simpleType><xs:restriction base="xs:string"/></xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="invertText" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>글자 반전</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="autoShow" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>자동 화면 전환</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="showTime" type="xs:nonNegativeInteger"/>
                     <xs:attribute name="applyTo">
                        <xs:annotation><xs:documentation>적용 범위</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="WholeDoc"/>
                                <xs:enumeration value="NewSection"/>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="textDirection" use="optional" default="HORIZONTAL">
             <xs:annotation><xs:documentation>텍스트 방향</xs:documentation></xs:annotation>
             <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="HORIZONTAL"/>
                    <xs:enumeration value="VERTICAL"/>
                    <xs:enumeration value="VERTICALALL">
                        <xs:annotation><xs:documentation>영문 눕힘</xs:documentation></xs:annotation>
                    </xs:enumeration>
                </xs:restriction>
             </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="spaceColumns" type="xs:integer" default="0">
             <xs:annotation><xs:documentation>다단 편집에서 서로 다른 단 사이의 간격</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="tabStopValue" type="xs:integer" default="0">
             <xs:annotation><xs:documentation>기본 탭 간격</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="tabStopUnit">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="CHAR"/>
                    <xs:enumeration value="HWPUNIT"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="outlineShapeIDRef" type="xs:nonNegativeInteger">
            <xs:annotation><xs:documentation>개요 번호 모양 아이디 참조</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="memoShapeIDRef" type="xs:nonNegativeInteger">
             <xs:annotation><xs:documentation>구역 내에서 사용되는 메모의 모양을 설정하기 위한 아이디 참조 값</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="textVerticalWidthHead" type="xs:boolean" default="false">
            <xs:annotation><xs:documentation>세로쓰기 머리말</xs:documentation></xs:annotation>
        </xs:attribute>
    </xs:complexType>
```xml
</xs:schema>
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
```
           xmlns:hp="http://www.owpml.org/owpml/2024/paragraph"
           xmlns:hc="http://www.owpml.org/owpml/2024/core"
           targetNamespace="http://www.owpml.org/owpml/2024/paragraph"
           elementFormDefault="qualified">

```xml
    <xs:import namespace="http://www.owpml.org/owpml/2024/core" schemaLocation="HWPMLCore.xsd"/>
    <xs:import namespace="http://www.w3.org/XML/1998/namespace" schemaLocation="http://www.w3.org/2001/xml.xsd"/>
```
    
    <xs:complexType name="SectionType">
        <xs:sequence>
            <xs:element name="p" type="hp:PType" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    
    <xs:complexType name="ParaListType">
        <xs:sequence>
            <xs:element name="p" type="hp:PType" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="textDirection" default="HORIZONTAL">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="HORIZONTAL"/>
                    <xs:enumeration value="VERTICAL"/>
                    <xs:enumeration value="VERTICALALL">
                        <xs:annotation><xs:documentation>영문 눕힘</xs:documentation></xs:annotation>
                    </xs:enumeration>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="lineWrap" default="BREAK">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="BREAK"/>
                    <xs:enumeration value="SQUEEZE"/>
                    <xs:enumeration value="KEEP"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="vertAlign" default="TOP"/>
    </xs:complexType>
    
    <xs:element name="sec" type="hp:SectionDefinitionType">
        <xs:annotation>
            <xs:documentation>HWPML 문서의 구역</xs:documentation>
        </xs:annotation>
    </xs:element>

    <xs:complexType name="PType">
        <xs:choice minOccurs="0" maxOccurs="unbounded">
            <xs:element name="run">
                <xs:complexType>
                    <xs:choice minOccurs="0" maxOccurs="unbounded">
                        <xs:element name="ctrl">
                            <xs:complexType>
                                <xs:choice minOccurs="1" maxOccurs="unbounded">
                                    <xs:element name="colPr" type="hp:ColumnDefType" minOccurs="0"/>
                                    <xs:element name="fieldBegin">
                                        <xs:complexType>
                                            <xs:sequence minOccurs="0">
                                                <xs:element name="parameters" type="hp:ParameterList" minOccurs="0"/>
                                                <xs:element name="subList" type="hp:ParaListType" minOccurs="0"/>
                                                <xs:element name="metaTag" type="hc:MetaTagType" minOccurs="0"/>
                                            </xs:sequence>
                                            <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
                                            <xs:attribute name="type" type="hp:FieldType" use="required"/>
                                            <xs:attribute name="name" type="xs:string"/>
                                            <xs:attribute name="editable" type="xs:boolean" default="true"/>
                                            <xs:attribute name="dirty" type="xs:boolean" default="false"/>
                                            <xs:attribute name="zorder" type="xs:integer"/>
                                            <xs:attribute name="fieldid" type="xs:nonNegativeInteger"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="fieldEnd">
                                        <xs:complexType>
                                            <xs:attribute name="beginIDRef" type="xs:nonNegativeInteger" use="required"/>
                                            <xs:attribute name="fieldid" type="xs:unsignedInt"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="bookmark">
                                        <xs:complexType>
                                            <xs:attribute name="name" type="xs:string"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="header" type="hp:HeaderFooterType"/>
                                    <xs:element name="footer" type="hp:HeaderFooterType"/>
                                    <xs:element name="footNote" type="hp:NoteType"/>
                                    <xs:element name="endNote" type="hp:NoteType"/>
                                    <xs:element name="autoNum" type="hp:AutoNumNewNumType"/>
                                    <xs:element name="newNum" type="hp:AutoNumNewNumType"/>
                                    <xs:element name="pageNumCtrl">
                                        <xs:complexType>
                                            <xs:attribute name="pageStartsOn" default="BOTH">
                                                <xs:simpleType>
                                                    <xs:restriction base="xs:string">
                                                        <xs:enumeration value="BOTH"/>
                                                        <xs:enumeration value="EVEN"/>
                                                        <xs:enumeration value="ODD"/>
                                                    </xs:restriction>
                                                </xs:simpleType>
                                            </xs:attribute>
                                            <!-- ... 기타 pageNumCtrl 속성들 ... -->
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="pageHiding">
                                        <xs:complexType>
                                            <xs:attribute name="hideHeader" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideFooter" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideMasterPage" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideBorder" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideFill" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hidePageNum" type="xs:boolean" default="false"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="pageNum">
                                        <xs:complexType>
                                            <xs:attribute name="pos" default="TOP_LEFT">
                                                <xs:annotation><xs:documentation>쪽 번호 위치</xs:documentation></xs:annotation>
                                                <xs:simpleType>
                                                    <xs:restriction base="xs:string">
                                                        <xs:enumeration value="NONE"/>
                                                        <xs:enumeration value="TOP_LEFT"/>
                                                        <xs:enumeration value="TOP_CENTER"/>
                                                        <xs:enumeration value="TOP_RIGHT"/>
                                                        <xs:enumeration value="BOTTOM_LEFT"/>
                                                        <xs:enumeration value="BOTTOM_CENTER"/>
                                                        <xs:enumeration value="BOTTOM_RIGHT"/>
                                                        <xs:enumeration value="OUTSIDE_TOP"/>
                                                        <xs:enumeration value="OUTSIDE_BOTTOM"/>
                                                        <xs:enumeration value="INSIDE_TOP"/>
                                                        <xs:enumeration value="INSIDE_BOTTOM"/>
                                                    </xs:restriction>
                                                </xs:simpleType>
                                            </xs:attribute>
                                            <xs:attribute name="formatType" type="hc:NumberType" default="DIGIT">
                                                <xs:annotation><xs:documentation>쪽 번호 형식</xs:documentation></xs:annotation>
                                            </xs:attribute>
                                            <xs:attribute name="sideChar" type="xs:string" default="-">
                                                 <xs:annotation><xs:documentation>앞뒤 장식 문자 넣기</xs:documentation></xs:annotation>
                                            </xs:attribute>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="indexmark">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="firstKey"/>
                                                <xs:element name="secondKey"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="hiddenComment">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="subList" type="hp:ParaListType"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:choice>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="t">
                            <!-- ... t(text) element definition ... -->
                        </xs:element>
                        <xs:element name="markpenBegin">
                            <xs:complexType>
                                <xs:attribute name="color" type="hc:RGBColorType"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="markpenEnd" minOccurs="0"/>
                        <xs:element name="titleMark">
                             <xs:complexType>
                                <xs:attribute name="ignore" type="xs:boolean" default="false"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="tab" minOccurs="0">
                             <xs:annotation><xs:documentation>Attribute 'width' 단위는 hwpunit</xs:documentation></xs:annotation>
                             <xs:complexType>
                                <xs:attribute name="width" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="leader" type="hc:LineType2"/>
                                <xs:attribute name="type">
                                    <xs:annotation><xs:documentation>탭의 종류</xs:documentation></xs:annotation>
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="LEFT"><xs:annotation><xs:documentation>왼쪽</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="RIGHT"><xs:annotation><xs:documentation>오른쪽</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="CENTER"><xs:annotation><xs:documentation>가운데</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="DECIMAL"><xs:annotation><xs:documentation>소수점</xs:documentation></xs:annotation></xs:enumeration>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="lineBreak" minOccurs="0"/>
                        <xs:element name="hyphen" minOccurs="0"/>
                        <xs:element name="nbspace" minOccurs="0"/>
                        <xs:element name="fwspace" minOccurs="0"/>
                        <xs:element name="insertBegin" type="hp:TrackChangeTag"/>
                        <xs:element name="insertEnd" type="hp:TrackChangeTag"/>
                        <xs:element name="deleteBegin" type="hp:TrackChangeTag"/>
                        <xs:element name="deleteEnd" type="hp:TrackChangeTag"/>
                        <xs:element name="tbl">
                            <xs:complexType>
                                <xs:attribute name="charStyleIDRef" type="xs:nonNegativeInteger"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="drawing" type="hp:ShapeType"/>
                        <xs:element name="pic" type="hp:PictureType"/>
                        <xs:element name="ole" type="hp:OLEType"/>
                        <xs:element name="container" type="hp:ContainerType"/>
                        <xs:element name="equation" type="hp:EquationType"/>
                        <xs:element name="line" type="hp:LineType"/>
                        <xs:element name="rect" type="hp:RectangleType"/>
                        <xs:element name="ellipse" type="hp:EllipseType"/>
                        <xs:element name="arc" type="hp:ArcType"/>
                        <xs:element name="polygon" type="hp:PolygonType"/>
                        <xs:element name="curve" type="hp:CurveType"/>
                        <xs:element name="connectLine" type="hp:ConnectLineType"/>
                        <xs:element name="textart">
                            <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractDrawingObjectType">
                                        <xs:sequence>
                                            <xs:element name="pt0" type="hc:PointType"/>
                                            <xs:element name="pt1" type="hc:PointType"/>
                                            <xs:element name="pt2" type="hc:PointType"/>
                                            <xs:element name="pt3" type="hc:PointType"/>
                                            <xs:element name="textartPr">
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="shadow" type="hp:ShadowType"/>
                                                    </xs:sequence>
                                                    <xs:attribute name="fontName" type="xs:string"/>
                                                    <xs:attribute name="fontStyle" type="xs:string"/>
                                                    <xs:attribute name="fontType" default="TTF">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="TTF"/>
                                                                <xs:enumeration value="HFT"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="textShape" default="REGULAR">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="REGULAR"/>
                                                                <xs:enumeration value="PARALLELOGRAM"/>
                                                                <xs:enumeration value="INVERTED_PARALLELOGRAM"/>
                                                                <xs:enumeration value="UPWARD_CASCADE"/>
                                                                <xs:enumeration value="DOWNWARD_CASCADE"/>
                                                                <xs:enumeration value="INVERTED_UPWARD_CASCADE"/>
                                                                <xs:enumeration value="INVERTED_DOWNWARD_CASCADE"/>
                                                                <xs:enumeration value="REDUCE_RIGHT"/>
                                                                <xs:enumeration value="REDUCE_LEFT"/>
                                                                <xs:enumeration value="ISOSCELES_TRAPEZOID"/>
                                                                <xs:enumeration value="INVERTED_ISOSCELES_TRAPEZOID"/>
                                                                <xs:enumeration value="TOP_RIBBON_RECTANGLE"/>
                                                                <xs:enumeration value="BOTTOM_RIBBON_RECTANGLE"/>
                                                                <xs:enumeration value="CHEVRON"/>
                                                                <xs:enumeration value="BOW_TIE"/>
                                                                <xs:enumeration value="HEXAGON"/>
                                                                <xs:enumeration value="WAVE1"/>
                                                                <xs:enumeration value="WAVE2"/>
                                                                <xs:enumeration value="WAVE3"/>
                                                                <xs:enumeration value="WAVE4"/>
                                                                <xs:enumeration value="LEFT_TILT_CYLINDER"/>
                                                                <xs:enumeration value="RIGHT_TILT_CYLINDER"/>
                                                                <xs:enumeration value="BOTTOM_WIDE_CYLINDER"/>
                                                                <xs:enumeration value="TOP_WIDE_CYLINDER"/>
                                                                <xs:enumeration value="THIN_CURVE_UP1"/>
                                                                <xs:enumeration value="THIN_CURVE_UP2"/>
                                                                <xs:enumeration value="THIN_CURVE_DOWN1"/>
                                                                <xs:enumeration value="THIN_CURVE_DOWN2"/>
                                                                <xs:enumeration value="INVERSED_FINGERNAIL"/>
                                                                <xs:enumeration value="FINGERNAIL"/>
                                                                <xs:enumeration value="GINKO_LEAF1"/>
                                                                <xs:enumeration value="GINKO_LEAF2"/>
                                                                <xs:enumeration value="INFLATE_RIGHT"/>
                                                                <xs:enumeration value="INFLATE_LEFT"/>
                                                                <xs:enumeration value="INFLATE_TOP_CONVEX"/>
                                                                <xs:enumeration value="INFLATE_BOTTOM_CONCAVE"/>
                                                                <xs:enumeration value="DEFLATE_TOP1"/>
                                                                <xs:enumeration value="DEFLATE_BOTTOM"/>
                                                                <xs:enumeration value="DEFLATE"/>
                                                                <xs:enumeration value="INFLATE"/>
                                                                <xs:enumeration value="INFLATE_TOP"/>
                                                                <xs:enumeration value="INFLATE_BOTTOM"/>
                                                                <xs:enumeration value="RECTANGLE"/>
                                                                <xs:enumeration value="LEFT_CYLINDER"/>
                                                                <xs:enumeration value="CYLINDER"/>
                                                                <xs:enumeration value="RIGHT_CYLINDER"/>
                                                                <xs:enumeration value="CIRCLE"/>
                                                                <xs:enumeration value="CURVE_DOWN"/>
                                                                <xs:enumeration value="ARCH_UP"/>
                                                                <xs:enumeration value="ARCH_DOWN"/>
                                                                <xs:enumeration value="SINGLE_LINE_CIRCLE1"/>
                                                                <xs:enumeration value="SINGLE_LINE_CIRCLE2"/>
                                                                <xs:enumeration value="TRIPLE_LINE_CIRCLE1"/>
                                                                <xs:enumeration value="TRIPLE_LINE_CIRCLE2"/>
                                                                <xs:enumeration value="DOUBLE_LINE_CIRCLE"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="lineSpacing" default="120">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:nonNegativeInteger">
                                                                <xs:minInclusive value="50"/>
                                                                <xs:maxInclusive value="500"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="charSpacing" default="100">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:nonNegativeInteger">
                                                                <xs:minInclusive value="-50"/>
                                                                <xs:maxInclusive value="500"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="align" default="LEFT">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="LEFT"/>
                                                                <xs:enumeration value="RIGHT"/>
                                                                <xs:enumeration value="CENTER"/>
                                                                <xs:enumeration value="FULL"/>
                                                                <xs:enumeration value="TABLE"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                </xs:complexType>
                                            </xs:element>
                                            <xs:element name="outline">
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="pt" type="hc:PointType" minOccurs="0" maxOccurs="unbounded"/>
                                                    </xs:sequence>
                                                    <xs:attribute name="cnt" type="xs:nonNegativeInteger"/>
                                                </xs:complexType>
                                            </xs:element>
                                        </xs:sequence>
                                        <xs:attribute name="text" type="xs:string"/>
                                    </xs:extension>
                                </xs:complexContent>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="compose">
                            <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="charPr" maxOccurs="unbounded">
                                        <xs:complexType>
                                            <xs:attribute name="prIDRef" type="xs:nonNegativeInteger"/>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:sequence>
                                <xs:attribute name="circleType" default="SHAPE_CIRCLE">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="CHAR"/>
                                            <xs:enumeration value="SHAPE_CIRCLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_CIRCLE"/>
                                            <xs:enumeration value="SHAPE_RECTANGLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_RECTANGLE"/>
                                            <xs:enumeration value="SHAPE_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_LIGHT"/>
                                            <xs:enumeration value="SHAPE_RHOMBUS"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_RHOMBUS"/>
                                            <xs:enumeration value="SHAPE_EMPTY_CIRCULATE_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_THICK_CIRCULATE_TRIANGLE"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="charSz" type="xs:integer">
                                     <xs:annotation><xs:documentation>글자 크기 비율 (%)</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="composeType">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="SPREAD"/>
                                            <xs:enumeration value="OVERLAP"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="charprCnt" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="composeText" type="xs:string"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="dutmal">
                             <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="mainText"/>
                                    <xs:element name="subText"/>
                                </xs:sequence>
                                <xs:attribute name="pos" default="TOP">
                                     <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="TOP"/>
                                            <xs:enumeration value="BOTTOM"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="szRatio" type="xs:positiveInteger"/>
                                <xs:attribute name="option" type="xs:unsignedInt" default="47"/>
                                <xs:attribute name="styleIDRef" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="align" default="CENTER">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="JUSTIFY"/>
                                            <xs:enumeration value="LEFT"/>
                                            <xs:enumeration value="RIGHT"/>
                                            <xs:enumeration value="CENTER"/>
                                            <xs:enumeration value="DISTRIBUTE"/>
                                            <xs:enumeration value="DISTRIBUTE_SPACE"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                             </xs:complexType>
                        </xs:element>
                        <xs:element name="btn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="radioBtn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="checkBtn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="comboBox" type="hp:ComboBoxType"/>
                        <xs:element name="listBox" type="hp:ListBoxType"/>
                        <xs:element name="edit" type="hp:EditType"/>
                        <xs:element name="scrollBar" type="hp:ScrollBarType"/>
                        <xs:element name="video">
                             <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractShapeComponentType">
                                        <xs:attribute name="videoType" use="required">
                                             <xs:annotation><xs:documentation>비디오 종류 (로컬/웹)</xs:documentation></xs:annotation>
                                             <xs:simpleType>
                                                <xs:restriction base="xs:string">
                                                    <xs:enumeration value="LOCAL">
                                                        <xs:annotation><xs:documentation>로컬 컴퓨터의 동영상</xs:documentation></xs:annotation>
                                                    </xs:enumeration>
                                                    <xs:enumeration value="WEB">
                                                        <xs:annotation><xs:documentation>웹 링크 동영상</xs:documentation></xs:annotation>
                                                    </xs:enumeration>
                                                </xs:restriction>
                                            </xs:simpleType>
                                        </xs:attribute>
                                        <xs:attribute name="fileIDRef" type="xs:string" use="optional"/>
                                        <xs:attribute name="imageIDRef" type="xs:string" use="optional"/>
                                        <xs:attribute name="tag" type="xs:string" use="optional"/>
                                    </xs:extension>
                                </xs:complexContent>
                             </xs:complexType>
                        </xs:element>
                        <xs:element name="chart">
                             <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractShapeObjectType">
                                        <xs:attribute name="version" type="xs:float"/>
                                        <xs:attribute name="chartIDRef" type="xs:string"/>
                                    </xs:extension>
                                </xs:complexContent>
                             </xs:complexType>
                        </xs:element>
                    </xs:choice>
                    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger"/>
                    <xs:attribute name="charTcid" type="xs:nonNegativeInteger" use="optional"/>
                </xs:complexType>
            </xs:element>
        </xs:choice>
        <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="paraPrIDRef" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="styleIDRef" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="pageBreak" type="xs:boolean" default="false"/>
        <xs:attribute name="columnBreak" type="xs:boolean" default="false"/>
        <xs:attribute name="merged" type="xs:boolean" default="false"/>
        <xs:attribute name="paraTcid" type="xs:nonNegativeInteger" use="optional"/>
    </xs:complexType>
    
    <xs:complexType name="SectionDefinitionType">
        <xs:sequence>
            <xs:element name="startNum" minOccurs="0">
                <xs:annotation><xs:documentation>시작 번호</xs:documentation></xs:annotation>
                <xs:complexType>
                     <xs:attribute name="pageStartsOn" default="BOTH">
                        <xs:annotation><xs:documentation>구역 나눔을 한 용지가 생길 때 페이지 번호 적용 옵션</xs:documentation></xs:annotation>
                        <xs:simpleType>
                            <xs:restriction base="xs:string">
                                <xs:enumeration value="BOTH"/>
                                <xs:enumeration value="EVEN"/>
                                <xs:enumeration value="ODD"/>
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="page" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>페이지 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="pic" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>그림 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="tbl" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>표 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="equation" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>수식 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="grid" minOccurs="0">
                <xs:annotation><xs:documentation>격자 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                    <xs:attribute name="lineGrid" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>줄 격자. 0이면 현재 글꼴을 한 줄로 함</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="charGrid" type="xs:nonNegativeInteger" default="0">
                         <xs:annotation><xs:documentation>글자 격자. 0이면 현재 글꼴을 한 글자로 함</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="wongojiFormat" type="xs:boolean" default="true">
                        <xs:annotation><xs:documentation>원고지 형식 여부</xs:documentation></xs:annotation>
                    </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="visibility" minOccurs="0">
                 <xs:annotation><xs:documentation>감추기/보여주기 설정</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:attribute name="hideFirstHeader" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 머리말 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstFooter" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 꼬리말 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstMasterPage" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 바탕쪽 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="border" type="hp:VisibilityValue"/>
                     <xs:attribute name="fill" type="hp:VisibilityValue"/>
                     <xs:attribute name="hideFirstPageNum" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 쪽번호 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstEmptyLine" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 빈 줄 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="showLineNumber" type="xs:boolean" default="false">
                         <xs:annotation><xs:documentation>줄 번호 표시 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="lineNumberShape" minOccurs="0">
                <xs:annotation><xs:documentation>줄 번호 모양</xs:documentation></xs:annotation>
                <xs:complexType>
                    <xs:attribute name="restartType" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>줄 번호 방식</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="countBy" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>번호 표시 간격</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="distance" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>본문과 번호 거리</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="startNumber" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>줄 번호 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="pagePr" minOccurs="0">
                <xs:annotation><xs:documentation>용지 설정</xs:documentation></xs:annotation>
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="margin">
                            <xs:complexType>
                                <xs:attributeGroup ref="hc:MarginAttributeGroup"/>
                                <xs:attribute name="header" type="xs:nonNegativeInteger" default="4252">
                                    <xs:annotation><xs:documentation>머리말 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="footer" type="xs:nonNegativeInteger" default="4252">
                                     <xs:annotation><xs:documentation>꼬리말 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="gutter" type="xs:nonNegativeInteger" default="0">
                                     <xs:annotation><xs:documentation>제본 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                    <xs:attribute name="landscape" default="NARROWLY">
                         <xs:annotation><xs:documentation>용지 방향</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                 <xs:enumeration value="WIDELY"/>
                                 <xs:enumeration value="NARROWLY"/>
                             </xs:restriction>
                         </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="width" type="xs:positiveInteger" default="59528">
                         <xs:annotation><xs:documentation>용지 가로 크기. 단위는 HWPUNIT</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="height" type="xs:positiveInteger" default="84188">
                         <xs:annotation><xs:documentation>용지 세로 크기. 단위는 HWPUNIT</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="gutterType" default="LEFT_ONLY">
                         <xs:annotation><xs:documentation>제본 방식</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="LEFT_ONLY"/>
                                <xs:enumeration value="LEFT_RIGHT"/>
                                <xs:enumeration value="TOP_BOTTOM"/>
                             </xs:restriction>
                         </xs:simpleType>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="footNotePr" type="hp:FootNoteShapeType" minOccurs="0">
                 <xs:annotation><xs:documentation>각주 모양</xs:documentation></xs:annotation>
            </xs:element>
            <xs:element name="endNotePr" type="hp:EndNoteShapeType" minOccurs="0">
                 <xs:annotation><xs:documentation>미주 모양</xs:documentation></xs:annotation>
            </xs:element>
            <xs:element name="pageBorderFill" minOccurs="0" maxOccurs="3">
                 <xs:annotation><xs:documentation>쪽 테두리/배경 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:sequence>
                         <xs:element name="offset">
                            <xs:annotation><xs:documentation>테두리/배경 위치</xs:documentation></xs:annotation>
                            <xs:complexType>
                                <xs:attribute name="left" type="xs:nonNegativeInteger" default="1417">
                                    <xs:annotation><xs:documentation>왼쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="right" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>오른쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="top" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>위쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="bottom" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>아래쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                            </xs:complexType>
                         </xs:element>
                     </xs:sequence>
                     <xs:attribute name="type">
                         <xs:annotation><xs:documentation>적용 쪽</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="BOTH"><xs:annotation><xs:documentation>양쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="EVEN"><xs:annotation><xs:documentation>짝수쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="ODD"><xs:annotation><xs:documentation>홀수쪽</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
                        <xs:annotation><xs:documentation>테두리/배경 아이디 참조</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="textBorder">
                        <xs:annotation><xs:documentation>테두리 위치 기준</xs:documentation></xs:annotation>
                        <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="CONTENT"><xs:annotation><xs:documentation>본문 기준</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="PAPER"><xs:annotation><xs:documentation>종이 기준</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="headerInside" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>머리말 포함 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="footerInside" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>꼬리말 포함 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="fillArea">
                         <xs:annotation><xs:documentation>채울 영역</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="PAPER"><xs:annotation><xs:documentation>종이</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="PAGE"><xs:annotation><xs:documentation>쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="BORDER"><xs:annotation><xs:documentation>테두리</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="masterpage" minOccurs="0" maxOccurs="unbounded">
                 <xs:annotation><xs:documentation>바탕쪽 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                    <xs:attribute name="idRef" type="xs:string" use="required"/>
                 </xs:complexType>
            </xs:element>
            <xs:element name="presentation" minOccurs="0">
                 <xs:annotation><xs:documentation>프레젠테이션 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:sequence>
                         <xs:element name="fillBrush" type="hc:FillBrushType" minOccurs="0">
                            <xs:annotation><xs:documentation>배경 정보</xs:documentation></xs:annotation>
                         </xs:element>
                     </xs:sequence>
                     <xs:attribute name="effect">
                         <xs:annotation><xs:documentation>화면 전환 효과</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="none"/>
                                <xs:enumeration value="serLen"/>
                                <xs:enumeration value="serRight"/>
                                <xs:enumeration value="serUp"/>
                                <xs:enumeration value="serDown"/>
                                <xs:enumeration value="rectOut"/>
                                <xs:enumeration value="rectIn"/>
                                <xs:enumeration value="windLeft"/>
                                <xs:enumeration value="windRight"/>
                                <xs:enumeration value="blindUp"/>
                                <xs:enumeration value="blindDown"/>
                                <xs:enumeration value="curtionHorzOut"/>
                                <xs:enumeration value="curtionHorzIn"/>
                                <xs:enumeration value="curtionVertOut"/>
                                <xs:enumeration value="curtionVertIn"/>
                                <xs:enumeration value="moveLeft"/>
                                <xs:enumeration value="moveRight"/>
                                <xs:enumeration value="moveUp"/>
                                <xs:enumeration value="moveDown"/>
                                <xs:enumeration value="random"/>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="soundIDRef">
                         <xs:simpleType><xs:restriction base="xs:string"/></xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="invertText" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>글자 반전</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="autoShow" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>자동 화면 전환</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="showTime" type="xs:nonNegativeInteger"/>
                     <xs:attribute name="applyTo">
                        <xs:annotation><xs:documentation>적용 범위</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="WholeDoc"/>
                                <xs:enumeration value="NewSection"/>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="textDirection" use="optional" default="HORIZONTAL">
             <xs:annotation><xs:documentation>텍스트 방향</xs:documentation></xs:annotation>
             <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="HORIZONTAL"/>
                    <xs:enumeration value="VERTICAL"/>
                    <xs:enumeration value="VERTICALALL">
                        <xs:annotation><xs:documentation>영문 눕힘</xs:documentation></xs:annotation>
                    </xs:enumeration>
                </xs:restriction>
             </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="spaceColumns" type="xs:integer" default="0">
             <xs:annotation><xs:documentation>다단 편집에서 서로 다른 단 사이의 간격</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="tabStopValue" type="xs:integer" default="0">
             <xs:annotation><xs:documentation>기본 탭 간격</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="tabStopUnit">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="CHAR"/>
                    <xs:enumeration value="HWPUNIT"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="outlineShapeIDRef" type="xs:nonNegativeInteger">
            <xs:annotation><xs:documentation>개요 번호 모양 아이디 참조</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="memoShapeIDRef" type="xs:nonNegativeInteger">
             <xs:annotation><xs:documentation>구역 내에서 사용되는 메모의 모양을 설정하기 위한 아이디 참조 값</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="textVerticalWidthHead" type="xs:boolean" default="false">
            <xs:annotation><xs:documentation>세로쓰기 머리말</xs:documentation></xs:annotation>
        </xs:attribute>
    </xs:complexType>
</xs:schema>
<xs:complexType name="BulletType">
    <xs:annotation>
        <xs:documentation>글머리표 문단 모양 정보</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="img" type="hc:ImageType" minOccurs="0"/>
        <xs:element name="paraHead" type="ParaHeadType"/>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="char" type="xs:string" use="required">
        <xs:annotation>
            <xs:documentation>글머리표 문자</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="checkedChar" type="xs:string">
        <xs:annotation>
            <xs:documentation>체크되었을 때의 글머리표 문자</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="useImage" type="xs:boolean" use="required">
        <xs:annotation>
            <xs:documentation>이미지 사용 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="ParaHeadType" mixed="true">
    <xs:annotation>
        <xs:documentation>
            번호/문단머리 정보.
            문자열 내 특정 문자에 제어코드(^, #)를 사용함으로써 해당 수준에서 표시되는 번호 또는 문단 머리의 포맷을 제어한다.
            ^n: n수준 정보를 표시한다. (예: 1.1.1.1.1.1.1)
            ^N: n수준 정보를 표시하며 마지막에 마침표를 하나 더 찍는다. (예: 1.1.1.1.1.1.1.)
            번호(1-7): 해당 수준에 해당하는 숫자 또는 문자 또는 기호를 표시한다.
        </xs:documentation>
    </xs:annotation>
    <xs:attribute name="start" type="xs:unsignedInt" default="1">
        <xs:annotation>
            <xs:documentation>시작 번호</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="level" use="required">
        <xs:annotation>
            <xs:documentation>수준</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:positiveInteger"/>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="align" default="LEFT">
        <xs:annotation>
            <xs:documentation>번호 정렬 방식</xs:documentation>
        </xs:annotation>
        <!-- align 속성의 simpleType 정의 누락되었으나 문맥상 Left, Right, Center 등 포함될 것으로 추정 -->
    </xs:attribute>
    <xs:attribute name="autoIndent" type="xs:boolean" default="true">
        <xs:annotation>
            <xs:documentation>자동 내어쓰기 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="widthAdjust" type="xs:integer" default="0">
        <xs:annotation>
            <xs:documentation>너비 보정 값. 단위는 hwpunit</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="textOffsetType" default="PERCENT">
        <xs:annotation>
            <xs:documentation>본문과의 거리 범위 유형</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="PERCENT"/>
                <xs:enumeration value="HWPUNIT"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="textOffset" type="xs:integer" default="50">
        <xs:annotation>
            <xs:documentation>본문과의 거리</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="numFormat" type="hc:NumberType" default="DIGIT">
        <xs:annotation>
            <xs:documentation>번호 포맷 (글머리표 문단의 경우에는 사용되지 않음)</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>글자 모양 아이디 참조</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="checkChar" type="xs:string">
        <xs:annotation>
            <xs:documentation>체크 글머리 문자</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="ParaShapeType">
    <xs:annotation>
        <xs:documentation>문단 모양 정보</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="align">
            <xs:annotation>
                <xs:documentation>문단 정렬</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="horizontal" use="required">
                    <xs:annotation>
                        <xs:documentation>수평 정렬</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="JUSTIFY">
                                <xs:annotation><xs:documentation>양쪽 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="LEFT">
                                <xs:annotation><xs:documentation>왼쪽 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="RIGHT">
                                <xs:annotation><xs:documentation>오른쪽 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER">
                                <xs:annotation><xs:documentation>가운데 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="DISTRIBUTE">
                                <xs:annotation><xs:documentation>배분 정렬</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="DISTRIBUTE_SPACE">
                                <xs:annotation><xs:documentation>나눔 정렬 (공백에만 배분)</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="vertical" use="required">
                    <xs:annotation>
                        <xs:documentation>수직 정렬</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="BASELINE">
                                <xs:annotation><xs:documentation>글자 기준선</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="TOP">
                                <xs:annotation><xs:documentation>위</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER">
                                <xs:annotation><xs:documentation>가운데</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BOTTOM">
                                <xs:annotation><xs:documentation>아래</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="heading">
            <xs:annotation>
                <xs:documentation>문단 머리 번호/글머리표</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="type" use="required">
                    <xs:annotation>
                        <xs:documentation>문단 머리 모양 종류</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="NONE">
                                <xs:annotation><xs:documentation>없음</xs:documentation></xs:annotation>
                            </xs:enumeration>
                             <xs:enumeration value="OUTLINE">
                                <xs:annotation><xs:documentation>개요</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="NUMBER">
                                <xs:annotation><xs:documentation>번호</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BULLET">
                                <xs:annotation><xs:documentation>글머리표</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="idRef" type="xs:nonNegativeInteger" use="required">
                    <xs:annotation>
                        <xs:documentation>번호/글머리표 문단 모양 아이디 참조</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="level" use="required">
                    <xs:annotation>
                        <xs:documentation>수준</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:nonNegativeInteger"/>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="breakSetting">
            <xs:annotation>
                <xs:documentation>줄 나눔 설정</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="breakLatinWord" use="required">
                    <xs:annotation>
                        <xs:documentation>라틴 문자의 줄나눔 단위</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="KEEP_WORD">
                                <xs:annotation><xs:documentation>단어</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="HYPHENATION">
                                <xs:annotation><xs:documentation>하이픈</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BREAK_WORD">
                                <xs:annotation><xs:documentation>글자</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="breakNonLatinWord" use="required">
                    <xs:annotation>
                        <xs:documentation>라틴 문자 이외의 문자의 줄나눔 단위</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                             <xs:enumeration value="KEEP_WORD">
                                <xs:annotation><xs:documentation>단어</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BREAK_WORD">
                                <xs:annotation><xs:documentation>글자</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="widowOrphan" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>고아/미망줄 보호 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="keepWithNext" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>다음 문단과 함께</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="keepLines" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>문단 보호 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="pageBreakBefore" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>문단 앞에서 항상 쪽나눔 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="lineWrap" use="required">
                    <xs:annotation>
                        <xs:documentation>줄바꿈 영역 사용 시의 형식</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                             <xs:enumeration value="BREAK">
                                <xs:annotation><xs:documentation>줄바꿈</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="SQUEEZE">
                                <xs:annotation><xs:documentation>자간을 조정하여 한 줄 유지</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="KEEP">
                                <xs:annotation><xs:documentation>내용에 따라 폭이 늘어남</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="margin">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="intent" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>들여쓰기/내어쓰기. 0보다 크면 들여쓰기, 0이면 보통, 0보다 작으면 내어쓰기.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="left" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>왼쪽 여백. 단위를 표기하지 않으면 hwpunit이고 표기하면 표기한 단위.</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="right" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>오른쪽 여백</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="prev" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>문단 간격 위</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="next" type="hc:HWPValue">
                        <xs:annotation>
                            <xs:documentation>문단 간격 아래</xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
        <xs:element name="lineSpacing">
            <xs:annotation>
                <xs:documentation>줄 간격</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="type" use="required">
                    <xs:annotation>
                        <xs:documentation>줄간격 종류</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="PERCENT">
                                <xs:annotation><xs:documentation>글자에 따라</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="FIXED">
                                <xs:annotation><xs:documentation>고정값</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BETWEEN_LINES">
                                <xs:annotation><xs:documentation>여백만 지정</xs:documentation></xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="AT_LEAST">
                                <xs:annotation><xs:documentation>최소</xs:documentation></xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="value" type="xs:integer" use="required">
                    <xs:annotation>
                        <xs:documentation>줄 간격 값. type이 PERCENT이면 0%-500%로 제한</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="unit">
                    <xs:annotation>
                        <xs:documentation>줄 간격 값의 단위</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="CHAR"/>
                            <xs:enumeration value="HWPUNIT"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="border">
            <xs:annotation>
                <xs:documentation>문단 테두리</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
                    <xs:annotation>
                        <xs:documentation>테두리/배경 모양 아이디</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetLeft" type="xs:integer" default="0">
                    <xs:annotation>
                        <xs:documentation>문단 테두리 왼쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetRight" type="xs:integer" default="0">
                     <xs:annotation>
                        <xs:documentation>문단 테두리 오른쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetTop" type="xs:integer" default="0">
                     <xs:annotation>
                        <xs:documentation>문단 테두리 위쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="offsetBottom" type="xs:integer" default="0">
                     <xs:annotation>
                        <xs:documentation>문단 테두리 아래쪽 간격. 단위는 hwpunit</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="connect" type="xs:boolean" default="false">
                    <xs:annotation>
                        <xs:documentation>문단 테두리 연결 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="ignoreMargin" type="xs:boolean" default="false">
                    <xs:annotation>
                        <xs:documentation>문단 테두리 여백 무시 여부</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
        <xs:element name="autoSpacing">
            <xs:annotation>
                <xs:documentation>문단 자동 간격 조정 설정</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="eAsianEng" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>아시아/영어 간격을 자동 조절</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="eAsianNum" type="xs:boolean" use="required">
                    <xs:annotation>
                        <xs:documentation>아시아/숫자 간격을 자동 조절</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="tabPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>탭 정의 아이디 참조</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="condense">
        <xs:annotation>
            <xs:documentation>줄 나눔 최소값. 단위는 %</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:minInclusive value="0"/>
                <xs:maxInclusive value="75"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="fontLineHeight" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>글꼴에 어울리는 줄 높이 사용 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="snapToGrid" type="xs:boolean" default="true">
        <xs:annotation>
            <xs:documentation>편집 용지의 줄 격자 사용 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="suppressLineNumbers" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>줄 번호 건너뛰기</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="checked" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>체크 글머리표 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="StyleType">
    <xs:annotation>
        <xs:documentation>스타일 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="type" use="required">
        <xs:annotation>
            <xs:documentation>스타일 타입</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="PARA">
                    <xs:annotation><xs:documentation>문단 스타일</xs:documentation></xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="CHAR">
                    <xs:annotation><xs:documentation>글자 스타일</xs:documentation></xs:annotation>
                </xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="name" type="xs:string" use="required">
        <xs:annotation>
            <xs:documentation>한글 스타일 이름. 한글 윈도우에서는 한글 스타일 이름.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="engName" type="xs:string">
        <xs:annotation>
            <xs:documentation>영문 스타일 이름</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="paraPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>문단 모양 아이디 참조. 스타일의 종류가 문단인 경우 지정해야 함.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>글자 모양 아이디 참조. 스타일의 종류가 글자인 경우 지정해야 함.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="nextStyleIDRef" type="xs:nonNegativeInteger">
        <xs:annotation>
            <xs:documentation>다음 스타일 아이디 참조. 문단 스타일에서 사용자가 리턴키를 입력하여 다음 문단으로 이동하였을 때 적용될 문단 스타일을 지정한다.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="langID" type="xs:unsignedShort">
        <xs:annotation>
            <xs:documentation>언어 아이디</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lockForm" type="xs:boolean" default="false">
        <xs:annotation>
            <xs:documentation>양식 모드에서 Style 보호하기 여부</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="MemoShapeType">
    <xs:annotation>
        <xs:documentation>메모 모양 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
    <xs:attribute name="width" type="xs:nonNegativeInteger" use="required">
        <xs:annotation>
            <xs:documentation>메모가 보이는 너비</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lineWidth" type="xs:string">
        <xs:annotation>
            <xs:documentation>메모의 라인 굵기</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lineType" type="hc:LineType2" use="required">
        <xs:annotation>
            <xs:documentation>메모의 선 종류</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="lineColor" type="hc:RGBColorType" use="required">
        <xs:annotation>
            <xs:documentation>메모의 선 색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="fillColor" type="hc:RGBColorType" use="required">
        <xs:annotation>
            <xs:documentation>메모 배경색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="activeColor" type="hc:RGBColorType" use="required">
        <xs:annotation>
            <xs:documentation>메모가 활성화되었을 때 색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="memoType">
        <xs:annotation>
            <xs:documentation>메모 변경 추적을 위한 속성</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="NORMAL"/>
                <xs:enumeration value="USER_INSERT"/>
                <xs:enumeration value="USER_DELETE"/>
                <xs:enumeration value="USER_UPDATE"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="CompatibleDocumentType">
    <xs:annotation>
        <xs:documentation>호환 문서 정보</xs:documentation>
    </xs:annotation>
    <xs:sequence>
        <xs:element name="layoutCompatibility">
             <xs:complexType>
                <xs:sequence>
                    <xs:element name="applyExtensionCharCompose" minOccurs="0"/>
                    <xs:element name="doNotAlignParagraphSpacingAtGrid" minOccurs="0"/>
                    <xs:element name="doNotAdjustWordSpacingInJustify" minOccurs="0"/>
                    <xs:element name="doNotApplyAsiaFontToParagraphLeading" minOccurs="0"/>
                    <xs:element name="doNotAdjustLineSpacingAtFont" minOccurs="0"/>
                    <xs:element name="doNotAdjustBaselineAtFont" minOccurs="0"/>
                    <xs:element name="doNotApplyParagraphLeading" minOccurs="0"/>
                    <xs:element name="doNotAdjustFragmentOfWord" minOccurs="0"/>
                    <xs:element name="adjustBaselineOfAsiaFont" minOccurs="0"/>
                    <xs:element name="doNotAdjustLastLineInJustify" minOccurs="0"/>
                    <xs:element name="doNotAdjustLineSpacingAtGrid" minOccurs="0"/>
                    <xs:element name="doNotAdjustBetweenLines" minOccurs="0"/>
                    <xs:element name="doNotAdjustFirstLineLeadingAtPage" minOccurs="0"/>
                    <xs:element name="doNotAdjustBetweenLinesAtPage" minOccurs="0"/>
                    <xs:element name="doNotBalanceHalfCharAndFullChar" minOccurs="0"/>
                    <xs:element name="doNotApplyUnderlineForSpace" minOccurs="0"/>
                    <xs:element name="doNotApplyBoldToSpace" minOccurs="0"/>
                    <xs:element name="doNotAdjustBlankAtWord" minOccurs="0"/>
                    <xs:element name="doNotAdjustWidthAtUnderline" minOccurs="0"/>
                    <xs:element name="doNotAdjustWidthAtStrike" minOccurs="0"/>
                    <xs:element name="doNotAdjustWidthAtOutline" minOccurs="0"/>
                    <xs:element name="doNotApplyCharSpacingAtLastChar" minOccurs="0"/>
                    <xs:element name="doNotSpreadAtTab" minOccurs="0"/>
                    <xs:element name="doNotAdjustBaselineAtTop" minOccurs="0"/>
                    <xs:element name="doNotAdjustSpacingAtNumber" minOccurs="0"/>
                    <xs:element name="doNotApplySmartTag" minOccurs="0"/>
                    <xs:element name="doNotApplyShapeComment" minOccurs="0"/>
                    <xs:element name="doNotApplyHyperlink" minOccurs="0"/>
                    <xs:element name="overlapBothAllowOverlap" minOccurs="0"/>
                    <xs:element name="doNotApplyVertOffsetOfForward" minOccurs="0"/>
                    <xs:element name="extendVertLimitToPageMargins" minOccurs="0"/>
                    <xs:element name="doNotHoldAnchorOfTable" minOccurs="0"/>
                    <xs:element name="doNotFormattingAtBeneathAnchor" minOccurs="0"/>
                    <xs:element name="adjustBaselineOfObjectToBottom" minOccurs="0"/>
                    <xs:element name="doNotApplyExtensionCharCompose" minOccurs="0"/>
                </xs:sequence>
             </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="targetProgram" use="required">
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="HWP201X"/>
                <xs:enumeration value="HWP200X"/>
                <xs:enumeration value="MS_WORD"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
</xs:complexType>

<xs:complexType name="TrackChange">
    <xs:annotation>
        <xs:documentation>변경 추적 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="type" type="hc:TrackChangeType"/>
    <xs:attribute name="date" type="xs:dateTime"/>
    <xs:attribute name="authorID" type="xs:nonNegativeInteger"/>
    <xs:attribute name="charShapeID" type="xs:nonNegativeInteger"/>
    <xs:attribute name="paraShapeID" type="xs:nonNegativeInteger"/>
    <xs:attribute name="hide" type="xs:boolean" use="required"/>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
</xs:complexType>

<xs:complexType name="TrackChangeAuthor">
    <xs:annotation>
        <xs:documentation>변경 추적 사용자 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="name" type="xs:string"/>
    <xs:attribute name="mark" type="xs:boolean"/>
    <xs:attribute name="color" type="hc:RGBColorType"/>
    <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
</xs:complexType>
(Body.xml.xsd 시작)
code
Xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
```
           xmlns:hp="http://www.owpml.org/owpml/2024/paragraph"
           xmlns:hc="http://www.owpml.org/owpml/2024/core"
           targetNamespace="http://www.owpml.org/owpml/2024/paragraph"
           elementFormDefault="qualified">

```xml
    <xs:import namespace="http://www.owpml.org/owpml/2024/core" schemaLocation="HWPMLCore.xsd"/>
    <xs:import namespace="http://www.w3.org/XML/1998/namespace" schemaLocation="http://www.w3.org/2001/xml.xsd"/>
```
    
    <xs:complexType name="SectionType">
        <xs:sequence>
            <xs:element name="p" type="hp:PType" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    
    <xs:complexType name="ParaListType">
        <xs:sequence>
            <xs:element name="p" type="hp:PType" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="textDirection" default="HORIZONTAL">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="HORIZONTAL"/>
                    <xs:enumeration value="VERTICAL"/>
                    <xs:enumeration value="VERTICALALL">
                        <xs:annotation><xs:documentation>영문 눕힘</xs:documentation></xs:annotation>
                    </xs:enumeration>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="lineWrap" default="BREAK">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="BREAK"/>
                    <xs:enumeration value="SQUEEZE"/>
                    <xs:enumeration value="KEEP"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="vertAlign" default="TOP"/>
    </xs:complexType>
    
    <xs:element name="sec" type="hp:SectionDefinitionType">
        <xs:annotation>
            <xs:documentation>HWPML 문서의 구역</xs:documentation>
        </xs:annotation>
    </xs:element>

    <xs:complexType name="PType">
        <xs:choice minOccurs="0" maxOccurs="unbounded">
            <xs:element name="run">
                <xs:complexType>
                    <xs:choice minOccurs="0" maxOccurs="unbounded">
                        <xs:element name="ctrl">
                            <xs:complexType>
                                <xs:choice minOccurs="1" maxOccurs="unbounded">
                                    <xs:element name="colPr" type="hp:ColumnDefType" minOccurs="0"/>
                                    <xs:element name="fieldBegin">
                                        <xs:complexType>
                                            <xs:sequence minOccurs="0">
                                                <xs:element name="parameters" type="hp:ParameterList" minOccurs="0"/>
                                                <xs:element name="subList" type="hp:ParaListType" minOccurs="0"/>
                                                <xs:element name="metaTag" type="hc:MetaTagType" minOccurs="0"/>
                                            </xs:sequence>
                                            <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
                                            <xs:attribute name="type" type="hp:FieldType" use="required"/>
                                            <xs:attribute name="name" type="xs:string"/>
                                            <xs:attribute name="editable" type="xs:boolean" default="true"/>
                                            <xs:attribute name="dirty" type="xs:boolean" default="false"/>
                                            <xs:attribute name="zorder" type="xs:integer"/>
                                            <xs:attribute name="fieldid" type="xs:nonNegativeInteger"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="fieldEnd">
                                        <xs:complexType>
                                            <xs:attribute name="beginIDRef" type="xs:nonNegativeInteger" use="required"/>
                                            <xs:attribute name="fieldid" type="xs:unsignedInt"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="bookmark">
                                        <xs:complexType>
                                            <xs:attribute name="name" type="xs:string"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="header" type="hp:HeaderFooterType"/>
                                    <xs:element name="footer" type="hp:HeaderFooterType"/>
                                    <xs:element name="footNote" type="hp:NoteType"/>
                                    <xs:element name="endNote" type="hp:NoteType"/>
                                    <xs:element name="autoNum" type="hp:AutoNumNewNumType"/>
                                    <xs:element name="newNum" type="hp:AutoNumNewNumType"/>
                                    <xs:element name="pageNumCtrl">
                                        <xs:complexType>
                                            <xs:attribute name="pageStartsOn" default="BOTH">
                                                <xs:simpleType>
                                                    <xs:restriction base="xs:string">
                                                        <xs:enumeration value="BOTH"/>
                                                        <xs:enumeration value="EVEN"/>
                                                        <xs:enumeration value="ODD"/>
                                                    </xs:restriction>
                                                </xs:simpleType>
                                            </xs:attribute>
                                            <!-- ... 기타 pageNumCtrl 속성들 ... -->
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="pageHiding">
                                        <xs:complexType>
                                            <xs:attribute name="hideHeader" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideFooter" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideMasterPage" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideBorder" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hideFill" type="xs:boolean" default="false"/>
                                            <xs:attribute name="hidePageNum" type="xs:boolean" default="false"/>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="pageNum">
                                        <xs:complexType>
                                            <xs:attribute name="pos" default="TOP_LEFT">
                                                <xs:annotation><xs:documentation>쪽 번호 위치</xs:documentation></xs:annotation>
                                                <xs:simpleType>
                                                    <xs:restriction base="xs:string">
                                                        <xs:enumeration value="NONE"/>
                                                        <xs:enumeration value="TOP_LEFT"/>
                                                        <xs:enumeration value="TOP_CENTER"/>
                                                        <xs:enumeration value="TOP_RIGHT"/>
                                                        <xs:enumeration value="BOTTOM_LEFT"/>
                                                        <xs:enumeration value="BOTTOM_CENTER"/>
                                                        <xs:enumeration value="BOTTOM_RIGHT"/>
                                                        <xs:enumeration value="OUTSIDE_TOP"/>
                                                        <xs:enumeration value="OUTSIDE_BOTTOM"/>
                                                        <xs:enumeration value="INSIDE_TOP"/>
                                                        <xs:enumeration value="INSIDE_BOTTOM"/>
                                                    </xs:restriction>
                                                </xs:simpleType>
                                            </xs:attribute>
                                            <xs:attribute name="formatType" type="hc:NumberType" default="DIGIT">
                                                <xs:annotation><xs:documentation>쪽 번호 형식</xs:documentation></xs:annotation>
                                            </xs:attribute>
                                            <xs:attribute name="sideChar" type="xs:string" default="-">
                                                 <xs:annotation><xs:documentation>앞뒤 장식 문자 넣기</xs:documentation></xs:annotation>
                                            </xs:attribute>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="indexmark">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="firstKey"/>
                                                <xs:element name="secondKey"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                    <xs:element name="hiddenComment">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="subList" type="hp:ParaListType"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:choice>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="t">
                            <!-- ... t(text) element definition ... -->
                        </xs:element>
                        <xs:element name="markpenBegin">
                            <xs:complexType>
                                <xs:attribute name="color" type="hc:RGBColorType"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="markpenEnd" minOccurs="0"/>
                        <xs:element name="titleMark">
                             <xs:complexType>
                                <xs:attribute name="ignore" type="xs:boolean" default="false"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="tab" minOccurs="0">
                             <xs:annotation><xs:documentation>Attribute 'width' 단위는 hwpunit</xs:documentation></xs:annotation>
                             <xs:complexType>
                                <xs:attribute name="width" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="leader" type="hc:LineType2"/>
                                <xs:attribute name="type">
                                    <xs:annotation><xs:documentation>탭의 종류</xs:documentation></xs:annotation>
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="LEFT"><xs:annotation><xs:documentation>왼쪽</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="RIGHT"><xs:annotation><xs:documentation>오른쪽</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="CENTER"><xs:annotation><xs:documentation>가운데</xs:documentation></xs:annotation></xs:enumeration>
                                            <xs:enumeration value="DECIMAL"><xs:annotation><xs:documentation>소수점</xs:documentation></xs:annotation></xs:enumeration>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="lineBreak" minOccurs="0"/>
                        <xs:element name="hyphen" minOccurs="0"/>
                        <xs:element name="nbspace" minOccurs="0"/>
                        <xs:element name="fwspace" minOccurs="0"/>
                        <xs:element name="insertBegin" type="hp:TrackChangeTag"/>
                        <xs:element name="insertEnd" type="hp:TrackChangeTag"/>
                        <xs:element name="deleteBegin" type="hp:TrackChangeTag"/>
                        <xs:element name="deleteEnd" type="hp:TrackChangeTag"/>
                        <xs:element name="tbl">
                            <xs:complexType>
                                <xs:attribute name="charStyleIDRef" type="xs:nonNegativeInteger"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="drawing" type="hp:ShapeType"/>
                        <xs:element name="pic" type="hp:PictureType"/>
                        <xs:element name="ole" type="hp:OLEType"/>
                        <xs:element name="container" type="hp:ContainerType"/>
                        <xs:element name="equation" type="hp:EquationType"/>
                        <xs:element name="line" type="hp:LineType"/>
                        <xs:element name="rect" type="hp:RectangleType"/>
                        <xs:element name="ellipse" type="hp:EllipseType"/>
                        <xs:element name="arc" type="hp:ArcType"/>
                        <xs:element name="polygon" type="hp:PolygonType"/>
                        <xs:element name="curve" type="hp:CurveType"/>
                        <xs:element name="connectLine" type="hp:ConnectLineType"/>
                        <xs:element name="textart">
                            <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractDrawingObjectType">
                                        <xs:sequence>
                                            <xs:element name="pt0" type="hc:PointType"/>
                                            <xs:element name="pt1" type="hc:PointType"/>
                                            <xs:element name="pt2" type="hc:PointType"/>
                                            <xs:element name="pt3" type="hc:PointType"/>
                                            <xs:element name="textartPr">
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="shadow" type="hp:ShadowType"/>
                                                    </xs:sequence>
                                                    <xs:attribute name="fontName" type="xs:string"/>
                                                    <xs:attribute name="fontStyle" type="xs:string"/>
                                                    <xs:attribute name="fontType" default="TTF">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="TTF"/>
                                                                <xs:enumeration value="HFT"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="textShape" default="REGULAR">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="REGULAR"/>
                                                                <xs:enumeration value="PARALLELOGRAM"/>
                                                                <xs:enumeration value="INVERTED_PARALLELOGRAM"/>
                                                                <xs:enumeration value="UPWARD_CASCADE"/>
                                                                <xs:enumeration value="DOWNWARD_CASCADE"/>
                                                                <xs:enumeration value="INVERTED_UPWARD_CASCADE"/>
                                                                <xs:enumeration value="INVERTED_DOWNWARD_CASCADE"/>
                                                                <xs:enumeration value="REDUCE_RIGHT"/>
                                                                <xs:enumeration value="REDUCE_LEFT"/>
                                                                <xs:enumeration value="ISOSCELES_TRAPEZOID"/>
                                                                <xs:enumeration value="INVERTED_ISOSCELES_TRAPEZOID"/>
                                                                <xs:enumeration value="TOP_RIBBON_RECTANGLE"/>
                                                                <xs:enumeration value="BOTTOM_RIBBON_RECTANGLE"/>
                                                                <xs:enumeration value="CHEVRON"/>
                                                                <xs:enumeration value="BOW_TIE"/>
                                                                <xs:enumeration value="HEXAGON"/>
                                                                <xs:enumeration value="WAVE1"/>
                                                                <xs:enumeration value="WAVE2"/>
                                                                <xs:enumeration value="WAVE3"/>
                                                                <xs:enumeration value="WAVE4"/>
                                                                <xs:enumeration value="LEFT_TILT_CYLINDER"/>
                                                                <xs:enumeration value="RIGHT_TILT_CYLINDER"/>
                                                                <xs:enumeration value="BOTTOM_WIDE_CYLINDER"/>
                                                                <xs:enumeration value="TOP_WIDE_CYLINDER"/>
                                                                <xs:enumeration value="THIN_CURVE_UP1"/>
                                                                <xs:enumeration value="THIN_CURVE_UP2"/>
                                                                <xs:enumeration value="THIN_CURVE_DOWN1"/>
                                                                <xs:enumeration value="THIN_CURVE_DOWN2"/>
                                                                <xs:enumeration value="INVERSED_FINGERNAIL"/>
                                                                <xs:enumeration value="FINGERNAIL"/>
                                                                <xs:enumeration value="GINKO_LEAF1"/>
                                                                <xs:enumeration value="GINKO_LEAF2"/>
                                                                <xs:enumeration value="INFLATE_RIGHT"/>
                                                                <xs:enumeration value="INFLATE_LEFT"/>
                                                                <xs:enumeration value="INFLATE_TOP_CONVEX"/>
                                                                <xs:enumeration value="INFLATE_BOTTOM_CONCAVE"/>
                                                                <xs:enumeration value="DEFLATE_TOP1"/>
                                                                <xs:enumeration value="DEFLATE_BOTTOM"/>
                                                                <xs:enumeration value="DEFLATE"/>
                                                                <xs:enumeration value="INFLATE"/>
                                                                <xs:enumeration value="INFLATE_TOP"/>
                                                                <xs:enumeration value="INFLATE_BOTTOM"/>
                                                                <xs:enumeration value="RECTANGLE"/>
                                                                <xs:enumeration value="LEFT_CYLINDER"/>
                                                                <xs:enumeration value="CYLINDER"/>
                                                                <xs:enumeration value="RIGHT_CYLINDER"/>
                                                                <xs:enumeration value="CIRCLE"/>
                                                                <xs:enumeration value="CURVE_DOWN"/>
                                                                <xs:enumeration value="ARCH_UP"/>
                                                                <xs:enumeration value="ARCH_DOWN"/>
                                                                <xs:enumeration value="SINGLE_LINE_CIRCLE1"/>
                                                                <xs:enumeration value="SINGLE_LINE_CIRCLE2"/>
                                                                <xs:enumeration value="TRIPLE_LINE_CIRCLE1"/>
                                                                <xs:enumeration value="TRIPLE_LINE_CIRCLE2"/>
                                                                <xs:enumeration value="DOUBLE_LINE_CIRCLE"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="lineSpacing" default="120">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:nonNegativeInteger">
                                                                <xs:minInclusive value="50"/>
                                                                <xs:maxInclusive value="500"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="charSpacing" default="100">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:nonNegativeInteger">
                                                                <xs:minInclusive value="-50"/>
                                                                <xs:maxInclusive value="500"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                    <xs:attribute name="align" default="LEFT">
                                                        <xs:simpleType>
                                                            <xs:restriction base="xs:string">
                                                                <xs:enumeration value="LEFT"/>
                                                                <xs:enumeration value="RIGHT"/>
                                                                <xs:enumeration value="CENTER"/>
                                                                <xs:enumeration value="FULL"/>
                                                                <xs:enumeration value="TABLE"/>
                                                            </xs:restriction>
                                                        </xs:simpleType>
                                                    </xs:attribute>
                                                </xs:complexType>
                                            </xs:element>
                                            <xs:element name="outline">
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="pt" type="hc:PointType" minOccurs="0" maxOccurs="unbounded"/>
                                                    </xs:sequence>
                                                    <xs:attribute name="cnt" type="xs:nonNegativeInteger"/>
                                                </xs:complexType>
                                            </xs:element>
                                        </xs:sequence>
                                        <xs:attribute name="text" type="xs:string"/>
                                    </xs:extension>
                                </xs:complexContent>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="compose">
                            <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="charPr" maxOccurs="unbounded">
                                        <xs:complexType>
                                            <xs:attribute name="prIDRef" type="xs:nonNegativeInteger"/>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:sequence>
                                <xs:attribute name="circleType" default="SHAPE_CIRCLE">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="CHAR"/>
                                            <xs:enumeration value="SHAPE_CIRCLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_CIRCLE"/>
                                            <xs:enumeration value="SHAPE_RECTANGLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_RECTANGLE"/>
                                            <xs:enumeration value="SHAPE_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_LIGHT"/>
                                            <xs:enumeration value="SHAPE_RHOMBUS"/>
                                            <xs:enumeration value="SHAPE_REVERSAL_RHOMBUS"/>
                                            <xs:enumeration value="SHAPE_EMPTY_CIRCULATE_TRIANGLE"/>
                                            <xs:enumeration value="SHAPE_THICK_CIRCULATE_TRIANGLE"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="charSz" type="xs:integer">
                                     <xs:annotation><xs:documentation>글자 크기 비율 (%)</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="composeType">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="SPREAD"/>
                                            <xs:enumeration value="OVERLAP"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="charprCnt" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="composeText" type="xs:string"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="dutmal">
                             <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="mainText"/>
                                    <xs:element name="subText"/>
                                </xs:sequence>
                                <xs:attribute name="pos" default="TOP">
                                     <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="TOP"/>
                                            <xs:enumeration value="BOTTOM"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                                <xs:attribute name="szRatio" type="xs:positiveInteger"/>
                                <xs:attribute name="option" type="xs:unsignedInt" default="47"/>
                                <xs:attribute name="styleIDRef" type="xs:nonNegativeInteger"/>
                                <xs:attribute name="align" default="CENTER">
                                    <xs:simpleType>
                                        <xs:restriction base="xs:string">
                                            <xs:enumeration value="JUSTIFY"/>
                                            <xs:enumeration value="LEFT"/>
                                            <xs:enumeration value="RIGHT"/>
                                            <xs:enumeration value="CENTER"/>
                                            <xs:enumeration value="DISTRIBUTE"/>
                                            <xs:enumeration value="DISTRIBUTE_SPACE"/>
                                        </xs:restriction>
                                    </xs:simpleType>
                                </xs:attribute>
                             </xs:complexType>
                        </xs:element>
                        <xs:element name="btn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="radioBtn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="checkBtn" type="hp:AbstractButtonObjectType"/>
                        <xs:element name="comboBox" type="hp:ComboBoxType"/>
                        <xs:element name="listBox" type="hp:ListBoxType"/>
                        <xs:element name="edit" type="hp:EditType"/>
                        <xs:element name="scrollBar" type="hp:ScrollBarType"/>
                        <xs:element name="video">
                             <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractShapeComponentType">
                                        <xs:attribute name="videoType" use="required">
                                             <xs:annotation><xs:documentation>비디오 종류 (로컬/웹)</xs:documentation></xs:annotation>
                                             <xs:simpleType>
                                                <xs:restriction base="xs:string">
                                                    <xs:enumeration value="LOCAL">
                                                        <xs:annotation><xs:documentation>로컬 컴퓨터의 동영상</xs:documentation></xs:annotation>
                                                    </xs:enumeration>
                                                    <xs:enumeration value="WEB">
                                                        <xs:annotation><xs:documentation>웹 링크 동영상</xs:documentation></xs:annotation>
                                                    </xs:enumeration>
                                                </xs:restriction>
                                            </xs:simpleType>
                                        </xs:attribute>
                                        <xs:attribute name="fileIDRef" type="xs:string" use="optional"/>
                                        <xs:attribute name="imageIDRef" type="xs:string" use="optional"/>
                                        <xs:attribute name="tag" type="xs:string" use="optional"/>
                                    </xs:extension>
                                </xs:complexContent>
                             </xs:complexType>
                        </xs:element>
                        <xs:element name="chart">
                             <xs:complexType>
                                <xs:complexContent>
                                    <xs:extension base="hp:AbstractShapeObjectType">
                                        <xs:attribute name="version" type="xs:float"/>
                                        <xs:attribute name="chartIDRef" type="xs:string"/>
                                    </xs:extension>
                                </xs:complexContent>
                             </xs:complexType>
                        </xs:element>
                    </xs:choice>
                    <xs:attribute name="charPrIDRef" type="xs:nonNegativeInteger"/>
                    <xs:attribute name="charTcid" type="xs:nonNegativeInteger" use="optional"/>
                </xs:complexType>
            </xs:element>
        </xs:choice>
        <xs:attribute name="id" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="paraPrIDRef" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="styleIDRef" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="pageBreak" type="xs:boolean" default="false"/>
        <xs:attribute name="columnBreak" type="xs:boolean" default="false"/>
        <xs:attribute name="merged" type="xs:boolean" default="false"/>
        <xs:attribute name="paraTcid" type="xs:nonNegativeInteger" use="optional"/>
    </xs:complexType>
    
    <xs:complexType name="SectionDefinitionType">
        <xs:sequence>
            <xs:element name="startNum" minOccurs="0">
                <xs:annotation><xs:documentation>시작 번호</xs:documentation></xs:annotation>
                <xs:complexType>
                     <xs:attribute name="pageStartsOn" default="BOTH">
                        <xs:annotation><xs:documentation>구역 나눔을 한 용지가 생길 때 페이지 번호 적용 옵션</xs:documentation></xs:annotation>
                        <xs:simpleType>
                            <xs:restriction base="xs:string">
                                <xs:enumeration value="BOTH"/>
                                <xs:enumeration value="EVEN"/>
                                <xs:enumeration value="ODD"/>
                            </xs:restriction>
                        </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="page" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>페이지 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="pic" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>그림 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="tbl" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>표 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="equation" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>수식 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="grid" minOccurs="0">
                <xs:annotation><xs:documentation>격자 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                    <xs:attribute name="lineGrid" type="xs:nonNegativeInteger" default="0">
                        <xs:annotation><xs:documentation>줄 격자. 0이면 현재 글꼴을 한 줄로 함</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="charGrid" type="xs:nonNegativeInteger" default="0">
                         <xs:annotation><xs:documentation>글자 격자. 0이면 현재 글꼴을 한 글자로 함</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="wongojiFormat" type="xs:boolean" default="true">
                        <xs:annotation><xs:documentation>원고지 형식 여부</xs:documentation></xs:annotation>
                    </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="visibility" minOccurs="0">
                 <xs:annotation><xs:documentation>감추기/보여주기 설정</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:attribute name="hideFirstHeader" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 머리말 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstFooter" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 꼬리말 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstMasterPage" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 바탕쪽 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="border" type="hp:VisibilityValue"/>
                     <xs:attribute name="fill" type="hp:VisibilityValue"/>
                     <xs:attribute name="hideFirstPageNum" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 쪽번호 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="hideFirstEmptyLine" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>첫 쪽에만 빈 줄 감추기 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="showLineNumber" type="xs:boolean" default="false">
                         <xs:annotation><xs:documentation>줄 번호 표시 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="lineNumberShape" minOccurs="0">
                <xs:annotation><xs:documentation>줄 번호 모양</xs:documentation></xs:annotation>
                <xs:complexType>
                    <xs:attribute name="restartType" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>줄 번호 방식</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="countBy" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>번호 표시 간격</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="distance" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>본문과 번호 거리</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="startNumber" type="xs:unsignedInt">
                        <xs:annotation><xs:documentation>줄 번호 시작 번호</xs:documentation></xs:annotation>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="pagePr" minOccurs="0">
                <xs:annotation><xs:documentation>용지 설정</xs:documentation></xs:annotation>
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="margin">
                            <xs:complexType>
                                <xs:attributeGroup ref="hc:MarginAttributeGroup"/>
                                <xs:attribute name="header" type="xs:nonNegativeInteger" default="4252">
                                    <xs:annotation><xs:documentation>머리말 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="footer" type="xs:nonNegativeInteger" default="4252">
                                     <xs:annotation><xs:documentation>꼬리말 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="gutter" type="xs:nonNegativeInteger" default="0">
                                     <xs:annotation><xs:documentation>제본 여백</xs:documentation></xs:annotation>
                                </xs:attribute>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                    <xs:attribute name="landscape" default="NARROWLY">
                         <xs:annotation><xs:documentation>용지 방향</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                 <xs:enumeration value="WIDELY"/>
                                 <xs:enumeration value="NARROWLY"/>
                             </xs:restriction>
                         </xs:simpleType>
                    </xs:attribute>
                    <xs:attribute name="width" type="xs:positiveInteger" default="59528">
                         <xs:annotation><xs:documentation>용지 가로 크기. 단위는 HWPUNIT</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="height" type="xs:positiveInteger" default="84188">
                         <xs:annotation><xs:documentation>용지 세로 크기. 단위는 HWPUNIT</xs:documentation></xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="gutterType" default="LEFT_ONLY">
                         <xs:annotation><xs:documentation>제본 방식</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="LEFT_ONLY"/>
                                <xs:enumeration value="LEFT_RIGHT"/>
                                <xs:enumeration value="TOP_BOTTOM"/>
                             </xs:restriction>
                         </xs:simpleType>
                    </xs:attribute>
                </xs:complexType>
            </xs:element>
            <xs:element name="footNotePr" type="hp:FootNoteShapeType" minOccurs="0">
                 <xs:annotation><xs:documentation>각주 모양</xs:documentation></xs:annotation>
            </xs:element>
            <xs:element name="endNotePr" type="hp:EndNoteShapeType" minOccurs="0">
                 <xs:annotation><xs:documentation>미주 모양</xs:documentation></xs:annotation>
            </xs:element>
            <xs:element name="pageBorderFill" minOccurs="0" maxOccurs="3">
                 <xs:annotation><xs:documentation>쪽 테두리/배경 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:sequence>
                         <xs:element name="offset">
                            <xs:annotation><xs:documentation>테두리/배경 위치</xs:documentation></xs:annotation>
                            <xs:complexType>
                                <xs:attribute name="left" type="xs:nonNegativeInteger" default="1417">
                                    <xs:annotation><xs:documentation>왼쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="right" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>오른쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="top" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>위쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                                <xs:attribute name="bottom" type="xs:nonNegativeInteger" default="1417">
                                     <xs:annotation><xs:documentation>아래쪽 간격. 단위는 HWPUNIT.</xs:documentation></xs:annotation>
                                </xs:attribute>
                            </xs:complexType>
                         </xs:element>
                     </xs:sequence>
                     <xs:attribute name="type">
                         <xs:annotation><xs:documentation>적용 쪽</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="BOTH"><xs:annotation><xs:documentation>양쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="EVEN"><xs:annotation><xs:documentation>짝수쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="ODD"><xs:annotation><xs:documentation>홀수쪽</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
                        <xs:annotation><xs:documentation>테두리/배경 아이디 참조</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="textBorder">
                        <xs:annotation><xs:documentation>테두리 위치 기준</xs:documentation></xs:annotation>
                        <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="CONTENT"><xs:annotation><xs:documentation>본문 기준</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="PAPER"><xs:annotation><xs:documentation>종이 기준</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="headerInside" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>머리말 포함 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="footerInside" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>꼬리말 포함 여부</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="fillArea">
                         <xs:annotation><xs:documentation>채울 영역</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="PAPER"><xs:annotation><xs:documentation>종이</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="PAGE"><xs:annotation><xs:documentation>쪽</xs:documentation></xs:annotation></xs:enumeration>
                                <xs:enumeration value="BORDER"><xs:annotation><xs:documentation>테두리</xs:documentation></xs:annotation></xs:enumeration>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
            <xs:element name="masterpage" minOccurs="0" maxOccurs="unbounded">
                 <xs:annotation><xs:documentation>바탕쪽 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                    <xs:attribute name="idRef" type="xs:string" use="required"/>
                 </xs:complexType>
            </xs:element>
            <xs:element name="presentation" minOccurs="0">
                 <xs:annotation><xs:documentation>프레젠테이션 정보</xs:documentation></xs:annotation>
                 <xs:complexType>
                     <xs:sequence>
                         <xs:element name="fillBrush" type="hc:FillBrushType" minOccurs="0">
                            <xs:annotation><xs:documentation>배경 정보</xs:documentation></xs:annotation>
                         </xs:element>
                     </xs:sequence>
                     <xs:attribute name="effect">
                         <xs:annotation><xs:documentation>화면 전환 효과</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="none"/>
                                <xs:enumeration value="serLen"/>
                                <xs:enumeration value="serRight"/>
                                <xs:enumeration value="serUp"/>
                                <xs:enumeration value="serDown"/>
                                <xs:enumeration value="rectOut"/>
                                <xs:enumeration value="rectIn"/>
                                <xs:enumeration value="windLeft"/>
                                <xs:enumeration value="windRight"/>
                                <xs:enumeration value="blindUp"/>
                                <xs:enumeration value="blindDown"/>
                                <xs:enumeration value="curtionHorzOut"/>
                                <xs:enumeration value="curtionHorzIn"/>
                                <xs:enumeration value="curtionVertOut"/>
                                <xs:enumeration value="curtionVertIn"/>
                                <xs:enumeration value="moveLeft"/>
                                <xs:enumeration value="moveRight"/>
                                <xs:enumeration value="moveUp"/>
                                <xs:enumeration value="moveDown"/>
                                <xs:enumeration value="random"/>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="soundIDRef">
                         <xs:simpleType><xs:restriction base="xs:string"/></xs:simpleType>
                     </xs:attribute>
                     <xs:attribute name="invertText" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>글자 반전</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="autoShow" type="xs:boolean" default="false">
                        <xs:annotation><xs:documentation>자동 화면 전환</xs:documentation></xs:annotation>
                     </xs:attribute>
                     <xs:attribute name="showTime" type="xs:nonNegativeInteger"/>
                     <xs:attribute name="applyTo">
                        <xs:annotation><xs:documentation>적용 범위</xs:documentation></xs:annotation>
                         <xs:simpleType>
                             <xs:restriction base="xs:string">
                                <xs:enumeration value="WholeDoc"/>
                                <xs:enumeration value="NewSection"/>
                             </xs:restriction>
                         </xs:simpleType>
                     </xs:attribute>
                 </xs:complexType>
            </xs:element>
        </xs:sequence>
        <xs:attribute name="id" type="xs:string" use="required"/>
        <xs:attribute name="textDirection" use="optional" default="HORIZONTAL">
             <xs:annotation><xs:documentation>텍스트 방향</xs:documentation></xs:annotation>
             <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="HORIZONTAL"/>
                    <xs:enumeration value="VERTICAL"/>
                    <xs:enumeration value="VERTICALALL">
                        <xs:annotation><xs:documentation>영문 눕힘</xs:documentation></xs:annotation>
                    </xs:enumeration>
                </xs:restriction>
             </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="spaceColumns" type="xs:integer" default="0">
             <xs:annotation><xs:documentation>다단 편집에서 서로 다른 단 사이의 간격</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="tabStopValue" type="xs:integer" default="0">
             <xs:annotation><xs:documentation>기본 탭 간격</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="tabStopUnit">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="CHAR"/>
                    <xs:enumeration value="HWPUNIT"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="outlineShapeIDRef" type="xs:nonNegativeInteger">
            <xs:annotation><xs:documentation>개요 번호 모양 아이디 참조</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="memoShapeIDRef" type="xs:nonNegativeInteger">
             <xs:annotation><xs:documentation>구역 내에서 사용되는 메모의 모양을 설정하기 위한 아이디 참조 값</xs:documentation></xs:annotation>
        </xs:attribute>
        <xs:attribute name="textVerticalWidthHead" type="xs:boolean" default="false">
            <xs:annotation><xs:documentation>세로쓰기 머리말</xs:documentation></xs:annotation>
        </xs:attribute>
    </xs:complexType>
</xs:schema>
---

## Source: okok1-4.md
<a name="source-okok14.md"></a>

KS X 6101 표준 문서 복원
338 / 414
KS X 6101:2024
code
Xml
```xml
<xs:annotation>
    <xs:documentation>구분선 굵기. 단위는 mm.</xs:documentation>
</xs:annotation>
</xs:attribute>
<xs:attribute name="color" type="hc:RGBColorType" default="000000">
    <xs:annotation>
        <xs:documentation>글자 색깔.</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="noteSpacing">
<xs:complexType>
<xs:attribute name="betweenNotes" type="xs:nonNegativeInteger" default="850">
    <xs:annotation>
        <xs:documentation>각주 사이 여백</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="belowLine" type="xs:nonNegativeInteger" default="567">
```
331
KSX 6101:2024
code
Xml
```xml
<xs:annotation>
        <xs:documentation>구분선 아래 여백</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="aboveLine" type="xs:nonNegativeInteger" default="567">
    <xs:annotation>
        <xs:documentation>구분선 위 여백</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="FootNoteShapeType">
<xs:annotation>
    <xs:documentation>각주 모양 및 속성</xs:documentation>
</xs:annotation>
<xs:complexContent>
<xs:extension base="hp:NoteShapeType">
<xs:sequence>
<xs:element name="numbering">
<xs:complexType>
<xs:attribute name="type" default="CONTINUOUS">
    <xs:annotation>
        <xs:documentation>번호 매기기 형식</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="CONTINUOUS">
                <xs:annotation>
                    <xs:documentation>앞 구역에 이어서</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ON_SECTION">
                <xs:annotation>
                    <xs:documentation>새 구역부터 새로 시작</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ON_PAGE">
                <xs:annotation>
                    <xs:documentation>쪽마다 새로 시작. 각주 전용</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
```
340 / 414
KSX 6101:2024
code
Xml
```xml
</xs:attribute>
<xs:attribute name="newNum" type="xs:positiveInteger" default="1">
    <xs:annotation>
        <xs:documentation>새 시작 번호. type이 ON_SECTION일 때만 사용한다.</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="placement">
<xs:complexType>
<xs:attribute name="place" default="EACH_COLUMN">
    <xs:annotation>
        <xs:documentation>한 페이지 내에서 각주를 다단에 어떻게 위치시킬지를 표시한다</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="EACH_COLUMN">
                <xs:annotation>
                    <xs:documentation>각 단에</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="MERGED_COLUMN">
                <xs:annotation>
                    <xs:documentation>단 합쳐서</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="RIGHT_MOST_COLUMN">
                <xs:annotation>
                    <xs:documentation>가장 오른쪽 단에</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="beneathText" type="xs:boolean" default="false">
    <xs:annotation>
        <xs:documentation>본문에 이어 바로 출력할지 여부</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
```
KSX 6101:2024
code
Xml
```xml
</xs:element>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="EndNoteShapeType">
<xs:annotation>
    <xs:documentation>미주 모양 및 속성</xs:documentation>
</xs:annotation>
<xs:complexContent>
<xs:extension base="hp:NoteShapeType">
<xs:sequence>
<xs:element name="numbering">
<xs:complexType>
<xs:attribute name="type" default="CONTINUOUS">
    <xs:annotation>
        <xs:documentation>번호 매기기 형식</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
```
341 / 414
code
Xml
```xml
<xs:restriction base="xs:string">
            <xs:enumeration value="CONTINUOUS">
                <xs:annotation>
                    <xs:documentation>앞 구역에 이어서</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ON_SECTION">
                <xs:annotation>
                    <xs:documentation>새 구역부터 새로 시작</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="newNum" type="xs:positiveInteger" default="1">
    <xs:annotation>
        <xs:documentation>새 시작 번호. type이 ON_SECTION일 때만 사용한다.</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="placement">
<xs:complexType>
<xs:attribute name="place" default="END_OF_DOCUMENT">
    <xs:annotation>
```
334
KSX 6101:2024
code
Xml
```xml
<xs:documentation>한 페이지 내에서 미주를 다단에 어떻게 위치시킬지를 표시한다</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="END_OF_DOCUMENT">
                <xs:annotation>
                    <xs:documentation>문서의 마지막</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="END_OF_SECTION">
                <xs:annotation>
                    <xs:documentation>구역의 마지막</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="beneathText" type="xs:boolean" default="false">
    <xs:annotation>
        <xs:documentation>본문에 이어 바로 출력할지 여부</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="AutoNumFormatType">
<xs:attribute name="type" type="hcf:NumberType2" default="DIGIT">
    <xs:annotation>
        <xs:documentation>번호 모양</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="userChar" type="xs:string">
    <xs:annotation>
        <xs:documentation>사용자 정의 문자</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="prefixChar" type="xs:string">
    <xs:annotation>
        <xs:documentation>앞 장식 문자</xs:documentation>
    </xs:annotation>
```
342 / 414
KSX 6101:2024
335
code
Xml
```xml
</xs:attribute>
<xs:attribute name="suffixChar" type="xs:string" default=".">
    <xs:annotation>
        <xs:documentation>뒤 장식 문자</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="supscript" type="xs:boolean" default="false">
    <xs:annotation>
        <xs:documentation>각주/미주 내용 중 번호 코드의 모양을 위 첨자 형식으로 할지 여부</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
<xs:simpleType name="VisibilityValue">
<xs:restriction base="xs:string">
<xs:enumeration value="HIDE_FIRST"/>
<xs:enumeration value="SHOW_FIRST"/>
<xs:enumeration value="SHOW_ALL"/>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="ColumnDefType">
<xs:sequence>
<xs:element name="colLine" minOccurs="0">
    <xs:annotation>
        <xs:documentation>단 구분선 모양</xs:documentation>
    </xs:annotation>
    <xs:complexType>
        <xs:attribute name="type" type="hc:LineType2" default="SOLID"/>
        <xs:attribute name="width" type="hc:LineWidth" default="0.12 mm"/>
        <xs:attribute name="color" type="hc:RGBColorType" default="000000"/>
    </xs:complexType>
</xs:element>
<xs:element name="colSz" minOccurs="0" maxOccurs="255">
    <xs:annotation>
        <xs:documentation>sameSize가 false일 때, 각 단의 크기 및 사이 간격</xs:documentation>
    </xs:annotation>
    <xs:complexType>
        <xs:attribute name="width" type="xs:positiveInteger"/>
        <xs:attribute name="gap" type="xs:nonNegativeInteger"/>
    </xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="id" type="xs:string" use="required"/>
<xs:attribute name="type" default="NEWSPAPER">
    <xs:annotation>
        <xs:documentation>단 종류</xs:documentation>
    </xs:annotation>
```
336
KSX 6101:2024
code
Xml
```xml
<xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="NEWSPAPER"/>
            <xs:enumeration value="BALANCED_NEWSPAPER"/>
            <xs:enumeration value="PARALLEL"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="layout" default="LEFT">
    <xs:annotation>
        <xs:documentation>단 방향 지정</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="LEFT"/>
            <xs:enumeration value="RIGHT"/>
            <xs:enumeration value="MIRROR"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="colCount" default="1">
    <xs:annotation>
        <xs:documentation>단 개수</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:positiveInteger">
            <xs:maxInclusive value="255"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="sameSize" type="xs:boolean" default="false">
    <xs:annotation>
        <xs:documentation>false: 단 너비 각각 지정. true: 단 너비 동일하게</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="sameGap" type="xs:nonNegativeInteger" default="0">
    <xs:annotation>
        <xs:documentation>단 사이 간격. sameSize가 true일 때만 지정.</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
<xs:complexType name="InsideMarginType">
<xs:attributeGroup ref="hc:MarginAttributeGroup"/>
</xs:complexType>
<xs:complexType name="LineShapeType">
<xs:attribute name="color" type="hc:RGBColorType"/>
```
KSX 6101:2024
code
Xml
```xml
<xs:attribute name="width" type="xs:nonNegativeInteger"/>
<xs:attribute name="style" type="hc:LineType" default="SOLID"/>
<xs:attribute name="endCap" default="FLAT">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="ROUND"/>
            <xs:enumeration value="FLAT"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="headStyle" type="hc:ArrowType" default="NORMAL"/>
<xs:attribute name="tailStyle" type="hc:ArrowType" default="NORMAL"/>
<xs:attribute name="headfill" type="xs:boolean" default="false"/>
<xs:attribute name="tailfill" type="xs:boolean" default="false"/>
<xs:attribute name="headSize" type="hc:ArrowSize" default="SMALL_SMALL"/>
<xs:attribute name="tailSize" type="hc:ArrowSize" default="SMALL_SMALL"/>
<xs:attribute name="outlineStyle" default="NORMAL">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="NORMAL"/>
            <xs:enumeration value="OUTER"/>
            <xs:enumeration value="INNER"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="alpha" type="xs:float"/>
</xs:complexType>
<xs:complexType name="EffectsType">
<xs:sequence>
<xs:element name="shadow" minOccurs="0">
<xs:complexType>
<xs:sequence>
<xs:element name="skew" type="hp:SkewType">
    <xs:annotation>
        <xs:documentation>기울이기 속성</xs:documentation>
    </xs:annotation>
</xs:element>
<xs:element name="scale" type="hp:ScaleType">
    <xs:annotation>
        <xs:documentation>크기 조절</xs:documentation>
    </xs:annotation>
```
345 / 414
KS X 6101:2024
338
code
Xml
```xml
</xs:element>
<xs:element name="effectsColor" type="hp:EffectColorType">
    <xs:annotation>
        <xs:documentation>그림자 색</xs:documentation>
    </xs:annotation>
</xs:element>
</xs:sequence>
<xs:attribute name="style">
    <xs:annotation>
        <xs:documentation>그림자 스타일</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="NONE"/>
            <xs:enumeration value="LEFT_TOP"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="alpha">
    <xs:annotation>
        <xs:documentation>그림자 투명도</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="1"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="radius" type="xs:float">
    <xs:annotation>
        <xs:documentation>부드러운 가장자리 크기. 단위는 HWPUNIT</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="glow" minOccurs="0">
<xs:complexType>
<xs:sequence>
<xs:element name="effectsColor" type="hp:GlowEffectColorType">
    <xs:annotation>
        <xs:documentation>네온 색</xs:documentation>
    </xs:annotation>
</xs:element>
</xs:sequence>
<xs:attribute name="alpha">
    <xs:annotation>
        <xs:documentation>투명도</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="1"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="radius" type="xs:float">
    <xs:annotation>
        <xs:documentation>네온 반경. 단위 HWPUNIT</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="softEdge" minOccurs="0">
<xs:complexType>
<xs:attribute name="radius" type="xs:float">
    <xs:annotation>
        <xs:documentation>부드러운 가장자리 크기. 단위는 HWPUNIT.</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="reflection" minOccurs="0">
<xs:complexType>
<xs:sequence>
<xs:element name="skew" type="hp:SkewType"/>
<xs:element name="scale" type="hp:ScaleType"/>
<xs:element name="alpha">
<xs:complexType>
```
340
KSX 6101:2024
code
Xml
```xml
<xs:attribute name="start">
    <xs:annotation>
        <xs:documentation>시작 위치 투명도</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="1"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="end">
    <xs:annotation>
        <xs:documentation>끝 위치 투명도</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="1"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
</xs:complexType>
</xs:element>
<xs:element name="pos">
    <xs:annotation>
        <xs:documentation>위치</xs:documentation>
    </xs:annotation>
    <xs:complexType>
        <xs:attribute name="start" type="xs:float">
            <xs:annotation>
                <xs:documentation>시작 위치</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="end" type="xs:float">
            <xs:annotation>
                <xs:documentation>끝 위치</xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
</xs:element>
```
348 / 414
KSX 6101:2024
code
Xml
```xml
</xs:sequence>
<xs:attribute name="alignStyle" type="hc:AlignStyleType"/>
<xs:attribute name="radius" type="xs:float">
    <xs:annotation>
        <xs:documentation>흐릿한 정도. 단위 HWPUNIT.</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="direction">
    <xs:annotation>
        <xs:documentation>그림자 방향 각도</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:integer">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="360"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="distance">
    <xs:annotation>
        <xs:documentation>거리. 단위는 HWPUNIT.</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="0"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="rotationStyle" type="xs:boolean">
    <xs:annotation>
        <xs:documentation>도형과 함께 회전 여부</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="fadeDirection">
    <xs:annotation>
        <xs:documentation>사라지는 방향</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:integer">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="360"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="EffectColorType">
<xs:sequence>
<xs:choice>
<xs:element name="rgb">
    <xs:complexType>
        <xs:attribute name="r" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="g" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="b" type="xs:nonNegativeInteger" use="required"/>
    </xs:complexType>
</xs:element>
```
KSX 6101:2024
code
Xml
```xml
<xs:element name="cmyk">
    <xs:complexType>
        <xs:attribute name="c" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="m" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="y" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="k" type="xs:nonNegativeInteger" use="required"/>
    </xs:complexType>
</xs:element>
<xs:element name="scheme">
    <xs:complexType>
        <xs:attribute name="r" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="g" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="b" type="xs:nonNegativeInteger" use="required"/>
    </xs:complexType>
</xs:element>
<xs:element name="system">
    <xs:complexType>
        <xs:attribute name="r" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="g" type="xs:nonNegativeInteger" use="required"/>
        <xs:attribute name="b" type="xs:nonNegativeInteger" use="required"/>
    </xs:complexType>
</xs:element>
</xs:choice>
</xs:sequence>
<xs:attribute name="type" use="required">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="RGB"/>
<xs:enumeration value="CMYK"/>
<xs:enumeration value="SCHEME"/>
<xs:enumeration value="SYSTEM"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="schemeIdx" type="xs:integer"/>
<xs:attribute name="presetIdx" type="xs:integer"/>
</xs:complexType>
<xs:complexType name="GlowEffectColorType">
<xs:complexContent>
<xs:extension base="hp:EffectColorType">
<xs:sequence>
<xs:element name="effect" minOccurs="0">
<xs:complexType>
<xs:attribute name="type" use="required">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="ALPHA"/>
```
350/414
KSX 6101:2024
code
Xml
```xml
<xs:enumeration value="ALPHA_MOD"/>
<xs:enumeration value="ALPHA_OFF"/>
<xs:enumeration value="RED"/>
<xs:enumeration value="RED_MOD"/>
<xs:enumeration value="RED_OFF"/>
<xs:enumeration value="GREEN"/>
<xs:enumeration value="GREEN_MOD"/>
<xs:enumeration value="GREEN_OFF"/>
<xs:enumeration value="BLUE"/>
<xs:enumeration value="BLUE_MOD"/>
<xs:enumeration value="BLUE_OFF"/>
<xs:enumeration value="HUE"/>
<xs:enumeration value="HUE_MOD"/>
<xs:enumeration value="HUE_OFF"/>
<xs:enumeration value="SAT"/>
<xs:enumeration value="SAT_MOD"/>
<xs:enumeration value="SAT_OFF"/>
<xs:enumeration value="LUM"/>
<xs:enumeration value="LUM_MOD"/>
<xs:enumeration value="LUM_OFF"/>
<xs:enumeration value="SHADE"/>
<xs:enumeration value="TINT"/>
<xs:enumeration value="GRAY"/>
<xs:enumeration value="COMP"/>
<xs:enumeration value="GAMMA"/>
<xs:enumeration value="INV_GAMMA"/>
<xs:enumeration value="INV"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
```
351/414
KSX 6101:2024
code
Xml
```xml
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="SkewType">
<xs:attribute name="x">
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="-90"/>
            <xs:maxInclusive value="90"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="y">
    <xs:simpleType>
        <xs:restriction base="xs:float">
            <xs:minInclusive value="-90"/>
            <xs:maxInclusive value="90"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
</xs:complexType>
<xs:complexType name="ScaleType">
<xs:attribute name="x" type="xs:float"/>
<xs:attribute name="y" type="xs:float"/>
</xs:complexType>
<xs:complexType name="ShadowType">
<xs:annotation>
    <xs:documentation>그림자 속성</xs:documentation>
</xs:annotation>
<xs:attribute name="type" default="NONE">
    <xs:annotation>
        <xs:documentation>그림자 종류</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="NONE"/>
            <xs:enumeration value="PARALLEL_LEFTTOP"/>
            <xs:enumeration value="PARALLEL_RIGHTTOP"/>
            <xs:enumeration value="PARALLEL_LEFTBOTTOM"/>
            <xs:enumeration value="PARALLEL_RIGHTBOTTOM"/>
            <xs:enumeration value="SHEAR_LEFTTOP"/>
            <xs:enumeration value="SHEAR_RIGHTTOP"/>
            <xs:enumeration value="SHEAR_LEFTBOTTOM"/>
            <xs:enumeration value="SHEAR_RIGHTBOTTOM"/>
            <xs:enumeration value="PERS_LEFTTOP"/>
            <xs:enumeration value="PERS_RIGHTTOP"/>
            <xs:enumeration value="PERS_LEFTBOTTOM"/>
            <xs:enumeration value="PERS_RIGHTBOTTOM"/>
            <xs:enumeration value="SCALE_NARROW"/>
            <xs:enumeration value="SCALE_ENLARGE"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="color" type="hc:RGBColorType" default="808080">
    <xs:annotation>
        <xs:documentation>그림자 색</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="offsetX">
    <xs:annotation>
        <xs:documentation>그림자 간격 X</xs:documentation>
    </xs:annotation>
```
345
KSX 6101:2024
code
Xml
```xml
<xs:simpleType>
        <xs:restriction base="xs:integer"/>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="offsetY">
    <xs:annotation>
        <xs:documentation>그림자 간격 Y</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:integer"/>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="alpha" type="xs:float"/>
</xs:complexType>
<xs:complexType name="AbstractShapeObjectType" abstract="true">
<xs:sequence>
<xs:element name="sz" minOccurs="0">
<xs:complexType>
<xs:attribute name="width" type="xs:nonNegativeInteger"/>
<xs:attribute name="widthRelTo" default="ABSOLUTE">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="PAPER"/>
            <xs:enumeration value="PAGE"/>
            <xs:enumeration value="COLUMN"/>
            <xs:enumeration value="PARA"/>
            <xs:enumeration value="ABSOLUTE"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="height" type="xs:nonNegativeInteger"/>
<xs:attribute name="heightRelTo" default="ABSOLUTE">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="PAPER"/>
            <xs:enumeration value="PAGE"/>
            <xs:enumeration value="ABSOLUTE"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="protect" type="xs:boolean" default="false"/>
</xs:complexType>
</xs:element>
<xs:element name="pos" minOccurs="0">
<xs:complexType>
<xs:attribute name="treatAsChar" type="xs:boolean" default="false"/>
<xs:attribute name="affectLSpacing" type="xs:boolean" default="false"/>
<xs:attribute name="flowWithText" type="xs:boolean" default="false"/>
<xs:attribute name="allowOverlap" type="xs:boolean" default="false"/>
<xs:attribute name="holdAnchorAndSO" type="xs:boolean" default="false"/>
<xs:attribute name="vertRelTo" default="PARA">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="PAPER"/>
            <xs:enumeration value="PAGE"/>
            <xs:enumeration value="PARA"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="horzRelTo" default="COLUMN">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="PAPER"/>
            <xs:enumeration value="PAGE"/>
            <xs:enumeration value="COLUMN"/>
            <xs:enumeration value="PARA"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="vertAlign" default="TOP">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="TOP"/>
            <xs:enumeration value="CENTER"/>
            <xs:enumeration value="BOTTOM"/>
            <xs:enumeration value="INSIDE"/>
            <xs:enumeration value="OUTSIDE"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="horzAlign" default="LEFT">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="LEFT"/>
            <xs:enumeration value="CENTER"/>
            <xs:enumeration value="RIGHT"/>
            <xs:enumeration value="INSIDE"/>
            <xs:enumeration value="OUTSIDE"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="vertOffset" type="xs:nonNegativeInteger" default="0"/>
<xs:attribute name="horzOffset" type="xs:nonNegativeInteger" default="0"/>
</xs:complexType>
</xs:element>
<xs:element name="outMargin" minOccurs="0">
```
이전 파일에서 이어짐
code
Xml
```xml
<xs:enumeration value="BEHIND_TEXT"/>
<xs:enumeration value="IN_FRONT_OF_TEXT"/>
```
KSX 6101:2024
code
Xml
```xml
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="textFlow" default="BOTH_SIDES">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="BOTH_SIDES"/>
<xs:enumeration value="LEFT_ONLY"/>
<xs:enumeration value="RIGHT_ONLY"/>
<xs:enumeration value="LARGEST_ONLY"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="lock" type="xs:boolean" default="false"/>
<xs:attribute name="dropcapstyle" type="hc:DropCapStyleType" default="None"/>
</xs:complexType>
<xs:complexType name="TableType">
<xs:complexContent>
<xs:extension base="hp:AbstractShapeObjectType">
<xs:sequence>
<xs:element name="inMargin" type="hp:InsideMarginType"/>
<xs:element name="cellzone">
<xs:complexType>
<xs:sequence>
<xs:element name="cell" maxOccurs="unbounded">
<xs:complexType>
<xs:attribute name="startRowAddr" type="xs:nonNegativeInteger">
    <xs:annotation>
        <xs:documentation>병합된 Row의 시작 주소</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="startColAddr" type="xs:nonNegativeInteger">
    <xs:annotation>
        <xs:documentation>병합된 Column의 시작 주소</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="endRowAddr" type="xs:nonNegativeInteger">
    <xs:annotation>
        <xs:documentation>병합된 Row의 끝 주소</xs:documentation>
    </xs:annotation>
</xs:attribute>
```
349
KSX 6101:2024
code
Xml
```xml
<xs:attribute name="endColAddr" type="xs:nonNegativeInteger">
    <xs:annotation>
        <xs:documentation>병합된 Column의 끝 주소</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger">
    <xs:annotation>
        <xs:documentation>테두리/배경 아이디 참조 값</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>
</xs:element>
<xs:element name="tc" maxOccurs="unbounded">
<xs:complexType>
<xs:sequence>
<xs:element name="subList" type="hp:ParaListType"/>
<xs:element name="cellAddr">
<xs:complexType>
<xs:attribute name="colAddr" type="xs:nonNegativeInteger"/>
<xs:attribute name="rowAddr" type="xs:nonNegativeInteger"/>
</xs:complexType>
</xs:element>
<xs:element name="cellSpan">
<xs:complexType>
<xs:attribute name="colSpan" type="xs:positiveInteger" default="1"/>
<xs:attribute name="rowSpan" type="xs:positiveInteger" default="1"/>
</xs:complexType>
</xs:element>
<xs:element name="cellSz">
<xs:complexType>
<xs:attribute name="width" type="xs:nonNegativeInteger"/>
<xs:attribute name="height" type="xs:nonNegativeInteger"/>
```
350
KSX 6101:2024
code
Xml
```xml
</xs:complexType>
</xs:element>
<xs:element name="cellMargin">
<xs:complexType>
<xs:attributeGroup ref="hc:MarginAttributeGroup"/>
</xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="name" type="xs:string"/>
<xs:attribute name="header" type="xs:boolean" default="false"/>
<xs:attribute name="hasMargin" type="xs:boolean" default="false"/>
<xs:attribute name="protect" type="xs:boolean" default="false"/>
<xs:attribute name="editable" type="xs:boolean" default="false"/>
<xs:attribute name="dirty" type="xs:boolean" default="false"/>
<xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger"/>
</xs:complexType>
</xs:element>
</xs:sequence>
</xs:complexType>
</xs:element>
<xs:element name="tbl" minOccurs="0">
<xs:complexType>
<xs:attribute name="topMargin" type="xs:nonNegativeInteger"/>
<xs:attribute name="leftMargin" type="xs:nonNegativeInteger"/>
<xs:attribute name="textWidth" type="xs:nonNegativeInteger"/>
<xs:attribute name="textLength" type="xs:nonNegativeInteger"/>
<xs:attribute name="downMarginHorz" type="xs:nonNegativeInteger"/>
<xs:attribute name="downMarginVert" type="xs:nonNegativeInteger"/>
<xs:attribute name="labelCols" type="xs:nonNegativeInteger"/>
<xs:attribute name="labelRows" type="xs:nonNegativeInteger"/>
<xs:attribute name="landscape">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="WIDELY"/>
<xs:enumeration value="NARROWLY"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="pageWidth" type="xs:nonNegativeInteger"/>
<xs:attribute name="pageHeight" type="xs:nonNegativeInteger"/>
</xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="pageBreak">
```
358/414
KSX 6101:2024
code
Xml
```xml
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="TABLE"/>
<xs:enumeration value="CELL"/>
<xs:enumeration value="NONE"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="repeatHeader" type="xs:boolean" default="false"/>
<xs:attribute name="noAdjust" type="xs:boolean" default="false"/>
<xs:attribute name="rowCnt" type="xs:positiveInteger"/>
<xs:attribute name="colCnt" type="xs:positiveInteger"/>
<xs:attribute name="cellSpacing" type="xs:nonNegativeInteger" default="0"/>
<xs:attribute name="borderFillIDRef" type="xs:nonNegativeInteger"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="EquationType">
<xs:complexContent>
<xs:extension base="hp:AbstractShapeObjectType">
<xs:sequence>
<xs:element name="script"/>
</xs:sequence>
<xs:attribute name="version" type="xs:string" default="Equation Version 60">
    <xs:annotation>
        <xs:documentation>수식 편집기 버전. 현재는 "Equation Version 60"</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="baseLine" default="85">
    <xs:annotation>
        <xs:documentation>수식이 그려질 기준선.</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:unsignedInt">
            <xs:maxInclusive value="100"/>
        </xs:restriction>
    </xs:simpleType>
```
352
KSX 6101:2024
code
Xml
```xml
</xs:attribute>
<xs:attribute name="textColor" type="hc:RGBColorType" default="000000">
    <xs:annotation>
        <xs:documentation>수식 글자 색</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="baseUnit" type="xs:nonNegativeInteger" default="1000">
    <xs:annotation>
        <xs:documentation>수식의 글자 크기. 단위는 HWPUNIT.</xs:documentation>
    </xs:annotation>
</xs:attribute>
<xs:attribute name="lineMode" default="CHAR">
    <xs:annotation>
        <xs:documentation>수식이 차지하는 범위.</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="LINE"/>
            <xs:enumeration value="CHAR"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="fontName" type="xs:string">
    <xs:annotation>
        <xs:documentation>수식 글꼴</xs:documentation>
    </xs:annotation>
</xs:attribute>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="AbstractShapeComponentType" abstract="true">
<xs:complexContent>
<xs:extension base="hp:AbstractShapeObjectType">
<xs:sequence>
<xs:element name="offset">
<xs:complexType>
<xs:attribute name="x" type="xs:nonNegativeInteger" default="0"/>
<xs:attribute name="y" type="xs:nonNegativeInteger" default="0"/>
</xs:complexType>
</xs:element>
<xs:element name="orgSz">
<xs:complexType>
<xs:attribute name="width" type="xs:nonNegativeInteger"/>
<xs:attribute name="height" type="xs:nonNegativeInteger"/>
</xs:complexType>
</xs:element>
<xs:element name="curSz">
<xs:complexType>
<xs:attribute name="width" type="xs:nonNegativeInteger"/>
<xs:attribute name="height" type="xs:nonNegativeInteger"/>
</xs:complexType>
</xs:element>
<xs:element name="flip">
<xs:complexType>
<xs:attribute name="horizontal" type="xs:boolean" default="false"/>
```
360/414
KSX 6101:2024
code
Xml
```xml
<xs:attribute name="vertical" type="xs:boolean" default="false"/>
</xs:complexType>
</xs:element>
<xs:element name="rotationInfo">
<xs:complexType>
<xs:attribute name="angle" type="xs:integer" default="0"/>
<xs:attribute name="centerX" type="xs:nonNegativeInteger"/>
<xs:attribute name="centerY" type="xs:nonNegativeInteger"/>
<xs:attribute name="rotateimage" type="xs:boolean"/>
</xs:complexType>
</xs:element>
<xs:element name="renderingInfo">
<xs:complexType>
<xs:sequence>
<xs:element name="transMatrix" type="hc:MatrixType"/>
<xs:sequence minOccurs="0" maxOccurs="unbounded">
<xs:element name="scaMatrix" type="hc:MatrixType"/>
<xs:element name="rotMatrix" type="hc:MatrixType"/>
</xs:sequence>
</xs:sequence>
</xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="href" type="xs:string"/>
<xs:attribute name="groupLevel" type="xs:nonNegativeInteger" default="0"/>
<xs:attribute name="instId" type="xs:nonNegativeInteger"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="PictureType">
<xs:complexContent>
<xs:extension base="hp:AbstractShapeComponentType">
<xs:sequence>
<xs:element name="lineShape" type="hp:LineShapeType" minOccurs="0"/>
<xs:element name="imgRect">
<xs:complexType>
<xs:sequence>
<xs:element name="pt0" type="hc:PointType"/>
<xs:element name="pt1" type="hc:PointType"/>
<xs:element name="pt2" type="hc:PointType"/>
<xs:element name="pt3" type="hc:PointType"/>
</xs:sequence>
</xs:complexType>
</xs:element>
<xs:element name="imgClip">
<xs:complexType>
<xs:attribute name="left" type="xs:integer"/>
<xs:attribute name="right" type="xs:integer"/>
```
354
KSX 6101:2024
code
Xml
```xml
<xs:attribute name="top" type="xs:integer"/>
<xs:attribute name="bottom" type="xs:integer"/>
</xs:complexType>
</xs:element>
<xs:element name="effects" type="hp:EffectsType"/>
<xs:element name="inMargin" type="hp:InsideMarginType"/>
<xs:element name="imgDim">
<xs:complexType>
<xs:attribute name="dimwidth" type="xs:unsignedInt"/>
<xs:attribute name="dimheight" type="xs:unsignedInt"/>
</xs:complexType>
</xs:element>
<xs:element name="img" type="hc:ImageType"/>
</xs:sequence>
<xs:attribute name="reverse" type="xs:boolean"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="OLEType">
<xs:complexContent>
<xs:extension base="hp:AbstractShapeComponentType">
<xs:sequence>
<xs:element name="extent" type="hc:PointType"/>
<xs:element name="lineShape" type="hp:LineShapeType"/>
</xs:sequence>
<xs:attribute name="objectType">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="UNKNOWN"/>
<xs:enumeration value="EMBEDDED"/>
<xs:enumeration value="LINK"/>
<xs:enumeration value="STATIC"/>
<xs:enumeration value="EQUATION"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="binaryItemIDRef" type="xs:string"/>
<xs:attribute name="hasMoniker" type="xs:boolean" default="false"/>
<xs:attribute name="drawAspect">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="CONTENT"/>
<xs:enumeration value="THUMB_NAIL"/>
<xs:enumeration value="ICON"/>
<xs:enumeration value="DOC_PRINT"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
```
355
363/414
KSX 6101:2024
code
Xml
<xs:attribute name="eqb" type="xs:boolean" default="false"/>
</xs:complexType>
<xs:complexType name="AbstractDrawingObjectType" abstract="true">
<xs:complexContent>
<xs:extension base="hp:AbstractShapeComponentType">
<xs:sequence>
<xs:element name="lineShape" type="hp:LineShapeType"/>
<xs:element name="fillBrush" type="hh:FillBrushType" minOccurs="0"/>
<xs:element name="drawText" minOccurs="0">
<xs:complexType>
<xs:sequence>
<xs:element name="subList" type="hp:ParaListType"/>
</xs:sequence>
<xs:attribute name="lastWidth" type="xs:nonNegativeInteger"/>
<xs:attribute name="name" type="xs:string"/>
<xs:attribute name="editable" type="xs:boolean" default="false"/>
</xs:complexType>
</xs:element>
<xs:element name="shadow" type="hp:ShadowType"/>
</xs:sequence>
<xs:attribute name="horzTextBoxAlign">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="LEFT"/>
<xs:enumeration value="CENTER"/>
<xs:enumeration value="RIGHT"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="vertTextBoxAlign" default="CENTER">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="TOP"/>
<xs:enumeration value="CENTER"/>
<xs:enumeration value="BOTTOM"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="textVerticalWidth" type="xs:nonNegativeInteger"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="RectangleType">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="pt0" type="hc:PointType"/>
<xs:element name="pt1" type="hc:PointType"/>
<xs:element name="pt2" type="hc:PointType"/>
<xs:element name="pt3" type="hc:PointType"/>
</xs:sequence>
<xs:attribute name="ratio" type="xs:nonNegativeInteger" default="0"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="EllipseType">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="center" type="hc:PointType"/>
<xs:element name="ax1" type="hc:PointType"/>
<xs:element name="ax2" type="hc:PointType"/>
</xs:sequence>
<xs:attribute name="type">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="ELLIPSE"/>
<xs:enumeration value="ARC"/>
<xs:enumeration value="PIE"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="centerX" type="xs:integer"/>
<xs:attribute name="centerY" type="xs:integer"/>
<xs:attribute name="ax1X" type="xs:integer"/>
<xs:attribute name="ax1Y" type="xs:integer"/>
<xs:attribute name="ax2X" type="xs:integer"/>
<xs:attribute name="ax2Y" type="xs:integer"/>
<xs:attribute name="startX" type="xs:integer"/>
<xs:attribute name="startY" type="xs:integer"/>
<xs:attribute name="endX" type="xs:integer"/>
<xs:attribute name="endY" type="xs:integer"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="ArcType">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="center" type="hc:PointType"/>
<xs:element name="ax1" type="hc:PointType"/>
<xs:element name="ax2" type="hc:PointType"/>
</xs:sequence>
<xs:attribute name="type">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="NORMAL"/>
<xs:enumeration value="QUARTER"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="half" type="xs:boolean" default="false"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="PolygonType">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="pt" type="hc:PointType" maxOccurs="unbounded"/>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="CurveType">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="pt" type="hc:PointType" maxOccurs="unbounded"/>
</xs:sequence>
<xs:attribute name="type">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="NORMAL"/>
<xs:enumeration value="THAN_PATH"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
</xs:extension>
</xs:complexContent>
</xs:complexType>
366/414
KSX 6101:2024
code
Xml
```xml
<xs:complexType name="ConnectLineType">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="startPt" type="hp:ConnectPointType"/>
<xs:element name="endPt" type="hp:ConnectPointType"/>
<xs:element name="controlPoints" minOccurs="0">
<xs:complexType>
<xs:sequence>
<xs:element name="point" type="hp:ConnectControlPointType" maxOccurs="unbounded"/>
</xs:sequence>
</xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="type">
    <xs:annotation>
        <xs:documentation>선 종류 - 직선, 꺾은선, 곡선과 화살표 유무의 조합</xs:documentation>
    </xs:annotation>
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="STRAIGHT_NOARROW"/>
            <xs:enumeration value="STRAIGHT_ONEWAY"/>
            <xs:enumeration value="STRAIGHT_BOTH"/>
            <xs:enumeration value="STROKE_NOARROW"/>
            <xs:enumeration value="STROKE_ONEWAY"/>
            <xs:enumeration value="STROKE_BOTH"/>
            <xs:enumeration value="ARC_NOARROW"/>
            <xs:enumeration value="ARC_ONEWAY"/>
            <xs:enumeration value="ARC_BOTH"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="ConnectControlPointType">
<xs:complexContent>
<xs:extension base="hc:PointType">
```
359
KSX 6101:2024
code
Xml
<xs:attribute name="type" type="xs:nonNegativeInteger"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="AbstractFormObjectType" abstract="true">
<xs:complexContent>
<xs:extension base="hp:AbstractDrawingObjectType">
<xs:sequence>
<xs:element name="text" minOccurs="0">
<xs:complexType>
<xs:simpleContent>
<xs:extension base="xs:string">
<xs:attribute name="vertAlign" default="CENTER">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="TOP"/>
            <xs:enumeration value="CENTER"/>
            <xs:enumeration value="BOTTOM"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
<xs:attribute name="horzAlign" default="LEFT">
    <xs:simpleType>
        <xs:restriction base="xs:string">
            <xs:enumeration value="LEFT"/>
            <xs:enumeration value="CENTER"/>
            <xs:enumeration value="RIGHT"/>
        </xs:restriction>
    </xs:simpleType>
</xs:attribute>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
</xs:element>
</xs:sequence>
<xs:attribute name="name" type="xs:string" use="required"/>
<xs:attribute name="foreColor" type="hc:RGBColorType" default="000000"/>
<xs:attribute name="backColor" type="hc:RGBColorType" default="FFFFFF"/>
<xs:attribute name="groupName" type="xs:string"/>
<xs:attribute name="tabOrder" type="xs:positiveInteger"/>
<xs:attribute name="enabled" type="xs:boolean" default="true"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="ButtonType">
<xs:complexContent>
<xs:extension base="hp:AbstractFormObjectType">
<xs:attribute name="type" default="PUSH">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="PUSH"/>
<xs:enumeration value="RADIO"/>
<xs:enumeration value="CHECK"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="defaultValue" type="xs:boolean" default="false"/>
<xs:attribute name="selected" type="xs:boolean" default="false"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="EditType">
<xs:complexContent>
<xs:extension base="hp:AbstractFormObjectType">
<xs:attribute name="multiLine" type="xs:boolean" default="false"/>
<xs:attribute name="passwordChar" type="xs:string"/>
<xs:attribute name="maxLength" type="xs:integer"/>
<xs:attribute name="readOnly" type="xs:boolean"/>
<xs:attribute name="wordWrap" default="NONE">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="NONE"/>
<xs:enumeration value="CHAR"/>
<xs:enumeration value="WORD"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="scrollBars" default="NONE">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="NONE"/>
<xs:enumeration value="HORIZONTAL"/>
<xs:enumeration value="VERTICAL"/>
<xs:enumeration value="BOTH"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
<xs:attribute name="tabKeyBehavior" type="xs:boolean" default="false"/>
<xs:attribute name="numOnly" type="xs:boolean" default="false"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="ComboBoxType">
<xs:complexContent>
<xs:extension base="hp:AbstractFormObjectType">
<xs:sequence>
<xs:element name="listItem" type="hp:ListItemType" minOccurs="0" maxOccurs="unbounded"/>
</xs:sequence>
<xs:attribute name="readOnly" type="xs:boolean" default="false"/>
<xs:attribute name="listBoxRows" type="xs:positiveInteger"/>
<xs:attribute name="selectedValue" type="xs:string"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="ListBoxType">
<xs:complexContent>
<xs:extension base="hp:AbstractFormObjectType">
<xs:sequence>
<xs:element name="listItem" type="hp:ListItemType" minOccurs="0" maxOccurs="unbounded"/>
</xs:sequence>
<xs:attribute name="itemHeight" type="xs:integer"/>
<xs:attribute name="topIdx" type="xs:nonNegativeInteger"/>
<xs:attribute name="selectedValue" type="xs:string"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:complexType name="ScrollBarType">
<xs:complexContent>
<xs:extension base="hp:AbstractFormObjectType">
<xs:attribute name="delay" type="xs:nonNegativeInteger"/>
<xs:attribute name="largeChange" type="xs:nonNegativeInteger"/>
<xs:attribute name="smallChange" type="xs:nonNegativeInteger"/>
<xs:attribute name="min" type="xs:int"/>
<xs:attribute name="max" type="xs:int"/>
<xs:attribute name="page" type="xs:int"/>
<xs:attribute name="value" type="xs:int"/>
<xs:attribute name="type">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="HORIZONTAL"/>
<xs:enumeration value="VERTICAL"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
</xs:extension>
</xs:complexContent>
</xs:complexType>
<xs:simpleType name="FieldType">
<xs:restriction base="xs:string">
<xs:enumeration value="CLICK_HERE"/>
<xs:enumeration value="HYPERLINK"/>
<xs:enumeration value="BOOKMARK"/>
<xs:enumeration value="FORMULA"/>
<xs:enumeration value="SUMMARY"/>
<xs:enumeration value="USER_INFO"/>
<xs:enumeration value="DATE"/>
<xs:enumeration value="DOC_DATE"/>
<xs:enumeration value="PATH"/>
<xs:enumeration value="CROSSREF"/>
<xs:enumeration value="MAILMERGE"/>
<xs:enumeration value="MEMO"/>
<xs:enumeration value="PROOFREADING_MARKS"/>
<xs:enumeration value="PRIVATE_INFO"/>
<xs:enumeration value="METATAG"/>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="HeaderFooterType">
363
KSX 6101:2024
code
Xml
```xml
<xs:sequence>
<xs:element name="subList" type="hp:ParaListType"/>
</xs:sequence>
<xs:attribute name="id" type="xs:nonNegativeInteger"/>
<xs:attribute name="applyPageType" default="BOTH">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="BOTH"/>
<xs:enumeration value="EVEN"/>
<xs:enumeration value="ODD"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
</xs:complexType>
<xs:complexType name="NoteType">
<xs:sequence>
<xs:element name="subList" type="hp:ParaListType"/>
</xs:sequence>
<xs:attribute name="instId" type="xs:nonNegativeInteger"/>
</xs:complexType>
<xs:complexType name="AutoNumNewNumType">
<xs:sequence>
<xs:element name="autoNumFormat" type="hp:AutoNumFormatType"/>
</xs:sequence>
<xs:attribute name="num" type="xs:integer" default="1"/>
<xs:attribute name="numType">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:enumeration value="PAGE"/>
<xs:enumeration value="FOOTNOTE"/>
<xs:enumeration value="ENDNOTE"/>
<xs:enumeration value="PICTURE"/>
<xs:enumeration value="TABLE"/>
<xs:enumeration value="EQUATION"/>
<xs:enumeration value="TOTAL_PAGE"/>
</xs:restriction>
</xs:simpleType>
</xs:attribute>
</xs:complexType>
<xs:complexType name="ListItemType">
<xs:attribute name="displayText" type="xs:string"/>
<xs:attribute name="value" type="xs:string"/>
</xs:complexType>
<xs:complexType name="ParameterList">
<xs:choice minOccurs="0" maxOccurs="unbounded">
<xs:element name="booleanParam">
<xs:complexType>
<xs:simpleContent>
```
364
371 / 414
KSX 6101:2024
code
Xml
```xml
<xs:extension base="xs:boolean">
<xs:attribute name="name" type="xs:string"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
</xs:element>
<xs:element name="integerParam">
<xs:complexType>
<xs:simpleContent>
<xs:extension base="xs:integer">
<xs:attribute name="name" type="xs:string"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
</xs:element>
<xs:element name="floatParam">
<xs:complexType>
<xs:simpleContent>
<xs:extension base="xs:float">
<xs:attribute name="name" type="xs:string"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
</xs:element>
<xs:element name="stringParam">
<xs:complexType>
<xs:simpleContent>
<xs:extension base="xs:string">
<xs:attribute name="name" type="xs:string"/>
<xs:attribute ref="xml:space"/>
</xs:extension>
</xs:simpleContent>
</xs:complexType>
</xs:element>
<xs:element name="listParam" type="hp:ParameterList"/>
</xs:choice>
<xs:attribute name="cnt" type="xs:positiveInteger" use="required"/>
<xs:attribute name="name" type="xs:string"/>
</xs:complexType>
<xs:complexType name="TrackChangeTag">
<xs:attribute name="paraend" type="xs:boolean"/>
<xs:attribute name="lId" type="xs:nonNegativeInteger"/>
<xs:attribute name="rId" type="xs:nonNegativeInteger"/>
</xs:complexType>
</xs:schema>
```
366
KSX 6101:2024
부속서 F
(규정)
Core XML 스키마
code
Xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:hcf="http://www.owpml.org/owpml/2024/core"
```
    targetNamespace="http://www.owpml.org/owpml/2024/core" elementFormDefault="qualified">

<xs:simpleType name="NumberType1">
    <xs:restriction base="xs:string">
        <xs:enumeration value="DIGIT">
            <xs:annotation>
                <xs:documentation>1, 2, 3</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_DIGIT">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 1, 2, 3</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="ROMAN_CAPITAL">
            <xs:annotation>
                <xs:documentation>I, II, III</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="ROMAN_SMALL">
            <xs:annotation>
                <xs:documentation>i, ii, iii</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="LATIN_CAPITAL">
            <xs:annotation>
                <xs:documentation>A, B, C</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="LATIN_SMALL">
            <xs:annotation>
                <xs:documentation>a, b, c</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_LATIN_CAPITAL">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 A, B, C</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_LATIN_SMALL">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 a, b, c</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="HANGUL_SYLLABLE">
            <xs:annotation>
                <xs:documentation>가, 나, 다</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_HANGUL_SYLLABLE">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 가, 나, 다</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="HANGUL_JAMO">
            <xs:annotation>
                <xs:documentation>ㄱ, ㄴ, ㄷ</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_HANGUL_JAMO">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 ㄱ, ㄴ, ㄷ</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="HANGUL_PHONETIC">
            <xs:annotation>
                <xs:documentation>하나, 둘, 셋</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="IDEOGRAPH">
            <xs:annotation>
                <xs:documentation>一, 二, 三</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_IDEOGRAPH">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 一, 二, 三</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="NumberType2">
    <xs:restriction base="xs:string">
        <xs:enumeration value="DIGIT">
            <xs:annotation>
                <xs:documentation>1, 2, 3</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
367
KSX 6101:2024
code
Xml
```xml
<xs:enumeration value="CIRCLED_DIGIT">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 1, 2, 3</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="ROMAN_CAPITAL">
            <xs:annotation>
                <xs:documentation>I, II, III</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="ROMAN_SMALL">
            <xs:annotation>
                <xs:documentation>i, ii, iii</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="LATIN_CAPITAL">
            <xs:annotation>
                <xs:documentation>A, B, C</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="LATIN_SMALL">
            <xs:annotation>
                <xs:documentation>a, b, c</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_LATIN_CAPITAL">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 A, B, C</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_LATIN_SMALL">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 a, b, c</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="HANGUL_SYLLABLE">
            <xs:annotation>
                <xs:documentation>가, 나, 다</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLED_HANGUL_SYLLABLE">
            <xs:annotation>
                <xs:documentation>동그라미 쳐진 가, 나, 다</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="HANGUL_JAMO">
            <xs:annotation>
                <xs:documentation>ㄱ, ㄴ, ㄷ</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
```
368
KSX 6101:2024```xml
```xml
</xs:enumeration>
<xs:enumeration value="CIRCLED_HANGUL_JAMO">
```
xs:annotation
xs:documentation동그라미 쳐진 ㄱ, ㄴ, ㄷ</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="HANGUL_PHONETIC">
xs:annotation
xs:documentation하나, 둘, 셋</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="CIRCLED_IDEOGRAPH">
xs:annotation
xs:documentation동그라미 쳐진 一, 二, 三</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="DECAGON_CIRCLE">
xs:annotation
xs:documentation갑, 을, 병, 정</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="DECAGON_CIRCLE_HANJA">
xs:annotation
xs:documentation甲, 乙, 丙, 丁, 戊, 己, 庚, 辛, 壬, 癸</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="SYMBOL">
xs:annotation
xs:documentation여러 가지 기호가 차례로 반복</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="USER_CHAR">
xs:annotation
xs:documentation사용자 지정 문자 반복</xs:documentation>
</xs:annotation>
</xs:enumeration>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="LineType1">
<xs:restriction base="xs:string">
<xs:enumeration value="NONE">
xs:annotation
code
Code
---
**369**
KSX 6101:2024
```xml
                <xs:documentation>없음</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="SOLID">
            <xs:annotation>
                <xs:documentation>실선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DOT">
            <xs:annotation>
                <xs:documentation>점선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="THICK">
            <xs:annotation>
                <xs:documentation>굵은 선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH">
            <xs:annotation>
                <xs:documentation>파선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH_DOT">
            <xs:annotation>
                <xs:documentation>-.-.-.</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH_DOT_DOT">
            <xs:annotation>
                <xs:documentation>-..-..-..</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="LineType2">
    <xs:restriction base="xs:string">
        <xs:enumeration value="NONE">
            <xs:annotation>
                <xs:documentation>없음</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="SOLID">
            <xs:annotation>
                <xs:documentation>실선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DOT">
370
KSX 6101:2024
code
Xml
<xs:annotation>
                <xs:documentation>점선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH">
            <xs:annotation>
                <xs:documentation>파선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH_DOT">
            <xs:annotation>
                <xs:documentation>-.-.-.</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH_DOT_DOT">
            <xs:annotation>
                <xs:documentation>-..-..-..</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="LONG_DASH">
            <xs:annotation>
                <xs:documentation>DASH보다 긴 선의 반복</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLE">
            <xs:annotation>
                <xs:documentation>DOT보다 큰 동그라미의 반복</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DOUBLE_SLIM">
            <xs:annotation>
                <xs:documentation>2중선 (가는 선 + 가는 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="SLIM_THICK">
            <xs:annotation>
                <xs:documentation>2중선 (가는 선 + 굵은 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="THICK_SLIM">
            <xs:annotation>
                <xs:documentation>2중선 (굵은 선 + 가는 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="SLIM_THICK_SLIM">
            <xs:annotation>
                <xs:documentation>3중선 (가는 선 + 굵은 선 + 가는 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
371
KSX 6101:2024
code
Xml
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="LineType3">
    <xs:restriction base="xs:string">
        <xs:enumeration value="NONE">
            <xs:annotation>
                <xs:documentation>없음</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="SOLID">
            <xs:annotation>
                <xs:documentation>실선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DOT">
            <xs:annotation>
                <xs:documentation>점선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH">
            <xs:annotation>
                <xs:documentation>파선</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH_DOT">
            <xs:annotation>
                <xs:documentation>-.-.-.</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DASH_DOT_DOT">
            <xs:annotation>
                <xs:documentation>-..-..-..</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="LONG_DASH">
            <xs:annotation>
                <xs:documentation>DASH보다 긴 선의 반복</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="CIRCLE">
            <xs:annotation>
                <xs:documentation>DOT보다 큰 동그라미의 반복</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="DOUBLE_SLIM">
            <xs:annotation>
                <xs:documentation>2중선 (가는 선 + 가는 선)</xs:documentation>
            </xs:annotation>
372
KSX 6101:2024
code
Xml
</xs:enumeration>
        <xs:enumeration value="SLIM_THICK">
            <xs:annotation>
                <xs:documentation>2중선 (가는 선 + 굵은 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="THICK_SLIM">
            <xs:annotation>
                <xs:documentation>2중선 (굵은 선 + 가는 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="SLIM_THICK_SLIM">
            <xs:annotation>
                <xs:documentation>3중선 (가는 선 + 굵은 선 + 가는 선)</xs:documentation>
            </xs:annotation>
        </xs:enumeration>
        <xs:enumeration value="WAVE"/>
        <xs:enumeration value="DOUBLEWAVE"/>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="LineWidth">
    <xs:restriction base="xs:string">
        <xs:whiteSpace value="collapse"/>
        <xs:enumeration value="0.1 mm"/>
        <xs:enumeration value="0.12 mm"/>
        <xs:enumeration value="0.15 mm"/>
        <xs:enumeration value="0.2 mm"/>
        <xs:enumeration value="0.25 mm"/>
        <xs:enumeration value="0.3 mm"/>
        <xs:enumeration value="0.4 mm"/>
        <xs:enumeration value="0.5 mm"/>
        <xs:enumeration value="0.6 mm"/>
        <xs:enumeration value="0.7 mm"/>
        <xs:enumeration value="1.0 mm"/>
        <xs:enumeration value="1.5 mm"/>
        <xs:enumeration value="2.0 mm"/>
        <xs:enumeration value="3.0 mm"/>
        <xs:enumeration value="4.0 mm"/>
        <xs:enumeration value="5.0 mm"/>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="RGBColorType">
    <xs:restriction base="xs:string">
        <xs:pattern value="[0-9a-fA-F]{6}"/>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="ArrowType">
    <xs:restriction base="xs:string">
        <xs:enumeration value="NORMAL"/>
        <xs:enumeration value="SPEAR"/>
        <xs:enumeration value="CONCAVE_ARROW"/>
        <xs:enumeration value="DIAMOND_ARROW"/>
        <xs:enumeration value="EMPTY_DIAMOND_ARROW"/>
        <xs:enumeration value="CIRCLE_ARROW"/>
        <xs:enumeration value="EMPTY_CIRCLE_ARROW"/>
        <xs:enumeration value="BOX_ARROW"/>
        <xs:enumeration value="EMPTY_BOX_ARROW"/>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="ArrowSize">
    <xs:restriction base="xs:string">
        <xs:enumeration value="SMALL_SMALL"/>
        <xs:enumeration value="SMALL_MEDIUM"/>
        <xs:enumeration value="SMALL_LARGE"/>
        <xs:enumeration value="MEDIUM_SMALL"/>
        <xs:enumeration value="MEDIUM_MEDIUM"/>
        <xs:enumeration value="MEDIUM_LARGE"/>
        <xs:enumeration value="LARGE_SMALL"/>
        <xs:enumeration value="LARGE_MEDIUM"/>
        <xs:enumeration value="LARGE_LARGE"/>
    </xs:restriction>
</xs:simpleType>
<xs:simpleType name="ShadowType2">
    <xs:restriction base="xs:string">
        <xs:enumeration value="NONE"/>
        <xs:enumeration value="OFFSET"/>
        <xs:enumeration value="OFFSET_LEFT"/>
        <xs:enumeration value="OFFSET_RIGHT"/>
        <xs:enumeration value="OFFSET_TOP"/>
        <xs:enumeration value="OFFSET_BOTTOM"/>
    </xs:restriction>
</xs:simpleType>
374
KSX 6101:2024
code
Xml
<xs:simpleType name="UnderlineType">
    <xs:restriction base="xs:string">
        <xs:enumeration value="None"/>
        <xs:enumeration value="DoubleLine"/>
        <xs:enumeration value="TripleLine"/>
        <xs:enumeration value="Margin"/>
    </xs:restriction>
</xs:simpleType>
<xs:attributeGroup name="MarginAttributeGroup">
    <xs:annotation>
        <xs:documentation>여백 속성</xs:documentation>
    </xs:annotation>
    <xs:attribute name="left" type="xs:nonNegativeInteger" use="required">
        <xs:annotation>
            <xs:documentation>왼쪽 여백. 단위는 HWPUNIT.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="right" type="xs:nonNegativeInteger" use="required">
        <xs:annotation>
            <xs:documentation>오른쪽 여백. 단위는 HWPUNIT.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="top" type="xs:nonNegativeInteger" use="required">
        <xs:annotation>
            <xs:documentation>위 여백. 단위는 HWPUNIT.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
    <xs:attribute name="bottom" type="xs:nonNegativeInteger" use="required">
        <xs:annotation>
            <xs:documentation>아래 여백. 단위는 HWPUNIT.</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:attributeGroup>
<xs:attributeGroup name="BorderAttributeGroup">
    <xs:annotation>
        <xs:documentation>테두리에서 공통적으로 사용되는 속성</xs:documentation>
    </xs:annotation>
    <xs:attribute name="type" default="Solid">
        <xs:annotation>
            <xs:documentation>테두리 선 종류</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="Solid">
                    <xs:annotation>
                        <xs:documentation>실선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
375
KSX 6101:2024
code
Xml
<xs:enumeration value="Dash">
                    <xs:annotation>
                        <xs:documentation>파선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="Dot">
                    <xs:annotation>
                        <xs:documentation>점선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="DashDot">
                    <xs:annotation>
                        <xs:documentation>-.-.-.</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="DashDotDot">
                    <xs:annotation>
                        <xs:documentation>-..-..-..</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="LongDash">
                    <xs:annotation>
                        <xs:documentation>Dash보다 긴 선의 반복</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="Circle">
                    <xs:annotation>
                        <xs:documentation>Dot보다 큰 동그라미의 반복</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="DoubleSlim">
                    <xs:annotation>
                        <xs:documentation>2중선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="SlimThick">
                    <xs:annotation>
                        <xs:documentation>가는 선 + 굵은 선 2중선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="ThickSlim">
                    <xs:annotation>
                        <xs:documentation>굵은 선 + 가는 선 2중선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
                <xs:enumeration value="SlimThickSlim">
                    <xs:annotation>
                        <xs:documentation>가는 선 + 굵은 선 + 가는 선 3중선</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
```---
**376**
KSX 6101:2024
```xml
                <xs:enumeration value="None">
                    <xs:annotation>
                        <xs:documentation>선 없음</xs:documentation>
                    </xs:annotation>
                </xs:enumeration>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="width" default="0.12mm">
        <xs:annotation>
            <xs:documentation>테두리 선 굵기</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="0.1mm"/>
                <xs:enumeration value="0.12mm"/>
                <xs:enumeration value="0.15mm"/>
                <xs:enumeration value="0.2mm"/>
                <xs:enumeration value="0.25mm"/>
                <xs:enumeration value="0.3mm"/>
                <xs:enumeration value="0.4mm"/>
                <xs:enumeration value="0.5mm"/>
                <xs:enumeration value="0.6mm"/>
                <xs:enumeration value="0.7mm"/>
                <xs:enumeration value="1.0mm"/>
                <xs:enumeration value="1.5mm"/>
                <xs:enumeration value="2.0mm"/>
                <xs:enumeration value="3.0mm"/>
                <xs:enumeration value="4.0mm"/>
                <xs:enumeration value="5.0mm"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="color" type="hcf:RGBColorType" default="000000">
        <xs:annotation>
            <xs:documentation>테두리 선 색</xs:documentation>
        </xs:annotation>
    </xs:attribute>
</xs:attributeGroup>
<xs:complexType name="ImageType">
    <xs:attribute name="binaryItemIDRef" type="xs:string"/>
    <xs:attribute name="bright" default="0">
        <xs:annotation>
            <xs:documentation>밝기</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:minInclusive value="-100"/>
                <xs:maxInclusive value="100"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="contrast" default="0">
        <xs:annotation>
            <xs:documentation>대비</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:integer">
                <xs:minInclusive value="-100"/>
                <xs:maxInclusive value="100"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="effect" default="REAL_PIC">
        <xs:annotation>
            <xs:documentation>이미지 효과</xs:documentation>
        </xs:annotation>
        <xs:simpleType>
            <xs:restriction base="xs:string">
                <xs:enumeration value="REAL_PIC"/>
                <xs:enumeration value="GRAY_SCALE"/>
                <xs:enumeration value="BLACK_WHITE"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
</xs:complexType>
378
KSX 6101:2024
code
Xml
<xs:attribute name="alpha" type="xs:float"/>
</xs:complexType>
<xs:complexType name="MatrixType">
    <xs:annotation>
        <xs:documentation>행렬 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="e1" type="xs:float"/>
    <xs:attribute name="e2" type="xs:float"/>
    <xs:attribute name="e3" type="xs:float"/>
    <xs:attribute name="e4" type="xs:float"/>
    <xs:attribute name="e5" type="xs:float"/>
    <xs:attribute name="e6" type="xs:float"/>
</xs:complexType>
<xs:complexType name="PointType">
    <xs:annotation>
        <xs:documentation>Point 정보</xs:documentation>
    </xs:annotation>
    <xs:attribute name="x" type="xs:integer"/>
    <xs:attribute name="y" type="xs:integer"/>
</xs:complexType>
<xs:complexType name="FillBrushType">
    <xs:annotation>
        <xs:documentation>채우기 정보</xs:documentation>
    </xs:annotation>
    <xs:choice>
        <xs:element name="winBrush" minOccurs="1">
            <xs:annotation>
                <xs:documentation>윈도우 채우기</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:attribute name="faceColor" type="hcf:RGBColorType" default="FFFFFF">
                    <xs:annotation>
                        <xs:documentation>면 색</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="hatchColor" type="hcf:RGBColorType" default="000000">
                    <xs:annotation>
                        <xs:documentation>무늬 색</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="hatchStyle">
                    <xs:annotation>
                        <xs:documentation>무늬 종류</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
379
KSX 6101:2024
code
Xml
<xs:restriction base="xs:string">
                            <xs:enumeration value="HORIZONTAL">
                                <xs:annotation>
                                    <xs:documentation>-----</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="VERTICAL">
                                <xs:annotation>
                                    <xs:documentation>|||||</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="BACK_SLASH">
                                <xs:annotation>
                                    <xs:documentation>\\\\\</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="SLASH">
                                <xs:annotation>
                                    <xs:documentation>/////</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CROSS">
                                <xs:annotation>
                                    <xs:documentation>+++++</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CROSS_DIAGONAL">
                                <xs:annotation>
                                    <xs:documentation>xxxxx</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="alpha" type="xs:float"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="gradation" minOccurs="1">
            <xs:annotation>
                <xs:documentation>그라데이션 효과</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="color" minOccurs="0" maxOccurs="unbounded">
                        <xs:annotation>
                            <xs:documentation>그라데이션 색</xs:documentation>
                        </xs:annotation>
                        <xs:complexType>
```---
**380**
**387/414**
KSX 6101:2024
```xml
                            <xs:attribute name="value" type="hcf:RGBColorType" use="required"/>
                        </xs:complexType>
                    </xs:element>
                </xs:sequence>
                <xs:attribute name="type">
                    <xs:annotation>
                        <xs:documentation>그라데이션 유형</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="LINEAR">
                                <xs:annotation>
                                    <xs:documentation>선형</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="RADIAL">
                                <xs:annotation>
                                    <xs:documentation>원형</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CONICAL"/>
                            <xs:enumeration value="SQUARE">
                                <xs:annotation>
                                    <xs:documentation>사각형</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="angle" type="xs:integer" default="90">
                    <xs:annotation>
                        <xs:documentation>그라데이션의 기울임 (시작각)</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="centerX" type="xs:integer" default="0">
                    <xs:annotation>
                        <xs:documentation>그라데이션의 가로 중심 (중심 X좌표)</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="centerY" type="xs:integer" default="0">
                    <xs:annotation>
                        <xs:documentation>그라데이션의 세로 중심 (중심 Y좌표)</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
381
KSX 6101:2024
code
Xml
<xs:attribute name="step" default="255">
                    <xs:annotation>
                        <xs:documentation>그라데이션 번짐 정도 (0~255)</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:minInclusive value="0"/>
                            <xs:maxInclusive value="255"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="colorNum" type="xs:nonNegativeInteger" default="2">
                    <xs:annotation>
                        <xs:documentation>그라데이션의 색 개수</xs:documentation>
                    </xs:annotation>
                </xs:attribute>
                <xs:attribute name="stepCenter" default="50">
                    <xs:annotation>
                        <xs:documentation>그라데이션 번짐 정도의 중심 (0~100)</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:integer">
                            <xs:minInclusive value="0"/>
                            <xs:maxInclusive value="100"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
                <xs:attribute name="alpha" type="xs:float"/>
            </xs:complexType>
        </xs:element>
        <xs:element name="imgBrush" minOccurs="1">
            <xs:annotation>
                <xs:documentation>그림으로 채우기</xs:documentation>
            </xs:annotation>
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="img" type="hcf:ImageType"/>
                </xs:sequence>
                <xs:attribute name="mode" default="TILE">
                    <xs:annotation>
                        <xs:documentation>채우기 유형</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="TILE">
                                <xs:annotation>
                                    <xs:documentation>바둑판식으로-모두</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="TILE_HORZ_TOP">
                                <xs:annotation>
                                    <xs:documentation>바둑판식으로-가로/위</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="TILE_HORZ_BOTTOM">
                                <xs:annotation>
                                    <xs:documentation>바둑판식으로-가로/아래</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="TILE_VERT_LEFT">
                                <xs:annotation>
                                    <xs:documentation>바둑판식으로-세로/왼쪽</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="TILE_VERT_RIGHT">
                                <xs:annotation>
                                    <xs:documentation>바둑판식으로-세로/오른쪽</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER">
                                <xs:annotation>
                                    <xs:documentation>가운데</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER_TOP">
                                <xs:annotation>
                                    <xs:documentation>가운데 위</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="CENTER_BOTTOM">
                                <xs:annotation>
                                    <xs:documentation>가운데 아래</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="LEFT_CENTER">
                                <xs:annotation>
                                    <xs:documentation>왼쪽 가운데</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
383
390/414
KSX 6101:2024
code
Xml
<xs:enumeration value="LEFT_TOP">
                                <xs:annotation>
                                    <xs:documentation>왼쪽 위</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="LEFT_BOTTOM">
                                <xs:annotation>
                                    <xs:documentation>왼쪽 아래</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="RIGHT_CENTER">
                                <xs:annotation>
                                    <xs:documentation>오른쪽 가운데</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="RIGHT_TOP">
                                <xs:annotation>
                                    <xs:documentation>오른쪽 위</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="RIGHT_BOTTOM">
                                <xs:annotation>
                                    <xs:documentation>오른쪽 아래</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                            <xs:enumeration value="ZOOM">
                                <xs:annotation>
                                    <xs:documentation>크기에 맞추어</xs:documentation>
                                </xs:annotation>
                            </xs:enumeration>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:complexType>
        </xs:element>
    </xs:choice>
</xs:complexType>
<xs:complexType name="KeyEncryptionType">
    <xs:sequence>
        <xs:element name="derivationKey">
            <xs:complexType>
                <xs:attribute name="algorithm" type="xs:string"/>
                <xs:attribute name="size" type="xs:nonNegativeInteger"/>
                <xs:attribute name="count" type="xs:nonNegativeInteger"/>
                <xs:attribute name="salt" type="xs:base64Binary"/>
            </xs:complexType>
        </xs:element>
384
KSX 6101:2024
code
Xml
<xs:element name="hash" type="xs:base64Binary"/>
    </xs:sequence>
</xs:complexType>
<xs:complexType name="MetaTagType" mixed="true"/>
</xs:schema>

385
KSX 6101:2024
부속서 G
(규정)
MasterPage XML 스키마
code
Xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:hcf="http://www.owpml.org/owpml/2024/core" xmlns:hp="http://www.owpml.org/owpml/2024/hp" xmlns:hpf="http://www.owpml.org/owpml/2024/hpf" targetNamespace="http://www.owpml.org/owpml/2024/hpf" elementFormDefault="qualified">
    <xs:import namespace="http://www.owpml.org/owpml/2024/hp" schemaLocation="HwpFile.xsd"/>
    <xs:import namespace="http://www.owpml.org/owpml/2024/core" schemaLocation="Core.xsd"/>
    <xs:element name="masterPage">
        <xs:annotation>
            <xs:documentation>마스터 페이지</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="subList" type="hp:ParaListType"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:int" use="required"/>
            <xs:attribute name="type" default="BOTH">
                <xs:annotation>
                    <xs:documentation>마스터 페이지 종류</xs:documentation>
                </xs:annotation>
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:enumeration value="BOTH"/>
                        <xs:enumeration value="EVEN"/>
                        <xs:enumeration value="ODD"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:attribute>
            <xs:attribute name="pageNumber">
                <xs:annotation>
                    <xs:documentation>페이지 번호</xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="width" type="xs:nonNegativeInteger" use="required"/>
            <xs:attribute name="height" type="xs:nonNegativeInteger" use="required"/>
            <xs:attribute name="header" type="hpf:HeaderFooterType"/>
            <xs:attribute name="footer" type="hpf:HeaderFooterType"/>
            <xs:attribute name="footNote" type="hpf:NoteType"/>
            <xs:attribute name="endNote" type="hpf:NoteType"/>
            <xs:attribute name="pageBorderFill" type="hpf:PageBorderFillType"/>
            <xs:attribute name="pageNumberPosition" type="hpf:PageNumPosType"/>
            <xs:attribute name="pageDblSided" default="false" type="xs:boolean"/>
            <xs:attribute name="pageFrontFirst" default="false" type="xs:boolean"/>
            <xs:attribute name="pageBindingType" default="DEFAULT" type="hpf:PageBindingType"/>
            <xs:attribute name="orientation" default="PORTRAIT">
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:enumeration value="PORTRAIT"/>
                        <xs:enumeration value="LANDSCAPE"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:complexType name="HeaderFooterType">
        <xs:attribute name="id" type="xs:nonNegativeInteger"/>
        <xs:attribute name="type" default="BOTH">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="BOTH"/>
                    <xs:enumeration value="EVEN"/>
                    <xs:enumeration value="ODD"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="NoteType">
        <xs:attribute name="id" type="xs:nonNegativeInteger"/>
    </xs:complexType>
    <xs:complexType name="PageBorderFillType">
        <xs:complexContent>
            <xs:extension base="hp:BorderFillType">
                <xs:attribute name="textBorder" type="xs:boolean" default="false"/>
                <xs:attribute name="headerInside" type="xs:boolean" default="false"/>
                <xs:attribute name="footerInside" type="xs:boolean" default="false"/>
                <xs:attribute name="fillArea" default="PAPER">
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="PAPER"/>
                            <xs:enumeration value="PAGE"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="PageNumPosType">
        <xs:attribute name="id" type="xs:nonNegativeInteger"/>
        <xs:attribute name="pageNum" type="xs:nonNegativeInteger"/>
        <xs:attribute name="type" default="NONE">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="LEFT_TOP"/>
                    <xs:enumeration value="CENTER_TOP"/>
                    <xs:enumeration value="RIGHT_TOP"/>
                    <xs:enumeration value="LEFT_BOTTOM"/>
                    <xs:enumeration value="CENTER_BOTTOM"/>
                    <xs:enumeration value="RIGHT_BOTTOM"/>
                    <xs:enumeration value="OUTSIDE_TOP"/>
                    <xs:enumeration value="OUTSIDE_BOTTOM"/>
                    <xs:enumeration value="INSIDE_TOP"/>
                    <xs:enumeration value="INSIDE_BOTTOM"/>
                    <xs:enumeration value="NONE"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
    </xs:complexType>
    <xs:simpleType name="PageBindingType">
        <xs:restriction base="xs:string">
            <xs:enumeration value="DEFAULT"/>
            <xs:enumeration value="OPPOSITE"/>
            <xs:enumeration value="TO_RIGHT"/>
            <xs:enumeration value="TO_LEFT"/>
        </xs:restriction>
    </xs:simpleType>
</xs:schema>
388
KSX 6101:2024
부속서 H
(규정)
수식 스크립트
<a name="s-1-1-sec"></a>
1.1 수식 버전
이 문서를 기준으로 수식 스크립트의 최신 버전은 6.0이다.
OWPML 본문 내에서는 수식 버전을 다음과 같이 표기한다.
Equation Version 60
<a name="s-1-2-sec"></a>
1.2 항의 구분 및 인식
수식에서 항(토큰)의 구분은 공백(Space, Tab)이나 줄바꿈으로 한다. 만약 공백을 포함한 여러 항을 하나의 항으로 인식하기 위해서는 {}를 사용해야 한다.
입력	결과
a over 2x^2 + y	a / (2x^2) + y
a over {2x^2 + y}	a / (2x^2 + y)
수식에서 한 항이 9자를 넘어가면 수식 스크립트 엔진은 이를 2개의 항으로 분리하여 인식한다. 9자 이상의 항을 하나의 항으로 처리하기 위해서는 따옴표(")를 두 항의 앞뒤에 사용해야 한다.
입력	결과
1234567890 over 5	123456789 * (0/5)
"1234567890" over 5	1234567890 / 5
<a name="s-1-3-sec"></a>
1.3 수식에 쓰이는 글씨체
기본적으로 수식 편집기에서 입력하는 로마자는 이탤릭체로 바뀌어 표현된다. 하지만 로만(영문·수식)체를 쓸 때에는 로만체 전환 명령어인 rm을 앞세워야 한다. 또 볼드체를 입력하기 위해서는 명령어 bold를 앞세운다.
기본: 이탤릭체
rm: 로만체
it: 로만체 입력 중 이탤릭체로 변경
bold: 볼드체
389
KSX 6101:2024
<a name="s-1-3-1-sec"></a>
1.3.1 예제
<a name="s-1-3-1-1-sec"></a>
1.3.1.1 기본
| 입력 | Equation font test |
|---|---|
| 결과 | Equation font test |
<a name="s-1-3-1-2-sec"></a>
1.3.1.2 로만체 - 이탤릭체
| 입력 | Equation rm font it test |
|---|---|
| 결과 | Equation font test |
<a name="s-1-3-1-3-sec"></a>
1.3.1.3 볼드체
| 입력 | rm Equation - bold Editor |
|---|---|
| 결과 | Equation - Editor |
<a name="s-1-4-White"></a>
1.4 White Space 표현
<a name="s-1-4-1-sec"></a>
1.4.1 공백 및 줄바꿈
수식 스크립트 엔진은, 공백(Space), 줄바꿈 등을 항을 구분하는 역할로만 쓰이며 화면 표시에는 사용되지 않고 무시된다. 수식 결과에 공백을 표시하기 위해서는 ~나 "를 사용해야 한다. 따옴표(")는 여러 개의 공백이 들어간 항을 표현할 때에도 사용될 수 있다. 줄바꿈은 #을 사용해서 표현할 수 있다.
입력	수식~편집기" "예제
결과	수식 편집기 예제
입력	"2차 방정식의 해법에는 인수분해에 의한 해법과 근의 공식에 의한 해법이 있다."
결과	2차 방정식의 해법에는 인수분해에 의한 해법과 근의 공식에 의한 해법이 있다.
<a name="s-1-4-2-sec"></a>
1.4.2 세로 칸 맞춤(&)
세로 칸 맞춤은 맞추고자 하는 기준 글자 앞에 &를 입력해 주어야 한다. 즉 글자 앞에서 <Tab>을 누른 것과 같은 효과를 준다.
입력	420 = 2 times 210 # = 2 times 2 times 105 # = 2^2 times 3 times 35 # = 2^2 times 3 times 5 times 7
결과	420 = 2 × 210<br>= 2 × 2 × 105<br>= 2² × 3 × 35<br>= 2² × 3 × 5 × 7
390
KSX 6101:2024
입력	420 &= 2 times 210 # &= 2 times 2 times 105 # &= 2^2 times 3 times 35 # &= 2^2 times 3 times 5 times 7
결과	420 = 2 × 210<br>      = 2 × 2 × 105<br>      = 2² × 3 × 35<br>      = 2² × 3 × 5 × 7
<a name="s-1-5-sec"></a>
1.5 예약어 및 명령어
예약어 및 명령어는 몇몇 예약어를 제외하고 기본적으로 대소문자를 구분하지 않는다. 대소문자를 구분하는 예약어인 경우 설명에 이를 명시한다.
<a name="s-1-5-1-sec"></a>
1.5.1 따옴표(")
글자 길이가 긴 단어나 공백을 포함한 문장을 하나로 묶기 위해 사용되는 예약어
<a name="s-1-5-2-OVER"></a>
1.5.2 분수 (OVER)
분수는 기본적으로 가운데 맞춤으로 정렬한다. 오른쪽이나 왼쪽 맞춤을 쓰려면 빈칸 넣기인 <_>나 <.>를 이용한다.
입력	1 OVER 1000 + {1<_> OVER 1000} + {1<.> OVER 1000}
결과	1/1000 + 1/1000 + 1/1000
391
KSX 6101:2024
<a name="s-1-5-6-ATOP"></a>
1.5.6 위 아래 (ATOP)
OVER 명령어와 같지만 분수를 나타내는 가로선을 생략해 준다.
<a name="s-1-5-9-SQRT"></a>
1.5.9 제곱근 (SQRT)
SQRT 대신하여 ROOT라고 입력해도 같은 결과를 얻을 수 있다.
입력	x SQRT {y+z}
결과	x√(y+z)
392
KSX 6101:2024
<a name="s-1-5-10-LEFT"></a>
1.5.10 LEFT, RIGHT
LEFT와 RIGHT는 양쪽에서 하나의 쌍을 이루도록 한다. 만약 한쪽을 생략하고 싶을 경우 생략하려는 쪽에 마침표(.)를 넣는다.
입력	LEFT ( a+b over x+y RIGHT )
결과	( (a+b)/(x+y) )
입력	LEFT . a+b over x+y RIGHT }
결과	(a+b)/(x+y) }
<a name="s-1-5-11-BIGG"></a>
1.5.11 BIGG 기호
입력	LEFT { a+b OVER a-b BIGG / x+y OVER x-y RIGHT }
결과	{ (a+b)/(a-b) / (x+y)/(x-y) }
<a name="s-1-5-12-INT"></a>
1.5.12 적분 (INT, OINT)
입력	INT _-inf ^inf {1 over x} dx
결과	∫[-inf, inf] (1/x) dx
입력	OINT _C {1 over x} dx
결과	∮[C] (1/x) dx
입력	OINT _C_l {1 over x} dx
결과	∮[C_l] (1/x) dx
<a name="s-1-5-13-lim"></a>
1.5.13 극한 (lim, Lim)
본 예약어는 대소문자를 구분하므로, 반드시 대소문자를 정확하게 표기해야 한다.
입력	lim _{x->0} {1 over x}
결과	lim[x→0] (1/x)
입력	Lim _{x->0} {1 over x}
결과	Lim[x→0] (1/x)
<a name="s-1-5-14-SUM"></a>
1.5.14 합 (SUM)
입력	x = SUM _{i=0} ^{inf} {x sub i}
결과	x = Σ[i=0, inf] x_i
<a name="s-1-5-15-UNION"></a>
1.5.15 합집합 (UNION), 교집합 (INTER), 곱집합 (PROD)
입력	A UNION B
결과	A ∪ B
입력	A INTER B
결과	A ∩ B
393
401/414
KSX 6101:2024
입력	A PROD B
결과	A × B
<a name="s-1-5-16-REL"></a>
1.5.16 상호관계 (REL)
두 항 간의 상호관계를 상세히 표현할 수 있게 하는 기능으로 두 항을 연결하는 화살표의 위/아래에 관계식 등의 내용을 삽입할 수 있다.
입력	A REL Lrarrow ^{abc} _{xyz} B
결과	A ←[xyz, abc] B
입력	rm PbO_2 + 2H_2 SO_4 + Pb REL lrarrow ^{충전} _{방전} 2PbSO_4 + 2H_2 O
결과	PbO₂ + 2H₂SO₄ + Pb ↔[방전, 충전] 2PbSO₄ + 2H₂O
<a name="s-1-5-17-BUILDREL"></a>
1.5.17 BUILDREL
Relation 이동과 유사한 기능으로 화살표 아래 부분의 내용을 생략할 수 있다.
입력	A BUILDREL Lrarrow ^{f(a) + g(a) + h(a)} B
결과	A ←[f(a)+g(a)+h(a)] B
입력	rm RCH_2 CH_2 COSCoA BUILDREL rarrow-2H- RCH=CHCOSCqA
결과	RCH₂CH₂COSCoA →[-2H-] RCH=CHCHSCoA
<a name="s-1-5-18-PILE"></a>
1.5.18 세로 쌓기 (PILE, LPILE, RPILE)
위에 있는 글자를 기준으로 가운데(PILE), 왼쪽(LPILE), 오른쪽(RPILE) 맞춤을 선택할 수 있다.
입력	PILE {tA3 # tA2 # t}
결과	tA3<br>tA2<br>t
<a name="s-1-5-19-CASES"></a>
1.5.19 경우 (CASES)
여러 개의 행 전체를 나타내는 큰 중괄호 {는 상황에 따라 그 크기가 자동으로 확대되어 표시된다.
| 입력 | |sign(x)| = CASES {1 &x>0 # 0 &x=0 # -1 &x<0} |
|---|---|
| 결과 | |sign(x)| = { 1 (x>0)<br>                 { 0 (x=0)<br>                 { -1 (x<0) |
<a name="s-1-5-20-CHOOSE"></a>
1.5.20 조합 (CHOOSE, BINOM)
입력	n CHOOSE x
결과	(n C x)
입력	BINOM n x
결과	(n, x)
<a name="s-1-5-21-MATRIX"></a>
1.5.21 행렬 (MATRIX, PMATRIX, BMATRIX, DMATRIX)
matrix는 행(row) 단위로 입력하는 방법과, 칸(column) 단위로 입력하는 방법이 있다.
col을 넣어 내용을 칸 단위로 입력할 때는 각 칸 앞에 col(가운데 맞춤) 대신 lcol(왼쪽 맞춤), rcol(오른쪽 맞춤)을 써서 위치를 정할 수도 있다.
matrix 대신에 pmatrix를 쓰면 소괄호 ( ), bmatrix를 쓰면 대괄호 [ ], dmatrix를 쓰면 세로줄 | |을 행렬 양옆에 각각 표시해 준다.
입력	matrix { a_1 & b_1 & c_1 & d_1 # a_2 & b_2 & c_2 & d_2 # a_3 & b_3 & c_3 & d_3 # a_4 & b_4 & c_4 & d_4 }
결과	a₁ b₁ c₁ d₁<br>a₂ b₂ c₂ d₂<br>a₃ b₃ c₃ d₃<br>a₄ b₄ c₄ d₄
395
KSX 6101:2024
입력	matrix { lcol {a_1 # abc_2 # a_3 # a_4} col {b_1 # b_2 # b_3 # b_4} col {c_1 # c_2 # c_3 # c_4} col {d_1 # d_2 # d_3 # d_4} }
결과	a₁      b₁ c₁ d₁<br>abc₂  b₂ c₂ d₂<br>a₃      b₃ c₃ d₃<br>a₄      b₄ c₄ d₄
MATRIX	PMATRIX	BMATRIX	DMATRIX
a₁ b₁ c₁<br>a₂ b₂ c₂	(a₁ b₁ c₁)<br>(a₂ b₂ c₂)	[a₁ b₁ c₁]<br>[a₂ b₂ c₂]	|a₁ b₁ c₁|<br>|a₂ b₂ c₂|
<a name="s-1-5-22-UNDERLINE"></a>
1.5.22 밑줄(UNDERLINE), 윗줄(OVERLINE)
입력	UNDERLINE {x+y} + OVERLINE {y+z}
결과	<u>x+y</u> + overline(y+z)
<a name="s-1-5-23-LSUB"></a>
1.5.23 왼쪽 아래첨자 (LSUB)
입력	x LSUB y
결과	<sub>y</sub>x
<a name="s-1-5-24-LSUP"></a>
1.5.24 왼쪽 위첨자 (LSUP)
입력	x LSUP y ~~(y>x)
결과	<sup>y</sup>x (y>x)
<a name="s-1-5-25-LADDER"></a>
1.5.25 최소공배수/최대공약수 함수 (LADDER)
최소공배수, 최대공약수를 구할 때 사용하는 명령어로 마지막 행의 마지막 열은 인자로 인식하지 않는다.
입력	LADDER {2&12&28#2&6&14#3&7&}
결과	2
396
403/414
KSX 6101:2024
<a name="s-1-5-26-SLADDER"></a>
1.5.26 2진수 변환 함수 (SLADDER)
10진수를 2진수로 변환할 때 사용하는 명령어로 첫 번째 행의 마지막 열과 마지막 행의 마지막 열은 인자로 인식하지 않는다.
입력	SLADDER{ 2&12& # 2&6&0 # 2&3&0 # 1&1 }
결과	2
<a name="s-1-5-27-LONGDIV"></a>
1.5.27 거꾸로 나눗셈 (LONGDIV)
나눗셈을 표현할 때 사용하는 명령어이다.
Layout을 맞추지 않은 방법으로도 나눗셈을 입력할 수 있으며 자동으로 Layout을 맞추려면 ~을 이용하여 자동으로 Layout을 맞출 수 있다. 마지막 인자에 숫자가 아닌 문자가 들어가면 자동 Layout을 하지 않는다.
입력	LONGDIV {6} {422} {2532#24#13#12#12#12#0}
결과	(복잡한 나눗셈 형식)
입력	LONGDIV {6} {422} {2532#24#~13#~12#~12#~12#~0}
결과	(자동 정렬된 복잡한 나눗셈 형식)
<a name="s-1-5-28-COLOR"></a>
1.5.28 색상 (COLOR)
부분적으로 Color를 바꾸기 위해 사용하는 명령어이다.
첫 번째 인자에 (R, G, B) 색상값이 들어간다.
입력	{COLOR {255,0,255}} {3} over {4}
결과	<span style="color:magenta">3</span>/4
<a name="s-1-5-29-sec"></a>
1.5.29 글자장식
글자 또는 단어에 간단한 명령어를 앞세워 여러 가지 글자 장식을 할 수 있다. 해당 명령어를 먼저 입력한 후 글자는 나중에 입력한다.
다음의 HAT, CHECK, ARCH, TILDE 명령어는 영문 3자까지만 감쌀 수 있다.
397
KSX 6101:2024
입력	결과	입력	결과
acute A	Á	bar A	Ā
grave A	À	vec A	A⃗
dot A	Ȧ	dyad A	̿A
ddot A	Ä	under A	<u>A</u>
hat A	Â	arch A	⌒A
hat AA	AÂ	arch AA	⌒AA
hat AAA	AÂA	arch AAA	⌒AAA
check A	Ǎ	tilde A	Ã
check AA	AǍ	tilde AA	AÃ
405/414
<a name="s-1-5-30-NOT"></a>
1.5.30 부정 (NOT)
글자 앞에 not을 붙이면 그 글자에 사선을 그어준다.
입력	u not== 전체집합
결과	u ≠ 전체집합
<a name="s-1-5-31-sec"></a>
1.5.31 그리스 문자
| Alpha | α | nu | ν | aleph | א |
|---|---|---|---|---|---|
| Beta | β | xi | ξ | hbar | ħ |
| Gamma | Γ | gamma | γ | IMATH | ı |
| Delta | Δ | delta | δ | JMATH | j |
| Epsilon | E | epsilon | ε | MHO | ℧ |
| Zeta | Z | zeta | ζ | ELL, LITER | ℓ |
| Eta | H | eta | η | WP | ℘ |
| Theta | Θ | theta | θ | REAL | ℜ |
| Iota | I | iota | ι | IMAG | ℑ |
| Kappa | K | kappa | κ | ANGSTROM | Å |
| Lambda | Λ | lambda | λ | | |
| Mu | M | mu | μ | vartheta | ϑ |
| Nu | N | nu | ν | varpi | ϖ |
| Xi | Ξ | xi | ξ | varsigma | ς |
| Omicron | O | omicron | o | varupsilon | ϒ |
398
KSX 6101:2024
입력	결과	입력	결과	입력	결과
Pi	Π	pi	π	varphi	φ
Rho	P	rho	ρ	varepsilon	ε
Sigma	Σ	sigma	σ		
Tau	T	tau	τ		
Upsilon	Y	upsilon	υ		
Phi	Φ	phi	φ		
Chi	X	chi	χ		
Psi	Ψ	psi	ψ		
Omega	Ω	omega	ω		
<a name="s-1-5-32-sec"></a>
1.5.32 괄호
| 입력 | 결과 | 입력 | 결과 |
|---|---|---|---|
| LBRACE | { | RBRACE | } |
| LCEIL | ⌈ | RCEIL | ⌉ |
| LFLOOR | ⌊ | RFLOOR | ⌋ |
<a name="s-1-5-33-sec"></a>
1.5.33 적분 기호
| 입력 | 결과 | 입력 | 결과 |
|---|---|---|---|
| SMALLINT | ∫ | SMALLOINT | ∮ |
| INT, INTEGRAL | ∫ | OINT | ∮ |
<a name="s-1-5-34-sec"></a>
1.5.34 합, 관계, 집합 기호
| 입력 | 결과 | 입력 | 결과 | 입력 | 결과 |
|---|---|---|---|---|---|
| SMALLSUM | ∑ | SUM | ∑ | SUBSET | ⊂ |
SMCOPROD, AMALG	⨿	COPROD	∐	SUPERSET	⊃
SMALLPROD	∏	PROD	∏	SUBSETEQ	⊆
SMALLUNION, CUP	∪	UNION, BIGCUP	⋃	SUPSETEQ	supseteq
SMALLINTER, CAP	∩	INTER, BIGCAP	⋂	IN	∈
SQCUP	⊔	BIGSQCUP	⨆	OWNS, NI	∋
SQCAP	⊓	BIGSQCAP	⨅	SQSUBSET	⊑
OMINUS	⊖	BIGOMINUS	⨀	SQSUPSET	⊒
ODIV	⊘	BIGODIV	⨸	SQSUBSETEQ	⊑
OTIMES	⊗	BIGOTIMES	⨂	SQSUPSETEQ	⊒
OSLASH	⊘	BIGOSLASH	⨸	LE	≤
ODOT	⊙	BIGODOT	⨀	NOTIN	∉
UPLUS	⊎	BIGUPLUS	⨄	GE	≥
WEDGE, LAND	∧	BIGWEDGE	⋀	<	≺
VEE, LOR	∨	BIGVEE	⋁	>=	≻
<<	≪
>>	≫
LLL, <<<	⋘
GGG, >>>	⋙
<a name="s-1-5-35-sec"></a>
1.5.35 화살표
이 예약어는 대소문자를 구분하므로, 반드시 대소문자를 정확하게 표기해야 한다.
입력	결과	입력	결과	입력	결과
larrow	←	LARROW	⇐	nwarrow	↖
rarrow	→	RARROW	⇒	searrow	↘
uparrow	↑	UPARROW	⇑	nearrow	↗
downarrow	↓	DOWNARROW	⇓	swarrow	↙
udarrow	↕	UDARROW	⇕	hookleft	↩
lrarrow	↔	LRARROW	⇔	hookright	↪
mapsto	↦	vert	|	VERT	‖
<a name="s-1-5-36-sec"></a>
1.5.36 연산/논리 기호
예약어 image, prime은 대소문자를 구분하므로 반드시 대소문자를 정확하게 표기해야 한다.
입력	결과	입력	결과	입력	결과
PLUSMINUS	±	EMPTYSET	∅	SIM	∼
MINUSPLUS	∓	THEREFORE	∴	APPROX	≈
TIMES	×	BECAUSE	∵	SIMEQ	≃
DIV, DIVIDE	÷	IDENTICAL	≡	CONG	≅
CIRC	∘	BIGCIRC	○	EQUIV	≡
BULLET	•	EXIST	∃	ASYMP	≍
DEG	°	NEQ, !=	≠	ISO	≅
AST	*	DOTEQ	≐	DIAMOND	⋄
STAR	★	image	ℑ	REIMAGE	ℜ
DSUM	⨄	FORALL	∀	prime	′
PARTIAL	∂	INF	∞	LNOT	¬
PROPTO	∝	XOR	⊕		
DAGGER	†	DDAGGER	‡		
<a name="s-1-5-37-sec"></a>
1.5.37 기타기호
입력	결과	입력	결과	입력	결과
CDOTS	⋯	LDOTS	…	VDOTS	⋮
DDOTS	⋱	TRIANGLE	△	TRIANGLED	▽
ANGLE	∠	MSANGLE	∡	SANGLE	∠
RTANGLE	∟	VDASH	⊫	HLEFT	⊣
BOT	⊥	TOP	⊤	MODELS	⊧
LAPLACE	ℒ	CENTIGRADE	℃	FAHRENHEIT	℉
LSLANT	/	RSLANT	\	ATT	@
HUND	%	THOU	‰	WELL	#
BASE	♭	BENZENE	⌬	OHM	Ω
401
KSX 6101:2024
해 설
이 해설은 이 표준과 관련된 사항을 설명하는 것으로 표준의 일부는 아니다.
1 개요
1.1 제정의 취지
이 표준은 국내 유통되고 있는 아래아한글 워드프로세서 문서(HWP)에 대한 100% 호환성을 갖는 표준적 전자문서 처리기술(XML)을 이용한 개방형 표준으로의 마이그레이션을 목적으로 한다. 이로 인하여 기술적 의존에 대비한 장기보존문서에 대한 안정성을 확보하고 특정 회사의 기술 및 애플리케이션에 종속적이지 않으며 다양한 애플리케이션에서 해당 워드프로세서 문서를 지원하여 기술개발의 확대를 가져올 수 있다.
1.2 제정의 경위
제1차 표준개발위원회(2011년 3월): 국가표준(KS) 제정을 위해 표준개발위원회에서 제정 방법을 논의 함.
제2차 표준개발위원회(2011년 5월): 국가표준(KS) 제정을 위한 전문위원 구성
제3차 기술심의위원회(2011년 7월): 한글과컴퓨터 양왕현 위원이 표준안 발표 및 수렴안.
제4차 표준개발위원회(2011년 9월): 1차 표준개발위원회 회의록을 보완하여 국가표준(KS) 제정 예고고시 요청을 위한 심의회를 가짐.
제5차 표준개발위원회(2011년 11월): 예고고시외 추가로 의견 수렴을 위한 공개 공청회를 개최.
2 2차 개정
<a name="s-2-1-sec"></a>
2.1 개정의 취지
이 표준의 문서(HWP)에 추가된 기능 및 요소들에 대하여 기본 포맷을 정의하고 기존 내용을 보완하기 위해 개정을 시행하였다. 이번 개정에서는 문서 보호를 위한 신규 기능인 변경 추적, 암호, 전자 서명 항목이 추가되었으며, 문서 버전 관리를 위한 문서 이력, 문서 설정 정보 기록을 위한 구조가 추가되었다.
402
KSX 6101:2024
<a name="s-2-2-sec"></a>
2.2 개정의 경위
2011년 12월: 개방형 워드프로세서 마크업 언어(OWPML) 문서 구조 - 국가표준 제정
2015년 12월: 개방형 워드프로세서 마크업 언어(OWPML) 문서 구조 - 국가표준 개정
2016년 12월: JTC1/SC34(문서처리기준 및 처리언어) 전문위원회를 통하여 '개방형 워드프로세서 마크업 언어(OWPML) 문서 구조' 개정 상정
2017년 2월 28일: JTC1/SC34(문서처리기술 및 처리언어) 전문위원회에서 개정 표준안에 대한 1차 논의를 하였으며, 표준안의 내용을 검토
2017년 4월 20일: JTC1/SC34(문서처리기술 및 처리언어) 전문위원회에서 개정 표준안에 대한 2차 논의를 하였으며, 표준안의 내용을 검토
2017년 7월 6일: JTC1/SC34(문서처리기술 및 처리언어) 전문위원회에서 개정 표준안에 대한 3차 논의를 하였으며, 차후 전문위원회 개최 전 전문가로 구성된 작업반 활동을 통해 표준안의 내용을 검토하기로 결정함.
2017년 8월 3일: 작업반 회의를 통해 개정의 취지 항목을 추가하며 추가된 항목에 대한 검토를 받음. 이를 통해 용어정의와 추가된 기능의 인용에 대하여 수정함.
상기 과정을 통해 표준 개정안에 대한 검토를 하고 최종 수정본 작업을 완료함.
<a name="s-2-3-sec"></a>
2.3 주요 개정 내역
<a name="s-2-3-1-sec"></a>
2.3.1 적용범위
기존 적용범위에 암호화, 전자서명 변경, 추적 기능 등의 내용을 추가
<a name="s-2-3-2-sec"></a>
2.3.2 자구 수정
'어플리케이션, 그라데이션, 디렉토리, 윈도우' 등의 용어를 '애플리케이션, 그러데이션, 디렉터리, 윈도' 등의 용어로 수정
<a name="s-2-3-3-sec"></a>
2.3.3 추가항목
언어 형식에 라인 align, 단락 정렬
<a name="s-2-3-4-KS"></a>
2.3.4 KS A 0001:2015 반영
이번의 표준 개정 내용 중 KS A 0001(표준의 서식과 작성방법)이 반영된 주요 내용을 요약하면 다음과 같다.
머리말, 개요의 추가
인용표준의 변경
3 이번 개정 (3차 개정)
<a name="s-3-1-sec"></a>
3.1 개정의 취지
이번 개정은 표준 개방형 텍스트 문서 규격(OWPML)에 대해 일부 새롭게 추가된 기능 및 요소들에 대하여 기본 포맷을 확장하여 개정하였다. 기존 수요자들이 해당 표준을 참조하거나 도입하여 실제 개발하는 데 많이 어려워한 부분을 수용하고 보완하여, 규격에 대한 상세한 설명과 표준 항목별 샘플 코드를 추가하였다. 명확하게 설명되지 못하였던 부분들에 대해서 자세한 설명을 추가하여 표준의 수요자들이 보다 용이하게 활용하고 적용할 수 있도록 하였다.
또한 확장성 제공을 위해 제공되는 메타데이터 추가 정의 방법에 대하여 수요자들의 이해를 돕기 위해 기존 내용을 보완하고 상세 설명을 추가하여 시스템 통합 또는 애플리케이션 개발자 등 이 표준 수요자들의 이해를 돕기 위해 개정을 시행하였다.
이번 개정에서는 텍스트 문서를 구성하는 구성 요소를 추가하였으며, 이를 구현하기 위해 사용되는
403
KSX 6101:2024
포맷의 수정, 추가된 마크업 부분을 개정 및 새롭게 추가 정의하였다. 또한 이에 따른 하위 호환성에도 문제가 발생하지 않도록 개정 시 고려하였다.
<a name="s-3-2-sec"></a>
3.2 개정의 경위
2021년 11월: '개방형 워드프로세서 마크업 언어(OWPML) 문서 구조' 학계, 산업계 관련 전문가 대상 설명회 및 공청회 개최를 통한 의견 수렴
2021년 11월: '개방형 워드프로세서 마크업 언어(OWPML) 문서 구조' JTC1/SC34(문서처리기준 및 처리언어) 전문위원회에서 개정 표준안 초안 제출
상기 과정을 통해 표준 개정안에 대한 검토를 하고 최종 수정본 작업을 완료함.
<a name="s-3-3-sec"></a>
3.3 주요 개정 내용
<a name="s-3-3-1-sec"></a>
3.3.1 적용범위
문서 전반에 상세한 설명을 추가하였다.
<a name="s-3-3-2-sec"></a>
3.3.2 자구 수정
사용해야 한다, 권고한다, 하지 말아야 한다 등 표준 내용을 명확하게 파악할 수 있도록 표준형식에 맞춰 문서 전반 개정
<a name="s-3-3-3-sec"></a>
3.3.3 추가항목
문서 전반에 상세한 설명을 추가하였으며, 항목별 샘플 예제를 추가하여 수요자의 이해를 돕고자 개정하였다.
<a name="s-3-3-4-KS"></a>
3.3.4 KS A 0001:2023 반영
이번의 표준 개정 내용 중 KS A 0001(표준의 서식과 작성방법)이 반영된 주요 내용을 요약하면 다음과 같다.
머리말, 해설의 정형문 수정
3절 용어와 정의에서 참고 추가
