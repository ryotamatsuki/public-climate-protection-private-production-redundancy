PYTHON ?= python

.PHONY: verify symbolic normalization policy global numerical portability benchmarks test objects ere-format stage13-integration stage14-qa paper exposition ere-source-package ere-title-page ere-review-package clean

verify: symbolic normalization policy global numerical portability benchmarks test objects ere-format stage13-integration stage14-qa paper exposition ere-source-package ere-title-page ere-review-package

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

ere-format:
	$(PYTHON) scripts/verify_ere_submission.py

stage13-integration:
	$(PYTHON) scripts/verify_stage13_integration.py

stage14-qa:
	$(PYTHON) scripts/verify_stage14_submission_qa.py

paper: objects
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null

exposition: paper
	$(PYTHON) scripts/verify_exposition_v25.py

ere-source-package: objects
	$(PYTHON) scripts/build_verify_ere_source_package.py

ere-title-page:
	cd submission && pdflatex -interaction=nonstopmode -halt-on-error ERE_title_page.tex >/dev/null

ere-review-package: objects
	$(PYTHON) scripts/build_ere_review_package.py

clean:
	rm -f paper/*.aux paper/*.bbl paper/*.blg paper/*.log paper/*.out paper/*.pdf paper/*.toc
	rm -f submission/*.aux submission/*.log submission/*.out submission/*.pdf
	rm -rf dist
