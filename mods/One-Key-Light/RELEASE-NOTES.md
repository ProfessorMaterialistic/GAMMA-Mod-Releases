# Light controls 2.2.2

Fixes light commands being ignored while a disabled modifier is held, such as
Shift for sprinting. Normal Tap, Double Tap, Hold and Momentary Hold now remain
available. Explicitly enabled modifier bindings still take priority, including
actions set to None. Saved settings and bindings are preserved.

MCM now includes a short sprinting note: disable Shift Actions to use your normal
controls while holding Shift. If Shift is also your active Quick Menu shortcut,
change its modifier or disable that shortcut. The existing shortcut remains
available when all modifier action groups are disabled.

Retains 2.2.1 reload/animation continuity, headlamp animations, sounds, laser fixes,
NVG linking and temporary-state restoration. No laser/SSS or engine changes.
Unified is provided as a matched 2.2.2 package; its gameplay scripts are unchanged.

Validation: 156 automated Lua 5.1/LuaJIT checks passed on the sprint-fix candidate.
The final MCM help and stable packages pass additional focused checks. The owner
authorized publication; the sprint fix has NOT yet been verified in-game.

## Updating

Save and close GAMMA/MO2. Install the new archives as separate mods, retaining
the previous pair for rollback. If using both mods, update both to 2.2.2 and keep
matching FOMOD backend/integration choices and existing load-order positions.
Select only installed integrations. Keep your settings; no new game/reset needed.
Requirements, credits and licenses are unchanged. Full installation details:
https://github.com/ProfessorMaterialistic/GAMMA-Mod-Releases/tree/main/mods

Check light gestures and the quick menu while sprinting, then Momentary Hold
release/cancel, NVG linking, headlamp animation, clicks and reload continuity.
To roll back, close the game/MO2, disable the new pair and re-enable the old pair.
