#!/usr/bin/env python3
"""Rebuild data/communities.json from the personal site's tagged publications.

The publications API (internal.stai-lab.org) carries no community tags, so the
tags come from coallaoh.github.io/data/publications.js, matched on title. The
fine-grained tags are then folded into the themes below, which is what the
chart on the publications page shows. A tag missing from THEMES falls into
"Other" and is reported, so new ones do not disappear quietly.

Usage: python3 scripts/sync-communities.py [path-to-coallaoh.github.io]
"""

import json
import re
import sys
import urllib.request
from pathlib import Path

# Theme order is fixed: it sets both the stacking order and the colour slot,
# so adding a paper never repaints the others. "Other" is always last.
THEMES = [
    ("Generalisation and robustness", ["OOD", "CoGe", "TTA", "AAML"]),
    ("Vision and multimodal", ["VLM", "SSeg", "WSOL", "OCL", "DiffM"]),
    ("Privacy and data rights", ["PILM", "TDI", "MIALM", "MU", "SILM"]),
    ("Uncertainty", ["UQCV", "UQLM", "UD", "BDL", "OODD"]),
    ("Language models and agents", ["LLMAG", "RALM", "ReLM", "LRM", "KELM"]),
    ("Evaluation and interpretability", ["ELM", "MLAU", "FAtt"]),
]

API = "https://internal.stai-lab.org/api/public/publications.json"
DEFAULT_SOURCE = Path(__file__).resolve().parents[2] / "coallaoh.github.io"
OUT = Path(__file__).resolve().parents[1] / "data" / "communities.json"


def js_array(path, marker):
    """Pull the single JSON array out of a `const x = [...]` file."""
    text = path.read_text()
    text = text[text.index(marker):]
    return json.loads(text[text.index("["):text.rindex("]") + 1])


def key(title):
    return re.sub(r"[^a-z0-9]", "", title.lower())


def main():
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE
    tagged = js_array(source / "data" / "publications.js", "const publicationsData")

    by_title = {key(p["title"]): p.get("rtai_tags") or [] for p in tagged}

    with urllib.request.urlopen(API) as r:
        pubs = json.load(r)["publications"]

    tags, used, unmatched, untagged = {}, set(), [], 0
    for pub in pubs:
        k = key(pub["title"])
        if k not in by_title:
            unmatched.append(pub["title"])
        if by_title.get(k):
            tags[k] = by_title[k]
            used.update(by_title[k])
        else:
            untagged += 1

    mapped = {tag for _, members in THEMES for tag in members}
    spare = sorted(used - mapped)

    themes = [{"name": name, "slot": i + 1, "tags": [t for t in members if t in used]}
              for i, (name, members) in enumerate(THEMES)]
    themes.append({"name": "Other", "slot": 0, "tags": spare})

    OUT.write_text(json.dumps({"themes": themes, "tags": tags},
                              indent=1, ensure_ascii=False) + "\n")

    print(f"{len(pubs)} publications, {untagged} untagged, {len(themes)} themes")
    for title in unmatched:
        print(f"  missing from the personal site: {title}")
    if spare:
        print(f"  filed under Other: {', '.join(spare)}")


if __name__ == "__main__":
    main()
