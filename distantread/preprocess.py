"""
Preprocess Project Gutenberg texts for distant reading visualization.
- Strips Gutenberg headers/footers
- Tokenizes and lowercases
- Removes stop words and short tokens
- Computes word frequency distributions per text
- Identifies key terms across the corpus
- Extracts concordance (keyword-in-context) for key terms
- Outputs data.json for the web visualization
"""

import json
import re
import os
from collections import Counter

# ── Stop words (common English) ──────────────────────────────────────────────
STOP_WORDS = set("""
a about above after again against all am an and any are aren't as at be
because been before being below between both but by can't cannot could
couldn't did didn't do does doesn't doing don't down during each few for
from further get got had hadn't has hasn't have haven't having he he'd
he'll he's her here here's hers herself him himself his how how's i i'd
i'll i'm i've if in into is isn't it it's its itself let's me more most
mustn't my myself no nor not of off on once only or other ought our ours
ourselves out over own same shan't she she'd she'll she's should
shouldn't so some such than that that's the their theirs them themselves
then there there's these they they'd they'll they're they've this those
through to too under until up upon us very was wasn't we we'd we'll we're
we've were weren't what what's when when's where where's which while who
who's whom why why's will with won't would wouldn't you you'd you'll
you're you've your yours yourself yourselves also one two three four five
six seven eight nine ten may much now well even still just like make made
said could would shall new old first last long great little own other
also back been being come could did each get got has him his how its just
like made make many may might more most much must new now old only other
our out over own said same see she some take tell than that the them then
there these they this time too two upon use very want was way well were
what when which who will with work would year yet you your
been had has have having do does did doing
will would shall should may might can could
give given goes going gone good got great
end however illustration illustrations fig figs figure figures
hundred hundreds thousand thousands million millions
thus therefore hence per cent page pages vol
york chapter part section number numbers note notes
though think thought things thing put came
given certain called every another became
turned gave set let left right found point
enough away along already always almost
later early often large small until since
john known name named says state states full
""".split())

# ── Gutenberg header/footer stripping ────────────────────────────────────────
START_MARKERS = [
    r"\*\*\* ?START OF (?:THE |THIS )?PROJECT GUTENBERG",
    r"\*\*\*START OF (?:THE |THIS )?PROJECT GUTENBERG",
]
END_MARKERS = [
    r"\*\*\* ?END OF (?:THE |THIS )?PROJECT GUTENBERG",
    r"\*\*\*END OF (?:THE |THIS )?PROJECT GUTENBERG",
]

def strip_gutenberg(text):
    """Remove Project Gutenberg header and footer boilerplate."""
    lines = text.split("\n")
    start_idx = 0
    end_idx = len(lines)

    for i, line in enumerate(lines):
        for pat in START_MARKERS:
            if re.search(pat, line, re.IGNORECASE):
                start_idx = i + 1
                break

    for i in range(len(lines) - 1, -1, -1):
        for pat in END_MARKERS:
            if re.search(pat, lines[i], re.IGNORECASE):
                end_idx = i
                break

    return "\n".join(lines[start_idx:end_idx])


def tokenize(text):
    """Lowercase and extract alphabetic tokens of length >= 3."""
    return re.findall(r"[a-z]{3,}", text.lower())


def get_word_freq(tokens):
    """Return frequency counter excluding stop words."""
    return Counter(t for t in tokens if t not in STOP_WORDS)


def concordance(tokens, keyword, window=6):
    """Extract keyword-in-context snippets."""
    results = []
    for i, t in enumerate(tokens):
        if t == keyword:
            left = tokens[max(0, i - window):i]
            right = tokens[i + 1:i + 1 + window]
            results.append({
                "left": " ".join(left),
                "keyword": keyword,
                "right": " ".join(right),
            })
            if len(results) >= 15:  # cap per text
                break
    return results


# ── Metadata for each text ───────────────────────────────────────────────────
TEXT_META = {
    "pg32677.txt": {
        "title": "The Invention of the Sewing Machine",
        "author": "Grace Rogers Cooper",
        "year": "1968",
    },
    "pg33154.txt": {
        "title": "The Telephone",
        "author": "A. E. Dolbear",
        "year": "1877",
    },
    "pg34765.txt": {
        "title": "The Story of the Atlantic Telegraph",
        "author": "Henry M. Field",
        "year": "1866",
    },
    "pg53481.txt": {
        "title": "Printing Telegraphy... A New Era Begins",
        "author": "Edward E. Kleinschmidt",
        "year": "1967",
    },
    "pg672.txt": {
        "title": "The Secret Guide to Computers",
        "author": "Russ Walter",
        "year": "1996",
    },
}


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    files = sorted(f for f in os.listdir(script_dir) if f.endswith(".txt"))

    corpus_tokens_all = []  # all tokens (with stop words) for concordance
    corpus_freq = Counter()
    per_text_freq = {}  # fname -> Counter
    texts_data = []

    for fname in files:
        path = os.path.join(script_dir, fname)
        raw = open(path, encoding="utf-8").read()
        body = strip_gutenberg(raw)
        tokens = tokenize(body)
        freq = get_word_freq(tokens)

        meta = TEXT_META.get(fname, {"title": fname, "author": "Unknown", "year": ""})
        word_count = len(tokens)
        unique_count = len(set(tokens))
        top50 = freq.most_common(50)

        # Skip texts with too little content (broken Gutenberg files)
        if word_count < 100:
            print(f"  Skipping {fname}: only {word_count} words (broken/stub file)")
            continue

        corpus_freq.update(freq)
        per_text_freq[fname] = freq
        corpus_tokens_all.append((fname, tokens))

        texts_data.append({
            "id": fname,
            "title": meta["title"],
            "author": meta["author"],
            "year": meta["year"],
            "wordCount": word_count,
            "uniqueWords": unique_count,
            "top50": [{"word": w, "count": c} for w, c in top50],
        })

    # ── Key terms: content words appearing across multiple texts ──────────
    # Count how many texts each word appears in (using full vocab, not just top50)
    term_text_counts = Counter()
    for fname, freq in per_text_freq.items():
        for w in freq:
            term_text_counts[w] += 1

    # Select key terms: appear in >=3 texts (majority), sorted by corpus freq
    candidate_keys = [
        w for w, tc in term_text_counts.items()
        if tc >= 3 and corpus_freq[w] >= 12
    ]
    key_terms = sorted(candidate_keys, key=lambda w: corpus_freq[w], reverse=True)[:25]

    # ── Build concordance data for key terms ─────────────────────────────
    concordance_data = {}
    for term in key_terms:
        concordance_data[term] = {}
        for fname, tokens in corpus_tokens_all:
            snippets = concordance(tokens, term)
            if snippets:
                concordance_data[term][fname] = snippets

    # ── Per-text frequency for key terms (for comparison chart) ──────────
    key_term_matrix = {}
    for td in texts_data:
        fname = td["id"]
        freq = per_text_freq[fname]
        key_term_matrix[fname] = {
            term: freq.get(term, 0) for term in key_terms
        }

    output = {
        "texts": texts_data,
        "keyTerms": key_terms,
        "keyTermMatrix": key_term_matrix,
        "concordance": concordance_data,
    }

    out_path = os.path.join(script_dir, "data.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"Wrote {out_path}")
    print(f"Texts processed: {len(texts_data)}")
    print(f"Key terms: {key_terms}")


if __name__ == "__main__":
    main()
