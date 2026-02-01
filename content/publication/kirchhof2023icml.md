+++
abstract = "Contrastively trained encoders have recently been proven to invert the data-generating process: they encode each input, e.g., an image, into the true latent vector that generated the image (Zimmermann et al., 2021). However, real-world observations often have inherent ambiguities. For instance, images may be blurred or only show a 2D view of a 3D object, so multiple latents could have generated them. This makes the true posterior for the latent vector probabilistic with heteroscedastic uncertainty. In this setup, we extend the common InfoNCE objective and encoders to predict latent distributions instead of points. We prove that these distributions recover the correct posteriors of the data-generating process, including its level of aleatoric uncertainty, up to a rotation of the latent space. In addition to providing calibrated uncertainty estimates, these posteriors allow the computation of credible intervals in image retrieval. They comprise images with the same latent as a given query, subject to its uncertainty."
date = "2023-07-24T00:00:00+00:00"
image = "kirchhof2023icml.png"
publication = "International Conference on Machine Learning"
publication_short = "ICML"
title = "Probabilistic Contrastive Learning Recovers the Correct Aleatoric Uncertainty of Ambiguous Inputs"
url_code = "https://github.com/mkirchhof/Probabilistic_Contrastive_Learning"
url_arxiv = "//arxiv.org/abs/2302.02865"
url_pdf = "//arxiv.org/pdf/2302.02865"
url_rtai = "//researchtrend.ai/papers/2302.02865"

[[authors]]
    name = "Michael Kirchhof"
    is_member = true
    id = "michael"
[[authors]]
    name = "Enkelejda Kasneci"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++
