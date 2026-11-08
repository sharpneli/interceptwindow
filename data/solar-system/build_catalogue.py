#!/usr/bin/env python3
"""Build the Intercept Window solar-system body catalogue.

Reads the raw JPL extracts in sources/ and writes bodies.csv: one row per body,
every orbit given as fixed Keplerian elements in the J2000 ecliptic frame of
its parent, ready to be put on rails.

Standard library only. Run from anywhere:  python build_catalogue.py
"""
import csv
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "sources")
OUT = os.path.join(HERE, "bodies.csv")

# --- constants -------------------------------------------------------------
G = 6.6743e-20                 # km^3 kg^-1 s^-2 (CODATA 2018)
GM_SUN = 1.32712440041279e11   # km^3 s^-2 (DE440)
AU = 149597870.7               # km (IAU 2012)
DAY = 86400.0
EPS_J2000 = math.radians(23.4392911)   # obliquity of the ecliptic at J2000
CATALOGUE_EPOCH_JD = 2461200.5          # epoch used for the planets (2026-06-09 TDB)
J2000_JD = 2451545.0

# IAU WGCCRE 2015 north (positive) poles, J2000 ICRF, deg. Used for reference only and
# for moon elements JPL gives in a planet's equatorial frame. Uranus is given as its
# positive (right-hand rotation) pole, which is how JPL refers its Uranian moons.
POLES = {
    "sun": (286.13, 63.87),
    "mercury": (281.0103, 61.4155),
    "venus": (272.76, 67.16),
    "earth": (0.0, 90.0),
    "mars": (317.269202, 54.432516),
    "jupiter": (268.056595, 64.495303),
    "saturn": (40.589, 83.537),
    "uranus": (77.311, 15.175),     # positive pole = antipode of IAU "north" 257.311/-15.175
    "neptune": (299.36, 43.46),
    "pluto": (132.993, -6.163),
}


def f(x):
    """Parse a float, or None for blank / n/a / NaN."""
    if x is None:
        return None
    x = str(x).strip()
    if x == "" or x.lower() in ("n/a", "nan", "-"):
        return None
    try:
        return float(x)
    except ValueError:
        return None


def slug(s):
    s = s.lower().replace("`", "").replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def fmt(v, n=10):
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    if v == 0:
        return "0"
    return f"{v:.{n}g}"


# --- vector helpers --------------------------------------------------------
def rot_x(a):
    c, s = math.cos(a), math.sin(a)
    return [[1, 0, 0], [0, c, -s], [0, s, c]]


def rot_z(a):
    c, s = math.cos(a), math.sin(a)
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]


def mat_mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def mat_vec(m, v):
    return [sum(m[i][k] * v[k] for k in range(3)) for i in range(3)]


def transpose(m):
    return [[m[j][i] for j in range(3)] for i in range(3)]


def unit_radec(ra, dec):
    ra, dec = math.radians(ra), math.radians(dec)
    return [math.cos(dec) * math.cos(ra), math.cos(dec) * math.sin(ra), math.sin(dec)]


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def norm(v):
    m = math.sqrt(sum(x * x for x in v))
    return [x / m for x in v]


# ICRF equatorial -> J2000 ecliptic
EQ_TO_ECL = rot_x(-EPS_J2000)


def plane_frame_to_icrf(pole_ra, pole_dec):
    """Matrix whose columns are the reference plane's x, y, z axes in ICRF.

    x points to the ascending node of the reference plane on the ICRF equator,
    z is the plane's pole. This is JPL's convention for Laplace-plane and
    planet-equator satellite elements.
    """
    z = unit_radec(pole_ra, pole_dec)
    x = cross([0.0, 0.0, 1.0], z)
    if math.sqrt(sum(c * c for c in x)) < 1e-12:   # pole on the ICRF pole
        x = [1.0, 0.0, 0.0]
    x = norm(x)
    y = cross(z, x)
    return [[x[0], y[0], z[0]], [x[1], y[1], z[1]], [x[2], y[2], z[2]]]


def orientation_matrix(node, inc, argp):
    """Perifocal -> reference-frame rotation for angles in degrees."""
    return mat_mul(mat_mul(rot_z(math.radians(node)), rot_x(math.radians(inc))),
                   rot_z(math.radians(argp)))


