# 3D fit check

`index.html` is a self-contained 3D model of the deck (plain WebGL, no libraries, no build step). Open it in a browser to rotate it, open and close the lid, view each face, edit part sizes, and see which parts collide or do not fit.

## For agents and scripts

- All sizes are in millimetres.
- Case sizes are in the `PRESETS` array: interior width `W` and depth `D`, base depth `bd`, lid depth `ld`, wall thickness `ws`/`wf`/`wb`, floor `fl`.
- Parts are in the `defaults()` function. Each part has `x`, `y`, `z` (position) and `w`, `h`, `d` (size). `g` is `"base"` or `"lid"`. Base parts measure X from the inside left wall, Z from the inside back (hinge) wall, and Y from the inside floor. Lid parts measure Y as the gap from the lid's inside face. `solid: 0` parts (the top plate) are drawn but not collision-checked.
- The fit check runs with the lid closed. Its results are written to the `#summary` and `#issues` elements, so a headless browser (Playwright, Chromium with SwiftShader) can load the page and read them.
- Edits made in the browser are not saved. To change the model, edit the numbers in `index.html` and commit.
- Only the case sizes come from listings. Board, battery, keyboard, trackpad, toggle and adapter sizes are estimates until measured.
