+++
title = "Information Retrieval for AI"
semester = "Autumn Semester 2026"
university = "KAIST AI"
image = "irai-2026.png"
sort_position = 5
subtitle = "How AI systems reach the knowledge they do not hold"
description = "Model weights are a lossy, frozen compression of the world, so every serious AI system needs a way to reach the rest of it. This course teaches that path, from the inverted index of the 1970s to the research agents of 2026. The framing is information retrieval for AI, not AI for information retrieval. Classical retrieval is the toolkit rather than the subject, and BM25 earns its place not as history but because dense retrievers still lose to it out of domain. Monday is a lecture on the method. Wednesday is a structured discussion of a research paper that uses it. Alongside both, the class builds its own document collection, writes its own queries, judges relevance by hand, and measures a retrieval system against the judgements it produced itself."
+++

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

## 2. Prerequisites

- Familiarity with Python and PyTorch coding.
- Working knowledge of transformers and standard deep learning.
- Basic maths: linear algebra, probability, statistics.
- No prior background in information retrieval is required, and none is expected. The classical material in September will be the new material for most of this audience.

## 3. Two questions that run through the term

**From sparse to dense.** TF-IDF, BM25, learned sparse retrieval, bi-encoders, late interaction. A spectrum, not a succession.

**Where knowledge sits when the system runs.** One figure, redrawn every few weeks.

| Regime | Mechanism | Example |
|---|---|---|
| Parametric | All knowledge in weights, fixed compute | A dense LLM |
| Conditionally parametric | A router selects parameter blocks | Mixture of experts, memory layers |
| Semi-parametric | An index wired into the forward pass | kNN-LM, RETRO, memory networks |
| Non-parametric | A corpus placed into the prompt | Retrieval-augmented generation |
| Open world | A policy decides what to fetch | Search agents, deep research |

The course opens with attention itself as retrieval over the context, so the whole spectrum reads as one idea at different scales.

## 4. How the course runs

**Monday** is a lecture on the method. 45 minutes of content, 10 minutes of questions, 5 minutes on the following Wednesday.

**Wednesday** is a discussion of a research paper that uses it. Four Wednesdays are lectures instead.

### Groups and roles

Students are divided into fixed discussion groups of five, held all semester. Each member takes a different role for the week, and roles rotate. Every student holds each role at least once over the term.

| Role | The job | Supporting paper |
|---|---|---|
| Adversary | Attack the experiments, find the missing baseline | A paper that contradicts the assigned one |
| Historian | What came before, and what this paper quietly discards | The predecessor it builds on |
| Replicator | Check that the numbers support the claims, and measure something | A reproduction or a rerun |
| Extender | Propose the next paper and say what it would test | The successor, chosen by the extenders themselves |
| Applier | Would you deploy this, at what index size, latency and cost | A systems or deployment paper |

Note-taking is a duty rather than a role. Rotate it inside the group.

Everyone reads the assigned paper closely. Each student additionally consults one supporting paper chosen for their role - the abstract, the relevant table, the part bearing on their role. The supporting paper belongs to the role, not the group, so all students holding a role in a given week read the same one. They do not coordinate, and there is no joint deliverable.

One Wednesday therefore puts six papers into circulation: the assigned paper, read by everyone, and five supporting papers.

### The weekly written review

**One review per student, half a page, due 18:00 on Tuesday.** That is the entire weekly obligation outside class. Four fields.

**1. Model check.** Give a language model the assigned paper and the prompt for your role. Name the model and version, paste its answer in two or three lines, then say what it got wrong or missed.

| Role | Prompt |
|---|---|
| Adversary | "What are the three weakest points in this paper's experimental evidence?" |
| Historian | "What prior work does this build on, and what does it discard from that work?" |
| Replicator | "Do the numbers in the results tables support the claim in the abstract? What would I need to rerun this?" |
| Extender | "What experiment should come next, and what would it settle?" |
| Applier | "What would it cost to deploy this - index size, latency, serving?" |

**2. What you found, in your role this week.** The substantive point, and what would be needed to believe or refute it. This is the bulk of the page.

**3. A class-local hook.** One sentence tying the paper to something only a class member knows.

**4. One question for the class.** Something you cannot answer from the paper. Three are chosen to open Wednesday.

The half-page cap is deliberate. It holds the weekly load down and forces you to pick your best point rather than list five.

### The Wednesday hour

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

### End-of-session questions

