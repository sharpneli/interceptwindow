# Solar System Body Catalogue – Bodies on Rails

Nov 7, 2026 · @Claude (for Teemu) · first cut

A catalogue of the 993 bodies the game puts on rails: the Sun, the planets, 147 moons and 837 small bodies. Each one has a mass, a size and a fixed Keplerian orbit about its parent. The data is in [`data/solar-system/bodies.csv`](../../data/solar-system/bodies.csv). It comes from JPL's open databases, and a script rebuilds it from the saved raw extracts. This doc covers what was picked and why, where each number comes from, how to propagate the orbits, and how far the rails drift from JPL's own ephemeris. It answers the "Ephemerides and bodies" line of the [Research Agenda](research-agenda.md) and the body-ephemeris half of gap 1 in [Prototype Readiness](prototype-readiness-gap-analysis.md).

## The short version

- **One CSV row per body.** Each row has mass, GM, radius, the basis of each figure, J2000 ecliptic Keplerian elements about the parent, an epoch and a mean motion. Derived columns give spheres of influence, Hill radii, surface gravity and escape velocity.
- **993 bodies, under the 1,000 cap.** The selection favours what matters to the game: everything big, everything cheap to reach, everything a spacecraft has visited, and every Trojan or co-orbital that sits at a strategic point.
- **All sources are open.** Orbits come from JPL's Small-Body Database, Horizons and the SSD planet and satellite tables. Accessibility comes from NASA's NHATS list. Sizes for the big trans-Neptunian objects come from occultation and thermal results.
- **The rails hold up against JPL.** After 3.6 years of pure Kepler propagation *(calc)*, the planets are within 0.04° of Horizons, Ceres within 0.3°, the Galilean moons and Titan within 0.2° and the Moon within 2°. Irregular moons drift about 5°. Apophis fails completely because its 2029 Earth flyby changes its orbit. Close encounters are the one thing rails can't fake.
- **Only 84 masses are measured.** The other 909 are estimated from size and an assumed density, and every row says which basis it uses. Sizes are firmer: 760 are measured or from the literature, and 228 are estimated from brightness.
- **The epoch is an ephemeris constant, not a start date.** The planets and most small bodies use JD 2461200.5 (June 9, 2026 TDB). That fits "no fixed dates": the game clock can count from it without the campaign starting in 2026.

## What is in it

| Category | Count | Selection rule |
| --- | ---: | --- |
| Star, planets | 1 + 8 | All |
| Moons | 147 | Every moon with a radius of at least 2.5 km, plus every regular (Laplace-plane or equatorial) moon whatever its size |
| Dwarf planets | 9 | Ceres, Pluto, Eris, Haumea, Makemake, Gonggong, Quaoar, Orcus, Sedna |
| Main belt | 370 | Every main-belt body with a diameter of at least 77.8 km, plus 16 visited or targeted by spacecraft (Ida, Mathilde, Gaspra, Steins, Dinkinesh, the Emirates mission targets…) and Hungaria |
| Near-Earth objects | 185 | All 98 with H < 15.5 (roughly 2.5 km and up); the 60 most accessible with H ≤ 22 (about 140 m and up) by NHATS round-trip Δv; the 15 most accessible of any size; 26 mission or notable targets |
| Earth co-orbitals | 7 | Trojans 2010 TK7 and 2020 XL5, quasi-satellites Kamo'oalewa, Cardea and 2023 FW13, plus 2006 FV35 and the 2024 mini-moon 2024 PT5 |
| Mars Trojans | 8 | All known, Eureka included |
| Jupiter Trojans | 76 | All with H < 10 (roughly 60 km and up), plus the Lucy targets |
| Centaurs | 36 | The 40 brightest, minus short-arc junk |
| Trans-Neptunian objects | 105 | The 110 brightest, plus Arrokoth and the d ≥ 100 km objects, minus short-arc junk |
| Neptune Trojans | 8 | Well-observed ones |
| Comets | 31 + 2 | Mission targets, meteor-shower parents, famous periodic comets, Hale-Bopp, NEOWISE and the giant C/2014 UN271; two main-belt comets (133P, 176P) |

**By parent, the moons are** Saturn 71, Uranus 29, Jupiter 23, Neptune 16, Pluto 5, Mars 2 and Earth 1. A 2.5 km radius cut drops about 300 tiny irregular moons, mostly Saturn's 2–4 km Norse-group rocks found since 2019. They add nothing a game needs that their larger cousins don't already show.

