"""Light-owned patches over official UTLF sources; no build or deployment side effects."""

def replace(source, old, new, count=1):
    assert source.count(old) >= count, old
    return source.replace(old, new, count)

def guard(source, declaration, key):
    return replace(source, declaration, declaration+'\n    -- LIGHT REBUILD: inhibit competing light handlers only in owned contexts.\n    if light_compat.owns_key('+key+') then return end')

def patch_input(s):
    s=replace(s,'local function toggle_light()','local function toggle_light()\n    local handled=light_compat.manual("utlf_visible")\n    if handled~=nil then return handled end')
    s=replace(s,'    local weapon, profile = utlf_core.active_supported_weapon()','    if not light_compat.module("utlf_core") then return false end\n    local weapon, profile = utlf_core.active_supported_weapon()')
    for event in ['press','release']:
        s=guard(s,'local function on_before_key_'+event+'(key, bind, dis, flags)','key')
    s=replace(s,'    wrap_engine_torch_toggle()\n\n    local settings','    if not light_compat.module("utlf_core") then return end\n    wrap_engine_torch_toggle()\n\n    local settings')
    s+='\n-- LIGHT REBUILD: direct entry and legacy alias.\nfunction oklc_toggle() return toggle_light() end\n'
    s+='\nfunction light_feedback(enabled) play_toggle_sound(enabled) end\n'
    s=s.replace('printf(','light_compat.trace(')

    return s

def patch_battery(s):
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
    s=replace(s,'function on_game_start()','function on_game_start()\n    if not light_compat.module("utlf_core") then return end')
    return s

def patch_items(s):
    s=replace(s,'min = 5, max = 80','min = 5, max = 200');s=replace(s,'min = 8, max = 90','min = 8, max = 120')

    return s
