# Solar system body catalogue

The bodies the game puts on rails: the Sun, 8 planets, 147 moons and 837 small bodies (993 in all), with masses, sizes and fixed Keplerian orbits. The study behind it, with selection rules, accuracy and caveats, is [Solar System Body Catalogue – Bodies on Rails](../../research/studies/solar-system-body-catalogue.md).

## Files

| File | What it is |
| --- | --- |
| `bodies.csv` | The catalogue. One row per body, UTF-8 |
| `build_catalogue.py` | Rebuilds `bodies.csv` from `sources/`. Python 3, standard library only |
| `check_catalogue.py` | Structural checks: unique ids, parents exist, moons inside Hill spheres, periods vs Kepler |
| `rails_check.py` | Propagates sample bodies to 2030-01-01 and compares with JPL Horizons |
| `sources/` | Raw extracts from JPL, saved Nov 7, 2026 |

## Columns of `bodies.csv`

| Column | Meaning |
| --- | --- |
| `id` | Stable slug: `earth`, `titan`, `1-ceres`, `2024-yr4`, `1p-halley` |
| `name`, `designation` | Display name; full official designation |
| `naif_id` | NAIF/SPK id (works as a Horizons `COMMAND`) |
| `parent` | `id` of the body it orbits; empty for the Sun |
| `category` | star, planet, dwarf_planet, moon, main_belt, neo, earth_coorbital, mars_trojan, jupiter_trojan, neptune_trojan, centaur, tno, comet, main_belt_comet |
| `jpl_class` | SBDB orbit class (MBA, OMB, APO, ATE, AMO, TJN, CEN, TNO, JFc, HTC, COM…) |
| `group` | Region label: main-belt zone, NEO class, Trojan camp, TNO class, moon family |
| `gm_km3_s2`, `mass_kg` | Gravitational parameter and mass (G = 6.6743e-20 km³ kg⁻¹ s⁻²) |
| `mass_basis` | `measured…` or `estimated (density X g/cm3 assumed)` |
| `radius_km`, `radius_basis` | Mean radius and where it came from |
| `density_g_cm3`, `albedo`, `abs_mag_h` | Where known (H is V(1,0) for moons and planets) |
| `rot_period_h` | Rotation period, hours; negative means retrograde (planets) |
| `spec_tholen`, `spec_smass` | Spectral types (SBDB) |
| `shape_km` | Triaxial dimensions where known |
| `surface_gravity_m_s2`, `escape_velocity_km_s` | From GM and the mean radius |
| `soi_radius_km`, `hill_radius_km` | Laplace sphere of influence and Hill radius relative to the parent |
| `epoch_jd_tdb` | Epoch of the elements (JD, TDB) |
| `frame` | J2000 ecliptic and equinox, centred on the parent |
| `a_km`, `a_au`, `e`, `i_deg`, `node_deg`, `argp_deg`, `mean_anomaly_deg` | Keplerian elements at the epoch |
| `mean_motion_deg_day`, `period_days` | Rate of mean anomaly; use it as given rather than recomputing from a and GM |
| `node_rate_deg_day`, `argp_rate_deg_day` | Secular rates (planets, Moon); zero elsewhere |
| `q_au`, `big_q_au` | Periapsis and apoapsis distance |
| `earth_moid_au` | Minimum orbit intersection distance with Earth (small bodies) |
| `nhats_min_dv_km_s`, `nhats_min_dur_days` | NASA NHATS minimum round-trip Δv from LEO and its mission duration (2025–2040 departures) |
| `pole_ra_deg`, `pole_dec_deg` | Spin pole (IAU 2015) for the Sun, planets and Pluto |
| `tags` | Why the body was selected (`mb_large`, `neo_large`, `nhats_big`, `neo_mission`, `lucy`…) |
| `notes`, `source` | Caveats and provenance per row |

## Propagation in one paragraph

M = M₀ + n·(t − epoch); Ω and ω advance by their rates; solve Kepler's equation; rotate by ω, i, Ω into the ecliptic; add the parent's position. "Earth" is the Earth–Moon barycentre and "134340 Pluto" is the Pluto–Charon barycentre.

## Refreshing the data

The project's cloud workspace and the local shell can't reach JPL (network allowlists), so the queries were run from a browser. Any machine that can reach `ssd-api.jpl.nasa.gov` can re-run them:

- Small bodies: `https://ssd-api.jpl.nasa.gov/sbdb_query.api?full-prec=true&fields=spkid,full_name,pdes,kind,class,neo,pha,H,diameter,albedo,GM,density,rot_per,spec_B,spec_T,extent,epoch,e,a,q,i,om,w,ma,tp,M1,moid` with these selections:
  - main belt `sb-class=MBA,IMB,OMB,MCA` and `diameter|GE|75`
  - `sb-group=neo` and `H|LT|15.5`
  - `sb-class=TJN` and `H|LT|10`
  - `sb-class=CEN&sort=H&limit=40`
  - `sb-class=TNO&sort=H&limit=110`
  - all objects with `diameter|GE|100`
  - named targets fetched one by one through `sbdb.api?sstr=…`
- Accessibility: `https://ssd-api.jpl.nasa.gov/nhats.api` (default parameters)
- Moons: Horizons `EPHEM_TYPE=ELEMENTS`, `REF_PLANE=ECLIPTIC`, `CENTER=500@<planet>` (`500@9` for Styx, Nix, Kerberos and Hydra), at JD 2461200.5 + 0, 3, 10, 30, 100, 300, 1000 and 3000 days; plus `https://ssd.jpl.nasa.gov/sats/elem/` and `/sats/phys_par/`
- Planets: `https://ssd.jpl.nasa.gov/planets/approx_pos.html` (Table 2a) and `/planets/phys_par.html`

The SBDB API serves one request at a time per client, so query it sequentially.
