# Pre-announcement validator and Actions audit — 2026-08-19

## Purpose

This is a second-pass audit of the repository's **auditing machinery itself**. The earlier execution audit established a commit-fixed source/execution baseline and hardened E1–E5 reproduction. This pass asks a different question: can the validators or workflow still report success when an important repository, rendering, provenance, or publication invariant is actually broken?

The pass began from `main` after `fe0ecca8c8bbaa10d4bdc5bc226a2ddaa60d226b` and applies only validation, reproducibility, repository-structure, CI-supply-chain, public-routing, and documentation corrections. It does not alter T1–T5, the S2 theorem/certificate line, the Everett bridge status, or locked historical experiment values.

## Findings corrected

### 1. Processed-data cleanliness was too narrow

The reproduction validator previously compared only manifest-declared current CSV outputs. An experiment script could therefore alter a locked historical CSV or create an undeclared output while the declared current files still matched.

The validator now requires all of the following immediately after E1–E5 execution and before figure generation:

- the manifest-declared current E1–E5 CSV set exactly matches the tracked `e1_...` through `e5_...` CSV set;
- every declared current output is byte-identical to `HEAD`;
- the complete tracked `data/processed/` tree is unchanged, so locked historical data cannot be silently rewritten;
- the actual filesystem under `data/processed/` contains no extra files, including files hidden by `.gitignore`.

This turns the experiment step into a side-effect-bounded reproduction test rather than a check of only selected filenames.

### 2. GitHub issue-template front matter had no CI validator

The four Markdown issue templates use GitHub chooser front matter, but the workflow did not validate it. A malformed or missing `name`/`about` field could remove an intake route from the chooser without breaking Markdown rendering.

`scripts/validate_issue_templates.py` now checks every Markdown issue template for:

- opening and closing YAML front-matter delimiters;
- required `name` and `about` values;
- supported top-level chooser fields;
- duplicate keys and duplicate template names;
- a nonempty issue body.

### 3. Repository-structure validation omitted core theory and archival provenance

The structure validator did not explicitly require the five `theory/` sources, including standalone `theory/core_theorems.tex`. It also did not require the split-license notices or the archived experiment provenance pages.

The required map now includes:

- all five core `theory/` sources;
- root and split-license metadata;
- `.gitignore`, dependency/Python configuration, and the validation workflow;
- `experiments/archive/README.md` and `experiments/archive/INDEX.md`;
- the pre-announcement audit records;
- all principal validator scripts, including the runtime-contract and worktree-artifact validators.

Required paths must be regular files, not merely existing paths, and duplicate declarations in the validator itself are rejected.

### 4. Three Markdown validators disagreed with CommonMark fence semantics

The math, repository-link, and GitHub-GFM source-structure validators previously accepted arbitrary leading whitespace before a fence. CommonMark fenced code blocks permit at most three leading spaces. Treating a four-space-indented fence-like line as a real fence could hide later prose from validation.

All three validators now use the same boundary:

- zero to three leading spaces for fence openers/closers;
- matching marker character and sufficient closing-marker length;
- backtick-fence info strings containing backticks are not accepted as valid fence openers.

### 5. Markdown link validation had multiple false-PASS paths

The link validator previously normalized a relative target and silently skipped it when the resolved path was outside the repository. It also validated the inner image in a linked-image form such as `[![...](image.svg)](page.md)` without validating the outer page target, and it did not cover reference-style definition targets.

It now:

- rejects relative targets that escape the repository root;
- validates ordinary inline links/images;
- validates linked-image outer destinations;
- validates reference-style definition targets;
- excludes GitHub footnote definitions (`[^id]: ...`), whose body is prose rather than a link target.

No current fragment/heading-anchor links were found, so fragment-slug validation is not presently a repository defect.

### 6. LaTeX reference preflight could resolve a compiled reference from an uncompiled file

The previous LaTeX preflight collected labels from every `paper/*.tex` source. A `\ref{...}` reachable from `paper/main.tex` could therefore appear resolved if the matching label existed only in a TeX file not included by the manuscript input graph.

The validator now:

- builds the TeX graph reachable from `paper/main.tex`;
- resolves compiled labels and references only within that graph;
- continues to lint all manuscript sources for environments and citation keys;
- requires standalone `theory/core_theorems.tex` explicitly.

