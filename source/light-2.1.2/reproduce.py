from pathlib import Path
import hashlib, json, shutil, subprocess, sys
base=Path(__file__).resolve().parent
build=base/'build'
assert not build.exists(), 'Use a clean source copy; preserve an existing build.'
(base/'reports').mkdir(exist_ok=True)
for slug,folder in [('One-Key-Light','One Key Light Rebuild'),('Unified-Player-Light-Controls','Unified Player Light Controls Rebuild')]:
    shutil.copytree(base/'retained'/slug,build/folder)
for name in ['customize.py','visuals.py','package.py']:
    subprocess.run([sys.executable,str(base/'tools'/name)],cwd=base,check=True)
expected=json.loads((base/'RUNTIME-MANIFEST.json').read_text())
for slug,folder in [('One-Key-Light','One Key Light Rebuild'),('Unified-Player-Light-Controls','Unified Player Light Controls Rebuild')]:
    actual={p.relative_to(build/folder).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (build/folder).rglob('*') if p.is_file() and 'gamedata' in p.parts}
    assert actual==expected[slug], slug+' runtime/assets differ'
print('PASS: all 85 runtime/asset members reproduced exactly. No live files accessed.')
