"""Lock audited supplementary boundary corrections across public/manuscript surfaces.

These checks are deliberately narrow. They do not attempt to re-prove the supplementary
results. They prevent concrete defects found during the pre-announcement audit from
silently reappearing:

* S2.8: the generic random certificate must be real-valued off the confidence event via
  ``U_M^+ = max(0,U_M)``;
* S2.9: the custom concentration-parameter domain must make all radii real/nonnegative;
* S2.10: the proof must separate the zero-variance boundary from the positive-variance
  Chebyshev step;
* recognition time: the confidence process must be typed as adapted/measurable, the
  continuous-time hitting statement must carry path/measurability hypotheses, and the FP
  stopping-rule value must satisfy the full T1 base/weighted integrability domain;
* repeated filtering: the weighted value must be defined by explicit absolute
  integrability before the derivative identity, which must retain its
  dominated-differentiation and weighted-moment regularity conditions;
* binary/Gaussian toys: accessibility/execution parameters must remain in their stated
  nonnegative domains and the binary model must exclude zero total accessibility.

The S2.8--S2.10 corrections must be present in the canonical supplementary note, compiled
manuscript appendix, and corresponding theorem-audit record. Repository-only notes are
locked directly at their canonical source; repeated-filter and Gaussian conditions are also
required on the manuscript derivation surface.
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
        r"\mathrm{Var}(Z_j)=0",
        "FOUND AND CORRECTED",
    ),
    ROOT / "supplementary/recognition_time.md": (
        r"C_t:\Omega\to\mathbb R",
        r"\mathcal F_t`-measurable",
        "continuous sample paths",
        "FP-admissible",
        r"E[|U_{\tau}|]<\infty",
        r"E[|U_{\tau}|S_{\tau}]<\infty",
    ),
    ROOT / "supplementary/repeated_filtering.md": (
        r"0<\lambda\le1",
        r"E[|U|\lambda^{N_B}]",
        "open positive neighborhood",
        r"E[|U|N_B\lambda^{N_B}]",
        r"E[N_B\lambda^{N_B}]",
        "left derivative",
    ),
    ROOT / "supplementary/binary_soft_qbs.md": (
        r"0\le p\le1",
        r"0\le\lambda\le1",
        r"p+(1-p)\lambda>0",
        r"(p,\lambda)=(0,0)",
        r"0\le q\le1",
        r"0\le\alpha\le1",
    ),
    ROOT / "supplementary/gaussian_model.md": (
        r"-1\le\rho\le1",
        r"0\le\lambda\le1",
        r"0\le q\le1",
        r"0\le\alpha\le1",
        "denominator strictly positive",
    ),
    ROOT / "paper/sections/appendix.tex": (
        r"0<\lambda\le1",
        r"\mathbb E[|U|\lambda^{N_B}]",
        "open positive neighborhood",
        r"\mathbb E[|U|N_B\lambda^{N_B}]",
        r"\mathbb E[N_B\lambda^{N_B}]",
        "left derivative",
        r"-1\le\rho\le1",
        r"0\le\lambda\le1",
        r"0\le q\le1",
        r"0\le\alpha\le1",
        "denominator is strictly positive",
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
    (
        ROOT / "supplementary/gaussian_model.md",
        ROOT / "paper/sections/appendix.tex",
        (r"-1\le\rho\le1", r"0\le\lambda\le1", r"0\le q\le1", r"0\le\alpha\le1"),
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
        "Supplementary consistency validation passed: audited S2.8--S2.10, recognition-time, "
        "repeated-filter, and binary/Gaussian domain/totality boundaries remain locked across "
        f"{len(REQUIRED_SNIPPETS)} source/manuscript/audit surfaces."
    )


if __name__ == "__main__":
    main()
