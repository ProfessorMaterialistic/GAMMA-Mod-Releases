from pathlib import Path
import shutil, re, json, hashlib, difflib
WORK=Path(__file__).resolve().parents[1];ROOT=WORK/'inputs'
ONE=WORK/'build/One Key Light Rebuild';UNI=WORK/'build/Unified Player Light Controls Rebuild'
def read(p): return p.read_text(encoding='utf-8-sig')
def write(p,s): p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8',newline='\n')
def replace(s,a,b,count=1):
    assert s.count(a)>=count,(a,s.count(a));return s.replace(a,b,count)
def clean(mod,file): return read(ROOT/'mods'/mod/'gamedata/scripts'/file)
def reference(pkg,name):
    p=ROOT/'mods'/('One Key Light v.1.3' if pkg=='one' else 'Unified Player Light Controls - Bling v.1.3')/'gamedata/scripts'/name
    return read(p)
def guard(s,decl,key): return replace(s,decl,decl+'\n    -- LIGHT REBUILD: inhibit competing light handlers only in owned contexts.\n    if light_compat.owns_key('+key+') then return end')
def remove_function(s,name,next_name):
    start=s.index('function '+name+'(');end=s.index('function '+next_name+'(',start);return s[:start]+s[end:]
patches={}

s=clean('G.A.M.M.A. 3D PDA and Headlamp Animations','actor_effects.script')
s=replace(s,'function Hit_TorchToggle()','''-- LIGHT REBUILD: original GAMMA animation with a target-independent switch callback.
function Hit_TorchToggle()
    if not light_compat.animation_pending() then
        local handled=light_compat.manual("headlamp")
        if handled~=nil then return handled end
    end
    local det=db.actor and db.actor:active_detector()
    if det and det:section()=="device_flashlight" then return false end''')
s=replace(s,'(not item_device.can_toggle_torch())','(not light_compat.animation_equipped() and not item_device.can_toggle_torch())')
# Only the two switch points inside the headlamp animation, not other device code.
start=s.index('function Hit_TorchToggle()');end=s.index('function Hit_MaskCleaning()',start)
chunk=s[start:end].replace('item_device.toggle_torch()','light_compat.animation_switch()')
chunk=chunk.replace('\t\t\tsnd_headlamp:play(db.actor,0,sound_object.s2d)\n','')
chunk=chunk.replace('\tlocal function torch_toggle_anim_fast()', '\tlocal animation_token=light_compat.animation_token()\n\tlocal function torch_toggle_anim_fast()',1)
for name in ['torch_toggle_anim_fast','torch_toggle_anim']:
    chunk=chunk.replace('local function '+name+'()','local function '+name+'()\n        if not light_compat.animation_current(animation_token) then return true end',1)
chunk=chunk.replace('RemoveTimeEvent(0, "play_torch_toggle")','RemoveTimeEvent(0, "play_torch_toggle")\n            light_compat.animation_complete(animation_token)')
chunk=chunk.rstrip();assert chunk.endswith('end')
chunk=chunk[:-3]+'    return true\nend\n\n'
s=s[:start]+chunk+s[end:]
s=guard(s,'local function on_key_release(key)','key')
s=replace(s,'\tgame.stop_hud_motion()','\t-- LIGHT REBUILD: stop_all_hud_anms above already resets HUD state.\n\t-- The zero-argument stop_hud_motion call throws on current Modded Exes.')
s+='\n-- LIGHT REBUILD: capture before upstream Torch wrappers are installed.\noklc_animated_headlamp=Hit_TorchToggle\n'
s+='''
function light_feedback(enabled) snd_headlamp:play(db.actor,0,sound_object.s2d) end
function oklc_cancel_headlamp_animation()
    RemoveTimeEvent(0,"play_torch_toggle")
    torch_anm_state=0;torch_anm_start=0;torch_anm_state_dbg=0
    game.only_allow_movekeys(false);game.set_actor_allow_ladder(true)
end
'''
s=s.replace('printf("PDA Out")','light_compat.trace("PDA Out")').replace('printf(state)','light_compat.trace("%s",tostring(state))')
patches['actor_effects.script']=s

s=clean('Universal_Tactical_Light_Framework-1.0.1','utlf_input.script')
s=replace(s,'local function toggle_light()','local function toggle_light()\n    local handled=light_compat.manual("utlf_visible")\n    if handled~=nil then return handled end')
s=replace(s,'    local weapon, profile = utlf_core.active_supported_weapon()','    if not light_compat.module("utlf_core") then return false end\n    local weapon, profile = utlf_core.active_supported_weapon()')
for event in ['press','release']:
    s=guard(s,'local function on_before_key_'+event+'(key, bind, dis, flags)','key')
