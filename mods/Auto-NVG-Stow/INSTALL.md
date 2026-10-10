# Install, update and remove Auto NVG Stow

[Overview](README.md) · [Compatibility](COMPATIBILITY.md) · [Download v0.1.2](https://github.com/ProfessorMaterialistic/GAMMA-Mod-Releases/releases/tag/auto-nvg-stow-v0.1.2)

## Install with MO2

1. Close the game. Back up an existing Auto Stow addon before updating. Duplicate
   your working profile when testing a different dependency configuration.
2. Download the v0.1.2 `.7z` release asset and use MO2's **Install a new mod from
   an archive**. The mod must have `gamedata/` directly at its root.
3. Enable the addon below its wearable/NVG/MCM dependencies in MO2's **left
   pane**. Enable only one Auto Stow copy. Keep the established order between
   upstream dependencies; moving Auto Stow cannot fix their conflicts.
4. Confirm Auto Stow wins its five `auto_nvg_stow` scripts and
   `gamedata/configs/text/eng/ui_mcm_auto_nvg_stow_wearables.xml`. Overwrite must
   not shadow them. Keep the `aaa_` and `zzzz_` filenames unchanged. No plugin
   or right-pane load-order change is needed.
5. Inspect the native providers in MO2's Data/conflict view:
   - With Fatal Error, its `item_device.script` must win for the inspected stack.
   - Without it, the inspected FDDA `item_device.script` supplies the contract.
   - FDDA provides `lam2.script` and its NVG animation configuration.
   - Original Beef needs FDDA's final `z_beefs_nvgs.script`. Better Beef .18 or
     the compatible AutoNVG adapter can instead provide the native NVG setter.
6. Enable **FDDA NVG animations**. In **MCM → Auto NVG Stow for Wearables**, enable
   the master and the desired Promin/Vektor switches; all default to On.

Keep Wearable Devices v0.8.14's files intact. The addon adds coordination only.

## Update an existing installation

With the game closed, preserve your previous addon and install v0.1.2 as a
separate mod, disabling the old copy. Alternatively, back up the existing mod
and replace its addon files. Do not enable both copies or merge dependency
scripts into Auto Stow. v0.1.1 is the known rollback; v0.1.0 had a stuck-handoff
defect.

## Check the result

With a charged ordinary NVG on, view Promin or Vektor. The NVG should lift first,
the wearable should raise, and lowering should permit one native restore.
Repeat/rapidly cancel and test manual NVG input; manual action or removal,
replacement or depletion of the device must cancel stale restoration.

The release includes `GAMEPLAY-CHECKLIST.txt` for configurations and equipment
variants that need individual confirmation. Source validation is separate from
gameplay testing.

## Roll back or uninstall

Lower the wearable and let animations finish, then close the game. Disable
v0.1.2 and re-enable your preserved v0.1.1 mod, or reinstall its archive. Keep
one copy enabled. To uninstall, disable Auto Stow only and leave dependencies
intact. Return to your preserved profile if you changed dependency selections.
