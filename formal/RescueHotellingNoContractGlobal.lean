import Mathlib
import RescueHotellingCore
import RescueHotellingLocation
import RescueHotellingCrossing

/-!
No-contract crossing deviations and the global reduced location Nash
in the exact baseline model (Proposition 2's location subgame).

No claim is made here about the whole extensive-form SPNE. The result
requires the stationarity equality and the bounds explicitly listed.
-/
noncomputable section
namespace RescueHotellingNoContractGlobal
open RescueHotelling RescueHotellingLocation RescueHotellingCrossing

def crossingNoContractPayoff (r t c d u : ℝ) : ℝ :=
  r*crossingDeviatorRevenue t d u-c*(d/2+u)^2/2

def locationPayoff (r t c d y : ℝ) : ℝ :=
  if y ≤ symmetricRivalPosition d then
    disagreementPayoff r t c (symmetricRivalPosition d)
      (symmetricRivalPosition d-y)
  else
    crossingNoContractPayoff r t c d (y-symmetricRivalPosition d)

theorem crossingNoContractUpper
    (r t c d u : ℝ)
    (hr : 0 ≤ r) (ht : 0 ≤ t)
    (hd : 0 ≤ d) (hd1 : d ≤ 1)
    (hu : 0 ≤ u) (hur : u ≤ (1-d)/2) :
    crossingNoContractPayoff r t c d u ≤
      -c*d*d/8+(r*t/2-c*d/2)*u-c*u*u/2 := by
  have hrev := (crossing_revenue_upper_bounds t d u ht hd hd1 hu hur).1
  have hprod := mul_le_mul_of_nonneg_left hrev hr
  unfold crossingNoContractPayoff
  nlinarith

theorem crossingR0FromFOC
    (r t c d : ℝ)
    (hrt : 0 < r*t) (hc : 0 < c) (hd : 0 < d)
    (hd1 : d ≤ 1)
    (hFOC : G0 r t c d = 0)
    (hcost : 4*r*t < 3*c) :
    ((r*t/2-c*d/2)^2)/(2*c) < r*t*d/2 := by
  have hlinear : r*t/2-c*d/2 = r*t*d/3 := by
    unfold G0 at hFOC
    linarith
  have hbound : r*t*d < 9*c := by
    have hrt_d : r*t*d ≤ r*t := by
      exact mul_le_of_le_one_right (le_of_lt hrt) hd1
    linarith
  have hrt_d_pos : 0 < r*t*d := mul_pos hrt hd
  rw [hlinear]
  apply (div_lt_iff₀ (by positivity : (0:ℝ) < 2*c)).2
  have hcore : (r*t*d)*(r*t*d) < (r*t*d)*(9*c) := by
    exact mul_lt_mul_of_pos_left hbound hrt_d_pos
  nlinarith

theorem crossingNoContractStrictlyWorse
    (r t c d u : ℝ)
    (hr : 0 ≤ r) (ht : 0 ≤ t) (hrt : 0 < r*t)
    (hc : 0 < c) (hd : 0 < d) (hd1 : d ≤ 1)
    (hu : 0 ≤ u) (hur : u ≤ (1-d)/2)
    (hFOC : G0 r t c d = 0)
    (hcost : 4*r*t < 3*c) :
    crossingNoContractPayoff r t c d u <
      disagreementPayoff r t c (symmetricRivalPosition d) d := by
  have hEnvelope := crossingNoContractUpper r t c d u hr ht hd hd1 hu hur
  have hQuad := RescueHotelling.strong_concavity_quadratic_bound
    c (r*t/2-c*d/2) u hc
  have hBound := crossingR0FromFOC r t c d hrt hc hd hd1 hFOC hcost
  rw [disagreement_symmetric_payoff]
  have hSquare : (r*t/2-c*d/2)*(r*t/2-c*d/2) =
      (r*t/2-c*d/2)^2 := by ring
  rw [hSquare] at hQuad
  linarith

def candidateLeft (d : ℝ) : ℝ := (1-d)/2

theorem candidateNoContract (r t c d : ℝ) (hd : 0 ≤ d) :
    locationPayoff r t c d (candidateLeft d) =
      disagreementPayoff r t c (symmetricRivalPosition d) d := by
  have hloc : candidateLeft d ≤ symmetricRivalPosition d := by
    unfold candidateLeft symmetricRivalPosition
    linarith
  have hdist : symmetricRivalPosition d-candidateLeft d = d := by
    unfold candidateLeft symmetricRivalPosition
    ring
  unfold locationPayoff
  rw [if_pos hloc, hdist]

theorem noContractGlobalBestResponse
    (r t c d : ℝ)
    (hr : 0 ≤ r) (ht : 0 ≤ t) (hrt : 0 < r*t)
    (hc : 0 < c) (hd : 0 < d) (hd1 : d ≤ 1/2)
    (hFOC : G0 r t c d = 0)
    (hcost : 4*r*t < 3*c) :
    ∀ y : ℝ, 0 ≤ y → y ≤ 1 →
      locationPayoff r t c d y ≤ locationPayoff r t c d (candidateLeft d) := by
  intro y hy0 hy1
  rw [candidateNoContract r t c d (le_of_lt hd)]
  by_cases hleft : y ≤ symmetricRivalPosition d
  · have hs : symmetricRivalPosition d-y ≤ 1 := by
      unfold symmetricRivalPosition
      linarith
    have hbest := no_contract_same_side_global_optimum r t c d
      (symmetricRivalPosition d-y) hr ht hc hs hFOC
    unfold locationPayoff
    rw [if_pos hleft]
    exact hbest
  · have hgreater : symmetricRivalPosition d < y := lt_of_not_ge hleft
    have hu : 0 ≤ y-symmetricRivalPosition d := by linarith
    have hur : y-symmetricRivalPosition d ≤ (1-d)/2 := by
      unfold symmetricRivalPosition
      linarith
    have hw := crossingNoContractStrictlyWorse r t c d
      (y-symmetricRivalPosition d) hr ht hrt hc hd
      (by linarith : d ≤ 1) hu hur hFOC hcost
    unfold locationPayoff
    rw [if_neg (not_le.mpr hgreater)]
    exact le_of_lt hw

end RescueHotellingNoContractGlobal
#print axioms RescueHotellingNoContractGlobal.noContractGlobalBestResponse
