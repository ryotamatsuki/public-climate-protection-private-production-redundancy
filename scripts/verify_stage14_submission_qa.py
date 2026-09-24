from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")

def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"Stage-14 QA failure: missing {label}: {needle!r}")

report = read("STAGE_14_REPORT.md")
ledger = read("docs/STAGE_14_LIVE_REQUIREMENTS_LEDGER_ERE_2026-09-25.md")
ai_log = read("docs/AI_PROVENANCE_LOG.md")
author_record = read("docs/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md")
manuscript = read("paper/main.tex")
checklist = read("submission/ERE_submission_checklist.md")
readme = read("README.md")
reviewer_report = read("docs/REVIEWER_VERIFIABILITY_REPORT.md")

require(report, "PUBLIC-RULE / REPOSITORY QA: PASS", "public-rule QA verdict")
require(report, "FULL STAGE-14 CLOSURE: HOLD", "fail-closed Stage-14 verdict")
require(report, "UNVERIFIED", "portal-only unresolved state")
require(ledger, "Article type", "live article-type ledger row")
require(ledger, "UNVERIFIED — PORTAL ONLY", "portal-only ledger state")
require(ai_log, "2026-09-06", "pre-2026-09-14 AI provenance")
require(ai_log, "2026-09-13", "Stage-11-era AI provenance")
require(author_record, "PERSONAL AUTHOR CONFIRMATION PENDING", "human confirmation boundary")
require(manuscript, r"\section*{AI Assistance Disclosure}", "manuscript AI disclosure")
require(manuscript, r"\section*{Data and Code Availability}", "data/code availability statement")
require(checklist, "Authenticated Editorial Manager checks", "portal checklist")
require(reviewer_report, "PASS — REVIEWER VERIFIABILITY", "v2.7 reviewer-verifiability verdict")
require(reviewer_report, "No item is classified **BRIDGE NEEDED**, **APPENDIX DETAIL NEEDED**, or **SUBSTANTIVE DEFECT**", "v2.7 clean-room closure")
require(report, "v2.7 reviewer-verifiability audit PASS recorded", "Stage-14 v2.7 closure record")
require(readme, "Stage 14 submission QA", "current phase")

for forbidden in [
    "Final verdict: PASS. The repository is ready for the external ERE portal-submission step.",
    "FULL STAGE-14 CLOSURE: PASS",
]:
    if forbidden in report:
        raise SystemExit(f"Stage-14 QA failure: stale/unsafe closure wording present: {forbidden!r}")

print("Stage-14 submission QA regression: PASS")
