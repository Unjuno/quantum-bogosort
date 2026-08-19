# QBS Current Research Status

**Updated:** 2026-08-19

This file is the concise source of truth for the current review/development state. Frozen snapshot identity is recorded in [`STATUS.md`](STATUS.md); detailed audit history is recorded in the four pre-announcement audit files; future release work is tracked in [`ROADMAP.md`](ROADMAP.md).

## Public source of truth

- current development/review branch: `main`;
- frozen v0.3 public-review snapshot: tag/Release `v0.3-public-review` at commit `58038763127258bd3e2f0d41708c4dfa01f81fd6`;
- archived v0.2 snapshot: tag/Release `v0.2-public-review` at commit `7405f7408f74fa32b16d1cc9f624070cc14624ab`;
- canonical claim/theorem/evidence map: [`docs/research_map.md`](docs/research_map.md);
- authoritative claim boundaries: [`docs/claims_and_assumptions.md`](docs/claims_and_assumptions.md);
- execution/reproduction audit: [`docs/pre_announcement_execution_audit_2026-08-19.md`](docs/pre_announcement_execution_audit_2026-08-19.md);
- validator/Actions/governance audit: [`docs/pre_announcement_validator_audit_2026-08-19.md`](docs/pre_announcement_validator_audit_2026-08-19.md);
- bibliography/prior-art truth audit: [`docs/pre_announcement_bibliography_audit_2026-08-19.md`](docs/pre_announcement_bibliography_audit_2026-08-19.md);
- mathematical-domain audit: [`docs/pre_announcement_mathematical_domain_audit_2026-08-19.md`](docs/pre_announcement_mathematical_domain_audit_2026-08-19.md).

The frozen tags are treated as commit-pinned historical snapshots. They are not described as platform-immutable unless a GitHub tag ruleset is actually configured and verified.

## Scientific state

The core theorem family remains **T1–T5** and the core experiment family remains **E1–E5**. The supplementary numbered line remains complete through **S2.13**.

Recognition is an information/policy-selection state. It has no privileged physical causal power merely by being recognized. A recognition-dependent policy can causally change trajectories and can change the modeled accessibility map. The base probability law itself is not changed by QBS weighting.

The first-person measure is a normalized change of measure. Future accessibility can reweight present self-location, but favorable/upward reweighting requires alignment with the favorability/utility statistic. The Everett accessibility bridge remains a separate unresolved physical assumption.

### Current-main T1–T5 domain corrections

The frozen v0.3 snapshot is untouched. Current `main` preserves T1–T5 identity, numbering, algebraic proof structure, sign/FOSD conclusions, support/extinction boundaries, and Everett-bridge statement while making the required domains explicit.

The compact canonical `theory/core_theorems.tex` differs from frozen v0.3 in exactly four audited textual locations:

1. a version-neutral document title;
2. explicit base integrability `E_mu[|U_pi|] < infinity` in the policy setup;
3. the complete generic T1 domain `S >= 0`, `0 < E[S] < infinity`, `E[|X|] < infinity`, and `E[|X|S] < infinity`;
4. T5 cross-integrability `E[|U_1|S_0] < infinity`, required because the proof introduces `Q(U_1,S_0)`.

`scripts/validate_core_theorem_lock.py` normalizes exactly those four changes and then requires byte identity with the frozen v0.3 canonical TeX blob `82986d7197e79446d6574aab538d1edaeff47eb6`. It also requires the same T1/T4/T5 domain assumptions across nine theory, experiment-card, and manuscript surfaces. Those nine audited surfaces are now themselves HEAD/worktree Git-blob locked, so a later edit cannot satisfy the domain check only through a comment or literal-code decoy without an explicit scientific-review contract update.

### Supplementary-domain corrections

The deeper mathematical audit also corrected several boundary/domain defects without changing the intended on-domain conclusions:

