# Methodology reviewer audit

Target journal: *Informatics and Health*  
Authors: Nafis Al Rahman; Tanvir Mahmud  
Draft section: `Methodology.tex`

## Reviewer-facing strengths

- Defines the estimand as incremental image contribution rather than accuracy alone.
- Makes the report-derived label and report-input relationship explicit.
- Separates confirmatory eight-seed conditions from post-hoc GACR-B/Adaptive-CADQ additions.
- States the exact cohort accounting: 2,962 candidate rows, 9 missing images removed, 2,953 usable studies, and 2,049/449/455 split.
- Documents one-token attention as feature interaction rather than token-level grounding.
- Reports the negative-KL Noise-Consistency implementation instead of calling it a conventional consistency loss.
- Prevents repeated test subjects from being treated as independent across seeds.
- Requires ECE/Brier recomputation from retained probabilities and uses `N/A` for unavailable values.
- Treats TOST's +/-0.01 as an operational margin, not a clinical or regulatory threshold.

## Items to verify before accepting this section as final

1. Correct the XRV input normalization and rerun every affected model, or retain the current wording as an explicit limitation.
2. Correct the Noise-Consistency loss sign and rerun that condition if it will support a positive method claim.
3. Recompute confirmatory AUROC, McNemar, permutation, ECE, and Brier inference using seed-aware/cluster-aware procedures.
4. Extract baseline gate values directly from every checkpoint and regenerate the gate figure; do not use hard-coded arrays.
5. Resolve duplicate `variant_seed` entries with a deterministic source-priority and hash manifest.
6. Decide whether the archived image-only result is retained as descriptive evidence or replaced after checkpoint correction.
7. Confirm the exact MIMIC-CXR/MIMIC-CXR-JPG release and access date from the final data manifest.
8. Merge `methodology_references.bib` into the master bibliography after checking duplicate keys and journal-specific formatting.

## Citation audit

Every citation in the section is tied to a methodological claim: MIMIC-CXR provenance, CheXpert label generation, TorchXRayVision/DenseNet, BERT/ClinicalBERT, TOST, DeLong, McNemar, Benjamini--Hochberg, CLAIM, or TRIPOD+AI. No citation is used to support a clinical conclusion that the cited paper did not establish.
