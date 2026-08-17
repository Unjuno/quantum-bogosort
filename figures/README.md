# Figure Plan

Publication figures should be generated from locked or reproducible repository outputs and should record the script/data source used.

## Planned figures

1. **Framework diagram** — recognition to policy to trajectory/accessibility to first-person distribution.
2. **FOSD figure** — base versus first-person CDF under monotone accessibility, plus a nonmonotone counterexample panel.
3. **Recognition decomposition** — ordinary trajectory effect, QBS conditioning effect, and total effect.
4. **Interaction sign** — rescue-bad / neutral / amplify-good interaction benchmark.
5. **Adaptation quality** — policy effect, QBS marginal effect, interaction, and total first-person effect versus adaptation quality.
6. **Branch coherence** — cross-copy action correlation versus shared environmental/recognition structure, contrasted with marginal FP uplift.

## Figure requirements

- source data must be committed under `data/processed/`;
- generation script must be committed under `figures/` or `scripts/`;
- axes and units must be explicit;
- uncertainty intervals should be shown when replication data exist;
- toy-model quantities must not be labeled as physical Everett observables;
- figure captions must state whether the panel is theorem illustration, simulation, or interpretation schematic.
