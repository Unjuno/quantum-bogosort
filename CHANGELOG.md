# Changelog

## Unreleased — `main`

### Changed

- clarified that recognition may include recognition of a QBS-type rule itself, while recognition has no privileged causal power beyond the policy and trajectory/accessibility changes it induces;
- added a concise landing-page statement of the self-referential QBS question and clarified that the name labels the observer-selection intuition rather than a literal utility-sorting operation by quantum mechanics;
- exposed present self-location under future accessibility in the root README, canonical claim ledger, research map, notation reference, and manuscript formal model;
- clarified that future accessibility can reweight present self-location without by itself guaranteeing a favorable direction; favorable/upward reweighting additionally requires alignment with the relevant favorability or utility statistic;
- aligned manuscript recognition wording with an information-state / policy-selection interpretation and replaced a residual generic `recognition-activated policy` phrase with `recognition-dependent policy`; evidence-threshold activation remains a distinct explicit supplementary model where intended;
- added a Mermaid dependency diagram to the root README and an experiment/theorem Mermaid map to `experiments/README.md`;
- added a static Figure 1 SVG fallback below the root Mermaid dependency diagram so the core visual remains available when Mermaid is not rendered;
- embedded the committed SVG theorem/simulation figures directly into the root README, experiment index, and figure-provenance page so results are visually inspectable without opening raw CSV files;
- added a dedicated E2 predictive-alignment review figure so every locked experiment family E1–E5 has a direct visual route from the repository landing page;
- made figure-level provenance explicit so deterministic theorem illustrations, current reproduction outputs, and locked historical summaries are not conflated; Figure 5 and Figure 7 are labeled as locked-summary visualizations;
- synchronized committed SVGs with the deterministic generator and added CI byte-for-byte verification after regeneration;
- added explicit white backgrounds to repository SVGs for GitHub dark-mode readability and separated overlapping Figure 5 series with distinct monochrome line styles;
- moved root README display mathematics to GitHub fenced `math` blocks after direct rendered-UI QA exposed broken double-dollar rendering;
- standardized display mathematics across public repository Markdown on GitHub fenced `math` blocks, including theory, experiment cards, canonical docs, supplementary theorem/certificate pages, audit pages, prior-art notes, and the experiment archive;
- standardized named Markdown math operators on repository roman forms such as `\mathrm{Cov}`, `\mathrm{Var}`, `\mathrm{Corr}`, `\mathrm{sign}`, and `\mathrm{median}` while leaving LaTeX manuscript sources unchanged; this is a repository consistency convention rather than a claim that MathJax lacks `\operatorname`;
- exhaustively inspected the complete then-current repository Markdown surface for rendering-critical structure, including issue-template front matter, math/code/Mermaid fences, tables, images, links, and public-state routing language;
- added `scripts/validate_github_markdown_render.py`, which sends every Markdown file through GitHub's own GFM REST renderer in CI and checks that expected headings, tables, and images survive structural conversion;
- added `scripts/validate_svg_sources.py` and subsequently hardened it to reject DTD/entities, animation/active elements, event-handler attributes, non-fragment hrefs, active/external CSS references, malformed/non-finite numeric attributes, and backgrounds that fail to cover the full viewBox;
- added `scripts/validate_latex_sources.py`, then changed compiled reference resolution to use only labels reachable from `paper/main.tex` and locked `paper/sections/robust_mom_summary.tex` as the sole intentionally uncompiled manuscript source;
- hardened `scripts/validate_markdown_math.py` to support variable-length CommonMark fences, ignore literal inline code, reject legacy dollar/LaTeX delimiter regressions, enforce repository macro conventions, and check brace, TeX-environment, and common `\left`/`\right` balance inside fenced math blocks;
- hardened `scripts/validate_markdown_links.py` so literal code does not create false positives, root-escaping relative targets fail, linked-image outer destinations are checked, reference-style definitions are checked, and GitHub footnote definitions are excluded from link-target parsing;
- aligned the math, link, and GFM source scanners on CommonMark's zero-to-three-space fenced-code boundary, preventing four-space-indented fence-like text from suppressing later validation;
- pinned the byte-reproduction contract to Ubuntu 24.04, Python 3.11.15, NumPy 2.4.6, pandas 3.0.5, and Matplotlib 3.11.1 after a commit-fixed audit reproduced a serialization-only Figure 2 CSV difference under a different numerical-library stack;
- added `scripts/validate_runtime_contract.py` to cross-check `.python-version`, exact primary NumPy/pandas/Matplotlib pins, installed versions, Ubuntu runner choice, required workflow jobs/commands, manual dispatch, full-SHA reusable-action pins, and checkout credential isolation; this is a primary-package/runtime contract rather than a claim that every transitive wheel is cryptographically locked;
- added executable E1–E5 scientific regression guards for the declared identities, nulls, sign/counterexample controls, predictive-alignment behavior, and branch-coherence contrasts;
- routed the E3 recognition-label null through the general first-person weighted-value calculation using identical trajectory/accessibility arrays while preserving the committed exact-zero null output;
- strengthened the experiment manifest validator to enforce exact E1–E5 ID/order, `LOCK` state, file existence, and separation of locked historical versus current reproduction provenance classes;
- added manifest-driven byte validation of every current reproduction CSV, replacing a duplicate hard-coded output list in CI;
- strengthened reproduction validation again so E1–E5 execution must leave the complete tracked `data/processed/` tree unchanged outside byte-identical current outputs and must not create undeclared files even when `.gitignore` would hide them;
- corrected the current E5 rho-sweep field name from misleading `recognition_corr_increment` to `action_corr_increment`; numerical values and Figure 6 are unchanged, and locked historical schemas are preserved;
- expanded repository-structure validation to cover the workflow, dependency/Python configuration, split-license metadata, all five core theory sources, experiment executables/manifest, archived experiment provenance, theorem-illustration data, the pre-announcement audit records, bibliography fact lock, and principal validator scripts;
- added `scripts/validate_issue_templates.py` and wired it into CI so GitHub issue-template chooser front matter and nonempty bodies are validated;
- pinned `actions/checkout`, `actions/setup-python`, and `actions/upload-artifact` to full commit SHAs rather than mutable major-version tags, and synchronized the validator audit record after a same-day refresh to the current Node-24/v7 Action commits;
- disabled persisted checkout credentials in both validation jobs, kept the workflow token at `contents: read`, and run the runtime contract in both repository and manuscript jobs;
- added `workflow_dispatch` so maintainers can repeat the complete `validate` workflow from the Actions UI without a dummy commit;
- added the `main` validation workflow badge to the root README and synchronized contributor validation commands with the current workflow;
- synchronized open Issue #14, the current S2 review surface, from stale `$$`/`\operatorname{Cov}` rendering syntax to fenced `math`/`\mathrm{Cov}` without changing its scientific review content;
- added `docs/pre_announcement_execution_audit_2026-08-19.md` recording the commit-fixed local execution audit, fixes, provenance boundaries, and remaining browser/Actions gates;
- added `docs/pre_announcement_validator_audit_2026-08-19.md` recording the second-pass false-PASS/validator and Actions-supply-chain audit;
- externally cross-checked manuscript prior-art metadata against publisher/authoritative records rather than relying only on syntactic BibTeX validation; established publication records now replace later arXiv-upload chronology where source identity is clear, including Greaves (2004), Sebens--Carroll (2018), Saunders branch-counting (2021), Hanson (2003), Hult--Nyquist (2016), and Conitzer (2015), while ambiguous/non-identical preprint-to-chapter transformations are not silently conflated;
- represented verified Saunders book chapters as `@incollection`, including *Chance in the Everett Interpretation* (2010, pp. 181--205) and *The Everett Interpretation: Probability* in the Routledge companion, and completed Khawaja's current BJPS page range;
- strengthened `scripts/validate_bibliography_metadata.py` so journal articles require journal/volume/pages/DOI, book chapters require booktitle/editor/publisher/pages/DOI, arXiv-only records remain a separate provenance class, and stock `plain.bst` DOI visibility is preserved through printable notes;
- added `paper/bibliography_fact_lock.md` and extended bibliography validation to require exact agreement on the externally reviewed citation-key set, record class, year, canonical DOI/arXiv identifier, and provenance class; this is a regression guard against silently reversing reviewed chronology, not an automated proof of external bibliographic truth;
- resolved the two same-title Saunders physical-probability arXiv records through the author's PhilSci-Archive provenance: the 2026 deposit is explicitly the latest version and links the 2025 deposit as an earlier available version, so the current `2601.12159` citation is retained;
- audited the frozen-v0.3/current-main core-theorem domain boundary and made four approved current-main corrections explicit: version-neutral canonical title, setup base-integrability, T1 base-integrability, and T5 cross-integrability for `Q(U_1,S_0)`; the frozen v0.3 snapshot remains untouched and the algebraic identities/proof steps are unchanged;
- synchronized those T1/T4/T5 domain assumptions across theory Markdown, canonical TeX, manuscript formal model, theorem section, and proof appendix, and extended `scripts/validate_core_theorem_lock.py` to require them across six public/manuscript surfaces while still normalizing exactly four approved changes back to the frozen canonical blob;
- corrected stale `CONTRIBUTING.md` references to removed release branches and replaced obsolete double-dollar contribution guidance with the current fenced-math convention;
- marked or rewrote historical stacked-branch S2 audit language so it cannot be mistaken for the current single-branch repository state;
- made current research-map and core-theorem headings version-neutral where historical version labels could be mistaken for current scientific status;
- removed public repository-process wording that depended on tool availability;
- removed merged/superseded development branches;
- migrated the frozen v0.2 and v0.3 review snapshots from `release/*` branches to named, commit-pinned `v0.2-public-review` and `v0.3-public-review` tags/GitHub Releases, leaving `main` as the only active branch; the repository no longer describes those tags as platform-immutable without a verified tag ruleset;
- added CI concurrency cancellation and runtime limits so stalled validation jobs cannot remain indefinitely in progress;
- routed manuscript LaTeX installation through explicit Ubuntu archive/security sources so transient runner-mirror failures do not masquerade as manuscript build failures.

