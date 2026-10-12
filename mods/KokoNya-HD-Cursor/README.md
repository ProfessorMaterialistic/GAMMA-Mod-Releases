# KokoNya HD Cursor 0.1.0

A faithful 256×256 remaster of the white KokoNya cursor for the inspected Modern-MT
DX11 renderer. It preserves the original silhouette, white shade, displayed size
and click origin. This update adds a consistent versioned MO2 name; runtime files
are unchanged.

## Status and availability

IMPLEMENTED and LOCALLY VALIDATED; deployed in the inspected setup. Individual
movement/click/menu/PDA and resolution checks have not been confirmed in game.
Public documentation is available; no public download is provided. Redistribution
permission for the original/derived artwork remains unverified.

## Features and requirements

Eight 256×256 RGBA8 frames replace the original 64×64 compressed frames. A pair of
cursor-only DX11 shader files compensates for the larger texture while preserving
engine cursor geometry/input. The existing HUD color/HDR handling and sequence
timing remain in control; no visible animation is added. No engine patch, font,
UI XML, ReShade or general HUD shader replacement is included.

REQUIRED: the inspected Modern-MT DX11 path and its normal shader resources.
DX8/DX9 and other engine forks are unverified. The original KokoNya addon is not
required to remain enabled in the inspected setup; keep it installed as rollback.
The current owner configuration has the original disabled and HD enabled.

## Installation, update and rollback

For an existing maintained installation, close GAMMA and MO2 and name the mod
**KokoNya HD Cursor 0.1.0**. Preserve its current priority. Verify it wins eight
`ui_ani_cursor_01` through `08` DDS files plus `shaders/r3/hud_cursor.s` and
`shaders/r3/kokonya_cursor_hd.ps`. Keep frames and the adapter together; do not mix
HD frames with the old shader or old frames with the HD adapter.

There are no settings, bindings or save migrations. To return to the original,
close GAMMA/MO2, disable HD and re-enable the preserved original cursor addon.
Removing HD alone does not re-enable a disabled original. No game executable,
save or shader-cache deletion is needed for this name update.

If the cursor appears cropped or the wrong size, check those ten files have the
same intended provider and that the renderer is DX11. The engine's normal
resolution scaling is retained; this is not a fixed physical-pixel sizing mode.

## Validation and remaining checks

The current ten files match their deployment hashes and win their paths; all
eight DDS frames decode at 256×256. Prior local work checked silhouette/alpha
parity, reproducible assets, shader compilation and archive integrity. Actual
movement, hotspot, clicks, menus/inventory/PDA, resolution changes and
1080p/1440p/2160p appearance remain individual in-game checks.

[Changelog](CHANGELOG.md) · [Credits](CREDITS.md)
