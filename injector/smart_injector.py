#!/usr/bin/env python3
"""
Smart Injector v3 - 통합 HWPX 데이터 주입 도구

=== 명령어 ===

1. analyze: HWPX 분석 → 프롬프트 + 빈 템플릿 생성
   python smart_injector.py analyze input.hwpx -o prefix
   
2. parse: 사용자 응답 → YAML 변환
   python smart_injector.py parse response.txt -o fields.yaml
   
3. inject: HWPX + YAML → 완성 문서
   python smart_injector.py inject input.hwpx fields.yaml -o output.hwpx
   
4. full: 전체 파이프라인 (analyze + 대기 + inject)
   python smart_injector.py full input.hwpx -o output.hwpx

=== 2단계 규칙 시스템 ===

1단계 (자동 감지):
   - 라벨 찾기 → 옆 셀 존재 + 비어있음 → 옆 셀에 작성
   - 라벨 찾기 → 옆 셀 없거나 내용 있음 → 콜론 뒤에 append

2단계 (명시적 지정):
   - YAML에서 mode를 명시하면 그 규칙 우선
   - mode: next_cell | append | replace | prepend | skip_colon
"""

import argparse
import zipfile
import tempfile
import os
import re
import yaml
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime


# XML 네임스페이스
HP_NS = '{http://www.hancom.co.kr/hwpml/2011/paragraph}'
HS_NS = '{http://www.hancom.co.kr/hwpml/2011/section}'
HC_NS = '{http://www.hancom.co.kr/hwpml/2011/core}'

NAMESPACES = {
    'hp': 'http://www.hancom.co.kr/hwpml/2011/paragraph',
    'hs': 'http://www.hancom.co.kr/hwpml/2011/section',
    'hc': 'http://www.hancom.co.kr/hwpml/2011/core',
}

for prefix, uri in NAMESPACES.items():
    ET.register_namespace(prefix, uri)


# ==============================================================================
# Phase 1: 라벨 정규화 및 플레이스홀더 인식
# ==============================================================================

# ==============================================================================
# Phase 2: 라벨 별칭 DB (동의어 매핑)
# ==============================================================================

# 정규화된 대표 라벨 → [별칭 리스트]
# 검색 시: YAML 라벨의 별칭들도 함께 검색
LABEL_ALIASES = {
    # 기업 관련
    "기업명": ["기업체명", "회사명", "상호", "법인명", "업체명"],
    "대표자": ["대표이사", "대표자명", "대표", "대표자또는대표이사", "대표자또는대표이사(본인)"],
    "사업자등록번호": ["사업자번호", "사업자등록", "등록번호", "사업자번호또는법인번호"],
    
    # 담당자 관련  
    "성명": ["이름", "담당자명", "담당자", "작성자"],
    "부서명": ["부서", "소속부서", "소속"],
    "직위": ["직책", "직급"],
    
    # 연락처 관련
    "휴대폰": ["휴대전화", "핸드폰", "모바일", "H.P", "HP"],
    "전화": ["전화번호", "유선전화", "TEL"],
    "이메일": ["E-mail", "email", "메일", "이메일주소"],
    "연락처": ["전화", "전화번호", "연락처"],
    
    # 주소 관련
    "주소": ["소재지", "사업장주소", "본사주소", "회사주소"],
    
    # 신청 관련
    "신청기업명": ["신청기업", "신청업체명", "신청회사명"],
    "신청자": ["신청인", "신청자명"],
    "신청일": ["신청일자", "접수일", "접수일자"],
    
    # 설립 관련
    "설립일자": ["설립일", "창업일", "창업일자", "개업일"],
    
    # 수신자 관련
    "귀중": ["귀하", "앞"],
}

# 역방향 매핑 생성 (별칭 → 대표 라벨)
ALIAS_TO_CANONICAL = {}
for canonical, aliases in LABEL_ALIASES.items():
    ALIAS_TO_CANONICAL[canonical] = canonical
    for alias in aliases:
        ALIAS_TO_CANONICAL[alias] = canonical

def get_label_variants(label: str) -> List[str]:
    """라벨의 모든 변형 반환 (자신 + 별칭들)
    
    Examples:
        "기업명" → ["기업명", "기업체명", "회사명", "상호", "법인명", "업체명"]
        "unknown" → ["unknown"]
    """
    normalized = normalize_label(label).replace(':', '').strip()
    
    # 대표 라벨이면 자신 + 별칭들
    if normalized in LABEL_ALIASES:
        return [normalized] + LABEL_ALIASES[normalized]
    
    # 별칭이면 대표 라벨 + 모든 별칭들
    if normalized in ALIAS_TO_CANONICAL:
        canonical = ALIAS_TO_CANONICAL[normalized]
        return [canonical] + LABEL_ALIASES.get(canonical, [])
    
    # 미등록 라벨
    return [normalized]

def normalize_label(text: str) -> str:
    """한국 공문서 라벨 정규화
    
    처리:
    1. 연속 공백 → 단일 공백
    2. 한글 자간 공백 제거 (신  청  자 → 신청자)
    3. 콜론 정규화 (：→ :)
    4. 접미사 제거 ((인), (서명) 등)
    
    Examples:
        "신  청  자 :" → "신청자:"
        "기 업 체 명" → "기업체명"
        "대표자    (인)" → "대표자"
    """
    if not text:
        return ""
    
    # 1. 전각 콜론 → 반각 콜론
    text = text.replace('：', ':')
    
    # 2. 한글 자간 공백 제거 (한글 문자 사이의 공백)
    # 예: "신  청  자" → "신청자"
    text = re.sub(r'([가-힣])\s+([가-힣])', r'\1\2', text)
    # 반복 적용 (3글자 이상의 경우)
    text = re.sub(r'([가-힣])\s+([가-힣])', r'\1\2', text)
    text = re.sub(r'([가-힣])\s+([가-힣])', r'\1\2', text)
    
    # 3. 연속 공백 → 단일 공백
    text = re.sub(r'\s+', ' ', text)
    
    # 4. 접미사 제거 (인), (서명), (날인), (직인)
    text = re.sub(r'\s*\([인서명날직]\w*\)\s*$', '', text)
    
    # 5. 앞뒤 공백 제거
    text = text.strip()
    
    return text


# 플레이스홀더 패턴 (빈 값으로 인식해야 할 것들)
PLACEHOLDER_PATTERNS = [
    r'^[ㅇ○◯]{2,}$',                    # ㅇㅇㅇ, ○○○
    r'^[_\-]{3,}$',                      # ___, ---
    r'^\s*$',                            # 빈 값
    r'^\([인서명날직]\w*\)$',            # (인), (서명), (날인), (직인)
    r'^\(법인\s*서명\)$',                # (법인 서명)
    r'^\(개인\s*서명\)$',                # (개인 서명)
    r'^\d{2,4}\s*년\s*월\s*일$',         # 20  년  월  일, 2025년 월 일
    r'^년\s*월\s*일$',                   # 년  월  일
]

