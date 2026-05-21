# Contributing

Thank you for helping maintain the STAI website. This document covers the workflow for group members and collaborators.

## Workflow

1. Create a branch from `master` for your change. Use a short descriptive name (e.g. `add-member-jane`, `update-tml-schedule`).
2. Make your edits and preview locally with `hugo server -D`.
3. Open a pull request against `master`. Fill in the PR template.
4. A reviewer checks the rendered diff and merges. Direct pushes to `master` are discouraged.

## Commit messages

- Use the imperative mood ("Add", "Update", "Fix").
- Keep the subject line under 70 characters.
- Add a short body when the change is non-trivial.

## Editing content

- Page content lives in `content/`. Each section has an archetype in `archetypes/` you can use via `hugo new`.
- Do not edit files in `public/`. It is the generated output and is regenerated on every deploy.
- Static assets (images, PDFs, slides) go in `static/`. Reference them with absolute paths (e.g. `/img/foo.png`).

## Style guide

- British English.
- Short sentences. Avoid filler.
- Use plain dashes (`-`), not em-dashes (`---`) or en-dashes (`--`).
- Limit colons.
- No excessive capitalisation.
- For Korean text, do not start paragraphs with `[제목]` headers.

## Adding a member

```sh
hugo new member/firstname-lastname.md
```

Edit the front matter (role, photo, links) and the body. Place the profile photo in `static/img/members/`.

## Adding a publication

```sh
hugo new publication/year-shortname.md
```

Fill in title, authors, venue, year, links (paper, code, project). Use existing entries as a reference.

## Reviewing a pull request

- Check that the build passes (GitHub Actions runs on every PR).
- Check the rendered output where relevant: spelling, links, images.
- Confirm that no private or unrelated files were committed.

## Reporting issues

Open a GitHub issue with a clear description and a link to the affected page. For urgent problems (site down, broken deploy), contact `coallaoh@gmail.com`.
