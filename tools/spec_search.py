#!/usr/bin/env python
"""
Keyword search over HWPX spec chunks with BM25, synonyms, and optional
sentence-level compaction.

Data sources:
- docs/hwpx_spec.md
- docs/hwpx_spec.index.json (section boundaries)
- docs/hwpx_terms.alias.json (term ↔ anchor synonyms)
- tools/chunks/sections.jsonl (built by chunk_builder.py)

Usage:
  python tools/spec_search.py "줄간격 line-spacing" [-k 5] [--json] [--auto-k]
  python tools/spec_search.py "paraPr 문단 모양" --compact 2 -k 5 --json
  python tools/spec_search.py "lineSpacing" --rerank-top 12 --compact 1 --auto-k

If chunks are missing, suggests running chunk builder.
"""
from __future__ import annotations
import argparse, json, os, re, sys
from pathlib import Path
from typing import List, Dict, Any, Tuple, Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TOOLS = ROOT / "tools"
CHUNKS = TOOLS / "chunks" / "sections.jsonl"
ALIASES = DOCS / "hwpx_terms.alias.json"


def load_chunks(path: Path) -> List[Dict[str, Any]]:
    chunks: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            chunks.append(json.loads(line))
    return chunks


def load_aliases(path: Path) -> Dict[str, List[str]]:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    anchor_to_terms: Dict[str, List[str]] = {}
    for ent in data.get("aliases", []):
        terms = ent.get("terms", [])
        anchor = ent.get("anchor")
        if not anchor:
            continue
        anchor_to_terms.setdefault(anchor, [])
        for t in terms:
            k = str(t).strip()
            if not k:
                continue
            anchor_to_terms[anchor].append(k)
    return anchor_to_terms


def _norm(s: str) -> str:
    return re.sub(r"[\s\-_/]", "", s).lower()


def _camel_variants(s: str) -> List[str]:
    # lineSpacing -> [line spacing, line-spacing, linespacing]
    parts = re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])|\d+", s)
    if not parts:
        return []
    base = " ".join(parts)
    return [base, base.replace(" ", "-"), base.replace(" ", "")] 


def expand_query_terms(q: str, alias: Dict[str, List[str]]) -> List[str]:
    base_terms = [t for t in re.split(r"\s+", q.strip()) if t]
    terms: list[str] = []
    seen = set()

    def add_term(t: str):
        key = _norm(t)
        if key and key not in seen:
            seen.add(key)
            terms.append(t)

    # Add base terms and their simple variants
    for bt in base_terms:
        add_term(bt)
        for v in (_camel_variants(bt) or []):
            add_term(v)
        # space/hyphen stripped
        add_term(bt.replace(" ", ""))
        add_term(bt.replace("-", ""))

    # If base term matches any alias group (normalized), include all synonyms + their variants
    for grp in alias.values():
        grp_norm = [_norm(g) for g in grp]
        if any(_norm(bt) in grp_norm for bt in base_terms):
            for t in grp:
                add_term(t)
                for v in (_camel_variants(t) or []):
                    add_term(v)
                add_term(t.replace(" ", ""))
                add_term(t.replace("-", ""))
    return terms


def tokenize(s: str) -> List[str]:
    # keep KR/EN/NUM; split on non-word excluding Korean syllables
    return [t for t in re.findall(r"[A-Za-z0-9_]+|[가-힣]+", s) if t]


def build_bm25(chunks: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, int], float]:
    docs: List[Dict[str, Any]] = []
    df: Dict[str, int] = {}
    total_len = 0
    for c in chunks:
        text = c.get("text") or ""
        toks = tokenize(text)
        tf: Dict[str, int] = {}
        for w in toks:
            tf[w] = tf.get(w, 0) + 1
        for w in tf.keys():
            df[w] = df.get(w, 0) + 1
        doc = {
            "chunk": c,
            "tf": tf,
            "len": len(toks),
            "title_tokens": tokenize((c.get("title") or "") + " " + (c.get("number") or "")),
        }
        total_len += doc["len"]
        docs.append(doc)
    avgdl = total_len / max(1, len(docs))
    return docs, df, avgdl


def bm25_score_doc(doc: Dict[str, Any], query_toks: List[str], df: Dict[str, int], N: int, avgdl: float,
                   k1: float = 1.2, b: float = 0.75) -> float:
    score = 0.0
    dl = max(1, doc["len"])
    tf = doc["tf"]
    for q in query_toks:
        n = df.get(q, 0)
        if n == 0:
            continue
        idf = max(0.0, ( (N - n + 0.5) / (n + 0.5) ))
        # use log(1 + idf) to smooth
        import math
        idf = math.log(1.0 + idf)
        f = tf.get(q, 0)
        if f == 0:
            continue
        denom = f + k1 * (1 - b + b * (dl / avgdl))
        score += idf * (f * (k1 + 1)) / denom
    return score