- **S2.8:** the generic confidence certificate now uses `U_M^+ = max(0,U_M)` so the reported random statistic remains real-valued even outside the simultaneous confidence event; on the event, `U_M^+ = U_M`, so the bound and coverage are unchanged;
- **S2.9:** sub-Gaussian/Bernstein concentration parameters are explicitly nonnegative, making all radii real/nonnegative by definition;
- **S2.10:** the zero-variance case `v_j=0` is handled separately: the target is almost surely constant, so the MoM error is exactly zero; Chebyshev is used only for `v_j>0`;
- **recognition time:** `C_t` is correctly typed as an adapted real random variable, continuous-time hitting is conditioned on standard path/measurability hypotheses, and FP stopping-rule values require the full T1 base/weighted integrability domain;
- **repeated filtering:** the sensitivity derivative explicitly requires the weighted moments and dominated-differentiation regularity needed to interchange differentiation and expectation;
- **binary soft-QBS:** `p`, `lambda`, `q`, and `alpha` domains are explicit and the zero-normalization corner `(p,lambda)=(0,0)` is excluded;
- **Gaussian toy:** `rho`, `lambda`, `q`, and `alpha` domains are explicit and positive normalization/denominator is guaranteed.

`scripts/validate_supplementary_consistency.py` locks these corrections across the relevant supplementary, manuscript, and theorem-audit surfaces. The fourteen audited consistency surfaces are now also HEAD/worktree Git-blob locked before semantic snippet checks, closing the same comment/literal-code false-PASS class for the supplementary boundary line.

The main S1, S2/S2.3/S2.4, S2.5–S2.7, and S2.11–S2.13 arguments were rechecked for the same class of domain/sign/coverage failure and no additional correction was identified in that pass.

## Reproducibility state

The primary byte-reproduction environment is fixed to:

- Ubuntu 24.04;
- Python 3.11.15;
- NumPy 2.4.6;
- pandas 3.0.5;
- Matplotlib 3.11.1.

The first execution audit locally reconstructed the commit-fixed executable subset because normal network cloning was unavailable in the audit runtime. Under that reconstruction:

- E1–E5 executed successfully;
- all twelve current reproduction CSVs matched their committed identities, except for the intentional E5 current-schema correction already committed to `main`;
- all seven committed SVGs regenerated byte-for-byte;
- manifest and reproduction negative tests rejected deliberate corruption.

The current E5 rho-sweep field is `action_corr_increment`; its numerical series and Figure 6 are unchanged. Locked historical schemas were not rewritten.

The continued validator audit now also enforces several repository-surface invariants that were previously only implicit:

- experiment-card CSV and `Linked theory` routing is parsed from the fence-filtered rendered Markdown surface rather than raw source, closing a fenced-code decoy route;
- experiment cards use an ATX-only H1/H2 schema, including rejection of multiline/raw-HTML H1/H2 tag forms, so visible non-ATX headings cannot sit outside the card parser;
- raw HTML `<a>`/`<img>` routes are rejected by the repository-link contract rather than bypassing Markdown link validation;
- tracked symlinks are rejected repository-wide, and required files, current reproduction CSVs, and generated figure outputs must be nonsymlink regular files;
- public SVG and manuscript PDF Figures 2–6 obtain their numerical series from shared `figures/figure_data.py`;
- the Fig2–6 refactor was independently recalculated against the current CSVs and preserves the pre-refactor x arrays, labels, ordering, values, and relevant NumPy/pandas scalar/array types;
- the figure-data module and both SVG/PDF renderer sources are fixed to audited Git blobs in addition to the AST shared-function checks, so a dead-code `shared_call()` cannot by itself satisfy the figure contract after an accidental renderer drift;
- the complete validation workflow is fixed to its audited Git blob before its human-readable runtime/order/security checks, closing the possibility that a required command survives only as a YAML/shell comment;
- issue-template front matter is restricted to the repository's supported one-line YAML scalar subset, rejecting malformed quoted scalars that the previous nonempty-string parser could accept;
- `CITATION.cff` and `STATUS.md` are fixed to their audited snapshot-metadata blobs before the narrow CFF/ledger checks, so malformed YAML/source drift cannot be hidden by successful string extraction.

Current CI additionally locks all sixteen historical E1–E5 CSVs to their frozen v0.3 Git blob identities, validates manifest/card/theorem routing, rejects experiment side effects outside the declared current outputs, and rejects undeclared ignored/nonignored worktree artifacts.

## Bibliography and prior-art state

The bibliography audit separates syntactic BibTeX validity from factual publication chronology. Where the same work has a clearly verified definitive journal/book publication, the current bibliography uses that publication rather than a later arXiv upload that could make prior art appear artificially recent. Earlier preprints remain when they are themselves the relevant historical record or when no definitive same-work publication was established.

