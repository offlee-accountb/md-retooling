"""텍스트 피팅: 열 너비 자동 계산, 자간/폰트 최적화.

_visual_text_width, _estimate_line_count, _fit_cell_text, _compute_col_widths
"""
from __future__ import annotations

import math
import re
from typing import List


# ---------------------------------------------------------------------------
# 자간/폰트 변형용 charPr ID 매핑
# ---------------------------------------------------------------------------

# (font_size_pt, spacing_pct) → charPr ID
TABLE_FIT_CHAR_IDS: dict[tuple[int, int], str] = {
    (11, 0):   "11",   # 기존 표 본문
    (11, -5):  "14",
    (11, -10): "15",
    (11, -15): "16",
    (11, -20): "17",
    (10, 0):   "18",
    (10, -5):  "19",
    (10, -10): "20",
    (10, -15): "21",
    (10, -20): "22",
}

# Bold 버전 (헤더용)
TABLE_FIT_BOLD_CHAR_IDS: dict[tuple[int, int], str] = {
    (11, 0):   "12",   # 기존 표 헤더
    (11, -5):  "23",
    (11, -10): "24",
    (11, -15): "25",
    (11, -20): "26",
    (10, 0):   "27",
    (10, -5):  "28",
    (10, -10): "29",
    (10, -15): "30",
    (10, -20): "31",
}

# 피팅 시도 순서: (font_size, spacing) — 자간 먼저 줄이고, 그 다음 폰트 축소
FIT_CANDIDATES: list[tuple[int, int]] = [
    (11, 0), (11, -5), (11, -10), (11, -15), (11, -20),
    (10, 0), (10, -5), (10, -10), (10, -15), (10, -20),
]


# ---------------------------------------------------------------------------
# 시각적 너비 측정
# ---------------------------------------------------------------------------


def _visual_text_width(text: str) -> float:
    """텍스트의 시각적 너비를 추정한다.

    한글/CJK 문자는 가중치 2.0, ASCII/영숫자는 1.0으로 계산하여
    실제 화면에서 차지하는 폭 비율을 근사한다.
    **bold** 마크업은 제거 후 측정한다.
    """
    # bold 마크업 제거
    clean = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    width = 0.0
    for ch in clean:
        cp = ord(ch)
        # CJK Unified Ideographs, Hangul Syllables, Fullwidth forms, etc.
        if (
            (0xAC00 <= cp <= 0xD7AF)       # 한글 완성형
            or (0x1100 <= cp <= 0x11FF)     # 한글 자모
            or (0x3130 <= cp <= 0x318F)     # 한글 호환 자모
            or (0x4E00 <= cp <= 0x9FFF)     # CJK 한자
            or (0xFF01 <= cp <= 0xFF60)     # Fullwidth Latin
            or (0x3000 <= cp <= 0x303F)     # CJK Symbols
        ):
            width += 2.0
        else:
            width += 1.0
    return width


def _estimate_line_count(
    text: str,
    cell_width_hwp: int,
    font_size_pt: int,
    spacing_pct: int,
) -> float:
    """주어진 셀 폭·폰트·자간에서 텍스트가 차지할 줄 수를 근사한다.

    근사 방법:
      - 글자 1자의 폭 ≈ font_size(pt) × HWPUNIT_PER_PT
      - 한글은 정방형(가로=세로), ASCII는 절반
      - spacing_pct 적용 시 글자 간격이 비례 축소
      - 셀 여백 (좌510 + 우510 = 1020 HWPUNIT) 차감
    """
    HWPUNIT_PER_PT = 100  # charPr height 기준: 1pt = 100 HWPUNIT
    char_base_width = font_size_pt * HWPUNIT_PER_PT  # 한글 1자 기본 폭

    # 자간 적용: spacing_pct는 글자폭 대비 %로, 음수면 좁아짐
    # ex) -20% → 각 자간이 0.2 * char_width만큼 줄어듦
    # 실효 글자폭 = char_width × (1 + spacing_pct/100)
    spacing_factor = 1.0 + spacing_pct / 100.0

    # 셀 여백 차감
    usable_width = cell_width_hwp - 1020  # 좌510 + 우510
    if usable_width <= 0:
        return 999.0

    # bold 마크업 제거 후 글자별 폭 합산
    clean = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    total_text_width = 0.0
    for ch in clean:
        cp = ord(ch)
        if (
            (0xAC00 <= cp <= 0xD7AF)
            or (0x1100 <= cp <= 0x11FF)
            or (0x3130 <= cp <= 0x318F)
            or (0x4E00 <= cp <= 0x9FFF)
            or (0xFF01 <= cp <= 0xFF60)
            or (0x3000 <= cp <= 0x303F)
        ):
            total_text_width += char_base_width * spacing_factor
        else:
            total_text_width += (char_base_width * 0.5) * spacing_factor

    if total_text_width <= 0:
        return 0.0

    return math.ceil(total_text_width / usable_width)


