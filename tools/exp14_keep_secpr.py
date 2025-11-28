#!/usr/bin/env python3
"""
실험 14: 불연속 ID 테스트 (exp10 구조 기반)
==========================================
- exp10과 동일한 구조 사용 (작동 확인됨)
- ID: 0,1,2,4,6,8,10 (7개, 불연속)
"""

import zipfile
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TEMPLATE_HWPX = BASE_DIR / "validator" / "tier_test" / "tier1" / "(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx"
OUTPUT_DIR = BASE_DIR / "output"

FONTS = ["한컴바탕", "맑은 고딕", "휴먼명조", "HY헤드라인M", "굴림", "돋움"]

# 연속 ID: 1~30 (30개)
TEST_CASES = []
COLORS = ["#FF0000", "#FF4400", "#FF8800", "#FFCC00", "#FFFF00", 
          "#CCFF00", "#88FF00", "#44FF00", "#00FF00", "#00FF44",
          "#00FF88", "#00FFCC", "#00FFFF", "#00CCFF", "#0088FF",
          "#0044FF", "#0000FF", "#4400FF", "#8800FF", "#CC00FF",
          "#FF00FF", "#FF00CC", "#FF0088", "#FF0044", "#CC0000",
          "#880000", "#440000", "#004400", "#000044", "#444444"]
for i in range(1, 31):
    pt = 8 + (i % 10)  # 8~17pt 반복
    color = COLORS[(i-1) % len(COLORS)]
    fref = (i-1) % len(FONTS)
    TEST_CASES.append((i, pt, color, fref, f"{pt}pt {color}"))


def build_fontfaces() -> str:
    font_items = [f'<hh:font id="{i}" face="{f}" type="TTF" isEmbedded="0"><hh:typeInfo familyType="FCAT_GOTHIC" weight="5" proportion="3" contrast="2" strokeVariation="0" armStyle="0" letterform="2" midline="0" xHeight="4"/></hh:font>' for i, f in enumerate(FONTS)]
    fonts_block = "".join(font_items)
    langs = ["HANGUL", "LATIN", "HANJA", "JAPANESE", "OTHER", "SYMBOL", "USER"]
    return f'<hh:fontfaces itemCnt="{len(langs)}">{"".join(f"""<hh:fontface lang="{l}" fontCnt="{len(FONTS)}">{fonts_block}</hh:fontface>""" for l in langs)}</hh:fontfaces>'


def build_charpr(cid, pt, color, fref) -> str:
    # exp10과 동일한 구조: underline → strikeout, strikeout shape="NONE"
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
    
    # paraProperties도 교체 (exp7 스타일) - 모든 charPrIDRef를 정의된 ID로
    new_paraprops = '''<hh:paraProperties itemCnt="1">
<hh:paraPr id="0" tabPrIDRef="0" condense="0" fontLineHeight="1" snapToGrid="0" suppressLineNumbers="0" checked="0">
<hh:align horizontal="JUSTIFY" vertical="BASELINE"/>
<hh:heading type="NONE" idRef="0" level="0"/>
<hh:breakSetting breakLatinWord="KEEP_WORD" breakNonLatinWord="KEEP_WORD" widowOrphan="0" keepWithNext="0" keepLines="0" pageBreakBefore="0" lineWrap="BREAK"/>
<hh:autoSpacing eAsianEng="0" eAsianNum="0"/>
<hh:margin><hc:intent value="0" unit="HWPUNIT"/><hc:left value="0" unit="HWPUNIT"/><hc:right value="0" unit="HWPUNIT"/><hc:prev value="0" unit="HWPUNIT"/><hc:next value="0" unit="HWPUNIT"/></hh:margin>
<hh:lineSpacing type="PERCENT" value="160" unit="HWPUNIT"/>
<hh:border borderFillIDRef="1" offsetLeft="0" offsetRight="0" offsetTop="0" offsetBottom="0" connect="0" ignoreMargin="0"/>
</hh:paraPr>
</hh:paraProperties>'''
    modified = re.sub(r'<hh:paraProperties itemCnt="\d+">.*?</hh:paraProperties>', new_paraprops, modified, flags=re.DOTALL)
    
    # styles - charPrIDRef=1 사용 (ID 0이 없으므로)
    new_styles = '''<hh:styles itemCnt="1">
<hh:style id="0" type="PARA" name="바탕글" engName="Normal" paraPrIDRef="0" charPrIDRef="1" nextStyleIDRef="0" langID="1042" lockForm="0"/>
</hh:styles>'''
    modified = re.sub(r'<hh:styles itemCnt="\d+">.*?</hh:styles>', new_styles, modified, flags=re.DOTALL)
    
    return modified


def create_test_section0_xml() -> str:
    # exp10과 동일한 구조: 첫 문단에 완전한 secPr 포함
    paragraphs = []
    for i, (cid, pt, color, fref, label) in enumerate(TEST_CASES):
        paragraphs.append(f'''<hp:p id="{100+i}" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="{cid}"><hp:t>[ID={cid:2d}] {label}</hp:t></hp:run>
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
<hp:run charPrIDRef="1"><hp:t>===== 연속 ID 테스트 (1~30) =====</hp:t></hp:run>
</hp:p>
<hp:p id="2" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="1"><hp:t>30개 연속 ID - 모두 적용되어야 함</hp:t></hp:run>
</hp:p>
{chr(10).join(paragraphs)}
</hs:sec>'''


def main():
    output_path = OUTPUT_DIR / "exp14_skip_ids.hwpx"
    
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
    print()
    print(f"테스트 케이스 (연속 ID 1~30, 총 {len(TEST_CASES)}개):")
    for cid, pt, color, fref, label in TEST_CASES[:10]:
        print(f"  ID {cid:2d}: {label}")
    print("  ...")
    for cid, pt, color, fref, label in TEST_CASES[-5:]:
        print(f"  ID {cid:2d}: {label}")
    print()
    print("확인할 것:")
    print("  - 모든 ID에 색상 적용 → 연속 ID OK")
    print("  - 일부만 적용 → 어디까지 되는지 확인")


if __name__ == "__main__":
    main()
