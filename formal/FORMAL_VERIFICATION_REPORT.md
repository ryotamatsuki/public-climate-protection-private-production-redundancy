# Formal verification report — Hotelling v0.4.2
Updated: 2026-11-14.

**FINAL RESEARCH VERDICT: PARTIAL FORMAL VERIFICATION (NOT FULL PASS).**

## 1. Source and provenance
Manuscript v0.4.2 (2026-11-12), LaTeX ZIP SHA256 `ba125cf13a35217432577e95b04f7a77e6f1eadba5862f3ae8d1a884a95ae457`, PDF SHA256 `e356a07675daca6cdfd3f305ae77cd0f012ec8065167e6433a19af13c8e5b2d6`.

Original formal CI run: `43548053495` (75 declarations), base commit `8a3c6a0aeb11888e17abcc549119e2a929438f1f`.
New branch: `hotelling-full-formal-verification-2026-11-14`.

GitHub compare against the base shows changed paths exclusively in `formal/` and `.github/workflows/`; no paper/LaTeX/PDF changes.

## 2. Stage status
| Stage | Actual result | What is not yet proved |
|---|---|---|
| 0 Proof obligations and complete numbered-result mapping | **PASS as an inventory**: 2 lemmas, 8 propositions, 3 corollaries, plus unnumbered rational certificates. | Scientific correctness of all results not established by inventory. |
| 1 Extensive game | **PARTIAL**: typed location, offer, response, pricing, order, stochastic outcome and pure contingent strategies in `RescueHotellingHistories.lean`. | Complete payoff/measure/information-set semantics and SPNE definition/constructive existence. |
| 2 Prices | **PARTIAL, previously verified**: clipped relative-share demand price Nash, candidate full-coverage bounds. | All reservation-demand and coincident-location continuations bound into the extensive-form game. |
| 3 Failure and bargaining | **SUBSTANTIAL PARTIAL**: six correlated failure/rescue outcomes, sum-to-one, nonnegative weights, equal bilateral delivery probabilities, correlation formula, joint incremental gains. Original bargaining best responses already compiled. | A single exact stochastic extensive-game payoff and strategy integration. |
| 4 Global locations, SPNE | **SUBSTANTIAL PARTIAL**: contracted reduced-game global Nash conditional on R1/R2, new no-contract all-location best response, R0 implies unique positive interior contracted stationary root. | Formal SPNE for all histories; R0/R1/R2 true throughout a nonempty open parameter box. |
| 5 Risk and rescue value | **PARTIAL**: d0 monotonicity, strict selected-root V ordering. | Full q-derivative/IFT and kernel-verified 800-cell risk-reversal certificate. |
| 6 Welfare and policy | **PARTIAL**: no-contract planner's global UNIQUE optimum (new), core welfare identities and conditional valuation cutoff. | Contract planner strict concavity and unique global optimum, policy ceff witnesses and SPNE. |
| 7 Imperfect correlation | **EXTERNAL VERIFIER ONLY**: reproduced `proof_rho09_interval.py` with Python Fraction on all 400 cells, exit code 0. | The 400-cell certificate and rho-adjusted R1/R2 crossing proof in Lean. |
| 8 Semantic correspondence audit | **PARTIAL**: theorem-to-manuscript mapping and missing premises documented. | Full reverse dependency audit for every theorem and reproduction of all claims. |

## 3. Source modules added
- `RescueHotellingNoContractGlobal.lean`: no-contract crossing deviations and global reduced best response.
- `RescueHotellingDelivery.lean`: six terminal outcomes and conditional rescue/state payoffs.
- `RescueHotellingHistories.lean`: typed stage histories and contingent strategies.
- `RescueHotellingValue.lean`: strict V-ordering of selected roots.
- `RescueHotellingWelfareGlobal.lean`: unique global no-contract planner optimum.
- `RescueHotellingRoot.lean`: R0 conditions imply existence and uniqueness of inner contracted root.

No intentionally unproved `sorry`, `admit` or new `axiom` declarations were introduced in these modules. Each new statement is counted as kernel verified **only when the corresponding CI run has succeeded**.

## 4. Key successful CI runs
- Original audit: https://github.com/ryotamatsuki/public-climate-protection-private-production-redundancy/actions/runs/43548053495
- Delivery first pass, same-side/no-contract crossing: https://github.com/ryotamatsuki/public-climate-protection-private-production-redundancy/actions/runs/43549976834
- Welfare and rescue value root ordering: https://github.com/ryotamatsuki/public-climate-protection-private-production-redundancy/actions/runs/43550289999
- Contracted R0 root: https://github.com/ryotamatsuki/public-climate-protection-private-production-redundancy/actions/runs/43550763217

## 5. Unresolved / critical blockers
1. Define the full extensive-form stochastic game payoff and all information sets, with consumer orders and zero-distance subgames.
2. Prove that the constructed complete contingent strategy profile is an SPNE, not just that its reduced locations are Nash.
3. Verify all R0/R1/R2 inequalities and root signs for the paper's 5D open parameter rectangle using Lean.
4. Turn exact Python Fraction certificates for 800/400 q-cells into Lean kernel checked certificates.
5. Formalize continuous derivatives/IFT for the chosen root branch, unique turning point, strict risk response gap.
6. Complete contracted welfare and tax/subsidy implementation theorems, policy witness envelopes, and rho0=0.9 robust extension.
7. Audit every manuscript assertion against a corresponding Lean theorem's *exact* quantified scope.

## 6. Sign-off
A CI `success` certifies compiled Lean theorem statements only. It never certifies an unformalized paper theorem. **FULL FORMAL VERIFICATION: NOT PASS.** There is no verified counterexample to a manuscript claim yet, but the proof audit is unfinished.
