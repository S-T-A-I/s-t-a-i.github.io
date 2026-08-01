+++
abstract = "Deployed large reasoning models (LRMs) often behave unexpectedly. Test-time steering controls LRM outputs by intervening on their hidden representations, but it can degrade output quality. We argue that prior steering work implicitly relies on internal features that detect behavior in already generated text. We show that these detection features are poor predictors of future behavioral outcomes, and thus not the natural intervention target. Instead, we train activation probes to predict future behavior likelihoods from intermediate reasoning steps. These probes predict the most likely behavior with 64%-91% accuracy, revealing a separate type of internal prediction features. Building on these prediction features, we introduce a text-level steering method, Future Probe Controlled Generation. FPCG samples multiple candidate sentences and chooses the best one according to a probe predicting the future behavior likelihood. This enables steering with almost no output quality degradation. FPCG also enables steering in several evaluations where activation steering fails. These results show that distinguishing detection and prediction features enables a more nuanced approach to controlling LRM behaviors."
date = "2026-06-09T00:00:00+00:00"
publication_date = "2026-06-09T00:00:00+00:00"
image = "evgenii2026futureprobes.png"
publication = "arXiv"
publication_short = "arXiv"
title = "Predicting Future Behaviors in Reasoning Models Enables Better Steering"
url_arxiv = "//arxiv.org/abs/2606.11172"
url_pdf = "//arxiv.org/pdf/2606.11172"

[[authors]]
    name = "Evgenii Kortukov"
    is_member = false
[[authors]]
    name = "Piotr Komorowski"
    is_member = false
[[authors]]
    name = "Florian Klein"
    is_member = false
[[authors]]
    name = "Paula Engl"
    is_member = false
[[authors]]
    name = "Gabriele Sarti"
    is_member = false
[[authors]]
    name = "Seong Joon Oh"
    is_member = true
    id = "joon"
[[authors]]
    name = "Sebastian Lapuschkin"
    is_member = false
[[authors]]
    name = "Wojciech Samek"
    is_member = false
+++
