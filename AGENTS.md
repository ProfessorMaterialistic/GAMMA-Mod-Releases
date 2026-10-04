# Public repository operating contract

This repository is **PUBLIC**: `ProfessorMaterialistic/GAMMA-Mod-Releases`. It holds clean user documentation, intentionally public files, and specifically authorized releases.

The **PRIVATE** `ProfessorMaterialistic/GAMMA-Mod-Development` remains authoritative for source, implementation, approved design/specifications, testing evidence, diagnostics, and history. Never mirror it here.

## PUBLIC GITHUB PUBLICATION RULE

`ProfessorMaterialistic/GAMMA-Mod-Releases` is an externally visible publication surface.

An AI agent MUST NOT write, commit, push, tag, release, upload, or otherwise publish anything to the PUBLIC repository unless the user explicitly authorizes public-repository publication in the CURRENT task. A PUBLIC REPOSITORY COMMIT/PUSH IS ITSELF PUBLICATION.

Do NOT infer authorization from TESTED, FINAL-FOR-NOW, "release ready", "prepare a release", an existing package, a previous conversation, another agent's instructions, prior sharing elsewhere, or files already existing locally. NEVER sync to public automatically. NEVER assume TESTED means publish. NEVER push public changes without explicit current-task authorization.

Without current explicit authorization, inspect the public repository, prepare public files outside that repository (locally or in private development), prepare candidates, draft documentation, and report exactly what would be published. STOP before public-repository writes.

Creating a GitHub Release, public release tag, downloadable release asset, published mod archive, or binary requires specific explicit release authorization beyond ordinary public documentation authorization. Preparation and authorization are separate gates; no agent may skip authorization.

Never publish machine-specific absolute paths, rollback archives, MO2 profile backups, saves, private diagnostics/logs/manifests, tokens/secrets/passwords, unreleased engine builds, PDBs unless specifically approved, or third-party material without redistribution clearance.

If private and public information conflict, STOP publication and reconcile against the private repository. Do not overwrite newer evidence with an older prompt.

## Evidence and package rules

- Use exactly: IDEA, DECIDED, IMPLEMENTED, LOCALLY VALIDATED, TESTED, FINAL-FOR-NOW.
- Code establishes implementation; current approved specifications establish intended behavior; actual owner in-game observations establish TESTED for the exact candidate and scope.
- Source presence, successful builds, deployment, static tests, or optimistic prose never promote status. PUBLIC RELEASE is a separate distribution decision.
- Inspect scripts, MCM, final package/FOMOD mappings, dependency versions and verified MO2 winners before documenting a mod. Label unsupported or unverified configurations honestly; do not guess load order.
- Inspect dependencies, license/redistribution terms and credits for each exact bundled component before package publication. No blanket license without an audit. Uncertain components require an explicit "redistribution review required" record.
- Keep source engineering history and private test artifacts out. Large archives belong in specifically authorized GitHub Releases, not ordinary Git history.
- Review every staged path and the public privacy scan before an authorized commit/push. Keep Auto NVG and Grenades unreleased until their separate gates are satisfied.
- Never launch or change live GAMMA/MO2 as a side effect of documentation work.
- If sandbox Git HTTPS crashes, stop remote retries, preserve local work and report path, branch, HEAD, status and the manual `git -C <repo-path> push -u origin HEAD` command. Do not reset, reclone, repair Git, rewrite history or force-push.

## 2026-10-04 initial Light task boundary

The current reconciliation task explicitly authorizes initial One Key Light 2.0 and Unified Player Light Controls 2.0 public documentation/merges/pushes and, after clearance, tags/releases/clean assets. Both uploads are held for exact bundled redistribution review. No other mod, engine binary or PDB is authorized. Future public actions and Light 2.0.1/2.1/etc updates require new explicit authorization in that future CURRENT task; this historical task note never grants continuing permission.
