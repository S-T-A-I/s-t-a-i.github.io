+++
abstract = "Open-vocabulary segmentation (OVS) has gained attention for its ability to recognize a broader range of classes. However, OVS models show significant performance drops when applied to unseen domains beyond the previous training dataset. Fine-tuning these models on new datasets can improve performance, but often leads to the catastrophic forgetting of previously learned knowledge. To address this issue, we propose a method that allows OVS models to learn information from new domains while preserving prior knowledge. Our approach begins by evaluating the input sample's proximity to multiple domains, using precomputed multivariate normal distributions for each domain. Based on this prediction, we dynamically interpolate between the weights of the pre-trained decoder and the fine-tuned decoders. Extensive experiments demonstrate that this approach allows OVS models to adapt to new domains while maintaining performance on the previous training dataset. The source code is available at this https URL."
date = "2025-09-01T00:00:00+00:00"
publication_date = "2025-12-01T00:00:00+00:00"
image = "dongjun2025ovs.png"
publication = "Conference on Neural Information Processing Systems"
publication_short = "NeurIPS"
title = "Overcoming Domain Limitations in Open-vocabulary Segmentation"
url_arxiv = "//arxiv.org/abs/2410.11536"
url_pdf = "//arxiv.org/pdf/2410.11536"
url_rtai = "//researchtrend.ai/papers/2410.11536"

[[authors]]
    name = "Dongjun Hwang"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
[[authors]]
    name = "Junsuk Choe"
    is_member = false
+++
