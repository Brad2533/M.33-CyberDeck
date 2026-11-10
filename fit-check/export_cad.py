#!/usr/bin/env python3
"""Export the M.33 CyberDeck fit-check model to CAD-friendly files.

Reads the case presets and parts straight from fit-check/index.html, so the
CAD files always match the 3D page. Run from the repo root or anywhere:

    python3 fit-check/export_cad.py            # Pelican 1470, lid open 105 deg
    python3 fit-check/export_cad.py --case 1 --open-angle 90

Writes to cad/:
    cyberdeck.scad              parametric OpenSCAD model (edit numbers, change lid_angle)
    assembly-closed.stl/.obj    whole deck, lid closed (OBJ keeps part colours and names)
    assembly-open.stl/.obj      whole deck, lid open
    parts/<id>.stl              each part on its own, at its closed position

Units are millimetres. CAD axes: X left to right, Y toward the back (hinge),
Z up. The inside front-left corner of the base floor is at X=0, Z=0, and the
inside front wall is at Y = -D (depth).
"""
import argparse, math, os, re, struct

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)


def num(s):
    return float(s)


def load(html_path):
    src = open(html_path, encoding="utf-8").read()
    presets = []
    pblock = re.search(r"var PRESETS = \[(.*?)\n\];", src, re.S).group(1)
    for m in re.finditer(r"\{name:\"([^\"]+)\"([^}]*)\}", pblock):
        d = {"name": m.group(1)}
        for k, v in re.findall(r"(\w+):(-?[\d.]+)", m.group(2)):
            d[k] = num(v)
        presets.append(d)
    parts = []
    dblock = re.search(r"function defaults\(\)\{ return \[(.*?)\n\];\}", src, re.S).group(1)
    for m in re.finditer(r"\{id:\"([^\"]+)\", name:\"([^\"]+)\", g:\"(\w+)\",([^\n]*)\}", dblock):
        d = {"id": m.group(1), "name": m.group(2), "g": m.group(3)}
        rest = m.group(4)
        col = re.search(r"c:\[([^\]]+)\]", rest).group(1)
        d["c"] = [num(v) for v in col.split(",")]
        rest = re.sub(r"c:\[[^\]]+\]", "", rest)
        for k, v in re.findall(r"(\w+):(-?[\d.]+)", rest):
            d[k] = num(v)
        parts.append(d)
    return presets, parts


# ---- geometry in the page's own frame (x right, y up, z toward the front) ----

def part_box(p, P):
    y0 = P["bd"] + P["ld"] - p["y"] - p["h"] if p["g"] == "lid" else p["y"]
    return [p["x"], y0, p["z"], p["w"], p["h"], p["d"]]


def shell_boxes(P):
    W, D, bd, ld, ws, wf, wb, fl = (P[k] for k in ("W", "D", "bd", "ld", "ws", "wf", "wb", "fl"))
    top = bd + ld
    base = [[-ws, -fl, -wb, W + 2 * ws, fl, D + wf + wb], [-ws, 0, -wb, ws, bd, D + wf + wb],
            [W, 0, -wb, ws, bd, D + wf + wb], [0, 0, -wb, W, bd, wb], [0, 0, D, W, bd, wf]]
    lid = [[-ws, top, -wb, W + 2 * ws, fl, D + wf + wb], [-ws, bd, -wb, ws, ld, D + wf + wb],
           [W, bd, -wb, ws, ld, D + wf + wb], [0, bd, -wb, W, ld, wb], [0, bd, D, W, ld, wf]]
    return base, lid


def extras(P):
    W, D, bd, ld, ws, wf, wb = (P[k] for k in ("W", "D", "bd", "ld", "ws", "wf", "wb"))
    g, k = [0.78, 0.80, 0.84], [0.16, 0.19, 0.22]
    vh = min(28, bd - 16)
    ay = bd + ld / 2 - 4
    base = [("vent_exhaust", "Fan exhaust vent (back)", [20, 10, -wb - 2, 130, vh, 2], [0.56, 0.78, 0.75]),
            ("vent_membrane", "Battery membrane vent (back)", [W - 130, 10, -wb - 2, 90, vh, 2], [0.89, 0.54, 0.23]),
            ("port_panel", "Port panel (left end)", [-ws - 2, 10, 30, 2, vh, 100], [0.55, 0.60, 0.66]),
            ("clip_bl", "Corner clip back left", [-ws - 10, bd - 26, -wb + 10, 10, 20, 30], g),
            ("clip_br", "Corner clip back right", [W + ws, bd - 26, -wb + 10, 10, 20, 30], g),
            ("clip_fl", "Corner clip front left", [-ws - 10, bd - 26, D + wf - 40, 10, 20, 30], g),
            ("clip_fr", "Corner clip front right", [W + ws, bd - 26, D + wf - 40, 10, 20, 30], g),
            ("latch_l_base", "Latch left (base half)", [W * 0.22, bd - 18, D + wf, 34, 16, 6], k),
            ("latch_r_base", "Latch right (base half)", [W * 0.78 - 34, bd - 18, D + wf, 34, 16, 6], k)]
    lid = [("sma_1", "RP-SMA bulkhead 1", [W + ws, ay - 2, 84, 10, 12, 12], [0.55, 0.59, 0.64]),
           ("ant_1", "Antenna 1", [W + ws + 10, ay, 86, 100, 8, 8], k),
           ("sma_2", "RP-SMA bulkhead 2", [W + ws, ay - 2, 144, 10, 12, 12], [0.55, 0.59, 0.64]),
           ("ant_2", "Antenna 2", [W + ws + 10, ay, 146, 100, 8, 8], k),
           ("latch_l_lid", "Latch left (lid half)", [W * 0.22, bd + 2, D + wf, 34, 16, 6], k),
           ("latch_r_lid", "Latch right (lid half)", [W * 0.78 - 34, bd + 2, D + wf, 34, 16, 6], k)]
    return base, lid


