+++
abstract = "Supervised learning of image classifiers distills human knowledge into a parametric model through pairs of images and corresponding labels (X,Y). We argue that this simple and widely used representation of human knowledge neglects rich auxiliary information from the annotation procedure, such as the time-series of mouse traces and clicks left after image selection. Our insight is that such annotation byproducts Z provide approximate human attention that weakly guides the model to focus on the foreground cues, reducing spurious correlations and discouraging shortcut learning. To verify this, we create ImageNet-AB and COCO-AB. They are ImageNet and COCO training sets enriched with sample-wise annotation byproducts, collected by replicating the respective original annotation tasks. We refer to the new paradigm of training models with annotation byproducts as learning using annotation byproducts (LUAB). We show that a simple multitask loss for regressing Z together with Y already improves the generalisability and robustness of the learned models. Compared to the original supervised learning, LUAB does not require extra annotation costs. ImageNet-AB and COCO-AB are at https://github.com/naver-ai/NeglectedFreeLunch."
date = "2023-10-01T00:00:00+00:00"
image = "han2023iccv.png"
publication = "International Conference on Computer Vision"
publication_short = "ICCV"
title = "Neglected Free Lunch -- Learning Image Classifiers Using Annotation Byproducts"
url_code = "https://github.com/naver-ai/NeglectedFreeLunch"
url_dataset = "https://huggingface.co/datasets/coallaoh/ImageNet-AB"
url_dataset2 = "https://huggingface.co/datasets/coallaoh/COCO-AB"
url_arxiv = "//arxiv.org/abs/2303.17595"
url_pdf = "//arxiv.org/pdf/2303.17595"
url_poster = "//coallaoh.github.io/data/han2023iccv_poster.pdf"
url_video = "https://www.youtube.com/watch?v=9HEj3Km2TW"
url_rtai = "//researchtrend.ai/papers/2303.17595"


[[authors]]
    name = "Dongyoon Han"
    is_member = false
    star = true
[[authors]]
    name = "Junsuk Choe"
    is_member = false
    star = true
[[authors]]
    name = "Seonghyeok Chun"
    is_member = false
[[authors]]
    name = "John Joon Young Chung"
    is_member = false
[[authors]]
    name = "Minsuk Chang"
    is_member = false
[[authors]]
    name = "Sangdoo Yun"
    is_member = false
[[authors]]
    name = "Jean Y. Song"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++
