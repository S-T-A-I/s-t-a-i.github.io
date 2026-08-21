#!/usr/bin/env python3
"""Rebuild data/communities.json from the personal site's tagged publications.

The publications API (internal.stai-lab.org) carries no community tags, so the
tags come from coallaoh.github.io/data/publications.js, matched on title. The
fine-grained tags are then folded into themes, which is what the chart on the
publications page shows. The theme table lives on the personal site too
(data/communities.js, communityThemes), so both charts cut the work the same
way. A tag missing from it falls into the last theme and is reported, so new
ones do not disappear quietly.

Usage: python3 scripts/sync-communities.py [path-to-coallaoh.github.io]
"""

import json
import re
import sys
import urllib.request
from pathlib import Path

API = "https://internal.stai-lab.org/api/public/publications.json"
DEFAULT_SOURCE = Path(__file__).resolve().parents[2] / "coallaoh.github.io"
OUT = Path(__file__).resolve().parents[1] / "data" / "communities.json"


def js_array(path, marker):
    """Pull the single JSON array out of a `const x = [...]` file."""
    text = path.read_text()
    text = text[text.index(marker):]
    return json.loads(text[text.index("["):text.rindex("]") + 1])


def themes_from(source):
    """The shared theme table, read from the personal site's data file."""
    text = (source / "data" / "communities.js").read_text()
    text = text[text.index("const communityThemes"):]
    return json.loads(text[text.index("["):text.rindex("]") + 1])


def key(title):
    return re.sub(r"[^a-z0-9]", "", title.lower())


def main():
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE
    tagged = js_array(source / "data" / "publications.js", "const publicationsData")
    table = themes_from(source)

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

    mapped = {tag for theme in table for tag in theme["tags"]}
    spare = sorted(used - mapped)

    themes = [{"name": t["name"], "short": t.get("short", t["name"]), "slot": t["slot"],
               "tags": [tag for tag in t["tags"] if tag in used]} for t in table]
    themes[-1]["tags"] = sorted(set(themes[-1]["tags"]) | set(spare))

    OUT.write_text(json.dumps({"themes": themes, "tags": tags},
                              indent=1, ensure_ascii=False) + "\n")

    print(f"{len(pubs)} publications, {untagged} untagged, {len(themes)} themes")
    for title in unmatched:
        print(f"  missing from the personal site: {title}")
    if spare:
        print(f"  not in the theme table, filed last: {', '.join(spare)}")


if __name__ == "__main__":
    main()
