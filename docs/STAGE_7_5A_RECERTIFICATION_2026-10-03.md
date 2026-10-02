# Stage 7.5A Re-Certification — Generality, Quantifiers, Portability, and Formal Scope

**Date:** 2026-10-03  
**Input:** Stage-6 re-certified candidate on `recert/v4-stage6-stage75a-2026-10-03`  
**Workflow:** Theory Paper Research Pipeline v2.5

## Verdict

**GO — GENERALITY / QUANTIFIER / PORTABILITY RE-CERTIFICATION PASS**

Headline classification remains:

**CONDITIONALLY PORTABLE**

This classification is retained with a narrower evidentiary interpretation than the
superseded 2026-09-24 certificate.

## 1. Canonical theorem scope

The exact theorem is:

> There exists a nonempty open set within the maintained symmetric baseline primitive
> family for which the coordinated protection-policy planner has unique optimum
> ((0,0)), while the decentralized jurisdictional game has a strictly positive symmetric
> Nash equilibrium.

The theorem does **not** assert:

- all-parameter overprovision;
- uniqueness of the full first-stage policy equilibrium correspondence;
- arbitrary risk technologies;
- arbitrary location-shock distributions;
- arbitrary backup technology;
- arbitrary product-market conduct;
- an unrestricted social first best;
- general empirical prevalence.

## 2. Quantifier / benchmark audit

| Claim | Certified scope | Classification |
|---|---|---|
| canonical planner optimum | unique global optimum on the certified policy square | PROVED |
| canonical positive symmetric local equilibrium | global unilateral best response at the exact root; existence of symmetric Nash equilibrium | PROVED |
| open-set persistence | nonempty neighborhood within maintained baseline family | PROVED analytically, outside Lean |
| marginal identity (M_L=M_S/4+2b\lambda_0) | symmetric origin under maintained incidence/hosting/cost structure | INSTITUTION-SPECIFIC |
| nonlinear-risk exercise | numerical diagnostic at fixed canonical non-risk primitives | NUMERICALLY SUPPORTED ONLY |
| logistic-location exercise | numerical diagnostic with matched symmetric density | NUMERICALLY SUPPORTED ONLY |
| general climate-protection overprovision | not claimed | REJECTED AS OVERSTATEMENT |

The planner is correctly described as a **protection-policy-constrained industrial-surplus
planner**. “First best” is not used for the headline benchmark.

## 3. Portability diagnostics — corrected evidentiary interpretation

### Alternative A: nonlinear risk

Diagnostic specification:

[
q(a)=q_0\exp(-a/q_0).
]

