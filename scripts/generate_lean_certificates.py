#!/usr/bin/env python3
"""Generate exact rational data for the Lean certificate checker.

Source model/certificate implementation:
  scripts/verify_global_certificate.py
Canonical manuscript/model SHA:
  77f0c0705e3759b4997b3b17355f0063c02673e1

The generator does NOT emit a Boolean PASS as a theorem.  It emits every exact
rational Bernstein coefficient used by the selected proof-critical sign checks.
Lean then checks the sign of each coefficient independently.
"""
from __future__ import annotations

import hashlib
import importlib.util
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

# Planner partial derivatives on the complete policy square.
px_n, px_d = bernstein(mod.dWdx, mod.FULL)
py_n, py_d = bernstein(mod.dWdy, mod.FULL)

# Local-government own-policy second derivative on full own-policy interval
# times the complete rational isolating interval for the rival root.
lg_n, lg_d = bernstein(mod.ddGdxx, mod.LOCAL)

# Root-bracketing data for the diagonal local-government FOC.  The exact
# manuscript interval is checked to contain the source certificate's isolated root.
L = mod.Q(1649737, 71666359)
U = mod.Q(380091, 16511564)
assert L < mod.lo < mod.hi < U or (L <= mod.lo and mod.hi <= U)

# Exact signs of the diagonal FOC numerator at the stated endpoints.
# Fnum is a SymPy polynomial over QQ; convert endpoint values back to the same
# rational domain used by the exact certificate.
def eval_poly_q(poly, x):
    import sympy as sp
    xs = sp.Rational(int(x.numerator), int(x.denominator))
    val = poly.eval(xs)
    return mod.Q(int(val.p), int(val.q))

fL = eval_poly_q(mod.Fnum, L)
fU = eval_poly_q(mod.Fnum, U)
assert fL != 0 and fU != 0 and (fL > 0) != (fU > 0)

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
parts.append("end PCPPR.GeneratedCertificates\n")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("".join(parts), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
print(f"source sha256: {source_sha256}")
