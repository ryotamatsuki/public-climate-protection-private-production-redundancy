from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "paper" / "sections"
AUX = ROOT / "paper" / "main.aux"

MAIN_TEXT = [
    "01_introduction.tex",
    "02_model.tex",
    "03_equilibrium.tex",
    "04_main_results.tex",
    "05_welfare.tex",
    "06_benchmarks.tex",
    "07_institutional.tex",
    "08_literature.tex",
    "09_discussion.tex",
    "10_conclusion.tex",
]

LABEL_ORDER = [
    "sec:introduction",
    "sec:model",
    "sec:equilibrium",
    "sec:main",
    "sec:welfare",
    "sec:benchmarks",
    "sec:institutions",
    "sec:literature",
    "sec:discussion",
    "sec:conclusion",
    "app:verification",
]

def load_main_text() -> str:
    return "\n".join((SECTIONS / f).read_text(encoding="utf-8") for f in MAIN_TEXT)

def section_counts() -> dict[str, dict[str, int]]:
    out = {}
    for name in MAIN_TEXT:
        text = (SECTIONS / name).read_text(encoding="utf-8")
        out[name] = {
            "chars": len(text),
            "figures": len(re.findall(r"\\begin\{figure\}", text)),
            "tables": len(re.findall(r"\\begin\{table\}", text)),
            "equations": len(re.findall(r"\\begin\{equation\}", text)),
            "subsections": len(re.findall(r"\\subsection", text)),
        }
    return out

def page_map() -> dict[str, int]:
    if not AUX.exists():
        raise AssertionError("paper/main.aux missing; run paper build before exposition audit")
    aux = AUX.read_text(encoding="utf-8", errors="ignore")
    labels = {}
    for label in LABEL_ORDER:
        m = re.search(
            rf"\\newlabel\{{{re.escape(label)}\}}\{{\{{[^}}]*\}}\{{([^}}]+)\}}",
            aux,
        )
        if not m:
            raise AssertionError(f"missing page label in aux: {label}")
        labels[label] = int(m.group(1))
    return labels

def main() -> None:
    manuscript = load_main_text()

    forbidden = [
        "For journal positioning",
        "Japanese policy documents provide direct examples",
        "-\\frac{26550065039062500}{13482801445834729}",
    ]
    for token in forbidden:
        if token in manuscript:
            raise AssertionError(f"v2.5 exposition regression found: {token}")

    counts = section_counts()
    total_figures = sum(v["figures"] for v in counts.values())
    total_tables = sum(v["tables"] for v in counts.values())
    if total_figures > 5 or total_tables > 5:
        raise AssertionError(
            f"unexpected main-text exhibit expansion: figures={total_figures}, tables={total_tables}"
        )

    pages = page_map()
    ordered_pages = [pages[x] for x in LABEL_ORDER]
    if ordered_pages != sorted(ordered_pages):
        raise AssertionError(f"section page order is nonmonotone: {pages}")

    intro_span = pages["sec:model"] - pages["sec:introduction"]
    if intro_span > 5:
        raise AssertionError(
            f"Introduction exceeds v2.5 soft heuristic without documented exception: {intro_span} pages"
        )

    print("v2.5 exposition audit PASS")
    print("section pages:", pages)
    print("main-text exhibits:", {"figures": total_figures, "tables": total_tables})
    print("section counts:", counts)

if __name__ == "__main__":
    main()
