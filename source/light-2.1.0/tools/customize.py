from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent))
from build import ROOT,WORK,ONE,UNI,read,write,reference,replace

s=reference('unified','bling_light_profiles.script')
s=replace(s,'local function read(k,d) local v=axr_main.config:r_value("mcm",k,2);if v==nil then return d end;return v end','local function read(k,d) return unified_light_store.get(k,d) end')
s=replace(s,'local function write(k,v) axr_main.config:w_value("mcm",k,v) end','local function write(k,v) unified_light_store.put(k,v) end')
s=replace(s,'function family(section)','local family_cache={}\nfunction invalidate() family_cache={} end\nlocal function resolve_family(section)')
pos=s.index('function get(mode,id,key,default)')
s=s[:pos]+'''function family(section)
    if not section then return end
    if family_cache[section]==nil then family_cache[section]=resolve_family(section) end
    return family_cache[section]
end
local values_cache={};local cache_generation=-1
'''+s[pos:]
s=replace(s,'function get(mode,id,key,default)','local function resolve(mode,id,key,default)')
s=replace(s,'write(p..key,v);axr_main.config:save();return v','return v')
pos=s.index('function put(mode,id,values,defaults)')
s=s[:pos]+'''function get(mode,id,key,default)
    if cache_generation~=unified_light_store.generation then values_cache={};cache_generation=unified_light_store.generation end
    local k=mode.."/"..tostring(id).."/"..key
    local entry=values_cache[k]
    if not entry then entry={value=resolve(mode,id,key,nil)};values_cache[k]=entry end
    return entry.value~=nil and entry.value or default
end
'''+s[pos:]
s=s.replace('function put(mode,id,values,defaults)','local function put_fields(mode,id,values,defaults)',1)
s=s.replace('    axr_main.config:save()','',1)
pos=s.index('function apply_all(mode,values)')
s=s[:pos]+'''function put(mode,id,values,defaults)
    return unified_light_store.edit(function() put_fields(mode,id,values,defaults) end)
end
'''+s[pos:]
s=s.replace('function apply_all(mode,values)','local function all_fields(mode,values)',1)
s=s.replace('write(p.."generation",read(p.."generation",0)+1);axr_main.config:save()','write(p.."generation",read(p.."generation",0)+1)',1)
pos=s.index('local hooked=false')
s=s[:pos]+'''function apply_all(mode,values)
    return unified_light_store.edit(function() all_fields(mode,values) end)
end
'''+s[pos:]
start=s.index('    ir.set_ir_settings=function');end=s.index('    hooked=true',start)
s=s[:start]+'''    ir.set_ir_settings=function(id,range,cone,brightness)
        if not id then return false end
        put("ir",id,{range=math.max(5,math.min(100,range)),cone_deg=math.max(8,math.min(120,cone)),brightness=math.max(.25,math.min(2,brightness))},old_get(family(id)))
        ir.apply_active_ir_settings();unified_lights.invalidate();return true
    end
    ir.reset_ir_settings=function(id,profile)
        if not id then return false end
        put("ir",id,{range=profile and profile.range or 30,cone_deg=profile and profile.cone_deg or 50,brightness=1,aim_policy=0})
        ir.apply_active_ir_settings();unified_lights.invalidate();return true
    end
'''+s[end:]
s=s.replace('function on_game_start() RegisterScriptCallback("actor_on_first_update",install_ir) end','function on_game_start() end')
write(UNI/'core/gamedata/scripts/bling_light_profiles.script',s)

s=reference('unified','bling_light_aim.script')
start=s.index('local installed=false');end=s.index('function snapshot(mode,c)')
s=s[:start]+'''function sync_enabled() return unified_lights.get_linked("weapon") end
function sync_available() return light_backends.installed("utlf_ir") end
function sync_update() return unified_lights.reconcile(nil,false) end
function toggle_sync() return unified_lights.set_linked("weapon",not sync_enabled()) end
function install() end
function on_game_start() end

'''+s[end:]
start=s.index('function battery_paused()');end=s.index('function sync_enabled()',start)
s=s[:start]+'''function battery_paused() return unified_lights.battery_paused() end
function update() return unified_lights.reconcile(nil,false) end
'''+s[end:]
write(UNI/'core/gamedata/scripts/bling_light_aim.script',s)