def angles_from_matrix(m):
    """Recover node, inclination, argument of periapsis (deg) from a perifocal matrix."""
    p = [m[0][0], m[1][0], m[2][0]]     # periapsis direction
    h = [m[0][2], m[1][2], m[2][2]]     # orbit normal
    inc = math.degrees(math.acos(max(-1.0, min(1.0, h[2]))))
    nvec = [-h[1], h[0], 0.0]           # z x h
    nlen = math.hypot(nvec[0], nvec[1])
    if nlen < 1e-12:                     # equatorial orbit: node undefined, put it at 0
        node = 0.0
        argp = math.degrees(math.atan2(p[1], p[0]))
        if h[2] < 0:
            argp = -argp
    else:
        node = math.degrees(math.atan2(nvec[1], nvec[0]))
        nhat = [nvec[0] / nlen, nvec[1] / nlen, 0.0]
        cosw = sum(nhat[i] * p[i] for i in range(3))
        sinw = sum(cross(nhat, p)[i] * h[i] for i in range(3))
        argp = math.degrees(math.atan2(sinw, cosw))
    return node % 360.0, inc, argp % 360.0


def to_ecliptic(node, inc, argp, frame, pole):
    """Convert satellite angles given in `frame` to the J2000 ecliptic."""
    if frame == "ecliptic":
        return node % 360.0, inc, argp % 360.0
    m_ref = orientation_matrix(node, inc, argp)
    m_icrf = mat_mul(plane_frame_to_icrf(*pole), m_ref)
    m_ecl = mat_mul(EQ_TO_ECL, m_icrf)
    return angles_from_matrix(m_ecl)


# --- diameters, densities --------------------------------------------------
def diameter_from_h(h, p):
    return 1329.0 / math.sqrt(p) * 10 ** (-h / 5.0)


C_TYPES = ("B", "C", "F", "G", "P", "D", "T")
S_TYPES = ("S", "Q", "K", "L", "A", "R", "O", "V")


def tax_group(spec_b, spec_t):
    """Very coarse taxonomic group: 'C', 'S', 'M', 'X', or None."""
    t = (spec_t or "").strip().upper()
    b = (spec_b or "").strip()
    if t.startswith("M"):
        return "M"
    if t.startswith("E"):
        return "E"
    for code in (b, t):
        if not code:
            continue
        c0 = code[0].upper()
        if c0 in C_TYPES:
            return "C"
        if c0 in S_TYPES:
            return "S"
        if c0 in ("X",):
            return "X"
        if c0 == "E":
            return "E"
    return None


ALBEDO_BY_TAX = {"C": 0.06, "S": 0.25, "M": 0.15, "X": 0.10, "E": 0.45}
DENSITY_BY_TAX = {"C": 1.4, "S": 2.7, "M": 3.5, "X": 2.0, "E": 2.5}
ALBEDO_BY_CAT = {
    "neo": 0.14, "earth_coorbital": 0.14, "main_belt": 0.10, "mars_trojan": 0.20,
    "jupiter_trojan": 0.07, "centaur": 0.07, "tno": 0.09, "neptune_trojan": 0.09,
    "dwarf_planet": 0.10, "main_belt_comet": 0.05, "comet": 0.04,
}
DENSITY_BY_CAT = {
    "neo": 2.0, "earth_coorbital": 2.0, "main_belt": 2.0, "mars_trojan": 2.5,
    "jupiter_trojan": 1.0, "centaur": 1.0, "tno": 1.0, "neptune_trojan": 1.0,
    "dwarf_planet": 1.8, "main_belt_comet": 1.5, "comet": 0.5,
}

