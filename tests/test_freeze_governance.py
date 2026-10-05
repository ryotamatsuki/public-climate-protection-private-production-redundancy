"""Governance must reject changed quantifiers/proofs and hidden Lean code."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import pytest
from verify_final_audit_freeze import scientific_text,lean_without_comments,discussion_without_empirical_addition


def test_prose_change_does_not_hide_a_changed_formula_or_quantifier():
    original=r'Intro $q=q_0-a$. \begin{theorem}For every $a$, $W_a<0$.\end{theorem}'
    edited=original.replace('Intro','Short introduction')
    assert scientific_text(original)==scientific_text(edited)
    assert scientific_text(original)!=scientific_text(original.replace('every','some'))
    assert scientific_text(original)!=scientific_text(original.replace('q_0-a','q_0+a'))


def test_nested_comments_cannot_mask_proof_code_changes():
    text='/-- outer /- nested -/ comment -/\ntheorem t : 1=1 := by rfl -- end\n'
    assert lean_without_comments(text)==lean_without_comments('theorem t : 1=1 := by rfl')
    assert lean_without_comments(text)!=lean_without_comments(text.replace('rfl','native_decide'))


def test_empirical_exposition_exception_preserves_original_discussion():
    original='Frozen scope $W_a<0$.\n\n\\subsection{Diagnostic portability}\nFrozen diagnostics.\n'
    addition=('% BEGIN EMPIRICAL IMPLICATIONS ONLY\n'
              '\\subsection{Empirical implications and testable predictions}\nProse with proxy $r_i$.\n'
              '% END EMPIRICAL IMPLICATIONS ONLY\n\n')
    edited=original.replace('\\subsection{Diagnostic portability}',addition+'\\subsection{Diagnostic portability}')
    assert discussion_without_empirical_addition(edited)==original
    assert discussion_without_empirical_addition(edited.replace('W_a<0','W_a>0'))!=original
    with pytest.raises(AssertionError):
        discussion_without_empirical_addition(edited.replace('Prose with proxy',r'\begin{theorem}New claim\end{theorem} Prose with proxy'))
    with pytest.raises(AssertionError):
        discussion_without_empirical_addition(edited+addition)
