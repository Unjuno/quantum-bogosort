"""Generate compact, publication-oriented SVG figures from committed QBS data."""
from pathlib import Path
from html import escape
import numpy as np
import pandas as pd

from figure_data import (
    adaptation_line_data,
    branch_line_data,
    fosd_curves,
    interaction_bar_data,
    recognition_bar_data,
)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "figures" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 720, 440
M = {"l": 82, "r": 24, "t": 55, "b": 72}
PW = W - M["l"] - M["r"]
PH = H - M["t"] - M["b"]


def start(title):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        f'<rect x="0" y="0" width="{W}" height="{H}" fill="white"/>',
        '<style>text{font-family:Arial,Helvetica,sans-serif;fill:#111}.axis{stroke:#222;stroke-width:1}.grid{stroke:#bbb;stroke-width:.6;stroke-dasharray:3 4}.s1{fill:none;stroke:#111;stroke-width:2.2}.s2{fill:none;stroke:#555;stroke-width:2.2;stroke-dasharray:8 5}.s3{fill:none;stroke:#888;stroke-width:2.2;stroke-dasharray:2 4}.s4{fill:none;stroke:#111;stroke-width:2.2;stroke-dasharray:12 4 2 4}.bar{fill:#bbb;stroke:#222;stroke-width:1}</style>',
        f'<text x="{W/2}" y="26" text-anchor="middle" font-size="16" font-weight="600">{escape(title)}</text>',
    ]