def is_placeholder(text: str) -> bool:
    """값이 플레이스홀더인지 확인
    
    플레이스홀더 = 실제 데이터가 아닌 자리 표시자
    
    Examples:
        "ㅇㅇㅇ" → True
        "(인)" → True  
        "20  년  월  일" → True
        "홍길동" → False
    """
    if not text:
        return True
    
    text = text.strip()
    if not text:
        return True
    
    # 패턴 매칭
    for pattern in PLACEHOLDER_PATTERNS:
        if re.match(pattern, text, re.IGNORECASE):
            return True
    
    return False


# ==============================================================================
# Phase 2: 날짜 패턴 인식
# ==============================================================================

# 날짜 플레이스홀더 패턴들
DATE_PLACEHOLDER_PATTERNS = [
    # "2025년   월   일" - 연도만 있고 월일이 비어있음
    r'^(\d{4})\s*년\s+월\s+일\s*$',
    # "20  년  월  일" - 연도 앞 두자리만 있음
    r'^(\d{2})\s+년\s+월\s+일\s*$',
    # "년  월  일" - 전부 비어있음
    r'^년\s+월\s+일\s*$',
]

def is_date_placeholder(text: str) -> bool:
    """날짜 플레이스홀더인지 확인
    
    Examples:
        "2025년   월   일" → True
        "20  년  월  일" → True
        "년  월  일" → True
        "2025년 11월 30일" → False (완성된 날짜)
    """
    if not text:
        return False
    
    text = text.strip()
    for pattern in DATE_PLACEHOLDER_PATTERNS:
        if re.match(pattern, text):
            return True
    return False


def format_current_date(template: str = None) -> str:
    """현재 날짜를 한국식 형식으로 반환
    
    Args:
        template: 날짜 템플릿 (None이면 기본 형식)
        
    Returns:
        "2025년 11월 30일" 형식
    """
    now = datetime.now()
    return f"{now.year}년 {now.month}월 {now.day}일"


def fill_date_placeholder(text: str) -> str:
    """날짜 플레이스홀더를 현재 날짜로 채움
    
    Examples:
        "2025년   월   일" → "2025년 11월 30일"
        "20  년  월  일" → "2025년 11월 30일"
    """
    now = datetime.now()
    
    # 패턴 1: 연도 있음
    match = re.match(r'^(\d{4})\s*년\s+월\s+일\s*$', text.strip())
    if match:
        year = int(match.group(1))
        return f"{year}년 {now.month}월 {now.day}일"
    
    # 패턴 2: 연도 앞 두자리
    match = re.match(r'^(\d{2})\s+년\s+월\s+일\s*$', text.strip())
    if match:
        year_prefix = match.group(1)
        # 20XX 형태로 가정
        year = int(f"20{year_prefix[-1]}{now.year % 10}" if len(year_prefix) == 2 else f"{year_prefix}{now.year % 100}")
        return f"{now.year}년 {now.month}월 {now.day}일"
    
    # 패턴 3: 전부 비어있음
    if re.match(r'^년\s+월\s+일\s*$', text.strip()):
        return f"{now.year}년 {now.month}월 {now.day}일"
    
    return text


# ==============================================================================
# Phase 2: 서명란 패턴 인식
# ==============================================================================

# 서명란 패턴: "라벨 : 플레이스홀더 (인/서명)"
# 예: "신  청  자 :             (인)"
#     "기업명 :     ㅇㅇㅇ  (인)"
#     "대표자 :     ㅇㅇㅇ  (인)"

SIGNATURE_SUFFIXES = ['(인)', '(印)', '(서명)', '(날인)', '(직인)', 
                      '(법인 서명)', '(개인 서명)', '(법인서명)', '(개인서명)']

def parse_signature_line(text: str) -> Optional[dict]:
    """서명란 패턴에서 라벨 추출
    
    Examples:
        "신  청  자 :             (인)" → {"label": "신청자", "suffix": "(인)"}
        "기업명 :     ㅇㅇㅇ  (인)" → {"label": "기업명", "suffix": "(인)"}
        
    Returns:
        {"label": 정규화된 라벨, "suffix": 서명 접미사} 또는 None
    """
    if not text:
        return None
    
    text = text.strip()
    
    # 서명 접미사 확인
    suffix_found = None
    for suffix in SIGNATURE_SUFFIXES:
        if text.endswith(suffix):
            suffix_found = suffix
            text = text[:-len(suffix)].strip()
            break
    
    if not suffix_found:
        return None
    
    # 플레이스홀더 제거 (ㅇㅇㅇ 등)
    text = re.sub(r'[ㅇ○◯]+', '', text).strip()
    
    # 콜론으로 분리
    if ':' in text:
        parts = text.split(':')
        label = parts[0].strip()
    elif '：' in text:
        parts = text.split('：')
        label = parts[0].strip()
    else:
        label = text
    
    # 라벨 정규화
    label = normalize_label(label)
    
    if not label:
        return None
    
    return {"label": label, "suffix": suffix_found}


def calc_similarity(s1: str, s2: str) -> float:
    """두 문자열의 유사도 계산 (0.0 ~ 1.0)
    
    간단한 방식: 공통 문자 비율
    """
    if not s1 or not s2:
        return 0.0
    
    # 정규화
    n1 = normalize_label(s1).replace(':', '').replace(' ', '').lower()
    n2 = normalize_label(s2).replace(':', '').replace(' ', '').lower()
    
    if not n1 or not n2:
        return 0.0
    
    if n1 == n2:
        return 1.0
    
    # 포함 관계
    if n1 in n2:
        return len(n1) / len(n2)
    if n2 in n1:
        return len(n2) / len(n1)
    
    # 공통 문자 수
    common = sum(1 for c in n1 if c in n2)
    return common / max(len(n1), len(n2))


class InjectionMode(Enum):
    """주입 모드"""
    AUTO = "auto"           # 자동 감지 (기본값)
    NEXT_CELL = "next_cell" # 다음 셀에 작성
    APPEND = "append"       # 라벨 뒤에 붙이기
    REPLACE = "replace"     # 라벨 전체 교체
    SKIP_COLON = "skip_colon"  # [라벨] | [:] | [값] 패턴 - 2칸 뒤에 주입
    PREPEND = "prepend"     # [_____ 라벨] 패턴 - 라벨 앞 밑줄에 주입


