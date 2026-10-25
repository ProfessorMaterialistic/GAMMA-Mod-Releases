# Install or update Light 2.2.2

1. Save and close GAMMA and MO2. Keep a pre-update save and your current Light mods.
2. Install each .7z through MO2 as a new mod. If using both Light mods, update both
   to 2.2.2 and choose the same headlamp backend and integrations in both installers.
3. Select only integrations whose dependencies are installed. Keep existing backend
   choices when upgrading. The installers do not supply complete dependencies.
4. Disable the replaced Light entries and enable the new ones at their previous
   relative priorities. Keep later compatibility overrides in their existing order.
   Check conflicts: an older light script winning over the new pair can hide changes.
5. Keep existing MCM settings and keybinds; no reset or new game is required by this
   update. Open One Key Light > Controls to configure Momentary Hold and modifiers.

One Key and Unified also work separately. Without Unified, advanced AUTO and
linked-mode controls are unavailable. Headlamps remain OFF/ON; supported weapon
lights and lasers retain AUTO when using Unified.

## Animation continuity check

With Weapon Light ON, reload and inspect; repeat White/IR and NVG Linked.
Check inventory/PDA with the weapon visible and holstered, then Momentary Hold
release/cancel and sounds. AUTO can switch off when you leave its aiming policy.

## Sprint controls

For normal gestures while holding Shift, disable Shift Actions. If the active
Quick Menu modifier shortcut also uses Shift, change or disable that shortcut.
Enabled modifier groups use their own bindings, even if an action is None.

## Quick check

From an OFF weapon light, hold past the threshold: it should turn on with one
click and turn off with one click on release. Tap and Double Tap still perform
their own actions. Repeat with the desired modifier, NVGs and laser combination.
Apply and reopen Controls after changing a modifier enable checkbox.

## Rollback

Close the game and MO2, disable both new entries and re-enable your previous pair
at the same priorities. Use your preserved pre-update save if investigating a
save-related problem. Do not mix an old One Key version with a new Unified version.
