# JPET submission readiness and evidence gate — 2026-11-05

## Scientific
- [x] JPET public-economics scope mapped to official journal aims.
- [x] Exact new gamma=0 positive-planner-optimum globally certified in independent SymPy code and journal CI.
- [x] Exact fixed-readiness and fixed-location policy games fully re-solved with globally verified choices.
- [x] Existing gamma>0 theorem kept unchanged from ERE frozen science.
- [ ] Full closest-parent theorem-absorption check: **Bayindir-Upmann (1998) restricted, UNRESOLVED**.
- [ ] Independent full rerun/third-party mathematical read-through of original gamma>0 certificate bridge and nonempty open set.
- [ ] Author scientific approval of newly added Propositions 4 and 5, their assumptions and AI provenance.
- [ ] Independent confirmation that the contribution meets JPET originality and importance (internal Ref 1 remains BORDERLINE).

## Technical
- [x] Latest successful JPET-specific GitHub Action `41919748445` for commit `a03fb99b8e9aeca21bd92f5ed239d943e9b010f2`, built 38-page PDF and executed new exact SymPy validations.
- [x] PDF text and selected rendered pages checked for added propositions, no '?' broken reference placeholders, bibliography.
- [x] Original ERE mathematical source, formal code, immutable locks not edited.
- [ ] Consolidated, extractable JPET reviewer archive including new `submission/JPET/review_cycles/*.py`, paper sources, exact certificates, bibliography, figures, and verified standalone instructions.
- [ ] Re-run source+pdf preflight after final last documentation commit if it affects package inputs.
- [ ] Provide journal intake metadata, verify live logged-in portal, declarations and publisher requirements at actual submission.
- [ ] Human author checks and explicit submission permission.

## Two separate statuses
- **Scientific R&R Readiness: BORDERLINE** (cannot justify R&R-CALIBER for originality).
- **Technical Submission Readiness: NOT READY** (missing full packaged evidence, parent full text, approvals).

## Required safeguards
Old `make verify` current-branch failure in `verify_final_audit_freeze.py` (unattested tracked JPET files) must not be claimed as a general scientific failure or bypassed via weakening the old lock. New JPET branch requires independent governance certificate. New scientific amendment must not be merged into the official ERE frozen baseline or submitted without human review.

## Source
- https://www.accessecon.com/Pubs/JPET/default.aspx?linkID=442&menu=2&page=content
- https://onlinelibrary.wiley.com/page/journal/14679779/homepage/forauthors.html
- https://onlinelibrary.wiley.com/doi/10.1111/jpet.12632
- https://ideas.repec.org/a/kap/itaxpf/v5y1998i4p471-487.html
