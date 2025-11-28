#!/usr/bin/env python3
"""
실험 1: charPr ID 범위 테스트
============================
목적: charPr ID가 특정 범위를 벗어나면 스타일이 적용되지 않는지 확인
방법: 작동하는 템플릿 파일을 복사하고, header.xml과 section0.xml만 수정

전략: 
- validator/tier_test/tier1/with_header/ 에서 작동하는 HWPX 복사
- Contents/header.xml의 charPr 정의만 추가 (기존 유지)
- Contents/section0.xml의 본문 내용만 수정
- 나머지는 모두 그대로 유지
"""

import zipfile
import re
from pathlib import Path

# 경로 설정
BASE_DIR = Path(__file__).parent.parent
# 머리말/꼬리말 있는 작동하는 HWPX 파일 사용
TEMPLATE_HWPX = BASE_DIR / "validator" / "tier_test" / "tier1" / "(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# 테스트할 charPr ID들과 해당 글자 크기 (구분을 위해)
TEST_CASES = [
    # (charPr ID, 글자 크기 pt, 설명)
    (0, 10, "10pt - ID 0 (기본)"),
    (1, 11, "11pt - ID 1"),
    (5, 14, "14pt - ID 5"),
    (8, 18, "18pt - ID 8 (경계)"),
    (9, 22, "22pt - ID 9 (경계+1)"),
    (10, 26, "26pt - ID 10"),
    (15, 30, "30pt - ID 15"),
    (20, 36, "36pt - ID 20"),
]


def modify_header_xml(original_xml: str) -> str:
    """
    기존 header.xml에서 charProperties 섹션만 수정
    - 기존 charPr들은 유지 (ID 0-8 등 기본 스타일)
    - 테스트용 charPr 추가 (ID 9, 10, 15, 20)
    """
    # 테스트용 charPr 생성 (ID 9 이상만 - 기존에 없을 것으로 예상)
    new_charpr_items = []
    for char_id, pt_size, _ in TEST_CASES:
        if char_id >= 9:  # 기존에 없을 것으로 예상되는 ID만
            height = pt_size * 100  # HWPUNIT (pt * 100)
            # 빨간색으로 설정하여 적용 여부 쉽게 확인
            new_charpr_items.append(f'''<hh:charPr id="{char_id}" height="{height}" textColor="#FF0000" shadeColor="none" useFontSpace="0" useKerning="0" symMark="NONE" borderFillIDRef="1">
<hh:fontRef hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>
<hh:ratio hangul="100" latin="100" hanja="100" japanese="100" other="100" symbol="100" user="100"/>
<hh:spacing hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>
<hh:relSz hangul="100" latin="100" hanja="100" japanese="100" other="100" symbol="100" user="100"/>
<hh:offset hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>
<hh:underline type="NONE" shape="SOLID" color="#000000"/>
<hh:strikeout shape="NONE" color="#000000"/>
<hh:outline type="NONE"/>
<hh:shadow type="NONE" color="#B2B2B2" offsetX="10" offsetY="10"/>
</hh:charPr>''')
    
    if not new_charpr_items:
        return original_xml
    
    new_charpr_block = "\n".join(new_charpr_items)
    
    # </hh:charProperties> 앞에 새 charPr 삽입
    modified = original_xml.replace(
        "</hh:charProperties>",
        new_charpr_block + "\n</hh:charProperties>"
    )
    
    # itemCnt 업데이트 (정규식으로)
    def update_itemcnt(match):
        old_cnt = int(match.group(1))
        new_cnt = old_cnt + len([c for c in TEST_CASES if c[0] >= 9])
        return f'<hh:charProperties itemCnt="{new_cnt}">'
    
    modified = re.sub(
        r'<hh:charProperties itemCnt="(\d+)">',
        update_itemcnt,
        modified
    )
    
    return modified