def to_cad(b):
    """Page box [x,y,z,w,h,d] -> CAD box origin and size (X right, Y back, Z up)."""
    x, y, z, w, h, d = b
    return [x, -(z + d), y], [w, d, h]


def box_corners(o, s):
    x, y, z = o
    w, d, h = s
    return [(x + i * w, y + j * d, z + k * h) for i in (0, 1) for j in (0, 1) for k in (0, 1)]


def hinge_rotate(pts, P, angle_deg):
    """Open the lid: rotate about the hinge line (along X at Y=wb, Z=bd)."""
    if not angle_deg:
        return pts
    a = math.radians(-angle_deg)
    c, s = math.cos(a), math.sin(a)
    hy, hz = P["wb"], P["bd"]
    out = []
    for x, y, z in pts:
        dy, dz = y - hy, z - hz
        out.append((x, hy + dy * c - dz * s, hz + dy * s + dz * c))
    return out


# corner index = i*4 + j*2 + k  (i: x, j: y, k: z)
QUADS = [(0, 1, 3, 2), (4, 6, 7, 5), (0, 4, 5, 1), (2, 3, 7, 6), (0, 2, 6, 4), (1, 5, 7, 3)]


def tris(c):
    t = []
    for a, b, cc, d in QUADS:
        t.append((c[a], c[b], c[cc]))
        t.append((c[a], c[cc], c[d]))
    return t


def normal(t):
    (ax, ay, az), (bx, by, bz), (cx, cy, cz) = t
    ux, uy, uz = bx - ax, by - ay, bz - az
    vx, vy, vz = cx - ax, cy - ay, cz - az
    nx, ny, nz = uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx
    l = math.sqrt(nx * nx + ny * ny + nz * nz) or 1
    return nx / l, ny / l, nz / l


def write_stl(path, triangles, name):
    with open(path, "wb") as f:
        f.write(name.encode()[:80].ljust(80, b" "))
        f.write(struct.pack("<I", len(triangles)))
        for t in triangles:
            f.write(struct.pack("<3f", *normal(t)))
            for v in t:
                f.write(struct.pack("<3f", *v))
            f.write(b"\0\0")


def build(P, parts, angle):
    """Return list of (id, name, colour, corners) for the assembly."""
    items = []
    sb, sl = shell_boxes(P)
    eb, el = extras(P)
    shell = [0.23, 0.26, 0.31]
    for i, b in enumerate(sb):
        items.append(("shell_base_%d" % i, "Case base shell", shell, box_corners(*to_cad(b))))
    for i, b in enumerate(sl):
        items.append(("shell_lid_%d" % i, "Case lid shell", shell, hinge_rotate(box_corners(*to_cad(b)), P, angle)))
    for pid, name, b, col in eb:
        items.append((pid, name, col, box_corners(*to_cad(b))))
    for pid, name, b, col in el:
        items.append((pid, name, col, hinge_rotate(box_corners(*to_cad(b)), P, angle)))
    for p in parts:
        c = box_corners(*to_cad(part_box(p, P)))
        if p["g"] == "lid":
            c = hinge_rotate(c, P, angle)
        items.append((p["id"], p["name"], p["c"], c))
    return items


def write_obj(path, items):
    mtl = os.path.splitext(path)[0] + ".mtl"
    with open(mtl, "w") as m:
        for pid, name, col, _ in items:
            m.write("newmtl m_%s\nKd %.3f %.3f %.3f\n\n" % (pid, col[0], col[1], col[2]))
    with open(path, "w") as f:
        f.write("# M.33 CyberDeck fit-check model, millimetres, Z up\nmtllib %s\n" % os.path.basename(mtl))
        base = 1
        for pid, name, col, c in items:
            f.write("o %s\n# %s\nusemtl m_%s\n" % (pid, name, pid))
            for v in c:
                f.write("v %.3f %.3f %.3f\n" % v)
            for q in QUADS:
                f.write("f %d %d %d %d\n" % tuple(base + i for i in q))
            base += 8


