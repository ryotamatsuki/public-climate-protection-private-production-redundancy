"""Editorial-only checks, intentionally excluded from anonymous reproduction."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    text=(ROOT/'submission/ERE_title_page.tex').read_text(encoding='utf-8')
    if 'implemented and verified the computer-assisted analysis' in text:
        raise AssertionError('contribution statement conflates author and tool verification')
    if 'those tools are not authors' not in text:
        raise AssertionError('tool/authorship boundary missing')
    for declaration in ('Funding','Competing','Author'):
        if declaration not in text:
            raise AssertionError(f'editorial declaration missing: {declaration}')
    print('editorial title-page checks completed separately from anonymous checks')

if __name__=='__main__':
    main()
