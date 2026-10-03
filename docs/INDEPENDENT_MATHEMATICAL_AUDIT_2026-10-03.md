# Independent primitive-to-theorem audit, 2026-10-03

Verification actors: **AI + COMPUTATION**, not AUTHOR or EXTERNAL HUMAN.
Starting GitHub main: 990bbe13dd1c3470b378ccd0040a78a030750701.
All previous PASS decisions were treated as claims to attack. Production
Python was imported only after the independent economic objects, signs, and
root isolation had been constructed. Lean success was not a starting premise.

## 1. Cournot block

From \(U=x_1+x_2-(x_1^2+x_2^2+2\gamma x_1x_2)/2\),
\(p_i=1-x_i-\gamma x_j\). With zero marginal production cost,
\(BR_i(x_j)=\max\{0,(1-\gamma x_j)/2\}\). Responses lie in
\([0,1/2]\), and the product response is a contraction of modulus
\(\gamma/2<1\). Neither zero-output corner is a fixed point for
\(0\leq\gamma<1\).

\[
x_D=p_D=\frac1{2+\gamma},\quad
\pi_D=\frac1{(2+\gamma)^2},\quad
CS_D=\frac{1+\gamma}{(2+\gamma)^2},\quad
T_D=\frac{3+\gamma}{(2+\gamma)^2}.
\]

For one available product, maximize \(x(1-x)\):
\(x_M=p_M=1/2,\ \pi_M=1/4,\ CS_M=1/8,\ T_M=3/8\).
The monopoly own second derivative is \(-2\). An independent symbolic
calculation differentiates utility and profits; numerical corner attacks
evaluate profits directly.

## 2. Availability law

Let \(s_i\) be firm i's primary failure probability and J the joint
primary-failure probability. The four primary probabilities are
\((1-s_1-s_2+J,s_1-J,s_2-J,J)\). Independently enumerate the two conditional
backup-success draws, each independent of primary failures and the other
draw, with success probability \(r_i\).
With \(m_i=s_i(1-r_i)\), \(z=J(1-r_1)(1-r_2)\),

| Final availability | Probability |
|---|---|
| neither | \(z\) |
| only 1 | \(m_2-z\) |
| only 2 | \(m_1-z\) |
| both | \(1-m_1-m_2+z\) |

Co-location uses a common primary hazard: \(s_1=s_2=J=q_j\).
Dispersion uses independent regional hazards: \(s_1=q_{L_1}\),
\(s_2=q_{L_2}\), \(J=q_Aq_B\). These structures are not interchanged.
The conditional backup-success law is a model assumption, not a claim
that real backup facilities always have independent exposure.

## 3. Backup game, including corners

State profits minus real readiness cost give
\[
\Pi_i=\pi_D-\pi_Ds_i(1-r_i)+\Delta s_j(1-r_j)
-\Delta J(1-r_i)(1-r_j)-kr_i^2/2,\qquad \Delta=\pi_M-\pi_D.
\]
The derivative is \(\pi_Ds_i+\Delta J(1-r_j)-kr_i\), and the own second
derivative is \(-k<0\) on the whole feasible interval. Its global response is
\[
BR_i(r_j)=\operatorname{clip}_{[0,1]}
\{[\pi_Ds_i+\Delta J(1-r_j)]/k\}.
\]
Projection is 1-Lipschitz. The full response on the compact square is a
contraction when \(\Delta J/k<1\), including corners.
At the witness the uniform bound is \(\Delta q_0/k=75600/162409<1\).

For an interior fixed point, independently eliminate the two FOCs:
\[
\begin{pmatrix}k&\Delta J\\\Delta J&k\end{pmatrix}
\binom{r_1}{r_2}=\binom{\pi_Ds_1+\Delta J}{\pi_Ds_2+\Delta J}.
\]
The determinant is \(k^2-(\Delta J)^2>0\).
Exact full-policy-square signs establish \(0<r_i<1\); hence this solution
is the unique fixed point of the clipped map. This does not make every
unclipped response interior: at q=q0, co-location, and rival readiness
zero, the unclipped response is \(225/169>1\).
Independent clipped-map iteration checks 2,916 policy/profile/start
combinations. Corner parameter cases are separately tested.

At symmetric policies, co-location readiness is
\(q\pi_M/(k+q\Delta)\), and dispersed readiness is
\(q(\pi_D+q\Delta)/(k+q^2\Delta)\).

## 4. Bayesian location game

