# Reviewer Verifiability Map — v4

**Date:** 2026-10-03  
**Canonical scientific freeze:** `PCPPR-THEORY-FREEZE-2026-10-03-v4`  
**Audited main:** `8869e6f1b342bc73e7b5a3c09dc685d607e1ce91`  
**Workflow:** Theory Paper Research Pipeline v2.5 / Reviewer Verifiability Gate

## Governing rule

A specialist referee should be able to reconstruct the proof-critical chain from the
manuscript-facing package without opening production code merely to discover what
mathematical object is being proved.

Machine assistance may certify large exact objects, but the manuscript must expose:

[
	ext{object}
ightarrow
	ext{domain}
ightarrow
	ext{certified property}
ightarrow
	ext{economic implication}.
]

## Headline derivation / proof map

| ID | Claim / object | Human-readable manuscript chain | Proof / bridge that remains visible | Machine / formal artifact | Scope state |
|---|---|---|---|---|---|
| RV1 | Cournot and monopoly continuation | utility → inverse demand → FOCs → duopoly/monopoly quantities and profits | Sec. 3; App. product-market identities | symbolic checks; Lean product-market layer | PASS |
| RV2 | Global backup best response | availability states → expected profit → strict own concavity → clipped BR | (Pi_i), `backup-br-global`, `backup-linear-system` | exact regularity/interiority certificate | PASS |
| RV3 | Unique backup equilibrium | clipped BR + Lipschitz constant (<1) → contraction; certified interior fixed point | `backup-contraction-bound`; Lemma continuation | `verify_global_certificate.py`; Lean only partial | PASS |
| RV4 | Unique location continuation | location-contingent profits → (d_A,d_B) → affine cutoff BR → endpoint interiority → (|B|<1) → unique fixed point | `location-br`, `location-endpoints`, `location-prob` | exact endpoint/denominator certificate | PASS |
| RV5 | National surplus policy object | state surplus → profile-specific (S^{XY}) → location-weighted (mathcal S) → (W,G_A,G_B) | `surplus`, `expected-surplus-location`, government/planner equations | symbolic/rational reconstruction | PASS |
| RV6 | Plant-attraction marginal decomposition | symmetry + incidence rule + zero marginal public cost at origin | Proposition Plant-attraction threshold | exact symbolic identity | PASS |
| RV7 | Canonical marginal sign conflict | exact witness → (M_S<0<M_L) | Sec. 4 witness and marginal definitions | exact marginal generator / exhibit checker | PASS |
| RV8 | Unique planner optimum at zero | unique downstream continuation → rational (W) → exact signs (W_{a_A}<0,W_{a_B}<0) on full square → monotonicity | Lemma Global planner monotonicity | Bernstein exact certificate | PASS |
| RV9 | Positive symmetric local policy Nash equilibrium | exact diagonal FOC root (alpha) + own-policy strict concavity on full feasible interval against root enclosure → unique global BR | Lemma Global local-government best response | exact root isolation + Bernstein concavity certificate | PASS |
| RV10 | Headline theorem at witness | RV3/RV4 continuations + RV8 planner + RV9 local Nash | explicit Proof of Theorem at canonical witness | same exact certificates | PASS |
| RV11 | Nonempty-open-set persistence | normalize policy domain → uniform strict margins → IFT with full diagonal derivative → preserved global BR | Lemma Persistence around canonical witness | analytic proof; exact derivative sign input | PASS |
| RV12 | Welfare channel decomposition | exact state surplus + private FOC → social/private readiness wedge | Sec. 5 derivation + Table 1 | exact derivatives / table generator | PASS |
| RV13 | Δ=0 benchmark | solve altered continuation directly → polynomial planner/local objectives → exact Bernstein bounds | Proposition Conflict with no incremental sole-survivor rent | `verify_benchmarks.py` | PASS |
| RV14 | Product-substitutability figure | exact origin marginals over (gamma) + isolated thresholds | Sec. 4 text and caption state figure is not equilibrium curve | `verify_marginal_exhibits.py` | PASS |
| RV15 | Diagnostic portability | alternative risk / logistic location models re-solved numerically; constructional matching disclosed | Discussion diagnostic portability | portability scripts / v4 Stage-7.5A certificate | NUMERICALLY SUPPORTED ONLY |
| RV16 | Lean scope | manuscript theorem → bounded formal objects / explicit supplied premises / explicit unformalized bridges | App. Scope of Lean formalization | Lean project + formal map + CI | PROOF-CRITICAL CORE |

## Complete headline proof reconstruction

A referee can reconstruct Theorem 1 using only the paper-facing mathematical package in
the following order.

### Step 1 — Solve the downstream product market

Sec. 3 derives the unique duopoly and monopoly state payoffs from the displayed inverse
demand system.

### Step 2 — Solve the backup game on the actual feasible strategy set

