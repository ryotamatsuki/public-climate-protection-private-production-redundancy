# FORMAL_PROOF_OBLIGATIONS — v0.4.2
Status: Stage 0 completed as an INVENTORY, not as a proof; audit date 2026-11-14. No manuscript modification.

## Authoritative source and toolchain
- Paper: *Mutual Production Contracts and Spatial Differentiation under Supply Disruptions*, v0.4.2, 2026-11-12.
- Source ZIP SHA256: `ba125cf13a35217432577e95b04f7a77e6f1eadba5862f3ae8d1a884a95ae457`.
- PDF SHA256: `e356a07675daca6cdfd3f305ae77cd0f012ec8065167e6433a19af13c8e5b2d6`.
- Toolchain: `formal/lean-toolchain` Lean v4.32.1, pinned mathlib through `formal/lake-manifest.json`.
- Base audit ref: `rescue-hotelling-model-audit-2026-11-14` @ `8a3c6a0aeb11888e17abcc549119e2a929438f1f`. Existing CI run `43548053495` reports success; do not infer whole-model verification from this.
- All source page numbers below refer to the 27-page v0.4.2 PDF; LaTeX labels are canonical.

## Primitive assumptions and full extensive-form objects
| ID | LaTeX source | Required Lean object / obligation | Status |
|---|---|---|---|
| M01 | `02_model.tex`, consumers | Firm A/B identities, [0,1] physical/consumer space, uniform mass, feasible locations | UNFORMALIZED |
| M02 | `02_model.tex`, consumers | quadratic mismatch (t(x-y_i)^2), utility (v-p_i-t(x-y_i)^2) iff delivered, zero otherwise | PARTIAL; utility not fully linked to order choices |
| M03 | `02_model.tex`, consumers | advance orders, no ex-post brand switch, unit demand, external option, payment only on delivery | UNFORMALIZED |
| M04 | `02_model.tex`, eq:hub | ex-ante real hub cost (c(y_i-1/2)^2/2); zero marginal ordinary production cost | PARTIAL |
| M05 | `02_model.tex`, eq:technology | 2 dependent Bernoulli failures with marginal q and correlation (ho(d)=1-d); probability simplex and exact covariance/correlation formula | PARTIAL: simplex and marginals checked; correlation quotient not checked |
| M06 | `02_model.tex`, eq:technology | rescue conditional probability (s(d)=1-d), unconditional (a(q,d)=q(1-q)d(1-d)) | PARTIAL |
| M07 | `02_model.tex`, failures | physical losses (Lambda), production cost k, (V=Lambda-k>0), fixed F, spare capacity and interfirm enforceability | SEMANTIC assumptions not formalized as operational capacity constraints |
| M08 | `02_model.tex`, game | locations simultaneous → stochastic proposer → proposer offer/accept → simultaneous prices/orders → correlated failures/rescue → payoffs | UNFORMALIZED as extensive-form stochastic game |
| M09 | `02_model.tex`, game | pure SPNE for every price, contracting and location continuation including ties and coincident sites | UNFORMALIZED; reduced-game Nash is not SPNE |
| M10 | `02_model.tex`, benchmark | no-contract game shares all primitives except available agreement action | PARTIAL |

