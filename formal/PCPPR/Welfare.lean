import PCPPR.Availability
import PCPPR.ProductMarket

namespace PCPPR.Welfare

open PCPPR.Availability

/-- Product-market surplus obtained by enumerating the four availability states,
net of real backup-readiness costs. -/
def surplusByStates
    (TD TM s1 s2 J k r1 r2 : ℝ) : ℝ :=
  p11 s1 s2 J r1 r2 * TD +
    (p10 s1 s2 J r1 r2 + p01 s1 s2 J r1 r2) * TM -
    k * (r1^2 + r2^2) / 2

/-- Closed-form surplus in paper equation (19). -/
def surplusClosed
    (TD TM s1 s2 J k r1 r2 : ℝ) : ℝ :=
  TD + (TM - TD) * (m s1 r1 + m s2 r2) +
    (TD - 2 * TM) * z J r1 r2 -
    k * (r1^2 + r2^2) / 2

/-- T7: welfare accounting is derived from final-state enumeration. -/
theorem surplus_state_eq_closed
    (TD TM s1 s2 J k r1 r2 : ℝ) :
    surplusByStates TD TM s1 s2 J k r1 r2 =
      surplusClosed TD TM s1 s2 J k r1 r2 := by
  unfold surplusByStates surplusClosed
  unfold p11 p10 p01 m z
  ring

end PCPPR.Welfare
