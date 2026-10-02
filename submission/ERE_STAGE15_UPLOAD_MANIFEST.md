# ERE Stage-15 Upload Manifest

Target: **Environmental and Resource Economics**  
Prepared: **2026-10-02**  
Scientific object base: `f0f86daa29bec6574cb4103050b1a18295928227`

This manifest defines the repository-complete submission object. Portal-specific file designations are deliberately not hard-coded; the live authenticated portal is authoritative.

## Submission files

1. **Anonymous manuscript PDF** — `paper/main.pdf`
2. **Identified title page PDF** — `submission/ERE_title_page.pdf`
3. **Editable anonymous manuscript source** — `dist/ERE_anonymous_manuscript_source.zip`
4. **Anonymous replication/reviewer package** — `dist/ERE_anonymous_replication.zip`
5. **Vector artwork companion** — `figures/policy_regime.eps` if the live portal requests separate artwork
6. **Cover letter text** — `submission/ERE_cover_letter.md`
7. **Submission checklist** — `submission/ERE_submission_checklist.md`
8. **Latest live-requirements ledger** — `docs/STAGE_14_LIVE_REQUIREMENTS_LEDGER_ERE_2026-10-02.md`
9. **Stage-15 report** — `STAGE_15_REPORT.md`

## Single transport bundle

`make verify` also builds:

`dist/ERE_submission_ready_bundle.zip`

The bundle contains the items above in a stable directory layout plus a generated `SOURCE_COMMIT.txt`.

## Upload order

Use the live portal's actual designations. The intended semantic order is:

1. identified title page;
2. anonymous manuscript;
3. editable source archive;
4. replication/reviewer material;
5. separate vector artwork only if requested;
6. cover letter / portal cover-letter field.

Do not infer portal designations from this manifest.

## Final portal review

Before the author selects the final submission action, inspect the portal-generated review PDF for:

- no author identity in the anonymous manuscript;
- title page separated correctly;
- complete equation rendering;
- complete tables and figures;
- references present and ordered correctly;
- declarations appearing only where intended;
- no missing pages;
- no source-package conversion warning;
- no unexpected portal-added metadata.

The final submission action remains blocked until these checks and the live portal questions are completed.
