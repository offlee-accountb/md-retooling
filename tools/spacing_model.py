#!/usr/bin/env python3
"""자간 자동조정 — 물리 모델 + 목표 HWPX 역검증.

모델:  줄폭 = Σ base_width[범주] + (자간% / 100) × 글자크기 × (글자수-1)
- 자간 단위는 HWPX 스펙상 % (글자크기 대비).  글자크기(em) = charPr height.
- base_width(한글전각 W / 좁은글자 N / 공백 S)는 '자간 0' 줄들에서 최소제곱 회귀.

검증: 사람이 자간을 음수로 넣은 문단은 "자간 0이었다면 한 줄 더 많았을" 문단이다.
      모델이 그 '자간0 줄 수'를 +1로 예측하면 모델이 사람의 판단을 재현하는 것.

사용:  python3 tools/spacing_model.py <hwpx_or_dir>
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from spacing_calibration import _read_contents, parse_charpr_spacing, classify

EM = 1500          # 본문 15pt
AVAIL = 48188      # 가용폭(HWP) = 페이지폭 - 좌우여백
# 정책: 표준(균형) — 마지막 줄이 가용폭의 절반 미만이면 한 줄로 압축 시도
WIDOW = 0.5        # 마지막 줄 점유율이 이 값 미만이면 압축 대상
FLOOR = -12        # 자간 하한(%) — 가독성


def _solve3(A, b):
    """3변수 정규방정식 (A^T A) x = A^T b 을 가우스 소거로 풀이."""
    # M = A^T A (3x3), v = A^T b (3)
    M = [[sum(A[k][i] * A[k][j] for k in range(len(A))) for j in range(3)] for i in range(3)]
    v = [sum(A[k][i] * b[k] for k in range(len(A))) for i in range(3)]
    # 가우스 소거
    for i in range(3):
        p = M[i][i]
        for j in range(3):
            M[i][j] /= p
        v[i] /= p
        for r in range(3):
            if r != i:
                f = M[r][i]
                for j in range(3):
                    M[r][j] -= f * M[i][j]
                v[r] -= f * v[i]
    return v  # [W, N, S]


def _counts(text):
    """(wide=한글/한자/전각, narrow=영숫자/기호, space) 글자 수."""
    w = n = s = 0
    for ch in text:
        c = classify(ch)
        if c in ("hangul", "hanja", "wide"):
            w += 1
        elif c == "space":
            s += 1
        else:
            n += 1
    return w, n, s


def collect(section, charpr):
    """문단별: (텍스트, 대표자간, 실제줄수, 줄별 꽉찬줄 폭표본)."""
    from collections import Counter
    paras = []
    for pm in re.finditer(r"<hp:p\b.*?</hp:p>", section, re.S):
        para = pm.group(0)
        segs = re.findall(r"<hp:lineseg\b[^>]*/>", para)
        if not segs:
            continue
        run_lens: Counter = Counter()
        full_parts = []
        for rm in re.finditer(r'<hp:run\b[^>]*charPrIDRef="(\d+)"[^>]*>(.*?)</hp:run>', para, re.S):
            rcid = int(rm.group(1))
            txt = "".join(re.findall(r"<hp:t>(.*?)</hp:t>", rm.group(2), re.S))
            txt = re.sub(r"<[^>]+>", "", txt)
            full_parts.append(txt)
            run_lens[rcid] += len(txt)
        if not run_lens:
            continue
        cid = run_lens.most_common(1)[0][0]
        info = charpr.get(cid, {})
        if info.get("font") != 5:
            continue
        full = "".join(full_parts).replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
        if not full.strip():
            continue
        pos = [int(re.search(r'textpos="(\d+)"', x).group(1)) for x in segs]
        hsz = [int(re.search(r'horzsize="(\d+)"', x).group(1)) for x in segs]
        paras.append({
            "text": full, "spacing": info.get("spacing", 0),
            "nlines": len(segs), "pos": pos, "hsz": hsz,
        })
    return paras


def model_width(text, spacing, W, N, S):
    w, n, s = _counts(text)
    base = W * w + N * n + S * s
    return base + (spacing / 100.0) * EM * max(len(text) - 1, 0)


def model_lines(text, spacing, W, N, S):
    """가용폭 대비 글자 누적으로 줄 수 추정 (글자단위 근사)."""
    avail = AVAIL
    lines, cur = 1, 0.0
    for i, ch in enumerate(text):
        c = classify(ch)
        bw = W if c in ("hangul", "hanja", "wide") else (S if c == "space" else N)
        adv = bw + (spacing / 100.0) * EM
        if cur + bw > avail and cur > 0:
            lines += 1
            cur = adv
        else:
            cur += adv
    return lines, cur / avail  # (줄수, 마지막줄 점유율)


def recommend(text, W, N, S):
    """위도 제거를 위한 자간 추천."""
    base_lines, last = model_lines(text, 0, W, N, S)
    if base_lines <= 1 or last >= WIDOW:
        return 0, base_lines  # 조정 불필요
    for sp in range(-1, FLOOR - 1, -1):
        nl, _ = model_lines(text, sp, W, N, S)
        if nl < base_lines:
            return sp, nl
    return 0, base_lines  # 하한 내 해결 불가


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    header, section = _read_contents(sys.argv[1])
    charpr = parse_charpr_spacing(header)
    paras = collect(section, charpr)

    # 1) 자간 0 줄로 base_width 회귀 (꽉 찬 줄만, 마지막 줄 제외)
    A, b = [], []
    for p in paras:
        if p["spacing"] != 0:
            continue
        bounds = p["pos"] + [len(p["text"])]
        for i in range(len(p["pos"]) - 1):  # 마지막 줄 제외
            line = p["text"][bounds[i]:bounds[i + 1]]
            if len(line) < 8:
                continue
            w, n, s = _counts(line)
            A.append([w, n, s]); b.append(p["hsz"][i])
    if len(A) >= 3:
        W, N, S = _solve3(A, b)
    else:
        W, N, S = 1430.0, 760.0, 470.0  # fallback 근사
    print(f"[회귀] 표본 {len(A)}줄 → 글자 기본폭(HWP):  한글/전각 W={W:.0f}  좁은글자 N={N:.0f}  공백 S={S:.0f}")
    print(f"       (em=1500 대비: 한글 {W/EM*100:.0f}%, 좁은글자 {N/EM*100:.0f}%, 공백 {S/EM*100:.0f}%)")

    # 2) 역검증: 사람이 자간 음수를 넣은 문단 → 모델이 '자간0 줄수 = 실제+1'을 예측하는가
    print("\n[역검증] 사람이 자간 조정한 본문 문단")
    print(" 실제자간 실제줄수 │ 모델(자간0)줄수 │ 모델추천자간→줄수 │ 판정 │ 텍스트")
    hit = tot = 0
    for p in sorted(paras, key=lambda x: x["spacing"]):
        if p["spacing"] >= 0:
            continue
        tot += 1
        m0, _ = model_lines(p["text"], 0, W, N, S)
        rec_sp, rec_nl = recommend(p["text"], W, N, S)
        # 기대: 자간0이면 실제보다 줄이 많아야(사람이 줄이려 자간 넣음) 그리고 추천이 실제줄수 도달
        ok = m0 > p["nlines"] and rec_nl <= p["nlines"]
        hit += ok
        print(f"   {p['spacing']:>4}     {p['nlines']}    │      {m0}        │   {rec_sp:>4} → {rec_nl}      │ {'✓' if ok else '·'}   │ {p['text'][:30]}")
    if tot:
        print(f"\n모델이 사람 판단을 재현: {hit}/{tot}")


if __name__ == "__main__":
    main()