**Dropped on purpose:**
- C/2023 A3 (Tsuchinshan–ATLAS) is on a hyperbolic orbit: it is passing through, not orbiting.
- Seven SBDB objects had no magnitude and no size. They are short-arc orbits from 2010–2021 discovery surveys and are unreliable.
- S/2009 S 2 has no size data at all.

## Where the numbers come from

| Data | Source | Notes |
| --- | --- | --- |
| Small-body orbits, H, diameter, albedo, GM, density, rotation, spectral type, Earth MOID | JPL SBDB Query API, full precision | Orbits are osculating at the SBDB epoch |
| Accessibility | NASA NHATS Data API | Minimum round-trip Δv and its mission duration, for departures in 2025–2040 |
| Planet orbits | JPL "Approximate Positions of the Planets", Table 2a (Standish), 3000 BC–3000 AD | Evaluated at the catalogue epoch, with secular rates |
| Planet physical data | JPL planetary physical parameters | Mass, radii, density, rotation, albedo |
| Moon orbits | JPL Horizons (osculating elements at the epoch) plus JPL SSD mean semi-major axes | Mean motions fitted to Horizons (see below) |
| Moon physical data | JPL satellite physical parameters (46 moons), Horizons object data, Wikipedia moon lists (literature diameters) | Wikipedia only fills sizes JPL lacks |
| Large TNO sizes and masses | Wikipedia "List of possible dwarf planets", which cites occultations, thermal results and Johnston's Archive | 24 objects |
| Planet poles | IAU WGCCRE 2015 | For reference and frame work |

**How the data was fetched.** The project's cloud workspace and the local shell both sit behind network allowlists that block JPL. The queries ran in the desktop app's browser pane instead. Results came back in chunks and were saved to `data/solar-system/sources/`, and each chunk was checked against a SHA-256 hash computed in the browser. The rebuild script reads only those saved files.

### Moon orbits needed more care

JPL's satellite mean-element table looked like the obvious source, and it failed the rails test. Two of its conventions are undocumented on the page:

- **The along-orbit angle has an unstated origin.** The plane orientation converted from JPL's Laplace and equatorial frames matched Horizons to 0.1° for Phobos, Ganymede, Titan, Ariel, Miranda, Cordelia and Charon. But the position along the orbit was off by 87° for Ganymede and 157° for Titan, even at the epoch itself.
- **The period column is not the sidereal period.** For Io it gives 1.7627 d against a sidereal 1.7691 d. It turns out to be the anomalistic period, with the argument of periapsis precessing separately.

So the moons use Horizons osculating elements at the epoch for orientation and phase. The mean motion is fitted by following the mean longitude through Horizons at +3, 10, 30, 100, 300, 1,000 and 3,000 days. A few cases need overrides:

| Case | Rule |
| --- | --- |
| Helene and Polydeuces, Telesto and Calypso | Use Dione's and Tethys's mean motion. Trojans librate, but on average they share their host's motion |
| Janus and Epimetheus | Both get their shared average. They swap orbits every four years, which rails can't show |
| Irregular moons (P > 100 d) | JPL's long-term mean period. Over the solar perturbation cycle it beats a 3,000-day fit |
| Earth's Moon | Mean lunar elements (Meeus ch. 47) with node regression and perigee advance as rates |
| Daphnis | Fitted over 100 days before 2018, when its Horizons ephemeris ends |
| S/2025 U 1 | Has no Horizons orbit. Uses JPL's mean elements, so its plane is right but its phase is approximate |

## Putting a body on rails

For a body at time *t* (JD, TDB):

1. M = `mean_anomaly_deg` + `mean_motion_deg_day` × (*t* − `epoch_jd_tdb`)
2. Ω = `node_deg` + `node_rate_deg_day` × Δt and ω = `argp_deg` + `argp_rate_deg_day` × Δt. The rates are zero except for the planets (secular, from Standish) and the Moon.
3. Solve Kepler's equation for E, then get the position in the orbital plane from `a_km` and `e`.
4. Rotate by ω, *i* and Ω into the J2000 ecliptic frame, centred on the parent.
5. Add the parent's position, recursively up to the Sun.

Use the given `mean_motion_deg_day`; don't recompute it from *a* and GM. For moons the given value is the observed mean motion, which already includes the effect of the planet's oblateness. Recomputing it can shift a fast inner moon by many degrees a year.

