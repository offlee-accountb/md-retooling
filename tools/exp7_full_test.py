#!/usr/bin/env python3
"""
실험 7: 40개 charPr + paraPr 스타일 테스트
==========================================
- charPr: ID 0~39 (40개)
- paraPr: ID 0~9 (10개, 각각 다른 정렬/줄간격)
- styles: 여러 스타일 정의
"""

import zipfile
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TEMPLATE_HWPX = BASE_DIR / "validator" / "tier_test" / "tier1" / "(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx"
OUTPUT_DIR = BASE_DIR / "output"

FONTS = ["한컴바탕", "맑은 고딕", "휴먼명조", "HY헤드라인M", "굴림", "돋움"]

# 40개 charPr (0~39)
def generate_charpr_cases():
    cases = []
    colors = ["#000000", "#FF0000", "#0000FF", "#00FF00", "#FF00FF", "#FF6600", "#006600", "#660066"]
    for i in range(40):
        pt = 8 + (i % 20)  # 8~27pt 반복
        color = colors[i % len(colors)]
        font = i % len(FONTS)
        cases.append((i, pt, color, font, f"{pt}pt {FONTS[font]}"))
    return cases

CHARPR_CASES = generate_charpr_cases()

# paraPr 테스트 (정렬, 줄간격)
PARAPR_CASES = [
    (0, "JUSTIFY", 160, "양쪽정렬 160%"),
    (1, "LEFT", 150, "왼쪽정렬 150%"),
    (2, "CENTER", 180, "가운데정렬 180%"),
    (3, "RIGHT", 130, "오른쪽정렬 130%"),
    (4, "JUSTIFY", 200, "양쪽정렬 200%"),
]

