"""A populated mathlib cache must not enter the anonymous scientific archive."""
import pathlib
import sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
import build_ere_review_package as builder

def test_formal_cache_and_nested_unrelated_sources_are_excluded(tmp_path,monkeypatch):
    paths=['formal/Main.lean','formal/PCPPR/Backup.lean',
           'formal/.lake/packages/mathlib/Mathlib/IdentifyingFixture.lean']
    for name in paths:
        p=tmp_path/name
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text('-- fixture\n')
    monkeypatch.setattr(builder,'ROOT',tmp_path)
    selected={p.relative_to(tmp_path).as_posix() for p in builder.selected_files()}
    assert selected=={'formal/Main.lean','formal/PCPPR/Backup.lean'}
