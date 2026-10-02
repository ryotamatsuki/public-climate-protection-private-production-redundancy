# Public Climate Protection and Private Production Redundancy

Reproducibility and manuscript repository for the theory project **Public Climate Protection and Private Production Redundancy: Local Resilience Competition, Plant Location, and Disaster-State Market Power**.

## Research status

- Current theory freeze record: `PCPPR-THEORY-FREEZE-2026-09-14-v2`
- Stage 12R theory checkpoint: `7a02e1b8558d8059c72287f2e226b74161ce36b3`
- Formal Verification Gate: **PASS / CLOSED**, merge `fc0c9cee8b83f0373659965b1615094e91e05c96`
- v2.2 structural-absorption retrofit: **CLOSED**
- v2.4 portability/falsification retrofit: **CLOSED — headline CONDITIONALLY PORTABLE**
- v2.5 exposition retrofit: **CLOSED**
- v2.7 reviewer-verifiability audit: **PASS / CLOSED**
- Stage 12 v2.3+v2.4 journal-positioning recertification: **CLOSED**, merge `06c67fe65ad5d80e42808aab6e7bd9f3db33eddb`
- Stage 13 integration refresh: **CLOSED**, merge `06609ae92d06911e93c633fa80c4137cc301641d`
- Current journal target: *Environmental and Resource Economics (ERE)*
- Current phase: **Stage 15 pre-submission repository freeze PASS; full Stage 15 HOLD because the official linked submission endpoint is not currently live and authenticated portal checks remain fail-closed**

## Core result

The model combines decentralized place-based climate protection, endogenous primary plant location, costly geographic backup readiness, localized disaster risk, and differentiated-product oligopoly.

The main result is a **Protection–Attraction Conflict**: within the maintained symmetric primitive family, there exists a nonempty open set in which coordinated welfare is maximized by zero additional local protection while the decentralized jurisdictional game has a strictly positive symmetric protection equilibrium. Public protection directly lowers disruption risk but can crowd out firms' private geographic redundancy; local governments may nevertheless continue protection because it attracts mobile primary production.

The exact global theorem is baseline-family specific. Pre-specified v2.4 diagnostics under a nonlinear risk technology and logistic location heterogeneity preserve the canonical planner-zero/local-positive ranking, supporting **conditional portability** without enlarging the exact theorem.

## Repository governance

Every submission candidate must point to an explicit freeze commit. Any change affecting probability primitives, equilibrium correctness, the policy-ranking theorem, parameter domains, welfare accounting, benchmark definitions, or the claim boundary reopens the relevant research gate.

AI, deterministic computation, formal verification, and author judgment are recorded as distinct evidence types. A successful Lean build certifies encoded statements under encoded assumptions; it does not substitute for author judgment, economic interpretation, novelty assessment, or final submission approval.

## ERE submission architecture

The journal-facing package separates double-anonymous reviewer materials from non-anonymous editorial materials.

- Anonymous manuscript source: `paper/main.tex`
- Stage 13 integration report: `STAGE_13_REPORT.md`
- Stage 14 live QA report: `STAGE_14_REPORT.md`
- Latest live requirements ledger: `docs/STAGE_14_LIVE_REQUIREMENTS_LEDGER_ERE_2026-10-02.md`
- Stage 15 report: `STAGE_15_REPORT.md`
- Stage 15 upload manifest: `submission/ERE_STAGE15_UPLOAD_MANIFEST.md`
- Stage 15 scientific-object lock: `submission/ERE_STAGE15_SCIENTIFIC_OBJECT.lock`
- Title page: `submission/ERE_title_page.tex`
- Cover letter: `submission/ERE_cover_letter.md`
- Submission checklist: `submission/ERE_submission_checklist.md`
- AI provenance log: `docs/AI_PROVENANCE_LOG.md`
- Author intellectual-contribution record: `docs/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md`
- Reviewer-verifiability report: `docs/REVIEWER_VERIFIABILITY_REPORT.md`
- Anonymous source-package builder: `scripts/build_verify_ere_source_package.py`
- Anonymous replication builder: `scripts/build_ere_review_package.py`
- ERE format/anonymity verifier: `scripts/verify_ere_submission.py`

`make verify` generates `dist/ERE_anonymous_manuscript_source.zip`, `dist/ERE_anonymous_replication.zip`, and the single transport artifact `dist/ERE_submission_ready_bundle.zip`. The source archive is extracted and clean-compiled in CI. The transport bundle is repository-complete but does not substitute for the live Editorial Manager review-PDF check.

## Canonical validation

```bash
make verify
```

The gate runs symbolic identities, certificate-normalization checks, exact policy and whole-domain certificates, numerical stress tests, v2.4 portability diagnostics, benchmark checks, regression tests, deterministic exposition-object generation, ERE format/anonymity checks, Stage-13 integration regression, Stage-14 submission-QA regression, Stage-15 scientific-object/fail-closed regression, a clean manuscript build, v2.5 exposition/page-arrival audit, clean-build source-package verification, title-page build, anonymous replication-package generation, and final submission-ready bundle generation. Lean verification runs as a separate pinned CI job.
