# Compatibility and dependencies — 2.1.0

## Tested engine and scope

The October 10 owner retest passed all ten Light cases on the deployed candidate:
weapon flashlight ON/AUTO, laser ON/AUTO, simultaneous output, full-auto comparison,
switch/reload, One Key/Unified controls, NVG/IR, headlamp/battery behavior.
The post-deployment session log records **MT-TEST 2026.08.04 / xrCore 10100**
(compiled October 3, 2026), **AnomalyDX11AVX.exe**, in the owner's Bodycam/MT
environment. This is a specific modified engine environment, not certification
of every executable carrying the same version strings. Matching engine gamedata
and an AVX-capable CPU are required. No engine binaries are included.

Historical 2.0 acceptance used MT-TEST 2026.09.07 / xrCore 10074. That is a separate
historical record, not a second 2.1 retest. Other engine builds, non-AVX variants,
base Anomaly and other modpacks are unverified. No universal minimum API is asserted.

## Dependency classification

| Component | Classification / tested version |
| --- | --- |
| Anomaly/GAMMA and matching engine gamedata | REQUIRED host; no independent numbered host pin established |
| Mod Configuration Menu (MCM) | REQUIRED; installed native/CMC MCM inspected, no independent numbered pin asserted |
| GAMMA 3D PDA and Headlamp Animations | REQUIRED presentation support |
| UTLF 1.0.1 and supported weapon/attachment registration | OPTIONAL INTEGRATION, required for weapon flashlight features |
| Soy Adjustable Headlamps 1.0 | OPTIONAL INTEGRATION for adjustable normal headlamp |
| Soy UTLF IR Mode 1.03 | OPTIONAL INTEGRATION for IR weapon lights; needs UTLF and suitable NVGs |
| Soy IR Headlamps 1.3.0 plus installed NVG illuminator | OPTIONAL INTEGRATION for IR headlamp |
| Borksy Laser Settings 2.7, BaS-compatible laser support and laser-capable weapon | OPTIONAL INTEGRATION for laser controls |
| MGI/MGUI 0.3.4 | OPTIONAL INTEGRATION for GUI launchers; core works without it |
| Native/G2X presets | OPTIONAL INTEGRATION; assets installed separately |
| Matching companion 2.1.0 | OPTIONAL INTEGRATION; no third mandatory core |
| Python, Lupa Lua 5.1, Pillow, 7-Zip | DEVELOPMENT ONLY; never runtime requirements |

Laser Settings lists BaS as a prerequisite; use GAMMA’s installed compatible
BaS/laser support. No independently numbered BaS pin is established.

The inspected setup also enables UTLF Built-In Weapon Support v2 and GAMMA Weapons
1.0.0-beta.2; the reproduced weapon is Viper 2. This does not certify all weapons.
Selected retest integration: Soy Adjustable, UTLF IR, IR Headlamp/illuminator and
Laser Settings. Alternative backends and absent integrations pass local mocks;
separate gameplay acceptance of every installer combination is not claimed.

MO2 order and conflict handling: see [INSTALL.md](INSTALL.md).
Dependency downloads: [official source index](https://github.com/ProfessorMaterialistic/GAMMA-Mod-Releases/blob/main/docs/DEPENDENCIES.md).
