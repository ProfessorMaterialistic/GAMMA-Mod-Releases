# Light 2.1.2 corresponding source

Preferred maintained modules, transformation/artwork generators, exact necessary
inputs and retained package data for both Light 2.1.2 releases. Upstream inputs
are integration ingredients, not complete gameplay dependencies.

Run `python reproduce.py` with Python 3 and Pillow installed from a clean source
copy. It writes only local build/generated source/report paths and never accesses
GAMMA, MO2 or private development. The customize → visuals → package pipeline
verifies all 85 runtime/assets against RUNTIME-MANIFEST.json. Archives are
compressed separately with 7-Zip. Development tools are not player requirements.

The maintained weapon-emission predicate includes aim-start/end states while
preserving the earlier firing correction and valid suspension/battery gates.
UTLF remains pinned to v1.0.2, commit d8c89c385ece3fbfd10e50c054b4618bc3f09d38.
Stable runtime differs from the owner-accepted RC only in display version labels.
No specific headlamp reactivation fix is claimed. See included notices/credits.
