+++
abstract = "Large-scale pre-trained vision-language models like CLIP demonstrate remarkable zero-shot performance across diverse tasks. However, fine-tuning these models to improve downstream performance often degrades robustness against distribution shifts. Recent approaches have attempted to mitigate this trade-off, but often rely on computationally expensive text-guidance. We propose a novel method for robust fine-tuning, SAE-FT, which operates only on the model's visual representations. SAE-FT regularizes changes to these representations by penalizing the addition and removal of semantically meaningful features identified by a Sparse Autoencoder trained on the pre-trained model. This constraint prevents catastrophic forgetting and makes the fine-tuning process interpretable, enabling direct analysis of semantic changes. SAE-FT is both mechanistically transparent and computationally efficient, matching or exceeding state-of-the-art performance on ImageNet and its associated distribution shift benchmarks. Code is publicly available at: https://github.com/Fabian-Mor/sae-ft"
date = "2026-05-15T00:00:00+00:00"
publication_date = "2026-05-15T00:00:00+00:00"
image = "fabian2026saeft.png"
publication = "arXiv"
publication_short = "arXiv"
title = "Sparse Autoencoders enable Robust and Interpretable Fine-tuning of CLIP models"
url_code = "//github.com/Fabian-Mor/sae-ft"
url_arxiv = "//arxiv.org/abs/2605.15961"
url_pdf = "//arxiv.org/pdf/2605.15961"

[[authors]]
    name = "Fabian Morelli"
    is_member = true
    id = "fabian"
[[authors]]
    name = "Arnas Uselis"
    is_member = true
    id = "arnas"
[[authors]]
    name = "Ankit Sonthalia"
    is_member = true
    id = "ankit"
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++