Three questions, answered individually in the last two minutes.

1. Which role's point won in your group?
2. Name one point that was dropped, and why it lost.
3. What did you walk in believing was strongest? Did that change, and what changed it?

Question 2 can only be answered by someone who followed the argument. You read one supporting paper; the other four reach you only through the discussion. Question 3 is the only place the course pays for changing your mind.

### One student's week

| When | What | Time |
|---|---|---|
| Thu-Sun | Read the assigned paper properly | 1.2 h |
| Mon 09:00-10:00 | The lecture teaching the method | 1 h |
| Mon evening | Consult the supporting paper, run the model check | 30 min |
| Tue | Write the half-page review, submit by 18:00 | 20 min |
| Wed 09:00-10:00 | The session | 1 h |

**Four hours a week, two of them contact time.** There is no project work in a normal week. Three weeks are heavier - sessions 9, 19 and 29 add about two hours each.

## 5. Schedule

Sessions run 09:00-10:00, except the three project workshops, which run 09:00-10:30.

| # | Date | Content | Due |
|---|---|---|---|
| 1 | Mon 31 Aug | Why retrieval now. Eight arguments, the knowledge-location spectrum, course mechanics | - |
| 2 | Wed 02 Sep | The inverted index. Tokenisation, postings, compression. TF-IDF and the vector space model | - |
| 3 | Mon 07 Sep | BM25 and probabilistic ranking. Query likelihood, smoothing, relevance feedback | - |
| 4 | Wed 09 Sep | **Discussion.** Critically Examining the "Neural Hype" | Review, Tue 18:00 |
| 5 | Mon 14 Sep | Evaluation. MAP, MRR, nDCG. Pooling and its biases. TREC, BEIR, online evaluation | - |
| 6 | Wed 16 Sep | **Discussion.** BEIR. Launch of the class collection and judging protocol | Review, Tue 18:00 |
| - | 21-23 Sep | No class - Chuseok week | - |
| 7 | Mon 28 Sep | Web search anatomy. Crawling, freshness, indexing at scale, PageRank, HITS | - |
| 8 | Wed 30 Sep | **Discussion.** The Anatomy of a Large-Scale Hypertextual Web Search Engine | Review, Tue 18:00 |
| - | Mon 05 Oct | No class - substitute holiday | - |
| 9 | Wed 07 Oct | **Project workshop 1, 90 min.** Building a test collection. Protocol design, live judging, disagreement analysis. Project kickoff | Two queries per student, in session |
| 10 | Mon 12 Oct | Commercial search today, and what is wrong with it. The modern stack, who owns an index, eleven weaknesses | Three-engine query comparison, before class |
| 11 | Wed 14 Oct | Bi-encoders. SentenceBERT, DPR. Contrastive objectives, hard negatives, distillation | - |
| 12 | Mon 19 Oct | Late interaction and learned sparse retrieval. ColBERT, SPLADE. Hybrid retrieval and fusion. When semantic search hurts | - |
| 13 | Wed 21 Oct | **Discussion.** ColBERT | Review, Tue 18:00 |
| 14 | Mon 26 Oct | Retrieval uncertainty. Probabilistic embeddings. Ambiguity as underspecification. Cross-modal retrieval | - |
| 15 | Wed 28 Oct | **Discussion.** Probabilistic Embeddings for Cross-Modal Retrieval | Review, Tue 18:00 |
| 16 | Mon 02 Nov | Approximate nearest neighbour search. HNSW, IVF-PQ, product quantisation. Vector databases. The recall-latency curve | - |
| 17 | Wed 04 Nov | Attention as retrieval. Memory networks, Neural Turing Machines, DNC. Product-key memory layers | - |
| 18 | Mon 09 Nov | Mixture of experts, and where routing resembles retrieval. Where the analogy holds and where it breaks | - |
| 19 | Wed 11 Nov | **Project workshop 2, 90 min.** Complete the judging pass, analyse judge agreement, implement and measure your group's modification | Relevance judgements complete |
| 20 | Mon 16 Nov | Language models with an index attached. kNN-LM, RETRO. Where the gradient stops. Long context versus retrieval | - |
| 21 | Wed 18 Nov | **Discussion.** End-To-End Memory Networks | Review, Tue 18:00 |
| 22 | Mon 23 Nov | Retrieval-augmented generation. Pipelines and failure modes. Chunking, reranking. Corpus poisoning and prompt injection | - |
| 23 | Wed 25 Nov | Multi-turn retrieval. Query rewriting, clarifying questions. Answer engines and citation faithfulness | - |
| 24 | Mon 30 Nov | Agentic retrieval and deep research. IRCoT, Self-RAG, ReAct. Search-augmented reinforcement learning. Report synthesis | - |
| 25 | Wed 02 Dec | **Discussion.** Nearest Neighbor Language Models | Review, Tue 18:00 |
| 26 | Mon 07 Dec | AI for science. Literature-based discovery. Citation recommendation. Hypothesis generation. Novelty versus correctness | - |
| 27 | Wed 09 Dec | **Discussion.** OpenScholar | Review, Tue 18:00 |
| 28 | Mon 14 Dec | Privacy, personalisation and unlearning. Adversarial retrieval and SEO. Why an index can forget and weights cannot | - |
| 29 | Wed 16 Dec | **Project workshop 3, 90 min.** Group presentations, review of the class record of model failures, and the closing answer to session 1 | Write-up due 09 Dec, 23:59 |

