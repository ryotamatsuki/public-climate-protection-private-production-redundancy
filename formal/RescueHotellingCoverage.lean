import Mathlib
import RescueHotellingExtendedGame

/-!
Candidate-equilibrium coverage of the outside option under v > 3t.
The economic result requires that consumers choose using expected
utility with the common positive delivery probability; the proof below
certifies the candidate ex-post delivered surplus is strictly positive.
-/
noncomputable section
namespace RescueHotellingCoverage
open RescueHotellingModelCheck RescueHotellingExtendedGame

theorem sq_distance_le_one (x y : ℝ)
    (hx0 : 0 ≤ x) (hx1 : x ≤ 1)
    (hy0 : 0 ≤ y) (hy1 : y ≤ 1) :
    (x-y)^2 ≤ 1 := by
  have hlo : 0 ≤ x-y+1 := by linarith
  have hhi : 0 ≤ 1-(x-y) := by linarith
  have hh := mul_nonneg hlo hhi
  nlinarith

theorem left_price_le_four_thirds_t (t d m : ℝ)
    (ht : 0 ≤ t) (hd0 : 0 ≤ d) (hd1 : d ≤ 1)
    (hm0 : 0 ≤ m) (hm1 : m ≤ 1) :
    priceLeft (t*d) m ≤ 4*t/3 := by
  have h0 : 0 ≤ 1+m := by linarith
  have hD : d*(1+m) ≤ (1+m) :=
    (mul_le_mul_of_nonneg_right hd1 h0).trans (by ring)
  have hM : d*(1+m) ≤ 2 := by linarith
  have hT := mul_le_mul_of_nonneg_left hM ht
  unfold priceLeft
  nlinarith

theorem right_price_le_four_thirds_t (t d m : ℝ)
    (ht : 0 ≤ t) (hd0 : 0 ≤ d) (hd1 : d ≤ 1)
    (hm0 : 0 ≤ m) (hm1 : m ≤ 1) :
    priceRight (t*d) m ≤ 4*t/3 := by
  have h0 : 0 ≤ 2-m := by linarith
  have hD : d*(2-m) ≤ (2-m) :=
    (mul_le_mul_of_nonneg_right hd1 h0).trans (by ring)
  have hM : d*(2-m) ≤ 2 := by linarith
  have hT := mul_le_mul_of_nonneg_left hM ht
  unfold priceRight
  nlinarith

theorem delivered_surplus_positive (v t p x y : ℝ)
    (ht : 0 < t) (hv : 3*t < v)
    (hp : p ≤ 4*t/3)
    (hx0 : 0 ≤ x) (hx1 : x ≤ 1)
    (hy0 : 0 ≤ y) (hy1 : y ≤ 1) :
    0 < v-p-t*(x-y)^2 := by
  have hDist := sq_distance_le_one x y hx0 hx1 hy0 hy1
  have hT := mul_le_mul_of_nonneg_left hDist (le_of_lt ht)
  linarith

theorem candidate_prices_cover_all_consumers (v t d m x yL yR : ℝ)
    (ht : 0 < t) (hv : 3*t < v)
    (hd0 : 0 ≤ d) (hd1 : d ≤ 1)
    (hm0 : 0 ≤ m) (hm1 : m ≤ 1)
    (hx0 : 0 ≤ x) (hx1 : x ≤ 1)
    (hyL0 : 0 ≤ yL) (hyL1 : yL ≤ 1)
    (hyR0 : 0 ≤ yR) (hyR1 : yR ≤ 1) :
    0 < v-priceLeft (t*d) m-t*(x-yL)^2 ∧
    0 < v-priceRight (t*d) m-t*(x-yR)^2 := by
  constructor
  · exact delivered_surplus_positive v t (priceLeft (t*d) m) x yL ht hv
      (left_price_le_four_thirds_t t d m (le_of_lt ht) hd0 hd1 hm0 hm1)
      hx0 hx1 hyL0 hyL1
  · exact delivered_surplus_positive v t (priceRight (t*d) m) x yR ht hv
      (right_price_le_four_thirds_t t d m (le_of_lt ht) hd0 hd1 hm0 hm1)
      hx0 hx1 hyR0 hyR1

end RescueHotellingCoverage
#print axioms RescueHotellingCoverage.candidate_prices_cover_all_consumers
