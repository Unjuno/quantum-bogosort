"""Generate PDF versions of the six QBS publication figures for LaTeX.

The committed SVGs remain the GitHub-readable canonical previews. These PDFs are
build products generated from the same committed data and deterministic theorem
illustrations for manuscript inclusion.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "figures" / "generated_pdf"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, format="pdf", bbox_inches="tight")
    plt.close(fig)


def fig1_framework():
    fig, ax = plt.subplots(figsize=(8.0, 3.6))
    ax.set_axis_off()
    boxes = {
        "Recognition\n$R$": (0.08, 0.50),
        "Policy\n$\\pi_R$": (0.29, 0.50),
        "Trajectory\n$U_R$": (0.54, 0.68),
        "Accessibility\n$S_R$": (0.54, 0.32),
        "First-person\nconditional value": (0.84, 0.50),
    }
    for label, (x, y) in boxes.items():
        ax.text(x, y, label, ha="center", va="center", transform=ax.transAxes,
                bbox=dict(boxstyle="round,pad=0.45", facecolor="white", edgecolor="black"))
    arrows = [
        ((0.14, 0.50), (0.22, 0.50)),
        ((0.36, 0.53), (0.47, 0.65)),
        ((0.36, 0.47), (0.47, 0.35)),
        ((0.61, 0.65), (0.76, 0.54)),
        ((0.61, 0.35), (0.76, 0.46)),
    ]
    for start, end in arrows:
        ax.annotate("", xy=end, xytext=start, xycoords=ax.transAxes,
                    arrowprops=dict(arrowstyle="->", linewidth=1.3))
    ax.set_title("Recognition-dependent QBS framework")
    save(fig, "fig1_framework.pdf")


def fig2_fosd():
    x = np.linspace(-4, 4, 801)
    phi = np.exp(-x * x / 2) / np.sqrt(2 * np.pi)

    def wcdf(weight):
        z = phi * weight
        c = np.cumsum(z) * (x[1] - x[0])
        return c / c[-1]

    base = wcdf(np.ones_like(x))
    mono = wcdf(0.1 + 0.9 / (1 + np.exp(-2 * x)))
    nonmono = wcdf(0.1 + 0.9 * np.exp(-(x / 0.9) ** 2))

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax.plot(x, base, label="Base")
    ax.plot(x, mono, linestyle="--", label="FP, monotone accessibility")
    ax.plot(x, nonmono, linestyle=":", label="FP, nonmonotone accessibility")
    ax.set_xlabel("Outcome")
    ax.set_ylabel("CDF")
    ax.set_title("FOSD and the monotone-accessibility boundary")
    ax.legend()
    ax.grid(alpha=0.2)
    save(fig, "fig2_fosd.pdf")


def fig3_recognition():
    d = pd.read_csv(DATA / "e3_recognition_decomposition_reproduction.csv").iloc[0]
    labels = ["Policy", "QBS", "Total"]
    vals = [d["policy_gain"], d["QBS_gain"], d["total_gain"]]
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    bars = ax.bar(labels, vals)
    ax.axhline(0, linewidth=0.8)
    ax.set_ylabel("First-person value difference")
    ax.set_title("Paired recognition decomposition")
    ax.bar_label(bars, fmt="%.3f", padding=3)
    save(fig, "fig3_recognition_decomposition.pdf")


def fig4_interaction():
    d = pd.read_csv(DATA / "e4_fixed_selector_sign_reproduction.csv")
    fig, ax = plt.subplots(figsize=(6.5, 4.0))
    bars = ax.bar(d["policy"], d["interaction"])
    ax.axhline(0, linewidth=0.8)
    ax.set_ylabel("Policy--QBS interaction")
    ax.set_title("Interaction sign under a fixed selector")
    ax.bar_label(bars, fmt="%.3f", padding=3)
    save(fig, "fig4_interaction_sign.pdf")


def fig5_adaptation():
    d = pd.read_csv(DATA / "qbs_adaptation_total_effect_summary.csv")
    x = d["adaptation_accuracy_p"]
    fig, ax = plt.subplots(figsize=(7.0, 4.3))
    ax.plot(x, d["policy_effect"], marker="o", label="Policy effect")
    ax.plot(x, d["QBS_after"], marker="o", label="QBS marginal after policy")
    ax.plot(x, d["interaction"], marker="o", label="Interaction")
    ax.plot(x, d["total_FP_effect"], marker="o", label="Total FP effect")
    ax.axhline(0, linewidth=0.8)
    ax.set_xlabel("Adaptation targeting accuracy")
    ax.set_ylabel("Effect size")
    ax.set_title("Adaptation quality and policy--selection substitution")
    ax.legend()
    ax.grid(alpha=0.2)
    save(fig, "fig5_adaptation_quality.pdf")


def fig6_branch_coherence():
    d = pd.read_csv(DATA / "e5_rho_paired_reproduction.csv")
    x = d["rho_env"]
    fig, ax = plt.subplots(figsize=(7.0, 4.3))
    ax.plot(x, d["action_corr_increment"], marker="o",
            label="Action-correlation increment")
    ax.plot(x, d["total_FP_gain"], marker="o", label="Total FP gain")
    ax.set_xlabel("Shared environmental correlation")
    ax.set_ylabel("Simulation quantity")
    ax.set_title("Branch coherence and marginal FP uplift are distinct")
    ax.legend()
    ax.grid(alpha=0.2)
    save(fig, "fig6_branch_coherence.pdf")


if __name__ == "__main__":
    fig1_framework()
    fig2_fosd()
    fig3_recognition()
    fig4_interaction()
    fig5_adaptation()
    fig6_branch_coherence()
    print(f"Generated manuscript PDFs in {OUT}")
