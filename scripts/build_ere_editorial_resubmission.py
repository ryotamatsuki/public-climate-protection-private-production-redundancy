"""Build the ERE editorial-resubmission documents from the frozen manuscript.

This produces a reviewer-blinded manuscript, a separate supplementary appendix,
the existing editorial title page, and a reproducible anonymous LaTeX source ZIP.
The canonical paper/main.tex and appendix source are not modified.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
OUT = ROOT / "dist" / "ERE_editorial_resubmission"
DATA_HEADING = "\\section*{Data and Code Availability}\n"
AI_HEADING = "\\section*{AI Assistance Disclosure}\n"
APPENDIX_INPUT = "\\appendix\n\\input{sections/A_proofs_verification}\n"
FORMAL_SCOPE_REFERENCE = "Appendix~\\ref{app:formal-scope} states the scope."
# Keep reviewer-bundled code itself anonymous, including its scanner literals.
IDENTIFIERS = ("Ryota" + " Matsuki", "ryota" + "." + "matsuki",
               "github.com/" + "ryota" + "matsuki",
               "orcid.org/" + "0009-0005-2329-531X")


def transform(original: str) -> tuple[str, str]:
    """Derive new LaTeX entrypoints without modifying any scientific section."""
    for marker in (DATA_HEADING, AI_HEADING, APPENDIX_INPUT,
                   FORMAL_SCOPE_REFERENCE, "\\begin{document}", "\\end{document}"):
        if original.count(marker) != 1:
            raise ValueError(f"Source changed or ambiguous; required marker count != 1: {marker!r}")
    start = original.index(DATA_HEADING)
    end = original.index(AI_HEADING)
    if end <= start:
        raise ValueError("Unexpected source ordering for availability/AI disclosures")
    blinded = original[:start] + original[end:]
    blinded = blinded.replace(APPENDIX_INPUT, "", 1)
    blinded = blinded.replace(
        FORMAL_SCOPE_REFERENCE,
        "Supplementary Appendix~\\ref{app:formal-scope} states the scope.", 1,
    )
    blinded = blinded.replace(
        "\\begin{document}",
        "\\usepackage{xr}\n\\externaldocument{ERE_supplementary_appendix}\n\n\\begin{document}", 1,
    )
    preamble = original.split("\\begin{document}", 1)[0]
    supplementary = (
        preamble
        + "\\usepackage{xr}\n\\externaldocument{ERE_blinded_manuscript}\n"
        + "\\begin{document}\n"
        + "\\begin{center}\n"
        + "{\\Large\\bfseries Supplementary Appendix}\\\\[6pt]\n"
        + "{\\normalsize Public Climate Protection and Private Production Redundancy:}\n"
        + "\\\\[3pt]\n"
        + "{\\normalsize Local Resilience Competition, Plant Location, and Disaster-State Market Power}\n"
        + "\\end{center}\n\\vspace{1em}\n"
        + APPENDIX_INPUT
        + "\\end{document}\n"
    )
    assert "\\input{sections/A_proofs_verification}" not in blinded
    assert DATA_HEADING not in blinded and AI_HEADING in blinded
    assert "\\input{sections/A_proofs_verification}" in supplementary
    for content in (blinded, supplementary):
        for forbidden in IDENTIFIERS:
            if forbidden.lower() in content.lower():
                raise ValueError("Identifying material found in anonymous LaTeX")
    return blinded, supplementary


def run_latex(work: Path, tex: str) -> None:
    cmd = ["pdflatex", "-no-shell-escape", "-interaction=nonstopmode",
           "-halt-on-error", tex]
    cp = subprocess.run(cmd, cwd=work, text=True, stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    if cp.returncode:
        raise RuntimeError(f"pdflatex failed for {tex}:\n{cp.stdout[-5500:]}")


def compile_pair(work: Path) -> None:
    # Bidirectional external references: both aux files must first exist.
    sequence = ("ERE_blinded_manuscript.tex", "ERE_supplementary_appendix.tex") * 3
    for tex in sequence:
        run_latex(work, tex)
    for name in ("ERE_blinded_manuscript", "ERE_supplementary_appendix"):
        pdf = work / (name + ".pdf")
        if not pdf.is_file() or pdf.stat().st_size < 1000:
            raise RuntimeError(f"Missing/invalid PDF: {pdf}")
        log = (work / (name + ".log")).read_text(errors="replace")
        if ("There were undefined references" in log or
                re.search(r"LaTeX Warning: Reference .+ undefined", log)):
            raise RuntimeError(f"Undefined cross references in {name}")


def source_files(work: Path) -> list[tuple[Path, str]]:
    files = [(work / f"{name}.tex", f"paper/{name}.tex")
             for name in ("ERE_blinded_manuscript", "ERE_supplementary_appendix")]
    for rel in ("paper/figure_legends.tex", "references/references.tex",
                "references/references.bib", "tables/channel_decomposition.tex"):
        files.append((ROOT / rel, rel))
    for path in sorted((PAPER / "sections").glob("*.tex")):
        files.append((path, path.relative_to(ROOT).as_posix()))
    for path in sorted((ROOT / "figures").glob("*")):
        if path.is_file() and path.suffix.lower() in (".pdf", ".eps"):
            files.append((path, path.relative_to(ROOT).as_posix()))
    return files


def assert_pdf_blinded(path: Path) -> None:
    program = shutil.which("pdftotext")
    if not program:
        raise RuntimeError("pdftotext is required for release anonymity QA")
    result = subprocess.run([program, str(path), "-"], check=True,
                            capture_output=True, text=True).stdout
    for word in (*IDENTIFIERS, "Data and Code Availability"):
        if word.lower() in result.lower():
            raise RuntimeError(f"Blind PDF contains forbidden text: {word}")
    if path.name == "ERE_blinded_manuscript.pdf" and "AI Assistance Disclosure" not in result:
        raise RuntimeError("AI assistance disclosure disappeared from reviewer manuscript")


def main() -> None:
    original = (PAPER / "main.tex").read_text(encoding="utf-8")
    blinded, appendix = transform(original)
    title_page = ROOT / "submission" / "ERE_title_page.pdf"
    if not title_page.is_file():
        raise RuntimeError("Build editorial title page first: make ere-title-page")
    if not (ROOT / "figures" / "policy_regime.pdf").is_file():
        raise RuntimeError("Build manuscript figures first: make objects")

    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="ere-editorial-resubmission-") as td:
        base = Path(td)
        work = base / "paper"
        work.mkdir()
        for name, target in (
            ("sections", PAPER / "sections"),
            ("figure_legends.tex", PAPER / "figure_legends.tex"),
        ):
            (work / name).symlink_to(target)
        for name in ("figures", "references", "tables"):
            (base / name).symlink_to(ROOT / name)
        (work / "ERE_blinded_manuscript.tex").write_text(blinded, encoding="utf-8")
        (work / "ERE_supplementary_appendix.tex").write_text(appendix, encoding="utf-8")

        compile_pair(work)
        for name in ("ERE_blinded_manuscript", "ERE_supplementary_appendix"):
            dest = OUT / f"{name}.pdf"
            shutil.copy2(work / f"{name}.pdf", dest)
            assert_pdf_blinded(dest)
        shutil.copy2(title_page, OUT / "ERE_title_page.pdf")

        source_zip = OUT / "ERE_anonymous_editable_source.zip"
        files = source_files(work)
        if not any(a == "figures/policy_regime.pdf" for _, a in files):
            raise RuntimeError("Generated chart not found in anonymous source package")
        with zipfile.ZipFile(source_zip, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for src, name in files:
                if src.suffix.lower() in (".tex", ".bib"):
                    content = src.read_text(encoding="utf-8")
                    for forbidden in IDENTIFIERS:
                        if forbidden.lower() in content.lower():
                            raise RuntimeError(f"Identifying text found in {name}")
                z.write(src, name)
        # Demonstrate the ZIP can compile without the original main.tex.
        with tempfile.TemporaryDirectory(prefix="ere-editorial-clean-") as check_dir:
            with zipfile.ZipFile(source_zip) as z:
                z.extractall(check_dir)
            compile_pair(Path(check_dir) / "paper")

    instructions = (
        "ERE-D-26-02567 | ERE editorial technical-check resubmission\n\n"
        "1. Upload ERE_blinded_manuscript.pdf as the anonymized manuscript.\n"
        "2. Upload ERE_supplementary_appendix.pdf under Supplementary File.\n"
        "3. Retain ERE_title_page.pdf as a separate, editorial-only title page.\n"
        "4. ERE_anonymous_editable_source.zip is an optional editable source;\n"
        "   do not mistakenly replace the supplementary appendix PDF with it.\n"
        "5. Keep the existing anonymous replication archive separate if required.\n"
        "6. Check that Editorial Manager metadata and title-page author name match:\n"
        "   Ryota" + " Matsuki. The editor has NOT clarified the alleged mismatch.\n"
        "7. Build the portal PDF, inspect it, then explicitly approve/submit.\n"
        "8. This folder is not evidence of successful portal resubmission.\n\n"
        "Change classification: editorial format only; original main.tex, section\n"
        "sources, proofs, certificates, scientific freeze, and identity-only title\n"
        "page are not modified by this script.\n"
    )
    (OUT / "UPLOAD_INSTRUCTIONS.txt").write_text(instructions, encoding="utf-8")
    files = sorted(x for x in OUT.iterdir() if x.is_file()
                   and x.name != "COMPONENT_SHA256.json")
    manifest = {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in files}
    (OUT / "COMPONENT_SHA256.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("ERE editorial resubmission PASS: two clean-compiling, cross-referenced PDFs,")
    print("editorial title page, anonymous editable-source ZIP and SHA-256 manifest.")
    for f in sorted(OUT.iterdir()):
        if f.is_file():
            print(f"{f.name} ({f.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
