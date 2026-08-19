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

The audited source/manuscript/audit surfaces are Git-blob locked in both HEAD and the
working tree before semantic snippet checks. This prevents required formulas or boundary
language from surviving only in comments/literal code while the actual reviewed surface
drifts; any wording or mathematical change to these surfaces requires an explicit audit
contract update.
"""
from __future__ import annotations

from pathlib import Path
import subprocess

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

EXPECTED_SURFACE_BLOBS = {
    "supplementary/confidence_envelope_certificate.md": "8980a4336d2bdc14bd7bf56931c6e9f2bb6535b6",
    "paper/sections/confidence_envelope_appendix.tex": "02e9623f94c4fced3ec300bd76da8a5e1e47dbb4",
    "docs/s2_confidence_envelope_audit.md": "fc80b9ff4db9768c1b2c505e04f30a09039c9966",
    "supplementary/light_tail_certificate.md": "e0a4f00db4f3da0174d8f353d6fe9200934c56b3",
    "paper/sections/light_tail_certificate_appendix.tex": "9fd831ecfa574c50a82d9fde07ea8b2c968c3390",
    "docs/s2_light_tail_certificate_audit.md": "e307d3d733fc862f1798f05f59ce209e4a073941",
    "supplementary/robust_mom_certificate.md": "c3316494c58f1fb221cac4c93ea67abd1533fbad",
    "paper/sections/robust_mom_certificate_appendix.tex": "fba18e511bc803c74fab4a435b8f6e7e5943a213",
    "docs/s2_robust_mom_certificate_audit.md": "1f232fb48d6ab64deb6cf4cdd02be6218076f0be",
    "supplementary/recognition_time.md": "37c808db43bf02a340cfffa920040edc8d1e25c4",
    "supplementary/repeated_filtering.md": "73a79b39e092ca24c27eb5d5a55aed42d620ed6a",
    "supplementary/binary_soft_qbs.md": "d3dcbf281e7111f432d1acf4ba5a29aad2e64209",
    "supplementary/gaussian_model.md": "e8f9a6c6d5a6683459e86b32f91ef61f610046c7",
    "paper/sections/appendix.tex": "f55de6faf4ce50edd5ba301670ce58810a9db49a",
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


def git_text(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def main() -> None:
    errors: list[str] = []
    texts: dict[Path, str] = {}

    expected_paths = {path.relative_to(ROOT).as_posix() for path in REQUIRED_SNIPPETS}
    if set(EXPECTED_SURFACE_BLOBS) != expected_paths:
        errors.append("validator self-contract: supplementary blob map differs from REQUIRED_SNIPPETS")

    for path, snippets in REQUIRED_SNIPPETS.items():
        relative = path.relative_to(ROOT).as_posix()
        if path.is_symlink() or not path.is_file():
            errors.append(f"missing/invalid supplementary consistency surface: {relative}")
            continue

        expected_blob = EXPECTED_SURFACE_BLOBS.get(relative)
        if expected_blob is None:
            errors.append(f"{relative}: no audited supplementary-surface blob identity")
            continue
        try:
            head_blob = git_text("rev-parse", f"HEAD:{relative}")
            worktree_blob = git_text("hash-object", relative)
        except subprocess.CalledProcessError as exc:
            errors.append(f"{relative}: unable to resolve Git blob identity: {exc}")
            continue
        if head_blob != expected_blob:
            errors.append(
                f"{relative}: committed supplementary-surface drift: "
                f"HEAD has {head_blob}, expected {expected_blob}"
            )
        if worktree_blob != expected_blob:
            errors.append(
                f"{relative}: working-tree supplementary-surface drift: "
                f"{worktree_blob}, expected {expected_blob}"
            )

        text = path.read_text(encoding="utf-8")
        texts[path] = text
        for snippet in snippets:
            if snippet not in text:
                errors.append(
                    f"{relative}: missing audited supplementary invariant {snippet!r}"
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
        f"{len(REQUIRED_SNIPPETS)} source/manuscript/audit surfaces; all audited HEAD/worktree "
        "blob identities and semantic invariants match."
    )


if __name__ == "__main__":
    main()
