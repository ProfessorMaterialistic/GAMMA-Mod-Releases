# Auto NVG Stow v0.1.2 compatibility

[Overview](README.md) · [Installation](INSTALL.md)

The inspected baseline is Wearable Devices v0.8.14, FDDA Redone v1.4.1/LAM2,
Better Beef .18 where enabled, the AutoNVG v0.4.1 adapter where enabled, and
Fatal Error v1.7.9.5 where enabled. MCM is required. Changed providers need
separate verification; these results do not certify every Anomaly NVG overhaul.

| Configuration | Source/runtime checks | In-game evidence for v0.1.2 |
| --- | --- | --- |
| Original Beef + FDDA + Fatal Error | 50 PASS / 0 FAIL | Not individually confirmed |
| Original Beef + FDDA, without Fatal Error | 50 PASS / 0 FAIL | Not individually confirmed; primary compatibility target |
| Better Beef + FDDA + Fatal Error | 50 PASS / 0 FAIL | Not individually confirmed |
| Better Beef + FDDA, without Fatal Error | 50 PASS / 0 FAIL | Not individually confirmed |
| Better Beef + AutoNVG + FDDA + Fatal Error | 50 PASS / 0 FAIL | Known deployed setup associated with owner general success confirmation |
| Better Beef + AutoNVG + FDDA, without Fatal Error | 50 PASS / 0 FAIL | Not individually confirmed |

The owner reports that v0.1.2 works correctly. The known deployment was the
fifth row; the general report does not enumerate all rows or individual test
behaviors. **300 automated passes are not six completed gameplay tests.**

## Fatal Error optional path

Fatal Error's broken-device flag is distinct from battery charge and remains
authoritative when available. Without Fatal Error, the inspected native torch
class and existing provider charge checks validate ordinary NVGs. The addon
does not invent a condition/damage threshold. Failed checks, partial Fatal
Error installations and unknown contracts issue no automatic transition.

## Native providers and limits

FDDA's tagged LAM2 animation setter is required for the original Beef stack.
Bare original Beef's older final setter does not supply this contract. Better
Beef and the inspected AutoNVG adapter retain compatible native actions. Keep
their dependency order and inspect final `item_device` / `z_beefs_nvgs` winners.

Promin wrist/source-mapped exo and Vektor/Vektor-2M wrist paths are implemented.
Aura, unknown devices and Vektor on exos are excluded. Gen 1/2/3, Classic/Tap/Hold
and equipment variants are not all individually gameplay-confirmed. PDA,
gain/Bodycam and whole-profile behavior after disabling Fatal Error require
their own configuration checks; this addon does not certify unrelated systems.

Other NVG overhauls, changed loaders and later setter overrides are unverified.
Only English strings are included. Native animation duration is preserved.
