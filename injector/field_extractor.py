#!/usr/bin/env python3
"""
HWPX 필드 분석기 (Field Extractor)
===================================

HWPX 문서를 분석하여:
1. 입력이 필요한 필드 목록 추출
2. 데이터 수집용 프롬프트 생성
3. 빈 입력 템플릿 YAML 생성

사용법:
    python field_extractor.py input.hwpx -o output_prefix
    
출력:
    - {output_prefix}_fields.yaml    : 빈 입력 템플릿
    - {output_prefix}_prompt.md      : 데이터 수집용 프롬프트
"""

import argparse
import zipfile
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict, Set, Tuple

# XML 네임스페이스
HP_NS = '{http://www.hancom.co.kr/hwpml/2011/paragraph}'

# 알려진 라벨 패턴 (정규화용)
KNOWN_LABELS = {
    # 기업 정보
    "기업명": ["기업체명", "회사명", "상호", "법인명", "업체명"],
    "대표자": ["대표이사", "대표자명", "대표", "대표자또는대표이사"],
    "사업자등록번호": ["사업자번호", "사업자등록", "등록번호", "사업자번호또는법인번호"],
    "설립일자": ["설립일", "창업일", "창업일자", "개업일"],
    "주소": ["소재지", "사업장주소", "본사주소", "회사주소"],
    
    # 담당자 정보
    "성명": ["이름", "담당자명", "담당자", "작성자"],
    "부서명": ["부서", "소속부서", "소속"],
    "직위": ["직책", "직급"],
    "휴대폰": ["휴대전화", "핸드폰", "모바일", "HP"],
    "전화": ["전화번호", "유선전화", "TEL"],
    "이메일": ["E-mail", "email", "메일", "이메일주소"],
    "연락처": ["전화", "전화번호"],
    
    # 신청 정보
    "신청기업명": ["신청기업", "신청업체명"],
    "신청자": ["신청인", "신청자명"],
    "신청일": ["신청일자", "접수일"],
    
    # 수신자
    "귀중": ["귀하", "앞"],
}

# 입력 예시
FIELD_EXAMPLES = {
    "기업명": "(주)스마트테크, ABC 주식회사",
    "대표자": "홍길동",
    "사업자등록번호": "123-45-67890 (10자리)",
    "설립일자": "2018-03-15 또는 2018년 3월 15일",
    "주소": "서울시 강남구 테헤란로 123",
    "부서명": "기술개발팀, 경영지원팀",
    "직위": "팀장, 과장, 대리",
    "성명": "김담당",
    "휴대폰": "010-1234-5678",
    "전화": "02-555-1234",
    "이메일": "contact@company.co.kr",
    "연락처": "02-555-1234",
    "신청기업명": "기업명과 동일",
    "신청자": "대표자와 동일",
    "신청일": "자동입력(오늘) 또는 2025-11-30",
    "귀중": "중소벤처기업부장관, OO기관장",
}


@dataclass
class FieldInfo:
    """추출된 필드 정보"""
    label: str                  # 원본 라벨
    normalized: str             # 정규화된 라벨
    section: str                # 발견된 섹션
    page_hint: str              # 페이지 힌트
    context: str                # 주변 컨텍스트
    pattern_type: str           # 패턴 유형 (table/paragraph/signature)
    example: str = ""           # 입력 예시


def normalize_label(text: str) -> str:
    """라벨 정규화: 공백, 특수문자 제거"""
    if not text:
        return ""
    # 공백 제거 (한글 사이 공백 포함)
    result = re.sub(r'\s+', '', text)
    # 콜론 제거
    result = result.replace(':', '').replace('：', '')
    return result


def find_canonical_label(label: str) -> str:
    """정규화된 라벨을 대표 라벨로 변환"""
    norm = normalize_label(label)
    
    # 직접 매칭
    for canonical, variants in KNOWN_LABELS.items():
        if norm == normalize_label(canonical):
            return canonical
        for v in variants:
            if norm == normalize_label(v):
                return canonical
    
    # 부분 매칭 (포함 관계)
    for canonical, variants in KNOWN_LABELS.items():
        if normalize_label(canonical) in norm or norm in normalize_label(canonical):
            return canonical
        for v in variants:
            if normalize_label(v) in norm or norm in normalize_label(v):
                return canonical
    
    return label  # 매칭 실패시 원본 반환


def is_label_candidate(text: str) -> bool:
    """라벨 후보인지 판단"""
    if not text or len(text) > 30:
        return False
    
    text = text.strip()
    
    # 빈 값, 숫자만, 특수문자만 제외
    if not text or text.isdigit():
        return False
    
    # 콜론으로 끝나면 라벨 가능성 높음
    if text.endswith(':') or text.endswith('：'):
        return True
    
    # 알려진 라벨 패턴 체크
    norm = normalize_label(text)
    for canonical, variants in KNOWN_LABELS.items():
        if norm == normalize_label(canonical):
            return True
        for v in variants:
            if norm == normalize_label(v):
                return True
    
    return False