s=reference('unified','bling_player_lights.script')
s=s.replace('axr_main.config:r_value("mcm",path,2)','unified_light_store.get(path)',1)
start=s.index('local function write(path, value)');end=s.index('local function path(',start)
s=s[:start]+'''local function write(path,value)
    local id,key=string.match(path,"^bling_player_lights/weapon/([^/]+)/([^/]+)$")
    if id then bling_light_profiles.put("weapon",id,{[key]=value});return end
    unified_light_store.put(path,value)
end
'''+s[end:]
s=replace(s,'function set_preset(mode,id,index)','local function preset_fields(mode,id,index)')
pos=s.index('function next_preset(mode,id)')
s=s[:pos]+'''function set_preset(mode,id,index)
    unified_light_store.edit(function() preset_fields(mode,id,index) end)
    unified_lights.invalidate()
end
'''+s[pos:]
start=s.index('function set_weapon_enabled(enabled)');end=s.index('local function weapon_context()',start)
s=s[:start]+'''function set_weapon_enabled(enabled) return unified_lights.set_mode("utlf_visible",enabled and 1 or 0) end
'''+s[end:]
s=replace(s,'function normal_update()','local tuning_light,tuning_generation\nfunction normal_update()')
s=replace(s,'    local c=context(1)\n    if not c then return end','    if rawequal(tuning_light,s.light) and tuning_generation==unified_light_store.generation then return end\n    local c=context(1)\n    if not c then return end')
s=replace(s,'    local p=c.profile','    tuning_light=s.light;tuning_generation=unified_light_store.generation\n    local p=c.profile')
s=replace(s,'function save(c, values)','local function save_fields(c, values)')
start=s.index('function on_game_start()')
s=s[:start]+'''function save(c,values)
    local result=unified_light_store.edit(function() return save_fields(c,values) end)
    unified_lights.invalidate();return result
end
function on_game_start() end
'''
write(UNI/'core/gamedata/scripts/bling_player_lights.script',s)

# Laser profile hooks retained; collapse nested GUI edits to a single backing-store commit.
s=reference('unified','bling_laser_policy.script')
s=s.replace('axr_main.config:r_value("mcm","bling_laser_policy/"..bling_light_profiles.family(section),2)','unified_light_store.get("bling_laser_policy/"..bling_light_profiles.family(section))')
s=s.replace('    local logical={}\n    laser.bling_is_on=function(id) return logical[id]==true end\n','')
s=s.replace('        if weapon then logical[weapon:id()]=enabled~=0 end\n','')
# Original hide flags remain physical visibility controls, not implicit mode edits.
start=s.index('        local before=effective(section)');end=s.index('        return original_save(section,cfg)',start)
s=s[:start]+'        bling_light_profiles.put("laser",section,numeric(cfg,section),numeric(effective(section),section))\n'+s[end:]
s=s.replace('function apply_all(dialog)','local function apply_all_fields(dialog)',1)
pos=s.index('function allowed(')
s=s[:pos]+'''function apply_all(dialog)
    return unified_light_store.edit(function() return apply_all_fields(dialog) end)
end
'''+s[pos:]
s=s.replace('function on_game_start() RegisterScriptCallback("actor_on_first_update",install) end','function on_game_start() end')
s=s.replace('    laser.set_weapon_cfg=function(section,cfg)','    laser.set_weapon_cfg=function(section,cfg)\n        return unified_light_store.edit(function()')
s=s.replace('        return original_save(section,cfg)\n    end','        local result=original_save(section,cfg);unified_lights.invalidate();return result\n        end)\n    end')
s=s.replace('    laser.clear_weapon_cfg=function(section)','    laser.clear_weapon_cfg=function(section)\n        return unified_light_store.edit(function()')
s=s.replace('        return result\n    end\n    laser.get_weapon_cfg','        unified_lights.invalidate();return result\n        end)\n    end\n    laser.get_weapon_cfg')
write(UNI/'options/laser-settings/gamedata/scripts/bling_laser_policy.script',s)

