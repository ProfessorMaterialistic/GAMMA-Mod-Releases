# Light controls 2.2.1

Weapon lights now stay available during reloads, inspection, misfire clearing and
supported fire-mode/launcher switching. These in-hand animations previously could
briefly detach the light and recreate it afterward.

Inventory/PDA keeps the light where the same equipped weapon and attachment remain
valid. Actual holstering or replacement with a non-weapon HUD item still uses the
framework's normal suspension and recovery. Fully holstered illumination is not
introduced. AUTO still follows its aiming policy; OFF stays OFF.

All 2.2.0 controls are retained: Tap, Double Tap, Hold, Momentary Hold, modifiers,
radial profiles/themes, NVG linking, saved modes and existing sounds/animations.
Laser controller, SSS settings, shader behavior and existing laser fixes are unchanged.
This update does not claim to fix a separately reported laser-not-turning-on issue.

The owner confirmed the installed matched 2.2.1-rc.1 pair works correctly on
October 25, 2026. Stable 2.2.1 changes version labels and documentation only.
112 focused Lua 5.1/LuaJIT checks passed on the candidate. Other weapon/engine
combinations are not universally certified.

If using both Light mods, update both to 2.2.1 and keep matching installer choices.
Save and close the game/MO2 before updating. Keep your existing settings, bindings
and a pre-update save. No new game or settings reset is required by this patch.
