# Formalization scope and reproduction

The pinned project uses Lean 4.32.1 and mathlib revision
`520045ab14e26149ee970e2e617ca04b09bde5d6` with transitive revisions in
`lake-manifest.json`. From the archive root, install `requirements.txt` and the
Lean toolchain and Git command, then run `make formal-verify`. Network access
is needed for the pinned external dependencies; the paper's Git checkout or
history is not needed. That target regenerates both
`PCPPR/GeneratedCertificates.lean` and `GENERATED_CERTIFICATE_ARCHIVE.json`,
restores the mathlib cache, builds all thirteen proof modules, and checks
`Main.lean` with Lean to print theorem dependencies
into `formal/FORMAL_AXIOM_REPORT.txt`. It does not link the optional native
`pcppr` executable: that step would compile mathlib's C object files, which are
not included in the proof cache. Every project proof module and the theorem
report remain checked. Generated certificates are also supplied
in the reviewer archive. Python exact verification is `make verify`.

## What is checked

| Layer | Statement checked | External assumptions / limits |
|---|---|---|
| Product market | Profit and wedge algebra; symmetric FOC quantities | Not a formal proof of the entire constrained Cournot game |
| Availability | State sum and nonnegativity implications | Assumes marginal/joint bounds; does not construct the probability law from model primitives |
| Backup | State-to-payoff identity; global optimality of an interior FOC; uniqueness of the interior linear system | Feasibility, full clipped-game contraction, and absence of corner equilibria are proved in the manuscript/exact Python layer |
| Location | No clipping from endpoint inequalities; affine pair uniqueness | Economic endpoint inequalities on the whole policy square are external exact obligations |
| Welfare and attraction | State-to-surplus identity and marginal decomposition | Government incidence and hosting-benefit interpretation are model assumptions |
| Canonical arithmetic | Model-derived rational checkpoints and signs | Several equalities use `native_decide` |
| Bernstein / policy implications | Negativity from Bernstein representation, monotonicity from derivative signs, global optimum from stationary concavity | Economic-function identities and large bivariate sign obligations are not instantiated as a closed Lean theorem |
| Generated FOC data | Finite endpoint signs and derivative-coefficient signs; root implication under the displayed bridges | Endpoint/interval finite arithmetic uses `native_decide`; representation of the economic function remains an assumption |
| Final theorem | A conditional implication for arbitrary `W`, `GA`, `GB`, `F` | Takes full-domain planner signs, own-policy second derivative signs, FOC/stationarity bridges, continuity and symmetry as premises |
| Open set | Outside Lean | Manuscript compactness and implicit-function proof uses the full diagonal derivative, not own-policy concavity alone |

## Trust boundary

Ordinary proof terms are checked by Lean's kernel under their displayed
hypotheses. `native_decide` additionally trusts native compilation and execution
and introduces dependency names containing `_native.native_decide`. These are
reported explicitly; they are not mistaken for a proof without any added trust.
The project has no intentional proof placeholders or explicit custom axiom
declarations. That source check does not remove `native_decide` dependencies.

The final `canonical_witness_from_generated_certificates` theorem is not a
closed proof of the economic model. In particular, its `hWderivA`, `hWderivB`,
`hGAsecond`, `hFderivCertificate`, endpoint values and stationarity bridges
remain visible premises. Exact Python computations and mathematical derivations
supply the model-specific evidence. Neither a build nor this scope map is a
certificate of novelty, policy interpretation, robustness outside the encoded
family, or journal acceptance.

Reference for the extended trusted base: https://lean-lang.org/faq/ .
