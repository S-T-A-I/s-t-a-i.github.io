+++
title = "Trustworthy Machine Learning"
semester = "Winter Semester 2022-2023"
university = "University of Tübingen"
image = "DALLE_TML.png"
sort_position = 1
description = "As machine learning technology gets applied to actual products and solutions, new challenges have emerged. Models unexpectedly fail to generalise well to small changes in the distribution; some models are found to utilise sensitive features that could treat certain demographic user groups unfairly; models tend to be confident on novel types of data; models cannot communicate the rationale behind their decisions effectively with the end users like medical staff to maximise the human-machine synergies. Collectively, we face a trustworthiness issue with the current machine learning technology. A large fraction of the machine learning research nowadays is dedicated to expanding the frontier of Trustworthy Machine Learning (TML). The course covers a theoretical and technical background for key topics in TML. We conduct a critical review of important classical and contemporary research papers on related topics and provide hands-on practicals to implement TML techniques."
+++

## Overview

### Goal

1. Students will be able to critically read, assess, and discuss research work in Trustworthy Machine Learning (TML).
2. Students will gain the technical background to implement basic TML techniques in a deep learning framework.
3. Students will be ready to conduct their own research in TML and make contributions to the research community.

### Prerequisites

- Familiarity with Python and PyTorch coding.
- A pass grade from the Deep Learning Course (or equivalent).
- Basic knowledge of machine learning concepts.
- Basic maths: multivariate calculus, linear algebra, probability, statistics, and optimisation.

### Reading list

Recommended papers from each topic.

