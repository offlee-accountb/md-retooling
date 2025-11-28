#!/usr/bin/env python3
"""
실험 5: 연속 ID + 폰트 테스트
============================
각 charPr에 다른 폰트 적용해서 폰트도 제대로 먹는지 확인
"""

import zipfile
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TEMPLATE_HWPX = BASE_DIR / "validator" / "tier_test" / "tier1" / "(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx"
OUTPUT_DIR = BASE_DIR / "output"

# 폰트 정의 (fontfaces에 들어갈 폰트들)
FONTS = [
    "한컴바탕",      # 0
    "맑은 고딕",     # 1
    "휴먼명조",      # 2
    "HY헤드라인M",   # 3
    "굴림",          # 4
    "돋움",          # 5
]

# 테스트 케이스: (ID, pt, color, fontRef, 설명)
TEST_CASES = [
    (0, 10, "#000000", 0, "10pt 검정 한컴바탕"),
    (1, 11, "#333333", 1, "11pt 회색 맑은고딕"),
    (2, 12, "#0000FF", 2, "12pt 파랑 휴먼명조"),
    (3, 13, "#0066FF", 3, "13pt 하늘 HY헤드라인"),
    (4, 14, "#00FF00", 4, "14pt 초록 굴림"),
    (5, 15, "#00FF66", 5, "15pt 연두 돋움"),
    (6, 16, "#FF0000", 0, "16pt 빨강 한컴바탕"),
    (7, 18, "#FF6600", 1, "18pt 주황 맑은고딕"),
    (8, 20, "#FF00FF", 2, "20pt 보라 휴먼명조"),
    (9, 24, "#9900FF", 3, "24pt 자주 HY헤드라인"),
    (10, 28, "#660000", 4, "28pt 갈색 굴림"),
]


def build_fontfaces() -> str:
    """폰트 정의"""
    font_items = []
    for i, font in enumerate(FONTS):
        font_items.append(f'<hh:font id="{i}" face="{font}" type="TTF" isEmbedded="0"><hh:typeInfo familyType="FCAT_GOTHIC" weight="5" proportion="3" contrast="2" strokeVariation="0" armStyle="0" letterform="2" midline="0" xHeight="4"/></hh:font>')
    
    fonts_block = "".join(font_items)
    
    # 각 언어별로 같은 폰트 세트
    langs = ["HANGUL", "LATIN", "HANJA", "JAPANESE", "OTHER", "SYMBOL", "USER"]
    fontfaces = []
    for lang in langs:
        fontfaces.append(f'<hh:fontface lang="{lang}" fontCnt="{len(FONTS)}">{fonts_block}</hh:fontface>')
    
    return f'<hh:fontfaces itemCnt="{len(langs)}">{" ".join(fontfaces)}</hh:fontfaces>'


def build_charpr(char_id: int, height_pt: int, color: str, font_ref: int) -> str:
    height = height_pt * 100
    return f'''<hh:charPr id="{char_id}" height="{height}" textColor="{color}" shadeColor="none" useFontSpace="0" useKerning="0" symMark="NONE" borderFillIDRef="1">
<hh:fontRef hangul="{font_ref}" latin="{font_ref}" hanja="{font_ref}" japanese="{font_ref}" other="{font_ref}" symbol="{font_ref}" user="{font_ref}"/>
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
    # 1. fontfaces 교체
    new_fontfaces = build_fontfaces()
    modified = re.sub(
        r'<hh:fontfaces itemCnt="\d+">.*?</hh:fontfaces>',
        new_fontfaces,
        original_xml,
        flags=re.DOTALL
    )
    
    # 2. charProperties 교체
    charpr_items = [build_charpr(cid, pt, color, fref) for cid, pt, color, fref, _ in TEST_CASES]
    new_charprops = f'''<hh:charProperties itemCnt="{len(TEST_CASES)}">
{chr(10).join(charpr_items)}
</hh:charProperties>'''
    
    modified = re.sub(
        r'<hh:charProperties itemCnt="\d+">.*?</hh:charProperties>',
        new_charprops,
        modified,
        flags=re.DOTALL
    )
    
    # 3. styles 교체
    new_styles = '''<hh:styles itemCnt="1">
<hh:style id="0" type="PARA" name="바탕글" engName="Normal" paraPrIDRef="0" charPrIDRef="0" nextStyleIDRef="0" langID="1042" lockForm="0"/>
</hh:styles>'''
    
    modified = re.sub(
        r'<hh:styles itemCnt="\d+">.*?</hh:styles>',
        new_styles,
        modified,
        flags=re.DOTALL
    )
    
    return modified


def create_test_section0_xml() -> str:
    paragraphs = []
    for i, (char_id, pt_size, color, font_ref, label) in enumerate(TEST_CASES):
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
<hp:t>===== 폰트 + 크기 + 색상 테스트 (ID 0~10) =====</hp:t>
</hp:run>
</hp:p>
{para_block}
</hs:sec>'''


def main():
    if not TEMPLATE_HWPX.exists():
        print(f"❌ 템플릿 없음")
        return
    
    output_path = OUTPUT_DIR / "exp5_font_test.hwpx"
    
    with zipfile.ZipFile(TEMPLATE_HWPX, 'r') as src_zip:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as dst_zip:
            for item in src_zip.namelist():
                data = src_zip.read(item)
                
                if item == "mimetype":
                    dst_zip.writestr(item, data, compress_type=zipfile.ZIP_STORED)
                elif item == "Contents/header.xml":
                    original = data.decode('utf-8')
                    modified = modify_header(original)
                    dst_zip.writestr(item, modified.encode('utf-8'))
                elif item == "Contents/section0.xml":
                    dst_zip.writestr(item, create_test_section0_xml().encode('utf-8'))
                else:
                    dst_zip.writestr(item, data)
    
    print(f"✅ 생성: {output_path}")
    print()
    print("폰트 목록:")
    for i, font in enumerate(FONTS):
        print(f"  fontRef {i}: {font}")
    print()
    print("테스트 케이스:")
    for cid, pt, color, fref, label in TEST_CASES:
        print(f"  ID {cid}: {label}")


if __name__ == "__main__":
    main()
