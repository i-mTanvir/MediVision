# Introduction section — reviewer audit

## Gap logic

The introduction establishes a practical evaluation gap: aggregate multimodal
metrics do not identify incremental image contribution when the target is
report-derived and the same report is supplied as input. It then links that gap
to the specific MIMIC-CXR/CheXpert setting and motivates a report-preserving
Gray-Square audit.

## Research questions covered

1. Whether removing image information while retaining the report changes
   performance.
2. Whether the tested fusion or text-debiasing interventions increase
   incremental image contribution.
3. Whether learned gate values support image reliance or collapse.
4. Whether calibration and class-specific behaviour qualify headline metrics.

## Evidence discipline

- MIMIC-CXR and CheXpert statements use the existing verified citations.
- No new performance number, p-value, or unsupported regulatory claim is
  introduced.
- “Text-debiasing” is framed as an evaluation problem under linked supervision,
  not as a universal failure of all methods.
- One-token attention and gate interpretation are bounded without claiming
  causal grounding.

## Reviewer-facing strengths

- Opens with a medical-informatics motivation and moves directly to the
  interpretive problem.
- Explains why report-derived labels can create label--report circularity
  without declaring the labels invalid.
- Defines the audit intervention, controls, ICM, seed-level replication, and
  research questions before discussing results.
- Ends with a clear claim boundary that aligns with Discussion, Limitations, and
  Conclusion.

## Final checks before submission

1. Confirm that the title uses the same bounded language as the final paragraph.
2. Add any approved literature from the final Related Work section only after
   verifying that it directly supports the claim being cited.
3. Ensure the final master includes `Introduction.tex` before Related Work and
   Methods, and remove preview-only `\nocite{*}` commands.
4. Revisit the wording if corrected preprocessing or independent-label reruns
   materially change the central result.
