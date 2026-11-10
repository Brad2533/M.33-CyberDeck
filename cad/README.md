# CAD exports

Generated from `fit-check/index.html` by `fit-check/export_cad.py`. Do not edit these by hand. Change the numbers in `index.html`, then rerun:

    python3 fit-check/export_cad.py              # Pelican 1470, lid open 105 degrees
    python3 fit-check/export_cad.py --case 1     # another case preset

Units are millimetres. Axes: X left to right, Y toward the back (hinge), Z up.

| File | Opens in | Use |
| --- | --- | --- |
| `cyberdeck.scad` | OpenSCAD | Parametric model. Change `lid_angle` (0 is closed) and the `show_*` switches. Set `ghost_shell = false` before exporting so the shell is included. |
| `assembly-closed.obj`, `assembly-open.obj` | Fusion 360, Blender, FreeCAD, most 3D viewers | Whole deck with part names and colours (`.mtl` files hold the colours). |
| `assembly-closed.stl`, `assembly-open.stl` | Any CAD tool or slicer | Whole deck as one mesh, no colours. |
| `parts/<id>.stl` | Any CAD tool or slicer | Each part on its own, at its closed position, for placing against your own designs. |

Limits:

- Every part is a plain box at approximate size. Only the case sizes come from listings.
- The meshes are overlapping boxes, not one merged solid, so they are for fit and layout, not for printing as is.
- There is no STEP file, because no CAD kernel was available to make one. FreeCAD can open the `.scad` (with OpenSCAD installed) or the meshes and save a STEP.
- The charging port is left out on purpose.
