# v2.4 Contribution Robustness Certificate — 2026-09-24

## Executive verdict

**GO — GENERALITY / QUANTIFIER / PORTABILITY CERTIFICATION PASS**

**v2.4 PORTABILITY / FALSIFICATION RETROFIT CLOSED**

The headline Protection–Attraction Conflict survives both pre-specified, orthogonal diagnostic alternatives at the canonical parameter vector. The result is therefore classified **CONDITIONALLY PORTABLE**, not fully portable: the exact global theorem and open-set certificate remain tied to the maintained baseline primitive family, while the alternative specifications provide independent numerical falsification evidence rather than new general theorems.

The baseline Formal Verification Gate remains **FORMAL VERIFICATION PASS / CLOSED**. No theorem statement was changed in this retrofit.

## 1. Frozen pre-specification

The diagnostic alternatives and success/failure criteria were committed before computation in docs/V2_4_PORTABILITY_PRESPEC_2026-09-24.md at commit a12ec09209a31faefd3917cbcec42344a529428e.

No alternative was chosen or redesigned after observing results.

## 2. Headline claim H1 — global Protection–Attraction Conflict

Canonical scope: within the maintained symmetric baseline primitive family, there exists a nonempty open set for which the coordinated planner's global optimum is zero additional protection while the decentralized policy game has a strictly positive symmetric Nash equilibrium. At the canonical rational witness, the planner optimum is uniquely (0,0), the positive symmetric equilibrium is globally best-response certified, and downstream continuations are unique and interior over the admissible policy domain.

Formal scope: this is an existence result for a nonempty open set, not a universal result over all primitives or microfoundations.

Mechanism invariant: protection lowers primary disruption risk; lower risk reduces costly private geographic redundancy; the private response can turn the national marginal value negative; unilateral protection attracts mobile primary production; and the attraction rent can keep the local marginal incentive positive after the national marginal value becomes negative.

### Alternative A — nonlinear protection technology

Frozen alternative: q(a)=q0 exp(-a/q0). Only the risk technology changes. It matches q(0)=q0 and q'(0)=-1 but has diminishing marginal risk reduction.

Re-solution artifacts: scripts/verify_portability_v24.py and docs/v2_4_portability_results.json.

Results: continuation failures 0; location-probability range approximately [0.43807, 0.56193]; backup-readiness range approximately [0.67381, 0.90847]; maximum tested location-contraction bound approximately 0.22590 < 1; planner grid maximum (0,0); all multistart planner optimizations return (0,0); positive symmetric local-policy fixed point 0.0104107516; dense unilateral-deviation maximum minus equilibrium payoff approximately -1.99e-11; origin diagnostic MS approximately -0.0064850 < 0 < ML approximately 0.0019309.

**Alternative-A classification: SURVIVES.** The local equilibrium moves materially relative to baseline, so this is not merely a relabeling of the baseline policy variable.

### Alternative B — logistic location heterogeneity

Frozen alternative: centered Logistic(0,sL) with sL=H/2. The scale was fixed ex ante so that density at the symmetric indifference point equals the baseline uniform density. The location best response is re-derived as a nonlinear logit map rather than the baseline affine cutoff.

Results: continuation failures 0; location-probability range approximately [0.42101, 0.57899]; backup-readiness range approximately [0.64498, 0.90847]; maximum tested global logit contraction bound approximately 0.24572 < 1; planner grid maximum (0,0); all multistart planner optimizations return (0,0); positive symmetric local-policy fixed point 0.0230196830; dense unilateral-deviation maximum minus equilibrium payoff approximately -2.87e-11; origin diagnostic MS approximately -0.0064850 < 0 < ML approximately 0.0019309.

**Alternative-B classification: SURVIVES.** The location game is nonlinear and the shock support is unbounded, so the baseline Uniform[-H,H] cutoff formula is not reused outside its derivation domain.

### H1 final classification

**CONDITIONALLY PORTABLE**

Reason: two pre-specified, economically meaningful, orthogonal alternatives preserve the headline ranking under independent re-solution, but exact global proof and open-set persistence remain baseline-specific. Numerical diagnostic survival does not license a universal theorem over risk technologies or heterogeneity distributions.

Maximum defensible wording: the exact global theorem is established for the maintained baseline primitive family; pre-specified diagnostic re-solutions under a decreasing nonlinear risk technology and logistic location heterogeneity preserve the planner-zero / local-positive ranking at the canonical primitives, supporting conditional portability of the mechanism.

