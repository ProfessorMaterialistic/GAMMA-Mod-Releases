# Installation and rollback â€” 2.1.0

Install the versioned .7z from the [GitHub Release](https://github.com/ProfessorMaterialistic/GAMMA-Mod-Releases/releases/tag/one-key-light-v2.1.0) through MO2.

## Requirements and installation

1. Close GAMMA before changing mods. Back up the MO2 profile and previous Light pair.
2. Install each desired .7z through MO2 as a separate mod. The archive root contains
   fomod/ModuleConfig.xml and its mapped Core/core and optional integration folders.
3. Disable earlier One Key/Unified providers. Install the selected dependencies
   separately; Light contains compatibility bridges, not complete dependencies.
4. In MO2's left pane put host/matching engine gamedata, MCM and GAMMA animation
   support first; selected light/laser dependencies and weapon registrations next;
   One Key Light 2.1.0 and/or Unified Player Light Controls 2.1.0 afterwards.
   Higher numerical priority wins conflicts. Use matching installer choices in both.
5. Choose Soy Adjustable only with 1.0; Laser Settings only with 2.7; UTLF IR only
   with Soy 1.03 and UTLF 1.0.1; IR Headlamp only with 1.3.0 and its illuminator.
   Native/G2X uses externally installed presets; native beam sliders are unavailable.
6. With matching 2.1.0 copies, either companion order is valid because all shared
   paths are identical. The owner's inspected profile has Unified winning overlap.
   No additional later patch is certified. Check MO2 conflict winners after updates.
7. Open MCM: One Key has Controls, Quick Menu, Anomaly Torch Binding, Compatibility;
   Unified has Light Linking and Compatibility / Debug. Apply saves pending edits;
   Reset/Cancel discard them. Keep Debug Mode off for normal play.

Both mods install independently. Neither requires the companion or a third core.
One Key alone uses OFF/ON; Unified adds supported weapon/laser AUTO and linking.

## Troubleshooting

Missing weapon output: check UTLF registration, supported attachment, power,
selected integration and MO2 winner. AUTO darkness outside its aim policy is normal.
IR darkness: deploy suitable NVGs and install the IR Headlamp illuminator on the
equipped NVG. Linked missing/depleted IR deliberately fails dark. Headlamps are
OFF/ON only. Low battery pulses remain intentional; check upstream battery settings.
Duplicate control/MCM entries: disable old providers and mismatched compatibility
patches. Verify matching companion versions and installer choices. A missing icon
atlas falls back to text; report reproducible defects with dependency versions,
MO2 conflicts, ON/AUTO mode and engine strings from the game log.

## Uninstall / rollback

Close GAMMA. If One Key cleared the vanilla Torch binding, use its Restore control
before removal. Disable the unwanted mod and re-enable the previous matched pair
or restore your backed-up profile/settings. Removing one companion leaves the
other independently usable. Do not delete saves or dependency mods. Installation
does not clear bindings or reset saved light modes; preserved configuration is
intentional. Do not mix 2.0/2.1 shared bridges. Keep previous archives for rollback.
