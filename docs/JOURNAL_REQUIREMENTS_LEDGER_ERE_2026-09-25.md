# Environmental and Resource Economics — Journal Requirements Ledger

Access date: 2026-09-25
Target: Environmental and Resource Economics (Springer Nature)

Primary official sources:
- https://link.springer.com/journal/10640/submission-guidelines
- https://link.springer.com/journal/10640/how-to-publish-with-us
- https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation
- https://www.springernature.com/gp/policies/editorial-policies/using-ai-in-research

Evidence hierarchy: current journal-specific instructions > current authenticated portal > publisher-wide policy > internal notes.

| Topic | Current operative rule | Repository/package status | Status |
|---|---|---|---|
| Review model | double-blind; author name/affiliation on separate page | anonymous manuscript + separate ERE_title_page.tex | PASS |
| Self-identification | avoid self-identifying material in review manuscript/data | manuscript empty author; anonymized review archive scan | PASS |
| Editable source | all relevant editable source files at every submission; LaTeX allowed for mathematical manuscripts | dedicated anonymous source ZIP generated and clean-compiled by make verify | PASS after CI |
| Title page | title, author, affiliation, city/country, active corresponding email, ORCID if available | separate title page contains all | PASS |
| Abstract | 150–250 words normally | automated ERE submission check | PASS |
| Keywords | 4–6 | six keywords | PASS |
| Statements / declarations | relevant declarations required | funding, competing interests, ethics/data/code, contribution on title page | PASS |
| Author contributions | contribution statement recommended/required by current publisher policy; separate title page appropriate | revised contribution statement separates human authorship from tool evidence | PASS |
| AI / LLM use | material AI use should be transparently documented; ERE page directs LLM use to Methods or suitable alternative | dedicated AI Assistance Disclosure; reconciliation log | PASS subject to Stage-15 author approval |
| Research data | mandatory sharing; data supporting conclusions available to reviewers/readers; DAS required | no empirical dataset; code/certificates supplied as anonymized review archive; DAS in manuscript/title page | PASS |
| Replication package | public repository required after successful peer review and before final acceptance; editor checklist later | reviewer archive now; public persistent deposit reserved for post-review | PASS for initial submission / FUTURE acceptance action |
| References | cited/accepted works; DOI as full links when available | automated DOI-format check | PASS |
| Tables | Arabic numbering, cited consecutively, captions | two main-text tables, referenced and generated | PASS |
| Figures | electronic; vector preferred EPS; fonts embedded; captions descriptive; accessible; figures normally in body | PDF used in LaTeX plus EPS companion generated; one figure | PASS subject to portal file designation / final visual QA |
| Figure caption | current journal page contains legacy and detailed artwork wording; detailed section places captions in text | caption embedded in manuscript, punctuation cleaned | PASS; portal generated PDF to confirm |
| Source archive clean build | exact uploaded layout should compile | build_verify_ere_source_package.py extracts ZIP and runs pdflatex 3x | PASS after CI |
| Anonymized replication | reviewer access should preserve double-blind | automated forbidden-token scan and ZIP artifact | PASS |
| Originality / simultaneous submission | not previously published and not under consideration elsewhere | cover letter declaration | PASS |
| Reviewer suggestions | allowed; institutional emails/identity evidence recommended if suggested | optional; portal-only decision | NOT APPLICABLE until portal |
| Fees | hybrid; subscription publishing has no APC; OA APC currently £2490 / $3390 / €2790 plus tax | subscription route available | PASS / no mandatory APC |
| Submission fee | no journal submission fee stated on current official pages | none identified | PASS |
| Portal file designations / warnings | authenticated Editorial Manager instructions control | cannot be fully observed outside authenticated portal | UNVERIFIED — PORTAL ONLY |
| Portal-generated review PDF | must be inspected for anonymity/layout before final submit | not yet generated | UNVERIFIED — PORTAL ONLY |
| Final author attestation | personal author approval cannot be automated | Stage-15 sign-off pending | UNVERIFIED — AUTHOR ACTION |

## Current conflicts / ambiguities

The submission-guidelines page contains some legacy wording near the top of the figure section about placing legends after references, while the detailed current artwork section says captions belong in the manuscript and figures should normally appear within the body. The current LaTeX package follows the detailed artwork section. Any portal-specific file designation or generated-PDF behavior will control at authenticated preflight.

## Stage-14 implication

All non-portal technical requirements can be closed by repository CI. Full submission authorization still requires:

1. authenticated Editorial Manager preflight;
2. inspection of the portal-generated review PDF;
3. personal author sign-off on the exact final commit/package.

Accordingly the maximum Stage-14 verdict is conditional until those Stage-15 actions occur.
