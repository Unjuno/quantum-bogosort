"""Verify the canonical T1-T5 body and approved domain corrections.

The frozen v0.3 snapshot remains untouched. Current ``main`` intentionally differs in
exactly four audited textual places in ``theory/core_theorems.tex``: a version-neutral
title, explicit base-integrability of policy utility in the setup, explicit
base-integrability of the generic T1 outcome, and T5 cross-integrability for the
intermediate ``Q(U_1,S_0)`` term. These close real domain gaps while leaving every
identity, proof step, sign result, and physical boundary unchanged.

The canonical TeX source is normalized only at those four approved places and must then
match the frozen v0.3 Git blob. In addition, the corresponding explicit domain assumptions
must remain present in the rendered theory pages and manuscript theorem/proof surfaces so
a later documentation edit cannot silently reintroduce the old incomplete domain wording.
"""
from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "theory" / "core_theorems.tex"
FROZEN_V03_COMMIT = "58038763127258bd3e2f0d41708c4dfa01f81fd6"
FROZEN_V03_BLOB = "82986d7197e79446d6574aab538d1edaeff47eb6"
FROZEN_TITLE = r"\title{Quantum Bogosort: Core Theorem Set v0.1}"
CURRENT_TITLE = r"\title{Quantum Bogosort: Core Theorem Set (T1--T5)}"
FROZEN_SETUP = r"0<\E_\mu[S_\pi]<\infty,\qquad \E_\mu[|U_\pi|S_\pi]<\infty."
CURRENT_SETUP = "\n".join(
    [
        r"0<\E_\mu[S_\pi]<\infty,\qquad",
        r"\E_\mu[|U_\pi|]<\infty,\qquad",
        r"\E_\mu[|U_\pi|S_\pi]<\infty.",
    ]
)
FROZEN_T1_ASSUMPTION = r"For any $X$ with $\E[|X|S]<\infty$,"
CURRENT_T1_ASSUMPTION = (
    r"For any $X$ with $\E[|X|]<\infty$ and $\E[|X|S]<\infty$,"
)
FROZEN_T5_INTRO = r"Let $D=U_1-U_0$ and"
CURRENT_T5_INTRO = (
    r"Assume additionally $\E[|U_1|S_0]<\infty$. Let $D=U_1-U_0$ and"
)

DOMAIN_SURFACES: dict[Path, tuple[str, ...]] = {
    ROOT / "theory/core_theorems.md": (
        r"E_\mu[|U_\pi|]<\infty",
        r"E_\mu[|U_\pi|S_\pi]<\infty",
    ),
    ROOT / "theory/theorem_1_3.md": (
        r"E[|X|]<\infty",
        r"E[|X|S]<\infty",
    ),
    ROOT / "theory/theorem_4_5.md": (
        r"E[|U_R|]<\infty",
        r"E[|U_R|S_R]<\infty",
        r"E[|U_1|S_0]<\infty",
    ),
    ROOT / "paper/sections/formal_model.tex": (
        r"\mathbb E_\mu[|U_R|]<\infty",
        r"\mathbb E_\mu[|U_R|S_R]<\infty",
        r"\mathbb E_\mu[|U_1|S_0]<\infty",
    ),
    ROOT / "paper/sections/theorems.tex": (
        r"\mathbb E[|X|]<\infty",
        r"\mathbb E[|X|S]<\infty",
        r"\mathbb E[|U_R|]<\infty",
        r"\mathbb E[|U_R|S_R]<\infty",
        r"\mathbb E[|U_1|S_0]<\infty",
    ),
    ROOT / "paper/sections/appendix.tex": (
        r"\mathbb E[|X|]<\infty",
        r"\mathbb E[|X|S]<\infty",
        r"\mathbb E[|U_R|]<\infty",
        r"\mathbb E[|U_R|S_R]<\infty",
        r"\mathbb E[|U_1|S_0]<\infty",
    ),
}


def git_blob_sha(text: str) -> str:
    result = subprocess.run(
        ["git", "hash-object", "--stdin"],
        cwd=ROOT,
        input=text,
        text=True,
        check=True,
        capture_output=True,
    )
    return result.stdout.strip()


def require_exact_current(text: str, current: str, label: str) -> None:
    if text.count(current) != 1:
        raise SystemExit(
            f"Core-theorem lock validation failed: approved current {label} must occur exactly once"
        )


def validate_domain_surfaces() -> None:
    errors: list[str] = []
    for path, snippets in DOMAIN_SURFACES.items():
        if not path.is_file():
            errors.append(f"missing theorem-domain surface: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for snippet in snippets:
            if snippet not in text:
                errors.append(
                    f"{path.relative_to(ROOT)}: missing approved domain assumption {snippet!r}"
                )
    if errors:
        raise SystemExit("Core-theorem domain-surface validation failed:\n" + "\n".join(errors))


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit("Core-theorem lock validation failed: missing theory/core_theorems.tex")

    text = SOURCE.read_text(encoding="utf-8")
    approved = [
        (CURRENT_TITLE, FROZEN_TITLE, "title"),
        (CURRENT_SETUP, FROZEN_SETUP, "setup integrability text"),
        (CURRENT_T1_ASSUMPTION, FROZEN_T1_ASSUMPTION, "T1 integrability text"),
        (CURRENT_T5_INTRO, FROZEN_T5_INTRO, "T5 cross-integrability text"),
    ]
    for current, _frozen, label in approved:
        require_exact_current(text, current, label)

    normalized = text
    for current, frozen, _label in approved:
        normalized = normalized.replace(current, frozen, 1)

    actual = git_blob_sha(normalized)
    if actual != FROZEN_V03_BLOB:
        raise SystemExit(
            "Core-theorem lock validation failed: after normalizing only the audited title/"
            "integrability corrections, the T1-T5 TeX body differs from frozen v0.3 canonical "
            f"blob {FROZEN_V03_BLOB}; got {actual}. Any additional theorem/proof/boundary change "
            "requires explicit scientific review."
        )

    validate_domain_surfaces()

    print(
        "Core-theorem lock validation passed: after exactly four approved normalizations "
        "(version-neutral title, setup/T1 base-integrability, and T5 cross-integrability), "
        f"theory/core_theorems.tex matches frozen v0.3 commit {FROZEN_V03_COMMIT[:12]}… "
        f"blob {FROZEN_V03_BLOB}; explicit domain assumptions are also present across "
        f"{len(DOMAIN_SURFACES)} rendered/manuscript surfaces."
    )


if __name__ == "__main__":
    main()