# One Key MCM retains all existing options, using optional public capability queries.
s=reference('one','one_key_lights_mcm.script')
s=s.replace('    if old~=nil then return old end','    if old=="headlamp_situational" and (id=="tap" or id=="double" or id=="hold") then return "headlamp" end\n    if old~=nil then return old end',1)
s=s.replace('function on_mcm_load()','function on_mcm_load()\n    light_compat.install_mcm_layout()',1)
s=s.replace('defaults.indicator_style=1;','defaults.gesture_behavior=1;defaults.radial_labels=1;defaults.icon_style=1\nmenu_options.radial_labels=true;menu_options.icon_style=true\ndefaults.indicator_style=1;',1)
s=s.replace('    if ui then ui:Reset_last_opt() end','    light_compat.refresh_mcm(ui)',1)
start=s.index('    local controls={');end=s.index('    local menu={',start)
s=s[:start]+'''    local controls={
        {id="general",type="title",text="GENERAL"},
        option("enabled","check",1,{caption="Enable One Key Light"}),
        option("key","key_bind",2,{caption="Main Light Control Key"}),
        {id="linking",type="title",text="LIGHT LINKING"}
    }
    if light_compat.controller() then
        controls[#controls+1]=light_compat.mcm_link_option("weapon")
        controls[#controls+1]=light_compat.mcm_link_option("head")
        controls[#controls+1]=desc("link_help","NVG Linked automatically switches visible and IR lighting with your NVGs.")
    else
        controls[#controls+1]=desc("link_help","NVG Linked requires Unified Player Light Controls.")
    end
    controls[#controls+1]={id="gestures",type="title",text="GESTURES"}
    for _,entry in ipairs({{"tap","Tap Action"},{"double","Double Tap Action"},{"hold","Hold Action"}}) do
        local id=entry[1]
        controls[#controls+1]=option(id,"list",0,{caption=entry[2],content=content,no_str=true,
            curr={function()
                local value=axr_main.config:r_value("mcm",path(id),0)
                if value==nil then value=legacy_default(id,0) end
                return value=="headlamp_situational" and "headlamp" or value
            end},functor={function(value) ui_mcm.set(path(id),value) end}})
    end
    controls[#controls+1]=option("double_ms","track",2,{caption="Double Tap Window",min=100,max=500,step=25})
    controls[#controls+1]=option("hold_ms","track",2,{caption="Hold Threshold",min=150,max=1000,step=25})
    if light_compat.controller() then
        controls[#controls+1]=option("gesture_behavior","list",2,{caption="Gesture Behavior",content={{1,"Smart ON/OFF"},{2,"OFF -> ON -> AUTO"}},no_str=true})
    end
'''+s[end:]
s=s.replace('    menu[#menu+1]=option("menu_size"','''    menu[#menu+1]=option("radial_labels","list",2,{caption="Label Mode",content={{1,"Icon + Text"},{2,"Icon Only"},{3,"Text Only"}},no_str=true})
    menu[#menu+1]=option("icon_style","list",2,{caption="Icons",content={{1,"Tactical"},{2,"Minimal Icons"}},no_str=true})
    menu[#menu+1]=option("menu_size"''',1)
