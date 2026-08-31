# Journal of Biomedical Informatics (JBI) — author and submission guide

**Publisher:** Elsevier / Academic Press  
**ISSN:** 1532-0464 (print record); the journal page also uses the JBI title and
ScienceDirect article identifier family.  
**Prepared:** 31 August 2026  
**Target manuscript:** MedVision modality-reliance and label--report
circularity audit

## 1. Verified journal identity and metrics

The supplied website is the correct Elsevier ScienceDirect journal page:

<https://www.sciencedirect.com/journal/journal-of-biomedical-informatics>

The ScienceDirect journal record currently displays **Impact Factor 4.5** and
**CiteScore 10.8**. These values are time-sensitive; verify the current
Clarivate Journal Citation Reports and Scopus records immediately before using
them in a CV, grant, or submission decision. Do not rely on third-party “Q1”
claims without checking the category and metric year. The journal page describes
JBI as a methodology journal endorsed by the American Medical Informatics
Association.

## 2. Scope and desk-rejection risk

JBI prioritizes new biomedical-informatics **methods and techniques with
general applicability**, motivated by a real biomedical or clinical problem and
compared with the state of the art. Country-specific or dataset-specific work
is acceptable only when it yields lessons generalizable beyond that setting.

The publisher explicitly cautions that papers primarily about signal processing,
imaging, medical devices or communication networks are outside scope unless
they combine a knowledge-intensive approach, such as ontologies or biomedical
knowledge representation. A routine CXR model benchmark or an imaging-only
engineering paper is therefore a high desk-rejection risk.

### MedVision fit assessment

The current paper has a potentially relevant JBI contribution because it audits
information provenance, report-derived targets, modality reliance, statistical
estimands and reproducibility. To make that contribution legible, the title,
abstract, introduction and cover letter should emphasize:

1. a general audit methodology for testing incremental modality information;
2. label/input provenance as an information-integrity problem;
3. seed-aware paired inference and an operational equivalence test;
4. reproducibility and checkpoint-provenance safeguards; and
5. lessons that transfer to other biomedical VLMs and report-linked datasets.

The manuscript must not present itself as only a new chest-radiograph
classifier. Before submission, send the title and abstract to the JBI editorial
office or use the journal's scope guidance to confirm that this methodological
audit is suitable.

## 3. Article categories

The journal page lists original research, methodological reviews, commentaries,
special communications, letters to the editor, book reviews and editorials.
MedVision should be submitted as an **Original Research** paper because it
contains a new empirical audit, controlled interventions and statistical
analysis. A methodological review category would be incorrect unless all
experimental results were removed and the work became a literature synthesis.

## 4. Word count, abstract and display limits

### What is confirmed

The live ScienceDirect Guide for Authors is the source of truth for the current
limits. It must be opened from the journal page immediately before submission:

<https://www.sciencedirect.com/journal/journal-of-biomedical-informatics/publish/guide-for-authors>

The guide page was not machine-readable during this audit (ScienceDirect
returned an access restriction), so a fixed number must not be treated as an
official JBI rule.

### Publicly indexed secondary observations (not a substitute for the live guide)

An independent journal-format checker currently reports **6,000 words** for the
article and **300 words** for the abstract, with an **8-display-item** limit.
These values are useful as a working ceiling only; verify them in the JBI
submission portal because article types and limits can change.

Recommended working target for the present paper until portal verification:

- Main text: ≤6,000 words excluding references unless the portal says otherwise.
- Abstract: ≤300 words.
- Main display items: aim for ≤8 combined figures/tables; move additional
  diagnostics to supplementary files.

## 5. Abstract pattern

Recent JBI original-research records commonly use a structured abstract with
the headings **Objective, Methods, Results, and Conclusions**. The abstract
should state the biomedical problem, the methodological contribution, the
cohort/design, the primary quantitative result and the properly bounded
interpretation. It should not contain citations, unexplained abbreviations or
claims of clinical deployment that the experiment did not test.

For MedVision, map the existing abstract as follows:

- **Objective:** test whether text-debiasing increases incremental image
  information under report-derived label circularity.
- **Methods:** MIMIC-CXR-derived cohort, five conditions, eight seeds,
  report-preserving Gray-Square control, ICM and prespecified TOST interval.
- **Results:** baseline ICM, Wilcoxon/TOST results, calibration change, gate
  extraction and the most important uncertainty/caveat.
- **Conclusions:** high report-conditioned performance did not establish
  incremental image grounding in this benchmark; independent labels and
  external cohorts are required.

Keep the abstract within 300 words provisionally, then apply the exact live
limit. Define ICM at first use and avoid introducing every model acronym in the
abstract.

## 6. Manuscript structure

Use a full-length original-research structure:

1. Title page and author information.
2. Abstract and keywords.
3. Introduction: clinical/biomedical problem, information-provenance risk,
   research gap, question and contributions.
4. Related work: biomedical VLMs, shortcut learning, report-derived labels,
   modality-reliance audits and evaluation standards.
5. Materials and methods: cohort, label construction, preprocessing, models,
   interventions, endpoints, statistics, software and provenance.
6. Results: cohort flow, baseline/controls, primary ICM, equivalence test,
   calibration, gate extraction, paired tests and failure analyses.
7. Discussion: principal finding, generalizable informatics implication,
   relation to prior work, clinical/evaluation implications and limitations.
