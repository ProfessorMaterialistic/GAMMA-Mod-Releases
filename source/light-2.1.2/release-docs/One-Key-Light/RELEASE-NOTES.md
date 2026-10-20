# One Key Light 2.1.2 — October 19, 2026

One-key Tap / Double Tap / Hold controls and a radial quick menu for your
installed lights. Works independently; add Unified for AUTO and NVG linking.

## Changes since 2.1.1

- Fix a weapon-light shutdown when entering or leaving ADS on supported weapons
  that use aim-transition animation states. Explicit ON remains requested ON
  through those states instead of detaching and recreating the emitter.
- Preserve OFF and AUTO policies, the earlier semi-auto firing fix, official
  UTLF 1.0.2 compatibility, genuine HUD suspension and battery handling.
- Both packages include the same corrected backend. Update both if you use them
  together. Each still works independently.
- No new keybinds, settings reset, engine changes or dependency update.

## Testing and remaining limits

The owner confirmed the installed matched 2.1.2-rc.1 pair works in game.
Stable 2.1.2 preserves those gameplay bytes; only version labels and release
documentation change. Offline validation passed 43 regression groups, including
144 ADS cases, 96 firing cases, 48 laser cases and 256 headlamp action checks.
All 49 packaged scripts compile under Lua 5.1 and LuaJIT 2.1.

This is acceptance of the tested setup, not a separate result for every weapon,
attachment, magnifier or backend. Headlamp reactivation was not reproduced or
causally attributed, so this release does not claim a specific headlamp fix.
If it returns, provide video/log evidence with the triggering action, light mode,
weapon/attachments and installed headlamp/animation integrations.

Real attachment-clone/battery transfer, every magnifier variant and universal
rendered-beam continuity remain unverified. A blocked or moved beam can have a
different cause from the corrected logical shutdown.

Install with MO2; see INSTALL.md. Original MichaelHochriegl/UTLF, GAMMA,
Soy and Borksy attribution and license notices are retained.
