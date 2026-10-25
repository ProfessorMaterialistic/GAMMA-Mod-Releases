"""Keep physical output bookkeeping on the existing Laser Settings setter path.

Shared by the upstream builder and the retained-baseline tactical builder.
No import-time writes; exact anchors reject unsupported source revisions.
"""


def patch(source):
    old = '''function on_slot_changed(new_slot, new_obj, prev_slot, prev_obj)
	last_laser_section = nil
	cached_param_6 = nil
	exec_console_cmd("shader_param_6 0, 0, 0, 0")
end'''
    assert source.count(old) == 1, 'Unsupported laser slot handler'
    source = source.replace(old, '''function on_slot_changed(new_slot, new_obj, prev_slot, prev_obj)
    -- Physical OFF must also update light_output. Keep saved weapon intent:
    -- the normal controller update restores the newly equipped weapon's mode.
    set_laser(0)
end''', 1)
    anchors = {
        'local function send_shader_params()': '''local function laser_trace(event, detail)
    local diagnostic=light_compat.module("light_laser_diagnostics")
    if diagnostic then diagnostic.sample(event, detail) end
end

local function send_shader_params()''',
        '\texec_console_cmd(cached_param_6)': '\texec_console_cmd(cached_param_6)\n    laser_trace("write", cached_param_6)',
        '\texec_console_cmd("shader_param_6 0, 0, 0, 0")': '\texec_console_cmd("shader_param_6 0, 0, 0, 0")\n    laser_trace("write", "shader_param_6 0, 0, 0, 0")',
        'function actor_on_update()': 'function actor_on_update()\n    laser_trace("update-before")',
        'function set_laser(on_off, section)': 'function set_laser(on_off, section)\n    laser_trace("setter", tostring(on_off)..":"..tostring(section))',
        'function light_set(id,enabled,manual)': 'function light_set(id,enabled,manual)\n    laser_trace("request", tostring(id)..":"..tostring(enabled)..":manual="..tostring(manual))',
    }
    for old, new in anchors.items():
        assert source.count(old) == 1, old
        source = source.replace(old, new, 1)
    return source
