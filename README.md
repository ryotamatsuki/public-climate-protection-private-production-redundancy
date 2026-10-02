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
issue-to-evidence map and validation. Earlier Stage 13--15 PASS/freeze records
are historical records for their old candidate, not certifications of this
revision. The Stage 15 pre-submission repository freeze was reopened for these
repairs; its scientific-object lock is not silently renewed.

The resulting submission candidate remains subject to author scientific review
and live journal-portal requirements. No automated check establishes editorial
novelty, journal acceptance, or final submission authorization.

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
Historical Stage verifiers are retained for provenance but are excluded from
the current scientific reproduction gate.
