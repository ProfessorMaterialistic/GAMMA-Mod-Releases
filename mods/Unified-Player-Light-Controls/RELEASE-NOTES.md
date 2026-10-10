# Changes from 2.0 to 2.1.0

- Preserve weapon flashlight emission during idle, primary fire and secondary fire
  states. Semi-auto shots no longer trigger Light's OFF/detach/recreate cycle.
- Reconcile meaningful availability changes instead of each idle/fire transition.
  Generated UTLF IR activation/recovery uses the same firing availability gate.
- Owner reports all ten gameplay tests PASS, including laser ON/AUTO and concurrent
  flashlight/laser. No separate laser shader rewrite was needed or performed.
- Coordinated 2.1.0 MCM/GUI labels, FOMOD metadata, delivery docs and archive names.

Existing gestures, radial modes/themes, native MCM navigation, linking, IR fail-dark,
headlamp animations/sounds, power/battery behavior and AUTO policies are preserved.
Headlamps remain OFF/ON; weapon/laser AUTO remains conditional on capabilities.

Final distribution adds scoped license notices and portable corresponding source.
Runtime and asset bytes are unchanged from the accepted 2.1.0 review packages.
