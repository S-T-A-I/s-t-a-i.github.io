+++
abstract = "Understanding how language-model outputs relate to the pretraining corpus is central to studying model behavior. Most training data attribution (TDA) methods ask which training examples causally influence a given output, often using leave-one-out tests. We invert the question: which outputs cannot be attributed to any pretraining example? We introduce un-attributability as an operational measure of semantic novelty: an output is novel if the pretraining corpus contains no semantically similar context. We approximate this with a simple two-stage retrieval pipeline: index the corpus with lightweight GIST embeddings, retrieve the top-n candidates, then rerank with ColBERTv2. If the nearest corpus item is less attributable than a human-generated text reference, we consider the output of the model as novel. We evaluate on SmolLM and SmolLM2 and report three findings: (1) models draw on pretraining data across much longer spans than previously reported; (2) some domains systematically promote or suppress novelty; and (3) instruction tuning not only alters style but also increases novelty. Reframing novelty assessment around un-attributability enables efficient analysis at pretraining scale."
date = "2025-10-01T00:00:00+00:00"
image = "philipp2026nonattrib.png"
publication = "arXiv"
publication_short = "arXiv"
title = "Un-Attributability: Computing Novelty From Retrieval & Semantic Similarity"
url_dataset = "//huggingface.co/datasets/stai-tuebingen/faiss-smollm"
url_arxiv = "//arxiv.org/abs/2510.27313"
url_pdf = "//arxiv.org/pdf/2510.27313"
url_rtai = "//researchtrend.ai/papers/2510.27313"

[[authors]]
    name = "Philipp Davydov"
    is_member = true
    id = "philipp"
[[authors]]
    name = "Ameya Prabhu"
    is_member = false
[[authors]]
    name = "Matthias Bethge"
    is_member = false
[[authors]]
    name = "Elisa Nguyen"
    is_member = true
    id = "elisa"
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++

