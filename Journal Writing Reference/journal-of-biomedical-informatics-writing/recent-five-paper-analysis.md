# Recent JBI paper analysis: reusable writing skill

**Source folder:** `E:\Defense\Discuss\Biomedical Informatics - Referances`  
**Analysis date:** 1 September 2026  
**Target journal:** *Journal of Biomedical Informatics* (JBI), Elsevier

This file converts the five supplied recent JBI papers into a practical
manuscript-writing skill. It is a style and reporting analysis, not a claim that
the five papers define a mandatory author limit. Exact word limits, article
types and display-item limits must still be checked in JBI's live Guide for
Authors immediately before submission.

## 1. Cross-paper measurements

The word counts below were obtained from the structured abstract and the PMC
full-text XML/BioC records corresponding to the supplied PDFs. Main-text counts
are approximate narrative-word counts (Introduction through Conclusion); table,
figure-caption, reference and publisher-boilerplate text are excluded where the
XML permits. PDF extraction can differ by a few percent because of hyphenation,
equations and captions.

| Paper | Final publication | PDF pages | Abstract words | Main narrative words (approx.) | Keywords | Main figures | Main tables | Graphical abstract | Main contribution |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| Zhuang et al., semantic-guided VLM | 2025, vol. 172, 104947 | 25 | 289 | ~6,000 | 4 | 3 (plus appendix) | 5 (plus appendix) | No | CLIP guided by radiologist semantic features for lung-nodule risk prediction |
| Smith et al., ImageVU | 2025, vol. 170, 104905 | 25 | 256 | ~5,930 | 9 | 3 | 4 | No | Scalable, compliant infrastructure for secondary radiological-data use |
| Lotspeich et al., whole-person EHR | 2025, vol. 170, 104904 | 29 | 295 | ~5,470 | 7 (plus supplement) | 1 (plus supplement) | Yes | Enriched validation and targeted sampling for an EHR phenotype |
| Mopidevi et al., MedVidDeID | 2025, vol. 170, 104901 | 22 | 266 | ~4,970 | 5 | 3 | 2 | No | Six-stage multimodal clinical-video de-identification pipeline |
| Xu et al., perplexity and proximity | 2025, vol. 170, 104899 | 28 | 300 | ~6,180 | No keyword block detected | 5 | 3 | No | LLM perplexity combined with embedding proximity for coherence assessment |

These are article-text estimates rather than a publisher-imposed range. The
important pattern is that JBI papers in this set are substantial, method-rich
articles of roughly 5,000-6,200 narrative words, with longer appendices or
supplementary material when needed.

## 2. Source records and lawful full text

The five local PDFs are author manuscripts marked as JBI publications and carry
open licences. The corresponding free full text is available through PMC:

