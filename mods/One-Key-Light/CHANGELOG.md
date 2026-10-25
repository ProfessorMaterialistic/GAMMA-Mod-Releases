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

## Previous releases

# 2.1.2 — October 19, 2026

- Keep weapon lights available through supported aim-start/end states.
- Preserve OFF/ON/AUTO, firing, UTLF 1.0.2, suspension and battery behavior.
- Promote the owner-accepted matched RC pair; no speculative headlamp change.

# 2.1.1 — October 14, 2026

- Official UTLF 1.0.2 compatibility: input/battery rebase, Unified item tuning
  rebase and obsolete White/IR replacement-call removal.
- Upstream HUD/light-pose ownership retained; previous firing fix, AUTO policies,
  family persistence, controls and installer choices preserved.
- Promoted owner-accepted RC with version-label/documentation changes only.
- Real clone attachment/battery transfer and universal beam/magnifier coverage
  remain documented limitations. Older release notes below are historical.

# Changes from 2.0 to 2.1.0

- Preserve weapon flashlight emission during idle, primary fire and secondary fire
  states. Semi-auto shots no longer trigger Light's OFF/detach/recreate cycle.
- Reconcile meaningful availability changes instead of each idle/fire transition.
  Generated UTLF IR activation/recovery uses the same firing availability gate.
- Owner reports all ten gameplay tests PASS, including laser ON/AUTO and concurrent
  flashlight/laser. No separate laser shader rewrite was needed or performed.
- Coordinated 2.1.0 MCM/GUI labels, FOMOD metadata, delivery docs and archive names.

Existing gestures, radial modes/themes, native MCM navigation, linking, IR fail-dark,
headlamp animations/sounds, power/battery behavior and AUTO policies are preserved.
Headlamps remain OFF/ON; weapon/laser AUTO remains conditional on capabilities.

Final distribution adds scoped license notices and portable corresponding source.
Runtime and asset bytes are unchanged from the accepted 2.1.0 review packages.

## Historical 2.0 record

# One Key Light changelog

## 2.0 - accepted development build; public release pending

- Tap / Double Tap / Hold and Quick Light Menu with independent standalone OFF/ON controls.
- Unified integration for supported AUTO modes and explicit shared NVG linking; gesture assignments do not silently change links.
- Native MCM Controls / Quick Menu / Anomaly Torch Binding / Compatibility pages.
- Binary headlamp behavior, existing animations and backend switch sounds without duplicate retry feedback.
- Configurable radial modes, themes/icons/labels, real battery/availability information and text fallback.
- Explicit persistent vanilla Torch clear/restore with conflict protection.

Owner acceptance recorded 2026-10-01; TESTED / FINAL-FOR-NOW applies to the accepted setup. Other configurations are not implicitly certified. No repository release or tag exists yet; earlier development/package labels are not public version history.

## 2026-10-04 documentation reconciliation

Verified unchanged tested runtime and installer choices; clarified dependency sources, update/removal and release hold. Showcase recording complete; Discord posting pending. No 2.0 tag, public archive or gameplay change.
