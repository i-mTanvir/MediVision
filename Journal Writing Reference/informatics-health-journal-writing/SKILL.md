---
name: informatics-health-journal-writing
description: Draft, revise, and audit health-informatics manuscripts for Informatics and Health and similar Elsevier journals, using the locally analyzed paper patterns while separating observed style from official author requirements.
metadata:
  short-description: Informatics and Health manuscript writing and structure
---

# Informatics and Health Journal Writing

Use this skill when preparing the user's MedVision manuscript, a related health-AI paper, or a revision intended for *Informatics and Health*. The target outcome is a submission-ready research manuscript with a clear clinical problem, explicit gap, reproducible methods, restrained claims, and a readable human academic voice.

## Source-of-truth boundary

The five local PDFs were used to learn writing and presentation patterns. Their published layout is evidence of journal style, not a substitute for the current Guide for Authors. Before submission, verify the live journal requirements for article type, word limit, highlights, graphical abstract, declarations, data availability, reference style, and file formats. Never invent a word count or page limit from the five PDFs.

Read [references/format-patterns-from-five-papers.md](references/format-patterns-from-five-papers.md) when detailed journal-specific guidance is needed.

## Select the correct article pattern

- For MedVision, use the **Full Length Article** pattern: Introduction, Related Work/Literature Review, Materials and Methods, Results, Discussion, and Conclusion.
- Use the **Review** pattern only when synthesizing prior literature without a new trained model or experiment.
- Use the **Perspective** pattern only for a forward-looking position or agenda without presenting a full original experiment.
- Do not mix a perspective-style broad narrative with a full-length experimental paper unless each section has a clear role.

## Manuscript workflow

1. Define the clinical problem and the intended claim before writing. For MedVision, distinguish image contribution, report-label circularity, model performance, and clinical diagnostic validity.
2. Build the Introduction around context, problem, evidence gap, research question/hypothesis, and a short numbered contribution list.
3. Write Materials and Methods so another researcher can reproduce the cohort, labels, split, preprocessing, model, interventions, metrics, statistics, and software environment.
4. Present Results in the same order as the prespecified outcomes. Give cohort counts first, then baseline/model comparisons, primary audit outcome, secondary analyses, robustness, and failures.
5. Write Discussion in four moves: principal findings, comparison with prior work, methodological/clinical implications, and limitations/future work.
6. Keep the Conclusion short. State what was demonstrated, what was not demonstrated, and the practical implication.
7. Complete ethics, data access, code availability, funding, conflicts, author contributions, and acknowledgements according to the current Guide for Authors.

## Recommended MedVision structure

### Title

Use a descriptive title containing the modality, setting, failure mode, and study type. Avoid promotional words such as "revolutionary", "ground truth", or "smoking gun". A scoped title such as *The Incoherence of Text-Debiasing in Medical Vision-Language Models: An Empirical Study of Label Circularity in MIMIC-CXR* is appropriate if the manuscript consistently supports that scope.

### Abstract

Follow the journal's current structured-abstract requirement if one exists. The local full-length papers commonly use a compact sequence equivalent to **Background -> Methods -> Findings/Results -> Interpretation**. Include:

- the clinical and methodological problem;
- cohort/data source and study design;
- model/intervention and primary evaluation;
- the most important quantitative result with uncertainty or a clear comparison;
- a restrained interpretation and no unsupported deployment claim.

The five papers suggest roughly 180-265 words as an observed range, not an official limit. Do not hide N/A metrics or exploratory post-hoc analyses in the abstract.

### Introduction

Use a funnel structure:

1. Clinical importance and current workflow.
2. What existing AI/VLM systems do well.
3. Why aggregate accuracy, calibration, or plausible explanations may still be misleading.
4. Specific gap: report-derived labels and report inputs can create label circularity; debiasing does not automatically establish image grounding.
5. Research question and hypotheses.
6. Three to five numbered contributions, each testable in the Results section.

Do not claim "first" without a checked literature search. For MedVision, scope novelty around the controlled audit design and statistical treatment rather than the general observation that medical VLMs can ignore images.

### Related Work / Literature Review

Organize by ideas, not by one-paper-per-paragraph chronology:

- medical image-text/VLM representation learning;
- shortcut learning and unimodal priors;
- report-derived labels and labeler uncertainty;
- debiasing methods such as bias-only models, RUBi, or product-of-experts;
- causal/behavioral grounding audits;
- statistical and reporting standards.

End each subsection with the limitation that motivates the present experiment. Cite the exact source for each claim and distinguish MIMIC-CXR provenance from the CheXpert labeler.

### Materials and Methods

Use numbered subsections and define every variable before the first result:

1. **Study design and data source:** dataset version, institution, dates, access conditions, unit of analysis, inclusion/exclusion criteria, and patient-level split.
2. **Label construction:** labeler, uncertainty policy, missing labels, class definitions, and the possibility that the target is extracted from the same report supplied to the text encoder.
3. **Preprocessing:** image range/normalization, resizing, augmentation, text cleaning/tokenization, maximum length, and leakage controls.
4. **Models and baselines:** image-only, text-only, gray-square/text, full VLM, fusion variants, initialization, frozen layers, optimizer, loss, epochs, hardware, and seeds.
5. **Audit interventions:** gray-square, report-preserving image replacement, image ablation, gate extraction, noise perturbation, or other counterfactuals. State which intervention is used at train time and which at test time.
6. **Outcomes and statistics:** primary outcome first; define ICM, equivalence margin/SESOI, confidence intervals, seed-level versus subject-level unit, paired testing, multiplicity correction, and missing-metric handling.
7. **Reproducibility and governance:** software versions, checkpoint provenance, source hashes/merge policy, code availability, ethics, and data access.

Do not describe a single-token vector interaction as token-level cross-attention. Do not call an anti-consistency objective "consistency" unless the sign and intended behavior agree.

### Results

Follow the prespecified order:

1. Cohort flow and class counts.
2. Baseline performance with uncertainty.
3. Primary modality-contribution/circularity result.
4. Secondary model-variant comparisons.
5. Calibration, robustness, gate behavior, and subgroup analyses.
6. Error/failure cases and missing outputs.

Report the analysis unit explicitly. If eight seeds reuse the same subjects, never present pooled rows as independent subjects. For unavailable ECE/Brier/AUC outputs, report N/A and explain why; never replace missing values with zero.

### Discussion

Use separate paragraphs for:

- principal finding and its uncertainty;
- agreement/disagreement with the closest prior work;
- what the result means for multimodal evaluation and clinical deployment;
- limitations: label circularity, independent-label absence, single dataset, external validation, post-hoc extensions, pretraining overlap, subgroup coverage, and statistical unit;
- concrete future experiments.

Interpret a learned gate as a parameter, not as causal attribution, unless intervention-based evidence supports the interpretation. Treat TOST equivalence as evidence within the prespecified margin, not proof that two systems are identical or clinically interchangeable.

## Tables and figures

Include only figures that answer a stated question. A strong MedVision set is:

- a cohort/split flow diagram;
- a compact model and intervention schematic;
- a main performance table with mean, spread, and confidence intervals;
- an ICM/equivalence figure with the prespecified margin;
- a seed-level gate distribution generated directly from checkpoints;
- calibration and/or per-class ROC plots when probability outputs are retained;
- one concise qualitative failure or saliency panel, clearly labeled as illustrative.

Every table/figure must be cited in the text before it appears, have a self-contained caption, define abbreviations, state the sample/seed count, and identify whether values are per-seed, per-subject, or pooled. Avoid decorative diagrams and avoid figures whose data cannot be traced to a saved artifact.

## Writing voice

Write in clear, natural academic English with varied sentence structure. Keep terminology stable, define acronyms once, and remove filler such as "it is worth noting", "in today's era", "revolutionary", or "very important". Do not repeat the same sentence pattern across sections. Prefer precise verbs ("estimated", "compared", "observed", "supports") over promotional verbs ("proves", "guarantees", "solves"). Paraphrase sources and cite them; do not imitate their wording.

## Final pre-submission checks

- Article type and live author instructions verified.
- Abstract matches the reported Results and contains no hidden N/A values.
- Primary and exploratory analyses clearly separated.
- Subject-level independence and paired alignment verified.
- No zero-filled missing metrics.
- Checkpoint-derived plots reproduce from the saved artifacts.
- Data/label provenance, ethics, code, funding, conflicts, and limitations are explicit.
- Every central claim has a matching result and citation.
