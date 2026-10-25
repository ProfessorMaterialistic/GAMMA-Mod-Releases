# Light 2.2.1 controls

Headlamp and Weapon Light automatically choose White/IR according to Light Linking.
Laser controls the supported weapon laser. Explicit actions are Headlamp - White
Light, Headlamp - IR, Weapon Light - White Light and Weapon Light - IR. None and
Quick Menu remain utility choices.

## Momentary Hold

- None
- Weapon Light (Temporary)
- Weapon Light + Laser (Temporary)
- Laser (Temporary)
- Weapon Light - White Light (Temporary)
- Weapon Light - IR (Temporary)

Momentary starts at the existing Hold Threshold (300 ms by default). It replaces
only Hold for that route, leaving Tap and Double Tap available. Release restores
previous lighting, including saved OFF/ON/AUTO intent. Equipment loss, menus and
other invalid contexts cancel the hold. NVG changes require release and a new hold.

## MCM and Quick Menu

Each ALT / CTRL / SHIFT + LIGHT KEY group has an enable checkbox and Tap, Double
Tap, Hold and Momentary Hold. Apply and reopen Controls to update row visibility.
The unmodified key remains independent. Use one modifier at a time.

Keep existing gesture behavior, timing, separate Quick Menu key, native Torch
binding clear/restore, radial selection and right-click preferences. The Quick
Menu includes three saved profiles, per-action order/visibility/icons, accent
color, 25 themes, labels and device-state/battery indicators. Profiles do not
overwrite your keys. Missing icon initialization falls back to text.

Unified retains saved modes, tuning and aim policies, per-weapon laser intent,
separate/NVG-linked routing and supported integration dialogs. Existing headlamp
animations and device sounds remain owned by their original integration modules.
