# One Key Light 2.0 installation

[Overview and controls](README.md) · [Requirements and MO2 order](COMPATIBILITY.md) · [Credits](CREDITS.md)

**Public download held for bundled-file redistribution review.** The flow below documents the final 2.0 installer. Install only after the authorized archive appears; [download status](README.md#download).

## Before installing

Verify [required host and feature dependencies](COMPATIBILITY.md), including MT-TEST **2026.09.07** / xrCore **10074**, matching engine gamedata and **AnomalyDX11AVX.exe**. Install chosen upstream mods separately. Save and close GAMMA; preserve your profile/settings and previous matched Light versions.

## MO2 / FOMOD

1. Once published, download the exact 2.0 archive from this hub’s [GitHub Releases](https://github.com/ProfessorMaterialistic/GAMMA-Mod-Releases/releases) and verify its SHA-256. No 2.0 Release exists yet.
2. In MO2, choose **Install a new mod from an archive**, select the archive, and keep it as a separate 2.0 entry. Do not manually copy every alternative folder into gamedata.
3. Confirm **GAMMA and MCM are installed**.
4. Choose exactly one **Headlamp backend**: **Native / G2X**, or **Soy Adjustable Headlamps 1.0** if that mod is separately installed. Native needs no Soy dependency; its beam is not tuned by Soy sliders.
5. Choose **No Laser Settings integration**, or **Laser Settings 2.7 installed** only with Borksy's dependency enabled.
6. For **UTLF IR compatibility**, choose **Not installed**, or **Soy's UTLF IR Mode 1.03 and UTLF 1.0.1 installed** only when both are enabled.
7. For **IR Headlamp compatibility**, choose **Not installed**, or **Soy's IR Headlamps 1.3.0 and its NVG illuminator module installed** only when both are present.
8. If installing both companions, choose the **same backend and compatibility options in both**. Each installs its own shared compatibility support; no third mandatory core exists.
9. Disable the previous version of this mod, enable 2.0, and place it after/higher priority than its selected dependencies in the **MO2 left pane**. Verify the Light files win conflicts. With matching selections, either companion order works.

No engine binary or complete upstream asset package is installed by these choices. Selecting **Not installed** skips a bridge rather than uninstalling another mod. FOMOD labels above were checked against final 2.0 delivery metadata, not just an earlier candidate README.

## First launch and configuration

Open **MCM → One Key Light 2.0**. Under **Compatibility**, check detected integrations. Under **Controls**, enable the mod and check Main Light Control Key, Tap/Double Tap/Hold actions and timing; defaults are Mouse 5, Headlamp / UTLF White / Laser. Change unavailable actions to an installed device or None.

Under **Quick Menu**, keep Shift + main key or assign a dedicated menu key, then choose selection/style preferences. With Unified installed, set explicit **Separate / NVG Linked** selectors and **Apply**. Gesture assignments do not enable linking.

If replacing vanilla Torch input, use **Anomaly Torch Binding → Clear Vanilla Torch Binding** explicitly. Installation does not clear it automatically. Clear preserves both Torch slots and keeps them disabled across restarts until Restore is used. Read the status before changing bindings.

## Update

Save and close GAMMA. Preserve your current entry, profile/settings and previous archive. Install the replacement as a separate version with the same dependency/backend choices; disable the old entry and enable the new one. Update both companions to a matched version if using the pair. Check file winners and MCM settings after launch. Saved Light settings are retained; use specific release migration notes rather than deleting them wholesale. Adding/removing an optional dependency requires rerunning the installer choices consistently in both companions.

## Uninstall / rollback

If you used **Clear Vanilla Torch Binding**, use **Restore Vanilla Torch Binding before disabling One Key**. Restore checks saved keys and refuses to overwrite a new Torch binding or a key assigned to another command; free the conflicting key in Controls and retry. Confirm the status says persistent disabling is off. If One Key is already removed, temporarily re-enable the matching version to Restore or restore your own known-good controls/settings backup.

Close GAMMA, disable this mod's MO2 entry, and re-enable the prior matched setup if needed. Dependencies continue with their own winning files when the Light overrides are removed. Keep the original entries recoverable; do not delete saves or dependency mods. Removing one companion leaves the other independent, but changes the available advanced/gesture functionality. Shared settings remain; an exact settings rollback requires your own previously preserved setup.

See [troubleshooting](../../docs/TROUBLESHOOTING.md) before reporting a problem.

## Verified installer choices

| Step / choice | Effect | Absent dependency behavior |
| --- | --- | --- |
| GAMMA and MCM are installed | Confirms required host baseline | Does not install the host, MCM or engine |
| Native / G2X | Uses engine headlamp and existing presets | No Soy Adjustable requirement; beam sliders do not tune the native light |
| Soy Adjustable Headlamps 1.0 | Installs the Adjustable bridge / enables supported tuning | Select only with its separate dependency; no dependency detection is implied by FOMOD |
| No Laser Settings integration | Skips laser bridge | No working Laser Settings integration added |
| Laser Settings 2.7 installed | Installs laser compatibility bridge | Requires separate Laser Settings and compatible weapon |
| UTLF IR: Not installed | Skips IR weapon bridge | Does not install / remove upstream IR assets |
| UTLF IR: Soy 1.03 + UTLF 1.0.1 installed | Installs weapon-IR compatibility | Requires both separately installed dependencies and suitable NVG/equipment |
| IR Headlamp: Not installed | Skips IR headlamp bridge | IR headlamp does not become available by assigning a key |
| IR Headlamp: Soy 1.3.0 + NVG illuminator installed | Installs IR headlamp compatibility | Requires dependency and illuminator separately |

Missing integrations are unavailable; equipped/power failures can show locks or fail dark while preserving intent. The installer choices are manual declarations, not automatic dependency installation or auto-hide detection.
