+++
abstract = "Training a diverse ensemble of models has several practical applications such as providing candidates for model selection with better out-of-distribution (OOD) generalization, and enabling the detection of OOD samples via Bayesian principles. An existing approach to diverse ensemble training encourages the models to disagree on provided OOD samples. However, the approach is computationally expensive and it requires well-separated ID and OOD examples, such that it has only been demonstrated in small-scale settings. Method: This work presents a Hardness-based Diversification Regularizer (HDR) applicable to large-scale settings (e.g. ImageNet) that does not require OOD samples. Instead, HDR identifies hard training samples on the fly and encourages the ensemble members to disagree on these. To improve scaling, we show how to avoid the expensive computations in existing methods of exhaustive pairwise disagreements across models. Results: We evaluate the benefits of diversification with experiments on ImageNet. First, for OOD generalization, we observe large benefits from the diversification in multiple settings including output-space (classical) ensembles and weight-space ensembles (model soups). Second, for OOD detection, we turn the diversity of ensemble hypotheses into a novel uncertainty score estimator that surpasses a large number of OOD detection baselines."
date = "2024-09-25T00:00:00+00:00"
image = "alex2024diversify.png"
publication = "arXiv"
publication_short = "arXiv"
title = "Scalable Ensemble Diversification for OOD Generalization and Detection"
url_code = "//github.com/AlexanderRubinstein/diverse-universe-public"
url_arxiv = "//arxiv.org/abs/2409.16797"
url_pdf = "//arxiv.org/pdf/2409.16797"
url_rtai = "//researchtrend.ai/papers/2409.16797"


[[authors]]
    name = "Alexander Rubinstein"
    is_member = true
    id = "alex"
[[authors]]
    name = "Luca Scimeca"
    is_member = false
[[authors]]
    name = "Damien Teney"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++
