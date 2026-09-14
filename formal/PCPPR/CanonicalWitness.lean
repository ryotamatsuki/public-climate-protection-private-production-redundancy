import PCPPR.MarginalDecomposition

namespace PCPPR.CanonicalWitness

/-- Exact rational canonical parameter vector from paper equation (24). -/
def gamma0 : ℚ := 12 / 25
def q0 : ℚ := 3 / 10
def k0 : ℚ := 169 / 3000
def H0 : ℚ := 1 / 100
def b0 : ℚ := 11 / 200
def c0 : ℚ := 3
def abar0 : ℚ := 2 / 25

/-- Exact product-market primitives evaluated at the canonical parameter vector. -/
def piD0 : ℚ := 1 / (2 + gamma0) ^ 2
def piM0 : ℚ := 1 / 4
def delta0 : ℚ := piM0 - piD0
def TD0 : ℚ := (3 + gamma0) / (2 + gamma0) ^ 2
def TM0 : ℚ := 3 / 8

/-- Exact forward-mode value/derivative pair over Q.  This is intentionally
small and transparent: it mirrors the primitive algebra used by the canonical
normalization audit instead of importing its terminal sign as a hypothesis. -/
structure DualQ where
  v : ℚ
  d : ℚ
  deriving DecidableEq, Repr

namespace DualQ

def const (x : ℚ) : DualQ := ⟨x, 0⟩
def seed (x dx : ℚ) : DualQ := ⟨x, dx⟩
def add (x y : DualQ) : DualQ := ⟨x.v + y.v, x.d + y.d⟩
def neg (x : DualQ) : DualQ := ⟨-x.v, -x.d⟩
def sub (x y : DualQ) : DualQ := add x (neg y)
def mul (x y : DualQ) : DualQ :=
  ⟨x.v * y.v, x.d * y.v + x.v * y.d⟩
def div (x y : DualQ) : DualQ :=
  ⟨x.v / y.v, (x.d * y.v - x.v * y.d) / y.v ^ 2⟩
def scale (a : ℚ) (x : DualQ) : DualQ := mul (const a) x
def sq (x : DualQ) : DualQ := mul x x

end DualQ

open DualQ

inductive Site where
  | A
  | B
  deriving DecidableEq, Repr

def supply (qA qB : DualQ) : Site → DualQ
  | .A => qA
  | .B => qB

def joint (qA qB : DualQ) : Site → Site → DualQ
  | .A, .A => qA
  | .B, .B => qB
  | _, _ => mul qA qB

structure ProfileDual where
  profit1 : DualQ
  surplus : DualQ
  deriving DecidableEq, Repr

/-- The exact canonical continuation block reconstructed directly from the
paper's product-market primitives, joint availability law, backup Nash system,
and surplus formula.  All arithmetic remains rational. -/
def profileDual (qA qB : DualQ) (l1 l2 : Site) : ProfileDual :=
  let s1 := supply qA qB l1
  let s2 := supply qA qB l2
  let J := joint qA qB l1 l2
  let dJ := scale delta0 J
  let a1 := add (scale piD0 s1) dJ
  let a2 := add (scale piD0 s2) dJ
  let den := sub (const (k0 ^ 2)) (sq dJ)
  let r1 := div (sub (scale k0 a1) (mul dJ a2)) den
  let r2 := div (sub (scale k0 a2) (mul dJ a1)) den
  let one := const 1
  let nr1 := sub one r1
  let nr2 := sub one r2
  let profit1 :=
    sub
      (sub
        (add
          (sub (const piD0) (mul (scale piD0 s1) nr1))
          (mul (scale delta0 s2) nr2))
        (mul (mul dJ nr1) nr2))
      (scale (k0 / 2) (sq r1))
  let m1 := mul s1 nr1
  let m2 := mul s2 nr2
  let z := mul (mul J nr1) nr2
  let surplus :=
    sub
      (add
        (add (const TD0) (scale (TM0 - TD0) (add m1 m2)))
        (scale (TD0 - 2 * TM0) z))
      (scale (k0 / 2) (add (sq r1) (sq r2)))
  ⟨profit1, surplus⟩

structure ExpectedDual where
  p : DualQ
  surplus : DualQ
  deriving DecidableEq, Repr

