+++
abstract = "Evaluating modern machine learning models has become prohibitively expensive. Benchmarks such as LMMs-Eval and HELM demand thousands of GPU hours per model. Costly evaluation reduces inclusivity, slows the cycle of innovation, and worsens environmental impact. The typical approach follows two steps. First, select an anchor subset of data. Second, train a mapping from the accuracy on this subset to the final test result. The drawback is that anchor selection depends on clustering, which can be complex and sensitive to design choices. We argue that promoting diversity among samples is not essential; what matters is to select samples that maximise diversity in model responses. Our method, Diversifying Sample Condensation (DISCO), selects the top-k samples with the greatest model disagreements. This uses greedy, sample-wise statistics rather than global clustering. The approach is conceptually simpler. From a theoretical view, inter-model disagreement provides an information-theoretically optimal rule for such greedy selection. DISCO shows empirical gains over prior methods, achieving state-of-the-art results in performance prediction across MMLU, Hellaswag, Winogrande, and ARC."
date = "2026-01-27T00:00:00+00:00"
publication_date = "2026-04-24T00:00:00+00:00"
image = "alex2025disco.png"
publication = "International Conference on Learning Representations"
publication_short = "ICLR"
title = "DISCO: Diversifying Sample Condensation for Efficient Model Evaluation"
url_code = "//github.com/arubique/disco-public"
url_arxiv = "//arxiv.org/abs/2510.07959"
url_pdf = "//arxiv.org/pdf/2510.07959"
url_rtai = "//researchtrend.ai/papers/2510.07959"
url_project = "//arubique.github.io/disco-site/"


[[authors]]
    name = "Alexander Rubinstein"
    is_member = true
    id = "alex"
[[authors]]
    name = "Benjamin Raible"
    is_member = false
[[authors]]
    name = "Martin Gubri"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++

