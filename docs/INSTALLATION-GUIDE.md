# Installation guide

[Home](../README.md) · [Troubleshooting](TROUBLESHOOTING.md)

Light public archive uploads are held for bundled redistribution review. These instructions describe the prepared installer flow; [check mod download status](MOD-INDEX.md) before installing.

1. Open the individual mod's requirements and compatibility page. Verify the exact supported engine/dependency versions.
2. Obtain the specifically versioned archive from its future GitHub Release. Check SHA-256 if provided. Do not use an internal test build as a stable release.
3. Save and close GAMMA. Preserve your current MO2 profile/settings and previous mod version for recovery.
4. Use MO2's **Install a new mod from an archive**. Keep the archive's FOMOD structure; do not manually flatten its alternative folders.
5. Select only integrations whose dependencies you installed separately. Install the mod as a separate entry, disable its older version, and enable the new entry.
6. Follow the documented **MO2 left-pane file priority**, with the mod overriding its selected dependencies. This is not a plugin/ESP load-order instruction.
7. On first launch, open MCM, check detected integrations, assign controls and apply settings. Follow any explicit binding-clear/restore instructions rather than deleting bindings blindly.

For the Light pair, use [One Key installation](../mods/One-Key-Light/INSTALL.md) and [Unified installation](../mods/Unified-Player-Light-Controls/INSTALL.md), with matching backend/integration selections. Each works without the companion.

For updates, close the game, preserve the previous matched version/options, install the replacement separately, and retain settings unless the release notes call for a specific migration. For removal, restore any explicitly cleared vanilla bindings before disabling their owner. Re-enable the previous matched setup if needed; do not delete saves or dependency mods.

An engine-dependent package must identify matching engine gamedata. A resource version alone does not prove engine compatibility. This hub currently distributes no engine executable.
