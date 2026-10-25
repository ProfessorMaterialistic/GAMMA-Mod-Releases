"""Stage the matched tactical pair from an explicit preserved FOMOD baseline.

Never imports legacy builders or writes to live mods. Stage once, test, then
archive with the exact committed source identity. Dependencies are development-only.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import xml.etree.ElementTree as ET
import tactical_patch

WORK = Path(__file__).resolve().parents[1]
VERSION = '2.2.0'
SLUGS = ('One-Key-Light', 'Unified-Player-Light-Controls')


def inventory(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob('*')) if p.is_file()}


def verify_baseline(root):
    expected = json.loads((WORK / 'tools/tactical-baseline.json').read_text(encoding='utf-8'))
    for slug in SLUGS:
        assert inventory(root / slug) == expected[slug], 'Preserved 2.1.3 baseline drift: ' + slug


def stage(args):
    assert not args.output.exists(), 'Use fresh staging; never overwrite a candidate'
    assert args.baseline.resolve() != args.output.resolve()
    shutil.copytree(args.baseline, args.output)
    (args.output / '.tactical-staging').write_text('Light tactical build staging\n')
    render(args)


def render(args):
    for slug in SLUGS:
        package = args.output / slug
        core = package / ('Core' if slug == SLUGS[0] else 'core') / 'gamedata/scripts'
        for folder in ('canonical', 'onekey' if slug == SLUGS[0] else 'unified'):
            for source in (WORK / folder).glob('*.script'):
                # Canonical compatibility facades are retained unless authored here.
                targets = list(package.rglob(source.name))
                if source.name in ('light_tactical.script', 'light_laser_diagnostics.script') or folder == 'onekey' and not targets:
                    targets = [core / source.name]
                for target in targets:
                    target.write_bytes(source.read_bytes())
        for name, patch in [('zzz_bas_laser_control', tactical_patch.laser), ('one_key_lights_menu', tactical_patch.menu), ('one_key_lights_mcm', tactical_patch.mcm)]:
            for path in package.rglob(name + '.script'):
                baseline = args.baseline / slug / path.relative_to(package)
                path.write_text(patch(baseline.read_text(encoding='utf-8-sig')), encoding='utf-8', newline='\n')
        for path in package.rglob('*'):
            if path.is_file() and path.suffix in ('.script', '.xml'):
                text = path.read_text(encoding='utf-8-sig')
                # Display strings only; never alter device modes or option paths.
                text = text.replace('2.1.3-rc.1', VERSION).replace('2.1.2-rc.1', VERSION)
                path.write_text(text, encoding='utf-8', newline='\n')
        (package / 'VERSION').write_text(VERSION + '\n', encoding='utf-8')
        notes = (WORK / 'release-docs/TACTICAL-2.2.md').read_text(encoding='utf-8')
        for name in ('README.md', 'RELEASE-NOTES.md', 'INSTALL.md'):
            (package / name).write_text(notes, encoding='utf-8')
        info_path = package / 'fomod/info.xml'
        info = ET.parse(info_path)
        info.find('Description').text = 'Fixes Momentary Hold ON/OFF sound feedback. Preserves rc.6 gesture timing and grouped controls, rc.5 laser correction, and existing tactical/radial features. Owner-confirmed rc.7 gameplay; stable labels and release documentation.'
        info.write(info_path, encoding='utf-8', xml_declaration=True)
        (package / 'CHANGELOG.md').write_text(notes + '\n## Previous candidate history\n\n' + (args.baseline / slug / 'CHANGELOG.md').read_text(encoding='utf-8'), encoding='utf-8')
        (package / 'CANDIDATE-PROVENANCE.json').unlink(missing_ok=True)
        if slug == SLUGS[0]:
            captions = package / 'Core/gamedata/configs/text/eng/st_one_key_tactical.xml'
            root = ET.Element('string_table')
            for key, value in {'save_profile': 'Save Profile', 'load_profile': 'Load Profile'}.items():
                node = ET.SubElement(root, 'string', id='ui_mcm_one_key_lights_menu_' + key)
                ET.SubElement(node, 'text').text = value
            hints = {
                'tap': 'Press and release the Light Control Key once. Tap remains available when Momentary Hold is assigned. Headlamp and Weapon Light follow the Light Linking settings.',
                'double': 'Press and release the Light Control Key twice within the Double Tap Window. Double Tap remains available when Momentary Hold is assigned.',
                'hold': 'Hold the Light Control Key until the Hold Threshold. This action is used only when Momentary Hold is None. Releasing does not undo this normal Hold action.',
                'held': 'Keep the Light Control Key down until the Hold Threshold to activate temporary lighting. Release to restore previous lighting. This replaces only Hold, leaving Tap and Double Tap available. Weapon Light follows NVGs; changing NVG state cancels it until release and a new hold.',
                'modifiers': 'Enable this modifier independently. Apply and reopen Controls to show or hide its four bindings. Disabling keeps your saved actions. Enabled modifier actions replace the old Quick Menu modifier shortcut.',
            }
            for key, value in hints.items():
                node = ET.SubElement(root, 'string', id='ui_mcm_light_' + key + '_desc')
                ET.SubElement(node, 'text').text = value
            ET.ElementTree(root).write(captions, encoding='utf-8', xml_declaration=True)
        # Native button captions use string IDs rather than the row caption.
        overrides = {
            'ui_mcm_one_key_lights_bindings_clear': 'Clear Vanilla Torch Binding',
            'ui_mcm_one_key_lights_bindings_restore': 'Restore Vanilla Torch Binding',
            'ui_mcm_one_key_lights_section_bindings': 'Anomaly Torch Binding',
            'ui_mcm_unified_lights_section_diagnostics': 'Compatibility / Debug',
        }
        for path in package.rglob('configs/text/eng/*.xml'):
            tree = ET.parse(path)
            for node in tree.findall('string'):
                if node.get('id') in overrides:
                    node.find('text').text = overrides[node.get('id')]
            tree.write(path, encoding='utf-8', xml_declaration=True)
    for slug in SLUGS:
        for document in (WORK / 'release-docs' / slug).iterdir():
            if document.is_file(): shutil.copy2(document, args.output / slug / document.name)
    validate(args.output)


def validate(root):
    for slug in SLUGS:
        package = root / slug
        assert (package / 'VERSION').read_text().strip() == VERSION
        assert ET.parse(package / 'fomod/info.xml').findtext('Version') == VERSION
        config = ET.parse(package / 'fomod/ModuleConfig.xml')
        for node in config.findall('.//folder') + config.findall('.//file'):
            relative = Path(node.attrib['source'])
            assert not relative.is_absolute() and '..' not in relative.parts
            assert (package / relative).exists(), relative
        for path in package.rglob('*.xml'):
            if not path.read_text(encoding='utf-8-sig').lstrip().startswith('#include'):
                ET.parse(path)
    one = {p.name: p.read_bytes() for p in (root / SLUGS[0]).rglob('*.script')}
    two = {p.name: p.read_bytes() for p in (root / SLUGS[1]).rglob('*.script')}
    for name in one.keys() & two.keys():
        assert one[name] == two[name], 'Shared script mismatch: ' + name


def package(args):
    assert len(args.source_commit or '') == 40
    validate(args.output)
    records = []
    for slug in SLUGS:
        root = args.output / slug
        provenance = dict(version=VERSION, source_commit=args.source_commit, gameplay='TESTED: owner-confirmed accepted configuration', baseline=inventory(args.baseline / slug))
        (root / 'CANDIDATE-PROVENANCE.json').write_text(json.dumps(provenance, indent=2) + '\n', encoding='utf-8')
        archive = args.output.parent / (slug + '-v' + VERSION + '.7z')
        assert not archive.exists()
        subprocess.run([str(args.seven_zip), 'a', '-t7z', '-mx=7', str(archive), '.'], cwd=root, check=True, capture_output=True)
        subprocess.run([str(args.seven_zip), 't', str(archive)], check=True, capture_output=True)
        extracted = args.output.parent / 'extracted' / slug
        assert not extracted.exists()
        subprocess.run([str(args.seven_zip), 'x', str(archive), '-o' + str(extracted), '-y'], check=True, capture_output=True)
        assert inventory(root) == inventory(extracted)
        records.append(dict(archive=archive.name, sha256=hashlib.sha256(archive.read_bytes()).hexdigest(), files=inventory(root)))
    (args.output.parent / 'package-manifest.json').write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
    print('PASS: matched FOMODs, shared scripts, archive integrity and extracted hashes')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--stage-only', action='store_true')
    parser.add_argument('--refresh', action='store_true')
    parser.add_argument('--source-commit')
    parser.add_argument('--seven-zip', type=Path, default=Path('7z'))
    args = parser.parse_args()
    verify_baseline(args.baseline)
    if args.refresh:
        assert (args.output / '.tactical-staging').is_file(), 'Not tactical staging'
        render(args)
    elif args.stage_only:
        stage(args)
    else:
        package(args)
