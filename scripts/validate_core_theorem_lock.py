"""Verify that the canonical standalone T1-T5 TeX body matches frozen v0.3.

The public Markdown theorem pages may receive rendering-only edits. The standalone
``theory/core_theorems.tex`` file is the compact canonical theorem/proof source. Since
v0.3 its only intentional change is the version-neutral document title. Normalize that
single title line back to the frozen title and require the resulting Git blob identity
to equal the v0.3 snapshot blob. Any other body/proof/boundary change therefore fails CI.
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


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit("Core-theorem lock validation failed: missing theory/core_theorems.tex")

    text = SOURCE.read_text(encoding="utf-8")
    if text.count(CURRENT_TITLE) != 1:
        raise SystemExit(
            "Core-theorem lock validation failed: canonical current title must occur exactly once"
        )
    if FROZEN_TITLE in text:
        raise SystemExit(
            "Core-theorem lock validation failed: stale frozen title remains in current source"
        )

    normalized = text.replace(CURRENT_TITLE, FROZEN_TITLE, 1)
    actual = git_blob_sha(normalized)
    if actual != FROZEN_V03_BLOB:
        raise SystemExit(
            "Core-theorem lock validation failed: normalized T1-T5 TeX body differs from "
            f"frozen v0.3 canonical blob {FROZEN_V03_BLOB}; got {actual}. "
            "A theorem/proof/boundary change requires explicit scientific review rather than "
            "being absorbed as repository QA."
        )

    print(
        "Core-theorem lock validation passed: after the single allowed version-neutral title "
        f"normalization, theory/core_theorems.tex matches frozen v0.3 commit "
        f"{FROZEN_V03_COMMIT[:12]}… blob {FROZEN_V03_BLOB}."
    )


if __name__ == "__main__":
    main()
