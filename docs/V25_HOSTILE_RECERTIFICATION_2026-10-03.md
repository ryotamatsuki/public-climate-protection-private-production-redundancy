# v2.5 Hostile Re-Certification Audit — 2026-10-03

Project: **Public Climate Protection and Private Production Redundancy**  
Audited canonical main: `2eec56e8cd22c96c5de4e81b7c88dfd9abb4080c`  
Current declared freeze: `PCPPR-THEORY-FREEZE-2026-10-02-v3`  
Workflow: `ryotamatsuki/research-paper-workflow/THEORY_PAPER_RESEARCH_PIPELINE.md`, v2.5

## Executive verdict

**NO NEW FATAL MATHEMATICAL DEFECT FOUND.**

**WORKFLOW VERDICT: RECERTIFICATION REQUIRED — ROLLBACK TO STAGE 6.**

The repaired canonical theorem survives an independent Stage-4A-style reconstruction and
the current exact/Lean machinery is materially more defensible than the superseded candidate.
However, the v2.5 workflow does not permit the present v3 freeze to remain the final
submission freeze because the hostile re-audit found a Stage-6 prior-art completeness
regression and downstream Stage-7.5A / Stage-13 certification artifacts that are stale
relative to the 2026-10-02 repair.

No finding below presently requires changing the canonical primitive vector, welfare
formula, or headline theorem. The expected repair path is literature/certification/package
repair followed by re-freeze, not theory reconstruction.

## Severity ledger

| ID | Earliest stage | Severity | Finding | Current impact |
|---|---|---|---|---|
| R1 | Stage 6 | **MAJOR BUT FIXABLE / CERTIFICATION REGRESSION** | Kousky, Luttmer & Zeckhauser (2006), *Private Investment and Government Protection*, was omitted from the theorem-absorption map and manuscript positioning. | v3 novelty certification is incomplete. |
| R2 | Stage 6 | **MINOR-to-MAJOR positioning gap** | Application-stripped search also identifies Mahmud & Barbier (2016), Lee & Pinto (2009), and Hickey et al. (2021) as relevant public/private-protection parent classes. | At minimum they belong in the hostile absorption map; selected citations may belong in the manuscript. |
| R3 | Stage 7.5A | **MAJOR BUT FIXABLE / CERTIFICATION REGRESSION** | The dated v2.4 Contribution Robustness Certificate overstates independence/orthogonality of the diagnostic alternatives relative to the repaired manuscript's more accurate account. | Stage 7.5A certificate is stale and must be refreshed. |
| R4 | Stage 7.5A / 8 | **MAJOR BUT FIXABLE / HUMAN-ACCOUNTABILITY BLOCKER** | The current Author Intellectual-Contribution Record is the 2026-09-25 record and does not personally confirm the repaired proof logic, Delta=0 benchmark, and revised novelty boundary. | Latest workflow does not permit final theory freeze from mere approval of AI output or CI. |
| R5 | Stage 13 | **MINOR / STALE CERTIFICATE** | The v2.5 exposition report says the manuscript has three main-text exhibits including a nested-benchmark table; the current manuscript has one figure and one table. | Manuscript is not harmed, but the Stage-13 evidence record is stale. |
| R6 | Stage 14 | **MINOR / PACKAGING REGRESSION** | The main-run `ERE-submission-components` artifact still uploads `figures/policy_regime.eps`; the transport bundle correctly contains `05_artwork/Fig1.eps`. | Final transport bundle is correct, but the convenience component artifact is inconsistent with the current upload manifest. |
| R7 | Stage 14 | **UNRESOLVED INSTRUCTION CONFLICT** | ERE's current page says figure legends should be placed after the references, while its later artwork instructions say figures should be in the body and captions in the text file. | Record as a live-requirement conflict; resolve at live portal/preflight rather than silently guessing. |

## Stage 4A — Independent mathematical adversarial certification

### Verdict

**GO — no new Stage-4A mathematical failure found.**

### Independent reconstruction

The audit reconstructed the economic model from the manuscript primitives rather than
accepting the repository PASS labels:

