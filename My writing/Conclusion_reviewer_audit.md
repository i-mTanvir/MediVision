# Conclusion section — reviewer audit

## Evidence alignment

- Restates only the principal result already documented in `Results.tex`: the
  Gray-Square control nearly matched baseline, ICM was near zero, and the gate
  remained near initialization.
- Keeps the conclusion tied to the report-linked MIMIC-CXR-derived task and the
  tested interventions.
- Distinguishes benchmark-level evidence from universal or causal claims.
- Does not introduce new data, p-values, figures, or citations.

## Reviewer-facing strengths

- Opens with the practical interpretation rather than repeating the full
  results table.
- Explains the label--report circularity as a supervision and endpoint issue.
- States the contribution of the ICM as a diagnostic audit measure, not a
  clinical-grounding certificate.
- Provides a focused validation agenda: corrected implementations, matched
  controls, independent labels, counterfactual text tests, provenance, and
  external validation.

## Claim boundary

The conclusion does not claim universal visual bypass, a non-functional image
pathway, or failure of all medical vision--language models. It is appropriate
for the current archive and should be revisited if corrected reruns materially
change the numerical findings.

## Final manuscript checks

1. Confirm that the final title and abstract use the same bounded wording.
2. Ensure the conclusion is placed after `Limitations.tex` and before reporting
   statements or supplementary material.
3. Reconcile the final conclusion with any corrected rerun, external validation,
   or independent-label sensitivity analysis.
