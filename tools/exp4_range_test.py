#!/usr/bin/env python3
"""
실험 4: 연속 ID 범위 테스트
==========================
발견: charPr ID는 0부터 연속이어야 함
질문: 최대 몇 개까지 가능한가?

테스트: ID 0~10 (11개 연속)
"""

import zipfile
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TEMPLATE_HWPX = BASE_DIR / "validator" / "tier_test" / "tier1" / "(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx"
OUTPUT_DIR = BASE_DIR / "output"

# 0~10 연속 (각각 다른 크기로)
TEST_CASES = [
    (0, 8, "#000000", "8pt 검정"),
    (1, 9, "#333333", "9pt 회색"),
    (2, 10, "#0000FF", "10pt 파랑"),
    (3, 11, "#0066FF", "11pt 하늘"),
    (4, 12, "#00FF00", "12pt 초록"),
    (5, 14, "#00FF66", "14pt 연두"),
    (6, 16, "#FF0000", "16pt 빨강"),
    (7, 18, "#FF6600", "18pt 주황"),
    (8, 20, "#FF00FF", "20pt 보라"),
    (9, 24, "#9900FF", "24pt 자주"),
    (10, 28, "#660000", "28pt 갈색"),
]


def build_charpr(char_id: int, height_pt: int, color: str) -> str:
    height = height_pt * 100
    return f'''<hh:charPr id="{char_id}" height="{height}" textColor="{color}" shadeColor="none" useFontSpace="0" useKerning="0" symMark="NONE" borderFillIDRef="1">
<hh:fontRef hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>
<hh:ratio hangul="100" latin="100" hanja="100" japanese="100" other="100" symbol="100" user="100"/>
<hh:spacing hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>
<hh:relSz hangul="100" latin="100" hanja="100" japanese="100" other="100" symbol="100" user="100"/>
<hh:offset hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>
<hh:underline type="NONE" shape="SOLID" color="#000000"/>
<hh:strikeout shape="NONE" color="#000000"/>
<hh:outline type="NONE"/>
<hh:shadow type="NONE" color="#B2B2B2" offsetX="10" offsetY="10"/>
</hh:charPr>'''


def replace_charproperties(original_xml: str) -> str:
    charpr_items = [build_charpr(cid, pt, color) for cid, pt, color, _ in TEST_CASES]
    new_charprops = f'''<hh:charProperties itemCnt="{len(TEST_CASES)}">
{chr(10).join(charpr_items)}
</hh:charProperties>'''
    
    return re.sub(
        r'<hh:charProperties itemCnt="\d+">.*?</hh:charProperties>',
        new_charprops,
        original_xml,
        flags=re.DOTALL
    )


def replace_styles(original_xml: str) -> str:
    new_styles = '''<hh:styles itemCnt="1">
<hh:style id="0" type="PARA" name="바탕글" engName="Normal" paraPrIDRef="0" charPrIDRef="0" nextStyleIDRef="0" langID="1042" lockForm="0"/>
</hh:styles>'''
    
    return re.sub(
        r'<hh:styles itemCnt="\d+">.*?</hh:styles>',
        new_styles,
        original_xml,
        flags=re.DOTALL
    )


def create_test_section0_xml() -> str:
    paragraphs = []
    for i, (char_id, pt_size, color, label) in enumerate(TEST_CASES):
        text = f"[ID={char_id}] {label}"
        paragraphs.append(f'''<hp:p id="{i + 10}" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="{char_id}">
<hp:t>{text}</hp:t>
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
<hp:t>===== 연속 ID 범위 테스트 (0~10) =====</hp:t>
</hp:run>
</hp:p>
{para_block}
</hs:sec>'''


def main():
    if not TEMPLATE_HWPX.exists():
        print(f"❌ 템플릿 없음")
        return
    
    output_path = OUTPUT_DIR / "exp4_range_0to10.hwpx"
    
    with zipfile.ZipFile(TEMPLATE_HWPX, 'r') as src_zip:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as dst_zip:
            for item in src_zip.namelist():
                data = src_zip.read(item)
                
                if item == "mimetype":
                    dst_zip.writestr(item, data, compress_type=zipfile.ZIP_STORED)
                elif item == "Contents/header.xml":
                    original = data.decode('utf-8')
                    modified = replace_charproperties(original)
                    modified = replace_styles(modified)
                    dst_zip.writestr(item, modified.encode('utf-8'))
                elif item == "Contents/section0.xml":
                    dst_zip.writestr(item, create_test_section0_xml().encode('utf-8'))
                else:
                    dst_zip.writestr(item, data)
    
    print(f"✅ 생성: {output_path}")
    print()
    print("ID 0~10 테스트:")
    for cid, pt, color, label in TEST_CASES:
        print(f"  {cid}: {label}")


if __name__ == "__main__":
    main()