Wednesday sessions are not recorded, so that criticism stays candid. Monday lectures are recorded.

## 6. The class test collection and the project

### Why the class builds its own test collection

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

### The project

> You are given a BM25 baseline over the class collection, an evaluation harness, and the class relevance judgements. **Make one change to the retrieval pipeline.** Predict its effect before you write any code. Measure it. Explain the gap between what you predicted and what happened.

| Fixed | Yours to change |
|---|---|
| The collection, the relevance judgements, the metrics, the harness | Anything between the query and the ranked list |

Groups claim one modification each at session 9, so that no two duplicate. The menu:

- Hybrid BM25 and dense retrieval, fused with reciprocal rank fusion
- A different bi-encoder checkpoint
- doc2query expansion over the collection
- An LLM reranker over the top ten
- Chunking papers into sections instead of indexing whole documents
- ColBERT late interaction

**Deliverables.** A run file (`query_id, doc_id, rank, score`), a one-page write-up due a week before session 29, and an eight-minute presentation.

**The relevance judgements freeze at session 19.** Groups may keep refining afterwards, and should report both their session-19 number and any later one.

**Compute is a laptop.** Fifty documents and sixty queries. Encoding with a small sentence transformer takes seconds on Colab's free CPU tier, and ColBERT inference over 48 documents runs on CPU. No compute credits are needed and no paid account is required, including for the weekly model check.

## 7. Assessment

| Component | Weight |
|---|---|
| Weekly paper reviews | 45% |
| End-of-session questions | 20% |
| Contribution to discussion | 10% |
| Project | 25% |
| **Total** | **100%** |

There is no exam and there are no quizzes.

**Two participation requirements**: writing queries, and completing your relevance judgements. More than two missed obligations across the term drops the final grade by one band.

### Weekly paper reviews (45%)

Eight reviews, one per discussion session. A random four are marked on the scale below and the rest on completion. You will not know in advance which count.

| Score | What it means |
|---|---|
| 4 | Found something real that changes how the paper should be read, or a model failure new to the class record |
| 3 | A substantive point the model check did not already contain |
| 2 | Competent, correct, adequate. The expected mark |
| 1 | Thin, or restates the model's output |
| 0 | Missing, fabricated numbers, or undeclared model use |

### End-of-session questions (20%)

Eight sets of three questions, scored against your group's filed conclusion. Question 1 and question 3 are checked mechanically. Question 2 passes if it names a point actually raised in your group.

### Contribution to discussion (10%)

Scored 0-2 whenever you are named to speak in plenary, either to defend your group's conclusion or to answer a question during synthesis. Opportunities are tracked and allocated so that every student is called roughly three times.

| Score | For |
|---|---|
| 2 | Answered the question actually asked, with a reason, and either held up under the follow-up or conceded cleanly |
| 1 | Answered, but restated the conclusion or your own review without engaging the challenge |
| 0 | Could not answer, or absent |

Marks go to the response to challenge. Not to fluency, and not to being right.

### Project (25%)

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

### Grades

Grades are assigned by ranking the class and cutting bands, with a target of roughly even distribution across A+, A0, A-, B+ and B0.

**A student who does all of the work competently lands in the middle of the distribution, not at the top.** On the review scale above, "did the work adequately" is a 2, not a 4. This is stated here rather than discovered in December.

