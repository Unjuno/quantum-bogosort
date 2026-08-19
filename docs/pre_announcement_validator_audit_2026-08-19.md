# Pre-announcement validator and Actions audit — 2026-08-19

## Purpose

This is a second-pass audit of the repository's **auditing machinery itself**. The earlier execution audit established a commit-fixed source/execution baseline and hardened E1–E5 reproduction. This pass asks a different question: can the validators or workflow still report success when an important repository, rendering, provenance, or publication invariant is actually broken?

The pass began from `main` after `fe0ecca8c8bbaa10d4bdc5bc226a2ddaa60d226b` and applies only validation, reproducibility, repository-structure, CI-supply-chain, and documentation corrections. It does not alter T1–T5, the S2 theorem/certificate line, the Everett bridge status, or locked historical experiment values.

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

- `theory/core_theorems.md`;
- `theory/core_theorems.tex`;
- `theory/propositions_boundaries.md`;
- `theory/theorem_1_3.md`;
- `theory/theorem_4_5.md`;
- root and split-license metadata;
- `.gitignore`, dependency/Python configuration, and the validation workflow;
- `experiments/archive/README.md` and `experiments/archive/INDEX.md`;
- all principal validator scripts.

Required paths must be regular files, not merely existing paths, and duplicate declarations in the validator itself are rejected.

### 4. Three Markdown validators disagreed with CommonMark fence semantics

The math, repository-link, and GitHub-GFM source-structure validators previously accepted arbitrary leading whitespace before a fence. CommonMark fenced code blocks permit at most three leading spaces. Treating a four-space-indented fence-like line as a real fence could hide later prose from validation.

All three validators now use the same boundary:

- zero to three leading spaces for fence openers/closers;
- matching marker character and sufficient closing-marker length;
- backtick-fence info strings containing backticks are not accepted as valid fence openers.

This reduces false PASS conditions where indented code-like text incorrectly suppresses later checks.

### 5. Repository-relative links could escape the repository root without failing

The link validator previously normalized a relative target and silently skipped it when the resolved path was outside the repository. A link such as an excessive `../` traversal was therefore neither validated nor rejected.

Relative Markdown targets that escape the repository root are now explicit validation errors.

### 6. LaTeX reference preflight could resolve a compiled reference from an uncompiled file

The previous LaTeX preflight collected labels from every `paper/*.tex` source. A `\ref{...}` reachable from `paper/main.tex` could therefore appear resolved if the matching label existed only in a TeX file not included by the manuscript input graph. Real LaTeX compilation would still produce an unresolved reference.

The validator now:

- builds the TeX graph reachable from `paper/main.tex`;
- resolves compiled labels and references only within that graph;
- continues to lint all manuscript sources for environments and citation keys;
- reports the number of paper TeX files intentionally outside the compiled graph;
- requires standalone `theory/core_theorems.tex` explicitly.

### 7. SVG “browser-safe” validation allowed active-content classes it did not inspect

The SVG validator already rejected malformed XML, selected active elements, external HTTP/data hrefs, and non-finite values. The remaining policy was still weaker than the repository's static-figure intent.

The validator now also rejects:

- DTD/entity declarations;
- animation elements (`animate`, `animateMotion`, `animateTransform`, `set`);
- event-handler attributes such as `onload`/`onclick`;
- all non-fragment `href` values, including `javascript:`;
- external/active CSS references in `<style>` blocks or style attributes;
- malformed numeric attributes that only begin with a number.

It also requires the explicit white background rectangle to cover the full SVG `viewBox`, not merely to exist at `(0,0)`.

### 8. GitHub Actions dependencies were mutable tags

The workflow previously referenced `actions/checkout@v4`, `actions/setup-python@v5`, and `actions/upload-artifact@v4`. Those major-version tags can move upstream.

The workflow now pins the exact commits resolved from those action repositories during this audit:

- `actions/checkout@11d5960a326750d5838078e36cf38b85af677262`;
- `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`;
- `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`.

This keeps the workflow implementation immutable until the repository deliberately updates those pins.

### 9. Complete validation could not be manually dispatched

The workflow now includes `workflow_dispatch` in addition to `push` and `pull_request`. Because `main` is the default branch, maintainers can repeat the complete validation from **Actions → validate → Run workflow** without creating a dummy commit.

### 10. E3 recognition-label null used a tautological arithmetic path

The E3 null previously assigned `V0` and `V1` from the same mean expression. The numerical conclusion was correct, but the check did not exercise the first-person value calculation.

The null now explicitly creates identical trajectory/accessibility arrays for the two inert labels and evaluates both through the same general first-person weighted-value function. `S_0=S_1=1`, so the committed null values and exact zero effect are preserved.

## Checks that remained valid

The second pass also rechecked several earlier decisions and did not find a correction requirement:

- GitHub's Markdown REST endpoint currently documents API version `2026-03-10`, matching the validator configuration;
- the pinned Python 3.11.15 / NumPy 2.4.6 / pandas 3.0.5 / Matplotlib 3.11.1 environment remains the explicit byte-reproduction contract;
- the four current Markdown issue templates contain the expected chooser front matter;
- the split Creative Commons files are intentionally concise licensing notices pointing to canonical legal codes rather than truncated copies presented as full legal text;
- no current `release/v0.*` development-branch routing remains in the repository search surface;
- `v0.3-public-review` still resolves to `58038763127258bd3e2f0d41708c4dfa01f81fd6`;
- `v0.2-public-review` still resolves to `7405f7408f74fa32b16d1cc9f624070cc14624ab`.

## Public CI visibility

The root README now exposes the `validate` workflow badge and links directly to the workflow page. The workflow can also be manually dispatched.

The connected GitHub interface used for this audit still does not expose direct-push workflow runs through its commit-run lookup, and its commit-status endpoint does not substitute for GitHub Actions check-run state. Therefore this audit does **not** convert the final Actions gate to PASS merely because source/configuration review is complete.

## Scientific/provenance boundary

This pass changes validator logic, E3 null test plumbing, workflow configuration, contribution/reproduction instructions, and repository QA documentation.

It does not change:

- T1–T5 theorem statements;
- S2-family theorem or certificate statements;
- the Everett accessibility bridge status;
- locked historical experiment CSV values;
- the numerical E3 recognition-null result;
- the numerical E1–E5 conclusions.

## Remaining release gates

Broad announcement remains gated on two things outside this source-level pass:

1. the final `main` `validate` workflow must complete successfully, including both `repository-validation` and `manuscript-build`;
2. representative GitHub pages must be inspected in the actual browser UI for MathJax, Mermaid, SVG sizing/readability, tables, navigation, and mobile layout.

A green badge or a completed manual workflow can establish the first gate; it does not replace the second visual gate.
