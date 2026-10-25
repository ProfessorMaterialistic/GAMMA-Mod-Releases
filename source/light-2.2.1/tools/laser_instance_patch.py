"""Extend the existing Laser Settings save owner; no additional controller."""

def replace_once(source, old, new):
    assert source.count(old) == 1, old
    return source.replace(old, new, 1)

def patch(source):
    source = replace_once(source, 'local saved_lasers = {}', '''local saved_lasers = {}
-- Activation belongs to the weapon instance, while visual tuning stays by family.
-- Only loaded legacy IDs may inherit old family modes during migration. A new
-- ID visited by actor_on_update must not become eligible merely by being seen.
local legacy_lasers = {}
local light_intents = {}
function light_has_legacy(id) return legacy_lasers[id] ~= nil end
function light_read_intent(id, owner, field)
    local weapon = light_intents[id]
    local intent = weapon and weapon[owner]
    return intent and intent[field]
end
function light_write_intent(id, owner, field, value)
    if not id then return false end
    light_intents[id] = light_intents[id] or {}
    local weapon = light_intents[id]
    weapon[owner] = weapon[owner] or {}
    local changed = weapon[owner][field] ~= value
    weapon[owner][field] = value
    return changed
end''')
    start=source.index('local CloneWep = _G.alife_clone_weapon')
    end=source.index('local function clamp(',start)
    source=source[:start]+'''local CloneWep = _G.alife_clone_weapon
function _G.alife_clone_weapon(se_obj, section, parent_id)
    local old_id = se_obj.id
    -- Capture before cloning: destruction can unregister the old server object.
    local saved, legacy, intent = saved_lasers[old_id], legacy_lasers[old_id], light_intents[old_id]
    local new_wep = CloneWep(se_obj, section, parent_id)
    local new_id = new_wep and new_wep.id
    if new_id then
        saved_lasers[old_id], legacy_lasers[old_id], light_intents[old_id] = nil, nil, nil
        saved_lasers[new_id], legacy_lasers[new_id], light_intents[new_id] = saved, legacy, intent
    end
    return new_wep
end

-- Server unregister means destruction, unlike a client going offline. Prevent
-- recycled object IDs from inheriting a destroyed weapon's activation intent.
local function forget_laser(obj)
    saved_lasers[obj.id], legacy_lasers[obj.id], light_intents[obj.id] = nil, nil, nil
end

'''+source[end:]
    source=replace_once(source,'m_data.saved_lasers_id = saved_lasers','m_data.saved_lasers_id = saved_lasers\n\tm_data.light_laser_intents = light_intents')
    source=replace_once(source,'saved_lasers = m_data.saved_lasers_id or m_data.saved_lasers or {}','''saved_lasers = m_data.saved_lasers_id or m_data.saved_lasers or {}
    legacy_lasers = {}
    for id, value in pairs(saved_lasers) do legacy_lasers[id] = value end
    light_intents = m_data.light_laser_intents or {}''')
    source=replace_once(source,'RegisterScriptCallback("save_state", save_state)','RegisterScriptCallback("save_state", save_state)\n\tRegisterScriptCallback("server_object_on_unregister", forget_laser)')
    return source
