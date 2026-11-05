# Round 0 — Referee 2 (mathematical and computational audit)
**Simulated audit, not journal review. 2026-11-05.**

## What was actually checked
The PR #40 GitHub Actions journal-specific build succeeded and its 34-page PDF was downloaded and inspected with raster page-contact sheets. The older general workflow failed at `scripts/verify_final_audit_freeze.py` with `AssertionError: Unattested tracked changes`, after previous symbolic, normalization, global exact, numerical, 32 pytest, and exposition stages reported success. This is an intentional historical tracked-set attestation failure, not proof that main mathematics failed. The skipped subsequent stages mean the entire legacy `make verify` did NOT pass on this branch.

A separate SymPy reconstruction of the gamma=0 benchmark was conducted, starting from r(q)=q/(4k), f(q)=(1-q)/4+q^2/(32k), and t(q)=3(1-q)/8+q^2/(16k). The national surplus and local objective were rederived from their primitives; exact symmetric local FOCs and planner margins agreed with the text.

## Assessment of claims
- **Proposition 1**: The reaction derivative is correctly stated under an interior affine best-response; the global clipped-game uniqueness depends on a contraction bound not independently recertified here for all canonical gamma>0 policy profiles.
- **Proposition 2**: The identity `ML=MS/4+2b lambda0` follows directly under equal fixed shares and zero marginal protection resource costs at the origin; it is not independently novel.
- **Theorem 1**: Exact whole-domain certificates are claimed and have a positive earlier independent audit. This Round 0 did not regenerate all gamma>0 Bernstein and Lean artifacts de novo; classify their verification as prior audited evidence + residual independent-replication requirement, not as a new PASS.
- **Proposition 3**: Independently checked algebraically in the gamma=0 benchmark. Parent formulas and the exact symmetric FOC `GA,aA(a,a)=5/128-(315/64)a` reproduce the stated symmetric alpha=1/126.

## Major comments
1. Preserve frozen theory, certificate semantics, and time-stamped author signoff; no silent edits to old proof objects.
2. Add explicit model-vs-certificate verification mapping for the new JPET candidate.
3. Simplify `gamma=0` case with a parameter-analytic counterpart if a meaningful new result is proven.
4. Explicitly segregate proof of global optimum from mere diagonal stationary FOCs; prove own-policy global best responses over the entire interval.

## Recommendation
**Major R&R conditional** on full certificate provenance and complete external-proof verification; mathematical evidence is promising, no new fatal contradiction identified, but do not claim entire main theorem independently reproved in this round.
