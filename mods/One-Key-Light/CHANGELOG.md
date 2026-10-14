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
