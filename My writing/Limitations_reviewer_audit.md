# Limitations section — reviewer audit

## Coverage

The section separates limitations into:

1. label provenance and cohort construction;
2. image preprocessing, loss implementation, and one-token architecture;
3. asymmetric control design and uncertainty;
4. merge provenance and post-hoc analysis history;
5. external and clinical generalisability; and
6. concrete mitigation commitments.

## Evidence discipline

- All numerical statements are consistent with `Results.tex` and
  `Methodology.tex`.
- The 47-test-case Pneumothorax count, 2,953 usable studies, 455-study test
  set, 40 merged model--seed records, and eight-seed inference are stated only
  as scope constraints.
- The Gray-Square control and image-only checkpoint issues are presented as
  uncertainty sources, not hidden or converted into definitive modality
  rankings.
- TOST is described as an operational equivalence analysis, not clinical or
  regulatory equivalence.
- No universal visual-bypass, causal grounding, or regulatory claim is made.

## Reviewer-facing strengths

- It acknowledges the label--report circularity directly and proposes
  independent labels and report-masking tests.
- It records the XRV normalization issue and negative-KL sign issue as rerun
  blockers.
- It explains why seed-level inference is conservative and why the single-run
  Gray-Square reference underestimates uncertainty.
- It distinguishes diagnostic usefulness of controls from modality ranking.
- It closes with an actionable release checklist rather than a generic future
  work paragraph.

## Required pre-submission actions

1. Correct preprocessing and the intended Noise-Consistency objective, then
   rerun the affected conditions.
2. Train Gray-Square and all controls across matched seeds with consistent
   checkpoint selection.
3. Freeze source-priority rules, hashes, configurations, and per-seed
   probabilities in a provenance manifest.
4. Add independent-label and external-cohort sensitivity analyses.
5. Reconcile the final limitations wording with the corrected rerun results;
   do not leave archive-specific caveats as unexplained contradictions.

## Claim boundary

The section supports a benchmark-level limitation statement: the current
report-linked audit cannot establish robust image grounding. It does not claim
that images are generally unnecessary or that every multimodal model has the
same failure mode.
