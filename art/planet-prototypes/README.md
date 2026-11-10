# Planet Prototypes

Nov 10, 2026 · @Claude · first look: planets, Moon and Mars elevation, small-body generator

Two browser benches.

- `planet-bench.html` tests the planet texture approach: a 2k base map per body, with procedural detail that fades in as the camera closes in. It needs `planet-textures.js` beside it.
- `small-body-bench.html` tests a best-guess shape generator for asteroids and small moons, beside real shape models. It needs `small-body-data.js` beside it. See [Small bodies](#small-bodies).

## The short version

- **Base maps are 2048 × 1024.** One map pixel is 19.5 km on Earth, 10.4 km on Mars and 5.3 km on the Moon *(calc)*.
- **Detail is a ladder of octaves.** Each octave is half the size of the last. An octave counts once it is wider than a few screen pixels, so there is no switch distance.
- **Detail never replaces the base map.** It adds slopes and small colour changes around the map's colour. Zooming out gives the real map back.
- **Earth's coast is the exception to 2k.** It comes from Fleetwright's land file (Natural Earth 1:10M) as an 8192 × 4096 distance field, so coasts stay sharp. Noise breaks the coast up below the file's resolution.
- **The Moon and Mars carry real elevation.** A 16-bit height map per body gives the large relief: crater walls, Olympus Mons, the Tharsis volcanoes. Procedural craters only fill in below the map's resolution.
- **Earth's land detail follows a surface-class map.** MODIS land cover is reduced to each map pixel's shares of forest, cropland, barren ground and ice (the rest is grass and shrub). Close in, noise breaks the shares into patches, and each class gets its own texture: canopy clumps, field patchwork, dune streaks, smooth ice.
- **Everything is seeded by integer hashes.** A body looks the same on every machine and every run.

## What the bench shows

| Control | What it does |
| --- | --- |
| Body | Earth, Moon or Mars |
| View | Jumps to a set scale: whole disc, one screen pixel per map pixel, 1 km and 100 m per pixel |
| Split compare | Left half shows the base map alone, right half adds detail |
| Sun phase | Turns the Sun round the body; relief shows best near the terminator |
| Relief | Scales all slopes; ×1 is the intended look |
| Handover card | Scale of a screen pixel against a map pixel, and how many procedural octaves are on screen |

## Files

| File | In git | What it is |
| --- | --- | --- |
| `planet-bench.html` | yes | The bench: one WebGL 2 shader that draws the sphere per pixel |
| `make_textures.py` | yes | Builds the maps and `planet-textures.js` from `sources/` and Fleetwright's land file. Height maps are 16-bit, packed as red (high byte) and green (low byte) |
| `planet-textures.js` | no | Generated. The maps as data URIs, so the bench runs from a local file |
| `sources/` | no | Downloaded source maps and shape models |
| `small-body-bench.html` | yes | The small-body bench: the generator and the view in one file |
| `make_small_bodies.py` | yes | Turns real shape models and catalogue rows into `small-body-data.js` |
| `small-body-data.js` | no | Generated. Real shapes as distance volumes, and the bench's catalogue rows |

To rebuild the textures (needs numpy, Pillow and scipy):

```
python -I make_textures.py sources C:\git\fleetwright\Content\World\land-10m.bin .
python -I make_small_bodies.py sources\small-bodies ..\..\data\solar-system\bodies.csv .
```

## Small bodies

Only 31 of the catalogue's 993 bodies have axes, and a dozen or so have a real shape model. The rest need a shape made up from what the row does say.

### The short version

- **A body is a distance volume.** A cube of 160³ cells, each holding the signed distance to the surface (negative inside), in units of the body's radius. It holds necks, overhangs and hollows. Real shape models convert to the same form, so a real shape is a drop-in replacement for a generated one.
- **The generator reads one catalogue row** (radius, axes, density, spin period, type, albedo) and turns it into seven weights, the body's character. Each weight is a smooth function of the row plus seeded rolls. There are no category switches.
- **The same row always gives the same body.** A variant number gives other bodies the row could equally be.
- **Small craters, boulders and grooves are not in the volume.** The shader adds them, as on the planets, laid out in 3D on the surface's tangent plane so nothing stretches on steep walls.
- **The view marches a ray through the volume**, so shapes cast hard shadows on themselves.

### Resource cell views

The toolbar's Cells, Cutaway, Sunlight and Ice picture views show how resource fields would sit on a shape: patches of real surface extended inward as columns, depth read from the volume, sunlight over one spin with cold traps, and a made-up ice picture with hatching for guesses. Click a cell for its area, column mass, depth and sunlight. The scheme is written up in the design doc.

### Character weights

| Weight | What it does | What drives the guess |
| --- | --- | --- |
| Lumpiness | Broad bulges and hollows | Falls with size: 1/(1 + (R/120 km)²) |
| Facets | Flat faces, as on a broken fragment | Small and dense bodies; less on rubble |
| Two lobes | One ellipsoid splits smoothly into two | Elongation a/b from 1.3 to 2.0, plus a rare roll |
| Spinning top | Rounder, with an equatorial ridge | Under a few km, low density, fast spin |
| Boulders | Boulders in place of small craters | Under a few km, low density |
| Grooves | Two families of parallel pitted trenches | A roll |
| Largest crater | Diameter of the biggest crater | A roll, 0.4 to 1.15 of the mean radius |

Rubble is read from density: 1 at 1.3 g/cm³ falling to 0 at 2.4. Without a density it is guessed from albedo and type. Without axes, the ratios are rolled, nearer round as bodies get bigger.

### Build order of a shape

1. One ellipsoid from the axis ratios, or two lobes in smooth union, with a slight bend if elongated.
2. Eight planes each slice off a share, scaled by Facets.
3. Low-frequency noise pushes the surface in and out, by Lumpiness.
4. Spinning top adds the equatorial ridge.
5. Craters from the largest down to 12% of the radius in diameter, numbers rising as D⁻². Each is a spherical cap cut into the surface with a raised rim. Old ones are shallow.
6. The result is sampled into the volume, clamped to a band either side of the surface.

All numbers are first-cut placeholders, set by eye against the real shapes.

### Real shapes for comparison

`make_small_bodies.py` reads Celestia `.cmod` meshes from `sources/small-bodies/`, turns each onto its own long and short axes, and writes `small-body-data.js` (out of git). Each mesh has a `.license` file beside it; the bench shows the credit.

| Body | Shape model | Licence |
| --- | --- | --- |
| Phobos, Deimos | Ernst et al. 2023 | CC BY 4.0 |
| Eros, Itokawa | Gaskell, NASA PDS 2008 (Itokawa also ISAS/JAXA) | CC0, CC BY 4.0 |
| Bennu | OSIRIS-REx Altimetry Working Group | CC0 |
| Ida | Thomas et al., NASA PDS 2021 | CC0 |
| Mathilde | Stooke, NASA PDS 2016 | CC0 |
| Toutatis | Hudson, Ostro and Scheeres 2003, NASA PDS | CC0 |
| Kleopatra | Vernazza et al. 2021 | CC BY 4.0 |
| Hyperion | Thomas et al., NASA PDS 2018 | CC0 |
| Gaspra, Vesta | From CelestiaContent, no licence file found | Check before use |

### Open questions

- [ ] The volume is 160 cells a side, so on a long body one cell is about 3% of the radius. Features under a few cells come from the shader, not the shape.
- [ ] The first version stored one radius per direction. It tore on necks and stretched detail on steep walls, so it was replaced by the volume.
- [ ] `shape_km` in `bodies.csv` mixes semi-axes (Phobos) and full diameters (Eros, Ceres). The generator uses ratios only, so it is unaffected, but the column should be made consistent.
- [ ] Two lobes is a roll once a body is elongated. Lightcurve amplitude, where known, would be a better clue.
- [ ] Albedo markings are a slow noise drift. Bright crater walls and dark ponds would add a lot.
- [ ] The engine version should build a mesh from the volume (marching cubes or similar) instead of marching it per pixel.

## Sources and licences

| Map | Source | Licence |
| --- | --- | --- |
| Earth colour, night lights, elevation | NASA Blue Marble and Black Marble, as packaged in the `three-globe` examples | NASA imagery, public domain |
| Earth coast | Natural Earth 1:10M via Fleetwright's `land-10m.bin` (world-atlas, ISC) | Public domain |
| Earth surface classes | MODIS MCD12C1 land cover 2019 (IGBP classes, 0.05°), from the `JPL-Evapotranspiration-Algorithms/MCD12C1-2019-v006` mirror | NASA data, public domain |
| Moon colour | Solar System Scope `2k_moon.jpg`, from NASA LRO data | CC BY 4.0 |
| Mars colour | Solar System Scope `2k_mars.jpg`, from NASA Viking data | CC BY 4.0 |
| Moon elevation | LROC WAC GLD100 at 16 px/deg (`WAC_GLD100_E000N1800_016P`), from the `jaanga/moon` mirror | NASA/ASU data, public domain |
| Mars elevation | MGS MOLA MEGDR at 4 px/deg (`megt90n000cb`), from the `jaanga/mars` mirror | NASA data, public domain |

The source maps came from GitHub mirrors, because that was what the session could reach. Before anything ships, fetch them again from NASA, USGS and Solar System Scope directly and check each licence.

## Open questions

- [x] Earth land close up was bland. A surface-class map now drives it. Still plain: no rivers, lakes, roads or towns, and wetland and built-up shares are stored but unused.
- [ ] Clouds for Earth: a map, a shader, or none on the strategic view?
- [ ] The Moon's poles are wrong. GLD100 stops at 79° latitude and the mirror's file is filler beyond it, and the equirectangular maps pinch at the pole. The south pole matters for the game (ice), so it needs LOLA polar data and cube-face maps.
- [ ] Mars elevation is 1440 × 720, coarser than the colour map. MOLA exists at far higher resolution.
- [ ] Relief is shading only. Mountains and crater rims cast no shadows yet.
- [ ] Night lights at 2k clip into blobs. Cities should come from the shared city drawing system.
- [ ] Below about 20 m per pixel the shader runs out of float precision. The engine version needs camera-relative coordinates.
- [ ] Gas giants, rings and the catalogue's small bodies are not in the bench yet.
