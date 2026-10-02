PYTHON ?= python

.PHONY: verify symbolic normalization policy global numerical portability benchmarks test objects marginal-exhibits ere-format title-page-format v4-freeze paper exposition formal-certificates formal-verify ere-source-package ere-title-page ere-review-package review-package-verify ere-submission-bundle clean

verify: symbolic normalization policy global numerical portability benchmarks test marginal-exhibits ere-format title-page-format exposition v4-freeze ere-submission-bundle

symbolic:
	$(PYTHON) scripts/verify_symbolic.py

normalization:
	$(PYTHON) scripts/verify_normalization.py

policy:
	$(PYTHON) scripts/verify_policy_certificate.py

global:
	$(PYTHON) scripts/verify_global_certificate.py

numerical:
	$(PYTHON) scripts/verify_numerical.py

portability:
	$(PYTHON) scripts/verify_portability_v24.py

benchmarks:
	$(PYTHON) scripts/verify_benchmarks.py

test:
	$(PYTHON) -m pytest -q

objects:
	$(PYTHON) scripts/generate_objects.py

marginal-exhibits: objects
	$(PYTHON) scripts/verify_marginal_exhibits.py

ere-format:
	$(PYTHON) scripts/verify_ere_submission.py

title-page-format:
	$(PYTHON) scripts/verify_ere_title_page.py

v4-freeze:
	$(PYTHON) scripts/verify_v4_freeze.py

paper: objects
	cd paper && pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex >/dev/null

exposition: paper
	$(PYTHON) scripts/verify_exposition_v25.py

formal-certificates:
	$(PYTHON) scripts/generate_lean_certificates.py

formal-verify: formal-certificates
	cd formal && lake exe cache get
	cd formal && lake build PCPPR.Primitives PCPPR.ProductMarket PCPPR.Availability PCPPR.Backup PCPPR.Location PCPPR.Welfare PCPPR.MarginalDecomposition PCPPR.Bernstein PCPPR.CanonicalWitness PCPPR.GeneratedCertificates PCPPR.GlobalPlanner PCPPR.GlobalLocalGovernment PCPPR.TheoremCore
	cd formal && lake env lean Main.lean > FORMAL_AXIOM_REPORT.txt

ere-source-package: objects
	$(PYTHON) scripts/build_verify_ere_source_package.py

ere-title-page:
	cd submission && pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error ERE_title_page.tex >/dev/null

ere-review-package: objects benchmarks formal-certificates
	$(PYTHON) scripts/build_ere_review_package.py

review-package-verify: ere-review-package
	$(PYTHON) scripts/verify_clean_review_package.py

ere-submission-bundle: paper ere-source-package ere-title-page review-package-verify
	$(PYTHON) scripts/build_ere_submission_bundle.py

# Historical Stage scripts are retained for provenance and are not current gates.

clean:
	rm -f paper/*.aux paper/*.bbl paper/*.blg paper/*.log paper/*.out paper/*.pdf paper/*.toc
	rm -f submission/*.aux submission/*.log submission/*.out submission/*.pdf
	rm -rf dist
