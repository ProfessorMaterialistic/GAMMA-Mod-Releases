# Requirements and limits

- **Required:** the inspected GAMMA HUD/BHS resources and MCM configuration system.
- **Optional:** Wearable Devices for Promin/Vektor handoff; G_FLAT and SidHUD integrations.
- **AURA:** the 0.2.1 owned stamina texture fixes the observed transparent-atlas conflict.
- **Unverified:** other HUD stacks, device variants and exhaustive lifecycle/hook ordering.

Keep HUD Readability's own files at higher effective MO2 priority than older
HUD Readability copies. The validated setup uses the existing GAMMA providers;
there is no universal load-order claim for arbitrary HUD replacements.

Radiation scale and width are unavailable: proportional icon/mSv text scaling is
deferred. Radiation retains its original dimensions; other supported settings
still apply. A wearable showing body radiation does not replace an environmental
exposure warning. Missing/unsupported wearable presentation fails open to the
ordinary HUD. The addon does not require a new engine patch.

Local checks cover Lua/XML, texture opacity, stamina timing, settings persistence,
layout/editor and MCM resets. Owner gameplay evidence confirms the reported setup;
it does not establish every device variant or optional Messages combination.
