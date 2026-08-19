"""Validate the repository's explicit runtime/reproduction contract.

This checks the primary numerical package pins and their installed versions,
consistency between `.python-version` and GitHub Actions, immutable reusable-action
pins, checkout credential isolation, required validation/manuscript jobs and commands,
and a small read-only workflow security contract. It does not claim that every
transitive wheel is cryptographically locked.
"""
from __future__ import annotations

from pathlib import Path
import importlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PYTHON_VERSION_FILE = ROOT / ".python-version"
REQUIREMENTS = ROOT / "requirements.txt"
WORKFLOW = ROOT / ".github/workflows/validate.yml"

EXPECTED_PRIMARY_PACKAGES = {"numpy", "pandas", "matplotlib"}
REQUIRED_JOBS = {"repository-validation", "manuscript-build"}
REQUIRED_GLOBAL_WORKFLOW_SNIPPETS = [
    "  push:\n",
    "  pull_request:\n",
    "  workflow_dispatch:\n",
    "permissions:\n  contents: read\n",
    "cancel-in-progress: true",
]
FORBIDDEN_WORKFLOW_SNIPPETS = [
    "pull_request_target:",
    "contents: write",
    "actions: write",
    "checks: write",
    "pull-requests: write",
]
REQUIRED_REPOSITORY_COMMANDS = [
    "python -m py_compile experiments/*.py figures/*.py scripts/*.py",
    "python scripts/validate_runtime_contract.py",
    "python scripts/validate_markdown_math.py",
    "python scripts/validate_repository_structure.py",
    "python scripts/validate_issue_templates.py",
    "python scripts/validate_manifest.py",
    "python scripts/validate_markdown_links.py",
    "python scripts/validate_github_markdown_render.py",
    "python experiments/exp1_fosd_and_stress.py",
    "python experiments/exp2_minimal_agent.py",
    "python experiments/exp3_recognition_decomposition.py",
    "python experiments/exp4_interaction.py",
    "python experiments/exp5_branch_map.py",
    "python scripts/validate_reproduction_outputs.py",
    "python figures/generate_figures.py",
    "python figures/generate_pdf_figures.py",
    "python scripts/validate_svg_sources.py",
    "git diff --exit-code --",
    "data/processed/fig2_fosd_theorem_illustration.csv",
]
REQUIRED_MANUSCRIPT_COMMANDS = [
    "python scripts/validate_runtime_contract.py",
    "python figures/generate_pdf_figures.py",
    "python scripts/validate_latex_sources.py",
    "latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex",
    "test -s paper/main.pdf",
    "name: qbs-manuscript-pdf",
    "path: paper/main.pdf",
]
EXACT_REQUIREMENT_RE = re.compile(r"^([A-Za-z0-9_.-]+)==([^\s#;]+)$")
FULL_SHA_ACTION_RE = re.compile(r"^\s*- uses:\s+([^@\s]+)@([0-9a-f]{40})(?:\s+#.*)?$")
PYTHON_WORKFLOW_RE = re.compile(r"^\s+python-version:\s*['\"]?([^'\"\s]+)['\"]?\s*$")
RUNNER_RE = re.compile(r"^\s+runs-on:\s*([^\s#]+)")
JOB_HEADER_RE = re.compile(r"^  ([A-Za-z0-9_-]+):\s*$", re.MULTILINE)
TIMEOUT_RE = re.compile(r"^\s{4}timeout-minutes:\s*(\d+)\s*$", re.MULTILINE)


def split_jobs(workflow_text: str) -> dict[str, str]:
    """Return top-level `jobs:` entries without adding a YAML dependency."""
    jobs_pos = workflow_text.find("\njobs:\n")
    if jobs_pos < 0:
        return {}
    jobs_text = workflow_text[jobs_pos + len("\njobs:\n") :]
    matches = list(JOB_HEADER_RE.finditer(jobs_text))
    jobs: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(jobs_text)
        jobs[match.group(1)] = jobs_text[start:end]
    return jobs


def require_snippets(scope: str, text: str, snippets: list[str], errors: list[str]) -> None:
    for snippet in snippets:
        if snippet not in text:
            errors.append(f"{scope}: missing required workflow contract snippet: {snippet!r}")


