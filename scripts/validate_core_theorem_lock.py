"""Verify the canonical standalone T1-T5 TeX body against frozen v0.3.

The frozen v0.3 snapshot remains untouched. Current ``main`` intentionally differs in
exactly four audited textual places: a version-neutral title, explicit base-integrability
of policy utility in the setup, explicit base-integrability of the generic T1 outcome,
and T5 cross-integrability for the intermediate ``Q(U_1,S_0)`` term. These close real
domain gaps while leaving every identity, proof step, sign result, and physical boundary
unchanged. Normalize only these approved corrections back to the frozen text and require
the resulting Git blob identity to equal the v0.3 canonical blob. Any other T1-T5
 theorem/proof/boundary change fails CI.
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


def require_exact_current(text: str, current: str, frozen: str, label: str) -> None:
    if text.count(current) != 1:
        raise SystemExit(
            f"Core-theorem lock validation failed: approved current {label} must occur exactly once"
        )
    if frozen in text:
        raise SystemExit(
            f"Core-theorem lock validation failed: stale frozen {label} remains in current source"
        )


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
    for current, frozen, label in approved:
        require_exact_current(text, current, frozen, label)

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

    print(
        "Core-theorem lock validation passed: after exactly four approved normalizations "
        "(version-neutral title plus T1/T4-domain and T5 cross-integrability corrections), "
        f"theory/core_theorems.tex matches frozen v0.3 commit {FROZEN_V03_COMMIT[:12]}… "
        f"blob {FROZEN_V03_BLOB}."
    )


if __name__ == "__main__":
    main()
