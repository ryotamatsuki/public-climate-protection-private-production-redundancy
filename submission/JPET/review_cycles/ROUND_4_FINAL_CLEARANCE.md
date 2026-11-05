# Round 4 — simulated Major R&R clearance audit (2026-11-05)

**This is a simulation, not an actual JPET review, editorial acceptance, or three independent human referees.** The three assigned reviewer roles were separated methodologically, but run in one model session. No main merge or journal submission has been authorized.

## What is being tested

The question is not whether this paper deserves an initial R&R: Round 2's model-internal evaluation favored Major R&R. Round 4 now tests whether *each major criticism identified by the project* has a scientifically supported response, so a referee could plausibly favor **Accept after minor revisions** upon receiving a major revision.

The prior Round 3 negative decision at discovery of an invalid proof is preserved unchanged. It is not silently rewritten as a positive report.

## Referee 1: substantive contribution and closest-parent novelty

**Recommendation: Accept subject to minor editorial/literature qualifications — conditional internal assessment.**

- Generic fiscal overprovision of industrial public inputs and public/private defensive substitution are conceded as known. Direct parents include Keen–Marchand (1997), Walz–Wellisch (1996), Bayindir-Upmann (1998), Maurer–Walz (2000), Billon (2023), Grossman–Helpman–Lhuillier (2023), and Pauser (2026).
- The sharper conditional claim is the *sign of the response of the decentralized-minus-coordinated protection gap to a commonly valued direct benefit*. In three **globally solved complete policy games**, the effect is positive when both backup and location are endogenous, zero when readiness is frozen, and negative when location is frozen.
- A strict primitive-inequality region, rather than only a rational witness, identifies when the global coordinated/local-policy conflict occurs. A compactness/IFT argument extends the positive-gap effect to an open region with positive product substitutability.
- The actual state-contingent Cournot system generates an additional local result: higher product substitutability itself increases decentralized overprovision at a specific exact primitive point, which cannot be inferred just from a public-input-overinvestment slogan.
- These are conditional game-theoretic results. No claim is made to a universally necessary set of conditions for overprovision.

**Important remaining uncertainty:** the published 1998 Bayindir-Upmann full article and other non-open-access full theorem proofs were not obtained. Accessible primary abstracts, the fiscal competition review and publication metadata support the absence of an explicit private backup technology, but they do not prove no general theorem could absorb these comparisons. A real referee could still demand further theorem-level mapping. Acceptance-caliber is therefore provisional and revocable on new evidence.

## Referee 2: mathematical correctness, completeness, reproducibility

**Recommendation: Accept subject to final author/third-party technical signoff — conditional internal assessment.**

- Real error discovered in Round 3: off-axis planner derivative omitted **+y/(16k)** in a newly added primitive-region proof. The error is documented and the invalid proof was replaced, not concealed.
- New proof: uniform globally strict planner concavity plus a strictly negative gradient at the nonnegative corner implies unique global coordinated zero optimum by the supporting-hyperplane inequality. Thus no extra off-axis condition is needed.
- Independent SymPy exact-rational reproduction certifies that a second rational witness violates the discarded overstrong restriction while satisfying the remaining primitive inequalities, demonstrating genuine increased theorem generality.
- The augmented positive-planner-optimum result, full restricted policy games, and two-dimensional global Hessian inequalities are checked by exact symbolic rational and Bernstein computations; no symmetric on-path FOC is misrepresented as a global Nash or planner proof.
- New perturbation theorem relaxes fixed regional industrial surplus incidence, credits local hosting only when the **local primary plant** operates, and verifies a nonzero perturbation with exact full-policy Bernstein certificates. Smoothness and compactness support extension to positive gamma in an open neighborhood.
- A fifth analytic proof and independent script differentiate the complete state-contingent Cournot profit/surplus, optimal backup, and Bayesian firm-location game in gamma. Exact right derivatives imply the local overprovision gap strictly increases with product substitutability at gamma=0 for the specified rational primitives.
- Historical ERE scientific files remain byte-identical to their prior archival source. A dedicated JPET workflow (not the older exact tracked-set ERE gate) re-runs original scientific calculations and all five additional exact checks before compiling the candidate manuscript and source archive.
- **Clean-room check on exact commit 0b8e5543cb854ca97c08ba143b41cccdcb8e5b87's PR GitHub Actions merge build:** the downloaded artifact's two SHA-256 sums matched after removing a nonportable filename prefix; all five independent exact scripts in the extracted Git archive passed; re-running the figure generator and three LaTeX passes produced a PDF with the same 48 pages and **identical per-page extracted text**. The workflow checksum-list filename prefix was subsequently corrected; a final follow-up CI is required on that packaging-only change.
- The underlying `gamma=12/25` original theorem's complete source-to-certificate bridge is inherited from prior audited work and re-run original tests; it is not independently fully formalized in Lean during this review. Formal TCB limits remain disclosed.

