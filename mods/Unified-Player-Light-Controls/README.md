# Unified Player Light Controls 2.0

Keep player light intent and tuning consistent across native controls, optional tuning GUIs, and One Key. Unified adds **saved modes, NVG linking, and weapon/laser AUTO behavior** while each companion remains independently usable.

**Development: TESTED / FINAL-FOR-NOW. Public: release preparation; no GitHub download yet.** Owner acceptance was recorded 2026-10-01 for the accepted setup. Public release/redistribution approval remains separate.

[Install / update / remove](INSTALL.md) · [Requirements / MO2 order / compatibility](COMPATIBILITY.md) · [Changelog](CHANGELOG.md) · [Credits](CREDITS.md)

## Devices and modes

| Device | Available modes / behavior |
| --- | --- |
| UTLF White weapon light | OFF / ON / AUTO with supported weapon/attachment |
| UTLF IR weapon light | OFF / ON / AUTO with Soy IR, suitable equipment and NVGs |
| Laser | OFF / ON / AUTO with Borksy Laser Settings / compatible weapon |
| Normal headlamp | OFF / ON |
| IR headlamp | OFF / ON with Soy IR Headlamps / illuminator |
| Linked Weapon Light | OFF / ON / AUTO; selects White or IR by NVG state |
| Linked Headlamp | OFF / ON; selects Normal or IR by NVG state |

OFF keeps requested output off. ON requests output whenever equipment/power/context allow it. AUTO retains intent and gates weapon/laser output using the selected aim policy. A temporarily hidden emitter does not erase your mode or tuning. Headlamp AUTO is intentionally absent.

## Separate and NVG Linked

Under **MCM → Light Linking**, select **Separate** or **NVG Linked** independently for Weapon Lights and Headlamps, then Apply. If One Key is installed, its Controls page edits the same selectors.

- Linked weapon ON/AUTO routes **White with NVGs stowed**, **IR with NVGs deployed**. AUTO follows the selected route's aim policy.
- Linked headlamp ON routes **Normal with NVGs stowed**, **IR with NVGs deployed**; OFF keeps both off.
- Independent channel modes/tuning are preserved when linking/unlinking. A missing or unable IR route **fails dark**; it does not expose visible light under NVGs. Intent remains available for equipment/power recovery.

Gestures choose/control devices; they do not turn linking on. Supported headlamp transitions use existing GAMMA animations; successful manual switches retain appropriate backend sounds without replaying them on retries or ordinary AUTO gating.

## Controls and tuning

Unified has no mandatory new gesture key. It works through supported native light controls and tuning dialogs; optional **MGI/MGUI 0.3.4** provides GUI launchers. One Key adds its Mouse 5 Tap/Double Tap/Hold and Quick Menu interface if desired.

Device dialogs expose applicable **OFF / ON / AUTO** controls. White/IR weapon AUTO policies include aiming in ADS and canted/alternate aim. Laser provides aim restrictions with its supported hide-during-primary/alternate controls. Explicit ON is the manual output request; AUTO applies the saved visibility policy. A manual toggle while AUTO emits selects OFF; while AUTO is hidden it selects ON.

Retained tuning includes:

- White weapon brightness/range/cone/visible color and aim policy; IR brightness/range/cone and independent aim policy.
- Weapon-family/attachment preferences and **Save and Apply to ALL** defaults, with later individual edits still possible.
- Supported Soy normal/IR headlamp tuning dialogs; Native/G2X beam sliders do not affect the native beam.
- Laser brightness, dot/beam size and brightness, hue, aim hiding, per-weapon settings, Apply All, reset and export through the supported Laser UI.
- Existing battery/device behavior, with supported AUTO-hidden weapon light charge use paused rather than changing saved intent.

Availability depends on the selected backend and separately installed dependency. A GUI launcher is not a complete light or laser dependency.

## MCM configuration

**Light Linking** contains the shared Weapon Lights and Headlamps selectors and routing help. **Compatibility / Debug** shows detected integrations and optional Debug Mode; leave debug disabled for ordinary play. Brightness/beam/laser settings live in the supported device tuning dialogs, not extra invented MCM pages. Apply commits link choices; Reset/Cancel discard pending MCM edits.

## With One Key / without One Key

One Key controls gestures and menu; Unified owns advanced modes and reconciliation. Use matching 2.0 versions and matching FOMOD selections. Either companion order works when shared files match. One Key is optional; no third core is required. Removing Unified leaves One Key standalone OFF/ON; removing One Key leaves Unified usable through native/device controls and optional MGI.

## Limits, issues and help

The exact declared engine baseline and conditional dependencies are in [compatibility](COMPATIBILITY.md). Other engine builds/variants are unverified; the newer Auto NVG test baseline is not a Light compatibility certification. No unresolved gameplay defect is recorded for the accepted setup; separate gameplay acceptance of every alternative is not claimed.

See [troubleshooting](../../docs/TROUBLESHOOTING.md) for unavailable output, linking, tuning and file conflicts, or [report a reproducible bug](https://github.com/ProfessorMaterialistic/GAMMA-Mod-Releases/issues/new/choose).
