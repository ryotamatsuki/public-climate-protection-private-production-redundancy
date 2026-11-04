# Mathematical independent audit — 2026-11-05

## Evidence hierarchy
1. **Independently recalculated here**: gamma=0 f(q), t(q), p(aA,aB), baseline origin signs, augmented gamma=0 Hessians and full-domain bounds, exact restricted games.
2. **Earlier audited, not fully rederived here**: gamma=12/25 original Theorem 1 full rational certificates, clipped backup contraction, all first-stage global deviations, existing Lean partial formalization; legacy repository CI reports mathematical stages passing before a historical tracked-file-lock failure.
3. **Not established**: positive-planner-optimum theorem over full gamma>0 oligopoly, full textbook microfoundation of local half-surplus incidence, theorem-level nonabsorption by all published prior art.

## Independent tools
- SymPy exact rational symbolic algebra with bivariate tensor Bernstein conversion in `positive_optimum_exact.py`.
- A separate primitive-based SymPy construction in `restricted_games_exact.py`.
- No import of the production certificate code, no reliance on prior PASS labels for new claims.
- Exact W Hessian negative definiteness via `W_AA<0` and `det Hessian>0` on entire compact policy square; local Nash via global strict own-policy concavity and interior symmetric FOCs.

## Checks that must remain explicit
- A positive stationary point **does not** by itself establish a Nash equilibrium or planner global optimum.
- `p` is always interior and readiness remains in (0,1) across full gamma=0 policy square.
- The new augmented objective changes welfare accounting but **not** the firms' incentives.
- No gamma>0 extension should be inferred from a gamma=0 certificate.
- The original ERE freeze attests a historical exact tracked set; added JPET files intentionally violate it. Do not weaken the old guard.
- A new claim's author approval is pending; historical author confirmation does not transfer.

## Numerical outputs
At mu=1/10:
- augmented planner optimum = 1/1350;
- augmented local Nash = 89/3150;
- same model with b=0 local Nash = 17/2950.
Unaugmented fixed-readiness:
- planner optimum = 3/1280;
- symmetric local Nash = 5/512.
Unaugmented fixed locations:
- planner and Nash = 0.

## Remaining verification
- CI on latest full PR #41 and PDF visual inspection.
- Third-party independent review (separate researcher or genuinely independent model) of new code and economic accounting.
- Full re-execution of the original gamma>0 formal and exact pipeline using a JPET-specific historical-freeze-preserving verification contract.
