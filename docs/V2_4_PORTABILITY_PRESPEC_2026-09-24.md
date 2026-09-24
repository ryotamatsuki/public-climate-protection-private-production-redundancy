# v2.4 Portability / Falsification Plan — Pre-Specification

Date frozen: 2026-09-24

Status: **PRE-SPECIFIED BEFORE COMPUTATION**

This file freezes the diagnostic alternatives, equilibrium concepts, and pass/fail criteria before any v2.4 alternative-model result is computed. The exercise is journal-neutral and does not authorize result-driven redesign.

## Headline claim under attack

Baseline headline theorem:

> Within the maintained symmetric primitive family, a nonempty open set exists in which the coordinated planner chooses zero additional local protection while decentralized jurisdictions have a strictly positive symmetric protection equilibrium.

The associated mechanism invariant is:

1. public protection lowers primary disruption risk;
2. safer primary production reduces firms' privately chosen geographic backup readiness;
3. this endogenous private response can make the national marginal value of additional protection negative;
4. a unilateral local protection increase still attracts mobile primary production;
5. the attraction rent can keep the local marginal incentive positive after the national marginal value has turned negative.

The exact baseline closed forms, rational witness, and Bernstein certificates are **not** themselves portability invariants.

## Baseline assumptions most plausibly carrying the result

- linear risk technology (q(a)=q_0-a);
- quadratic readiness cost;
- differentiated-Cournot disaster-state rents;
- conditional independence of backup success given primary failures;
- Uniform[-H,H] private location-fit shocks, which make the location best response affine;
- equal one-half incidence of national market surplus across jurisdictions;
- quadratic public-protection cost;
- simultaneous local-government policy choice.

The first and fifth assumptions are selected for the two orthogonal diagnostic attacks below. They directly affect, respectively, policy curvature and the location-equilibrium mapping.

## Alternative A — nonlinear public-protection technology

### Frozen primitives

Replace only

[
q(a)=q_0-a
]

by

[
q_A(a)=q_0exp(-a/q_0).
]

All other primitives, timing, strategy sets, payoff definitions, and the canonical numerical parameter vector remain unchanged.

This alternative satisfies

[
q_A(0)=q_0,qquad q_A'(0)=-1,qquad q_A''(a)>0,
]

so it matches the baseline risk level and first-order protection effectiveness at the origin while introducing diminishing marginal risk reduction away from the origin.

### Credibility rationale

Physical protection commonly has diminishing marginal effectiveness. This attack changes a result-driving technology rather than a cosmetic normalization while preserving the same economic interpretation of protection.

### Re-solution requirement

The full downstream backup and location continuation must be re-solved at each policy profile using the alternative risk function. Baseline policy derivatives or exact rational certificates may not be reused outside their derivation domain.

### Ex ante survival criterion

Alternative A counts as a **survival** of the headline mechanism at the canonical parameter vector only if all of the following hold in an independent numerical/global diagnostic:

1. every tested admissible policy profile has a valid unique interior backup continuation and unique interior location continuation;
2. the planner's global numerical optimum over ([0,ar a]^2) is ((0,0)), up to stated numerical tolerance;
3. a strictly positive symmetric local-government Nash fixed point exists in ((0,ar a));
4. a dense finite-deviation audit finds no profitable unilateral policy deviation at that fixed point beyond tolerance;
5. finite-difference origin derivatives satisfy (M_S<0<M_L).

Failure of any item is recorded as a portability failure; the alternative is not redesigned.

## Alternative B — logistic private location heterogeneity

### Frozen primitives

Retain the baseline linear risk technology and all other primitives, but replace

[
arepsilon_isim U[-H,H]
]

with a centered logistic location-fit shock having scale

[
s_L=H/2.
]

The scale is chosen ex ante so that the logistic density at zero,

[
f_L(0)=1/(4s_L),
]

equals the baseline uniform density (1/(2H)). Thus the alternative matches the local density at the symmetric indifference point but removes the affine cutoff-probability mapping and bounded-support assumption.

For deterministic location advantage (D(p)), the choice probability is re-derived as

[
BR_L(p)=rac{1}{1+exp[-D(p)/s_L]}.
]

### Credibility rationale

Smooth unbounded location-fit heterogeneity is standard in discrete choice. The test directly attacks whether the headline result depends on Uniform[-H,H] and the affine contraction structure.

### Re-solution requirement

At every policy profile the nonlinear fixed-point equation (p=BR_L(p)) must be solved independently. Root multiplicity on ([0,1]) must be checked rather than assuming the baseline unique affine fixed point.

### Ex ante survival criterion

Alternative B counts as a **survival** at the canonical parameter vector only if:

1. the nonlinear location equation has exactly one root on ((0,1)) at every tested admissible policy profile;
2. backup continuations remain valid and interior;
3. the planner's global numerical optimum over ([0,ar a]^2) is ((0,0)), up to tolerance;
4. a strictly positive symmetric local-government Nash fixed point exists;
5. a dense unilateral-deviation audit supports that fixed point as a global best response;
6. finite-difference origin derivatives satisfy (M_S<0<M_L).

Failure is preserved and does not trigger a favorable distribution search.

## Numerical evidence standard

These diagnostic alternatives are **falsification/portability evidence, not new theorems**. The baseline theorem remains the exact certified result. The portability script must:

- independently compute continuation payoffs from the changed primitives;
- use dense policy grids plus multistart continuous optimization for the planner;
- enumerate all nonlinear location roots for Alternative B on a fine bracket grid;
- use global one-dimensional best-response optimization and dense finite-deviation checks for the local-government equilibrium;
- record minimum/maximum continuation probabilities and readiness;
- record any unresolved or multiple-equilibrium profile as a failure, not silently discard it;
- emit a deterministic machine-readable result artifact.

## Classification rule frozen before computation

- If both orthogonal alternatives satisfy their survival criteria, the headline mechanism may be classified at most **CONDITIONALLY PORTABLE**, because exact global proof remains baseline-specific.
- If one survives and one fails, classify the headline result **CONDITIONALLY PORTABLE** only if a clear sufficient-condition boundary explains the failure; otherwise **MODEL-SPECIFIC**.
- If both fail and no abstract sufficient-condition statement survives, apply the v2.4 stop rule and classify **MODEL-SPECIFIC**.
- A failure of the baseline theorem inside its stated domain would be **FALSIFIED** and would reopen an earlier analytic stage.
- No alternative outcome may be used to change these criteria retroactively.

## Formal-verification state

The baseline proof-critical Formal Verification Gate is already **PASS / CLOSED**. These diagnostic alternatives are not incorporated into the formal theorem unless a later, separately authorized research rollback makes an alternative canonical.
