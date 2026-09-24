# AI Provenance Log

Updated: 2026-09-25

This log records material AI use by reference. It is not a transcript archive. Verification actors are kept distinct: AUTHOR, AI, COMPUTATION, FORMAL, EXTERNAL HUMAN.

| Date | Tool/model | Purpose | Adopted artifact / decision | Disposition | Verification method | Actor(s) | Evidence ref / downstream effect |
|---|---|---|---|---|---|---|---|
| 2026-09-14 | OpenAI Astra-configured audit | Independent adversarial reconstruction of the Stage-12 theory and submission claims | Three repairs: backup-success joint law made explicit; product-substitutability interaction wording narrowed; certificate scaling recorded | Adopted after repair | exact symbolic/numerical regression; later formal regression | AI + COMPUTATION + FORMAL | docs/STAGE_12R_REPORT.md; docs/PROVENANCE.md; theory refreeze |
| 2026-09-24 | OpenAI ChatGPT GPT-5.6 Sol | Repair and harden Lean formal-verification branch | Lean source/CI fixes for Primitives, Location, ProductMarket, Backup; full lake build and axiom report | Adopted | Lean kernel build, placeholder/axiom scan, CI | AI + FORMAL | docs/FORMAL_VERIFICATION_GATE_CLOSURE_2026-09-24.md |
| 2026-09-24 | OpenAI ChatGPT GPT-5.6 Sol + literature-search tooling | v2.2 structural-isomorphism / theorem-absorption attack | Safe-development parent lineage added; decomposition explicitly downgraded from theorem novelty | Adopted | source comparison + repository verification | AI + COMPUTATION | docs/V2_2_STRUCTURAL_ABSORPTION_AUDIT_2026-09-24.md |
| 2026-09-24 | OpenAI ChatGPT GPT-5.6 Sol | v2.4 portability/falsification design and diagnostic implementation | Pre-specified nonlinear-risk and logistic-location alternatives; reproducible diagnostic | Adopted | deterministic numerical re-solution + regression + Lean baseline regression | AI + COMPUTATION + FORMAL | docs/V2_4_PORTABILITY_PRESPEC_2026-09-24.md; scripts/verify_portability_v24.py |
| 2026-09-24 | OpenAI ChatGPT GPT-5.6 Sol | v2.5 exposition streamlining | Removed redundancy, compressed benchmark prose, added exposition regression audit | Adopted | clean manuscript build + page-arrival audit | AI + COMPUTATION | docs/EXPOSITION_STREAMLINING_REPORT_2026-09-24.md |
| 2026-09-25 | OpenAI ChatGPT GPT-5.6 Sol | Refreshed ERE Stage-14 compliance audit and package hardening | current-policy ledger, AI-disclosure rewrite, source-package clean-compile gate, EPS companion artwork | Adopted subject to final CI | current official policy review + deterministic build/QA | AI + COMPUTATION | docs/JOURNAL_REQUIREMENTS_LEDGER_ERE_2026-09-25.md; refreshed Stage-14 report |

## Verification boundary

- AI analysis is recorded as AI evidence, not external human review.
- Deterministic scripts are COMPUTATION evidence.
- Lean is FORMAL evidence about encoded statements under encoded assumptions.
- No AI/computation/formal PASS is represented as AUTHOR verification.
- The author's personal final approval of the exact submission commit/PDF/package is a Stage-15 action and is not asserted here.