### Scientific scope

- T1–T5 retain their identities, numbering, proof algebra, sign/FOSD conclusions, and physical-boundary content; current `main` explicitly closes audited integrability/domain gaps while the frozen v0.3 snapshot remains unchanged;
- no numerical E1–E5 experiment result is changed by the execution/validator audits; the E5 rho current-output schema has one corrected column name and the E3 null test plumbing is stronger without changing its values;
- no S2-family theorem or statistical certificate is changed;
- the manuscript wording change from generic `recognition-activated` to `recognition-dependent` is terminological consistency, not a theorem or mechanism change;
- the bibliography/prior-art metadata corrections change citation provenance and chronology, not the mathematical claims; they reduce the risk of making established prior art look artificially recent through later arXiv upload dates;
- the visualization, GitHub-math compatibility, validation, reproducibility, and workflow-supply-chain changes do not add new physical or statistical evidence;
- the present-self-location identities are direct consequences of the already-defined first-person weighted measure, not a new physical bridge claim;
- locked historical Figure 5/E4 and Figure 7/E2 data provenance remains unchanged and separate from current reruns;
- the Everett accessibility bridge remains physically open;
- tag/Release `v0.3-public-review` remains the frozen v0.3 scientific snapshot at commit `58038763127258bd3e2f0d41708c4dfa01f81fd6`.

