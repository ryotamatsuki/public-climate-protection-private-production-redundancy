# Stage 13 — Full-Paper Integration Refresh

**Date:** 2026-09-25  
**Target:** Environmental and Resource Economics (ERE)  
**Theory freeze:** `PCPPR-THEORY-FREEZE-2026-09-14-v2`  
**Stage-12R theory checkpoint:** `7a02e1b8558d8059c72287f2e226b74161ce36b3`  
**Formal Verification Gate:** PASS / CLOSED at merge `fc0c9cee8b83f0373659965b1615094e91e05c96`  
**Stage-12 v2.3+v2.4 recertification:** PASS / ERE Primary at merge `06c67fe65ad5d80e42808aab6e7bd9f3db33eddb`

The historical 2026-09-14 Stage-13 record is preserved at `docs/STAGE_13_HISTORICAL_2026-09-14.md`.

## Executive integration verdict

**CONDITIONAL GO — INTEGRATION COMPLETE; CI EVIDENCE PENDING**

The manuscript and ERE package have been refreshed against the current certified research lineage:

- v2.2 structural/theorem-absorption closure;
- v2.4 portability/falsification certificate;
- v2.5 exposition streamlining;
- closed Formal Verification Gate;
- Stage-12 v2.3 candidate-universe recertification selecting ERE as Primary.

No model primitive, theorem statement, canonical witness, equilibrium concept, welfare definition, or exact certificate is changed in Stage 13.

## 1. Section-role audit

The theory-first architecture remains unchanged from the v2.5 streamlining gate.

| Section | Role | Classification | Stage-13 decision |
|---|---|---|---|
| Introduction | question, mechanism, headline result, novelty | CORE | retain |
| Model | primitives, timing, objectives | CORE | retain |
| Equilibrium | downstream product/backup/location solution | CORE | retain |
| Main Result | local/social wedge and global theorem | CORE | retain |
| Welfare | channel decomposition | CORE | retain |
| Nested Benchmarks | mechanism identification | HELPFUL | retain in compressed form |
| Institutional Interpretation | empirical meaning/predictions | HELPFUL | retain |
| Related Literature | novelty boundary / absorption map | HELPFUL | retain |
| Discussion | scope, portability, limitations | HELPFUL | retain |
| Conclusion | answer to research question | CORE | retain |
| Proof/verification appendix | proofs and exact certificates | APPENDIX | retain |

No main-text section is DELETE.

## 2. Contribution-claim audit

PASS.

The manuscript, cover letter, title page, and package now use the same contribution boundary:

- exact global theorem: existence of a nonempty open set **within the maintained symmetric primitive family**;
- headline mechanism: **CONDITIONALLY PORTABLE** based on two pre-specified v2.4 diagnostic re-solutions;
- exact `1/4` marginal coefficient: tied to the maintained incidence/objective structure;
- no novelty claim for public/private adaptation crowd-out, plant attraction, local-public-input competition, or backup strategic substitution separately;
- v2.2 safe-development and local-public-input parent literatures remain acknowledged.

The cover letter was tightened to the manuscript theorem scope and now labels alternative specifications as diagnostics rather than extensions of the exact theorem.

## 3. Related-literature structure audit

PASS.

The v2.2 retrofit remains intact. The contribution is positioned against:

- public/private adaptation crowd-out;
- safe-development/location responses;
- local-public-input competition for mobile firms;
- endogenous environmental policy and plant location;
- private adaptation with imperfect competition.

No author-by-author catalogue expansion was added in Stage 13.

## 4. Results / Discussion separation

PASS.

Results continue to establish the formal policy-ranking conflict, marginal decomposition, exact witness, and product-substitutability interval. Discussion handles portability, interpretation, limitations, and applicability. No new result is introduced in Discussion or Conclusion.

## 5. Abstract / Introduction / Conclusion alignment

PASS subject to CI regression.

All three documents answer the same question and preserve the same claim scope. The abstract does not promote the v2.4 diagnostics to a general theorem. The conclusion introduces no new policy result.

## 6. Exposition streamlining status

The v2.5 `EXPOSITION_STREAMLINING_REPORT_2026-09-24.md` remains controlling.

Article profile: **GENERAL THEORY / THEORY-FIRST**.

Reader-arrival landmarks from the last certified v2.5 build:

- Introduction: page 1
- Model: page 3
- Equilibrium: page 6
- Main Result: page 9
- Welfare: page 12
- Benchmarks: page 13
- Institutional Interpretation: page 14
- Related Literature: page 16
- Discussion: page 17
- Conclusion: page 18
- Appendix: page 19

The Stage-13 build re-runs the page-arrival audit. Any structural regression blocks closure.

## 7. Figure / Table Architecture reconciliation

PASS.

Main text remains intentionally sparse:

1. one policy-regime figure;
2. one welfare-channel table;
3. one nested-benchmark table.

The policy-regime figure is regenerated deterministically as both PDF and EPS. No new visual or numerical result was introduced.

## 8. Stage-12 Journal Requirements Ledger integration

The Stage-12 ERE requirements baseline was consumed rather than silently treated as permanent.

Implemented at Stage 13:

- anonymous manuscript + separate identified title page;
- LaTeX source retained;
- clean-build anonymous source ZIP;
- abstract and keyword constraints under automated check;
- declarations and availability text;
- title-page author-contribution statement;
- reproducible PDF/EPS figure;
- anonymous reviewer replication package;
- AI/accountability wording that separates AUTHOR / AI / COMPUTATION / FORMAL roles.

Intentionally left **UNVERIFIED for Stage 14 live refresh**:

- authenticated Editorial Manager article type;
- portal file designations;
- portal AI/declaration fields;
- portal warnings;
- portal-generated review PDF;
- any journal/publisher rule changed after the Stage-12 access date.

## 9. Anonymous source and replication package

Stage 13 adds a dedicated anonymous manuscript-source builder.

`dist/ERE_anonymous_manuscript_source.zip` must:

- contain manuscript/section/reference source and generated figure/table dependencies;
- pass identifying-token scans;
- be extracted into a clean temporary directory;
- compile successfully with three pdfLaTeX passes.

The reviewer replication package now includes:

- v2.4 portability diagnostics and result snapshot;
- v2.5 exposition regression;
- proof-critical Lean source;
- pinned Lean/mathlib environment;
- symbolic/exact/numerical/benchmark tests.

## 10. AI provenance / accountability integration

Added:

- `docs/AI_PROVENANCE_LOG.md`;
- `docs/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md`.

The manuscript/title page no longer imply that AI, deterministic computation, or Lean constitutes author verification.

Two human-only items remain explicit rather than being fabricated:

1. confirm whether additional material AI use before 2026-09-14 must be added to the provenance log;
2. personally confirm the retrospective intellectual-contribution record.

These are accountability actions, not theory or manuscript-integration defects. Stage 14 disclosure reconciliation may not close until they are resolved. Stage 15 still requires a separate sign-off on the exact final package.

## 11. Cross-document and regression audit

A new `scripts/verify_stage13_integration.py` is part of `make verify`. It blocks:

- reintroduction of the historical Stage-13 checkpoint into active package documents;
- loss of the Stage-12 ERE selection;
- broader cover-letter theorem scope;
- loss of the portability-diagnostic distinction;
- AI/Lean-to-author verification conflation;
- unrecorded human sign-off;
- obvious workflow placeholders/TODOs.

## 12. Changes made

- synchronized package lineage to Stage-12 recertification;
- added clean-build anonymous source-package gate;
- updated reviewer replication package for v2.4/v2.5/Lean;
- added deterministic EPS artwork;
- tightened cover-letter theorem and portability scope;
- aligned manuscript/title-page AI/accountability wording;
- added AI provenance and retrospective author-contribution records;
- replaced stale ERE checklist with Stage-13 integration contract;
- added Stage-13 cross-document CI regression;
- updated CI artifact bundle and formal-verification provenance fields;
- preserved the historical 2026-09-14 Stage-13 report.

## 13. Remaining blockers

### Technical
- final branch `make verify`: **PENDING**
- final Lean regression / axiom report: **PENDING**
- Stage-13 integration artifact upload: **PENDING**

### Human-only / next-stage
- pre-2026-09-14 material-AI-use confirmation;
- personal confirmation of the retrospective intellectual-contribution record;
- Stage-14 live journal-rule refresh and authenticated-portal checks;
- Stage-15 final package sign-off.

## 14. Current verdict

**CONDITIONAL GO — bounded evidence completion only.**

If the technical CI gates are green, the manuscript/package is integrated and may advance to Stage 14 submission QA. The human-only accountability items remain fail-closed for Stage 14/15 and are not converted into automated PASS claims.