# Literature values for the largest trans-Neptunian objects, which SBDB does not size.
# Source: Wikipedia "List of possible dwarf planets" (accessed 2026-11-07), which cites
# occultation and thermal results and Johnston's Archive for system masses.
# pdes: (diameter km, mass kg or None, geometric albedo, density g/cm3 or None, method)
TNO_LIT = {
    "134340": (2377, 1.3025e22, 0.58, 1.854, "direct"),
    "136199": (2326, 1.6466e22, 0.96, 2.43, "occultation"),
    "136108": (1544, 3.95244e21, 0.49, 2.05, "occultation"),
    "136472": (1430, 2.69e21, 0.83, 1.76, "occultation"),
    "225088": (1230, 1.75e21, 0.14, 1.74, "thermal"),
    "50000": (1098, 1.212e21, 0.11, 1.751, "occultation"),
    "90482": (910, 5.48e20, 0.23, 1.4, "thermal"),
    "90377": (906, None, 0.41, None, "thermal"),
    "120347": (838, 4.92e20, 0.05, 1.50, "thermal"),
    "55565": (802, None, 0.10, None, "occultation"),
    "307261": (796, None, 0.10, None, "occultation"),
    "208996": (772, None, 0.11, None, "occultation"),
    "532037": (742, None, 0.18, None, "thermal"),
    "174567": (740, 2.44e20, 0.099, None, "occultation"),
    "28978": (697, None, 0.11, None, "occultation"),
    "90568": (680, None, 0.08, None, "thermal"),
    "145452": (679, None, 0.11, None, "thermal"),
    "55637": (659, 1.25e20, 0.12, 0.82, "thermal"),
    "20000": (654, None, 0.12, None, "thermal"),
    "145451": (644, None, 0.11, None, "occultation"),
    "2014 UZ224": (635, None, 0.14, None, "thermal"),
    "229762": (634, 1.36e20, 0.14, 1.04, "occultation"),
    "303775": (584, None, 0.13, None, "thermal"),
    # C/2014 UN271 nucleus, Lellouch et al. 2022 (ALMA thermal)
    "2014 UN271": (137, None, 0.049, None, "thermal"),
}
DWARF_PLANETS = {"1", "134340", "136199", "136108", "136472", "225088", "50000", "90482", "90377"}


def dyn_group(cat, cls, a, e, inc):
    """Coarse dynamical neighbourhood, useful as a game region label."""
    q = a * (1 - e)
    if cat in ("main_belt", "main_belt_comet", "dwarf_planet") and a < 5:
        if cls == "IMB" or (1.78 <= a < 2.0 and inc > 16):
            return "Hungaria" if 1.78 <= a < 2.0 else "inner (Mars-crossing)"
        if cls == "MCA":
            return "Mars-crosser"
        if a < 2.5:
            return "inner belt"
        if a < 2.82:
            return "middle belt"
        if a < 3.3:
            return "outer belt"
        if a < 3.7:
            return "Cybele"
        if a < 4.2:
            return "Hilda (3:2 with Jupiter)"
        return "Thule (4:3 with Jupiter)"
    if cat in ("neo", "earth_coorbital"):
        return {"ATE": "Aten", "APO": "Apollo", "AMO": "Amor", "IEO": "Atira"}.get(cls, cls)
    if cat == "comet":
        return {"JFc": "Jupiter-family", "JFC": "Jupiter-family", "ETc": "Encke-type",
                "HTC": "Halley-type", "COM": "long-period", "CTc": "Chiron-type"}.get(cls, cls)
    if cat in ("tno", "dwarf_planet"):
        if 39.0 <= a <= 39.8:
            return "plutino (3:2 with Neptune)"
        if 47.4 <= a <= 48.4:
            return "twotino (2:1 with Neptune)"
        if 42.0 <= a <= 48.0 and e < 0.2:
            return "classical Kuiper belt"
        if q >= 38 and a >= 150:
            return "detached / sednoid"
        if a >= 50:
            return "scattered disc"
        return "resonant / scattered"
    if cat == "centaur":
        return "centaur"
    return ""


def planet_mean_longitude(pname, jd):
    """Mean longitude (deg) of a planet from Standish Table 2a."""
    key = "EMBary" if pname == "Earth" else pname
    (a0, e0, i0, L0, w0, O0), (da, de, di, dL, dw, dO) = approx[key]
    t = (jd - J2000_JD) / 36525.0
    return (L0 + dL * t) % 360.0


