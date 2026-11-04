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