def finish(parts, note):
    parts.append(f'<text x="{W/2}" y="{H-12}" text-anchor="middle" font-size="10">{escape(note)}</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def axes(parts, xlabel, ylabel, ymin, ymax, yticks=5):
    x0, y0 = M["l"], H - M["b"]
    parts += [
        f'<line class="axis" x1="{x0}" y1="{M["t"]}" x2="{x0}" y2="{y0}"/>',
        f'<line class="axis" x1="{x0}" y1="{y0}" x2="{W-M["r"]}" y2="{y0}"/>',
        f'<text x="{W/2}" y="{H-38}" text-anchor="middle" font-size="12">{escape(xlabel)}</text>',
        f'<text x="18" y="{H/2}" text-anchor="middle" font-size="12" transform="rotate(-90 18 {H/2})">{escape(ylabel)}</text>',
    ]
    for i in range(yticks + 1):
        value = ymin + (ymax - ymin) * i / yticks
        y = y0 - PH * i / yticks
        parts += [
            f'<line class="grid" x1="{x0}" y1="{y}" x2="{W-M["r"]}" y2="{y}"/>',
            f'<text x="{x0-9}" y="{y+4}" text-anchor="end" font-size="10">{value:.2f}</text>',
        ]


def mapx(v, lo, hi):
    return M["l"] + PW * (v - lo) / (hi - lo)


def mapy(v, lo, hi):
    return H - M["b"] - PH * (v - lo) / (hi - lo)


def polyline(parts, xs, ys, xlo, xhi, ylo, yhi, cls):
    points = " ".join(f"{mapx(x,xlo,xhi):.1f},{mapy(y,ylo,yhi):.1f}" for x, y in zip(xs, ys))
    parts.append(f'<polyline class="{cls}" points="{points}"/>')


def legend(parts, entries):
    x, y = W - 245, 62
    for i, (label, cls) in enumerate(entries):
        yy = y + 18 * i
        parts += [
            f'<line class="{cls}" x1="{x}" y1="{yy}" x2="{x+28}" y2="{yy}"/>',
            f'<text x="{x+36}" y="{yy+4}" font-size="10">{escape(label)}</text>',
        ]


def write(name, content):
    (OUT / name).write_text(content, encoding="utf-8")


def fig1():
    parts = start("Recognition-dependent QBS framework")
    boxes = [
        (40, 170, 115, 64, "Recognition", "R"),
        (210, 170, 115, 64, "Policy", "pi_R"),
        (390, 95, 125, 64, "Trajectory", "U_R"),
        (390, 245, 125, 64, "Accessibility", "S_R"),
        (565, 170, 135, 64, "First-person", "conditional value"),
    ]
    for x, y, w, h, a, b in boxes:
        parts += [
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="white" stroke="#222"/>',
            f'<text x="{x+w/2}" y="{y+26}" text-anchor="middle" font-size="12">{a}</text>',
            f'<text x="{x+w/2}" y="{y+46}" text-anchor="middle" font-size="12">{b}</text>',
        ]
    def arrow(x1, y1, x2, y2):
        parts.extend([
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#222" stroke-width="1.5"/>',
            f'<polygon points="{x2},{y2} {x2-9},{y2-5} {x2-9},{y2+5}" fill="#222"/>',
        ])
    arrow(155, 202, 205, 202); arrow(325, 195, 385, 135); arrow(325, 209, 385, 277); arrow(515, 127, 560, 190); arrow(515, 277, 560, 214)
    write("fig1_framework.svg", finish(parts, "Schematic: theorem variables, not a physical branch diagram."))


def fig2():
    x, base, mono, mid = fosd_curves()
    pd.DataFrame({"x": x, "base_cdf": base, "fp_monotone_cdf": mono, "fp_nonmonotone_cdf": mid}).to_csv(DATA / "fig2_fosd_theorem_illustration.csv", index=False)
    parts = start("FOSD and the monotone-accessibility boundary")
    axes(parts, "Outcome x", "CDF", 0, 1, 5)
    idx = np.arange(0, len(x), 5)
    polyline(parts, x[idx], base[idx], -4, 4, 0, 1, "s1")
    polyline(parts, x[idx], mono[idx], -4, 4, 0, 1, "s2")
    polyline(parts, x[idx], mid[idx], -4, 4, 0, 1, "s3")
    legend(parts, [("Base", "s1"), ("FP monotone", "s2"), ("FP nonmonotone", "s3")])
    write("fig2_fosd.svg", finish(parts, "Theorem illustration: nonmonotone accessibility can produce CDF crossing."))


def bar_chart(name, title, labels, values, ylabel, note):
    lo, hi = min(0, min(values)), max(0, max(values))
    pad = max(0.05, (hi - lo) * 0.15)
    lo, hi = lo - pad, hi + pad
    parts = start(title)
    axes(parts, "", ylabel, lo, hi, 5)
    slot = PW / len(values)
    for i, (label, value) in enumerate(zip(labels, values)):
        cx, bw = M["l"] + slot * (i + 0.5), slot * 0.48
        y0, yv = mapy(0, lo, hi), mapy(value, lo, hi)
        y, h = min(y0, yv), abs(y0 - yv)
        parts += [
            f'<rect class="bar" x="{cx-bw/2:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{h:.1f}"/>',
            f'<text x="{cx:.1f}" y="{H-M["b"]+22}" text-anchor="middle" font-size="10">{escape(label)}</text>',
            f'<text x="{cx:.1f}" y="{yv-7 if value>=0 else yv+15:.1f}" text-anchor="middle" font-size="10">{value:.3f}</text>',
        ]
    write(name, finish(parts, note))


def fig3():
    labels, values = recognition_bar_data()
    bar_chart("fig3_recognition_decomposition.svg", "Recognition decomposition", labels, values, "FP value difference", "Paired primitive randomness; total equals policy plus QBS to numerical precision.")


def fig4():
    labels, values = interaction_bar_data()
    bar_chart("fig4_interaction_sign.svg", "Policy-QBS interaction sign", labels, values, "Interaction", "Fixed selector: sign matches Cov(D,S).")


def line_chart(name, title, x, xlabel, series, ylabel, note):
    allv = np.concatenate([np.asarray(y, float) for _, y, _ in series])
    lo, hi = min(0, float(allv.min())), max(0, float(allv.max()))
    pad = max(0.04, (hi - lo) * 0.12)
    lo, hi = lo - pad, hi + pad
    xlo, xhi = float(np.min(x)), float(np.max(x))
    parts = start(title)
    axes(parts, xlabel, ylabel, lo, hi, 5)
    for label, y, cls in series:
        polyline(parts, x, y, xlo, xhi, lo, hi, cls)
        for xx, yy in zip(x, y):
            parts.append(f'<circle cx="{mapx(xx,xlo,xhi):.1f}" cy="{mapy(yy,lo,hi):.1f}" r="2.5" fill="#222"/>')
    for xx in x:
        parts.append(f'<text x="{mapx(xx,xlo,xhi):.1f}" y="{H-M["b"]+20}" text-anchor="middle" font-size="9">{xx:.2f}</text>')
    legend(parts, [(label, cls) for label, _, cls in series])
    write(name, finish(parts, note))


def fig5():
    x, raw_series = adaptation_line_data()
    classes = ["s1", "s2", "s3", "s4"]
    series = [(label, values, cls) for (label, values), cls in zip(raw_series, classes)]
    line_chart("fig5_adaptation_quality.svg", "Adaptation quality and substitution", x, "Targeting accuracy p", series, "Effect size", "Toy adaptation study: total value rises while the interaction becomes more negative.")


def fig6():
    x, raw_series = branch_line_data()
    classes = ["s1", "s2"]
    series = [(label, values, cls) for (label, values), cls in zip(raw_series, classes)]
    line_chart("fig6_branch_coherence.svg", "Branch coherence versus marginal FP uplift", x, "Shared environmental correlation", series, "Simulation quantity", "Cross-copy coherence changes strongly while single-observer FP gain remains nearly flat.")


def fig7():
    d = pd.read_csv(DATA / "qbs_nonlinear_minimal_mock_summary.csv")
    d = d[d.metric == "corr_score_luck"]
    x = np.array(sorted(d.noise_sigma.unique()), dtype=float)

    def values(evaluator):
        s = d[d.evaluator == evaluator].set_index("noise_sigma").loc[x]
        return s["mean"].to_numpy(dtype=float)

    line_chart(
        "fig7_predictive_alignment.svg",
        "Learned predictive alignment under noise",
        x,
        "Environment noise sigma",
        [
            ("Interaction-capable", values("interaction_4param"), "s1"),
            ("Misspecified linear", values("linear_3param"), "s2"),
            ("Random control", values("random_control"), "s3"),
        ],
        "Mean score-outcome correlation",
        "E2 toy model: the representable interaction structure retains predictive alignment as noise rises.",
    )


if __name__ == "__main__":
    fig1(); fig2(); fig3(); fig4(); fig5(); fig6(); fig7()
    print(f"Generated seven SVG figures in {OUT}")
