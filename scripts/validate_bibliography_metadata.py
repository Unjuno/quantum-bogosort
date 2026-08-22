"""Validate the reviewed QBS manuscript bibliography and fact-lock contract.

The manuscript uses stock ``plain`` BibTeX. DOI-backed publications therefore carry a
printable ``note = {doi:...}``, while arXiv-only records are ``@misc`` entries with
``howpublished = {arXiv:...}``.

The BibTeX file and reviewed fact-lock table are Git-blob locked before semantic checks.
Updating either reviewed source therefore requires an explicit audit update here.
"""
from __future__ import annotations

from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "paper/references.bib"
FACT_LOCK = ROOT / "paper/bibliography_fact_lock.md"
EXPECTED_REVIEWED_BLOBS = {
    "paper/references.bib": "41c64261da92734c59ab2a3550c30cc08cd52fb4",
    "paper/bibliography_fact_lock.md": "25054fbbc757fa631694e51d4a4ba62041eec392",
}

ENTRY_START_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.IGNORECASE)
FIELD_RE = re.compile(r"^\s*([A-Za-z][A-Za-z0-9]*)\s*=\s*\{(.*)\}\s*,?\s*$")
ARXIV_NEW_RE = re.compile(r"^\d{4}\.\d{4,5}(?:v\d+)?$")
ARXIV_OLD_RE = re.compile(r"^[a-z-]+/\d{7}(?:v\d+)?$", re.IGNORECASE)
ARXIV_CLASS_RE = re.compile(r"^[A-Za-z]+(?:[.-][A-Za-z]+)*$")
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
ALLOWED_TYPES = {"article", "incollection", "misc"}
FACT_LOCK_HEADER = [
    "citation_key",
    "record_type",
    "year",
    "author",
    "title",
    "locator",
    "canonical_id",
    "provenance",
]
ALLOWED_PROVENANCE = {
    "definitive-publication",
    "retained-early-preprint",
    "retained-preprint",
    "retained-working-paper",
    "latest-working-preprint",
}


