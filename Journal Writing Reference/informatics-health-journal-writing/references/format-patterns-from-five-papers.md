# Informatics and Health: Patterns Observed in Five Local Papers

**Source folder:** `E:\Defense\Discuss\Journal Writing Reference`  
**Purpose:** This is a local style analysis, not the journal's official Guide for Authors. It records recurring patterns that can inform the MedVision manuscript.

## Source inventory

| Local file | Article type | Authors / year | Pages | Main structure | Observed abstract pattern |
|---|---|---|---:|---|---|
| `1-s2.0-S2949953426000305-main.pdf` | Review | Mohamed Mustaf Ahmed et al., 2026 | 14 | Introduction; data ecosystem; model families; applications; clinical impact; ethics/legal/social; implementation; future directions; conclusion | Narrative review with problem, evidence, governance, and practical agenda; approximately 240 words |
| `2. 1-s2.0-S2949953426000317-main.pdf` | Full Length Article | Kazi Tanvir et al., 2026 | 19 | Introduction; literature review; methodology; results; conclusion; clinical significance; limitations/future work | Background, Methods, Findings, Interpretation; emphasizes model, resampling, feature selection, XAI, and benchmark comparison |
| `3. 1-s2.0-S2949953426000299-main.pdf` | Full Length Article | Muhammad Ashad Kabir et al., 2026 | 14 | Introduction; materials and methods; results; discussion; conclusions | Background, Methods, Findings, Interpretation; gives cohort size, CV design, tasks, best model, and SHAP findings |
| `4. 1-s2.0-S2949953425000141-main.pdf` | Perspective | Nalan Karunanayake, 2025 | 11 | Introduction; agentic-AI significance; challenges/recommendations; future directions; conclusion | Broad problem framing, opportunities, governance risks, and forward-looking interpretation; approximately 210 words |
| `5. 1-s2.0-S2949953425000311-main.pdf` | Full Length Article | Muhammad Minoar Hossain et al., 2025 | 15 | Introduction (background, existing works, gap, contributions); materials/methodology; results; discussion; conclusion | Background, Methods, Findings, Interpretation; reports preprocessing, model comparisons, external validation, and significance testing; approximately 265 words |

## Shared publication-layout pattern

All five PDFs are final Elsevier/ScienceDirect typeset articles. The first page commonly contains:

1. Article type (Review, Perspective, or Full length article).
2. Descriptive title.
3. Full author list with affiliation markers and corresponding-author symbol.
4. Affiliations.
5. An `ARTICLE INFO` block with keywords and, where relevant, a dataset link.
6. A structured or semi-structured abstract.
7. The beginning of the Introduction.
8. DOI, received/revised/accepted/published dates, copyright/license, and journal metadata.

The final PDFs use a compact two-column layout, numbered headings, numbered references, captioned figures/tables, and restrained black/blue typography. This is production layout and should not be mistaken for a submission-page or word-limit rule.

## What appears to help readability and reviewability

### 1. Make the gap visible

The strongest full-length examples do not leave the gap implicit. Tanvir et al. use `Research motivation and identified gap`; Hossain et al. use `Research gap` followed by `Prime contributions`. MedVision should similarly state:

- what current MIMIC-CXR VLM evaluations measure;
- why report-derived labels plus report inputs create a circularity risk;
- why text-debiasing does not necessarily establish image reliance;
- which controlled audit and statistical tests resolve the gap.

### 2. Explain novelty as a reproducible design

The papers emphasize a pipeline rather than a vague claim of novelty. Contributions should name the concrete design choice and its test: for example, report-preserving image ablation, image replacement, ICM with a prespecified equivalence margin, checkpoint-based gate extraction, and seed-aware inference.

### 3. Keep methods operational

The full-length papers break Methods into small numbered subsections. Common useful subsections are Dataset, Data Preparation/Preprocessing, Feature Selection or Optimization, Model/Classifier, Performance Metrics, Explainability, Experimental Setup, and Statistical Testing. This makes the work easier to reproduce and gives reviewers a place to check leakage, imbalance, and validation.

### 4. Report more than one headline score

The experimental papers use class-sensitive metrics and model comparisons rather than accuracy alone. Depending on the task, they include balanced accuracy, precision/recall, F1, AUROC, Brier score, calibration, cross-validation, significance tests, and external validation. For MedVision, the primary audit outcome should be separated from secondary model-performance metrics.

### 5. Tie explainability to a question

