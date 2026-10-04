# Public mod documentation standard

Write for a player installing the exact package. Inspect source, MCM, final FOMOD/package mappings, tested status, build inputs and real MO2 winner evidence. Do not promote design notes into implemented features.

| Section | Required content |
| --- | --- |
| Overview | What the mod does, why to use it, concise feature list |
| Status | Actual public version/channel or unreleased status; evidence scope and last verified baseline |
| Requirements | Separate REQUIRED, OPTIONAL, and INCOMPATIBLE / UNSUPPORTED; exact names, purpose, versions, feature conditions, links when verified |
| MO2 order | Simple file-priority example; dependency/mod/patch placement supported by source/package/tested evidence; explain missing evidence if uncertain |
| Installation | Actual download availability, archive/MO2/FOMOD flow, choices, enable step, first launch, MCM and any key takeover |
| Features | Every implemented player-facing feature; distinguish unavailable equipment from an uninstalled integration |
| Controls | Defaults, bindings, gestures/timing, modifiers, menu actions, cycle/toggle and binding restore |
| Configuration | Important settings and effects in player language; distinguish MCM from separate tuning dialogs |
| Compatibility | GAMMA/Anomaly and engine baseline, integrations, unsupported/unverified combinations, companion behavior |
| Update | Safe replacement and settings/migration instructions |
| Uninstall / rollback | Disable/restore flow, vanilla bindings and dependency behavior, what settings remain |
| Known issues | Actual current defects only; distinguish expected limits and untested configurations |
| Troubleshooting | Concrete symptom, checks and remedy; sanitized bug-report link |
| Credits | Original authorship, derived files, dependencies, assets, license notices and unresolved exact components |
| Changelog | Player-facing history; unreleased entries labeled; no raw engineering history |

Use README for overview/features/controls/settings; INSTALL for setup/update/removal; COMPATIBILITY for dependency/order/limits; CREDITS and CHANGELOG for provenance and history. Relative links must work. Avoid empty placeholder files and invented release/download links.

Before a release, check [release workflow](RELEASE-WORKFLOW.md), including explicit current-task publication authorization. No private paths, settings, logs, backups, manifests, binaries or unapproved upstream material belong in public documentation.
