import Mathlib
import RescueHotellingCore

/-!
Construct the closed-form contracting stationary root and establish that
the paper's R0 restrictions imply it exists uniquely in (0,1/2).
This closes the analytic ROOT portion of Proposition 1, not
participation, the global SPNE, or the open parameter box.
-/
noncomputable section
namespace RescueHotellingRoot
open RescueHotelling

def candidateDistance (q t c V : ℝ) : ℝ :=
  2*cCoeff q t V /
    (bCoeff q t c V + Real.sqrt
      ((bCoeff q t c V)^2+4*tCoeff q t*cCoeff q t V))

theorem contractFOC_at_half (q t c V : ℝ) :
    contractFOC q t c V (1/2) =
      (c-4*survival q*t/3-intensity q*t/2)/4 := by
  unfold contractFOC quadratic tCoeff bCoeff cCoeff survival intensity
  ring

theorem closed_form_unique_admissible_root
    (q t c V : ℝ)
    (hq0 : 0 < q) (hq1 : q < 1) (ht : 0 < t)
    (hV : 0 < V)
    (hR0a : 47*intensity q*t/12 < c)
    (hR0b : 4*survival q*t/3+intensity q*t/2 < c) :
    0 < candidateDistance q t c V ∧
      candidateDistance q t c V < 1/2 ∧
      contractFOC q t c V (candidateDistance q t c V) = 0 ∧
      (∀ x : ℝ, 0 ≤ x → contractFOC q t c V x = 0 →
        x = candidateDistance q t c V) := by
  have hA : 0 < intensity q := by
    unfold intensity
    exact mul_pos hq0 (by linarith)
  have hr : 0 < survival q := by
    unfold survival
    linarith
  have hAt : 0 < intensity q*t := mul_pos hA ht
  have hRt : 0 < survival q*t := mul_pos hr ht
  have hT : 0 < tCoeff q t := by
    unfold tCoeff
    positivity
  have hC : 0 < cCoeff q t V := by
    unfold cCoeff
    positivity
  have hB : 0 < bCoeff q t c V := by
    unfold bCoeff
    have hav : 0 ≤ intensity q*V := le_of_lt (mul_pos hA hV)
    nlinarith
  let T := tCoeff q t
  let B := bCoeff q t c V
  let C := cCoeff q t V
  have hRad : 0 ≤ B^2+4*T*C := by
    dsimp [T,B,C]
    positivity
  have hDen : 0 < B+Real.sqrt (B^2+4*T*C) :=
    add_pos_of_pos_of_nonneg hB (Real.sqrt_nonneg _)
  have hroot : contractFOC q t c V (candidateDistance q t c V) = 0 := by
    change quadratic T B C (2*C/(B+Real.sqrt (B^2+4*T*C))) = 0
    simpa only [pow_two] using (quadratic_closed_form_root hT hB hC)
  have hpos : 0 < candidateDistance q t c V := by
    change 0 < 2*C/(B+Real.sqrt (B^2+4*T*C))
    exact div_pos (by positivity) hDen
  have hhalf : 0 < contractFOC q t c V (1/2) := by
    rw [contractFOC_at_half]
    linarith
  have hless : candidateDistance q t c V < 1/2 := by
    by_contra hnot
    have hge : (1/2 : ℝ) ≤ candidateDistance q t c V := le_of_not_gt hnot
    rcases eq_or_lt_of_le hge with heq | hgt
    · rw [heq] at hhalf
      linarith
    · have hinc : contractFOC q t c V (1/2) <
          contractFOC q t c V (candidateDistance q t c V) := by
        change quadratic T B C (1/2) <
          quadratic T B C (candidateDistance q t c V)
        exact quadratic_strict_increase (le_of_lt hT) hB
          (by norm_num) hgt
      linarith
  refine ⟨hpos,hless,hroot,?_⟩
  intro x hx hzero
  by_contra hneq
  rcases lt_or_gt_of_ne hneq with hlt | hgt
  · have hinc : contractFOC q t c V x <
        contractFOC q t c V (candidateDistance q t c V) := by
      change quadratic T B C x <
        quadratic T B C (candidateDistance q t c V)
      exact quadratic_strict_increase (le_of_lt hT) hB hx hlt
    linarith
  · have hinc : contractFOC q t c V (candidateDistance q t c V) <
        contractFOC q t c V x := by
      change quadratic T B C (candidateDistance q t c V) <
        quadratic T B C x
      exact quadratic_strict_increase (le_of_lt hT) hB
        (le_of_lt hpos) hgt
    linarith

end RescueHotellingRoot
#print axioms RescueHotellingRoot.closed_form_unique_admissible_root
