# Unified Player Light Controls 2.1.1 — October 14, 2026

Authoritative OFF / ON / AUTO for supported tactical White/IR lights and lasers,
configurable normal/alternate ADS policies, weapon-family persistence and
NVG linking. Native and IR headlamps remain OFF/ON. One Key is optional.

## Changes since 2.1.0

- Support official Universal Tactical Light Framework v1.0.2, commit
  `d8c89c385ece3fbfd10e50c054b4618bc3f09d38`.
- Rebase bundled input/battery patches and Unified item tuning onto v1.0.2.
  Preserve authoritative AUTO intent, battery pause and existing tuning limits.
- Remove obsolete White/IR replacement-state calls; retain upstream HUD/world
  beam positioning and PDA/quick-melee lifecycle ownership.
- Preserve existing firing fixes, gestures, themes, settings, animations,
  sounds and weapon-family normalization. No new feature or engine change.

## Acceptance and limitations

The owner confirmed the exact matched 2.1.1-rc.1 pair works in game with UTLF
1.0.2. Stable promotion changes metadata/docs only; runtime differs solely in
five version-label members across the pair. Local validation passed 33 groups,
49 Lua 5.1 compilations, 96 firing cases and 48 laser-policy cases.

This is qualitative owner acceptance, not a separately recorded PASS for every
weapon or installation option. Real object-clone module/battery transfer,
rendered beam continuity and all magnifier variants are not universally verified.
Bone-based flips preserve the object; a clone fallback creates a new weapon.
Existing family intent persists, but cannot recreate an attachment lost by the
clone. These limitations are accepted for release and remain documented.

Install with MO2, matching companion FOMOD choices and dependencies listed in
COMPATIBILITY.md. Keep prior archives/folders for rollback. See INSTALL.md.
MichaelHochriegl owns UTLF and its v1.0.2 improvements; Bling's One Key/Unified
controls and scoped compatibility modifications are separate. Preserve included
GPL/AGPL/MIT texts, notices and original contributor credits.