**Residual risks:** a new independent scholar's handwritten proof check and mathematical audit of the original source-to-certificate bridge would improve confidence. Machine checks are evidence, not a guarantee against an error in the underlying representation.

## Referee 3: economic interpretation, comparative statics, model relevance

**Recommendation: Accept subject to narrow interpretative corrections — conditional internal assessment.**

- The zero planner optimum in the original industrial-only benchmark is now complemented by a strictly positive planner optimum that remains below local investment. The augmented direct benefit changes welfare accounting, not private firm preferences.
- Exact restricted games isolate which private decision margins are responsible for the new benefit-gap *comparative static*, not for every form of fiscal overprovision.
- The full oligopoly comparative static resolves the main concern that the rich Cournot-disaster-state structure was irrelevant because a gamma-zero example already generated the sign conflict.
- The national-surplus incidence assumption and local hosting return no longer have to be exactly fixed and state-independent, respectively. A small location-linked regional share and primary-plant-operation-dependent hosting return preserve the local ranking.
- The added welfare benefit `mu` is a reduced-form social value, not a calibrated estimate. The policy model cannot establish that actual flood defenses should be reduced or increased in a particular location.

**Remaining scope:** institutional ownership/labor-market foundations and external empirical calibration are not part of this theoretical model and should not be rhetorically promised.

## Simulated handling editor: clearance decision

**INTERNAL SCIENTIFIC R&R CLEARANCE: ACCEPT-CALIBER, SUBJECT TO MINOR REVISIONS AND EXTERNAL VERIFICATION.**

The main defects in the *simulated Major R&R* have concrete mathematics, refutable counterfactuals, bounded economic interpretation, manuscript prose, and current standalone evidence. The documented fatal mathematical *proof gap* was repaired with a more general proof; the richer oligopoly model now supplies a separate substantive comparative static.

This recommendation is **not a claim of actual acceptability by the JPET editor**, not a certification that no parent theorem absorbs the claimed results, and not a substitute for genuinely independent human reviewers. Any newly found theorem absorption or mathematical counterexample must overturn it.

## Submission gate separate from scientific judgement

**Technical submission is NOT YET AUTHORIZED** until:
1. the final packaging-only checksum-manifest correction has a successful dedicated JPET CI at the same latest source commit;
2. the actual human author approves all new propositions, proof changes, AI assistance disclosure and final manuscript;
3. the latest Wiley portal/document metadata and combined reproduction package are reviewed;
4. the author explicitly chooses to submit.

The original ERE frozen science has not been modified or merged. The draft PR remains open. The historical `verify` workflow can intentionally fail its prior ERE exact-file-set gate with added JPET files, and this is not reclassified as success.

## Audit trail and original decisions

- Round 0: BELOW R&R.
- Round 1: BORDERLINE.
- Round 2: simulated MAJOR R&R / R&R-CALIBER.
- Round 3 at defect discovery: NOT CLEARED (invalid math proof).
- Round 4 after correction, new perturbation and positive-gamma comparatives, and clean-room replication: **internally ACCEPT-CALIBER conditionally**, independent of actual journal decision.

The Round 0–3 reports, comments and adverse records remain immutable and are not replaced by this file.
