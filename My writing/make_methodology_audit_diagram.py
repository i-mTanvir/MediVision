"""Create a publication-style methodology schematic for the MedVision audit.

The diagram is intentionally typeset with Matplotlib rather than generated as
an illustration: all labels, arrows, and coordinates are deterministic so the
figure remains legible and reproducible in a journal submission.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


OUT = Path(r"E:\Defense\Discuss\My writing\figures")
OUT.mkdir(parents=True, exist_ok=True)


NAVY = "#173F63"
TEAL = "#247C80"
AMBER = "#C17C1A"
RED = "#B33A3A"
INK = "#1F2937"
MUTED = "#52606D"
PALE_BLUE = "#F4F8FC"
PALE_TEAL = "#F2FAF9"
PALE_AMBER = "#FFF9ED"
PALE_RED = "#FFF5F4"
LINE = "#536272"


def add_stage(ax, x, y, w, h, number, title, color, title_size=12.5):
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.025,rounding_size=0.06",
            linewidth=1.2, edgecolor=color, facecolor="white", zorder=1,
        )
    )
    ax.add_patch(plt.Circle((x + 0.30, y + h - 0.36), 0.20, color=color, zorder=3))
    ax.text(x + 0.30, y + h - 0.36, str(number), ha="center", va="center",
            color="white", fontsize=11, fontweight="bold", zorder=4)
    ax.text(x + 0.62, y + h - 0.36, title, ha="left", va="center",
            color=color, fontsize=title_size, fontweight="bold", zorder=4)


def add_box(ax, x, y, w, h, title, lines, edge, fill, body_size=7.55,
            title_size=9.4, dashed=False):
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.018,rounding_size=0.045",
            linewidth=1.15, edgecolor=edge, facecolor=fill,
            linestyle=(0, (4, 2)) if dashed else "-", zorder=2,
        )
    )
    ax.text(x + 0.14, y + h - 0.22, title, ha="left", va="top",
            color=edge, fontsize=title_size, fontweight="bold", zorder=4)
    yy = y + h - 0.49
    for line in lines:
        ax.text(x + 0.14, yy, line, ha="left", va="top", color=INK,
                fontsize=body_size, zorder=4)
        yy -= 0.205


def add_arrow(ax, start, end, color=LINE, lw=1.25, dashed=False, rad=0.0):
    ax.add_patch(
        FancyArrowPatch(
            start, end, arrowstyle="-|>", mutation_scale=10,
            linewidth=lw, color=color,
            linestyle=(0, (4, 2)) if dashed else "-",
            connectionstyle=f"arc3,rad={rad}", zorder=3,
        )
    )


fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
fig.patch.set_facecolor("white")
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis("off")

ax.text(0.35, 9.70,
        "Methodology: auditing incremental image evidence under label-report circularity",
        ha="left", va="center", fontsize=16, fontweight="bold", color=NAVY)
ax.text(0.35, 9.38,
        "MIMIC-CXR-derived three-class task  |  fixed report text  |  seed-level inference",
        ha="left", va="center", fontsize=9.2, color=MUTED)

# Stage containers.
add_stage(ax, 0.35, 0.70, 4.35, 8.35, 1, "COHORT AND PROVENANCE", TEAL)
add_stage(ax, 4.88, 0.70, 5.10, 8.35, 2, "MODEL AND CONTROLLED CONDITIONS", NAVY,
          title_size=10.6)
add_stage(ax, 10.16, 0.70, 5.48, 8.35, 3, "EVALUATION AND AUDIT OUTPUTS", AMBER,
          title_size=11.8)

# Stage 1: data flow and the explicit provenance problem.
add_box(ax, 0.63, 6.95, 3.80, 1.35, "MIMIC-CXR cohort", [
    "2,962 candidates -> 2,953 usable studies",
    "Frontal radiographs only; patient-level split",
    "Train 2,049  |  validation 449  |  test 455",
    "Classes: Normal, Pneumonia, Pneumothorax",
], TEAL, PALE_TEAL, body_size=7.35)
add_box(ax, 0.63, 5.10, 3.80, 1.40, "Shared report provenance", [
    "CheXpert targets generated from report language",
    "Model text input = the same report's findings field",
    "Target and text therefore share an information source",
    "Audit target: report-linked shortcut potential",
], RED, PALE_RED, body_size=7.35)
add_box(ax, 0.63, 3.08, 3.80, 1.52, "Preprocessing", [
    "Image: resize 256 -> crop 224; one channel; [0,255] -> [-1,1]",
    "Text: BioClinicalBERT tokenizer; truncate/pad to 256 tokens",
    "Training: 10% text masking plus image augmentation",
    "Validation/test preprocessing deterministic",
], TEAL, PALE_TEAL, body_size=7.2)
add_box(ax, 0.63, 1.15, 3.80, 1.25, "Audit question", [
    "Does removing the image change performance?",
    "Do interventions increase incremental image evidence?",
    "Interpretation remains bounded to this report-linked task",
], AMBER, PALE_AMBER, body_size=7.3)

add_arrow(ax, (2.53, 6.95), (2.53, 6.52), color=TEAL)
add_arrow(ax, (2.53, 5.10), (2.53, 4.60), color=RED)
add_arrow(ax, (2.53, 3.08), (2.53, 2.40), color=TEAL)
add_arrow(ax, (3.95, 5.80), (4.95, 7.55), color=RED, dashed=True, rad=-0.16)

# Stage 2: representation, fusion, conditions, and controls.
add_box(ax, 5.17, 6.95, 4.52, 1.35, "Multimodal representation", [
    "Image branch: XRV DenseNet-121 -> 512-d feature",
    "Text branch: BioClinicalBERT -> 512-d feature",
    "One image token + one text token; 8-head attention",
    "Feature interaction, not word-region alignment",
], NAVY, PALE_BLUE, body_size=7.25)
add_box(ax, 5.17, 5.22, 4.52, 1.25, "Baseline CADQ fusion", [
    "Per-class gate: a_c = 0.20 + 0.60 sigmoid(u_c)",
    "z_c = a_c z_img + (1 - a_c) z_text",
    "Best validation Macro-F1 checkpoint restored",
], NAVY, PALE_BLUE, body_size=7.35)
add_box(ax, 5.17, 3.02, 4.52, 1.70, "Five evaluated conditions", [
    "CADQ baseline: gated dual-path fusion",
    "LMH: text-prior product-of-experts + calibration",
    "Noise-Consistency: archived negative-KL anti-consistency",
    "Adaptive-CADQ: entropy-driven sample gate",
    "GACR-B: exploratory grounding penalty (post hoc)",
], NAVY, PALE_BLUE, body_size=7.15)
add_box(ax, 5.17, 1.15, 4.52, 1.40, "Report-preserving controls", [
    "Gray-Square: constant intensity-128 image; report preserved",
    "Text-only control and image-only control",
    "Controls were retained single runs, not seed ensembles",
], AMBER, PALE_AMBER, body_size=7.25)

add_arrow(ax, (7.43, 6.95), (7.43, 6.47), color=NAVY)
add_arrow(ax, (7.43, 5.22), (7.43, 4.72), color=NAVY)
add_arrow(ax, (7.43, 3.02), (7.43, 2.55), color=NAVY)
add_arrow(ax, (4.43, 3.80), (5.17, 7.55), color=TEAL, lw=1.35, rad=-0.18)

# Stage 3: the statistical unit, endpoint, metrics, and reporting.
add_box(ax, 10.45, 6.95, 4.90, 1.35, "Evaluation design", [
    "455 held-out studies; eight seeds for five conditions",
    "40 model-seed records; controls are single retained runs",
    "The same test subjects recur across seeds",
    "Predictions, probabilities, gates, and metadata logged",
], AMBER, PALE_AMBER, body_size=7.35)
add_box(ax, 10.45, 5.25, 4.90, 1.22, "Primary diagnostic endpoint", [
    "Image Contribution Metric (ICM)",
    "ICM = (F1_VLM - F1_Gray) / F1_VLM",
    "TOST equivalence interval: [-0.01, 0.01]",
], RED, PALE_RED, body_size=7.45)
add_box(ax, 10.45, 3.55, 4.90, 1.28, "Secondary analyses", [
    "Macro-F1, accuracy, AUROC, per-class F1",
    "ECE, Brier score, confusion matrices",
    "Checkpoint gate extraction and qualitative Grad-CAM",
], AMBER, PALE_AMBER, body_size=7.35)
add_box(ax, 10.45, 1.92, 4.90, 1.25, "Seed-level inference", [
    "Paired Wilcoxon and t-tests; matched DeLong/McNemar",
    "Benjamini-Hochberg FDR; no pooling across seeds",
    "Pooled displays, if any, are explicitly exploratory",
], AMBER, PALE_AMBER, body_size=7.2)
add_box(ax, 10.45, 0.83, 4.90, 0.78, "Reproducibility and interpretation", [
    "Deterministic seeds, source provenance, corrected reruns, bounded claims",
], NAVY, PALE_BLUE, body_size=7.2, title_size=8.6)

add_arrow(ax, (12.90, 6.95), (12.90, 6.47), color=AMBER)
add_arrow(ax, (12.90, 5.25), (12.90, 4.83), color=RED)
add_arrow(ax, (12.90, 3.55), (12.90, 3.17), color=AMBER)
add_arrow(ax, (12.90, 1.92), (12.90, 1.61), color=AMBER)
add_arrow(ax, (9.69, 3.80), (10.45, 7.55), color=NAVY, lw=1.35, rad=-0.16)
add_arrow(ax, (9.69, 1.85), (10.45, 7.15), color=AMBER, lw=1.2, dashed=True, rad=-0.22)

# Audit guardrail: a single non-duplicative visual cue for the limitations that
# determine how the workflow may be interpreted.
ax.add_patch(FancyBboxPatch((0.62, 0.16), 14.73, 0.42,
                            boxstyle="round,pad=0.015,rounding_size=0.04",
                            linewidth=1.0, edgecolor=RED, facecolor=PALE_RED,
                            zorder=2))
ax.text(0.82, 0.37, "INTERPRETIVE GUARDRAIL", color=RED, fontsize=7.8,
        fontweight="bold", va="center", ha="left", zorder=4)
ax.text(3.02, 0.37,
        "label-report circularity  |  normalization and loss-sign checks  |  matched controls  |  no universal clinical claim",
        color=INK, fontsize=7.45, va="center", ha="left", zorder=4)
ax.text(15.35, 0.03, "solid arrows = data flow; dashed arrows = audit constraint",
        color=MUTED, fontsize=6.8, ha="right", va="bottom")

fig.savefig(OUT / "methodology_audit_workflow.pdf", bbox_inches="tight", pad_inches=0.08)
fig.savefig(OUT / "methodology_audit_workflow.png", dpi=600, bbox_inches="tight", pad_inches=0.08)
plt.close(fig)
print("Wrote", OUT / "methodology_audit_workflow.pdf")
print("Wrote", OUT / "methodology_audit_workflow.png")
