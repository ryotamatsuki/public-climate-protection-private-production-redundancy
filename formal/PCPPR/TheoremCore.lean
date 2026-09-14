import PCPPR.GlobalPlanner
import PCPPR.GlobalLocalGovernment

open Set

namespace PCPPR.TheoremCore

/-- T14 generic implication layer for the canonical-witness part of Theorem 1.
The assumptions are certificate-level local facts (full-domain planner
derivative signs and full-own-domain local concavity), not the desired global
conclusions themselves.

The open-neighborhood persistence claim is intentionally absent from this theorem. -/
theorem canonical_witness_core
    {W GA GB : ℝ → ℝ → ℝ}
    {abar alpha L U : ℝ}
    (habar : 0 < abar)
    (halpha : alpha ∈ Ioo (0 : ℝ) abar)
    (hinterval : alpha ∈ Ioo L U)
    (hWcontA : ∀ y ∈ Icc (0 : ℝ) abar,
      ContinuousOn (fun x => W x y) (Icc (0 : ℝ) abar))
    (hWcontB : ∀ x ∈ Icc (0 : ℝ) abar,
      ContinuousOn (fun y => W x y) (Icc (0 : ℝ) abar))
    (hWderivA : ∀ y ∈ Icc (0 : ℝ) abar,
      ∀ x ∈ interior (Icc (0 : ℝ) abar), deriv (fun t => W t y) x < 0)
    (hWderivB : ∀ x ∈ Icc (0 : ℝ) abar,
      ∀ y ∈ interior (Icc (0 : ℝ) abar), deriv (fun t => W x t) y < 0)
    (hGAcont : ContinuousOn (fun x => GA x alpha) (Icc (0 : ℝ) abar))
    (hGAsecond : ∀ x ∈ interior (Icc (0 : ℝ) abar),
      (deriv^[2] (fun t => GA t alpha)) x < 0)
    (hGAstationary : HasDerivAt (fun x => GA x alpha) 0 alpha)
    (hsym : ∀ x y, GB x y = GA y x) :
    (∀ a ∈ Icc (0 : ℝ) abar, ∀ b ∈ Icc (0 : ℝ) abar,
      W 0 0 ≤ W a b → a = 0 ∧ b = 0) ∧
    alpha ∈ Ioo L U ∧
    0 < alpha ∧
    (∀ x ∈ Icc (0 : ℝ) abar, GA x alpha ≤ GA alpha alpha) ∧
    (∀ y ∈ Icc (0 : ℝ) abar, GB alpha y ≤ GB alpha alpha) := by
  have hAanti : ∀ y ∈ Icc (0 : ℝ) abar,
      StrictAntiOn (fun x => W x y) (Icc (0 : ℝ) abar) := by
    intro y hy
    exact GlobalPlanner.strictAntiOn_Icc_of_deriv_neg (hWcontA y hy) (hWderivA y hy)
  have hBanti : ∀ x ∈ Icc (0 : ℝ) abar,
      StrictAntiOn (fun y => W x y) (Icc (0 : ℝ) abar) := by
    intro x hx
    exact GlobalPlanner.strictAntiOn_Icc_of_deriv_neg (hWcontB x hx) (hWderivB x hx)
  have hplanner : ∀ a ∈ Icc (0 : ℝ) abar, ∀ b ∈ Icc (0 : ℝ) abar,
      W 0 0 ≤ W a b → a = 0 ∧ b = 0 := by
    intro a ha b hb hmax
    exact GlobalPlanner.origin_unique_global_maximizer habar hAanti hBanti ha hb hmax
  have hlocalStrict :=
    GlobalLocalGovernment.second_deriv_negative_stationary_unique_global_max
      habar halpha hGAcont hGAsecond hGAstationary
  have hA : ∀ x ∈ Icc (0 : ℝ) abar, GA x alpha ≤ GA alpha alpha := by
    intro x hx
    by_cases heq : x = alpha
    · simp [heq]
    · exact le_of_lt (hlocalStrict x hx heq)
  have hB : ∀ y ∈ Icc (0 : ℝ) abar, GB alpha y ≤ GB alpha alpha := by
    intro y hy
    rw [hsym alpha y, hsym alpha alpha]
    exact hA y hy
  exact ⟨hplanner, hinterval, halpha.1, hA, hB⟩

/-- T14 final canonical-witness gate.

Unlike `canonical_witness_core`, this theorem does not receive the symmetric
policy root as a hypothesis. It obtains the unique root from T12's generated
exact certificate interface, uses the exact canonical interval theorem to put
that root strictly inside the feasible policy domain, converts the certified
FOC root to stationarity through the explicit category-C semantic bridge, and
then invokes the T13 full-domain best-response theorem. The planner side is the
T11 coordinatewise-monotonicity implication.

