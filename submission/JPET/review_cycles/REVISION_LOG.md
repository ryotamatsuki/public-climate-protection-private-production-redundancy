# Revision log — PR #41 (2026-11-05)

## Round 0: immutable assessment before revision
- Three functional-lens reviewer reports and a handling-editor report were completed and committed prior to new math.
- Editor verdict: BELOW R&R. Primary blockers: originality/significance, weak baseline-zero applicability, unproven full restricted-game counterfactuals, frozen-ERE CI conflict.
- Parent theorem ledger marked the inaccessible Bayindir-Upmann full text UNRESOLVED; Billon 2023 and other public-input parents acknowledged.

## Round 1: scientific revision and checks
1. **PR #41 created** from PR #40 JPET scope revision. Historical `paper/`, `references/`, original certificates, and ERE submission lock left unchanged.
2. **New JPET copy of benchmark section** `submission/JPET/sections/06_benchmarks.tex` referenced by the JPET wrapper only.
3. **Exact positive planner optimum under augmented benefits** with 3/32<mu<227/640, aP=(32mu-3)/270 and aN=(128mu+5)/630; exact full-square W Hessian and GA own-policy negative bounds.
4. **Transparent primitive-band remark** 3k<q0<4k, b>H(q0-3k)/(4k-q0); expressly first-order, not global.
5. **Full restricted policy games** for fixed private readiness (positive planner and local overprovision) and fixed location (both zero); exact global planner and local government checks.
6. **Independent standalone SymPy scripts** `positive_optimum_exact.py` and `restricted_games_exact.py` added and invoked from JPET-specific CI.
7. JPET title-page/abstract/introduction/conclusion/cover-letter/README updated to separate original frozen ERE theorem from unapproved additions.
8. **Real defect found and resolved:** literal `\n` in a draft LaTeX conclusion caused an intermediate JPET CI PDF build failure; corrected and following JPET PDF build succeeded.
9. Current JPET PDF from successful CI for commit `a03fb99b8e9aeca21bd92f5ed239d943e9b010f2` has 38 pages, new Propositions 4–5, and searchable Bayindir-Upmann bibliography. Render and cross-reference check performed.
10. Re-review preserved original scoring calibration. Verdict remains BORDERLINE, not R&R-CALIBER. No claims of author approval, merge, or submission.

## Explanation of historical CI
The old ERE `make verify` invokes a historical exact-file-set freeze and is expected to fail on any branch with new tracked JPET documents. That failure is not relabeled PASS. Mathematical stages prior to the freeze have separately passed; a full JPET-specific attestation and proof package still have to be assembled.

## Publication ethics
New mathematical results were produced with substantial AI assistance. User must personally verify and affirm scientific interpretation and contributions; updated disclosure covers November 2026. Do not submit the candidate until author approves it.
