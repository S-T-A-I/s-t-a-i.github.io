# Scalable Trustworthy AI (STAI) Website

Source for the STAI research group website at <https://s-t-a-i.github.io/>.

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

## Deployment

A push to `master` triggers `.github/workflows/gh-pages.yml`, which builds the site with Hugo and publishes `public/` to the `gh-pages` branch. Pull requests trigger a build-only check.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the branching and review workflow.

## Contact

`coallaoh@gmail.com`
