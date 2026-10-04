# Light Mods compatibility and requirements

Applies to the accepted **2.0** One Key Light and Unified builds. Each companion is optional. Last documentation reconciliation: 2026-10-04; owner acceptance recorded 2026-10-01. This is a supported setup description, not a claim that every FOMOD combination received separate gameplay testing.

## REQUIRED

| Requirement | Purpose / verified scope | Placement |
| --- | --- | --- |
| S.T.A.L.K.E.R. Anomaly with GAMMA | Host gameplay/device/battery/animation environment | Base before Light Mods |
| MCM - Mod Configuration Menu (RavenAscendant) | Configuration and key binding | Before Light Mods; standalone MCM version not independently pinned |
| Modded Exes MT-TEST **2026.09.07**, xrCore **10074**, matching engine gamedata | Exact declared author-test baseline | Engine installed according to its own instructions; matching gamedata before Light overrides |
| **AnomalyDX11AVX.exe**, AVX-capable CPU | Declared supported executable variant | Verify executable and both engine version strings in the log |
| GAMMA's 3D PDA and Headlamp Animations component | Existing headlamp presentation used by the compatibility patch | Its `actor_effects.script` must be overridden by the Light package |

The Light package does not supply GAMMA, MCM or an engine executable. A precise GAMMA/Anomaly numbered-version pin is not independently established by the Light acceptance record; do not infer support for every update. Other engine dates/builds/variants remain unverified.

## OPTIONAL - required when using that feature

| Dependency | Purpose | Verified version / conditions | Placement |
| --- | --- | --- | --- |
| [Universal Tactical Light Framework (UTLF)](https://github.com/MichaelHochriegl/Stalker.Anomaly.Universal.Tactical.Light.Framework) | White weapon lighting | **1.0.1**; supported registered weapon / modular attachment needed; Light Mods do not install the weapon/model assets | UTLF before its weapon compatibility registrations; selected dependency files before Light Mods |
| Soy's Adjustable Headlamps | ScriptLight normal headlamp and beam tuning | **1.0**; choose its backend in FOMOD | Before both Light Mods |
| Soy's UTLF IR Mode | IR weapon-light channel | **1.03**, with UTLF **1.0.1** and suitable NVG/equipment | Before both; select UTLF IR compatibility |
| Soy's IR Headlamps | IR headlamp channel | **1.3.0**, including its **NVG illuminator module** | Before both; select IR Headlamp compatibility |
| Borksy Laser Settings | Laser controls and, with Unified, tuning/AUTO policy | **2.7**; compatible laser-equipped weapon | Before both; select Laser Settings integration |
| MGI/MGUI (Conditional Integration Fix) | Optional tuning GUI launchers | **0.3.4** inspected integration; no mandatory third control core | Preserve its own dependency order; verified setup puts it before Light Mods |
| Native / G2X headlamp setup | Alternative native engine headlamp/presets | Separate preset assets; Native backend is an installer alternative, not an added dependency on Soy | Presets before Light override; do not install both headlamp backends |
| The other Light Mod 2.0 | One Key gestures/menu plus Unified advanced modes | Same version and matching FOMOD backend/integrations | Either companion order works for matching files |

UTLF is optional for headlamp-only use; it is required for white/IR weapon light features. The official UTLF README confirms a compatible weapon registration is needed. A feature dependency must be installed separately; the Light FOMOD installs compatibility scripts, not complete dependencies. Obtain Soy/Borksy/MGI dependencies from their author's distribution; exact public URLs are not supplied where unverified.

## Verified MO2 file priority

In the MO2 **left pane**, later/higher-priority entries win same-path conflicts:

```text
Anomaly / GAMMA + supported engine gamedata + MCM + GAMMA animations
  ↓
Selected feature dependencies / their required registrations and assets
  ↓
One Key Light 2.0
  ↓
Unified Player Light Controls 2.0
```

The two Light rows may be reversed when **backend and integration selections match**. Their shared installed paths are byte-identical for matching selections. Both must win the patched GAMMA/UTLF/Soy/Borksy scripts; placing an upstream dependency later can remove the integration. No additional optional compatibility patch after the Light pair is currently verified.

This is a verified dependency-to-Light override relationship, not a new universal order among all upstream mods. Follow each upstream package's own dependency order. The accepted setup used Soy Adjustable 1.0 + UTLF IR 1.03 + IR Headlamps 1.3.0/illuminator + Laser Settings 2.7. Native/G2X and absent-integration branches are locally validated; separate owner acceptance of every alternative is not claimed.

## NOT INSTALLED / hidden / unavailable

- Selecting **Not installed** skips the relevant IR compatibility files. **No Laser Settings integration** skips the laser bridge. These selections do not remove a separately installed dependency.
- One Key lists installed device integrations; missing integrations do not become working actions because a key is assigned. Unequipped devices can show an unavailable lock; depleted power can prevent output while saved intent remains.
- Linking and Gesture Behavior controls require Unified; without it, One Key uses standalone OFF/ON and explains that NVG Linked needs the companion.
- Normal, IR and linked headlamps are **OFF/ON only**. Headlamp AUTO is not implemented in the accepted design.
- Native/G2X beam brightness/cone/range/color sliders do not tune the engine's native beam. Use its separately installed presets or choose Soy Adjustable for tuning.

## INCOMPATIBLE / UNSUPPORTED

- Mixed old/new One Key or Unified versions, mismatched headlamp backend choices, and mismatched shared compatibility files are unsupported.
- Earlier/later engine builds, DX11 non-AVX variants and different hosts are unverified. This does not prove that another build is inherently incompatible or identify a historical crash cause.
- A third-party mod that overwrites the same light/input/animation scripts needs a reviewed compatibility patch; no general compatibility claim is made.
- Neither GEKF nor Auto NVG is a dependency. The newer Auto NVG Bodycam diagnostic does not expand the Light Mods' accepted engine coverage.

## Expected behavior and current issue limits

Linked routes fail dark when the selected IR device cannot emit; they do not fall back to white light under NVGs. Saved intent/tuning remain for recovery. IR output requires deployed NVGs and appropriate equipment/power. An installed UTLF framework alone does not give an unsupported weapon a light.

No unresolved gameplay defect is recorded for the final accepted setup. Historical test failures are not asserted as current bugs; the acceptance record also does not establish their exact native cause. Broader configuration/engine coverage remains unverified. See [troubleshooting](../../docs/TROUBLESHOOTING.md) for concrete checks.

[Overview](README.md) · [Installation](INSTALL.md)
