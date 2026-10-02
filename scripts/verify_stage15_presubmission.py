from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "submission" / "ERE_STAGE15_SCIENTIFIC_OBJECT.lock"
REPORT = ROOT / "STAGE_15_REPORT.md"
LEDGER = ROOT / "docs" / "STAGE_14_LIVE_REQUIREMENTS_LEDGER_ERE_2026-10-02.md"
CHECKLIST = ROOT / "submission" / "ERE_submission_checklist.md"
MANIFEST = ROOT / "submission" / "ERE_STAGE15_UPLOAD_MANIFEST.md"


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()


def parse_lock() -> dict[str, str]:
    out: dict[str, str] = {}
    for raw in LOCK.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        key, value = line.split("=", 1)
        out[key] = value
    return out


def main() -> None:
    required = [LOCK, REPORT, LEDGER, CHECKLIST, MANIFEST]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
    if missing:
        raise AssertionError(f"Stage-15 control files missing: {missing}")

    lock = parse_lock()
    tree_paths = {
        "paper_tree": "paper",
        "formal_tree": "formal",
        "references_tree": "references",
        "tables_tree": "tables",
        "tests_tree": "tests",
    }
    for key, path in tree_paths.items():
        actual = git("rev-parse", f"HEAD:{path}")
        expected = lock[key]
        if actual != expected:
            raise AssertionError(
                f"scientific object changed at {path}: expected {expected}, got {actual}"
            )

    theory_blob = git("hash-object", "docs/THEORY_FREEZE.md")
    if theory_blob != lock["theory_freeze_blob"]:
        raise AssertionError(
            "docs/THEORY_FREEZE.md changed after the Stage-15 scientific-object lock"
        )

    report = REPORT.read_text(encoding="utf-8")
    if "REPOSITORY-LAYER PRE-SUBMISSION FREEZE: PASS" not in report:
        raise AssertionError("Stage-15 repository-layer PASS record missing")
    if "FULL STAGE 15 / LIVE SUBMISSION AUTHORIZATION: HOLD" not in report:
        raise AssertionError("Stage-15 fail-closed portal HOLD record missing")

    ledger = LEDGER.read_text(encoding="utf-8")
    if "Site under development. Do not use for live manuscript submission." not in ledger:
        raise AssertionError("current ERE portal-availability blocker not recorded")
    if ledger.count("UNVERIFIED — PORTAL ONLY") < 5:
        raise AssertionError("portal-only requirements must remain explicitly unresolved")

    checklist = CHECKLIST.read_text(encoding="utf-8")
    for item in (
        "- [ ] Exact final package approval — after live portal review PDF inspection.",
        "- [ ] Article type confirmed in the live portal.",
        "- [ ] File designations confirmed in the live portal.",
        "- [ ] Portal-specific AI/declaration questions captured and reconciled.",
        "- [ ] Portal warnings resolved.",
        "- [ ] Generated review PDF inspected for anonymity, order, equations, figures, references, and declarations.",
    ):
        if item not in checklist:
            raise AssertionError(f"fail-closed checklist item missing: {item}")

    manifest = MANIFEST.read_text(encoding="utf-8")
    for token in (
        "paper/main.pdf",
        "submission/ERE_title_page.pdf",
        "dist/ERE_anonymous_manuscript_source.zip",
        "dist/ERE_anonymous_replication.zip",
        "dist/ERE_submission_ready_bundle.zip",
    ):
        if token not in manifest:
            raise AssertionError(f"upload manifest missing {token}")

    print("Stage-15 pre-submission freeze gate PASS")
    print(f"scientific object base: {lock['base_commit']}")
    print("full Stage 15 remains HOLD on authenticated live-portal checks")


if __name__ == "__main__":
    main()
