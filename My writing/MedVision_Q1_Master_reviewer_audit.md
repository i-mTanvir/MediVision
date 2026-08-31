# MedVision Q1 Master Manuscript — Integration Audit

## Build scope

The working master imports the approved section files in this order:

1. Introduction
2. Related Work
3. Methods
4. Results
5. Discussion
6. Limitations
7. Conclusion
8. Reporting statements

The master now includes a structured, citation-free abstract and six keywords
aligned with the current journal instructions.

## Integration checks completed

- CAS single-column class (`cas-sc`) compiles locally with the project helper script.
- Both related-work and methods BibTeX databases are loaded in one bibliography pass.
- `natbib` citation commands resolve in the integrated manuscript.
- All seven local figure assets are found through the `figures/` path and render in the output PDF.
- Figure and table placement uses the CAS key-value float syntax (`pos=htbp`) rather than the generic `H` specifier.
- The final 15-page build has no LaTeX errors, undefined citations, undefined references, or missing figures. A title-page overfull-box warning and a few underfull boxes from long FDA URLs remain; visual inspection showed no clipping or unreadable content.
- The integrated PDF was rendered to page images and representative text, table, figure, discussion, reporting, and bibliography pages were visually checked for clipping and missing assets.
- Abbreviations were audited for first-use definitions; the abstract retains only the defined ICM abbreviation, with the placement map documented in `Informatics_and_Health_abbreviation_audit.md`.

## Items requiring author confirmation before submission

- Confirm the institutional ethics-committee name and exemption/waiver reference, if required.
- The GitHub repository URL is now populated; add the archival DOI if a frozen release is deposited before submission.
- Confirm the author affiliation, ORCID values, CRediT roles, and any protocol identifiers.
- Cross-check venue, year, author, and DOI metadata for all references against the final source PDFs or publisher records.
- Review the title wording and decide whether “audit” or “empirical study” best matches the final scope.
- Before release, archive the exact notebook commit/hash, configuration files, figure-generation scripts, and deterministic merge manifest referenced by the manuscript.
- The section-level word-count audit is in `Informatics_and_Health_word_limit_audit.md`; after compression, the main narrative is approximately 3,676 words and the conservative rendered pre-bibliography count is approximately 4,923, both within the journal's 5,000-word Research Article limit.
- Figure 1 now uses the supplied four-stage methodology diagram, with a caption scoped to the implemented MIMIC-CXR audit. Figures 6--11 received a further modest size reduction while Figure 3 was left unchanged; the rebuilt 15-page PDF was checked for legibility, clipping, and caption placement. Tables S2--S4 are supplied in the separate one-page `MedVision_Q1_Supplementary.tex` companion; Table S1 remains in the main manuscript.
- The current source still uses author--year `natbib` output for readability during drafting. Before submission, convert citations and the bibliography to the journal's required superscript numeric AMA style and re-run the reference-order audit.

## Interpretation boundary preserved

The master retains the bounded conclusion that a report-preserving Gray-Square intervention and near-zero ICM diagnose possible modality--endpoint mismatch in this report-linked cohort. It does not claim universal image bypass, clinical invalidity of report-conditioned prediction, or general behaviour of all medical vision--language models.
