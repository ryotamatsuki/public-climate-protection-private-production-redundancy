#!/usr/bin/env python3
"""Generate exact rational data for the Lean certificate checker.

Source model/certificate implementation:
  scripts/verify_global_certificate.py
Canonical manuscript/model SHA:
  77f0c0705e3759b4997b3b17355f0063c02673e1

The generator does NOT emit a Boolean PASS as a theorem. It emits exact
rational coefficient payloads and, for the diagonal local-government FOC, the
polynomial itself plus an exact Bernstein representation of its normalized
formal derivative. Lean rechecks all signs and polynomial identities.
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
    return int(q.numerator), int(q.denominator)


def lean_rat(q) -> str:
    n, d = rat_parts(q)
    if d == 1:
        return f"({n} : ℚ)"
    return f"(({n} : ℚ) / {d})"


def sympy_q(q):
    """Convert a SymPy QQ element/Rational to the certificate field element."""
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


def emit_list(name: str, xs) -> str:
    body = ",\n    ".join(lean_rat(x) for x in xs)
    return f"def {name} : List ℚ := [\n    {body}\n  ]\n"


def emit_sign_theorem(name: str, sign: int) -> str:
    if sign > 0:
        prop = f"∀ q ∈ {name}, 0 < q"
    else:
        prop = f"∀ q ∈ {name}, q < 0"
    return f"theorem {name}_strict_sign : {prop} := by\n  native_decide\n"


def poly_coeffs_ascending(poly):
    return [sympy_q(poly.nth(i)) for i in range(poly.degree() + 1)]


def emit_polynomial_q(name: str, coeffs) -> str:
    terms = []
    for i, q in enumerate(coeffs):
        if q == 0:
            continue
        terms.append(f"Polynomial.C {lean_rat(q)} * Polynomial.X ^ {i}")
    expr = " +\n    ".join(terms) if terms else "0"
    return f"def {name} : Polynomial ℚ :=\n    {expr}\n"


def normalized_bernstein_coeffs(poly, lo, hi):
    """Bernstein coefficients of poly(lo+(hi-lo)t) on t in [0,1]."""
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


def emit_bernstein_polynomial_q(name: str, degree: int, coeffs) -> str:
    terms = [
        f"Polynomial.C {lean_rat(q)} * bernsteinPolynomial ℚ {degree} {i}"
        for i, q in enumerate(coeffs)
    ]
    return f"def {name} : Polynomial ℚ :=\n    " + " +\n    ".join(terms) + "\n"


# Planner partial derivatives on the complete policy square.
px_n, px_d = bernstein(mod.dWdx, mod.FULL)
py_n, py_d = bernstein(mod.dWdy, mod.FULL)

# Local-government own-policy second derivative on full own-policy interval
# times the complete rational isolating interval for the rival root.
lg_n, lg_d = bernstein(mod.ddGdxx, mod.LOCAL)

# Root-bracketing data for the diagonal local-government FOC. The exact
# manuscript interval is checked to contain the source certificate's isolated root.
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
assert fL != 0 and fU != 0 and (fL > 0) != (fU > 0)

# T12 monotonicity payload: exact polynomial and exact Bernstein coefficients
# of P'(L + (U-L)t).  This does not trust SymPy's final root count inside Lean.
foc_coeffs = poly_coeffs_ascending(mod.Fnum)
foc_deriv_beta = normalized_bernstein_coeffs(mod.Fnum.diff(), L, U)
assert strict_sign(foc_deriv_beta) < 0
foc_deriv_degree = len(foc_deriv_beta) - 1

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
    parts.append(emit_list(name, vals))
    parts.append(emit_sign_theorem(name, strict_sign(vals)))
    parts.append("\n")

parts += [
    f"def alphaL : ℚ := {lean_rat(L)}\n",
    f"def alphaU : ℚ := {lean_rat(U)}\n",
    f"def diagonalFOCNumeratorAtL : ℚ := {lean_rat(fL)}\n",
    f"def diagonalFOCNumeratorAtU : ℚ := {lean_rat(fU)}\n\n",
    "theorem alpha_interval_order : 0 < alphaL ∧ alphaL < alphaU := by\n  native_decide\n\n",
]

if fL > 0:
    root_prop = "0 < diagonalFOCNumeratorAtL ∧ diagonalFOCNumeratorAtU < 0"
else:
    root_prop = "diagonalFOCNumeratorAtL < 0 ∧ 0 < diagonalFOCNumeratorAtU"
parts.append(f"theorem diagonal_FOC_endpoint_sign_change : {root_prop} := by\n  native_decide\n\n")

parts.append(emit_polynomial_q("diagonalFOCPolynomialQ", foc_coeffs))
parts.append("\n")
parts.append(emit_fin_vector("diagonalFOCDerivativeBernsteinCoeffs", foc_deriv_beta))
parts.append(
    "theorem diagonalFOCDerivativeBernsteinCoeffs_negative : "
    "∀ i, diagonalFOCDerivativeBernsteinCoeffs i < 0 := by\n  native_decide\n\n"
)
parts.append(emit_bernstein_polynomial_q(
    "diagonalFOCDerivativeBernsteinPolynomialQ", foc_deriv_degree, foc_deriv_beta
))
parts.append("\n")
parts.append(
    "def diagonalFOCAffineQ : Polynomial ℚ :=\n"
    "  Polynomial.C alphaL + Polynomial.C (alphaU - alphaL) * Polynomial.X\n\n"
)
parts.append(
    "theorem diagonal_FOC_derivative_bernstein_identity :\n"
    "    diagonalFOCPolynomialQ.derivative.comp diagonalFOCAffineQ =\n"
    "      diagonalFOCDerivativeBernsteinPolynomialQ := by\n"
    "  native_decide\n\n"
)
parts.append(
    "theorem diagonal_FOC_polynomial_endpoint_sign_change :\n"
    "    0 < diagonalFOCPolynomialQ.eval alphaL ∧\n"
    "      diagonalFOCPolynomialQ.eval alphaU < 0 := by\n"
    "  native_decide\n\n"
)
parts.append("end PCPPR.GeneratedCertificates\n")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("".join(parts), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
print(f"source sha256: {source_sha256}")
print(f"diagonal FOC degree: {len(foc_coeffs) - 1}")
print(f"normalized derivative Bernstein degree: {foc_deriv_degree}")