def exact_boosts(chunk: Dict[str, Any], query_terms: List[str], alias: Dict[str, List[str]]) -> float:
    title = (chunk.get("title") or "") + " " + (chunk.get("number") or "")
    anchor = chunk.get("anchor") or ""
    s = 0.0
    # Title/number exact string matches
    for t in query_terms:
        if not t:
            continue
        # strong boost for exact case-insensitive title substring
        if re.search(re.escape(t), title, flags=re.IGNORECASE):
            s += 0.5
    # Anchor boost via synonyms: if any query term maps to this anchor
    qnorm = {_norm(t) for t in query_terms}
    for a, terms in alias.items():
        if any(_norm(t) in qnorm for t in terms):
            if a == anchor:
                s += 2.0
            # If the title contains a group term, give strong group-title boost
            for gt in terms:
                if re.search(re.escape(gt), title, flags=re.IGNORECASE):
                    s += 5.0
                    break
    # Raw text phrase boost for camel/hyphen terms
    text = chunk.get("text") or ""
    for t in query_terms:
        if not t:
            continue
        if re.search(r"[A-Z]", t) or "-" in t:
            if re.search(re.escape(t), text, flags=re.IGNORECASE):
                s += 2.0
    return s


def score_chunk_bm25(doc: Dict[str, Any], query_terms: List[str], df: Dict[str, int], N: int, avgdl: float,
                      alias: Dict[str, List[str]]) -> float:
    # tokenize query and compute BM25 on text tokens only
    q_toks: List[str] = []
    seen = set()
    for t in query_terms:
        for tok in tokenize(t):
            k = tok.lower()
            if k not in seen:
                seen.add(k)
                q_toks.append(tok)
    bm = bm25_score_doc(doc, q_toks, df, N, avgdl)
    # Light title weighting: if title contains query tokens
    title = " ".join(doc.get("title_tokens", []))
    tboost = 0.0
    for t in q_toks:
        if re.search(re.escape(t), title, flags=re.IGNORECASE):
            tboost += 0.4
    # Anchor/synonyms boost
    ab = exact_boosts(doc["chunk"], query_terms, alias)
    return bm + tboost + ab


def compact_text(text: str, terms: List[str], window: int = 1, max_spans: int = 4) -> str:
    lines = text.splitlines()
    hits: List[int] = []
    for i, ln in enumerate(lines):
        for t in terms:
            if t and re.search(re.escape(t), ln, flags=re.IGNORECASE):
                hits.append(i)
                break
    if not hits:
        return text
    spans: List[Tuple[int, int]] = []
    for h in hits:
        s = max(0, h - window)
        e = min(len(lines) - 1, h + window)
        spans.append((s, e))
    # merge overlapping spans
    spans.sort()
    merged: List[Tuple[int, int]] = []
    for s, e in spans:
        if not merged or s > merged[-1][1] + 1:
            merged.append((s, e))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
    # limit number of spans
    merged = merged[:max_spans]
    parts = []
    for s, e in merged:
        parts.append("\n".join(lines[s : e + 1]))
    return "\n…\n".join(parts)


