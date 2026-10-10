from pathlib import Path
import xml.etree.ElementTree as ET,hashlib,json,shutil,re,zipfile
WORK=Path(__file__).resolve().parents[1];ROOT=WORK/'inputs';ONE=WORK/'build/One Key Light Rebuild';UNI=WORK/'build/Unified Player Light Controls Rebuild'
def write(p,s): p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8',newline='\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def folder(parent,source,priority=10): ET.SubElement(parent,'folder',source=source,destination='gamedata',priority=str(priority))
def plugin(parent,name,description,source=None,recommended=False,flag=None):
    p=ET.SubElement(parent,'plugin',name=name);ET.SubElement(p,'description').text=description
    if source:folder(ET.SubElement(p,'files'),source)
    if flag: ET.SubElement(ET.SubElement(p,'conditionFlags'),'flag',name=flag[0]).text=flag[1]
    ET.SubElement(ET.SubElement(p,'typeDescriptor'),'type',name='Recommended' if recommended else 'Optional')
    return p
def group(steps,step_name,name,kind):
    step=ET.SubElement(steps,'installStep',name=step_name)
    g=ET.SubElement(ET.SubElement(step,'optionalFileGroups',order='Explicit'),'group',name=name,type=kind)
    return ET.SubElement(g,'plugins',order='Explicit')
for root,title,core in [(ONE,'One Key Light','Core'),(UNI,'Unified Player Light Controls','core')]:
    xml=ET.Element('config',{'xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance','xsi:noNamespaceSchemaLocation':'http://qconsulting.ca/fo3/ModConfig5.0.xsd'})
    ET.SubElement(xml,'moduleName').text=title+' 2.1.0'
    req=ET.SubElement(xml,'requiredInstallFiles');folder(req,core+'/gamedata',0)
    for name in ['README.md','RELEASE-NOTES.md','INSTALL.md','FEATURES.md','COMPATIBILITY.md','CHANGELOG.md','CREDITS.md','VERSION','LICENSE-NOTICES.md','SOURCE-AVAILABILITY.md','UTLF-GPL-3.0.txt','GAMMA-AGPL-3.0.txt','SOY-MIT.txt','MODIFICATIONS.md']:ET.SubElement(req,'file',source=name,destination=name,priority='0')
    steps=ET.SubElement(xml,'installSteps',order='Explicit')
    g=group(steps,'Dependencies','Required host','SelectAtLeastOne')
    plugin(g,'GAMMA and MCM are installed','Owner retest: MT-TEST 2026.08.04 / xrCore 10100 in the specific Bodycam/MT environment, AnomalyDX11AVX.exe with matching engine gamedata and MCM. Other engines/variants are unverified. Historical 2.0 used MT-TEST 2026.09.07 / xrCore 10074; it is not a second 2.1 retest. MGI and companion are optional. Includes scoped license notices and corresponding-source information.',recommended=True)
    g=group(steps,'Headlamp backend','Choose the same backend in both mods','SelectExactlyOne')
    plugin(g,'Native / G2X','Keeps the engine headlamp and installed G2X/DLTX presets. No Soy Adjustable dependency. Brightness, cone, range and visible color sliders do not control the native beam. G2X assets must be installed separately. Use the same backend choice in both companion installers.','HeadlampBackends/Native/gamedata',True)
    plugin(g,"Soy Adjustable Headlamps 1.0","Requires Soy's Adjustable Headlamps 1.0 installed separately. Uses its ScriptLight rendering and battery integration. Enables headlamp tuning. Use the same backend choice in both companion installers.",'HeadlampBackends/Adjustable/gamedata')
    g=group(steps,'Laser integration','Laser Settings support','SelectExactlyOne')
    plugin(g,'No Laser Settings integration','Lighting controls only. Does not install a laser dependency.',recommended=True)
    plugin(g,'Laser Settings 2.7 installed','Requires Borksy Laser Settings 2.7. Installs the canonical synchronous input/setter bridge. Unified also retains its existing tuning GUI, reset/export and aim policies.',('LaserBackends/LaserSettings' if root==ONE else 'options/laser-settings')+'/gamedata')
    for label,sub,version in [('UTLF IR','UTLF_IR',"Soy's UTLF IR Mode 1.03 and UTLF 1.0.1"),('IR Headlamp','Headlamp_IR',"Soy's IR Headlamps 1.3.0 and its NVG illuminator module")]:
        g=group(steps,label+' compatibility',label+' supported dependency','SelectExactlyOne')
        plugin(g,'Not installed','Skip this compatibility patch.',recommended=True)
        plugin(g,version+' installed','Select only with the listed dependencies enabled. Installs compatibility scripts, not dependency assets. Neither companion mod is required.','Compatibility/'+sub+'/gamedata')
    ET.indent(xml,space='  ');write(root/'fomod/ModuleConfig.xml',ET.tostring(xml,encoding='unicode',xml_declaration=True))
    info=ET.Element('fomod');ET.SubElement(info,'Name').text=title+' 2.1.0';ET.SubElement(info,'Author').text='Bling';ET.SubElement(info,'Version').text='2.1.0';ET.SubElement(info,'Description').text='Owner-tested 2.1.0 firing correction; independently installable Light controls with optional integrations.'
    write(root/'fomod/info.xml',ET.tostring(info,encoding='unicode',xml_declaration=True))
    for old in ['RELEASE-v1.3.md','FEATURES.md','UPDATE-NOTES.md','CHANGELOG.md','REQUIREMENTS-AND-LOAD-ORDER.md']:
        p=root/old
        if p.exists():p.unlink()

