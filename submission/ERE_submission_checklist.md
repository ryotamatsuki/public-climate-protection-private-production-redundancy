# ERE submission checklist

Target: **Environmental and Resource Economics**

Input theory checkpoint: `7a02e1b8558d8059c72287f2e226b74161ce36b3` (`freeze-pcppr-stage12r-2026-09-14`).

## Journal-format requirements

- [x] Anonymous manuscript for double-blind review.
- [x] Separate title-page file prepared.
- [x] Abstract length: 189 words (journal range 150–250).
- [x] Keywords: 6.
- [x] Mathematical manuscript retained in LaTeX, which ERE accepts.
- [x] Anonymous Data and Code Availability statement included in manuscript.
- [x] Separate Declarations section included in title-page template.
- [ ] Confirm author affiliation, city/country, corresponding e-mail, and ORCID if available.
- [ ] Confirm funding statement.
- [ ] Confirm competing-interest statement.
- [ ] Confirm sole-author contribution statement.

## Editorial positioning

- [x] Climate adaptation and endogenous private resilience are the opening research question.
- [x] General marginal decomposition is surfaced in the introduction.
- [x] Martín-Herrán et al. (2026) added and distinguished near the front.
- [x] Grames et al. (2019) and Zhao et al. (2026) are explicitly separated from the paper's full-game contribution.
- [x] No claim of novelty for public/private adaptation crowd-out itself.
- [x] No change to Stage 12R theorem architecture or canonical witness.

## Double-blind replication package

- [x] Reviewer-facing replication README prepared without identifying information.
- [ ] Build an anonymized ZIP from the required code, certificates, tests, generated outputs, and manuscript-independent instructions.
- [ ] Ensure the ZIP contains no Git metadata, usernames, local absolute paths, author names, e-mail addresses, or repository URLs that reveal identity.
- [ ] Upload anonymized ZIP as supplementary material or to an anonymity-preserving repository at submission.
- [ ] Replace anonymized availability wording with the permanent public repository in the accepted version.

## References and source files

- [ ] Convert DOI entries to full `https://doi.org/...` links where available, consistent with current ERE guidance.
- [ ] Confirm that all references are cited and all cited items appear in the reference list.
- [ ] Supply all editable LaTeX source files at submission.
- [ ] Check figure placement/captions and generated-object reproducibility.

## Final gate

- [ ] Run full `make verify` on the ERE branch.
- [ ] Build title page separately.
- [ ] Review the anonymous PDF for accidental identifying information.
- [ ] Record `STAGE_13_ERE_REPORT.md`.
- [ ] Merge only if all theory/reproducibility checks are green.
- [ ] Create final ERE submission freeze.
