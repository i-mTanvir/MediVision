# MedVision Source Documents — Deep Analysis

## Priority and source-of-truth policy

The most important writing base is `MedVision_Q1_Paper_FINAL_v9.docx`. It is marked here as **PRIMARY DRAFT / HIGH PRIORITY**. However, factual claims must be checked against executed notebooks and exported result artifacts before manuscript finalisation.

Recommended authority order:

1. Executed notebook code and its actual saved outputs (`all_results.pkl`, `img_text_results.pkl`, JSON, figures).
2. `MedVision_Q1_Paper_FINAL_v9.docx` for narrative structure, section order and writing direction.
3. `MedVision_Code_Walkthrough.pdf` for conceptual code explanation, after reconciling stale descriptions.
4. `MedVision_Project_Guide.pdf` for handoff context and project history, not for final numerical claims.

## Source files inspected

- `MedVision_Project_Guide.pdf`: 10 pages, A4, ReportLab-generated handoff guide.
- `MedVision_Code_Walkthrough.pdf`: 10 pages, A4, ReportLab-generated architecture/data-flow guide.
- `MedVision_Q1_Paper_FINAL_v9.docx`: 181 paragraphs, 7 tables, 13 embedded figures, 30 numbered references, approximately 7,700 words by structural count. It has one section, no comments, no tracked changes, no footnotes/endnotes, and no hyperlinks in the OOXML package.

## Project Guide analysis

The Project Guide frames the study as an audit of whether MIMIC-CXR VLMs use images or exploit reports. It describes:

- a three-class MIMIC-CXR cohort;
- five fusion conditions and eight seeds;
- Gray-Square ablation, ICM, TOST and gate extraction;
- high Macro-F1 but very small gray-square gap;
- gate values close to initialization;
- planned Q1 submission and handoff steps.

The guide is useful for project narrative, but it contains several statements that must not be copied into the paper without correction:

1. It says the project has 11 training notebooks plus an audit notebook and refers to Part 11/adaptive training. The current folder has Part 1–10, the legacy audit, and `medvision-q1-audit-final-FIXED-MERGE-v2.ipynb`; the standalone adaptive notebook was removed.
2. It reports an initial 6,000-image budget but the audit export loads 2,962 rows, removes 9 unavailable images, and evaluates 2,953 studies. The manuscript must explain this accounting rather than imply that exactly 6,000 studies entered training.
3. It calls the image contribution “statistically zero” and “complete visual bypass.” The evidence supports negligible incremental Macro-F1 under this gray-square control, not proof that images are never used or that every prediction is text-only.
4. It calls gate drift less than float16 precision. The current alpha values are close to initialization, but the stronger causal statement “text was sufficient, therefore the gate received no useful gradient” is an interpretation that requires gradient logging or ablation, not just checkpoint alpha values.
5. It labels the Noise-Consistency method as an anti-consistency objective that maximizes KL. That may be intentional, but the name and clinical interpretation are nonstandard and must be justified explicitly.
6. It states the draft is ready for JBI submission. Submission readiness is not established: the draft has factual contradictions, stale figure claims, unsupported regulatory language and unresolved methodological concerns.

## Code Walkthrough analysis

The Code Walkthrough correctly explains the shared notebook structure, Config, encoders, fusion variants, resume logic and audit flow. It is particularly useful for Methods planning. The following code-to-document mismatches require correction:

- The embedded methodology figure labels the image encoder as **ResNet-50**, with a 2048→256 projection. Actual code uses TorchXRayVision **DenseNet-121**, a 1024→512 projection, and a 512-dimensional fusion space.
- The figure depicts a dynamic gate `alpha = sigmoid(W[img;txt])`, whereas the Baseline CADQ gate is a static learnable per-class parameter of shape `[3]`; Adaptive-CADQ is the entropy-gated dynamic variant.
- The walkthrough says the current audit is `medvision-q1-audit-v2.ipynb` and presents the old cell order. The current fixed-merge notebook adds a patch cell and merges five conditions/40 entries.
- It describes GACR-B probability outputs as unavailable. The current `New Added` `all_results.pkl` contains `all_probs` for GACR-B and the fixed audit reports GACR-B AUROC/ECE/Brier; the draft’s N/A claims are stale.
- The walkthrough presents the negative-KL Noise-Consistency path as designed anti-consistency. This should be retained only if the research hypothesis explicitly requires sensitivity to image noise; otherwise it is a loss-sign/terminology problem.

