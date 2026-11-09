"""Regression checks for the submission-only ERE document transformation."""
from pathlib import Path

import pytest

from scripts.build_ere_editorial_resubmission import (
    AI_HEADING, APPENDIX_INPUT, DATA_HEADING, IDENTIFIERS, transform,
)

ROOT = Path(__file__).resolve().parents[1]


def test_editorial_split_retains_science_and_ai_disclosure():
    original = (ROOT / "paper/main.tex").read_text(encoding="utf-8")
    blinded, supplementary = transform(original)
    assert DATA_HEADING in original and DATA_HEADING not in blinded
    assert AI_HEADING in blinded
    assert APPENDIX_INPUT in supplementary and APPENDIX_INPUT not in blinded
    assert r"\externaldocument{ERE_supplementary_appendix}" in blinded
    assert r"\externaldocument{ERE_blinded_manuscript}" in supplementary
    assert r"\input{../references/references.tex}" in blinded
    for section in ("01_introduction", "02_model", "03_equilibrium",
                    "04_main_results", "05_welfare", "06_benchmarks",
                    "07_institutional", "08_literature", "09_discussion",
                    "10_conclusion"):
        assert r"\input{sections/" + section + "}" in blinded
    for value in IDENTIFIERS:
        assert value.lower() not in (blinded + supplementary).lower()
    assert (ROOT / "paper/main.tex").read_text(encoding="utf-8") == original


def test_unexpected_editorial_format_fails_closed():
    original = (ROOT / "paper/main.tex").read_text(encoding="utf-8")
    with pytest.raises(ValueError, match="required marker"):
        transform(original.replace(DATA_HEADING, ""))
    with pytest.raises(ValueError, match="required marker"):
        transform(original.replace(APPENDIX_INPUT, ""))


def test_appendix_source_is_preserved():
    _, supplementary = transform((ROOT / "paper/main.tex").read_text())
    appendix = (ROOT / "paper/sections/A_proofs_verification.tex").read_text()
    assert r"\label{app:verification}" in appendix
    assert r"\label{app:formal-scope}" in appendix
    assert supplementary.count(r"\input{sections/A_proofs_verification}") == 1
