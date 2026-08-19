"""Validate the narrow BibTeX metadata contract used by the QBS manuscript.

The manuscript intentionally uses the stock ``plain`` BibTeX style. Machine-readable
``eprint``/``doi`` fields are therefore paired with standard printable fields:
arXiv-only records are ``@misc`` entries with ``howpublished = {arXiv:<id>}``, while
journal and book-chapter records carry a printable ``note = {doi:<doi>}``.

A separate reviewed fact lock records the citation-key set, record type, year, author,
title, publication locator, canonical DOI/arXiv identifier, and provenance class. The
lock prevents a later edit from silently reverting already-reviewed publication identity
or chronology. It does not replace external factual verification of the bibliography.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "paper/references.bib"
FACT_LOCK = ROOT / "paper/bibliography_fact_lock.md"
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


def split_entries(text: str) -> list[tuple[str, str, str]]:
    """Return (type, key, body) while respecting braces inside an entry."""
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
        end = None
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
        body_start = match.end()
        entries.append((entry_type.lower(), key, text[body_start:end]))
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


def require_fields(key: str, fields: dict[str, str], names: tuple[str, ...], errors: list[str]) -> None:
    for name in names:
        if not fields.get(name, "").strip():
            errors.append(f"{key}: missing/nonempty required field {name}")


def publication_locator(entry_type: str, fields: dict[str, str]) -> str:
    """Return the exact human-readable publication locator locked by the audit."""
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
    """Parse the single Markdown fact-lock table into a citation-key mapping."""
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
            errors.append(
                f"paper/bibliography_fact_lock.md:{key}: unsupported record_type "
                f"{record['record_type']!r}"
            )
        if not re.fullmatch(r"(?:19|20)\d{2}", record["year"]):
            errors.append(
                f"paper/bibliography_fact_lock.md:{key}: invalid four-digit year {record['year']!r}"
            )
        for field_name in ("author", "title", "locator"):
            if not record[field_name]:
                errors.append(
                    f"paper/bibliography_fact_lock.md:{key}: empty reviewed field {field_name}"
                )
        if record["provenance"] not in ALLOWED_PROVENANCE:
            errors.append(
                f"paper/bibliography_fact_lock.md:{key}: unsupported provenance "
                f"{record['provenance']!r}"
            )

        canonical_id = record["canonical_id"]
        if canonical_id.startswith("doi:"):
            if record["record_type"] not in {"article", "incollection"}:
                errors.append(
                    f"paper/bibliography_fact_lock.md:{key}: DOI-backed record must be a publication"
                )
            if not DOI_RE.fullmatch(canonical_id.removeprefix("doi:")):
                errors.append(
                    f"paper/bibliography_fact_lock.md:{key}: malformed DOI canonical_id {canonical_id!r}"
                )
        elif canonical_id.startswith("arxiv:"):
            if record["record_type"] != "misc":
                errors.append(
                    f"paper/bibliography_fact_lock.md:{key}: arXiv-backed record must be @misc"
                )
            eprint = canonical_id.removeprefix("arxiv:")
            if not (ARXIV_NEW_RE.fullmatch(eprint) or ARXIV_OLD_RE.fullmatch(eprint)):
                errors.append(
                    f"paper/bibliography_fact_lock.md:{key}: malformed arXiv canonical_id {canonical_id!r}"
                )
        else:
            errors.append(
                f"paper/bibliography_fact_lock.md:{key}: canonical_id must begin doi: or arxiv:"
            )
        records[key] = record
    return records


def main() -> None:
    errors: list[str] = []
    if not BIB.is_file():
        raise SystemExit("Missing paper/references.bib")
    if not FACT_LOCK.is_file():
        raise SystemExit("Missing paper/bibliography_fact_lock.md")

    try:
        entries = split_entries(BIB.read_text(encoding="utf-8"))
    except ValueError as exc:
        raise SystemExit(f"Bibliography metadata validation failed:\n{exc}") from exc

    if not entries:
        errors.append("paper/references.bib contains no entries")

    fact_lock = parse_fact_lock(FACT_LOCK.read_text(encoding="utf-8"), errors)

    keys: set[str] = set()
    dois: dict[str, str] = {}
    eprints: dict[str, str] = {}
    bib_records: dict[str, tuple[str, dict[str, str]]] = {}
    article_count = 0
    incollection_count = 0
    misc_count = 0

    for entry_type, key, body in entries:
        if key in keys:
            errors.append(f"duplicate bibliography key: {key}")
        keys.add(key)

        if entry_type not in ALLOWED_TYPES:
            errors.append(
                f"{key}: bibliography contract permits only @article/@incollection/@misc, got @{entry_type}"
            )

        fields = parse_fields(key, body, errors)
        bib_records[key] = (entry_type, fields)
        require_fields(key, fields, ("author", "title", "year"), errors)

        year = fields.get("year", "")
        if year and not re.fullmatch(r"(?:19|20)\d{2}", year):
            errors.append(f"{key}: year must be four digits in 1900-2099; got {year!r}")

        doi = fields.get("doi", "")
        eprint = fields.get("eprint", "")
        journal = fields.get("journal", "")
        note = fields.get("note", "")
        howpublished = fields.get("howpublished", "")

        if entry_type == "article":
            article_count += 1
            require_fields(key, fields, ("journal", "volume", "pages", "doi"), errors)
            if eprint:
                errors.append(
                    f"{key}: current @article contract uses DOI publication provenance, not eprint"
                )
            if howpublished:
                errors.append(f"{key}: @article must not use howpublished")
            if fields.get("booktitle") or fields.get("publisher"):
                errors.append(f"{key}: @article must not use book-chapter fields")
            if doi and note != f"doi:{doi}":
                errors.append(
                    f"{key}: stock plain.bst printable DOI note must be exactly 'doi:{doi}'"
                )

        elif entry_type == "incollection":
            incollection_count += 1
            require_fields(
                key,
                fields,
                ("booktitle", "editor", "publisher", "pages", "doi"),
                errors,
            )
            if journal:
                errors.append(f"{key}: @incollection must not contain journal")
            if eprint:
                errors.append(
                    f"{key}: current @incollection contract uses DOI publication provenance, not eprint"
                )
            if howpublished:
                errors.append(f"{key}: @incollection must not use howpublished")
            if doi and note != f"doi:{doi}":
                errors.append(
                    f"{key}: stock plain.bst printable DOI note must be exactly 'doi:{doi}'"
                )

        elif entry_type == "misc":
            misc_count += 1
            if journal:
                errors.append(f"{key}: arXiv @misc must not contain journal")
            if fields.get("booktitle") or fields.get("publisher"):
                errors.append(f"{key}: arXiv @misc must not use publication-container fields")
            if doi:
                errors.append(f"{key}: arXiv @misc must not contain DOI")
            if note:
                errors.append(f"{key}: arXiv @misc uses howpublished, not note")
            if not eprint:
                errors.append(f"{key}: arXiv @misc requires an eprint identifier")
            if eprint and howpublished != f"arXiv:{eprint}":
                errors.append(
                    f"{key}: stock plain.bst printable arXiv field must be exactly "
                    f"'arXiv:{eprint}' in howpublished"
                )

        if doi:
            if not DOI_RE.fullmatch(doi):
                errors.append(f"{key}: malformed DOI {doi!r}")
            normalized_doi = doi.lower()
            if normalized_doi in dois:
                errors.append(f"{key}: DOI duplicates {dois[normalized_doi]}: {doi}")
            else:
                dois[normalized_doi] = key

        if eprint:
            if not (ARXIV_NEW_RE.fullmatch(eprint) or ARXIV_OLD_RE.fullmatch(eprint)):
                errors.append(f"{key}: malformed arXiv eprint identifier {eprint!r}")
            if fields.get("archiveprefix", "") != "arXiv":
                errors.append(f"{key}: eprint requires archivePrefix = {{arXiv}}")

            primary_class = fields.get("primaryclass", "")
            if not primary_class:
                errors.append(f"{key}: arXiv eprint requires primaryClass")
            elif not ARXIV_CLASS_RE.fullmatch(primary_class):
                errors.append(f"{key}: malformed arXiv primaryClass {primary_class!r}")

            normalized_eprint = eprint.lower()
            if normalized_eprint in eprints:
                errors.append(f"{key}: eprint duplicates {eprints[normalized_eprint]}: {eprint}")
            else:
                eprints[normalized_eprint] = key

        if fields.get("primaryclass") and not eprint:
            errors.append(f"{key}: primaryClass is present without an arXiv eprint")
        if fields.get("archiveprefix") and not eprint:
            errors.append(f"{key}: archivePrefix is present without an arXiv eprint")

        for field_name, value in fields.items():
            lowered = value.lower()
            if any(token in lowered for token in ("todo", "tbd", "placeholder", "example.com")):
                errors.append(f"{key}: placeholder-like value in {field_name}: {value!r}")

    if set(fact_lock) != keys:
        missing_from_lock = sorted(keys - set(fact_lock))
        missing_from_bib = sorted(set(fact_lock) - keys)
        if missing_from_lock:
            errors.append(
                "bibliography fact lock is missing BibTeX key(s): " + ", ".join(missing_from_lock)
            )
        if missing_from_bib:
            errors.append(
                "bibliography fact lock names absent BibTeX key(s): " + ", ".join(missing_from_bib)
            )

    for key in sorted(keys & set(fact_lock)):
        entry_type, fields = bib_records[key]
        locked = fact_lock[key]
        if entry_type != locked["record_type"]:
            errors.append(
                f"{key}: BibTeX record type @{entry_type} != reviewed fact lock @{locked['record_type']}"
            )
        if fields.get("year", "") != locked["year"]:
            errors.append(
                f"{key}: BibTeX year {fields.get('year')!r} != reviewed fact lock {locked['year']!r}"
            )
        for field_name in ("author", "title"):
            actual_value = fields.get(field_name, "")
            if actual_value != locked[field_name]:
                errors.append(
                    f"{key}: BibTeX {field_name} {actual_value!r} != reviewed fact lock "
                    f"{locked[field_name]!r}"
                )

        actual_locator = publication_locator(entry_type, fields)
        if actual_locator != locked["locator"]:
            errors.append(
                f"{key}: BibTeX publication locator {actual_locator!r} != reviewed fact lock "
                f"{locked['locator']!r}"
            )

        canonical_id = locked["canonical_id"]
        if canonical_id.startswith("doi:"):
            locked_doi = canonical_id.removeprefix("doi:")
            if fields.get("doi", "") != locked_doi:
                errors.append(
                    f"{key}: BibTeX DOI {fields.get('doi')!r} != reviewed fact lock {locked_doi!r}"
                )
            if locked["provenance"] != "definitive-publication":
                errors.append(
                    f"{key}: DOI-backed fact lock must use definitive-publication provenance"
                )
        elif canonical_id.startswith("arxiv:"):
            locked_eprint = canonical_id.removeprefix("arxiv:")
            if fields.get("eprint", "") != locked_eprint:
                errors.append(
                    f"{key}: BibTeX eprint {fields.get('eprint')!r} != reviewed fact lock {locked_eprint!r}"
                )
            if locked["provenance"] == "definitive-publication":
                errors.append(
                    f"{key}: arXiv-backed fact lock cannot use definitive-publication provenance"
                )

    if errors:
        raise SystemExit("Bibliography metadata validation failed:\n" + "\n".join(errors))

    print(
        "Bibliography metadata validation passed: "
        f"{len(entries)} unique records ({article_count} journal @article, "
        f"{incollection_count} book-chapter @incollection, {misc_count} arXiv @misc); "
        f"{len(dois)} unique printable DOI records and {len(eprints)} unique printable arXiv "
        f"identifiers/classes validated for stock plain.bst; {len(fact_lock)} reviewed fact-lock "
        "records match citation key, class, year, author, title, publication locator, and "
        "canonical identifier exactly."
    )


if __name__ == "__main__":
    main()
