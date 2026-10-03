# Public Climate Protection and Private Production Redundancy

Manuscript and replication source for **Public Climate Protection and Private
Production Redundancy: Local Resilience Competition, Plant Location, and
Disaster-State Market Power**. Journal target: *Environmental and Resource
Economics (ERE)*.

## Current revision

The 2026-10-02 independent audit identified an invalid numerical equilibrium
curve, two proof defects, an incomplete mechanism/novelty comparison, and
standalone anonymous-package failures. The audit repair retains the canonical
primitives and global baseline ranking while correcting those objects and
narrowing the claims. See `docs/INDEPENDENT_AUDIT_REPAIRS_2026-10-02.md` for the
issue-to-evidence map and validation. Earlier Stage 13--15 PASS/freeze records are historical records for their old
candidate, not certifications of this revision. The independent-audit repair is
re-certified under workflow v2.5 and is now frozen as
`PCPPR-THEORY-FREEZE-2026-10-03-v4`, with refreshed Stage-6/7.5A evidence,
author scientific reconfirmation, and a new CI-enforced scientific-object lock.

The resulting submission candidate remains subject to live journal-portal
requirements and final submission authorization. No automated check establishes
editorial novelty or journal acceptance.

## Main result and boundary

Within the maintained symmetric baseline family, the coordinated
**protection-policy** objective has a unique zero optimum at the canonical
witness, while a positive symmetric policy Nash equilibrium satisfies global
unilateral incentives. Strict margins and the full diagonal FOC derivative
support persistence in an open neighborhood. Private location, readiness and
Cournot behavior remain in place in the coordinated benchmark; welfare covers
industrial surplus and resilience costs.

The minimal mechanism is a social/private readiness wedge combined with plant
attraction. Incremental disaster-state monopoly rents and strategic backup
substitution are **not necessary**: an exact Delta=0 benchmark proves the same
ranking with different interiority-maintaining parameters. Oligopoly affects
readiness and correlated-risk responses. Figure 1 now plots exact origin
marginals, **not policy-equilibrium levels across gamma**. Nonlinear-risk and
logistic-location exercises are explicitly numerical diagnostics; matched
origin slopes/densities create some of their agreement by construction.

## Reproduce

Use Python 3.13, the direct dependency pins in `requirements.txt`, GNU Make,
and LaTeX:

```bash
python -m pip install -r requirements.txt
make verify
```

This runs symbolic and normalization identities, whole-domain exact
certificates, the diagonal-root derivative and clipped-backup contraction,
numerical FOC/deviation searches, the exact mechanism benchmark, regression
tests, exact exhibit checks, anonymous and editorial format checks separately,
LaTeX builds, and reproduction from the actual anonymous ZIP in a temporary
directory without a project Git checkout. It creates:

- `paper/main.pdf`: anonymous manuscript.
- `submission/ERE_title_page.pdf`: separate editorial identity/declarations.
- `dist/ERE_anonymous_manuscript_source.zip`: clean-compiled editable source.
- `dist/ERE_anonymous_replication.zip`: anonymous standalone reproduction.
- `dist/ERE_submission_ready_bundle.zip`: author/editorial transport bundle.

The transport bundle includes identifying editorial files and controls; submit
its individual components with the correct portal designations, never the
whole bundle as an anonymous reviewer supplement. Portal requirements are in
`submission/ERE_submission_checklist.md` and the dated live-requirements ledger.

## Partial formalization

```bash
make formal-verify
```

This regenerates certificates before restoring the pinned mathlib cache and
building Lean 4.32.1. `formal/README.md` distinguishes generic implications,
model-specific premises, unformalized bridges/open-set persistence, and
`native_decide`'s native compiler/runtime trust. The build writes the theorem
axiom report. The full economic theorem is not a closed Lean statement.

The anonymous archive's corresponding commands are also `make verify` and
`make formal-verify`; neither depends on the editorial title page or the paper's
Git history. Formal dependency installation requires the Git command and
network access, even though the extracted project has no Git metadata.

Current freeze controls:
- `docs/THEORY_FREEZE.md`: v4 theory freeze.
- `submission/ERE_STAGE15_V4_SCIENTIFIC_OBJECT.lock`: exact Git-object lock.
- `STAGE_15_V4_REPORT.md`: workflow-v2.5 recertified pre-submission freeze report.
- `scripts/verify_v4_freeze.py`: CI gate enforcing the lock.
- `docs/STAGE_6_RECERTIFICATION_2026-10-03.md` and `docs/STAGE_7_5A_RECERTIFICATION_2026-10-03.md`: current novelty/scope certificates.

Historical Stage verifiers and the former Stage-15 lock are retained for
provenance but are not current scientific certifications.

## Independent final audit (2026-10-03)

The adversarial audit starts from GitHub main `990bbe13dd1c3470b378ccd0040a78a030750701`, not from prior PASS decisions. See [the full audit](docs/INDEPENDENT_FINAL_AUDIT_2026-10-03.md), [independent derivations](docs/INDEPENDENT_MATHEMATICAL_AUDIT_2026-10-03.md), [novelty/portability mappings](docs/INDEPENDENT_NOVELTY_PORTABILITY_AUDIT_2026-10-03.md), and [ERE requirements](docs/ERE_REQUIREMENTS_AND_DESK_AUDIT_2026-10-03.md).

`make independent-audit` runs separately written primitive-derived numerical and exact checks, then compares the production bridge. `make verify` includes these checks and clean anonymous reproduction. Fresh outputs are under `dist/`; dated snapshots are under `docs/`. The [freeze-governance note](docs/FINAL_AUDIT_FREEZE_GOVERNANCE_2026-10-03.md) preserves the immutable v4 lock and pins the non-scientific descendant separately. No new author scientific confirmation or live-submission approval is supplied by this audit.