/-- Location fixed point and expected surplus, evaluated from the four plant
location profiles exactly as in the canonical economic model. -/
def expectedDual (qA qB : DualQ) : ExpectedDual :=
  let AA := profileDual qA qB .A .A
  let AB := profileDual qA qB .A .B
  let BA := profileDual qA qB .B .A
  let BB := profileDual qA qB .B .B
  let dA := sub AA.profit1 BA.profit1
  let dB := sub AB.profit1 BB.profit1
  let p := div (add (const H0) dB)
    (add (sub (const (2 * H0)) dA) dB)
  let oneMinusP := sub (const 1) p
  let surplus :=
    add
      (add
        (mul (sq p) AA.surplus)
        (scale 2 (mul (mul p oneMinusP) AB.surplus)))
      (mul (sq oneMinusP) BB.surplus)
  ⟨p, surplus⟩

/-- Planner common-policy marginal at the origin, computed from the economic
pipeline itself. q_A and q_B both fall one-for-one with the common policy. -/
def MSModel : ℚ :=
  (expectedDual (seed q0 (-1)) (seed q0 (-1))).surplus.d

/-- Plant-attraction derivative under a unilateral A policy change. -/
def lambdaModel : ℚ :=
  (expectedDual (seed q0 (-1)) (seed q0 0)).p.d

/-- Local-government unilateral marginal at the origin, including the plant
attraction term 2 b p'. -/
def MLModel : ℚ :=
  let out := expectedDual (seed q0 (-1)) (seed q0 0)
  out.surplus.d / 2 + 2 * b0 * out.p.d

/-- Independently reconstructed exact planner common-policy marginal at the origin.
This terminal rational is retained as an audit checkpoint, not as a premise. -/
def MS0 : ℚ :=
  -10651615424202276975145722347598033 /
    1643142955852817767935206845318567220

/-- Independently reconstructed exact local unilateral marginal at the origin.
This terminal rational is retained as an audit checkpoint, not as a premise. -/
def ML0 : ℚ :=
  717004319683029789719275067656347639039338956556328208736741107 /
    371338299758534039173259783433492599466444392472176495572868210320

/-- Exact plant-attraction response at the symmetric origin. -/
def lambda0 : ℚ :=
  434154857586848106411014309280220 /
    13447073651202386523890945009299301

/-- T9 statement-fidelity bridge: the Lean economic pipeline evaluates to the
independently reconstructed exact planner marginal. -/
theorem MSModel_eq_checkpoint : MSModel = MS0 := by
  native_decide

/-- T9 statement-fidelity bridge for the local unilateral marginal. -/
theorem MLModel_eq_checkpoint : MLModel = ML0 := by
  native_decide

/-- T9 statement-fidelity bridge for the plant-attraction response. -/
theorem lambdaModel_eq_checkpoint : lambdaModel = lambda0 := by
  native_decide

/-- T9: exact rational sign of the planner marginal, now attached to the
primitive economic calculation rather than a hard-coded terminal rational. -/
theorem canonical_MS_negative : MSModel < 0 := by
  rw [MSModel_eq_checkpoint]
  norm_num [MS0]

/-- T9: exact rational sign of the local-government marginal, attached to the
primitive economic calculation. -/
theorem canonical_ML_positive : 0 < MLModel := by
  rw [MLModel_eq_checkpoint]
  norm_num [ML0]

/-- Exact rational sign of the plant-attraction response from the same model. -/
theorem canonical_lambda_positive : 0 < lambdaModel := by
  rw [lambdaModel_eq_checkpoint]
  norm_num [lambda0]

/-- The model-derived exact values satisfy the paper's central marginal
decomposition identically. -/
theorem canonical_marginal_decomposition :
    MLModel = MSModel / 4 + 2 * b0 * lambdaModel := by
  rw [MLModel_eq_checkpoint, MSModel_eq_checkpoint, lambdaModel_eq_checkpoint]
  norm_num [ML0, MS0, b0, lambda0]

/-- Rational endpoints of the local-government FOC isolating interval. -/
def alphaL : ℚ := 1649737 / 71666359
def alphaU : ℚ := 380091 / 16511564

/-- T12 arithmetic layer: the isolating interval is nonempty, positive, and
strictly inside the canonical policy interval. -/
theorem alpha_interval_inside_policy_domain :
    0 < alphaL ∧ alphaL < alphaU ∧ alphaU < abar0 := by
  norm_num [alphaL, alphaU, abar0]

end PCPPR.CanonicalWitness