def extract_table_fields(root, section_name: str) -> List[FieldInfo]:
    """테이블에서 필드 추출"""
    fields = []
    seen_labels = set()
    
    for tbl_idx, tbl in enumerate(root.iter(f'{HP_NS}tbl')):
        for tr in tbl.iter(f'{HP_NS}tr'):
            cells = list(tr.findall(f'{HP_NS}tc'))
            
            for cell_idx, tc in enumerate(cells):
                # 셀 텍스트 추출
                texts = [t.text for t in tc.iter(f'{HP_NS}t') if t.text]
                cell_text = ''.join(texts).strip()
                
                if not is_label_candidate(cell_text):
                    continue
                
                # 다음 셀이 비어있는지 확인 (입력 필드 가능성)
                has_empty_next = False
                if cell_idx + 1 < len(cells):
                    next_texts = [t.text for t in cells[cell_idx + 1].iter(f'{HP_NS}t') if t.text]
                    next_text = ''.join(next_texts).strip()
                    if not next_text or next_text in ['', ' ', '　']:
                        has_empty_next = True
                
                # PREPEND 패턴 체크 (밑줄 + 라벨)
                runs = list(tc.iter(f'{HP_NS}run'))
                is_prepend = False
                if len(runs) >= 2:
                    for i, run in enumerate(runs):
                        t = run.find(f'{HP_NS}t')
                        if t is not None and t.text:
                            if normalize_label(cell_text) in normalize_label(t.text):
                                if i > 0:
                                    prev_t = runs[i-1].find(f'{HP_NS}t')
                                    if prev_t is not None and prev_t.text:
                                        if prev_t.text.strip() == '' and len(prev_t.text) >= 5:
                                            is_prepend = True
                
                if has_empty_next or is_prepend:
                    canonical = find_canonical_label(cell_text)
                    
                    if canonical not in seen_labels:
                        seen_labels.add(canonical)
                        fields.append(FieldInfo(
                            label=cell_text,
                            normalized=canonical,
                            section=section_name,
                            page_hint=f"테이블 {tbl_idx + 1}",
                            context=f"테이블 내 라벨",
                            pattern_type="prepend" if is_prepend else "table",
                            example=FIELD_EXAMPLES.get(canonical, "")
                        ))
    
    return fields


def extract_paragraph_fields(root, section_name: str) -> List[FieldInfo]:
    """본문 패러그래프에서 필드 추출 (서명란 등)"""
    fields = []
    seen_labels = set()
    
    # 서명란 패턴: "라벨 : ㅇㅇㅇ (인)", "라벨 :     (인)"
    sig_pattern = re.compile(r'([가-힣a-zA-Z]+)\s*[:：]\s*(ㅇ+|_+|\s+)\s*\((인|印)\)')
    
    for t_elem in root.iter(f'{HP_NS}t'):
        text = t_elem.text or ''
        
        # 서명란 패턴 매칭
        match = sig_pattern.search(text)
        if match:
            label = match.group(1)
            canonical = find_canonical_label(label)
            
            if canonical not in seen_labels:
                seen_labels.add(canonical)
                fields.append(FieldInfo(
                    label=label,
                    normalized=canonical,
                    section=section_name,
                    page_hint="서명란",
                    context=text[:50],
                    pattern_type="signature",
                    example=FIELD_EXAMPLES.get(canonical, "")
                ))
    
    return fields


def extract_date_fields(root, section_name: str) -> List[FieldInfo]:
    """날짜 필드 추출"""
    fields = []
    
    # 날짜 패턴: "년 월 일", "2025년   월   일"
    date_patterns = [
        (r'\d{4}년\s+월\s+일', "YYYY년 월 일 형식"),
        (r'\d{2}\s*년\s+월\s+일', "YY년 월 일 형식"),
        (r'년\s+월\s+일', "년 월 일 형식"),
    ]
    
    found_date = False
    for t_elem in root.iter(f'{HP_NS}t'):
        text = t_elem.text or ''
        for pattern, desc in date_patterns:
            if re.search(pattern, text) and not found_date:
                fields.append(FieldInfo(
                    label="날짜",
                    normalized="신청일",
                    section=section_name,
                    page_hint="날짜 필드",
                    context=desc,
                    pattern_type="date",
                    example="AUTO_DATE (자동) 또는 2025-11-30"
                ))
                found_date = True
                break
    
    return fields


