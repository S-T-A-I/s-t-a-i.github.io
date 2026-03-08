+++
title = "Trustworthy Machine Learning"
semester = "Spring Semester 2026"
university = "KAIST AI"
image = "compass-2026.png"
sort_position = 4
subtitle = "Bridging the Communication Gap in Deploying General AI"
description = "Why does AI solve the Math Olympiad but fail to manage your calendar? General AI is not trustworthy in private settings because of three broken communication channels. Human to AI: underspecification (it doesn't know what I want). AI to Human: unexplainability and overconfidence (I don't know why it did that or if it's guessing). Environment: hostility (privacy leaks and security attacks). This course covers theoretical and technical background for these key topics in Trustworthy Machine Learning (TML). We conduct a critical review of classical and contemporary research papers and provide hands-on practicals."
+++

## 1. Goal

1. Students will be able to critically read, assess, and discuss research work in Trustworthy Machine Learning (TML).
2. Students will gain the technical background to implement basic TML techniques in a deep learning framework.
3. Students will be ready to conduct their own research in TML and make contributions to the research community.

## 2. Prerequisites

- Familiarity with Python and PyTorch coding.
- A pass grade from the Deep Learning Course (or equivalent).
- Basic knowledge of machine learning concepts.
- Basic maths: multivariate calculus, linear algebra, probability, statistics, and optimisation.

## 3. TML Book

Previous course materials are available as a book: https://trustworthyml.io/ (also on [arXiv](https://arxiv.org/abs/2310.08215)).

The book will be useful for the course. However, the course materials are updated yearly to stay aligned with the latest research, so it won't cover new topics.

## 4. Schedule

<table class="table table-bordered">
<thead>
<tr><th>#</th><th>Date</th><th>Content</th><th>Project</th></tr>
</thead>
<tbody>
<tr class="part-0"><td>L1</td><td>Mar 06</td><td><a href="https://docs.google.com/presentation/d/17BCFaHw7q4Momahitjh-9yj12tGIzV6-hsnCwl9k5Ao/edit?usp=sharing">Orientation (short session)</a> · <a href="https://drive.google.com/file/d/1_HKmdhgUxwxeqyRJ5E6_Dcx_xQmVfsOv/view?usp=sharing">Video</a></td><td>—</td></tr>
<tr class="part-1"><td>L2</td><td>Mar 13</td><td><strong>I. Human → AI:</strong> ML Foundations & Generalisation Primer</td><td>—</td></tr>
<tr class="part-1"><td>L3</td><td>Mar 20</td><td>Underspecification & Cues</td><td><strong>Team formation due (23:59)</strong></td></tr>
<tr class="part-1"><td>L4</td><td>Mar 27</td><td>LLM Communication & Modularity</td><td>—</td></tr>
<tr class="part-2"><td>L5</td><td>Apr 03</td><td><strong>II. AI → Human:</strong> Explanation & XAI</td><td>—</td></tr>
<tr class="part-2"><td>L6</td><td>Apr 10</td><td>Attribution Methods</td><td>—</td></tr>
<tr class="part-2"><td>L7</td><td>Apr 17</td><td>TDA Frontiers & Mechanistic Interpretability</td><td>—</td></tr>
<tr class="part-5"><td>L8</td><td>Apr 24</td><td>Proposal presentations (midterm week)</td><td><strong>Proposal report due (23:59); Proposal presentation</strong></td></tr>
<tr class="part-2"><td>L9</td><td>May 01</td><td>Uncertainty I (Aleatoric)</td><td>—</td></tr>
<tr class="part-2"><td>L10</td><td>May 08</td><td>Uncertainty II (Epistemic)</td><td>—</td></tr>
<tr class="part-2"><td>L11</td><td>May 15</td><td>Uncertainty III (LLMs)</td><td>—</td></tr>
<tr class="part-3"><td>L12</td><td>May 22</td><td><strong>III. Privacy & Security:</strong> Landscape & Data Privacy</td><td>—</td></tr>
<tr class="part-3"><td>L13</td><td>May 29</td><td>Contextual Privacy & Model Integrity</td><td>—</td></tr>
<tr class="part-3"><td>L14</td><td>Jun 05</td><td>Adversarial Attacks & Jailbreaking</td><td>—</td></tr>
<tr class="part-4"><td>L15</td><td>Jun 12</td><td><strong>IV. Synthesis & Wrap-up</strong></td><td><strong>Final report due (23:59); Peer eval due (23:59)</strong></td></tr>
<tr class="part-5"><td>L16</td><td>Jun 19</td><td>Final Presentations</td><td><strong>Final presentation</strong></td></tr>
</tbody>
</table>

## 5. Grading

{{<table "table table-striped table-bordered">}}
| Component | Weight |
|---|---|
| Proposal presentation | 15% |
| Proposal report | 15% |
| Final presentation | 35% |
| Final report | 35% |
| **Total** | **100%** |
{{</table>}}

Late submissions are not accepted. A missed deadline counts as a zero.

## 6. Projects

