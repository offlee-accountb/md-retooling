#!/usr/bin/env python3
"""
실험 10: 개수 제한 테스트
=========================
가설: charPr 개수에 제한이 있음 (ID 값이 아니라 개수)
테스트: 18개 정의 (1~16, 18~20) - 17 빠짐
"""

import zipfile
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TEMPLATE_HWPX = BASE_DIR / "validator" / "tier_test" / "tier1" / "(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx"
OUTPUT_DIR = BASE_DIR / "output"

FONTS = ["한컴바탕", "맑은 고딕", "휴먼명조", "HY헤드라인M", "굴림", "돋움"]

# 18개: 1~16, 18~20 (17 빠짐)
TEST_CASES = [
    (1, 8, "#000000", 0, "8pt 한컴바탕"),
    (2, 9, "#111111", 1, "9pt 맑은고딕"),
    (3, 10, "#0000FF", 2, "10pt 휴먼명조"),
    (4, 11, "#0033FF", 3, "11pt HY헤드라인"),
    (5, 12, "#0066FF", 4, "12pt 굴림"),
    (6, 13, "#0099FF", 5, "13pt 돋움"),
    (7, 14, "#00FF00", 0, "14pt 한컴바탕"),
    (8, 15, "#33FF00", 1, "15pt 맑은고딕"),
    (9, 16, "#66FF00", 2, "16pt 휴먼명조"),
    (10, 17, "#99FF00", 3, "17pt HY헤드라인"),
    (11, 18, "#FF0000", 4, "18pt 굴림"),
    (12, 19, "#FF3300", 5, "19pt 돋움"),
    (13, 20, "#FF6600", 0, "20pt 한컴바탕"),  # 13번째
    (14, 22, "#FF9900", 1, "22pt 맑은고딕"),  # 14번째
    (15, 24, "#FF00FF", 2, "24pt 휴먼명조"),  # 15번째
    (16, 26, "#FF33FF", 3, "26pt HY헤드라인"),  # 16번째
    # 17 빠짐
    (18, 28, "#9900FF", 4, "28pt 굴림"),      # 17번째 정의
    (19, 30, "#6600FF", 5, "30pt 돋움"),      # 18번째 정의
    (20, 32, "#3300FF", 0, "32pt 한컴바탕"),  # 19번째 정의
]


def build_fontfaces() -> str:
    font_items = [f'<hh:font id="{i}" face="{f}" type="TTF" isEmbedded="0"><hh:typeInfo familyType="FCAT_GOTHIC" weight="5" proportion="3" contrast="2" strokeVariation="0" armStyle="0" letterform="2" midline="0" xHeight="4"/></hh:font>' for i, f in enumerate(FONTS)]
    fonts_block = "".join(font_items)
    langs = ["HANGUL", "LATIN", "HANJA", "JAPANESE", "OTHER", "SYMBOL", "USER"]
    return f'<hh:fontfaces itemCnt="{len(langs)}">{"".join(f"""<hh:fontface lang="{l}" fontCnt="{len(FONTS)}">{fonts_block}</hh:fontface>""" for l in langs)}</hh:fontfaces>'


def build_charpr(cid, pt, color, fref) -> str:
    return f'''<hh:charPr id="{cid}" height="{pt*100}" textColor="{color}" shadeColor="none" useFontSpace="0" useKerning="0" symMark="NONE" borderFillIDRef="1">
<hh:fontRef hangul="{fref}" latin="{fref}" hanja="{fref}" japanese="{fref}" other="{fref}" symbol="{fref}" user="{fref}"/>
<hh:ratio hangul="100" latin="100" hanja="100" japanese="100" other="100" symbol="100" user="100"/>
<hh:spacing hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>
<hh:relSz hangul="100" latin="100" hanja="100" japanese="100" other="100" symbol="100" user="100"/>
<hh:offset hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>
<hh:underline type="NONE" shape="SOLID" color="#000000"/>
<hh:strikeout shape="NONE" color="#000000"/>
<hh:outline type="NONE"/>
<hh:shadow type="NONE" color="#B2B2B2" offsetX="10" offsetY="10"/>
</hh:charPr>'''


def modify_header(original_xml: str) -> str:
    modified = re.sub(r'<hh:fontfaces itemCnt="\d+">.*?</hh:fontfaces>', build_fontfaces(), original_xml, flags=re.DOTALL)
    
    charpr_items = [build_charpr(cid, pt, color, fref) for cid, pt, color, fref, _ in TEST_CASES]
    new_charprops = f'<hh:charProperties itemCnt="{len(TEST_CASES)}">\n' + '\n'.join(charpr_items) + '\n</hh:charProperties>'
    modified = re.sub(r'<hh:charProperties itemCnt="\d+">.*?</hh:charProperties>', new_charprops, modified, flags=re.DOTALL)
    
    new_styles = '''<hh:styles itemCnt="1">
<hh:style id="0" type="PARA" name="바탕글" engName="Normal" paraPrIDRef="0" charPrIDRef="1" nextStyleIDRef="0" langID="1042" lockForm="0"/>
</hh:styles>'''
    modified = re.sub(r'<hh:styles itemCnt="\d+">.*?</hh:styles>', new_styles, modified, flags=re.DOTALL)
    
    return modified


def create_test_section0_xml() -> str:
    paragraphs = []
    for i, (cid, pt, color, fref, label) in enumerate(TEST_CASES):
        order = i + 1  # 정의 순서
        paragraphs.append(f'''<hp:p id="{100+i}" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="{cid}"><hp:t>[{order}번째 정의] ID={cid:2d}: {label}</hp:t></hp:run>
</hp:p>''')
    
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<hs:sec xmlns:ha="http://www.hancom.co.kr/hwpml/2011/app" xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph" xmlns:hs="http://www.hancom.co.kr/hwpml/2011/section" xmlns:hc="http://www.hancom.co.kr/hwpml/2011/core" xmlns:hh="http://www.hancom.co.kr/hwpml/2011/head" xmlns:hm="http://www.hancom.co.kr/hwpml/2011/master-page">
<hp:p id="0" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="1">
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
</hp:p>

<hp:p id="1" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="1"><hp:t>===== 19개 정의 테스트 (1~16, 18~20) - 17 빠짐 =====</hp:t></hp:run>
</hp:p>
<hp:p id="2" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="1"><hp:t>이전 결과: 14개 정의 시 13번째(ID=13)까지 OK, 14~15 미적용</hp:t></hp:run>
</hp:p>
{chr(10).join(paragraphs)}
</hs:sec>'''


def main():
    output_path = OUTPUT_DIR / "exp10_count_test.hwpx"
    
    with zipfile.ZipFile(TEMPLATE_HWPX, 'r') as src, zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as dst:
        for item in src.namelist():
            data = src.read(item)
            if item == "mimetype":
                dst.writestr(item, data, compress_type=zipfile.ZIP_STORED)
            elif item == "Contents/header.xml":
                dst.writestr(item, modify_header(data.decode('utf-8')).encode('utf-8'))
            elif item == "Contents/section0.xml":
                dst.writestr(item, create_test_section0_xml().encode('utf-8'))
            else:
                dst.writestr(item, data)
    
    print(f"✅ 생성: {output_path}")
    print(f"\n총 {len(TEST_CASES)}개 정의")
    print()
    print("테스트 케이스:")
    for i, (cid, pt, color, fref, label) in enumerate(TEST_CASES):
        print(f"  {i+1:2d}번째 정의: ID {cid:2d} = {label}")
    print()
    print("예상: 13번째까지만 적용되면 → 개수 제한 13개")


if __name__ == "__main__":
    main()
