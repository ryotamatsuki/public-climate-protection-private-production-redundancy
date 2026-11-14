# THEOREM_CORRESPONDENCE_MATRIX — v0.4.2 (Stage 0)
Audit date: 2026-11-14. All existing 75 statements compiled in previous CI, run 43548053495. **The table documents correspondence, not proof completeness.** No manuscript edits.

Legend: **A** = exact substatement algebra, **C** = conditional narrower conclusion, **X** = unformalized required proof, **E** = external exact-rational Python certificate only.

| Paper item | Lean theorem(s) already present | Correspondence | Exact missing obligation |
|---|---|---|---|
| Lemma 1: price equilibrium | ModelCheck.price_left_reaction / price_right_reaction; ExtendedGame.price_competition_nash; Coverage.candidate_prices_cover_all_consumers | C | arbitrary histories with reservation demand and no external-option profitable deviation; equal-site Bertrand continuation |
| Lemma 2: voluntary contract | Core.contract_surplus_split; ModelCheck.bilateral_transfer_feasible_iff; Bargaining.proposer_gain_attains_global_maximum | C | joint surplus derived from full stochastic payoff and unique prescribed response on each history, proposer lottery expectation |
| Prop 1: contracted SPNE | Core.quadratic_closed_form_root; Location.agreement_same_side_global_optimum; Refusal.R1_rules_out_every_same_side_refusal; Crossing.R2_rules_out_all_crossing_deviations; ReducedNash.globally_symmetric_reduced_location_nash | C | full extensive-form strategy profile/SPNE predicate and proof; R0–R2 certificate over an open parameter box |
| Prop 2: no-contract SPNE | Core.no_contract_distance_solves_FOC/no_contract_distance_lt_half; Location.no_contract_same_side_global_optimum | C | no-contract cross-rival deviation, price subgames, full SPNE |
| Prop 3: dispersion | Core.contract_distance_gt_no_contract; contractMarginal_pos | C | linkage to unique positive root and all parameter restrictions in source |
| Prop 4: risk reversal | ModelCheck.no_contract_distance_strictly_decreases | A / E | IFT, strict concavity, 800-cell Lean interval certificate, open neighborhood, selected SPNE bridge |
| Cor 1: dC/dV | Core.contract_FOC_decomposition | X | Lean differentiability/IFT and sign |
| Cor 2: generalized technology | none | X | differentiable a, rho, s; log-derivative and local result |
| Prop 5: welfare functions | Core.mismatch_midpoint_comparison/welfare_contract_increment | A / X | true integral and planner social-accounting derivation |
| Prop 6: excessive d0 | Core.no_contract_excessive_distance | A / X | global uniqueness of planner optimizer |
| Prop 7: social threshold | Core.welfare_cutoff_at_private_FOC/welfare_slope_sign_above_cutoff | A / X | strict curvature, unique global optimizer, all sign cases |
| Cor 3: valuation witness | none | E | exact vcrit interval certificate `8 < vcrit < 9` |
| Prop 8: policy implementation | none | E / X | ceff algebra and full instrument induced continuation and R0–R2 witness |
| Imperfect correlation (unnumbered) | ExtendedGame.joint_failures_nonnegative (basic distribution) | E / X | rho-specific rescue, crossing, 400-cell exact certificate, strict turning point |
| Open box/welfare/risk certs | external Python `verification/*.py` | E | Lean checks of certificates or fully analytic rational bounds |

## Preventing statement laundering
- `RescueHotellingReducedNash.globally_symmetric_reduced_location_nash` quantifies over deviations in a *reduced payoff function*, not all contingent strategies/information sets. It is NOT a formal SPNE proof.
- `RescueHotellingCore.quadratic_closed_form_root` proves a conditional identity, not existence of a root in the model's admissible parameter domain.
- `RescueHotellingCore.welfare_slope_sign_above_cutoff` proves a conditional sign, not uniqueness of a global planner maximizer.
- `RescueHotellingExtendedGame.price_competition_nash` uses clipped relative-share demand and common positive delivery probability; off-path customer reservation demand needs a separate upper-envelope lemma.
- The paper treats strictly positive, unbounded transferable payments. A contract decision at S=0 must be consistent with the responder's acceptance-at-indifference rule.
- `#print axioms` checks actual dependencies and absence of `sorryAx`; successful typechecking alone does NOT establish fidelity to manuscript model.
- The 800-/400-cell interval claims must verify continuum coverage; discrete sampling or reported Python terminal messages are not formal Lean proofs.

## Independent check requirement
Before completion, create the converse audit: every Lean assumption must be traceable to a declared manuscript primitive or theorem-specific premise. If not traceable, report a theorem **gap** and do not silently enlarge the hypothesis set.

## Stage 0 follow-up: audited additional theorems (2026-11-14)
| Paper obligation | New Lean theorem | Scope of verified contribution | Remaining gap |
|---|---|---|---|
| Correlated failures and rescue delivery (Model M05/M06) | `RescueHotellingDelivery.totalProbability_eq_one`, `linear_geography_delivered_probability`, `failure_correlation_exact`, `total_contract_surplus_for_linear_geography` | exact six-outcome probability construction, common delivery factor, covariance/correlation, and identity for joint incremental surplus | complete payoff derived from consumers' actual order mass and stochastic terminal utility |
| P2 no-contract location | `RescueHotellingNoContractGlobal.noContractGlobalBestResponse` | full [0,1] unilateral-location deviations in reduced game, incl. crossing and same-side, under explicit cost/FOC assumptions | off-path extensive-form SPNE and root/hypothesis linkage |
| P1 contracted candidate root | `RescueHotellingRoot.closed_form_unique_admissible_root` | R0a/R0b imply positive unique interior root of stationarity quadratic | contract participation R1/R2 for stated open box, plus full SPNE |
| Cor 1 rescue value | `RescueHotellingValue.higher_rescue_value_increases_selected_root` | strict root ordering as V rises, conditional on regular roots | derivative/IFT statement from manuscript |
| P6 constrained no-contract welfare | `RescueHotellingWelfareGlobal.no_contract_planner_global_unique` | GLOBAL, UNIQUE maximizer of the full no-contract welfare polynomial | tie to full integral and equilibrium allocation, and rest of social-analysis results |
| Extensive-form game objects | `RescueHotellingHistories.Primitives`, `Locations`, `PureStrategyProfile` | typed primitives, histories and contingent strategic action spaces | probability law of full histories, payoff integrals, formal SPNE predicate and theorem |

**No theorem in this update is designated FULL SPNE.** The above are exact scoped sub-results only.
