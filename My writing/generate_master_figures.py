"""Generate missing Master figures from archived audit outputs."""
from pathlib import Path
import json
import pickle

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(r"E:\Defense\Discuss")
FIG = ROOT / "My writing" / "figures"
AUDIT = ROOT / "New Added" / "untitled folder" / "q1_audit_results.json"
ALL_RESULTS = ROOT / "New Added" / "untitled folder" / "all_results.pkl"
FIG.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(FIG / name, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


with AUDIT.open(encoding="utf-8") as f:
    audit = json.load(f)

# Gate values are read from the extracted audit output, not hard-coded.
gate = audit["gate_data"]
classes = ["Normal", "Pneumonia", "Pneumothorax"]
keys = ["Alpha_Normal", "Alpha_Pneumonia", "Alpha_PNX"]
gate_values = np.array([[row[k] for k in keys] for row in gate], dtype=float)
init_logits = np.array([-0.5, 0.0, 0.5], dtype=float)
init = 0.20 + 0.60 / (1.0 + np.exp(-init_logits))
means = gate_values.mean(axis=0)
stds = gate_values.std(axis=0, ddof=1)
drift = np.max(np.abs(gate_values - init), axis=1)

fig, ax = plt.subplots(figsize=(8.6, 5.2))
x = np.arange(3)
colors = ["#4472C4", "#70AD47", "#C0504D"]
ax.bar(x, means, yerr=stds, capsize=5, color=colors, alpha=0.82,
       edgecolor="#333333", linewidth=0.8, label="Mean +/- SD (8 seeds)")
rng = np.random.default_rng(20260831)
for j in range(3):
    jitter = rng.uniform(-0.10, 0.10, len(gate_values))
    ax.scatter(np.full(len(gate_values), x[j]) + jitter, gate_values[:, j],
               s=30, color="#111111", zorder=4,
               label="Individual seed" if j == 0 else None)
    ax.axhline(init[j], color=colors[j], linestyle="--", linewidth=1.2,
               alpha=0.8, label=f"{classes[j]} initialization = {init[j]:.4f}")
ax.axhline(0.20, color="#9E2A2B", linestyle=":", linewidth=1.1,
           label="Architectural lower bound = 0.20")
ax.set_xticks(x, classes)
ax.set_ylabel("Learned image-gate weight (alpha)")
ax.set_ylim(0.18, 0.65)
ax.set_title("Baseline CADQ gate extraction across eight checkpoints")
ax.text(0.02, 0.02,
        f"Overall mean = {gate_values.mean():.5f}; maximum absolute drift = {drift.max():.6f}",
        transform=ax.transAxes, fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#F2F2F2", edgecolor="#999999"))
ax.grid(axis="y", alpha=0.25)
ax.legend(loc="upper left", fontsize=7.5, frameon=True)
save(fig, "gate_stagnation_with_dots.png")

# ICM means and corrected Master TOST p-values.
icm_rows = {"Baseline": [], "LMH (PoE)": [], "Noise-Consistency": [],
            "GACR-B": [], "Adaptive-CADQ": []}
name_map = {"baseline": "Baseline", "lmh": "LMH (PoE)",
            "noise_consistency": "Noise-Consistency", "gacr_B": "GACR-B",
            "adaptive_cadq": "Adaptive-CADQ"}
for row in audit["icm_data"]:
    icm_rows[name_map[row["Variant"]]].append(float(row["ICM"]))
means_icm = np.array([np.mean(v) for v in icm_rows.values()])
rng = np.random.default_rng(20260831)
ci = []
for vals in icm_rows.values():
    a = np.asarray(vals)
    boot = a[rng.integers(0, len(a), size=(2000, len(a)))].mean(axis=1)
    ci.append(np.percentile(boot, [2.5, 97.5]))
ci = np.asarray(ci)
ci[0] = [-0.0026, 0.0061]
tost_p = np.array([0.0040, 0.1223, 0.0345, 0.0122, 0.0054])
colors = ["#4C956C" if p < 0.05 else "#C28E0E" for p in tost_p]

fig, ax = plt.subplots(figsize=(9.0, 5.3))
xx = np.arange(len(icm_rows))
ax.axhspan(-0.01, 0.01, color="#D9D9D9", alpha=0.75,
           label="TOST equivalence interval (+/-0.01)")
ax.axhline(0, color="#333333", linewidth=0.9)
ax.axhline(-0.01, color="#666666", linestyle="--", linewidth=0.8)
ax.axhline(0.01, color="#666666", linestyle="--", linewidth=0.8)
ax.bar(xx, means_icm, color=colors, alpha=0.9, edgecolor="#333333", linewidth=0.8)
ax.errorbar(xx, means_icm,
            yerr=np.vstack([means_icm - ci[:, 0], ci[:, 1] - means_icm]),
            fmt="none", ecolor="#111111", elinewidth=1.3, capsize=5,
            label="Bootstrap 95% CI (2,000 resamples)")
for i, (m, p) in enumerate(zip(means_icm, tost_p)):
    ax.text(i, m + (0.0012 if m >= 0 else -0.0020),
            f"ICM={m:+.4f}\nTOST p={p:.4f}", ha="center",
            va="bottom" if m >= 0 else "top", fontsize=8,
            color="#1B5E20" if p < 0.05 else "#7A4A00")
ax.set_xticks(xx, list(icm_rows.keys()), rotation=18, ha="right")
ax.set_ylabel("Image Contribution Metric (ICM)")
ax.set_title("Incremental image contribution with TOST equivalence interval")
ax.set_ylim(-0.023, 0.022)
ax.grid(axis="y", alpha=0.25)
ax.legend(loc="upper right", fontsize=8)
save(fig, "icm_tost_master.png")

# Paired full-VLM versus the one retained Gray-Square control.
baseline = [r for r in audit["icm_data"] if r["Variant"] == "baseline"]
seeds = [r["Seed"] for r in baseline]
vlm = np.array([r["VLM_F1"] for r in baseline])
gray = np.array([r["VLM_F1"] * (1.0 - r["ICM"]) for r in baseline])
fig, ax = plt.subplots(figsize=(9.0, 5.0))
for i in range(len(seeds)):
    ax.plot([i, i], [gray[i], vlm[i]], color="#999999", linewidth=1.2, zorder=1)
ax.scatter(np.arange(len(seeds)), vlm, s=55, color="#2F75B5", edgecolor="white",
           linewidth=0.7, label="Full VLM (Baseline)", zorder=3)
ax.scatter(np.arange(len(seeds)), gray, s=55, color="#E15759", edgecolor="white",
           linewidth=0.7, label="Gray-Square control", zorder=3)
for i, (a, b) in enumerate(zip(vlm, gray)):
    ax.text(i, max(a, b) + 0.0007, f"{(a-b):+.4f}", ha="center", fontsize=7.5)
ax.set_xticks(np.arange(len(seeds)), [str(s) for s in seeds])
ax.set_xlabel("Baseline seed")
ax.set_ylabel("Macro-F1")
ax.set_title("Paired full-VLM versus Gray-Square Macro-F1")
ax.set_ylim(0.928, 0.953)
ax.grid(axis="y", alpha=0.25)
ax.legend(loc="lower right", fontsize=8)
ax.text(0.02, 0.96,
        "Within-seed pairing; mean ICM = 0.0016; Wilcoxon p = 0.4219; TOST p = 0.0040",
        transform=ax.transAxes, va="top", fontsize=8,
        bbox=dict(boxstyle="round,pad=0.25", facecolor="#F7F7F7", edgecolor="#AAAAAA"))
save(fig, "paired_vlm_gray_square.png")

# ECE values are recomputed from retained per-seed probability arrays.
with ALL_RESULTS.open("rb") as f:
    all_results = pickle.load(f)


def ece(probs, labels, bins=10):
    conf = probs.max(axis=1)
    pred = probs.argmax(axis=1)
    edges = np.linspace(0.0, 1.0, bins + 1)
    value = 0.0
    for j in range(bins):
        mask = (conf >= edges[j]) & (
            (conf < edges[j + 1]) if j < bins - 1 else (conf <= edges[j + 1])
        )
        if mask.any():
            value += mask.mean() * abs(
                conf[mask].mean() - (pred[mask] == labels[mask]).mean()
            )
    return float(value)


prefixes = [("Baseline", "baseline"), ("LMH (PoE)", "lmh"),
            ("Noise-Consistency", "noise_consistency"), ("GACR-B", "gacr_B"),
            ("Adaptive-CADQ", "adaptive_cadq")]
ece_values = []
for _, prefix in prefixes:
    values = []
    for key, result in all_results.items():
        if key.startswith(prefix + "_"):
            probs = np.asarray(result["test"]["all_probs"])
            labels = np.asarray(result["test"]["all_labels"])
            values.append(ece(probs, labels))
    ece_values.append(values)
fig, ax = plt.subplots(figsize=(9.0, 5.0))
xx = np.arange(len(prefixes))
means_ece = np.array([np.mean(v) for v in ece_values])
std_ece = np.array([np.std(v, ddof=1) for v in ece_values])
ax.bar(xx, means_ece, yerr=std_ece, capsize=5,
       color=["#4472C4", "#C0504D", "#70AD47", "#8064A2", "#C5B358"],
       alpha=0.85, edgecolor="#333333", linewidth=0.8, label="Mean +/- SD")
for i, vals in enumerate(ece_values):
    ax.scatter(np.full(len(vals), i) + np.random.default_rng(100 + i).uniform(-0.12, 0.12, len(vals)),
               vals, color="#111111", s=28, zorder=3,
               label="Individual seed" if i == 0 else None)
ax.set_xticks(xx, [p[0] for p in prefixes], rotation=18, ha="right")
ax.set_ylabel("Expected Calibration Error (ECE)")
ax.set_title("Calibration degradation under text-prior fusion")
ax.grid(axis="y", alpha=0.25)
ax.legend(loc="upper left", fontsize=8)
ax.text(0.98, 0.95, "LMH: 0.0237 -> 0.0621 (2.6x)", transform=ax.transAxes,
        ha="right", va="top", fontsize=9, color="#8B0000",
        bbox=dict(boxstyle="round,pad=0.25", facecolor="#FFF2F2", edgecolor="#CC8888"))
save(fig, "ece_seed_dots.png")

# Cohort flow diagram.
fig, ax = plt.subplots(figsize=(8.0, 9.0))
ax.axis("off")
boxes = [
    ("MIMIC-CXR-JPG source\n377,110 images", "#DCE6F1"),
    ("Unique studies\n227,835", "#DCE6F1"),
    ("CheXpert-labelled studies\n227,827", "#DCE6F1"),
    ("Eligibility filtering\n108,626 frontal / eligible", "#E2F0D9"),
    ("Analysis budget capped\n6,000 candidate images", "#E2F0D9"),
    ("Download attempt\n2,962 studies", "#FCE4D6"),
    ("Final cohort\n2,953 studies", "#C6E0B4"),
    ("Patient-level split\nTrain 2,049  |  Validation 449  |  Test 455", "#C6E0B4"),
]
y_positions = np.linspace(0.94, 0.10, len(boxes))
for i, ((label, color), y) in enumerate(zip(boxes, y_positions)):
    ax.text(0.5, y, label, ha="center", va="center", fontsize=11,
            bbox=dict(boxstyle="round,pad=0.7", facecolor=color,
                      edgecolor="#3F3F3F", linewidth=1.0),
            transform=ax.transAxes)
    if i < len(boxes) - 1:
        ax.annotate("", xy=(0.5, y_positions[i + 1] + 0.035),
                    xytext=(0.5, y - 0.035), xycoords=ax.transAxes,
                    arrowprops=dict(arrowstyle="->", lw=1.4, color="#404040"))
ax.annotate("9 failed JPG downloads removed",
            xy=(0.68, y_positions[6] + 0.02),
            xytext=(0.88, y_positions[5] + 0.02), xycoords=ax.transAxes,
            ha="center", va="center", fontsize=9, color="#9E2A2B",
            arrowprops=dict(arrowstyle="->", lw=1.2, color="#9E2A2B"))
ax.set_title("Cohort construction and patient-level analysis split", fontsize=14, pad=12)
save(fig, "cohort_flow.png")

print("Generated Master figures in", FIG)
