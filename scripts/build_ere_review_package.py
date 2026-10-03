from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
OUT = DIST / "ERE_anonymous_replication.zip"
EXCLUDED_FILES = {
    "scripts/build_ere_review_package.py",
    "scripts/build_verify_ere_source_package.py",
    "scripts/build_ere_submission_bundle.py",
    "scripts/verify_stage15_presubmission.py",
    "scripts/verify_stage13_integration.py",
    "scripts/verify_stage14_submission_qa.py",
    "scripts/verify_ere_title_page.py",
    "scripts/verify_clean_review_package.py",
    # Repository-only freeze governance; the anonymous commands need no Git.
    "scripts/verify_v3_freeze.py",
    "scripts/verify_v4_freeze.py",
    "scripts/verify_final_audit_freeze.py",
    # This editorial packager regression imports the excluded identity scanner.
    "tests/test_archive_selection.py",
    "tests/test_freeze_governance.py",
}

EXACT_FILES = {
    "requirements.txt",
    "docs/certificate_normalization.json",
    "docs/certificate_polynomials.json",
    "docs/v2_4_portability_results.json",
    "formal/lakefile.lean",
    "formal/lake-manifest.json",
    "formal/lean-toolchain",
    "formal/README.md",
    "formal/GENERATED_CERTIFICATE_ARCHIVE.json",
    "docs/mechanism_benchmark.json",
    "docs/independent_exact_audit_2026-10-03.json",
    "docs/independent_numerical_audit_2026-10-03.json",
}

PATTERNS = (
    "paper/*.tex",
    "paper/sections/*.tex",
    "references/*.tex",
    "references/*.bib",
    "scripts/*.py",
    "tests/*.py",
    "figures/*",
    "tables/*",
    "formal/*.lean",
    "formal/PCPPR/*.lean",
)

FORBIDDEN_TEXT = (
    "ryotamatsuki",
    "Ryota Matsuki",
    "github.com/ryotamatsuki",
    "users.noreply.github.com",
    "THEORY-FREEZE",
    "STAGE_15",
)

TEXT_SUFFIXES = {".tex", ".py", ".md", ".txt", ".json", ".bib", ".csv", ".yml", ".yaml", ".lean"}


def selected_files() -> list[Path]:
    chosen: set[Path] = set()
    for rel in EXACT_FILES:
        p = ROOT / rel
        if p.exists():
            chosen.add(p)
    # Path globbing does not let '*' cross directory separators. In contrast,
    # fnmatch('formal/*.lean') would accidentally include .lake dependencies.
    for pattern in PATTERNS:
        for p in ROOT.glob(pattern):
            if p.is_file() and p.relative_to(ROOT).as_posix() not in EXCLUDED_FILES:
                chosen.add(p)
    return sorted(chosen)


def assert_anonymous(path: Path) -> None:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return
    for token in FORBIDDEN_TEXT:
        if token.lower() in text.lower():
            raise RuntimeError(f"identifying token {token!r} found in {path.relative_to(ROOT)}")


def main() -> None:
    for rel in ("formal/PCPPR/GeneratedCertificates.lean", "formal/GENERATED_CERTIFICATE_ARCHIVE.json"):
        if not (ROOT/rel).is_file():
            raise RuntimeError(f"review package requires generated certificates: {rel}; run make formal-certificates")
    DIST.mkdir(exist_ok=True)
    if OUT.exists():
        OUT.unlink()

    files = selected_files()
    if not files:
        raise RuntimeError("no files selected for ERE review package")

    replication_readme = ROOT / "submission" / "ERE_replication_README.md"
    review_makefile = ROOT / "submission" / "ERE_review_Makefile"
    assert_anonymous(replication_readme)
    assert_anonymous(review_makefile)

    for p in files:
        assert_anonymous(p)

    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        zf.write(replication_readme, "README.md")
        zf.write(review_makefile, "Makefile")
        for p in files:
            rel = p.relative_to(ROOT).as_posix()
            zf.write(p, rel)

    with zipfile.ZipFile(OUT) as zf:
        names = zf.namelist()
        forbidden_paths = [n for n in names if n.startswith(".git/") or n.startswith(".github/") or n.startswith("submission/")]
        if forbidden_paths:
            raise RuntimeError(f"forbidden paths in review package: {forbidden_paths}")
        if "README.md" not in names or "Makefile" not in names:
            raise RuntimeError("review package missing anonymized README or review Makefile")
        for rel in ("formal/PCPPR/GeneratedCertificates.lean", "formal/GENERATED_CERTIFICATE_ARCHIVE.json", "formal/README.md"):
            if rel not in names:
                raise RuntimeError(f"review package missing {rel}")

    print(f"ERE anonymous review package ready: {OUT.relative_to(ROOT)}")
    print(f"files: {len(files)} source items + anonymized README + review Makefile")


if __name__ == "__main__":
    main()
