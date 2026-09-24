import PCPPR.Primitives

namespace PCPPR.Availability

/-- Marginal unavailability probability implied by primary failure and failed backup. -/
def m (s r : ℝ) : ℝ := s * (1 - r)

/-- Joint unavailability probability under the paper's maintained conditional-independence law. -/
def z (J r1 r2 : ℝ) : ℝ := J * (1 - r1) * (1 - r2)

/-- Both firms finally available. -/
def p11 (s1 s2 J r1 r2 : ℝ) : ℝ :=
  1 - m s1 r1 - m s2 r2 + z J r1 r2

/-- Firm 1 available and firm 2 unavailable. -/
def p10 (s1 s2 J r1 r2 : ℝ) : ℝ :=
  m s2 r2 - z J r1 r2

/-- Firm 1 unavailable and firm 2 available. -/
def p01 (s1 s2 J r1 r2 : ℝ) : ℝ :=
  m s1 r1 - z J r1 r2

/-- Both firms finally unavailable. -/
def p00 (s1 s2 J r1 r2 : ℝ) : ℝ := z J r1 r2

/-- The four final availability-state probabilities sum to one.  This is
an algebraic consequence of the state-accounting definitions, not an extra
probability assumption. -/
theorem state_probabilities_sum_one (s1 s2 J r1 r2 : ℝ) :
    p11 s1 s2 J r1 r2 + p10 s1 s2 J r1 r2 +
      p01 s1 s2 J r1 r2 + p00 s1 s2 J r1 r2 = 1 := by
  unfold p11 p10 p01 p00
  ring

/-- Nonnegativity is deliberately conditional on the exact Fréchet-style
bounds needed for these reduced-form probabilities.  Lean does not silently
infer these bounds from an economic interpretation of `s`, `J`, or `r`. -/
theorem state_probabilities_nonnegative
    (s1 s2 J r1 r2 : ℝ)
    (hz0 : 0 ≤ z J r1 r2)
    (hz_m1 : z J r1 r2 ≤ m s1 r1)
    (hz_m2 : z J r1 r2 ≤ m s2 r2)
    (hunion : m s1 r1 + m s2 r2 - z J r1 r2 ≤ 1) :
    0 ≤ p11 s1 s2 J r1 r2 ∧
    0 ≤ p10 s1 s2 J r1 r2 ∧
    0 ≤ p01 s1 s2 J r1 r2 ∧
    0 ≤ p00 s1 s2 J r1 r2 := by
  unfold p11 p10 p01 p00
  constructor
  · linarith
  constructor
  · linarith
  constructor
  · linarith
  · exact hz0

end PCPPR.Availability
