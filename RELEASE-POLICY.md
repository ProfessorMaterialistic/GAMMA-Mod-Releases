# Release Policy

## Purpose

This repository is a clean public distribution surface. The private development repository remains the authoritative location for source-state tracking, experiments, diagnostics, and unreleased work.

## Public release gate

A mod should not be published here merely because code exists or a build succeeds.

Before publishing a normal release:

- gameplay scope required for the release is TESTED;
- release package is built from known source/revision;
- dependencies are identified;
- installation and upgrade path are documented;
- known issues are written down;
- redistributed third-party material is reviewed for permission/license requirements;
- credits and attribution are complete;
- archive contents are inspected for private/local files;
- checksums are recorded where useful;
- rollback/uninstall instructions exist for anything that touches shared engine/runtime files.

## Version naming

Prefer per-project semantic versions:

- `one-key-light-v2.0.0`
- `unified-player-light-controls-v2.0.0`
- `beefs-nvg-agc-v0.4.0`
- `grenades-expanded-v0.1.0`

Release candidates may use suffixes such as `-rc.1`.

Do not publish internal diagnostic identifiers as stable releases.

## Release contents

A GitHub Release should contain:

1. clean distributable archive;
2. concise release notes;
3. install/update instructions;
4. dependency and compatibility notes;
5. known issues;
6. credits/licenses;
7. SHA-256 checksum when practical.

## Engine-dependent projects

A release that requires a custom executable must state the exact supported engine lineage and compatibility assumptions.

Do not distribute an engine binary unless its redistribution requirements have been reviewed and cleared. If binary redistribution is not appropriate, publish source patches/build instructions instead.

## Private material exclusion

Never publish:

- machine-specific absolute paths;
- MO2 profile backups;
- save files;
- private rollback archives;
- authentication tokens or secrets;
- private development history that is not intentionally public;
- third-party assets without redistribution permission;
- diagnostic binaries that have not cleared the public release gate.