def write_scad(path, P, parts, angle):
    sb, sl = shell_boxes(P)
    eb, el = extras(P)
    L = []
    w = L.append
    w("// M.33 CyberDeck fit-check model, generated from fit-check/index.html by export_cad.py.")
    w("// Units: millimetres. Axes: X left to right, Y toward the back (hinge), Z up.")
    w("// Case: %s. Part sizes other than the case are estimates until measured." % P["name"])
    w("// Change lid_angle (0 = closed) and the show_* switches, then press F5 or F6.")
    w("// Edit sizes here for quick tries, but edit index.html and rerun the exporter to keep both in sync.")
    w("")
    w("lid_angle = %g;" % angle)
    w("show_shell = true;")
    w("ghost_shell = true; // see-through in preview (F5); set false so F6 render and STL export include the shell")
    w("show_parts = true;")
    w("show_extras = true;")
    w("")
    for k in ("W", "D", "bd", "ld", "ws", "wf", "wb", "fl"):
        w("%s = %g;" % (k, P[k]))
    w("")
    w("// Page frame box [x, y_up, z_front, w, h, d] -> CAD cube.")
    w("module pbox(b, col) { color(col) translate([b[0], -(b[2] + b[5]), b[1]]) cube([b[3], b[5], b[4]]); }")
    w("module lid_frame() { translate([0, wb, bd]) rotate([-lid_angle, 0, 0]) translate([0, -wb, -bd]) children(); }")
    w("")
    w("module shell_base() {")
    for b in sb:
        w("  pbox([%s], [0.23, 0.26, 0.31]);" % ", ".join("%g" % v for v in b))
    w("}")
    w("module shell_lid() {")
    for b in sl:
        w("  pbox([%s], [0.23, 0.26, 0.31]);" % ", ".join("%g" % v for v in b))
    w("}")
    w("module extras_base() {")
    for pid, name, b, col in eb:
        w("  pbox([%s], [%s]); // %s" % (", ".join("%g" % v for v in b), ", ".join("%g" % v for v in col), name))
    w("}")
    w("module extras_lid() {")
    for pid, name, b, col in el:
        w("  pbox([%s], [%s]); // %s" % (", ".join("%g" % v for v in b), ", ".join("%g" % v for v in col), name))
    w("}")
    w("")
    w("// Parts: [x, y, z, w, h, d] as in the fit-check table. Lid parts use y = gap from the lid's inside face.")
    w("module parts_base() {")
    for p in parts:
        if p["g"] != "lid":
            b = part_box(p, P)
            w("  pbox([%s], [%s]); // %s" % (", ".join("%g" % v for v in b), ", ".join("%g" % v for v in p["c"]), p["name"]))
    w("}")
    w("module parts_lid() {")
    for p in parts:
        if p["g"] == "lid":
            b = part_box(p, P)
            w("  pbox([%s], [%s]); // %s" % (", ".join("%g" % v for v in b), ", ".join("%g" % v for v in p["c"]), p["name"]))
    w("}")
    w("")
    w("if (show_shell) { if (ghost_shell) { %shell_base(); lid_frame() %shell_lid(); } else { shell_base(); lid_frame() shell_lid(); } }")
    w("if (show_extras) { extras_base(); lid_frame() extras_lid(); }")
    w("if (show_parts) { parts_base(); lid_frame() parts_lid(); }")
    w("")
    open(path, "w").write("\n".join(L))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--case", type=int, default=0, help="index into PRESETS (0 = Pelican 1470)")
    ap.add_argument("--open-angle", type=float, default=105)
    ap.add_argument("--out", default=os.path.join(REPO, "cad"))
    a = ap.parse_args()
    presets, parts = load(os.path.join(HERE, "index.html"))
    P = presets[a.case]
    os.makedirs(os.path.join(a.out, "parts"), exist_ok=True)
    for angle, tag in ((0, "closed"), (a.open_angle, "open")):
        items = build(P, parts, angle)
        tri = [t for _, _, _, c in items for t in tris(c)]
        write_stl(os.path.join(a.out, "assembly-%s.stl" % tag), tri, "M.33 CyberDeck %s" % tag)
        write_obj(os.path.join(a.out, "assembly-%s.obj" % tag), items)
    for pid, name, col, c in build(P, parts, 0):
        if pid.startswith("shell_"):
            continue
        write_stl(os.path.join(a.out, "parts", pid + ".stl"), tris(c), name)
    write_scad(os.path.join(a.out, "cyberdeck.scad"), P, parts, a.open_angle)
    print("Case: %s, %d parts, wrote %s" % (P["name"], len(parts), a.out))


if __name__ == "__main__":
    main()
