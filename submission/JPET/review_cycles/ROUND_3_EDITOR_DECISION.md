# Round 3 — Simulated handling-editor decision after adversarial mathematical re-audit

**Internal simulation, 2026-11-05. Not an actual JPET decision.**

## Decision at discovery: MAJOR REVISION STILL REQUIRED

The prior Round-2 simulated R&R-CALIBER result cannot be carried over as an unconditional verification certificate. An independent symbolic derivation found that the main JPET-added primitive-region proof omitted a positive `+y/(16k)` term in an off-axis boundary derivative. As originally written, the attempted proof of the planner's global corner optimum was invalid. The claim itself need not be discarded, because strict concavity of the planner objective on the entire policy square and its negative gradient at the zero-policy origin imply global optimality by the supporting-hyperplane inequality.

The subsequent correction is **not** a stronger numerical assumption artificially rescuing the theorem. The unnecessary off-axis boundary condition was removed, and a second exact parameter witness was found that violates the discarded condition while satisfying all retained strict conditions. A separate test-script namespace collision (`S` as surplus versus `sp` as the SymPy module) was detected in CI and corrected without altering the mathematical assertions.

## Outstanding conditions for clearing Major R&R

1. Implement the strictly concave planner supporting-hyperplane proof, and compile a clean PDF.
2. Require the independent SymPy regression and counterexample witness to pass in CI.
3. Explain the economically meaningful generality: positive optimum, positive gamma, and benefit-gap sign interaction.
4. Relax the fixed half-surplus incidence and the state-independent hosting benefits with a physically coherent primary-operation definition.
5. Supply complete separate mathematical appendices and reproducibility archive with source hash.
6. Re-run independent referee roles using **unchanged** criteria; do not mark ACCEPT merely because the previous assessment was favorable.
7. Leave the closest-parent theorem-absorption uncertainty (Bayindir-Upmann 1998 full text inaccessible) transparent and do not invent review results.

**Status for the Round-3 discovery-stage manuscript: NOT YET CLEARED.** This report is immutable historical evidence and does not attempt to prejudge later corrected versions.
