import PCPPR.CanonicalWitness
import PCPPR.Bernstein
import PCPPR.GeneratedCertificates
import Mathlib.Analysis.Convex.Deriv

open Set
open scoped unitInterval

namespace PCPPR.GlobalLocalGovernment

/-- A stationary interior point of a strictly concave objective is its unique
global maximizer on the whole policy interval. -/
theorem strictConcave_stationary_unique_global_max
    {G : ℝ → ℝ} {abar α : ℝ}
    (habar : 0 < abar)
    (hα : α ∈ Ioo (0 : ℝ) abar)
    (hconc : StrictConcaveOn ℝ (Icc (0 : ℝ) abar) G)
    (hstat : HasDerivAt G 0 α) :
    ∀ x ∈ Icc (0 : ℝ) abar, x ≠ α → G x < G α := by
  let S : Set ℝ := Icc (0 : ℝ) abar
  have hαS : α ∈ S := ⟨le_of_lt hα.1, le_of_lt hα.2⟩
  have hαint : α ∈ interior S := by
    simpa [S, interior_Icc, habar.ne'] using hα
  have hnegStrict : StrictConvexOn ℝ S (-G) := by
    rw [neg_strictConvexOn_iff]
    simpa [S] using hconc
  have hnegStat : HasDerivAt (-G) 0 α := by
    simpa using hstat.neg
  have hright : derivWithin (-G) (Ioi α) α = 0 := by
    exact hnegStat.hasDerivWithinAt.derivWithin (uniqueDiffWithinAt_Ioi α)
  have hmin : IsMinOn (-G) S α :=
    hnegStrict.convexOn.isMinOn_of_rightDeriv_eq_zero hαint hright
  have hmax : IsMaxOn G S α := by
    intro x hx
    have h := hmin hx
    simpa only [Pi.neg_apply, neg_le_neg_iff] using h
  intro x hx hne
  have hle : G x ≤ G α := hmax hx
  have hneq : G x ≠ G α := by
    intro heq
    have hmaxx : IsMaxOn G S x := by
      intro y hy
      calc
        G y ≤ G α := hmax hy
        _ = G x := heq.symm
    have hxeq : x = α := hconc.eq_of_isMaxOn hmaxx hmax hx hαS
    exact hne hxeq
  exact lt_of_le_of_ne hle hneq

/-- T12 generic root-certificate logic. Exact endpoint signs plus continuity
and strict monotonicity establish one and only one zero in the open isolating
interval. -/
theorem existsUnique_root_in_interval
    {F : ℝ → ℝ} {L U : ℝ}
    (hLU : L < U)
    (hcont : ContinuousOn F (Icc L U))
    (hL : 0 < F L)
    (hU : F U < 0)
    (hanti : StrictAntiOn F (Icc L U)) :
    ∃! α : ℝ, α ∈ Ioo L U ∧ F α = 0 := by
  have hzero : (0 : ℝ) ∈ Icc (F U) (F L) :=
    ⟨le_of_lt hU, le_of_lt hL⟩
  have himage : (0 : ℝ) ∈ F '' Icc L U :=
    intermediate_value_Icc' (le_of_lt hLU) hcont hzero
  obtain ⟨α, hαcc, hαzero⟩ := himage
  have hαL : L < α := by
    rcases hαcc.1.eq_or_lt with rfl | hlt
    · linarith
    · exact hlt
  have hαU : α < U := by
    rcases hαcc.2.eq_or_lt with rfl | hlt
    · linarith
    · exact hlt
  refine ⟨α, ⟨⟨hαL, hαU⟩, hαzero⟩, ?_⟩
  intro β hβ
  rcases hβ with ⟨hβoo, hβzero⟩
  have hβcc : β ∈ Icc L U := ⟨le_of_lt hβoo.1, le_of_lt hβoo.2⟩
  rcases lt_trichotomy α β with hab | hab | hba
  · have hlt := hanti hαcc hβcc hab
    rw [hαzero, hβzero] at hlt
    linarith
  · exact hab.symm
  · have hlt := hanti hβcc hαcc hba
    rw [hαzero, hβzero] at hlt
    linarith

/-- T12 concrete generated-certificate layer.

`F` is the canonical diagonal local-government FOC. The generated certificate
(category C) supplies the exact endpoint values and the exact Bernstein
representation of `F'` on the isolating interval. Lean itself checks every
derivative Bernstein coefficient is negative, uses mathlib's actual Bernstein
basis to derive `F' < 0`, and then proves existence and uniqueness of the root.

The `hderivCertificate` premise is the explicit semantic bridge from the
canonical economic FOC to the generated coefficient payload; it is not a sign
or root conclusion. -/
theorem generated_diagonal_FOC_unique_root
    {F : ℝ → ℝ}
    (hcont : ContinuousOn F
      (Icc (PCPPR.GeneratedCertificates.alphaL : ℝ)
           (PCPPR.GeneratedCertificates.alphaU : ℝ)))
    (hLvalue : F (PCPPR.GeneratedCertificates.alphaL : ℝ) =
      (PCPPR.GeneratedCertificates.diagonalFOCNumeratorAtL : ℝ))
    (hUvalue : F (PCPPR.GeneratedCertificates.alphaU : ℝ) =
      (PCPPR.GeneratedCertificates.diagonalFOCNumeratorAtU : ℝ))
    (hderivCertificate :
      ∀ x ∈ interior
        (Icc (PCPPR.GeneratedCertificates.alphaL : ℝ)
             (PCPPR.GeneratedCertificates.alphaU : ℝ)),
        ∃ t : I,
          deriv F x =
            ∑ i : Fin 52,
              bernstein 51 i t *
                (PCPPR.GeneratedCertificates.diagonalFOCDerivativeBernsteinCoeffs i : ℝ)) :
    ∃! α : ℝ,
      α ∈ Ioo (PCPPR.GeneratedCertificates.alphaL : ℝ)
                  (PCPPR.GeneratedCertificates.alphaU : ℝ) ∧
      F α = 0 := by
  have hLUq := PCPPR.GeneratedCertificates.alpha_interval_order
  have hLU : (PCPPR.GeneratedCertificates.alphaL : ℝ) <
      (PCPPR.GeneratedCertificates.alphaU : ℝ) := by
    exact_mod_cast hLUq.2
  have hsign := PCPPR.GeneratedCertificates.diagonal_FOC_endpoint_sign_change
  have hLcert : (0 : ℝ) <
      (PCPPR.GeneratedCertificates.diagonalFOCNumeratorAtL : ℝ) := by
    exact_mod_cast hsign.1
  have hUcert :
      (PCPPR.GeneratedCertificates.diagonalFOCNumeratorAtU : ℝ) < 0 := by
    exact_mod_cast hsign.2
  have hL : 0 < F (PCPPR.GeneratedCertificates.alphaL : ℝ) := by
    rw [hLvalue]
    exact hLcert
  have hU : F (PCPPR.GeneratedCertificates.alphaU : ℝ) < 0 := by
    rw [hUvalue]
    exact hUcert
  have hβ : ∀ i : Fin 52,
      (PCPPR.GeneratedCertificates.diagonalFOCDerivativeBernsteinCoeffs i : ℝ) < 0 := by
    intro i
    exact_mod_cast
      (PCPPR.GeneratedCertificates.diagonalFOCDerivativeBernsteinCoeffs_negative i)
  have hderivNeg :
      ∀ x ∈ interior
        (Icc (PCPPR.GeneratedCertificates.alphaL : ℝ)
             (PCPPR.GeneratedCertificates.alphaU : ℝ)),
        deriv F x < 0 := by
    intro x hx
    obtain ⟨t, ht⟩ := hderivCertificate x hx
    rw [ht]
    exact PCPPR.Bernstein.bernstein_sum_negative 51 t
      (fun i : Fin 52 =>
        (PCPPR.GeneratedCertificates.diagonalFOCDerivativeBernsteinCoeffs i : ℝ)) hβ
  have hanti : StrictAntiOn F
      (Icc (PCPPR.GeneratedCertificates.alphaL : ℝ)
           (PCPPR.GeneratedCertificates.alphaU : ℝ)) := by
    exact strictAntiOn_of_deriv_neg
      (convex_Icc (PCPPR.GeneratedCertificates.alphaL : ℝ)
                  (PCPPR.GeneratedCertificates.alphaU : ℝ))
      hcont hderivNeg
  exact existsUnique_root_in_interval hLU hcont hL hU hanti

/-- T13: the paper's certificate premise G''<0 on the full feasible interval,
together with an interior stationary point, implies a unique global best
response. This theorem separates the generic implication from the exact
certificate supplying the second-derivative sign. -/
theorem second_deriv_negative_stationary_unique_global_max
    {G : ℝ → ℝ} {abar α : ℝ}
    (habar : 0 < abar)
    (hα : α ∈ Ioo (0 : ℝ) abar)
    (hcont : ContinuousOn G (Icc (0 : ℝ) abar))
    (hsecond : ∀ x ∈ interior (Icc (0 : ℝ) abar), (deriv^[2] G) x < 0)
    (hstat : HasDerivAt G 0 α) :
    ∀ x ∈ Icc (0 : ℝ) abar, x ≠ α → G x < G α := by
  have hconc : StrictConcaveOn ℝ (Icc (0 : ℝ) abar) G :=
    strictConcaveOn_of_deriv2_neg (convex_Icc (0 : ℝ) abar) hcont hsecond
  exact strictConcave_stationary_unique_global_max habar hα hconc hstat

/-- Symmetric best-response implication: if the same strictly positive alpha
is the unique global best response of each jurisdiction to alpha, then the
symmetric profile is a positive Nash equilibrium. No uniqueness claim for
the entire policy-game equilibrium correspondence is made. -/
theorem symmetric_positive_nash_of_unique_best_responses
    {GA GB : ℝ → ℝ → ℝ} {abar α : ℝ}
    (hα : α ∈ Ioo (0 : ℝ) abar)
    (hA : ∀ x ∈ Icc (0 : ℝ) abar, GA x α ≤ GA α α)
    (hB : ∀ y ∈ Icc (0 : ℝ) abar, GB α y ≤ GB α α) :
    0 < α ∧
      (∀ x ∈ Icc (0 : ℝ) abar, GA x α ≤ GA α α) ∧
      (∀ y ∈ Icc (0 : ℝ) abar, GB α y ≤ GB α α) := by
  exact ⟨hα.1, hA, hB⟩

end PCPPR.GlobalLocalGovernment
