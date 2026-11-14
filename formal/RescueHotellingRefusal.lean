import Mathlib
import RescueHotellingCore
import RescueHotellingModelCheck
import RescueHotellingLocation

/-!
R1 refusal-deviation exclusion derived from the paper's actual
disagreement and contracting payoff polynomials.
Does NOT prove cross-rival deviations, bargaining strategy SPNE,
nor the original parameter-box certificate.
-/
noncomputable section
namespace RescueHotellingRefusal
open RescueHotelling RescueHotellingLocation

def g (A t V d : ℝ) : ℝ :=
  A*(1-2*d)*(t*d/2+V)+A*t*d*(1-d)/2
def H (A t V F d : ℝ) : ℝ :=
  A*d*(1-d)*(t*d/2+V)-F

theorem stationarity_implies_g (r A t c V d : ℝ)
    (hFOC : G r A t c V d = 0) :
    G0 r t c d = g A t V d := by
  unfold G G0 g at *
  linarith

theorem refusal_payoff_global_envelope
    (r A t c V d s : ℝ)
    (hr : 0 ≤ r) (ht : 0 ≤ t) (hc : 0 < c) (hs : s ≤ 1)
    (hFOC : G r A t c V d = 0) :
    disagreementPayoff r t c (symmetricRivalPosition d) s -
      disagreementPayoff r t c (symmetricRivalPosition d) d
    ≤ -g A t V d*(s-d)-c*(s-d)^2/2 := by
  have hG0 := stationarity_implies_g r A t c V d hFOC
  have hgap := disagreement_payoff_gap_exact r t c d s
  rw [hG0] at hgap
  have hRt : r*t*(s-6) ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos (mul_nonneg hr ht) (by linarith)
  have hK : noContractRemainder r t c s ≤ -c/2 := by
    unfold noContractRemainder
    linarith
  have hSq : 0 ≤ (s-d)^2 := sq_nonneg _
  have hprod := mul_le_mul_of_nonneg_left hK hSq
  nlinarith [hgap, hprod]

theorem agreement_at_candidate_equals_disagreement_plus_H
    (r A t c V F d : ℝ) :
    agreementPayoff r A t c V F (symmetricRivalPosition d) d =
      disagreementPayoff r t c (symmetricRivalPosition d) d + H A t V F d := by
  rw [agreement_symmetric_payoff, disagreement_symmetric_payoff]
  unfold H
  ring

theorem R1_rules_out_every_same_side_refusal
    (r A t c V F d s : ℝ)
    (hr : 0 ≤ r) (ht : 0 ≤ t) (hc : 0 < c) (hs : s ≤ 1)
    (hFOC : G r A t c V d = 0)
    (hR1 : (g A t V d)^2 / (2*c) < H A t V F d) :
    disagreementPayoff r t c (symmetricRivalPosition d) s <
      agreementPayoff r A t c V F (symmetricRivalPosition d) d := by
  have hEnv := refusal_payoff_global_envelope r A t c V d s hr ht hc hs hFOC
  have hQuad := RescueHotelling.strong_concavity_quadratic_bound
    c (-(g A t V d)) (s-d) hc
  have hSquare : (-(g A t V d)) * (-(g A t V d)) =
      (g A t V d)^2 := by ring
  rw [hSquare] at hQuad
  have hOnPath := agreement_at_candidate_equals_disagreement_plus_H
    r A t c V F d
  nlinarith

end RescueHotellingRefusal
#print axioms RescueHotellingRefusal.R1_rules_out_every_same_side_refusal
