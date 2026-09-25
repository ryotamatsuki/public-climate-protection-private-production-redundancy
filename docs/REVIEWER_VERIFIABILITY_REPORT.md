# Reviewer Verifiability Report — 2026-09-25

## Verdict

**PASS — REVIEWER VERIFIABILITY**

Scope: **FULL**.

Reference checklist: `ryotamatsuki/research-paper-workflow/checklists/REVIEWER_VERIFIABILITY_CHECKLIST.md` (prospective v2.7 reviewer-verifiability refinement).

This audit asks whether a competent specialist referee can follow and audit the proof-critical chain from the manuscript-facing package without reverse-engineering missing conceptual bridges. It does not require every mechanical algebraic expansion, exact coefficient list, root-isolation trace, or proof-assistant kernel trace to appear in the PDF.

No theorem, parameter, equilibrium concept, welfare definition, numerical result, or certificate is changed by this audit.

## 1. Headline-result map

| Claim / result | Manuscript location | Derivation / proof location | Computational / formal artifact | State |
|---|---|---|---|---|
| Cournot / monopoly continuation and scarcity-rent wedge | Sec. 3 | App. A, Product-market and backup identities | `scripts/verify_symbolic.py`; Lean T1 | PASS |
| Backup best response, strategic substitution, co-location / dispersion formulas | Sec. 3 | Sec. 3 proofs + App. A | `scripts/verify_global_certificate.py`; Lean T3–T5 | PASS |
| Unique interior backup continuation on full policy square | Sec. 3 | Lemma “Unique interior continuation” | `scripts/verify_global_certificate.py`; Lean T4 | PASS |
| Unique unclipped private-information location continuation | Sec. 3 | Lemma “Unique interior continuation” | `scripts/verify_global_certificate.py`; Lean T6 | PASS |
| Plant-attraction marginal decomposition | Sec. 4 | Proposition “Plant-attraction threshold” | symbolic checks; Lean T8 | PASS |
| Canonical marginal sign conflict | Sec. 4 / Sec. 5 | exact witness arithmetic | generated exact arithmetic; Lean T9 | PASS |
| Global planner optimum at zero | Theorem 1 / App. A | Lemma “Global planner monotonicity” | Bernstein exact certificate; Lean T10–T11 | PASS |
| Positive symmetric local-government equilibrium | Theorem 1 / App. A | Lemma “Global local-government best response” | exact root isolation + whole-domain concavity; Lean T12–T14 | PASS |
| Open-set persistence around canonical witness | Theorem 1 / App. A | Lemma “Persistence around the canonical witness” | analytic compactness / continuity / implicit-function argument; explicitly outside Lean scope | PASS |
| Fit-payoff robustness | App. A | “Robustness to counting the selected location-fit payoff” | exact symmetric-advantage identity in `verify_global_certificate.py` | PASS |

## 2. Reviewer reconstruction

A clean reconstruction was performed from the manuscript-facing mathematical chain.

### 2.1 Primitives to downstream backup continuation

The manuscript gives:

- utility and inverse demand;
- public protection and failure-risk mapping;
- primary and joint failure probabilities;
- backup readiness and its cost;
- final-availability probabilities;
- expected firm profit.

The backup FOCs are no longer left as an implicit “two-equation system.” Equation `backup-linear-system` displays

[
\begin{pmatrix}
k & \Delta J\\
\Delta J & k
\end{pmatrix}
\begin{pmatrix}
r_1\\r_2
\end{pmatrix}
=
\begin{pmatrix}
\pi_D s_1+\Delta J\\
\pi_D s_2+\Delta J
\end{pmatrix},
]

and identifies the determinant (k^2-(\Delta J)^2). A referee can therefore see the object whose determinant/interiority is later certified.

**Finding:** PASS. No proof-critical bridge is missing.

### 2.2 Backup continuation to location continuation

