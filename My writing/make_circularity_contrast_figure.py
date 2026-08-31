from pathlib import Path
import pickle

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(r"E:\Defense\Discuss\New Added\untitled folder")
OUT = Path(r"E:\Defense\Discuss\My writing\figures\circularity_contrast.png")
SEEDS = [42, 123, 456, 789, 1010, 1111, 1212, 1313]

with (ROOT / "all_results.pkl").open("rb") as handle:
    all_results = pickle.load(handle)
with (ROOT / "img_text_results.pkl").open("rb") as handle:
    controls = pickle.load(handle)

vlm = np.array(
    [all_results[f"baseline_s{seed}"]["test"]["macro_f1"] for seed in SEEDS],
    dtype=float,
)
gray = float(controls["gray_square"]["macro_f1"])

fig, ax = plt.subplots(figsize=(6.4, 4.6), dpi=180)
x = np.arange(2)
ax.errorbar(
    x[0],
    vlm.mean(),
    yerr=vlm.std(ddof=1),
    fmt="o",
    markersize=8,
    capsize=5,
    color="#287a50",
    ecolor="#287a50",
    linewidth=1.5,
    label="mean +/- SD (8 seeds)",
)
ax.scatter(
    x[1],
    gray,
    s=70,
    color="#9bc9ad",
    edgecolor="black",
    linewidth=0.8,
    zorder=3,
    label="single retained control run",
)
rng = np.random.default_rng(11)
ax.scatter(x[0] + rng.uniform(-0.12, 0.12, len(vlm)), vlm, color="black", s=18, zorder=3)
ax.axhline(gray, color="#3d6b50", linestyle="--", linewidth=1.0, alpha=0.9)
ax.text(
    0.99,
    gray + 0.00045,
    f"Gray-square F1 = {gray:.4f}",
    ha="right",
    va="bottom",
    fontsize=8,
)
ax.set_xticks(x, ["Full CADQ\n(VLM)", "Gray-square\n(text preserved)"])
ax.set_ylabel("Macro-F1")
ax.set_ylim(0.91, 0.96)
ax.set_title("Report-preserving image ablation")
ax.grid(axis="y", alpha=0.25)
ax.legend(frameon=False, fontsize=8, loc="lower left")
fig.text(
    0.5,
    0.01,
    "Gray-square is one retained control run; no subject-pooled significance is shown.",
    ha="center",
    fontsize=7.5,
)
fig.tight_layout(rect=(0, 0.06, 1, 1))
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=300, bbox_inches="tight")
plt.close(fig)
print(OUT)
