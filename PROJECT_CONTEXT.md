# MedVision - current project context

Updated: 2026-09-03

## Latest user decision

The user will correct and manually upload the methodology image. This turn is
a context-only update: do not replace an image, edit the manuscript, or compile
a new PDF. Wait for the user's updated image and instruction to integrate it.
The last displayed image is a review candidate, not an approved final figure.

## Active manuscript and source priority

- Active target: Journal of Biomedical Informatics (JBI).
- Active manuscript: `My writing/MedVision_JBI_V2.tex` and its compiled PDF.
- Current compiled version: 15 pages, from commit `6107992`.
- This is an internal working manuscript for subsequent team/supervisor review;
  do not describe it as submission-ready.
- Preserve `My writing/MedVision_Q1_Master.tex` and its PDF as the separate
  Informatics and Health fallback; do not develop both versions in parallel.
- Authors: Nafis Al Rahman and Tanvir Mahmud.
- Bibliographies: `My writing/related_work_references.bib` and
  `My writing/methodology_references.bib`; the current JBI version cites 35
  sources. Do not add, remove, or revert citations as part of image integration.
- `MedVision_Q1_Paper_FINAL_v9.docx` remains the narrative reference, but its
  embedded figures and prose contain internal contradictions. Executed code,
  retained outputs, and the reconciled JBI statistics take precedence for facts.
- Current audit notebook:
  `ipynb Files/medvision-q1-audit-final-FIXED-MERGE-v2.ipynb`.

## Methodology image state

- Currently embedded A-C asset:
  `My writing/figures/methodology_diagram_v2_abc.png`.
- That asset is an unchanged copy of
  `D:/Downlodes/Telegram Desktop/Methodology Diagram v2.png`; it is older than
  the successive screenshots reviewed in this conversation.
- The older `My writing/figures/methodology.png` is preserved, not overwritten.
- Current Figure 1 retains `My writing/figures/cohort_flow.png` as panel D.
  Panel C is the audit workflow and does not duplicate cohort selection.
- Most recent review screenshot:
  `C:/Users/USER/AppData/Local/Temp/codex-clipboard-8e914beb-c1b3-4dde-9805-dedce301e943.png`.
  This temporary path is only a review reference; do not assume it is the file
  the user will ultimately upload or that it will persist.
- The current caption identifies A-C as a proposed schematic with unresolved
  implementation differences. After a corrected image is supplied, recheck
  those differences and update only caveats that the image actually resolves.

## Diagram content to preserve or correct

### Architecture

- Image encoder: TorchXRayVision DenseNet-121, not ResNet-50.
- Text encoder: Bio_ClinicalBERT; model input is the radiology report's Findings
  section, not nursing notes, discharge summaries, or pharmacy notes.
- Omitting embedding dimensions from the overview figure is acceptable; keep
  the verified 512-dimensional projections in Methods. Do not reintroduce the
  legacy 256-dimensional projection labels.
- Cross-attention precedes the gated logit combination: image query, text
  key/value, eight heads, one projected token per modality.
- Separate image/text classification heads supply class logits. Baseline CADQ
  combines those logits with a static learnable per-class gate bounded to
  [0.20, 0.80]. It is not an input-dependent feature gate.
- High-level display order:
  image/text representations -> cross-attention and classification heads ->
  class logits -> CADQ per-class gated logit fusion -> softmax -> class
  probabilities (Normal, Pneumonia, Pneumothorax).
- The latest screenshot still places a box named "Per-class logit fusion"
  before the gate. The last suggested correction is to rename that middle box
  "Image/text classification heads -> class logits", and rename the gate box
  "CADQ per-class gated logit fusion; alpha in [0.20, 0.80]".
- Replace the final neural-network illustration with a clear softmax/probability
  output if necessary; do not imply a new learned classifier after gated logits.
- Remove the remaining unexplained `0.74` and unused vertical strokes from the
  text-encoder illustration.
- Connect prediction probabilities to the audit's "Save probabilities + labels"
  step. Gate extraction should be traced to saved checkpoints, not predictions.
