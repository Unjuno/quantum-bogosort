"""Generate PDF versions of the six QBS publication figures for LaTeX.

The committed SVGs remain the GitHub-readable canonical previews. These PDFs are
build products generated from the same committed data and deterministic theorem
illustrations for manuscript inclusion. Numerical series for Figures 2--6 are supplied by
``figure_data.py``, shared with the SVG generator.
"""
from pathlib import Path
import matplotlib.pyplot as plt

from figure_data import (
    adaptation_line_data,
    branch_line_data,
    fosd_curves,
    interaction_bar_data,
    recognition_bar_data,
)

ROOT = Path(__file__).resolve().parents[1]
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
    x, base, mono, nonmono = fosd_curves()

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
    labels, vals = recognition_bar_data()
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    bars = ax.bar(labels, vals)
    ax.axhline(0, linewidth=0.8)
    ax.set_ylabel("First-person value difference")
    ax.set_title("Paired recognition decomposition")
    ax.bar_label(bars, fmt="%.3f", padding=3)
    save(fig, "fig3_recognition_decomposition.pdf")


def fig4_interaction():
    labels, vals = interaction_bar_data()
    fig, ax = plt.subplots(figsize=(6.5, 4.0))
    bars = ax.bar(labels, vals)
    ax.axhline(0, linewidth=0.8)
    ax.set_ylabel("Policy--QBS interaction")
    ax.set_title("Interaction sign under a fixed selector")
    ax.bar_label(bars, fmt="%.3f", padding=3)
    save(fig, "fig4_interaction_sign.pdf")


def fig5_adaptation():
    x, series = adaptation_line_data()
    fig, ax = plt.subplots(figsize=(7.0, 4.3))
    for label, values in series:
        ax.plot(x, values, marker="o", label=label)
    ax.axhline(0, linewidth=0.8)
    ax.set_xlabel("Adaptation targeting accuracy")
    ax.set_ylabel("Effect size")
    ax.set_title("Adaptation quality and policy--selection substitution")
    ax.legend()
    ax.grid(alpha=0.2)
    save(fig, "fig5_adaptation_quality.pdf")


def fig6_branch_coherence():
    x, series = branch_line_data()
    fig, ax = plt.subplots(figsize=(7.0, 4.3))
    for label, values in series:
        ax.plot(x, values, marker="o", label=label)
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
