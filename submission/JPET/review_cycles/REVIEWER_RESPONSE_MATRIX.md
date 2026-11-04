# Round 2 updated response matrix — 2026-11-05

| Blocker from previous reviews | Substantive Round 2 evidence | Status for internal R&R gate |
|---|---|---|
| N1: Existing fiscal competition plus private protection may absorb result | Global primitive theorem plus exact +16/189, 0, −16/1593 benefit-gap sign pattern and small gamma>0 persistence; sources explicitly acknowledge Keen–Marchand, Bayindir-Upmann, Matsumoto, Grossman et al | **Resolved enough to support Major R&R, not exhaustively disproved**; full Bayindir theorem text still needed |
| N2: Special rational witness insufficient for significance | Nonempty strict sufficient primitive parameter region and global full-policy Nash/planner proof; new welfare comparative statics, private-response ablations | **Major improvement** |
| M1/M2: No identification of which mechanism matters | Counterfactual derivatives with fixed readiness vs fixed location, both fully re-solved and globally certified | **Closed for stated benchmark only** |
| R1: Gamma0 and zero planner optimum too restrictive | Directly valued benefit produces positive planner; continuity of private Nash and strict global planner/local curvature gives nonempty open gamma>0 region | **Closed as existence, not uniform all gamma** |
| T1/T2: Derivation and global-deviation proof gaps | Exact symbolic identities and global Hessian bounds, Nash best response strict concavity; independent code; original frozen science rerun by JPET CI | **No new counterexample; independent external proof review still desirable** |
| W1: Unrepresentative industrial-only welfare | Explicit augmented direct local benefit and constrained social planner; no blanket adaptation prescription | **Closed as scope clarification, not welfare microfoundation** |
| P1: Historical freeze vs new source CI | Unmodified ERE source verified against archival SHA, new standalone scripts run in separate JPET workflow | **Scientific CI reproducible; combined reviewer bundle pending** |
| L1: Under-citation/closest theorem absorption | Keen–Marchand and Matsumoto added; Ogawa review supports Bayindir capital-not-firm mobility; no unsupported claim of fully read proofs | **Incomplete full-text check acknowledged as major R&R task** |

This is not an assertion that publication is guaranteed. Material new adverse scholarship or mathematical counterexamples veto the internal favorable verdict.

---

## Archived Round 0–1 matrix

# Reviewer comments -> implemented response matrix

| ID | Round 0 objection | Round 1 response | Evidence | Status |
|---|---|---|---|---|
| N1 | Well-known fiscal-competition overprovision plus protection substitution may absorb paper | Narrowed claims; first-order primitive band; structured 10-paper parent map | `PRIOR_ART_THEOREM_ABSORPTION.md`, `NOVELTY_AND_CONTRIBUTION_MATRIX.md`; revised main/Intro/Related | PARTIAL; full Bayindir theorem unavailable |
| N2 | Model-specific existential witness lacks broader interest | Additional exact positive-planner-optimum welfare benchmark; full policy ablation games | new Propositions 4–5, exact SymPy scripts and global Hessian bounds | IMPROVED, not fully closed |
| M1 | Crowd-out conflated with generic overprovision | Separately show readiness affects industrial optimum, hosting affects local attraction, general overprovision may remain without either mechanism | fixed-readiness and fixed-location reoptimized policy equilibria, b=0 test | CLOSED for gamma=0 witness, not universal |
| M2 | Too many IO elements if delta=0 suffices | `Delta=0` minimal mechanism explicit; all gamma>0 observations limited to their own analytical comparative static | new mechanism text and scoped conclusion | PARTIAL |
| T1/T2 | Global validity cannot be inferred from symmetric FOCs | Strict global W Hessian and own-policy concavity; exact independent scripts and CI | `positive_optimum_exact.py`, `restricted_games_exact.py` | CLOSED for new gamma=0 claims; main gamma>0 prior-audit evidence only |
| R1/W1 | Zero planner optimum too extreme for policy application | Symmetric positive planner and excessive local choice under added direct benefits | Proposition 4; distinct augmented welfare explicitly declared | CLOSED as gamma=0 limited robustness, not broad gamma>0 |
| P1 | New proof must not inherit obsolete ERE freeze | Dedicated JPET CI; old immutable freeze untouched; disclosures corrected | `.github/workflows/jpet-candidate.yml`, README/checklist | PARTIAL; JPET replication bundle unassembled |
| E1 | Readability and journal fit | JPET narrative, reviewer-oriented statements, revised abstract and conclusion | 38-page compiled PDF, references | IMPROVED |
| A1 | New science needs human approval | Explicitly classified unapproved separate science, no merge or submission | README/checklist and PR discussion | OPEN, requires author |

No row is marked CLOSED if evidence is only an on-path FOC or unpublished inference.
