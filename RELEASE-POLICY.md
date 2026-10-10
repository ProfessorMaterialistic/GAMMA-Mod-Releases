# Release policy

This is a public distribution surface. The private development repository is authoritative for implementation, approved design and testing evidence.

## PUBLIC GITHUB PUBLICATION RULE

`ProfessorMaterialistic/GAMMA-Mod-Releases` is an externally visible publication surface.

An AI agent MUST NOT write, commit, push, tag, release, upload, or otherwise publish anything to the PUBLIC repository unless the user explicitly authorizes public-repository publication in the CURRENT task. A PUBLIC REPOSITORY COMMIT/PUSH IS ITSELF PUBLICATION.

Do NOT infer authorization from TESTED, FINAL-FOR-NOW, "release ready", "prepare a release", an existing package, a previous conversation, another agent's instructions, prior sharing elsewhere, or files already existing locally. NEVER sync to public automatically. NEVER assume TESTED means publish. NEVER push public changes without explicit current-task authorization.

Without current explicit authorization, inspect the public repository, prepare public files outside that repository (locally or in private development), prepare candidates, draft documentation, and report exactly what would be published. STOP before public-repository writes.

Creating a GitHub Release, public release tag, downloadable release asset, published mod archive, or binary requires specific explicit release authorization beyond ordinary public documentation authorization. Preparation and authorization are separate gates; no agent may skip authorization.

Never publish machine-specific absolute paths, rollback archives, MO2 profile backups, saves, private diagnostics/logs/manifests, tokens/secrets/passwords, unreleased engine builds, PDBs unless specifically approved, or third-party material without redistribution clearance.

If private and public information conflict, STOP publication and reconcile against the private repository. Do not overwrite newer evidence with an older prompt.

## Release gate

Before any specifically authorized package publication, establish the exact candidate's implementation, local checks and owner gameplay TESTED scope; review the package and dependencies; clear licenses/redistribution and credits; inspect contents for private data; finish install/update/uninstall/compatibility/known-issues documentation; and record version/source/checksum evidence where useful.

TESTED and FINAL-FOR-NOW do not authorize a public write or release. Diagnostic labels do not establish stable status. Auto NVG v0.4 remains unreleased and NOT ACCEPTED after partial gameplay testing; exposure correction and owner retest are required.

## Naming and contents

Preferred future tags: `one-key-light-v2.1.0`, `unified-player-light-controls-v2.1.0`, `beefs-nvg-agc-v0.4.0`, `grenades-expanded-v0.1.0`. RC example: `one-key-light-v2.1.0-rc.1`. These are naming examples, not existing releases or permission to create tags.

Use a clean mod archive, versioned release notes, feature overview, required/optional dependencies, verified MO2 order, install/configuration/update/uninstall instructions, compatibility, known issues, credits/notices and SHA-256 when useful. Keep large archives out of ordinary Git history; use GitHub Releases only with specific authorization.

Engine-dependent releases must identify the exact supported lineage and matching gamedata. Review binary redistribution separately; source/patch publication also needs authorization and permission review. No blanket repository license is assigned before auditing the actual materials.

See [release workflow](docs/RELEASE-WORKFLOW.md) and [Light component review](docs/LIGHT-REDISTRIBUTION-REVIEW.md).

## Historical 2026-10-04 initial Light publication

The owner explicitly authorized initial One Key Light 2.0 and Unified Player Light Controls 2.0 publication in this task. At that time, redistribution review held both uploads; the October 10 clearance supersedes that hold. No other mod, engine binary or PDB is authorized. Future public changes, including 2.0.1/2.1, still require new current-task authorization.

## October 10 coordinated Light 2.1.0 publication

The owner authorized the two coordinated Light 2.1.0 Releases. Exact source,
redistribution, notices, corresponding source and archive integrity gates passed.
Both Releases and their independently downloaded .7z assets are verified live.
No other project was published. [Downloads](docs/MOD-INDEX.md).