The audit also identified exactly one intentionally retained TeX source outside the compiled graph: `paper/sections/robust_mom_summary.tex`. That single-file set is now an explicit allowlist. If any other paper TeX file becomes unreachable from `main.tex`, CI fails instead of merely reporting a larger informational count. `paper/README.md` records that the compiled robust-MoM treatment is `robust_mom_certificate_appendix.tex`.

### 7. SVG “browser-safe” validation allowed active-content classes it did not inspect

The static SVG validator now rejects:

- DTD/entity declarations;
- scripts, `foreignObject`, and animation elements;
- event-handler attributes such as `onload`/`onclick`;
- all non-fragment `href` values, including `javascript:`;
- external/active CSS references in `<style>` blocks or style attributes;
- malformed or non-finite numeric attributes.

It also requires the explicit white background rectangle to cover the full SVG `viewBox`, not merely to exist at `(0,0)`.

### 8. GitHub Actions dependencies were mutable tags

The workflow originally referenced reusable Actions by mutable major-version tags. During this audit it was first moved to immutable full-commit SHA pins. A later same-day Actions-runtime refresh advanced those immutable pins to the current Node-24/v7 releases while preserving the same supply-chain rule.

The current audited pins are:

- `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1` (`v7.0.1`);
- `actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97` (`v7.0.0`);
- `actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a` (`v7.0.1`).

`scripts/validate_runtime_contract.py` treats those full SHAs and their expected multiplicities as the current workflow contract, so action-pin drift fails CI rather than silently changing the execution environment.

### 9. Complete validation could not be manually dispatched

The workflow now includes `workflow_dispatch` in addition to `push` and `pull_request`. Because `main` is the default branch, maintainers can repeat the complete validation from **Actions → validate → Run workflow** without creating a dummy commit.

### 10. E3 recognition-label null used a tautological arithmetic path

The E3 null previously assigned `V0` and `V1` from the same mean expression. The numerical conclusion was correct, but the check did not exercise the first-person value calculation.

The null now explicitly creates identical trajectory/accessibility arrays for the two inert labels and evaluates both through the same general first-person weighted-value function. `S_0=S_1=1`, so the committed null values and exact zero effect are preserved.

### 11. Runtime contract was duplicated but not cross-validated

`.python-version`, `requirements.txt`, and the workflow each encoded part of the reproduction environment, but CI did not verify that they agreed.

`scripts/validate_runtime_contract.py` now checks:

- exact `X.Y.Z` Python pinning and equality with the running interpreter;
- exact `==` pins for the three primary numerical/plotting packages used by the repository (`numpy`, `pandas`, `matplotlib`);
- equality between installed primary-package versions and `requirements.txt`;
- equality between every workflow `python-version` and `.python-version`;
- `ubuntu-24.04` for both validation jobs;
- presence of `workflow_dispatch`;
- full 40-hex commit-SHA pinning for every reusable `uses:` step;
- the exact currently audited action SHAs and expected action multiplicities;
- presence of the final ignored-artifact validation command.

This is intentionally a **primary-package/runtime contract**, not a claim that every transitive wheel is cryptographically locked. Byte-level output identity is still the final executable check.

The audit independently confirmed that Python 3.11.15 is a stable release and that the `actions/python-versions` manifest contains a Linux 24.04 x64 build for 3.11.15. The exact NumPy, pandas, and Matplotlib pins also publish Python-3.11/Linux-compatible distributions.

### 12. Public current-review issue used stale rendering syntax

The root README links open Issue #14 as the current v0.3 S2 technical-review surface. Its issue body still used `$$` display math and `\operatorname{Cov}` even though repository Markdown had been standardized on fenced `math` and repository roman operator forms.

The open issue body was synchronized to fenced `math` and `\mathrm{Cov}` without changing the theorem statements, review questions, snapshot routing, or historical comments.

### 13. Root CI visibility was weak

The root README now exposes the `main` `validate` workflow badge and links directly to the workflow page. The validation section and contributor instructions are synchronized with the current CI checks and manual-dispatch path.

### 14. Ignored untracked files could evade the final clean-worktree check

The workflow already rejected tracked diffs and nonignored untracked files. However, `git ls-files --others --exclude-standard` deliberately omits paths matched by `.gitignore`. A validator or experiment could therefore create an unexpected file such as `stray.log` or `stray.out` and still leave the final CI clean check green.

