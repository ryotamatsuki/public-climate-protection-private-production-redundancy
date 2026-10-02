from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "submission" / "ERE_STAGE15_V3_SCIENTIFIC_OBJECT.lock"
FREEZE = ROOT / "docs" / "THEORY_FREEZE.md"
REPORT = ROOT / "STAGE_15_V3_REPORT.md"


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
        raise AssertionError("v3 scientific-object lock missing")
    if not REPORT.exists():
        raise AssertionError("v3 Stage-15 report missing")

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
                f"v3 frozen object changed at {path}: expected {lock[key]}, got {actual}"
            )

    blob_paths = {
        "theory_freeze_blob": "docs/THEORY_FREEZE.md",
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
                f"v3 frozen blob changed at {path}: expected {lock[key]}, got {actual}"
            )

    freeze = FREEZE.read_text(encoding="utf-8")
    if "PCPPR-THEORY-FREEZE-2026-10-02-v3" not in freeze:
        raise AssertionError("v3 freeze ID missing from THEORY_FREEZE.md")

    report = REPORT.read_text(encoding="utf-8")
    if "REPOSITORY-LAYER V3 RE-FREEZE: PASS" not in report:
        raise AssertionError("v3 repository-layer PASS record missing")
    if "LIVE SUBMISSION AUTHORIZATION: HOLD" not in report:
        raise AssertionError("live-portal HOLD record missing")

    print("PCPPR v3 scientific-object freeze gate PASS")
    print("freeze=PCPPR-THEORY-FREEZE-2026-10-02-v3")
    print("live submission authorization remains HOLD pending portal preflight")


if __name__ == "__main__":
    main()
