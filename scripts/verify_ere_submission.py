from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "paper" / "main.tex"
INTRO = ROOT / "paper" / "sections" / "01_introduction.tex"
LIT = ROOT / "paper" / "sections" / "08_literature.tex"
REFS = ROOT / "references" / "references.tex"
TITLE_PAGE = ROOT / "submission" / "ERE_title_page.tex"


def strip_tex_commands(text: str) -> str:
    text = re.sub(r"%.*", " ", text)
    text = re.sub(r"\\[a-zA-Z*]+(?:\[[^\]]*\])?", " ", text)
    text = text.replace("{", " ").replace("}", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def main() -> None:
    main_tex = MAIN.read_text(encoding="utf-8")
    intro = INTRO.read_text(encoding="utf-8")
    lit = LIT.read_text(encoding="utf-8")
    refs = REFS.read_text(encoding="utf-8")
    title_page = TITLE_PAGE.read_text(encoding="utf-8")

    abstract_match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", main_tex, flags=re.S)
    if not abstract_match:
        raise AssertionError("abstract not found")
    abstract_plain = strip_tex_commands(abstract_match.group(1))
    words = re.findall(r"\b[\w’'-]+\b", abstract_plain, flags=re.UNICODE)
    if not 150 <= len(words) <= 250:
        raise AssertionError(f"ERE abstract word count out of range: {len(words)}")

    kw_match = re.search(r"\\textbf\{Keywords:\}\s*(.*?)\\\\", main_tex, flags=re.S)
    if not kw_match:
        raise AssertionError("keywords line not found")
    keywords = [x.strip() for x in kw_match.group(1).split(";") if x.strip()]
    if not 4 <= len(keywords) <= 6:
        raise AssertionError(f"ERE keyword count out of range: {len(keywords)}")

    if "\\author{}" not in main_tex:
        raise AssertionError("anonymous manuscript must retain an empty author field")

    manuscript = "\n".join([main_tex, intro, lit])
    for token in ("github.com/", "orcid.org/", "mailto:"):
        if token.lower() in manuscript.lower():
            raise AssertionError(f"potential identifying link found in anonymous manuscript: {token}")

    if "Data and Code Availability" not in main_tex:
        raise AssertionError("anonymous data/code availability statement missing")
    if "AI Assistance Disclosure" not in main_tex:
        raise AssertionError("ERE AI-assistance disclosure missing")
    if "do not substitute for author judgment" not in main_tex:
        raise AssertionError("AI disclosure must preserve the human-accountability boundary")
    if "independently checked against" in main_tex:
        raise AssertionError("stale AI-verification boilerplate found")
    if "implemented and verified the computer-assisted analysis" in title_page:
        raise AssertionError("title-page contribution statement conflates author and tool verification")
    if "those tools are not authors" not in title_page:
        raise AssertionError("title-page contribution statement missing tool/authorship boundary")

    if "MartinHerranEtAl2026" not in intro or "MartinHerranEtAl2026" not in lit:
        raise AssertionError("closest ERE industrial-allocation paper must be positioned in introduction and literature review")

    if "MartinHerranEtAl2026" not in refs:
        raise AssertionError("Martin-Herran et al. reference missing")

    doi_entries = [line for line in refs.splitlines() if "doi:" in line.lower()]
    if doi_entries:
        raise AssertionError("DOIs should be rendered as full https://doi.org/ links for ERE")

    print(f"ERE submission checks PASS: abstract={len(words)} words; keywords={len(keywords)}")


if __name__ == "__main__":
    main()
