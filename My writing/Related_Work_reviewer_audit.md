# Related Work — Reviewer Audit

## Scope and evidence base

This section was drafted against the local 25-paper reference synthesis, the corresponding PDFs in `E:\Defense\Discuss\Referances`, the verified MedVision source documents, and the existing foundational bibliography used for the Methods section. The literature is organized around the paper's actual claim: whether text-debiasing produces genuine image reliance when the prediction target is itself derived from radiology reports.

## Coverage check

- **Medical image–text learning and report-derived targets:** ConVIRT, GLoRIA, biomedical report semantics, MIMIC-CXR, CheXpert, and NLP label-bias work are used to establish how image–text pretraining and report-derived supervision can be useful while also coupling labels to language.
- **Shortcut learning and unimodal bias:** The section connects general shortcut-learning findings, radiology shortcut evidence, VQA bias, product-of-experts/ensemble behavior, and RUBi-style debiasing to the specific possibility of a report shortcut in MedVision.
- **Audits of image use:** Recent image-use and reliance audits are summarized, including the closest prior work by Lotfinia et al.; the present study is positioned as a narrower, controlled audit rather than a “first” claim.
- **Fusion gates, explanations, and reasoning traces:** Gated multimodal fusion, counterfactual prototype methods, and reasoning-CXR work are discussed with an explicit distinction between an interpretable interface and evidence of causal image grounding.
- **Positioning:** The unresolved intersection is stated explicitly: report-derived CheXpert targets, exposure to the findings field, train-time text-debiasing, Gray-Square image intervention, ICM/TOST equivalence evidence, gate inspection, calibration, and seed-level uncertainty.

## Citation and claim-discipline audit

1. No novelty claim uses “first.” The closest prior image-use audit is acknowledged and the contribution is scoped to the MedVision/CheXpert setting and its intervention-based evaluation.
2. MIMIC-CXR is treated as the dataset and CheXpert as the report-derived labeler; the two are not conflated.
3. Claims about shortcut learning, VQA bias, gated fusion, and explanation limits are supported by directly relevant references rather than by the MedVision results bibliography alone.
4. No new numerical result is introduced in Related Work. All MedVision-specific numbers remain in Results and Methods.
5. Local arXiv/preprint records are retained where that is the available source. Before submission, venue, year, DOI, and author metadata should be cross-checked against the final published records for every reference.
6. The preview uses `\nocite{*}` only to expose the complete bibliography during QA. The production master should remove that command and cite only works that directly support its claims.

## Reviewer-facing strengths

- The section moves from enabling literature to failure modes, then to auditing methods and the study's precise gap; this avoids a disconnected paper-by-paper catalogue.
- It explains why high performance, a fusion gate, attention, or a fluent reasoning trace cannot independently establish image grounding.
- It makes the label/report circularity issue central without implying that all report supervision is invalid.
- It separates the present controlled audit from broad claims about all medical VLMs.

## Final checks before master integration

- Verify every DOI, venue, and publication status against the final reference PDFs or publisher records.
- Merge duplicate BibTeX keys with `methodology_references.bib` and preserve one canonical record per work.
- Replace preview-only `\nocite{*}` with the exact citation set used by the complete manuscript.
- Re-check that each paragraph's citations support the sentence-level claim and that no 2026 preprint is described as peer-reviewed unless verified.
- Keep the closest-prior comparison and bounded contribution statement when shortening for the journal's final word limit.
