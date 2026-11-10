"""Build the small-body bench's data: real shape models as radius maps, and catalogue rows.

    python -I make_small_bodies.py SOURCES_DIR BODIES_CSV OUT_DIR

SOURCES_DIR holds Celestia .cmod meshes (CelestiaContent/models, each with a .license file
naming the shape model it came from). Each becomes a radius map: the distance from the
body's centre to its surface on a longitude/latitude grid, in units of the mean radius.
That is the same form the generator in small-body-bench.html produces, so a real shape is
a drop-in replacement for a generated one.

Writes small-body-data.js: window.REAL_SHAPES (16-bit PNGs as data URIs, red the high
byte and green the low) and window.CATALOGUE (the bench's rows from bodies.csv).
"""
import base64, csv, io, json, os, struct, sys
import numpy as np
from PIL import Image
from scipy.interpolate import LinearNDInterpolator
from scipy.spatial import cKDTree

SRC, CSV, OUT = sys.argv[1:4]
W, H = 512, 256

# name in the catalogue -> mesh file
REAL = {"phobos": "phobos", "deimos": "deimos", "433-eros": "eros", "101955-bennu": "bennu",
        "25143-itokawa": "itokawa", "243-ida": "ida", "951-gaspra": "gaspra", "253-mathilde": "mathilde",
        "4179-toutatis": "toutatis", "216-kleopatra": "kleopatra", "4-vesta": "vesta", "hyperion": "hyperion"}
# catalogue-only bodies shown as well: no shape model here, so the generator is on its own
EXTRA = ["16-psyche", "21-lutetia", "162173-ryugu", "486958-arrokoth", "amalthea", "proteus", "2867-steins", "1-ceres"]


def cmod_vertices(path):
    """Positions from a binary Celestia model (all meshes)."""
    d = open(path, "rb").read()
    assert d[:16] == b"#celmodel_binary", path
    p = 16
    sizes = {0: 4, 1: 8, 2: 12, 3: 16, 4: 4}          # vertex attribute formats, bytes
    out = []

    def i16():
        nonlocal p
        v = struct.unpack_from("<h", d, p)[0]; p += 2
        return v

    def u32():
        nonlocal p
        v = struct.unpack_from("<I", d, p)[0]; p += 4
        return v

    def value():                                         # a typed material value
        nonlocal p
        t = i16()
        if t in (1, 2, 3, 4): p += 4 * t
        elif t == 5: p += 2 + struct.unpack_from("<H", d, p)[0]
        elif t == 6: p += 4
        elif t == 7: p += 12
        else: raise ValueError("cmod value type %d" % t)

    while p < len(d):
        tok = i16() - 1000
        if tok == 1:                                     # material
            while True:
                t = i16() - 1000
                if t == 2: break
                if t == 7: i16(); value()                # texture: semantic, then a string
                elif t == 15: i16()                      # blend mode
                else: value()
        elif tok == 9:                                   # mesh
            assert i16() == 1011
            attrs = []
            while True:
                sem = i16()
                if sem == 1012: break
                attrs.append((sem, i16()))
            stride = sum(sizes[f] for _, f in attrs)
            off = 0
            for sem, f in attrs:
                if sem == 0: break
                off += sizes[f]
            assert i16() == 1013
            n = u32()
            raw = np.frombuffer(d, np.uint8, n * stride, p).reshape(n, stride)
            out.append(raw[:, off:off + 12].copy().view("<f4").reshape(n, 3))
            p += n * stride
            while True:
                t = i16()
                if t == 1010: break
                u32(); cnt = u32(); p += 4 * cnt
        else:
            raise ValueError("cmod token %d at %d" % (tok, p))
    return np.concatenate(out).astype(np.float64)


def grid_dirs(w, h):
    """Unit directions of a map's pixel centres. Longitude 0 faces +Z, 90 E faces +X, north is +Y."""
    lon = ((np.arange(w) + 0.5) / w - 0.5) * 2 * np.pi
    lat = (0.5 - (np.arange(h) + 0.5) / h) * np.pi
    lon, lat = np.meshgrid(lon, lat)
    return np.stack([np.cos(lat) * np.sin(lon), np.sin(lat), np.cos(lat) * np.cos(lon)], -1), lat