- Cournot and monopoly continuation;
- four availability states;
- backup FOCs and clipped best responses;
- Bayesian location cutoff;
- national surplus, planner welfare, and local-government payoff;
- canonical planner optimization;
- symmetric local-policy FOC;
- unilateral best response to the symmetric candidate.

An independent numerical evaluator, written from the manuscript equations rather than
importing the production code, reproduced:

- planner maximum at ((0,0));
- a single detected symmetric FOC root near (0.0230196849);
- the same root as the global unilateral best response against the rival root;
- both unilateral boundaries strictly below the equilibrium payoff;
- no additional first-stage equilibrium in a multistart best-response search.

These numerical checks are falsification evidence, not substitutes for the repository's
exact proof.

### Exact proof-chain audit

The current exact proof architecture is coherent:

1. the feasible backup game uses **clipped** best responses;
2. clipping is 1-Lipschitz and the canonical bound
   (Delta q_0/k=75600/162409<1) yields a contraction;
3. exact whole-square certificates separately establish that the fixed point is interior;
4. location endpoint interiority makes the affine probability best response globally
   unclipped and (|B|<1), excluding asymmetric probability fixed points;
5. exact Bernstein signs establish both planner partial derivatives are negative on the
   complete policy square;
6. exact root isolation gives the positive symmetric local-policy stationary point;
7. own-policy strict concavity on the full feasible own-action interval makes that point
   the unique global best response to itself;
8. the open-set proof now correctly uses
   (F_a=G_{A,a_Aa_A}+G_{A,a_Aa_B}), not own concavity alone;
9. the open-set proof explicitly preserves the strict clipped-backup contraction margin.

The Bernstein basis transformation used by the certificate was independently
stress-tested against direct random-polynomial evaluation; no transformation defect was
found.

### Multiplicity / boundary distinction

The manuscript does **not** claim uniqueness of the full first-stage policy equilibrium.
It claims existence of a positive symmetric Nash equilibrium and uniqueness of the
planner optimum and downstream continuations where stated. The current proof therefore
does not improperly infer D2 (no alternative policy equilibrium) from D1 (no profitable
deviation at the claimed equilibrium).

### Stage-4A conclusion

No FATAL or MAJOR mathematical repair is currently indicated.

## Stage 6 — Theorem-level novelty re-kill

### Verdict

**ROLLBACK REQUIRED — prior-art completeness regression, theorem not absorbed.**

### Newly located closest prior art

#### Kousky, Luttmer & Zeckhauser (2006)

Carolyn Kousky, Erzo F. P. Luttmer, and Richard J. Zeckhauser,
“Private Investment and Government Protection,”
*Journal of Risk and Uncertainty* 33, 73–100.
DOI: https://doi.org/10.1007/s11166-006-0172-y

This paper is materially closer than the current audit record recognizes. It models
government disaster protection and endogenous private investment in risk-prone locations,
and explicitly emphasizes that greater protection attracts more private capital and can
produce non-concave protection benefits and multiple equilibria.

It therefore absorbs any broad claim that the paper is first to connect **public disaster
protection to endogenous private capital/location**.

However, it explicitly states that it does **not** analyze complementarity or
substitutability between private and public investments in protection. It also does not
contain the present two-jurisdiction mobile-oligopoly policy competition with endogenous
geographic backup readiness.

**Absorption verdict: PARTIALLY ABSORBED, NOT FULLY ABSORBED.**

#### Mahmud & Barbier (2016)

Sakib Mahmud and Edward B. Barbier,
“Are private defensive expenditures against storm damages affected by public programs
and natural barriers? Evidence from the coastal areas of Bangladesh,”
*Environment and Development Economics* 21(6), 767–788.
DOI: https://doi.org/10.1017/S1355770X16000164

The paper contains an explicit model of public programs / physical barriers and private
self-protection / self-insurance. It absorbs additional broad public-private risk-protection
interaction claims, but not the mobile-firm/local-government policy game.

#### Lee & Pinto (2009)