Prohibited stronger wording: the theorem holds for any decreasing protection technology; the result is distribution-free; the result is generic across location heterogeneity distributions; the alternative models are formally proved; the open-set theorem has been established outside the baseline primitive family.

Stop-rule status: **NOT TRIGGERED**. Both pre-specified attacks survive; no rescue redesign was attempted.

Rollback authorization: **NONE**.

## 3. Claim H2 — public protection crowds out private geographic readiness

The nonlinear-risk diagnostic preserves the same economic channel. Final classification: **CONDITIONALLY PORTABLE**. Essential condition: the private backup optimum remains interior/regular and equilibrium readiness increases with primary risk over the relevant region. This does not establish portability to fixed-cost/discrete backup technologies or alternative backup-success dependence.

## 4. Claim H3 — plant-attraction response under private location heterogeneity

The logistic diagnostic re-solves the location stage and preserves the relevant response with a unique contraction-certified tested continuation. Final classification: **CONDITIONALLY PORTABLE**. Essential conditions include monotone choice probability in deterministic location advantage and sufficiently weak strategic feedback for uniqueness.

## 5. Claim H4 — marginal decomposition

The exact identity ML = MS/4 + 2 b lambda0 follows from the maintained government objective, one-half incidence of national market surplus, symmetry, and zero marginal public cost at the origin.

Final classification: **INSTITUTION-SPECIFIC** for the exact 1/4 coefficient. The broader idea that local marginal incentives combine an internalized share of national surplus with a plant-attraction rent extends more broadly, but the coefficient changes with incidence and objective structure.

## 6. Assumption-dependence and current boundary

- Linear risk technology: changed in Alternative A and survived; linearity is not essential to the diagnostic mechanism.
- Uniform bounded location shock: changed in Alternative B and survived; the affine/uniform form is not essential to the diagnostic mechanism.
- Quadratic backup cost: not changed; remains a material baseline restriction.
- Cournot product competition: not changed; remains a material baseline restriction.
- Conditional independence of backup success: not changed; substantive baseline institution.
- Equal one-half surplus incidence: not changed; exact marginal coefficient is institution-specific.
- Quadratic public cost: retained; baseline restriction including zero marginal cost at origin.
- Simultaneous policy choice: retained; institutional timing restriction.

## 7. Welfare / benchmark scope

The paper compares decentralized policy with the coordinated planner defined in the manuscript. It does not claim an unrestricted social first best over every production architecture or policy instrument. The benchmark is the coordinated planner within the model's feasible policy and firm-response structure.

## 8. Evidence ledger

- exact baseline global theorem and certificates: existing Stage 14 and formal-verification artifacts
- Formal Verification Gate closure: docs/FORMAL_VERIFICATION_GATE_CLOSURE_2026-09-24.md
- v2.2 theorem-absorption audit: docs/V2_2_STRUCTURAL_ABSORPTION_AUDIT_2026-09-24.md
- v2.4 pre-specification: docs/V2_4_PORTABILITY_PRESPEC_2026-09-24.md
- v2.4 executable diagnostic: scripts/verify_portability_v24.py
- v2.4 machine-readable results: docs/v2_4_portability_results.json
- manuscript scope repairs: paper/sections/02_model.tex and paper/sections/09_discussion.tex

## 9. Formal Verification Gate status

**FORMAL VERIFICATION PASS / CLOSED**

The v2.4 diagnostics do not alter the canonical theorem or formal statement. They are explicitly noncanonical falsification tests. No new Lean theorem is claimed for the alternatives. Repository-wide Lean CI remains a regression guard.

## 10. Claim-scope regression rule

Reopen Stage 7.5A if future manuscript wording promotes diagnostic survival to a universal theorem, claims arbitrary decreasing risk technologies, claims distribution-free location results, changes an untouched material assumption while retaining the same portability classification without a new test, or makes either diagnostic alternative part of the canonical theorem.

## 11. Closure verdict

- journal-neutrality: **PASS**
- pre-specification before computation: **PASS**
- Alternative A independent re-solution: **PASS / SURVIVES**
- Alternative B independent re-solution: **PASS / SURVIVES**
- stop rule: **NOT TRIGGERED**
- headline classification: **CONDITIONALLY PORTABLE**
- exact marginal 1/4 identity: **INSTITUTION-SPECIFIC**
- manuscript scope alignment: **PASS after wording repair**
- Formal Verification state: **PASS / CLOSED**
- v2.4 final verdict: **GO — GENERALITY / QUANTIFIER / PORTABILITY CERTIFICATION PASS**
- routing: **v2.4 CLOSED; proceed to v2.5 exposition audit**