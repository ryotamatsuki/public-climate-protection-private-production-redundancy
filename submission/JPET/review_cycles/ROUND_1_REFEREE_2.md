# Round 1 — Referee 2 re-review: mathematics
**Simulated technical review; not an actual separate researcher's audit.**

The gamma=0 augmented-welfare extension and two restricted-policy games have been rederived with independent SymPy exact rational algebra. The globally negative planner Hessian and local strictly concave best-response functions are certified over the full policy rectangle, not inferred from symmetric stationary equations.

- Augmented positive-optimum: for `3/32<mu<227/640`, `aP=(32mu-3)/270`, `aN=(128mu+5)/630>aP`. W diagonal Hessian in `[-2485/256,-1885/256]` and determinant in `[128925/2048,2607175/32768]`; GA own Hessian negative.
- Without hosting benefit, the augmented example can still feature overprovision, with an exactly verified globally concave government objective. This is acknowledged in the text rather than concealed.
- Unaugmented fixed-readiness: unique full-square planner `3/1280`; symmetric Nash `5/512`.
- Unaugmented fixed-location: strictly decreasing policy payoffs, so both optimum and Nash zero.
- Original main Theorem 1 gamma=12/25 is unchanged; its global policy certificate remains only previously verified, not independently re-certified in full during this round.

Potential issue that was actually found and fixed: a LaTeX literal `\n` control sequence in the new conclusion prevented PDF compilation in a journal CI run. It has been removed; check latest CI and examine updated PDF before marking technical-ready.

**Recommendation:** Mathematical evidence sufficient for **Major R&R on the new appendix results, conditional on latest CI/replication**. Main gamma>0 proof needs the separately specified full independent reproduction gate. T1=3 (overall), T2=3 (overall), P1=3; new gamma=0 addenda T1=4.
