+++
abstract = "Humans easily determine which color belongs to which shape in multi-object scenes, an ability known as concept binding. Vision-language embedding models such as CLIP struggle with binding: they recognize individual concepts but fail to represent which concepts form which objects. Although CLIP behaves like a bag-of-concepts model in cross-modal retrieval, object information is recoverable from its image and text embeddings separately. We study this tension through the binding function, which maps concepts to scene embeddings. We find that scene embeddings decompose additively into object representations, explaining why uni-modal probes can recover object information. However, CLIP's binding function is high-complexity, which likely prevents the image and text encoders from learning a shared binding mechanism that generalizes to unseen concept combinations. We then ask whether this limitation is fundamental. We show that it is not. In controlled transformer models trained from scratch, binding generalization emerges with sufficient data coverage. These models learn low-complexity binding functions characterized by multiplicative interactions between concepts, enabling systematic generalization."
date = "2026-05-01T00:00:00+09:00"
image = "arnas2026binding.png"
publication = "International Conference on Machine Learning"
publication_short = "ICML Spotlight"
award = "Spotlight"
title = "How can embedding models bind concepts?"
url_arxiv = "//arxiv.org/abs/2605.31503"
url_pdf = "//arxiv.org/pdf/2605.31503"

[[authors]]
    name = "Arnas Uselis"
    is_member = true
    id = "arnas"
    star = true
[[authors]]
    name = "Darina Koishigarina"
    is_member = true
    id = "darina"
    star = true
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++
