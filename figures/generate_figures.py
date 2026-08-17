"""Generate publication-oriented QBS figures from committed source data.

Outputs are SVG so they remain diffable and scalable. The script intentionally
uses only repository data or deterministic theorem illustrations. Plotted toy
quantities are not physical Everett observables.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "figures" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "legend.fontsize": 9,
    "figure.dpi": 160,
    "savefig.bbox": "tight",
    "svg.hashsalt": "qbs-v0.2",
})


def save(fig, name):
    fig.savefig(OUT / name, format="svg", metadata={"Date": None})
    plt.close(fig)


def fig1_framework():
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    ax.set_axis_off()
    nodes = {
        "Recognition\n$R$": (0.10, 0.55),
        "Policy\n$\\pi_R$": (0.32, 0.55),
        "Trajectory\n$U_R$": (0.57, 0.72),
        "Accessibility\n$S_R$": (0.57, 0.38),
        "First-person\nconditional value": (0.84, 0.55),
    }
    for label, (x, y) in nodes.items():
        ax.text(x, y, label, ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.45", fc="white", ec="black"))
    arrows = [
        ((0.16, 0.55), (0.26, 0.55)),
        ((0.38, 0.58), (0.50, 0.69)),
        ((0.38, 0.52), (0.50, 0.41)),
        ((0.64, 0.69), (0.77, 0.59)),
        ((0.64, 0.41), (0.77, 0.51)),
    ]
    for p0, p1 in arrows:
        ax.annotate("", xy=p1, xytext=p0,
                    arrowprops=dict(arrowstyle="->", lw=1.4))
    ax.text(
        0.5,
        0.08,
        "Mathematical model: recognition may change both branch-wise trajectories and observer-indexed accessibility.",
        ha="center",
        va="center",
    )
    save(fig, "fig1_framework.svg")


def weighted_cdf(grid, density, weight):
    dx = grid[1] - grid[0]
    w = density * weight
    cdf = np.cumsum(w) * dx
    return cdf / cdf[-1]


def fig2_fosd():
    x = np.linspace(-4.0, 4.0, 4001)
    phi = np.exp(-x * x / 2.0) / np.sqrt(2.0 * np.pi)
    base = weighted_cdf(x, phi, np.ones_like(x))
    monotone_s = 0.1 + 0.9 / (1.0 + np.exp(-2.0 * x))
    middle_s = 0.1 + 0.9 * np.exp(-(x / 0.9) ** 2)
    fp_mono = weighted_cdf(x, phi, monotone_s)
    fp_middle = weighted_cdf(x, phi, middle_s)

    pd.DataFrame({
        "x": x,
        "base_cdf": base,
        "fp_monotone_cdf": fp_mono,
        "fp_nonmonotone_cdf": fp_middle,
    }).to_csv(DATA / "fig2_fosd_theorem_illustration.csv", index=False)

    fig, ax = plt.subplots(figsize=(7.2, 4.5))
    ax.plot(x, base, label="Base distribution")
    ax.plot(x, fp_mono, label="FP: monotone accessibility")
    ax.plot(x, fp_middle, label="FP: nonmonotone accessibility")
    ax.set_xlabel("Outcome x")
    ax.set_ylabel("CDF")
    ax.set_title("FOSD requires monotone outcome-aligned accessibility")
    ax.legend()
    ax.grid(alpha=0.2)
    save(fig, "fig2_fosd.svg")


def fig3_recognition():
    d = pd.read_csv(DATA / "e3_recognition_decomposition_reproduction.csv").iloc[0]
    labels = ["Policy", "QBS", "Total"]
    vals = [d["policy_gain"], d["QBS_gain"], d["total_gain"]]
    fig, ax = plt.subplots(figsize=(6.3, 4.2))
    ax.bar(labels, vals)
    ax.axhline(0, linewidth=0.8)
    ax.set_ylabel("First-person value difference")
    ax.set_title("Recognition decomposition on paired primitive branches")
    for i, value in enumerate(vals):
        ax.text(i, value, f"{value:.3f}", ha="center", va="bottom")
    save(fig, "fig3_recognition_decomposition.svg")


def fig4_interaction():
    d = pd.read_csv(DATA / "e4_fixed_selector_sign_reproduction.csv")
    fig, ax = plt.subplots(figsize=(6.7, 4.2))
    ax.bar(d["policy"], d["interaction"])
    ax.axhline(0, linewidth=0.8)
    ax.set_ylabel("Policy–QBS interaction")
    ax.set_title("Interaction sign follows Cov(D,S)")
    for i, value in enumerate(d["interaction"]):
        ax.text(
            i,
            value + (0.008 if value >= 0 else -0.015),
            f"{value:.3f}",
            ha="center",
            va="bottom" if value >= 0 else "top",
        )
    save(fig, "fig4_interaction_sign.svg")


def fig5_adaptation():
    d = pd.read_csv(DATA / "qbs_adaptation_total_effect_summary.csv")
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.plot(d["adaptation_accuracy_p"], d["policy_effect"], marker="o", label="Policy effect")
    ax.plot(d["adaptation_accuracy_p"], d["QBS_after"], marker="o", label="QBS marginal after policy")
    ax.plot(d["adaptation_accuracy_p"], d["interaction"], marker="o", label="Interaction")
    ax.plot(d["adaptation_accuracy_p"], d["total_FP_effect"], marker="o", label="Total FP effect")
    ax.axhline(0, linewidth=0.8)
    ax.set_xlabel("Adaptation targeting accuracy p")
    ax.set_ylabel("Effect size")
    ax.set_title("Better adaptation can raise total value while increasing substitution")
    ax.legend()
    ax.grid(alpha=0.2)
    save(fig, "fig5_adaptation_quality.svg")


def fig6_branch_coherence():
    d = pd.read_csv(DATA / "e5_rho_paired_reproduction.csv")
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.plot(
        d["rho_env"],
        d["recognition_corr_increment"],
        marker="o",
        label="Recognition-induced action-correlation increment",
    )
    ax.plot(
        d["rho_env"],
        d["total_FP_gain"],
        marker="o",
        label="Single-observer total FP gain",
    )
    ax.set_xlabel("Shared environmental correlation")
    ax.set_ylabel("Simulation quantity")
    ax.set_title("Cross-branch coherence and marginal FP uplift are distinct")
    ax.legend()
    ax.grid(alpha=0.2)
    save(fig, "fig6_branch_coherence.svg")


if __name__ == "__main__":
    fig1_framework()
    fig2_fosd()
    fig3_recognition()
    fig4_interaction()
    fig5_adaptation()
    fig6_branch_coherence()
    print(f"Generated figures in {OUT}")
