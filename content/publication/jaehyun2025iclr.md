+++
abstract = "Joint finetuning of a pretrained encoder and a randomly initialized decoder has been the de facto standard in semantic segmentation, but the vulnerability of this approach to domain shift has not been studied. We investigate the vulnerability issue of joint finetuning, and propose a novel finetuning framework called Decoupled FineTuning for domain generalization (DeFT) as a solution. DeFT operates in two stages. Its first stage warms up the decoder with the frozen, pretrained encoder so that the decoder learns task-relevant knowledge while the encoder preserves its generalizable features. In the second stage, it decouples finetuning of the encoder and decoder into two pathways, each of which concatenates a usual component (UC) and generalized component (GC); each of the encoder and decoder plays a different role between UC and GC in different pathways. UCs are updated by gradients of the loss on the source domain, while GCs are updated by exponential moving average biased toward their initialization to retain their generalization capability. By the two separate optimization pathways with opposite UC-GC configurations, DeFT reduces the number of learnable parameters virtually, and decreases the distance between learned parameters and their initialization, leading to improved generalization capability. DeFT significantly outperformed existing methods in various domain shift scenarios, and its performance could be further boosted by incorporating a simple distance regularization."
date = "2025-04-02T00:00:00+00:00"
image = "jaehyun2025iclr.png"
publication = "International Conference on Learning Representations"
publication_short = "ICLR"
title = "Decoupled Finetuning for Domain Generalizable Semantic Segmentation"
url_pdf = "//openreview.net/forum?id=qZEdmyqCHF"

[[authors]]
    name = "Jaehyun Pahk"
    is_member = false
[[authors]]
    name = "Donghyeon Kwon"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
[[authors]]
    name = "Suha Kwak"
    is_member = false
+++
