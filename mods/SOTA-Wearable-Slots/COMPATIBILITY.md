# Requirements and limits

- **Required:** SOTA Inventory and Wearable Devices ownership/slot APIs, including
  the bracer's read-only worn-object compatibility adapter.
- **Supported styling integration:** FIUT category headers and sorting remain owned by FIUT.
- **Inspected WD baseline:** 0.8.14. Other WD versions and inventory replacements are unverified.
- **Not required:** 3DSS, UTLF or a new engine patch.

Local checks exercise exact worn-item IDs, spares, unequip/re-equip, save/load,
startup ordering, category queries, loot/trade and XML geometry at three bag widths.
The owner confirms appearance and general operation in the tested SOTA/FIUT setup.
Individual click boundaries, empty/spare-device cases, alternate layouts,
loot/trade and save/reload remain unconfirmed in game.

This is UI presentation: it does not transfer/create/destroy items, change actor
stats, or own equipment/save keys. It preserves original inventory method calls
and refreshes when WD's authoritative equipped state changes.
