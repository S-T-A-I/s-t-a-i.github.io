+++
abstract = "Text-to-image diffusion models achieve impressive visual fidelity, yet they remain unreliable in multi-object generation. Despite extensive empirical evidence of these failures, the underlying causes remain unclear. We begin by asking how much of this limitation arises from the data itself. To disentangle data effects, we consider two regimes across different dataset sizes: (1) concept generalization, where each individual concept is observed during training under potentially imbalanced data distributions, and (2) compositional generalization, where specific combinations of concepts are systematically held out. To study these regimes, we introduce mosaic (Multi-Object Spatial relations, AttrIbution, Counting), a controlled framework for dataset generation. By training diffusion models on mosaic, we find that scene complexity plays a dominant role rather than concept imbalance, and that counting is uniquely difficult to learn in low-data regimes. Moreover, compositional generalization collapses as more concept combinations are held out during training. These findings highlight fundamental limitations of diffusion models and motivate stronger inductive biases and data design for robust multi-object compositional generation."
date = "2026-05-01T00:00:00+09:00"
image = "yujin2026diffusion.png"
publication = "International Conference on Machine Learning"
publication_short = "ICML"
title = "When Do Diffusion Models learn to Generate Multiple Objects?"
url_arxiv = "//arxiv.org/abs/2605.00273"
url_pdf = "//arxiv.org/pdf/2605.00273"

[[authors]]
    name = "Yujin Jeong"
    is_member = false
[[authors]]
    name = "Arnas Uselis"
    is_member = true
    id = "arnas"
[[authors]]
    name = "Iro Laina"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
[[authors]]
    name = "Anna Rohrbach"
    is_member = false
+++
