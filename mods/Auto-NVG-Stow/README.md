# Auto NVG Stow for Wearable Devices

**Version 0.1.2** automatically lifts active ordinary NVGs before you view
Promin or Vektor, then restores them when you lower the wearable and the
original device is still valid. Manual NVG input takes priority.

[Download v0.1.2](https://github.com/ProfessorMaterialistic/GAMMA-Mod-Releases/releases/tag/auto-nvg-stow-v0.1.2)
· [Install / update](INSTALL.md) · [Compatibility](COMPATIBILITY.md)
· [Changelog](CHANGELOG.md) · [Credits and rights](CREDITS.md)

The addon uses your existing native NVG animations and sounds. Wearable Devices
keeps control of its wearable behavior; the addon coordinates the transition
and cancels stale restores after manual input or equipment changes.

## What changed in 0.1.2?

Fatal Error is optional for the inspected ordinary Beef/Better Beef + FDDA
stack. Without it, the addon checks native NVG device identity and the existing
charge rules. With it, Fatal Error's separate broken-device state remains
authoritative. Unknown or incomplete contracts issue no automatic NVG transition.

## Requirements

- Wearable Devices **v0.8.14 API contract**.
- FDDA Redone / LAM2 with native NVG animations **enabled**; inspected FDDA
  baseline **v1.4.1**.
- MCM (Mod Configuration Menu).
- Compatible ordinary Beef/Better Beef NVG stack with exported device state,
  charge and torch APIs and the native tagged animation setter. Original Beef
  needs FDDA's final animation provider.

Install dependencies separately. The download supplies five addon scripts,
English MCM strings and distribution notes; it contains no dependency files,
animations, shaders or engine binaries.

Fatal Error, AutoNVG and Custom Mod Categories are **optional integrations**.
This addon does not require a new engine build. It does not provide AutoNVG
gain/Bodycam features; those retain their own requirements.

## Wearables and controls

| Wearable | Implemented path |
| --- | --- |
| Promin | Wrist and source-mapped exo screen |
| Vektor / Vektor-2M | Wrist |
| Aura, unknown hardware, Vektor on exos | Unsupported |

Use your existing Wearable Devices controls. In **MCM → Auto NVG Stow for
Wearables**, the master, Promin and Vektor switches default to On. There is
no separate restore mode.

## Validation and limits

The owner confirmed correct in-game operation of v0.1.2. The known deployed
setup was **Better Beef + AutoNVG + Fatal Error**. The report does not separately
identify every configuration, NVG generation, input mode or equipment variant.

Automated source-executing checks passed **300 cases, 0 failures** across six
configurations. Other combinations are source-validated and not individually
gameplay-confirmed; see the [compatibility table](COMPATIBILITY.md).

Only ordinary Gen 1/2/3 NVG effects are handled. Bare original Beef without
FDDA's tagged LAM2 setter, other NVG overhauls, later setter overrides and
changed loaders are unsupported or unverified. English strings are bundled.
The addon waits for real native animation completion; it does not shorten
the native transition. Faster handoff is not included in this release.

If transitions do not activate, check the native animation setting and file
winners described in [installation](INSTALL.md). Do not replace upstream
dependency scripts to force support. Include your actual dependency versions,
NVG generation/input mode and winning providers in a
[bug report](https://github.com/ProfessorMaterialistic/GAMMA-Mod-Releases/issues/new).

Copyright 2026 ProfessorMaterialistic. All rights reserved. No standalone
open-source license is granted. Separate dependencies retain their own terms.
See [notices](NOTICES.txt).

Release archive SHA-256: `48d1f9bda1a133e0e53c67aec3db691421d96b7b7676844a6bcee05d54bdcbcb` (11,415 bytes).
