# Rescue Hotelling v0.4.2 — full-model Lean verification audit (2026-11-14)

**Status: PARTIALLY FORMALIZED — NOT a complete Lean proof of the economic model.**

Paper: *Mutual Production Contracts and Spatial Differentiation under Supply Disruptions*, v0.4.2. No manuscript TeX or PDF has been modified.

## Mechanical certificate scope

Audit branch: `rescue-hotelling-model-audit-2026-11-14`.

All executable theorems are in `formal/RescueHotelling*.lean`; the dedicated workflow checks the pinned Lean 4.32.1/mathlib toolchain, rejects `sorry`, `admit`, and project-level `axiom` declarations, then emits logs. A theorem is considered kernel-passed only if its module completed successfully in GitHub Actions. Full workflow success requires all modules to pass.

Modules:
- `RescueHotellingCore.lean`: algebraic FOC, root order, comparative welfare identities.
- `RescueHotellingModelCheck.lean`: price equations, rational monotonicity, bargaining transfer feasibility, concavity envelope algebra.
- `RescueHotellingExtendedGame.lean`: price best responses with clipped demand, correlated Bernoulli failure distribution.
- `RescueHotellingLocation.lean`: exact actual-payoff polynomials and whole same-side deviation region.
- `RescueHotellingRefusal.lean`: refusal deviations excluded using R1 applied to actual payoffs.
- `RescueHotellingCrossing.lean`: crossing deviations excluded using R2, including voluntary continuation.
- `RescueHotellingReducedNash.lean`: conditional global Nash optimality of both locations in reduced game, if G=0 and R0/R1/R2-like conditions hold.
- `RescueHotellingCoverage.lean`: candidate-price delivered surplus is positive for all consumers under v>3t.
- `RescueHotellingBargaining.lean`: proposer optimizes over all possible unrestricted lump-sum transfer offers with responder acceptance at indifference.

## Critical outstanding proof obligations

1. Formalize all extensive-form histories, the positive delivery probability and customer outside option, and the full strategy-space definition of **subgame-perfect Nash equilibrium**. The reduced location Nash theorem, by itself, does not satisfy this requirement.
2. Certify the paper's R0/R1/R2 parameter region and the existence/uniqueness of the selected regular equilibrium root **within Lean**, rather than via external Python exact intervals.
3. Establish a kernel-verified derivative/implicit-function theorem for the selected equilibrium branch and all inequalities on the **entire** q∈[0.05,0.15] continuum; include strict concavity and unique turning point.
4. Kernel-verify all welfare and planner optimization arguments, tax/subsidy implementation and correlated-risk robustness family, including the q-interval certificate.
5. Map each paper theorem to a Lean statement with **no weaker assumptions and no stronger conclusions**. Proving a statement conditioned on R1/R2 is not proving those conditions hold on a nonempty open parameter region.
6. Cross-check numerical and data-generation code with theorem statements. Lean can certify formal internal correctness, not real-world validity of the economic assumptions or novelty.

## Source provenance

Original 19 Lean declarations and follow-up 14 declarations were previously verified in Actions runs 42777492177 and 43544427035 respectively. New verification happens entirely in this isolated branch. Never interpret the raw count of theorem declarations as the count of verified economic propositions or as proof of the entire model.