def parse_rot_hours(s, period_days):
    """Rotation period in hours from Horizons-style text; synchronous -> orbital period."""
    if not s:
        return None, ""
    s = s.strip()
    low = s.lower()
    if low.startswith("synchronous"):
        return period_days * 24.0, "synchronous"
    if low.startswith("chaotic"):
        return None, "chaotic"
    m = re.match(r"([\d.]+)\s*h\s*([\d.]+)\s*m", s)
    if m:
        return float(m.group(1)) + float(m.group(2)) / 60.0, ""
    m = re.match(r"([\d.]+)\s*d", s)
    if m:
        return float(m.group(1)) * 24.0, ""
    return None, ""


def new_row():
    return {k: None for k in COLUMNS}


COLUMNS = [
    "id", "name", "designation", "naif_id", "parent", "category", "jpl_class", "group",
    "gm_km3_s2", "mass_kg", "mass_basis", "radius_km", "radius_basis", "density_g_cm3",
    "albedo", "abs_mag_h", "rot_period_h", "spec_tholen", "spec_smass", "shape_km",
    "surface_gravity_m_s2", "escape_velocity_km_s", "soi_radius_km", "hill_radius_km",
    "epoch_jd_tdb", "frame", "a_km", "a_au", "e", "i_deg", "node_deg", "argp_deg",
    "mean_anomaly_deg", "mean_motion_deg_day", "period_days",
    "node_rate_deg_day", "argp_rate_deg_day",
    "q_au", "big_q_au", "earth_moid_au", "nhats_min_dv_km_s", "nhats_min_dur_days",
    "pole_ra_deg", "pole_dec_deg", "tags", "notes", "source",
]


rows = []

# --- Sun -------------------------------------------------------------------
sun = new_row()
sun.update(id="sun", name="Sun", designation="Sun", naif_id="10", parent="",
           category="star", gm_km3_s2=GM_SUN, mass_kg=GM_SUN / G, mass_basis="measured",
           radius_km=695700.0, radius_basis="measured", density_g_cm3=1.408,
           rot_period_h=609.12, pole_ra_deg=POLES["sun"][0], pole_dec_deg=POLES["sun"][1],
           frame="", source="DE440 GM; IAU 2015 nominal radius", notes="System origin; static on rails")
rows.append(sun)

# --- Planets ---------------------------------------------------------------
phys = {r["name"]: r for r in csv.DictReader(open(os.path.join(SRC, "planets_phys.csv")))}
approx = {}
extra = {}
with open(os.path.join(SRC, "planets_approx_2a.txt")) as fh:
    lines = [l for l in fh if l.strip() and not l.startswith("#")]
i = 0
while i < len(lines):
    parts = lines[i].split()
    if len(parts) == 7 and not lines[i][0].isspace():
        name = parts[0]
        rates = [float(x) for x in lines[i + 1].split()]
        approx[name] = ([float(x) for x in parts[1:]], rates)
        i += 2
    elif len(parts) == 5:
        extra[parts[0]] = [float(x) for x in parts[1:]]
        i += 1
    else:
        i += 1

T = (CATALOGUE_EPOCH_JD - J2000_JD) / 36525.0
NAIF = {"Mercury": 199, "Venus": 299, "Earth": 399, "Mars": 499, "Jupiter": 599,
        "Saturn": 699, "Uranus": 799, "Neptune": 899}
for pname in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
    key = "EMBary" if pname == "Earth" else pname
    (a0, e0, i0, L0, w0, O0), (da, de, di, dL, dw, dO) = approx[key]
    a, e, inc = a0 + da * T, e0 + de * T, i0 + di * T
    L, wbar, node = L0 + dL * T, w0 + dw * T, O0 + dO * T
    M = L - wbar
    if pname in extra:
        b, c, s, ff = extra[pname]
        M += b * T * T + c * math.cos(math.radians(ff * T)) + s * math.sin(math.radians(ff * T))
    argp = wbar - node
    p = phys[pname]
    mass = float(p["mass_1e24kg"]) * 1e24
    n = (dL - dw) / 36525.0
    r = new_row()
    r.update(id=pname.lower(), name=pname, designation=pname, naif_id=str(NAIF[pname]),
             parent="sun", category="planet", gm_km3_s2=G * mass, mass_kg=mass,
             mass_basis="measured", radius_km=float(p["R_mean_km"]), radius_basis="measured",
             density_g_cm3=float(p["density_gcc"]), albedo=float(p["albedo"]),
             abs_mag_h=float(p["V10"]), rot_period_h=float(p["rot_period_d"]) * 24.0,
             epoch_jd_tdb=CATALOGUE_EPOCH_JD, frame="ecliptic_j2000",
             a_km=a * AU, a_au=a, e=e, i_deg=inc, node_deg=node % 360, argp_deg=argp % 360,
             mean_anomaly_deg=M % 360, mean_motion_deg_day=n, period_days=360.0 / n,
             node_rate_deg_day=dO / 36525.0, argp_rate_deg_day=(dw - dO) / 36525.0,
             q_au=a * (1 - e), big_q_au=a * (1 + e),
             pole_ra_deg=POLES[pname.lower()][0], pole_dec_deg=POLES[pname.lower()][1],
             source="JPL SSD approx_pos Table 2a (Standish) evaluated at epoch; JPL planets phys_par",
             notes=f"Equatorial radius {p['R_eq_km']} km")
    if pname == "Earth":
        r["notes"] += "; orbit is the Earth-Moon barycentre. Earth sits 4671 km from it toward the Moon's opposite side"
    rows.append(r)

