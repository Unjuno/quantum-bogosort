"""Verify the canonical T1-T5 body and approved domain corrections.

The frozen v0.3 snapshot remains untouched. Current ``main`` intentionally differs in
exactly four audited textual places in ``theory/core_theorems.tex``: a version-neutral
title, explicit base-integrability of policy utility in the setup, an explicit complete
T1 domain for generic accessibility/outcome variables, and T5 cross-integrability for the
intermediate ``Q(U_1,S_0)`` term. These close real domain gaps while leaving every
identity, proof step, sign result, and physical boundary unchanged.

The canonical TeX source is normalized only at those four approved places and must then
match the frozen v0.3 Git blob. The nine corresponding theory/card/manuscript domain
surfaces are also locked to their audited HEAD/worktree Git blobs before semantic snippet
checks. This makes later wording/domain changes an explicit scientific-review contract
update rather than allowing required assumptions to survive only in comments or literal
code while visible text drifts.
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
    r"For any $S\ge0$ with $0<\E[S]<\infty$ and any $X$ with "
    r"$\E[|X|]<\infty$ and $\E[|X|S]<\infty$,"
)
FROZEN_T5_INTRO = r"Let $D=U_1-U_0$ and"
CURRENT_T5_INTRO = (
    r"Assume additionally $\E[|U_1|S_0]<\infty$. Let $D=U_1-U_0$ and"
)

DOMAIN_SURFACES: dict[Path, tuple[str, ...]] = {
    ROOT / "theory/core_theorems.md": (
        r"0<E_\mu[S_\pi]<\infty",
        r"E_\mu[|U_\pi|]<\infty",
        r"E_\mu[|U_\pi|S_\pi]<\infty",
    ),
    ROOT / "theory/theorem_1_3.md": (
        r"E[|X|]<\infty",
        r"0<E[S]<\infty",
        r"E[|X|S]<\infty",
    ),
    ROOT / "theory/theorem_4_5.md": (
        r"E[|U_R|]<\infty",
        r"E[|U_R|S_R]<\infty",
        r"E[|U_1|S_0]<\infty",
    ),
    ROOT / "experiments/E1_FOSD.md": (
        r"0<E[S]<\infty",
        r"E[|X|]<\infty",
        r"E[|X|S]<\infty",
    ),
    ROOT / "experiments/E3_RECOGNITION.md": (
        r"0<E[S_R]<\infty",
        r"E[|U_R|]<\infty",
        r"E[|U_R|S_R]<\infty",
    ),
    ROOT / "experiments/E4_INTERACTION.md": (
        r"0<E[S_R]<\infty",
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
        r"0<\mathbb E[S]<\infty",
        r"\mathbb E[|X|]<\infty",
        r"\mathbb E[|X|S]<\infty",
        r"\mathbb E[|U_R|]<\infty",
        r"\mathbb E[|U_R|S_R]<\infty",
        r"\mathbb E[|U_1|S_0]<\infty",
    ),
    ROOT / "paper/sections/appendix.tex": (
        r"0<\mathbb E[S]<\infty",
        r"\mathbb E[|X|]<\infty",
        r"\mathbb E[|X|S]<\infty",
        r"\mathbb E[|U_R|]<\infty",
        r"\mathbb E[|U_R|S_R]<\infty",
        r"\mathbb E[|U_1|S_0]<\infty",
    ),
}
EXPECTED_DOMAIN_SURFACE_BLOBS = {
    "theory/core_theorems.md": "0047670c137ed9ee4fb06780454b4d8bbdbb7c26",
    "theory/theorem_1_3.md": "b78fae00f097555944c2c9f9b42cbe269136461a",
    "theory/theorem_4_5.md": "a84c2667dc5138e744fea1ea5ad2730cc2d88995",
    "experiments/E1_FOSD.md": "a45119f37c3bdde640900b66052b3add935f5f75",
    "experiments/E3_RECOGNITION.md": "0db4c2a54067749659a8123ec5599c8814529f21",
    "experiments/E4_INTERACTION.md": "9e7ba2125e5f4dfd10713cccd213ee822481e25e",
    "paper/sections/formal_model.tex": "b98223ce0b38f5d9c5e49f447cbddd8d4eee4196",
    "paper/sections/theorems.tex": "54c6cc260ff39344933d432d85790298454a7492",
    "paper/sections/appendix.tex": "f55de6faf4ce50edd5ba301670ce58810a9db49a",
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


def git_text(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def require_exact_current(text: str, current: str, label: str) -> None:
    if text.count(current) != 1:
        raise SystemExit(
            f"Core-theorem lock validation failed: approved current {label} must occur exactly once"
        )


def validate_domain_surfaces() -> None:
    errors: list[str] = []
    if set(EXPECTED_DOMAIN_SURFACE_BLOBS) != {
        path.relative_to(ROOT).as_posix() for path in DOMAIN_SURFACES
    }:
        errors.append("validator self-contract: domain-surface blob map differs from DOMAIN_SURFACES")

    for path, snippets in DOMAIN_SURFACES.items():
        relative = path.relative_to(ROOT).as_posix()
        if path.is_symlink() or not path.is_file():
            errors.append(f"missing/invalid theorem-domain surface: {relative}")
            continue

        expected_blob = EXPECTED_DOMAIN_SURFACE_BLOBS.get(relative)
        if expected_blob is None:
            errors.append(f"{relative}: no audited domain-surface blob identity")
            continue
        try:
            head_blob = git_text("rev-parse", f"HEAD:{relative}")
            worktree_blob = git_text("hash-object", relative)
        except subprocess.CalledProcessError as exc:
            errors.append(f"{relative}: unable to resolve Git blob identity: {exc}")
            continue
        if head_blob != expected_blob:
            errors.append(
                f"{relative}: committed theorem-domain surface drift: "
                f"HEAD has {head_blob}, expected {expected_blob}"
            )
        if worktree_blob != expected_blob:
            errors.append(
                f"{relative}: working-tree theorem-domain surface drift: "
                f"{worktree_blob}, expected {expected_blob}"
            )

        text = path.read_text(encoding="utf-8")
        for snippet in snippets:
            if snippet not in text:
                errors.append(
                    f"{relative}: missing approved domain assumption {snippet!r}"
                )
    if errors:
        raise SystemExit("Core-theorem domain-surface validation failed:\n" + "\n".join(errors))


def main() -> None:
    if SOURCE.is_symlink() or not SOURCE.is_file():
        raise SystemExit(
            "Core-theorem lock validation failed: theory/core_theorems.tex must be a "
            "nonsymlink regular file"
        )

    text = SOURCE.read_text(encoding="utf-8")
    approved = [
        (CURRENT_TITLE, FROZEN_TITLE, "title"),
        (CURRENT_SETUP, FROZEN_SETUP, "setup integrability text"),
        (CURRENT_T1_ASSUMPTION, FROZEN_T1_ASSUMPTION, "T1 accessibility/integrability text"),
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
            "domain corrections, the T1-T5 TeX body differs from frozen v0.3 canonical "
            f"blob {FROZEN_V03_BLOB}; got {actual}. Any additional theorem/proof/boundary change "
            "requires explicit scientific review."
        )

    validate_domain_surfaces()

    print(
        "Core-theorem lock validation passed: after exactly four approved normalizations "
        "(version-neutral title, setup base-integrability, complete generic T1 domain, and "
        "T5 cross-integrability), "
        f"theory/core_theorems.tex matches frozen v0.3 commit {FROZEN_V03_COMMIT[:12]}… "
        f"blob {FROZEN_V03_BLOB}; all {len(DOMAIN_SURFACES)} audited theory/card/manuscript "
        "domain surfaces match their committed/worktree blob identities and contain the "
        "approved domain assumptions."
    )


if __name__ == "__main__":
    main()