- **Team size:** 3 students per team.
- **Formation:** Use the `#team-formation` Slack channel to find team members. Teams finalised by L3 (Mar 20, 23:59).
- **Compute:** Each student receives a 50 USD Google Cloud Platform voucher for the project. Each team of three therefore has 150 USD credit.
- **Template:** Use the [ICML 2026 LaTeX template](https://icml.cc/Conferences/2026/AuthorInstructions) for both proposal and final reports.
- **Deliverables:**
  - Proposal: 1-2 page report + 5 min presentation.
  - Final: 4-page report (ICML format, excluding references) + 10 min presentation.
- **Peer evaluation:** Mandatory form at the end. Distribute 100 points among your team members based on contribution. Unequal splits will affect individual grades.

### Example project topics

Topics are open; students choose direction and methods. Examples of the kind of project that fits the course:

1. **Test-time detection of prompt sensitivity.** Prior work has shown that VLMs are sensitive to prompt phrasing. The open question is whether we can detect *at test time* that a prediction is prompt-sensitive and flag it to the user, without access to ground truth. Propose and evaluate a detection method. Models: CLIP ViT-B/32, LLaVA-7B (both run on a single T4). Datasets: ImageNet, EuroSAT, or other zero-shot classification benchmarks. References: [PARC](https://arxiv.org/abs/2506.14808) (CVPR 2025, quantifying VLM prompt sensitivity), [WaffleCLIP](https://openaccess.thecvf.com/content/ICCV2023/papers/Roth_Waffling_Around_for_Performance_Visual_Classification_with_Random_Words_and_ICCV_2023_paper.pdf) (ICCV 2023, random descriptors match LLM-generated prompts).
2. **Surfacing knowledge conflicts in RAG.** Recent work resolves parametric-contextual conflicts silently. An open problem is whether the system can instead *detect and surface* the conflict to the user, letting them decide. Build a conflict-detection pipeline and evaluate its precision. Models: Llama 3.1 8B or Mistral 7B with a FAISS index (A100 or T4 with quantisation). Datasets: Natural Questions or TriviaQA with synthetically altered retrieval passages. References: [FaithfulRAG](https://aclanthology.org/2025.acl-long.1062/) (ACL 2025, fact-level conflict modelling), [AdaCAD](https://aclanthology.org/2025.naacl-long.581/) (NAACL 2025, adaptive decoding for knowledge conflicts), [JuICE](https://proceedings.mlr.press/v267/li25c.html) (ICML 2025, test-time attention intervention).
3. **Mechanistic vs data attribution for the same failure.** Recent work attributes model failures either to training data (TDA) or to internal mechanisms (layer-wise dynamics, circuit analysis). These perspectives are rarely compared. Pick a failure mode (e.g. hallucination, gender bias) and apply both attribution families to the same cases. Do they agree? Models: ViT-B on ImageNet for vision; Llama 3.1 8B or a smaller LLM for language. Datasets: task-specific failure sets you curate. References: [Accountability Attribution](https://icml.cc/virtual/2025/50882) (ICML 2025, tracing behaviour to training stages), [DDA](https://aclanthology.org/2024.emnlp-main.782/) (EMNLP 2024, influence functions with fitting error correction).
4. **Confidence under distribution shift.** Methods like BaseCal and EAGLE improve calibration on in-distribution data. Less is known about how confidence estimates degrade under distribution shift or across multi-turn conversations. Evaluate existing calibration methods on shifted inputs and propose a detection strategy. Models: Llama 3.1 8B or Mistral 7B (sampling-based methods need ~20-50 forward passes per input; budget for this). Datasets: TriviaQA, MMLU with domain-shifted or adversarially perturbed variants. References: [IB-EDL](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0cbdd1e6613c42fe975337671790f406-Abstract-Conference.html) (ICLR 2025, information-theoretic evidential calibration), [Multicalibration](https://proceedings.mlr.press/v235/detommaso24a.html) (ICML 2024, group-wise calibration for LLMs).
5. **Paper reproduction.** Reproduce the key experiments of a published paper covered in the course. Verify the claims, test on a different model or dataset, and report where the results hold and where they break. Choose a paper whose experiments fit the compute budget.

## 7. Generative AI Policies

Students may use generative AI tools (e.g. LLMs, VLMs, image generators). However, you are solely responsible for all outputs you submit. We will apply heavy penalties for:
- Hallucinated or factually incorrect outputs.
- Unsound or fabricated citations.
- Plagiarised materials.
- AI slop (low-effort, generic AI-generated content).

Severe cases may be reported to the university for disciplinary action.

You must be ready to answer clarification requests from the lecturer or tutors at any point. Inability to explain your own work will be treated as evidence of academic misconduct.

We do not tolerate very similar creative work among class members. AI tends to produce similar outputs across sessions and model families. Diversify your answers, especially for creative work. Suspicion of copied work will be penalised.

## 8. Communication & Logistics

**Language:** English

**Lecturer:** [Seong Joon Oh](../../member/joon/)

**Tutors:** TBA

**When:** Fridays 13:00-15:30 (1st session 13:00-14:10, break 14:10-14:20, 2nd session 14:20-15:30)

**Where:** 양재산학캠퍼스 대강의실 (Hybrid, [Zoom](https://kaist.zoom.us/j/8340478956))

**Email:** `stai.there@gmail.com` for submissions, questions, and feedback.

**Slack:** Email us your name and preferred email address to be added. Use it for questions, announcements, and finding team members.