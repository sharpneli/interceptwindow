"""Build the planet bench's texture set from the sources.

    python -I make_textures.py SOURCES_DIR LAND_BIN OUT_DIR

Writes 2k maps per body, Earth's coast as a signed distance field from Fleetwright's
land file (Natural Earth 1:10M), and planet-textures.js (the maps as data URIs, so the
bench also runs from file://).
"""
import base64, json, os, struct, sys
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

SRC, LAND, OUT = sys.argv[1:4]
os.makedirs(OUT, exist_ok=True)
W, H = 2048, 1024
SDF_W, SDF_H, SDF_RANGE = 8192, 4096, 16.0   # px either side of the coast mapped to 0..255


def base(name, out, mode="RGB", q=88):
    im = Image.open(os.path.join(SRC, name)).convert(mode).resize((W, H), Image.LANCZOS)
    im.save(os.path.join(OUT, out), quality=q)


def land_rings(path):
    d = open(path, "rb").read()
    magic, ver, n = struct.unpack_from("<iii", d, 0)
    assert magic == 0x444C5746 and ver == 1
    counts = struct.unpack_from("<%di" % n, d, 12)
    off = 12 + 4 * n
    for c in counts:
        pts = np.frombuffer(d, "<i4", 2 * c, off).reshape(c, 2) / 1e6
        off += 8 * c
        yield pts


def coast_sdf():
    rings = []
    for pts in land_rings(LAND):
        # Unwrap the longitude so a ring that crosses the antimeridian stays in one piece.
        lon = pts[:, 0].copy()
        step = np.diff(lon)
        lon[1:] += np.cumsum(np.where(step > 180, -360.0, np.where(step < -180, 360.0, 0.0)))
        x = (lon + 180.0) / 360.0 * SDF_W
        y = (90.0 - pts[:, 1]) / 180.0 * SDF_H
        close = lon[0] - lon[-1]
        close -= 360.0 * round(close / 360.0) if abs(close) < 180 else 0.0
        if abs(lon[-1] - lon[0]) > 180:
            # A ring round a pole (Antarctica): close it along the map's edge.
            edge = SDF_H if pts[:, 1].mean() < 0 else 0.0
            x = np.concatenate([x, [x[-1], x[0]]])
            y = np.concatenate([y, [edge, edge]])
            area = 0.0
            polar = True
        else:
            area = 0.5 * np.sum(x * np.roll(y, -1) - np.roll(x, -1) * y)
            polar = False
        rings.append((area, polar, x, y))
    # Outer coasts wind one way and holes the other; the biggest ring is an outer coast.
    sign = np.sign(max(rings, key=lambda r: abs(r[0]))[0])
    rings.sort(key=lambda r: (not r[1], -abs(r[0])))
    im = Image.new("L", (SDF_W, SDF_H), 0)
    dr = ImageDraw.Draw(im)
    for area, polar, x, y in rings:
        fill = 255 if polar or np.sign(area) == sign else 0
        for shift in (0, -SDF_W, SDF_W):
            if (x + shift).max() < 0 or (x + shift).min() > SDF_W:
                continue
            dr.polygon(list(zip((x + shift).tolist(), y.tolist())), fill=fill)
    land = np.asarray(im) > 0
    land = land.copy()
    land[int((90 + 84.0) / 180 * SDF_H):, :] = True   # the file's Antarctica stops short of the pole
    d_out = ndimage.distance_transform_edt(~land)
    d_in = ndimage.distance_transform_edt(land)
    sd = np.where(land, d_in - 0.5, 0.5 - d_out)
    v = np.clip(sd / SDF_RANGE * 127.5 + 127.5, 0, 255).astype(np.uint8)
    Image.fromarray(v).save(os.path.join(OUT, "earth-coast-sdf.png"), optimize=True)
    return land


def packed16(path):
    """A height map packed into 8-bit channels: green the high byte, red the low."""
    Image.MAX_IMAGE_PIXELS = None
    a = np.asarray(Image.open(os.path.join(SRC, path))).astype(np.float64)
    return a[..., 1] * 256.0 + a[..., 0]


META = {}


