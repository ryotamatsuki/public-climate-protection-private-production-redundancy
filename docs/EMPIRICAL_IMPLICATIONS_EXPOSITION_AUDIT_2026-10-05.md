# Empirical implications exposition audit — 2026-10-05

**EXPOSITION / EMPIRICAL-IMPLICATIONS ONLY — NO THEORY-FREEZE CHANGE**

Starting main: `86ce214ff467ecea6c3ba79f11f2817d52575261`.
Scientific freeze retained: `PCPPR-THEORY-FREEZE-2026-10-03-v4`.

## Manuscript change

Discussion subsection 9.3, **Empirical implications and testable predictions**, is
inserted after **Risk and readiness primitives** and before **Diagnostic portability**.
It contains three paragraphs (approximately 300 words), with identification in the
last four sentences. Introduction, Model, Equilibrium, Main Results, Welfare,
Institutional Interpretation, Related Literature, Conclusion, and the analytic
appendix are unchanged from starting main. No empirical data, analysis, calibration,
regression, numerical policy interpretation, new theorem, or new citation is added.

The interpretation uses the existing Section 7 and its connection to Section 8.
Geographic alternative production and pre-arranged capacity are proposed indicators;
they are not equated with the conditional success probability in the model.

## Claim and identification audit

| Requested check | Assessment |
|---|---|
| 1. No implicit new theorem | PASS: no formal claim environment or additional comparative static is introduced. |
| 2. Existence versus empirical average effect | PASS: prevalence and quantitative importance remain empirical questions; no average treatment effect is inferred. |
| 3. Readiness variable versus BCP indicators | PASS: indicators are explicitly distinguished from conditional backup success. |
| 4. Causal variation versus correlation | PASS: direct tests need identifying variation; cross-sectional regressions cannot establish causality. |
| 5. Endogenous protection placement | PASS: hazard risk affects policy placement and firm behavior; expected plant location can also affect protection. |
| 6. Strategic interaction identification | PASS: no universal response sign; common shocks, funding, and exposure are alternative explanations for spatial correlation. |
| 7. Welfare scope | PASS: observing the responses does not establish excessive protection when nonindustrial benefits are included. |
| 8. Existing-text duplication | PASS: Section 7 is cross-referenced; the new content concerns measurement, joint testing, composition, heterogeneity, and design. Its existing predictions are preserved. |
| 9. Theory-paper pacing | PASS: three compact paragraphs; no evidence table or empirical result is inserted in the manuscript. |
| 10. Length and layout | PASS: subsection heading and body occupy 428.50 pt of a 648 pt text area, approximately 0.66 pages, wholly on PDF page 20. |

The readiness sign on the symmetric interior protection path and the unilateral
location sign at the canonical origin are distinct results. The subsection explicitly
preserves that distinction. The joint response to one policy improvement is a motivated
empirical hypothesis, not a newly proved all-asymmetric sign claim. Within-firm
readiness and the composition of located firms must be distinguished in a test.

Mobility, interruption losses, access to separate contingency production, and the
social/private availability-value gap are empirical dimensions to examine, not
proved interaction effects. Staggered completion, predetermined infrastructure
plans, and funding eligibility discontinuities are design candidates, not verified
natural experiments. Event-study/DiD use requires attention to anticipation,
differential trends, spillovers, and concurrent development policies.

## Freeze governance

The original v4 scientific-object lock and all author-confirmation records remain
byte identical. The existing non-scientific descendant lock is refreshed for the
explicitly enumerated exposition and audit changes only.

The existing freeze verifier admits exactly one delimited empirical subsection,
rejects formal-claim/equation/exhibit environments within it, and requires removal
of that addition to recover the **entire baseline Discussion byte for byte**.
All its other original mathematical and file-integrity checks remain in force.
Regression coverage verifies that original Discussion edits, new formal claims,
and duplicate addition markers are rejected. This is a narrow exposition exception,
not permission to reopen the risk, welfare, or portability discussion.

No new author scientific confirmation, external human verification, final-package
sign-off, or journal submission is asserted. Verification is AI + COMPUTATION;
any fresh formal result is identified separately in GitHub CI.

## Validation

- Python 3.13.15, direct dependency versions pinned in `requirements.txt`.
- Bibliography/citation scan: all 28 cited keys resolve; both reference source
  files remain byte identical to starting main; no new references.
- LaTeX: three-pass no-shell-escape build and `verify_exposition_v25.py` PASS;
  no unresolved citations/references, rerun warning, or overfull box.
- PDF: 32 baseline pages become 33; subsection is wholly on page 20 and the
  following diagnostic subsection starts cleanly on page 21. This is natural
  repagination, not a one-page empirical insert. Final affected pages are
  visually inspected for clipping, overlap, broken characters, and heading layout.
- Existing symbolic/normalization identities, policy/global exact certificates,
  numerical deviation audit, portability diagnostics, Delta-zero benchmark,
  independent primitive-derived numerical/exact audits, marginal exhibits, and
  anonymous/editorial format checks: PASS.
- Repository regression suite: **31 passed**. The three freeze-governance tests
  also pass separately; the original v4 lock and recovery of the entire prior
  Discussion were independently checked before committing.
- Anonymous editable-source ZIP: clean extracted LaTeX build PASS. The actual
  anonymous replication ZIP's `make verify`: PASS, without editorial files or
  project Git metadata. Submission transport bundle: PASS.
- Committed descendant-integrity gate: PASS; original v4 lock, mathematical
  objects, and complete original Discussion remain preserved. Repository
  `make verify` / Lean CI outcomes are additionally preserved in commit-linked
  check history and build artifacts; no future CI result is predeclared here.

Commands: `make PYTHON=.venv/bin/python exposition`; all remaining `make verify`
components (symbolic, normalization, policy, global, numerical, portability,
benchmarks, independent-audit, test, marginal-exhibits, ere-format,
title-page-format, ere-submission-bundle); `make PYTHON=.venv/bin/python v4-freeze`
after committing. The commit-bound gate requires a clean tracked worktree.
