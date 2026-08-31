# Discussion section — reviewer audit

## Scope and evidence used

The section is anchored to the corrected `Results.tex` and `Methodology.tex`.
It uses only retained notebook outputs and the established citation set; no
new numerical result or unsupported regulatory claim has been introduced.

## Strengths

- Separates the principal empirical finding (near-zero operational ICM) from
  the stronger claim that images are universally unused.
- Explains why report-derived CheXpert labels and the `findings` input create a
  label--report circularity risk rather than declaring the labels invalid.
- Interprets the Gray-Square, text-only, and image-only controls together.
- Identifies the LMH calibration penalty and the archived negative-KL
  Noise-Consistency implementation as mechanistic context, not as proof of a
  universal method failure.
- Names the one-token attention limitation and avoids using attention or
  Grad-CAM as causal grounding evidence.
- Recommends matched multi-seed controls, seed-level inference, deterministic
  provenance, independent labels, counterfactual text tests, and external
  validation.
- Keeps clinical interpretation bounded and distinguishes discrimination,
  calibration, and modality reliance.

## Claims deliberately avoided

- “Complete visual bypass,” “non-functional image pathway,” or “the gate
  received no gradient.”
- A claim that TOST proves clinical or regulatory equivalence.
- A claim that all text-debiasing methods are incoherent or that all medical
  VLMs ignore images.
- An unsupported assertion that current regulatory guidance mandates a specific
  visual-grounding test.

## Required checks before submission

1. Correct the TorchXRayVision input-normalisation compatibility and rerun the
   primary experiments.
2. Correct the Noise-Consistency loss sign if consistency, rather than
   divergence, is the intended hypothesis, then rerun it.
3. Train Gray-Square controls for the same eight seeds and propagate their
   uncertainty into ICM.
4. Repair and document image-only best-checkpoint restoration.
5. Add deterministic source-priority rules and a hash manifest for merged
   result artifacts.
6. Reconcile the final citation, figure, and supplementary-material archive
   before submission.

## Reviewer decision risk

The Discussion is suitable as a bounded interpretation of the current audit,
but a reviewer can reasonably request corrected reruns and independent-label
validation before accepting a causal image-grounding conclusion.
