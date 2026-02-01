+++
abstract = "Several studies have empirically compared in-distribution (ID) and out-of-distribution (OOD) performance of various models. They report frequent positive correlations on benchmarks in computer vision and NLP. Surprisingly, they never observe inverse correlations suggesting necessary trade-offs. This matters to determine whether ID performance can serve as a proxy for OOD generalization. This short paper shows that inverse correlations between ID and OOD performance do happen in real-world benchmarks. They may have been missed in past studies because of a biased selection of models. We show an example of the pattern on the WILDS-Camelyon17 dataset, using models from multiple training epochs and random seeds. Our observations are particularly striking on models trained with a regularizer that diversifies the solutions to the ERM objective. We nuance recommendations and conclusions made in past studies. (1) High OOD performance does sometimes require trading off ID performance. (2) Focusing on ID performance alone may not lead to optimal OOD performance: it can lead to diminishing and eventually negative returns in OOD performance. (3) Our example reminds that empirical studies only chart regimes achievable with existing methods: care is warranted in deriving prescriptive recommendations."
date = "2023-12-01T00:00:00+00:00"
publication_date= "2023-12-01T00:00:00+00:00"
image = "teney2023neurips.png"
publication = "Conference on Neural Information Processing Systems"
publication_short = "NeurIPS"
title = "ID and OOD Performance Are Sometimes Inversely Correlated on Real-world Datasets"
url_arxiv = "//arxiv.org/abs/2209.00613"
url_pdf = "//arxiv.org/pdf/2209.00613"
url_rtai = "//researchtrend.ai/papers/2209.00613"

[[authors]]
    name = "Damien Teney"
    is_member = false
[[authors]]
    name = "Lin Yong"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
[[authors]]
    name = "Ehsan Abbasnejad"
    is_member = false
+++