s=replace(s,'    wrap_engine_torch_toggle()\n\n    local settings','    if not light_compat.module("utlf_core") then return end\n    wrap_engine_torch_toggle()\n\n    local settings')
s+='\n-- LIGHT REBUILD: direct entry and legacy alias.\nfunction oklc_toggle() return toggle_light() end\n'
s+='\nfunction light_feedback(enabled) play_toggle_sound(enabled) end\n'
s=s.replace('printf(','light_compat.trace(')
patches['utlf_input.script']=s

s=clean("Soy's UTLF IR Mode v1.03",'utlf_ir_mode.script')
# Use the same emission gate for IR recovery/activation during a shot.
s=replace(s,'if weapon:get_state() ~= 0 then','if not light_backends.weapon_emission_ready(weapon) then')
s=replace(s,'local function toggle_ir_mode()','local function toggle_ir_mode()\n    local handled=light_compat.manual("utlf_ir")\n    if handled~=nil then return handled end')
for event in ['press','release']: s=guard(s,'local function on_before_key_'+event+'(key, bind, dis, flags)','key')
s=replace(s,'    if normal_utlf_key_pressed(key) then','''    if normal_utlf_key_pressed(key) then
        -- The authoritative White handler owns the shared emitter transition.
        if light_compat.controller() or light_compat.module("one_key_lights_standalone") then return end''')
s=replace(s,'    local enabling = not ir_requested','''    local handled=light_compat.manual("utlf_ir")
    if handled~=nil then return end
    local enabling = not ir_requested''')
s=replace(s,'local function actor_on_update()','''local function actor_on_update()
    -- LIGHT REBUILD: Unified alone owns routing/recovery; upstream transforms stay intact.
    if light_compat.controller() then return end''')
s+='''
-- LIGHT REBUILD: synchronous silent physical setter and inexpensive legacy aliases.
function light_has_nvgs() return has_equipped_nvgs() end
function light_set(enabled)
    if not enabled then
        if ir_requested or _G.utlf_weapon_ir_active then
            ir_requested=false;previous_nv_state=nil;detach_ir_light("Light OFF")
        end
        return true
    end
    if not has_equipped_nvgs() or not get_nv_state() then return false end
    ir_requested=true;previous_nv_state=get_nv_state()
    local s=current_state()
    if not s then return false end
    if not s.light or not _G.utlf_weapon_ir_active then return attach_ir_light("Light IR") end
    if not rawequal(s.light,last_ir_light_object) then
        apply_active_ir_settings();last_ir_light_object=s.light
    end
    return true
end
function oklc_requested() return ir_requested end
function bling_ir_requested() return ir_requested end
function oklc_toggle() return toggle_ir_mode() end
function bling_ir_toggle() return toggle_ir_mode() end
function oklc_disable() return light_set(false) end
function bling_pair_set(v) return light_set(v) end
function oklc_available() return has_equipped_nvgs() and utlf_core.active_supported_weapon()~=nil end
function light_feedback(enabled) play_toggle_sound(enabled) end
'''
patches['utlf_ir_mode.script']=s

s=clean('Soys_IR_Headlamps_v1.3.0','ir_headlamp.script')
s=guard(s,'function on_key_press(dik)','dik')
s=replace(s,'function toggle_ir()','function toggle_ir()\n    local handled=light_compat.manual("headlamp_ir")\n    if handled~=nil then return handled end')
s=replace(s,'function set_ir_enabled(enabled)','function set_ir_enabled(enabled)\n    local handled=light_compat.select("headlamp_ir",enabled)\n    if handled~=nil then return handled end')
s=replace(s,'function actor_on_update()','function actor_on_update()\n    -- LIGHT REBUILD: keep transform rendering, suppress competing AUTO ownership.\n    if light_compat.controller() then update_ir_light();return end')
s+='''
-- LIGHT REBUILD: physical setter is silent; the animation job owns all presentation.
function light_set(enabled)
    if enabled and not has_ir_illuminator() then return false end
    ir_enabled=enabled==true
    if not ir_enabled then destroy_ir_light() else update_ir_light() end
    return true
end
function bling_pair_set(enabled) return light_set(enabled) end
function light_feedback(enabled) play_ir_toggle_sound(enabled) end
'''
patches['ir_headlamp.script']=s

