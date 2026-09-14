import Mathlib

namespace PCPPR.MarginalDecomposition

/-- T8: at a symmetric origin with zero marginal public cost, symmetry gives
MS = 2*S_aA and ML = S_aA/2 + 2*b*lambda. -/
theorem plant_attraction_decomposition
    (MS ML Sa b lambda : ℝ)
    (hMS : MS = 2 * Sa)
    (hML : ML = Sa / 2 + 2 * b * lambda) :
    ML = MS / 4 + 2 * b * lambda := by
  linarith

/-- Proposition 1's threshold equivalence. -/
theorem attraction_threshold_iff
    {MS ML b lambda : ℝ}
    (hlambda : 0 < lambda)
    (hMS : MS < 0)
    (hdecomp : ML = MS / 4 + 2 * b * lambda) :
    ML > 0 ↔ b > -MS / (8 * lambda) := by
  constructor
  · intro hML
    have hden : 0 < 8 * lambda := by positivity
    apply (div_lt_iff₀ hden).2
    nlinarith
  · intro hb
    have hden : 0 < 8 * lambda := by positivity
    have hmul := (div_lt_iff₀ hden).1 hb
    nlinarith

/-- The first transparent-conflict inequality is exactly MS<0 under
MS=E0+R0. -/
theorem social_conflict_iff
    {MS E0 R0 : ℝ} (hMS : MS = E0 + R0) :
    MS < 0 ↔ -R0 > E0 := by
  rw [hMS]
  linarith

/-- Under the decomposition, the pair of transparent inequalities implies
the marginal sign conflict.  This theorem deliberately makes no global
planner or Nash-equilibrium claim. -/
theorem transparent_conflict_implies_marginal_signs
    {MS ML E0 R0 b lambda : ℝ}
    (hMSdef : MS = E0 + R0)
    (hdecomp : ML = MS / 4 + 2 * b * lambda)
    (h1 : -R0 > E0)
    (h2 : 8 * b * lambda > -E0 - R0) :
    MS < 0 ∧ 0 < ML := by
  constructor
  · rw [hMSdef]
    linarith
  · rw [hMSdef] at hdecomp
    linarith

/-- Conversely, given the maintained MS decomposition, the marginal sign
conflict is equivalent to the two inequalities printed in equation (23). -/
theorem marginal_signs_imply_transparent_conflict
    {MS ML E0 R0 b lambda : ℝ}
    (hMSdef : MS = E0 + R0)
    (hdecomp : ML = MS / 4 + 2 * b * lambda)
    (hMSneg : MS < 0)
    (hMLpos : 0 < ML) :
    -R0 > E0 ∧ 8 * b * lambda > -E0 - R0 := by
  constructor
  · rw [hMSdef] at hMSneg
    linarith
  · rw [hMSdef] at hdecomp
    linarith

end PCPPR.MarginalDecomposition
