+++
abstract = "Image-Text matching (ITM) is a common task for evaluating the quality of Vision and Language (VL) models. However, existing ITM benchmarks have a significant limitation. They have many missing correspondences, originating from the data construction process itself. For example, a caption is only matched with one image although the caption can be matched with other similar images and vice versa. To correct the massive false negatives, we construct the Extended COCO Validation (ECCV) Caption dataset by supplying the missing associations with machine and human annotators. We employ five state-of-the-art ITM models with diverse properties for our annotation process. Our dataset provides x3.6 positive image-to-caption associations and x8.5 caption-to-image associations compared to the original MS-COCO. We also propose to use an informative ranking-based metric mAP@R, rather than the popular Recall@K (R@K). We re-evaluate the existing 25 VL models on existing and proposed benchmarks. Our findings are that the existing benchmarks, such as COCO 1K R@K, COCO 5K R@K, CxC R@1 are highly correlated with each other, while the rankings change when we shift to the ECCV mAP@R. Lastly, we delve into the effect of the bias introduced by the choice of machine annotator."
date = "2022-08-01T00:00:00+00:00"
publication_date= "2022-10-23T00:00:00+00:00"
image = "chun2022eccv.png"
publication = "European Conference on Computer Vision"
publication_short = "ECCV"
title = "ECCV Caption: Correcting False Negatives by Collecting Machine-and-Human-verified Image-Caption Associations for MS-COCO"
url_code = "//github.com/naver-ai/eccv-caption"
url_arxiv = "//arxiv.org/abs/2204.03359"
url_pdf = "//arxiv.org/pdf/2204.03359"
url_rtai = "//researchtrend.ai/papers/2204.03359"

[[authors]]
    name = "Shanghyuk Chun"
    is_member = false
[[authors]]
    name = "Wonjae Kim"
    is_member = false
[[authors]]
    name = "Song Park"
    is_member = false
[[authors]]
    name = "Minsuk Chang"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++