{{< details "OOD Generalisation" >}}
- [Generalizing from a Few Examples: A Survey on Few-Shot Learning](https://arxiv.org/pdf/1904.05046.pdf)
- [Generalizing to Unseen Domains: A Survey on Domain Generalization](https://changliu00.github.io/dg_survey/dg_survey.pdf)
- [In Search of Lost Domain Generalization](https://arxiv.org/pdf/2007.01434.pdf)
- [Underspecification Presents Challenges for Credibility in Modern Machine Learning](https://arxiv.org/pdf/2011.03395.pdf)
- [Shortcut Learning in Deep Neural Networks](https://arxiv.org/pdf/2004.07780.pdf)
- [Which Shortcut Cues Will DNNs Choose? A Study from the Parameter-Space Perspective](https://coallaoh.github.io/data/scimeca2022iclr.pdf)
- [Environment Inference for Invariant Learning](http://proceedings.mlr.press/v139/creager21a/creager21a.pdf)
- [ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness.](https://arxiv.org/abs/1811.12231)
{{< /details >}}

{{< details "Explainability" >}}
- [Explanation in artificial intelligence: Insights from the social sciences](https://www.sciencedirect.com/science/article/pii/S0004370218305988?casa_token=HfkXcrQBLj4AAAAA:i4QhGuIsXDlmZ_EhfMyCCFkn2tnoI0JsVM5O8Qggf01HG0aMZeatCEY2UsJxKfvYD2BtwG6EZkI)
- [Sanity Checks for Saliency Maps](https://proceedings.neurips.cc/paper/2018/file/294a8ed24b1ad22ec2e7efea049b8737-Paper.pdf)
- [A benchmark for interpretability methods in deep neural networks](https://proceedings.neurips.cc/paper/2019/file/fe4b8556000d0f0cae99daa5c5c5a410-Paper.pdf)
- [Expanding Explainability: Towards Social Transparency in AI systems](https://dl.acm.org/doi/abs/10.1145/3411764.3445188?casa_token=6ZTaKuOCMUYAAAAA:vhJnNcizK2MMk4huftyKY4ANzL0_v2g4_eOc2DnZ582koWoD4ohfagwS4np45fNWLOeTeODd-BeL)
- [Human-Centered Explainable AI: Towards a Reflective Sociotechnical Approach](http://link.springer.com/10.1007/978-3-030-60117-1_33)
- [Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps](https://arxiv.org/abs/1312.6034)
- [Axiomatic attribution for deep networks](http://proceedings.mlr.press/v70/sundararajan17a.html)
- [SmoothGrad: removing noise by adding noise](https://arxiv.org/pdf/1706.03825.pdf)
- [A Unified Approach to Interpreting Model Predictions](https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html)
- [Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)](http://proceedings.mlr.press/v80/kim18d/kim18d.pdf)
- [Visualizing Deep Neural Network Decisions: Prediction Difference Analysis](https://openreview.net/pdf?id=BJ5UeU9xx)
- [Learning Deep Features for Discriminative Localization](http://cnnlocalization.csail.mit.edu/Zhou_Learning_Deep_Features_CVPR_2016_paper.pdf)
- [Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization](https://arxiv.org/abs/1610.02391)
- ["Why Should I Trust You?": Explaining the Predictions of Any Classifier](https://dl.acm.org/doi/abs/10.1145/2939672.2939778)
- [Feature Visualization](10.23915/distill.00007)
- [Understanding Black-box Predictions via Influence Functions](http://arxiv.org/abs/1703.04730)
- [Estimating Training Data Influence by Tracing Gradient Descent](http://arxiv.org/abs/2002.08484)
{{< /details >}}

{{< details "Uncertainty" >}}
- [A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks](https://openreview.net/forum?id=Hkg4TI9xl)
- [On calibration of modern neural networks](http://proceedings.mlr.press/v70/guo17a/guo17a.pdf)
- [Deep Anomaly Detection with Outlier Exposure](https://openreview.net/forum?id=HyxCxhRcY7)
- [A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks](https://papers.nips.cc/paper/7947-a-simple-unified-framework-for-detecting-out-of-distribution-samples-and-adversarial-attacks.pdf)
- [Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning](http://proceedings.mlr.press/v48/gal16.pdf)
- [Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles](http://papers.nips.cc/paper/7219-simple-and-scalable-predictive-uncertainty-estimation-using-deep-ensembles.pdf)
- [Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs](https://papers.nips.cc/paper/2018/hash/be3087e74e9100d4bc4c6268cdbe8456-Abstract.html)
- [Averaging weights leads to wider optima and better generalization](https://arxiv.org/abs/1803.05407)
- [Efficient and scalable Bayesian neural nets with rank-1 factors](http://proceedings.mlr.press/v119/dusenberry20a/dusenberry20a.pdf)
- [What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?](https://papers.nips.cc/paper/7141-what-uncertainties-do-we-need-in-bayesian-deep-learning-for-computer-vision)
- [Addressing Failure Prediction by Learning Model Confidence](https://papers.nips.cc/paper/8556-addressing-failure-prediction-by-learning-model-confidence.pdf)
- [Why M Heads are Better than One: Training a Diverse Ensemble of Deep Networks](https://arxiv.org/abs/1511.06314)
- [DiverseNet: When One Right Answer is not Enough](https://openaccess.thecvf.com/content_cvpr_2018/papers/Firman_DiverseNet_When_One_CVPR_2018_paper.pdf)
{{< /details >}}

{{< details "Evaluation" >}}
- [Question and Answer Test-Train Overlap in Open-Domain Question Answering Datasets](https://aclanthology.org/2021.eacl-main.86.pdf)
- [A Metric Learning Reality Check](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123700681.pdf)
- [Evaluating Weakly-Supervised Object Localization Methods Right](https://openaccess.thecvf.com/content_CVPR_2020/papers/Choe_Evaluating_Weakly_Supervised_Object_Localization_Methods_Right_CVPR_2020_paper.pdf)
- [Do ImageNet Classifiers Generalize to ImageNet?](http://proceedings.mlr.press/v97/recht19a/recht19a.pdf)
- [Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations.](http://proceedings.mlr.press/v97/locatello19a/locatello19a.pdf)
- [Realistic Evaluation of Deep Semi-Supervised Learning Algorithms](https://papers.nips.cc/paper/2018/file/c1fea270c48e8079d8ddf7d06d26ab52-Paper.pdf)
- [Zero-Shot Learning-The Good, the Bad and the Ugly](https://openaccess.thecvf.com/content_cvpr_2017/papers/Xian_Zero-Shot_Learning_-_CVPR_2017_paper.pdf)
- [Sanity Checks for Saliency Maps](https://proceedings.neurips.cc/paper/2018/file/294a8ed24b1ad22ec2e7efea049b8737-Paper.pdf)
- [In Search of Lost Domain Generalization](https://arxiv.org/pdf/2007.01434.pdf)
- [Are We Learning Yet? A Meta-Review of Evaluation Failures Across Machine Learning](https://openreview.net/forum?id=mPducS1MsEK)
- [How to avoid machine learning pitfalls: a guide for academic researchers](https://arxiv.org/abs/2108.02497)
- [Show Your Work: Improved Reporting of Experimental Results](http://aclanthology.lst.uni-saarland.de/D19-1224.pdf)
{{< /details >}}




## Policies

{{< details "Registration & Exercise 0" >}}
<!-- ### Registration & Exercise 0 -->

The **registration period** ends on **27 October 2022**. During this period, you are required to work on Exercise 0 and submit it.
The Exercise 0 is an individual exercise and will be based on the prerequisite materials for the course.
It will be published right after the first lecture on 21 October 2022 on this web page (see `Schedule & exercises` section below).
Students who wish to enrol must submit their work on Exercise 0.
To prevent an empty submission, there is a minimal score (30%) for the exercise.
The necessary prerequisite materials will be lectured in the first lecture.

Exercise 0 serves two purposes:
- For us to admit students who are sufficiently motivated for the course.
- For you to gauge your own readiness for the course.

The timeline for registration is as follows:
- Now-20 October 2022: Check time & location for the course.
- 21 October 2022: Attend the first lecture.
- 21-27 October 2022: Work on Exercise 0 & submit.
- 28 October 2022: Register students who have submitted Exercise 0.
{{< /details >}}

### Grading policy

![TML_grading](/img/grading_scheme.png)

The final grade is essentially based on your exam performance. However, to encourage the participation in the exercises,
we award bonus boosts on the final grade based on the exercise performance.

**Exercise 0 and registration for course**

- We admit only those who submit the zeroth exercise to the course.
- Exercise 0 is an individual exercise.

**Exercise 1-3 score E% (0 - 100%)**

- Average score from Exercises 1-3.
- Exercises 1-3 are group exercises.

**Admission to exam**

- When the exercise grade is $\geq 60$%, you are granted the right to participate in the exam.
- Can take care of exceptional cases on an individual basis.

**Exam score (0 - 100%)**

- Based on your performance on your exam.
- The pass threshold for the course will be $\geq 50$% on the exam.
- There will be two exams: Exam 1 and Exam 2.
    - Case A: Sit Exam 1 and pass → Exam 1 score will be final (cannot sit Exam 2).
    - Case B: Sit Exam 1 and fail → You may sit Exam 2; Exam 2 score will be final.
    - Case C: Choose to skip Exam 2 → Exam 2 score will be final.


**Final score (0 - 100%)**

- The final score is your exam score with possible increments from your exercise performance.
- Increment from exercise = $(E-60)/40 \times 20$%, where $E$% is your exercise score.
    - If $E=100$, you will get 20%p additional points on top of your exam grade.
    - If $E=60$, no additional points will be awarded.
    - If $E< 60$, you will not be admitted to the exam.
- Increments from exercise will not let you pass the course if your exam score is below $50\%$.

**Final grade (1,0 - 5,0)**

- The final grade of the course will be based on the final score.


## Communication

### Lecturer

- [Seong Joon Oh](/#members)

### Tutors

- [Alexander Rubinstein](/#members)
- [Elif Akata](/#members)
- [Elisa Nguyen](/#members)
- [Michael Kirchhof](https://www.eml-unitue.de/people/michael-kirchhof)

### Central email

Please use the STAI group email `stai.there@gmail.com` to
- Submit your Colab exercises;
- Ask questions; and
- Send us feedback.

### Discord forum

For those who're registered for the course, ask the lecturer or tutors to add you to the Discord channel. We need your name and email address. Use it for

- Asking questions;
- Sending us feedback;
- Receiving official announcements; and
- Communicating others (e.g. finding partners).


## When & where

### Lecture & tutorial location

Seminarraum C118a (Informatik Sand 14)
https://goo.gl/maps/mP6Q92s6QcLoHK5v7

### Lecture times

- Fridays
- 1st session: 14:15-15:00
- 5-min break: 15:00-15:05
- 2nd session: 15:05-15:50

### Tutorial times

- Fridays 16:00-18:00
- Up to discussion

### Exam dates and locations

- Exam 1: 10:00 - 11:30, Tuesday 21.02.2023, Hörsaal N04 (Hörsaalzentrum Morgenstelle)
- Exam 2: 13:00 - 14:30, Friday 14.04.2023, Hörsaal **N16** (Hörsaalzentrum Morgenstelle)


## Schedule & exercises

{{<table "table table-striped table-bordered">}}
|   #  	|   Date  	|   Content  	|   Exercises  	|   Lead tutor  	|
|---	|---	|---	|---	|---	|
|   L1  	|   21/10/2022  	|   [Introduction](https://docs.google.com/presentation/d/1HbM1oXIwduT8Lldj5S1DlOO_cZC8P2_OK9Chh4R2IZo/edit?usp=sharing)  	|   [Exercise 0](https://colab.research.google.com/drive/1m34hoUQApiuT673oKcR97utOXFdmYRRm?usp=sharing)   (Due: 27/10/2022)  	|   Elif  	|
|   L2  	|   28/10/2022  	|   [OOD Generalisation - Definition and limitations](https://docs.google.com/presentation/d/1HQtkLVuxCjmU0mGEebIOOnHZED5lmBcrf1vPBhIzHCA/edit?usp=sharing) ([Video](https://youtu.be/DqrWiaEVKx4&list=PL5iDtgKiCe5SuhyyGQT5OImWmsItHr8OQ))   	|   [Exercise 1](https://colab.research.google.com/drive/1RyRuqBCoXb3zRZ2lxoS4vt1tvDHpSNHx?usp=sharing) <br />(Due: 21/11/2022)  	|   Alex  	|
|   L3  	|   04/11/2022  	|   [OOD Generalisation - Cue selection problem](https://docs.google.com/presentation/d/1NODSaP31IuT0923X6PQ0AkwqgEcyxuZZYpFf9kkdQQw/edit?usp=sharing) ([Video](https://youtu.be/5vWcflV8Gq8&list=PL5iDtgKiCe5SuhyyGQT5OImWmsItHr8OQ))  	|     	|   Alex  	|
|   L4  	|   11/11/2022  	|   [OOD Generalisation - Cue selection and adversarial generalisation](https://docs.google.com/presentation/d/1G459l_R_ir_mxuIJtaMHk-RLzXaEumlwB-oG0AeDfsk/edit?usp=sharing) ([Video](https://youtu.be/AZZv105ubbk&list=PL5iDtgKiCe5SuhyyGQT5OImWmsItHr8OQ)) 	|     	|   Alex  	|
|   L5  	|   18/11/2022  	|   [More OOD and Explainability - Definition and limitations](https://docs.google.com/presentation/d/1a9OGP5zZjEdOY5fb0L3CGskMjlS65U5AFYPV9XbfP-I/edit?usp=sharing) ([Video](https://youtu.be/TPVwXbXH0l8&list=PL5iDtgKiCe5SuhyyGQT5OImWmsItHr8OQ))  	|     	|   Alex / Elisa 	|
|   L6  	|   25/11/2022  	|   [Explainability - Attribution](https://docs.google.com/presentation/d/1GZBCZQWzqjAsUnNfgUmO9Ge1DX0M5flEjWMfHtabsJU/edit?usp=sharing) ([Video](https://youtu.be/Vk6UERA_HuI&list=PL5iDtgKiCe5SuhyyGQT5OImWmsItHr8OQ))  	|    [Exercise 2](https://colab.research.google.com/drive/1UO4hWoUKWB9lO_dACNDf8fxeBoXr4cvd?usp=sharing) <br /> (Due: 16/12/2022) 	|   Elisa  	|
|   L7  	|   02/12/2022  	|   [Explainability - Attribution & evaluation](https://docs.google.com/presentation/d/1ZXX_x8EJjUooktGP26fxntsa8mcFb0sKTALQZYVhJJY/edit?usp=sharing) ([Video](https://youtu.be/nN_PjSWAxdQ&list=PL5iDtgKiCe5SuhyyGQT5OImWmsItHr8OQ))	|     	|   Elisa  	|
|   L8  	|   09/12/2022  	|   [Explainability - Model explanation](https://docs.google.com/presentation/d/1iRvMVG6xOf2bIm2-zE05XMFpY6LVoaEL7gYSDejQpu4/edit?usp=sharing) ([Video](https://youtu.be/ZqFRKoupo_4&list=PL5iDtgKiCe5SuhyyGQT5OImWmsItHr8OQ)) 	|     	|   Elisa  	|
|       	|                	|   Christmas Break  	|     	|     	|
|   L9  	|   13/01/2023  	|   [Uncertainty - Definition and evaluation](https://docs.google.com/presentation/d/1DgA9oJQ_OzWS9wZ_qmPZAgxY9OqJHO4Q0n-5uCuQnrI/edit?usp=sharing) ([Video](https://www.youtube.com/watch?v=3zuGShCWPaU&list=PL5iDtgKiCe5SuhyyGQT5OImWmsItHr8OQ)) 	|   [Exercise 3](https://colab.research.google.com/drive/12y5Dfh6PXQrO0iSyA6DZNEhjWdllqDHt?usp=sharing) (Due: 03/02/2023)  	|   Michael  	|
|   L10  	|   20/01/2023  	|   [Uncertainty - Epistemic uncertainty](https://docs.google.com/presentation/d/1tRckcZxKats1qC4ePJjm4Nf-_Hg_fN6maCwrt5Ydwec/edit?usp=sharing) ([Video](https://www.youtube.com/watch?v=y_HmpYQmpXs&list=PL5iDtgKiCe5SuhyyGQT5OImWmsItHr8OQ))  	|     	|   Michael  	|
|   L11  	|   27/01/2023  	|   [Uncertainty - Aleatoric uncertainty](https://docs.google.com/presentation/d/1AO182cBObhU21-4F_5d4SkipEYslentLxxKxn4xeN8k/edit?usp=sharing) ([Video](https://www.youtube.com/watch?v=k7xOfJ7UZEY&list=PL5iDtgKiCe5SuhyyGQT5OImWmsItHr8OQ)) 	|     	|   Michael  	|
|   L12  	|   03/02/2023  	|   [Exam information, Final topics, Research @ STAI](https://docs.google.com/presentation/d/1DvisaUmvm6AaCm9pQ3z2zg5Gd1bG-AHJxe3HbeuhGTc/edit?usp=sharing) ([Video](https://www.youtube.com/watch?v=8Yny2EVAA94&list=PL5iDtgKiCe5SuhyyGQT5OImWmsItHr8OQ))  	|     	|   Elif  	|
{{</table>}}