## v0.3 — Public Review — 2026-08-18

### Added

- Supplementary Theorem S2 for score-measurable predictive-calibration alignment;
- Corollary S2.2 for posterior-mean self-calibration;
- Corollaries S2.3–S2.10 for calibration robustness, prediction-MSE bounds, finite-sample certification, selection validity, generic confidence envelopes, light-tail concentration, and robust median-of-means certification;
- Supplementary Theorem S2.11 extending predictive alignment beyond score-measurable accessibility via the exact law of total covariance;
- Supplementary Theorem S2.12 lower-bounding the residual term using conditional variances;
- Supplementary Theorem S2.13 rewriting the residual penalty in explained-variance / conditional-mean-correlation form;
- `docs/s2_stack_review_map.md` for dependency, manuscript-placement, and theorem-expansion stop rules;
- `docs/s2_stack_semantic_audit.md` for preservation of theorem and interpretation boundaries;
- `docs/post_v02_manuscript_compression_audit.md` for H/T/D/C/U review of the compressed manuscript structure;
- `docs/post_v02_core_s2_proof_review.md` for a dedicated proof-review pass over S2, S2.11, S2.12, and S2.13;
- `literature/post_v02_targeted_prior_art.md` for a narrow direct-overlap search after the general-accessibility development;
- repository-relative Markdown link validation in CI;
- current/stable/history routing for public review.