[`paper/bibliography_fact_lock.md`](paper/bibliography_fact_lock.md) records, for all current bibliography entries:

- citation key;
- record type;
- year;
- author;
- title;
- publication locator;
- DOI or arXiv identifier;
- provenance class.

For journal records the locator fixes journal, volume/number, and pages/article number; for book chapters it fixes book title, editors, publisher, and pages. `scripts/validate_bibliography_metadata.py` requires exact agreement with that reviewed lock. This is a regression guard against later corruption of already-reviewed bibliography facts, not an automated proof of external bibliographic truth.

The three working prior-art ledgers are aligned with the current recognition boundary: recognition/information state can alter policy selection, but recognition is not described as a privileged physical causal variable.

## GitHub Actions validation contract

The workflow runs on push, pull request, and manual dispatch. Both jobs use Ubuntu 24.04 and Python 3.11.15. Reusable Actions are pinned to audited full commit SHAs, checkout credentials are not persisted, and workflow permissions remain read-only. `scripts/validate_runtime_contract.py` additionally fixes the complete audited workflow source to its current Git blob, so command-presence/order checks cannot be satisfied by commented/dead copies unless the workflow contract is explicitly reviewed and updated.

`repository-validation` currently checks, in enforced relative order where order matters:

- runtime/workflow contract;
- Python compilation;
- Markdown math and repository structure;
- frozen T1–T5 canonical theorem/body/domain lock plus audited cross-surface blob identities;
- supplementary theorem/domain consistency plus audited cross-surface blob identities;
- citation/snapshot metadata blobs and bibliography fact-lock metadata;
- split licensing, repository-wide nonsymlink classification, and live frozen snapshot refs;
- issue templates, rendered-surface experiment cards, and manifest/provenance/theory routing;
- repository-relative links and GitHub GFM structural rendering;
- E1–E5 scientific invariants and byte-identical current reproduction outputs;
- frozen historical data identities;
- deterministic figure regeneration, shared SVG/PDF numerical-data contract, audited figure-source blobs, exact nonsymlink figure sets, and SVG safety;
- final tracked and untracked/ignored worktree cleanliness.

`manuscript-build` independently validates the runtime contract, generates PDF figures, preflights the reachable LaTeX/citation/reference graph, installs the TeX toolchain, compiles `paper/main.pdf`, verifies it, and uploads the PDF artifact.

## What is still unverified

**The latest final `main` GitHub Actions result is not yet recorded as PASS.** The connected GitHub interface available in this audit does not expose direct-push Actions check-run state, and the combined commit-status endpoint returning no statuses is not evidence of success. Because this audit is still committing fixes, prior runs may also be cancelled by workflow concurrency; only the final settled commit matters.

The shared figure-data refactor has been checked at the numerical-object level in this audit, but the final pinned-environment Actions regeneration remains the authoritative post-refactor byte check for all seven committed SVGs and the deterministic Figure 2 CSV.

Source-level GFM/SVG/math validators also do not replace direct browser inspection. The actual GitHub UI still needs representative desktop/mobile review for:

- MathJax;
- Mermaid;
- SVG sizing/readability;
- tables and navigation;
- overall mobile/desktop layout.

Accordingly, the repository is **not yet certified ready for broad announcement**.

## Governance / presentation items

The current public-source-of-truth branch should receive an appropriate branch/ruleset policy after CI stabilizes. A tag ruleset is optional if platform-level deletion/update protection is desired for frozen review tags.

Repository-header description/topics are presentation metadata and remain separate from the scientific/source audit. They may be normalized before broad promotion, but are not a substitute for the Actions and browser gates.

## Release gates

Before broad announcement:

1. stop source-changing audit commits long enough for the final `main` `validate` workflow to finish;
2. confirm both `repository-validation` and `manuscript-build` are green for that exact final commit;
3. inspect representative GitHub pages directly in the real browser UI on desktop and mobile;
4. configure the desired `main` branch/ruleset policy after CI is stable;
5. optionally normalize repository-header description/topics and add a tag ruleset;
6. continue external proof/prior-art/Everett-bridge review as scientific review, not as a substitute for repository QA.

No S2.14 or sixth core experiment is added by default. New mathematical machinery should respond to a concrete modeling gap or review finding.
