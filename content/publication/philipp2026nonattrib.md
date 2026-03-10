+++
abstract = "Generation novelty is a key indicator of an LLM's ability to generalize, yet measuring it against full pretraining corpora is computationally challenging. Existing evaluations often rely on lexical overlap, failing to detect paraphrased text, or do not consider the full pretraining corpus. We frame novelty as a semantic retrieval problem. This framing enables us to address novelty with modern embedding and indexing pipelines, allowing for efficient analysis at pre-training scale. Specifically, we propose a three-stage framework that retrieves semantically similar samples, reranks them at varying subsequence lengths, and calibrates scores using a human novelty reference for interpretability. We apply this framework to the SmolLM model family and report three key findings: (1) models draw on pre-training data across much longer sequences than previously reported; (2) some task domains systematically promote or suppress generation novelty; and (3) instruction tuning not only alters style but also increases novelty. These results highlight the value of semantic novelty analysis for studying generalization. To support reproducibility and further research, we release ~20 TB of corpus chunks and index artifacts at https://huggingface.co/datasets/stai-tuebingen/faiss-smollm."
date = "2025-10-01T00:00:00+00:00"
image = "philipp2026nonattrib.png"
publication = "arXiv"
publication_short = "arXiv"
title = "LLM generation novelty through the lens of semantic similarity"
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

