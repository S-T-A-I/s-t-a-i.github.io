+++
abstract = "Spurious correlations in the data, where multiple cues are predictive of the target labels, often lead to a phenomenon known as shortcut learning, where a model relies on erroneous, easy-to-learn cues while ignoring reliable ones. In this work, we propose DiffDiv an ensemble diversification framework exploiting Diffusion Probabilistic Models (DPMs) to mitigate this form of bias. We show that at particular training intervals, DPMs can generate images with novel feature combinations, even when trained on samples displaying correlated input features. We leverage this crucial property to generate synthetic counterfactuals to increase model diversity via ensemble disagreement. We show that DPM-guided diversification is sufficient to remove dependence on shortcut cues, without a need for additional supervised signals. We further empirically quantify its efficacy on several diversification objectives, and finally show improved generalization and diversification on par with prior work that relies on auxiliary data collection."
date = "2025-04-01T00:00:00+00:00"
image = "luca2025diffdiv.png"
publication = "ICLR Workshop on Spurious Correlation and Shortcut Learning: Foundations and Solutions"
publication_short = "SCSL @ ICLR"
title = "Mitigating Shortcut Learning with Diffusion Counterfactuals and Diverse Ensembles"
url_arxiv = "//arxiv.org/abs/2311.16176"
url_pdf = "//arxiv.org/pdf/2311.16176"
url_rtai = "//researchtrend.ai/papers/2311.16176"


[[authors]]
    name = "Luca Scimeca"
    is_member = false
[[authors]]
    name = "Alexander Rubinstein"
    is_member = true
    id = "alex"
[[authors]]
    name = "Damien Teney"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
[[authors]]
    name = "Yoshua Bengio"
    is_member = false
+++
