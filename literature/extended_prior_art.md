# Extended Prior-Art Review

This note expands the initial literature ledger with explicit criticism of Everettian probability programs, alternative many-world probability constructions, classical weighted-measure mathematics, and direct work connecting self-locating beliefs to policy choice.

## Everett probability: criticism and boundary conditions

### Huw Price

**Sources:**
- Huw Price, "Probability in the Everett World: Comments on Wallace and Greaves," arXiv:quant-ph/0604191 (2006).
- Huw Price, "Decisions, Decisions, Decisions: Can Savage Salvage Everettian Probability?", in *Many Worlds? Everett, Quantum Theory, and Reality*, pp. 369–390 (Oxford University Press, 2010), DOI `10.1093/acprof:oso/9780199560561.003.0014`; earlier arXiv:0802.1390.

Price challenges the analogy between Everettian branching and ordinary decision under uncertainty and raises objections to Deutsch-Wallace-Greaves style probability arguments.

**QBS relevance:** QBS should not assume that a branch-sensitive decision rule automatically has a privileged physical-probability interpretation. The mathematical change of measure must remain separate from the physical Everett bridge.

### Adrian Kent

**Source:** Adrian Kent, "One World Versus Many: The Inadequacy of Everettian Accounts of Evolution, Probability, and Scientific Confirmation," in *Many Worlds? Everett, Quantum Theory, and Reality*, pp. 307–354 (Oxford University Press, 2010), DOI `10.1093/acprof:oso/9780199560561.003.0012`; earlier arXiv:0905.0624.

Kent argues that branch weights, rational decision roles, and empirical confirmation are logically distinct problems and criticizes attempts to identify them too quickly.

**QBS relevance:** this reinforces the repository's separation between base branch measure, rational policy effects, observer-indexed conditioning, and empirical confirmation. A successful abstract QBS theorem does not establish that its accessibility weight is a physical chance measure.

## Alternative probability constructions in many-world theories

### Mateus Araújo

**Source:** Mateus Araújo, "Probability in Two Deterministic Universes," *Foundations of Physics* 49(3), 202–231 (2019), DOI `10.1007/s10701-019-00241-7`; earlier arXiv:1805.01753.

Araújo studies subjective and objective probability in deterministic many-world theories and emphasizes that the appropriate norm/measure depends on the underlying dynamics.

**QBS relevance:** the base measure cannot be treated as arbitrary if the framework is mapped to a physical theory. A future Everett bridge must explain why a particular accessibility construction is compatible with the physical dynamics rather than merely mathematically admissible.

### Simon Saunders — branch counting and physical probability

**Sources:**
- Simon Saunders, "Branch-counting in the Everett Interpretation of quantum mechanics," *Proceedings of the Royal Society A* 477(2255), 20210600 (2021), DOI `10.1098/rspa.2021.0600`.
- Simon Saunders, "Physical probability in the Everett interpretation and Bell inequalities," arXiv:2601.12159 (2026). The author's PhilSci-Archive record identifies the 2026 deposit as the latest version and links the 2025 same-title deposit as an earlier version.

These works develop explicit physical-probability proposals inside Everettian quantum mechanics rather than treating probability as a free observer-indexed reweighting.

**QBS relevance:** they sharpen the bridge-assumption question. QBS currently takes a base measure as given and introduces a distinct policy-dependent accessibility map. Any physical Everett application must explain whether that map is compatible with, derived from, or independent of a physical probability account.

## Weighted measures and importance sampling

### Hult and Nyquist

**Source:** Henrik Hult and Pierre Nyquist, "Large deviations for weighted empirical measures arising in importance sampling," *Stochastic Processes and their Applications* 126(1), 138–170 (2016), DOI `10.1016/j.spa.2015.08.002`; earlier arXiv:1210.2251.

Importance sampling and related change-of-measure methods routinely represent expectations under weighted probability measures.

