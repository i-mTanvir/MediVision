# `New Added` Folder — Complete Artifact Analysis

Analysis target: `E:\Defense\Discuss\New Added`

## Folder structure

The folder contains one substantive export directory, `untitled folder`, plus `__MACOSX` metadata. `__MACOSX` contains AppleDouble `._*` files and should be ignored; these are packaging metadata, not research artifacts.

Inside `untitled folder`:

- 2 pickle artifacts: `all_results.pkl`, `img_text_results.pkl`
- 6 JSON/metadata artifacts at the root: final results, audit results, fix results, two compliance files, Hugging Face repository metadata
- 1 preregistration text file
- 1 generated requirements freeze
- 11 PNG figures
- `medvision_final/`, which contains exact duplicate copies of the legacy final JSON, legacy compliance checklist and preregistration text

The expected `medvision_final.zip` is not present as a usable root artifact; only an AppleDouble metadata stub exists under `__MACOSX`.

## Result artifact integrity

`medvision_final_results.json`, `compliance_checklist.json`, `q1_audit_results.json` and `preregistration.txt` are byte-identical to the copies inside `medvision_final/` (SHA-256 comparison). The fixed-patch outputs are only at the root: `q1_fix_results.json`, `q1_fix_compliance_checklist_full.json`, `requirements.txt`, and the fixed figures.

## Pickle contents

### `all_results.pkl`

- Python dictionary with 40 entries.
- Exactly 5 variants × 8 seeds:
  - `baseline`
  - `lmh`
  - `noise_consistency`
  - `gacr_B`
  - `adaptive_cadq`
- Each entry has `history` and `test`.
- Test fields: accuracy, macro-F1, AUROC, per-class F1, per-class recall, predictions, labels, probabilities, confusion matrix and classification report.
- Test arrays are repeated for the same 455 test studies across different seeds; they must not be treated as 3,640 independent patients in inferential statistics.

### `img_text_results.pkl`

Three single-run controls:

- Image-only: Macro-F1 0.4611; AUROC 0.6728
- Text-only: Macro-F1 0.8555; AUROC 0.9820
- Gray-square + text: Macro-F1 0.9381; AUROC 0.9960

The gray-square control nearly matches the full baseline, so the result primarily demonstrates strong report/text signal rather than clear incremental image contribution.

## Per-variant performance

| Variant | Macro-F1 mean ± SD | PNX-F1 mean ± SD | AUROC mean ± SD |
|---|---:|---:|---:|
| Baseline | 0.9397 ± 0.0061 | 0.8810 ± 0.0174 | 0.99743 ± 0.00040 |
| LMH | 0.9435 ± 0.0093 | 0.9003 ± 0.0191 | 0.98487 ± 0.01129 |
| Noise-Consistency | 0.9346 ± 0.0075 | 0.8753 ± 0.0237 | 0.99601 ± 0.00131 |
| GACR-B | 0.9417 ± 0.0059 | 0.8880 ± 0.0167 | 0.99719 ± 0.00048 |
| Adaptive-CADQ | 0.9388 ± 0.0072 | 0.8772 ± 0.0175 | 0.99724 ± 0.00082 |

Best mean Macro-F1 is LMH, but the eight-seed Wilcoxon comparison against baseline is not significant (p=0.2500). GACR-B has a paired t-test p=0.0441 but exact Wilcoxon p=0.0547; after BH-FDR across 28 comparisons, no test remains below 0.05.

## Fixed statistical patch outputs

`q1_fix_results.json` contains seven sections: DeLong, McNemar, Wilson CI, multi-metric statistics, pooled permutation AUC, compliance summary and ten manuscript prose patches.

The patch correctly adds reporting machinery, but it also has implementation limitations:

