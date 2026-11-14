import Mathlib
import RescueHotellingCore

/-!
Pure strategic transfer bargaining in the paper: a proposer offers an
unrestricted real lump-sum transfer; responder accepts exactly when
their incremental payoff is nonnegative, with acceptance at equality.
The optimal proposer gain is max(0, joint surplus), whether that total
surplus is positive or negative. This verifies the *bargaining subgame*
under those complete-information assumptions, not full SPNE.
-/
noncomputable section
namespace RescueHotellingBargaining
open RescueHotelling

def proposerGain (own responder transfer : ℝ) : ℝ :=
  if 0 ≤ responder+transfer then own-transfer else 0

theorem proposer_gain_never_exceeds_joint_surplus_option
    (own responder transfer : ℝ) :
    proposerGain own responder transfer ≤ max 0 (own+responder) := by
  unfold proposerGain
  split_ifs with hAcc
  · have hAtMost : own-transfer ≤ own+responder := by linarith
    exact le_trans hAtMost (le_max_right 0 _)
  · exact le_max_left 0 _

theorem proposer_can_attain_optimal_joint_surplus_option
    (own responder : ℝ) :
    ∃ transfer : ℝ,
      proposerGain own responder transfer = max 0 (own+responder) := by
  by_cases hS : 0 ≤ own+responder
  · refine ⟨-responder, ?_⟩
    have haccept : 0 ≤ responder + -responder := by simp
    unfold proposerGain
    rw [if_pos haccept, max_eq_right hS]
    ring
  · refine ⟨-responder-1, ?_⟩
    have hrejected : ¬ (0 ≤ responder + (-responder-1)) := by linarith
    have hSneg : own+responder ≤ 0 := le_of_lt (lt_of_not_ge hS)
    unfold proposerGain
    rw [if_neg hrejected, max_eq_left hSneg]

theorem proposer_gain_attains_global_maximum (own responder : ℝ) :
    (∃ transfer : ℝ,
      proposerGain own responder transfer = max 0 (own+responder)) ∧
    (∀ transfer : ℝ,
      proposerGain own responder transfer ≤ max 0 (own+responder)) := by
  exact ⟨proposer_can_attain_optimal_joint_surplus_option own responder,
    proposer_gain_never_exceeds_joint_surplus_option own responder⟩

theorem symmetric_random_proposer_payoff (surplus : ℝ) :
    (1/2 : ℝ)*max 0 surplus+(1/2 : ℝ)*0 = max 0 surplus/2 := by
  ring

end RescueHotellingBargaining
#print axioms RescueHotellingBargaining.proposer_gain_attains_global_maximum