For every asymmetric policy deviation, recompute all four backup
continuations and profits. Let \(d_A=\pi_1^{AA}-\pi_1^{BA}\),
\(d_B=\pi_1^{AB}-\pi_1^{BB}\), \(D(p)=p d_A+(1-p)d_B\).
A uniform private fit shifter favoring A gives cutoff
\(\varepsilon_i\geq-D(p_2)\) and A-response
\(\operatorname{clip}_{[0,1]}(1/2+D(p_2)/(2H))\).
Its endpoint responses are \(u_0=(H+d_B)/(2H)\),
\(u_1=(H+d_A)/(2H)\).

Exact inequalities on the entire asymmetric policy square establish
\(0<u_0,u_1<1\), so clipping never occurs there. The affine slope
\(B=u_1-u_0\) lies strictly between -1 and 1.
Subtracting the two probability equations gives
\((1+B)(p_1-p_2)=0\); solve the remaining equation:
\[
p_1=p_2=p=\frac{H+d_B}{2H-d_A+d_B}.
\]
Equal firm probabilities do not mean equal government policies.
The supplementary grid endpoint range is [0.322459368,0.677540632];
the largest absolute grid slope is 0.245719676.

## 5. Welfare from states

State surplus includes consumer surplus and operating producer surplus.
Subtract each firm's resource cost once:
\[
S=T_D+(T_M-T_D)(m_1+m_2)+(T_D-2T_M)z-k(r_1^2+r_2^2)/2.
\]
Sum all four location profiles with weights \(p^2,p(1-p),p(1-p),(1-p)^2\)
to obtain \(\mathcal S\). Then
\[
G_A=\mathcal S/2+2bp-ca_A^2/2,\quad
G_B=\mathcal S/2+2b(1-p)-ca_B^2/2,\quad
W=\mathcal S+2b-c(a_A^2+a_B^2)/2.
\]
Exactly \(G_A+G_B=W\), also at asymmetric policies. Hosting benefits are
real and state-independent. National total \(2b\) is constant, while
the local attraction derivative is \(2bp_{a_A}\).
Half-surplus incidence is a maintained reduced-form rule, not a derived
household or ownership allocation.

Fit shocks affect decisions but are excluded from baseline industrial
surplus. This is explicit and internally consistent. The planner is a
**protection-policy-constrained industrial-surplus planner**, not a first
best over output, location, and readiness. Lives, other assets, risk
aversion, and unmodeled spillovers lie outside the criterion.
The Appendix's selected-fit-payoff extension adds
\(R(D)=H/2-D^2/(2H)\), maximized at D=0. All symmetric profiles have D=0,
so the specified nonnegative-share extension preserves the ranking.
It does not cover arbitrary taste valuations.

At a private readiness FOC,
\[
S_{r_i}=\frac{(2-3\gamma)s_i}{8(2+\gamma)}
+\frac{\gamma J(1-r_j)}{2(2+\gamma)}.
\]
Preparedness-resource savings are therefore included in Table 1's
induced-readiness channel; no cost is deducted twice.

## 6. Globality and counterexample searches

The manuscript witness is
\((\gamma,q_0,k,H,b,c,\bar a)=(12/25,3/10,169/3000,1/100,11/200,3,2/25)\).
Independent exact Bernstein signs establish both planner partials
strictly negative on the full square, making (0,0) the unique optimum.
Supplementary attacks: 301-by-301 grid, 50,000 seeded uniform points,
25 gradient-based multistarts, and differential evolution.
No positive gain relative to the origin was found.

Independently rediscovered \(\alpha=0.02301968487055536\).
An independent Sturm calculation counts one numerator root and zero
denominator roots on the full symmetric policy interval. Forty-eight
rational bisections isolate it. Whole-own-domain Bernstein curvature
against the independently isolated rival interval proves strict concavity,
so the root is a global best response against itself, including endpoints.
A 4,001-point derivative scan finds only one stationary point.
Deviation payoff differences at own policies 0 and 0.08 are approximately
\(-2.95386\cdot10^{-5}\) and \(-3.18595\cdot10^{-4}\).

Forty-nine FOC starts, nine damped global-response dynamics starts, and
boundary-response attacks found no additional equilibrium.
One solver reported success at the origin with residual 0.0019308655;
the audit rejected it. Successful roots were separately checked against
direct feasible-payoff maximization. These searches do not prove absence
of asymmetric equilibria or full first-stage uniqueness. Neither is
claimed in the manuscript.

## 7. Open-set logic: all necessary strict margins

For the economic FOC \(F(a,\theta)=G_{A,a_A}(a,a;\theta)\),
\(F_a=G_{A,a_Aa_A}+G_{A,a_Aa_B}\).
Independent witness values are
\(-0.148249423-0.031783426=-0.180032849\).

The strict conditions to preserve together are:

1. \(0<\gamma<1,\ k,H,b,c>0,\ 0<\bar a<q_0<1\).
2. Uniform clipped-backup contraction \(\Delta(\gamma)q_0/k<1\).
3. Nonzero backup determinants and interior readiness in every profile
   over the entire policy square.
4. Nonzero policy/rational denominators.
5. Interior location endpoints and uniform location contraction.
6. Both planner partials uniformly strictly negative.
7. Own-policy curvature strictly negative on the entire own interval
   against a small rival-root neighborhood.
8. A simple symmetric FOC root with its full diagonal derivative nonzero.
9. Positive equilibrium policy strictly below the policy upper bound.

Normalize \(a_j=\bar a x_j\) to a fixed compact square. Uniform strict
conditions have positive minimum slack there. Joint continuity preserves
them in a sufficiently small common primitive neighborhood.
In particular J<=q0 for all histories, so continuity of
\(\Delta(\gamma)q_0/k<1\) supplies the uniform backup contraction margin.
The IFT yields a symmetric interior root; preserved own curvature
separately yields global best responses. Intersect the finitely many
neighborhoods. The set is open **within the maintained symmetric primitive
family**, not independently heterogeneous regional parameters.
No numerical neighborhood radius is claimed.

A numerical attack with 100 common primitive vectors within relative
radius \(10^{-5}\) found no failure. This is not certification of that radius.

## 8. Delta-zero benchmark

Set \(\gamma=0,\ k=2/25,\ c=10\), retaining the other benchmark primitives.
Then \(\Delta=0,\ r=q/(4k)\), with continuation profit and per-firm value
\[
f(q)=(1-q)/4+q^2/(32k),\qquad
t(q)=3(1-q)/8+q^2/(16k).
\]
The cutoff is independent of the rival's location:
\(p=1/2+[f(q_A)-f(q_B)]/(2H)\), and
\(\mathcal S=2[p t(q_A)+(1-p)t(q_B)]\).
Readiness ranges from 11/16 to 15/16 and p from 5/16 to 11/16.
\[
M_S=-3/16,\quad M_L=5/128,\quad
F(a)=5/128-(315/64)a,\quad \alpha=1/126.
\]
Independent full-square planner derivative Bernstein bounds:
[-497/640,-7/128]. Full-own-domain curvature against 1/126:
[-21726685/4064256,-18154585/4064256].
Thus both benchmark optimization claims are global.

This removes incremental sole-survivor rent and strategic backup
substitution. Producer markups and product-availability surplus remain.
It is not a competitive benchmark and does not show market power irrelevant.

## 9. Certificate-generator and exhibit attacks

The independent conversion uses forward substitution in actual Bernstein
basis polynomials rather than the production binomial-ratio algorithm.
Sixty random and six known polynomials, four rectangles (including
nonzero endpoints and a degenerate slice), and three evaluation points
give 792 exact reconstruction identities. Additional tests reject
poles, zeros under strict sign requests, and reversed endpoints, and
check Sturm counts including a repeated root.

After independent certification, compare five economic rational objects,
forty random production transforms, and archive normalizations:
FOC scale -76880 and common planner-derivative scale -19220/3.
Compare all eight generated bivariate coefficient vectors against
independent economic numerators/denominators on their actual full, local,
and root rectangles. Check two root endpoint values and all 52
raw-numerator derivative coefficients, including Lean rational encodings.
The mapped derivative is P'(a) evaluated after a=L+(U-L)t, not dP/dt.
Independently check T9's three exact economic marginal checkpoints.

Figure 1: 101 independently reconstructed points, maximum numerical
discrepancy about \(6\cdot10^{-15}\).
Thresholds: gammaL=0.47458933341847187,
gammaS=0.49829122170464374.
Table 1: direct 0.041459678195; induced -0.047942142418;
MS -0.006482464223; ML 0.001930865521.
Attraction 0.003551481577, lambda=0.032286196153;
\(M_L=M_S/4+2b\lambda\) holds independently.

## Executable evidence

- scripts/independent_model_audit.py: separate numerical economic solver.
- scripts/independent_exact_audit.py: separate symbolic/rational objects,
  conversion, signs, roots, and then production bridge.
- tests/test_independent_audit.py: corner, probability, welfare, and
  conversion regressions, without a production model import.
- docs/independent_*_audit_2026-10-03.json: dated observed snapshots.
- dist/independent_*_audit_2026-10-03.json: fresh run outputs.

Exact checks share SymPy rational arithmetic with production.
Numerical reconstruction uses NumPy/SciPy. Algorithmic independence does
not constitute an independent compiler/arithmetic proof.
Large coefficient checks remain computation with an explicit trust boundary.