The construction matches both (q(0)=q_0) and (q'(0)=-1). Therefore equality of
the baseline and nonlinear-risk **origin marginal** is partly built into the diagnostic.
That equality is not independent evidence of portability.

What remains informative:

- the positive symmetric policy candidate moves materially away from the baseline root;
- continuation solves successfully on the tested domain;
- the planner's tested optimum remains zero;
- full-interval numerical unilateral searches find no profitable deviation against the
  reported candidate;
- off-origin responses differ from the linear-risk baseline.

**Classification:** SURVIVES AS A NONLINEAR OFF-ORIGIN DIAGNOSTIC.

### Alternative B: logistic location heterogeneity

Diagnostic specification:

centered logistic location-fit shocks with scale (H/2), chosen so that the density at
symmetric indifference equals the baseline uniform density.

That calibration implies the same local location-response derivative at the symmetric
origin. Because expected surplus is stationary in the location probability at the
symmetric point, the symmetric government FOC is structurally matched. Hence the nearly
identical symmetric policy root is **not independent evidence** of distributional
portability.

What remains informative:

- the location best-response map is nonlinear rather than affine;
- support is unbounded rather than bounded;
- tested off-diagonal continuations satisfy the numerical contraction checks;
- numerical unilateral deviations against the candidate are unprofitable on the tested
  search;
- the tested planner ranking remains zero.

**Classification:** SURVIVES AS AN OFF-DIAGONAL / CONTINUATION DIAGNOSTIC, NOT AS
INDEPENDENT ROOT REPLICATION.**

## 4. Why CONDITIONALLY PORTABLE is retained

The two alternatives change distinct primitives and were pre-specified before their
results were computed. Both require their affected continuation to be re-solved rather
than inserting altered primitives into the baseline closed form.

However, the strongest symmetric local comparisons were deliberately matched by
construction. The diagnostics therefore do **not** constitute two orthogonal independent
replications of the headline theorem.

The final classification remains `CONDITIONALLY PORTABLE` only in the following narrow
sense:

- the exact theorem is baseline-family-specific;
- the identified economic chain survives meaningful nonbaseline perturbations away from
  the matched local object;
- no tested alternative generates a counterexample to the policy ranking;
- no general theorem over the alternative function classes is claimed.

A reader should not interpret this as evidence that the theorem is “robust across
functional forms” without qualification.

## 5. Mechanism invariant

The smallest mechanism whose preservation matters is:

1. public protection lowers primary risk;
2. lower primary risk reduces private demand for costly geographic contingency readiness;
3. the induced readiness response can lower national industrial surplus enough to offset
   direct reliability gains and saved readiness cost;
4. unilateral protection attracts mobile primary production;
5. local hosting incentives can remain positive after the national protection margin turns
   negative.

The exact functional forms are not the claimed contribution.

## 6. Essential assumptions and current failure boundaries

Material baseline restrictions not relaxed by the diagnostics:

- quadratic backup cost;
- differentiated Cournot competition;
- conditional independence of backup success given primary failures;
- the baseline primary-failure correlation structure;
- equal one-half incidence of national market surplus in local objectives;
- state-independent hosting benefit;
- quadratic public-protection cost;
- simultaneous local policy choice;
- two jurisdictions / two firms.

Known failure/scope boundaries:

- sufficiently large omitted direct protection benefits can reverse the planner's origin
  marginal;
- different incidence/ownership/tax systems change the local-versus-national wedge;
- discrete/fixed-cost backup or correlated backup hazards require a new continuation;
- the diagnostics do not prove whole-domain globality for their alternative families.

## 7. Formal Verification Gate re-assessment

**FORMAL VERIFICATION PASS — PROOF-CRITICAL CORE / BOUNDED SCOPE**

Current Lean evidence is accepted with these explicit boundaries:

- Lean proves encoded algebraic and optimization implications from stated hypotheses;
- generated exact sign/certificate bridges remain explicit premises where documented;
- clipped-backup global uniqueness is proved analytically/computationally outside the
  final Lean theorem;
- open-set persistence is outside Lean;
- `native_decide` introduces native compiler/runtime trust for the relevant exact
  arithmetic checks;
- no `sorry`, `admit`, or project-specific custom axiom is accepted by CI.

The 2026-09-24 formal closure is historical evidence. The current repaired statement/scope
is governed by `formal/README.md`, `docs/FORMALIZATION_TARGET_MAP.md`, the v4
freeze, and the green post-repair CI.

## 8. Claim-scope ledger

| Object | Maximum wording | Prohibited stronger wording |
|---|---|---|
| headline theorem | nonempty open set in maintained symmetric baseline family | generic or universal overprovision |
| nonlinear-risk diagnostic | ranking survives stated numerical diagnostic | theorem for arbitrary decreasing risk functions |
| logistic diagnostic | tested continuation/deviation behavior survives matched-density logistic alternative | distribution-free theorem |
| public/private protection interaction | established parent mechanism used in new full game | first demonstration of crowd-out/complementarity |
| protection attracting investment | established parent mechanism | first demonstration of safe-development/location response |
| marginal (1/4) coefficient | exact under maintained incidence rule | general decentralization coefficient |
| Lean | proof-critical encoded core under explicit premises | complete formal proof of economic model/open set |

## 9. Stop rule

No portability claim was rescued by redesign after failure. Neither pre-specified
alternative overturns the mechanism. Further functional-form searching is **not
authorized as a pre-freeze rescue exercise**.

## 10. Stage 7.5A closure

- quantifier audit: PASS
- benchmark-definition audit: PASS
- portability wording: PASS after narrowing
- negative/constructed features disclosed: PASS
- formal-verification applicability: APPLICABLE
- formal-verification state: PASS / bounded proof-critical core
- author intellectual-contribution confirmation: required before Stage 8 and recorded
  separately
- routing: **GO → Stage 8 after author confirmation**
