# Scalable Trustworthy AI (STAI) Website

Source for the STAI research group website at <https://stai-lab.org/>.

Built with [Hugo](https://gohugo.io/) and deployed via GitHub Pages on every push to `master`.

## Local development

Install Hugo (extended version recommended):

```sh
brew install hugo
```

Serve locally with live reload:

```sh
hugo server -D
```

The site is then available at <http://localhost:1313/>.

## Repository layout

| Path | Purpose |
|---|---|
| `config.toml` | Site configuration: title, menus, parameters. |
| `content/` | Page content (Markdown + front matter). |
| `content/member/` | Group members. |
| `content/publication/` | Publications. |
| `content/courses/` | Course pages. |
| `content/opening/` | Open positions. |
| `content/overview/` | Group overview sections. |
| `content/post/` | Blog posts. |
| `layouts/` | HTML templates (custom; no external theme). |
| `archetypes/` | Templates for new content via `hugo new`. |
| `static/` | Static assets served as-is (images, PDFs, files). |
| `data/` | Build-time data. `communities.json` holds the research themes behind the chart on the publications page. |
| `scripts/` | Maintenance scripts. `sync-communities.py` rebuilds `data/communities.json`. |
| `.github/workflows/` | GitHub Actions deploy pipeline. |

Set `params.members_api_url` in `config.toml` to the public
`stai-lab-assets` members endpoint to render the members tab from the central DB.

## Research themes

The chart on the publications page groups papers into research themes. The
publications API carries no tags, so the fine-grained ones come from the
personal site, matched on title, and folded into themes by the shared table
there (`data/communities.js`, `communityThemes`) - the same cut the chart on
the personal site uses:

```sh
python3 scripts/sync-communities.py [path-to-coallaoh.github.io]
```

Run it after new papers land, otherwise they count as "Untagged". The script
reports any tag missing from the table. To change the themes, edit the table on
the personal site and run this again; the colour slots follow the order
declared there, and the last theme is the catch-all.

## Adding content

Use `hugo new` with the relevant archetype:

```sh
hugo new member/firstname-lastname.md
hugo new publication/year-shortname.md
hugo new courses/course-slug.md
hugo new opening/role-slug.md
hugo new post/yyyy-mm-dd-slug.md
```

Each archetype seeds the required front matter.

## Landing page recruitment content

The landing page leads with publications, student research, mentorship and alumni careers. The Apply buttons share `params.application_url` in `config.toml`.

Conference counts and Oral/Spotlight highlights use the central publications API and the same venue rules as the publication listing. `data/student_publications.json` selects student examples by publication slug; titles and venues come from the API.

`data/research_focus.json` defines the four research directions, example questions for applicants and related publication slugs. The focus section follows the publication record; linked paper titles come from the public API. Keep proposed research questions distinct from claims about completed work.

`data/alumni_outcomes.json` holds curated current roles, profile links, continuing collaborations and source URLs. The Members page matches careers by member handle; entries with `featured: true` also supply the landing page collaboration stories. Show only the main current position; omit secondary employment, internships alongside a main role, and project affiliations. Omit unverified job titles and leave an alumnus without a career entry when their current destination cannot be confirmed. Verify roles against the alumni's own profiles and update `verified_on` when editing a card. A former role at STAI must not be presented as a current position. Linked collaborations should postdate their graduation or departure. Paper titles and venues come from the API when available; the sourced external paper link remains usable if a paper is not in the feed. Add testimonials only when an attributable, approved quote is available.

## Publication order and venue labels

Papers are grouped by venue within each year. Main-conference tracks share one group; workshops stay separate. Add a newly accepted conference to the front of its year's list in `data/publication_order.json`. The other groups retain their feed order within the venue categories.

Venue labels use the strongest confirmed record: conference, journal, workshop, arXiv, then other. An arXiv link supplies the fallback when acceptance is not known. Submission and under-review labels do not count as acceptances. Only Oral and Spotlight receive emphasis; Poster is omitted.

The listing reads the central public API at build time. Update that database when a paper is accepted, then rebuild the site. `layouts/partials/data/publication-venue.html` selects labels and `publication-order.html` keeps each venue group together.

## Deployment

A push to `master` triggers `.github/workflows/gh-pages.yml`, which builds the site with Hugo and publishes `public/` to the `gh-pages` branch. Pull requests trigger a build-only check.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the branching and review workflow.

## Contact

`coallaoh@gmail.com`
