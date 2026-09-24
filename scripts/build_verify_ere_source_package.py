from __future__ import annotations

import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
OUT = DIST / "ERE_anonymous_manuscript_source.zip"

REQUIRED = [
    ROOT / "paper" / "main.tex",
    *sorted((ROOT / "paper" / "sections").glob("*.tex")),
    ROOT / "references" / "references.tex",
    *sorted((ROOT / "references").glob("*.bib")),
    ROOT / "tables" / "channel_decomposition.tex",
    ROOT / "figures" / "policy_regime.pdf",
    ROOT / "figures" / "policy_regime.eps",
]

FORBIDDEN = (
    "Ryota Matsuki",
    "ryota.matsuki",
    "orcid.org/0009-0005-2329-531X",
    "github.com/ryotamatsuki",
)

TEXT_SUFFIXES = {".tex", ".bib", ".txt", ".md"}

def check_anonymity(path: Path) -> None:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return
    text = path.read_text(encoding="utf-8", errors="ignore")
    for token in FORBIDDEN:
        if token.lower() in text.lower():
            raise RuntimeError(f"identifying token {token!r} found in {path.relative_to(ROOT)}")

def archive_name(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()

def main() -> None:
    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.exists()]
    if missing:
        raise RuntimeError(f"source package missing required files: {missing}")

    for p in REQUIRED:
        check_anonymity(p)

    DIST.mkdir(exist_ok=True)
    if OUT.exists():
        OUT.unlink()

    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in REQUIRED:
            zf.write(p, archive_name(p))

    with tempfile.TemporaryDirectory(prefix="ere-source-") as td:
        work = Path(td)
        with zipfile.ZipFile(OUT) as zf:
            zf.extractall(work)
        cmd = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"]
        for _ in range(3):
            subprocess.run(cmd, cwd=work / "paper", check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        pdf = work / "paper" / "main.pdf"
        if not pdf.exists() or pdf.stat().st_size == 0:
            raise RuntimeError("clean extracted source archive did not produce paper/main.pdf")

    with zipfile.ZipFile(OUT) as zf:
        names = set(zf.namelist())
        for required in ("paper/main.tex", "references/references.tex", "tables/channel_decomposition.tex",
                         "figures/policy_regime.pdf", "figures/policy_regime.eps"):
            if required not in names:
                raise RuntimeError(f"source archive missing {required}")

    print(f"ERE anonymous manuscript source package PASS: {OUT.relative_to(ROOT)}")
    print(f"source files: {len(REQUIRED)}; clean extracted LaTeX build: PASS")

if __name__ == "__main__":
    main()