## Draft DOCX analysis — structure

The draft has a strong conventional manuscript skeleton:

1. Introduction
2. Related Work
3. Methods
4. Results
5. Discussion
6. Limitations
7. Conclusion
8. Reporting Statements
Supplementary Materials
References

It contains sections for cohort, architecture, gray-square control, ICM, gate extraction, statistics, compliance, calibration, cross-variant results, Grad-CAM, limitations and reporting statements. This is a good base for a paper, but the current version should be treated as a **substantive draft requiring a factual-consistency pass**, not as a final submission copy.

### Major factual and statistical corrections needed

1. **Cohort sentence contradiction.** The split paragraph says the test set contains 47 Pneumothorax cases and then repeats that it contains approximately 150 cases. Keep only the verified value: 47.
2. **Stale GACR-B availability.** Results and figure notes mark GACR-B AUC/ECE/Brier as N/A because probabilities were allegedly unavailable. Current merged artifacts contain GACR-B probabilities and report mean AUROC ≈0.9972, ECE ≈0.0245 and Brier ≈0.0540. Update Table 1, Figure 4/6 notes, Results and Limitations.
3. **Stale figure coverage.** The draft says GACR-B is missing from ROC/confusion figures. The current fixed figures include GACR-B in the five-variant comparison; either embed the fixed figure or clearly label the draft figure as legacy.
4. **Incorrect McNemar interpretation.** `p=1.000` does not mean byte-identical predictions or zero discordance. The fixed output reports nonzero discordance (for example baseline vs GACR-B n01=9, n10=8; baseline vs Adaptive n01=15, n10=14). Rewrite the claim as “no evidence of asymmetric error rates,” not identical predictions.
5. **Pairwise p-value wording.** The sentence “all six paired Wilcoxon tests were p>0.07” is false because GACR-B vs baseline is approximately p=0.0547. Use exact values and distinguish uncorrected from BH-FDR-adjusted results.
6. **Permutation count mismatch.** The draft repeatedly says 2,000 permutations/resamples. The current fixed patch’s multi-seed permutation AUC uses `n_perm=500`; legacy figures may use 2,000 bootstrap resamples. State the exact procedure and count for each analysis.
7. **ECE/Brier inference mismatch.** Current fixed patch metric functions default missing `test['ece']`/`test['brier']` to zero. The manuscript’s displayed mean ECE/Brier values were computed elsewhere on the fly, but the fixed multi-metric p-values are not valid. Recompute per seed from `all_probs`/`all_labels` before reporting inferential statistics.
8. **Repeated-test-subject pooling.** DeLong, McNemar and pooled permutation analyses concatenate the same test studies over seeds. These tests need clustered/per-seed analysis; otherwise their p-values should be labelled exploratory and not presented as ordinary independent-sample evidence.
9. **Gray-square uncertainty.** ICM repeats one single-run gray-square F1 across eight baseline seeds. This treats the control as error-free and understates uncertainty. Ideally train gray-square across the same seeds or use a paired control design.
10. **TOST margin language.** ±0.01 is a relative Macro-F1 equivalence margin selected by the project; it is not automatically a clinically validated or “regulatory-grade” threshold. Describe it as a pre-specified operational margin and justify sensitivity to alternative bounds.
11. **Pre-registration wording.** The draft first says all tests were pre-registered, then says Adaptive-CADQ and GACR-B were added post hoc. Use “partially pre-registered” and specify which variants/outcomes were confirmatory.
12. **Overclaiming causality.** “Proved complete visual bypass,” “non-functional image pathway,” “the gate received no gradient,” “all debiasing is structurally incapable,” and “mandatory for regulatory submissions” exceed the current evidence. Replace with bounded statements: negligible incremental performance under this intervention, observed gate stagnation in this architecture, and failure of tested variants on this cohort.
13. **Unsupported regulatory statement.** The claim that 2026 FDA AI/ML guidance demands proof of visual grounding is not established by the local files and should be removed or sourced precisely after verification.
14. **Label circularity is a risk, not an accidental bug.** CheXpert labels derive from reports and the same findings text is input to the model. The paper should call this label/report circularity or construct-validity limitation, not imply that it proves every text prediction is clinically invalid.
15. **Noise-Consistency naming.** The implementation maximizes prediction divergence under image noise. If intentional, rename it to an anti-consistency/noise-sensitivity intervention and state the hypothesis; if consistency was intended, correct the loss and rerun.