planet_gm = {r["id"]: r["gm_km3_s2"] for r in rows}

# --- Moons -----------------------------------------------------------------
PARENT_POLE_FOR_EQ = {"Saturn": "saturn", "Uranus": "uranus", "Neptune": "neptune", "Pluto": "pluto"}
# Orientation, phase and mean motion from JPL Horizons at the catalogue epoch
HZ = {r["naif_id"]: r for r in csv.DictReader(open(os.path.join(SRC, "moons_horizons.csv"), encoding="utf-8"))}
moon_rows = []
for m in csv.DictReader(open(os.path.join(SRC, "moons_raw.csv"), encoding="utf-8")):
    if not f(m["Rf"]):
        continue    # no size information at all (S/2009 S 2, a 300 m ring moonlet)
    planet = m["planet"]
    frame = m["frame"]
    a_km = f(m["a"])
    hz = HZ.get(m["code"])
    if hz:
        enode, einc, eargp = f(hz["node_deg"]), f(hz["i_deg"]), f(hz["argp_deg"])
        ecc, M0, n_moon = f(hz["e"]), f(hz["mean_anomaly_deg"]), f(hz["mean_motion_deg_day"])
        jd = f(hz["epoch_jd_tdb"])
        P = 360.0 / n_moon
        orbit_note = f"orbit: Horizons osculating at epoch, mean motion {hz['n_basis']}"
        if hz["horizons_center"].startswith("9"):
            orbit_note += "; orbits the Pluto-Charon barycentre"
    else:
        node, inc, argp = f(m["node"]), f(m["i"]), f(m["w"])
        if frame == "Laplace":
            pole = (f(m["ra"]), f(m["dec"]))
        elif frame == "equatorial":
            pole = POLES[PARENT_POLE_FOR_EQ[planet]]
        else:
            pole = None
        enode, einc, eargp = to_ecliptic(node, inc, argp, frame, pole)
        ecc, M0, P = f(m["e"]), f(m["M"]), f(m["P"])
        n_moon = 360.0 / P
        y, mo, d = m["epoch"].split("-")
        Y, Mo, day = int(y), int(mo), float(d)
        if Mo <= 2:
            Y, Mo = Y - 1, Mo + 12
        A = Y // 100
        jd = int(365.25 * (Y + 4716)) + int(30.6001 * (Mo + 1)) + day + (2 - A + A // 4) - 1524.5
        orbit_note = (f"orbit: JPL mean elements converted from the {frame} frame; "
                      "no Horizons ephemeris, phase along the orbit is approximate")
    R = f(m["Rf"])
    gm = f(m["GM"])
    rho_given = f(m["rho"])
    if gm and gm > 0:
        mass, mass_basis = gm / G, "measured"
    else:
        if frame == "ecliptic":
            rho = 1.5           # irregular captured moons
        elif planet == "Saturn" and a_km < 500000:
            rho = 0.5           # Saturn's small ring-region moons are porous ice
        else:
            rho = 1.2
        mass = rho * 1e12 * 4.0 / 3.0 * math.pi * R ** 3   # g/cm3 -> kg/km3 is 1e12
        gm = G * mass
        mass_basis = f"estimated (density {rho} g/cm3 assumed)"
        rho_given = None
    rot_h, rot_note = parse_rot_hours(m["rot"], P)
    rb = {"JPL": "measured", "lit": "literature estimate", "est_H": "estimated from magnitude"}[m["Rsrc"]]
    node_rate = argp_rate = 0.0
    if m["code"] == "301":
        # Earth's Moon: solar perturbations make osculating elements a poor rail, so use the
        # mean lunar elements (Meeus, Astronomical Algorithms ch. 47, after Chapront ELP),
        # referred to the J2000 equinox by removing general precession in longitude.
        Tm = (CATALOGUE_EPOCH_JD - J2000_JD) / 36525.0
        prec = 1.3969713   # deg per century
        Lm = 218.3164477 + 481267.88123421 * Tm - prec * Tm
        Om = 125.0445479 - 1934.1362891 * Tm - prec * Tm
        wb = 83.3532465 + 4069.0137287 * Tm - prec * Tm
        ecc, einc, a_km = 0.0549, 5.145, 384400.0
        enode, eargp, M0 = Om % 360, (wb - Om) % 360, (Lm - wb) % 360
        jd = CATALOGUE_EPOCH_JD
        n_moon = (481267.88123421 - 4069.0137287) / 36525.0     # anomalistic rate
        node_rate = (-1934.1362891 - prec) / 36525.0
        argp_rate = (4069.0137287 + 1934.1362891) / 36525.0
        P = 360.0 / ((481267.88123421 - prec) / 36525.0)          # sidereal month
        orbit_note = ("orbit: mean lunar elements (Meeus ch. 47) with node regression (18.6 yr) "
                      "and perigee advance (8.85 yr) as rates; mean_motion is the anomalistic rate")
    r = new_row()
    parent = planet.lower()
    notes = [orbit_note]
    if rot_note == "chaotic":
        notes.append("chaotic rotation")
    if m["tri"]:
        notes.append("triaxial")
    r.update(id=slug(m["name"]) if m["name"] != "Magaclite" else "megaclite",
             name=("Megaclite" if m["name"] == "Magaclite" else m["name"].replace("_", " ").replace("S20", "S/20")),
             designation=m["name"], naif_id=m["code"], parent=parent, category="moon",
             group=m["grp"] or ("regular" if frame != "ecliptic" else "irregular"),
             gm_km3_s2=gm, mass_kg=mass, mass_basis=mass_basis,
             radius_km=R, radius_basis=rb, density_g_cm3=rho_given, albedo=f(m["p"]),
             abs_mag_h=f(m["V"]), rot_period_h=rot_h, shape_km=m["tri"] or None,
             epoch_jd_tdb=jd, frame=f"ecliptic_j2000 ({parent}-centred)",
             a_km=a_km, a_au=a_km / AU, e=ecc, i_deg=einc, node_deg=enode, argp_deg=eargp,
             mean_anomaly_deg=M0 % 360, mean_motion_deg_day=n_moon, period_days=P,
             node_rate_deg_day=node_rate, argp_rate_deg_day=argp_rate,
             q_au=a_km * (1 - ecc) / AU, big_q_au=a_km * (1 + ecc) / AU,
             tags="moon", notes="; ".join(notes),
             source=f"JPL Horizons ({m['eph']}) + JPL SSD sats/elem mean a; phys: JPL sats/phys_par, Horizons, Wikipedia moon lists")
    moon_rows.append(r)

# --- Small bodies ----------------------------------------------------------
SB_COLS = ["spkid", "full_name", "pdes", "kind", "class", "neo", "pha", "H", "M1", "diameter",
           "albedo", "GM", "density", "rot_per", "spec_B", "spec_T", "extent", "epoch", "a", "e",
           "i", "om", "w", "ma", "q", "tp", "moid", "nh_dv", "nh_dur", "tags"]
sb = []
for k in range(4):
    with open(os.path.join(SRC, f"sb_{k}.csv"), encoding="utf-8") as fh:
        for rec in csv.reader(fh):
            sb.append(dict(zip(SB_COLS, rec)))

dropped = []
sb_rows = []
for s in sb:
    tags = set(s["tags"].split(";"))
    if s["pha"] == "Y":
        tags.add("pha")
    tags = sorted(tags)
    a = f(s["a"])
    e = f(s["e"])
    H = f(s["H"])
    D = f(s["diameter"])
    pdes = s["pdes"]
    if e is not None and e >= 1.0:
        dropped.append((s["full_name"], "hyperbolic: passing through, not on rails"))
        continue
    if H is None and D is None and not s["kind"].startswith("c") and pdes not in TNO_LIT:
        dropped.append((s["full_name"], "no magnitude or size: short-arc orbit, unreliable"))
        continue
    is_comet = s["kind"].startswith("c")
    cls = s["class"]
    if pdes in DWARF_PLANETS:
        cat = "dwarf_planet"
    elif "earth_coorbital" in tags:
        cat = "earth_coorbital"
    elif "mars_trojan" in tags:
        cat = "mars_trojan"
    elif "nep_trojan" in tags:
        cat = "neptune_trojan"
    elif is_comet:
        cat = "comet"
    elif "comet" in tags:
        cat = "main_belt_comet"
    elif cls == "TJN":
        cat = "jupiter_trojan"
    elif s["neo"] == "Y":
        cat = "neo"
    elif cls == "CEN":
        cat = "centaur"
    elif cls == "TNO":
        cat = "tno"
    else:
        cat = "main_belt"
    tg = tax_group(s["spec_B"], s["spec_T"])
    albedo = f(s["albedo"])
    gm = f(s["GM"])
    rho = f(s["density"])
    lit = TNO_LIT.get(pdes)
    if lit:
        D, mlit, plit, rholit, meth = lit
        radius_basis = f"literature ({meth})"
        albedo = plit
        if mlit and not gm:
            gm = G * mlit
            mass_basis = "measured (literature, binary orbit)"
        rho = rholit or rho
    elif D:
        radius_basis = "measured (SBDB: thermal IR, radar or spacecraft)"
    elif H is not None:
        p = albedo or (ALBEDO_BY_TAX.get(tg) if tg and cat in ("neo", "main_belt", "mars_trojan", "earth_coorbital") else None) \
            or ALBEDO_BY_CAT[cat]
        D = diameter_from_h(H, p)
        radius_basis = f"estimated from H with albedo {p}"
    else:
        D = 4.0
        radius_basis = "assumed (comet nucleus size unknown)"
    R = D / 2.0
    if gm:
        mass = gm / G
        if not lit or not lit[1]:
            mass_basis = "measured (SBDB GM)"
    else:
        dens = rho or (DENSITY_BY_TAX.get(tg) if tg and cat not in ("comet",) else None) or DENSITY_BY_CAT[cat]
        if cat == "tno" and D >= 600:
            dens = rho or 1.8
        mass = dens * 1e12 * 4.0 / 3.0 * math.pi * R ** 3
        gm = G * mass
        mass_basis = f"estimated (density {dens} g/cm3{' measured' if rho else ' assumed'})"
    if rho and rho > 20:          # SBDB occasionally stores kg/m^3
        rho = rho / 1000.0
    n = math.degrees(math.sqrt(GM_SUN / (a * AU) ** 3)) * DAY
    name = s["full_name"]
    m_ = re.match(r"^(\d+)\s+(.+?)\s+\(", name)
    if is_comet:
        short = name
        sid = slug(name)
    elif m_:
        short = m_.group(2)
        sid = slug(f"{m_.group(1)} {short}")
    else:
        m2 = re.match(r"^(\d+)\s+\(", name)
        short = name.strip("()") if not m2 else name
        sid = m2.group(1) if m2 else slug(pdes)
    notes = []
    if f(s["epoch"]) < 2460000.5:
        notes.append("old osculating epoch; rails drift more")
    if s["extent"]:
        notes.append("triaxial")
    r = new_row()
    r.update(id=sid,
             name=short, designation=name, naif_id=s["spkid"], parent="sun",
             category=cat, jpl_class=cls, group=dyn_group(cat, cls, a, e, f(s["i"])),
             gm_km3_s2=gm, mass_kg=mass, mass_basis=mass_basis, radius_km=R,
             radius_basis=radius_basis, density_g_cm3=rho, albedo=albedo, abs_mag_h=H,
             rot_period_h=f(s["rot_per"]), spec_tholen=s["spec_T"] or None,
             spec_smass=s["spec_B"] or None, shape_km=s["extent"] or None,
             epoch_jd_tdb=f(s["epoch"]), frame="ecliptic_j2000",
             a_km=a * AU, a_au=a, e=e, i_deg=f(s["i"]), node_deg=f(s["om"]),
             argp_deg=f(s["w"]), mean_anomaly_deg=f(s["ma"]), mean_motion_deg_day=n,
             period_days=360.0 / n, node_rate_deg_day=0.0, argp_rate_deg_day=0.0,
             q_au=a * (1 - e), big_q_au=a * (1 + e), earth_moid_au=f(s["moid"]),
             nhats_min_dv_km_s=f(s["nh_dv"]), nhats_min_dur_days=f(s["nh_dur"]),
             tags=";".join(t for t in tags if t), notes="; ".join(notes),
             source="JPL SBDB (sbdb_query API, full precision)" + ("; NASA NHATS" if s["nh_dv"] else "")
             + ("; size/mass: Wikipedia list of possible dwarf planets" if lit and pdes != "2014 UN271" else "")
             + ("; size: Lellouch et al. 2022" if pdes == "2014 UN271" else ""))
    if pdes == "134340":
        r["notes"] = ("orbit is the Pluto-Charon barycentre; moons orbit Pluto. " + r["notes"]).strip("; ")
        r["pole_ra_deg"], r["pole_dec_deg"] = POLES["pluto"]
    if cat.endswith("_trojan"):
        host = {"jupiter_trojan": "Jupiter", "mars_trojan": "Mars", "neptune_trojan": "Neptune"}[cat]
        lam_host = planet_mean_longitude(host, r["epoch_jd_tdb"])
        lam = r["node_deg"] + r["argp_deg"] + r["mean_anomaly_deg"]
        d = (lam - lam_host) % 360.0
        r["group"] = (f"{host} L4 (leading)" if d < 180 else f"{host} L5 (trailing)") + \
            (" - Greek camp" if host == "Jupiter" and d < 180 else " - Trojan camp" if host == "Jupiter" else "")
    sb_rows.append(r)

# Pluto's moons link to Pluto's catalogue id
pluto_id = next(r["id"] for r in sb_rows if r["designation"].startswith("134340 Pluto"))
for r in moon_rows:
    if r["parent"] == "pluto":
        r["parent"] = pluto_id

# normalise negative inclinations (Standish gives Earth a tiny negative i)
for r in rows + moon_rows + sb_rows:
    if r["i_deg"] is not None and r["i_deg"] < 0:
        r["i_deg"] = -r["i_deg"]
        r["node_deg"] = (r["node_deg"] + 180.0) % 360.0
        r["argp_deg"] = (r["argp_deg"] - 180.0) % 360.0

all_rows = rows + moon_rows + sb_rows

# derived: sphere of influence, Hill radius, surface gravity, escape velocity
gm_by_id = {r["id"]: r["gm_km3_s2"] for r in all_rows}
for r in all_rows:
    gm, R = r["gm_km3_s2"], r["radius_km"]
    if R:
        r["surface_gravity_m_s2"] = gm / R ** 2 * 1000.0
        r["escape_velocity_km_s"] = math.sqrt(2 * gm / R)
    if r["parent"]:
        ratio = gm / gm_by_id[r["parent"]]
        r["soi_radius_km"] = r["a_km"] * ratio ** 0.4
        r["hill_radius_km"] = r["a_km"] * (1 - r["e"]) * (ratio / 3.0) ** (1.0 / 3.0)

# unique ids
seen = {}
for r in all_rows:
    base = r["id"]
    if base in seen:
        seen[base] += 1
        r["id"] = f"{base}-{seen[base]}"
    else:
        seen[base] = 1

with open(OUT, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(COLUMNS)
    for r in all_rows:
        w.writerow([fmt(r[c]) if not isinstance(r[c], str) else r[c] for c in COLUMNS])

print(f"wrote {len(all_rows)} bodies to {OUT}")
for name, why in dropped:
    print(f"  dropped {name}: {why}")