The paper displays the expected-profit function and shows strict own concavity. The global
best response is explicitly **clipped** to ([0,1]). The paper does not infer uniqueness
from the interior FOC alone.

The visible bridge is:

[
BR_i(r_j)
=
operatorname{clip}_{[0,1]}
left{rac{pi_Ds_i+Delta J(1-r_j)}{k}ight},
]

with

[
rac{Delta J}{k}
leq
rac{Delta q_0}{k}
<1.
]

The contraction argument is human-readable. Exact computation supplies whole-policy-domain
interiority of the fixed point and denominator signs.

### Step 3 — Solve the private-information location game

The paper defines (d_A,d_B,D(p)), the cutoff response (BR(p)=u_0+Bp), and the endpoint
objects (u_0,u_1). It explains why endpoint interiority gives global no-clipping and
why (B=u_1-u_0) then implies (|B|<1).

The unique probability fixed point is displayed. A reader does not need code to know what
is being certified.

### Step 4 — Construct the welfare and local-policy objects

Sec. 5 displays state-level surplus and then

[
mathcal S
=
p^2S^{AA}+p(1-p)S^{AB}+p(1-p)S^{BA}+(1-p)^2S^{BB}.
]

The government and planner objectives were already defined in Sec. 2. This closes the
model-to-policy bridge.

### Step 5 — Prove planner globality

The Appendix states the rational derivative objects

[
W_{a_A}=P_A/Q_A,qquad W_{a_B}=P_B/Q_B
]

and explains the Bernstein weighted-average principle before invoking it. The exact
certificate proves denominator positivity and numerator negativity on the **entire**
policy square. Strict coordinatewise monotonicity then yields the unique optimum
((0,0)).

### Step 6 — Prove the local Nash equilibrium globally

The paper defines

[
F(a)=G_{A,a_A}(a,a)
]

and gives an exact isolating interval for its unique symmetric root (alpha). It then
separately proves whole-own-domain strict concavity of (G_A(cdot,a_B)) while the rival
action ranges over the root enclosure. Therefore the stationary point is the unique global
best response, including both policy boundaries.

The proof does not equate “FOC root” with “Nash equilibrium.”

### Step 7 — Extend to a nonempty open set

The Appendix normalizes the policy square and uses compactness/continuity to preserve the
strict continuation, denominator, interiority, and planner-sign margins. For the symmetric
policy root it uses the correct diagonal derivative

[
F_a=G_{A,a_Aa_A}+G_{A,a_Aa_B}.
]

It separately preserves the strict clipped-backup contraction margin. The IFT then yields
a nearby positive symmetric root, and preserved own-policy strict concavity keeps it a
global best response.

No uniqueness of all first-stage policy equilibria is claimed.

## Computer-assisted proof disclosure map

| Delegated object | Domain stated? | Property stated? | Economic implication stated? | Reviewer can reproduce? |
|---|---|---|---|---|
| backup determinant/interiority | full policy square | positivity / (0<r_i<1) | certified interior fixed point | YES |
| location endpoint inequalities | full policy square | (0<u_0,u_1<1) | no clipping / (|B|<1) / uniqueness | YES |
| planner derivative signs | full policy square | both partials negative | unique planner optimum | YES |
| local root isolation | full symmetric policy interval | exactly one root in interval | stationary candidate identified | YES |
| local own-policy curvature | full own interval × rival-root enclosure | (G_{A,a_Aa_A}<0) | global unique BR | YES |
| diagonal root derivative | root-enclosure square | (F_a<0) | simple root for IFT | YES |
| marginal exhibit | 101 exact rational (gamma) points + isolated roots | exact (M_S,M_L) | Figure 1 only | YES |
| Δ=0 benchmark | full benchmark policy square | exact polynomial signs / curvature | benchmark planner/Nash claims | YES |

## Formal-verification boundary

Lean is not used as a substitute for the economic proof.

The Appendix explicitly states that:

- the final Lean theorem receives some economic-function/sign bridges as premises;
- full clipped-backup uniqueness is not proved by the final Lean theorem;
- open-set persistence is outside Lean;
- generated finite exact checks using `native_decide` trust the native compiler/runtime;
- Lean does not certify novelty, welfare interpretation, or unencoded extensions.

This wording matches the v4 formal-verification state:
**PASS — PROOF-CRITICAL CORE / BOUNDED SCOPE**.

## Opaque-compression attack

The v4 manuscript was searched for the principal workflow red flags:

- “straightforward algebra”
- unsupported “by symmetry” jumps
- “the certificate verifies” without naming the object
- “the solver finds” as proof
- unqualified omitted proof steps

No proof-critical use of those shortcuts was identified.

Routine expanded polynomial algebra is omitted only after the mathematical target and
logical implication have been made explicit.

## Reviewer-verifiability verdict

**PASS.**

A competent specialist referee can reconstruct the complete headline proof architecture
from the manuscript-facing package. Production code is needed to **check** large exact
certificates, not to discover the missing economic or mathematical bridge.