s=s.replace('{18,"Zombified"}', '{18,"Zombified"},{19,"GAMMA Default"},{20,"Minimal Dark"},{21,"PDA Green"},{22,"Amber Tactical"},{23,"NVG Green"},{24,"OLED"},{25,"Monochrome"}')
s=s.replace('MISSING (required)','Not installed (optional)')
s=s.replace('Single radial: click a weapon light to cycle OFF > ON > AUTO; the menu stays open. Release-to-select cycles once and closes. AUTO follows the saved aim rule. Headlamps and standalone lights keep their normal toggles. Movement uses your normal bindings; the mouse controls the menu. Detailed layouts use at least 200px.', 'Headlamps always toggle OFF / ON. With Unified, weapon lights and Laser can cycle OFF > ON > AUTO. A linked headlamp switches Normal / IR with NVG state. The two-step picker offers only supported modes. Movement uses your normal bindings; the mouse controls the menu. Icons use at least 220px.')
s=s.replace('Shortcuts force the beam ON/OFF; AUTO resumes saved aim rules.', 'Headlamps use OFF/ON. Weapon lights and Laser retain AUTO aim rules.')
s=s.replace('Headlamps use OFF/ON. Weapon lights and Laser retain AUTO aim rules. Optional linked pairs follow NVGs continuously: IR deployed, white stowed. OFF stays off. Separate controls and tuning remain available.', 'Linked Weapon Light: White with NVGs stowed, IR deployed; its ON/AUTO mode is retained. Linked Headlamp: Normal stowed, IR deployed; OFF keeps both off.')
start=s.index('    local binding={')
s=s[:start]+'''    -- Keep native controls and persisted option paths; group the existing rows only.
    local by_id={};for _,opt in ipairs(menu) do by_id[opt.id]=opt end
    local organized={}
    local groups={
        {"QUICK MENU",{"menu_key","menu_selection","shortcut","modifier","radial_behavior","right_click","allow_movement","hide_bound"}},
        {"APPEARANCE",{"radial_theme","menu_size","menu_opacity"}},
        {"ICONS & LABELS",{"radial_labels","icon_style","indicator_style","show_battery","show_locks","battery_color"}}
    }
    for index,group in ipairs(groups) do
        organized[#organized+1]={id="section_"..index,type="title",text=group[1]}
        for _,id in ipairs(group[2]) do organized[#organized+1]=assert(by_id[id]) end
    end
    for _,opt in ipairs(menu) do if opt.id:find("^show_") and opt.id~="show_battery" and opt.id~="show_locks" then organized[#organized+1]=opt end end
    menu=organized
    local binding={
        {id="title",type="title",text="ANOMALY TORCH BINDING"},
        desc("help","Use this if One Key Light replaces your normal Anomaly torch key."),
        {id="clear",type="button",caption="Clear Vanilla Torch Binding",functor_ui={clear_binding}},
        {id="restore",type="button",caption="Restore Vanilla Torch Binding",functor_ui={restore_binding}},
        {id="status",type="desc",text="",ui_hook_functor={function(anchor,handlers)
            if handlers and handlers.desc then
                handlers.desc:SetText(one_key_lights_bindings.status())
                handlers.desc:AdjustHeightToText()
                handlers.desc:SetWndSize(vector2():set(handlers.desc:GetWidth(),handlers.desc:GetHeight()+20))
            end
        end}}
    }
    local compatibility=light_compat.mcm_integrations()
    local sections={}
    for _,section in ipairs({{"controls","Controls",controls},{"menu","Quick Menu",menu},{"bindings","Anomaly Torch Binding",binding},{"compatibility","Compatibility",compatibility}}) do
        sections[#sections+1]={id=section[1],text="ui_mcm_one_key_lights_section_"..section[1],sh=true,gr=section[3]}
    end
    return {id="one_key_lights",text="ui_mcm_menu_one_key_lights",gr=sections}
end
'''
write(ONE/'Core/gamedata/scripts/one_key_lights_mcm.script',s)

s=reference('one','one_key_lights_theme.script')
pos=s.index('function get(index)')
s=s[:pos]+'''-- Universal additions preserve all legacy theme indices.
local universal={
 {{28,30,24},{82,89,51},{229,224,196},{175,179,154},{126,235,96},{255,190,64},{133,142,120}},
 {{14,16,19},{47,53,60},{235,240,245},{162,173,186},{106,238,164},{246,191,92},{118,128,140}},
 {{8,25,14},{25,77,43},{175,239,165},{108,169,104},{167,255,113},{247,216,105},{84,132,82}},
 {{23,17,8},{83,61,23},{245,207,131},{185,154,95},{251,211,107},{255,170,51},{137,112,68}},
 {{3,19,4},{13,61,14},{145,245,139},{78,162,73},{156,255,125},{223,247,97},{55,109,52}},
 {{0,0,0},{26,30,33},{244,249,250},{155,170,174},{91,244,165},{250,192,71},{99,116,122}},
 {{12,12,12},{54,54,54},{245,245,245},{173,173,173},{255,255,255},{201,201,201},{96,96,96}},
}
for _,p in ipairs(universal) do presets[#presets+1]={bg=p[1],hover=p[2],text=p[3],muted=p[4],on=p[5],auto=p[6],off=p[7]} end
function count() return #presets end
'''+s[pos:]
write(ONE/'Core/gamedata/scripts/one_key_lights_theme.script',s)