# Delivery documentation is maintained separately from runtime generators.
for root,slug in [(ONE,'One-Key-Light'),(UNI,'Unified-Player-Light-Controls')]:
    for document in (WORK/'release-docs'/slug).iterdir():
        if document.is_file(): shutil.copyfile(document,root/document.name)
    obsolete=root/'TESTING.md'
    if obsolete.exists(): obsolete.unlink()

# Add captions for every newly introduced MCM option; upstream IDs retain their strings.
def strings(root,core,entries):
    xml=ET.Element('string_table')
    for key,text in entries.items(): ET.SubElement(ET.SubElement(xml,'string',id='ui_mcm_'+key),'text').text=text
    old=root/core/'gamedata/configs/text/eng/st_light_rebuild.xml'
    if old.exists():old.unlink()
    filename='st_one_key_rebuild.xml' if root==ONE else 'st_unified_light_rebuild.xml'
    write(root/core/'gamedata/configs/text/eng'/filename,ET.tostring(xml,encoding='unicode',xml_declaration=True))
strings(ONE,'Core',{'one_key_lights_section_controls':'Controls','one_key_lights_section_menu':'Quick Menu','one_key_lights_section_bindings':'Anomaly Torch Binding','one_key_lights_section_compatibility':'Compatibility','one_key_lights_controls_gesture_behavior':'Gesture Behavior','one_key_lights_controls_link_weapon':'Weapon Lights','one_key_lights_controls_link_head':'Headlamps','one_key_lights_menu_radial_labels':'Label Mode','one_key_lights_menu_icon_style':'Icons'})
strings(UNI,'core',{'menu_unified_lights':'Unified Player Light Controls 2.1.0','unified_lights_section_links':'Light Linking','unified_lights_section_diagnostics':'Compatibility / Debug','unified_lights_link_help':'NVG Linked uses visible lighting with NVGs stowed and IR lighting with NVGs deployed.','unified_lights_links_link_weapon':'Weapon Lights','unified_lights_links_link_head':'Headlamps','unified_lights_diagnostics_debug':'Debug Mode','unified_lights_debug':'Debug Mode'})
# Edit the retained title in place: duplicate string IDs have undefined load precedence.
title_file=ONE/'Core/gamedata/configs/text/eng/st_one_key_lights.xml'
title_xml=ET.parse(title_file)
title_xml.find(".//string[@id='ui_mcm_menu_one_key_lights']/text").text='One Key Light 2.1.0'
for key,value in {'bindings_clear':'Clear Vanilla Torch Binding','bindings_restore':'Restore Vanilla Torch Binding','menu_hide_bound':'Hide Gesture-Bound Actions'}.items():
    title_xml.find(".//string[@id='ui_mcm_one_key_lights_"+key+"']/text").text=value
write(title_file,ET.tostring(title_xml.getroot(),encoding='unicode',xml_declaration=True))
for root in [ONE,UNI]:
    for p in root.rglob('st_one_key_situational.xml'):p.unlink()

def files(root):
    out={}
    for p in root.rglob('*'):
        if p.is_file() and 'gamedata' in p.parts:
            key='/'.join(p.parts[p.parts.index('gamedata'):]);out.setdefault(key,[]).append(p)
    return out
a,b=files(ONE),files(UNI)
overlap=[]
for key in sorted(a.keys()&b.keys()):
    one_hashes={sha(p) for p in a[key]};uni_hashes={sha(p) for p in b[key]}
    assert one_hashes==uni_hashes,(key,one_hashes,uni_hashes)
    overlap.append({'path':key,'hashes':sorted(one_hashes),'variant_count':len(one_hashes),'status':'IDENTICAL for matching selections'})
write(WORK/'reports/overlap-hashes.json',json.dumps(overlap,indent=2))
print('Matching same-path overlap:',len(overlap),'paths, 0 differing files; Native/Adjustable variants are deliberate.')

# Installer source checks and texture coordinate bounds.
for root in [ONE,UNI]:
    tree=ET.parse(root/'fomod/ModuleConfig.xml')
    for e in tree.findall('.//folder')+tree.findall('.//file'):assert (root/e.attrib['source']).exists(),e.attrib
    for p in root.rglob('*.script'):assert 'test-deps' not in str(p)
atlas=ET.parse(ONE/'Core/gamedata/configs/ui/textures_descr/ui_one_key_light_icons.xml')
for t in atlas.findall('.//texture'):
    assert int(t.attrib['x'])+int(t.attrib['width'])<=512 and int(t.attrib['y'])+int(t.attrib['height'])<=256
