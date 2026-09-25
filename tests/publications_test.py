"""Exercise the actual Hugo publication templates with controlled feed records."""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def paper(slug, short=None, full=None, workshop=None, award=None, arxiv=False):
    return dict(slug=slug, title=slug, year="2026", publicationShort=short,
                publication=full, workshop=workshop, award=award, authors=[],
                links=[dict(name="arXiv", url="https://arxiv.org/abs/2607.00547")] if arxiv else [])


class PublicationsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = Path(cls.tmp.name)
        (root / "hugo.toml").write_text('baseURL = "https://example.org/"\n')
        (root / "data").mkdir()
        (root / "data/publication_order.json").write_text((ROOT / "data/publication_order.json").read_text())
        records = [
            paper("workshop-first", "SCSL @ ICLR", "ICLR Workshop on Shortcuts"),
            paper("egogap", arxiv=True),
            paper("icml-oral", "ICML Oral", award="Oral"),
            paper("neurips-main", "NeurIPS (Poster)", award="Poster"),
            paper("journal", "arXiv", "Nature Human Behaviour", "ICML Workshop", arxiv=True),
            paper("acl-findings", "ACL Findings"),
            paper("neurips-data", "NeurIPS Evaluations and Datasets Track (Poster)"),
            paper("icml-plain", "ICML"),
            paper("acl-demo", "ACL System Demo"),
            paper("accepted-with-arxiv", "arXiv", "International Conference on Learning Representations", arxiv=True),
            paper("workshop-over-arxiv", "arXiv", workshop="ICML Workshop", arxiv=True),
            paper("full-workshop", "arXiv", "ICLR Workshop on Testing", arxiv=True),
            paper("pending", "ICLR", "Submitted to ICLR", arxiv=True),
            paper("unpublished", "Under review at NeurIPS"),
            paper("spotlight", "NeurIPS D&B (Spotlight)", award="Spotlight"),
            paper("bare-poster", "NeurIPS Poster", award="Poster"),
            paper("best-paper", "ICML", award="Best Paper"),
        ]
        cls.records = records
        (root / "data/fixture.json").write_text(json.dumps(records))
        for rel in ["data/publication-venue.html", "data/publication-order.html", "index/publications.html"]:
            target = root / "layouts/partials" / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(ROOT / "layouts/partials" / rel, target)
        (root / "layouts/partials/data/publications.html").write_text('{{ return site.Data.fixture }}')
        (root / "layouts/partials/index/publication_communities.html").write_text('')
        (root / "layouts/index.html").write_text('''
{{ $papers := partial "data/publication-order.html" (dict "papers" site.Data.fixture "year" "2026") }}
<script id="ordered">{{ $papers | jsonify | safeJS }}</script>
{{ partial "index/publications.html" . }}
''')
        run = subprocess.run([os.environ.get("HUGO_BIN", "hugo"), "--source", str(root)],
                             text=True, capture_output=True)
        if run.returncode:
            raise RuntimeError(run.stdout + run.stderr)
        cls.html = (root / "public/index.html").read_text()
        cls.ordered = json.loads(re.search(r'<script id="ordered">(.*?)</script>', cls.html, re.S)[1])
        cls.by_slug = {p["slug"]: p for p in cls.ordered}

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_new_acceptance_group_is_first_and_tracks_stay_together(self):
        self.assertEqual([p["slug"] for p in self.ordered[:4]],
                         ["neurips-main", "neurips-data", "spotlight", "bare-poster"])
        groups = [p["venueGroup"] for p in self.ordered]
        for group in set(groups):
            indices = [i for i, value in enumerate(groups) if value == group]
            self.assertEqual(indices, list(range(indices[0], indices[-1] + 1)))
        self.assertEqual(len(self.ordered), len(self.records))
        self.assertNotEqual(self.by_slug["workshop-first"]["venueGroup"],
                            self.by_slug["accepted-with-arxiv"]["venueGroup"])

    def test_primary_venue_priority_and_arxiv_fallback(self):
        for slug, expected in {
            "egogap": "arXiv", "journal": "Nature Human Behaviour",
            "accepted-with-arxiv": "International Conference on Learning Representations",
            "workshop-over-arxiv": "ICML Workshop", "full-workshop": "ICLR Workshop on Testing",
            "pending": "arXiv", "unpublished": "",
        }.items():
            self.assertEqual(self.by_slug[slug]["displayVenue"], expected)
        self.assertEqual(self.by_slug["workshop-first"]["venueRank"], 2)

    def test_only_oral_and_spotlight_are_highlighted(self):
        markup = self.html.split('</script>', 1)[1]
        self.assertNotIn('Poster', markup)
        bold = re.findall(r'<b>(.*?)</b>', markup)
        self.assertTrue(bold)
        self.assertTrue(all(value.strip('()') in ['Oral', 'Spotlight'] for value in bold), bold)
        self.assertEqual(sum('Spotlight' in value for value in bold), 1)
        self.assertIn('Best Paper', markup)


if __name__ == "__main__":
    unittest.main()
