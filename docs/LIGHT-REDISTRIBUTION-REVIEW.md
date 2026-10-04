# Light bundled component review — 2026-10-04

**Both initial 2.0 public archive uploads are held.** Current-task publication authorization exists, and runtime/package checks passed, but exact bundled component clearance is incomplete. No tags or GitHub Releases were created. No blanket repository license is assigned.

## Component classifications

| Bundled component | Classification | Evidence / remaining action |
| --- | --- | --- |
| Authored One Key actions/input/gestures/display/standalone; Unified store/logic/controller; shared light compatibility/backends; Native adapter | ORIGINAL / SAFE TO PUBLISH | Preserved project source matches tested content; retained inputs below remain separately scoped |
| Generated semantic icon atlas and its descriptor | ORIGINAL / SAFE TO PUBLISH | Original geometric drawing code in the project visual generator; no downloaded artwork used for the atlas |
| `utlf_input.script`, `utlf_battery.script`, `utlf_items.script` | UPSTREAM / REDISTRIBUTION CONFIRMED, subject to license compliance | Clean input hashes exactly match official UTLF **v1.0.1**. [Pinned GPL-3.0](https://github.com/MichaelHochriegl/Stalker.Anomaly.Universal.Tactical.Light.Framework/blob/v1.0.1/LICENSE). Retain attribution, modified-source notices and applicable source/license obligations; current candidates lack finalized notices |
| `actor_effects.script`, required animation bridge | REVIEW REQUIRED — exact inherited lineage / notices | Official [GAMMA credits](https://github.com/Grokitach/Stalker_GAMMA#credits) allow modified GAMMA addons with source credit; [repository AGPL-3.0](https://github.com/Grokitach/Stalker_GAMMA/blob/main/LICENSE) is published. The pinned local input differs from current official component bytes; identify exact inherited source/credit chain and satisfy applicable terms before clearing this file |
| Soy Adjustable `adjustable_flashlight.script` / tuning UI and XML | REVIEW REQUIRED | Exact inspected archive has a functional README but no redistribution grant identified. Confirm Soy/upstream permission and retained UI attribution |
| Soy UTLF IR `utlf_ir_mode.script`, tuning UI and XML | REVIEW REQUIRED | Exact archive README documents behavior, not redistribution permission. Confirm exact modified-source/UI terms |
| Soy IR `ir_headlamp.script`, `ir_headlamp_ui.script`, XML | REVIEW REQUIRED | Exact archive supplied no permission/license notice. [Recorded author thread](https://discord.com/channels/912320241713958912/1532841384732659873) is not a permission grant |
| Borksy `zzz_bas_laser_control.script`, `laser_settings_ui.script` and XML | REVIEW REQUIRED | [Official 2.7 author release](https://www.moddb.com/mods/laser-settings/downloads/laser-settings-v2-7) identified. No grant for these exact modified copies established |
| Retained One Key menu/theme/binding/UI, localized input and ring/dot DDS | REVIEW REQUIRED | Preserved earlier One Key inputs; verify original authorship/inherited artwork and notices rather than assuming all retained material is new/original |
| Retained Unified facades/dialog XML/localized inputs mixed with original extensions | REVIEW REQUIRED | Identify prior project / Soy / UTLF / Laser contribution chains file by file |
| Anomaly/GAMMA host, MCM, MGI/MGUI, engine executables, dependency weapon models/textures/sounds, G2X presets, illuminator assets | EXTERNAL DEPENDENCY / NOT BUNDLED | Installed separately; [dependency sources](DEPENDENCIES.md). Only modified bridge scripts/UI listed above are bundled in proposed archives |

## Why the current package cannot be trimmed silently

The accepted setup selects Soy Adjustable, UTLF IR, IR Headlamps/illuminator and Laser Settings. Their compatibility code provides tested behavior, while `actor_effects.script` is in the mandatory core. Removing it removes required presentation support. Replacing the accepted selection with Native/absent-integration alternatives would change the shipped feature/install scope; these alternatives have local validation rather than separate owner acceptance. No runtime file was removed or changed to bypass review.

## Package review

- Both final source archives passed integrity/extraction checks; all **85** runtime files match synchronized staging, and selected installed runtime hashes match the TESTED manifest.
- Clean local candidates exclude internal `SOURCE_VERSIONS.json` and `TESTING.md`, replace only delivery docs, and remove the obsolete installer reference to the excluded testing document. Installer choices and every runtime/asset byte are preserved.
- Candidate contents and notes remain local, outside this public repository. They are **not distribution-cleared** and were not uploaded.
- Resolve exact component terms/attribution, finalize applicable license and modified-source notices, then revalidate the final archive/checksum under a newly explicit current-task publication request. Future authorization must never be inferred from this historical task.
