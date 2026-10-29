# Publication updates

- Group papers by conference within each year. Main, Findings, demo and dataset tracks of the same conference stay consecutive; workshops remain separate from the main conference.
- Whenever a new conference batch is accepted, move that conference to the front of its year's list in `data/publication_order.json`. This brings the whole accepted batch to the top without splitting its venue group.
- Choose the strongest confirmed venue for each paper: conference > journal > workshop > arXiv > other. A submission or under-review venue is not an acceptance. If there is no confirmed venue but an arXiv link exists, label it `arXiv`.
- When acceptance becomes known, update the central publication database as well as the source entry. The public API, not the Markdown files, supplies the main publication listing.
- Highlight only Oral and Spotlight. Do not show Poster as an award or highlight. Other awards may appear as plain text.
- Thumbnails are a memorable visual token for finding a paper, not a message. Use one simple flat object tied to the paper's theme on an off-white `#F8F9FB` tile, in the palette ink `#111014`, orange `#C2521C`, blue `#2a78d6`, green `#1baf7a` and magenta `#A6249D`, at 800x600. Add the paper's short name as a dark pill label at the bottom left, in its own band below the object. Save as `static/img/<slug>-thumb.png` and set the publication's `image` in STAI Internal to that filename. Check it at card size in both bright and dark mode.
