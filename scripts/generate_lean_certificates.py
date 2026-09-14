#!/usr/bin/env python3
"""Generate exact certificate data for the Lean checker.

Source model/certificate implementation:
  scripts/verify_global_certificate.py
Canonical manuscript/model SHA:
  77f0c0705e3759b4997b3b17355f0063c02673e1

Large bivariate Bernstein payloads are encoded by signed numerators and
positive denominators. Lean checks those integer signs exactly, avoiding
expensive normalization of very large Rational literals.

For the diagonal local-government FOC (T12), the generator emits the exact
isolating interval, endpoint values, the Bernstein coefficients of the FOC on
the normalized interval, and the Bernstein coefficients of its formal
derivative.  The source-to-certificate conversion is category C (generated
exact certificate); Lean checks the endpoint and coefficient signs and the
generic Bernstein/root implications.  We intentionally do not ask the Lean
kernel to re-expand a degree-19 polynomial with huge rationals into two bases,
which is computationally disproportionate and was causing CI to stall.
"""
from __future__ import annotations

import hashlib
import importlib.util
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scripts" / "verify_global_certificate.py"
OUT = ROOT / "formal" / "PCPPR" / "GeneratedCertificates.lean"
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


def emit_int_list(name: str, xs) -> str:
    body = ",\n    ".join(f"({int(x)} : ℤ)" for x in xs)
    return f"def {name} : List ℤ := [\n    {body}\n  ]\n"


def emit_nat_list(name: str, xs) -> str:
    body = ",\n    ".join(str(int(x)) for x in xs)
    return f"def {name} : List ℕ := [\n    {body}\n  ]\n"


def emit_rational_sign_payload(name: str, xs) -> str:
    """Emit an exact, Lean-cheap sign certificate for rational coefficients."""
    sign = strict_sign(xs)
    nums, dens = zip(*(rat_parts(q) for q in xs))
    out = [emit_int_list(name + "Numerators", nums), emit_nat_list(name + "Denominators", dens)]
    if sign > 0:
        prop = f"∀ z ∈ {name}Numerators, 0 < z"
    else:
        prop = f"∀ z ∈ {name}Numerators, z < 0"
    out.append(f"theorem {name}_numerator_strict_sign : {prop} := by\n  native_decide\n")
    out.append(
        f"theorem {name}_denominators_positive : "
        f"∀ d ∈ {name}Denominators, 0 < d := by\n  native_decide\n"
    )
    return "".join(out)


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


def emit_fin_vector(name: str, xs) -> str:
    body = ",\n    ".join(lean_rat(x) for x in xs)
    return f"def {name} : Fin {len(xs)} → ℚ := ![\n    {body}\n  ]\n"


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

# Exact canonical FOC on normalized coordinate t in [0,1].
# The derivative coefficients are for P'(L+(U-L)t); multiplication by the
# positive affine scale (U-L) is unnecessary for a sign certificate.
foc_beta = normalized_bernstein_coeffs(mod.Fnum, L, U)
foc_deriv_beta = normalized_bernstein_coeffs(mod.Fnum.diff(), L, U)
assert len(foc_beta) == mod.Fnum.degree() + 1
assert len(foc_deriv_beta) == mod.Fnum.degree()
assert strict_sign(foc_deriv_beta) < 0
assert foc_beta[0] == fL
assert foc_beta[-1] == fU

source_sha256 = hashlib.sha256(SOURCE.read_bytes()).hexdigest()

parts = [
    "import Mathlib\n\n",
    "namespace PCPPR.GeneratedCertificates\n\n",
    f'def canonicalManuscriptSHA : String := "{CANONICAL_SHA}"\n',
    f'def generatorSourceSHA256 : String := "{source_sha256}"\n\n',
]

for name, vals in [
    ("plannerXNumeratorCoeffs", px_n),
    ("plannerXDenominatorCoeffs", px_d),
    ("plannerYNumeratorCoeffs", py_n),
    ("plannerYDenominatorCoeffs", py_d),
    ("localSecondNumeratorCoeffs", lg_n),
    ("localSecondDenominatorCoeffs", lg_d),
]:
    parts.append(emit_rational_sign_payload(name, vals))
    parts.append("\n")

parts += [
    f"def alphaL : ℚ := {lean_rat(L)}\n",
    f"def alphaU : ℚ := {lean_rat(U)}\n",
    f"def diagonalFOCNumeratorAtL : ℚ := {lean_rat(fL)}\n",
    f"def diagonalFOCNumeratorAtU : ℚ := {lean_rat(fU)}\n\n",
    "theorem alpha_interval_order : 0 < alphaL ∧ alphaL < alphaU := by\n  native_decide\n\n",
    "theorem diagonal_FOC_endpoint_sign_change :\n"
    "    0 < diagonalFOCNumeratorAtL ∧ diagonalFOCNumeratorAtU < 0 := by\n"
    "  native_decide\n\n",
]

parts.append(emit_fin_vector("diagonalFOCBernsteinCoeffs", foc_beta))
parts.append("\n")
parts.append(emit_fin_vector("diagonalFOCDerivativeBernsteinCoeffs", foc_deriv_beta))
parts.append(
    "theorem diagonalFOCDerivativeBernsteinCoeffs_negative : "
    "∀ i, diagonalFOCDerivativeBernsteinCoeffs i < 0 := by\n  native_decide\n\n"
)
parts.append(
    "theorem diagonalFOCBernstein_endpoint_coeff_signs :\n"
    "    0 < diagonalFOCBernsteinCoeffs 0 ∧\n"
    "      diagonalFOCBernsteinCoeffs (Fin.last 19) < 0 := by\n"
    "  native_decide\n\n"
)
parts.append("end PCPPR.GeneratedCertificates\n")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("".join(parts), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
print(f"source sha256: {source_sha256}")
print(f"diagonal FOC degree: {mod.Fnum.degree()}")
print(f"diagonal derivative Bernstein degree: {len(foc_deriv_beta) - 1}")
