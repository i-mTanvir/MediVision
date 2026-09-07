# MedVision Draft V1 Revision Plan

## Purpose

Create a journal-neutral master manuscript that preserves the verified MedVision results while improving readability, evidence flow, and later portability to a target journal. The existing JBI V2 files remain unchanged.

## Evidence rules

- Use the corrected V2 numerical set throughout.
- Use V9 only to recover useful coverage or explanation, not its outdated statistics or stronger causal claims.
- Cite only entries already supported by the two verified bibliography files.
- Treat the Gray-Square comparison and ICM as the primary modality audit.
- Treat gate extraction and Grad-CAM as supporting evidence.
- Preserve the single-control-run and seed-42 inference disclosures.

## Writing and layout plan

1. Use the short title `Auditing Image Use in Medical Vision Language Models`.
2. Use a journal-neutral A4 two-column layout with numbered references.
3. Remove the Statement of Significance from this version.
4. Expand the Introduction from clinical context to target provenance, audit gaps, and research questions.
5. Expand Related Work and add a comparison table covering representation learning, language-prior mitigation, and modality audits.
6. Reorganize Methods around cohort, estimand, architecture, conditions, training, outcomes, and statistics.
7. Retain only the A-C methodology artwork in Figure 1 and remove the separate D cohort panel.
8. Add a short overview before each major section and explain each display item in the body.
9. Keep figure and table captions concise and place composite-panel markers below the displayed panels where LaTeX controls them.
10. Expand Results and Discussion without changing verified findings or widening their claim boundary.
11. Retain reporting statements and supplementary audit tables.
12. Compile, check citations and references, render all pages, and inspect the final PDF.

## Completion status

All planned manuscript edits are implemented in `MedVision_Draft_V1.tex`. The final output is designed to remain near 22 pages before journal-specific reformatting.
