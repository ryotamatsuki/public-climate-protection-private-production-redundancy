# ERE submission checklist

Target: **Environmental and Resource Economics**

Input theory checkpoint: `7a02e1b8558d8059c72287f2e226b74161ce36b3` (`freeze-pcppr-stage12r-2026-09-14`).
Stage 13 submission checkpoint: `b1bc210e8dce59455466fa2113e1c178c5756208` (`checkpoint-stage13-ere-2026-09-14`).

## Journal-format requirements

- [x] Anonymous manuscript prepared for double-anonymous review.
- [x] Separate title-page file prepared.
- [x] Abstract length within the journal range (150–250 words).
- [x] Six keywords.
- [x] Mathematical manuscript retained in LaTeX.
- [x] Anonymous Data and Code Availability statement included in manuscript.
- [x] Separate Statements and Declarations section included in title page.
- [x] Author affiliation, city/country, corresponding e-mail, and ORCID finalized.
- [x] Funding statement finalized: no external funding.
- [x] Competing-interest statement finalized: none declared.
- [x] Sole-author contribution statement finalized.
- [x] AI-assistance disclosure included and author responsibility stated.

## Editorial positioning

- [x] Climate adaptation and endogenous private resilience are the opening research question.
- [x] General marginal decomposition is surfaced in the introduction.
- [x] Martín-Herrán et al. (2026) is distinguished near the front.
- [x] Grames et al. (2019) and the 2026 Zhao–Yang–Zhang working paper are explicitly separated from the paper's full-game contribution.
- [x] No claim of novelty for public/private adaptation crowd-out itself.
- [x] No change to Stage 12R theorem architecture or canonical witness.

## Double-anonymous replication package

- [x] Reviewer-facing replication README prepared without identifying information.
- [x] Anonymized ZIP generated from required code, certificates, tests, generated outputs, and instructions.
- [x] ZIP contains no Git metadata, usernames, local absolute paths, author names, e-mail addresses, or identifying repository URLs.
- [x] GitHub Actions uploads the anonymous ZIP as a workflow artifact.
- [x] Accepted-version availability wording is reserved for replacement with a persistent public repository after review.

## References and source files

- [x] DOI links use `https://doi.org/...` where supplied in the manuscript reference list.
- [x] Zhao–Yang–Zhang (2026) is identified in text as a working paper rather than presented as a journal article.
- [x] LaTeX build completes without unresolved citations or cross-references under the repository verification pipeline.
- [x] Editable LaTeX source files are retained for portal upload.
- [x] Figure placement/caption style and generated-object reproducibility checked.

## Final preflight

- [x] Full `make verify` passed on Stage 13 and will be rerun on the Stage 14 final branch head.
- [x] Title page builds separately.
- [x] Anonymous manuscript visually inspected for identifying information and layout problems.
- [x] Anonymous review artifact digest recorded from Stage 13 main run.
- [x] Cover letter finalized.
- [x] Exact upload set defined: anonymous manuscript/source files, separate title page, cover letter, and anonymized replication archive.
- [x] Portal metadata prepared: title, abstract, six keywords, JEL H73/L13/Q54/R38, author details, declarations, and AI-use disclosure.
- [ ] Actual upload/submission in the ERE portal (outside the Stage 14 repository gate).
