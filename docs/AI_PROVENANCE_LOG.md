# AI Provenance Log

Updated: 2026-09-25

This log records material AI use by reference. It is not a transcript archive. Verification actors are kept distinct: AUTHOR, AI, COMPUTATION, FORMAL, EXTERNAL HUMAN.

| Date | Tool/model | Purpose | Adopted artifact / decision | Disposition | Verification method | Actor(s) | Evidence ref / downstream effect |
|---|---|---|---|---|---|---|---|
| 2026-09-14 | OpenAI Astra-configured audit | Independent adversarial reconstruction of the Stage-12 theory and submission claims | Three repairs: backup-success joint law made explicit; product-substitutability interaction wording narrowed; certificate scaling recorded | Adopted after repair | exact symbolic/numerical regression; later formal regression | AI + COMPUTATION + FORMAL | docs/STAGE_12R_REPORT.md; docs/PROVENANCE.md; theory refreeze |
| 2026-09-24 | OpenAI ChatGPT GPT-5.6 Sol | Repair and harden Lean formal-verification branch | Lean source/CI fixes; full build and axiom report | Adopted | Lean kernel build, placeholder/axiom scan, CI | AI + FORMAL | docs/FORMAL_VERIFICATION_GATE_CLOSURE_2026-09-24.md |
| 2026-09-24 | OpenAI ChatGPT GPT-5.6 Sol + literature-search tooling | v2.2 structural-isomorphism / theorem-absorption attack | Safe-development parent lineage added; marginal decomposition explicitly downgraded from theorem novelty | Adopted | source comparison + repository verification | AI + COMPUTATION | docs/V2_2_STRUCTURAL_ABSORPTION_AUDIT_2026-09-24.md |
| 2026-09-24 | OpenAI ChatGPT GPT-5.6 Sol | v2.4 portability/falsification design and implementation | Pre-specified nonlinear-risk and logistic-location alternatives; reproducible diagnostic | Adopted | deterministic numerical re-solution + regression + Lean baseline regression | AI + COMPUTATION + FORMAL | docs/V2_4_PORTABILITY_PRESPEC_2026-09-24.md; scripts/verify_portability_v24.py |
| 2026-09-24 | OpenAI ChatGPT GPT-5.6 Sol | v2.5 exposition streamlining | Removed redundancy, compressed benchmark prose, added exposition regression audit | Adopted | clean manuscript build + page-arrival audit | AI + COMPUTATION | docs/EXPOSITION_STREAMLINING_REPORT_2026-09-24.md |
| 2026-09-25 | OpenAI ChatGPT GPT-5.6 Sol + current journal evidence | Stage-12 v2.3+v2.4 recertification | broad candidate universe, explicit exclusions, journal-fit matrix, ERE selected as Primary | Adopted | official journal evidence + repository CI/Lean regression | AI + COMPUTATION | docs/STAGE_12_REPORT.md; docs/STAGE_12_CANDIDATE_UNIVERSE_LEDGER_2026-09-25.md |
| 2026-09-25 | OpenAI ChatGPT GPT-5.6 Sol | Stage-13 integration refresh | source-package clean-build gate, reviewer package update, disclosure/accountability wording, package synchronization | Adopted subject to final CI | deterministic package QA + manuscript build + Lean regression | AI + COMPUTATION + FORMAL | STAGE_13_REPORT.md; current Stage-13 PR |

## Historical coverage boundary

The repository was created after earlier local development. This log does **not** assert a complete reconstruction of every material AI use before 2026-09-14. Before Stage 14 disclosure reconciliation closes, the author must confirm whether any additional material pre-2026-09-14 AI use should be added.

## Verification boundary

- AI analysis is AI evidence, not external-human review.
- Deterministic scripts are COMPUTATION evidence.
- Lean is FORMAL evidence about encoded statements under encoded assumptions.
- No AI/computation/formal PASS is represented as AUTHOR verification.
- Personal author confirmation of the intellectual-contribution record and final submitted package remains a human action.