# styles 정의
STYLE_CASES = [
    (0, "바탕글", "Normal", 0, 0),
    (1, "제목1", "Heading1", 1, 5),
    (2, "제목2", "Heading2", 2, 10),
    (3, "본문", "Body", 0, 15),
    (4, "강조", "Emphasis", 3, 20),
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


def build_parapr(pid, align, linespace) -> str:
    return f'''<hh:paraPr id="{pid}" tabPrIDRef="0" condense="0" fontLineHeight="1" snapToGrid="0" suppressLineNumbers="0" checked="0">
<hh:align horizontal="{align}" vertical="BASELINE"/>
<hh:heading type="NONE" idRef="0" level="0"/>
<hh:breakSetting breakLatinWord="KEEP_WORD" breakNonLatinWord="KEEP_WORD" widowOrphan="0" keepWithNext="0" keepLines="0" pageBreakBefore="0" lineWrap="BREAK"/>
<hh:autoSpacing eAsianEng="0" eAsianNum="0"/>
<hh:margin><hc:intent value="0" unit="HWPUNIT"/><hc:left value="0" unit="HWPUNIT"/><hc:right value="0" unit="HWPUNIT"/><hc:prev value="0" unit="HWPUNIT"/><hc:next value="0" unit="HWPUNIT"/></hh:margin>
<hh:lineSpacing type="PERCENT" value="{linespace}" unit="HWPUNIT"/>
<hh:border borderFillIDRef="1" offsetLeft="0" offsetRight="0" offsetTop="0" offsetBottom="0" connect="0" ignoreMargin="0"/>
</hh:paraPr>'''


def build_style(sid, name, engname, parapr, charpr) -> str:
    return f'<hh:style id="{sid}" type="PARA" name="{name}" engName="{engname}" paraPrIDRef="{parapr}" charPrIDRef="{charpr}" nextStyleIDRef="{sid}" langID="1042" lockForm="0"/>'


def modify_header(original_xml: str) -> str:
    # fontfaces
    modified = re.sub(r'<hh:fontfaces itemCnt="\d+">.*?</hh:fontfaces>', build_fontfaces(), original_xml, flags=re.DOTALL)
    
    # charProperties (40개)
    charpr_items = [build_charpr(cid, pt, color, fref) for cid, pt, color, fref, _ in CHARPR_CASES]
    new_charprops = f'<hh:charProperties itemCnt="{len(CHARPR_CASES)}">\n' + '\n'.join(charpr_items) + '\n</hh:charProperties>'
    modified = re.sub(r'<hh:charProperties itemCnt="\d+">.*?</hh:charProperties>', new_charprops, modified, flags=re.DOTALL)
    
    # paraProperties
    parapr_items = [build_parapr(pid, align, ls) for pid, align, ls, _ in PARAPR_CASES]
    new_paraprops = f'<hh:paraProperties itemCnt="{len(PARAPR_CASES)}">\n' + '\n'.join(parapr_items) + '\n</hh:paraProperties>'
    modified = re.sub(r'<hh:paraProperties itemCnt="\d+">.*?</hh:paraProperties>', new_paraprops, modified, flags=re.DOTALL)
    
    # styles
    style_items = [build_style(sid, name, eng, ppr, cpr) for sid, name, eng, ppr, cpr in STYLE_CASES]
    new_styles = f'<hh:styles itemCnt="{len(STYLE_CASES)}">\n' + '\n'.join(style_items) + '\n</hh:styles>'
    modified = re.sub(r'<hh:styles itemCnt="\d+">.*?</hh:styles>', new_styles, modified, flags=re.DOTALL)
    
    return modified


def create_test_section0_xml() -> str:
    # Part 1: charPr 40개 테스트 (처음 20개만 표시)
    charpr_paras = []
    for i in range(20):  # 처음 20개
        cid, pt, color, fref, label = CHARPR_CASES[i]
        charpr_paras.append(f'''<hp:p id="{100+i}" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="{cid}"><hp:t>[charPr {cid}] {label}</hp:t></hp:run>
</hp:p>''')
    
    # Part 2: charPr 20~39 테스트
    for i in range(20, 40):
        cid, pt, color, fref, label = CHARPR_CASES[i]
        charpr_paras.append(f'''<hp:p id="{100+i}" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="{cid}"><hp:t>[charPr {cid}] {label}</hp:t></hp:run>
</hp:p>''')
    
    # Part 3: paraPr 테스트
    parapr_paras = []
    for pid, align, ls, label in PARAPR_CASES:
        parapr_paras.append(f'''<hp:p id="{200+pid}" paraPrIDRef="{pid}" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="0"><hp:t>[paraPr {pid}] {label}</hp:t></hp:run>
</hp:p>''')
    
    # Part 4: style 테스트
    style_paras = []
    for sid, name, eng, ppr, cpr in STYLE_CASES:
        style_paras.append(f'''<hp:p id="{300+sid}" paraPrIDRef="{ppr}" styleIDRef="{sid}" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="{cpr}"><hp:t>[style {sid}] {name} (paraPr={ppr}, charPr={cpr})</hp:t></hp:run>
</hp:p>''')
    
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
<hp:run charPrIDRef="0"><hp:t>========== charPr 테스트 (40개: 0~39) ==========</hp:t></hp:run>
</hp:p>
{chr(10).join(charpr_paras)}

<hp:p id="50" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="0"><hp:t>========== paraPr 테스트 (정렬/줄간격) ==========</hp:t></hp:run>
</hp:p>
{chr(10).join(parapr_paras)}

<hp:p id="60" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="0"><hp:t>========== style 테스트 ==========</hp:t></hp:run>
</hp:p>
{chr(10).join(style_paras)}
</hs:sec>'''


def main():
    output_path = OUTPUT_DIR / "exp7_40ids_styles.hwpx"
    
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
    print(f"\n=== charPr 40개 (0~39) ===")
    print(f"=== paraPr 5개 (정렬/줄간격) ===")
    for pid, align, ls, label in PARAPR_CASES:
        print(f"  {pid}: {label}")
    print(f"\n=== styles 5개 ===")
    for sid, name, eng, ppr, cpr in STYLE_CASES:
        print(f"  {sid}: {name} (paraPr={ppr}, charPr={cpr})")


if __name__ == "__main__":
    main()
