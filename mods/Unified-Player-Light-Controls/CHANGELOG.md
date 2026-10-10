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

**Publication held:** exact redistribution rights are unresolved. Local archive
preparation and gameplay acceptance do not establish a public release.

## Historical 2.0 record

# Unified Player Light Controls changelog

## 2.0 - accepted development build; public release pending

- Shared saved light modes and consistent control through native/device controls and optional One Key.
- Explicit Separate / NVG Linked weapon/headlamp routing with preserved independent tuning and fail-dark IR behavior.
- Weapon/laser AUTO policies; Normal/IR/linked headlamps remain OFF/ON.
- Retained supported tuning dialogs, per-family/attachment preferences, Apply All and laser reset/export.
- Existing headlamp animations/backend sound behavior, silent recovery and optional MGI launchers.
- Native MCM linking and compatibility/debug pages.

Owner acceptance recorded 2026-10-01; TESTED / FINAL-FOR-NOW applies to the accepted setup. Other configurations are not implicitly certified. No repository release or tag exists yet; earlier development/package labels are not public version history.

## 2026-10-04 documentation reconciliation

Verified unchanged tested runtime and installer choices; clarified dependency sources, update/removal and release hold. Showcase recording complete; Discord posting pending. No 2.0 tag, public archive or gameplay change.
