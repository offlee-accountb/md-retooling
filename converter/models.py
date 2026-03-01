"""MD → HWPX 변환기 데이터 모델.

BlockType enum과 Block/TableBlock 등 데이터클래스를 정의한다.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import List


class BlockType(Enum):
    TITLE = auto()       # <주제목>
    SUBTITLE = auto()    # □
    BODY = auto()        # ◦
    DESC2 = auto()       # - (3 spaces)
    DESC3 = auto()       # * (4 spaces)
    EMPHASIS = auto()    # <강조>
    TABLE = auto()       # markdown table
    SUMMARY_TABLE = auto()  # <요약표> 전용
    PROCESS = auto()     # <프로세스> 흐름도
    DIAGRAM = auto()     # <도식도> 레이어 스택
    PLAIN = auto()       # fallback / other


@dataclass
class Block:
    type: BlockType
    raw: str            # original line
    text: str           # content without leading markers


@dataclass
class TableBlock(Block):
    """Markdown 표를 담는 특수 블록."""

    title: str
    header: List[str]
    aligns: List[str]
    rows: List[List[str]]


@dataclass
class SummaryTableBlock(Block):
    """요약표(<요약표 시작> ~ <요약표 끝>) 범위를 하나의 표로 묶는다."""

    items: List[Block]


@dataclass
class ProcessBlock(Block):
    """프로세스 흐름도 (<프로세스> 태그).
    
    rows: 각 행은 (단계명, 담당자) 튜플의 리스트.
           방향이 역방향(←)이면 reversed=True.
    """
    proc_title: str
    proc_rows: List[tuple]  # [(steps, reversed), ...]
    # steps = [(name, desc), ...]


@dataclass
class DiagramBox:
    """도식도 안의 개별 박스."""
    title: str            # Bold 제목
    items: List[str]      # 내용 항목들 (· xxx)


@dataclass
class DiagramBlock(Block):
    """도식도 (<도식도> 태그).
    
    layers: 각 레이어는 DiagramBox 리스트.
    connectors: 레이어 간 연결 ('↓' 또는 '↔').
    """
    diagram_title: str
    layers: List[List]       # [layer1_boxes, layer2_boxes, ...]
    connectors: List[str]    # ['↓', '↔', ...] (len = len(layers) - 1)


@dataclass
class DocumentMetadata:
    title: str
    creator: str
    subject: str
    description: str
    last_saved_by: str
    keyword: str
    created_at: datetime
    modified_at: datetime
    display_date: str