def height(name, metres, roll_px, size=(W, H)):
    """Metres on any equirectangular grid -> a 16-bit height map (red high byte, green low)."""
    metres = np.roll(metres, roll_px, axis=1)
    im = Image.fromarray(metres.astype(np.float32), "F")
    if im.size != size:
        im = im.resize(size, Image.LANCZOS)
    m = np.asarray(im, dtype=np.float64)
    lo, hi = float(m.min()), float(m.max())
    v = np.round((m - lo) / (hi - lo) * 65535.0).astype(np.uint16)
    rgb = np.zeros(v.shape + (3,), np.uint8)
    rgb[..., 0] = v >> 8
    rgb[..., 1] = v & 255
    Image.fromarray(rgb).save(os.path.join(OUT, name + ".png"), optimize=True)
    META[name] = {"minKm": round(lo / 1000.0, 4), "maxKm": round(hi / 1000.0, 4)}


# Moon: LROC WAC GLD100, 16 px/deg, metres, centred on 180 E (so rolled half a turn).
# It covers 79 S to 79 N; nearer the poles the file is filler.
g = packed16("moon-gld100-16p-lroc.png")
height("moon-height", g - np.median(g), g.shape[1] // 2)
# Mars: MOLA MEGDR 4 px/deg topography, metres + 32768, left edge at 0 E.
m = packed16("mars-megt90n000cb-mola.png")
height("mars-height", m - 32768.0, m.shape[1] // 2, (m.shape[1], m.shape[0]))   # kept at its own 1440 x 720

def land_cover():
    """MODIS MCD12C1 (IGBP classes at 0.05 deg) -> two 2k maps of surface-class shares.

    A map pixel is 20 km, so it rarely holds one class. Each channel is the share of the
    pixel's land in one class: A = forest, cropland, barren; B = ice, wetland, built-up.
    What is left over is grass, shrub and savanna. Shares filter cleanly; class ids would not.
    """
    Image.MAX_IMAGE_PIXELS = None
    a = np.asarray(Image.open(os.path.join(SRC, "earth-landcover-mcd12c1-2019.tif")))
    groups = [[1, 2, 3, 4, 5, 8], [12, 14], [16], [15], [11], [13]]
    down = lambda m: np.asarray(Image.fromarray(m.astype(np.float32), "F").resize((W, H), Image.BOX), dtype=np.float64)
    land = down(a != 0)
    wide = ndimage.gaussian_filter(land, 2.5, mode="wrap")
    out = []
    for ids in groups:
        m = down(np.isin(a, ids))
        # share of the land in the pixel; out at sea, carry the nearest coast's shares so coasts do not fade
        near = ndimage.gaussian_filter(m, 2.5, mode="wrap") / np.maximum(wide, 1e-4)
        out.append(np.clip(np.where(land > 0.3, m / np.maximum(land, 1e-4), near), 0, 1))
    for name, ch in (("earth-class-a", out[:3]), ("earth-class-b", out[3:])):
        Image.fromarray((np.stack(ch, -1) * 255).round().astype(np.uint8)).save(os.path.join(OUT, name + ".jpg"), quality=92)


land_cover()
base("earth-blue-marble.jpg", "earth-color.jpg")
base("earth-night.jpg", "earth-night.jpg", q=82)
base("earth-topology.png", "earth-height.jpg", "L", 90)
base("sss-2k_moon.jpg", "moon-color.jpg")
base("sss-2k_mars.jpg", "mars-color.jpg")
coast_sdf()

mime = {".jpg": "image/jpeg", ".png": "image/png"}
with open(os.path.join(OUT, "planet-textures.js"), "w") as f:
    f.write("// Generated by make_textures.py. Do not edit.\nwindow.PLANET_TEX={\n")
    for n in sorted(os.listdir(OUT)):
        e = os.path.splitext(n)[1]
        if e in mime:
            b = base64.b64encode(open(os.path.join(OUT, n), "rb").read()).decode()
            f.write('"%s":"data:%s;base64,%s",\n' % (os.path.splitext(n)[0], mime[e], b))
    f.write("};\n")
    f.write("window.PLANET_TEX_META=" + json.dumps(META) + ";\n")