| Grade | Profile |
|---|---|
| A+ | Reviews that found something real more than once. A project that beat the baseline for a defensible reason |
| A0 | Consistently sharp reviews, holds up when called on, strong project |
| A- | Good work throughout, one or two standout contributions |
| B+ | All the work done competently. Nothing missing, nothing exceptional |
| B0 | Work done but thin in places |
| B- | Repeated gaps, or reviews showing the paper was not read |
| F | Non-participation |

## 8. Generative AI policy

**Use is expected, declared and marked.** The course does not defend against it. Detection does not work, and a ban would be absurd in a course about retrieval-augmented systems.

**Credit begins above what a model gives you.** Everything a model produces is free, so a review that restates the model's output scores low even when it is correct. A 3 requires a point the model check did not already contain. This removes any incentive to conceal.

**The bright line: any number in a submitted review must be reproducible from a submitted log.** Fabrication scores zero on that review, no argument. This is not an AI rule. It is the research norm, and it would have applied in 1996.

Undeclared model use scores zero on that submission.

The weekly model check is where this becomes concrete. Each role's task needs a capability that is weak in a different way.

| What you ask for | What tends to come back |
|---|---|
| Ten objections to this paper | Fluent objections that dissolve on contact. The skill is triage |
| The paper's lineage | Hallucinated citations |
| A rerun script | Code that runs and computes the wrong thing |
| Next experiments | Generic, hedged, unfalsifiable proposals |
| Index size and cost | Confident bad arithmetic |

Every review contributes one line to a class record of model failures - model, version, paper type, failure observed, how it was caught. It is reviewed at sessions 19 and 29. The interesting question is which failures disappear as models improve during the term, and nobody knows that in advance.

The instructor prepares lecture material with model assistance and adds the model's mistakes to the same record.

## 9. Reading list

### The eight assigned papers

| # | Session | Paper |
|---|---|---|
| 1 | 4 (9 Sep) | Yang, Lu & Lin (2019), *Critically Examining the "Neural Hype"* (SIGIR) |
| 2 | 6 (16 Sep) | Thakur et al. (2021), *BEIR* (NeurIPS Datasets and Benchmarks) |
| 3 | 8 (30 Sep) | Brin & Page (1998), *The Anatomy of a Large-Scale Hypertextual Web Search Engine* (WWW) |
| 4 | 13 (21 Oct) | Khattab & Zaharia (2020), *ColBERT* (SIGIR) |
| 5 | 15 (28 Oct) | Chun et al. (2021), *Probabilistic Embeddings for Cross-Modal Retrieval* (CVPR) |
| 6 | 21 (18 Nov) | Sukhbaatar et al. (2015), *End-To-End Memory Networks* (NeurIPS) |
| 7 | 25 (2 Dec) | Khandelwal et al. (2020), *Generalization through Memorization: Nearest Neighbor Language Models* (ICLR) |
| 8 | 27 (9 Dec) | Asai et al. (2024), *OpenScholar* |

Three notes on the choices. Session 4 opens with a paper whose whole argument is that other people's baselines were weak, which sets the tone. Session 15 is the instructor's own paper, and that is deliberate - six students attacking it in front of the author settles the question of whether criticism is welcome. Sessions 21 and 25 pair a dead idea with the successor that beat it, given to the adversary, so the argument happens inside the groups.

### Supporting papers

Supporting papers for the first four discussion sessions are below. The rest are published two weeks before each session. Extenders choose their own.

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
| 8 | Adversary | Kleinberg (1999), *HITS* |
| 8 | Historian | Garfield (1955), *Citation Indexes for Science* |
| 8 | Replicator | Langville & Meyer (2004), *Deeper Inside PageRank* |
| 8 | Applier | Dean & Ghemawat (2004), *MapReduce* |
| 13 | Adversary | Hofstätter et al. (2021), *Balanced Topic Aware Sampling* (TAS-B) |
| 13 | Historian | Karpukhin et al. (2020), *DPR* |
| 13 | Replicator | Santhanam et al. (2022), *ColBERTv2* (NAACL) |
| 13 | Applier | Santhanam et al. (2022), *PLAID* (CIKM) |

### Pre-reading for project workshop 1

Session 9 will produce low agreement between judges, and these explain why that is a result rather than a failure.

- **Voorhees (2000), *Variations in relevance judgments and the measurement of retrieval effectiveness*** (IP&M). Required. TREC's own finding that judges disagree substantially yet system rankings stay stable.
- Zobel (1998), *How Reliable Are the Results of Large-Scale IR Experiments?* (SIGIR).
- Buckley & Voorhees (2004), *Retrieval Evaluation with Incomplete Information* (SIGIR).

