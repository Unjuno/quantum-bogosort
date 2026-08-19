"""Validate the canonical H/T/D/C/U experiment-card contract against the manifest.

The manifest fixes machine-readable experiment metadata and provenance. The Markdown
cards are the human review surface. This validator prevents either side from drifting
while still looking superficially complete: titles/claims are locked, the seven rendered
H2 sections and their order are fixed, and every manifest CSV must appear exactly once in
``D — Data / Result`` and nowhere else in the rendered card surface. Experiment cards
standardize on ATX headings; Setext and raw-HTML H1/H2 forms are rejected so additional
visible headings cannot evade the canonical schema parser.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "experiments" / "manifest.csv"
EXPECTED_H2 = [
    "H — Hypothesis",
    "T — Test",
    "D — Data / Result",
    "C — Controls / Counterexamples",
    "U — Uncertainty / Interpretation Boundary",
    "ERROR CHECK",
    "Linked theory",
]
EXPECTED = {
    "E1": {
        "card": "experiments/E1_FOSD.md",
        "heading": "E1 — Pure QBS Weighting, Tail Identities, and FOSD",
        "title": "Pure QBS weighting, tail identities, and FOSD",
        "primary_claim": "Outcome-aligned accessibility changes FP means/tails; monotone conditional accessibility implies FOSD.",
    },
    "E2": {
        "card": "experiments/E2_LEARNED_AGENT.md",
        "heading": "E2 — Minimal Learned Agent and Endogenous Predictive Correlation",
        "title": "Minimal learned agent / endogenous predictive correlation",
        "primary_claim": "A small model that represents the needed nonlinear world structure learns predictive information and produces QBS uplift; misspecified models do not.",
    },
    "E3": {
        "card": "experiments/E3_RECOGNITION.md",
        "heading": "E3 — Recognition Decomposition on Paired Primitive Branches",
        "title": "Recognition decomposition on paired primitive branches",
        "primary_claim": "Recognition can change trajectories and FP accessibility simultaneously; total FP effect decomposes exactly into policy and QBS terms.",
    },
    "E4": {
        "card": "experiments/E4_INTERACTION.md",
        "heading": "E4 — Adaptive-Policy / QBS Interaction",
        "title": "Adaptive-policy / QBS interaction",
        "primary_claim": "The interaction sign follows the covariance of policy improvement with accessibility under a fixed selector; the general selector-changing case decomposes into targeting and selector-map-shift terms.",
    },
    "E5": {
        "card": "experiments/E5_BRANCH_MAP.md",
        "heading": "E5 — Cross-Branch Recognition and Correlated Decision Maps",
        "title": "Cross-branch recognition and correlated decision maps",
        "primary_claim": "Shared recognition-dependent policy and shared world structure induce correlated decisions; execution-strength sweeps are paired on common primitive randomness.",
    },
}
H1_RE = re.compile(r"^ {0,3}#\s+(.+?)\s*$", re.MULTILINE)
H2_RE = re.compile(r"^ {0,3}##\s+(.+?)\s*$", re.MULTILINE)
CSV_RE = re.compile(r"data/processed/([A-Za-z0-9_.-]+\.csv)")
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
CLOSING_FENCE_RE = re.compile(r"^ {0,3}([`~]{3,})[ \t]*$")
SETEXT_UNDERLINE_RE = re.compile(r"^ {0,3}(?:=+|-+)[ \t]*$")
RAW_HTML_H1_H2_RE = re.compile(r"<\s*/?\s*h[12](?:\s|>)", re.IGNORECASE)


def split_files(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def closes_fence(line: str, marker: str) -> bool:
    match = CLOSING_FENCE_RE.match(line)
    if not match:
        return False
    candidate = match.group(1)
    return candidate[0] == marker[0] and len(candidate) >= len(marker)


def rendered_markdown_surface(text: str) -> str:
    """Remove fenced literal code so card structure is parsed from rendered Markdown."""
    output: list[str] = []
    fence_marker: str | None = None

    for line in text.splitlines():
        if fence_marker is not None:
            if closes_fence(line, fence_marker):
                fence_marker = None
            continue

        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)
            info = match.group(2)
            if marker[0] != "`" or "`" not in info:
                fence_marker = marker
                continue

        output.append(line)

    return "\n".join(output)


def non_atx_heading_errors(relative: str, text: str) -> list[str]:
    """Reject rendered H1/H2 forms outside the experiment-card ATX schema."""
    errors: list[str] = []
    lines = text.splitlines()

    for index, line in enumerate(lines):
        if RAW_HTML_H1_H2_RE.search(line):
            errors.append(
                f"{relative}:{index + 1}: raw-HTML H1/H2 is outside the canonical ATX card schema"
            )

        if index == 0 or not SETEXT_UNDERLINE_RE.match(line):
            continue
        previous = lines[index - 1]
        if previous.strip():
            errors.append(
                f"{relative}:{index + 1}: Setext H1/H2 is outside the canonical ATX card schema"
            )

    return errors


def sections(text: str) -> tuple[list[str], dict[str, str]]:
    """Return ordered rendered H2 headings and exact bodies between H2 boundaries."""
    matches = list(H2_RE.finditer(text))
    headings = [match.group(1).strip() for match in matches]
    bodies: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        bodies[match.group(1).strip()] = text[start:end].strip()
    return headings, bodies


def main() -> None:
    errors: list[str] = []
    with MANIFEST.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    ids = [row.get("experiment_id", "") for row in rows]
    if ids != list(EXPECTED):
        errors.append(
            f"manifest/card validator expects experiment IDs {list(EXPECTED)!r}; got {ids!r}"
        )

    for row in rows:
        experiment_id = row.get("experiment_id", "")
        expected = EXPECTED.get(experiment_id)
        if expected is None:
            continue

        if row.get("title", "") != expected["title"]:
            errors.append(
                f"{experiment_id}: canonical manifest title drift: {row.get('title')!r} "
                f"!= {expected['title']!r}"
            )
        if row.get("primary_claim", "") != expected["primary_claim"]:
            errors.append(
                f"{experiment_id}: canonical manifest primary_claim drift: "
                f"{row.get('primary_claim')!r} != {expected['primary_claim']!r}"
            )

        card_path = ROOT / expected["card"]
        if not card_path.is_file():
            errors.append(f"{experiment_id}: missing experiment card {expected['card']}")
            continue
        relative = card_path.relative_to(ROOT).as_posix()
        text = rendered_markdown_surface(card_path.read_text(encoding="utf-8"))
        errors.extend(non_atx_heading_errors(relative, text))

        h1 = H1_RE.findall(text)
        if h1 != [expected["heading"]]:
            errors.append(
                f"{experiment_id}: rendered card must contain exactly canonical H1 "
                f"{expected['heading']!r}; got {h1!r}"
            )

        headings, bodies = sections(text)
        if headings != EXPECTED_H2:
            errors.append(
                f"{experiment_id}: rendered H2 schema/order drift: {headings!r} != {EXPECTED_H2!r}"
            )

        for heading in EXPECTED_H2:
            body = bodies.get(heading)
            if body is None:
                continue
            if not body.strip():
                errors.append(f"{experiment_id}: empty rendered card section {heading!r}")

        expected_csvs = split_files(row.get("locked_files", "")) + split_files(
            row.get("reproduction_files", "")
        )
        d_body = bodies.get("D — Data / Result", "")
        d_csvs = CSV_RE.findall(d_body)
        d_counts = Counter(d_csvs)
        expected_counts = Counter(expected_csvs)
        if d_counts != expected_counts:
            missing = sorted((expected_counts - d_counts).elements())
            extra = sorted((d_counts - expected_counts).elements())
            if missing:
                errors.append(
                    f"{experiment_id}: manifest CSV(s) missing from rendered D section: "
                    + ", ".join(missing)
                )
            if extra:
                errors.append(
                    f"{experiment_id}: unexpected/duplicate CSV(s) in rendered D section: "
                    + ", ".join(extra)
                )

        non_d_text = "\n".join(
            body for heading, body in bodies.items() if heading != "D — Data / Result"
        )
        outside_csvs = CSV_RE.findall(non_d_text)
        if outside_csvs:
            errors.append(
                f"{experiment_id}: data/processed CSV reference(s) outside rendered D section: "
                + ", ".join(outside_csvs)
            )

        full_counts = Counter(CSV_RE.findall(text))
        if full_counts != expected_counts:
            errors.append(
                f"{experiment_id}: rendered card-wide CSV occurrence contract drift: "
                f"{dict(full_counts)!r} != {dict(expected_counts)!r}"
            )

    if errors:
        raise SystemExit("Experiment-card validation failed:\n" + "\n".join(errors))

    print(
        "Experiment-card validation passed: E1-E5 canonical manifest titles/claims, rendered "
        "ATX-only H1/H2 schema, ordered H/T/D/C/U + ERROR CHECK + Linked theory sections, and "
        "rendered D-section-only CSV routing match exactly."
    )


if __name__ == "__main__":
    main()
