from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "stage12": ROOT / "docs" / "STAGE_12_REPORT.md",
    "stage13": ROOT / "STAGE_13_REPORT.md",
    "checklist": ROOT / "submission" / "ERE_submission_checklist.md",
    "cover": ROOT / "submission" / "ERE_cover_letter.md",
    "manuscript": ROOT / "paper" / "main.tex",
    "title": ROOT / "submission" / "ERE_title_page.tex",
    "provenance": ROOT / "docs" / "AI_PROVENANCE_LOG.md",
    "author_record": ROOT / "docs" / "AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md",
    "source_builder": ROOT / "scripts" / "build_verify_ere_source_package.py",
}

def read(name: str) -> str:
    p = FILES[name]
    if not p.exists():
        raise AssertionError(f"missing Stage-13 integration artifact: {p.relative_to(ROOT)}")
    return p.read_text(encoding="utf-8", errors="ignore")

def main() -> None:
    texts = {k: read(k) for k in FILES}

    if "ENVIRONMENTAL AND RESOURCE ECONOMICS" not in texts["stage12"].upper():
        raise AssertionError("Stage-12 recertification does not select ERE")
    if "06c67fe65ad5d80e42808aab6e7bd9f3db33eddb" not in texts["checklist"]:
        raise AssertionError("Stage-13 checklist is not synchronized to the v2.3+v2.4 Stage-12 merge")
    if "maintained symmetric primitive family" not in texts["cover"]:
        raise AssertionError("cover letter theorem scope is broader than the manuscript")
    if "Pre-specified diagnostic re-solutions" not in texts["cover"]:
        raise AssertionError("cover letter does not distinguish portability diagnostics from the exact theorem")
    if "do not substitute for author judgment" not in texts["manuscript"]:
        raise AssertionError("manuscript AI disclosure lost the accountability boundary")
    if "those tools are not authors" not in texts["title"]:
        raise AssertionError("title page lost the tool/authorship boundary")
    if "Historical coverage boundary" not in texts["provenance"]:
        raise AssertionError("AI provenance log does not disclose incomplete pre-repository historical coverage")
    pending = "PERSONAL AUTHOR CONFIRMATION PENDING" in texts["author_record"]
    confirmed = "PERSONALLY CONFIRMED BY AUTHOR — 2026-09-25" in texts["author_record"]
    if not (pending or confirmed):
        raise AssertionError("author record has neither the Stage-13 pending state nor a later explicit author-confirmed state")
    if confirmed and "This confirmation is author-controlled and was not inferred or supplied by automated QA." not in texts["author_record"]:
        raise AssertionError("later author confirmation lacks the explicit human-control boundary")

    active = "\n".join(
        texts[k] for k in ("stage13", "checklist", "cover", "manuscript", "title")
    )
    stale = [
        "checkpoint-stage13-ere-2026-09-14",
        "GO-RAND",
        "[RESEARCH_TOPIC]",
        "[WORKING_TITLE]",
        "TODO",
    ]
    for token in stale:
        if token in active:
            raise AssertionError(f"stale/placeholder Stage-13 token found: {token}")

    print("Stage-13 integration consistency PASS")

if __name__ == "__main__":
    main()
