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
8. **New gamma=0 primitive bridge:** proves the separable Cournot
   profit bound; a completed-square global and unique private-readiness
   optimum; exact optimized private profit and material surplus;
   whole-square bounds on private readiness and the uniform-fit
   location cutoff; exact equality between primitive expected surplus
   and the full-endogenous reduced policy surplus.
9. **Restricted-game bridge:** derives the fixed-readiness and
   fixed-location policy objectives directly from the corresponding
   restricted private response rules, verifying equality with the
   reduced objectives up to displayed policy-independent constants.
10. The original seven main theorem dependencies are printed by
   Lean's `#print axioms` for an explicit trust-boundary audit.

No `sorry`, `admit`, explicitly declared `axiom`, or `native_decide`
occurs in this new proof module.

## Remaining trust boundary (IMPORTANT)

The new bridge derives **gamma=0** reduced policy payoffs from
explicit state-dependent, separable-market primitives, checks the
optimal private readiness and its policy-domain interiority, and
verifies the location cutoff's interiority on the whole policy square.
It also matches the two restricted policy games to their corresponding
primitive objectives. These algebraic and inequality proofs substantially
reduce the former private-continuation trust boundary.

This is **not a measure-theoretic formalization of the five-stage game**:
the meaning of the uniform-fit cutoff as a Bayesian choice probability,
the assumed conditional-independence distribution of regional shocks and
backup draws, and the underlying economic interpretation of separable
market surplus are taken from the manuscript, not constructed as Lean
random variables or stochastic strategies. The specific gamma=0 witness
is proved, not a parameter-general theorem.

Positive-gamma continuation and the gamma comparative static
(Proposition 10), model perturbations, and the baseline gamma=12/25
global certificates are not re-proved here. The frozen ERE formal proof
retains its own independent trust boundary.

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