`scripts/validate_worktree_artifacts.py` now inspects:

```text
git ls-files --others --ignored --exclude-standard
```

and permits only the ignored outputs the repository-validation job intentionally creates:

- Python bytecode files under `experiments/__pycache__/`, `figures/__pycache__/`, or `scripts/__pycache__/`;
- the exact six manuscript figure PDFs already declared by `scripts/validate_figure_set.py`.

All six PDF outputs are also required to be present. Any other ignored/untracked path fails validation. The workflow runs this validator after figure generation and the tracked/nonignored clean checks, and the runtime contract requires that invocation.

The Git enumeration semantics and the validator's failure behavior were negative-tested independently: the expected bytecode/PDF set passes, adding a `stray.log` fails, and removing one expected manuscript PDF fails.

## Checks that remained valid

The second pass also rechecked several earlier decisions and did not find a correction requirement:

- GitHub's Markdown REST endpoint currently documents API version `2026-03-10`, matching the validator configuration;
- the pinned Python 3.11.15 / NumPy 2.4.6 / pandas 3.0.5 / Matplotlib 3.11.1 primary runtime contract remains internally coherent;
- the four current Markdown issue templates contain the expected chooser front matter;
- the split Creative Commons files are intentionally concise licensing notices pointing to canonical legal codes rather than truncated copies presented as full legal text;
- `CITATION.cff` contains the required root CFF 1.2.0 fields and intentionally tracks the frozen v0.3 public-review snapshot;
- no current `release/v0.*` development-branch routing remains in the repository search surface;
- the only open issue is the current S2 review issue #14, whose main body is now synchronized;
- `v0.3-public-review` still resolves to `58038763127258bd3e2f0d41708c4dfa01f81fd6`;
- `v0.2-public-review` still resolves to `7405f7408f74fa32b16d1cc9f624070cc14624ab`.

## Repository-header metadata observation

The GitHub repository header currently has no topics and its description still says **“recognition-activated Quantum Bogosort”**. That wording is less precise than the repository's current recognition-dependent information-state formulation and could be read as implying a special activation mechanism.

The GitHub connector available during this audit exposes repository metadata reads but no repository-description/topics update action, so this header-level item could not be corrected from the audit runtime. It is a presentation/metadata item, not a source or scientific defect. A preferable description would be along the lines of:

> Formal theory and reproducible simulations of recognition-dependent policies, observer-indexed accessibility, first-person conditioning, and cross-copy coherence.

Reasonable repository topics would include `decision-theory`, `quantum-foundations`, `self-locating-uncertainty`, `observer-selection`, and `reproducible-research`.

## Public CI visibility

The root README exposes the `validate` workflow badge and links directly to the workflow page. The workflow can also be manually dispatched.

The connected GitHub interface used for this audit still does not expose direct-push workflow runs through its commit-run lookup, and its commit-status endpoint does not substitute for GitHub Actions check-run state. Public workflow/badge fetches from this audit environment also remain cache-miss limited. Therefore this audit does **not** convert the final Actions gate to PASS merely because source/configuration review is complete.

Release-tag commits were re-resolved successfully, but the rendered GitHub Release descriptions themselves were not retrievable through the available connector/web paths. No claim is made here that Release-body presentation was visually audited.

## Scientific/provenance boundary

This pass changes validator logic, E3 null test plumbing, workflow configuration, current-review issue rendering syntax, contribution/reproduction instructions, and repository QA documentation.

It does not change:

- T1–T5 theorem statements;
- S2-family theorem or certificate statements;
- the Everett accessibility bridge status;
- locked historical experiment CSV values;
- the numerical E3 recognition-null result;
- the numerical E1–E5 conclusions;
- the seven committed SVG figure files.

## Remaining release gates

Broad announcement remains gated on:

1. the final `main` `validate` workflow completing successfully, including both `repository-validation` and `manuscript-build`;
2. representative GitHub pages being inspected in the actual browser UI for MathJax, Mermaid, SVG sizing/readability, tables, navigation, and mobile layout;
3. optionally normalizing the repository-header description/topics before broad promotion.

A green badge or a completed manual workflow can establish the first gate; it does not replace the second visual gate.
