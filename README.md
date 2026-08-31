# MediVision: Auditing Modality Inertia in Medical Vision–Language Models

[![Status: research artifact](https://img.shields.io/badge/status-research%20artifact-355C7D)](#project-status)
[![Manuscript: Informatics and Health](https://img.shields.io/badge/target-Informatics%20and%20Health-2F7D32)](#manuscript)
[![LaTeX](https://img.shields.io/badge/manuscript-LaTeX-008080?logo=latex)](#build-the-manuscript)
[![Python](https://img.shields.io/badge/analysis-Python-3776AB?logo=python&logoColor=white)](#reproducing-the-audit)

> A reproducibility-oriented audit of whether high performance in a
> MIMIC-CXR-derived medical vision–language model reflects incremental image
> evidence when labels and report inputs share provenance.

![MediVision audit workflow](My%20writing/figures/methodology.png)

## Project status

This repository accompanies the manuscript:

**Quantifying Modality Inertia in Medical Vision-Language Models: Image
Contribution Metric, Gate Stagnation, and the Failure of Debiasing Under Label
Circularity**

The current manuscript is a research draft targeting *Informatics and Health*.
It is not a clinical decision-support system and must not be used for diagnosis
or patient care.

## Authors

- **Nafis Al Rahman** — equal contribution
- **Tanvir Mahmud** — equal contribution

## Research question

When CheXpert targets are derived from the same radiology reports supplied to a
multimodal classifier, does text debiasing create measurable image dependence,
or can high predictive performance persist with little incremental radiographic
information?

The audit combines report-preserving image replacement, seed-level paired
inference, calibration analysis, learned-gate extraction, and qualitative
saliency inspection. The primary endpoint is the Image Contribution Metric
(ICM), evaluated with an operational equivalence interval of `[-0.01, 0.01]`.

## Evidence snapshot

| Audit item | Current result | Interpretation boundary |
|---|---:|---|
| Final cohort | 2,953 studies | Patient-level split: 2,049 / 449 / 455 |
| Baseline Macro-F1 | 0.9397 ± 0.0061 | High aggregate performance alone is not grounding evidence |
| Gray-Square Macro-F1 | 0.9381 | One retained report-preserving control run |
| Baseline ICM | 0.0016 ± 0.0065 | Wilcoxon `p=0.4219`; TOST `p=0.0040` |
| Mean learned image gate | 0.49975 | Remained near the 0.50000 initialization |
| LMH ECE | 0.0237 → 0.0621 | Calibration worsened despite competitive Macro-F1 |

![ICM with equivalence interval](My%20writing/figures/icm_tost_master.png)

## Repository map

| Path | Contents |
|---|---|
| [`My writing/`](My%20writing/) | Authoritative LaTeX manuscript, BibTeX databases, final PDF, figure scripts, figures, and reviewer audits |
| [`ipynb Files/`](ipynb%20Files/) | Sequential training notebooks and the current fixed-merge audit notebook |
| [`New Added/untitled folder/`](New%20Added/untitled%20folder/) | Retained result dictionaries, audit JSON, compliance data, and environment requirements |
| [`Journal Writing Reference/`](Journal%20Writing%20Reference/) | Journal-specific writing skill and extracted formatting patterns; third-party PDFs are omitted |
| [`Referances/`](Referances/) | Reference-library manifest; third-party article PDFs are omitted |
| [`markdown_exports/`](markdown_exports/) | Local-only notebook exports; ignored because they duplicate the notebooks |
| Root `*.md` files | Project knowledge base, source-document analysis, reference synthesis, and writing guidance |

## Reproducing the audit

### 1. Data access

MIMIC-CXR is not redistributed here. Obtain credentialed access through
PhysioNet, complete the required training and Data Use Agreement, and attach
the authorised dataset in the execution environment. Never commit credentials,
raw radiographs, reports, or patient-level exports.

### 2. Notebook sequence

The historical training pipeline is stored as
`ipynb Files/medvision-thesis-part1.ipynb` through `part10.ipynb`. The current
authoritative audit is:

```text
ipynb Files/medvision-q1-audit-final-FIXED-MERGE-v2.ipynb
```

The fixed-merge notebook consumes retained upstream results. Its outputs should
be checked against `New Added/untitled folder/q1_audit_results.json` and the
provenance statements in the manuscript. Notebook outputs are retained for
traceability, but claims should be based on the corrected seed-level statistics
reported in the Master manuscript.

### 3. Regenerate manuscript figures

From `My writing/`:

```powershell
python generate_master_figures.py
```

The script reads the retained audit result files and regenerates the ICM,
paired-control, ECE, cohort-flow, and gate-stagnation figures.

## Manuscript

The authoritative sources are:

- `My writing/MedVision_Q1_Master.tex`
- `My writing/related_work_references.bib`
- `My writing/methodology_references.bib`
- `My writing/figures/`
- `My writing/MedVision_Q1_Master.pdf`
- `My writing/MedVision_Q1_Supplementary.tex` (Tables S2--S4; submit as a separate supplement when requested)

### Build the manuscript

With MiKTeX or TeX Live installed:

```powershell
cd "My writing"
pdflatex -interaction=nonstopmode -halt-on-error MedVision_Q1_Master.tex
bibtex MedVision_Q1_Master
pdflatex -interaction=nonstopmode -halt-on-error MedVision_Q1_Master.tex
pdflatex -interaction=nonstopmode -halt-on-error MedVision_Q1_Master.tex
```

Alternatively, run `compile_informatics_health.ps1` from the repository root.

The main manuscript is 15 pages.  The checklist and provenance tables are kept
in the one-page `MedVision_Q1_Supplementary.tex` companion so that the review
copy remains readable; Table S1 (training hyperparameters) remains in the main
manuscript's reporting statements.

## Interpretation and reproducibility notes

- The same 455 held-out studies recur across seeds; confirmatory inference is
  therefore performed at the matched seed level rather than by pooling repeated
  subject observations.
- The Gray-Square control is one retained run reused across seed-level ICM
  calculations, so control uncertainty is understated.
- Adaptive-CADQ was extended from three to eight seeds post hoc, and GACR-B was
  added post hoc; both facts are disclosed in the manuscript.
- The archived Noise-Consistency objective uses a negative-KL sign and should
  not be interpreted as conventional consistency regularisation.
- The one-image-token/one-text-token attention design cannot establish
  word–region alignment, and qualitative Grad-CAM panels are not causal
  grounding evidence.
- The central result is a construct-validity warning under label–report
  circularity, not a universal claim that radiographs are unnecessary.

## Versioning policy

Manuscript, analysis, figure, and documentation changes are committed with
descriptive messages and pushed to the `main` branch. This makes each accepted
state recoverable with standard Git history. Temporary renders, LaTeX auxiliary
files, raw datasets, model checkpoints, credentials, and third-party article
PDFs are excluded through `.gitignore`.

## Citation

Repository citation metadata is provided in [`CITATION.cff`](CITATION.cff).
Please cite the final peer-reviewed article once publication metadata becomes
available.
