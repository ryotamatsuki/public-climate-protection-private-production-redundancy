from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "submission" / "ERE_STAGE15_V4_SCIENTIFIC_OBJECT.lock"
FREEZE = ROOT / "docs" / "THEORY_FREEZE.md"
REPORT = ROOT / "STAGE_15_V4_REPORT.md"


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, text=True, capture_output=True
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
    if not LOCK.exists():
        raise AssertionError("v4 scientific-object lock missing")
    if not REPORT.exists():
        raise AssertionError("v4 Stage-15 report missing")

    lock = parse_lock()

    tree_paths = {
        "paper_tree": "paper",
        "formal_tree": "formal",
        "references_tree": "references",
        "tables_tree": "tables",
        "tests_tree": "tests",
        "scripts_tree": "scripts",
    }
    for key, path in tree_paths.items():
        actual = git("rev-parse", f"HEAD:{path}")
        if actual != lock[key]:
            raise AssertionError(
                f"v4 frozen object changed at {path}: expected {lock[key]}, got {actual}"
            )

    blob_paths = {
        "theory_freeze_blob": "docs/THEORY_FREEZE.md",
        "stage6_recert_blob": "docs/STAGE_6_RECERTIFICATION_2026-10-03.md",
        "stage75_recert_blob": "docs/STAGE_7_5A_RECERTIFICATION_2026-10-03.md",
        "formal_addendum_blob": "docs/FORMAL_VERIFICATION_GATE_ADDENDUM_2026-10-03.md",
        "independent_scientific_confirmation_blob": "docs/INDEPENDENT_SCIENTIFIC_CONFIRMATION_2026-10-03.md",
        "author_confirmation_blob": "docs/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md",
        "ai_provenance_blob": "docs/AI_PROVENANCE_LOG.md",
        "mechanism_benchmark_blob": "docs/mechanism_benchmark.json",
        "portability_results_blob": "docs/v2_4_portability_results.json",
        "audit_repairs_blob": "docs/INDEPENDENT_AUDIT_REPAIRS_2026-10-02.md",
        "requirements_blob": "requirements.txt",
        "makefile_blob": "Makefile",
        "workflow_blob": ".github/workflows/verify.yml",
    }
    for key, path in blob_paths.items():
        actual = git("rev-parse", f"HEAD:{path}")
        if actual != lock[key]:
            raise AssertionError(
                f"v4 frozen blob changed at {path}: expected {lock[key]}, got {actual}"
            )

    freeze = FREEZE.read_text(encoding="utf-8")
    if "PCPPR-THEORY-FREEZE-2026-10-03-v4" not in freeze:
        raise AssertionError("v4 freeze ID missing from THEORY_FREEZE.md")

    author = (ROOT / "docs" / "AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md").read_text(
        encoding="utf-8"
    )
    if "PERSONALLY RECONFIRMED BY AUTHOR — 2026-10-03" not in author:
        raise AssertionError("v4 author scientific reconfirmation missing")

    report = REPORT.read_text(encoding="utf-8")
    if "REPOSITORY-LAYER V4 RE-FREEZE: PASS" not in report:
        raise AssertionError("v4 repository-layer PASS record missing")
    if "LIVE SUBMISSION AUTHORIZATION: HOLD" not in report:
        raise AssertionError("live-portal HOLD record missing")

    print("PCPPR v4 scientific-object freeze gate PASS")
    print("freeze=PCPPR-THEORY-FREEZE-2026-10-03-v4")
    print("Stage 6 / Stage 7.5A / author scientific confirmation locked")
    print("live submission authorization remains HOLD pending portal preflight")


if __name__ == "__main__":
    main()
