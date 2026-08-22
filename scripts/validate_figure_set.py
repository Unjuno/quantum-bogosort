"""Validate exact figure sets and the audited SVG/PDF numerical-data source contract.

Committed SVGs remain byte-reproducible outputs. The deterministic Figure 2 numerical CSV
is compared structurally and with a tight floating-point tolerance because GitHub-hosted
runner hardware can differ in the last few serialized bits even under the same pinned
Python/NumPy/pandas stack. After a successful comparison, the committed canonical CSV
bytes are restored so the workflow's later clean-worktree check remains exact.
"""
from pathlib import Path
import ast
import csv
import io
import math
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SVG_DIR = ROOT / "figures" / "generated"
PDF_DIR = ROOT / "figures" / "generated_pdf"
FIGURE_DATA = ROOT / "figures" / "figure_data.py"
SVG_GENERATOR = ROOT / "figures" / "generate_figures.py"
PDF_GENERATOR = ROOT / "figures" / "generate_pdf_figures.py"
FIG2_DATA_RELATIVE = "data/processed/fig2_fosd_theorem_illustration.csv"
FIG2_DATA = ROOT / FIG2_DATA_RELATIVE
NUMERIC_REL_TOL = 1e-12
NUMERIC_ABS_TOL = 1e-14
MAX_REPORTED_CELL_ERRORS = 20
EXPECTED_SOURCE_BLOBS = {
    "figures/figure_data.py": "6d765e7cf226bf538a2c967dabb6e565d652b3a4",
    "figures/generate_figures.py": "beae4597aa6f4e91ba0e6da29072a33e96619160",
    "figures/generate_pdf_figures.py": "7ef3f1aaddc8be33bdf7df77f342ff1c594ee5df",
}
EXPECTED_SVGS = {
    "fig1_framework.svg",
    "fig2_fosd.svg",
    "fig3_recognition_decomposition.svg",
    "fig4_interaction_sign.svg",
    "fig5_adaptation_quality.svg",
    "fig6_branch_coherence.svg",
    "fig7_predictive_alignment.svg",
}
EXPECTED_PDFS = {
    "fig1_framework.pdf",
    "fig2_fosd.pdf",
    "fig3_recognition_decomposition.pdf",
    "fig4_interaction_sign.pdf",
    "fig5_adaptation_quality.pdf",
    "fig6_branch_coherence.pdf",
}
SHARED_DATA_FUNCTIONS = {
    "fig2": "fosd_curves",
    "fig3": "recognition_bar_data",
    "fig4": "interaction_bar_data",
    "fig5": "adaptation_line_data",
    "fig6": "branch_line_data",
}
RENDERER_FUNCTIONS = {
    SVG_GENERATOR: {
        "fig2": "fig2",
        "fig3": "fig3",
        "fig4": "fig4",
        "fig5": "fig5",
        "fig6": "fig6",
    },
    PDF_GENERATOR: {
        "fig2": "fig2_fosd",
        "fig3": "fig3_recognition",
        "fig4": "fig4_interaction",
        "fig5": "fig5_adaptation",
        "fig6": "fig6_branch_coherence",
    },
}