def radius_map(verts):
    # Celestia: x to the prime meridian, y north, -z to 90 E. The bench: +Z, +Y, +X.
    v = np.stack([-verts[:, 2], verts[:, 1], verts[:, 0]], -1)
    r = np.linalg.norm(v, axis=1)
    u = v / r[:, None]
    lon, lat = np.arctan2(u[:, 0], u[:, 2]), np.arcsin(np.clip(u[:, 1], -1, 1))
    # Linear interpolation over the vertices in longitude/latitude, with a copy either
    # side of the seam; the nearest vertex fills the caps the triangulation misses.
    pts = np.concatenate([np.stack([lon + k, lat], -1) for k in (-2 * np.pi, 0, 2 * np.pi)])
    val = np.concatenate([r, r, r])
    keep = np.abs(pts[:, 0]) < np.pi * 1.25
    dirs, glat = grid_dirs(W, H)
    glon = np.arctan2(dirs[..., 0], dirs[..., 2])
    m = LinearNDInterpolator(pts[keep], val[keep])(glon, glat)
    near = r[cKDTree(u).query(dirs.reshape(-1, 3))[1]].reshape(H, W)
    m = np.where(np.isnan(m), near, m)
    mean = np.sum(m * np.cos(glat)) / np.sum(np.cos(glat))
    # Twice the grid, bicubic: the view shades from the map's slopes, so they should not step.
    big = Image.fromarray((m / mean).astype(np.float32), "F").resize((2 * W, 2 * H), Image.BICUBIC)
    return np.asarray(big, dtype=np.float64)


def png16(m):
    lo, hi = float(m.min()), float(m.max())
    v = np.round((m - lo) / (hi - lo) * 65535).astype(np.uint16)
    rgb = np.zeros(v.shape + (3,), np.uint8)
    rgb[..., 0] = v >> 8; rgb[..., 1] = v & 255
    b = io.BytesIO(); Image.fromarray(rgb).save(b, "PNG", optimize=True)
    return {"w": m.shape[1], "h": m.shape[0], "min": round(lo, 5), "max": round(hi, 5),
            "src": "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()}


def number(s):
    try: return float(s)
    except ValueError: return None


rows = {r["id"]: r for r in csv.DictReader(open(CSV, encoding="utf-8"))}
shapes, cat = {}, []
for cid in list(REAL) + EXTRA:
    r = rows[cid]
    axes = sorted((float(x) for x in r["shape_km"].replace(" ", "").split("x")), reverse=True) if r["shape_km"] else None
    credit = None
    if cid in REAL:
        m = radius_map(cmod_vertices(os.path.join(SRC, REAL[cid] + ".cmod")))
        shapes[cid] = png16(m)
        lic = os.path.join(SRC, REAL[cid] + ".cmod.license")
        if os.path.exists(lic):
            t = [l.split(":", 1)[1].strip() for l in open(lic, encoding="utf-8") if l.startswith("SPDX-FileCopyrightText")]
            credit = "; ".join(t) or None
        print(cid, "radius %.3f .. %.3f of the mean" % (m.min(), m.max()))
    cat.append({"id": cid, "name": r["name"], "category": r["category"], "radiusKm": number(r["radius_km"]),
                "axes": axes, "density": number(r["density_g_cm3"]), "albedo": number(r["albedo"]),
                "rotH": number(r["rot_period_h"]), "spec": r["spec_smass"] or r["spec_tholen"] or None,
                "real": cid in REAL, "credit": credit})

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "small-body-data.js"), "w") as f:
    f.write("// Generated by make_small_bodies.py. Do not edit.\n")
    f.write("window.CATALOGUE=" + json.dumps(cat, indent=0) + ";\n")
    f.write("window.REAL_SHAPES=" + json.dumps(shapes) + ";\n")
