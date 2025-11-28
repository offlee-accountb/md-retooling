#!/usr/bin/env python3
"""
실험 2: charPr 완전 교체 테스트
==============================
목적: 
1. 기존 charPr를 완전히 교체했을 때 적용되는지
2. 큰 ID (50, 100)도 작동하는지

전략:
- 템플릿의 charProperties 섹션 전체를 교체
- ID 0, 1, 5, 50, 100 테스트
- 각각 다른 크기 + 색상으로 시각적 구분
"""

import zipfile
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TEMPLATE_HWPX = BASE_DIR / "validator" / "tier_test" / "tier1" / "(phase 1 finised) test_shift_sample-머리말꼬리말 추가.hwpx"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# 테스트 케이스: (ID, 글자크기pt, 색상, 설명)
TEST_CASES = [
    (0, 10, "#000000", "10pt 검정 - ID 0"),
    (1, 14, "#0000FF", "14pt 파랑 - ID 1"),
    (5, 18, "#FF0000", "18pt 빨강 - ID 5"),
    (50, 24, "#00FF00", "24pt 초록 - ID 50"),
    (100, 30, "#FF00FF", "30pt 보라 - ID 100"),
]


def build_charpr(char_id: int, height_pt: int, color: str) -> str:
    """단일 charPr 정의 생성"""
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
    """charProperties 섹션 전체 교체"""
    
    # 새 charPr들 생성
    charpr_items = []
    for char_id, pt_size, color, _ in TEST_CASES:
        charpr_items.append(build_charpr(char_id, pt_size, color))
    
    new_charprops = f'''<hh:charProperties itemCnt="{len(TEST_CASES)}">
{chr(10).join(charpr_items)}
</hh:charProperties>'''
    
    # 기존 charProperties 섹션 찾아서 교체
    pattern = r'<hh:charProperties itemCnt="\d+">[^§]*?</hh:charProperties>'
    
    # §는 절대 안 나올 문자. 대신 DOTALL로 처리
    modified = re.sub(
        r'<hh:charProperties itemCnt="\d+">.*?</hh:charProperties>',
        new_charprops,
        original_xml,
        flags=re.DOTALL
    )
    
    return modified


def create_test_section0_xml() -> str:
    """테스트 본문 생성"""
    paragraphs = []
    for i, (char_id, pt_size, color, label) in enumerate(TEST_CASES):
        text = f"[charPrIDRef={char_id}] 예상: {label}"
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
<hp:t>===== charPr 교체 + 큰 ID 테스트 =====</hp:t>
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
    if not TEMPLATE_HWPX.exists():
        print(f"❌ 템플릿 없음: {TEMPLATE_HWPX}")
        return
    
    print(f"📄 템플릿: {TEMPLATE_HWPX.name}")
    
    output_path = OUTPUT_DIR / "exp2_charpr_replace.hwpx"
    
    with zipfile.ZipFile(TEMPLATE_HWPX, 'r') as src_zip:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as dst_zip:
            for item in src_zip.namelist():
                data = src_zip.read(item)
                
                if item == "mimetype":
                    dst_zip.writestr(item, data, compress_type=zipfile.ZIP_STORED)
                
                elif item == "Contents/header.xml":
                    original = data.decode('utf-8')
                    modified = replace_charproperties(original)
                    dst_zip.writestr(item, modified.encode('utf-8'))
                    print(f"  ✏️ charProperties 교체: {item}")
                
                elif item == "Contents/section0.xml":
                    new_section = create_test_section0_xml()
                    dst_zip.writestr(item, new_section.encode('utf-8'))
                    print(f"  ✏️ 본문 교체: {item}")
                
                else:
                    dst_zip.writestr(item, data)
    
    print()
    print(f"✅ 생성: {output_path}")
    print()
    print("테스트 케이스:")
    for char_id, pt_size, color, label in TEST_CASES:
        print(f"  - ID {char_id}: {pt_size}pt {color} ({label})")
    print()
    print("예상 결과:")
    print("  - 모든 ID 적용됨 → ID 제한 없음, 교체 방식이 올바름")
    print("  - ID 0,1,5만 적용 → 큰 ID (50,100) 제한 있음")
    print("  - 아무것도 적용 안됨 → 교체 방식 문제 또는 styles 연동 필요")


if __name__ == "__main__":
    main()
