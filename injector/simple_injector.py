#!/usr/bin/env python3
"""
Simple Injector - 빈 HWPX 템플릿에 데이터 주입

테스트 케이스:
1. (1-1): 키워드 뒤에 텍스트 추가 (추진배경, 구성, 투입예산)
2. (1-2): 표에 데이터 주입

사용법:
    python simple_injector.py template.hwpx data.md --output filled.hwpx
"""

import argparse
import zipfile
import tempfile
import shutil
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

# XML 네임스페이스
NAMESPACES = {
    'hp': 'http://www.hancom.co.kr/hwpml/2011/paragraph',
    'hs': 'http://www.hancom.co.kr/hwpml/2011/section',
    'hc': 'http://www.hancom.co.kr/hwpml/2011/core',
}

for prefix, uri in NAMESPACES.items():
    ET.register_namespace(prefix, uri)


@dataclass
class InjectionData:
    """주입할 데이터"""
    keywords: Dict[str, str]  # {키워드: 내용}
    table_data: List[List[str]]  # 2D 테이블 데이터
    title: Optional[str] = None


def parse_md_data(md_path: str) -> InjectionData:
    """MD 파일 파싱하여 주입 데이터 추출"""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    keywords = {}
    table_data = []
    title = None
    
    # 제목 추출: <주제목> 또는 # 제목
    title_match = re.search(r'<주제목>\s*(.+?)(?:\n|$)', content)
    if title_match:
        title = title_match.group(1).strip()
    
    # 키워드 패턴: ◦ (키워드) 내용 또는  ◦ (키워드) 내용
    # 줄바꿈 통일
    content_normalized = content.replace('\r\n', '\n').replace('\r', '\n')
    
    # 각 줄에서 키워드 추출
    for line in content_normalized.split('\n'):
        line = line.strip()
        # ◦ (키워드) 내용 패턴
        match = re.match(r'^[◦○]\s*\(([^)]+)\)\s*(.+)$', line)
        if match:
            key = match.group(1).strip()
            value = match.group(2).strip()
            keywords[key] = value
        # (키워드) 내용 패턴 (◦ 없이)
        else:
            match = re.match(r'^\(([^)]+)\)\s+(.+)$', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip()
                keywords[key] = value
    
    # 테이블 파싱: | 구분 | 값 | 형식
    table_lines = [line for line in content.split('\n') if line.strip().startswith('|')]
    if len(table_lines) >= 2:  # 헤더 + 구분선 + 데이터
        for line in table_lines:
            if '---' in line:  # 구분선 스킵
                continue
            cells = [c.strip() for c in line.split('|')[1:-1]]  # 앞뒤 빈 요소 제거
            if cells:
                table_data.append(cells)
    
    return InjectionData(keywords=keywords, table_data=table_data, title=title)


def inject_keywords(xml_content: str, data: InjectionData) -> str:
    """키워드 뒤에 텍스트 주입
    
    패턴: <hp:t>(키워드)</hp:t></hp:run><hp:run ...><hp:t> </hp:t>
    → <hp:t>(키워드)</hp:t></hp:run><hp:run ...><hp:t> 주입내용</hp:t>
    """
    modified = xml_content
    
    for keyword, content in data.keywords.items():
        # 패턴: (키워드) 뒤의 빈 텍스트를 찾아서 내용으로 교체
        # 방법 1: 직접 텍스트 교체
        patterns = [
            # (키워드)</hp:t></hp:run><hp:run ...><hp:t> </hp:t>
            (rf'\({re.escape(keyword)}\)</hp:t></hp:run>(<hp:run[^>]*>)<hp:t>\s*</hp:t>',
             rf'({keyword})</hp:t></hp:run>\1<hp:t> {content}</hp:t>'),
            # (키워드)</hp:t></hp:run><hp:run ...><hp:t> (공백만)
            (rf'\({re.escape(keyword)}\)</hp:t></hp:run>(<hp:run[^>]*>)<hp:t> </hp:t>',
             rf'({keyword})</hp:t></hp:run>\1<hp:t> {content}</hp:t>'),
        ]
        
        for pattern, replacement in patterns:
            modified = re.sub(pattern, replacement, modified)
    
    # linesegarray 제거 - 한글이 자동 재계산하도록
    modified = re.sub(
        r'<hp:linesegarray>.*?</hp:linesegarray>',
        '',
        modified,
        flags=re.DOTALL
    )
    
    return modified


def inject_table_data(xml_content: str, data: InjectionData) -> str:
    """표에 데이터 주입
    
    빈 셀(<hp:t> </hp:t> 또는 빈 run)에 데이터 채우기
    """
    if not data.table_data:
        return xml_content
    
    # XML 파싱
    root = ET.fromstring(xml_content)
    hp_ns = '{http://www.hancom.co.kr/hwpml/2011/paragraph}'
    
    # 모든 테이블 찾기
    tables = list(root.iter(f'{hp_ns}tbl'))
    
    for tbl in tables:
        rows = list(tbl.iter(f'{hp_ns}tr'))
        
        # 데이터 행 인덱스 (헤더 스킵)
        data_row_idx = 0
        
        for row_idx, row in enumerate(rows):
            cells = list(row.iter(f'{hp_ns}tc'))
            
            for col_idx, cell in enumerate(cells):
                # 셀 내 텍스트 요소 찾기
                t_elems = list(cell.iter(f'{hp_ns}t'))
                
                for t_elem in t_elems:
                    text = t_elem.text or ''
                    
                    # 빈 셀이거나 공백만 있는 경우
                    if text.strip() == '' or text.strip() == ' ':
                        # 해당 위치에 데이터가 있으면 주입
                        if data_row_idx < len(data.table_data):
                            if col_idx < len(data.table_data[data_row_idx]):
                                new_text = data.table_data[data_row_idx][col_idx]
                                t_elem.text = new_text
            
            # 빈 셀이 있었으면 다음 데이터 행으로
            data_row_idx += 1
    
    # XML 문자열로 변환
    return ET.tostring(root, encoding='unicode')


def inject_data(hwpx_path: str, data: InjectionData, output_path: str) -> str:
    """HWPX 템플릿에 데이터 주입"""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # 압축 해제
        with zipfile.ZipFile(hwpx_path, 'r') as zf:
            zf.extractall(temp_dir)
        
        # section0.xml 수정
        section_path = os.path.join(temp_dir, 'Contents', 'section0.xml')
        with open(section_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 키워드 주입
        modified = inject_keywords(content, data)
        
        # 테이블 주입 (필요시)
        if data.table_data:
            modified = inject_table_data(modified, data)
        
        # 저장
        with open(section_path, 'w', encoding='utf-8') as f:
            f.write(modified)
        
        # 다시 압축
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf_out:
            for root_dir, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root_dir, file)
                    arc_name = os.path.relpath(file_path, temp_dir)
                    if file == 'mimetype':
                        zf_out.writestr(arc_name, open(file_path, 'rb').read(), 
                                       compress_type=zipfile.ZIP_STORED)
                    else:
                        zf_out.write(file_path, arc_name)
    
    print(f"✅ 생성: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description='빈 HWPX 템플릿에 데이터 주입')
    parser.add_argument('template', help='빈 HWPX 템플릿 파일')
    parser.add_argument('data', help='주입할 데이터 MD 파일')
    parser.add_argument('--output', '-o', help='출력 파일 경로')
    parser.add_argument('--dry-run', action='store_true', help='실제 파일 생성 없이 파싱만')
    
    args = parser.parse_args()
    
    # 데이터 파싱
    data = parse_md_data(args.data)
    
    print("\n" + "="*60)
    print("📋 파싱된 데이터")
    print("="*60)
    
    if data.title:
        print(f"\n📌 제목: {data.title}")
    
    if data.keywords:
        print(f"\n🔑 키워드 ({len(data.keywords)}개):")
        for k, v in data.keywords.items():
            preview = v[:50] + '...' if len(v) > 50 else v
            print(f"  ({k}): {preview}")
    
    if data.table_data:
        print(f"\n📊 테이블 ({len(data.table_data)}행):")
        for i, row in enumerate(data.table_data[:5]):
            print(f"  [{i}]: {row[:4]}...")
        if len(data.table_data) > 5:
            print(f"  ... 외 {len(data.table_data)-5}행")
    
    if args.dry_run:
        print("\n[Dry-run 모드 - 파일 생성 안함]")
        return
    
    # 출력 경로
    if args.output:
        output_path = args.output
    else:
        template_path = Path(args.template)
        output_path = str(template_path.parent / f"{template_path.stem}_filled.hwpx")
    
    # 주입 실행
    inject_data(args.template, data, output_path)


if __name__ == "__main__":
    main()
