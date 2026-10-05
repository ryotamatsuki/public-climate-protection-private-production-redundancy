# ERE pre-submission final audit — 2026-10-05

Audited starting main: `cf44480768c2d71c188428ed9b54bc4f04869dcd`.
This is an AI-assisted independent reconstruction and adversarial review, not
an assertion of external human peer review or new personal author sign-off.
The corrective commit and its release checks are recorded in Git history and
GitHub Actions. No journal submission is performed.

## Central contribution and verdict

**SUBMISSION READY AFTER MINOR FIXES.** The scientific audit found no reason to
change the manuscript, including the general-incidence remark. The required
repair is registration of that already-added local mathematical remark in the
descendant freeze controls; a small title-page overflow is also corrected.
Final artifacts must be generated from the corrected green main commit.

Public protection directly improves primary reliability, but lowers firms'
private incentive to maintain geographic backup readiness. When disaster-state
market power creates a positive social--private readiness wedge, the resulting
readiness reduction can outweigh the direct industrial welfare gain, even after
saved readiness resource costs are counted. A unilateral policy simultaneously
attracts primary plants and their hosting benefit. The latter can support a
positive decentralized protection equilibrium although the constrained
coordinated planner uniquely chooses zero on the entire policy square. This
joint mechanism is the paper's Protection--Attraction Conflict; neither
adaptation crowd-out, the readiness wedge, nor regional firm competition is
claimed to be new by itself.

## Audit findings

| Area | Finding and boundary |
|---|---|
| Core and novelty | The channels connect through endogenous readiness and location. The literature discussion credits prior sourcing wedges, public/private adaptation, safe development, and regional public-input competition. No unsupported first-ever claim was found. |
| Mathematics | Cournot continuation, readiness best responses, state-enumerated surplus, Bayesian location cutoff, attraction derivative, marginal threshold, Delta-zero benchmark, full-domain planner signs, global own-policy best responses, and open-set persistence agree across text, analytic appendix, exact scripts, and independent rederivation. |
| New remark | The identity and threshold are correct. The baseline is recovered exactly; the remark explicitly does not extend the global theorem. See the derivation below. |
| Welfare and objectives | Consumer and producer surplus and real private/public resource costs are counted consistently. There are always two primary plants; national hosting benefit is the constant `2b`, while local attraction redistributes it. Baseline local objectives sum to national welfare. Fixed local incidence is an explicit reduced-form assumption. |
| Economic interpretation | The abstract, introduction, discussion, and conclusion consistently restrict the result to industrial welfare, the maintained model family, the constrained coordination benchmark, and an existence result. Lives, housing, public assets, and other adaptation benefits are outside the comparison. |
| ERE fit | Climate adaptation changes the joint distribution of production availability and incentives for private geographic backup. This is a substantive adaptation question with policy coordination implications. The maintained risk/readiness specification limits external generality, not internal environmental relevance. |
| Literature and priority | Primary sources support the distinctions drawn from Grossman--Helpman--Lhuillier, Kousky--Luttmer--Zeckhauser, safe-development models, regional public-input competition, and recent public-protection crowd-out evidence. No priority-critical omission was identified in the reviewed sources. No additional citation is needed for this audit. |
| Empirical implications | Unilateral attraction and symmetric-path readiness reduction are distinguished. A lower readiness level with greater substitutability is not identified with stronger crowd-out. Spatial policy correlation is not treated as causal strategic interaction; proposed identification designs retain their required assumptions. |
| Exposition | No inconsistent definitions, formula/prose mismatches, exaggerated theorem scope, or broken cross-references requiring manuscript revision were found. The abstract is 193 words with six keywords. |
| Submission and reproduction | Main PDF: 33 pages, visually inspected throughout; no unresolved references/citations or box warnings. The anonymous source archive builds cleanly; the actual extracted anonymous replication archive completes its advertised verification without editorial files or a project Git checkout. Title-page overflow is fixed without declaration changes. |

## Independent check of the general-incidence remark

Write the local objective as
`G_A~ = omega S + B(2p) - C(a_A)` and the coordinated objective as
`W~ = S + B(2p) + B(2(1-p)) - C(a_A) - C(a_B)`.
Here `B` applies to the expected local primary-plant count, and `omega` is a
fixed local weight. It need not be an exhaustive national surplus share;
the coordinated benchmark uses unit weight on national industrial surplus.

Symmetry gives `p(a,a)=1/2`, so the coordinated hosting terms equal `2B(1)`
on the common-policy path. Also `S_A(0,0)=S_B(0,0)`. With `C'(0)=0`,
`M_S~ = 2 S_A(0,0)`, whereas
`M_L~ = omega S_A(0,0) + 2B'(1) lambda_0`.
Consequently,

