# HUD Readability 0.2.1

Readable, configurable stamina and radiation feedback for S.T.A.L.K.E.R. Anomaly / GAMMA.

## Status

Current documented version: **0.2.1**, verified 2026-10-12. The owner confirms
stamina rendering in the AURA/SOTA setup. Earlier customization, resets and
wearable checks retain their scoped acceptance. Other variants are unverified.
This is a public project page; **no 0.2.1 downloadable archive is published here**.

## Features and controls

Open **MCM → HUD Readability**. Stamina supports 50–150% scale and 50–200% width,
both in 5% steps. Stamina and radiation independently support opacity, eight
palette colors, source appearance, Static/Dynamic color, position presets and
wearable handoff. Dynamic color moves from green through yellow to red.

Edit HUD Layout returns to the game: drag a visible element, hold Shift to bypass
snapping, and press Escape or right-click to finish. Positions save while dragging.
Reset buttons restore the selected element or both elements. Reset accepts other
pending MCM edits too, then closes the menu; reopen it to view the saved values.

Stamina appears when depleted, holds briefly at recovery, then fades. Smart Handoff
hides equivalent normal information only when a supported wearable visibly
provides it. Always Show Normal HUD bypasses wearable suppression; recovery fades
still apply. Zero opacity and a hidden game HUD keep the bar hidden.

## What changed in 0.2.1?

AURA's replacement texture was transparent at the stamina bar's old coordinates.
The bar updated correctly but could not be seen. An original opaque bar texture
fixes that conflict. Stamina-reducing equipment was not the cause. The fix preserves
sampling, fade timing, settings and wearable ownership.

[Install/update](INSTALL.md) · [Requirements and limits](COMPATIBILITY.md)
· [Changelog](CHANGELOG.md) · [Credits](CREDITS.md) · [Mod index](../../docs/MOD-INDEX.md)
