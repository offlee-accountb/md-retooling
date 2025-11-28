#!/usr/bin/env python3
"""
실험 15: paraPr ID 테스트
=========================
Test 1: 연속 ID 0~29 (30개) - 모두 적용되는지
Test 2: 불연속 ID 0,1,2,3,4,5,7,9,11,13,15 (step 2) - 어디까지 적용되는지
"""

import zipfile
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TEMPLATE_HWPX = BASE_DIR / "validator" / "tier_test" / "tier1" / "(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx"
OUTPUT_DIR = BASE_DIR / "output"

FONTS = ["한컴바탕", "맑은 고딕"]

# Test mode: 'continuous' or 'skip'
TEST_MODE = 'skip'  # 먼저 연속 테스트

# 연속 ID: 0~29 (30개)
if TEST_MODE == 'continuous':
    PARAPR_IDS = list(range(30))  # 0~29
else:
    # 불연속: 0,1,2,3,4,5 + 7,9,11,13,15 (step 2)
    PARAPR_IDS = [0,1,2,3,4,5,10,11,12]


def build_fontfaces() -> str:
    font_items = [f'<hh:font id="{i}" face="{f}" type="TTF" isEmbedded="0"><hh:typeInfo familyType="FCAT_GOTHIC" weight="5" proportion="3" contrast="2" strokeVariation="0" armStyle="0" letterform="2" midline="0" xHeight="4"/></hh:font>' for i, f in enumerate(FONTS)]
    fonts_block = "".join(font_items)
    langs = ["HANGUL", "LATIN", "HANJA", "JAPANESE", "OTHER", "SYMBOL", "USER"]
    return f'<hh:fontfaces itemCnt="{len(langs)}">{"".join(f"""<hh:fontface lang="{l}" fontCnt="{len(FONTS)}">{fonts_block}</hh:fontface>""" for l in langs)}</hh:fontfaces>'


def build_charpr(cid) -> str:
    return f'''<hh:charPr id="{cid}" height="1000" textColor="#000000" shadeColor="none" useFontSpace="0" useKerning="0" symMark="NONE" borderFillIDRef="1">
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


def build_parapr(pid) -> str:
    left_margin = pid * 500
    line_spacing = 140 + pid * 5
    
    return f'''<hh:paraPr id="{pid}" tabPrIDRef="0" condense="0" fontLineHeight="1" snapToGrid="0" suppressLineNumbers="0" checked="0">
<hh:align horizontal="JUSTIFY" vertical="BASELINE"/>
<hh:heading type="NONE" idRef="0" level="0"/>
<hh:breakSetting breakLatinWord="KEEP_WORD" breakNonLatinWord="KEEP_WORD" widowOrphan="0" keepWithNext="0" keepLines="0" pageBreakBefore="0" lineWrap="BREAK"/>
<hh:autoSpacing eAsianEng="0" eAsianNum="0"/>
<hh:margin><hc:intent value="0" unit="HWPUNIT"/><hc:left value="{left_margin}" unit="HWPUNIT"/><hc:right value="0" unit="HWPUNIT"/><hc:prev value="0" unit="HWPUNIT"/><hc:next value="0" unit="HWPUNIT"/></hh:margin>
<hh:lineSpacing type="PERCENT" value="{line_spacing}" unit="HWPUNIT"/>
<hh:border borderFillIDRef="1" offsetLeft="0" offsetRight="0" offsetTop="0" offsetBottom="0" connect="0" ignoreMargin="0"/>
</hh:paraPr>'''


def modify_header(original_xml: str) -> str:
    modified = re.sub(r'<hh:fontfaces itemCnt="\d+">.*?</hh:fontfaces>', build_fontfaces(), original_xml, flags=re.DOTALL)
    
    charpr_items = [build_charpr(0)]
    new_charprops = f'<hh:charProperties itemCnt="1">\n' + '\n'.join(charpr_items) + '\n</hh:charProperties>'
    modified = re.sub(r'<hh:charProperties itemCnt="\d+">.*?</hh:charProperties>', new_charprops, modified, flags=re.DOTALL)
    
    parapr_items = [build_parapr(pid) for pid in PARAPR_IDS]
    new_paraprops = f'<hh:paraProperties itemCnt="{len(PARAPR_IDS)}">\n' + '\n'.join(parapr_items) + '\n</hh:paraProperties>'
    modified = re.sub(r'<hh:paraProperties itemCnt="\d+">.*?</hh:paraProperties>', new_paraprops, modified, flags=re.DOTALL)
    
    new_styles = '''<hh:styles itemCnt="1">
<hh:style id="0" type="PARA" name="바탕글" engName="Normal" paraPrIDRef="0" charPrIDRef="0" nextStyleIDRef="0" langID="1042" lockForm="0"/>
</hh:styles>'''
    modified = re.sub(r'<hh:styles itemCnt="\d+">.*?</hh:styles>', new_styles, modified, flags=re.DOTALL)
    
    return modified


def create_test_section0_xml() -> str:
    paragraphs = []
    for i, pid in enumerate(PARAPR_IDS):
        left_margin = pid * 500
        line_spacing = 140 + pid * 5
        paragraphs.append(f'''<hp:p id="{100+i}" paraPrIDRef="{pid}" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="0"><hp:t>[paraPr ID={pid:2d}] 왼쪽여백={left_margin} 줄간격={line_spacing}%</hp:t></hp:run>
</hp:p>''')
    
    mode_label = "연속 ID 0~29 (30개)" if TEST_MODE == 'continuous' else "불연속 ID 0,1,2,3,4,5,7,9,11,13,15"
    
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
</hp:p>

<hp:p id="1" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="0"><hp:t>===== paraPr 테스트: {mode_label} =====</hp:t></hp:run>
</hp:p>
<hp:p id="2" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="0"><hp:t>각 문단의 왼쪽 여백이 점점 커져야 함 (들여쓰기 효과)</hp:t></hp:run>
</hp:p>
{chr(10).join(paragraphs)}
</hs:sec>'''


def main():
    suffix = "continuous" if TEST_MODE == 'continuous' else "skip"
    output_path = OUTPUT_DIR / f"exp15_parapr_{suffix}.hwpx"
    
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
    print(f"테스트 모드: {'연속 ID 0~29' if TEST_MODE == 'continuous' else '불연속 ID'}")
    print(f"paraPr ID: {PARAPR_IDS}")


if __name__ == "__main__":
    main()
