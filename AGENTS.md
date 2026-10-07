# Publication updates

- Group papers by conference within each year. Main, Findings, demo and dataset tracks of the same conference stay consecutive; workshops remain separate from the main conference.
- Whenever a new conference batch is accepted, move that conference to the front of its year's list in `data/publication_order.json`. This brings the whole accepted batch to the top without splitting its venue group.
- Choose the strongest confirmed venue for each paper: conference > journal > workshop > arXiv > other. A submission or under-review venue is not an acceptance. If there is no confirmed venue but an arXiv link exists, label it `arXiv`.
- When acceptance becomes known, update the central publication database as well as the source entry. The public API, not the Markdown files, supplies the main publication listing.
- Highlight only Oral and Spotlight. Do not show Poster as an award or highlight. Other awards may appear as plain text.
- Thumbnails should catch attention and give a memorable index for visual search. Avoid text altogether. Prefer distinct objects, silhouettes and colours; use a transparent background wherever possible. Check each thumbnail at card size against both bright and dark backgrounds. Do not force it to explain the paper. A cropped impressive figure, a symbolic object, a random image or an emoji are all valid choices.
