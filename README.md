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
| `.github/workflows/` | GitHub Actions deploy pipeline. |

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
