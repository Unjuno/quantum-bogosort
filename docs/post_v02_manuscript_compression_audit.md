# Post-v0.2 Manuscript Compression Audit

**Status:** editorial / semantic audit  
**Scope:** PR #21 manuscript presentation after the S2.11–S2.13 general-accessibility extension

## H — editorial hypothesis

The post-v0.2 S2 stack should strengthen the paper without making the main text read like a sequence of concentration-inequality variants.

The intended main-text spine is:

$$
\text{recognition}
\to
\text{policy / trajectory}
\to
\text{predictive signal}
\to
\text{accessibility alignment}
\to
\text{first-person conditioning}.
$$

For general accessibility the central exact identity is:

$$
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(E[U\mid Y],E[S\mid Y])
+
E[\mathrm{Cov}(U,S\mid Y)].
$$

The statistical certification machinery should support this spine without replacing it.

## T — target manuscript structure

### Main text

The main text should contain:

1. T1–T5 as the locked core theorem set;
2. S2 as the clean predictive-alignment mechanism;
3. S2.2 as the posterior-mean calibration corollary;
4. S2.11 as the exact general-accessibility decomposition;
5. the compact S2.12 worst-case residual penalty needed to motivate S2.13;
6. S2.13 as the interpretable explained-variance sufficient condition;
7. E1–E5 as the locked core computational evidence;
8. the Everett bridge as a separate physical assumption.

### Appendix-first

The detailed validation machinery should remain primarily in the Appendix:

- S2.3 calibration-error robustness;
- S2.4 prediction-MSE bound;
- S2.5 bounded held-out certificate;
- S2.6 independent-training validity;
- S2.7 finite-candidate multiplicity control;
- S2.8 generic confidence-envelope composition;
- S2.9 light-tail instantiation;
- S2.10 median-of-means instantiation;
- the full S2.12 proof and sharpness argument;
- the full S2.13 proof and boundary algebra.

## D — implemented changes

### Adaptive-Agent section

The previous main-text derivations of S2.5–S2.9 were compressed into one paragraph describing their role and referring detailed finite-sample machinery to the Appendix.

The main section now emphasizes:

$$
m(y)=E[U\mid Y=y],
$$

$$
S=s(Y),
$$

and:

$$
\mathrm{Cov}(U,S)
=
\mathrm{Cov}(m(Y),s(Y)).
$$

It retains the mutual-information boundary:

$$
I(U;Y)>0
$$

does not by itself imply favorable covariance.

### General-accessibility section

A dedicated main-text section now follows the adaptive-agent mechanism. It introduces:

$$
m(Y)=E[U\mid Y],
\qquad
 a(Y)=E[S\mid Y],
$$

and the exact S2.11 decomposition. It then states the compact S2.12 residual-variance penalty and the S2.13 explained-variance form.

### Statistical summary demotion

The standalone `robust_mom_summary` section is no longer included in `paper/main.tex`. S2.10 remains available in the Appendix and supplementary theorem notes.

### Front and back matter synchronization

The Abstract and Introduction now mention the predictive-alignment mechanism and the general-accessibility residual term without claiming a physical Everett derivation.

The Limitations section now states that:

- positive mutual information is insufficient;
- residual conditional covariance cannot be dropped;
- S2.12/S2.13 are sufficient worst-case certificates;
- certificate failure is inconclusive;
- finite-sample validity depends on held-out and selection assumptions.

The Discussion now frames S2.11/S2.13 as structural decomposition and interpretation tools rather than standalone novelty of standard probability identities.

## C — claim-preservation checks

### Core theorem identity

T1–T5 remain the locked core theorem set.

**Check:** PASS.

### FOSD boundary

Positive covariance is not presented as sufficient for FOSD; T3 retains its monotonicity condition.

**Check:** PASS.

### Recognition null

Recognition remains causally effective only through trajectory and/or accessibility changes.

**Check:** PASS.

### General-accessibility residual term

The main text explicitly retains:

$$
E[\mathrm{Cov}(U,S\mid Y)].
$$

It is not silently set to zero outside the score-measurable special case.

**Check:** PASS.

### S2.13 sufficiency boundary

The condition:

$$
\rho_{ma}\sqrt{A_UA_S}
>
\sqrt{(1-A_U)(1-A_S)}
$$

is stated as sufficient, not necessary.

**Check:** PASS.

### Physical interpretation boundary

No statistical certificate is described as deriving the Everett accessibility bridge.

**Check:** PASS.

## U — unresolved editorial questions

Before promotion to a preprint branch, external or dedicated internal review should decide:

1. whether S2.13 improves intuition enough to remain in the main text;
2. whether the compact S2.12 inequality should be stated in the main text or only described verbally;
3. whether the full S2.5–S2.10 statistical stack belongs in the paper Appendix or partly in repository-only supplementary material;
4. whether the manuscript length remains appropriate for a foundations preprint;
5. whether direct prior art exists for the combined recognition-policy / conditional-accessibility / residual-dependence construction.

These are editorial and novelty questions, not unresolved algebraic identities.

## ERROR CHECK

1. No new theorem is introduced by this audit.
2. The core E1–E5 experiment list is unchanged.
3. The frozen v0.2 `main` baseline is unchanged.
4. Statistical validation is not conflated with the Everett bridge.
5. The general-accessibility residual term is preserved explicitly.
6. S2.12/S2.13 remain worst-case sufficient certificates.
7. The standalone robust-MoM main-text summary is demoted without deleting its proof or supplementary source.
8. Abstract, Introduction, main mechanism sections, Limitations, and Discussion now use the same conceptual hierarchy.

## Audit conclusion

**PASS — THE POST-v0.2 MANUSCRIPT NOW PRESENTS THE S2 FAMILY AS A CONCEPTUAL SPINE WITH APPENDIX-FIRST STATISTICAL SUPPORT, RATHER THAN AS A FLAT SEQUENCE OF EQUALLY PROMINENT THEOREMS.**
