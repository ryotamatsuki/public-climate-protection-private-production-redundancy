import Mathlib
import RescueHotellingCore
import RescueHotellingDelivery

/-!
Typed stage histories and complete contingent strategy spaces for the
paper's game. This defines the extensive form *syntax*, including
price choices after all contracts and locations. It does NOT yet
construct the stochastic extensive-form payoff or prove SPNE.
-/
noncomputable section
namespace RescueHotellingHistories
open RescueHotelling RescueHotellingDelivery

inductive Firm | A | B deriving DecidableEq
inductive Choice | buyA | buyB | outside deriving DecidableEq

structure Primitives where
  q : ℝ
  t : ℝ
  c : ℝ
  v : ℝ
  Lambda : ℝ
  k : ℝ
  F : ℝ

def Primitives.Admissible (P : Primitives) : Prop :=
  0 < P.q ∧ P.q < 1 ∧ 0 < P.t ∧ 0 < P.c ∧
    0 < P.Lambda ∧ 0 ≤ P.k ∧ P.k < P.Lambda ∧
    0 < P.F ∧ 3*P.t < P.v

structure Locations where
  yA : ℝ
  yB : ℝ
  hA0 : 0 ≤ yA
  hA1 : yA ≤ 1
  hB0 : 0 ≤ yB
  hB1 : yB ≤ 1

def Locations.distance (loc : Locations) : ℝ :=
  |loc.yA - loc.yB|

def Locations.midpoint (loc : Locations) : ℝ :=
  (loc.yA + loc.yB)/2

structure Prices where
  pA : ℝ
  pB : ℝ
  hA : 0 ≤ pA
  hB : 0 ≤ pB

structure OfferHistory where
  location : Locations
  proposer : Firm
  transferToResponder : ℝ
  accepted : Bool

structure PriceHistory where
  offer : OfferHistory
  prices : Prices

structure OrderHistory where
  priceHistory : PriceHistory
  consumerOrders : ℝ → Choice

structure TerminalHistory where
  orderHistory : OrderHistory
  physicalOutcome : Outcome

def deliveredValue (P : Primitives) (x y p : ℝ) : ℝ :=
  P.v - p - P.t*(x-y)^2

def deliveryFactor (P : Primitives) (o : OfferHistory) : ℝ :=
  if o.accepted then
    survival P.q + rescue P.q o.location.distance
  else
    survival P.q

def expectedOrderUtilityA (P : Primitives)
    (H : PriceHistory) (x : ℝ) : ℝ :=
  deliveryFactor P H.offer *
    deliveredValue P x H.offer.location.yA H.prices.pA

def expectedOrderUtilityB (P : Primitives)
    (H : PriceHistory) (x : ℝ) : ℝ :=
  deliveryFactor P H.offer *
    deliveredValue P x H.offer.location.yB H.prices.pB

def IsOptimalConsumerChoice (P : Primitives)
    (H : PriceHistory) (x : ℝ) : Choice → Prop
  | .outside =>
      expectedOrderUtilityA P H x ≤ 0 ∧
      expectedOrderUtilityB P H x ≤ 0
  | .buyA =>
      0 ≤ expectedOrderUtilityA P H x ∧
      expectedOrderUtilityB P H x ≤ expectedOrderUtilityA P H x
  | .buyB =>
      0 ≤ expectedOrderUtilityB P H x ∧
      expectedOrderUtilityA P H x ≤ expectedOrderUtilityB P H x

def IsConsumerOrderEquilibrium (P : Primitives)
    (H : OrderHistory) : Prop :=
  ∀ x : ℝ, 0 ≤ x → x ≤ 1 →
    IsOptimalConsumerChoice P H.priceHistory x (H.consumerOrders x)

structure PureStrategyProfile where
  locationA : {y : ℝ // 0 ≤ y ∧ y ≤ 1}
  locationB : {y : ℝ // 0 ≤ y ∧ y ≤ 1}
  offerA : Locations → ℝ
  offerB : Locations → ℝ
  acceptsA : Locations → Firm → ℝ → Bool
  acceptsB : Locations → Firm → ℝ → Bool
  priceA : OfferHistory → {p : ℝ // 0 ≤ p}
  priceB : OfferHistory → {p : ℝ // 0 ≤ p}
  consumerOrder : PriceHistory → ℝ → Choice

theorem distance_nonnegative (loc : Locations) :
    0 ≤ loc.distance := by
  unfold Locations.distance
  exact abs_nonneg _

theorem distance_le_one (loc : Locations) :
    loc.distance ≤ 1 := by
  have hL : -1 ≤ loc.yA - loc.yB := by
    have := loc.hA0
    have := loc.hB1
    linarith
  have hU : loc.yA-loc.yB ≤ 1 := by
    have := loc.hA1
    have := loc.hB0
    linarith
  unfold Locations.distance
  exact abs_le.mpr ⟨hL,hU⟩

theorem common_delivery_probability_is_positive
    (P : Primitives) (o : OfferHistory)
    (hq : 0 < P.q) (hqlt : P.q < 1) :
    0 < deliveryFactor P o := by
  by_cases hA : o.accepted
  · simp only [deliveryFactor, hA, if_pos]
    have hr : 0 < survival P.q := by
      unfold survival
      linarith
    have hAq : 0 ≤ intensity P.q := by
      unfold intensity
      positivity
    have hd0 : 0 ≤ o.location.distance := distance_nonnegative _
    have hd1 : o.location.distance ≤ 1 := distance_le_one _
    have he : 0 ≤ rescue P.q o.location.distance := by
      unfold rescue
      have h1 : 0 ≤ 1-o.location.distance := by linarith
      positivity
    linarith
  · simp only [deliveryFactor, if_neg hA]
    unfold survival
    linarith

end RescueHotellingHistories

#print axioms RescueHotellingHistories.distance_le_one
#print axioms RescueHotellingHistories.common_delivery_probability_is_positive
