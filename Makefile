PYTHON ?= python

.PHONY: verify symbolic policy numerical benchmarks test objects paper clean

verify: symbolic policy numerical benchmarks test objects paper

symbolic:
	$(PYTHON) scripts/verify_symbolic.py

policy:
	$(PYTHON) scripts/verify_policy_certificate.py

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

clean:
	rm -f paper/*.aux paper/*.bbl paper/*.blg paper/*.log paper/*.out paper/*.pdf paper/*.toc
