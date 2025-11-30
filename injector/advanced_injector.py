#!/usr/bin/env python3
"""
Advanced Injector - HWPX 문서에 다양한 패턴으로 데이터 주입

지원 패턴:
1. 키워드 패턴: "(키워드)" 뒤의 빈 텍스트에 값 주입
2. 라벨 패턴: "라벨 :" 같은 셀 내에서 콜론 뒤에 값 주입  
3. 라벨-값 셀 패턴: "라벨" 셀 옆의 빈 셀에 값 주입
4. 테이블 패턴: 표의 빈 셀에 순차적으로 데이터 주입

사용법:
    python advanced_injector.py template.hwpx data.yaml --output filled.hwpx
"""

import argparse
import zipfile
import tempfile
import shutil
import os
import re
import yaml
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field

# XML 네임스페이스
NAMESPACES = {
    'hp': 'http://www.hancom.co.kr/hwpml/2011/paragraph',
    'hs': 'http://www.hancom.co.kr/hwpml/2011/section',
    'hc': 'http://www.hancom.co.kr/hwpml/2011/core',
}

HP_NS = '{http://www.hancom.co.kr/hwpml/2011/paragraph}'

for prefix, uri in NAMESPACES.items():
    ET.register_namespace(prefix, uri)


@dataclass
class InjectionData:
    """주입할 데이터 구조"""
    # 키워드 패턴: "(키워드)" 뒤에 값 주입
    keywords: Dict[str, str] = field(default_factory=dict)
    
    # 라벨 패턴: "라벨:" 뒤에 값 주입 (같은 셀 내)
    labels: Dict[str, str] = field(default_factory=dict)
    
    # 라벨-값 셀 패턴: "라벨" 셀 옆 빈 셀에 값 주입
    cells: Dict[str, str] = field(default_factory=dict)
    
    # 테이블 데이터: 이름별 테이블 데이터
    tables: Dict[str, List[List[str]]] = field(default_factory=dict)
    
    # 제목
    title: Optional[str] = None


