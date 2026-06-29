#!/usr/bin/env python3
"""자간 자동조정 캘리브레이션 — 목표 HWPX의 lineSeg에서 '정답 데이터셋' 추출.

HWPX의 <hp:linesegarray><hp:lineseg textpos= horzsize= .../> 는 한글이 렌더링한
실제 줄 레이아웃 캐시다. 연속 lineseg의 textpos 차이 = 그 줄에 들어간 글자 수.
이를 모아 "글자 구성 + 자간% → 한 줄에 들어가는 폭" 관계를 실측한다.

사용:
    python3 tools/spacing_calibration.py <hwpx_or_extracted_dir>
"""
from __future__ import annotations

import re
import sys
import zipfile
import unicodedata
from pathlib import Path
from collections import Counter

NS = {
    "hp": "http://www.hancom.co.kr/hwpml/2011/paragraph",
    "hh": "http://www.hancom.co.kr/hwpml/2011/head",
}


def _read_contents(target: str) -> tuple[str, str]:
    """hwpx 파일 또는 압축해제 폴더에서 (header.xml, section0.xml) 텍스트 반환."""
    p = Path(target)
    if p.is_dir():
        header = (p / "Contents" / "header.xml").read_text(encoding="utf-8")
        section = (p / "Contents" / "section0.xml").read_text(encoding="utf-8")
        return header, section
    with zipfile.ZipFile(p) as z:
        header = z.read("Contents/header.xml").decode("utf-8")
        section = z.read("Contents/section0.xml").decode("utf-8")
    return header, section


def parse_charpr_spacing(header: str) -> dict[int, dict]:
    """charPr id -> {spacing(한글 자간%), ratio, height, font}"""
    out: dict[int, dict] = {}
    for m in re.finditer(r'<hh:charPr id="(\d+)"[^>]*height="(\d+)"(.*?)</hh:charPr>', header, re.S):
        cid, height, body = int(m.group(1)), int(m.group(2)), m.group(3)
        sp = re.search(r'<hh:spacing[^>]*hangul="(-?\d+)"', body)
        rt = re.search(r'<hh:ratio[^>]*hangul="(\d+)"', body)
        fr = re.search(r'<hh:fontRef[^>]*hangul="(\d+)"', body)
        out[cid] = {
            "spacing": int(sp.group(1)) if sp else 0,
            "ratio": int(rt.group(1)) if rt else 100,
            "height": height,
            "font": int(fr.group(1)) if fr else -1,
        }
    return out


def classify(ch: str) -> str:
    """글자를 폭 추정용 범주로 분류."""
    if ch == " ":
        return "space"
    o = ord(ch)
    # 한글 음절/자모, CJK 한자 = 전각(1.0em)
    if 0xAC00 <= o <= 0xD7A3 or 0x1100 <= o <= 0x11FF or 0x3130 <= o <= 0x318F:
        return "hangul"
    if 0x4E00 <= o <= 0x9FFF or 0x3400 <= o <= 0x4DBF:
        return "hanja"
    # 전각 기호/문장부호
    if unicodedata.east_asian_width(ch) in ("W", "F"):
        return "wide"
    if ch.isdigit():
        return "digit"
    if ch.isascii() and ch.isalpha():
        return "latin"
    return "narrow"  # 기타 ascii 기호 등


def extract_dataset(section: str, charpr: dict[int, dict]):
    """각 문단의 (줄별 글자구성, 자간%, horzsize) 레코드 리스트."""
    records = []
    # 문단 단위로 분리
    for pm in re.finditer(r"<hp:p\b.*?</hp:p>", section, re.S):
        para = pm.group(0)
        segs = re.findall(r'<hp:lineseg\b[^>]*/>', para)
        if len(segs) < 1:
            continue
        # 문단 전체 텍스트 (run 순서대로 hp:t 이어붙임). 자간은 첫 run charPr 기준(근사).
        texts = re.findall(r"<hp:t>(.*?)</hp:t>", para, re.S)
        full = "".join(re.sub(r"<[^>]+>", "", t) for t in texts)
        full = (full.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&"))
        if not full.strip():
            continue
        # 문단 대표 자간 = 가장 긴 텍스트를 가진 run의 charPr (글머리기호 run에 속지 않도록)
        run_lens: Counter = Counter()
        for rm in re.finditer(r'<hp:run\b[^>]*charPrIDRef="(\d+)"[^>]*>(.*?)</hp:run>', para, re.S):
            rcid = int(rm.group(1))
            rtxt = "".join(re.findall(r"<hp:t>(.*?)</hp:t>", rm.group(2), re.S))
            run_lens[rcid] += len(re.sub(r"<[^>]+>", "", rtxt))
        if not run_lens:
            continue
        cid = run_lens.most_common(1)[0][0]
        info = charpr.get(cid, {})
        if info.get("font") != 5:  # 휴먼명조(본문)만 대상
            continue
        # lineseg textpos로 줄별 글자수 산출
        seg_pos = [int(re.search(r'textpos="(\d+)"', s).group(1)) for s in segs]
        seg_hsz = [int(re.search(r'horzsize="(\d+)"', s).group(1)) for s in segs]
        bounds = seg_pos + [len(full)]
        for i in range(len(segs)):
            line = full[bounds[i]:bounds[i + 1]]
            if not line:
                continue
            comp = Counter(classify(c) for c in line)
            records.append({
                "spacing": info.get("spacing", 0),
                "height": info.get("height", 1500),
                "horzsize": seg_hsz[i],
                "nchar": len(line),
                "comp": dict(comp),
                "is_last": i == len(segs) - 1,
                "text": line,
            })
    return records


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    header, section = _read_contents(sys.argv[1])
    charpr = parse_charpr_spacing(header)
    recs = extract_dataset(section, charpr)

    # 마지막 줄(끝까지 안 참)은 폭 측정 노이즈 → '꽉 찬 줄'만 캘리브레이션에 사용
    full_lines = [r for r in recs if not r["is_last"]]
    print(f"본문(휴먼명조) 줄 레코드: {len(recs)}개  (그 중 꽉찬 줄 {len(full_lines)}개)")

    # 자간%별로 '글자당 평균 폭(horzsize/nchar)' 집계 → 단위/계수 실측
    by_sp: dict[int, list[float]] = {}
    for r in full_lines:
        if r["nchar"] >= 10:  # 표본 안정성
            by_sp.setdefault(r["spacing"], []).append(r["horzsize"] / r["nchar"])
    print("\n자간%  표본수  글자당평균폭(HWP)  (height=1500 기준 전각=1500)")
    for sp in sorted(by_sp):
        xs = by_sp[sp]
        print(f"  {sp:>4}   {len(xs):>4}     {sum(xs)/len(xs):8.1f}")

    # 한글 비중 높은 줄만 추려, '순수 한글 글자폭 vs 자간' 관계
    print("\n[한글 90%+ 줄] 자간% → 한글 글자당 폭")
    pure: dict[int, list[float]] = {}
    for r in full_lines:
        h = r["comp"].get("hangul", 0) + r["comp"].get("wide", 0) + r["comp"].get("hanja", 0)
        if r["nchar"] >= 10 and h / r["nchar"] >= 0.9:
            pure.setdefault(r["spacing"], []).append(r["horzsize"] / r["nchar"])
    for sp in sorted(pure):
        xs = pure[sp]
        print(f"  {sp:>4}   n={len(xs):>3}   {sum(xs)/len(xs):8.1f} HWP/글자  "
              f"(글자크기대비 {sum(xs)/len(xs)/1500*100:5.1f}%)")


if __name__ == "__main__":
    main()
