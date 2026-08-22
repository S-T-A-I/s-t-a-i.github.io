+++
title = "Information Retrieval for AI"
semester = "Autumn Semester 2026"
university = "KAIST AI"
image = "irai-2026.png"
sort_position = 5
subtitle = "How AI systems reach the knowledge they do not hold"
description = "Model weights are a lossy, frozen compression of the world, so every serious AI system needs a way to reach the rest of it. This course teaches that path, from the inverted index of the 1970s to the research agents of 2026. Half the assigned papers were published in the last eighteen months, and one of them has no venue yet. The framing is information retrieval for AI, not AI for information retrieval. Classical retrieval is the toolkit rather than the subject, and BM25 earns its place not as history but because dense retrievers still lose to it out of domain. Monday is a lecture on the method. Wednesday is a structured discussion of a research paper that uses it. Alongside both, the class builds its own document collection, writes its own queries, judges relevance by hand, and measures a retrieval system against the judgements it produced itself."
+++

**In one line.** Mondays are lectures, Wednesdays are structured paper discussions in fixed groups of five, and the only weekly deadline is a half-page written review due Tuesday at 18:00. Four hours a week, two of them contact time. No exam.

**Contents**

- [1. Goal](#1-goal)
- [2. Prerequisites](#2-prerequisites)
- [3. How the course runs](#3-how-the-course-runs)
- [4. Schedule](#4-schedule)
- [5. The class test collection and the project](#5-the-class-test-collection-and-the-project)
- [6. Assessment](#6-assessment)
- [7. Generative AI policy](#7-generative-ai-policy)
- [8. Reading list](#8-reading-list)
- [9. Logistics](#9-logistics)

## 1. Goal

By December, students will be able to:

1. Place a retrieval method on the spectrum from sparse to dense, and say when BM25 still beats it.
2. Say where an AI system's knowledge sits when it runs, and what that choice costs.
3. Build a test collection, and state what nDCG measures and what it hides.
4. Find where a fluent, correct-sounding account of a paper is subtly wrong.
5. Report from their own records where language models fail on research reading.
6. Diagnose why a change to a retrieval system did or did not help.
7. Defend a technical position under challenge, and change it when given a reason.

Objectives 4, 5 and 7 matter most. Few students will ever build a search engine. All of them will read papers whose claims outrun their evidence, work with models that are fluent and wrong, and have to defend a position in a room.

{{< details "The two threads that run through the term" >}}

**From sparse to dense.** TF-IDF, BM25, learned sparse retrieval, bi-encoders, late interaction. A spectrum, not a succession.

**Where knowledge sits when the system runs.** One figure, redrawn every few weeks.

| Regime | Mechanism | Example |
|---|---|---|
| Parametric | All knowledge in weights, fixed compute | A dense LLM |
| Conditionally parametric, by compute | A router selects which parameters to run | Mixture of experts |
| Conditionally parametric, by lookup | A hash selects which parameters to read | Product-key memory, memory layers, Engram |
| Written at inference | The memory is learned while the model runs | Titans, cartridges, sparse memory finetuning |
| Semi-parametric | An index wired into the forward pass | kNN-LM, RETRO, memory networks |
| Non-parametric | A corpus placed into the prompt | Retrieval-augmented generation |
| Open world | A policy decides what to fetch | Search agents, deep research |

The course opens with attention itself as retrieval over the context, so the whole spectrum reads as one idea at different scales.

The middle three rows are where the figure changed in 2026. Routing computation and routing a lookup used to be one row, until a result that year found them complementary rather than alternative, with an optimum between them. The row above them did not exist at all.

{{< /details >}}

## 2. Prerequisites

- Familiarity with Python and PyTorch coding.
- Working knowledge of transformers and standard deep learning.
- Basic maths: linear algebra, probability, statistics.
- No prior background in information retrieval is required, and none is expected. The classical material in September will be the new material for most of this audience.

## 3. How the course runs

**Monday** is a lecture on the method. 45 minutes of content, 10 minutes of questions, 5 minutes on the following Wednesday.

**Wednesday** is a discussion of a research paper that uses it, in fixed groups of five. Four Wednesdays are lectures instead.

**The only weekly deadline is Tuesday 18:00**, when you submit a half-page written review of the assigned paper.

| When | What | Time |
|---|---|---|
| Thu-Sun | Read the assigned paper properly | 1.2 h |
| Mon 09:00-10:00 | The lecture teaching the method | 1 h |
| Mon evening | Consult the supporting paper, run the model check | 30 min |
| Tue | Write the half-page review, submit by 18:00 | 20 min |
| Wed 09:00-10:00 | The session | 1 h |

**Four hours a week, two of them contact time.** There is no project work in a normal week. Three weeks are heavier - sessions 9, 19 and 29 add about two hours each.

{{< details "Groups and roles" >}}

Students are divided into fixed discussion groups of five, held all semester. Each member takes a different role for the week, and roles rotate. Every student holds each role at least once over the term.

| Role | The job | Supporting paper |
|---|---|---|
| Adversary | Attack the experiments, find the missing baseline | A paper that contradicts the assigned one |
| Historian | What came before, and what this paper quietly discards | The predecessor it builds on |
| Replicator | Check that the numbers support the claims, and measure something | A reproduction or a rerun |
| Referee | On a paper too new to have been reproduced: would you accept it? | The paper's public review thread, or none |
| Extender | Propose the next paper and say what it would test | The successor, chosen by the extenders themselves |
| Applier | Would you deploy this, at what index size, latency and cost | A systems or deployment paper |

**There are five roles, not six.** On the four assigned papers published in the last eighteen months, the Replicator becomes the Referee, because no reproduction study exists for a paper that new. The role keeps the same question - should this be believed - and changes the evidence. Where the paper has a public review thread, you read what four reviewers decided and compare it with what your group decided. Where it does not, you write the first review yourself.

Sessions 13 and 27 have threads. Session 21 does not, so the Referee reads the reviews of the *contradicting* paper as a worked example and then reviews the anchor cold. Session 25 has neither, and that Referee writes a review with no model to follow at all.

Note-taking is a duty rather than a role. Rotate it inside the group.

Everyone reads the assigned paper closely. Each student additionally consults one supporting paper chosen for their role - the abstract, the relevant table, the part bearing on their role. The supporting paper belongs to the role, not the group, so all students holding a role in a given week read the same one. They do not coordinate, and there is no joint deliverable.

One Wednesday therefore puts six papers into circulation: the assigned paper, read by everyone, and five supporting papers.

{{< /details >}}

{{< details "The weekly written review, and its four fields" >}}

**One review per student, half a page, due 18:00 on Tuesday.** That is the entire weekly obligation outside class.

**1. Model check.** Give a language model the assigned paper and the prompt for your role. Name the model and version, paste its answer in two or three lines, then say what it got wrong or missed.

| Role | Prompt |
|---|---|
| Adversary | "What are the three weakest points in this paper's experimental evidence?" |
| Historian | "What prior work does this build on, and what does it discard from that work?" |
| Replicator | "Do the numbers in the results tables support the claim in the abstract? What would I need to rerun this?" |
| Referee | "Write the four weakest points a conference reviewer would raise about this paper, and give it a score out of 10 with reasons." |
| Extender | "What experiment should come next, and what would it settle?" |
| Applier | "What would it cost to deploy this - index size, latency, serving?" |

**2. What you found, in your role this week.** The substantive point, and what would be needed to believe or refute it. This is the bulk of the page.

**3. A class-local hook.** One sentence tying the paper to something only a class member knows.

**4. One question for the class.** Something you cannot answer from the paper. Three are chosen to open Wednesday.

The half-page cap is deliberate. It holds the weekly load down and forces you to pick your best point rather than list five.

{{< /details >}}

{{< details "The Wednesday hour, minute by minute" >}}

| Time | What happens |
|---|---|
| 0-5 | Framing of the assigned paper, this week's ranking criterion, three student questions |
| 5-22 | Discussion groups. Table the five points, rank them, file a written conclusion |
| 22-40 | Open challenge. Groups defend their conclusions against each other |
| 40-58 | Synthesis, corrections, and placement on the knowledge-location spectrum |
| 58-60 | End-of-session questions, answered individually |

The 17 minutes in groups are not open discussion. There is one forced decision and a deadline.

| | Task |
|---|---|
| 5 min | Table the five points, one minute each, in role order. State your point in one sentence, give your evidence, stop. No interruptions until all five have spoken |
| 8 min | Rank the five points against this week's criterion. The group must converge on one ranking |
| 4 min | File the written conclusion by minute 22. Whatever is written at 22:00 is what gets challenged |

**The written conclusion is four lines.**

1. The strongest point in the group this week, and which role brought it.
2. What would settle it - the experiment, the number, the missing baseline.
3. Does the paper survive? Yes / yes with caveats / no.
4. Where it sits on the knowledge-location spectrum, in one phrase.

**The ranking criterion is announced at 9:00 and varies weekly.** Examples: which point most threatens the central claim; which would most change whether you would use this method; which would the authors find hardest to answer; which will still matter in five years; which would you spend a week testing.

**During the open challenge, the member who answers is named at the moment the group is called.** Every member must therefore be able to defend the group's conclusion. There are no prepared presentations of the assigned paper. Everyone has read it, and a summary would waste eight minutes of sixty.

{{< /details >}}

{{< details "End-of-session questions" >}}

Three questions, answered individually in the last two minutes.

1. Which role's point won in your group?
2. Name one point that was dropped, and why it lost.
3. What did you walk in believing was strongest? Did that change, and what changed it?

Question 2 can only be answered by someone who followed the argument. You read one supporting paper; the other four reach you only through the discussion. Question 3 is the only place the course pays for changing your mind.

{{< /details >}}

## 4. Schedule

Sessions run 09:00-10:00, except the three project workshops, which run 09:00-10:30.

| # | Date | Content | Due |
|---|---|---|---|
| 1 | Mon 31 Aug | Why retrieval now. Eight arguments, the knowledge-location spectrum, course mechanics | - |
| 2 | Wed 02 Sep | The inverted index. Tokenisation, postings, compression. TF-IDF and the vector space model | - |
| 3 | Mon 07 Sep | BM25 and probabilistic ranking. Query likelihood, smoothing, relevance feedback | - |
| 4 | Wed 09 Sep | **Discussion.** Critically Examining the "Neural Hype" | Review, Tue 18:00 |
| 5 | Mon 14 Sep | Evaluation, and how benchmarks lie. MAP, MRR, nDCG. Pooling and its biases. TREC, BEIR, and the same failure recurring in 2026 | - |
| 6 | Wed 16 Sep | **Discussion.** BEIR. Launch of the class collection and judging protocol | Review, Tue 18:00 |
| - | 21-23 Sep | No class - Chuseok week | - |
| 7 | Mon 28 Sep | Web search, and what is wrong with it today. Crawling, indexing at scale, PageRank, HITS. The modern commercial stack, who owns an index, eleven weaknesses | Three-engine query comparison, before class |
| 8 | Wed 30 Sep | Bi-encoders, and one space for both jobs. SentenceBERT, DPR, hard negatives, distillation. LLM embedders. Generating and retrieving in a single pass | - |
| - | Mon 05 Oct | No class - substitute holiday | - |
| 9 | Wed 07 Oct | **Project workshop 1, 90 min.** Building a test collection. Protocol design, live judging, disagreement analysis. Project kickoff | Two queries per student, in session |
| 10 | Mon 12 Oct | Late interaction, and multi-vector made servable. ColBERT, SPLADE, hybrid retrieval and fusion. MUVERA, CRISP, ColPali | - |
| 11 | Wed 14 Oct | **Discussion.** ColBERT | Review, Tue 18:00 |
| 12 | Mon 19 Oct | Retrieval that needs reasoning. Reasoning-intensive queries, synthetic training data, rerankers that reason | - |
| 13 | Wed 21 Oct | **Discussion.** BRIGHT | Review, Tue 18:00 |
| 14 | Mon 26 Oct | Retrieval uncertainty. Probabilistic embeddings. Ambiguity as underspecification. Cross-modal retrieval | - |
| 15 | Wed 28 Oct | **Discussion.** Probabilistic Embeddings for Cross-Modal Retrieval | Review, Tue 18:00 |
| 16 | Mon 02 Nov | Approximate nearest neighbour search. HNSW, IVF-PQ, product quantisation. Vector databases. The recall-latency curve | - |
| 17 | Wed 04 Nov | Attention as retrieval. Retrieval heads, attention as associative memory, and the memory-network lineage | - |
| 18 | Mon 09 Nov | Memory as an architectural axis. Product-key memory, memory layers at scale, mixture of experts, and Engram's second axis of sparsity | - |
| 19 | Wed 11 Nov | **Project workshop 2, 90 min.** Complete the judging pass, analyse judge agreement, implement and measure your group's modification | Relevance judgements complete |
| 20 | Mon 16 Nov | Memory learned at test time. Titans, nested learning, cartridges. Weights that can be edited without forgetting | - |
| 21 | Wed 18 Nov | **Discussion.** Engram | Review, Tue 18:00 |
| 22 | Mon 23 Nov | Language models with an index attached. kNN-LM, RETRO. Where the gradient stops. Long context versus retrieval | - |
| 23 | Wed 25 Nov | Retrieval-augmented generation. Pipelines and failure modes. Chunking, reranking. Graph and memory RAG. Corpus poisoning and prompt injection | - |
| 24 | Mon 30 Nov | Agentic retrieval and deep research. IRCoT, Self-RAG, ReAct. Search-augmented reinforcement learning. Report synthesis, citation faithfulness, literature synthesis | - |
| 25 | Wed 02 Dec | **Discussion.** Search-R1 | Review, Tue 18:00 |
| 26 | Mon 07 Dec | Agent memory and context engineering. Compaction, isolated contexts, long-term memory. What production systems do, and whether anyone can measure it | - |
| 27 | Wed 09 Dec | **Discussion.** Evaluating Memory in LLM Agents | Review, Tue 18:00 |
| 28 | Mon 14 Dec | Privacy, personalisation and unlearning. Adversarial retrieval and SEO. Why an index can forget, and what 2025 did to that argument | - |
| 29 | Wed 16 Dec | **Project workshop 3, 90 min.** Group presentations, review of the class record of model failures, and the closing answer to session 1 | Write-up due 09 Dec, 23:59 |

Wednesday sessions are not recorded, so that criticism stays candid. Monday lectures are recorded.

## 5. The class test collection and the project

> You are given a BM25 baseline over the class collection, an evaluation harness, and the class relevance judgements. **Make one change to the retrieval pipeline.** Predict its effect before you write any code. Measure it. Explain the gap between what you predicted and what happened.

| Fixed | Yours to change |
|---|---|
| The collection, the relevance judgements, the metrics, the harness | Anything between the query and the ranked list |

**Compute is a laptop.** Fifty documents and sixty queries. Encoding with a small sentence transformer takes seconds on Colab's free CPU tier, and ColBERT inference over 48 documents runs on CPU. No compute credits are needed and no paid account is required, including for the weekly model check.

{{< details "Why the class builds its own test collection" >}}

To say that system A beats system B, you must know which documents are relevant for a set of queries. That list is a test collection, and a human made it by hand. Every number in every retrieval paper rests on one.

Most students read "nDCG 0.43" as a measurement. It is not. It is the output of a chain of human decisions about what counts as relevant, and you only see that by making those decisions.

The collection is built from the papers the class has read - about 48 documents by December. You cannot judge relevance for documents you do not understand, so a public benchmark in an unfamiliar domain would produce guesses rather than disagreements worth studying.

**What a query looks like matters.**

| Query | What happens |
|---|---|
| "ColBERT" | Bad. The relevant documents are obvious, everyone agrees, nothing is learned |
| "methods whose reported gains came from better training rather than better architecture" | Good. Judging requires reading and thinking, and reasonable people disagree at the borders |

At least one conceptual query per student is required.

The numbers work out at roughly 60 queries, 480 query-document pairs, and two judges per pair, which is about 32 judgements each - some 15 minutes of work. Two judges per pair is what makes agreement measurable. Expect agreement to be low, and treat that as the finding rather than the failure.

At 48 documents the metrics are noisy and rankings will flip on reruns. That is also part of the lesson.

{{< /details >}}

{{< details "The modification menu and what you hand in" >}}

Groups claim one modification each at session 9, so that no two duplicate.

- Hybrid BM25 and dense retrieval, fused with reciprocal rank fusion
- A different bi-encoder checkpoint
- doc2query expansion over the collection
- An LLM reranker over the top ten
- Chunking papers into sections instead of indexing whole documents
- ColBERT late interaction

**Deliverables.** A run file (`query_id, doc_id, rank, score`), a one-page write-up due a week before session 29, and an eight-minute presentation.

**The relevance judgements freeze at session 19.** Groups may keep refining afterwards, and should report both their session-19 number and any later one.

{{< /details >}}

## 6. Assessment

| Component | Weight |
|---|---|
| Weekly paper reviews | 45% |
| End-of-session questions | 20% |
| Contribution to discussion | 10% |
| Project | 25% |
| **Total** | **100%** |

There is no exam and there are no quizzes.

**Two participation requirements**: writing queries, and completing your relevance judgements. More than two missed obligations across the term drops the final grade by one band.

**A student who does all of the work competently lands in the middle of the distribution, not at the top.** Grades are assigned by ranking the class and cutting bands, with a target of roughly even distribution across A+, A0, A-, B+ and B0. This is stated here rather than discovered in December.

{{< details "Weekly paper reviews, 45%" >}}

Eight reviews, one per discussion session. A random four are marked on the scale below and the rest on completion. You will not know in advance which count.

| Score | What it means |
|---|---|
| 4 | Found something real that changes how the paper should be read, or a model failure new to the class record |
| 3 | A substantive point the model check did not already contain |
| 2 | Competent, correct, adequate. The expected mark |
| 1 | Thin, or restates the model's output |
| 0 | Missing, fabricated numbers, or undeclared model use |

Note that "did the work adequately" is a 2, not a 4.

{{< /details >}}

{{< details "End-of-session questions, 20%" >}}

Eight sets of three questions, scored against your group's filed conclusion. Question 1 and question 3 are checked mechanically. Question 2 passes if it names a point actually raised in your group.

{{< /details >}}

{{< details "Contribution to discussion, 10%" >}}

Scored 0-2 whenever you are named to speak in plenary, either to defend your group's conclusion or to answer a question during synthesis. Opportunities are tracked and allocated so that every student is called roughly three times.

| Score | For |
|---|---|
| 2 | Answered the question actually asked, with a reason, and either held up under the follow-up or conceded cleanly |
| 1 | Answered, but restated the conclusion or your own review without engaging the challenge |
| 0 | Could not answer, or absent |

Marks go to the response to challenge. Not to fluency, and not to being right.

{{< /details >}}

{{< details "Project, 25%" >}}

Scored out of 10, then adjusted by peer evaluation within the group.

| Points | For |
|---|---|
| 0-3 | **The prediction.** Specific and falsifiable? "It will help" scores 0. "nDCG@10 rises about 0.03, because doc2query adds vocabulary our queries actually use" scores 3 |
| 0-3 | **The measurement.** Did it run? Is the comparison fair - same judgements, same metric, baseline re-run rather than quoted? Is every number reproducible from the submitted run file? |
| 0-3 | **The diagnosis.** Why did the result differ from the prediction? A wrong prediction correctly diagnosed scores 3. A right prediction with no explanation scores 1 |
| 0-1 | **Beating the baseline.** One point. That is all |

Position on the leaderboard is worth 10% of the project mark and 2.5% of the final grade. This is deliberate. A modification that made things worse, correctly diagnosed against a wrong prediction, outscores one that helped by accident.

**If your modification does not run**, you can still score on prediction and diagnosis - up to 6 of 10 - provided you submit an honest account of what broke. Only the measurement points are lost.

**Peer evaluation.** Each member distributes 100 points across all five members, including themselves. The mean of what the other four give you becomes a multiplier between 0.85 and 1.15.

{{< /details >}}

{{< details "What each grade looks like" >}}

| Grade | Profile |
|---|---|
| A+ | Reviews that found something real more than once. A project that beat the baseline for a defensible reason |
| A0 | Consistently sharp reviews, holds up when called on, strong project |
| A- | Good work throughout, one or two standout contributions |
| B+ | All the work done competently. Nothing missing, nothing exceptional |
| B0 | Work done but thin in places |
| B- | Repeated gaps, or reviews showing the paper was not read |
| F | Non-participation |

{{< /details >}}

## 7. Generative AI policy

**Use is expected, declared and marked.** The course does not defend against it. Detection does not work, and a ban would be absurd in a course about retrieval-augmented systems.

**Credit begins above what a model gives you.** Everything a model produces is free, so a review that restates the model's output scores low even when it is correct. A 3 requires a point the model check did not already contain. This removes any incentive to conceal.

**The bright line: any number in a submitted review must be reproducible from a submitted log.** Fabrication scores zero on that review, no argument. This is not an AI rule. It is the research norm, and it would have applied in 1996.

Undeclared model use scores zero on that submission.

{{< details "The class record of model failures" >}}

The weekly model check is where the policy becomes concrete. Each role's task needs a capability that is weak in a different way.

| What you ask for | What tends to come back |
|---|---|
| Ten objections to this paper | Fluent objections that dissolve on contact. The skill is triage |
| The paper's lineage | Hallucinated citations |
| A rerun script | Code that runs and computes the wrong thing |
| Next experiments | Generic, hedged, unfalsifiable proposals |
| Index size and cost | Confident bad arithmetic |

Every review contributes one line to a class record of model failures - model, version, paper type, failure observed, how it was caught. It is reviewed at sessions 19 and 29. The interesting question is which failures disappear as models improve during the term, and nobody knows that in advance.

The instructor prepares lecture material with model assistance and adds the model's mistakes to the same record.

{{< /details >}}

## 8. Reading list

| # | Session | Paper |
|---|---|---|
| 1 | 4 (9 Sep) | Yang, Lu & Lin (2019), *Critically Examining the "Neural Hype"* (SIGIR) |
| 2 | 6 (16 Sep) | Thakur et al. (2021), *BEIR* (NeurIPS Datasets and Benchmarks) |
| 3 | 11 (14 Oct) | Khattab & Zaharia (2020), *ColBERT* (SIGIR) |
| 4 | 13 (21 Oct) | Su et al. (2025), *BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval* (ICLR) |
| 5 | 15 (28 Oct) | Chun et al. (2021), *Probabilistic Embeddings for Cross-Modal Retrieval* (CVPR) |
| 6 | 21 (18 Nov) | Cheng et al. (2026), *Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models* - the Engram paper |
| 7 | 25 (2 Dec) | Jin et al. (2025), *Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning* (COLM) |
| 8 | 27 (9 Dec) | Hu, Wang & McAuley (2026), *Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions* (ICLR) |

**Four of the eight were published in the last eighteen months, and that is the point.** An earlier draft of this course required every assigned paper to be two to six years old, so that a real contradicting paper, a real predecessor and a reproduction all existed. That rule produces a tidy syllabus about a field that has moved on. It is gone. Sessions 21 and 27 assign work whose lineage is still being written, and part of the exercise is judging a paper without the safety of a literature that has already judged it.

Four notes on the choices.

- **Session 4** opens with a paper whose whole argument is that other people's baselines were weak. That sets the tone for eight sessions.
- **Sessions 6 and 13** are the same finding five years apart. BEIR reports that BM25 beats dense retrievers out of domain; BRIGHT reports that they lose again once the query needs reasoning. Nobody is told in advance that these are related.
- **Session 15** is the instructor's own paper, deliberately. Six students attacking it in front of the author settles the question of whether criticism is welcome.
- **Session 27** closes the loop to session 4 with 2026 material. A benchmark finds that no memory method masters all four competencies it defines; the adversary's paper then finds that swapping only the embedding model flips which method wins.

{{< details "Supporting papers, where they are settled" >}}

The rest are published two weeks before each session. Extenders choose their own. Eight slots are still open. The Referee role closed four of them: a paper published in January 2026 has no reproduction study, but it usually has reviewers, and their thread is a better document than an invented rerun.

| Session | Role | Paper |
|---|---|---|
| 4 | Adversary | Nogueira & Cho (2019), *Passage Re-ranking with BERT* |
| 4 | Historian | Armstrong et al. (2009), *Improvements That Don't Add Up* (CIKM) |
| 4 | Replicator | Trotman, Puurula & Burgess (2014), *Improvements to BM25 and Language Models Examined* |
| 4 | Applier | Yang, Fang & Lin (2018), *Anserini* |
| 6 | Adversary | Ni et al. (2022), *Large Dual Encoders Are Generalizable Retrievers* |
| 6 | Historian | Nguyen et al. (2016), *MS MARCO* |
| 6 | Replicator | Kamalloo, Thakur, Lin et al. (2024), *Resources for Brewing BEIR* |
| 6 | Applier | Lin et al. (2021), *Pyserini* |
| 11 | Adversary | Hofstätter et al. (2021), *Balanced Topic Aware Sampling* (TAS-B) |
| 11 | Historian | Karpukhin et al. (2020), *DPR* |
| 11 | Replicator | Santhanam et al. (2022), *ColBERTv2* (NAACL) |
| 11 | Applier | Santhanam et al. (2022), *PLAID* (CIKM) |
| 13 | Adversary | Shao et al. (2025), *ReasonIR: Training Retrievers for Reasoning Tasks* |
| 13 | Referee | The paper's ICLR 2025 review thread, on OpenReview |
| 13 | Applier | Zhang et al. (2025), *Qwen3 Embedding* |
| 21 | Adversary | Behrouz, Zhong & Mirrokni (2025), *Titans: Learning to Memorize at Test Time* (NeurIPS) |
| 21 | Historian | Sukhbaatar et al. (2015), *End-To-End Memory Networks* (NeurIPS) |
| 21 | Referee | Titans' NeurIPS 2025 review thread, as a worked example. Engram itself has no thread, so you write the first review |
| 21 | Applier | Berges et al. (2024), *Memory Layers at Scale* |
| 25 | Adversary | Chen et al. (2025), *BrowseComp-Plus* |
| 25 | Historian | Trivedi et al. (2023), *IRCoT* (ACL) |
| 25 | Referee | No thread exists for this paper. You write the first review, from the reviewer guidelines alone |
| 27 | Adversary | Wang (2026), *MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation* |
| 27 | Referee | The paper's ICLR 2026 review thread, on OpenReview |

Everyone holding the Referee role also reads the NeurIPS reviewer guidelines. Two pages, and it is what the role is being asked to do.

{{< /details >}}

{{< details "Pre-reading for project workshop 1, and reference texts" >}}

Session 9 will produce low agreement between judges, and these explain why that is a result rather than a failure.

- **Voorhees (2000), *Variations in relevance judgments and the measurement of retrieval effectiveness*** (IP&M). Required. TREC's own finding that judges disagree substantially yet system rankings stay stable.
- Zobel (1998), *How Reliable Are the Results of Large-Scale IR Experiments?* (SIGIR).
- Buckley & Voorhees (2004), *Retrieval Evaluation with Incomplete Information* (SIGIR).

**Reference text.** Manning, Raghavan & Schütze, *Introduction to Information Retrieval* (Cambridge University Press, 2008). Free online. The classical retrieval chapters cover sessions 2, 3, 5 and 7.

{{< /details >}}

{{< details "Further reading by topic" >}}

**Where knowledge sits, the classical lineage.** Weston, Chopra & Bordes (2014) *Memory Networks*; Graves et al. (2014) *Neural Turing Machines*; Graves et al. (2016) *DNC* (Nature); Lample et al. (2019) *Large Memory Layers with Product Keys*; Shazeer et al. (2017) *Outrageously Large Neural Networks*; Fedus, Zoph & Shazeer (2022) *Switch Transformers* (JMLR); Jiang et al. (2024) *Mixtral of Experts*; He (2024) *Mixture of a Million Experts*.

**Where knowledge sits, 2025 and 2026.** Berges et al. (2024) *Memory Layers at Scale*; Cheng et al. (2026) *Conditional Memory via Scalable Lookup* - the Engram paper, and session 21's anchor; Behrouz, Zhong & Mirrokni (2025) *Titans* (NeurIPS); Behrouz et al. (2025) *Nested Learning* (NeurIPS); Eyuboglu et al. (2025) *Cartridges*; Lin et al. (2025) *Continual Learning via Sparse Memory Finetuning*, which is the counter-example to this course's own argument that weights cannot forget.

**Attention as retrieval.** Wu et al. (2024) *Retrieval Head Mechanistically Explains Long-Context Factuality*, the empirical version of an analogy this course used to assert; Zhang & Bottou (2025) *Memory Mosaics at scale* (NeurIPS).

**Long context versus retrieval.** Liu et al. (2023) *Lost in the Middle* (TACL); Li et al. (2024) *Retrieval Augmented Generation or Long-Context LLMs?* (EMNLP).

**Dense retrieval, and one space for two jobs.** Reimers & Gurevych (2019) *Sentence-BERT* (EMNLP); Karpukhin et al. (2020) *DPR* (EMNLP); Ni et al. (2022) *Large Dual Encoders Are Generalizable Retrievers* (EMNLP); Muennighoff et al. (2024) *Generative Representational Instruction Tuning*; Zhang et al. (2024) *OneGen* (EMNLP Findings); Lee et al. (2025) *Gemini Embedding*; Zhang et al. (2025) *Qwen3 Embedding*.

**Retrieval that needs reasoning.** Su et al. (2025) *BRIGHT* (ICLR), session 13's anchor; Shao et al. (2025) *ReasonIR*.

**Multi-vector retrieval, and making it servable.** Khattab & Zaharia (2020) *ColBERT* (SIGIR); Santhanam et al. (2022) *ColBERTv2* (NAACL) and *PLAID* (CIKM); Dhulipala et al. (2024) *MUVERA* (NeurIPS); Veneroso et al. (2025) *CRISP*; Faysse et al. (2025) *ColPali* (ICLR).

**Nearest neighbour search and systems.** Malkov & Yashunin (2018) *HNSW* (TPAMI); Jégou, Douze & Schmid (2011) *Product Quantization*; Johnson, Douze & Jégou (2019) *Billion-scale similarity search with GPUs*.

**Learning to rank and click bias.** Burges (2010) *From RankNet to LambdaRank to LambdaMART*; Joachims et al. (2017) *Unbiased Learning-to-Rank with Biased Feedback* (WSDM); Craswell et al. (2008) *An Experimental Comparison of Click Position-Bias Models* (WSDM).

**Retrieval-augmented generation.** Lewis et al. (2020) *RAG*; Borgeaud et al. (2022) *RETRO*; Khandelwal et al. (2020) *kNN-LM* (ICLR); GraphRAG (2024); Gutiérrez et al. (2025) *From RAG to Memory* (ICML), which is HippoRAG 2.

**Agentic retrieval and deep research.** Yao et al. (2023) *ReAct*; Trivedi et al. (2023) *IRCoT* (ACL); Asai et al. (2023) *Self-RAG*; Jin et al. (2025) *Search-R1* (COLM), session 25's anchor; Chen et al. (2025) *BrowseComp-Plus*, which re-evaluates that literature on a fixed corpus and finds much smaller numbers; Liu, Zhang & Liang (2023) *Evaluating Verifiability in Generative Search Engines* (EMNLP Findings), on whether citations support the claims attached to them.

**Agent memory, and whether it can be measured.** Hu, Wang & McAuley (2026) *Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions* (ICLR), session 27's anchor; Wang (2026) *MemDelta*, on hidden confounds in that evaluation; Anthropic, *Effective context engineering for AI agents*, read critically as a primary source.

**Semantic search in practice.** Cormack, Clarke & Buettcher (2009) *Reciprocal Rank Fusion* (SIGIR); Formal et al. (2021) *SPLADE*; Nogueira et al., *doc2query*.

**Adversarial retrieval.** Greshake et al. (2023) *Not what you've signed up for* (AISec); Zou et al. (2024) *PoisonedRAG*.

**Commercial search.** Shah & Bender (2022) *Situating Search* (CHIIR), the strongest case against replacing search with language models, and worth reading precisely because this course argues the other way; Google's *How Search Works*, read critically as a primary source.

**Scholarly search and literature synthesis.** Lo et al. (2020) *S2ORC* (ACL); Swanson (1986) on literature-based discovery; Wang et al. (2024) *SciMON* (ACL); Asai et al. (2024) *OpenScholar*; Skarlinski et al. (2024) *PaperQA2*. This block lost its own lecture in the 2026 revision and is now read alongside session 24, because deep research and literature synthesis are the same problem.

{{< /details >}}

## 9. Logistics

**Language:** English

**Lecturer:** [Seong Joon Oh](/#members)

**Tutors:** To be announced.

**When:** Mondays and Wednesdays, 09:00-10:00. Sessions 9, 19 and 29 run 09:00-10:30.

**Where:** Online (Zoom), for every session. Joining details are circulated by email before the first session. Cameras are required in discussion groups and optional in plenary.

The course registration system lists a classroom at 양재산학캠퍼스 against both slots. **That room is not used.** Do not go there.

**Enrolment:** Capped at 40.

**Email:** `coallaoh@stai-lab.org` for submissions, questions, and feedback.

**Slack:** The course workspace carries announcements, the weekly roster, and questions. [Join here](https://join.slack.com/t/irai2026/shared_invite/zt-469u9zuz7-mMki5OXgvpkOKAsidUITHw).

**A note on time zones.** The Wednesday session cannot be missed and is not recorded. If 09:00 KST is unreasonable where you are, say so on the first-day survey, before groups are formed.
