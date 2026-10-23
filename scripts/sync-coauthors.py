#!/usr/bin/env python3
"""Rebuild data/coauthors.json, the web pages behind external author names.

The publications page links each author. Members link to their member page
through the handle in the publications API. Everyone else links to the page
recorded for them on the personal site (coallaoh.github.io/data/authors.js),
matched on name or alias with accents and punctuation ignored. The output is keyed by
the exact name the API uses, so the template needs no name matching.

Usage: python3 scripts/sync-coauthors.py [path-to-coallaoh.github.io]
"""

import json
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = Path(__file__).resolve().parents[2] / "coallaoh.github.io"
OUT = ROOT / "data" / "coauthors.json"


def key(name):
    folded = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", folded.lower())


def api_url():
    """The publications feed the site itself builds from (config.toml)."""
    return re.search(r'publications_api_url\s*=\s*"([^"]+)"', (ROOT / "config.toml").read_text())[1]


def authors_from(source):
    text = (source / "data" / "authors.js").read_text()
    text = text[text.index("const authorsData"):]
    return json.loads(text[text.index("{"):text.rindex("};") + 1])["authors"]


def main():
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE
    urls = {key(name): a["url"] for a in authors_from(source) if a.get("url")
            for name in [a["name"], *a.get("aliases", [])]}

    with urllib.request.urlopen(api_url()) as r:
        pubs = json.load(r)["publications"]

    out, missing = {}, set()
    for pub in pubs:
        for author in pub["authors"]:
            if author.get("handle"):
                continue
            url = urls.get(key(author["name"]))
            if url:
                out[author["name"]] = url
            else:
                missing.add(author["name"])

    OUT.write_text(json.dumps(dict(sorted(out.items())), indent=1, ensure_ascii=False) + "\n")

    print(f"{len(out)} external authors linked")
    for name in sorted(missing):
        print(f"  no page on the personal site: {name}")


if __name__ == "__main__":
    main()
