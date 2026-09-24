# ERE submission checklist — refreshed Stage 14

Target: **Environmental and Resource Economics**
Refresh date: **2026-09-25**

Current certified lineage:

- Stage-12R theory refreeze: `PCPPR-THEORY-FREEZE-2026-09-14-v2`
- Formal Verification Gate merged: `fc0c9cee8b83f0373659965b1615094e91e05c96`
- v2.2 structural-absorption retrofit merged: `52ffb2f134e507557b736c3fa2f6082794abba1f`
- v2.4 portability/falsification retrofit merged: `7cf7117e6319c7c595a3d10ef5475cc74a97c209`
- v2.5 exposition retrofit merged: `ea67d654f3a44a19ede96dafacdf2419160a8496`

## Current official ERE requirements

Official sources re-opened on 2026-09-25:

- https://link.springer.com/journal/10640/submission-guidelines
- https://link.springer.com/journal/10640/how-to-publish-with-us
- https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation
- https://www.springernature.com/gp/policies/editorial-policies/using-ai-in-research

- [x] Double-blind manuscript with separate title page.
- [x] Abstract within 150–250 words.
- [x] 4–6 keywords (six supplied).
- [x] Mathematical manuscript retained in LaTeX, which ERE explicitly permits.
- [x] All relevant editable manuscript source files packaged for upload.
- [x] Exact anonymous source ZIP is extracted and clean-compiled in CI.
- [x] Data Availability statement included.
- [x] Reviewer-accessible anonymized replication archive supplied; no empirical dataset is used.
- [x] Public persistent replication deposit reserved for the journal's post-review / pre-acceptance requirement.
- [x] Funding, competing interests, ethics/data/code, and author-contribution statements included on title page.
- [x] Current Springer Nature AI-use policy reconciled with the manuscript.
- [x] AI, COMPUTATION, FORMAL, and AUTHOR verification roles are not collapsed.
- [x] DOI links use full https://doi.org/... form where available.
- [x] Figure 1 generated as PDF for LaTeX and EPS companion artwork for portal use.
- [x] Main-text exhibit architecture remains one figure + two tables.
- [x] v2.5 page-arrival / exposition audit is part of `make verify`.
- [x] v2.4 portability diagnostics are part of `make verify`.
- [x] Lean source and pinned formal environment are included in the anonymized reviewer archive.

## Double-anonymous package

- [x] Anonymous manuscript contains no author field content.
- [x] Title page is separate.
- [x] Reviewer replication ZIP forbidden-token scan covers manuscript/code/formal source.
- [x] No Git metadata, submission-only files, author names, e-mail addresses, ORCID, or identifying repository URLs are included in the reviewer ZIP.
- [x] Formal Lean source is present but does not identify the author.
- [x] Reviewer Makefile reproduces computational, portability, exposition, and manuscript checks.
- [x] Formal build is separately available via `make formal-verify`.

## Exact upload set

Prepared locally/by CI:

1. anonymous manuscript PDF;
2. `ERE_anonymous_manuscript_source.zip` — editable LaTeX/source package, clean-build certified;
3. separate title-page PDF/source;
4. cover letter;
5. `ERE_anonymous_replication.zip`;
6. EPS companion artwork if Editorial Manager requests a separate figure designation.

## AI / accountability

- [x] `docs/AI_PROVENANCE_LOG.md` records material AI use.
- [x] `docs/AI_DISCLOSURE_RECONCILIATION.md` maps actual use to disclosure wording and placement.
- [x] `docs/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md` records the central claim/assumptions/proof logic and explicitly reserves personal author sign-off for Stage 15.
- [x] Manuscript does not claim that AI/computation/Lean constitutes author verification.
- [ ] Personal author approval of the exact final commit/PDF/package — Stage 15 only.

## Fees

- [x] ERE is hybrid.
- [x] Subscription publishing has no APC.
- [x] OA is optional; current official APC is £2490 / $3390 / €2790 plus applicable tax.
- [x] No mandatory submission fee was identified on the current official journal pages.

## Remaining authenticated-portal items

- [ ] Confirm article type / section in Editorial Manager.
- [ ] Confirm file designations for anonymous manuscript source, title page, replication material, and figure.
- [ ] Complete author/declaration/AI/data-code portal fields.
- [ ] Supply or skip optional reviewer suggestions as appropriate.
- [ ] Inspect all portal warnings.
- [ ] Inspect the Editorial Manager-generated review PDF for anonymity, equations, references, figure/table placement, and declarations.
- [ ] Record personal author sign-off on the exact frozen package.
- [ ] Submit.

## Stage-14 status

All non-portal technical items are designed to close under CI. The final Stage-14 verdict may be no stronger than:

**CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT + PERSONAL AUTHOR SIGN-OFF REQUIRED**

until the two human/portal-only items above are completed.
