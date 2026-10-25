"""Bounded patches to retained 2.1.3 generated facades. No import-time writes."""


def replace(source, old, new):
    assert source.count(old) == 1, old
    return source.replace(old, new, 1)


def laser(source):
    from laser_output_patch import patch
    source = patch(source)
    source = replace(source, 'local saved_lasers = {}', '''local saved_lasers = {}
-- Temporary output is separate from the existing save owner and instance modes.
local function tactical_mode(id)
    local tactical=light_compat.module("light_tactical")
    local weapon=light_backends.weapon()
    if tactical and weapon and weapon:id()==id then return tactical.mode("laser") end
end
local function effective_request(id)
    local temporary=tactical_mode(id)
    if temporary~=nil then return temporary~=0 end
    return saved_lasers[id]==true
end
function light_tactical_clear()
    local weapon=light_backends.weapon()
    set_laser(weapon and saved_lasers[weapon:id()] and 1 or 0,weapon and weapon:section())
end''')
    source = replace(source, 'if wpn_id and saved_lasers[wpn_id] ~= nil then', 'if wpn_id and (saved_lasers[wpn_id] ~= nil or tactical_mode(wpn_id)~=nil) then')
    source = replace(source, 'set_laser(saved_lasers[wpn_id] and 1 or 0, section)', 'set_laser(effective_request(wpn_id) and 1 or 0, section)')
    source = replace(source, '    saved_lasers[id]=enabled', '    if tactical_mode(id)==nil then saved_lasers[id]=enabled end')
    source = replace(source, 'function oklc_is_on(id) return saved_lasers[id]==true end', 'function oklc_is_on(id) return effective_request(id) end')
    return source


def menu(source):
    source = replace(source, 'self.theme=one_key_lights_theme.get(cfg.radial_theme)', 'self.theme=one_key_lights_radial.palette(one_key_lights_theme.get(cfg.radial_theme),cfg)')
    source = replace(source, '    if target then self.items=', '    self.items=one_key_lights_radial.arrange(self.items,cfg)\n    if target then self.items=')
    source = replace(source, 'one_key_lights_icons.action(self.items[i].id)', 'one_key_lights_radial.icon(self.items[i].id,cfg)')
    source = replace(source, '    if not actor_menu.is_hud_free() then return end', '    if not actor_menu.is_hud_free() then return end\n    local tactical=light_compat.module("light_tactical");if tactical then tactical.cancel("radial opened") end')
    return source


