#!/usr/bin/env python3
"""
실험 16: borderFill ID 테스트 (문단 배경색 방식)
=================================================
표 대신 문단 배경색으로 테스트 - 더 간단한 구조

⚠️ 주의: 배열 인덱스(i)와 ID(bid)를 혼동하지 말 것!
   - COLORS[bid] 사용 (O)
   - COLORS[i] 사용 (X) - 밀림 발생
"""

import zipfile
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TEMPLATE_HWPX = BASE_DIR / "validator" / "tier_test" / "tier1" / "(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx"
OUTPUT_DIR = BASE_DIR / "output"

# Test mode: 'continuous' or 'skip'
TEST_MODE = 'continuous'

# 배경색 팔레트 - 인덱스 = borderFill ID
# ⚠️ 한글은 borderFill을 1-based로 해석! (ID 0은 "없음"이 아니라 무시됨)
# COLORS[1] = 색없음(기본), COLORS[2] = 빨강, ...
COLORS = {
    1: ("none", "색없음"),   # ID 1 - 기본 (fillBrush 없음)
    2: ("#FF0000", "빨강"),
    3: ("#FF8000", "주황"),
    4: ("#FFFF00", "노랑"),
    5: ("#80FF00", "연두"),
    6: ("#00FF00", "초록"),
    7: ("#00FF80", "청록"),
    8: ("#00FFFF", "하늘"),
    9: ("#0080FF", "파랑"),
    10: ("#0000FF", "남색"),
    11: ("#8000FF", "보라"),
    12: ("#FF00FF", "분홍"),
    13: ("#FF0080", "자홍"),
    14: ("#800000", "진빨강"),
    15: ("#008000", "진초록"),
    16: ("#000080", "진파랑"),
    17: ("#808000", "올리브"),
    18: ("#800080", "진보라"),
    19: ("#008080", "청록2"),
    20: ("#C0C0C0", "은색"),
}

if TEST_MODE == 'continuous':
    # 연속: 1~20 (0은 한글이 무시함)
    BORDERFILL_IDS = list(range(1, 21))
else:
    # 불연속: 1,2,3,5,7,9,11,13,15
    BORDERFILL_IDS = [1,2,3,5,7,9,11,13,15]


def build_borderfill(bid) -> str:
    """borderFill 생성 - bid를 직접 COLORS 딕셔너리 키로 사용"""
    color, _ = COLORS[bid]
    if color == "none":
        # 색없음: fillBrush 태그 자체를 생략
        return f'''<hh:borderFill id="{bid}" threeD="0" shadow="0" centerLine="NONE" breakCellSeparateLine="0"><hh:slash type="NONE" Crooked="0" isCounter="0"/><hh:backSlash type="NONE" Crooked="0" isCounter="0"/><hh:leftBorder type="NONE" width="0.1 mm" color="#000000"/><hh:rightBorder type="NONE" width="0.1 mm" color="#000000"/><hh:topBorder type="NONE" width="0.1 mm" color="#000000"/><hh:bottomBorder type="NONE" width="0.1 mm" color="#000000"/><hh:diagonal type="SOLID" width="0.1 mm" color="#000000"/></hh:borderFill>'''
    return f'''<hh:borderFill id="{bid}" threeD="0" shadow="0" centerLine="NONE" breakCellSeparateLine="0"><hh:slash type="NONE" Crooked="0" isCounter="0"/><hh:backSlash type="NONE" Crooked="0" isCounter="0"/><hh:leftBorder type="NONE" width="0.1 mm" color="#000000"/><hh:rightBorder type="NONE" width="0.1 mm" color="#000000"/><hh:topBorder type="NONE" width="0.1 mm" color="#000000"/><hh:bottomBorder type="NONE" width="0.1 mm" color="#000000"/><hh:diagonal type="SOLID" width="0.1 mm" color="#000000"/><hc:fillBrush><hc:winBrush faceColor="{color}" hatchColor="#000000" alpha="0"/></hc:fillBrush></hh:borderFill>'''