Category-C premises here are exactly the semantic bridges from the canonical
economic expressions to the generated derivative/FOC/second-derivative
certificates. Existence/uniqueness of alpha and all global-optimization
implications are derived in Lean. -/
theorem canonical_witness_from_generated_certificates
    {W GA GB : ℝ → ℝ → ℝ} {F : ℝ → ℝ}
    (hWcontA : ∀ y ∈ Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ),
      ContinuousOn (fun x => W x y)
        (Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ)))
    (hWcontB : ∀ x ∈ Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ),
      ContinuousOn (fun y => W x y)
        (Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ)))
    (hWderivA : ∀ y ∈ Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ),
      ∀ x ∈ interior (Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ)),
        deriv (fun t => W t y) x < 0)
    (hWderivB : ∀ x ∈ Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ),
      ∀ y ∈ interior (Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ)),
        deriv (fun t => W x t) y < 0)
    (hFcont : ContinuousOn F
      (Icc (GeneratedCertificates.alphaL : ℝ)
           (GeneratedCertificates.alphaU : ℝ)))
    (hFLvalue : F (GeneratedCertificates.alphaL : ℝ) =
      (GeneratedCertificates.diagonalFOCNumeratorAtL : ℝ))
    (hFUvalue : F (GeneratedCertificates.alphaU : ℝ) =
      (GeneratedCertificates.diagonalFOCNumeratorAtU : ℝ))
    (hFderivCertificate :
      ∀ x ∈ interior
        (Icc (GeneratedCertificates.alphaL : ℝ)
             (GeneratedCertificates.alphaU : ℝ)),
        ∃ t : I,
          deriv F x =
            ∑ i : Fin 52,
              bernstein 51 i t *
                (GeneratedCertificates.diagonalFOCDerivativeBernsteinCoeffs i : ℝ))
    (hGAcont :
      ∀ alpha ∈ Ioo (GeneratedCertificates.alphaL : ℝ)
                     (GeneratedCertificates.alphaU : ℝ),
        ContinuousOn (fun x => GA x alpha)
          (Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ)))
    (hGAsecond :
      ∀ alpha ∈ Ioo (GeneratedCertificates.alphaL : ℝ)
                     (GeneratedCertificates.alphaU : ℝ),
        ∀ x ∈ interior (Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ)),
          (deriv^[2] (fun t => GA t alpha)) x < 0)
    (hFOCstationaryBridge :
      ∀ alpha ∈ Ioo (GeneratedCertificates.alphaL : ℝ)
                     (GeneratedCertificates.alphaU : ℝ),
        F alpha = 0 → HasDerivAt (fun x => GA x alpha) 0 alpha)
    (hsym : ∀ x y, GB x y = GA y x) :
    (∀ a ∈ Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ),
      ∀ b ∈ Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ),
        W 0 0 ≤ W a b → a = 0 ∧ b = 0) ∧
    ∃ alpha : ℝ,
      alpha ∈ Ioo (GeneratedCertificates.alphaL : ℝ)
                   (GeneratedCertificates.alphaU : ℝ) ∧
      alpha ∈ Ioo (0 : ℝ) (CanonicalWitness.abar0 : ℝ) ∧
      (∀ x ∈ Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ),
        GA x alpha ≤ GA alpha alpha) ∧
      (∀ y ∈ Icc (0 : ℝ) (CanonicalWitness.abar0 : ℝ),
        GB alpha y ≤ GB alpha alpha) := by
  obtain ⟨alpha, hroot, _hrootUnique⟩ :=
    GlobalLocalGovernment.generated_diagonal_FOC_unique_root
      hFcont hFLvalue hFUvalue hFderivCertificate
  have hgenOrderQ := GeneratedCertificates.alpha_interval_order
  have hLpos : (0 : ℝ) < (GeneratedCertificates.alphaL : ℝ) := by
    exact_mod_cast hgenOrderQ.1
  have hcanonical := CanonicalWitness.alpha_interval_inside_policy_domain
  have hUeqQ : GeneratedCertificates.alphaU = CanonicalWitness.alphaU := by
    rfl
  have hUbarQ : GeneratedCertificates.alphaU < CanonicalWitness.abar0 := by
    rw [hUeqQ]
    exact hcanonical.2.2
  have hUbar : (GeneratedCertificates.alphaU : ℝ) <
      (CanonicalWitness.abar0 : ℝ) := by
    exact_mod_cast hUbarQ
  have habarQ : (0 : ℚ) < CanonicalWitness.abar0 :=
    lt_trans hcanonical.1 (lt_trans hcanonical.2.1 hcanonical.2.2)
  have habar : (0 : ℝ) < (CanonicalWitness.abar0 : ℝ) := by
    exact_mod_cast habarQ
  have halpha : alpha ∈ Ioo (0 : ℝ) (CanonicalWitness.abar0 : ℝ) := by
    exact ⟨lt_trans hLpos hroot.1.1, lt_trans hroot.1.2 hUbar⟩
  have hstationary := hFOCstationaryBridge alpha hroot.1 hroot.2
  have hcore := canonical_witness_core
    (W := W) (GA := GA) (GB := GB)
    (abar := (CanonicalWitness.abar0 : ℝ))
    (alpha := alpha)
    (L := (GeneratedCertificates.alphaL : ℝ))
    (U := (GeneratedCertificates.alphaU : ℝ))
    habar halpha hroot.1
    hWcontA hWcontB hWderivA hWderivB
    (hGAcont alpha hroot.1) (hGAsecond alpha hroot.1)
    hstationary hsym
  exact ⟨hcore.1, ⟨alpha, hroot.1, halpha,
    hcore.2.2.2.1, hcore.2.2.2.2⟩⟩

end PCPPR.TheoremCore
