# Public roadmap

[Home](README.md) · [Showcase](docs/LIGHT-SHOWCASE-CHECKLIST.md) · [Release workflow](docs/RELEASE-WORKFLOW.md)

Updated 2026-10-04. Release status is separate from development evidence and explicit authorization.

```mermaid
flowchart TD
    L["One Key + Unified TESTED / FINAL-FOR-NOW"] --> V["Showcase clip recorded COMPLETE"]
    V --> P["Public release preparation<br/>initial Light releases authorized"]
    P --> C{"Bundled redistribution review<br/>pending clearance"}
    C --> O["One Key 2.0 release PENDING"]
    O --> U["Unified 2.0 release PENDING"]
    U --> D["Discord post PENDING"]
    A["Auto NVG v0.4 gameplay testing"] --> F["Exposure-control defects found"]
    F --> X["v0.4.1 correction planned"] --> T["Owner retest"]
    T --> R["Future release decision<br/>new explicit authorization required"]
    G["Grenades Expanded<br/>in development"]
    K["GEKF<br/>future / not implemented"]
```

## Light releases and community

- [x] Both Light mods TESTED / FINAL-FOR-NOW for the accepted setup.
- [x] Owner recorded showcase clip.
- [x] Current task explicitly authorizes the two initial Light 2.0 releases.
- [x] Inspect unchanged final package runtime, FOMOD and dependency file priority; prepare documentation and local archives.
- [ ] Clear [exact bundled redistribution](docs/LIGHT-REDISTRIBUTION-REVIEW.md).
- [ ] Publish One Key Light 2.0 and verify archive download.
- [ ] Publish Unified Player Light Controls 2.0 and verify archive download.
- [x] Place exact approved [banner screenshot](assets/README.md).
- [ ] Post clip to Discord; no completed-post evidence supplied.

## Auto NVG

v0.4 underwent gameplay testing. Core Bodycam migration and controls worked in the tested scope. Exposure-control defects remain; **v0.4.1 correction is planned**, followed by owner retest and a future release decision. **No public download is available.**

## Grenades and GEKF

Grenades remains in development; radial design remains IDEA until explicitly locked. GEKF is a future framework with DECIDED architecture, not implemented on the maintained engine base. It follows a stable engine baseline, historical recovery and locked implementation spec.

## Evidence states

IDEA → DECIDED → IMPLEMENTED → LOCALLY VALIDATED → TESTED → FINAL-FOR-NOW. Never infer later states. Public release is a separate distribution decision. Future public changes, including Light 2.0.1/2.1, require new explicit current-task authorization.