@dataclass
class FieldSpec:
    """필드 주입 명세"""
    label: str              # 찾을 라벨
    value: str              # 주입할 값
    mode: InjectionMode = InjectionMode.AUTO  # 주입 모드
    
    @classmethod
    def from_dict(cls, d: dict) -> 'FieldSpec':
        mode_str = d.get('mode', 'auto')
        try:
            mode = InjectionMode(mode_str)
        except ValueError:
            mode = InjectionMode.AUTO
        return cls(
            label=d['label'],
            value=str(d['value']),
            mode=mode
        )


@dataclass
class InjectionConfig:
    """주입 설정"""
    fields: List[FieldSpec] = field(default_factory=list)
    keywords: Dict[str, str] = field(default_factory=dict)  # (키워드) 패턴
    tables: Dict[str, List[List[str]]] = field(default_factory=dict)
    title: Optional[str] = None


def parse_yaml_config(yaml_path: str) -> InjectionConfig:
    """YAML 설정 파일 파싱"""
    with open(yaml_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    result = InjectionConfig()
    
    if not config:
        return result
    
    result.title = config.get('title')
    result.keywords = config.get('keywords', {})
    result.tables = config.get('tables', {})
    
    # fields 파싱 (새로운 형식)
    for field_dict in config.get('fields', []):
        result.fields.append(FieldSpec.from_dict(field_dict))
    
    # 하위 호환성: labels, cells → fields로 변환
    for label, value in config.get('labels', {}).items():
        result.fields.append(FieldSpec(label=label, value=value, mode=InjectionMode.APPEND))
    
    for label, value in config.get('cells', {}).items():
        result.fields.append(FieldSpec(label=label, value=value, mode=InjectionMode.NEXT_CELL))
    
    return result


class SmartInjector:
    """스마트 인젝터 v3 - 정규화 + colSpan 인식"""
    
    def __init__(self, xml_content: str):
        self.original_xml = xml_content
        self.root = ET.fromstring(xml_content)
        self.injection_log = []  # 주입 로그
    
    def log(self, message: str):
        """로그 기록"""
        self.injection_log.append(message)
        print(f"  {message}")
    
    def get_cell_text(self, tc) -> str:
        """셀의 전체 텍스트 추출"""
        return ''.join(t.text or '' for t in tc.iter(f'{HP_NS}t'))
    
    def get_cell_span(self, tc) -> dict:
        """셀의 병합 정보 추출"""
        cell_span = tc.find(f'{HP_NS}cellSpan')
        if cell_span is not None:
            return {
                'col': int(cell_span.get('colSpan', 1)),
                'row': int(cell_span.get('rowSpan', 1))
            }
        return {'col': 1, 'row': 1}
    
    def is_cell_empty(self, tc) -> bool:
        """셀이 비어있는지 확인 (플레이스홀더도 빈 것으로 취급)"""
        texts = list(tc.iter(f'{HP_NS}t'))
        if not texts:
            return True
        
        cell_text = ''.join((t.text or '') for t in texts).strip()
        
        # 빈 문자열
        if not cell_text:
            return True
        
        # 플레이스홀더 체크
        if is_placeholder(cell_text):
            return True
        
        return False
    
    def inject_to_cell(self, tc, value: str) -> bool:
        """셀에 값 주입"""
        # 기존 hp:t 요소 찾기
        texts = list(tc.iter(f'{HP_NS}t'))
        
        if texts:
            # 첫 번째 빈 hp:t에 값 설정
            for t in texts:
                if (t.text or '').strip() == '' or is_placeholder((t.text or '')):
                    t.text = value
                    return True
            # 모든 hp:t가 비어있지 않으면 첫 번째에 추가
            texts[0].text = (texts[0].text or '') + value
            return True
        else:
            # hp:t가 없으면 hp:run 안에 생성
            runs = list(tc.iter(f'{HP_NS}run'))
            if runs:
                t_elem = ET.SubElement(runs[0], f'{HP_NS}t')
                t_elem.text = value
                return True
        return False
    
    def detect_injection_mode(self, label: str, tc, row_cells: list, cell_idx: int) -> InjectionMode:
        """자동 감지: 다음 셀 존재 여부 기반
        
        규칙 (HWPX 테이블 분석 결과):
        1. 라벨 앞에 공백 run이 있음 → PREPEND (밑줄 영역에 값)
        2. 다음 셀이 존재하고 비어있음 → NEXT_CELL (값을 다음 셀에)
        3. 다음 셀이 ':'만 있고, 그 다음 셀이 비어있음 → SKIP_COLON (2칸 뒤에)
        4. 다음 셀이 없거나 내용이 있음 → APPEND (라벨 뒤에 붙이기)
        
        ※ colSpan은 라벨 셀의 크기일 뿐, 값 위치와 무관함
           예: "대표자"(colSpan=2) 옆에 빈 셀(colSpan=2) → NEXT_CELL
           예: [기 업 체 명] | [:] | [빈칸] → SKIP_COLON (2칸 뒤에 값)
           예: [___ 귀중] → PREPEND (밑줄 자리에 값)
        """
        # 1. PREPEND 패턴 감지: 셀 내에서 라벨 앞에 공백 run이 있는지
        runs = list(tc.iter(f'{HP_NS}run'))
        if len(runs) >= 2:
            # 라벨이 포함된 run 찾기
            label_run_idx = -1
            norm_label = normalize_label(label)
            for i, run in enumerate(runs):
                t = run.find(f'{HP_NS}t')
                if t is not None and t.text:
                    if norm_label in normalize_label(t.text):
                        label_run_idx = i
                        break
            
            # 라벨 run 앞에 공백만 있는 run이 있으면 PREPEND
            if label_run_idx > 0:
                prev_run = runs[label_run_idx - 1]
                prev_t = prev_run.find(f'{HP_NS}t')
                if prev_t is not None and prev_t.text:
                    # 공백만 있고 최소 5자 이상이면 밑줄 영역으로 판단
                    if prev_t.text.strip() == '' and len(prev_t.text) >= 5:
                        return InjectionMode.PREPEND
        
        # 2. 다음 셀 확인
        has_next_empty_cell = False
        skip_colon_pattern = False
        
        if cell_idx + 1 < len(row_cells):
            next_tc = row_cells[cell_idx + 1]
            next_text = self.get_cell_text(next_tc).strip()
            
            # 다음 셀이 콜론만 있는 경우 (: 또는 ：)
            if next_text in [':', '：']:
                # 그 다음 셀(2칸 뒤)이 비어있는지 확인
                if cell_idx + 2 < len(row_cells):
                    next_next_tc = row_cells[cell_idx + 2]
                    if self.is_cell_empty(next_next_tc):
                        skip_colon_pattern = True
            elif self.is_cell_empty(next_tc):
                has_next_empty_cell = True
        
        if skip_colon_pattern:
            return InjectionMode.SKIP_COLON
        elif has_next_empty_cell:
            return InjectionMode.NEXT_CELL
        else:
            return InjectionMode.APPEND
    
    def match_label(self, search_label: str, cell_text: str, threshold: float = 0.8) -> bool:
        """라벨 매칭 (정규화 + 별칭 DB + 퍼지 매칭 + 서명란 인식)
        
        Args:
            search_label: 찾으려는 라벨
            cell_text: 셀의 텍스트
            threshold: 유사도 임계값 (기본 80%)
        """
        # 정규화
        norm_cell = normalize_label(cell_text)
        norm_cell_no_colon = norm_cell.replace(':', '').strip()
        
        # 셀 텍스트가 너무 길면 라벨이 아닐 가능성 높음 (섹션 제목 등)
        # 단, 서명란은 길 수 있으므로 50자까지 허용
        if len(norm_cell_no_colon) > 50:
            return False
        
        # 서명란 패턴 체크 (예: "신청자 :    (인)")
        sig_info = parse_signature_line(cell_text)
        if sig_info:
            norm_cell_no_colon = sig_info['label'].replace(':', '').strip()
        
        # 라벨의 모든 변형 가져오기 (별칭 DB 활용)
        label_variants = get_label_variants(search_label)
        
        for variant in label_variants:
            norm_search = normalize_label(variant)
            norm_search_no_colon = norm_search.replace(':', '').strip()
            
            # 1. 정확히 일치
            if norm_search == norm_cell:
                return True
            if norm_search_no_colon == norm_cell_no_colon:
                return True
            
            # 2. 시작 부분 일치 (prefix match) - 단, 라벨 길이가 충분해야 함
            #    "신청자" → "신청자격" 매칭 방지: 셀이 라벨보다 훨씬 길면 무시
            len_ratio = len(norm_search_no_colon) / max(len(norm_cell_no_colon), 1)
            if len_ratio >= 0.7:  # 라벨이 셀 길이의 70% 이상이어야 매칭
                if norm_cell.startswith(norm_search) or norm_cell_no_colon.startswith(norm_search_no_colon):
                    return True
            
            # 3. 셀 텍스트가 짧으면 포함 관계 체크 (라벨이 셀 텍스트에 포함)
            #    라벨 길이 비율도 체크
            if len(norm_cell) <= 15 and len_ratio >= 0.7:
                if norm_search_no_colon in norm_cell_no_colon:
                    return True
        
        # 4. 퍼지 매칭 (유사도) - 대표 라벨만으로 체크
        similarity = calc_similarity(search_label, cell_text)
        if similarity >= threshold:
            return True
        
        return False
    
    def inject_field(self, spec: FieldSpec) -> int:
        """필드 주입 - 정규화 + colSpan 인식 적용
        
        Returns: 주입된 횟수
        """
        injected = 0
        
        # 특수값 처리: AUTO_DATE → 현재 날짜
        value = spec.value
        if value == "AUTO_DATE":
            value = format_current_date()
        
        # 1단계: 모든 테이블 순회
        for tbl in self.root.iter(f'{HP_NS}tbl'):
            for tr in tbl.iter(f'{HP_NS}tr'):
                row_cells = list(tr.findall(f'{HP_NS}tc'))
                
                for cell_idx, tc in enumerate(row_cells):
                    cell_text = self.get_cell_text(tc)
                    
                    # 라벨 매칭 (정규화 + 퍼지 매칭)
                    if not self.match_label(spec.label, cell_text):
                        continue
                    
                    # 모드 결정 (명시적 > 자동)
                    if spec.mode == InjectionMode.AUTO:
                        mode = self.detect_injection_mode(spec.label, tc, row_cells, cell_idx)
                    else:
                        mode = spec.mode
                    
                    # colSpan 정보 로깅
                    cell_span = self.get_cell_span(tc)
                    span_info = f"(colSpan={cell_span['col']})" if cell_span['col'] > 1 else ""
                    
                    # 모드에 따라 주입
                    if mode == InjectionMode.NEXT_CELL:
                        # 다음 셀에 주입
                        if cell_idx + 1 < len(row_cells):
                            next_tc = row_cells[cell_idx + 1]
                            if self.inject_to_cell(next_tc, value):
                                self.log(f"✓ [{spec.label}] → 다음셀에 '{value[:20]}...' 주입")
                                injected += 1
                                break
                    
                    elif mode == InjectionMode.APPEND:
                        # 라벨 뒤에 붙이기
                        texts = list(tc.iter(f'{HP_NS}t'))
                        for t in texts:
                            if spec.label in (t.text or ''):
                                # 콜론 뒤에 값 추가
                                current = t.text or ''
                                if current.rstrip().endswith(':') or current.rstrip().endswith('：'):
                                    t.text = current.rstrip() + ' ' + value
                                else:
                                    t.text = current + ' ' + value
                                self.log(f"✓ [{spec.label}] ← 뒤에 '{value[:20]}...' 붙임")
                                injected += 1
                                break
                        if injected:
                            break
                    
                    elif mode == InjectionMode.REPLACE:
                        # 라벨 전체 교체
                        texts = list(tc.iter(f'{HP_NS}t'))
                        if texts:
                            texts[0].text = value
                            self.log(f"✓ [{spec.label}] = '{value[:20]}...'로 교체")
                            injected += 1
                            break
                    
                    elif mode == InjectionMode.SKIP_COLON:
                        # [라벨] | [:] | [값] 패턴 - 2칸 뒤 셀에 주입
                        if cell_idx + 2 < len(row_cells):
                            target_tc = row_cells[cell_idx + 2]
                            if self.inject_to_cell(target_tc, value):
                                self.log(f"✓ [{spec.label}] → 콜론 건너뛰고 '{value[:20]}...' 주입")
                                injected += 1
                                break
                    
                    elif mode == InjectionMode.PREPEND:
                        # [___ 라벨] 패턴 - 라벨 앞 밑줄 영역에 주입
                        runs = list(tc.iter(f'{HP_NS}run'))
                        norm_label = normalize_label(spec.label)
                        for i, run in enumerate(runs):
                            t = run.find(f'{HP_NS}t')
                            if t is not None and t.text and norm_label in normalize_label(t.text):
                                # 이 run 앞의 run에 값 주입
                                if i > 0:
                                    prev_run = runs[i - 1]
                                    prev_t = prev_run.find(f'{HP_NS}t')
                                    if prev_t is not None:
                                        prev_t.text = value
                                        self.log(f"✓ [{spec.label}] ← 앞 밑줄에 '{value[:20]}...' 주입")
                                        injected += 1
                                        break
                        if injected:
                            break
                
                if injected:
                    break
            if injected:
                break
        
        # 2단계: 테이블에서 못 찾으면 일반 paragraph에서 검색
        if not injected:
            injected = self._inject_in_paragraph(spec, value)
        
        if not injected:
            self.log(f"✗ [{spec.label}] 찾지 못함")
        
        return injected
    
    def _inject_in_paragraph(self, spec: FieldSpec, value: str = None) -> int:
        """일반 paragraph (테이블 외부) 에서 라벨 찾아 주입
        
        패턴: "라벨 : " 형태에서 콜론 뒤에 값 추가
        """
        if value is None:
            value = spec.value
            if value == "AUTO_DATE":
                value = format_current_date()
        
        for t_elem in self.root.iter(f'{HP_NS}t'):
            text = t_elem.text or ''
            
            # 정규화 후 매칭
            if not self.match_label(spec.label, text):
                continue
            
            # 서명란 패턴 체크
            sig_info = parse_signature_line(text)
            if sig_info:
                # 서명란: 플레이스홀더를 값으로 교체, 서명 접미사 유지
                # "신청자 :     (인)" → "신청자 : 김철수 (인)"
                label_part = sig_info['label']
                suffix = sig_info['suffix']
                
                # 원본 라벨 형태 유지하면서 값 삽입
                # 정규화된 라벨로 찾아서 교체
                new_text = re.sub(
                    r'^(.*?[:：]\s*).*?' + re.escape(suffix) + r'\s*$',
                    rf'\1{value} {suffix}',
                    text
                )
                if new_text != text:
                    t_elem.text = new_text
                    self.log(f"✓ [{spec.label}] ← (서명란) '{value[:15]}...' 주입")
                    return 1
            
            # 일반 패턴: 콜론 뒤에 값 추가
            current = text.rstrip()
            if current.endswith(':') or current.endswith('：'):
                t_elem.text = current + ' ' + value
                self.log(f"✓ [{spec.label}] ← (본문) 뒤에 '{value[:20]}...' 붙임")
                return 1
            else:
                # 콜론이 없으면 공백 추가
                t_elem.text = text + ' ' + value
                self.log(f"✓ [{spec.label}] ← (본문) 뒤에 '{value[:20]}...' 붙임")
                return 1
        
        return 0
    
    def inject_date_placeholders(self) -> int:
        """문서 전체에서 날짜 플레이스홀더를 찾아 현재 날짜로 채움
        
        패턴: "2025년   월   일", "20  년  월  일", "년  월  일"
        """
        count = 0
        for t_elem in self.root.iter(f'{HP_NS}t'):
            text = t_elem.text or ''
            if is_date_placeholder(text):
                new_text = fill_date_placeholder(text)
                if new_text != text:
                    t_elem.text = new_text
                    self.log(f"✓ [날짜] '{text.strip()[:15]}...' → '{new_text}'")
                    count += 1
        return count
    
    def inject_split_date_cells(self) -> int:
        """분리된 날짜 셀 패턴을 찾아 현재 날짜로 채움
        
        패턴: [년] | [월] | [일] - 각각 별도 셀로 구성
        테이블 행에서 연속된 3개 셀이 '년', '월', '일'로 끝나면 날짜 주입
        """
        count = 0
        now = datetime.now()
        
        for tbl in self.root.iter(f'{HP_NS}tbl'):
            for tr in tbl.iter(f'{HP_NS}tr'):
                cells = list(tr.findall(f'{HP_NS}tc'))
                
                # 연속된 3개 셀에서 년/월/일 패턴 찾기
                for i in range(len(cells) - 2):
                    cell1_text = self.get_cell_text(cells[i]).strip()
                    cell2_text = self.get_cell_text(cells[i+1]).strip()
                    cell3_text = self.get_cell_text(cells[i+2]).strip()
                    
                    # 패턴 매칭: 셀이 '년', '월', '일'로 끝나는지
                    if cell1_text.endswith('년') and cell2_text.endswith('월') and cell3_text.endswith('일'):
                        # 이미 숫자가 있는지 확인 (빈 플레이스홀더만 채움)
                        year_match = re.search(r'\d{4}', cell1_text)
                        month_match = re.search(r'\d{1,2}', cell2_text)
                        day_match = re.search(r'\d{1,2}', cell3_text)
                        
                        injected_any = False
                        
                        # 년 셀 처리
                        if not year_match or cell1_text.strip() == '년':
                            t_elems = list(cells[i].iter(f'{HP_NS}t'))
                            if t_elems:
                                t_elems[0].text = f"{now.year}년"
                                injected_any = True
                        
                        # 월 셀 처리
                        if not month_match or cell2_text.strip() == '월':
                            t_elems = list(cells[i+1].iter(f'{HP_NS}t'))
                            if t_elems:
                                t_elems[0].text = f"{now.month}월"
                                injected_any = True
                        
                        # 일 셀 처리
                        if not day_match or cell3_text.strip() == '일':
                            t_elems = list(cells[i+2].iter(f'{HP_NS}t'))
                            if t_elems:
                                t_elems[0].text = f"{now.day}일"
                                injected_any = True
                        
                        if injected_any:
                            self.log(f"✓ [분리날짜] '{cell1_text}|{cell2_text}|{cell3_text}' → '{now.year}년|{now.month}월|{now.day}일'")
                            count += 1
        
        return count
    
    def inject_signature_fields(self, config: InjectionConfig) -> int:
        """서명란 패턴을 찾아 해당 필드 값으로 채움
        
        패턴: "라벨 : ㅇㅇㅇ (인)", "라벨 :     (인)"
        """
        count = 0
        
        # 필드 값 맵 생성 (정규화된 라벨 → 값)
        field_map = {}
        for spec in config.fields:
            norm_label = normalize_label(spec.label).replace(':', '').strip()
            field_map[norm_label] = spec.value
            
            # 별칭도 등록
            for variant in get_label_variants(spec.label):
                norm_variant = normalize_label(variant).replace(':', '').strip()
                field_map[norm_variant] = spec.value
        
        for t_elem in self.root.iter(f'{HP_NS}t'):
            text = t_elem.text or ''
            sig_info = parse_signature_line(text)
            
            if not sig_info:
                continue
            
            # 서명란 라벨에 해당하는 값 찾기
            label = sig_info['label'].replace(':', '').strip()
            suffix = sig_info['suffix']
            
            value = field_map.get(label)
            if not value:
                continue
            
            # 이미 값이 채워져 있으면 건너뜀
            if value in text:
                continue
            
            # 서명란 형식으로 값 주입
            # "라벨 :     ㅇㅇㅇ (인)" → "라벨 : 값 (인)"
            new_text = re.sub(
                r'^(.*?[:：]\s*).*?' + re.escape(suffix) + r'\s*$',
                rf'\g<1>{value} {suffix}',
                text.strip()
            )
            
            # 원래 앞 공백 유지
            leading_spaces = len(text) - len(text.lstrip())
            new_text = ' ' * leading_spaces + new_text
            
            if new_text != text:
                t_elem.text = new_text
                self.log(f"✓ [{label}] ← (서명란) '{value[:15]}...' 주입")
                count += 1
        
        return count
    
    def inject_keyword(self, keyword: str, value: str) -> int:
        """(키워드) 패턴 주입"""
        # regex로 처리 (기존 방식)
        pattern = rf'\({re.escape(keyword)}\)</hp:t></hp:run>(<hp:run[^>]*>)<hp:t>\s*</hp:t>'
        replacement = rf'({keyword})</hp:t></hp:run>\1<hp:t> {value}</hp:t>'
        
        xml_str = ET.tostring(self.root, encoding='unicode')
        new_xml, count = re.subn(pattern, replacement, xml_str)
        
        if count > 0:
            self.root = ET.fromstring(new_xml)
            self.log(f"✓ ({keyword}) → '{value[:30]}...' 주입")
        
        return count
    
    def process(self, config: InjectionConfig) -> str:
        """전체 주입 처리"""
        print("\n" + "="*60)
        print("🔧 Smart Injector v2 - 주입 시작")
        print("="*60)
        
        total_injected = 0
        
        # 0. 날짜 플레이스홀더 자동 주입 (Phase 2)
        date_count = self.inject_date_placeholders()
        if date_count > 0:
            print(f"\n📅 날짜 자동 주입 ({date_count}개)")
            total_injected += date_count
        
        # 0.5. 분리된 날짜 셀 자동 주입 (년|월|일 패턴)
        split_date_count = self.inject_split_date_cells()
        if split_date_count > 0:
            print(f"\n📅 분리 날짜 자동 주입 ({split_date_count}개)")
            total_injected += split_date_count
        
        # 1. 필드 주입 (2단계 규칙)
        if config.fields:
            print(f"\n📝 필드 주입 ({len(config.fields)}개):")
            for spec in config.fields:
                total_injected += self.inject_field(spec)
        
        # 1.5. 서명란 자동 주입 (Phase 2)
        sig_count = self.inject_signature_fields(config)
        if sig_count > 0:
            print(f"\n✍️ 서명란 자동 주입 ({sig_count}개)")
            total_injected += sig_count
        
        # 2. 키워드 주입
        if config.keywords:
            print(f"\n🔑 키워드 주입 ({len(config.keywords)}개):")
            for keyword, value in config.keywords.items():
                total_injected += self.inject_keyword(keyword, value)
        
        print(f"\n✅ 총 {total_injected}개 주입 완료")
        
        return ET.tostring(self.root, encoding='unicode')


def remove_linesegarray(xml_content: str) -> str:
    """linesegarray 제거"""
    return re.sub(
        r'<hp:linesegarray>.*?</hp:linesegarray>',
        '',
        xml_content,
        flags=re.DOTALL
    )


# ==============================================================================
# 분석 기능 (analyze 명령)
# ==============================================================================

# 알려진 라벨 패턴 (정규화용) - 분석시 사용
KNOWN_LABELS_FOR_ANALYZE = {
    "기업명": ["기업체명", "회사명", "상호", "법인명", "업체명"],
    "대표자": ["대표이사", "대표자명", "대표", "대표자또는대표이사"],
    "사업자등록번호": ["사업자번호", "사업자등록", "등록번호", "사업자번호또는법인번호"],
    "설립일자": ["설립일", "창업일", "창업일자", "개업일"],
    "주소": ["소재지", "사업장주소", "본사주소", "회사주소"],
    "성명": ["이름", "담당자명", "담당자", "작성자"],
    "부서명": ["부서", "소속부서", "소속"],
    "직위": ["직책", "직급"],
    "휴대폰": ["휴대전화", "핸드폰", "모바일", "HP"],
    "전화": ["전화번호", "유선전화", "TEL"],
    "이메일": ["E-mail", "email", "메일", "이메일주소"],
    "연락처": ["전화", "전화번호"],
    "신청기업명": ["신청기업", "신청업체명"],
    "신청자": ["신청인", "신청자명"],
    "신청일": ["신청일자", "접수일"],
    "귀중": ["귀하", "앞"],
}

FIELD_EXAMPLES = {
    "기업명": "(주)스마트테크",
    "대표자": "홍길동",
    "사업자등록번호": "123-45-67890",
    "설립일자": "2018-03-15",
    "주소": "서울시 강남구 테헤란로 123",
    "부서명": "기술개발팀",
    "직위": "팀장",
    "성명": "김담당",
    "휴대폰": "010-1234-5678",
    "전화": "02-555-1234",
    "이메일": "contact@company.co.kr",
    "연락처": "02-555-1234",
    "신청기업명": "(기업명과 동일)",
    "신청자": "(대표자와 동일)",
    "신청일": "AUTO_DATE",
    "귀중": "중소벤처기업부장관",
}


@dataclass
class AnalyzedField:
    """분석된 필드 정보"""
    label: str
    normalized: str
    section: str
    pattern_type: str
    example: str = ""


def find_canonical_for_analyze(label: str) -> str:
    """분석용 정규화 라벨 변환"""
    norm = normalize_label(label)
    for canonical, variants in KNOWN_LABELS_FOR_ANALYZE.items():
        if norm == normalize_label(canonical):
            return canonical
        for v in variants:
            if norm == normalize_label(v):
                return canonical
    for canonical, variants in KNOWN_LABELS_FOR_ANALYZE.items():
        if normalize_label(canonical) in norm or norm in normalize_label(canonical):
            return canonical
    return label


def is_label_candidate(text: str) -> bool:
    """라벨 후보인지 판단"""
    if not text or len(text) > 30:
        return False
    text = text.strip()
    if not text or text.isdigit():
        return False
    if text.endswith(':') or text.endswith('：'):
        return True
    norm = normalize_label(text)
    for canonical, variants in KNOWN_LABELS_FOR_ANALYZE.items():
        if norm == normalize_label(canonical):
            return True
        for v in variants:
            if norm == normalize_label(v):
                return True
    return False


def analyze_hwpx(hwpx_path: str) -> tuple:
    """HWPX 파일 분석 - 필드 추출"""
    all_fields = []
    meta = {
        "filename": Path(hwpx_path).name,
        "sections": [],
        "analyzed_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    with zipfile.ZipFile(hwpx_path, 'r') as zf:
        section_files = sorted([f for f in zf.namelist() 
                               if f.startswith('Contents/section') and f.endswith('.xml')])
        
        for section_file in section_files:
            section_name = Path(section_file).stem
            meta["sections"].append(section_name)
            
            content = zf.read(section_file).decode('utf-8')
            root = ET.fromstring(content)
            
            seen_labels = set()
            
            # 테이블 필드 추출
            for tbl_idx, tbl in enumerate(root.iter(f'{HP_NS}tbl')):
                for tr in tbl.iter(f'{HP_NS}tr'):
                    cells = list(tr.findall(f'{HP_NS}tc'))
                    for cell_idx, tc in enumerate(cells):
                        texts = [t.text for t in tc.iter(f'{HP_NS}t') if t.text]
                        cell_text = ''.join(texts).strip()
                        
                        if not is_label_candidate(cell_text):
                            continue
                        
                        # 다음 셀 비어있는지 확인
                        has_empty_next = False
                        if cell_idx + 1 < len(cells):
                            next_texts = [t.text for t in cells[cell_idx + 1].iter(f'{HP_NS}t') if t.text]
                            next_text = ''.join(next_texts).strip()
                            if not next_text:
                                has_empty_next = True
                        
                        # PREPEND 패턴 체크
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
                            canonical = find_canonical_for_analyze(cell_text)
                            if canonical not in seen_labels:
                                seen_labels.add(canonical)
                                all_fields.append(AnalyzedField(
                                    label=cell_text,
                                    normalized=canonical,
                                    section=section_name,
                                    pattern_type="prepend" if is_prepend else "table",
                                    example=FIELD_EXAMPLES.get(canonical, "")
                                ))
            
            # 날짜 필드 추출
            date_found = False
            for t_elem in root.iter(f'{HP_NS}t'):
                text = t_elem.text or ''
                if re.search(r'\d{2,4}년\s+월\s+일', text) and not date_found:
                    if "신청일" not in seen_labels:
                        seen_labels.add("신청일")
                        all_fields.append(AnalyzedField(
                            label="날짜",
                            normalized="신청일",
                            section=section_name,
                            pattern_type="date",
                            example="AUTO_DATE"
                        ))
                        date_found = True
    
    # 중복 제거
    seen = set()
    unique_fields = []
    for f in all_fields:
        if f.normalized not in seen:
            seen.add(f.normalized)
            unique_fields.append(f)
    
    return unique_fields, meta


def generate_yaml_template(fields: list, meta: dict) -> str:
    """빈 YAML 템플릿 생성"""
    lines = [
        f"# {meta['filename']} - 데이터 입력",
        f"# 생성일: {meta['analyzed_at']}",
        "#",
        "# 각 필드의 value에 실제 값을 입력하세요",
        "# ============================================================",
        "",
        "fields:"
    ]
    
    current_section = None
    for f in fields:
        if f.section != current_section:
            current_section = f.section
            lines.append(f"  # --- {current_section} ---")
        
        example_comment = f"  # 예: {f.example}" if f.example else ""
        lines.append(f"  - label: \"{f.normalized}\"")
        lines.append(f"    value: \"\"{example_comment}")
        lines.append("")
    
    lines.extend(["keywords: {}", "tables: {}"])
    return '\n'.join(lines)


def generate_prompt(fields: list, meta: dict) -> str:
    """데이터 수집용 프롬프트 생성"""
    lines = [
        f"# {meta['filename']} 작성",
        "",
        "아래 항목들의 값을 입력해 주세요.",
        "형식: `라벨: 값`",
        "",
        "---",
        ""
    ]
    
    for f in fields:
        example = f" (예: {f.example})" if f.example else ""
        lines.append(f"- **{f.normalized}**{example}")
    
    lines.extend([
        "",
        "---",
        "",
        "입력 예시:",
        "```",
        "기업명: (주)ABC",
        "대표자: 홍길동",
        "사업자등록번호: 123-45-67890",
        "```"
    ])
    
    return '\n'.join(lines)


# ==============================================================================
# 응답 파싱 (parse 명령)
# ==============================================================================

def parse_response(response_text: str) -> dict:
    """사용자 응답을 YAML 구조로 파싱
    
    지원 형식:
    - "라벨: 값"
    - "라벨 : 값"
    - "라벨：값" (전각 콜론)
    """
    fields = []
    
    # 라인별로 파싱
    for line in response_text.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('-'):
            continue
        
        # 콜론으로 분리
        match = re.match(r'^([^:：]+)[:：]\s*(.*)$', line)
        if match:
            label = match.group(1).strip()
            value = match.group(2).strip()
            
            # 빈 값, "없음" 등 제외
            if value and value.lower() not in ['없음', '해당없음', '모름', '-', '']:
                # 라벨 정규화
                canonical = find_canonical_for_analyze(label)
                fields.append({
                    "label": canonical,
                    "value": value
                })
    
    return {"fields": fields, "keywords": {}, "tables": {}}


def generate_yaml_from_response(parsed: dict, meta: dict = None) -> str:
    """파싱된 응답을 YAML 문자열로 변환"""
    lines = [
        f"# 응답 데이터 - {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "#",
        "fields:"
    ]
    
    for field in parsed["fields"]:
        lines.append(f"  - label: \"{field['label']}\"")
        # 값에 따옴표가 필요한 경우 처리
        value = field['value'].replace('"', '\\"')
        lines.append(f"    value: \"{value}\"")
        lines.append("")
    
    lines.extend(["keywords: {}", "tables: {}"])
    return '\n'.join(lines)


def process_hwpx(hwpx_path: str, config: InjectionConfig, output_path: str, 
                 remove_lines: bool = True) -> str:
    """HWPX 파일 처리"""
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # 압축 해제
        with zipfile.ZipFile(hwpx_path, 'r') as zf:
            zf.extractall(temp_dir)
        
        # section XML 파일들 처리
        contents_dir = os.path.join(temp_dir, 'Contents')
        for filename in os.listdir(contents_dir):
            if filename.startswith('section') and filename.endswith('.xml'):
                section_path = os.path.join(contents_dir, filename)
                
                with open(section_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 스마트 인젝터로 처리
                injector = SmartInjector(content)
                modified = injector.process(config)
                
                # linesegarray 제거
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
    
    print(f"\n📄 생성: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description='Smart Injector v3 - 통합 HWPX 데이터 주입 도구',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
명령어 예시:
  # 1. HWPX 분석 → 프롬프트 생성
  python smart_injector.py analyze input.hwpx -o prefix
  
  # 2. 사용자 응답 → YAML 변환
  python smart_injector.py parse response.txt -o fields.yaml
  
  # 3. 주입 실행
  python smart_injector.py inject input.hwpx fields.yaml -o output.hwpx
  
  # 4. 전체 파이프라인 (대화형)
  python smart_injector.py full input.hwpx -o output.hwpx
"""
    )
    
    subparsers = parser.add_subparsers(dest='command', help='명령어')
    
    # === analyze 명령 ===
    analyze_parser = subparsers.add_parser('analyze', help='HWPX 분석 → 프롬프트 + 템플릿 생성')
    analyze_parser.add_argument('hwpx', help='분석할 HWPX 파일')
    analyze_parser.add_argument('-o', '--output', help='출력 파일 접두사')
    analyze_parser.add_argument('--yaml-only', action='store_true', help='YAML만 생성')
    analyze_parser.add_argument('--prompt-only', action='store_true', help='프롬프트만 생성')
    
    # === parse 명령 ===
    parse_parser = subparsers.add_parser('parse', help='사용자 응답 → YAML 변환')
    parse_parser.add_argument('response', help='응답 텍스트 파일')
    parse_parser.add_argument('-o', '--output', help='출력 YAML 파일', default='parsed_fields.yaml')
    
    # === inject 명령 ===
    inject_parser = subparsers.add_parser('inject', help='HWPX + YAML → 완성 문서')
    inject_parser.add_argument('hwpx', help='HWPX 템플릿 파일')
    inject_parser.add_argument('data', help='주입 설정 YAML 파일')
    inject_parser.add_argument('-o', '--output', help='출력 파일 경로')
    inject_parser.add_argument('--keep-lineseg', action='store_true', help='linesegarray 유지')
    
    # === full 명령 ===
    full_parser = subparsers.add_parser('full', help='전체 파이프라인 (analyze → 입력 대기 → inject)')
    full_parser.add_argument('hwpx', help='HWPX 템플릿 파일')
    full_parser.add_argument('-o', '--output', help='출력 파일 경로')
    full_parser.add_argument('--response', '-r', help='응답 파일 (없으면 대화형 입력)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # === analyze 명령 처리 ===
    if args.command == 'analyze':
        print(f"📂 분석 중: {args.hwpx}")
        fields, meta = analyze_hwpx(args.hwpx)
        print(f"✓ {len(fields)}개 필드 발견")
        
        prefix = args.output if args.output else Path(args.hwpx).stem
        
        if not args.prompt_only:
            yaml_content = generate_yaml_template(fields, meta)
            yaml_path = f"{prefix}_fields.yaml"
            with open(yaml_path, 'w', encoding='utf-8') as f:
                f.write(yaml_content)
            print(f"✓ 저장: {yaml_path}")
        
        if not args.yaml_only:
            prompt_content = generate_prompt(fields, meta)
            prompt_path = f"{prefix}_prompt.md"
            with open(prompt_path, 'w', encoding='utf-8') as f:
                f.write(prompt_content)
            print(f"✓ 저장: {prompt_path}")
        
        print(f"\n📋 발견된 필드:")
        for f in fields:
            print(f"  - {f.normalized} ({f.pattern_type})")
    
    # === parse 명령 처리 ===
    elif args.command == 'parse':
        print(f"📂 파싱 중: {args.response}")
        
        with open(args.response, 'r', encoding='utf-8') as f:
            response_text = f.read()
        
        parsed = parse_response(response_text)
        yaml_content = generate_yaml_from_response(parsed)
        
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(yaml_content)
        
        print(f"✓ {len(parsed['fields'])}개 필드 파싱")
        print(f"✓ 저장: {args.output}")
        
        for field in parsed['fields']:
            print(f"  - {field['label']}: {field['value'][:20]}...")
    
    # === inject 명령 처리 ===
    elif args.command == 'inject':
        config = parse_yaml_config(args.data)
        
        print(f"\n📋 설정 로드: {args.data}")
        print(f"  - 필드: {len(config.fields)}개")
        print(f"  - 키워드: {len(config.keywords)}개")
        print(f"  - 테이블: {len(config.tables)}개")
        
        if args.output:
            output_path = args.output
        else:
            template_path = Path(args.hwpx)
            output_path = str(template_path.parent / f"{template_path.stem}_filled.hwpx")
        
        process_hwpx(
            args.hwpx,
            config,
            output_path,
            remove_lines=not args.keep_lineseg
        )
    
    # === full 명령 처리 ===
    elif args.command == 'full':
        # 1. 분석
        print(f"\n{'='*60}")
        print("📂 Step 1: HWPX 분석")
        print('='*60)
        
        fields, meta = analyze_hwpx(args.hwpx)
        print(f"✓ {len(fields)}개 필드 발견")
        
        for f in fields:
            print(f"  - {f.normalized}")
        
        # 2. 응답 수집
        print(f"\n{'='*60}")
        print("📝 Step 2: 데이터 입력")
        print('='*60)
        
        if args.response:
            # 파일에서 읽기
            with open(args.response, 'r', encoding='utf-8') as f:
                response_text = f.read()
            print(f"✓ 응답 파일 로드: {args.response}")
        else:
            # 대화형 입력
            print("\n각 항목의 값을 입력하세요 (빈 값은 Enter):\n")
            responses = []
            for f in fields:
                example = f" (예: {f.example})" if f.example else ""
                value = input(f"  {f.normalized}{example}: ").strip()
                if value:
                    responses.append(f"{f.normalized}: {value}")
            response_text = '\n'.join(responses)
        
        # 3. 파싱
        parsed = parse_response(response_text)
        print(f"\n✓ {len(parsed['fields'])}개 필드 파싱됨")
        
        # 4. 주입
        print(f"\n{'='*60}")
        print("🔧 Step 3: 주입 실행")
        print('='*60)
        
        # 파싱된 데이터로 config 생성
        config = InjectionConfig(
            fields=[FieldSpec(label=f['label'], value=f['value']) for f in parsed['fields']],
            keywords={},
            tables={}
        )
        
        if args.output:
            output_path = args.output
        else:
            template_path = Path(args.hwpx)
            output_path = str(template_path.parent / f"{template_path.stem}_filled.hwpx")
        
        process_hwpx(args.hwpx, config, output_path, remove_lines=True)
        
        print(f"\n{'='*60}")
        print("✅ 완료!")
        print('='*60)


if __name__ == "__main__":
    main()
