# JPET Proposition 8 — bounded Lean certification

The independent certificate lives in [ResponseInteraction.lean](ResponseInteraction.lean).
It uses the original project's pinned Lean 4.32.1 / mathlib manifest, but
**does not change the frozen ERE formal modules**, their scientific source,
or the existing Theorem 1 trust boundary.

## Claims covered

- Closed rational checks of the exact primitive coefficients (mu0, tc, s, m).
- Exact polynomial-deviation identities for the *fully endogenous* gamma=0
  coordinator and unilateral local-government objectives, including every
  quadratic-and-higher remainder term. This identifies the actual FOC
  coefficients from the continuation-derived policy payoff functions.
- FOCs and strict interior feasibility of all six policy levels on
  3/32 < mu < 1/8.
- Exact finite-change identities for the three policy gaps, proving the
  positive, zero and negative slopes without relying on numerical differentiation.
- Global maximization of the two-dimensional planner and unilateral Nash
  objective functions for the *fixed-readiness* and *fixed-location* restricted
  games by sum-of-squares; no first-order-only globality inference.

## Deliberately unproved here

- The private-game equilibrium derivation of the reduced-form fullSurplus and
  locationProb objects; these are established in the mathematical appendix
  and tested in the independent SymPy script.
- Full-endogenous global planner and unilateral local-optimality over the
  entire two-dimensional policy square. These remain in the existing exact
  Python/math proof layer; the Lean first-order expansion does NOT establish
  globality.
- Positive-product-substitutability continuity, the nonempty primitive
  region, incidence robustness, and the full model's 43-page prose claims.
- Other original theorem obligations in formal/README.md, including
  native_decide in *pre-existing* original formal modules.

## Run

From the repository root (with the pinned toolchain and mathlib cache):

```bash
cd formal
lake exe cache get
lake env lean ../submission/JPET/formal/ResponseInteraction.lean
cd ..
python submission/JPET/review_cycles/restricted_games_exact.py
```

The separate workflow
`.github/workflows/jpet-lean-response.yml` compiles this module and
runs the independent restricted-games exact Python check.

A green CI proves that Lean accepted this *stated* set of theorems. It does
not constitute a proof of novelty, a claim that all paper propositions were
formalized, or journal acceptance.
