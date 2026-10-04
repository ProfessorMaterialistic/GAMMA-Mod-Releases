# One Key Light 2.0

Control installed player lights with **Tap, Double Tap, Hold**, or an on-screen **Quick Light Menu**. Use it alone for OFF/ON, or with Unified for advanced weapon/laser modes and NVG linking.

**Development: TESTED / FINAL-FOR-NOW. Public: release preparation; no GitHub download yet.** Owner acceptance was recorded 2026-10-01 for the accepted setup. Public release/redistribution approval remains separate.

[Install / update / remove](INSTALL.md) · [Requirements / MO2 order / compatibility](COMPATIBILITY.md) · [Changelog](CHANGELOG.md) · [Credits](CREDITS.md)

## Features

- Assign installed Headlamp, UTLF White, UTLF IR, Laser or IR Headlamp actions to three gestures; None and Quick Menu are also available.
- Quick Menu with device state, current output/route, real battery information when available, and unavailable-device locks.
- Standalone OFF/ON without Unified. With Unified, weapon/laser OFF/ON/AUTO and shared explicit Separate/NVG Linked settings.
- Normal and IR headlamp switching uses the existing GAMMA animations. Appropriate physical switch sounds come from the backend; One Key adds no duplicate sound.
- Optional manual vanilla Torch binding clear/restore with saved primary/secondary slots and conflict checks.

Feature integrations need their separately installed dependencies and matching FOMOD options. Missing integrations are not installed by assigning an action. See the [complete dependency table](COMPATIBILITY.md).

## Default controls

| Input | Default result |
| --- | --- |
| Mouse 5 Tap | Headlamp toggle |
| Mouse 5 Double Tap | UTLF White toggle, when installed |
| Mouse 5 Hold | Laser toggle, when installed |
| Shift + Mouse 5 | Quick Light Menu |
| Dedicated menu key | Unassigned until configured |

Tap waits for the **225 ms Double Tap Window** to resolve. Hold fires at **300 ms**, once per gesture, rather than repeatedly cycling while held. A completed Hold does not also fire Tap. MCM permits a 100–500 ms double window and 150–1000 ms hold threshold. Choose a practical main key in MCM; do not assume unverified extended keys are bindable.

Without Unified, actions toggle OFF/ON. With Unified, default **Smart ON/OFF** toggles based on current output: an emitting AUTO becomes OFF; a hidden AUTO becomes ON. Optional **OFF → ON → AUTO** cycles modes for supported weapon/laser devices. All headlamps still alternate OFF/ON.

## Quick Menu controls

Move the mouse to a sector; left click acts on it. Escape or the center closes/cancels. Tap-open menus can close with their opening key.

The **selection** setting offers:

- **Tap: click / Hold: release** (default): click for a tap-open menu, select the hovered action on releasing a held opener.
- **Left click only (release closes)**: hold the opener, click to change lights; release closes without another selection.
- **Release Opening Key**: select the hovered action when the opening key is released.

**Radial light selection** offers Single radial mode cycling, Two-step choose-a-mode, or Original quick toggle. The two-step picker offers only modes supported by the selected device. Explicit menu mode selection is independent of gesture preference. Without Unified, advanced mode controls remain unavailable.

Default right click cycles backward / chooses the highlighted mode. Alternatives close the radial, act like left click, or toggle OFF / last ON-or-AUTO. Linked device aliases fold into one menu action; **Hide Gesture-Bound Actions** can remove duplicate gesture targets. Movement while open follows normal bindings when enabled.

## MCM configuration

| Page | Settings |
| --- | --- |
| Controls | Enable, Main Light Control Key, explicit Weapon Lights/Headlamps linking with Unified, Tap/Double Tap/Hold assignments, timing, Gesture Behavior with Unified |
| Quick Menu | Dedicated key, modifier shortcut (Shift/Ctrl/Alt), selection, radial behavior/right click/movement/hiding, size/opacity, theme/icons/labels, state/battery/lock display and per-action visibility |
| Anomaly Torch Binding | Clear / Restore and current binding/conflict/persistent-disable status |
| Compatibility | Detected companion and backend integrations |

Appearance includes **25 themes**, Tactical or Minimal icons, and Icon + Text / Icon Only / Text Only labels. Missing icon initialization falls back to text. State indicator choices include words, marks or colored dots. Battery percentages are shown only when a backend supplies real charge; they are not fabricated for every device.

Apply commits MCM choices; Reset/Cancel discard pending changes. The link selectors edit Unified's shared state. Selecting an action or using a gesture does **not** silently change link mode.

## Limits, issues and help

Normal/IR/linked headlamps are OFF/ON only. Native/G2X beam tuning is limited to the separate preset setup. IR needs suitable equipment and deployed NVGs; linked IR failure remains dark rather than switching to visible light. Other engine variants and all optional configurations are not automatically covered by accepted gameplay evidence.

No unresolved gameplay defect is recorded for the accepted setup. See [compatibility](COMPATIBILITY.md) for scope and [troubleshooting](../../docs/TROUBLESHOOTING.md) for missing devices, file conflicts or bindings. [Report reproducible bugs](https://github.com/ProfessorMaterialistic/GAMMA-Mod-Releases/issues/new/choose).
