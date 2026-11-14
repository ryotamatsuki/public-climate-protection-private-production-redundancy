# Formal verification report — Hotelling v0.4.2
Status: **PARTIAL FORMAL VERIFICATION** (provisional Stage 0 and Stage 1 audit)
Date: 2026-11-14

## Baseline
The pre-existing audit branch at `8a3c6a0aeb11888e17abcc549119e2a929438f1f` contains nine Lean modules and 75 kernel-compiling declarations, CI run 43548053495. This is evidence for those exact Lean statements, NOT an entire SPNE proof.

## This audit
1. Created a separate branch, leaving the LaTeX/PDF unchanged.
2. Extracted the definitive v0.4.2 source ZIP and mapped every numbered theorem (2 lemmas, 8 propositions, 3 corollaries) and all unnumbered exact certificates.
3. Created `FORMAL_PROOF_OBLIGATIONS.md` and `THEOREM_CORRESPONDENCE_MATRIX.md` before adding new Lean proofs.
4. New modules under review: `RescueHotellingNoContractGlobal.lean` (candidate global best response in no-contract model), `RescueHotellingDelivery.lean` (joint failure/rescue outcome kernel), `RescueHotellingHistories.lean` (types for full histories and contingent strategies).
5. There is no basis yet to claim full extensive-form SPNE, complete interval certificates, or full welfare/robustness formalization.

## Compliance
- New proprietary axioms / sorry / admit: NOT INTENTIONALLY USED; verify with final CI.
- Manuscript, TeX and PDF: UNCHANGED.
- Remaining theorem gaps: `UNRESOLVED_PROOF_OBLIGATIONS.md`.
- Current terminal verdict: **NOT PASS** for full-model formalization; meaningful scoped formal verification is possible.
