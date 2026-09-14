PYTHON ?= python

.PHONY: verify symbolic normalization policy global numerical benchmarks test objects paper ere-review-package clean

verify: symbolic normalization policy global numerical benchmarks test objects paper ere-review-package

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

benchmarks:
	$(PYTHON) scripts/verify_benchmarks.py

test:
	$(PYTHON) -m pytest -q

objects:
	$(PYTHON) scripts/generate_objects.py

paper: objects
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null

ere-review-package: objects
	$(PYTHON) scripts/build_ere_review_package.py

clean:
	rm -f paper/*.aux paper/*.bbl paper/*.blg paper/*.log paper/*.out paper/*.pdf paper/*.toc
	rm -rf dist
