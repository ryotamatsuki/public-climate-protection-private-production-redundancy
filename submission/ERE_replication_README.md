# Anonymized replication package

This archive accompanies a theoretical manuscript submitted for double-blind review.

It contains the code and exact algebraic certificates needed to reproduce the paper's symbolic identities, policy-root isolation, whole-domain sign certificates, numerical stress tests, benchmark checks, regression tests, generated exposition objects, and manuscript build.

## Environment

Recommended environment:

- Python 3.13 or later
- SymPy 1.14.0
- NumPy 2.3.5
- SciPy 1.17.0
- pytest
- a standard LaTeX distribution with the packages used by the manuscript

## Reproduction

From the root of the anonymized archive, run:

```bash
make verify
```

The command executes the symbolic checks, primitive-to-certificate normalization identities, exact policy and whole-domain certificates, numerical stress tests, the pre-specified v2.4 portability diagnostics, nested-benchmark checks, regression tests, deterministic object generation, the exposition/page-arrival audit, and the LaTeX build.

## Formal verification

The archive also contains the pinned Lean 4/mathlib proof-critical formalization. After installing the toolchain declared in `formal/lean-toolchain`, run:

```bash
make formal-verify
```

A successful Lean build certifies only the encoded statements under their encoded assumptions; it does not by itself certify economic interpretation, novelty, or unformalized model scope.

## Interpretation of computer-assisted proofs

The code is not used as a substitute for the mathematical argument in the manuscript. The appendix states the lemmas, domains, denominator-sign conditions, Bernstein sign principle, and logical implications required for the main theorem. The scripts provide independently inspectable exact certificates for those stated mathematical claims.

## Double-blind note

This reviewer-facing archive intentionally omits author names, affiliations, e-mail addresses, Git metadata, public repository URLs, and other identifying information. A permanent public repository and archival citation will be supplied in the final accepted version.