def git_text(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def git_raw_text(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def check_source_blob_contract(errors: list[str]) -> None:
    """Lock the reviewed shared-data/rendering implementation to HEAD and worktree bytes.

    The AST checks below make the intended relationship readable, but a call-count check
    alone can be satisfied by dead code. These Git blob identities make any change to the
    audited figure-data/rendering layer an explicit contract update rather than an
    accidental green CI result.
    """
    for relative, expected in EXPECTED_SOURCE_BLOBS.items():
        path = ROOT / relative
        if path.is_symlink() or not path.is_file():
            errors.append(f"{relative}: missing/invalid audited figure source")
            continue
        try:
            head_blob = git_text("rev-parse", f"HEAD:{relative}")
            worktree_blob = git_text("hash-object", relative)
        except subprocess.CalledProcessError as exc:
            errors.append(f"{relative}: unable to resolve Git blob identity: {exc}")
            continue
        if head_blob != expected:
            errors.append(
                f"{relative}: committed audited figure-source drift: "
                f"HEAD has {head_blob}, expected {expected}"
            )
        if worktree_blob != expected:
            errors.append(
                f"{relative}: working-tree audited figure-source drift: "
                f"{worktree_blob}, expected {expected}"
            )


def check_exact(directory: Path, expected: set[str], label: str, errors: list[str]) -> None:
    if directory.is_symlink() or not directory.is_dir():
        errors.append(
            f"missing/invalid {label} directory: {directory.relative_to(ROOT)} "
            "(real directory required)"
        )
        return

    entries = {path.name for path in directory.iterdir()}
    missing = sorted(expected - entries)
    extra = sorted(entries - expected)
    if missing:
        errors.append(f"{label}: missing expected file(s): " + ", ".join(missing))
    if extra:
        errors.append(f"{label}: unexpected generated entry/entries: " + ", ".join(extra))

    invalid_files = sorted(
        name
        for name in expected
        if (directory / name).is_symlink() or not (directory / name).is_file()
    )
    if invalid_files:
        errors.append(
            f"{label}: expected path is not a nonsymlink regular file: "
            + ", ".join(invalid_files)
        )


def parsed_module(path: Path, errors: list[str]) -> ast.Module | None:
    if path.is_symlink() or not path.is_file():
        errors.append(
            f"missing/invalid figure source: {path.relative_to(ROOT)} "
            "(nonsymlink regular file required)"
        )
        return None
    try:
        return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc:
        errors.append(f"{path.relative_to(ROOT)}: unable to parse Python AST: {exc}")
        return None


def imported_from_figure_data(tree: ast.Module) -> set[str]:
    imported: set[str] = set()
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module == "figure_data" and node.level == 0:
            imported.update(alias.name for alias in node.names)
    return imported


def function_call_names(tree: ast.Module, function_name: str) -> list[str] | None:
    matches = [
        node for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == function_name
    ]
    if len(matches) != 1:
        return None
    names: list[str] = []
    for node in ast.walk(matches[0]):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            names.append(node.func.id)
    return names


def check_shared_data_contract(errors: list[str]) -> None:
    data_tree = parsed_module(FIGURE_DATA, errors)
    if data_tree is None:
        return
    data_definitions = {
        node.name
        for node in data_tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    expected_shared = set(SHARED_DATA_FUNCTIONS.values())
    missing_data_functions = sorted(expected_shared - data_definitions)
    if missing_data_functions:
        errors.append(
            "figures/figure_data.py: missing shared numerical-data function(s): "
            + ", ".join(missing_data_functions)
        )

    for renderer_path, functions in RENDERER_FUNCTIONS.items():
        tree = parsed_module(renderer_path, errors)
        if tree is None:
            continue
        imported = imported_from_figure_data(tree)
        missing_imports = sorted(expected_shared - imported)
        if missing_imports:
            errors.append(
                f"{renderer_path.relative_to(ROOT)}: missing shared figure_data import(s): "
                + ", ".join(missing_imports)
            )

        for figure_id, renderer_function in functions.items():
            required_call = SHARED_DATA_FUNCTIONS[figure_id]
            calls = function_call_names(tree, renderer_function)
            if calls is None:
                errors.append(
                    f"{renderer_path.relative_to(ROOT)}: expected exactly one top-level "
                    f"renderer function {renderer_function}"
                )
                continue
            count = calls.count(required_call)
            if count != 1:
                errors.append(
                    f"{renderer_path.relative_to(ROOT)}:{renderer_function}: shared numerical "
                    f"function {required_call} must be called exactly once; got {count}"
                )


def csv_rows(text: str) -> list[list[str]]:
    return list(csv.reader(io.StringIO(text)))


def numeric_equivalent(expected: str, actual: str) -> bool:
    if expected == actual:
        return True
    if expected == "" or actual == "":
        return False
    try:
        expected_value = float(expected)
        actual_value = float(actual)
    except ValueError:
        return False
    if math.isnan(expected_value) or math.isnan(actual_value):
        return math.isnan(expected_value) and math.isnan(actual_value)
    if not math.isfinite(expected_value) or not math.isfinite(actual_value):
        return expected_value == actual_value
    return math.isclose(
        expected_value,
        actual_value,
        rel_tol=NUMERIC_REL_TOL,
        abs_tol=NUMERIC_ABS_TOL,
    )


def validate_and_restore_fig2_data(errors: list[str]) -> None:
    """Validate generated Figure 2 data semantically, then restore canonical bytes."""
    if FIG2_DATA.is_symlink() or not FIG2_DATA.is_file():
        errors.append(
            f"{FIG2_DATA_RELATIVE}: missing/invalid theorem-illustration CSV"
        )
        return

    try:
        expected_rows = csv_rows(git_raw_text("show", f"HEAD:{FIG2_DATA_RELATIVE}"))
    except subprocess.CalledProcessError as exc:
        errors.append(f"{FIG2_DATA_RELATIVE}: unable to read committed CSV: {exc}")
        return
    actual_rows = csv_rows(FIG2_DATA.read_text(encoding="utf-8"))

    if len(actual_rows) != len(expected_rows):
        errors.append(
            f"{FIG2_DATA_RELATIVE}: row-count drift: generated {len(actual_rows)} "
            f"!= committed {len(expected_rows)}"
        )
        return

    cell_errors: list[str] = []
    for row_index, (expected_row, actual_row) in enumerate(
        zip(expected_rows, actual_rows), start=1
    ):
        if len(actual_row) != len(expected_row):
            cell_errors.append(
                f"row {row_index} column-count drift: generated {len(actual_row)} "
                f"!= committed {len(expected_row)}"
            )
            if len(cell_errors) >= MAX_REPORTED_CELL_ERRORS:
                break
            continue
        for column_index, (expected_cell, actual_cell) in enumerate(
            zip(expected_row, actual_row), start=1
        ):
            if numeric_equivalent(expected_cell, actual_cell):
                continue
            cell_errors.append(
                f"row {row_index}, column {column_index}: generated {actual_cell!r} "
                f"!= committed {expected_cell!r} beyond numeric tolerance"
            )
            if len(cell_errors) >= MAX_REPORTED_CELL_ERRORS:
                break
        if len(cell_errors) >= MAX_REPORTED_CELL_ERRORS:
            break

    if cell_errors:
        errors.append(
            f"{FIG2_DATA_RELATIVE}: generated theorem-illustration data exceeds the tight "
            f"numeric-equivalence contract (rtol={NUMERIC_REL_TOL:g}, "
            f"atol={NUMERIC_ABS_TOL:g}):\n" + "\n".join(cell_errors)
        )
        return

    subprocess.run(
        ["git", "checkout", "--", FIG2_DATA_RELATIVE],
        cwd=ROOT,
        check=True,
    )


def main() -> None:
    errors: list[str] = []
    check_source_blob_contract(errors)
    check_exact(SVG_DIR, EXPECTED_SVGS, "public SVG set", errors)
    check_exact(PDF_DIR, EXPECTED_PDFS, "manuscript PDF figure set", errors)
    check_shared_data_contract(errors)
    validate_and_restore_fig2_data(errors)

    if errors:
        raise SystemExit("Figure-set validation failed:\n" + "\n".join(errors))

    print(
        "Figure-set validation passed: audited figure-data/SVG/PDF source blobs match HEAD and "
        "working tree; exact nonsymlink regular-file "
        f"{len(EXPECTED_SVGS)}-SVG public set and {len(EXPECTED_PDFS)}-PDF manuscript set present; "
        "Figures 2-6 in both renderers each call the canonical shared numerical-data function "
        f"exactly once; Figure 2 theorem-illustration CSV matches committed HEAD within "
        f"rtol={NUMERIC_REL_TOL:g}, atol={NUMERIC_ABS_TOL:g} and canonical bytes were restored."
    )


if __name__ == "__main__":
    main()
