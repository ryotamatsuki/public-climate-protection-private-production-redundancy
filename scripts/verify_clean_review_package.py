"""Execute the advertised commands from the actual anonymous ZIP, without Git."""
from __future__ import annotations
import argparse
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--formal',action='store_true',help='also execute the advertised Lean command')
    args=parser.parse_args()
    archive=ROOT/'dist/ERE_anonymous_replication.zip'
    target='formal-verify' if args.formal else 'verify'
    log=ROOT/'dist'/f'anonymous-{target}-reproduction.log'
    with tempfile.TemporaryDirectory(prefix='ere-anonymous-reproduction-') as td:
        work=Path(td)
        with zipfile.ZipFile(archive) as zf:
            if zf.testzip() is not None:
                raise AssertionError('corrupt replication archive')
            zf.extractall(work)
        assert not (work/'submission').exists() and not (work/'.git').exists()
        # This also tests the dependency repair if generation is genuinely needed.
        if args.formal:
            (work/'formal/PCPPR/GeneratedCertificates.lean').unlink()
            (work/'formal/GENERATED_CERTIFICATE_ARCHIVE.json').unlink()
        command=['make',f'PYTHON={sys.executable}',target]
        with log.open('w') as stream:
            result=subprocess.run(command,cwd=work,stdout=stream,stderr=subprocess.STDOUT)
        if result.returncode:
            tail=log.read_text(errors='replace').splitlines()[-35:]
            raise RuntimeError(f'extracted anonymous {target} failed:\n'+'\n'.join(tail))
        if not args.formal:
            assert (work/'paper/main.pdf').stat().st_size>0
        else:
            report=work/'formal/FORMAL_AXIOM_REPORT.txt'
            assert report.is_file() and 'sorryAx' not in report.read_text()
            (ROOT/'dist/anonymous-FORMAL_AXIOM_REPORT.txt').write_bytes(report.read_bytes())
    print(f'actual anonymous ZIP: make {target} completed without editorial files or Git')


if __name__=='__main__':
    main()