The manuscript defines the four location-contingent equilibrium profits, the deterministic location differences (d_A,d_B), the affine cutoff best response, its endpoint probabilities (u_0,u_1), slope (B), and the unique fixed-point probability (p).

The Appendix states exactly what the whole-domain certificate checks: endpoint interiority, no clipping, (|B|<1), denominator positivity, and interiority of the resulting fixed point. It also explains why these facts imply uniqueness rather than merely existence.

**Finding:** PASS.

### 2.3 State/profile objects to expected surplus and policy objectives

The manuscript now explicitly defines (S^{XY}(a_A,a_B)) as profile-specific surplus after solving backup continuation and displays

[
\mathcal S(a_A,a_B)
=
p^2 S^{AA}
+p(1-p)S^{AB}
+p(1-p)S^{BA}
+(1-p)^2S^{BB}.
]

It then states that substituting profile-specific backup solutions and the location probability into this aggregation, and then into (W) and (G_A), yields the rational policy functions used by the exact certificates.

This closes the previously implicit bridge:

[
\text{primitives}
\to r^{XY}
\to S^{XY}
\to p
\to \mathcal S
\to W,G_A
\to \text{certificate target}.
]

**Finding:** PASS.

### 2.4 Certificate target to global planner result

The Appendix defines the rational structure

[
W_{a_A}=P_A/Q_A,qquad W_{a_B}=P_B/Q_B,
]

states the policy domain, explains the Bernstein weighted-average argument, certifies denominator positivity and numerator negativity, and then explicitly derives strict coordinatewise monotonicity and the unique optimum at ((0,0)).

The manuscript need not print the mechanically generated expansions of (P_A,Q_A,P_B,Q_B); the exact script and certificate archive identify the delegated computation.

**Finding:** PASS.

### 2.5 Root isolation and concavity to decentralized equilibrium

The Appendix defines

[
F(a)=G_{A,a_A}(a,a),
]

states the exact isolating interval for the unique root (alpha), and separately writes

[
G_{A,a_Aa_A}=P_G/Q_G.
]

It explains that root isolation supplies stationarity while the whole-domain Bernstein sign certificate supplies strict concavity over the full own-policy interval when the rival lies in the root enclosure. The proof then explicitly uses “stationary point + strict concavity” to obtain the unique global best response, including boundary actions.

This avoids conflating an FOC solution with a global equilibrium.

**Finding:** PASS.

### 2.6 Lemmas to headline theorem

The theorem proof explicitly combines:

1. unique downstream continuation;
2. unique planner optimum;
3. unique positive symmetric local-government best response;
4. open-set persistence.

The canonical-witness result and the nonempty-open-set extension are visibly separated.

**Finding:** PASS.

## 3. Computer-assisted proof audit

### Object

The manuscript names the relevant rational functions, backup/location continuation objects, planner derivatives, diagonal local-government FOC, and local second derivative.

### Domain

The principal global certificates are stated on the full policy square ([0,2/25]^2), and the local-government concavity certificate uses the full own-action interval times the exact rival-root enclosure.

### Certified property

The manuscript distinguishes:

- denominator sign;
- backup interiority;
- location no-clipping and contraction;
- planner derivative negativity;
- root uniqueness;
- own-policy strict concavity;
- symmetric deterministic location advantage.

### Logical implication

The Appendix explains the implication from each certified property to the corresponding lemma and from those lemmas to Theorem 1.

### Reproduction mapping

The manuscript-facing package identifies:

- `scripts/verify_global_certificate.py`;
- `scripts/verify_policy_certificate.py`;
- `scripts/verify_symbolic.py`;
- `scripts/verify_normalization.py`;
- `docs/certificate_polynomials.json`;
- `docs/certificate_normalization.json`.

The formal layer is separately mapped in `docs/FORMALIZATION_TARGET_MAP.md`.

**Finding:** PASS.

## 4. Formal-verification scope mapping