1. [Zhuang et al., 104947 - PMC13283286](https://pmc.ncbi.nlm.nih.gov/articles/PMC13283286/) and [DOI](https://doi.org/10.1016/j.jbi.2025.104947)
2. [Smith et al., 104905 - PMC13275161](https://pmc.ncbi.nlm.nih.gov/articles/PMC13275161/) and [DOI](https://doi.org/10.1016/j.jbi.2025.104905)
3. [Lotspeich et al., 104904 - PMC13126318](https://pmc.ncbi.nlm.nih.gov/articles/PMC13126318/) and [DOI](https://doi.org/10.1016/j.jbi.2025.104904)
4. [Mopidevi et al., 104901 - PMC13162565](https://pmc.ncbi.nlm.nih.gov/articles/PMC13162565/) and [DOI](https://doi.org/10.1016/j.jbi.2025.104901)
5. [Xu et al., 104899 - PMC13222020](https://pmc.ncbi.nlm.nih.gov/articles/PMC13222020/) and [DOI](https://doi.org/10.1016/j.jbi.2025.104899)

Licensing varies: the first four supplied manuscripts state CC BY; Xu et al.
states CC BY-NC-ND. Check the individual licence before redistributing a PDF or
reusing a figure.

## 3. JBI writing DNA

### 3.1 Title construction

The titles are informative rather than decorative. They normally contain:

- the methodological object or named system;
- the clinical/informatics problem; and
- the task, outcome or operational setting.

Examples include a named pipeline followed by its function (MedVidDeID), a
named infrastructure followed by its approach (ImageVU), or a paired-method
title that states the complementarity being tested (perplexity and proximity).
For MedVision, retain a specific audit concept and the biomedical-informatics
problem in the title. Avoid vague titles such as "A Novel AI Model".

### 3.2 Front matter and abstract

Four papers use the structured labels **Objective, Methods, Results,
Conclusion**. Xu et al. uses **Objective, Method, Results, Conclusion**. The
abstracts are approximately 256-300 words in the supplied final manuscripts.

Use this four-part pattern:

1. **Objective (about 60-85 words):** establish the clinical/informatics risk,
   identify the unresolved limitation, and state the study aim.
2. **Methods (about 80-115 words):** give cohort/data scale, core method or
   pipeline stages, comparator or validation design, and the main endpoint.
3. **Results (about 50-85 words):** report the principal numerical result,
   external/held-out performance or operational gain, and the relevant
   uncertainty or comparison.
4. **Conclusion (about 35-55 words):** state what the method demonstrates,
   its practical value, and an appropriately bounded implication.

Do not put a literature review, broad claims, or implementation promises in the
abstract. Define every important acronym at first use. Include one or two
numbers that allow a reader to judge scale and effect. If code is available,
one short availability sentence may appear in the conclusion, as in Zhuang et
al.

### 3.3 Keywords

Most papers provide a short semicolon-separated keyword line. The observed
range is 4-9 terms. Use 5-8 terms for MedVision, mixing:

- the domain (medical imaging, clinical informatics);
- the data/provenance concept (MIMIC-CXR, report-derived labels);
- the method (vision-language model, modality audit, image contribution);
- the evaluation concept (shortcut learning, calibration, label circularity).

Avoid repeating the full title word-for-word and avoid unexplained internal
abbreviations. Xu et al. is an exception with no keyword block in the supplied
manuscript; for a new submission, following the keyword convention is safer.

### 3.4 Significance box

Zhuang, Smith, Lotspeich, Mopidevi and Xu include a compact **Statement of
Significance** or equivalent. It answers, in a small table or labelled block:

- What is the problem or issue?
- What is already known?
- What does this paper add?
- Who benefits from the knowledge? (included in several papers)

This is particularly useful for MedVision because it forces the paper to state a
generalizable informatics contribution rather than only a model score.

## 4. Section architecture extracted from the five papers

### 4.1 Introduction

The introduction is usually 4-6 narrative paragraphs followed by a concise
aim/contribution statement. The recurring progression is:

1. clinical or operational importance;
2. what current computational/infrastructure approaches do;
3. the specific limitation, risk or reproducibility gap;
4. why the proposed informatics method addresses that gap; and
5. explicit study aim and contributions.

Zhuang and Xu add a Related work section inside the introductory part. Smith
uses a short Introduction followed by the significance box. Do not turn the
introduction into a catalogue of citations; each citation should support a
claim, limitation or design choice.

### 4.2 Related work

When present, Related work is organized by method or modality, not by a paper-
by-paper list. The Zhuang paper uses imaging-based prediction, semantic-guided
feature learning and vision-language models. Mopidevi uses text, audio, video
and integrated privacy approaches. End each subsection with the unresolved gap
that motivates the present method.

For MedVision, a compact organization is preferable:

- report and label provenance in medical imaging;
- multimodal shortcut/modality bias and debiasing;
- direct modality-contribution and calibration audits; and
- the unresolved problem of report-label circularity.

### 4.3 Methods

JBI methods are modular and auditable. A reader should be able to reproduce the
data flow without inferring hidden steps. The five papers use the following
recurring order:

1. **Data or system setting:** source, inclusion/exclusion, scale, governance,
   and the unit of analysis.
2. **Preprocessing or infrastructure:** transformations, de-identification,
   feature construction, missingness handling, or data routing.
3. **Core method:** architecture, pipeline stages, equations or decision rules.
4. **Training/estimation:** objective, hyperparameters, compute, model
   selection and reproducibility controls.
5. **Evaluation design:** primary endpoint, comparators, held-out/external
   validation, ablations, uncertainty and statistical tests.

Use descriptive subheadings. The supplied papers range from a few broad
subsections to detailed stage-by-stage headings; subheadings are justified when
they make a reproducible operation easier to locate, not merely to increase the
section count.

### 4.4 Results

Results follow the Methods order. A typical sequence is:

- cohort/data quality and descriptive characteristics;
- primary endpoint or main system performance;
- secondary analyses (explainability, calibration, efficiency or robustness);
- ablation/comparator results;
- error analysis or failure cases.

Each subsection begins with the result, then points to a table or figure, then
gives a restrained interpretation. Avoid repeating every table value in prose.
Report denominators, confidence intervals or standard deviations, and the
validation split whenever relevant.

### 4.5 Discussion

The papers use Discussion to interpret mechanisms and deployment meaning, not to
repeat Results. A strong pattern is:

1. one paragraph summarizing the central finding;
2. comparison with prior work or the expected mechanism;
3. clinical/informatics implications;
4. limitations and threats to generalizability; and
5. a concrete future-study or implementation path.

Xu explicitly separates key findings, the unique contribution of the method,
complementarity of feature sets, and implications/limitations. This is a useful
template for explaining modality inertia and label circularity without
overclaiming causality.

### 4.6 Conclusion

Conclusions are short (usually one focused paragraph). State the method, the
main empirical result and the bounded implication. Do not introduce a new
experiment, citation cluster or unqualified clinical claim.

### 4.7 End matter

The supplied papers consistently use a CRediT authorship statement and a
Declaration of competing interest. Acknowledgments are common. Data/code
availability appears when the study can disclose it; infrastructure papers may
describe access restrictions instead. Include, as applicable:

- ethics/IRB or data-use statement;
- data availability and access conditions;
- code and model/checkpoint availability;
- funding;
- competing interests;
- CRediT roles; and
- generative-AI disclosure required by the publisher.

## 5. Figures, tables and supplementary material

### 5.1 Figure strategy

The common JBI pattern is a small number of purposeful figures, not decorative
graphics:

- one end-to-end workflow or architecture figure;
- one cohort/data-flow or system architecture figure when applicable;
- one or more primary-result plots with uncertainty;
- one robustness, ablation, explainability or error-analysis figure.

Captions are self-contained: define abbreviations, identify the sample or seed
unit, state what error bars represent, and explain color/line encodings. Refer to
each figure in the Results text before it appears. Put additional diagnostics in
the supplement rather than shrinking the main figure until labels are unreadable.

For MedVision, the workflow/cohort flow, ICM with the TOST band, paired
VLM-versus-control plot, gate-stagnation plot and calibration plot form a
coherent primary visual set. The architecture schematic is useful only if it
clarifies where each variant attaches.

### 5.2 Table strategy

Tables in these papers carry auditable quantities:

- cohort or system inventory;
- metric definitions and primary performance;
- subgroup, ablation or validation comparisons;
- implementation/tool inventory; and
- supplementary hyperparameters or sensitivity analyses.

Use one decimal precision convention, state `mean (SD)` or `mean (95% CI)` in
the header/footnote, and define every abbreviation below the table. A table
should answer a question; do not duplicate an entire paragraph of Results.

### 5.3 Supplementary material

Supplementary figures/tables are used for extended ablations, sensitivity
analyses, additional cohorts, detailed tool lists and implementation details.
Keep the main article understandable without opening the supplement and cite
each supplementary item at its first relevant mention.

## 6. Statistical and reproducibility cues to adopt

Across the five papers, accepted-style reporting consistently makes the
evaluation unit visible. For MedVision this means:

- state whether inference is paired by seed or study;
- never pool repeated subjects across seeds as independent observations;
- report the primary endpoint before secondary metrics;
- include confidence intervals, variability and denominators;
- distinguish exploratory analyses from pre-registered/confirmatory analyses;
- describe comparator construction and checkpoint selection;
- provide enough hyperparameters and software details to reproduce the run; and
- explain missing outputs rather than replacing them with zero.

The newer papers also make external validation, error analysis, data provenance,
privacy, and operational constraints explicit. These are high-value signals for
a methodology-focused JBI reviewer.

## 7. How to apply this skill to MedVision

Recommended compact structure:

1. Introduction plus a four-row Statement of Significance.
2. Related work grouped by provenance/circularity, shortcuts, multimodal bias,
   and direct contribution auditing.
3. Methods: data and label provenance; model/variants; training and checkpoint
   rules; ICM and control construction; gate extraction; calibration; and
   seed-level statistical plan.
4. Results: cohort flow; baseline performance; gate stagnation; ICM/TOST and
   paired control; calibration; variant/failure analysis; and sensitivity/error
   analysis.
5. Discussion: mechanism, implications, limitations, and regulator-facing
   future design.
6. Conclusion and complete reporting statements.

Target approximately 5,500-6,500 narrative words for the main article unless
the live JBI guide or the editor gives a different instruction. Put exhaustive
per-seed values, provenance manifests and extended diagnostics in the
Supplementary Material. This is a working target derived from the supplied
papers, not an official limit.

## 8. Reviewer-facing pre-submission checklist

- [ ] The title names the informatics problem and the generalizable audit method.
- [ ] Objective/Methods/Results/Conclusion abstract is 250-300 words or within
      the live JBI limit.
- [ ] Five to eight keywords are defined and searchable.
- [ ] Statement of Significance identifies the problem, known evidence, added
      contribution and beneficiaries.
- [ ] Every claim has a matching experiment, table, figure or citation.
- [ ] Cohort flow, exclusions, denominators and label provenance are explicit.
- [ ] Seed-level pairing, uncertainty and statistical independence are correct.
- [ ] Missing ECE/Brier outputs are marked as unavailable, never silently set to
      zero.
- [ ] Variant origins, post-hoc extensions, checkpoint rules and merge/source
      provenance are disclosed.
- [ ] Figure captions define abbreviations, error bars and aggregation units.
- [ ] Tables use consistent precision and include definitions/footnotes.
- [ ] Data/code, ethics, funding, conflict, CRediT and AI statements are
      complete and factually accurate.
- [ ] Main text is concise; extended audits are moved to supplementary files.

