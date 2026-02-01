+++
abstract = "Object-centric learning (OCL) seeks to learn representations that only encode an object, isolated from other objects or background cues in a scene. This approach underpins various aims, including out-of-distribution (OOD) generalization, sample-efficient composition, and modeling of structured environments. Most research has focused on developing unsupervised mechanisms that separate objects into discrete slots in the representation space, evaluated using unsupervised object discovery. However, with recent sample-efficient segmentation models, we can separate objects in the pixel space and encode them independently. This achieves remarkable zero-shot performance on OOD object discovery benchmarks, is scalable to foundation models, and can handle a variable number of slots out-of-the-box. Hence, the goal of OCL methods to obtain object-centric representations has been largely achieved. Despite this progress, a key question remains: How does the ability to separate objects within a scene contribute to broader OCL objectives, such as OOD generalization? We address this by investigating the OOD generalization challenge caused by spurious background cues through the lens of OCL. We propose a novel, training-free probe called Object-Centric Classification with Applied Masks (OCCAM), demonstrating that segmentation-based encoding of individual objects significantly outperforms slot-based OCL methods. However, challenges in real-world applications remain. We provide the toolbox for the OCL community to use scalable object-centric representations, and focus on practical applications and fundamental questions, such as understanding object perception in human cognition."
date = "2025-04-01T00:00:00+00:00"
image = "alex2025ocl.png"
publication = "ICLR Workshop on Spurious Correlation and Shortcut Learning: Foundations and Solutions"
publication_short = "SCSL @ ICLR"
title = "Are We Done with Object-Centric Learning?"
url_code = "//github.com/AlexanderRubinstein/OCCAM"
url_arxiv = "//arxiv.org/abs/2504.07092"
url_pdf = "//arxiv.org/pdf/2504.07092"
url_project = "//alexanderrubinstein.github.io/are-we-done-with-ocl/"
url_rtai = "//researchtrend.ai/papers/2504.07092"


[[authors]]
    name = "Alexander Rubinstein"
    is_member = true
    id = "alex"
[[authors]]
    name = "Ameya Prabhu"
    is_member = false
[[authors]]
    name = "Matthias Bethge"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++
