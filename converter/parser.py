"""MD 파서: 마크다운 텍스트를 Block 리스트로 변환한다.

parse_md_lines() 함수가 메인 엔트리포인트.
"""
from __future__ import annotations

import re
from typing import Iterable, List

from converter.models import (
    BlockType, Block, TableBlock, SummaryTableBlock,
    ProcessBlock, DiagramBox, DiagramBlock,
)


def parse_md_lines(lines: Iterable[str]) -> List[Block]:
    def _normalize_line(raw: str) -> str:
        # 탭 → 스페이스 치환 후 개행 제거
        return raw.replace("\t", "    ").rstrip("\n")

    def _parse_table_block(idx: int, line_list: List[str]) -> tuple[TableBlock | None, int]:
        """현재 인덱스에서 마크다운 표를 파싱한다. 다음 소비할 인덱스까지 반환."""

        title_match = re.match(r"^<\s*표\s*제목\s*:\s*(.+?)>\s*$", line_list[idx].strip())
        if not title_match:
            return None, idx
        title = title_match.group(1).strip()
        table_lines: List[str] = []
        j = idx + 1
        # 제목 다음의 공백/빈 줄은 건너뛴다.
        while j < len(line_list) and not line_list[j].strip():
            j += 1
        while j < len(line_list):
            ln = line_list[j].rstrip("\n")
            if ln.strip().startswith("|"):
                table_lines.append(ln.strip())
                j += 1
                continue
            # 표 블록이 끝났다고 판단
            break

        if len(table_lines) < 2:
            return None, idx

        def _split_row(row: str) -> List[str]:
            cells = row.strip().strip("|").split("|")
            return [c.strip() for c in cells]

        header_cells = _split_row(table_lines[0])
        align_cells = _split_row(table_lines[1])
        body_rows = [_split_row(r) for r in table_lines[2:]]

        def _parse_align(token: str) -> str:
            token = token.strip()
            if token.startswith(":") and token.endswith(":"):
                return "CENTER"
            if token.endswith(":"):
                return "RIGHT"
            if token.startswith(":"):
                return "LEFT"
            return "LEFT"

        aligns = [_parse_align(a) for a in align_cells]
        tbl = TableBlock(
            type=BlockType.TABLE,
            raw="\n".join([line_list[idx]] + table_lines),
            text=title,
            title=title,
            header=header_cells,
            aligns=aligns,
            rows=body_rows,
        )
        return tbl, j

    def _parse_summary_block(idx: int, line_list: List[str]) -> tuple[SummaryTableBlock | None, int]:
        marker = line_list[idx].strip().replace(" ", "")
        if marker not in ("<요약표시작>", "<요약표시작>"):
            return None, idx
        items: List[Block] = []
        j = idx + 1
        while j < len(line_list):
            ln_original = _normalize_line(line_list[j])
            ln = ln_original.lstrip(" ")
            if ln.replace(" ", "") == "<요약표끝>":
                j += 1
                break
            if not ln:
                j += 1
                continue
            if ln.startswith("◦"):
                text = ln[len("◦") :].strip()
                items.append(Block(BlockType.BODY, ln_original, text))
            elif ln.startswith("-"):
                text = ln[len("-") :].strip()
                items.append(Block(BlockType.DESC2, ln_original, text))
            else:
                # 요약표 내부의 기타 라인은 PLAIN으로 유지
                items.append(Block(BlockType.PLAIN, ln_original, ln))
            j += 1
        summ = SummaryTableBlock(
            type=BlockType.SUMMARY_TABLE,
            raw="\n".join(line_list[idx:j]),
            text="요약표",
            items=items,
        )
        return summ, j

    def _parse_process_block(idx: int, line_list: List[str]) -> tuple:
        """<프로세스: 제목> ~ </프로세스> 블록을 파싱한다."""
        proc_match = re.match(r"^<\s*프로세스\s*:\s*(.+?)>\s*$", line_list[idx].strip())
        if not proc_match:
            return None, idx
        proc_title = proc_match.group(1).strip()
        j = idx + 1
        proc_rows = []  # [(steps_list, is_reversed), ...]
        
        while j < len(line_list):
            ln = line_list[j].strip()
            if ln.replace(" ", "") in ("</프로세스>", "</프로세스>"):
                j += 1
                break
            if not ln or ln == "↓":
                j += 1
                continue
            
            # 방향 결정: ← 가 있으면 역방향
            is_reversed = "←" in ln
            
            # 화살표로 분리
            if is_reversed:
                raw_steps = [s.strip() for s in re.split(r"\s*←\s*", ln) if s.strip()]
            else:
                raw_steps = [s.strip() for s in re.split(r"\s*→\s*", ln) if s.strip()]
            
            steps = []
            for step in raw_steps:
                # "단계명(담당자)" 형식 파싱
                m = re.match(r"^(.+?)\((.+?)\)$", step)
                if m:
                    steps.append((m.group(1).strip(), m.group(2).strip()))
                else:
                    steps.append((step, ""))
            
            if steps:
                proc_rows.append((steps, is_reversed))
            j += 1
        
        if not proc_rows:
            return None, idx
        
        block = ProcessBlock(
            type=BlockType.PROCESS,
            raw="\n".join(line_list[idx:j]),
            text=proc_title,
            proc_title=proc_title,
            proc_rows=proc_rows,
        )
        return block, j

    def _parse_diagram_block(idx: int, line_list: List[str]) -> tuple:
        """<도식도: 제목> ~ </도식도> 블록을 파싱한다."""
        diag_match = re.match(r"^<\s*도식도\s*:\s*(.+?)>\s*$", line_list[idx].strip())
        if not diag_match:
            return None, idx
        diag_title = diag_match.group(1).strip()
        j = idx + 1
        layers = []       # [[DiagramBox, ...], ...]
        connectors = []   # ['↓', '↔', ...]
        current_layer = []

        def _flush_layer():
            nonlocal current_layer
            if current_layer:
                layers.append(current_layer)
                current_layer = []

        while j < len(line_list):
            ln = line_list[j].strip()
            if ln.replace(" ", "") in ("</도식도>", "</도식도>"):
                j += 1
                break
            if not ln:
                # 빈 줄 = 레이어 구분
                _flush_layer()
                j += 1
                continue
            if ln in ("↓", "↔"):
                _flush_layer()
                connectors.append(ln)
                j += 1
                continue

            # [제목 | 내용1 | 내용2] 형식 파싱
            box_match = re.match(r"^\[(.+)\]\s*$", ln)
            if box_match:
                content = box_match.group(1)
                parts = [p.strip() for p in content.split("|")]
                box_title = parts[0]
                box_items = parts[1:] if len(parts) > 1 else []
                current_layer.append(DiagramBox(title=box_title, items=box_items))
            j += 1

        _flush_layer()

        if not layers:
            return None, idx

        block = DiagramBlock(
            type=BlockType.DIAGRAM,
            raw="\n".join(line_list[idx:j]),
            text=diag_title,
            diagram_title=diag_title,
            layers=layers,
            connectors=connectors,
        )
        return block, j

    blocks: List[Block] = []
    line_list = [_normalize_line(ln) for ln in lines]
    i = 0
    while i < len(line_list):
        line = line_list[i]
        stripped = line.lstrip(" ")
        leading_spaces = len(line) - len(stripped)

        # 마크다운 헤더 접두사 (###, ##, #) 제거 — 커스텀 마커가 인식되도록
        stripped = re.sub(r'^#{1,6}\s+', '', stripped)

        # 도식도
        diagram_block, next_idx = _parse_diagram_block(i, line_list)
        if diagram_block is not None:
            blocks.append(diagram_block)
            i = next_idx
            continue

        # 프로세스 흐름도
        process_block, next_idx = _parse_process_block(i, line_list)
        if process_block is not None:
            blocks.append(process_block)
            i = next_idx
            continue

        # 요약표
        summary_block, next_idx = _parse_summary_block(i, line_list)
        if summary_block is not None:
            blocks.append(summary_block)
            i = next_idx
            continue

        # 표
        table_block, next_idx = _parse_table_block(i, line_list)
        if table_block is not None:
            blocks.append(table_block)
            i = next_idx
            continue

        if not stripped:
            blocks.append(Block(BlockType.PLAIN, line, ""))
            i += 1
            continue

        if stripped.startswith("<주제목>"):
            text = stripped[len("<주제목>") :].strip()
            if not text and i + 1 < len(line_list):
                text = line_list[i + 1].strip()
                i += 1
            blocks.append(Block(BlockType.TITLE, line, text))
            i += 1
            continue

        if stripped.startswith("<강조>"):
            text = stripped[len("<강조>") :].strip()
            if not text and i + 1 < len(line_list):
                text = line_list[i + 1].strip()
                i += 1
            blocks.append(Block(BlockType.EMPHASIS, line, text))
            i += 1
            continue

        if stripped.startswith("□"):
            text = stripped[len("□") :].strip()
            blocks.append(Block(BlockType.SUBTITLE, line, text))
            i += 1
            continue

        if stripped.startswith(("◦", "•", "∙", "·")):
            text = stripped[len("◦") :].strip()
            blocks.append(Block(BlockType.BODY, line, text))
            i += 1
            continue

        if stripped.startswith(("-", "–", "—")) and leading_spaces <= 3:
            text = stripped[len(stripped[0]) :].strip()
            blocks.append(Block(BlockType.DESC2, line, text))
            i += 1
            continue

        if stripped.startswith(("*", "●")) and leading_spaces <= 4:
            text = stripped[len(stripped[0]) :].strip()
            blocks.append(Block(BlockType.DESC3, line, text))
            i += 1
            continue

        blocks.append(Block(BlockType.PLAIN, line, stripped))
        i += 1

    return blocks
