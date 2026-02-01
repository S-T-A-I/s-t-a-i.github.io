+++
abstract = "Training data attribution (TDA) techniques find influential training data for the model's prediction on the test data of interest. They approximate the impact of down- or up-weighting a particular training sample. While conceptually useful, they are hardly applicable in practice, particularly because of their sensitivity to different model initialisation. In this paper, we introduce a Bayesian perspective on the TDA task, where the learned model is treated as a Bayesian posterior and the TDA estimates as random variables. From this novel viewpoint, we observe that the influence of an individual training sample is often overshadowed by the noise stemming from model initialisation and SGD batch composition. Based on this observation, we argue that TDA can only be reliably used for explaining model predictions that are consistently influenced by certain training data, independent of other noise factors. Our experiments demonstrate the rarity of such noise-independent training-test data pairs but confirm their existence. We recommend that future researchers and practitioners trust TDA estimates only in such cases. Further, we find a disagreement between ground truth and estimated TDA distributions and encourage future work to study this gap."
date = "2023-12-01T00:00:00+00:00"
image = "elisa2023neurips.png"
publication = "Conference on Neural Information Processing Systems"
publication_short = "NeurIPS"
title = "A Bayesian Perspective On Training Data Attribution"
url_code = "https://github.com/elisanguyen/bayesian-tda"
url_arxiv = "//arxiv.org/abs/2305.19765"
url_pdf = "//arxiv.org/pdf/2305.19765"
url_rtai = "//researchtrend.ai/papers/2305.19765"


[[authors]]
    name = "Elisa Nguyen"
    is_member = true
    id = "elisa"
[[authors]]
    name = "Minjoon Seo"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++
