# Wearable Devices Monochrome UI 1.0.0

A white-on-black screen theme for **Promin and Vektor**, with thin gray rules,
white typography and consistent device panels. Previously named WD - Vektor
Promin Monochrome; this update makes the name/version consistent without changing
the existing 22 texture files.

## Status and availability

IMPLEMENTED and LOCALLY VALIDATED; deployed in the inspected setup. Separate
in-game appearance/behavior acceptance has not been recorded. Public documentation
is available; no downloadable release archive is published with this update.

## Features and controls

Promin backgrounds cover Biomonitor, Navigation, Identification and Messages.
Vektor has PWR, HP and AIR faces. Its clock, compass, distance and status/battery
behavior remain owned by Wearable Devices. Use existing WD page and brightness
controls; this theme adds no bindings or MCM settings.

The payload is 22 DDS textures only: no scripts, XML, shaders, models or AURA
atlases. AURA keeps its live body/limb/psy display, health colors, warning colors
and pending-heal presentation. The background body area is intentionally empty
for AURA's live overlay. Physical Signalis device materials are unaffected.

## Requirements and compatibility

Wearable Devices is REQUIRED; the inspected baseline is 0.8.14. AURA, Wearable
Devices PDA Messages and Immersive Identification are OPTIONAL INTEGRATIONS,
whose scripts/layouts remain separately installed. The theme was locally checked
against the combined AURA/Identification/Messages stack. Other combinations,
physical device rendering and live sensors remain unverified.

## Installation, update and rollback

For an existing maintained installation, close GAMMA and MO2, preserve the old
mod, and name it **Wearable Devices Monochrome UI 1.0.0**. Keep it enabled at its
current effective priority. Its textures should win over WD, Identification and
other WD screen themes; preserve compatibility-patch order. Avoid overlapping
screen themes that override these same texture paths. The default fonts and
runtime tint settings still belong to their original providers.

No settings or save migration is needed. Disable this one theme in MO2 to restore
the underlying screen textures; original mods need no file restoration. The name
change itself does not require reinstalling the payload.

If the old colors/backgrounds appear, inspect texture conflicts in MO2. If Promin
controls are missing or a script/XML error occurs, inspect the separately installed
WD/AURA/Messages compatibility stack: this texture-only theme does not repair it.

## Validation and remaining checks

All 22 current DDS files match the validated payload and win their texture paths.
Prior offline tests exercised Promin controls/pages/power/popups and Vektor clock,
distance, three faces, brightness and compass/arrow visibility with mocked engine
windows. Those tests do not prove actual in-game rendering. Remaining checks include
both Vektor tiers, Promin pages, live readings and AURA overlays during gameplay.

[Changelog](CHANGELOG.md) · [Credits](CREDITS.md)
