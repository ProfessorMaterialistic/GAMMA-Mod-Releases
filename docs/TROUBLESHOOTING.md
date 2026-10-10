# Troubleshooting

[Home](../README.md) · [One Key](../mods/One-Key-Light/README.md) · [Unified](../mods/Unified-Player-Light-Controls/README.md)

| Symptom | Check / action |
| --- | --- |
| Finding the archive | Open the mod's [GitHub Release](MOD-INDEX.md), expand Assets and select its named v2.1.0 .7z. The source zip/tar.gz is for development, not the MO2 installer. |
| Light MCM page absent / old labels | Enable the intended 2.1.0 entry; disable the older provider; verify its files win MO2 conflicts; check MCM and exact engine identity. |
| UTLF action absent / no weapon light | Install UTLF 1.0.1 and supported weapon registration/attachment; select matching optional IR bridge if using IR; check Compatibility detection and battery/equipment. |
| Laser unavailable | Install Laser Settings 2.7 separately, select its FOMOD integration with compatible BaS/laser support and use a laser-capable weapon. |
| IR unavailable | Check the corresponding Soy dependency, FOMOD choice, deployed NVGs and, for IR headlamps, the NVG illuminator module. |
| Linked lights stay dark under NVGs | Expected when selected IR cannot emit. Restore appropriate equipment/power; do not assume white fallback. Verify both shared linking selectors and Apply. |
| Headlamp never offers AUTO | Expected: Normal, IR and linked headlamps are OFF/ON only. |
| Native headlamp sliders do nothing | Native/G2X beam tuning uses its separate presets; Soy-style sliders cannot tune the native emitter. |
| Tap feels delayed | The single tap waits for the Double Tap Window (default 225 ms). Adjust timing in Controls. |
| Gesture toggles a different device | Check saved Tap/Double Tap/Hold assignments; gestures do not themselves enable linking. |
| Two actions fire on one key | Review vanilla Torch and upstream bindings. Use One Key's explicit Clear Torch function if replacing Torch; do not erase unrelated bindings. Verify patched input files win. |
| Torch reappears after removal | Restore Torch through One Key before disabling it. If already removed, re-enable the matching version to Restore; inspect its status/conflict message. |
| Restore refuses a key | A saved key now belongs to another command or Torch was rebound. Free the conflict in Controls, then retry Restore. |
| Icons missing | Text fallback is supported; try Text Only. Verify the correct UI/atlas files win conflicts. |
| Link state differs between pages | Apply pending MCM edits; verify matching companions/backend/options and shared compatibility files. Reset/Cancel do not commit pending edits. |
| Crash / unexpected animation or sound | Record exact versions, steps and sanitized log excerpt before changing candidates. Do not infer a cause from an unsymbolized native error alone. |

For a reproducible issue, [open a bug report](https://github.com/ProfessorMaterialistic/GAMMA-Mod-Releases/issues/new/choose) with mod version, GAMMA/Anomaly, exact engine/date/core/executable, dependency versions, MO2 file priority, expected/actual behavior and new/current-save context. Sanitize paths, usernames, tokens and unrelated private information from screenshots/log excerpts. Do not upload full profiles, saves or backup archives unless separately requested and approved.

Accepted setup documentation does not promise every dependency/engine update. Keep old entries and your own settings recovery material while investigating; do not replace engine files by guesswork.
