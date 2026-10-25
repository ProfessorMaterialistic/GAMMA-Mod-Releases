# Light 2.2.1 corresponding source

Run `python reproduce.py` from a clean source copy with Python 3. It writes only
`build/`, stages both full installers and verifies every package member against
PACKAGE-MANIFEST.json. It never accesses a game installation, MO2 or private data.
Compress each built package folder with 7-Zip if an installable archive is needed.

`canonical/`, `onekey/` and `unified/` are preferred maintained runtime modules.
`tools/tactical_patch.py` and `tools/laser_output_patch.py` own changes to retained
integration facades. Exact readable inputs live in `retained/`; earlier upstream
transformations, their inputs and original drawing source are in
`upstream-generation/`. Pillow is needed only to redraw artwork, not to reproduce
the retained release. Runtime dependencies are installed separately.

The accepted 2.2.1-rc.1 gameplay source is unchanged except display version labels.
The optional bounded laser diagnostic is a user-invoked support feature, disabled
by default; private diagnostics, logs and machine information are not included.
Original credits, scoped GPL/AGPL/MIT notices and source disclosures are retained.
