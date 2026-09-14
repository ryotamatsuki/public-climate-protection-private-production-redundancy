from __future__ import annotations

import fnmatch
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
OUT = DIST / "ERE_anonymous_replication.zip"
PACKAGER = "scripts/build_ere_review_package.py"

EXACT_FILES = {
    "requirements.txt",
    "docs/certificate_normalization.json",
    "docs/certificate_polynomials.json",
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
)

FORBIDDEN_TEXT = (
    "ryotamatsuki",
    "Ryota Matsuki",
    "github.com/ryotamatsuki",
    "users.noreply.github.com",
)

TEXT_SUFFIXES = {".tex", ".py", ".md", ".txt", ".json", ".bib", ".csv", ".yml", ".yaml"}


def selected_files() -> list[Path]:
    chosen: set[Path] = set()
    for rel in EXACT_FILES:
        p = ROOT / rel
        if p.exists():
            chosen.add(p)
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel == PACKAGER:
            continue
        if any(fnmatch.fnmatch(rel, pattern) for pattern in PATTERNS):
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

    # Re-open the archive and verify that identifying or submission-only paths were not included.
    with zipfile.ZipFile(OUT) as zf:
        names = zf.namelist()
        forbidden_paths = [n for n in names if n.startswith(".git/") or n.startswith(".github/") or n.startswith("submission/")]
        if forbidden_paths:
            raise RuntimeError(f"forbidden paths in review package: {forbidden_paths}")
        if "README.md" not in names or "Makefile" not in names:
            raise RuntimeError("review package missing anonymized README or review Makefile")

    print(f"ERE anonymous review package ready: {OUT.relative_to(ROOT)}")
    print(f"files: {len(files)} source items + anonymized README + review Makefile")


if __name__ == "__main__":
    main()
