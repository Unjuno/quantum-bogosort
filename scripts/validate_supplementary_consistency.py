"""Lock audited S2.8--S2.10 boundary corrections across public/manuscript surfaces.

These checks are deliberately narrow. They do not attempt to re-prove the supplementary
results. They prevent three concrete defects found during the pre-announcement audit from
silently reappearing in only one representation:

* S2.8: the generic random certificate must be real-valued off the confidence event via
  ``U_M^+ = max(0,U_M)``;
* S2.9: the custom concentration-parameter domain must make all radii real/nonnegative;
* S2.10: the proof must separate the zero-variance boundary from the positive-variance
  Chebyshev step.

Each correction must be present in the canonical supplementary note, compiled manuscript
appendix, and corresponding theorem-audit record.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SNIPPETS: dict[Path, tuple[str, ...]] = {
    ROOT / "supplementary/confidence_envelope_certificate.md": (
        r"U_M^+",
        r"\max\{0,U_M\}",
        r"\sqrt{U_M^+V_U}",
        "real-valued statistic",
    ),
    ROOT / "paper/sections/confidence_envelope_appendix.tex": (
        r"U_M^+=\max\{0,U_M\}",
        r"\sqrt{U_M^+V_U}",
        "real-valued",
    ),
    ROOT / "docs/s2_confidence_envelope_audit.md": (
        r"U_M^+",
        r"\max\{0,U_M\}",
        "total-definedness",
    ),
    ROOT / "supplementary/light_tail_certificate.md": (
        r"\sigma_X\ge0",
        r"v_W\ge0",
        r"b_W\ge0",
        r"U_M^+=U_M",
    ),
    ROOT / "paper/sections/light_tail_certificate_appendix.tex": (
        r"\sigma_X\ge0",
        r"v_W\ge0",
        r"b_W\ge0",
        r"U_M^+=U_M",
    ),
    ROOT / "docs/s2_light_tail_certificate_audit.md": (
        r"\sigma_X\ge0",
        r"v_W\ge0",
        r"b_W\ge0",
        r"U_M^+=U_M",
    ),
    ROOT / "supplementary/robust_mom_certificate.md": (
        r"v_j\ge0",
        "If `v_j=0`",
        r"\mathrm{Var}(Z_j)=0",
        "No Chebyshev division is needed",
    ),
    ROOT / "paper/sections/robust_mom_certificate_appendix.tex": (
        r"0\le \operatorname{Var}(Z_j)\le v_j<\infty",
        "If $v_j=0$",
        r"\operatorname{Var}(Z_j)=0",
        "Now suppose $v_j>0$",
    ),
    ROOT / "docs/s2_robust_mom_certificate_audit.md": (
        "zero-variance",
        "If:",
        r"\mathrm{Var}(Z_j)=0",
        "FOUND AND CORRECTED",
    ),
}

# Guard the mathematical relationships, not only prose markers.
PAIRWISE_FORMULAS: tuple[tuple[Path, Path, tuple[str, ...]], ...] = (
    (
        ROOT / "supplementary/confidence_envelope_certificate.md",
        ROOT / "paper/sections/confidence_envelope_appendix.tex",
        (r"U_M^+", r"\sqrt{U_M^+V_U}"),
    ),
    (
        ROOT / "supplementary/light_tail_certificate.md",
        ROOT / "paper/sections/light_tail_certificate_appendix.tex",
        (r"\sigma_X\ge0", r"v_W\ge0", r"b_W\ge0", r"U_M^+=U_M"),
    ),
    (
        ROOT / "supplementary/robust_mom_certificate.md",
        ROOT / "paper/sections/robust_mom_certificate_appendix.tex",
        (r"\mathrm{Var}(Z_j)=0",),
    ),
)


def main() -> None:
    errors: list[str] = []
    texts: dict[Path, str] = {}

    for path, snippets in REQUIRED_SNIPPETS.items():
        if not path.is_file():
            errors.append(f"missing supplementary consistency surface: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        texts[path] = text
        for snippet in snippets:
            if snippet not in text:
                errors.append(
                    f"{path.relative_to(ROOT)}: missing audited supplementary invariant {snippet!r}"
                )

    for left, right, formulas in PAIRWISE_FORMULAS:
        left_text = texts.get(left, "")
        right_text = texts.get(right, "")
        if not left_text or not right_text:
            continue
        for formula in formulas:
            if formula not in left_text or formula not in right_text:
                errors.append(
                    f"supplementary/manuscript drift for {formula!r}: "
                    f"{left.relative_to(ROOT)} <-> {right.relative_to(ROOT)}"
                )

    if errors:
        raise SystemExit(
            "Supplementary consistency validation failed:\n" + "\n".join(errors)
        )

    print(
        "Supplementary consistency validation passed: S2.8 off-event totality, "
        "S2.9 nonnegative concentration-parameter domain, and S2.10 zero-variance "
        f"boundary remain synchronized across {len(REQUIRED_SNIPPETS)} source/manuscript/audit surfaces."
    )


if __name__ == "__main__":
    main()