def highlight(snippet: str, terms: List[str], width: int = 160) -> str:
    # Very light highlighter: wrap first few matches with « »
    for t in terms[:3]:
        if not t:
            continue
        snippet = re.sub(re.escape(t), f"«{t}»", snippet, flags=re.IGNORECASE)
    # Trim to reasonable width
    snippet = snippet.replace("\n", " ⏎ ")
    return (snippet[: width] + ("…" if len(snippet) > width else ""))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", help="검색 키워드 (공백 구분, KR/EN 모두 가능)")
    ap.add_argument("-k", type=int, default=5, help="Top-K 결과 수")
    ap.add_argument("--json", action="store_true", help="JSON 출력")
    ap.add_argument("--auto-k", dest="auto_k", action="store_true", help="스코어 격차에 따라 K 자동 축소")
    ap.add_argument("--compact", type=int, default=0, help="문장/라인 윈도우 압축 크기 (0=비활성)")
    ap.add_argument("--rerank-top", type=int, default=0, help="상위 N 섹션을 문장 TF-IDF 유사도로 재정렬 (0=비활성)")
    args = ap.parse_args()

    if not CHUNKS.exists():
        print("[hint] chunks 파일이 없습니다. 먼저 빌드하세요:", file=sys.stderr)
        print("       python tools/chunk_builder.py", file=sys.stderr)
        return 2

    chunks = load_chunks(CHUNKS)
    aliases = load_aliases(ALIASES)
    terms = expand_query_terms(args.query, aliases)

    # Build BM25 index in-memory
    docs, df, avgdl = build_bm25(chunks)
    N = len(docs)
    scored: List[Tuple[float, Dict[str, Any]]] = []
    for d in docs:
        s = score_chunk_bm25(d, terms, df, N, avgdl, aliases)
        if s > 0:
            scored.append((s, d["chunk"]))
    scored.sort(key=lambda x: x[0], reverse=True)

    # Deduplicate by anchor
    seen_anchors = set()
    uniq: List[Tuple[float, Dict[str, Any]]] = []
    for s, c in scored:
        a = c.get("anchor")
        if a and a in seen_anchors:
            continue
        seen_anchors.add(a)
        uniq.append((s, c))

    # Optional sentence-level TF-IDF re-ranking
    if args.rerank_top and len(uniq) > 1:
        # Consider top M for re-ranking
        M = min(args.rerank_top, len(uniq))
        cands = uniq[:M]
        # Build sentence corpus
        sent_docs: list[str] = []
        offsets: list[tuple[int, int]] = []  # (doc_index, sentence_index_start)
        term_set = set()
        for idx, (_s, c) in enumerate(cands):
            text = c.get("text") or ""
            sents = text.splitlines()
            offsets.append((idx, len(sent_docs)))
            for ln in sents:
                sent_docs.append(ln)
                for tok in tokenize(ln):
                    term_set.add(tok.lower())
        # Build DF for sentences
        df_sent: Dict[str, int] = {}
        for ln in sent_docs:
            seen = set()
            for tok in tokenize(ln):
                k = tok.lower()
                if k not in seen:
                    df_sent[k] = df_sent.get(k, 0) + 1
                    seen.add(k)
        import math
        Nsent = max(1, len(sent_docs))
        # Query vector (tf-idf)
        qtf: Dict[str, int] = {}
        for t in terms:
            for tok in tokenize(t):
                k = tok.lower()
                qtf[k] = qtf.get(k, 0) + 1
        def tfidf_vec_tf(tf: Dict[str, int]) -> Dict[str, float]:
            vec: Dict[str, float] = {}
            for w, f in tf.items():
                n = df_sent.get(w, 0)
                if n == 0:
                    continue
                idf = math.log(1.0 + (Nsent - n + 0.5) / (n + 0.5))
                vec[w] = (1.0 + math.log(1.0 + f)) * idf
            return vec
        def cosine(a: Dict[str, float], b: Dict[str, float]) -> float:
            import math
            num = 0.0
            for w, av in a.items():
                bv = b.get(w)
                if bv is not None:
                    num += av * bv
            da = math.sqrt(sum(v*v for v in a.values())) or 1.0
            db = math.sqrt(sum(v*v for v in b.values())) or 1.0
            return num / (da * db)
        qvec = tfidf_vec_tf(qtf)
        # For each candidate doc, compute max sentence cosine
        reranked: List[Tuple[float, Dict[str, Any]]] = []
        for idx, (orig_score, c) in enumerate(cands):
            text = c.get("text") or ""
            sents = text.splitlines()
            maxcos = 0.0
            for ln in sents:
                tf: Dict[str, int] = {}
                for tok in tokenize(ln):
                    k = tok.lower()
                    tf[k] = tf.get(k, 0) + 1
                svec = tfidf_vec_tf(tf)
                maxcos = max(maxcos, cosine(qvec, svec))
            # Combine
            combined = orig_score + 3.0 * maxcos
            reranked.append((combined, c))
        # Replace the top-M part, keep the rest
        reranked.sort(key=lambda x: x[0], reverse=True)
        uniq = reranked + uniq[M:]

    # Auto-K reduction based on score gaps
    K = args.k
    if args.auto_k and len(uniq) >= 2:
        top1, top2 = uniq[0][0], uniq[1][0]
        if top1 > 3.0 * (top2 + 1e-6) and top1 > 1.0:
            K = min(K, 2)
    top = uniq[:K]

    if args.json:
        out = []
        for s, c in top:
            text = c.get("text") or ""
            if args.compact > 0:
                compact = compact_text(text, terms, window=args.compact)
            else:
                compact = text[:800]
            out.append({
                "score": round(s, 4),
                "anchor": c.get("anchor"),
                "number": c.get("number"),
                "title": c.get("title"),
                "source_file": c.get("source_file"),
                "start_line": c.get("start_line"),
                "end_line": c.get("end_line"),
                "compact_text": compact,
            })
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0

    # Human-readable
    if not top:
        print("검색 결과가 없습니다.")
        return 0

    for i, (s, c) in enumerate(top, start=1):
        title = c.get("title") or ""
        number = c.get("number") or ""
        anchor = c.get("anchor") or ""
        src = c.get("source_file") or ""
        sline, eline = c.get("start_line"), c.get("end_line")
        print(f"[{i}] {number} {title}  ({src}:{sline}-{eline})  #{anchor}  score={s:.3f}")
        text = c.get("text") or ""
        if args.compact > 0:
            comp = compact_text(text, terms, window=args.compact)
            print("    " + highlight(comp, terms))
        else:
            print("    " + highlight(text, terms))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
