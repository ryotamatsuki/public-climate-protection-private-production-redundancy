# Exposition Architecture — v4 Integrated Manuscript

**Date:** 2026-10-03  
**Canonical scientific freeze:** `PCPPR-THEORY-FREEZE-2026-10-03-v4`  
**Audited canonical main:** `8869e6f1b342bc73e7b5a3c09dc685d607e1ce91`  
**Workflow:** Theory Paper Research Pipeline v2.5, Stage 10 / Stage 13  
**Profile:** GENERAL THEORY / THEORY-FIRST

## 1. Reader objective

The manuscript should let a competent environmental/IO theorist understand the paper in
this order, without consulting code:

1. public protection changes physical reliability and private geographic contingency
   readiness;
2. decentralized governments additionally value plant attraction;
3. the model makes those two margins explicit;
4. downstream product, backup, and location continuations are solved before policy;
5. the main theorem establishes planner-zero / local-positive protection on a nonempty
   open set;
6. welfare accounting explains why protection can have a negative industrial margin;
7. mechanism benchmarks identify which parts of the oligopoly block are necessary;
8. institutional, literature, discussion, and conclusion sections delimit interpretation,
   novelty, and portability;
9. the Appendix supplies the human-readable proof and delegates only large exact sign
   computations to reproducible certificates.

This is the governing exposition architecture. The manuscript is not organized around
the proof assistant, codebase, or repository workflow.

## 2. Actual reader-arrival budget

Measured from the clean v4 main build in workflow run `37075140839`:

| Milestone | First page | Assessment |
|---|---:|---|
| Research question / mechanism / main result | 1 | PASS |
| Model begins | 3 | PASS |
| Full backward-induction equilibrium characterization begins | 6 | PASS |
| Headline policy-result section begins | 9 | PASS |
| Welfare mechanism section begins | 13 | PASS |
| Mechanism benchmark section begins | 15 | PASS |
| Institutional interpretation | 16 | PASS |
| Related literature | 18 | PASS |
| Discussion / scope | 19 | PASS |
| Conclusion | 21 | PASS |
| Proof Appendix | 22 | PASS |

The Introduction occupies roughly two manuscript pages before the Model. No background,
literature, institutional detail, formal-method discussion, or computational workflow
delays the core economic object.

## 3. Section-purity architecture

| Section | Dominant function | Classification | Stage-13 decision |
|---|---|---|---|
| Introduction | question, mechanism, result, contribution boundary, roadmap | CORE | retain |
| Model | primitives, timing, strategy sets, objectives, welfare benchmark | CORE | retain |
| Equilibrium Characterization | product market → backup → location continuation | CORE | retain |
| Local Protection Competition and Main Result | marginal wedge, theorem, exact witness, interpretation | CORE | retain |
| Welfare | state accounting, aggregation, readiness wedge, channel decomposition | CORE | retain |
| Mechanism Benchmarks | exact Δ=0 benchmark and restricted-margin interpretation | HELPFUL / near-CORE | retain |
| Institutional Interpretation | map primitives to policy/BCP setting and state testable implications | HELPFUL | retain |
| Related Literature | theorem-level novelty boundary and closest parent classes | HELPFUL | retain |
| Discussion | welfare scope, primitive limitations, diagnostic portability | HELPFUL | retain |
| Conclusion | answer question and restate certified scope only | CORE | retain |
| Appendix | human-readable proofs, exact certificate method, reproducibility/formal boundary | APPENDIX | retain |

No current main-text section is classified DELETE.

## 4. Proof exposition architecture

The proof-facing exposition follows the dependency chain:

[
	ext{primitives}
ightarrow
	ext{product-market state payoffs}
ightarrow
	ext{backup best responses}
ightarrow
	ext{location cutoff equilibrium}
ightarrow
mathcal S
ightarrow
W,G_A,G_B
ightarrow
	ext{planner / local policy results}.
]

The manuscript preserves the following conceptual bridge equations in human-readable form:

1. expected firm profit, equation `expected-profit`;
2. clipped backup best response, equation `backup-br-global`;
3. backup linear system, equation `backup-linear-system`;
4. backup contraction bound, equation `backup-contraction-bound`;
5. affine location best response and endpoint map, equations `location-br` and
   `location-endpoints`;
6. unique location fixed point, equation `location-prob`;
7. location-weighted expected national surplus, equation
   `expected-surplus-location`;
8. local/social marginal decomposition, equation `marginal-decomposition`;
9. exact witness and headline theorem;
10. diagonal FOC derivative
   (F_a=G_{A,a_Aa_A}+G_{A,a_Aa_B}) for open-set persistence.

These bridges remain in the PDF. Large expanded polynomials, Bernstein coefficient arrays,
normalization archives, root-isolation traces, and Lean kernel traces remain outside the
main flow because they are mechanical verification objects rather than economic reasoning.

## 5. Human-readable proof / machine-verification boundary

### Human-readable in the manuscript

A reader can see why:

- Cournot continuation is unique;
- backup choice is globally optimized over ([0,1]);
- clipping matters and the full clipped backup game is contractive;
- location choices admit a cutoff representation;
- endpoint interiority implies no probability clipping and (|B|<1);
- state-level surplus aggregates to the policy objective;
- the plant-attraction wedge arises from the local objective;
- planner monotonicity plus the policy domain implies the unique planner optimum;
- root isolation plus own-policy strict concavity implies a global local best response;
- the open-set extension needs the full diagonal FOC derivative and persistence of all
  strict continuation/globality margins.

### Delegated to exact computation

The manuscript delegates only objects whose printed expansion would add reader cost
without adding economic content:

- exact Bernstein coefficient lists;
- very large rational numerator/denominator expansions;
- exact root-isolation traces;
- generated finite exact-arithmetic payloads;
- formal proof-assistant kernel details.

For every delegated object, the manuscript states the mathematical target, domain, sign
or root property being certified, and the implication for the economic result.

## 6. Main-text necessity ledger

### CORE

- research question and policy conflict;
- protection, risk, location, backup, government-objective primitives;
- full timing and equilibrium concept;
- global clipped-backup logic;
- location cutoff/fixed-point logic;
- national/local policy objectives;
- marginal plant-attraction decomposition;
- headline theorem and exact witness;
- welfare accounting and social/private readiness wedge;
- theorem scope and constrained-planner interpretation;
- conclusion.

### HELPFUL

- exact Δ=0 benchmark;
- Figure 1 origin-marginal visualization;
- Table 1 channel decomposition;
- institutional interpretation and empirical implications;
- closest-literature comparison;
- diagnostic portability discussion.

### APPENDIX

- Bernstein method tutorial and coefficient logic;
- global planner and local-best-response lemmas;
- open-set persistence proof;
- exact product-substitutability cross-partial;
- fit-payoff robustness;
- numerical stress-test implementation details;
- formal-verification scope.

### DELETE

No material current item is classified DELETE. The prior v2.5 removals remain absent:
duplicated institutional motivation, redundant benchmark prose, giant exact fraction in
the empirical-prediction flow, and internal journal/workflow language.

## 7. Exhibit architecture

The current integrated manuscript has exactly **two** main-text exhibits.

### Exhibit 1 — Figure 1: origin marginal incentives

Question answered:
How do the local and coordinated origin marginals vary with product substitutability near
the canonical witness?

Why it remains:
The two root-isolated thresholds and their ordering are easier to understand visually than
from intervals alone.

Boundary:
The caption explicitly states that the curves are origin marginals, **not policy-equilibrium
levels**. The figure is generated from exact rational evaluations and uses non-color line
encoding.

Classification: **HELPFUL / CORE FOR INTERPRETATION**.

### Exhibit 2 — Table 1: marginal welfare channels

Question answered:
Why can the coordinated protection margin be negative even though direct engineering
reliability is positive?

Why it remains:
The table separates direct protection, endogenous readiness response, and net coordinated
and local margins in one object.

Boundary:
Values are exact derivatives converted to decimals, not finite-difference estimates.

Classification: **CORE**.

### Five-exhibit thought experiment

Only two main-text exhibits exist; both survive. There is no exhibit-count pressure and no
additional figure/table is required for completeness.

## 8. Introduction compression test

The Introduction exposes, in order:

1. the environmental/economic question;
2. the crowd-out mechanism and why cost savings alone do not establish inefficiency;
3. the exact headline result and constrained-planner scope;
4. the minimal game architecture;
5. the contribution relative to resilience and local-public-input theory;
6. the mechanism decomposition and Δ=0 benchmark;
7. the closest environmental prior art, including Kousky et al. (2006);
8. appraisal interpretation and limitations;
9. roadmap.

It does not introduce Lean, CI, Bernstein coefficient lists, repository stages, or other
production-process material.

**Introduction compression: PASS.**

## 9. Redundancy audit

Permitted repetitions have distinct reader functions:

- Abstract / Introduction: headline claim;
- Main Result: exact theorem and witness;
- Discussion: limitation and portability boundary;
- Conclusion: short answer to the research question.

The literature comparison is fuller in Related Literature than in the Introduction.
Institutional evidence is concentrated in Section 7. The Appendix does not repeat main-text
economic intuition except where needed to connect a proof step.

No material repetition currently warrants deletion.

## 10. Compression-without-damage audit

Compression has not removed:

- strategy domains or timing;
- conditional-independence law;
- government-incidence assumption;
- planner feasible policy set;
- global/corner handling for backup;
- location no-clipping logic;
- theorem quantifiers;
- distinction between existence and full policy-equilibrium uniqueness;
- welfare population/accounting;
- diagnostic-versus-theorem boundary;
- formal-verification boundary;
- prior-art limitations.

**Compression-without-damage: PASS.**

## 11. Stage-13 architecture verdict

**PASS — CURRENT V4 EXPOSITION ARCHITECTURE CERTIFIED.**

No manuscript rewrite is required to satisfy the Stage-13 exposition gate. Any later
change to theorem scope, proof-critical bridges, exhibit inventory, or section ordering
must rerun this architecture audit.