`M_L~ = (omega/2) M_S~ + 2B'(1) lambda_0`.

For `lambda_0>0` and `M_S~<0`, strict positivity of the local marginal is
equivalent to `B'(1) > -omega M_S~/(4 lambda_0)`. Without the maintained
zero initial marginal public cost, the identity would contain the extra term
`(omega-1)C'(0)`; the remark correctly imposes the needed assumption.
Taking `omega=1/2`, `B(n)=bn`, and `C(a)=ca^2/2` recovers the baseline
`M_L=M_S/4+2b lambda_0` and its threshold. No global certificate for a
nonlinear `B`, alternative `C`, or arbitrary local weight is inferred.

The exact remark has SHA-256
`aa8d95812c572ebb9c81b0bafdabca8e8b13f54f51698fdc8319299275d0a71b`.
Removing only that remark and its two trailing newlines recovers the complete
pre-remark main-results file, Git blob
`d6dd2b8fa948d67613748ef210db896f3cb1728f`.
The freeze gate checks both facts, then retains its previous comparison of
baseline formulas, theorem statements, and proof logic. The immutable v4
lock is not rewritten, and numerical/mathematical tests are not changed.

## Verification evidence and scope

Fresh starting-main verification passed the existing symbolic, normalization,
policy, global, numerical, portability, Delta-zero, independent-model,
independent-exact, exhibit, submission-format, and clean-archive checks;
all **31 existing tests passed**. The single failing target was the descendant
freeze gate's stale digest for the new remark, rather than a mathematical
certificate failure. Merely replacing that digest would not suffice because
the existing ordered formula comparison also detects the added equations.

The fresh independent exact audit covers 32 sign targets and isolates exactly
one admissible symmetric FOC root with no denominator root in the interval.
Planner monotonicity is certified on the full policy square. Local own-policy
concavity is certified over the full deviation interval with the rival's
choice in the isolated equilibrium enclosure. A local FOC alone is never used
to establish a global optimum. The simple diagonal FOC root and strict compact
domain margins justify persistence in the maintained symmetric primitive family;
uniqueness of all decentralized policy equilibria is not claimed.

The canonical numerical channel check gives `M_S=-0.006482464222763948`,
`M_L=0.0019308655211412436`, and `lambda_0=0.03228619615302028`.
These approximations summarize the mechanism; exact rational and Bernstein
checks provide the sign and global evidence. No new numerical experiment or
empirical analysis was introduced.

The Lean layer verifies its stated finite arithmetic and conditional logical
interfaces. Full rational-economy bridges and open-set analysis remain outside
the closed formal theorem, as disclosed in the manuscript and formal README.
`native_decide`'s compiler/runtime boundary is disclosed. Fresh final-main
Actions must also pass the pinned Lean/mathlib build, axiom report, and actual
anonymous-ZIP formal reproduction; local symbolic checks are not a substitute
for these release checks. Their run status is recorded by Actions, not invented
in this report. The correction changes no Lean proof source or payload.

## Minimal changes and deliberately unchanged limitations

- Register the already-present remark as a separately audited **local marginal
  robustness addendum**, with exact byte guards and an updated descendant lock.
- Add `microtype` to the separate title page and build it twice, eliminating
  the 7.69606 pt overflow and first-pass PDF-outline warning without changing
  any author declaration.
- Update provenance/upload controls and include this report in the editorial
  transport bundle.

No manuscript text, theorem, model primitive, welfare definition, existing
test, mathematical verification script, exact certificate, or Lean proof is
modified. A richer local-incidence microfoundation, broader risk/readiness
families, quantitative calibration, asymmetric primitives, and causal empirical
validation could be future research; none is necessary to establish the
paper's carefully delimited existence result before submission.

The most likely referee objection is that reduced-form local hosting benefits
and the maintained disaster/readiness family limit policy generality. The
objective accounting and new remark answer the claim of an artifact of exactly
one-half incidence or linear hosting benefits at the marginal level. They do
not establish global robustness for arbitrary objectives or empirical policy
magnitudes, and the manuscript does not claim those conclusions.

Official journal sources checked on the audit date:

- https://link.springer.com/journal/10640/aims-and-scope
- https://link.springer.com/journal/10640/submission-guidelines

The journal requires double-anonymous review, a separate title page, an
abstract of 150--250 words, four to six keywords, and editable source files.
Its replication policy requires public materials following successful peer
review and before final acceptance. Actual portal file designations and the
portal-generated reviewer PDF belong to the author's subsequent submission
operation; this audit does not perform that operation.
