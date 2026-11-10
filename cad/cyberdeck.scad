// M.33 CyberDeck fit-check model, generated from fit-check/index.html by export_cad.py.
// Units: millimetres. Axes: X left to right, Y toward the back (hinge), Z up.
// Case: Pelican 1470. Part sizes other than the case are estimates until measured.
// Change lid_angle (0 = closed) and the show_* switches, then press F5 or F6.
// Edit sizes here for quick tries, but edit index.html and rerun the exporter to keep both in sync.

lid_angle = 105;
show_shell = true;
ghost_shell = true; // see-through in preview (F5); set false so F6 render and STL export include the shell
show_parts = true;
show_extras = true;

W = 399;
D = 272;
bd = 61;
ld = 37;
ws = 15;
wf = 32;
wb = 32;
fl = 8;

// Page frame box [x, y_up, z_front, w, h, d] -> CAD cube.
module pbox(b, col) { color(col) translate([b[0], -(b[2] + b[5]), b[1]]) cube([b[3], b[5], b[4]]); }
module lid_frame() { translate([0, wb, bd]) rotate([-lid_angle, 0, 0]) translate([0, -wb, -bd]) children(); }

module shell_base() {
  pbox([-15, -8, -32, 429, 8, 336], [0.23, 0.26, 0.31]);
  pbox([-15, 0, -32, 15, 61, 336], [0.23, 0.26, 0.31]);
  pbox([399, 0, -32, 15, 61, 336], [0.23, 0.26, 0.31]);
  pbox([0, 0, -32, 399, 61, 32], [0.23, 0.26, 0.31]);
  pbox([0, 0, 272, 399, 61, 32], [0.23, 0.26, 0.31]);
}
module shell_lid() {
  pbox([-15, 98, -32, 429, 8, 336], [0.23, 0.26, 0.31]);
  pbox([-15, 61, -32, 15, 37, 336], [0.23, 0.26, 0.31]);
  pbox([399, 61, -32, 15, 37, 336], [0.23, 0.26, 0.31]);
  pbox([0, 61, -32, 399, 37, 32], [0.23, 0.26, 0.31]);
  pbox([0, 61, 272, 399, 37, 32], [0.23, 0.26, 0.31]);
}
module extras_base() {
  pbox([20, 10, -34, 130, 28, 2], [0.56, 0.78, 0.75]); // Fan exhaust vent (back)
  pbox([269, 10, -34, 90, 28, 2], [0.89, 0.54, 0.23]); // Battery membrane vent (back)
  pbox([-17, 10, 30, 2, 28, 100], [0.55, 0.6, 0.66]); // Port panel (left end)
  pbox([-25, 35, -22, 10, 20, 30], [0.78, 0.8, 0.84]); // Corner clip back left
  pbox([414, 35, -22, 10, 20, 30], [0.78, 0.8, 0.84]); // Corner clip back right
  pbox([-25, 35, 264, 10, 20, 30], [0.78, 0.8, 0.84]); // Corner clip front left
  pbox([414, 35, 264, 10, 20, 30], [0.78, 0.8, 0.84]); // Corner clip front right
  pbox([87.78, 43, 304, 34, 16, 6], [0.16, 0.19, 0.22]); // Latch left (base half)
  pbox([277.22, 43, 304, 34, 16, 6], [0.16, 0.19, 0.22]); // Latch right (base half)
}
module extras_lid() {
  pbox([414, 73.5, 84, 10, 12, 12], [0.55, 0.59, 0.64]); // RP-SMA bulkhead 1
  pbox([424, 75.5, 86, 100, 8, 8], [0.16, 0.19, 0.22]); // Antenna 1
  pbox([414, 73.5, 144, 10, 12, 12], [0.55, 0.59, 0.64]); // RP-SMA bulkhead 2
  pbox([424, 75.5, 146, 100, 8, 8], [0.16, 0.19, 0.22]); // Antenna 2
  pbox([87.78, 63, 304, 34, 16, 6], [0.16, 0.19, 0.22]); // Latch left (lid half)
  pbox([277.22, 63, 304, 34, 16, 6], [0.16, 0.19, 0.22]); // Latch right (lid half)
}

// Parts: [x, y, z, w, h, d] as in the fit-check table. Lid parts use y = gap from the lid's inside face.
module parts_base() {
  pbox([12, 5, 6, 170, 28, 170], [0.12, 0.5, 0.48]); // Bare board with cooler
  pbox([235, 4, 8, 160, 35, 100], [0.89, 0.54, 0.23]); // Battery pack, 150 to 200 Wh
  pbox([222, 0, 0, 4, 50, 150], [0.1, 0.11, 0.13]); // Wall between bays
  pbox([188, 4, 10, 30, 15, 50], [0.45, 0.62, 0.3]); // 5 V converter
  pbox([196, 4, 120, 16, 25, 16], [0.84, 0.2, 0.2]); // Shutdown button
  pbox([232, 4, 112, 86, 20, 63], [0.2, 0.33, 0.62]); // Capture adapter
  pbox([322, 4, 114, 60, 12, 25], [0.35, 0.42, 0.72]); // USB hub
  pbox([322, 4, 145, 60, 20, 40], [0.5, 0.4, 0.7]); // USB switch (pass-through)
  pbox([0, 50, 155, 399, 3, 117], [0.3, 0.35, 0.42]); // Top plate (front zone)
  pbox([8, 35, 163, 295, 38, 105], [0.4, 0.46, 0.54]); // 60% keyboard
  pbox([318, 30, 160, 20, 48, 32], [0.8, 0.22, 0.22]); // Toggle 1: board power
  pbox([344, 30, 160, 20, 48, 32], [0.8, 0.22, 0.22]); // Toggle 2: screen power
  pbox([370, 30, 160, 20, 48, 32], [0.8, 0.22, 0.22]); // Toggle 3: pass-through
  pbox([318, 53, 200, 72, 5, 48], [0.13, 0.16, 0.2]); // Trackpad
  pbox([318, 53, 252, 34, 6, 14], [0.2, 0.24, 0.29]); // Mouse button, left
  pbox([356, 53, 252, 34, 6, 14], [0.2, 0.24, 0.29]); // Mouse button, right
}
module parts_lid() {
  pbox([72, 84, 54, 255, 12, 165], [0.06, 0.09, 0.11]); // Screen, 10.1 in panel
}

if (show_shell) { if (ghost_shell) { %shell_base(); lid_frame() %shell_lid(); } else { shell_base(); lid_frame() shell_lid(); } }
if (show_extras) { extras_base(); lid_frame() extras_lid(); }
if (show_parts) { parts_base(); lid_frame() parts_lid(); }
