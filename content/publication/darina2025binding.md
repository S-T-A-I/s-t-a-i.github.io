+++
abstract = "CLIP (Contrastive Language-Image Pretraining) has become a popular choice for various downstream tasks. However, recent studies have questioned its ability to represent compositional concepts effectively. These works suggest that CLIP often acts like a bag-of-words (BoW) model, interpreting images and text as sets of individual concepts without grasping the structural relationships. In particular, CLIP struggles to correctly bind attributes to their corresponding objects when multiple objects are present in an image or text. In this work, we investigate why CLIP exhibits this BoW-like behavior. We find that the correct attribute-object binding information is already present in individual text and image modalities. Instead, the issue lies in the cross-modal alignment, which relies on cosine similarity. To address this, we propose Linear Attribute Binding CLIP or LABCLIP. It applies a linear transformation to text embeddings before computing cosine similarity. This approach significantly improves CLIP's ability to bind attributes to correct objects, thereby enhancing its compositional understanding."
date = "2026-01-27T00:00:00+00:00"
publication_date = "2026-04-24T00:00:00+00:00"
image = "darina2025binding.png"
publication = "International Conference on Learning Representations"
publication_short = "ICLR"
title = "CLIP Behaves like a Bag-of-Words Model Cross-modally but not Uni-modally"
url_code = "//github.com/AlexanderRubinstein/OCCAM"
url_arxiv = "//arxiv.org/abs/2502.03566"
url_pdf = "//arxiv.org/pdf/2502.03566"
url_project = "//alexanderrubinstein.github.io/are-we-done-with-ocl/"
url_rtai = "//researchtrend.ai/papers/2502.03566"


[[authors]]
    name = "Darina Koishigarina"
    is_member = true
    id = "darina"
[[authors]]
    name = "Arnas Uselis"
    is_member = true
    id = "arnas"
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++