Tanvir et al. organize SHAP, LIME, partial-dependence plots, anchor rules, ELI5, and surrogate trees as separate results subsections. Kabir et al. use SHAP for both population and individual interpretation. The lesson is not to add every XAI tool; it is to state what each tool is intended to reveal and what it cannot establish. For MedVision, Grad-CAM is illustrative and should not be presented as causal proof without intervention evidence.

### 6. Separate Results, Discussion, and clinical significance

The full-length papers first report measurements, then interpret them. Tanvir et al. include `Discussion`, `Clinical significance`, and `Limitations and future work`; Kabir et al. separate `Insights and observations`, `Clinical validation`, `Limitations`, and `Future directions`. MedVision should use this separation to prevent speculative clinical language from appearing as a result.

### 7. State limitations explicitly

The accepted-paper pattern is to name dataset scope, sample size, validation design, model assumptions, and future validation needs. For MedVision, this must include same-report label circularity, lack of independent radiologist labels, single-dataset evaluation, no external validation, pretraining overlap, post-hoc seed extensions, and the statistical unit used for each test.

## Recommended MedVision manuscript blueprint

### Front matter

- Specific title.
- Authors, affiliations, corresponding author.
- 4–7 keywords chosen from the actual paper: medical vision-language model, MIMIC-CXR, label circularity, shortcut learning, image grounding, multimodal fusion, clinical AI audit.
- Structured abstract following the live journal requirement.

### 1. Introduction

- Clinical role of chest radiography and multimodal AI.
- Report-derived weak labels and the paired report input.
- Shortcut/unimodal-bias problem.
- Why performance, consistency, and gate values are insufficient on their own.
- Explicit research gap.
- Three to five numbered contributions.

### 2. Related Work

- Medical VLP and CXR models.
- Shortcut learning and text priors.
- Labeler noise and report-text bias.
- Debiasing/fusion strategies.
- Grounding and causal audit methods.

### 3. Materials and Methods

- Study design, dataset version, cohort flow, eligibility.
- CheXpert label construction and uncertainty policy.
- Patient-level split and test-subject alignment.
- Image/text preprocessing and encoder provenance.
- Baseline VLM, image-only, text-only, gray-square, and intervention variants.
- ICM definition, TOST/SESOI, confidence intervals, seed-level inference, multiplicity correction.
- Checkpoint/merge provenance and reproducibility.

### 4. Results

- Cohort counts and class distribution.
- Baseline and variant performance by seed.
- Primary ICM and equivalence result.
- Properly paired secondary tests.
- Calibration only where probability outputs exist.
- Gate values extracted directly from each checkpoint.
- Robustness and failure analysis.

### 5. Discussion

- Main finding in one paragraph.
- Relation to the closest medical-VLM grounding work.
- What debiasing did and did not change.
- Implication for reporting and deployment evaluation.
- Limitations and future validation.

### 6. Conclusion

- One paragraph: the empirical finding, its scope, and the required evaluation practice.

## Figure and table plan

These are recommendations, not mandatory journal requirements:

| Item | Purpose | Minimum caption information |
|---|---|---|
| Figure 1 | Cohort and split flow | number of subjects/studies, exclusions, train/validation/test units |
| Figure 2 | Model plus audit interventions | image/text paths, gray-square/image-swap operation, train vs test intervention |
| Table 1 | Cohort and class distribution | unit of analysis, class counts, split policy |
| Table 2 | Main model comparison | mean ± SD/CI, seed count, metric definitions, N/A policy |
| Figure 3 | ICM and equivalence | prespecified margin, CI, test unit, TOST interpretation |
| Figure 4 | Gate behavior | real checkpoint extraction, seed labels, initialization and bounds |
| Figure 5 | Calibration/ROC | probability availability, class/one-vs-rest definition, CI method |
| Figure 6 | Failure or qualitative audit | case selection rule, no causal overinterpretation |

## Style decisions to carry forward

- Use numbered headings and numbered citations consistent with the journal's Elsevier output style.
- Define abbreviations at first use and keep names stable throughout.
- Put the numerical result before the interpretation.
- Use “supports”, “is consistent with”, and “suggests” when evidence is observational or audit-based.
- Reserve “demonstrates” for a result directly established by the stated design.
- Avoid repeating the same claim in Abstract, Results, Discussion, and Conclusion with only word substitutions.
- Avoid promotional language and generic AI phrasing.
- Keep captions self-contained and cite every figure/table in the main text.

## What cannot be inferred from these five papers

The PDFs do not establish the current official word limit, page limit, required highlights, graphical-abstract rule, LaTeX/Word submission preference, cover-letter requirements, or mandatory reporting checklist. Those must be checked against the live *Informatics and Health* Guide for Authors immediately before submission.

