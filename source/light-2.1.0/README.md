# Light 2.1.0 corresponding source

This directory contains the preferred maintained Lua modules, transformation and
artwork generators, exact necessary generation inputs and retained package data.
The inputs are source ingredients for these integrations, not complete external
dependency distributions. Install external dependencies separately for gameplay.

Run `python reproduce.py` with Python 3 and Pillow installed. It writes only to
this directory's `build/` and generated source/report paths. It never accesses an
installed game, MO2 profile or private development repository. The ordered build
runs customize (which imports build), visuals, then package; do not import build
again after customization. Every generated runtime/asset is compared against the
versioned manifest. Archives are compressed separately with 7-Zip.

The package Lua/XML files are readable source. Runtime APIs come from the
separately installed GAMMA/MCM/UTLF host described in the compatibility guides.
See LICENSE-NOTICES.md, MODIFICATIONS.md and CREDITS.md for terms and authors.