### Reference texts

Manning, Raghavan & Schütze, *Introduction to Information Retrieval* (Cambridge University Press, 2008). Free online. The classical retrieval chapters cover sessions 2, 3, 5 and 7.

### Further reading by topic

**Where knowledge sits.** Weston, Chopra & Bordes (2014) *Memory Networks*; Graves et al. (2014) *Neural Turing Machines*; Graves et al. (2016) *DNC* (Nature); Lample et al. (2019) *Large Memory Layers with Product Keys*; Shazeer et al. (2017) *Outrageously Large Neural Networks*; Fedus, Zoph & Shazeer (2022) *Switch Transformers* (JMLR); Jiang et al. (2024) *Mixtral of Experts*; He (2024) *Mixture of a Million Experts*; Berges et al. (2024) *Memory Layers at Scale*.

**Long context versus retrieval.** Liu et al. (2023) *Lost in the Middle* (TACL); Li et al. (2024) *Retrieval Augmented Generation or Long-Context LLMs?* (EMNLP).

**Nearest neighbour search and systems.** Malkov & Yashunin (2018) *HNSW* (TPAMI); Jégou, Douze & Schmid (2011) *Product Quantization*; Johnson, Douze & Jégou (2019) *Billion-scale similarity search with GPUs*.

**Learning to rank and click bias.** Burges (2010) *From RankNet to LambdaRank to LambdaMART*; Joachims et al. (2017) *Unbiased Learning-to-Rank with Biased Feedback* (WSDM); Craswell et al. (2008) *An Experimental Comparison of Click Position-Bias Models* (WSDM).

**Retrieval-augmented generation.** Lewis et al. (2020) *RAG*; Borgeaud et al. (2022) *RETRO*; GraphRAG (2024); Search-R1 (2025); Asai et al. (2023) *Self-RAG*; Trivedi et al. (2023) *IRCoT*; Yao et al. (2023) *ReAct*.

**Multi-turn retrieval.** Radlinski & Craswell (2017) *A Theoretical Framework for Conversational Search* (CHIIR); Elgohary, Peskov & Boyd-Graber (2019) *CANARD* (EMNLP); Anantha et al. (2021) *QReCC* (NAACL); the TREC CAsT overviews; Aliannejadi et al. (2019) *Asking Clarifying Questions* (SIGIR); Zamani et al. (2023) *Conversational Information Seeking*.

**Answer engines.** Liu, Zhang & Liang (2023) *Evaluating Verifiability in Generative Search Engines* (EMNLP Findings). Measures whether citations actually support the claims attached to them, and finds they often do not.

**Semantic search in practice.** Cormack, Clarke & Buettcher (2009) *Reciprocal Rank Fusion* (SIGIR); Formal et al. (2021) *SPLADE*; Nogueira et al., *doc2query*.

**Adversarial retrieval.** Greshake et al. (2023) *Not what you've signed up for* (AISec); Zou et al. (2024) *PoisonedRAG*.

**Commercial search.** Shah & Bender (2022) *Situating Search* (CHIIR), the strongest case against replacing search with language models, and worth reading precisely because this course argues the other way; Google's *How Search Works*, read critically as a primary source.

**Scholarly search and AI for science.** Lo et al. (2020) *S2ORC* (ACL); Swanson (1986) on literature-based discovery; Wang et al. (2024) *SciMON* (ACL); Skarlinski et al. (2024) *PaperQA2*.

## 10. Communication and logistics

**Language:** English

**Lecturer:** [Seong Joon Oh](/#members)

**Tutors:** To be announced.

**When:** Mondays and Wednesdays, 09:00-10:00. Sessions 9, 19 and 29 run 09:00-10:30.

**Where:** Online (Zoom), for every session. Joining details are circulated by email before the first session. Cameras are required in discussion groups and optional in plenary.

The course registration system lists a classroom at 양재산학캠퍼스 against both slots. **That room is not used.** Do not go there.

**Enrolment:** Capped at 40.

**Email:** `coallaoh@stai-lab.org` for submissions, questions, and feedback.

**A note on time zones.** The Wednesday session cannot be missed and is not recorded. If 09:00 KST is unreasonable where you are, say so on the first-day survey, before groups are formed.