def create_test_section0_xml() -> str:
    """테스트 문단들을 포함한 section0.xml 생성"""
    
    # 각 charPr ID에 대해 테스트 문단 생성
    paragraphs = []
    for i, (char_id, pt_size, label) in enumerate(TEST_CASES):
        text = f"[charPrIDRef={char_id}] 예상: {label}"
        # ID 9 이상은 빨간색으로 정의했으므로 색상으로도 구분 가능
        color_note = " (빨간색이어야 함)" if char_id >= 9 else ""
        paragraphs.append(f'''<hp:p id="{i + 10}" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="{char_id}">
<hp:t>{text}{color_note}</hp:t>
</hp:run>
</hp:p>''')
    
    para_block = "\n".join(paragraphs)
    
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<hs:sec xmlns:ha="http://www.hancom.co.kr/hwpml/2011/app" xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph" xmlns:hs="http://www.hancom.co.kr/hwpml/2011/section" xmlns:hc="http://www.hancom.co.kr/hwpml/2011/core" xmlns:hh="http://www.hancom.co.kr/hwpml/2011/head" xmlns:hm="http://www.hancom.co.kr/hwpml/2011/master-page">
<hp:p id="0" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="0">
<hp:secPr id="" textDirection="HORIZONTAL" spaceColumns="1134" tabStop="8000" tabStopVal="4000" tabStopUnit="HWPUNIT" outlineShapeIDRef="1" memoShapeIDRef="0" textVerticalWidthHead="0" masterPageCnt="0">
<hp:grid lineGrid="0" charGrid="0" wonggojiFormat="0"/>
<hp:startNum pageStartsOn="BOTH" page="0" pic="0" tbl="0" equation="0"/>
<hp:visibility hideFirstHeader="0" hideFirstFooter="0" hideFirstMasterPage="0" border="SHOW_ALL" fill="SHOW_ALL" hideFirstPageNum="0" hideFirstEmptyLine="0" showLineNumber="0"/>
<hp:lineNumberShape restartType="0" countBy="0" distance="0" startNumber="0"/>
<hp:pagePr landscape="WIDELY" width="59528" height="84186" gutterType="LEFT_ONLY">
<hp:margin header="2834" footer="2834" gutter="0" left="5669" right="5669" top="4251" bottom="4251"/>
</hp:pagePr>
<hp:footNotePr><hp:autoNumFormat type="DIGIT" userChar="" prefixChar="" suffixChar=")" supscript="0"/><hp:noteLine length="-1" type="SOLID" width="0.12 mm" color="#000000"/><hp:noteSpacing betweenNotes="283" belowLine="567" aboveLine="850"/><hp:numbering type="CONTINUOUS" newNum="1"/><hp:placement place="EACH_COLUMN" beneathText="0"/></hp:footNotePr>
<hp:endNotePr><hp:autoNumFormat type="DIGIT" userChar="" prefixChar="" suffixChar=")" supscript="0"/><hp:noteLine length="14692344" type="SOLID" width="0.12 mm" color="#000000"/><hp:noteSpacing betweenNotes="0" belowLine="567" aboveLine="850"/><hp:numbering type="CONTINUOUS" newNum="1"/><hp:placement place="END_OF_DOCUMENT" beneathText="0"/></hp:endNotePr>
<hp:pageBorderFill type="BOTH" borderFillIDRef="1" textBorder="PAPER" headerInside="0" footerInside="0" fillArea="PAPER"><hp:offset left="1417" right="1417" top="1417" bottom="1417"/></hp:pageBorderFill>
<hp:pageBorderFill type="EVEN" borderFillIDRef="1" textBorder="PAPER" headerInside="0" footerInside="0" fillArea="PAPER"><hp:offset left="1417" right="1417" top="1417" bottom="1417"/></hp:pageBorderFill>
<hp:pageBorderFill type="ODD" borderFillIDRef="1" textBorder="PAPER" headerInside="0" footerInside="0" fillArea="PAPER"><hp:offset left="1417" right="1417" top="1417" bottom="1417"/></hp:pageBorderFill>
</hp:secPr>
<hp:ctrl><hp:colPr id="" type="NEWSPAPER" layout="LEFT" colCount="1" sameSz="1" sameGap="0"/></hp:ctrl>
</hp:run>
<hp:run charPrIDRef="0">
<hp:t>===== charPr ID 범위 테스트 =====</hp:t>
</hp:run>
</hp:p>
{para_block}
<hp:p id="99" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="0">
<hp:t>===== 테스트 종료 =====</hp:t>
</hp:run>
</hp:p>
</hs:sec>'''


def main():
    # 템플릿 HWPX 확인
    if not TEMPLATE_HWPX.exists():
        print(f"❌ 템플릿 파일을 찾을 수 없습니다: {TEMPLATE_HWPX}")
        return
    
    print(f"📄 템플릿: {TEMPLATE_HWPX.name}")
    
    output_path = OUTPUT_DIR / "exp1_charpr_id_range.hwpx"
    
    # 템플릿 복사 후 수정
    with zipfile.ZipFile(TEMPLATE_HWPX, 'r') as src_zip:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as dst_zip:
            for item in src_zip.namelist():
                data = src_zip.read(item)
                
                # mimetype은 압축 없이
                if item == "mimetype":
                    dst_zip.writestr(item, data, compress_type=zipfile.ZIP_STORED)
                
                # header.xml 수정 (charPr 추가)
                elif item == "Contents/header.xml":
                    original_xml = data.decode('utf-8')
                    modified_xml = modify_header_xml(original_xml)
                    dst_zip.writestr(item, modified_xml.encode('utf-8'))
                    print(f"  ✏️ 수정: {item}")
                
                # section0.xml 교체 (테스트 본문)
                elif item == "Contents/section0.xml":
                    new_section = create_test_section0_xml()
                    dst_zip.writestr(item, new_section.encode('utf-8'))
                    print(f"  ✏️ 교체: {item}")
                
                # 나머지는 그대로 복사
                else:
                    dst_zip.writestr(item, data)
    
    print()
    print(f"✅ 생성 완료: {output_path}")
    print()
    print("테스트 케이스:")
    for char_id, pt_size, label in TEST_CASES:
        status = "새로 추가 (빨간색)" if char_id >= 9 else "기존 사용"
        print(f"  - charPrIDRef={char_id}: {label} [{status}]")
    print()
    print("확인 방법:")
    print("1. 한글에서 파일 열기")
    print("2. 각 줄의 글자 크기와 색상 확인")
    print("   - ID 0-8: 검정색 (기존 템플릿 스타일)")
    print("   - ID 9+: 빨간색이어야 함 (적용되면), 또는 검정/기본 크기 (무시되면)")
    print("3. ID 9 이상에서 스타일이 적용 안 되면 제한 발견")


if __name__ == "__main__":
    main()
