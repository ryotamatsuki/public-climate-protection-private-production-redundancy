# JPET Proposition 8 — model-specific Lean 4 verification

Source: [ResponseInteraction.lean](ResponseInteraction.lean)

The module uses the repository's **Lean 4.32.1** and pinned mathlib
manifest, and operates over **real-valued policy variables (ℝ)** with exact
rational coefficients. It does not alter any frozen ERE scientific file,
the original formal Theorem 1, or the article's mathematical statements.

## Proved in Lean (the reduced gamma=0 benchmark)

1. Primitive-to-policy coefficient identities: mu0, tc, s, m.
2. Exact full-endogenous two-policy economic payoff functions, including
   unilateral-deviation polynomials and the full higher-order remainders.
3. Analytic stationarity and strict policy feasibility for all six
   planner/Nash levels throughout 3/32 < mu < 1/8.
4. Three finite-change gap laws, for all real benefit increments:
   16/189 (positive), zero, and -16/1593 (negative).
5. **Full-endogenous planner global optimality:** an exact
   square-completion decomposition and an interval bound on U(q) prove
   the symmetric policy is globally optimal on the entire policy square.
6. **Full-endogenous local Nash globality:** a quartic deviation
   identity and interval remainder inequality exclude profitable
   unilateral deviations anywhere in the entire policy square.
7. Fixed-readiness and fixed-location counterfactuals: exact
   sum-of-squares proofs of global coordinated and unilateral local
   policy optima, not just first-order stationarity.
8. The seven key theorem dependencies are printed by Lean's
   `#print axioms` for an explicit trust-boundary audit.

No `sorry`, `admit`, explicitly declared `axiom`, or `native_decide`
occurs in this new proof module.

## Remaining trust boundary (IMPORTANT)

The module takes the **gamma=0 private-equilibrium reduced-form
identities** (expected surplus, primary-location response, and the
restricted-game reduced payoffs) as mathematical definitions. The
derivation of those identities from the five-stage model and the
proof of the validity/interiority of private continuations are still
in the manuscript plus independent exact Python verification.

Therefore a green Lean check does NOT by itself provide a closed
formalization from original economic primitives through every game
stage to Proposition 8. Positive-gamma continuation and the gamma
comparative static (Proposition 10), model perturbations, and the
baseline gamma=12/25 global certificates are not re-proved here.

The frozen ERE Lean code also has separate explicit conditional
hypotheses and `native_decide` trust dependencies; see
`formal/README.md`. This new module should not be represented as
an unconditional formal proof of the entire paper.

## Reproduce

```bash
cd formal
lake exe cache get
lake env lean ../submission/JPET/formal/ResponseInteraction.lean
cd ..
python submission/JPET/review_cycles/restricted_games_exact.py
```

The dedicated CI workflow is
`.github/workflows/jpet-lean-response.yml`.