def build_parapr(pid, borderfill_id) -> str:
    """paraPr - border에서 borderFillIDRef로 배경색 참조"""
    return f'''<hh:paraPr id="{pid}" tabPrIDRef="0" condense="0" fontLineHeight="0" snapToGrid="1" suppressLineNumbers="0" checked="0"><hh:align horizontal="LEFT" vertical="BASELINE"/><hh:heading type="NONE" idRef="0" level="0"/><hh:breakSetting breakLatinWord="KEEP_WORD" breakNonLatinWord="KEEP_WORD" widowOrphan="0" keepWithNext="0" keepLines="0" pageBreakBefore="0" lineWrap="BREAK"/><hh:autoSpacing eAsianEng="0" eAsianNum="0"/><hh:margin><hc:intent value="0" unit="HWPUNIT"/><hc:left value="0" unit="HWPUNIT"/><hc:right value="0" unit="HWPUNIT"/><hc:prev value="0" unit="HWPUNIT"/><hc:next value="0" unit="HWPUNIT"/></hh:margin><hh:lineSpacing type="PERCENT" value="160" unit="HWPUNIT"/><hh:border borderFillIDRef="{borderfill_id}" offsetLeft="283" offsetRight="283" offsetTop="283" offsetBottom="283" connect="0" ignoreMargin="0"/></hh:paraPr>'''


def modify_header(original_xml: str) -> str:
    # borderFills - 각 bid에 대해 COLORS[bid] 색상 적용
    borderfill_items = []
    for bid in BORDERFILL_IDS:
        borderfill_items.append(build_borderfill(bid))
    new_borderfills = f'<hh:borderFills itemCnt="{len(borderfill_items)}">' + ''.join(borderfill_items) + '</hh:borderFills>'
    modified = re.sub(r'<hh:borderFills itemCnt="\d+">.*?</hh:borderFills>', new_borderfills, original_xml, flags=re.DOTALL)
    
    # paraProperties - paraPr[i]가 borderFill[bid]를 참조
    parapr_items = []
    for i, bid in enumerate(BORDERFILL_IDS):
        parapr_items.append(build_parapr(i, bid))
    new_paraprops = f'<hh:paraProperties itemCnt="{len(parapr_items)}">' + ''.join(parapr_items) + '</hh:paraProperties>'
    modified = re.sub(r'<hh:paraProperties itemCnt="\d+">.*?</hh:paraProperties>', new_paraprops, modified, flags=re.DOTALL)
    
    return modified


def create_test_section0_xml() -> str:
    mode_label = "연속 ID 1~20" if TEST_MODE == 'continuous' else "불연속 ID"
    
    # 문단들 생성
    # paraPrIDRef = i (배열 순서)
    # 텍스트에는 bid와 COLORS[bid] 정보 표시
    paragraphs = []
    for i, bid in enumerate(BORDERFILL_IDS):
        color_hex, name = COLORS[bid]
        paragraphs.append(f'''<hp:p id="{i+10}" paraPrIDRef="{i}" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="0"><hp:t>[borderFill ID={bid}] {name} {color_hex}</hp:t></hp:run>
</hp:p>''')
    
    para_content = '\n'.join(paragraphs)
    
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
<hp:pageBorderFill type="BOTH" borderFillIDRef="0" textBorder="PAPER" headerInside="0" footerInside="0" fillArea="PAPER"><hp:offset left="1417" right="1417" top="1417" bottom="1417"/></hp:pageBorderFill>
<hp:pageBorderFill type="EVEN" borderFillIDRef="0" textBorder="PAPER" headerInside="0" footerInside="0" fillArea="PAPER"><hp:offset left="1417" right="1417" top="1417" bottom="1417"/></hp:pageBorderFill>
<hp:pageBorderFill type="ODD" borderFillIDRef="0" textBorder="PAPER" headerInside="0" footerInside="0" fillArea="PAPER"><hp:offset left="1417" right="1417" top="1417" bottom="1417"/></hp:pageBorderFill>
</hp:secPr>
<hp:ctrl><hp:colPr id="" type="NEWSPAPER" layout="LEFT" colCount="1" sameSz="1" sameGap="0"/></hp:ctrl>
</hp:run>
</hp:p>

<hp:p id="1" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="0"><hp:t>===== borderFill 테스트: {mode_label} =====</hp:t></hp:run>
</hp:p>
<hp:p id="2" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="0"><hp:t>각 문단의 배경색이 텍스트와 일치해야 함</hp:t></hp:run>
</hp:p>

{para_content}

</hs:sec>'''


def main():
    suffix = "continuous" if TEST_MODE == 'continuous' else "skip"
    output_path = OUTPUT_DIR / f"exp16_borderfill_{suffix}.hwpx"
    
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
    print(f"테스트 모드: {'연속 ID 1~20' if TEST_MODE == 'continuous' else '불연속 ID'}")
    print(f"borderFill ID: {BORDERFILL_IDS}")
    print()
    print("확인할 것: 텍스트와 배경색이 일치하는지")
    for bid in BORDERFILL_IDS:
        color_hex, name = COLORS[bid]
        print(f"  ID {bid:2d}: {name} {color_hex}")


if __name__ == "__main__":
    main()
