from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md", "STATUS.md", "DEVELOPMENT_STATUS.md", "ROADMAP.md", "CHANGELOG.md",
    "CONTRIBUTING.md", "CITATION.cff", "requirements.txt", ".python-version", ".gitignore",
    "LICENSE", "LICENSES/README.md", "LICENSES/CC-BY-4.0.txt", "LICENSES/CC0-1.0.txt",
    ".github/workflows/validate.yml",
    "docs/research_map.md", "docs/notation.md", "docs/claims_and_assumptions.md",
    "docs/everett_bridge_tests.md", "docs/manuscript_claim_audit.md", "docs/v0.2_release_audit.md",
    "docs/pre_announcement_execution_audit_2026-08-19.md",
    "docs/pre_announcement_validator_audit_2026-08-19.md",
    "docs/s2_stack_review_map.md", "docs/s2_stack_semantic_audit.md",
    "docs/post_v02_manuscript_compression_audit.md", "docs/post_v02_core_s2_proof_review.md",
    "docs/s2_adaptive_alignment_audit.md", "docs/s2_finite_sample_certificate_audit.md",
    "docs/s2_selection_validity_audit.md", "docs/s2_confidence_envelope_audit.md",
    "docs/s2_light_tail_certificate_audit.md", "docs/s2_robust_mom_certificate_audit.md",
    "docs/s2_residual_covariance_audit.md", "docs/s2_residual_variance_audit.md",
    "docs/s2_explained_variance_audit.md",
    ".github/ISSUE_TEMPLATE/proof-counterexample.md", ".github/ISSUE_TEMPLATE/prior-art.md",
    ".github/ISSUE_TEMPLATE/reproducibility.md", ".github/ISSUE_TEMPLATE/everett-bridge.md",
    "theory/core_theorems.md", "theory/core_theorems.tex", "theory/propositions_boundaries.md",
    "theory/theorem_1_3.md", "theory/theorem_4_5.md",
    "experiments/README.md", "experiments/E1_FOSD.md", "experiments/E2_LEARNED_AGENT.md",
    "experiments/E3_RECOGNITION.md", "experiments/E4_INTERACTION.md", "experiments/E5_BRANCH_MAP.md",
    "experiments/archive/README.md", "experiments/archive/INDEX.md",
    "experiments/exp1_fosd_and_stress.py", "experiments/exp2_minimal_agent.py",
    "experiments/exp3_recognition_decomposition.py", "experiments/exp4_interaction.py",
    "experiments/exp5_branch_map.py", "experiments/manifest.csv",
    "supplementary/README.md", "supplementary/research_notes.md",
    "supplementary/multi_observer.md", "supplementary/binary_soft_qbs.md",
    "supplementary/repeated_filtering.md", "supplementary/gaussian_model.md", "supplementary/adaptive_agent.md",
    "supplementary/finite_sample_certificate.md", "supplementary/selection_validity.md",
    "supplementary/confidence_envelope_certificate.md", "supplementary/light_tail_certificate.md",
    "supplementary/robust_mom_certificate.md", "supplementary/residual_covariance_extension.md",
    "supplementary/residual_variance_certificate.md", "supplementary/explained_variance_certificate.md",
    "supplementary/evidence_activation.md", "supplementary/recognition_time.md",
    "supplementary/selectivity_frontier.md", "supplementary/branch_recognition.md",
    "literature/prior_art.md", "literature/extended_prior_art.md", "literature/post_v02_targeted_prior_art.md",
    "paper/README.md", "paper/main.tex", "paper/references.bib",
    "figures/README.md", "figures/generate_figures.py", "figures/generate_pdf_figures.py",
    "figures/generated/fig1_framework.svg", "figures/generated/fig2_fosd.svg",
    "figures/generated/fig3_recognition_decomposition.svg", "figures/generated/fig4_interaction_sign.svg",
    "figures/generated/fig5_adaptation_quality.svg", "figures/generated/fig6_branch_coherence.svg",
    "figures/generated/fig7_predictive_alignment.svg",
    "data/processed/fig2_fosd_theorem_illustration.csv",
    "scripts/validate_bibliography_metadata.py", "scripts/validate_citation_metadata.py",
    "scripts/validate_figure_set.py", "scripts/validate_github_markdown_render.py",
    "scripts/validate_issue_templates.py", "scripts/validate_latex_sources.py",
    "scripts/validate_license_map.py", "scripts/validate_manifest.py",
    "scripts/validate_reproduction_outputs.py", "scripts/validate_runtime_contract.py",
    "scripts/validate_markdown_links.py", "scripts/validate_markdown_math.py",
    "scripts/validate_repository_structure.py", "scripts/validate_svg_sources.py",
]

if len(required) != len(set(required)):
    raise SystemExit("Repository structure validator contains duplicate required paths")

missing = [path for path in required if not (ROOT / path).is_file()]
if missing:
    raise SystemExit("Missing required repository-map files:\n" + "\n".join(missing))

declared_markdown = {path for path in required if path.endswith(".md")}
actual_markdown = {
    path.relative_to(ROOT).as_posix()
    for path in ROOT.rglob("*.md")
    if ".git" not in path.parts
}
if actual_markdown != declared_markdown:
    undeclared = sorted(actual_markdown - declared_markdown)
    declared_but_absent = sorted(declared_markdown - actual_markdown)
    details: list[str] = []
    if undeclared:
        details.append(
            "Markdown files outside the declared public/audit inventory: " + ", ".join(undeclared)
        )
    if declared_but_absent:
        details.append(
            "Declared Markdown inventory entries absent from the repository: "
            + ", ".join(declared_but_absent)
        )
    raise SystemExit("Markdown inventory mismatch:\n" + "\n".join(details))

main_tex = (ROOT / "paper/main.tex").read_text(encoding="utf-8")
section_refs = re.findall(r"\\input\{([^}]+)\}", main_tex)
missing_sections = []
for ref in section_refs:
    path = ROOT / "paper" / f"{ref}.tex"
    if not path.is_file():
        missing_sections.append(str(path.relative_to(ROOT)))

if missing_sections:
    raise SystemExit("Missing manuscript sections:\n" + "\n".join(missing_sections))

print(
    f"Repository structure OK: {len(required)} required files; complete {len(actual_markdown)}-file "
    f"Markdown inventory declared; all five core theory sources; consolidated/archived research "
    f"provenance; both pre-announcement audit records; runtime/citation/bibliography/license/figure-set "
    f"validators; and {len(section_refs)} manuscript sections found."
)
