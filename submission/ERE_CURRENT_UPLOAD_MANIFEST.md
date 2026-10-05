# ERE upload components — independent final audit, 2026-10-03

This supersedes the former Stage-15 upload candidate for the repaired
manuscript and is governed by
`PCPPR-THEORY-FREEZE-2026-10-03-v4`.
The original v4 lock remains immutable and is checked against canonical
main 990bbe13dd1c3470b378ccd0040a78a030750701. A separate
ERE_FINAL_AUDIT_DESCENDANT.lock.json pins every changed/new audit file.
Historical Stage records are retained as history, not current independent
evidence. The build records the source commit and per-component SHA-256
hashes. Regenerate the bundle from the final green main commit after this independent final-audit PR is merged.

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


## Current freeze controls

- `docs/INDEPENDENT_FINAL_AUDIT_2026-10-03.md`
- `docs/FINAL_AUDIT_FREEZE_GOVERNANCE_2026-10-03.md`
- `submission/ERE_FINAL_AUDIT_DESCENDANT.lock.json`
- `STAGE_15_V4_REPORT.md` (immutable baseline history)
- `submission/ERE_STAGE15_V4_SCIENTIFIC_OBJECT.lock`
- `docs/STAGE_6_RECERTIFICATION_2026-10-03.md`
- `docs/STAGE_7_5A_RECERTIFICATION_2026-10-03.md`

Only artifacts regenerated from the green main-branch merge commit are final
repository-side submission objects.

## 2026-10-05 exposition update

Discussion subsection 9.3 adds empirical measurement and identification implications.
Classification: **EXPOSITION / EMPIRICAL-IMPLICATIONS ONLY — NO THEORY-FREEZE CHANGE**.
The v4 scientific lock remains immutable; the non-scientific descendant lock pins
the added prose and its narrow governance exception. The audit is in
`docs/EMPIRICAL_IMPLICATIONS_EXPOSITION_AUDIT_2026-10-05.md`.
Regenerate all manuscript/source/replication components from the final commit;
earlier PDF and ZIP components omit this subsection. This update does not supply
personal final-package sign-off or live journal submission authorization.


## 2026-10-05 AI disclosure compliance re-freeze

The manuscript AI Assistance Disclosure was expanded for submission transparency to identify the material OpenAI tool/model families, the September–October 2026 use period, and the categories of prompts used. This is classified as **SUBMISSION COMPLIANCE / AI DISCLOSURE ONLY — NO THEORY-FREEZE CHANGE**.

The scientific freeze remains `PCPPR-THEORY-FREEZE-2026-10-03-v4`. The immutable v4 scientific lock is unchanged; the non-scientific descendant lock pins the revised manuscript, updated provenance log, and `docs/AI_DISCLOSURE_COMPLIANCE_REFREEZE_2026-10-05.md`.

Regenerate the manuscript PDF and all submission archives from the final green main commit. Authenticated portal preflight and author approval of the portal-generated reviewer PDF remain external final gates.
