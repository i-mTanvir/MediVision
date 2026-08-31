# MedVision JBI V2 — internal peer-review audit

Audit date: 1 September 2026

## Overall verdict

The V2 draft is structurally aligned with a Journal of Biomedical Informatics research article and is suitable for supervisor review. It is not yet scientifically ready for final submission. The manuscript now reports the archived experiment honestly, but several implementation and control defects require confirmatory reruns before the strongest modality-reliance claims can be presented as definitive.

## Journal and reporting fit

- The contribution is framed as a general biomedical-informatics evaluation problem: target provenance, shortcut learning, modality contribution, calibration, and reproducible auditing.
- The abstract is structured and quantitative; a Statement of Significance follows it.
- Numeric citations are ordered by first appearance and the bibliography contains 35 cited sources.
- The principal endpoint is visible in both a statistics table and the ICM/equivalence-band figure.
- Performance, calibration, paired tests, controls, gate extraction, cohort flow, uncertainty, and provenance are reported rather than left only in prose.
- CLAIM 2024 and TRIPOD+AI summaries are included as supplementary reporting audits.
- The manuscript stays below the working 6,000-word target under a conservative count.

## Strong features

1. The paper clearly separates predictive performance from incremental image contribution.
2. Label/report circularity is defined from the actual MIMIC-CXR and CheXpert provenance chain rather than treated as a generic bias claim.
3. Corrected seed-level statistics are used consistently: baseline ICM 0.0016 ± 0.0065, Wilcoxon p = 0.4219, and TOST p = 0.0040.
4. McNemar p = 1.000 is interpreted as balanced off-diagonal discordance, not as byte-identical predictions.
5. DeLong comparisons are described as within the retained matched seed-42 probability set; subjects are not pooled across seeds for inference.
6. Post-hoc experiments, the reused Gray-Square comparator, recovered GACR-B probabilities, merge provenance, and checkpoint asymmetries are disclosed.
7. Gate stability is presented as a diagnostic observation rather than proof of zero gradient or causal visual grounding.

## Required before submission

1. Rerun the affected image experiments with preprocessing verified against the selected TorchXRayVision weight convention.
2. Replace the archived negative-KL Noise-Consistency objective with the intended positive consistency loss and rerun it.
3. Train Gray-Square and image-only controls at every seed with a uniform best-checkpoint rule; propagate comparator uncertainty into ICM.
4. Rebuild the result archive with deterministic source priority, dataset/split hashes, checkpoint hashes, retained probability arrays, and a machine-readable provenance manifest.
5. If the claim is broadened beyond this benchmark audit, validate on an external cohort or on labels that are independent of the report text supplied to the model.
6. Add institutional affiliations, corresponding-author email, postal address, and any author identifiers required by the submission system; these details were not provided in the source material and were not invented.

## Editorial refinements recommended

- Confirm the exact current article type and portal word-count rule immediately before submission.
- Keep the title and conclusion scoped to the audited implementation and report-linked MIMIC-CXR setting.
- Supply an archived release/DOI only after the public repository is versioned; the current wording intentionally does not fabricate one.
- Have both authors verify the CRediT roles and generative-AI disclosure against their actual contributions and the journal policy at submission time.

## Decision simulation

Likely editorial outcome in its present form: **major revision before external submission**, driven by confirmatory experimental validity rather than manuscript organization. After the required reruns and provenance lock, the study has a coherent methodological contribution and a defensible fit with biomedical informatics evaluation and reproducibility.