Kangoh Lee and Santiago M. Pinto,
“Crime in a Multi-Jurisdictional Model with Private and Public Prevention,”
*Journal of Regional Science* 49(5), 977–996.
DOI: https://doi.org/10.1111/j.1467-9787.2009.00619.x

Application-neutralized, this is a relevant parent class because local public prevention
changes private prevention and spatial behavior across jurisdictions. The mobile object is
crime rather than productive firms, and the paper does not reproduce the PCPPR
plant-attraction / industrial-resilience theorem.

#### Hickey et al. (2021)

Ross Hickey, Steeve Mongrain, Joanne Roberts, and Tanguy van Ypersele,
“Private protection and public policing,”
*Journal of Public Economic Theory* 23, 5–28.
DOI: https://doi.org/10.1111/jpet.12473

This paper directly analyzes public/private protection complementarity and substitution.
It is a structural parent for the protection-interaction block, not for the full climate /
plant-location / fiscal-competition theorem.

### Strongest theorem-absorption attack after re-search

The strongest attack is now the combination:

**Kousky et al. (government protection ↔ endogenous private investment/location)**
+
**Grames et al. / public-private flood adaptation**
+
**Walz–Wellisch / Maurer–Walz (competition for mobile firms through local public inputs)**.

That combination contains most economic intuitions separately.

The current headline theorem nevertheless survives the absorption test narrowly: no
identified prior theorem directly specializes to a game in which the attracting public
input lowers primary disruption risk, endogenously changes firms' geographic contingency
readiness, produces a negative coordinated industrial protection margin, and still supports
a globally verified positive local-policy Nash equilibrium.

The paper must therefore continue to sell the **full coupled policy-ranking result**, not
any individual ingredient or the mere combination of familiar ingredients.

### Required Stage-6 repair

- add Kousky et al. to the structural-isomorphism / theorem-absorption map;
- include a direct comparison in Related Literature and likely the Introduction;
- consider Mahmud–Barbier as the climate/disaster public-private-protection lineage;
- record Lee–Pinto and Hickey et al. in the application-neutral parent-class audit,
  whether or not all are ultimately cited in the paper;
- refresh the maximum-defensible novelty sentence and cover-letter comparison.

No theorem change is presently required by these papers.

## Stage 7 — Welfare / benchmark / institutional audit

### Verdict

**PASS WITH MATERIAL SCOPE RISK ALREADY DISCLOSED.**

The state-level welfare algebra, backup costs, public costs, and hosting-benefit accounting
are internally consistent. The paper correctly avoids treating the location-attached
benefit as an additional national resource gain: two plants imply aggregate (2b) is
constant.

The paper also now states the central limitation correctly: the planner is a
**protection-policy-constrained industrial-surplus planner**, not a first-best climate
planner. The omitted direct-benefit sensitivity in the Discussion makes the limitation
quantitative.

The main remaining referee attack is substantive rather than algebraic: the local
incidence rule and state-independent hosting benefit (b) are reduced-form assumptions,
and they provide the plant-attraction wedge. A hostile referee can reasonably ask how much
of the result is the resilience mechanism versus familiar zero-sum fiscal competition.
The current manuscript acknowledges this, but it remains a contribution-strength risk.

## Stage 7.5A — Generality / quantifier / portability / formal gate

### Verdict

**CONDITIONAL GO ONLY — certificate refresh required before a new freeze.**

### Quantifier alignment

Current manuscript wording is materially disciplined:

- exact theorem: existence on a nonempty open set within the maintained symmetric
  baseline family;
- canonical planner optimum: unique;
- positive symmetric local policy equilibrium: existence, not full policy-game
  uniqueness;
- nonlinear-risk and logistic exercises: numerical diagnostics only;
- exact (1/4) marginal coefficient: institution-specific;
- no claim of general climate-protection overprovision.

No current headline prose was found that exceeds those quantifiers.

### Portability certificate regression

The dated `V2_4_CONTRIBUTION_ROBUSTNESS_CERTIFICATE_2026-09-24.md` still describes
the two diagnostics as “orthogonal” and repeatedly describes them as independent
re-solutions supporting conditional portability.

