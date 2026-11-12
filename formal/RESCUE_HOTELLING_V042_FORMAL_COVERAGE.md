# Rescue Hotelling v0.4.2 — Lean extension certification and coverage ledger

**Date:** 2026-11-12 (JST)
**Target manuscript:** `Mutual Production Contracts and Spatial Differentiation under Supply Disruptions`, v0.4.2.
**Source:** `formal/RescueHotellingCore.lean` on the dedicated draft PR branch.
**Existing proof source provenance:** original kernel record commit `01d9f681856bb13e70ef2d9beae013833953fcf3`.
**Lean/toolchain:** `leanprover/lean4:v4.32.1`, pinned mathlib `v4.32.1` at `520045ab14e26149ee970e2e617ca04b09bde5d6`.

## Completed checks

- Original kernel-checked declarations: **19**.
- New algebraic / conditional global-deviation / risk-sign declarations: **19**.
- Total theorem declarations in the proof source: **38**.
- Dedicated CI run: https://github.com/ryotamatsuki/public-climate-protection-private-production-redundancy/actions/runs/43137617363
- Job `rescue-hotelling-kernel`: **SUCCESS** (kernel compile, pinned toolchain, placeholder scan, axiom report).
- Axiom report contains only standard Lean/Mathlib dependencies `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx` on the audited headline claims.
- The manuscript PDF, mathematical equations, economic model, and Python interval certificates were not modified by this Lean PR.

## Exact proof-to-claim mapping

| Manuscript target | Added Lean theorem(s) | What the kernel checks | What remains an economic/analytic premise |
|---|---|---|---|
| Appendix B, R1 | `R1_excludes_contract_refusal` | From a strong-concavity disagreement-payoff envelope and `H>g²/(2c)`, every same-side refusal continuation has strictly lower payoff | The curvature-envelope property of the actual Hotelling disagreement payoff |
| Appendix B, R2 | `baseline_rescue_upper_linear`, `baseline_contract_option_upper`, `baseline_crossing_payoff_envelope`, `quadratic_crossing_upper_bound`, `R2_excludes_crossing_from_primitive_bounds` | Baseline option `A u(1-u)`, conditional revenue upper bounds and quadratic hub costs imply the R2 global exclusion for all feasible crossing locations | Derivation of the price-subgame revenue bounds from the game, and completeness of the location deviation partition |
| Appendix H, R2rho | `rhoRescue_upper_affine`, `rho_contract_option_upper`, `rho_crossing_payoff_envelope`, `R2rho_excludes_crossing_from_primitive_bounds` | The positive intercept `A e V` is retained, the rescue option is upper-bounded, the crossing quadratic is maximized on the nonnegative ray, and R2rho excludes the deviations | Economic interpretation of the rescue distribution, the conditional-revenue bounds and complete game coverage |
| Proposition 4 | `contracted_G_risk_decomposition`, `contracted_G_q_increment`, `contracted_G_d_increment`, `positive_contract_risk_response`, `no_contract_risk_slope_negative`, `risk_response_reversal` | Exact polynomial increments establish the numerator `D` and denominator `G_d`; from `G_d d'_C=D`, `G_d>0`, `D>0`, show `d'_C>0>d'_0` | Analytic implicit-function theorem producing the derivative relation; SPNE existence and selection; entire interval and uniqueness-of-turnover claims |

The Lean declaration named `R2rho_from_paper_envelope` also exposes an intermediate conditional step; the later `R2rho_excludes_crossing_from_primitive_bounds` closes the algebraic bridge from option and conditional sales bounds. The same holds for the baseline R2.

## Deliberately unformalized results — do not claim full kernel proof

1. Complete extensive-form game (price subgame, random proposer, accepting/rejecting strategies in every history).
2. Derivation of all uniform curvature inequalities from the original consumer-demand formulas.
3. All R0–R2 feasibility and all equilibrium parameter and root-isolation assumptions.
4. The analytic implicit-function-theorem proof of the identity `G_d d'_C = D` for an endogenous equilibrium path.
5. Strict concavity in risk, unique turning point, the 800-cell and 400-cell exact-rational continuous-interval certificates: still certified by the separate reproducible Python Fraction verification and mathematical reasoning, *not* by Lean.
6. Welfare/implementation claims beyond the original algebraic Lean subset.
7. Claims of all-SPNE uniqueness, arbitrary rescue technologies, or generic geographic applicability.

## Reviewer-verifiability boundary

The Lean extension verifies concrete algebraic steps in a paper-accurate model-to-envelope chain; it is **not** a formal proof of the complete SPNE or an independent assessment of economic novelty. A specialist reader should combine the manuscript's analytic location/price derivations with the kernel-checkable envelope and sign implications and the exact-rational risk-interval verification.

## Reproduce

```sh
cd formal
lake exe cache get
lake env lean RescueHotellingCore.lean
```

Do not merge this draft PR to the unrelated project main branch without an explicit author decision. If adopted as an Online Resource for the NETS submission, export this frozen source, toolchain, lake manifest and CI log as a versioned independent formal supplement. The author must review the claim-to-proof mapping and approve final submission statements.
