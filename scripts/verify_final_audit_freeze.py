"""Validate an explicitly classified non-scientific descendant of immutable v4.

The original v4 lock is never regenerated or silently redirected. It is
checked against the exact GitHub baseline commit. Every changed/new tracked
file is separately pinned by the audit descendant lock. Economic formulas,
theorem statements, proofs, baseline model files and Lean proof code retain
their original content. Approval of prose is not fabricated author signoff.
"""
from __future__ import annotations
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE='990bbe13dd1c3470b378ccd0040a78a030750701'
DESC='submission/ERE_FINAL_AUDIT_DESCENDANT.lock.json'
OLD='submission/ERE_STAGE15_V4_SCIENTIFIC_OBJECT.lock'
FREEZE='PCPPR-THEORY-FREEZE-2026-10-03-v4'
# All other original files must remain byte identical to canonical main.
ALLOWED={
    '.github/workflows/verify.yml','Makefile','README.md',
    'paper/main.tex','paper/sections/01_introduction.tex',
    'paper/sections/04_main_results.tex','paper/sections/08_literature.tex',
    'paper/sections/10_conclusion.tex','paper/sections/A_proofs_verification.tex',
    'references/references.tex','references/references.bib',
    'formal/README.md','formal/PCPPR/GlobalLocalGovernment.lean',
    'scripts/generate_objects.py','scripts/build_verify_ere_source_package.py',
    'scripts/build_ere_review_package.py','scripts/build_ere_submission_bundle.py',
    'scripts/verify_ere_submission.py',
    'submission/ERE_review_Makefile','submission/ERE_replication_README.md',
    'submission/ERE_CURRENT_UPLOAD_MANIFEST.md','submission/ERE_cover_letter.md',
    'docs/AI_PROVENANCE_LOG.md','docs/EXPOSITION_ARCHITECTURE.md',
    'docs/EXPOSITION_STREAMLINING_REPORT_2026-10-03.md',
    'docs/REVIEWER_VERIFIABILITY_MAP.md','docs/REVIEWER_VERIFIABILITY_REPORT.md',
    'STAGE_13_REPORT.md','STAGE_14_REPORT.md',
}


def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT)


def blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def scientific_text(text):
    # Artwork legends are editorial objects and separately pinned. All other
    # equations, including inline math, retain their ordered byte content.
    text=re.sub(r'\\begin\{figure\}.*?\\end\{figure\}','',text,flags=re.S)
    parts=re.findall(r'\$(?:\\.|[^$])*\$|\\\[.*?\\\]|\\begin\{equation\*?\}.*?\\end\{equation\*?\}',text,re.S)
    claims=[m.group(0) for m in re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|proof)\}.*?\\end\{\1\}',text,re.S)]
    return parts+claims


def lean_without_comments(text):
    out=[];i=0;depth=0
    while i<len(text):
        if text.startswith('/-',i):depth+=1;i+=2
        elif depth and text.startswith('-/',i):depth-=1;i+=2
        elif depth:i+=1
        elif text.startswith('--',i):
            j=text.find('\n',i);i=len(text) if j<0 else j
        else:out.append(text[i]);i+=1
    if depth:raise AssertionError('Unterminated Lean comment')
    return ''.join(''.join(out).split())


def baseline_lock():
    original=git('show',f'{BASE}:{OLD}')
    assert (ROOT/OLD).read_bytes()==original,'Immutable v4 lock changed'
    lock=dict(line.split('=',1) for line in original.decode().splitlines() if line and not line.startswith('#'))
    trees={'paper_tree':'paper','formal_tree':'formal','references_tree':'references',
           'tables_tree':'tables','tests_tree':'tests','scripts_tree':'scripts'}
    paths={'theory_freeze_blob':'docs/THEORY_FREEZE.md',
           'stage6_recert_blob':'docs/STAGE_6_RECERTIFICATION_2026-10-03.md',
           'stage75_recert_blob':'docs/STAGE_7_5A_RECERTIFICATION_2026-10-03.md',
           'formal_addendum_blob':'docs/FORMAL_VERIFICATION_GATE_ADDENDUM_2026-10-03.md',
           'independent_scientific_confirmation_blob':'docs/INDEPENDENT_SCIENTIFIC_CONFIRMATION_2026-10-03.md',
           'author_confirmation_blob':'docs/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md',
           'ai_provenance_blob':'docs/AI_PROVENANCE_LOG.md',
           'mechanism_benchmark_blob':'docs/mechanism_benchmark.json',
           'portability_results_blob':'docs/v2_4_portability_results.json',
           'audit_repairs_blob':'docs/INDEPENDENT_AUDIT_REPAIRS_2026-10-02.md',
           'requirements_blob':'requirements.txt','makefile_blob':'Makefile',
           'workflow_blob':'.github/workflows/verify.yml'}
    for key,path in (trees|paths).items():
        assert git('rev-parse',f'{BASE}:{path}').decode().strip()==lock[key],(key,path)
    assert FREEZE in (ROOT/'docs/THEORY_FREEZE.md').read_text()
    return original


def main():
    original=baseline_lock()
    lock=json.loads((ROOT/DESC).read_text())
    assert lock['baseline_commit']==BASE and lock['scientific_freeze']==FREEZE
    assert lock['classification']=='non-scientific audited descendant'
    assert lock['original_v4_lock_sha256']==hashlib.sha256(original).hexdigest()
    oldfiles={e.split('\t',1)[1]:e.split()[2] for e in git('ls-tree','-r',BASE).decode().splitlines()}
    current={e.split('\t',1)[1]:e.split()[2] for e in git('ls-tree','-r','HEAD').decode().splitlines()}
    changed={p for p,sha in current.items() if oldfiles.get(p)!=sha}
    assert not (oldfiles.keys()-current.keys()),'Deletion requires scientific review'
    assert changed-{DESC}==set(lock['files']),'Unattested tracked changes'
    for path,expected in current.items():
        assert blob((ROOT/path).read_bytes())==expected,f'Uncommitted change at {path}'
        if path in oldfiles and oldfiles[path]!=expected:
            assert path in ALLOWED,f'Frozen science or unreviewed file changed: {path}'
        if path in lock['files']:
            assert expected==lock['files'][path],f'Descendant digest mismatch: {path}'
    for path in sorted(ALLOWED):
        if path.startswith('paper/'):
            old=git('show',f'{BASE}:{path}').decode();new=(ROOT/path).read_text()
            if path.endswith('A_proofs_verification.tex'):
                marker='\\subsection{Scope of the Lean formalization}'
                assert old.split(marker)[0]==new.split(marker)[0],'Analytic proof logic changed'
            else:
                assert scientific_text(old)==scientific_text(new),f'Economic formula or theorem changed: {path}'
        if path.endswith('.lean'):
            assert lean_without_comments(git('show',f'{BASE}:{path}').decode())==lean_without_comments((ROOT/path).read_text()),'Lean proof code changed'
    oldlog=git('show',f'{BASE}:docs/AI_PROVENANCE_LOG.md')
    assert (ROOT/'docs/AI_PROVENANCE_LOG.md').read_bytes().startswith(oldlog),'Old provenance overwritten'
    print('Immutable v4 baseline + pinned non-scientific final-audit descendant: PASS')
    print('Equations/theorem/proof logic, model, welfare, witness, exact production certificates and Lean proof code unchanged')
    print('No new author scientific confirmation or live submission authorization is asserted')


if __name__=='__main__':main()
