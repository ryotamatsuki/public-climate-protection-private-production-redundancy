from __future__ import annotations

import subprocess
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
OUT = DIST / "ERE_submission_ready_bundle.zip"

FILES = {
    ROOT / "paper" / "main.pdf": "01_anonymous_manuscript/ERE_anonymous_manuscript.pdf",
    ROOT / "submission" / "ERE_title_page.pdf": "02_title_page/ERE_title_page.pdf",
    ROOT / "dist" / "ERE_anonymous_manuscript_source.zip": "03_editable_source/ERE_anonymous_manuscript_source.zip",
    ROOT / "dist" / "ERE_anonymous_replication.zip": "04_replication/ERE_anonymous_replication.zip",
    ROOT / "figures" / "policy_regime.eps": "05_artwork/policy_regime.eps",
    ROOT / "submission" / "ERE_cover_letter.md": "06_cover_letter/ERE_cover_letter.md",
    ROOT / "submission" / "ERE_submission_checklist.md": "07_controls/ERE_submission_checklist.md",
    ROOT / "submission" / "ERE_CURRENT_UPLOAD_MANIFEST.md": "07_controls/ERE_CURRENT_UPLOAD_MANIFEST.md",
    ROOT / "docs" / "INDEPENDENT_AUDIT_REPAIRS_2026-10-02.md": "07_controls/INDEPENDENT_AUDIT_REPAIRS_2026-10-02.md",
    ROOT / "docs" / "STAGE_14_LIVE_REQUIREMENTS_LEDGER_ERE_2026-10-02.md": "07_controls/STAGE_14_LIVE_REQUIREMENTS_LEDGER_ERE_2026-10-02.md",
    ROOT / "STAGE_15_REPORT.md": "08_historical_controls/STAGE_15_REPORT.md",
    ROOT / "submission" / "ERE_STAGE15_SCIENTIFIC_OBJECT.lock": "08_historical_controls/ERE_STAGE15_SCIENTIFIC_OBJECT.lock",
}


def git_head() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        ).stdout.strip()
    except Exception:
        return "UNKNOWN"


def main() -> None:
    missing = [str(p.relative_to(ROOT)) for p in FILES if not p.exists()]
    if missing:
        raise RuntimeError(f"submission-ready bundle missing required inputs: {missing}")

    DIST.mkdir(exist_ok=True)
    if OUT.exists():
        OUT.unlink()

    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        zf.writestr(
            "SOURCE_COMMIT.txt",
            f"repository=public-climate-protection-private-production-redundancy\n"
            f"commit={git_head()}\n"
            f"target=Environmental and Resource Economics\n"
            f"status=independent-audit repair candidate; author scientific review and live portal sign-off pending\n",
        )
        for src, arc in FILES.items():
            zf.write(src, arc)
        zf.writestr("COMPONENT_SHA256.json",json.dumps(
            {arc:hashlib.sha256(src.read_bytes()).hexdigest() for src,arc in FILES.items()},
            indent=2,sort_keys=True)+"\n")

    with zipfile.ZipFile(OUT) as zf:
        names = set(zf.namelist())
        required = {"SOURCE_COMMIT.txt", "COMPONENT_SHA256.json", *FILES.values()}
        missing_names = sorted(required - names)
        if missing_names:
            raise RuntimeError(f"submission-ready bundle incomplete: {missing_names}")

    print(f"ERE submission-ready transport bundle PASS: {OUT.relative_to(ROOT)}")
    print(f"files: {len(FILES)} + source commit and component hashes")


if __name__ == "__main__":
    main()