### Writing/formatting issues

- Figure numbering is inconsistent: captions and body references jump among Figure 1, Figure 2, Figure 3, Figure 4, Figure 5, Figure 6, Figure 7, Figure 8, Figure 9, Figure 10, Figure 11, Figure 12 and Figure 13 without a single clean order.
- Only 7 paragraphs use the Word Caption style; several figure captions are plain Normal paragraphs. Use one caption system and regenerate cross-references.
- The main Methods figure contains incorrect architecture labels (ResNet-50/256 dimensions), making it unsafe as a paper figure.
- The embedded ICM/TOST figure contains a malformed legend that prints a literal Python dictionary expression instead of a clean p-value label.
- The document has 13 embedded images, while prose alternately describes 7, 10, 12 and 13 figures. Reconcile the final figure set before submission.
- Table geometry uses equal-width grid columns even for highly unequal content. This may wrap poorly in Word/PDF; visual page QA is still required.
- The first title is directly formatted as a Normal paragraph rather than a stable title style. Author, affiliation and email remain placeholders.
- `MedVision_Q1_Paper_FINAL_v9.docx` has no comments or tracked changes, so there is no built-in revision history.
- Headless DOCX rendering could not be completed in this environment because LibreOffice/soffice is unavailable. Structural review and embedded-image inspection were completed, but final page-level clipping/overflow remains to be checked on a machine with Word or LibreOffice.

## Title idea evaluation

Proposed title:

> *The Incoherence of Text-Debiasing in Medical Vision-Language Models: An Empirical Study of Label Circularity in MIMIC-CXR*

Strengths:

- It foregrounds the conceptual contribution rather than a narrow architecture name.
- It makes label circularity and text-debiasing immediately discoverable.
- It is more aligned with the observed negative/diagnostic result than a conventional “new model” title.

Risks:

- “The incoherence of text-debiasing” sounds universal, although the experiments test a limited set of variants on one dataset.
- The evidence is strongest for report-derived labels and the tested implementations, not all medical VLMs or all text-debiasing methods.

Safer recommended title:

> **When Text Is the Label: Evaluating Image Contribution and Text-Debiasing in MIMIC-CXR Vision-Language Models**

If the user prefers the proposed framing, a bounded version is:

> **The Incoherence of Text-Debiasing Under Label Circularity: An Empirical Audit of MIMIC-CXR Vision-Language Models**

## Recommended paper positioning

The defensible central claim is:

> On this MIMIC-CXR-derived three-class task, where CheXpert labels and model input reports are text-linked, a gray-square control nearly matches full VLM Macro-F1. Across the tested fusion interventions, the study found no robust evidence of increased incremental image contribution, while the baseline CADQ gate remained close to initialization.

Avoid claiming that the image is universally unused, that the architecture is clinically non-functional, or that ICM is already regulator-approved. Frame ICM as a proposed diagnostic metric requiring validation on independent labels, external datasets and modern VLMs.

