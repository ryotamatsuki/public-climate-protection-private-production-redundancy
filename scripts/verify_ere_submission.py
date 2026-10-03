from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "paper" / "main.tex"
INTRO = ROOT / "paper" / "sections" / "01_introduction.tex"
LIT = ROOT / "paper" / "sections" / "08_literature.tex"
REFS = ROOT / "references" / "references.tex"

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

    manuscript = "\n".join([main_tex, *(p.read_text(encoding="utf-8") for p in (ROOT/"paper/sections").glob("*.tex"))])
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

    if "MartinHerranEtAl2026" not in intro or "MartinHerranEtAl2026" not in lit:
        raise AssertionError("closest ERE industrial-allocation paper must be positioned in introduction and literature review")
    if "MartinHerranEtAl2026" not in refs:
        raise AssertionError("Martin-Herran et al. reference missing")
    if "GrossmanHelpmanLhuillier2023" not in intro or "GrossmanHelpmanLhuillier2023" not in lit:
        raise AssertionError("closest backup-diversification theory must be discussed")
    if "GrossmanHelpmanLhuillier2023" not in refs:
        raise AssertionError("Grossman et al. reference missing")

    doi_entries = [line for line in refs.splitlines() if "doi:" in line.lower()]
    if doi_entries:
        raise AssertionError("DOIs should be rendered as full https://doi.org/ links for ERE")

    # Journal-specific instructions take precedence over generic artwork text.
    legends = ROOT / 'paper' / 'figure_legends.tex'
    if not legends.is_file() or main_tex.index('references/references.tex') > main_tex.index('input{figure_legends}'):
        raise AssertionError('ERE figure legends must follow the references')
    if '\\textbf{Fig.' not in legends.read_text() or '\\caption{' in (ROOT/'paper/sections/04_main_results.tex').read_text():
        raise AssertionError('Figure 1 needs one complete legend after references')
    for key in ('CapponiDuStiglitz2024','CastroVincenziEtAl2024','ZhaoYangZhang2026'):
        if key in refs:
            raise AssertionError('Unpublished works belong in the text, not the ERE reference list')
    cited=set()
    for group in re.findall(r'\\cite\w*(?:\[[^]]*\])?\{([^}]+)\}',manuscript):
        cited.update(s.strip() for s in group.split(','))
    listed=set(re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}',refs))
    if cited!=listed:
        raise AssertionError(f'Citation/list mismatch: uncited={listed-cited}, missing={cited-listed}')

    print(f"ERE submission checks PASS: abstract={len(words)} words; keywords={len(keywords)}")

if __name__ == "__main__":
    main()
