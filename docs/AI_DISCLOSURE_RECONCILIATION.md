# AI Disclosure Reconciliation

Updated: 2026-09-25
Target: Environmental and Resource Economics / Springer Nature

Official policy checked:
- https://link.springer.com/journal/10640/submission-guidelines
- https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation
- https://www.springernature.com/gp/policies/editorial-policies/using-ai-in-research

## Material use -> disclosure mapping

| Material use | Actor/evidence | Required disclosure implication | Final manuscript treatment | Status |
|---|---|---|---|---|
| research assistance / mechanism stress-testing | AI | research-method AI use should be transparent | named in AI Assistance Disclosure | PASS |
| adversarial mathematical review | AI | do not call external human or author verification | named as adversarial mathematical review; no human-verification claim | PASS |
| coding / numerical verification support | AI + COMPUTATION | distinguish assistance from deterministic evidence | AI support disclosed; exact/numerical tests described separately | PASS |
| Lean formalization support | AI + FORMAL | formal proof scope must not be inflated | AI support disclosed; Lean described as kernel-checked encoded statements only | PASS |
| literature / claim stress-testing | AI + source checks | references/claims remain source-verifiable | disclosed; bibliography remains source-based | PASS |
| manuscript organization / language editing | AI | manuscript-preparation use should be transparent when substantive | disclosed | PASS |
| figure generation | deterministic matplotlib code, not opaque generative image creation | reproducible code/source required; AI-image rules not invoked | figure regenerated from verified model outputs; no generative image | PASS |

## Final disclosure wording

The anonymous manuscript states:

> OpenAI generative-AI tools were used during manuscript development for research assistance, literature and claim stress-testing, adversarial mathematical review, coding and formalization support, manuscript organization, and language editing. AI outputs were not treated as independent scholarly evidence. Mathematical claims are supported, as applicable, by explicit derivations, deterministic exact and numerical regression tests, and Lean kernel-checked formal statements; those checks certify only their encoded or tested scopes and do not substitute for author judgment. The author remains accountable for the research decisions, interpretations, and final submitted content. No AI system is listed as an author.

## Placement

ERE's current instructions say LLM use should be documented in the Methods section, or a suitable alternative part when no Methods section exists. This is a theory paper without a conventional Methods section; the dedicated AI Assistance Disclosure in the manuscript is the selected suitable alternative.

## Human-accountability boundary

The disclosure does not claim that all substantive claims were independently verified by the author. Personal author approval of the final frozen package is reserved for Stage 15.
