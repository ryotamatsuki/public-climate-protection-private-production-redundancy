#!/usr/bin/env python3
"""Generate exact certificate data for the Lean checker.

Source model/certificate implementation:
  scripts/verify_global_certificate.py
Canonical manuscript/model SHA:
  77f0c0705e3759b4997b3b17355f0063c02673e1

The large bivariate Bernstein certificates used for T11 and T13 are category-C
objects. They are preserved exactly in a deterministic JSON archive as signed
numerator/positive-denominator pairs, together with their strict-sign result.
They are deliberately not elaborated as thousands of Lean constants because
the canonical semantic bridge treats these large source-to-certificate
expansions as category C rather than category A.

For the diagonal local-government FOC (T12), the generator emits the exact
isolating interval, exact endpoint values, and all 52 Bernstein coefficients
of the degree-51 normalized formal derivative. Those proof-critical
coefficients remain in Lean. Each negative rational is encoded exactly as
`-(m+1)/(d+1)` with `m,d : Nat`; this makes strict negativity structural rather
than asking `native_decide` to normalize 52 enormous rational literals. The
source-to-certificate conversion is category C; endpoint signs, exact
coefficient representation, derivative-coefficient signs, and the generic
Bernstein/root implications are checked in Lean. The kernel is not asked to
re-expand the degree-52 FOC into multiple polynomial bases.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scripts" / "verify_global_certificate.py"
OUT = ROOT / "formal" / "PCPPR" / "GeneratedCertificates.lean"
ARCHIVE = ROOT / "formal" / "GENERATED_CERTIFICATE_ARCHIVE.json"
CANONICAL_SHA = "77f0c0705e3759b4997b3b17355f0063c02673e1"

spec = importlib.util.spec_from_file_location("pcppr_global_certificate", SOURCE)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load exact certificate source")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def rat_parts(q):
    n, d = int(q.numerator), int(q.denominator)
    if d <= 0:
        raise RuntimeError("certificate rational denominator is not positive")
    return n, d


def lean_rat(q) -> str:
    n, d = rat_parts(q)
    if d == 1:
        return f"({n} : ℚ)"
    return f"(({n} : ℚ) / {d})"


def sympy_q(q):
    if hasattr(q, "p") and hasattr(q, "q"):
        return mod.Q(int(q.p), int(q.q))
    return mod.Q(int(q.numerator), int(q.denominator))


def bernstein(frac, rect):
    n = list(mod.bernstein_coeffs(frac.numer, *rect).values())
    d = list(mod.bernstein_coeffs(frac.denom, *rect).values())
    return n, d


def strict_sign(xs) -> int:
    if all(x > 0 for x in xs):
        return 1
    if all(x < 0 for x in xs):
        return -1
    raise RuntimeError("coefficient list has no uniform strict sign")


def normalized_bernstein_coeffs(poly, lo, hi):
    """Bernstein coefficients of poly(lo+(hi-lo)t), t in [0,1]."""
    import sympy as sp

    z = poly.gens[0]
    t = sp.symbols("_t")
    lo_s = sp.Rational(int(lo.numerator), int(lo.denominator))
    hi_s = sp.Rational(int(hi.numerator), int(hi.denominator))
    expr = sp.expand(poly.as_expr().subs(z, lo_s + (hi_s - lo_s) * t))
    p = sp.Poly(expr, t, domain=sp.QQ)
    n = p.degree()
    power = [sympy_q(p.nth(r)) for r in range(n + 1)]
    beta = []
    for i in range(n + 1):
        q = mod.Q(0)
        for r in range(i + 1):
            q += power[r] * mod.Q(comb(i, r), comb(n, r))
        beta.append(q)
    return beta


def emit_fin_nat_vector(name: str, xs) -> str:
    body = ",\n    ".join(str(int(x)) for x in xs)
    return f"def {name} : Fin {len(xs)} → ℕ := ![\n    {body}\n  ]\n"


def archive_payload(xs):
    sign = strict_sign(xs)
    return {
        "strict_sign": sign,
        "coefficients": [list(rat_parts(q)) for q in xs],
    }


# Planner partial derivatives on the complete policy square.
px_n, px_d = bernstein(mod.dWdx, mod.FULL)
py_n, py_d = bernstein(mod.dWdy, mod.FULL)

# Local-government own-policy second derivative on full own-policy interval
# times the exact rival-root isolating interval.
lg_n, lg_d = bernstein(mod.ddGdxx, mod.LOCAL)

# Exact root-bracketing data for the diagonal local-government FOC.
L = mod.Q(1649737, 71666359)
U = mod.Q(380091, 16511564)
assert L < mod.lo < mod.hi < U or (L <= mod.lo and mod.hi <= U)


def eval_poly_q(poly, x):
    import sympy as sp

    xs = sp.Rational(int(x.numerator), int(x.denominator))
    val = poly.eval(xs)
    return mod.Q(int(val.p), int(val.q))


fL = eval_poly_q(mod.Fnum, L)
fU = eval_poly_q(mod.Fnum, U)
assert fL > 0 and fU < 0

# Exact derivative sign certificate for P'(alpha) on alpha in [L,U].
# Under alpha=L+(U-L)t, all Bernstein coefficients are strictly negative.
foc_deriv_beta = normalized_bernstein_coeffs(mod.Fnum.diff(), L, U)
assert len(foc_deriv_beta) == mod.Fnum.degree()
assert strict_sign(foc_deriv_beta) < 0
foc_nums, foc_dens = zip(*(rat_parts(q) for q in foc_deriv_beta))
assert all(n < 0 for n in foc_nums)
assert all(d > 0 for d in foc_dens)
# Exact structural encoding: n/d = -(((-n)-1)+1) / ((d-1)+1).
foc_num_magnitude_pred = [(-n) - 1 for n in foc_nums]
foc_den_pred = [d - 1 for d in foc_dens]
assert all(m >= 0 for m in foc_num_magnitude_pred)
assert all(d >= 0 for d in foc_den_pred)

source_sha256 = hashlib.sha256(SOURCE.read_bytes()).hexdigest()

archive = {
    "canonical_manuscript_model_sha": CANONICAL_SHA,
    "generator_source_sha256": source_sha256,
    "planner_x_numerator_bernstein": archive_payload(px_n),
    "planner_x_denominator_bernstein": archive_payload(px_d),
    "planner_y_numerator_bernstein": archive_payload(py_n),
    "planner_y_denominator_bernstein": archive_payload(py_d),
    "local_second_numerator_bernstein": archive_payload(lg_n),
    "local_second_denominator_bernstein": archive_payload(lg_d),
    "diagonal_foc": {
        "degree": int(mod.Fnum.degree()),
        "alphaL": list(rat_parts(L)),
        "alphaU": list(rat_parts(U)),
        "value_at_alphaL": list(rat_parts(fL)),
        "value_at_alphaU": list(rat_parts(fU)),
        "derivative_bernstein_degree": len(foc_deriv_beta) - 1,
        "derivative_bernstein": [list(rat_parts(q)) for q in foc_deriv_beta],
        "derivative_strict_sign": strict_sign(foc_deriv_beta),
    },
}
archive_text = json.dumps(archive, indent=2, sort_keys=True) + "\n"
archive_sha256 = hashlib.sha256(archive_text.encode("utf-8")).hexdigest()

parts = [
    "import Mathlib\n\n",
    "namespace PCPPR.GeneratedCertificates\n\n",
    f'def canonicalManuscriptSHA : String := "{CANONICAL_SHA}"\n',
    f'def generatorSourceSHA256 : String := "{source_sha256}"\n',
    f'def generatedArchiveSHA256 : String := "{archive_sha256}"\n\n',
    f"def plannerXNumeratorCoeffCount : ℕ := {len(px_n)}\n",
    f"def plannerXDenominatorCoeffCount : ℕ := {len(px_d)}\n",
    f"def plannerYNumeratorCoeffCount : ℕ := {len(py_n)}\n",
    f"def plannerYDenominatorCoeffCount : ℕ := {len(py_d)}\n",
    f"def localSecondNumeratorCoeffCount : ℕ := {len(lg_n)}\n",
    f"def localSecondDenominatorCoeffCount : ℕ := {len(lg_d)}\n\n",
    f"def alphaL : ℚ := {lean_rat(L)}\n",
    f"def alphaU : ℚ := {lean_rat(U)}\n",
    f"def diagonalFOCNumeratorAtL : ℚ := {lean_rat(fL)}\n",
    f"def diagonalFOCNumeratorAtU : ℚ := {lean_rat(fU)}\n\n",
    "theorem alpha_interval_order : 0 < alphaL ∧ alphaL < alphaU := by\n  native_decide\n\n",
    "theorem diagonal_FOC_endpoint_sign_change :\n"
    "    0 < diagonalFOCNumeratorAtL ∧ diagonalFOCNumeratorAtU < 0 := by\n"
    "  native_decide\n\n",
]

parts.append(emit_fin_nat_vector(
    "diagonalFOCDerivativeBernsteinNumeratorMagnitudePred", foc_num_magnitude_pred))
parts.append(emit_fin_nat_vector(
    "diagonalFOCDerivativeBernsteinDenominatorPred", foc_den_pred))
parts.append(
    "\ndef diagonalFOCDerivativeBernsteinCoeffs : Fin 52 → ℚ := fun i =>\n"
    "  -(((diagonalFOCDerivativeBernsteinNumeratorMagnitudePred i + 1 : ℕ) : ℚ)) /\n"
    "    ((diagonalFOCDerivativeBernsteinDenominatorPred i + 1 : ℕ) : ℚ)\n\n"
)
parts.append(
    "theorem diagonalFOCDerivativeBernsteinCoeffs_negative :\n"
    "    ∀ i, diagonalFOCDerivativeBernsteinCoeffs i < 0 := by\n"
    "  intro i\n"
    "  have hn : (0 : ℚ) <\n"
    "      ((diagonalFOCDerivativeBernsteinNumeratorMagnitudePred i + 1 : ℕ) : ℚ) := by\n"
    "    positivity\n"
    "  have hd : (0 : ℚ) <\n"
    "      ((diagonalFOCDerivativeBernsteinDenominatorPred i + 1 : ℕ) : ℚ) := by\n"
    "    positivity\n"
    "  exact div_neg_of_neg_of_pos (neg_lt_zero.mpr hn) hd\n\n"
)
parts.append("end PCPPR.GeneratedCertificates\n")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("".join(parts), encoding="utf-8")
ARCHIVE.write_text(archive_text, encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
print(f"wrote {ARCHIVE.relative_to(ROOT)}")
print(f"source sha256: {source_sha256}")
print(f"archive sha256: {archive_sha256}")
print(f"diagonal FOC degree: {mod.Fnum.degree()}")
print(f"diagonal derivative Bernstein degree: {len(foc_deriv_beta) - 1}")
