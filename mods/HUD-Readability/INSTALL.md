# Installation and updates

No 0.2.1 archive is published on this page. Do not use an older rc2 archive as a
0.2.1 installer: it predates the AURA texture repair.

For an existing maintained installation, close GAMMA and MO2, preserve the old
mod, and replace only its HUD Readability payload with the complete 0.2.1 payload.
Name it **HUD Readability 0.2.1**. Keep its existing effective priority, disable
older copies, and verify this mod wins conflicts for its own scripts and UI files.
Keep required GAMMA/BHS and MCM providers enabled. There is no FOMOD selection or
key-binding takeover. Open MCM → HUD Readability after launch.

Saved MCM identifiers are unchanged; there is no settings migration. Preserve
your existing settings. To uninstall, close GAMMA/MO2 and disable the mod. To roll
back, restore the preserved version at its former priority. No gameplay/save
values are owned by this addon; saved HUD configuration may remain in MCM.

If stamina is invisible, check opacity, saved position and the game HUD setting.
Drain stamina with the wearable lowered, or use Always Show Normal HUD to bypass
wearable handoff. A full meter fading out is expected. Confirm the owned bar
texture and descriptor are installed together, and that only one candidate wins.