def git_text(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def validate_reviewed_blobs(errors: list[str]) -> None:
    for relative, expected in EXPECTED_REVIEWED_BLOBS.items():
        path = ROOT / relative
        if path.is_symlink() or not path.is_file():
            errors.append(f"{relative}: missing/invalid reviewed bibliography source")
            continue
        try:
            head_blob = git_text("rev-parse", f"HEAD:{relative}")
            worktree_blob = git_text("hash-object", relative)
        except subprocess.CalledProcessError as exc:
            errors.append(f"{relative}: unable to resolve Git blob identity: {exc}")
            continue
        if head_blob != expected:
            errors.append(
                f"{relative}: committed reviewed-bibliography drift: HEAD has {head_blob}, expected {expected}"
            )
        if worktree_blob != expected:
            errors.append(
                f"{relative}: working-tree reviewed-bibliography drift: {worktree_blob}, expected {expected}"
            )


def split_entries(text: str) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    pos = 0
    while True:
        match = ENTRY_START_RE.search(text, pos)
        if not match:
            if text[pos:].strip():
                raise ValueError(f"unsupported text outside BibTeX entries: {text[pos:].strip()!r}")
            break
        if text[pos:match.start()].strip():
            raise ValueError(
                "unsupported text between BibTeX entries: "
                f"{text[pos:match.start()].strip()!r}"
            )
        entry_type, key = match.groups()
        brace_start = text.find("{", match.start())
        depth = 0
        escaped = False
        end: int | None = None
        for index in range(brace_start, len(text)):
            char = text[index]
            if escaped:
                escaped = False
                continue
            if char == "\\":
                escaped = True
                continue
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    end = index
                    break
        if end is None:
            raise ValueError(f"unclosed BibTeX entry {key}")
        entries.append((entry_type.lower(), key, text[match.end():end]))
        pos = end + 1
    return entries


def parse_fields(key: str, body: str, errors: list[str]) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in body.splitlines():
        if not line.strip():
            continue
        match = FIELD_RE.fullmatch(line)
        if not match:
            errors.append(f"{key}: unsupported/multiline BibTeX field syntax: {line.strip()!r}")
            continue
        name, value = match.groups()
        normalized = name.lower()
        if normalized in fields:
            errors.append(f"{key}: duplicate field {name}")
        fields[normalized] = value.strip()
    return fields


def require_fields(
    key: str, fields: dict[str, str], names: tuple[str, ...], errors: list[str]
) -> None:
    for name in names:
        if not fields.get(name, "").strip():
            errors.append(f"{key}: missing/nonempty required field {name}")


def publication_locator(entry_type: str, fields: dict[str, str]) -> str:
    if entry_type == "article":
        volume = fields.get("volume", "")
        number = fields.get("number", "")
        volume_number = f"{volume}({number})" if number else volume
        return f"{fields.get('journal', '')}; {volume_number}; {fields.get('pages', '')}"
    if entry_type == "incollection":
        return "; ".join(
            [
                fields.get("booktitle", ""),
                fields.get("editor", ""),
                fields.get("publisher", ""),
                fields.get("pages", ""),
            ]
        )
    if entry_type == "misc":
        return "arXiv"
    return ""


def parse_fact_lock(text: str, errors: list[str]) -> dict[str, dict[str, str]]:
    table_lines = [line.strip() for line in text.splitlines() if line.strip().startswith("|")]
    if len(table_lines) < 3:
        errors.append("paper/bibliography_fact_lock.md: missing bibliography fact-lock table")
        return {}

    def cells(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip().strip("|").split("|")]

    header = cells(table_lines[0])
    if header != FACT_LOCK_HEADER:
        errors.append(
            "paper/bibliography_fact_lock.md: fact-lock header must be exactly "
            f"{FACT_LOCK_HEADER!r}; got {header!r}"
        )
    separator = cells(table_lines[1])
    if len(separator) != len(FACT_LOCK_HEADER) or any(
        not re.fullmatch(r":?-{3,}:?", cell) for cell in separator
    ):
        errors.append("paper/bibliography_fact_lock.md: malformed Markdown table separator")

    records: dict[str, dict[str, str]] = {}
    for line_no, line in enumerate(table_lines[2:], start=3):
        row = cells(line)
        if len(row) != len(FACT_LOCK_HEADER):
            errors.append(
                f"paper/bibliography_fact_lock.md: table row {line_no} has {len(row)} cells; "
                f"expected {len(FACT_LOCK_HEADER)}"
            )
            continue
        record = dict(zip(FACT_LOCK_HEADER, row, strict=True))
        key = record["citation_key"]
        if not key:
            errors.append(f"paper/bibliography_fact_lock.md: table row {line_no} has empty citation_key")
            continue
        if key in records:
            errors.append(f"paper/bibliography_fact_lock.md: duplicate citation_key {key}")
            continue
        if record["record_type"] not in ALLOWED_TYPES:
            errors.append(f"paper/bibliography_fact_lock.md:{key}: unsupported record_type")
        if not re.fullmatch(r"(?:19|20)\d{2}", record["year"]):
            errors.append(f"paper/bibliography_fact_lock.md:{key}: invalid year {record['year']!r}")
        for field in ("author", "title", "locator"):
            if not record[field]:
                errors.append(f"paper/bibliography_fact_lock.md:{key}: empty reviewed field {field}")
        if record["provenance"] not in ALLOWED_PROVENANCE:
            errors.append(
                f"paper/bibliography_fact_lock.md:{key}: unsupported provenance {record['provenance']!r}"
            )

        canonical = record["canonical_id"]
        if canonical.startswith("doi:"):
            if record["record_type"] not in {"article", "incollection"}:
                errors.append(f"paper/bibliography_fact_lock.md:{key}: DOI record must be a publication")
            if not DOI_RE.fullmatch(canonical.removeprefix("doi:")):
                errors.append(f"paper/bibliography_fact_lock.md:{key}: malformed DOI canonical_id")
        elif canonical.startswith("arxiv:"):
            if record["record_type"] != "misc":
                errors.append(f"paper/bibliography_fact_lock.md:{key}: arXiv record must be @misc")
            eprint = canonical.removeprefix("arxiv:")
            if not (ARXIV_NEW_RE.fullmatch(eprint) or ARXIV_OLD_RE.fullmatch(eprint)):
                errors.append(f"paper/bibliography_fact_lock.md:{key}: malformed arXiv canonical_id")
        else:
            errors.append(f"paper/bibliography_fact_lock.md:{key}: canonical_id must begin doi: or arxiv:")
        records[key] = record
    return records


def main() -> None:
    errors: list[str] = []
    validate_reviewed_blobs(errors)

    try:
        entries = split_entries(BIB.read_text(encoding="utf-8"))
    except ValueError as exc:
        raise SystemExit(f"Bibliography metadata validation failed:\n{exc}") from exc
    fact_lock = parse_fact_lock(FACT_LOCK.read_text(encoding="utf-8"), errors)

    keys: set[str] = set()
    dois: dict[str, str] = {}
    eprints: dict[str, str] = {}
    bib_records: dict[str, tuple[str, dict[str, str]]] = {}
    counts = {"article": 0, "incollection": 0, "misc": 0}

    for entry_type, key, body in entries:
        if key in keys:
            errors.append(f"duplicate bibliography key: {key}")
        keys.add(key)
        if entry_type not in ALLOWED_TYPES:
            errors.append(f"{key}: unsupported bibliography type @{entry_type}")

        fields = parse_fields(key, body, errors)
        bib_records[key] = (entry_type, fields)
        require_fields(key, fields, ("author", "title", "year"), errors)
        if not re.fullmatch(r"(?:19|20)\d{2}", fields.get("year", "")):
            errors.append(f"{key}: year must be four digits in 1900-2099")

        if entry_type in counts:
            counts[entry_type] += 1

        doi = fields.get("doi", "")
        eprint = fields.get("eprint", "")
        if entry_type == "article":
            require_fields(key, fields, ("journal", "volume", "pages", "doi"), errors)
            if eprint or fields.get("howpublished") or fields.get("booktitle") or fields.get("publisher"):
                errors.append(f"{key}: @article contains incompatible preprint/book fields")
            if doi and fields.get("note") != f"doi:{doi}":
                errors.append(f"{key}: printable DOI note must be exactly 'doi:{doi}'")
        elif entry_type == "incollection":
            require_fields(key, fields, ("booktitle", "editor", "publisher", "pages", "doi"), errors)
            if fields.get("journal") or eprint or fields.get("howpublished"):
                errors.append(f"{key}: @incollection contains incompatible journal/preprint fields")
            if doi and fields.get("note") != f"doi:{doi}":
                errors.append(f"{key}: printable DOI note must be exactly 'doi:{doi}'")
        elif entry_type == "misc":
            require_fields(key, fields, ("eprint", "archiveprefix", "primaryclass", "howpublished"), errors)
            if fields.get("journal") or fields.get("booktitle") or fields.get("publisher") or doi or fields.get("note"):
                errors.append(f"{key}: arXiv @misc contains incompatible publication fields")
            if eprint and fields.get("howpublished") != f"arXiv:{eprint}":
                errors.append(f"{key}: printable arXiv field must be exactly 'arXiv:{eprint}'")
            if fields.get("archiveprefix") != "arXiv":
                errors.append(f"{key}: archivePrefix must be exactly 'arXiv'")
            if fields.get("primaryclass") and not ARXIV_CLASS_RE.fullmatch(fields["primaryclass"]):
                errors.append(f"{key}: malformed primaryClass {fields['primaryclass']!r}")

        if doi:
            if not DOI_RE.fullmatch(doi):
                errors.append(f"{key}: malformed DOI {doi!r}")
            norm = doi.lower()
            if norm in dois:
                errors.append(f"{key}: DOI duplicates {dois[norm]}: {doi}")
            else:
                dois[norm] = key
        if eprint:
            if not (ARXIV_NEW_RE.fullmatch(eprint) or ARXIV_OLD_RE.fullmatch(eprint)):
                errors.append(f"{key}: malformed arXiv identifier {eprint!r}")
            norm = eprint.lower()
            if norm in eprints:
                errors.append(f"{key}: arXiv identifier duplicates {eprints[norm]}: {eprint}")
            else:
                eprints[norm] = key

    if keys != set(fact_lock):
        missing_lock = sorted(keys - set(fact_lock))
        missing_bib = sorted(set(fact_lock) - keys)
        if missing_lock:
            errors.append("BibTeX entries missing from fact lock: " + ", ".join(missing_lock))
        if missing_bib:
            errors.append("Fact-lock entries missing from BibTeX: " + ", ".join(missing_bib))

    for key in sorted(keys & set(fact_lock)):
        entry_type, fields = bib_records[key]
        record = fact_lock[key]
        expected_id = (
            f"doi:{fields.get('doi', '')}"
            if entry_type in {"article", "incollection"}
            else f"arxiv:{fields.get('eprint', '')}"
        )
        checks = {
            "record_type": entry_type,
            "year": fields.get("year", ""),
            "author": fields.get("author", ""),
            "title": fields.get("title", ""),
            "locator": publication_locator(entry_type, fields),
            "canonical_id": expected_id,
        }
        for field, expected in checks.items():
            if record[field] != expected:
                errors.append(
                    f"{key}: fact-lock {field} mismatch: {record[field]!r} != {expected!r}"
                )

    if errors:
        raise SystemExit("Bibliography metadata validation failed:\n" + "\n".join(errors))

    print(
        "Bibliography metadata validation passed: reviewed references.bib/fact-lock HEAD/worktree "
        f"blobs match; {len(entries)} unique records ({counts['article']} journal @article, "
        f"{counts['incollection']} book-chapter @incollection, {counts['misc']} arXiv @misc); "
        f"{len(dois)} unique printable DOI records and {len(eprints)} unique printable arXiv "
        "identifiers/classes validated for stock plain.bst; reviewed fact-lock records match "
        "citation key, class, year, author, title, publication locator, and canonical identifier exactly."
    )


if __name__ == "__main__":
    main()
