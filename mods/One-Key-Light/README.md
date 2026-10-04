# One Key Light 2.0

## Overview

Control installed player lights with one key and a compact on-screen menu. Each Light mod works independently. Use matching 2.0 companions and installer choices when combining them.

**TESTED / FINAL-FOR-NOW** for the accepted setup, owner confirmation recorded 2026-10-01. **Public release held for bundled redistribution review.**

[Features / configuration](FEATURES.md) · [Install / update / remove](INSTALL.md) · [Compatibility](COMPATIBILITY.md) · [Changelog](CHANGELOG.md) · [Credits](CREDITS.md)

## Feature highlights

- Tap / Double Tap / Hold with configurable assignments and timing.
- Quick Light Menu with device states, themes, locks and text fallback.
- Standalone OFF/ON; optional Unified AUTO and NVG linking.
- Existing headlamp animations and one backend click per supported manual switch.

## Requirements

| Mod / host | Required? | Purpose | Load relationship | Link |
| --- | --- | --- | --- | --- |
| Anomaly / GAMMA, MCM | Yes | Host and configuration | Before Light files | [Sources](../../docs/DEPENDENCIES.md) |
| MT-TEST 2026.09.07 / xrCore 10074 + matching gamedata | Supported baseline | DX11-AVX, AVX CPU | Engine instructions; gamedata before Light | [Engine source](https://github.com/themrdemonized/xray-monolith) |
| GAMMA 3D PDA and Headlamp Animations | Yes | Headlamp presentation | Light animation override wins | [Sources](../../docs/DEPENDENCIES.md) |

## Optional integrations

UTLF 1.0.1 for weapon lighting; Soy Adjustable 1.0 for its headlamp backend; Soy UTLF IR 1.03 for weapon IR; Soy IR Headlamps 1.3.0 plus illuminator for IR headlamp; Laser Settings 2.7 for lasers; MGI/MGUI 0.3.4 for optional GUI launchers; the matching companion for combined controls.

These are **feature-conditional and separately installed**. [Complete requirements, source links and limitations](COMPATIBILITY.md).

## Quick install

1. Install the supported host and chosen dependencies separately.
2. Once released, download the versioned archive and install through MO2's archive / FOMOD flow.
3. Match backend/integration choices in both Light installers, enable the mod and let its files override its dependencies.
4. Configure MCM and verify output with the intended equipment.

[Full installation guide](INSTALL.md) · [Verified MO2 priority](COMPATIBILITY.md#verified-mo2-file-priority).

## Controls / behavior

| Input | Action |
| --- | --- |
| Mouse 5 Tap | Headlamp toggle |
| Mouse 5 Double Tap | UTLF White toggle when installed |
| Mouse 5 Hold | Laser toggle when installed |
| Shift + Mouse 5 | Quick Light Menu |
| Dedicated menu key | Unassigned until configured |

Normal and IR headlamps support OFF/ON. Supported weapon lights and laser gain AUTO with Unified. One Key standalone uses OFF/ON. IR needs appropriate equipment/power and deployed NVGs.

## Linked / AUTO behavior

Unified links White/IR weapon light or Normal/IR headlamp explicitly in MCM. Visible lighting routes with NVGs stowed; IR routes with NVGs deployed. Unavailable IR fails dark. Independent modes/tuning survive link/unlink. Gestures do not silently enable links. AUTO gates supported weapon/laser output using saved aim policy; headlamp AUTO is absent.

## Configuration

Use the native MCM pages and supported device dialogs. [Detailed controls, timing, menu options and configuration](FEATURES.md). Tap waits for the 225 ms double window; Hold fires once at 300 ms by default.

## One Key / Unified integration

Each works independently; no third mandatory core. When combining them, use matching 2.0 versions and FOMOD choices. Either companion order is valid when shared files match and both override their selected dependencies.

## Update and uninstall

Close the game, replace the old MO2 entry with the matched version/options and retain settings. Restore any Torch binding cleared by One Key before removing its binding owner. [Detailed update/removal](INSTALL.md).

## Compatibility and known issues

No unresolved gameplay defect is recorded for the accepted setup. Other engine variants and every optional installer configuration are not separately gameplay certified. Native/G2X beam tuning uses separate presets. [Compatibility details](COMPATIBILITY.md) · [Troubleshooting](../../docs/TROUBLESHOOTING.md).

## Download

**Not publicly released.** Initial 2.0 publication is authorized in the 2026-10-04 task, but bundled component clearance is incomplete. No download archive or release tag has been published. [Release status / future downloads](https://github.com/ProfessorMaterialistic/GAMMA-Mod-Releases/releases) · [Component review](../../docs/LIGHT-REDISTRIBUTION-REVIEW.md).

## Credits

Bling / ProfessorMaterialistic, UTLF, Soy, Borksy, GAMMA animation contributors and configuration/UI contributors. [Full attribution](CREDITS.md).