**Frames and centres:**
- Heliocentric rows are relative to the Sun's centre. The Sun stays fixed at the origin, and the Sun's wobble about the barycentre (up to about two solar radii) is ignored.
- **The "Earth" row is the Earth–Moon barycentre.** The Earth itself sits about 4,670 km from it, on the side away from the Moon. The same holds for Pluto: its row is the Pluto–Charon barycentre, and its four small moons orbit that point. Charon's elements are Pluto-centred, so putting it around the barycentre misplaces it by about 2,100 km *(calc)*.
- Every orbit uses the J2000 ecliptic and equinox, Horizons's ICRF-based ecliptic frame. This is the frame of the existing "heliocentric doubles" decision.

## How good the rails are

Positions propagated from the catalogue to Jan 1, 2030 (3.6 years past the epoch), compared with JPL Horizons *(calc)*:

| Body | Position error | Error as angle at parent |
| --- | ---: | ---: |
| Earth–Moon barycentre | 5,060 km | 0.00° |
| Mars | 54,000 km | 0.01° |
| Jupiter | 586,000 km | 0.04° |
| Neptune | 1.97 million km | 0.02° |
| Ceres | 2.18 million km | 0.28° |
| Eros | 147,000 km | 0.04° |
| Patroclus | 1.62 million km | 0.08° |
| Moon | 13,200 km | 2.1° |
| Io | 3,100 km | 0.21° |
| Titan | 2,100 km | 0.09° |
| Triton | 9,500 km | 1.5° |
| Himalia (irregular) | 1.08 million km | 5.5° |
| **Apophis** | **194 million km** | **64°** |

The rails are good to a fraction of a degree for planets, big asteroids and regular moons over years. Errors grow roughly linearly with time, so expect several degrees per century for the main belt *(calc, from the Ceres rate)*. That meets the "close enough" rule for the Rails tier in the [Fleetwright Principles](../design/fleetwright-principles-for-intercept-window.md).

**Where rails break:**
- **Close planetary encounters.** Apophis passes 38,000 km from Earth's centre on Apr 13, 2029, and its orbit afterwards is a different one. The catalogue has 64 potentially hazardous objects (tag `pha`: Earth MOID ≤ 0.05 AU, H ≤ 22), and any of them can be re-anchored by a flyby. For the game this is a feature: a known flyby date is an event that re-anchors the rail, which fits the Fleetwright rails model.
- **Strongly perturbed moons.** The Moon is off by evection and variation (±1–2°). Irregular moons swing by the Sun's pull. Hyperion, Methone and Anthe librate in resonances. Mean rails reproduce none of this.
- **Old epochs.** A few bodies keep their SBDB epoch: Bennu (2010), Pluto (2016), several comets (2011–2022) and the newest objects. They drift a little more.

## Masses and sizes

**The basis of each figure is in the row** (`mass_basis`, `radius_basis`).

| Basis | Masses | Radii |
| --- | ---: | ---: |
| Measured (spacecraft, binary orbits, radar, thermal infrared, occultation) | 84 | 654 + 24 literature |
| Literature estimate (moon lists) | – | 80 |
| Estimated | 909 | 228 from absolute magnitude H |
| Assumed | – | 7 (comet nuclei, 2 km radius) |

**Size from brightness:** D = 1329 km / √p × 10^(−H/5). The albedo p comes from SBDB where known. Otherwise it is set by spectral type (C 0.06, S 0.25, M 0.15, X 0.10, E 0.45), and failing that by category (NEO 0.14, main belt 0.10, Jupiter Trojan and centaur 0.07, TNO 0.09). A factor-of-two albedo error is a 41 % size error and a factor of 2.8 in mass. Estimated sizes are first-cut placeholders.

**Mass from size:** spherical volume times a density. Measured densities are used where SBDB has them. Otherwise the density goes by spectral type (C 1.4, S 2.7, M 3.5, X 2.0, E 2.5 g/cm³), then by category (comets 0.5, Trojans, centaurs and small TNOs 1.0, TNOs over 600 km 1.8). Small moons without a measured mass use 0.5 g/cm³ for Saturn's porous ring-region moons, 1.2 for other regular moons and 1.5 for irregular moons. These densities are typical sample values, not measurements of each body. The [solar resources baseline](solar-resources/03-small-bodies.md) is the place for real composition.

## Using it in the game