- "Audit summary & visualizations" is acceptable for the audit output. The
  model does not generate radiology reports.

### Audit and statistical scope

- Five fusion conditions each have eight retained seeds. Adaptive-CADQ's seed
  extension and exploratory GACR-B were post hoc; retain these disclosures.
- Gray-Square, text-only, and image-only each have one retained control run.
  The same Gray-Square reference is reused across seed-level ICM values.
- Gate-stagnation results shown here are from eight baseline checkpoints;
  do not imply equivalent gate extraction for every variant.
- Current JBI V2 reports seed-level Wilcoxon, TOST with operational bounds
  [-0.01, 0.01], percentile bootstrap intervals, calibration, and BH-FDR.
- DeLong and McNemar use matched retained seed-42 test arrays in current V2,
  not subjects concatenated across eight seeds.
- Permutation AUROC appears in v9's Methods and its old Figure 10, but not in
  current V2's reported inference. A figure integrated into V2 must match V2;
  do not silently import that analysis from v9.
- Keep the terminology "noise-sensitivity (anti-consistency) condition" and
  "exploratory GACR-B" in current-manuscript labels/captions.

## v9 inspection findings

The v9 DOCX was read directly, including Section 3.2, statistical methods,
training table, and the embedded Figure 10 (`word/media/image13.png`).

- Section 3.2 says DenseNet-121, Linear 512 projection, eight-head attention,
  and a static per-class baseline gate.
- Its old Figure 10 instead shows ResNet-50, 2048->256 and 768->256 projections,
  and an input-dependent gate. Do not treat those legacy labels as authority.
- Section 3.2 freezes the first four text-transformer layers; the training
  table says six. Resolve implementation questions against code, not the table.
- Both the v9 text and diagram describe classification, not report generation.
- A stylistic resemblance to v9 is not permission to reinstate stale numerical
  results or unsupported causal/statistical interpretations.

## Retained JBI result values and interpretation

- Baseline Macro-F1: 0.9397 +/- 0.0061.
- Gray-Square Macro-F1: 0.9381 (single retained run).
- Baseline ICM: 0.0016 +/- 0.0065.
- Bootstrap 95% CI: [-0.0026, 0.0061].
- Wilcoxon p: 0.4219; TOST p: 0.0040.
- Overall baseline gate mean: 0.49975.
- ECE: baseline 0.0237, LMH 0.0621.
- McNemar p=1 does not imply byte-identical predictions.
- Gate stagnation / modality inertia is a diagnostic observation, not proof of
  absent gradients or a causal mechanism.
- Patient-level isolation prevents subject overlap; it does not remove
  label/report circularity.

## Internal wording proposals already in the manuscript

The user requested two statements for a draft preview: (1) shared preprocessing
affects all scores equally without changing relative contrasts; (2) the
image-only control merely lacked exhaustive checkpoint tuning.

In commit `6107992`, their wording was included in two explicitly labelled
"Internal wording proposal - validation pending" footnotes (currently page 5).
They are not verified findings. The main text still explains that a shared
normalization shift need not affect conditions equally and that best-checkpoint
restoration was not guaranteed. No experiment or checkpoint fix was performed.
Do not silently promote either proposal to an executed-method or results claim.

## Next authorized workflow

When the user supplies the corrected image and requests integration:

1. Inspect the actual supplied file, using the checklist above.
2. Copy it into `My writing/figures/` with a descriptive versioned name; retain
   earlier assets and do not modify image pixels unless requested.
3. Use the already embedded A-C labels without duplicating them in LaTeX.
   Retain cohort flow as D unless the supplied image genuinely includes it.
4. Update the Figure 1 caption and local Methods references only as needed.
   Preserve numerical results, citations, and unrelated text.
5. Compile and render-check the PDF, including references and page flow.
   The current 15-page layout uses a float barrier before Discussion instead
   of a forced page break; keep the Results figures ahead of Discussion.
6. Commit only task-related files with a meaningful message and push to
   `https://github.com/i-mTanvir/MediVision.git` on `main`, following the user's
   standing versioning instruction. Do not include unrelated untracked folders.

