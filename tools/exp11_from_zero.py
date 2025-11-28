#!/usr/bin/env python3
"""
실험 11: ID 0부터 시작해서 최대 몇 개까지 작동하는지 테스트
- ID 0~24 (25개) 정의
- 각 ID마다 다른 색상으로 구분
"""

import zipfile
import os
import re
import shutil

TEMPLATE = "validator/tier_test/tier1/(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx"
OUTPUT = "output/exp11_from_zero.hwpx"

# 25개 charPr 정의 (ID 0~24)
COLORS = [
    "#FF0000",  # 0: 빨강
    "#FF4400",  # 1: 주황-빨강
    "#FF8800",  # 2: 주황
    "#FFCC00",  # 3: 금색
    "#FFFF00",  # 4: 노랑
    "#CCFF00",  # 5: 연두-노랑
    "#88FF00",  # 6: 연두
    "#44FF00",  # 7: 초록-연두
    "#00FF00",  # 8: 초록
    "#00FF44",  # 9: 청록-초록
    "#00FF88",  # 10: 청록
    "#00FFCC",  # 11: 시안-청록
    "#00FFFF",  # 12: 시안
    "#00CCFF",  # 13: 하늘-시안
    "#0088FF",  # 14: 하늘
    "#0044FF",  # 15: 파랑-하늘
    "#0000FF",  # 16: 파랑
    "#4400FF",  # 17: 보라-파랑
    "#8800FF",  # 18: 보라
    "#CC00FF",  # 19: 자주-보라
    "#FF00FF",  # 20: 마젠타
    "#FF00CC",  # 21: 핑크-마젠타
    "#FF0088",  # 22: 핑크
    "#FF0044",  # 23: 빨강-핑크
    "#880000",  # 24: 진한 빨강
]

def build_charprops():
    """25개 charPr 정의 생성"""
    items = []
    for i in range(25):
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
    
    return f'<hh:charProperties itemCnt="25">\n' + '\n'.join(items) + '\n</hh:charProperties>'

def build_section():
    """25개 테스트 문단 생성"""
    paragraphs = []
    for i in range(25):
        color = COLORS[i]
        paragraphs.append(f'''<hp:p id="{i+100}" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">
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
    # 출력 폴더 확인
    os.makedirs("output", exist_ok=True)
    
    # 템플릿 복사
    shutil.copy(TEMPLATE, OUTPUT)
    
    # 새 charProperties
    new_charprops = build_charprops()
    
    # header.xml 수정
    with zipfile.ZipFile(OUTPUT, 'r') as zf:
        header_xml = zf.read("Contents/header.xml").decode('utf-8')
    
    # charProperties 교체
    modified = re.sub(
        r'<hh:charProperties itemCnt="\d+">.*?</hh:charProperties>',
        new_charprops,
        header_xml,
        flags=re.DOTALL
    )
    
    # section0.xml 생성
    new_section = build_section()
    
    # ZIP 업데이트
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
    print(f"총 25개 정의 (ID 0~24)")
    print("테스트 케이스:")
    for i in range(25):
        print(f"  ID {i}: {COLORS[i]}")

if __name__ == "__main__":
    main()