# Headlamp GUIs use the same mode API and animate manual ON/OFF.
for name,id in [('adjustable_flashlight_ui.script','headlamp'),('ir_headlamp_ui.script','headlamp_ir')]:
    p=UNI/'core/gamedata/scripts'/name if id=='headlamp' else UNI/'Compatibility/Headlamp_IR/gamedata/scripts'/name
    s=reference('unified',name) if id=='headlamp' else read(p)
    if id=='headlamp':
        s=s.replace('adjustable_flashlight.set_enabled(requested)','unified_lights.set_mode("headlamp",requested and 1 or 0)')
        s=s.replace('adjustable_flashlight.set_enabled(false)','unified_lights.set_mode("headlamp",0)')
    else:
        s=s.replace('ir_headlamp.set_ir_enabled(requested)','unified_lights.set_mode("headlamp_ir",requested and 1 or 0)')
        s=s.replace('ir_headlamp.set_ir_enabled(false)','unified_lights.set_mode("headlamp_ir",0)')
    write(p,s)

print('Custom facades, cached profiles, transactional tuning, MCM and themes assembled.')

# Clean optional IR GUI is canonical in both packages. Add modes through optional API only.
s=read(ROOT/'mods/Soys_IR_Headlamps_v1.3.0/gamedata/scripts/ir_headlamp_ui.script')
s=s.replace('    self:InitCallbacks()','''    self:InitCallbacks()
    local controls=light_compat.module("bling_light_control")
    if controls then controls.init(self,self.back,"headlamp_ir",188) end''',1)
s=s.replace('    self.chk_ir = xml:InitCheck("chk_ir_enabled", self.back)','''    self.chk_ir = xml:InitCheck("chk_ir_enabled", self.back)
    if light_compat.controller() then lbl_ir:Show(false);self.chk_ir:Show(false) end''',1)
s=s.replace('        set_mcm("ir_headlamp/auto_sync", requested_sync)','        if api then api.set_linked("head",requested_sync) else set_mcm("ir_headlamp/auto_sync", requested_sync) end',1)
s=s.replace('    self.chk_sync:SetCheck(status.auto_sync)','    local sync_state=status.auto_sync;if api then sync_state=api.get_linked("head") end\n    self.chk_sync:SetCheck(sync_state)',1)
s=s.replace('    if requested_sync ~= status.auto_sync then','    local sync_state=status.auto_sync;if api then sync_state=api.get_linked("head") end\n    if requested_sync ~= sync_state then',1)
s=s.replace('    ir_headlamp.set_ir_enabled(false)','    local api=light_compat.controller()\n    if api then api.set_mode("headlamp_ir",0) else ir_headlamp.set_ir_enabled(false) end',1)
s=s.replace('    set_mcm("ir_headlamp/auto_sync", true)', '    local api=light_compat.controller()\n    if api then api.set_linked("head",true) else set_mcm("ir_headlamp/auto_sync",true) end',1)
s=s.replace('    self.chk_ir:SetCheck(status.enabled)','''    local api=light_compat.controller()
    local intent=api and api.get_mode("headlamp_ir") or (status.enabled and 1 or 0)
    self.chk_ir:SetCheck(intent~=0);self.last_ir=intent~=0
    if self.light_modes then bling_light_control.refresh(self,"headlamp_ir") end''',1)
s=s.replace('    if requested_ir ~= status.enabled then\n        ir_headlamp.set_ir_enabled(requested_ir)','''    local api=light_compat.controller()
    if requested_ir ~= self.last_ir then
        if api then api.set_mode("headlamp_ir",requested_ir and 1 or 0)
        else ir_headlamp.set_ir_enabled(requested_ir) end''',1)
s=s.replace('local function get_mcm(path, default)','''local function get_mcm(path, default)
    local store=light_compat.module("unified_light_store")
    if store then return store.get(path,default,type(default)=="boolean" and 1 or 2) end''',1)
s=s.replace('local function set_mcm(path, value)','''local function set_mcm(path, value)
    local store=light_compat.module("unified_light_store")
    if store then store.put(path,value);return true end
    light_compat.settings_generation=light_compat.settings_generation+1''',1)