- **IDs are stable slugs.** Planets and moons go by name (`earth`, `titan`). Numbered minor planets use number and name (`1-ceres`, `85-io`), which keeps them apart from the moon `io`. The rest use their designation (`2024-yr4`) or the full comet name (`1p-halley`).
- **`category` and `group` are region labels.** `group` gives the main-belt zone (inner, middle, outer, Cybele, Hilda, Thule), the NEO class (Aten, Apollo, Amor), the comet family, the TNO class (plutino, twotino, classical, scattered, detached) and the Trojan camp (Jupiter L4 "Greek" with 49 bodies, L5 "Trojan" with 27). These match the regions in the [Outward](../design/outward-the-belt-jupiter-and-independence-from-earth.md) and [resource field](../design/resource-fields-grades-and-yield-curves.md) designs.
- **NHATS Δv is a ready-made accessibility score** for 82 NEOs: the cheapest round trip from low Earth orbit, from 3.3 km/s for 2026 QQ8 upward. The "nhats_tiny" set are metre-scale rocks, the cheapest bodies in the system. They are realistic first targets for a bag-a-boulder mission in the [bulk logistics](interplanetary-bulk-logistics-mines-depots-and-shipyards.md) sense.
- **The derived columns cover the physics a ship needs:** `soi_radius_km` (Laplace sphere of influence), `hill_radius_km`, `surface_gravity_m_s2` and `escape_velocity_km_s`. Pluto and Charon are a true binary with the barycentre outside Pluto, so Charon's sphere-of-influence and Hill figures are only rough.
- **The spectral columns** (`spec_tholen`, `spec_smass`) cover 442 bodies. That is enough to seed C/S/M resource classes until the resource-field model assigns grades.

## Rebuilding and refreshing

`data/solar-system/build_catalogue.py` rebuilds `bodies.csv` from `sources/` using only the Python standard library. `check_catalogue.py` runs the structural checks. `rails_check.py` repeats the Horizons comparison above.

To refresh the data, re-run the queries listed in `data/solar-system/README.md` from a browser, or from any machine that can reach `ssd-api.jpl.nasa.gov`, and overwrite the files in `sources/`. Selection is by rule, so a refresh may swap a few bodies near the cut lines.

## Open questions

- [ ] Is 2.5 km the right radius cut for moons, or should the ~300 small irregulars come in later as cheap scenery?
- [ ] Should NEO flybys (Apophis 2029 and others) be scripted re-anchoring events, or should the catalogue epoch move past them?
- [ ] For the cislunar battler: is the Earth–Moon barycentre plus mean lunar elements enough, or does the Moon need its main periodic terms (evection, variation)?
- [ ] Should the moons' node and apsidal precession go on the rails? JPL gives the periods, but the frames need care. Triton's 1.5° in 3.6 years is the largest effect.
- [ ] Should the ten or so 2025–2026 discoveries near the TNO and centaur cut lines be held back until their orbits firm up?
- [ ] Mass uncertainty: should estimated masses carry an error band that surveys can narrow (see [Detection and the Picture](../design/detection-and-the-picture.md))?

## Sources

- JPL Small-Body Database Query API, https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html, and SBDB API, https://ssd-api.jpl.nasa.gov/doc/sbdb.html (queried Nov 7, 2026)
- NASA NHATS Data API, https://ssd-api.jpl.nasa.gov/doc/nhats.html (queried Nov 7, 2026)
- JPL Horizons API, https://ssd-api.jpl.nasa.gov/doc/horizons.html (queried Nov 7, 2026)
- JPL SSD, Planetary Satellite Mean Elements, https://ssd.jpl.nasa.gov/sats/elem/
- JPL SSD, Planetary Satellite Physical Parameters, https://ssd.jpl.nasa.gov/sats/phys_par/
- JPL SSD, Planetary Physical Parameters, https://ssd.jpl.nasa.gov/planets/phys_par.html
- E. M. Standish, Approximate Positions of the Planets, https://ssd.jpl.nasa.gov/planets/approx_pos.html
- Wikipedia, "Moons of Jupiter", "Moons of Saturn", "Moons of Uranus", "Moons of Neptune" (sizes for moons JPL does not size), and "List of possible dwarf planets" (large TNO sizes and masses), accessed Nov 7, 2026
- E. Lellouch et al. (2022), "The 2.15 mm ALMA thermal emission of comet C/2014 UN271", ApJL 930 L22 (nucleus size)
- J. Meeus, *Astronomical Algorithms*, 2nd ed., ch. 47 (mean lunar elements)
- B. A. Archinal et al. (2018), "Report of the IAU Working Group on Cartographic Coordinates and Rotational Elements: 2015", Celest. Mech. Dyn. Astron. 130:22 (poles)
