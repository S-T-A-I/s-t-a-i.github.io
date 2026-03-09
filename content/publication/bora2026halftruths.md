+++
abstract = "When a text description is extended with an additional detail, image-text similarity should drop if that detail is wrong. We show that CLIP-style dual encoders often violate this intuition: appending a plausible but incorrect object or relation to an otherwise correct description can increase the similarity score. We call such cases half-truths. On COCO, CLIP prefers the correct shorter description only 40.6% of the time, and performance drops to 32.9% when the added detail is a relation. We trace this vulnerability to weak supervision on caption parts: contrastive training aligns full sentences but does not explicitly enforce that individual entities and relations are grounded. We propose CS-CLIP (Component-Supervised CLIP), which decomposes captions into entity and relation units, constructs a minimally edited foil for each unit, and fine-tunes the model to score the correct unit above its foil while preserving standard dual-encoder inference. CS-CLIP raises half-truth accuracy to 69.3% and improves average performance on established compositional benchmarks by 5.7 points, suggesting that reducing half-truth errors aligns with broader gains in compositional understanding. Code is publicly available at: https://github.com/kargibora/CS-CLIP"
date = "2026-02-27T00:01:00+00:00"
publication_date = "2026-02-27T00:00:00+00:00"
image = "bora2026halftruths.png"
publication = "arXiv"
publication_short = "arXiv"
title = "Half-Truths Break Similarity-Based Retrieval"
url_code = "//github.com/kargibora/CS-CLIP"
url_arxiv = "//arxiv.org/abs/2602.23906"
url_pdf = "//arxiv.org/pdf/2602.23906"

[[authors]]
    name = "Bora Kargi"
    is_member = true
    id = "kargi"
[[authors]]
    name = "Arnas Uselis"
    is_member = true
    id = "arnas"
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++
