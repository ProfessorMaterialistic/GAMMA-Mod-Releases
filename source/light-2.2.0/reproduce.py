from pathlib import Path
import hashlib, json, subprocess, sys
base=Path(__file__).resolve().parent
output=base/'build'
assert not output.exists(), 'Use a clean source copy; preserve an existing build.'
subprocess.run([sys.executable,str(base/'tools/tactical_candidate.py'),'--baseline',str(base/'retained'),'--output',str(output),'--stage-only'],check=True)
expected=json.loads((base/'PACKAGE-MANIFEST.json').read_text(encoding='utf-8'))
for slug,wanted in expected.items():
    actual={p.relative_to(output/slug).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((output/slug).rglob('*')) if p.is_file()}
    assert actual==wanted, slug+' package differs'
print('PASS: both complete package trees reproduced exactly')