8. Conclusion: one short paragraph with scope explicitly bounded.
9. Declarations: ethics/data access, code availability, funding, competing
   interests, author contributions, acknowledgements and AI disclosure.
10. References, figure legends, tables and supplementary files as requested by
    the submission portal.

## 7. Methods requirements reviewers will check

- Define the biomedical unit of analysis and patient-level split.
- State how CheXpert labels were generated and that the report can also be a
  model input; distinguish label provenance from independent ground truth.
- Describe all preprocessing, XRV normalization, tokenization and leakage
  controls.
- Identify model versions, checkpoints, optimizer, schedule, hardware and all
  seeds.
- Distinguish confirmatory baseline analyses from post-hoc Adaptive-CADQ and
  GACR-B extensions.
- Define ICM, the operational equivalence margin, bootstrap procedure, paired
  seed-level unit, multiplicity correction and missing-output policy.
- Never pool the same 455 studies across seeds as independent observations.
- Explain that one image token and one text token do not establish word--region
  grounding, and that Grad-CAM is qualitative rather than causal evidence.
- Provide code, configuration, environment and deterministic provenance records
  through an enduring repository when permitted by data-access restrictions.

## 8. Figures, tables and supplementary material

Number figures and tables in the order cited. Captions/legends should be
self-contained and state the cohort or seed count, conditions, error-bar/CI
meaning and statistical test. Preserve source images and underlying numeric
measurements; do not obscure data through image processing.

JBI papers frequently include a graphical abstract or a concise methodological
overview. Treat this as a portal requirement to verify, not as a license to add
decorative artwork. For MedVision, prioritize the following main items if an
8-item display limit is confirmed:

1. methodology/cohort workflow;
2. primary performance/control table;
3. ICM with TOST band;
4. paired VLM-versus-Gray-Square plot;
5. calibration or ROC diagnostic;
6. gate extraction/stagnation figure;
7. one compact failure/saliency panel; and
8. one supplementary or cohort table only if required for the main argument.

Move checklists, provenance manifest, full per-seed tables and secondary
diagnostics to supplementary files. Ensure every main display item is called out
before it appears.

## 9. Citation and reference style

JBI/Elsevier published articles use numbered citations in square brackets in
the text and a numbered reference list ordered by first appearance. The current
MedVision draft uses author--year `natbib` citations for drafting; that must be
converted to JBI's numbered style before submission and the order audited after
conversion. Do not renumber manually without recompiling and checking every
cross-reference.

References should be complete, current and directly relevant. Verify DOI,
author list, year, volume/article number and whether an arXiv item has a later
peer-reviewed version.

## 10. Submission files and declarations

Use Elsevier Editorial Manager for JBI:

<https://www.editorialmanager.com/jbi>

Prepare a cover letter that states the generalizable methodological contribution
and explains why the work fits JBI rather than a purely imaging or engineering
venue. The submission should include, as applicable:

- manuscript source and compiled PDF;
- separate figures/high-resolution files if the portal requests them;
- highlights or graphical abstract if shown as mandatory in the live portal;
- title-page author affiliations and corresponding-author details;
- ethics/data-access statement for MIMIC-CXR;
- code/data availability statement with the GitHub URL and future archival DOI;
- funding, competing interests, CRediT roles and acknowledgements;
- honest disclosure of any generative-AI or language assistance;
- reporting checklist or supplementary material requested by the article type.

Elsevier's current generative-AI policy applies. AI tools cannot be authors;
authors remain responsible for accuracy, attribution, confidentiality and
originality, and permitted use affecting text, code, images or analysis should
be disclosed.

## 11. Decision checklist for MedVision

Before opening a JBI submission, confirm:

- [ ] The editor accepts a biomedical-informatics audit whose experiment uses
      medical images rather than presenting a routine image-classification
      benchmark.
- [ ] The live portal confirms the article word limit, abstract limit and
      display-item limit.
- [ ] The abstract uses Objective/Methods/Results/Conclusions and is within the
      verified limit.
- [ ] The title and Introduction claim a generalizable information-provenance
      and modality-audit method.
- [ ] The manuscript uses numbered square-bracket citations and first-appearance
      reference order.
- [ ] All eight-seed tests respect matched pairing; no repeated-subject pooling
      is used for inferential P values.
- [ ] Ethics/access, code, funding, conflict, CRediT and AI statements are
      complete and factually accurate.
- [ ] The main display items comply with the portal's current count and file
      resolution rules.

## Sources

- [Latest five JBI Original Research papers and access links](latest-five-papers/README.md)

- [ScienceDirect JBI journal page](https://www.sciencedirect.com/journal/journal-of-biomedical-informatics)
- [ScienceDirect JBI Guide for Authors](https://www.sciencedirect.com/journal/journal-of-biomedical-informatics/publish/guide-for-authors)
- [Elsevier medical-informatics journal overview](https://www.elsevier.com/en-in/subject/medical-informatics/journals)
- [Elsevier journal subscription/aims page](https://shop.elsevier.com/journals/journal-of-biomedical-informatics/1532-0464)
- [JBI Editorial Manager](https://www.editorialmanager.com/jbi)
- [Secondary working-limit summary (verify against the live guide)](https://scraiber.com/journals/journal-of-biomedical-informatics)

## Status note

This guide is a reusable research aid, not a substitute for the live publisher
instructions. The exact word/page/abstract/display limits and any mandatory
graphical abstract or highlights requirement must be captured from the JBI
submission portal immediately before submission.
