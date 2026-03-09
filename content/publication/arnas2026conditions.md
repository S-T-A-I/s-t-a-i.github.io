+++
abstract = "Compositional generalization, the ability to recognize familiar parts in novel contexts, is a defining property of intelligent systems. Although modern models are trained on massive datasets, they still cover only a tiny fraction of the combinatorial space of possible inputs, raising the question of what structure representations must have to support generalization to unseen combinations. We formalize three desiderata for compositional generalization under standard training (divisibility, transferability, stability) and show they impose necessary geometric constraints: representations must decompose linearly into per-concept components, and these components must be orthogonal across concepts. This provides theoretical grounding for the Linear Representation Hypothesis: the linear structure widely observed in neural representations is a necessary consequence of compositional generalization. We further derive dimension bounds linking the number of composable concepts to the embedding geometry. Empirically, we evaluate these predictions across modern vision models (CLIP, SigLIP, DINO) and find that representations exhibit partial linear factorization with low-rank, near-orthogonal per-concept factors, and that the degree of this structure correlates with compositional generalization on unseen combinations. As models continue to scale, these conditions predict the representational geometry they may converge to. Code is available at https://github.com/oshapio/necessary-compositionality."
date = "2026-02-27T00:00:00+00:00"
publication_date = "2026-02-27T00:00:00+00:00"
image = "arnas2026conditions.png"
publication = "arXiv"
publication_short = "arXiv"
title = "Compositional Generalization Requires Linear, Orthogonal Representations in Vision Embedding Models"
url_code = "//github.com/oshapio/necessary-compositionality"
url_arxiv = "//arxiv.org/abs/2602.24264"
url_pdf = "//arxiv.org/pdf/2602.24264"

[[authors]]
    name = "Arnas Uselis"
    is_member = true
    id = "arnas"
[[authors]]
    name = "Andrea Dittadi"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++