The manuscript and formal-verification records distinguish three classes:

- Lean-derived claims;
- maintained model assumptions;
- generated exact certificates imported through explicit semantic bridges.

The formal map explicitly excludes the open-neighborhood persistence theorem from the Lean claim. No manuscript language was found that upgrades selected Lean certification into a claim that Lean proves the entire economic theorem from primitives.

**Finding:** PASS.

## 5. Proof-exposition audit

The current manuscript has visible proof environments for the material propositions and Appendix lemmas. The recent exposition repairs make the following transitions explicit:

- FOC → backup 2×2 linear system;
- state/profile surplus → location-weighted expected surplus;
- expected surplus → policy rational functions;
- rational functions → Bernstein sign objects;
- root isolation + strict concavity → global best response;
- lemma chain → theorem.

Routine algebra remains compressed where it does not carry conceptual content.

No remaining instance was identified where a specialist referee must open production code merely to discover what mathematical object is being proved.

**Finding:** PASS.

## 6. Clean-room gap classification

| Potential gap | Classification | Resolution |
|---|---|---|
| Full symbolic expansion of large certificate polynomials not printed | ROUTINE / delegated mechanical detail | Acceptable; target objects, domain, property, and scripts are identified |
| Full Bernstein coefficient lists not printed | ROUTINE / delegated mechanical detail | Acceptable; exact checker and coefficient archive are identified |
| Root-isolation trace not printed | ROUTINE / delegated mechanical detail | Acceptable; exact interval and checking scripts are identified |
| Open-set persistence not Lean-certified | Not a reviewer-verifiability defect | Analytic proof is stated; formal map explicitly marks it out of scope |
| Full first-principles measure-theoretic construction of Uniform shocks not formalized | Not a reviewer-verifiability defect | Maintained primitive is visible and formal scope boundary is explicit |

No item is classified **BRIDGE NEEDED**, **APPENDIX DETAIL NEEDED**, or **SUBSTANTIVE DEFECT** after the proof-exposition and model-to-certificate bridge repairs merged on 2026-09-25.

## 7. Compression versus verifiability

PASS.

The current split follows the governing rule:

> **Compress routine algebra; preserve proof-critical bridges.**

The manuscript contains the conceptual derivation chain. Mechanically generated large objects remain in the reproducibility archive.

## 8. Stage-specific closure

### Stage 10 retrospective architecture check

PASS retrospectively. The current manuscript contains the bridge equations and named certificate targets that a Stage-10 reviewer-verifiability map would require.

### Stage 11 hostile reconstruction

PASS. A complete headline chain was reconstructed from the manuscript-facing mathematical package without requiring production code to infer a missing conceptual step.

### Stage 13 integrated-manuscript audit

PASS. The integrated manuscript retains the proof-critical chain and the delegated computational/formal mapping.

### Stage 14 final-package preflight

PASS at repository level. The current source package preserves the proof architecture.

The authenticated ERE portal-generated review PDF must still be inspected after upload; this is a separate portal-only Stage-14 item and is not inferred here.

## 9. Final verdict

**PASS — REVIEWER VERIFIABILITY**

A competent specialist referee can identify the relevant mathematical objects, follow the non-routine derivation and proof chain, understand what is delegated to exact computation / Lean, and see why the certified properties imply the paper's conclusions.

This verdict does not assert that every generated polynomial or coefficient can be reproduced manually from the PDF. It certifies that the manuscript-facing package is sufficiently explicit for specialist review and that delegated mechanical computations are mathematically identified and reproducible.

## 10. Remaining non-v2.7 submission blockers

This report closes the reviewer-verifiability workflow delta only. It does not close:

1. the author's personal intellectual-contribution / provenance confirmation;
2. authenticated Editorial Manager article-type, file-designation, declaration, and warning checks;
3. inspection of the portal-generated review PDF;
4. Stage-15 approval of the exact final package.