def main() -> None:
    errors: list[str] = []

    expected_python = PYTHON_VERSION_FILE.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", expected_python):
        errors.append(f".python-version must be an exact X.Y.Z version, got {expected_python!r}")

    actual_python = ".".join(map(str, sys.version_info[:3]))
    if actual_python != expected_python:
        errors.append(
            f"running Python {actual_python} does not match .python-version {expected_python}"
        )

    requirement_versions: dict[str, str] = {}
    for line_no, raw in enumerate(REQUIREMENTS.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = EXACT_REQUIREMENT_RE.fullmatch(line)
        if not match:
            errors.append(
                f"requirements.txt:{line_no}: primary runtime contract requires exact == pins; got {line!r}"
            )
            continue
        name, version = match.groups()
        normalized = name.lower().replace("_", "-")
        if normalized in requirement_versions:
            errors.append(f"requirements.txt:{line_no}: duplicate requirement {normalized}")
        requirement_versions[normalized] = version

    if set(requirement_versions) != EXPECTED_PRIMARY_PACKAGES:
        errors.append(
            "requirements.txt primary package set must be exactly "
            f"{sorted(EXPECTED_PRIMARY_PACKAGES)!r}; got {sorted(requirement_versions)!r}"
        )

    for package, expected_version in sorted(requirement_versions.items()):
        module = importlib.import_module(package)
        actual_version = getattr(module, "__version__", None)
        if actual_version != expected_version:
            errors.append(
                f"installed {package} version {actual_version!r} != pinned {expected_version!r}"
            )

    workflow_text = WORKFLOW.read_text(encoding="utf-8")
    require_snippets("workflow", workflow_text, REQUIRED_GLOBAL_WORKFLOW_SNIPPETS, errors)
    for snippet in FORBIDDEN_WORKFLOW_SNIPPETS:
        if snippet in workflow_text:
            errors.append(f"workflow contains forbidden elevated/unsafe construct: {snippet!r}")

    workflow_python_versions = PYTHON_WORKFLOW_RE.findall(workflow_text)
    if len(workflow_python_versions) < len(REQUIRED_JOBS):
        errors.append(
            f"workflow must declare python-version for both required jobs; got {workflow_python_versions!r}"
        )
    elif any(version != expected_python for version in workflow_python_versions):
        errors.append(
            "workflow python-version declarations must all match .python-version; got "
            + ", ".join(workflow_python_versions)
        )

    runners = RUNNER_RE.findall(workflow_text)
    if len(runners) < len(REQUIRED_JOBS) or any(runner != "ubuntu-24.04" for runner in runners):
        errors.append(
            "all required validation jobs must use the explicit ubuntu-24.04 runner; got "
            + (", ".join(runners) if runners else "<none>")
        )

    action_lines = [line for line in workflow_text.splitlines() if re.match(r"^\s*- uses:", line)]
    if not action_lines:
        errors.append("validation workflow contains no reusable action steps")
    for line in action_lines:
        if not FULL_SHA_ACTION_RE.fullmatch(line):
            errors.append(f"workflow reusable action is not pinned to a full commit SHA: {line.strip()}")

    jobs = split_jobs(workflow_text)
    missing_jobs = sorted(REQUIRED_JOBS - set(jobs))
    if missing_jobs:
        errors.append("workflow missing required job(s): " + ", ".join(missing_jobs))

    for job_name in sorted(REQUIRED_JOBS & set(jobs)):
        job_text = jobs[job_name]
        timeout_match = TIMEOUT_RE.search(job_text)
        if not timeout_match:
            errors.append(f"{job_name}: missing timeout-minutes")
        elif int(timeout_match.group(1)) > 30:
            errors.append(f"{job_name}: timeout-minutes exceeds 30")
        if "pip install -r requirements.txt" not in job_text:
            errors.append(f"{job_name}: missing pinned requirements installation")
        if job_text.count("persist-credentials: false") != 1:
            errors.append(
                f"{job_name}: checkout must set persist-credentials: false exactly once"
            )

    repository_job = jobs.get("repository-validation", "")
    manuscript_job = jobs.get("manuscript-build", "")
    require_snippets("repository-validation", repository_job, REQUIRED_REPOSITORY_COMMANDS, errors)
    require_snippets("manuscript-build", manuscript_job, REQUIRED_MANUSCRIPT_COMMANDS, errors)

    if "GITHUB_TOKEN: ${{ github.token }}" not in repository_job:
        errors.append("repository-validation: GFM renderer must receive the scoped github.token")

    if repository_job.count("actions/checkout@") != 1 or repository_job.count("actions/setup-python@") != 1:
        errors.append("repository-validation must contain exactly one checkout and one setup-python action")
    if manuscript_job.count("actions/checkout@") != 1 or manuscript_job.count("actions/setup-python@") != 1:
        errors.append("manuscript-build must contain exactly one checkout and one setup-python action")
    if manuscript_job.count("actions/upload-artifact@") != 1:
        errors.append("manuscript-build must contain exactly one upload-artifact action")

    if errors:
        raise SystemExit("Runtime contract validation failed:\n" + "\n".join(errors))

    package_summary = ", ".join(
        f"{name}=={version}" for name, version in sorted(requirement_versions.items())
    )
    print(
        "Runtime contract validation passed: "
        f"Python {expected_python}; {package_summary}; ubuntu-24.04; required jobs/commands present; "
        "read-only workflow security contract; "
        f"{len(action_lines)} reusable action steps full-SHA pinned."
    )


if __name__ == "__main__":
    main()
