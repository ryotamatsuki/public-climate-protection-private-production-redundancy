# Stage 15 v3 — ERE repaired pre-submission freeze

**Date:** 2026-10-02  
**Target:** Environmental and Resource Economics (ERE)  
**Freeze:** `PCPPR-THEORY-FREEZE-2026-10-02-v3`  
**Scientific snapshot head:** `102ade7953bb78d7ab7e453049491a15e692200d`

## Verdict

**REPOSITORY-LAYER V3 RE-FREEZE: PASS**  
**LIVE SUBMISSION AUTHORIZATION: HOLD**

The independent-audit repair cycle is scientifically re-frozen at v3. The
canonical primitive vector and baseline policy-ranking theorem are retained,
while the repaired proof architecture and narrowed claim boundary are now the
frozen object.

## Repairs absorbed into v3

- the former non-Nash policy-equilibrium exhibit is permanently withdrawn;
- Figure 1 reports exact origin marginals only;
- Figure 1 uses solid/dash-dotted series and dotted threshold lines so meaning
  is not encoded by color alone;
- a journal-facing vector file `Fig1.eps` is generated;
- backup-game uniqueness is based on the clipped best-response contraction;
- the strict clipped-backup contraction margin is carried explicitly into the
  open-set persistence argument;
- the open-set IFT step uses the full diagonal derivative
  `G_A,a_Aa_A + G_A,a_Aa_B`;
- the Delta=0 benchmark, welfare scope, prior-art positioning, Lean scope, and
  anonymous reproduction boundary are retained as repaired in PR #31.

## Locked scientific object

The exact Git object identities are recorded in:

`submission/ERE_STAGE15_V3_SCIENTIFIC_OBJECT.lock`

The lock covers the manuscript, formalization, references, tables, tests,
scientific/reproduction scripts, theory-freeze record, mechanism benchmark,
portability results, audit-repair record, pinned Python requirements, canonical
Makefile, and verification workflow.

`make verify` executes `scripts/verify_v3_freeze.py`; any change to a locked
object fails the repository gate until a deliberate new freeze is created.

## Submission package

The current package builder emits:

- anonymous manuscript PDF;
- separate identified title page;
- editable anonymous source ZIP;
- anonymous replication ZIP;
- `Fig1.eps` as the journal-facing vector artwork;
- cover letter and current upload manifest;
- v3 report and v3 scientific-object lock;
- historical Stage-15 controls separated from current controls.

## Remaining non-scientific gates

The following are not closed by the v3 scientific freeze:

- official live ERE submission route;
- live article type;
- live file designations;
- portal-specific declarations;
- portal warnings;
- portal-generated review PDF;
- exact final submission authorization after portal review.

These remain fail-closed.

## Completion condition

After PR #31 is merged, the merge commit must pass the full main-branch
`verify` and `lean-verification` workflows. Only artifacts regenerated from
that green main commit should be treated as the final repository-side
submission package.
