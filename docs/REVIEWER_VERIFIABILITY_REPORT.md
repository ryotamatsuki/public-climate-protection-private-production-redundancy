> **Independent final audit update, 2026-10-03:** The record below is historical input, not inherited evidence. Current independent findings, repairs, and release conditions are in [INDEPENDENT_FINAL_AUDIT_2026-10-03.md](INDEPENDENT_FINAL_AUDIT_2026-10-03.md). The immutable v4 baseline and its separately pinned non-scientific descendant are distinguished explicitly.

# Reviewer Verifiability Report — v4

**Date:** 2026-10-03  
**Canonical scientific freeze:** \`PCPPR-THEORY-FREEZE-2026-10-03-v4\`  
**Audited canonical main:** \`8869e6f1b342bc73e7b5a3c09dc685d607e1ce91\`  
**Workflow:** Theory Paper Research Pipeline v2.5 / Stage 13  
**Map:** \`docs/REVIEWER_VERIFIABILITY_MAP.md\`

## Executive verdict

**PASS — REVIEWER VERIFIABILITY RE-CLOSED FOR V4**

The current paper is theorem-bearing and computer-assisted, so reviewer verifiability is a
Stage-13 closure condition.

A clean reconstruction of the headline result finds no proof-critical transition that
requires the referee to guess an omitted object or open production code merely to identify
the derivation.

The manuscript follows the governing rule:

> compress routine algebra; preserve conceptual bridges.

## 1. Manuscript-facing proof architecture

The current paper presents the complete conceptual chain:

\[
\text{primitives}
\rightarrow
\text{availability-state payoffs}
\rightarrow
\text{backup game}
\rightarrow
\text{location game}
\rightarrow
\text{national/local policy objectives}
\rightarrow
\text{planner and decentralized policy results}.
\]

Every high-stakes transition has an explicit displayed object or named lemma.

### Backup

PASS.

The global feasible best response is explicitly clipped. The manuscript acknowledges that
the unclipped response can exceed one for some rival actions and therefore does not use
interior FOCs as a global equilibrium argument. The contraction bound is visible in the
main text.

### Location

PASS.

The location payoff differences, affine cutoff response, endpoint objects, contraction
slope, and fixed point are displayed. The Appendix explains exactly which endpoint and
denominator inequalities are computer-certified.

### Policy-object construction

PASS.

Profile-level surplus after backup is defined, then explicitly aggregated over the
endogenous location probabilities. The government and planner objectives are already
defined in the Model. No hidden “code-only welfare function” is needed.

### Planner globality

PASS.

The Appendix identifies the rational derivative objects, explains the Bernstein
weighted-average principle in a simple one-dimensional example, extends it to the policy
rectangle, and states the sign implication. Large coefficient arrays are delegated to the
archive.

### Local Nash equilibrium

PASS.

The paper separates root isolation from global best-response verification. The symmetric
FOC root is stationary; whole-own-domain strict concavity makes it the unique global best
response. Boundary actions are covered.

### Open-set theorem

PASS.

The current proof uses the full diagonal derivative
\(G_{A,a_Aa_A}+G_{A,a_Aa_B}\) and explicitly preserves the clipped-backup contraction
margin in the parameter neighborhood. The proof states that it does not establish
uniqueness of all first-stage policy equilibria or asymmetric-primitive persistence.

## 2. Computer-assisted-proof audit

For every exact certificate used in the headline theorem, the manuscript exposes:

1. mathematical object;
2. strategy/policy domain;
3. certified sign/root/interiority property;
4. logical implication for the economic claim.

The delegated calculations are mechanical exact objects: Bernstein coefficients, rational
numerator/denominator expansions, root-isolation traces, generated finite arithmetic, and
formal-kernel details.

Numerical optimization is explicitly described as counterexample search / implementation
stress testing and is not used as proof of the headline theorem.

**Computer-assisted-proof exposition: PASS.**

## 3. Economic-paper readability

The paper does not read like a verification report.

- the Introduction contains no Lean or CI discussion;
- the Model states economic primitives and timing first;
- Sec. 3 solves economically interpretable continuation games;
- Sec. 4 states the policy wedge and theorem;
- Sec. 5 explains welfare channels;
- Sec. 6 uses a benchmark to identify the minimal mechanism;
- formal verification appears only in the Appendix after the economic proof is complete.

The proof assistant is therefore an assurance layer, not the narrative spine.

**Economic-paper readability: PASS.**

## 4. Formal-verification statement fidelity

PASS.

The Appendix says explicitly that the final Lean theorem is conditional on supplied
function/sign bridges and that clipped-backup uniqueness and open-set persistence remain
outside the final Lean theorem. It also discloses the \`native_decide\` trust boundary.

The manuscript does not claim “Lean proves the entire model.”

## 5. Scope / quantifier readability

PASS.

A reader can distinguish:

- unique downstream continuations;
- unique planner optimum at the canonical witness;
- existence of a strictly positive symmetric local policy Nash equilibrium;
- no claim of uniqueness of all first-stage policy equilibria;
- exact baseline-family open-set theorem;
- numerical-only nonlinear-risk/logistic diagnostics;
- constrained industrial-surplus planner rather than first best.

This matches the v4 Stage-7.5A certificate.

## 6. Welfare-selection readability

PASS.

The planner objective and policy choice set are explicit. Location and backup remain private
choices. The text repeatedly labels the benchmark as protection-policy constrained and
industrial-surplus specific.

The national constant \(2b\) and equal local incidence rule are explained rather than
hidden in accounting.

## 7. Exhibit / proof interaction

PASS.

Figure 1 is clearly labeled as an origin-marginal exhibit rather than an equilibrium curve.
Table 1 is an exact derivative decomposition rather than a simulation table.

No exhibit is relied on as proof of the theorem.

## 8. Clean-room hostile reconstruction result

The full headline chain can be reconstructed from the paper-facing package:

1. product-state payoffs;
2. globally feasible backup game;
3. unique location continuation;
4. national/local policy functions;
5. global planner sign certificate;
6. exact local FOC root;
7. whole-domain own-policy concavity;
8. positive symmetric Nash equilibrium;
9. open-set persistence.

No item is classified:

- BRIDGE NEEDED;
- APPENDIX DETAIL NEEDED for conceptual correctness;
- SUBSTANTIVE DEFECT.

Large exact expansion details are correctly classified as delegated mechanical detail.

## 9. Residual reader burdens

The paper remains technically demanding. The principal unavoidable burdens are:

- understanding the conditional-independence availability law;
- tracking how location-profile continuations enter expected national surplus;
- accepting the Bernstein sign argument before checking the generated coefficient archive;
- distinguishing own-policy concavity from the diagonal derivative used for IFT.

All four are now explicitly discussed in the manuscript. None requires inference from code.

## 10. Stage-13 reviewer-verifiability closure

**PASS — FULL FOR THE CLAIMED MANUSCRIPT SCOPE.**

No manuscript change is required for reviewer verifiability at the current v4 scientific
object.

If later edits remove a proof-critical bridge, enlarge theorem quantifiers, change the
computer-assisted proof target, alter the formal scope, or change the headline equilibrium
claim, this report becomes stale and Stage 13 must be rerun.
