# Stage 14 — ERE Submission QA / Live Requirements Refresh

**Date:** 2026-09-25  
**Target:** Environmental and Resource Economics (ERE)  
**Input Stage-13 merge:** `06609ae92d06911e93c633fa80c4137cc301641d`  
**Theory freeze:** `PCPPR-THEORY-FREEZE-2026-09-14-v2`

The previous Stage-14 record has been preserved at `docs/STAGE_14_HISTORICAL_2026-09-14.md`. It referred to an obsolete pre-recertification package and is not controlling.

## Executive verdict

**PUBLIC-RULE / REPOSITORY QA: PASS**  
**FULL STAGE-14 CLOSURE: HOLD — AUTHENTICATED-PORTAL ITEMS REMAIN**

Stage 14 has been re-opened against the live 2026-09-25 ERE instructions rather than inheriting the historical PASS. No theory, theorem, witness, equilibrium concept, welfare definition, or proof certificate is changed.

## 1. Live journal-rule refresh

Current ERE instructions were re-opened on 2026-09-25. The following remain applicable:

- double-anonymous review;
- separate author-identifying title page;
- editable source files at every submission/revision;
- LaTeX permitted for mathematical manuscripts;
- normally 150–250 words for the abstract;
- 4–6 keywords;
- relevant Statements and Declarations;
- material LLM use documented in Methods or a suitable alternative section where no Methods section exists;
- human accountability for the final text;
- Data Availability Statement for original research;
- public replication package after successful peer review and before final acceptance.

See `docs/STAGE_14_LIVE_REQUIREMENTS_LEDGER_ERE_2026-09-25.md`.

## 2. Manuscript / package QA

PASS on the repository-visible package:

- anonymous manuscript contains no author block;
- identified title page is separate;
- abstract/keyword constraints remain covered by automated ERE checks;
- manuscript contains `Data and Code Availability`;
- manuscript contains an explicit `AI Assistance Disclosure`;
- disclosure distinguishes AI assistance, deterministic computation, Lean formal checking, and author accountability;
- cover letter uses the certified theorem scope;
- reviewer replication archive remains anonymized;
- clean-build anonymous LaTeX source package remains part of `make verify`.

## 3. Historical AI provenance reconciliation

Stage 13 correctly refused to assume that pre-2026-09-14 AI use was absent.

The Stage-14 refresh found documented material AI-assisted work before that date:

- **2026-09-06:** theory freeze / full-draft construction, proofs, welfare/literature integration, symbolic certificates, numerical audits, tests, and LaTeX package work;
- **2026-09-13:** Stage-10 transfer and Stage-11 hostile audit, including identification of a global-certification gap;
- **2026-09-13 to 2026-09-14:** Stage-11C repair/certification work and Stage-12 journal-positioning/submission-package work.

These periods are now added to `docs/AI_PROVENANCE_LOG.md`. The previous blanket uncertainty about whether material pre-2026-09-14 use existed is therefore removed.

This is a provenance reconstruction from dated project interactions and repository milestones; it is intentionally role-level rather than a claim of a complete prompt transcript.

## 4. AI-policy reconciliation

PASS at the document level.

ERE's current instructions state that material LLM use must be documented in the Methods section or a suitable alternative if no Methods section exists. This theory manuscript has no conventional empirical Methods section and uses a dedicated `AI Assistance Disclosure` section.

The disclosure does not list an AI system as author and does not characterize AI, computation, or Lean as author verification.

## 5. Data / code / replication reconciliation

PASS at the document/package level.

The paper has no empirical dataset. The Data and Code Availability statement identifies the reviewer-facing anonymous computational/formal package. The live ERE rule requiring a public replication package after successful peer review and before final acceptance is preserved as a future-stage obligation; no premature public deanonymizing repository link is inserted into the anonymous manuscript.

## 6. Fees / publication route

Current ERE status remains hybrid. The subscription route carries no APC. The current published OA APC is £2490 / $3390 / €2790 plus applicable tax and is determined at acceptance.

This is informational only; Stage 14 does not require choosing OA.

## 7. v2.7 reviewer-verifiability closure

**PASS — REVIEWER VERIFIABILITY.**

The prospective v2.7 specialist-referee audit is recorded in `docs/REVIEWER_VERIFIABILITY_REPORT.md`. The audit reconstructs the full proof-critical chain from manuscript primitives through backup and location continuation, location-weighted surplus, policy rational functions, exact certificates, globality lemmas, and the headline theorem.

The recent proof-exposition repairs make the two previously implicit bridges explicit:

- the backup first-order conditions are displayed as the 2x2 linear system whose determinant/interiority are certified;
- profile-specific surplus is explicitly aggregated across the four location profiles before entering the planner and local-government policy objectives.

The audit finds no remaining **BRIDGE NEEDED**, **APPENDIX DETAIL NEEDED**, or **SUBSTANTIVE DEFECT** item. Large generated polynomial expansions, Bernstein coefficient lists, and root-isolation traces remain appropriately delegated to the reproducibility archive.

This PASS closes the latest-workflow reviewer-verifiability delta. It does not substitute for the author's personal intellectual-contribution confirmation or for authenticated portal QA.

## 8. Authenticated portal items

The following are deliberately **UNVERIFIED**, not guessed:

- Editorial Manager article type;
- file-designation labels;
- portal-specific AI/declaration questions;
- submission warnings;
- portal-generated review PDF.

These require an actual authenticated submission draft and must be recorded before Stage 14 can be fully closed.

## 9. Human-only accountability item

**PASS — AUTHOR CONFIRMATION RECORDED.**

On 2026-09-25, the author explicitly confirmed all five required intellectual-contribution items and confirmed that the reconstructed AI provenance is materially complete. The confirmation is recorded in `docs/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md`.

This closes the human-only Stage-14 accountability item. The confirmation was not inferred by automated QA.

## 10. Stage-14 regression gate

`scripts/verify_stage14_submission_qa.py` is added to `make verify`. It prevents:

- restoration of the obsolete Stage-14 PASS as the controlling record;
- omission of the live-requirements ledger;
- loss of the manuscript AI disclosure or data/code statement;
- loss of reconstructed pre-2026-09-14 provenance entries;
- accidental representation of authenticated portal items as verified;
- loss of the recorded author-confirmation state or replacement by an automated/inferred confirmation;
- loss of the v2.7 reviewer-verifiability report or PASS verdict.

## 11. Closure status

### Completed now
- live public ERE requirements refresh;
- AI-policy/document-placement reconciliation;
- data/code/replication reconciliation;
- historical AI provenance reconstruction;
- stale Stage-14 record archived;
- Stage-14 regression gate added;
- v2.7 reviewer-verifiability audit PASS recorded;
- author intellectual-contribution and AI-provenance confirmation recorded;
- package remains theory-frozen.

### Still required for full Stage-14 closure
1. authenticated Editorial Manager article-type/file/declaration review;
2. generated review-PDF inspection.

## Final Stage-14 status

**TECHNICAL / PUBLIC-RULE QA READY.**

The repository is ready to enter the authenticated Editorial Manager submission-draft step. Stage 14 remains fail-closed only on the portal-only checks and generated review-PDF inspection. Stage 15 final package freeze/sign-off is not yet authorized.
