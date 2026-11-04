# Round 2 revision log — 2026-11-05

**Prior record:** Round 0 BELOW R&R, Round 1 BORDERLINE; those reviews were not edited to fabricate success.

**Scientific change:** New overlay-only Section 7, submission/JPET/sections/06b_analytic_region.tex, derives the global gamma=0 identity, a primitive sufficient-condition region (risk q0, backup k, location dispersion H, hosting b, policy cost c), a positive-planner-optimum/positive-local-overprovision comparative static with respect to direct benefit mu, and an open gamma>0 persistence result via compactness and implicit function theorem. An additional Proposition tests the sign of the mu slope in fully re-solved fixed-readiness and fixed-location policy games: +16/189, 0, −16/1593.

**Independent verification:** analytic_region_exact.py derives identities from primitives with SymPy; positive_optimum_exact.py proves exact bivariate Bernstein bounds; restricted_games_exact.py verifies three policy games and the new slope-sign pattern. Original ERE scientific files untouched. Separate JPET workflow requires old original mathematical code tests and source byte identity. Run 41925816466 passed source-invariance, complete scientific audit, separate exact tests and a 42-page PDF *before* the final comparative-static proposition was added; subsequent latest CI and PDF must be checked.

**Closest literature:** Keen and Marchand (1997) added as an existing public-input spending-overbias parent, Matsumoto (1998) contrasted with this public protection policy game, Ogawa (2010) supports Bayindir fixed-firm/mobile-capital distinction. Full published Bayindir paper not obtained; no claim of complete exclusion.

**Editorial simulated assessment:** Round 2 all three functional reviewer perspectives favor Major R&R because the new comparative-static signs constitute a more precise and testable theoretical prediction than the known general overprovision mechanisms. `ROUND_2_EDITOR_DECISION.md` records internal R&R-CALIBER without altering threshold. Remains draft and author-unapproved. No main merge, no actual journal submission.

---

## Archived Round 0–1 log

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