# Wrap one GUI update/reset as one transaction; standalone uses upstream MCM.
for method in ['Update','Reset']:
    decl='function IRHeadlampDialog:'+method+'()'
    s=s.replace(decl,decl.replace(method,'_'+method),1)
    s+='''
function IRHeadlampDialog:'''+method+'''()
    local store=light_compat.module("unified_light_store")
    if store then return store.edit(function() return self:_'''+method+'''() end) end
    return self:_'''+method+'''()
end
'''
for root in [ONE,UNI]:write(root/'Compatibility/Headlamp_IR/gamedata/scripts/ir_headlamp_ui.script',s)
# Both optional IR GUIs use their own dependency assets; One Key never requires Unified UI assets.
for p in (ROOT/'mods/Soys_IR_Headlamps_v1.3.0/gamedata/configs/ui').glob('ui_ir_headlamp*.xml'):
    for root in [ONE,UNI]:write(root/'Compatibility/Headlamp_IR/gamedata/configs/ui'/p.name,read(p))

s=read(UNI/'core/gamedata/scripts/adjustable_flashlight_ui.script')
s=s.replace('    self:InitCallbacks()','''    self:InitCallbacks()
    self.lbl_enabled:Show(false);self.chk_enabled:Show(false)
    bling_light_control.init(self,self.back,"headlamp",134)''',1)
s=s.replace('    local linked=bling_situational and bling_situational.linked("head")','    bling_light_control.refresh(self,"headlamp")\n    local linked=bling_situational and bling_situational.linked("head")',1)
s=s.replace('    self.last_enabled=linked and bling_situational.state("head")~=0 or not linked and status.enabled','    self.last_enabled=unified_lights.get_mode("headlamp")~=0\n    self.chk_enabled:SetCheck(self.last_enabled)\n    local adjustable=adjustable_flashlight.oklc_backend_name=="Soy Adjustable Headlamps"\n    self.track_brightness:Enable(adjustable);self.track_range:Enable(adjustable);self.track_beam:Enable(adjustable)')
start=s.index('local function get_mcm(path, default)');end=s.index('local function set_mcm(path, value)',start)
s=s[:start]+'''local function get_mcm(path,default)
    return unified_light_store.get(path,default,type(default)=="boolean" and 1 or 2)
end
'''+s[end:]
start=s.index('local function set_mcm(path, value)');end=s.index('local function different(',start)
s=s[:start]+'''local function set_mcm(path,value) unified_light_store.put(path,value);return true end
'''+s[end:]
for method in ['Update','Reset']:
    decl='function AdjustableFlashlightDialog:'+method+'()';s=s.replace(decl,decl.replace(method,'_'+method),1)
    s+='\nfunction AdjustableFlashlightDialog:'+method+'() return unified_light_store.edit(function() return self:_'+method+'() end) end\n'
write(UNI/'core/gamedata/scripts/adjustable_flashlight_ui.script',s)

# Delayed MGI discovery retries once per second in the unified coordinator.
p=UNI/'core/gamedata/scripts/bling_nvg_mgi.script';s=reference('unified','bling_nvg_mgi.script')
s=s.replace('function on_game_start()','local registered=false\nfunction register()\n    if registered then return end',1)
s=s.replace('        MGI.register_gui','        registered=MGI.register_gui',1)
s=s.replace('    if not MGI or not MGI.register_gui then return end','    local MGI=light_compat.module("mgi") or light_compat.module("MGI")\n    if not MGI or not MGI.register_gui then return end',1)
s+='\nfunction on_game_start() end\n';s=s.replace('version="1.3"','version="2.1.0"');write(p,s)
p=UNI/'options/laser-settings/gamedata/scripts/bling_laser_mgi.script';s=reference('unified','bling_laser_mgi.script')
s=s.replace('function on_game_start()','local registered=false\nfunction register()\n    if registered then return end',1).replace('    MGI.register_gui','    registered=MGI.register_gui',1)
s=s.replace('    if not MGI or type(MGI.register_gui)', '    local MGI=light_compat.module("mgi") or light_compat.module("MGI")\n    if not MGI or type(MGI.register_gui)',1)
s+='\nfunction on_game_start() end\n';s=s.replace('version="1.3"','version="2.1.0"');write(p,s)

# UI diagnostics are disabled by the same release debug sink.
p=UNI/'Compatibility/UTLF_IR/gamedata/scripts/utlf_ir_mode_ui.script'
s=read(p).replace('printf(','light_compat.trace(');write(p,s)