1. DeLong and McNemar concatenate predictions from eight seeds. The test subjects are the same in each seed, so this is clustered/repeated data, not independent observations.
2. The pooled multi-seed permutation AUC repeats the same problem.
3. `metric_fns` reads `test['ece']` and `test['brier']`; those fields are absent from the pickle test dictionaries. Missing values become 0.0, producing p=1.0 and `nan` t-tests. ECE/Brier inference is therefore not valid in this output.
4. The Shapiro precheck is performed on baseline values, whereas a paired t-test requires checking the paired differences.
5. Gate values in the new figure are hard-coded constants copied into eight synthetic seed points, not re-extracted from each checkpoint.
6. Merge conflicts are resolved by first-seen value. Without a deterministic source-priority rule and a provenance manifest, conflicting upstream runs may be silently selected.

## Compliance assessment

Full checklist summary:

- CLAIM 2024: 13 YES, 10 PARTIAL, 4 NO
- TRIPOD+AI: 9 YES, 18 PARTIAL, 14 NO

The checklist appropriately marks external validation, power analysis, subgroup analysis, clinical impact, hyperparameter search, and other reporting items as incomplete. The legacy `compliance_checklist.json` is only an 11-item summary and should not replace the full checklist.

## Preregistration and provenance

`preregistration.txt` declares ICM as the primary outcome and predicts text circularity plus image-gate collapse. The actual gate values are approximately 0.426 (Normal), 0.500 (Pneumonia) and 0.573 (Pneumothorax), with mean alpha 0.4997. This is stagnation near initialization, not collapse to the 0.20 floor. The prediction therefore needs to be reported as a null/unsupported gate-collapse result.

The checklist itself discloses that Adaptive-CADQ was extended from three seeds to eight seeds post hoc. This must be stated explicitly in the manuscript.

`__huggingface_repos__.json` records Bio_ClinicalBERT repository commit `d5892b39a4adaed74b92212a44081509db72f87b`, useful for model provenance.

`requirements.txt` is a broad Kaggle environment freeze generated under Python 3.12.13. It includes many unrelated packages and is not a minimal reproducibility lockfile. A smaller project-specific requirements file should be generated from the actual imports and pinned CUDA/PyTorch/TorchXRayVision versions.

## Figure review

- `gate_stagnation_with_dots.png`: visually communicates alpha near 0.5 and far above the 0.2 floor, but dots are hard-coded and the legacy `gate_collapse.png` remains misleadingly named.
- `boxplots_with_strip_and_sig.png`: Macro-F1 and AUC panels are readable, but significance brackets extend above the natural metric range; ECE and Brier panels collapse to zero because of the missing-field bug.
- `roc_curves_with_ci.png`: useful per-class multi-seed display. Pneumothorax ROC shows a substantially lower LMH mean AUC than the other variants.
- `reliability_diagram.png`: baseline calibration appears close to the diagonal in the pooled display; however, pooling repeated subjects across seeds invalidates ordinary uncertainty interpretation.
- `circularity_evidence_bar.png`: correctly shows near-identical VLM and gray-square Macro-F1 and reports Wilcoxon p=0.4688.
- `confusion_matrices_normalised.png`: row-normalised matrices are interpretable. Pneumothorax recall is approximately baseline 89.36%, LMH 88.56%, Noise 92.82%, GACR-B 89.36%, Adaptive 90.16%.
- `gradcam_baseline.png`: provides three Pneumonia examples with heatmaps, but its interpretation depends on the unresolved XRV normalization warning and therefore should be treated as provisional.
- Legacy `f1_boxplots.png`, `confusion_matrices.png`, `roc_curves.png`, `gate_collapse.png`, `reliability_diagram.png` remain useful historical artifacts but should not be mixed with fixed-patch figures without clear version labels.

## Final scientific interpretation

The `New Added` folder is a result/audit export, not a new training dataset or new model-training notebook. Its strongest defensible conclusion is that all five reported fusion variants achieve high within-dataset performance, while the gray-square control shows that the incremental image contribution is very small. The fixed audit improves transparency and reporting coverage, but it does not resolve the core validity risks: report-label circularity, XRV normalization mismatch, negative-KL Noise-Consistency loss, degenerate one-token attention, image-only checkpoint selection, repeated-subject pooled inference, and missing ECE/Brier values in the new statistical table.

Before using these artifacts as final paper evidence, correct the training/evaluation code, rerun affected models, recompute calibration and clustered statistics, and preserve a deterministic provenance manifest for every merged result.

