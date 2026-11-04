# Round 2 — Referee 2: Mathematics, game theory and proof accountability

**Simulated technical report, 2026-11-05; not a separate human referee.**

## New primary claims reviewed
1. Strict gamma=0 primitive sufficient-condition region, compact-policy full planner and local best responses.
2. Positive social planner optimum, positive local overinvestment under direct benefit mu.
3. Strict positive derivative d(aN−aP)/dmu under b>H.
4. Strict positive gamma persistence and smooth continuation of both augmented planner and local equilibrium policies.
5. Exact three-way counterfactual derivatives (+16/189, 0, −16/1593) and global policy equilibria.

## Proof assessment
The gamma=0 social-surplus identity S=2t(q)+U(q)(aA−aB)^2 and the location identity p=1/2+h(q)(aA−aB)/(2H) were independently rederived by SymPy. Uniform strict inequalities control private-readiness interiority and location clipping. The derived public-welfare Hessian is shown to be uniformly negative definite by a conservative strict diagonal-dominance bound; local-government own-policy curvature is uniformly negative. A strict origin-bound and own-policy derivative monotonicity prove planner zero for unaugmented policies, while symmetric local FOCs and strict global own-policy concavity establish a genuine Nash equilibrium with all unilateral deviations excluded.

The mu-augmented result has the same curvature because mu enters objectives linearly, and interior global roots can be written exactly. The continued-gamma theorem is supported by a mathematically standard compact-domain continuity argument: uniform interior continuation margins, Δ(0)=0, a smooth nonsingular backup system, affine unique Bayesian location best response, strict Hessian margins and an implicit-function continuation of the interior FOCs. It *proves existence of epsilon*, not an explicit gamma interval or a globally valid statement for arbitrary product substitutability.

The counterfactual games are fully re-solved at each restriction, and the mu derivatives are verified using exact rational arithmetic, rather than inferred from one-sided missing-on-path margins. In particular, fixed private readiness gives a constant gap, whereas fixed locations yield a declining gap. The fixed-readiness, fixed-location and positive-mu social planner roots are all interior over 3/32<mu<1/8.

## Verification layers
- New standalone SymPy files analytic_region_exact.py, positive_optimum_exact.py, restricted_games_exact.py reconstruct basic policy objects and exact parameter margins without importing original production certificate logic.
- On commit 4d13ebdedae03ec38c6a58b25fa83e97002a92fa, the journal-specific workflow run 41925816466 passed original ERE science byte-identity, legacy symbolic/global/numerical/independent audit/test stages, independent new exact tests and PDF build. Subsequent extra comparative-static proof code and manuscript changes MUST have a separately successful CI before technical readiness is declared.
- The legacy ERE tracked-file-set workflow is expected to reject new tracked JPET files; its failure must remain visible and cannot be reclassified as a passed old freeze.
- The canonical gamma=12/25 original theorem has archived exact proofs and was rerun through original production tests, but it was not reconstructed by an *independent new proof formalization* in this simulation; remaining formal trust assumptions are disclosed.

## Remaining major comments
- The positive-gamma proposition derives from analytic continuity, and epsilon is not quantified. An illustrative numerical gamma range may be helpful, but must not be confused with rigorous coverage.
- Exact-source script parity is necessary but is not independent human proof review.
- The full alternative augmented model requires new author science review and a clean integrated replication bundle.

## Recommendation
**MAJOR R&R (conditional on latest CI passing)**, T1=4/5, T2=4/5, P1=4/5. No mathematical counterexample has been established to the checked new results; this does not claim full Lean formalization of the entire revised game.