def _fit_cell_text(
    text: str,
    cell_width_hwp: int,
    *,
    is_header: bool = False,
) -> tuple[int, int]:
    """셀 텍스트에 대해 최적 (font_size, spacing) 조합을 결정한다.

    전략:
      1. 11pt spacing=0으로 시작 → 2줄 이하면 바로 채택
      2. 3줄 이상이면 spacing을 -5%씩 줄여서 줄 수가 줄어드는 지점 탐색
      3. -20%까지 해도 개선 안 되면 10pt로 넘어감
      4. 최소 줄 수를 달성하는 조합을 반환

    Returns:
        (font_size_pt, spacing_pct) 튜플
    """
    if not text or not text.strip():
        return (11, 0)

    best = (11, 0)
    best_lines = _estimate_line_count(text, cell_width_hwp, 11, 0)

    # 이미 2줄 이하면 조정 불필요
    if best_lines <= 2:
        return best

    for font_pt, spacing in FIT_CANDIDATES[1:]:  # (11,0) 이미 체크함
        lines = _estimate_line_count(text, cell_width_hwp, font_pt, spacing)
        if lines < best_lines:
            best_lines = lines
            best = (font_pt, spacing)
        # 2줄 이하 달성하면 즉시 채택
        if best_lines <= 2:
            break

    return best


def _compute_col_widths(
    header: List[str],
    rows: List[List[str]],
    col_cnt: int,
    total_width: int,
    *,
    min_ratio: float = 0.12,
) -> List[int]:
    """헤더 + 본문 콘텐츠를 분석하여 최적 열 너비(HWPUNIT)를 반환한다.

    알고리즘:
      1. 각 열에 대해 (헤더 + 모든 행)의 최대 시각적 너비를 측정
      2. 최대 너비 비율에 따라 total_width를 배분
      3. 각 열은 최소 min_ratio(기본 12%) 이상의 폭을 보장
      4. 나머지 1 HWPUNIT은 마지막 열에 보정

    Returns:
        각 열의 너비 리스트 (HWPUNIT, 합계 = total_width)
    """
    # 1) 열별 최대 시각적 너비 수집
    max_widths = [0.0] * col_cnt
    # 헤더
    for col_idx in range(col_cnt):
        if col_idx < len(header):
            max_widths[col_idx] = max(max_widths[col_idx], _visual_text_width(header[col_idx]))
    # 본문 행
    for row in rows:
        for col_idx in range(col_cnt):
            if col_idx < len(row):
                max_widths[col_idx] = max(max_widths[col_idx], _visual_text_width(row[col_idx]))

    # 2) 모든 열의 너비가 0이면 균등 분할 fallback
    total_visual = sum(max_widths)
    if total_visual == 0:
        base = total_width // col_cnt
        widths = [base] * col_cnt
        widths[-1] += total_width - base * col_cnt
        return widths

    # 3) 최소 비율 적용하여 비율 계산
    min_width_hwp = int(total_width * min_ratio)
    ratios = [w / total_visual for w in max_widths]

    # 최소 비율 미달 열에 대해 floor 적용 후 나머지 재배분
    locked = [False] * col_cnt
    locked_sum = 0.0
    for i in range(col_cnt):
        if ratios[i] < min_ratio:
            locked[i] = True
            locked_sum += min_ratio

    remaining_ratio = 1.0 - locked_sum
    unlocked_visual = sum(max_widths[i] for i in range(col_cnt) if not locked[i])

    final_ratios = [0.0] * col_cnt
    for i in range(col_cnt):
        if locked[i]:
            final_ratios[i] = min_ratio
        elif unlocked_visual > 0:
            final_ratios[i] = (max_widths[i] / unlocked_visual) * remaining_ratio
        else:
            final_ratios[i] = remaining_ratio / max(1, sum(1 for x in locked if not x))

    # 4) HWPUNIT으로 변환
    widths = [max(min_width_hwp, int(total_width * r)) for r in final_ratios]

    # 5) 합계 보정 (반올림 오차 → 마지막 열에서 조정)
    diff = total_width - sum(widths)
    widths[-1] += diff

    return widths
