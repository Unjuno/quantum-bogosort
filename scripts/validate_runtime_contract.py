"""Validate the repository's explicit runtime/reproduction contract.

This checks the primary numerical package pins and their installed versions, plus
consistency between `.python-version` and the GitHub Actions workflow. It does not
claim that every transitive wheel is cryptographically locked.
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
EXACT_REQUIREMENT_RE = re.compile(r"^([A-Za-z0-9_.-]+)==([^\s#;]+)$")
FULL_SHA_ACTION_RE = re.compile(r"^\s*- uses:\s+([^@\s]+)@([0-9a-f]{40})(?:\s+#.*)?$")
PYTHON_WORKFLOW_RE = re.compile(r"^\s+python-version:\s*['\"]?([^'\"\s]+)['\"]?\s*$")
RUNNER_RE = re.compile(r"^\s+runs-on:\s*([^\s#]+)")


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
    workflow_python_versions = PYTHON_WORKFLOW_RE.findall(workflow_text)
    if not workflow_python_versions:
        errors.append("workflow contains no python-version declaration")
    elif any(version != expected_python for version in workflow_python_versions):
        errors.append(
            "workflow python-version declarations must all match .python-version; got "
            + ", ".join(workflow_python_versions)
        )

    runners = RUNNER_RE.findall(workflow_text)
    if not runners or any(runner != "ubuntu-24.04" for runner in runners):
        errors.append(
            "all validation jobs must use the explicit ubuntu-24.04 runner; got "
            + (", ".join(runners) if runners else "<none>")
        )

    if "workflow_dispatch:" not in workflow_text:
        errors.append("workflow_dispatch trigger is missing from validation workflow")

    action_lines = [line for line in workflow_text.splitlines() if re.match(r"^\s*- uses:", line)]
    if not action_lines:
        errors.append("validation workflow contains no reusable action steps")
    for line in action_lines:
        if not FULL_SHA_ACTION_RE.fullmatch(line):
            errors.append(f"workflow reusable action is not pinned to a full commit SHA: {line.strip()}")

    if errors:
        raise SystemExit("Runtime contract validation failed:\n" + "\n".join(errors))

    package_summary = ", ".join(
        f"{name}=={version}" for name, version in sorted(requirement_versions.items())
    )
    print(
        "Runtime contract validation passed: "
        f"Python {expected_python}; {package_summary}; ubuntu-24.04 workflow; "
        f"{len(action_lines)} reusable action steps full-SHA pinned."
    )


if __name__ == "__main__":
    main()
