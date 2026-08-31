# Results reviewer audit

Target journal: *Informatics and Health*  
Authors: Nafis Al Rahman; Tanvir Mahmud  
Draft section: `Results.tex`

## Evidence used

- `all_results.pkl`: 40 variant-seed records, each with 455 test labels,
  predictions, and probability arrays.
- `img_text_results.pkl`: one retained output for each of the image-only,
  text-only, and Gray-Square controls.
- `q1_audit_results.json`: eight extracted baseline gate records and ICM
  values.
- Fixed-merge figures copied into `figures/`; the circularity contrast figure
  was regenerated without the misleading pooled Wilcoxon annotation.

## Reviewer-facing strengths

- Reports mean +/- SD across eight seeds rather than presenting one favorable
  run as the primary result.
- Separates confirmatory conditions from post-hoc GACR-B.
- Recomputes ECE and multiclass Brier from retained probabilities instead of
  converting missing values to zero.
- Uses seed-level paired tests and explicitly disallows repeated-subject
  concatenation for confirmatory inference.
- Reports both signed testing and TOST equivalence for the ICM.
- Treats Gray-Square and other controls as single retained outputs and avoids
  calling them seed ensembles.
- Reframes gate collapse as gate stagnation and reports actual checkpoint
  extraction values.
- Uses figures with captions that state when a display is descriptive or
  exploratory.

## Mandatory verification before submission

1. Re-run all confirmatory comparisons after correcting the TorchXRayVision
   input normalization and the Noise-Consistency negative-KL sign.
2. Generate a deterministic source-priority rule and hash manifest for merged
   result files; rerun the tables if any selected record changes.
3. Re-run Gray-Square, image-only, and text-only controls at all eight seeds if
   seed-level control inference is required.
4. Correct the archived image-only checkpoint-selection logic before using its
   result as anything more than descriptive evidence.
5. Verify the exact MIMIC-CXR/MIMIC-CXR-JPG release and access date from the
   final data manifest.
6. Regenerate ROC and reliability figures from a cluster-aware procedure if
   they will be presented as inferential rather than descriptive.
7. Confirm every numerical value against the final locked result archive and
   merge the section's references only after duplicate-key checking.

## Claim boundary

The Results section supports a cohort-specific finding: real-image replacement
by a report-preserving Gray-Square control produced nearly identical Macro-F1,
while the baseline image gate stayed near initialization. It does not support
the stronger claims that the image branch is universally non-functional, that
the model never uses visual information, or that the result is regulatory-grade.