The repaired manuscript is more precise:

- nonlinear risk was constructed to match (q(0)) and (q'(0)), so equality of the
  origin marginals is built in;
- logistic heterogeneity was calibrated to match the density at symmetric indifference,
  which makes the symmetric government FOC structurally identical along the symmetric
  path;
- the informative content is therefore off-origin/off-diagonal continuation and deviation
  behavior, not independent reproduction of every headline sign.

This does not automatically require downgrading the final classification from
`CONDITIONALLY PORTABLE`, but the certificate must be rewritten to match the actual
diagnostic content before Stage 7.5A can close.

### Formal-verification gate

Current main CI rebuilds the repaired Lean project successfully and the current
`formal/README.md` gives an accurate bounded scope:

- final Lean theorem is conditional on full-domain sign/bridge premises;
- clipped-backup uniqueness remains outside Lean;
- open-set persistence remains outside Lean;
- `native_decide` extends the trusted base;
- no claim is made that Lean closes the entire economic model.

No current statement-fidelity defect was found. The older dated formal-gate closure refers
to an earlier canonical manuscript SHA; the current v3 evidence should be summarized in a
refreshed closure/addendum, but a new Lean theorem is not presently required.

### Human accountability blocker

The current `AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md` is personally confirmed on
2026-09-25. The 2026-10-02 repair subsequently changed proof logic, added the exact
Delta=0 benchmark, and narrowed/clarified the contribution.

Under workflow v2.5, mere approval of an AI-generated repair or a green CI run is
insufficient. Before a new Stage-8 freeze, the author must personally reconfirm:

- the repaired central mechanism;
- current material assumptions;
- clipped-game / full-diagonal-derivative proof logic;
- Delta=0 benchmark interpretation;
- limitations and failure boundaries;
- maximum defensible novelty after the updated Stage-6 map.

## Stage 8 — Freeze consequence

**The current v3 freeze should be treated as reopened for workflow purposes.**

This is not because the canonical theorem has failed. It is because Stage 6 and Stage
7.5A entry requirements for a final v2.5 freeze are no longer fully certified.

After the above repairs and author confirmation, issue a new freeze (v4 or equivalent)
rather than silently treating the current v3 lock as final.

## Stage 9 / reproducibility

### Verdict

**PASS for scientific reproduction.**

The main run `37010905510` is green for both repository verification and Lean.
The anonymous archive reproduces the advertised Python/LaTeX and formal commands.
No identity token was found in the current editable anonymous source archive in a
separate artifact inspection.

The EPS in the final transport bundle contains embedded Type-3 DejaVuSans font resources,
so the current vector artwork satisfies the font-embedding requirement in substance.

## Stage 10 / 13 — Exposition and reviewer verifiability

### Manuscript verdict

**PASS.**

The current manuscript has one main-text figure and one main-text table. The proof-critical
bridges for backup, location, planner monotonicity, local global best response, and open-set
persistence are now visible in manuscript-facing text.

### Certification artifact issue

The old exposition report still says there are three main-text exhibits and describes a
nested-benchmark table that no longer exists. The current automated exposition script itself
passes and permits the leaner architecture, so this is a stale report, not a manuscript flaw.

The historical reviewer-verifiability report correctly marks itself superseded. A fresh
post-repair v2.7-style reviewer-verifiability report should be produced from the current
v3/v4 manuscript before Stage 13 closes again.

## Stage 11 — Full hostile-referee attack

### Verdict

**NO FATAL DEFECT; MAJOR EDITORIAL RISK REMAINS.**

Most plausible hostile referee objection:

> Once known public/private adaptation distortions and classic local-public-input
> competition are acknowledged, the paper may look like a carefully certified parameterized
> combination of familiar mechanisms rather than a sufficiently general new theorem.

The current response is defensible but must be made with the updated Stage-6 map:
the contribution is the full coupled policy-ranking result and its global certification,
not protection-induced location, adaptation crowd-out, strategic substitution, or fiscal
competition separately.

Additional non-fatal referee risks:

- the equal-half surplus incidence and state-independent (b) are deliberately reduced-form;
- the exact theorem is baseline-family-specific;
- omitted nonindustrial protection benefits can reverse the zero-protection planner margin;
- the exact Delta=0 benchmark shows disaster-state incremental monopoly rents are not
  necessary, so market power should not be framed as the unique source of the result;
- the formal layer is partial and should remain presented as assurance, not contribution.

No new mathematical inconsistency, welfare double count, hidden boundary equilibrium, or
Lean-scope inflation was found in the current manuscript.

## Stage 12 — ERE positioning

### Verdict

**ERE remains substantively plausible, but Stage 12 should be refreshed after Stage 6.**

The current ERE aims explicitly include economic theory applied to environmental problems,
policy instruments, cost-benefit analysis, modelling/simulation, and institutional
arrangements. The paper's adaptation-policy question is within that scope.

The principal desk-risk is therefore contribution strength / environmental interpretation,
not an obvious out-of-scope topic. The paper's existing restriction to industrial adaptation
appraisal is important and should remain prominent.

## Stage 14 — Current submission QA

Official ERE requirements were re-opened on 2026-10-03.

Current confirmed requirements include:

- double-blind review and separate author page;
- editable source files at submission/revision;
- LaTeX permitted for mathematical manuscripts;
- abstract 150–250 words normally;
- 4–6 keywords;
- relevant Statements and Declarations;
- material LLM use documented with human accountability;
- EPS preferred for vector graphics;
- figure names such as `Fig1.eps`;
- non-color visual encoding for accessibility.

The current final transport bundle contains `05_artwork/Fig1.eps`, and its fonts are
embedded. Figure 1 uses solid, dash-dotted, and dotted line encodings.

### Packaging regression

The separate GitHub Actions artifact `ERE-submission-components` still contains the old
`figures/policy_regime.eps` instead of `Fig1.eps`. The final transport bundle is correct.
Update the workflow's component-upload path so both artifacts agree.

### Live-portal status

On 2026-10-03 the official ERE Editorial Manager page still states:

> “Site under development. Do not use for live manuscript submission.”

Thus authenticated portal fields and the generated reviewer PDF remain fail-closed.

### Figure-instruction conflict

The same current ERE instructions contain both:

- a journal-specific instruction to place figure legends after the references; and
- later Springer artwork guidance to place figures in the body and captions in the text file.

Record this as a current instruction conflict. Do not silently infer portal behavior.

## Required repair sequence under workflow v2.5

1. **Rollback to Stage 6:** rebuild theorem-absorption map with Kousky et al. and the
   application-neutral parent classes above; update manuscript/cover-letter positioning.
2. **Re-run Stage 7.5A:** refresh the Contribution Robustness Certificate so its diagnostic
   evidentiary claims match the repaired manuscript; refresh formal-scope closure/addendum.
3. **Author confirmation:** obtain a new Author Intellectual-Contribution Record for the
   repaired theorem/proof/benchmark/novelty boundary.
4. **Stage 8:** issue a new canonical freeze.
5. **Stage 11:** rerun hostile manuscript attack against the updated literature map.
6. **Stage 12:** refresh ERE positioning from the surviving contribution.
7. **Stage 13:** regenerate exposition and reviewer-verifiability reports from the current
   manuscript.
8. **Stage 14:** fix the `ERE-submission-components` Fig1 path; refresh current ERE ledger;
   preserve the portal-only HOLD.
9. **Stage 15:** create a new scientific-object lock and submission freeze only after all
   affected gates are green and the author personally approves the exact final object.

## Final research judgment

**Mathematics:** no new fatal defect found.  
**Headline theorem:** survives current audit.  
**Novelty:** survives narrowly, but current certification is incomplete until Stage 6 is repaired.  
**Portability:** likely remains no stronger than `CONDITIONALLY PORTABLE`; current certificate is stale.  
**Current v3 freeze:** not final under workflow v2.5.  
**Submission state:** **NOT READY — RECERTIFICATION REQUIRED**, with no present indication that the canonical theory must be abandoned.