## Manuscript lemmas, propositions and corollaries (ALL numbered results)
| ID | PDF page | Label/LaTeX | Statement and dependencies | Closest existing Lean code | Gap |
|---|---|---|---|---|---|
| L1 | 5 | `lem:price`; `03_equilibrium.tex` eq:prices/eq:revenues | all distinct feasible sites, global equilibrium pricing, identical conditional prices across agreement/no-agreement, equal-site Bertrand p=0; M01–M06 | `RescueHotellingExtendedGame.price_competition_nash`, `RescueHotellingCoverage.candidate_prices_cover_all_consumers` | complete reservation/outside option, full allocation and coincident continuation missing |
| L2 | 5 | `lem:contract`; eq:baseline_payoff/eq:surplus/eq:reduced_payoff | S(d) formula, iff signing, ex ante continuation `N_i+max(0,S/2)`; L1,M06–M09 | `RescueHotellingBargaining.proposer_gain_attains_global_maximum`, `RescueHotellingCore.contract_surplus_split` | complete off-path strategic bargaining embedding missing |
| P1 | 6 | `prop:existence`; eq:BC/eq:contract_distance/eq:Rconditions/eq:plant_locations | exists pure SPNE under R0–R2, candidate strictly profitable, `0<dC<1/2`, open nonempty parameter region; L1/L2, R0/R1/R2, open-box | `RescueHotellingReducedNash.globally_symmetric_reduced_location_nash`, `RescueHotellingCore.quadratic_closed_form_root` | full SPNE, parameter-box certification in Lean, root and all assumptions bridged |
| P2 | 7 | `prop:baseline`; eq:d0 | no-contract symmetric pure SPNE under R0, d0 formula and price; L1, no-contract crossing | `RescueHotellingCore.no_contract_distance_solves_FOC`, `RescueHotellingLocation.no_contract_same_side_global_optimum` | crossing no-contract and extensive-form continuation |
| P3 | 7 | `prop:dispersion`; eq:main_order | selected dC>d0 and pC>p0; P1/P2 | `RescueHotellingCore.contract_distance_gt_no_contract` | connect formula solution and exact param premises |
| P4 | 8–9 | `prop:risk_reversal`; eq:Gq/eq:Dq/eq:risk_derivatives/eq:risk_witness | implicit derivative sign, `q∈[1/20,3/20]` R0–R2, strictly concave branch, unique q*, increasing gap, open neighborhoods; P1/P2/P3 | `RescueHotellingModelCheck.no_contract_distance_strictly_decreases`, core algebra | formal IFT, derivative continuity, uniform exact rational interval certificates, open-set proof |
| C1 | 9 | `cor:value`; eq:V_derivative | positive dC/dV, pC/dV at regular contracted SPNE | `RescueHotellingCore.contract_FOC_decomposition` | derivative/IFT proof with branch integration |
| C2 | 9 | `cor:general`; eq:Gd_general/eq:tech_condition | C2 rescue technology comparative static with C² nonnegative a; log derivative condition | none directly | derivative, sign, local branch hypotheses |
| P5 | 10 | `prop:welfare`; eq:mismatch_general/eq:M/eq:W0/eq:WC/eq:welfare_contract_gain | exact mismatch integral and planner midpoint, regime-specific W and difference | `RescueHotellingCore.mismatch_midpoint_comparison`, `welfare_contract_increment` | integral and explicit welfare accounting derived from primitives |
| P6 | 11 | `prop:no_welfare`; eq:dSW0 | globally unique constrained no-contract welfare optimum and positive private-social distance gap | `RescueHotellingCore.no_contract_excessive_distance` | global maximizer proof (not mere algebra) |
| P7 | 11 | `prop:welfare_cutoff`; eq:vcrit/eq:Wprime/eq:cutoff_identity | strictly concave W_C, unique dSW∈(0,1/2), sign classification by vcrit | `RescueHotellingCore.welfare_cutoff_at_private_FOC` | global maximum and sign proof on full interval |
| C3 | 12 | `cor:fixed_private` | q=1/20,t=1,c=5,V=1/5,F=1/1000,Λ=3/2; 8<vcrit<9, v=4 vs 10 reversals | no Lean exact witness | rational interval certificate |
| P8 | 12 | `prop:policy`; eq:policy_transfer/eq:ceff | implements dC^SW as SPNE if R0–R2 with ceff; numerical subsidy and tax witnesses | no Lean policy theorem | positivity ceff, recertify R0–R2 and global SPNE, precise finance assumptions |

## Additional unnumbered claims that also require certificates
| ID | Source | Claim | Status |
|---|---|---|---|
| A01 | `A_proofs.tex` appendices A/B | global price best responses including demand saturation; full same-side, refusal, cross-rival incl. tie, no-contract crossing | PARTIAL |
| A02 | `03_equilibrium.tex` eq:open_box; `B_certificates.tex` | ALL points in 5-dimensional open rectangle satisfy root bracket and R0–R2, dC>d0 | EXTERNAL rational verifier only |
| A03 | `C_risk_reversal_proof.tex` | 800 rational q-cells: signs `Gd>0`, R0/R1/R2, dC''<0, (dC-d0)'>0 and endpoint signs | EXTERNAL rational verifier only |
| A04 | `B_certificates.tex` welfare/policy | all three welfare witnesses, vcrit bracket and ceff subsidy/tax exact rational bounds | EXTERNAL verifier only |
| A05 | `06_policy_robustness.tex`, `D_imperfect_corr_proof.tex` | rho0=9/10, 400 rational cells, new R2rho envelope, SPNE, d''<0, turning point uniqueness and gap derivative | EXTERNAL verifier only |
| A06 | `A_proofs.tex`; appendix rho | differentiability/IFT/strict open-neighborhood inference from uniform margins | UNFORMALIZED |
| A07 | release / figures | consistency of all displayed numerical values with certified exact enclosures | NOT YET IN LEAN |

## Stage dependency graph
M01–M09 → L1,L2 → P1, P2 → P3 → P4,C1,C2; M01–M09,L1 → P5 → P6,P7 → C3,P8. Separate appendix obligations A01–A07 are proof dependencies, NOT optional exhibits.

## Completion criterion
A direct Lean theorem for every row above must match the actual manuscript quantifiers, domains, assumptions and conclusions, with kernel-verified certificates for finite computations. `FULL FORMAL VERIFICATION: PASS` is FORBIDDEN until complete. The inventory itself is `Stage 0: PASS` only.
