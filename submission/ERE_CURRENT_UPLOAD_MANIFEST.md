# ERE upload components — independent-audit repair

This supersedes the Stage-15 upload candidate for the repaired manuscript.
Historical Stage records are retained as history, not current scientific
certification. The build records the source commit and per-component SHA-256
hashes. Regenerate the bundle from the final committed source.

| Component | Generated file | Audience / designation |
|---|---|---|
| Anonymous manuscript | `paper/main.pdf` | Reviewer-facing manuscript |
| Separate title page | `submission/ERE_title_page.pdf` | Editorial author information/declarations |
| Editable anonymous source | `dist/ERE_anonymous_manuscript_source.zip` | Manuscript source; anonymous |
| Anonymous replication | `dist/ERE_anonymous_replication.zip` | Reviewer supplementary code/certificates |
| Vector artwork | `figures/Fig1.eps` | Figure 1 vector artwork; exact origin marginals with non-color line encoding |
| Cover letter | `submission/ERE_cover_letter.md` | Editorial only |
| Transport bundle | `dist/ERE_submission_ready_bundle.zip` | Author/editorial transport only; contains identifying material |

Do not submit the whole transport bundle as an anonymous supplement. Its
`07_controls` directory contains the current repair report and checklist;
`08_historical_controls` contains the superseded Stage-15 records. Neither is
intended as evidence of theorem correctness or novelty for referees.

The independent-audit repair does not perform live submission. Confirm the
current official portal, article type, file designations, declaration fields,
and the portal-generated reviewer PDF before author submission. The dated
requirements ledger records unresolved live-portal items; it is not a claim
that a blocked endpoint has become operational.
