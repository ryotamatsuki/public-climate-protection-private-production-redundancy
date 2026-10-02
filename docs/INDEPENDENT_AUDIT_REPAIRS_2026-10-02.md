# Independent audit repairs — 2026-10-02

The repair starts from `581a7fa499267f34774faafe6dcc0bd961f34965` and responds
to the author's request to correct the independent audit. It retains the
canonical primitives and material surplus accounting. Earlier PASS/freeze
records were treated as historical author-side assertions, not correctness
evidence. Their active role has been superseded explicitly, not silently
renewed by changing a lock.

## Issue-to-repair map

| Audit issue | Concrete repair | Scientific boundary / verification |
|---|---|---|
| F1: plotted non-Nash policy at gamma=0.474 | Replace the whole policy-equilibrium curve with exact origin MS/ML marginals. Remove its obsolete CSV. | All 101 rational points and both isolated roots checked. No global policy ranking across the figure interval is claimed. The former profitable deviation is a regression case. |
| M1: necessary mechanism and nearest prior art | Derive the social/private readiness wedge; add an exact Delta=0 global witness; compare Grossman--Helpman--Lhuillier and regional public-input competition explicitly. | Delta=0 does not eliminate own-product markups. Its k,c differ from the canonical witness. No automatic conclusion of publishable novelty follows. |
| M2(a): false unclipped-interiority claim | Use 1-Lipschitz clipping and Delta*q0/k=75600/162409<1 to exclude all other backup fixed points. | Certifies the clipped action game; interiority of the linear solution is checked separately. |
| M2(b): wrong IFT derivative | Use F'=G_A,AA+G_A,AB. Add its exact root-square Bernstein check and record root multiplicity one/nonzero denominator. | Own-policy concavity establishes global incentives; the diagonal derivative establishes root persistence. |
| M3: anonymous commands fail | Split anonymous manuscript from editorial title-page checks. Include generated Lean payloads and regenerate them as prerequisites. | Run advertised commands from the actual ZIP without a project Git checkout; formal integration also deletes generated files first. Git is needed only to fetch pinned external Lean dependencies. |
| M4: welfare/planner/b scope | Define a protection-policy-constrained industrial planner and ex ante immobile-factor hosting benefit. Separate pure transfer interpretation. | No first-best, regional ownership microfoundation, realized-employment or all-project-benefits claim. Adding mu to each policy changes MS by 2mu. |
| M5: unproved benchmark absence | Withdraw universal absence; fixed-location/readiness interventions identify removed derivatives only. | Exact Delta=0 benchmark is a separate fully solved polynomial game. |
| M6: Lean assumptions / native trust | Add reader-facing formal scope map, appendix and AI statement. Print native arithmetic dependencies. | Final theorem takes full-domain signs and semantic bridges as hypotheses. Clipped-game uniqueness and open-set persistence remain outside Lean. |
| M7: portability overinterpretation | Explain matched-density logistic equality of symmetric FOC and matched-risk-slope equality at origin. Validate continuous-FOC candidates against boundaries and all grid-detected payoff peaks. | Numerical searches only; no whole-square theorem for either alternative. |
| Minor: file clipping / bibliography / pins | Breakable paths with xurl; alphabetical bibliography; formal SSRN citation/date; pytest pin and b guard. | Source and actual submitted PDF inspected separately from mathematical proof. |
| Additional package defect found during repair | Replace recursive fnmatch selection by path glob selection. | A local mathlib cache must not be accidentally included in formal/*.lean archive selection. |
| Additional formal reproduction defect found during execution | Build all thirteen proof modules and check Main.lean with Lean, instead of linking the optional executable. | The pinned mathlib proof cache supplies C sources but no C object files. The default executable build would compile the whole imported mathlib; proof checking does not require that link step. |
| Git-derived identity in newly generated payload | Use a primitive identifier, source SHA-256 and content archive hashes; keep repository commit provenance outside anonymous payload. | Anonymous outputs contain no author identity or repository commit metadata. Public title search remains possible, as for any public working paper. |

## Reconstructed mathematical checkpoints

| Object | Result |
|---|---:|
| Canonical MS | -0.006482464222763817 |
| Canonical ML | +0.0019308655211414177 |
| Canonical lambda | +0.032286196153021564 |
| Canonical symmetric root | in (1649737/71666359, 380091/16511564) |
| Full diagonal FOC derivative at root | approximately -0.18003285 |
| Clipped-backup Lipschitz bound | 75600/162409 < 1 |
| Delta=0 MS, ML | -3/16, 5/128 |
| Delta=0 Nash policy | 1/126 |
| Added direct-benefit origin threshold | mu > 0.00324123212 makes the common marginal positive |

The four availability-state surplus values and readiness/public costs are
unchanged. The new readiness wedge is derived by subtracting the private FOC
from the social derivative. Saved real readiness costs are retained.

## Validation procedure

Local validation uses Python 3.13.15 with the pinned direct requirements and `make verify`. The current target
runs exact and numerical checks, eleven repository regressions (ten scientific regressions in the anonymous ZIP), 101-point marginal
exhibit validation, anonymous/editorial checks separately, PDF builds, clean
source-ZIP compilation, and the full advertised Python/LaTeX command from the
actual replication ZIP. The archive supplies generated Lean certificates,
their exact JSON source archive, and a scope map.
The final manuscript build checks a complete PDF header/trailer, resolved
references/citations, and absence of overfull boxes. All 31 manuscript pages
and the separate title page were rendered and inspected after the scientific
edits.

`make formal-verify` regenerates dependencies and builds the pinned Lean
project, printing axiom dependencies. CI additionally extracts the actual
reviewer ZIP into a fresh directory, deletes its generated certificates, and
executes that advertised command. Build success checks executable reproduction
and encoded implications; it does not discharge unformalized model premises.
The workflow run tied to the repair commit is the build provenance. Local
Python/PDF execution and remote native Lean execution are recorded separately;
no earlier CI status is reused as verification.

## Prior-art evidence

The revision uses primary publisher or author sources:

- Grossman, Helpman and Lhuillier (2023), *JPE* 131(12), 3462--3496,
  https://doi.org/10.1086/725173 . Author manuscript:
  https://www.princeton.edu/~grossman/SupplyChainResilienceJPE.pdf .
- Gnutzmann, Kowalewski and Spiewanowski (2020), *AJAE* 102(3), 911--933,
  https://doi.org/10.1093/ajae/aaz041 .
- Bacchiocchi, Bellocchi and Coveri (2024), *Economic Analysis and Policy* 84,
  1490--1508, https://doi.org/10.1016/j.eap.2024.10.023 . The comparison is
  restricted to the published abstract's government/location/disruption scope.
- Gawel, Lehmann, Strunz and Heuson (2018), *Journal of Institutional Economics*
  14(3), 473--499, https://doi.org/10.1017/S1744137416000163 .
- Zhao, Yang and Zhang (2026), working paper SSRN 6996377, posted 25 June,
  https://doi.org/10.2139/ssrn.6996377 . The indexed primary abstract was checked;
  unavailable full text was not represented as read.

The bibliography is alphabetized and the reference keys are synchronized across
TeX and BibTeX. Established components are acknowledged. The distinct question
is the protective-input policy ranking with an endogenous private substitute;
there is no claim that a new combination alone proves sufficient novelty for ERE.

## What remains a judgment rather than a software repair

ERE can still judge the contribution incremental or prefer a different economic
microfoundation. The revised manuscript makes the minimum mechanism and
constrained welfare scope reviewable; it cannot guarantee acceptance. Author
scientific review and the official live portal's article type, file designation,
declaration fields, and generated review PDF remain separate. No submission,
editor contact, approval inference, or author-confirmation impersonation is
performed by this repair.
