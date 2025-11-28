#!/usr/bin/env python3
"""
실험 12: 불연속 ID 패턴 테스트
- ID: 0,1,2,4,6,8,10 (7개, 3과 5,7,9 빠짐)
- 연속 끊김 후 적용 여부 확인
"""

import zipfile
import os
import re
import shutil

TEMPLATE = "validator/tier_test/tier1/(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx"
OUTPUT = "output/exp12_skip_pattern.hwpx"

# 테스트할 ID와 색상
TEST_IDS = [0, 1, 2, 4, 6, 8, 10]
COLORS = {
    0: "#FF0000",   # 빨강
    1: "#FF8800",   # 주황
    2: "#FFFF00",   # 노랑
    4: "#00FF00",   # 초록
    6: "#00FFFF",   # 시안
    8: "#0000FF",   # 파랑
    10: "#FF00FF",  # 마젠타
}

def build_charprops():
    """7개 charPr 정의 생성 (불연속 ID)"""
    items = []
    for i in TEST_IDS:
        color = COLORS[i]
        items.append(f'''<hh:charPr id="{i}" height="1200" textColor="{color}" shadeColor="none" useFontSpace="0" useKerning="0" symMark="NONE" borderFillIDRef="2">
<hh:fontRef hangul="1" latin="1" hanja="1" japanese="1" other="1" symbol="1" user="1" />
<hh:ratio hangul="100" latin="100" hanja="100" japanese="100" other="100" symbol="100" user="100" />
<hh:spacing hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0" />
<hh:relSz hangul="100" latin="100" hanja="100" japanese="100" other="100" symbol="100" user="100" />
<hh:offset hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0" />
<hh:strikeout type="NONE" shape="SOLID" color="#000000" />
<hh:underline type="NONE" shape="SOLID" color="#000000" />
<hh:outline type="NONE" />
<hh:shadow type="NONE" color="#B2B2B2" offsetX="10" offsetY="10" />
</hh:charPr>''')
    
    return f'<hh:charProperties itemCnt="{len(TEST_IDS)}">\n' + '\n'.join(items) + '\n</hh:charProperties>'

def build_section():
    """7개 테스트 문단 생성"""
    paragraphs = []
    for idx, i in enumerate(TEST_IDS):
        color = COLORS[i]
        paragraphs.append(f'''<hp:p id="{idx+100}" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
<hp:run charPrIDRef="{i}">
<hp:secPr />
<hp:ctrl />
<hp:t>ID {i}: {color} - 이 텍스트가 색상 적용되어야 함</hp:t>
</hp:run>
</hp:p>''')
    
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<hs:sec xmlns:hs="http://www.hancom.co.kr/hwpml/2011/section" xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph" xmlns:hr="http://www.hancom.co.kr/hwpml/2011/run" xmlns:ht="http://www.hancom.co.kr/hwpml/2011/table" xmlns:hc="http://www.hancom.co.kr/hwpml/2011/chart" xmlns:he="http://www.hancom.co.kr/hwpml/2011/equation" xmlns:hd="http://www.hancom.co.kr/hwpml/2011/drawing" xmlns:hm="http://www.hancom.co.kr/hwpml/2011/master" xmlns:hhs="http://www.hancom.co.kr/hwpml/2011/headersummary" xmlns:hpf="http://www.hancom.co.kr/hwpml/2011/paraformat" xmlns:hf="http://www.hancom.co.kr/hwpml/2011/footnote" xmlns:hen="http://www.hancom.co.kr/hwpml/2011/endnote">
''' + '\n'.join(paragraphs) + '''
</hs:sec>'''

def main():
    os.makedirs("output", exist_ok=True)
    shutil.copy(TEMPLATE, OUTPUT)
    
    new_charprops = build_charprops()
    
    with zipfile.ZipFile(OUTPUT, 'r') as zf:
        header_xml = zf.read("Contents/header.xml").decode('utf-8')
    
    modified = re.sub(
        r'<hh:charProperties itemCnt="\d+">.*?</hh:charProperties>',
        new_charprops,
        header_xml,
        flags=re.DOTALL
    )
    
    new_section = build_section()
    
    temp_output = OUTPUT + ".tmp"
    with zipfile.ZipFile(OUTPUT, 'r') as zf_in:
        with zipfile.ZipFile(temp_output, 'w', zipfile.ZIP_DEFLATED) as zf_out:
            for item in zf_in.namelist():
                if item == "Contents/header.xml":
                    zf_out.writestr(item, modified.encode('utf-8'))
                elif item == "Contents/section0.xml":
                    zf_out.writestr(item, new_section.encode('utf-8'))
                else:
                    zf_out.writestr(item, zf_in.read(item))
    
    os.replace(temp_output, OUTPUT)
    
    print(f"✅ 생성: {OUTPUT}")
    print(f"테스트 ID: {TEST_IDS} (총 {len(TEST_IDS)}개)")
    print("\n예상 패턴:")
    print("  0,1,2 연속 → 3에서 끊김")
    print("  4 적용? → 끊김 후 +1 여유?")
    print("  6,8,10 적용?")

if __name__ == "__main__":
    main()
