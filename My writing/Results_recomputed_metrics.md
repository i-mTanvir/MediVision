# Recomputed Results metrics

These values were recomputed locally from `all_results.pkl` and
`img_text_results.pkl` in the fixed-merge archive. ECE uses ten equal-width
confidence bins. Multiclass Brier is the mean across studies of the summed
squared error between the three-class probability vector and the one-hot
label. Variant comparisons are paired by seed (`42, 123, 456, 789, 1010,
1111, 1212, 1313`).

## Seed means

| Condition | Macro-F1 | Accuracy | Macro-AUROC | ECE | Brier |
|---|---:|---:|---:|---:|---:|
| Baseline CADQ | 0.9397 +/- 0.0061 | 0.9607 +/- 0.0032 | 0.9974 +/- 0.0004 | 0.0237 +/- 0.0048 | 0.0522 +/- 0.0040 |
| LMH | 0.9435 +/- 0.0093 | 0.9596 +/- 0.0070 | 0.9849 +/- 0.0113 | 0.0621 +/- 0.0160 | 0.0685 +/- 0.0213 |
| Noise-Consistency | 0.9346 +/- 0.0075 | 0.9560 +/- 0.0039 | 0.9960 +/- 0.0013 | 0.0347 +/- 0.0137 | 0.0655 +/- 0.0130 |
| GACR-B | 0.9417 +/- 0.0059 | 0.9610 +/- 0.0042 | 0.9972 +/- 0.0005 | 0.0245 +/- 0.0023 | 0.0540 +/- 0.0038 |
| Adaptive-CADQ | 0.9388 +/- 0.0072 | 0.9610 +/- 0.0044 | 0.9972 +/- 0.0008 | 0.0241 +/- 0.0070 | 0.0527 +/- 0.0028 |

## Controls

| Control | Macro-F1 | Accuracy | Macro-AUROC | ECE | Brier |
|---|---:|---:|---:|---:|---:|
| Image-only | 0.4611 | 0.5670 | 0.6728 | 0.0993 | 0.6142 |
| Text-only | 0.8555 | 0.9077 | 0.9820 | 0.0203 | 0.1289 |
| Gray-Square | 0.9381 | 0.9604 | 0.9960 | 0.0369 | 0.0589 |

## Paired Wilcoxon p-values versus baseline

| Condition | Macro-F1 | Macro-AUROC | ECE | Brier |
|---|---:|---:|---:|---:|
| LMH | 0.2500 (FDR 0.3333) | 0.0078 (0.0104) | 0.0078 (0.0313) | 0.0078 (0.0156) |
| Noise-Consistency | 0.1953 (0.3333) | 0.0078 (0.0104) | 0.0781 (0.1563) | 0.0078 (0.0156) |
| GACR-B | 0.0547 (0.2188) | 0.0078 (0.0104) | 0.5469 (0.7292) | 0.0156 (0.0208) |
| Adaptive-CADQ | 0.8438 (0.8438) | 0.8438 (0.8438) | 0.7422 (0.7422) | 0.7422 (0.7422) |

The FDR values are Benjamini-Hochberg adjustments within each four-comparison
metric family. They are not subject-level p-values.