def mcm(source):
    # The linked-headlamp alias is an explicit choice again. Display its existing
    # saved ID without rewriting it; runtime alias/link behavior stays unchanged.
    source = replace(source, '    if old=="headlamp_situational" and (id=="tap" or id=="double" or id=="hold") then return "headlamp" end\n', '')
    source = replace(source, 'return value=="headlamp_situational" and "headlamp" or value', 'return value')
    source = replace(source, '        return o\n', '''        local short_press=id=="tap" or id=="double" or id:find("_tap$") or id:find("_double$")
        if short_press and o.content then
            local persistent={}
            for _,entry in ipairs(o.content) do
                if not light_tactical.known(entry[1]) then persistent[#persistent+1]=entry end
            end
            o.content=persistent
        end
        -- Retain an already-saved tactical choice when its hardware is absent.
        -- New unsupported choices are not offered, and activation still fails closed.
        if kind=="list" and val==0 and o.content then
            local saved=axr_main.config:r_value("mcm",path(id),0)
            if saved==nil then saved=legacy_default(id,0) end
            if saved=="headlamp_situational" or saved=="weapon_situational" then
                local found=false;for _,entry in ipairs(o.content) do if entry[1]==saved then found=true end end
                if not found then
                    local choices={};for _,entry in ipairs(o.content) do choices[#choices+1]=entry end
                    choices[#choices+1]={saved,light_compat.action_name(saved).." (link unavailable)"};o.content=choices
                end
            end
            if not short_press and not id:find("^momentary_") and saved and light_tactical.known(saved) and not light_tactical.available(saved) then
                local choices={};for _,entry in ipairs(o.content) do choices[#choices+1]=entry end
                local name=id:find("^momentary_") and light_tactical.momentary_label(saved) or light_tactical.label(saved)
                choices[#choices+1]={saved,name.." (unavailable)"};o.content=choices
            end
        end
        return o
''')
    source = replace(source, 'function path(id)', '''defaults.matrix_enabled=false
for _,modifier in ipairs({"alt","ctrl","shift"}) do defaults["enable_"..modifier]=false end
for _,modifier in ipairs({"none","alt","ctrl","shift"}) do
    defaults["momentary_"..modifier]="none"
    if modifier~="none" then
        for _,gesture in ipairs({"tap","double","hold"}) do defaults[modifier.."_"..gesture]="none" end
    end
end
defaults.custom_accent=false;defaults.accent_r=70;defaults.accent_g=160;defaults.accent_b=110;defaults.radial_profile=1
for _,id in ipairs({"custom_accent","accent_r","accent_g","accent_b","radial_profile"}) do menu_options[id]=true end
for index,id in ipairs(one_key_lights_radial.actions) do
    defaults["show_"..id]=index<=5;defaults["position_"..id]=index;defaults["icon_"..id]="default"
    for _,prefix in ipairs({"show_","position_","icon_"}) do menu_options[prefix..id]=true end
end
function modifier_enabled(name)
    local saved=axr_main.config:r_value("mcm","one_key_lights/controls/enable_"..name,1)
    if saved~=nil then return saved==true end
    -- Read-through migration, never a save write: keep prior enabled routes.
    local matrix=axr_main.config:r_value("mcm","one_key_lights/controls/matrix_enabled",1)
    local momentary=axr_main.config:r_value("mcm","one_key_lights/controls/momentary_"..name,0)
    return matrix==true or (momentary~=nil and momentary~="none")
end
function path(id)''')
    source = replace(source, 'function legacy_default(id,kind)', '''function legacy_default(id,kind)
    local modifier=id:match("^enable_(.+)$")
    if modifier then return modifier_enabled(modifier) end''')
    source = replace(source, '    local menu={', '''    controls[#controls+1]=option("matrix_enabled","check",1,{caption="Enable modifier gesture matrix"})
    controls[#controls+1]=desc("matrix_help","Momentary Hold replaces only Hold at the Hold Threshold. Tap and Double Tap remain available. Multiple modifiers cancel.")
    for _,modifier in ipairs({"none","alt","ctrl","shift"}) do
        if modifier~="none" then
            controls[#controls+1]=option("enable_"..modifier,"check",1,{caption="Enable "..modifier.." Actions"})
            for _,gesture in ipairs({"tap","double","hold"}) do
                controls[#controls+1]=option(modifier.."_"..gesture,"list",0,{caption=modifier.." / "..gesture,content=content,no_str=true})
            end
        end
        local temporary={{"none","None"}}
        for _,entry in ipairs(light_tactical.choices(true)) do temporary[#temporary+1]={entry.id,entry.name} end
        controls[#controls+1]=option("momentary_"..modifier,"list",0,{caption=modifier.." / Momentary Hold",content=temporary,no_str=true})
    end
    controls[#controls+1]={id="conflicts",type="desc",text="",ui_hook_functor={function(anchor,handlers)
        if handlers and handlers.desc then
            local current={};for id,default in pairs(defaults) do local v=ui_mcm.get(path(id));if v==nil then v=default end;current[id]=v end
            local lines=one_key_lights_matrix.conflicts(current)
            handlers.desc:SetText(#lines>0 and table.concat(lines,"\\n") or "No overlapping Light bindings. Use one modifier at a time.")
        end
    end}}
    local menu={''')
    # Do not let dynamic capability discovery overwrite saved/default visibility.
    source = replace(source, 'defaults[id]=true; menu_options[id]=true;', 'if defaults[id]==nil then defaults[id]=true end; menu_options[id]=true;')
    source = replace(source, '    local binding={', '''    menu[#menu+1]={id="customization",type="title",text="SECTOR POSITIONS AND PROFILES"}
    menu[#menu+1]=desc("position_help","Lower position numbers appear first, clockwise from the top. Ties keep device order. The first five visible actions fit the existing radial; hide or move others to make room. Linked devices use the white device position/icon. CQB actions require equipped hardware. IR laser requires an explicit IR-capable backend.")
    local icons={{"default","Automatic"},{"weapon_light","White beam"},{"weapon_ir","IR beam"},{"headlamp","Headlamp"},{"laser","Laser reticle"},{"nvg","NVG goggles"},{"linked","Linked devices"},{"auto","AUTO"}}
    for _,id in ipairs(one_key_lights_radial.actions) do
        if id:find("^cqb_") or id=="momentary_laser" then
            menu[#menu+1]=option("show_"..id,"check",1,{caption="Show "..one_key_lights_radial.label(id)})
        end
        menu[#menu+1]=option("position_"..id,"track",2,{caption=one_key_lights_radial.label(id).." / Position",min=1,max=10,step=1})
        menu[#menu+1]=option("icon_"..id,"list",0,{caption=one_key_lights_radial.label(id).." / Icon",content=icons,no_str=true})
    end
    menu[#menu+1]=option("custom_accent","check",1,{caption="Custom accent color"})
    for _,channel in ipairs({"r","g","b"}) do menu[#menu+1]=option("accent_"..channel,"track",2,{caption="Accent "..channel,min=0,max=255,step=5}) end
    menu[#menu+1]=option("radial_profile","list",2,{caption="Saved configuration",content={{1,"Configuration 1"},{2,"Configuration 2"},{3,"Configuration 3"}},no_str=true})
    menu[#menu+1]={id="save_profile",type="button",caption="Save radial configuration",functor_ui={function(ui)
        one_key_lights_radial.save_profile(one_key_lights_radial.profile_slot(ui),ui);refresh_status(ui)
    end}}
    menu[#menu+1]={id="load_profile",type="button",caption="Load radial configuration",functor_ui={function(ui)
        one_key_lights_radial.load_profile(one_key_lights_radial.profile_slot(ui),ui);refresh_status(ui)
    end}}
    local binding={''')
    source = replace(source, '    local compatibility=light_compat.mcm_integrations()',
        '    controls,menu,binding=one_key_lights_presentation.organize(controls,menu,binding)\n    local compatibility=light_compat.mcm_integrations()')
    return source
