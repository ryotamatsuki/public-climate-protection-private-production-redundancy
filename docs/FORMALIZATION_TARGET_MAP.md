# Formalization Target Map

Canonical manuscript/model SHA: `77f0c0705e3759b4997b3b17355f0063c02673e1`

This map is statement-faithful to the canonical manuscript. It separates:

- **A — Lean derived:** proved by the Lean kernel from stated premises.
- **B — maintained model assumption:** primitive assumptions of the economic model.
- **C — generated exact certificate:** exact Python/SymPy certificate data or the explicit semantic bridge connecting that data to the canonical economic expression.

A category-C fact is never described as category A merely because Lean uses it as a premise.

| ID | Formal target | A/B/C boundary | Status |
|---|---|---|---|
| T1 | Product-market identities, including `ProductMarket.delta_identity` | A: algebraic Cournot/monopoly identities and sign implications. | PASS |
| T2 | Four-state availability accounting | B: conditional independence of backup-success draws after primary failures. A: `m`, `z`, four state probabilities, sum-to-one and conditional nonnegativity implications. | PASS + ASSUMPTION |
| T3 | State-enumerated expected profit equals paper closed form | A: `Backup.expectedProfit_state_eq_closed`. | PASS |
| T4 | Backup FOC, strict global optimum, interior linear-system uniqueness | A: quadratic payoff identity, FOC implication, strict global optimum, linear-system uniqueness. C: canonical whole-policy-square denominator/readiness regularity certificate from `verify_global_certificate.py`. | PASS + GENERATED_CERTIFICATE |
| T5 | Strategic substitution; co-location `rC`; dispersed `rD`; symmetric FOC identities | A: `-(Delta*J)/k<0`, `rC` and `rD` formulas satisfy the manuscript FOCs. **No claim `rC < rD` is formalized or required.** The canonical witness can have `rC > rD`; this is not an analytic defect because the manuscript does not assert the opposite ordering. | PASS |
| T6 | Location no-clipping, contraction, fixed-point uniqueness | A: endpoint-interiority implies no clipping and `|B|<1`; asymmetric affine probability fixed points are excluded. C: canonical whole-policy-square endpoint probabilities, denominator sign, and equilibrium-probability interiority. | PASS + GENERATED_CERTIFICATE |
| T7 | Welfare state accounting | A: four-state surplus enumeration equals the manuscript closed form. | PASS |
| T8 | Marginal decomposition and Proposition-1 threshold logic | A: `ML = MS/4 + 2*b*lambda`, threshold equivalence, transparent-conflict implications. | PASS |
| T9 | Exact canonical witness arithmetic | A: `DualQ` reconstructs backup equilibrium, all four location profiles, firm profit, market surplus, location fixed point, expected surplus, common-policy derivative, unilateral derivative, and plant-attraction derivative; `MSModel`, `MLModel`, `lambdaModel` are therefore model-derived exact rationals. Checkpoint equalities and signs are kernel checked. | PASS |
| T10 | Actual mathlib Bernstein sign logic | A: univariate and tensor-product sign theorems use mathlib `bernstein_nonneg` and `bernstein.probability`; no abstract partition-of-unity premise replaces the actual basis. | PASS |
| T11 | Planner global optimum | C: generated exact Bernstein coefficient payload and semantic bridge to the canonical welfare partial derivatives. A: coefficient-sign implication, derivative negativity to coordinatewise `StrictAntiOn`, origin strict dominance, and unique global maximizer implication. | PASS + GENERATED_CERTIFICATE |
| T12 | Unique diagonal local-government FOC root | C: exact `alphaL`, `alphaU`, endpoint FOC values, degree-51 normalized derivative Bernstein payload, and the semantic bridge from the canonical FOC derivative to that payload. A: exact coefficient negativity check, actual Bernstein sign implication, `F'<0`, `StrictAntiOn`, continuity + endpoint sign change, and `∃! alpha ∈ (alphaL,alphaU), F alpha=0`. Python `len(roots)==1` is not imported as the Lean conclusion. | PASS + GENERATED_CERTIFICATE |
| T13 | Full-domain unique best response | C: full-own-domain second-derivative certificate for every rival action in the root interval and its bridge to the canonical `GA`. A: strict second derivative implies strict concavity; interior stationarity implies the stationary point is the unique global maximizer. | PASS + GENERATED_CERTIFICATE |
| T14 | Final canonical-witness theorem core | A: `TheoremCore.canonical_witness_from_generated_certificates` obtains `alpha` from T12 rather than accepting its existence as a theorem premise, proves `0<alpha<abar0`, applies T13 to both governments using symmetry, and combines this with T11 to conclude the planner's unique optimum is `(0,0)` and a strictly positive symmetric Nash equilibrium exists in the exact isolating interval. C inputs remain explicit certificate bridges. | PASS + GENERATED_CERTIFICATE |
| T15 | No-placeholder / custom-axiom / `#print axioms` audit | A/CI: fail-closed scans reject `sorry`, `admit`, and custom `axiom` declarations; `Main.lean` prints axioms for the proof-critical theorem inventory. CI run `36012426830` reached and passed the axiom-report step on the repaired formalization head. | PASS |
| T16 | Reproducible formal-verification environment and CI evidence | C/CI: deterministic certificate generation is executed twice and compared; Lean 4.32.1, mathlib commit `520045ab14e26149ee970e2e617ca04b09bde5d6`, and all transitive manifest revisions are pinned; no `lake update` occurs in CI; evidence artifacts record generated data, axiom report, provenance, and manifest. | PASS |

## Explicitly out of scope

The open-neighborhood persistence theorem (compactness/uniform margins/continuity/IFT continuation from the canonical witness) is **OUT_OF_SCOPE** for this Lean gate. The current formal result is the canonical-witness theorem core only. No document or badge may describe it as a Lean proof of the entire open-set persistence statement.

A measure-theoretic construction of the private Uniform location shock and a first-principles Lean re-expansion of every large generated rational-function numerator are also outside the current proof-critical scope. Their use is exposed through B/C boundaries above, not hidden.