def analyze_hwpx(hwpx_path: str) -> Tuple[List[FieldInfo], Dict]:
    """HWPX 파일 분석"""
    all_fields = []
    meta = {
        "filename": Path(hwpx_path).name,
        "sections": [],
        "analyzed_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    with zipfile.ZipFile(hwpx_path, 'r') as zf:
        # 섹션 파일 목록
        section_files = sorted([f for f in zf.namelist() if f.startswith('Contents/section') and f.endswith('.xml')])
        
        for section_file in section_files:
            section_name = Path(section_file).stem  # section0, section1, ...
            meta["sections"].append(section_name)
            
            content = zf.read(section_file).decode('utf-8')
            root = ET.fromstring(content)
            
            # 각 패턴별 필드 추출
            all_fields.extend(extract_table_fields(root, section_name))
            all_fields.extend(extract_paragraph_fields(root, section_name))
            all_fields.extend(extract_date_fields(root, section_name))
    
    # 중복 제거 (normalized 기준)
    seen = set()
    unique_fields = []
    for f in all_fields:
        if f.normalized not in seen:
            seen.add(f.normalized)
            unique_fields.append(f)
    
    return unique_fields, meta


def generate_yaml_template(fields: List[FieldInfo], meta: Dict) -> str:
    """빈 입력 템플릿 YAML 생성"""
    lines = [
        f"# {meta['filename']} - 데이터 입력 템플릿",
        f"# 생성일: {meta['analyzed_at']}",
        f"# 섹션: {', '.join(meta['sections'])}",
        "#",
        "# 사용법: 각 필드의 value에 실제 값을 입력하세요",
        "# ============================================================",
        "",
        "fields:"
    ]
    
    current_section = None
    for f in fields:
        if f.section != current_section:
            current_section = f.section
            lines.append(f"  # --- {current_section} ---")
        
        comment = f"# {f.example}" if f.example else f"# {f.context}"
        lines.append(f"  - label: \"{f.normalized}\"")
        lines.append(f"    value: \"\"                    {comment}")
        lines.append("")
    
    lines.extend([
        "keywords: {}",
        "tables: {}"
    ])
    
    return '\n'.join(lines)


def generate_prompt(fields: List[FieldInfo], meta: Dict) -> str:
    """데이터 수집용 프롬프트 생성"""
    lines = [
        f"# 📋 {meta['filename']} 작성 도우미",
        "",
        f"이 문서 작성을 도와드리겠습니다.",
        "",
        "아래 정보들을 입력해 주세요.",
        "잘 모르거나 해당 없는 항목은 \"없음\"이라고 답해주세요.",
        "",
        "---",
        "",
        "## 입력 필요 항목",
        "",
        "| 항목 | 입력 예시 | 위치 |",
        "|------|----------|------|"
    ]
    
    for f in fields:
        example = f.example if f.example else "-"
        location = f"{f.section} ({f.page_hint})"
        lines.append(f"| **{f.normalized}** | {example} | {location} |")
    
    lines.extend([
        "",
        "---",
        "",
        "## 입력 방법",
        "",
        "각 항목에 대해 순서대로 답변해 주시면 됩니다.",
        "",
        "예시:",
        "```",
        "기업명: (주)스마트테크",
        "대표자: 홍길동",
        "사업자등록번호: 123-45-67890",
        "...",
        "```",
        "",
        "---",
        "",
        "위 항목들에 대한 정보를 알려주세요!"
    ])
    
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='HWPX 필드 분석기')
    parser.add_argument('hwpx', help='분석할 HWPX 파일')
    parser.add_argument('-o', '--output', help='출력 파일 접두사', default=None)
    parser.add_argument('--yaml-only', action='store_true', help='YAML만 출력')
    parser.add_argument('--prompt-only', action='store_true', help='프롬프트만 출력')
    
    args = parser.parse_args()
    
    # 분석
    print(f"📂 분석 중: {args.hwpx}")
    fields, meta = analyze_hwpx(args.hwpx)
    print(f"✓ {len(fields)}개 필드 발견")
    
    # 출력 파일명 결정
    if args.output:
        prefix = args.output
    else:
        prefix = Path(args.hwpx).stem
    
    # YAML 템플릿 생성
    if not args.prompt_only:
        yaml_content = generate_yaml_template(fields, meta)
        yaml_path = f"{prefix}_fields.yaml"
        with open(yaml_path, 'w', encoding='utf-8') as f:
            f.write(yaml_content)
        print(f"✓ 저장: {yaml_path}")
    
    # 프롬프트 생성
    if not args.yaml_only:
        prompt_content = generate_prompt(fields, meta)
        prompt_path = f"{prefix}_prompt.md"
        with open(prompt_path, 'w', encoding='utf-8') as f:
            f.write(prompt_content)
        print(f"✓ 저장: {prompt_path}")
    
    # 요약 출력
    print(f"\n📋 발견된 필드:")
    for f in fields:
        print(f"  - {f.normalized} ({f.pattern_type}, {f.section})")


if __name__ == "__main__":
    main()
