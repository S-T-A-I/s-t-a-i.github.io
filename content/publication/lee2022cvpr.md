+++
abstract = "Weakly supervised semantic segmentation (WSSS) methods are often built on pixel-level localization maps obtained from a classifier. However, training on class labels only, classifiers suffer from the spurious correlation between foreground and background cues (e.g. train and rail), fundamentally bounding the performance of WSSS. There have been previous endeavors to address this issue with additional supervision. We propose a novel source of information to distinguish foreground from the background: Out-of-Distribution (OoD) data, or images devoid of foreground object classes. In particular, we utilize the hard OoDs that the classifier is likely to make false-positive predictions. These samples typically carry key visual features on the background (e.g. rail) that the classifiers often confuse as foreground (e.g. train), so these cues let classifiers correctly suppress spurious background cues. Acquiring such hard OoDs does not require an extensive amount of annotation efforts; it only incurs a few additional image-level labeling costs on top of the original efforts to collect class labels. We propose a method, W-OoD, for utilizing the hard OoDs. W-OoD achieves state-of-the-art performance on Pascal VOC 2012."
date = "2022-06-01T00:00:00+00:00"
image = "lee2022cvpr.png"
publication = "Conference on Computer Vision and Pattern Recognition"
publication_short = "CVPR"
title = "Weakly Supervised Semantic Segmentation Using Out-of-Distribution Data"
url_code = "//github.com/naver-ai/w-ood"
url_arxiv = "//arxiv.org/abs/2203.03860"
url_pdf = "//arxiv.org/pdf/2203.03860"
url_rtai = "//researchtrend.ai/papers/2203.03860"

[[authors]]
    name = "Jungbeom Lee"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
[[authors]]
    name = "Sangdoo Yun"
    is_member = false
[[authors]]
    name = "Junsuk Choe"
    is_member = false
[[authors]]
    name = "Eunji Kim"
    is_member = false
[[authors]]
    name = "Sungroh Yoon"
    is_member = false
+++