**QBS relevance:** the generic fact that weighted expectations differ from unweighted expectations, and the use of normalized nonnegative weights, are not themselves novel. The covariance identity in QBS should be presented as a transparent mathematical identity within a larger recognition-dependent decision framework, not as a new theory of weighted probability.

## Direct overlap: self-location and policy optimization

### Cooper, Oesterheld, and Conitzer (2024)

**Source:** Emery Cooper, Caspar Oesterheld, and Vincent Conitzer, "Can CDT rationalise the ex ante optimal policy via modified anthropics?", arXiv:2411.04462 (2024). The authors' current publication listing still classifies it as a working paper.

This work studies Newcomb-like problems in which self-locating beliefs, including beliefs about being in simulations of the agent, can change the action recommended by causal decision theory. It characterizes conditions under which modified anthropic/self-locating beliefs recover policies that are optimal from an ex ante policy-optimization perspective.

**Why this is close to QBS:** it explicitly links self-locating structure to policy selection rather than treating self-location as passive belief only. This weakens any novelty claim based merely on "self-location affects decisions" or "copy structure can support policy-level optimization."

**Remaining QBS distinction:** the present project centers on a recognition/information state that can change which policy is selected; the selected policy may jointly change trajectory utility and an observer-indexed accessibility map, yielding exact decomposition of trajectory, conditioning, and interaction terms. It also separately studies realized cross-branch action correlation. Those structural components, rather than the generic link between anthropics and policy, must carry any novelty claim.

### Conitzer (2015)

**Source:** Vincent Conitzer, "Can rational choice guide us to correct de se beliefs?", *Synthese* 192(12), 4107–4119 (2015), DOI `10.1007/s11229-015-0737-x`; a later arXiv posting is 1705.06332.

Conitzer studies whether decision-theoretic behavior can adjudicate self-locating beliefs in Sleeping-Beauty-style settings and cautions that apparently unreasonable actions can arise for reasons other than the underlying de se probabilities.

**QBS relevance:** this reinforces the need to separate an accessibility/self-location rule from the policy technology and utility structure. A policy outcome cannot by itself validate the self-location measure used to evaluate it.

### Armstrong (2011)

**Source:** Stuart Armstrong, "Anthropic decision theory," arXiv:1110.6437 (2011).

Anthropic decision theory addresses action choice directly in self-locating problems and shows that relationships among copies/agents and their objectives matter for the resulting decisions.

**QBS relevance:** this is another reason not to claim novelty for applying decision theory to anthropic copies. QBS must instead be positioned by its recognition-dependent trajectory/accessibility decomposition and branch-coherence analysis.

## Consequence for novelty claims

After the targeted overlap search, the novelty hypothesis should be stated more narrowly:

1. recognition/information state can change which policy is selected, without assigning recognition a privileged physical causal power;
2. the selected policy changes branch-wise trajectory utility and may also change accessibility;
3. ordinary trajectory effects and first-person conditioning effects admit an exact decomposition;
4. policy-QBS interaction admits a separate exact decomposition;
5. adaptation can endogenously generate predictor/outcome alignment in toy agents;
6. marginal first-person uplift is separated from branch-wide policy coherence;
7. shared-latent branch-policy coherence has an explicit supplementary theorem under hierarchical assumptions.

The project should **not** claim novelty for:

- weighted conditional expectation;
- self-locating probability or de se belief;
- observer selection in general;
- decision theory in anthropic/copy settings;
- using self-locating beliefs to alter action recommendations;
- ex ante policy optimization in problems with agent copies;
- Everettian decision theory or branch-sensitive probability measures by themselves.

## Remaining search directions

The highest-value remaining search is now narrower:

- work where an agent's recognition or information state changes policy selection and a self-location/selection rule;
- work deriving an observer-indexed selection measure endogenously from adaptive policy or observer persistence;
- direct decompositions separating ordinary causal policy effects from self-location-weighting effects;
- causal-decision formulations where the weighting map itself changes with policy.

These are more specific than a general search for anthropic decision theory, which already has substantial prior art.
