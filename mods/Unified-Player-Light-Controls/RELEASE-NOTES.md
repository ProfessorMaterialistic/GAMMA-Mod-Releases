# Light controls 2.2.0

Momentary Hold now keeps Tap and Double Tap available. Hold the key past the
existing Hold Threshold to activate temporary lighting; release to restore the
previous state. Only normal Hold on that modifier route is replaced. Choose
None to restore normal Hold. Short taps never briefly activate a temporary light.

## What's new

- Independent None / Alt / Ctrl / Shift routes, with grouped modifier controls.
- Separate Enable Alt Actions, Enable Ctrl Actions and Enable Shift Actions.
  Apply and reopen Controls to show or hide rows; disabled groups keep bindings.
- Clear device names: Headlamp and Weapon Light are linked actions. Explicit
  White Light and IR actions select a particular channel.
- Momentary Weapon Light, Weapon Light + Laser, Laser, White Light and IR choices.
  No temporary headlamp choices and no temporary entries in Tap/Double Tap lists.
- Existing ON/OFF sounds play once per changed device on momentary activation
  and normal release; holding the key does not repeat the sound.
- Quick Menu profiles, per-action visibility/order/icons, custom accent color,
  25 themes, existing animations, saved modes and native MCM Apply/Cancel.
- Retained per-weapon laser behavior and slot-change output bookkeeping fix.

Generic temporary weapon choices use White with NVGs up and IR with NVGs down,
without changing saved linking. Explicit White/IR choices retain their route.
Changing NVG state cancels the active hold; release and hold again to restart.
The combined choice uses the supported visible laser, not an IR laser.

Existing saved temporary Tap/Double bindings remain active until reassigned;
a help line identifies a legacy binding that is no longer offered in the list.
A newer explicit command takes precedence over restoring an older light state.

## Acceptance

The owner confirmed the matched rc.7 pair works correctly, including the sound
fix, on October 24, 2026. Version 2.2.0 preserves that gameplay code; promotion
changes version labels and release documentation only. The 90 focused Lua 5.1 /
LuaJIT checks also pass. This does not certify every engine, weapon or optional
configuration. No engine binary or complete dependency is bundled.

The earlier separate report of a permanently visible laser has no confirmed
renderer-level cause. The verified slot bookkeeping correction is retained;
the optional bounded laser diagnostic is off by default and never saved.
