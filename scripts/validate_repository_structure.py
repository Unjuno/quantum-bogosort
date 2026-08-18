from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

required = [
    "STATUS.md", "ROADMAP.md", "CHANGELOG.md",
    "docs/research_map.md", "docs/notation.md", "docs/claims_and_assumptions.md",
    "docs/everett_bridge_tests.md", "docs/manuscript_claim_audit.md", "docs/v0.2_release_audit.md",
    "docs/s2_stack_review_map.md", "docs/s2_stack_semantic_audit.md",
    "docs/post_v02_manuscript_compression_audit.md",
    "docs/s2_adaptive_alignment_audit.md", "docs/s2_finite_sample_certificate_audit.md",
    "docs/s2_selection_validity_audit.md", "docs/s2_confidence_envelope_audit.md",
    "docs/s2_light_tail_certificate_audit.md", "docs/s2_robust_mom_certificate_audit.md",
    "docs/s2_residual_covariance_audit.md", "docs/s2_residual_variance_audit.md",
    "docs/s2_explained_variance_audit.md",
    "experiments/E1_FOSD.md", "experiments/E2_LEARNED_AGENT.md", "experiments/E3_RECOGNITION.md",
    "experiments/E4_INTERACTION.md", "experiments/E5_BRANCH_MAP.md",
    "supplementary/README.md", "supplementary/multi_observer.md", "supplementary/binary_soft_qbs.md",
    "supplementary/repeated_filtering.md", "supplementary/gaussian_model.md", "supplementary/adaptive_agent.md",
    "supplementary/finite_sample_certificate.md", "supplementary/selection_validity.md",
    "supplementary/confidence_envelope_certificate.md", "supplementary/light_tail_certificate.md",
    "supplementary/robust_mom_certificate.md", "supplementary/residual_covariance_extension.md",
    "supplementary/residual_variance_certificate.md", "supplementary/explained_variance_certificate.md",
    "supplementary/evidence_activation.md", "supplementary/recognition_time.md",
    "supplementary/selectivity_frontier.md", "supplementary/branch_recognition.md",
    "literature/prior_art.md", "literature/extended_prior_art.md",
    "paper/README.md", "paper/main.tex", "paper/references.bib",
    "figures/README.md", "figures/generate_figures.py", "figures/generate_pdf_figures.py",
    "figures/generated/fig1_framework.svg", "figures/generated/fig2_fosd.svg",
    "figures/generated/fig3_recognition_decomposition.svg", "figures/generated/fig4_interaction_sign.svg",
    "figures/generated/fig5_adaptation_quality.svg", "figures/generated/fig6_branch_coherence.svg",
]

missing = [path for path in required if not (ROOT / path).exists()]
if missing:
    raise SystemExit("Missing required repository-map files:\n" + "\n".join(missing))

main_tex = (ROOT / "paper/main.tex").read_text(encoding="utf-8")
section_refs = re.findall(r"\\input\{([^}]+)\}", main_tex)
missing_sections = []
for ref in section_refs:
    path = ROOT / "paper" / f"{ref}.tex"
    if not path.exists():
        missing_sections.append(str(path.relative_to(ROOT)))

if missing_sections:
    raise SystemExit("Missing manuscript sections:\n" + "\n".join(missing_sections))

print(f"Repository structure OK: {len(required)} required files and {len(section_refs)} manuscript sections found.")
