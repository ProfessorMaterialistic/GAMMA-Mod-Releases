# Light dependency sources

[One Key requirements](../mods/One-Key-Light/COMPATIBILITY.md) · [Unified requirements](../mods/Unified-Player-Light-Controls/COMPATIBILITY.md)

These are separately installed dependencies. The Light packages include modified compatibility scripts/UI, **not complete upstream packages, engine executables, weapon models, sounds or preset assets**. Dependency download permission does not clear redistribution of modified copies.

| Dependency | Verified baseline / relationship | Authoritative source |
| --- | --- | --- |
| Anomaly | Host; exact numbered host version not independently pinned by Light acceptance | [Official Anomaly download/install](https://anomalymod.com/download-install/) |
| GAMMA | Required host environment | [Official GAMMA project](https://github.com/Grokitach/Stalker_GAMMA) / [installation wiki](https://github.com/Grokitach/Stalker_GAMMA/wiki) |
| MCM / RavenAscendant | Required Light configuration; separately pinned standalone version not established | [Official ModDB addon](https://www.moddb.com/mods/stalker-anomaly/addons/anomaly-mod-configuration-menu) |
| Modded Exes | 2.1 retest: MT-TEST 2026.08.04 / xrCore 10100 in the specific owner Bodycam/MT environment; matching gamedata, DX11-AVX on an AVX CPU. Historical 2.0: MT-TEST 2026.09.07 / xrCore 10074 | [Official engine project](https://github.com/themrdemonized/xray-monolith) / [releases](https://github.com/themrdemonized/xray-monolith/releases); newer release is not automatically a tested substitute |
| GAMMA 3D PDA and Headlamp Animations | Required animation component, before Light overrides | [GAMMA source component](https://github.com/Grokitach/Stalker_GAMMA/tree/main/G.A.M.M.A/modpack_addons/G.A.M.M.A.%203D%20PDA%20and%20Headlamp%20Animations) |
| UTLF / MichaelHochriegl | 1.0.1, conditional for weapon lights; requires supported weapon registration / attachment | [Official project](https://github.com/MichaelHochriegl/Stalker.Anomaly.Universal.Tactical.Light.Framework) / [releases](https://github.com/MichaelHochriegl/Stalker.Anomaly.Universal.Tactical.Light.Framework/releases) |
| Soy Adjustable Headlamps | 1.0, conditional for Adjustable backend | [Official MIT-labelled author upload](https://www.moddb.com/mods/stalker-anomaly/addons/adjustable-flashlight-v); exact archive checksum matched |
| Soy UTLF IR Mode | 1.03 with UTLF 1.0.1, conditional for weapon IR | [Official Proprietary-labelled author upload](https://www.moddb.com/mods/stalker-anomaly/addons/soys-ir-mode-for-universal-tactical-light-framework); exact archive checksum matched, modified-copy redistribution held |
| Soy IR Headlamps | 1.3.0 with NVG illuminator, conditional for IR headlamp | [Official MIT-labelled author upload](https://www.moddb.com/mods/stalker-anomaly/addons/ir-headlamp); exact locally tested same-version archive differs from current upload. [Recorded author thread](https://discord.com/channels/912320241713958912/1532841384732659873) remains a discovery link |
| Borksy Laser Settings | 2.7, conditional for laser integration | [Official author release](https://www.moddb.com/mods/laser-settings/downloads/laser-settings-v2-7) |
| MGI/MGUI Conditional Integration Fix | 0.3.4, optional GUI launchers | Exact author distribution URL not verified. [GAMMA community entry](https://discord.gg/stalker-gamma) is a discovery/help link |
| Native / G2X | Installer alternative, using separately installed presets | No extra Soy dependency. Exact preset package URL not verified; retain the supported GAMMA setup rather than substituting an arbitrary package |
| Companion Light mod | Optional, matching 2.1.0 and identical FOMOD choices | [One Key](../mods/One-Key-Light/README.md) / [Unified](../mods/Unified-Player-Light-Controls/README.md); downloads currently held |

## Verification limits

Updated October 10, 2026: official Soy author pages and exact archive checksums
were inspected. Author MIT labels do not resolve unidentified inherited UI rights.
The 2.1 retest engine environment is specific; other engines remain unverified.


Official GitHub and ModDB pages above were identified from authoritative project/author pages and recorded package metadata on 2026-10-04. Remaining missing MGI/G2X author URLs are stated explicitly; no fabricated download is supplied. Browser/network access can limit availability checks; the IR Headlamps thread is a recorded author source, not a verified publicly accessible archive. Exact date/core engine support remains the accepted Light baseline regardless of newer upstream versions.

HTTP checks reached the listed GitHub, Anomaly and Discord landing pages successfully. ModDB rejected automated HEAD requests with 403; its MCM and Laser 2.7 author pages were verified through web page retrieval. A Discord landing-page response does not establish access to the thread's messages or downloads.