def parse_yaml_data(yaml_path: str) -> InjectionData:
    """YAML 파일에서 주입 데이터 로드
    
    YAML 형식:
    ```yaml
    title: "문서 제목"
    
    keywords:
      추진 배경: "배경 내용"
      구성: "구성 내용"
    
    labels:
      "부서명 :": "개발팀"
      "휴대폰 :": "010-1234-5678"
    
    cells:
      기업명: "ABC 주식회사"
      대표자: "홍길동"
    
    tables:
      제출서류:
        - ["1", "사업계획서", "필수"]
        - ["2", "재무제표", "선택"]
    ```
    """
    with open(yaml_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    data = InjectionData()
    
    if config:
        data.title = config.get('title')
        data.keywords = config.get('keywords', {})
        data.labels = config.get('labels', {})
        data.cells = config.get('cells', {})
        data.tables = config.get('tables', {})
    
    return data


def parse_md_data(md_path: str) -> InjectionData:
    """MD 파일 파싱하여 주입 데이터 추출 (하위 호환성)"""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    data = InjectionData()
    
    # 제목 추출
    title_match = re.search(r'<주제목>\s*(.+?)(?:\n|$)', content)
    if title_match:
        data.title = title_match.group(1).strip()
    
    # 키워드 패턴
    content_normalized = content.replace('\r\n', '\n').replace('\r', '\n')
    
    for line in content_normalized.split('\n'):
        line = line.strip()
        match = re.match(r'^[◦○]\s*\(([^)]+)\)\s*(.+)$', line)
        if match:
            data.keywords[match.group(1).strip()] = match.group(2).strip()
        else:
            match = re.match(r'^\(([^)]+)\)\s+(.+)$', line)
            if match:
                data.keywords[match.group(1).strip()] = match.group(2).strip()
    
    return data


def inject_keywords(xml_content: str, data: InjectionData) -> str:
    """키워드 패턴 주입: "(키워드)" 뒤의 빈 텍스트에 값 주입"""
    modified = xml_content
    
    for keyword, content in data.keywords.items():
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
    
    return modified


def inject_labels(xml_content: str, data: InjectionData) -> str:
    """라벨 패턴 주입: "라벨 :" 뒤에 값 주입 (같은 셀 내)
    
    예: <hp:t>부서명 :</hp:t> → <hp:t>부서명 : 개발팀</hp:t>
    """
    modified = xml_content
    
    for label, value in data.labels.items():
        # 라벨 끝에 공백 패턴 처리
        label_escaped = re.escape(label)
        
        # 패턴 1: <hp:t>라벨 :</hp:t> 형태
        patterns = [
            # 정확한 라벨 매칭 (공백 포함)
            (rf'<hp:t>({label_escaped})\s*</hp:t>',
             rf'<hp:t>\1 {value}</hp:t>'),
            # 라벨: 뒤에 아무것도 없는 경우
            (rf'<hp:t>({label_escaped})</hp:t>',
             rf'<hp:t>\1 {value}</hp:t>'),
        ]
        
        for pattern, replacement in patterns:
            modified = re.sub(pattern, replacement, modified)
    
    return modified


def inject_cells(xml_content: str, data: InjectionData) -> str:
    """라벨-값 셀 패턴: "라벨" 셀 옆의 빈 셀에 값 주입
    
    테이블 구조:
    | 라벨 셀 | 값 셀 (빈칸) |
    
    "라벨" 텍스트를 찾고, 그 옆 tc의 빈 hp:t에 값 주입
    
    특수 케이스:
    - 빈 셀이 <hp:run .../> (자기 닫힘) 형태인 경우 <hp:t> 요소를 생성해서 넣어야 함
    """
    # XML 파싱으로 처리
    root = ET.fromstring(xml_content)
    injected_count = 0
    
    for label, value in data.cells.items():
        found = False
        # 모든 테이블 순회
        for tbl in root.iter(f'{HP_NS}tbl'):
            if found:
                break
            for tr in tbl.iter(f'{HP_NS}tr'):
                if found:
                    break
                cells = list(tr.findall(f'{HP_NS}tc'))
                
                for i, tc in enumerate(cells):
                    # 이 셀에서 라벨 텍스트 찾기
                    cell_text = ''.join(t.text or '' for t in tc.iter(f'{HP_NS}t'))
                    
                    # 라벨이 정확히 일치하거나 포함되어 있는지 확인
                    if label == cell_text.strip() or label in cell_text.strip():
                        # 다음 셀(들)에서 빈 셀 찾아 값 주입
                        for next_tc in cells[i+1:]:
                            # 다음 셀의 모든 텍스트 확인
                            next_texts = list(next_tc.iter(f'{HP_NS}t'))
                            cell_has_content = any((t.text or '').strip() for t in next_texts)
                            
                            if cell_has_content:
                                # 셀에 이미 내용이 있으면 스킵
                                continue
                            
                            # 빈 셀에 값 주입
                            if next_texts:
                                # hp:t 요소가 있으면 그 곳에 값 설정
                                next_texts[0].text = value
                                found = True
                                injected_count += 1
                                break
                            else:
                                # hp:t 요소가 없으면 hp:run 안에 생성
                                runs = list(next_tc.iter(f'{HP_NS}run'))
                                if runs:
                                    # 첫 번째 run에 hp:t 추가
                                    run = runs[0]
                                    t_elem = ET.SubElement(run, f'{HP_NS}t')
                                    t_elem.text = value
                                    found = True
                                    injected_count += 1
                                    break
                        if found:
                            break
    
    if injected_count > 0:
        print(f"  → 셀 주입: {injected_count}개 완료")
    
    return ET.tostring(root, encoding='unicode')


def inject_table_data(xml_content: str, data: InjectionData) -> str:
    """테이블 데이터 주입 (개선된 버전)
    
    tables 딕셔너리의 이름과 매칭되는 테이블에 데이터 주입
    """
    if not data.tables:
        return xml_content
    
    root = ET.fromstring(xml_content)
    tables = list(root.iter(f'{HP_NS}tbl'))
    
    # 각 테이블의 헤더로 매칭
    for tbl_idx, tbl in enumerate(tables):
        # 첫 번째 행의 텍스트로 테이블 식별
        first_row = tbl.find(f'{HP_NS}tr')
        if first_row is None:
            continue
        
        header_texts = []
        for tc in first_row.findall(f'{HP_NS}tc'):
            cell_text = ''.join(t.text or '' for t in tc.iter(f'{HP_NS}t'))
            header_texts.append(cell_text.strip())
        
        # 테이블 이름과 매칭
        for table_name, table_data in data.tables.items():
            if table_name in ' '.join(header_texts):
                # 데이터 주입
                rows = list(tbl.findall(f'{HP_NS}tr'))
                data_idx = 0
                
                for row in rows[1:]:  # 헤더 스킵
                    if data_idx >= len(table_data):
                        break
                    
                    cells = list(row.findall(f'{HP_NS}tc'))
                    row_data = table_data[data_idx]
                    
                    for col_idx, tc in enumerate(cells):
                        if col_idx >= len(row_data):
                            break
                        
                        # 셀의 첫 번째 빈 텍스트 요소에 데이터 주입
                        for t_elem in tc.iter(f'{HP_NS}t'):
                            if (t_elem.text or '').strip() in ('', ' '):
                                t_elem.text = str(row_data[col_idx])
                                break
                    
                    data_idx += 1
    
    return ET.tostring(root, encoding='unicode')


def remove_linesegarray(xml_content: str) -> str:
    """linesegarray 제거 - 한글이 자동 재계산하도록"""
    return re.sub(
        r'<hp:linesegarray>.*?</hp:linesegarray>',
        '',
        xml_content,
        flags=re.DOTALL
    )


def inject_data(hwpx_path: str, data: InjectionData, output_path: str, 
                remove_lines: bool = True) -> str:
    """HWPX 파일에 데이터 주입"""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # 압축 해제
        with zipfile.ZipFile(hwpx_path, 'r') as zf:
            zf.extractall(temp_dir)
        
        # section XML 파일들 수정
        contents_dir = os.path.join(temp_dir, 'Contents')
        for filename in os.listdir(contents_dir):
            if filename.startswith('section') and filename.endswith('.xml'):
                section_path = os.path.join(contents_dir, filename)
                
                with open(section_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 각 패턴 적용
                modified = content
                
                if data.keywords:
                    modified = inject_keywords(modified, data)
                
                if data.labels:
                    modified = inject_labels(modified, data)
                
                if data.cells:
                    modified = inject_cells(modified, data)
                
                if data.tables:
                    modified = inject_table_data(modified, data)
                
                # linesegarray 제거 (자동 줄바꿈)
                if remove_lines:
                    modified = remove_linesegarray(modified)
                
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


def print_data_summary(data: InjectionData):
    """데이터 요약 출력"""
    print("\n" + "="*60)
    print("📋 주입 데이터 요약")
    print("="*60)
    
    if data.title:
        print(f"\n📌 제목: {data.title}")
    
    if data.keywords:
        print(f"\n🔑 키워드 패턴 ({len(data.keywords)}개):")
        for k, v in list(data.keywords.items())[:5]:
            preview = v[:40] + '...' if len(v) > 40 else v
            print(f"  ({k}): {preview}")
        if len(data.keywords) > 5:
            print(f"  ... 외 {len(data.keywords)-5}개")
    
    if data.labels:
        print(f"\n🏷️ 라벨 패턴 ({len(data.labels)}개):")
        for k, v in list(data.labels.items())[:5]:
            print(f"  {k} → {v}")
        if len(data.labels) > 5:
            print(f"  ... 외 {len(data.labels)-5}개")
    
    if data.cells:
        print(f"\n📝 셀 패턴 ({len(data.cells)}개):")
        for k, v in list(data.cells.items())[:5]:
            print(f"  [{k}] → {v}")
        if len(data.cells) > 5:
            print(f"  ... 외 {len(data.cells)-5}개")
    
    if data.tables:
        print(f"\n📊 테이블 ({len(data.tables)}개):")
        for name, rows in data.tables.items():
            print(f"  {name}: {len(rows)}행")


def main():
    parser = argparse.ArgumentParser(description='HWPX 문서에 다양한 패턴으로 데이터 주입')
    parser.add_argument('template', help='HWPX 템플릿 파일')
    parser.add_argument('data', help='주입할 데이터 (YAML 또는 MD 파일)')
    parser.add_argument('--output', '-o', help='출력 파일 경로')
    parser.add_argument('--dry-run', action='store_true', help='실제 파일 생성 없이 파싱만')
    parser.add_argument('--keep-lineseg', action='store_true', help='linesegarray 유지')
    
    args = parser.parse_args()
    
    # 데이터 파싱
    data_path = Path(args.data)
    if data_path.suffix in ('.yaml', '.yml'):
        data = parse_yaml_data(args.data)
    else:
        data = parse_md_data(args.data)
    
    # 요약 출력
    print_data_summary(data)
    
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
    inject_data(
        args.template, 
        data, 
        output_path,
        remove_lines=not args.keep_lineseg
    )


if __name__ == "__main__":
    main()
