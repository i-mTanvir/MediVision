"""Create an image-assisted, publication-style methodology workflow.

The figure follows a clean four-stage medical-informatics workflow, while
embedding thumbnails from the project's actual figures. All labels and
connectors are typeset deterministically so the asset remains reproducible
and does not resemble an AI-generated infographic.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


ROOT = Path(r"E:\Defense\Discuss\My writing")
FIGURES = ROOT / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)
GRADCAM = ROOT.parent / "New Added" / "untitled folder" / "gradcam_baseline.png"
CIRCULARITY = ROOT.parent / "New Added" / "untitled folder" / "circularity_evidence_bar.png"


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


def rounded(ax, x, y, w, h, edge, fill="white", lw=1.1, dashed=False,
            radius=0.045, z=1):
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h,
            boxstyle=f"round,pad=0.018,rounding_size={radius}",
            linewidth=lw,
            edgecolor=edge,
            facecolor=fill,
            linestyle=(0, (4, 2)) if dashed else "-",
            zorder=z,
        )
    )


def stage(ax, x, y, w, h, number, title, color):
    rounded(ax, x, y, w, h, color, fill="white", lw=1.25, dashed=True, z=1)
    rounded(ax, x + 0.12, y + h - 0.62, w - 0.24, 0.42, color,
            fill={TEAL: "#EAF7F6", NAVY: "#EAF1F8", AMBER: "#FFF4DC", RED: "#FCEDEC"}[color],
            lw=0.7, radius=0.03, z=2)
    ax.add_patch(plt.Circle((x + 0.35, y + h - 0.41), 0.16, color=color, zorder=3))
    ax.text(x + 0.35, y + h - 0.41, str(number), ha="center", va="center",
            color="white", fontsize=9.5, fontweight="bold", zorder=4)
    ax.text(x + 0.60, y + h - 0.41, title, ha="left", va="center",
            color=color, fontsize=10.3, fontweight="bold", zorder=4)


def box(ax, x, y, w, h, title, lines, edge, fill, body_size=7.0,
        title_size=8.5, dashed=False):
    rounded(ax, x, y, w, h, edge, fill=fill, lw=1.0, dashed=dashed, z=2)
    ax.text(x + 0.13, y + h - 0.19, title, ha="left", va="top",
            color=edge, fontsize=title_size, fontweight="bold", zorder=5)
    yy = y + h - 0.46
    for line in lines:
        ax.text(x + 0.13, yy, line, ha="left", va="top", color=INK,
                fontsize=body_size, zorder=5)
        yy -= 0.20


def arrow(ax, start, end, color=INK, lw=1.25, dashed=False, rad=0.0,
          mutation=10):
    ax.add_patch(
        FancyArrowPatch(
            start, end, arrowstyle="-|>", mutation_scale=mutation,
            linewidth=lw, color=color,
            linestyle=(0, (4, 2)) if dashed else "-",
            connectionstyle=f"arc3,rad={rad}", zorder=6,
        )
    )


def image_panel(ax, path, x, y, w, h, border, label, crop=None):
    rounded(ax, x, y, w, h, border, fill="white", lw=0.9, z=3)
    try:
        image = plt.imread(path)
        if crop is not None:
            h_img, w_img = image.shape[:2]
            x0, x1, y0, y1 = crop
            image = image[int(y0 * h_img):int(y1 * h_img),
                          int(x0 * w_img):int(x1 * w_img)]
        ax.imshow(image, extent=(x + 0.07, x + w - 0.07, y + 0.29, y + h - 0.08),
                  aspect="auto", interpolation="bilinear", zorder=4)
    except (FileNotFoundError, OSError):
        ax.text(x + w / 2, y + h / 2, "image unavailable", ha="center", va="center",
                color=MUTED, fontsize=7, zorder=4)
    ax.text(x + 0.08, y + 0.11, label, ha="left", va="center",
            color=MUTED, fontsize=6.2, zorder=5)


fig, ax = plt.subplots(figsize=(18, 10), dpi=300)
fig.patch.set_facecolor("white")
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)
ax.axis("off")

ax.text(0.30, 9.67,
        "Methodology workflow: auditing incremental image evidence under label-report circularity",
        ha="left", va="center", fontsize=15.2, fontweight="bold", color=NAVY)
ax.text(0.30, 9.36,
        "MIMIC-CXR three-class task  |  fixed report text  |  matched controls  |  seed-level inference",
        ha="left", va="center", fontsize=8.8, color=MUTED)

# Four stage containers. The layout mirrors a conventional clinical-informatics
# workflow while keeping every data-flow arrow horizontal and unambiguous.
stage(ax, 0.24, 0.82, 4.20, 8.22, 1, "DATA & PROVENANCE", TEAL)
stage(ax, 4.58, 0.82, 4.20, 8.22, 2, "ENCODING", NAVY)
stage(ax, 8.92, 0.82, 4.20, 8.22, 3, "FUSION & CONDITIONS", AMBER)
stage(ax, 13.26, 0.82, 4.48, 8.22, 4, "EVALUATION & AUDIT", RED)

# Stage 1: real project image plus the provenance and preprocessing logic.
rounded(ax, 0.50, 5.20, 3.68, 2.55, TEAL, fill=PALE_TEAL, lw=1.0, z=2)
ax.text(0.64, 7.54, "MIMIC-CXR cohort", ha="left", va="top",
        color=TEAL, fontsize=8.8, fontweight="bold", zorder=5)
image_panel(ax, GRADCAM, 0.64, 5.50, 1.22, 1.64, TEAL,
            "frontal radiograph / source image", crop=(0.02, 0.32, 0.08, 0.51))
cohort_lines = [
    "2,962 -> 2,953 usable studies",
    "Train 2,049 | Val 449 | Test 455",
    "Classes: Normal | Pneumonia |",
    "Pneumothorax",
    "Patient-level split; held-out test",
]
yy = 7.09
for line in cohort_lines:
    ax.text(2.01, yy, line, ha="left", va="top", color=INK, fontsize=6.85, zorder=5)
    yy -= 0.23

box(ax, 0.50, 3.55, 3.68, 1.28, "Shared report provenance", [
    "CheXpert targets <- report language",
    "Model text <- the same report findings field",
    "Target and text share one information source",
    "Audit target: report-linked shortcut potential",
], RED, PALE_RED, body_size=6.85, title_size=8.4, dashed=True)
box(ax, 0.50, 1.28, 3.68, 1.78, "Deterministic preprocessing", [
    "Image: 256 -> crop 224; one channel; [0,255] -> [-1,1]",
    "Text: BioClinicalBERT tokenizer; 256-token limit",
    "Training: 10% text masking plus image augmentation",
    "Validation/test preprocessing deterministic",
], TEAL, PALE_TEAL, body_size=6.65, title_size=8.4)
arrow(ax, (2.34, 5.20), (2.34, 4.83), color=TEAL)
arrow(ax, (2.34, 3.55), (2.34, 3.06), color=RED, dashed=True)

# Stage 2: paired encoder streams and explicit one-token limitation.
box(ax, 4.84, 5.20, 3.68, 2.55, "Image + text encoding", [
    "Paired inputs: frontal image and fixed findings text",
    "Image branch: XRV DenseNet-121 -> z_img (512-d)",
    "Text branch: BioClinicalBERT -> z_text (512-d)",
], NAVY, PALE_BLUE, body_size=6.85, title_size=8.55)
# Small token lanes make the representation path visible without decorative icons.
ax.add_patch(Rectangle((5.02, 5.48), 1.18, 0.30, facecolor="#D9EAF5", edgecolor=NAVY, lw=0.7, zorder=4))
ax.add_patch(Rectangle((6.34, 5.48), 1.18, 0.30, facecolor="#E1F2F0", edgecolor=TEAL, lw=0.7, zorder=4))
ax.text(5.61, 5.63, "image token", ha="center", va="center", fontsize=6.4, color=NAVY, zorder=5)
ax.text(6.93, 5.63, "text token", ha="center", va="center", fontsize=6.4, color=TEAL, zorder=5)
arrow(ax, (6.20, 5.63), (6.32, 5.63), color=MUTED, lw=0.9)

box(ax, 4.84, 1.28, 3.68, 3.25, "Feature interaction", [
    "8-head attention over one image token + one text token",
    "Fused representation is used for classification",
    "Interaction, not word-region alignment",
    "Image and text paths remain separately auditable",
], NAVY, PALE_BLUE, body_size=6.8, title_size=8.55)
rounded(ax, 5.06, 2.36, 3.24, 0.84, NAVY, fill="white", lw=0.75, z=3)
ax.text(5.20, 2.95, "attention / feature interaction", ha="left", va="top",
        color=NAVY, fontsize=7.0, fontweight="bold", zorder=5)
for i, label in enumerate(["img", "text", "fused"]):
    xx = 5.27 + i * 0.92
    ax.add_patch(plt.Circle((xx, 2.59), 0.12, color=[TEAL, AMBER, NAVY][i], zorder=4))
    ax.text(xx, 2.59, label, ha="center", va="center", color="white", fontsize=5.2, zorder=5)
arrow(ax, (6.68, 5.20), (6.68, 4.55), color=NAVY)
arrow(ax, (6.68, 2.36), (6.68, 2.08), color=NAVY)

# Stage 3: gate equation, interventions, and matched controls.
box(ax, 9.18, 5.20, 3.68, 2.55, "CADQ fusion + interventions", [
    "Per-class gate: a_c = 0.20 + 0.60 sigmoid(u_c)",
    "z_c = a_c z_img + (1 - a_c) z_text",
    "Best validation Macro-F1 checkpoint restored",
], AMBER, PALE_AMBER, body_size=6.75, title_size=8.35)
rounded(ax, 9.36, 5.47, 3.31, 0.55, AMBER, fill="white", lw=0.75, z=3)
ax.text(11.02, 5.75, "gate -> fused logits -> classifier", ha="center", va="center",
        color=AMBER, fontsize=7.0, fontweight="bold", zorder=5)
box(ax, 9.18, 3.17, 3.68, 1.47, "Five evaluated conditions", [
    "CADQ baseline | LMH text-prior PoE + calibration",
    "Noise-Consistency: archived negative-KL anti-consistency",
    "Adaptive-CADQ | GACR-B grounding penalty (post hoc)",
], AMBER, PALE_AMBER, body_size=6.25, title_size=8.3)
box(ax, 9.18, 1.28, 3.68, 1.48, "Report-preserving controls", [
    "Gray-Square: intensity-128 image; report preserved",
    "Text-only and image-only controls",
    "Single retained runs; no seed ensembles",
], RED, PALE_RED, body_size=6.45, title_size=8.2)
# The gray-square is an explicit visual control, not a decorative icon.
ax.add_patch(Rectangle((12.28, 1.36), 0.30, 0.30, facecolor="#808080", edgecolor=RED, lw=0.8, zorder=4))
arrow(ax, (11.02, 5.20), (11.02, 4.64), color=AMBER)
arrow(ax, (11.02, 3.17), (11.02, 2.78), color=AMBER)

# Stage 4: actual audit-output thumbnail plus the statistical unit and endpoint.
rounded(ax, 13.52, 5.20, 3.96, 2.55, RED, fill=PALE_RED, lw=1.0, z=2)
ax.text(13.68, 7.54, "Held-out evaluation", ha="left", va="top",
        color=RED, fontsize=8.75, fontweight="bold", zorder=5)
image_panel(ax, CIRCULARITY, 13.68, 5.46, 1.60, 1.72, RED, "audit-output example")
eval_lines = [
    "455 held-out studies",
    "Eight seeds x five conditions",
    "40 model-seed records",
    "Same subjects recur across seeds",
    "No subject-pooled significance",
]
yy = 7.10
for line in eval_lines:
    ax.text(15.42, yy, line, ha="left", va="top", color=INK, fontsize=6.55, zorder=5)
    yy -= 0.22

box(ax, 13.52, 3.25, 3.96, 1.50, "Primary endpoint + secondary analyses", [
    "ICM = (F1_VLM - F1_Gray) / F1_VLM",
    "TOST equivalence interval: [-0.01, 0.01]",
    "Macro-F1, accuracy, AUROC, per-class F1, ECE, Brier",
], RED, PALE_RED, body_size=6.55, title_size=8.2)
box(ax, 13.52, 1.28, 3.96, 1.56, "Seed-level inference + interpretation", [
    "Paired Wilcoxon/t-tests; matched DeLong/McNemar",
    "Benjamini-Hochberg FDR; pooled displays exploratory",
    "Deterministic seeds, provenance, corrected reruns, bounded claims",
], NAVY, PALE_BLUE, body_size=6.45, title_size=8.2)
arrow(ax, (15.50, 5.20), (15.50, 4.75), color=RED)
arrow(ax, (15.50, 3.25), (15.50, 2.84), color=RED)

# Main horizontal data-flow connectors. They terminate on actual panel edges.
arrow(ax, (4.18, 6.47), (4.84, 6.47), color=TEAL, lw=1.45)
arrow(ax, (8.52, 6.47), (9.18, 6.47), color=NAVY, lw=1.45)
arrow(ax, (12.86, 6.47), (13.52, 6.47), color=AMBER, lw=1.45)

# A single, non-duplicative interpretive guardrail spans the workflow.
rounded(ax, 0.50, 0.20, 16.98, 0.42, RED, fill=PALE_RED, lw=1.0, z=2)
ax.text(0.70, 0.41, "INTERPRETIVE GUARDRAIL", color=RED, fontsize=7.2,
        fontweight="bold", va="center", ha="left", zorder=5)
ax.text(2.78, 0.41,
        "label-report circularity | normalization and loss-sign checks | matched controls | no universal clinical claim",
        color=INK, fontsize=6.75, va="center", ha="left", zorder=5)
ax.text(17.48, 0.04, "solid arrows = data flow; dashed borders = audit constraints",
        color=MUTED, fontsize=6.1, ha="right", va="bottom")

out_pdf = FIGURES / "methodology_audit_workflow_visual_v2.pdf"
out_png = FIGURES / "methodology_audit_workflow_visual_v2.png"
fig.savefig(out_pdf, bbox_inches="tight", pad_inches=0.08)
fig.savefig(out_png, dpi=600, bbox_inches="tight", pad_inches=0.08)
plt.close(fig)
print("Wrote", out_pdf)
print("Wrote", out_png)
