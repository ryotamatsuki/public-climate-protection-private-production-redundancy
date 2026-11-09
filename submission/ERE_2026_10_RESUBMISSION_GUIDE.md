# ERE technical-check resubmission — 2026-10-18

**Manuscript:** EARE-D-26-02567 — *Public Climate Protection and Private Production Redundancy: Local Resilience Competition, Plant Location, and Disaster-State Market Power*

## Basis: editorial messages, 2026-10-10 and 2026-10-13

The 10 October sent-back notice requested (i) identical author names in the submission metadata and manuscript and (ii) removal of the manuscript Appendix and upload as a separately designated supplementary file. The 13 October personal editorial response additionally requests that **Data and Code Availability statements be absent from the blinded manuscript**, under the journal's double-blind rules. The 13 October automatic incomplete-submission reminder states that a submission not completed or answered within 14 days may be removed.

The metadata/name discrepancy remains **unexplained**: the submitting author reported that both Editorial Manager and the separate title page display "Ryota Matsuki", and the 13 October reply did not identify any offending field. Do not silently change the author name. Verify the metadata, PDF author field, and author order in the portal.

## Build instructions

Run on a checkout with LaTeX, Python dependencies and poppler-utils:

```bash
python -m pip install -r requirements.txt
make objects ere-title-page
python -m pytest -q tests/test_ere_editorial_resubmission.py
python scripts/build_ere_editorial_resubmission.py
```

The outputs under `dist/ERE_editorial_resubmission/` are:

| Output | Portal designation |
|---|---|
| `ERE_blinded_manuscript.pdf` | Manuscript (blinded), replacing the old combined paper/main.pdf |
| `ERE_supplementary_appendix.pdf` | Supplementary File (Appendix) |
| `ERE_title_page.pdf` | Title Page / author information only |
| `ERE_anonymous_editable_source.zip` | Optional source upload, only if requested |
| `COMPONENT_SHA256.json` | Internal QA audit, do not submit unless asked |
| `UPLOAD_INSTRUCTIONS.txt` | Internal guidance, do not submit |

**Do not submit the old `paper/main.pdf` as the blinded manuscript.** The canonical `paper/main.tex` is intentionally unchanged to preserve the 2026-10-03 v4 scientific freeze and existing descendant audit. The new script derives a journal-facing version that includes the full scientific main text and reference list while moving the Appendix into its own cross-referenced PDF. All subsection content, theorem statements, mathematical derivations, figures, and citation definitions are unmodified. The separate title page retains data and code declarations outside the blinded manuscript. The manuscript's existing AI Assistance Disclosure remains (journal did not request its deletion).

**Separate replication archive:** The prior `dist/ERE_anonymous_replication.zip` remains an independently prepared code/certificates artifact. It is not the Appendix requested by the editor. Provide it as an additional supplement only under the applicable portal designation; do not replace the required Appendix PDF with it.

## Portal actions remaining (manual and not executed here)

1. Sign in at https://www.editorialmanager.com/eare/ and open **Submissions Sent Back to Author → Edit Submission**.
2. Check authorship metadata against the editorial-only title page. There is no known corrected spelling to apply.
3. Replace the old manuscript with `ERE_blinded_manuscript.pdf`.
4. Add `ERE_supplementary_appendix.pdf` under **Supplementary File** and retain the Title Page separately.
5. Build the portal PDF, inspect all text, figures, supplementary designations, anonymous metadata and references; explicitly approve and complete the submission.
6. Confirm the portal status changes to a submitted state; submission is not completed by GitHub Actions alone.

The 13 October reminder's 14-day warning indicates action should be taken *before 27 October 2026* (confirm the exact cutoff with the editorial office if necessary).

## Boundaries and audit classification

**EDITORIAL FORMAT / DOUBLE-BLIND COMPLIANCE ONLY — NO THEORY-FREEZE CHANGE.** The canonical scientific source files and original locked descendant remain unchanged. The script asserts exact markers, checks anonymous PDF text and independently compiles the extracted editable source ZIP. A dedicated GitHub Actions job exposes the PDFs as a workflow artifact. The original submission pipeline remains historical and can still render the old unsplit `paper/main.pdf`; that artifact is not suitable for this resubmission.

No claim is made that ERE has accepted, approved, or processed this revision.
