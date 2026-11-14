# Lean proof reproduction (audit branch)
Date 2026-11-14. Manuscript files remain untouched.

Source branch: `hotelling-full-formal-verification-2026-11-14`
Baseline: `rescue-hotelling-model-audit-2026-11-14`, commit `8a3c6a0aeb11888e17abcc549119e2a929438f1f`.

Manuscript source ZIP SHA256:
`ba125cf13a35217432577e95b04f7a77e6f1eadba5862f3ae8d1a884a95ae457`.
Published PDF SHA256:
`e356a07675daca6cdfd3f305ae77cd0f012ec8065167e6433a19af13c8e5b2d6`.

```bash
git clone https://github.com/ryotamatsuki/public-climate-protection-private-production-redundancy.git
cd public-climate-protection-private-production-redundancy
git checkout hotelling-full-formal-verification-2026-11-14
cd formal
cat lean-toolchain
lake exe cache get
lake env lean -o RescueHotellingCore.olean RescueHotellingCore.lean
lake env lean -o RescueHotellingModelCheck.olean RescueHotellingModelCheck.lean
# Check the exact ordering in .github/workflows/rescue-hotelling-model-audit.yml
```

The CI workflow installs the pinned toolchain, obtains the mathlib cache, compiles the original 9 modules and new modules, rejects `sorry`, `admit`, and project `axiom` declarations, and scans kernel output for `sorryAx`. Source-level checks are necessary but not sufficient to rule out all semantic mismatches.

Inspect each `#print axioms` output. Lean's standard logical axioms (`propext`, `Classical.choice`, `Quot.sound`) are permitted; new arbitrary axioms are not.

For all numerical certificates, verify the interval partition and exact outward rational comparisons rather than trusting figure samples or floating-point logs.

This repository audit is not declared FULL FORMAL VERIFICATION until all entries in `FORMAL_PROOF_OBLIGATIONS.md` and `UNRESOLVED_PROOF_OBLIGATIONS.md` are closed.