s=clean("Soy's Adjustable Headlamps v1.0",'adjustable_flashlight.script')
# Trace itself is upstream temporary diagnostics; retain call sites, gate one sink.
s=replace(s,'local function trace(message, ...)','local function trace(message, ...)\n    if not light_compat.debug_enabled then return end')
for event in ['press','release']: s=guard(s,'function on_key_'+event+'(dik)','dik')
s=replace(s,'if force or applied_brightness ~= brightness then','if light_compat.module("bling_player_lights") then\n        bling_player_lights.tint_headlamp(flashlight_light,brightness,"headlamp")\n    elseif force or applied_brightness ~= brightness then')
s=replace(s,'function toggle_immediate()','function toggle_immediate()\n    local handled=light_compat.manual("headlamp")\n    if handled~=nil then return handled end')
s=replace(s,'function set_enabled(enabled)','function set_enabled(enabled)\n    local handled=light_compat.select("headlamp",enabled)\n    if handled~=nil then return handled end')
s=replace(s,'function toggle_from_vanilla()','function toggle_from_vanilla()\n    local handled=light_compat.manual("headlamp")\n    if handled~=nil then return handled end')
# Native key fallback must not compete with Unified's intent/animation target.
s=replace(s,'function on_key_release(dik)','function on_key_release(dik)\n    if light_compat.controller() then return end')
s+='\n-- LIGHT REBUILD: availability is equipment; battery is a separate capability.\nfunction oklc_available() return not handheld_flashlight_active() and get_equipped_torch()~=nil end\noklc_backend_name="Soy Adjustable Headlamps"\n'
patches['adjustable_flashlight.script']=s

s=clean('465- Laser Settings - Borksy','zzz_bas_laser_control.script')
for event in ['press','release']: s=guard(s,'function on_key_'+event+'(key)','key')
s=guard(s,'function on_before_key_press(key, bind, dis, flags)','key')
start=s.index('function toggle_laser(id)');end=s.index('function set_laser(',start)
s=s[:start]+'''-- LIGHT REBUILD: synchronous intent setter, preserving upstream camera/sound.
function light_feedback(enabled,manual)
    if manual then level.add_cam_effector("camera_effects\\\\weapon\\\\ak74_switch_off.anm",9342,false,'') end
    snd_laser.frequency=enabled and 1.15 or 0.85
    snd_laser:play(db.actor,0,sound_object.s2d)
end
function light_set(id,enabled,manual)
    enabled=enabled==true
    local changed=saved_lasers[id]~=enabled
    saved_lasers[id]=enabled
    if changed and manual then
        light_feedback(enabled,true)
    end
    local w=level.object_by_id(id)
    set_laser(enabled and 1 or 0,w and w:section())
    return true
end
function oklc_is_on(id) return saved_lasers[id]==true end
bling_is_on=oklc_is_on
function bling_set_enabled(id,v) return light_set(id,v,false) end
function toggle_laser(id)
    local handled=light_compat.manual("laser")
    if handled~=nil then return handled end
    return light_set(id,not saved_lasers[id],true)
end
local light_output=false
function light_emitting() return light_output end

'''+s[end:]
s=replace(s,'function set_laser(on_off, section)','function set_laser(on_off, section)\n    light_output=on_off~=0')
patches['zzz_bas_laser_control.script']=s

s=clean('Universal_Tactical_Light_Framework-1.0.1','utlf_battery.script')
s=replace(s,'local drain = nil','''local drain = nil
-- LIGHT REBUILD: preserve the upstream battery record while AUTO hides emission.
local function aim_paused()
    local api=light_compat.controller()
    return api and api.battery_paused()==true or false
end
function is_flickering_off() return drain~=nil and drain.flicker_off==true end''')
s=replace(s,'if s.light and s.desired_on and not s.hud_item_light_suspended then','if s.light and s.desired_on and not s.hud_item_light_suspended and not aim_paused() then')
needle='    update_low_battery_flicker(now)'
s=replace(s,needle,'''    if aim_paused() then
        drain.last_update=now;drain.aim_paused=true;drain.flicker_off=false;drain.next_flicker_at=nil
        s.light.enabled=false;return false
    end
    if drain.aim_paused then drain.last_update=now;drain.aim_paused=nil end
'''+needle)
patches['utlf_battery.script']=s
s=replace(s,'function on_game_start()','function on_game_start()\n    if not light_compat.module("utlf_core") then return end')
patches['utlf_battery.script']=s
s=clean('Universal_Tactical_Light_Framework-1.0.1','utlf_items.script')
s=replace(s,'min = 5, max = 80','min = 5, max = 200');s=replace(s,'min = 8, max = 90','min = 8, max = 120')
patches['utlf_items.script']=s

