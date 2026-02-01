+++
abstract = "Retrieval-augmented generation (RAG) mitigates many problems of fully parametric language models, such as temporal degradation, hallucinations, and lack of grounding. In RAG, the model's knowledge can be updated from documents provided in context. This leads to cases of conflict between the model's parametric knowledge and the contextual information, where the model may not always update its knowledge. Previous work studied knowledge conflicts by creating synthetic documents that contradict the model's correct parametric answers. We present a framework for studying knowledge conflicts in a realistic setup. We update incorrect parametric knowledge using real conflicting documents. This reflects how knowledge conflicts arise in practice. In this realistic scenario, we find that knowledge updates fail less often than previously reported. In cases where the models still fail to update their answers, we find a parametric bias: the incorrect parametric answer appearing in context makes the knowledge update likelier to fail. These results suggest that the factual parametric knowledge of LLMs can negatively influence their reading abilities and behaviors."
date = "2024-10-01T00:00:00+00:00"
image = "evgenii2024ralm.png"
publication = "Conference on Language Modeling"
publication_short = "CoLM"
title = "Studying Large Language Model Behaviors Under Realistic Knowledge Conflicts"
url_code = "//github.com/kortukov/realistic_knowledge_conflicts"
url_arxiv = "//arxiv.org/abs/2404.16032"
url_pdf = "//arxiv.org/pdf/2404.16032"
url_rtai = "//researchtrend.ai/papers/2404.16032"


[[authors]]
    name = "Evgenii Kortukov"
    is_member = true
    id = "evgenii"
[[authors]]
    name = "Alexander Rubinstein"
    is_member = true
    id = "alex"
[[authors]]
    name = "Elisa Nguyen"
    is_member = true
    id = "elisa"
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
+++