### Changed

- the main manuscript is compressed around the conceptual predictive-alignment → general-accessibility → residual-penalty → explained-variance spine rather than presenting all S2 statistical layers with equal prominence;
- detailed S2.3–S2.10 validation machinery is Appendix-first;
- S2 is explicitly identified as the zero-residual special case of S2.11 when accessibility is score-measurable;
- S2.11 now uses explicit square-integrability assumptions;
- S2.11 and S2.12 counterexample/sharpness constructions use bounded Rademacher residuals with strictly positive accessibility;
- S2.13 states the domain and feasibility of the symmetric threshold explicitly;
- observer-selection and Everett self-location prior art is expanded and novelty positioning remains conservative;
- future S2 theorem/statistical expansion is deferred by default unless review identifies a specific need;
- public repository navigation now treats `docs/research_map.md` as the canonical claim-to-source index;
- README, STATUS, DEVELOPMENT_STATUS, ROADMAP, CONTRIBUTING, manuscript routing, and citation metadata are synchronized to the v0.3 public-review snapshot;
- informal `effective/indexical luck` language is explicitly secondary to the formal first-person uplift / trajectory-reweighting terminology.

### Unchanged core

- T1–T5 remain the locked core theorem set;
- E1–E5 remain the locked core experiment suite;
- no sixth core experiment is introduced;
- no S2.14 is introduced;
- the Everett accessibility bridge remains physically open;
- external random generators becoming objectively lucky is not claimed.

## v0.2 — Public Review — 2026-08-17

### Added

- canonical `STATUS.md` research ledger;
- `ROADMAP.md` for repository and manuscript milestones;
- research map, notation reference, and claims/assumptions ledger;
- H/T/D/C/U experiment cards for E1–E5;
- topic-split supplementary notes;
- recognition-time stopping-time formalization with explicit v0.2 defer of a universal timing-order theorem;
- initial and extended prior-art ledgers;
- manuscript scaffold with Related Work and bibliography;
- six committed publication-oriented SVG figures with deterministic regeneration script;
- PDF figure generator for LaTeX manuscript builds;
- complete manuscript appendix proofs for T1–T5 and supplementary derivations;
- Supplementary Theorem S1 for shared-latent policy coherence;
- historical experiment archive index and supersession ledger;
- explicit Everett bridge support / constraint / rejection criteria;
- v0.2 manuscript claim consistency audit and post-layout re-audit;
- final `docs/v0.2_release_audit.md` repository audit;
- independent LaTeX/PDF manuscript build job in GitHub Actions.

### Changed

- narrowed novelty positioning so normalized weighting, anthropic decision-making, self-location-dependent action, and the elementary covariance identity are not treated as standalone novelty claims;
- expanded Related Work to include advocates and critics of Everettian probability, alternative many-world measure proposals, classical weighted-measure context, and direct self-locating policy-optimization work;
- integrated all six figures into the manuscript with captions that identify schematic/theorem-illustration or classical-simulation status;
- clarified that earlier recognition is not universally better without explicit causal and information assumptions;
- clarified that structural bridge coherence, interpretive adequacy, and empirical falsifiability are distinct levels of evaluation.

## v0.1 — Public Technical Review

- core theorem set published;
- E1–E5 reproduction scripts and result summaries published;
- null and counterexample stress tests published;
- split licensing and citation metadata added;
- GitHub Actions validation added;
- Markdown math rendering corrected;
- E4/E5 reproducibility audit completed.