# Cache upstream MCM reads used by transform loops; invalidate on edits/load.
for name in ['adjustable_flashlight.script','ir_headlamp.script']:
    s=patches[name]
    declaration='local function get_mcm_value(path, default)'
    s=replace(s,declaration,'''local light_settings_cache={}
local light_settings_generation=-1
local function read_mcm_value(path, default)''')
    next_decl='local function get_config_key()' if name=='adjustable_flashlight.script' else 'local function get_toggle_key()'
    pos=s.index(next_decl)
    wrapper='''local function get_mcm_value(path, default)
    local store=light_compat.module("unified_light_store")
    if store then
        local value=store.get(path,nil,type(default)=="boolean" and 1 or 2)
        if value~=nil then return value end
    end
    if light_settings_generation~=light_compat.settings_generation then
        light_settings_cache={};light_settings_generation=light_compat.settings_generation
    end
    local entry=light_settings_cache[path]
    if not entry then entry={value=read_mcm_value(path,default)};light_settings_cache[path]=entry end
    return entry.value
end

'''
    s=s[:pos]+wrapper+s[pos:];patches[name]=s

# Gate upstream temporary print diagnostics without changing their behavior or callbacks.
for n,s in patches.items():
    if n in ['adjustable_flashlight.script','utlf_ir_mode.script','ir_headlamp.script']:
        s=re.sub(r'(?<![\w.])printf\(', 'light_compat.trace(',s)
    write(WORK/'canonical'/n,s)

# Replaced custom state owners are retained as cheap GUI/legacy compatibility facades.
for root in [ONE,UNI]:
    for p in root.rglob('bling_situational.script'): p.unlink()
for p in ONE.rglob('one_key_lights_*_compat.script'): p.unlink()
# Canonical scripts are shipped in each core; optional upstream scripts stay optional.
for root,core in [(ONE,'Core'),(UNI,'core')]:
    for n in ['light_compat.script','light_backends.script','actor_effects.script','utlf_input.script','utlf_battery.script']:
        shutil.copyfile(WORK/'canonical'/n,root/core/'gamedata/scripts'/n)
for n in ['utlf_battery.script','utlf_items.script']:
    shutil.copyfile(WORK/'canonical'/n,UNI/'core/gamedata/scripts'/n)
for root in [ONE,UNI]:
    for n in ['utlf_ir_mode.script','ir_headlamp.script','adjustable_flashlight.script','zzz_bas_laser_control.script']:
        for p in root.rglob(n): shutil.copyfile(WORK/'canonical'/n,p)
# Unified IR dependencies used to be unconditional. Put them behind matching FOMOD options.
for n in ['utlf_ir_mode.script','utlf_ir_mode_ui.script']:
    p=UNI/'core/gamedata/scripts'/n
    if p.exists():
        target=UNI/'Compatibility/UTLF_IR/gamedata/scripts'/n;target.parent.mkdir(parents=True,exist_ok=True);shutil.move(p,target)
for p in (UNI/'core/gamedata/configs/ui').glob('*utlf_ir*'):
    target=UNI/'Compatibility/UTLF_IR/gamedata/configs/ui'/p.name;target.parent.mkdir(parents=True,exist_ok=True);shutil.move(p,target)
for p in (ONE/'Compatibility/Headlamp_IR/gamedata').rglob('*'):
    if p.is_file():
        target=UNI/'Compatibility/Headlamp_IR/gamedata'/p.relative_to(ONE/'Compatibility/Headlamp_IR/gamedata');target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
# Both packages use the same Native/Adjustable variants at the same install path.
for root,core in [(ONE,'Core'),(UNI,'core')]:
    p=root/core/'gamedata/scripts/adjustable_flashlight.script'
    if p.exists(): p.unlink()
    for backend in ['Native','Adjustable']:
        src=WORK/'native/adjustable_flashlight.script' if backend=='Native' else WORK/'canonical/adjustable_flashlight.script'
        if src.exists():
            dest=root/'HeadlampBackends'/backend/'gamedata/scripts/adjustable_flashlight.script';dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
for p in (WORK/'unified').glob('*.script'): shutil.copyfile(p,UNI/'core/gamedata/scripts'/p.name)
for p in (WORK/'onekey').glob('*.script'): shutil.copyfile(p,ONE/'Core/gamedata/scripts'/p.name)
print('Staged canonical patches and modules assembled. No live files changed.')
