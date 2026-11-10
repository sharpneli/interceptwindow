# Intercept Window: Body Surfaces and Shapes – Base Maps, Procedural Detail and Generated Small Bodies

Nov 10, 2026 · @Teemu, @Claude · agreed approach, prototyped in two browser benches; resource cells are a proposal

How the game draws the 993 bodies in the catalogue: planets and large moons from real maps, small bodies from generated shapes, and one procedural detail system on top of both. The approach is decided. The numbers are first-cut placeholders set by eye in the benches ([`art/planet-prototypes/`](../../art/planet-prototypes/README.md)); the structure is the part to keep.

## The short version

- **Three kinds of body, one detail system.** Mapped bodies get a real 2k base map. Gas giants, rings and the Sun get shaders. Everything else gets a generated shape. The same procedural detail sits on top of all solid surfaces.
- **The usual view is far away.** 2k maps are enough for it. Close views are filled by procedural detail, which is allowed to be plain.
- **Detail never replaces the base map.** It adds slopes and small colour changes around the map's own colour, so zooming out always gives the real map back.
- **No switch distance.** Detail is a ladder of octaves. Each octave fades in once it is wider than a few screen pixels.
- **Earth's coast is the one exception to 2k.** It comes from the Fleetwright land file as a distance field. Earth is not where the player spends time, so its land detail is last in the queue.
- **A small body is a distance volume.** A cube of cells holding the signed distance to the surface. A generator fills it from one catalogue row. A real shape model converts to the same form and replaces the guess.
- **The generator guesses a character, not a category.** Seven smooth weights (lumpiness, facets, two lobes, spinning top, boulders, grooves, largest crater) come from the row's numbers plus seeded rolls.
- **Resource fields sit on cells cut from the real shape.** A cell is a patch of surface extended inward to the core, with depth read from the same volume. On a sphere this is the geodesic grid the bases doc already assumes.
- **The look shows only what is measured.** Hidden resources never leak into the texture.
- **Deterministic throughout.** The same body always looks the same, on every machine. All randomness is integer hashes seeded by the body's id.

## Decisions

| # | Decision | Why |
| --- | --- | --- |
| 1 | 2048 × 1024 base maps for mapped bodies | The usual view is from far off; one pixel is 5–20 km, which is finer than the screen shows at whole-disc scale |
| 2 | Procedural detail below the base map's resolution, on every solid body | Close views are rare; real high-resolution data would cost a tiled pipeline for little play value |
| 3 | Earth's land and water from the Fleetwright land file | Coasts are what people recognise, and launch sites are coastal |
| 4 | 16-bit elevation maps where they exist (Moon, Mars so far) | Real relief at the terminator is what makes airless bodies read as real |
| 5 | Small bodies as generated distance volumes, real shape models where they exist | Only about a dozen bodies have shape models; the belt is hundreds of potatoes |
| 6 | Cities and bases are drawn by a separate shared system | The same procedural city drawing serves off-world colonies and Earth |
| 7 | Resource cells are patches of real surface, extended inward; no unwrapping | One address (body, patch, depth band) works on spheres and potatoes alike |
| 8 | A body's look depends only on measured things (type, albedo, density, shape) | Otherwise players read ore from the texture and the shake-up rule breaks |
| 9 | Source data stays out of git | Third-party maps and models; the repo holds the scripts and the credits |

## Which body gets what

| Kind | Bodies | Shape | Surface |
| --- | --- | --- | --- |
| Mapped | Earth, Moon, Mars, Mercury, Venus, Ceres, Vesta, Pluto, Charon, the large moons (about 25–30) | Sphere | 2k colour map, elevation where it exists, procedural detail below |
| Fluid | Sun, Jupiter, Saturn, Uranus, Neptune, rings | Sphere or ring plane | Shader; a 2k map as the base for the banded giants |
| Small, with a shape model | Phobos, Deimos, Eros, Bennu, Itokawa, Ida, Mathilde and a few more | Real distance volume | Procedural detail |
| Small, without | The rest of the catalogue (about 950) | Generated distance volume | Procedural detail |

The line between "mapped" and "small" is not a size cutoff. A body is mapped if a map exists. Vesta has both a map and a shape model, and can use both.

## Mapped bodies

### Base maps

Maps are equirectangular, longitude 0 at the centre, north up.

| Body | One map pixel at the equator *(calc)* | Whole disc fills a 1000 px view at *(calc)* |
| --- | --- | --- |
| Earth | 19.5 km | 12.7 km per screen pixel |
| Mars | 10.4 km | 6.8 km |
| Moon | 5.3 km | 3.5 km |

So the base map carries the picture alone until a body roughly fills the screen. Closer than that, detail starts to contribute. It gets more use than "extreme close-up" suggests.

Some bodies are mapped on one hemisphere only (Triton, the Uranian moons). The missing half is filled procedurally, matched in colour and crater density to the mapped half.

### The detail ladder

The law, the same on every solid body:

- Octave k has wavelength λ₀ / 2ᵏ, where λ₀ is two base-map pixels. Everything wider than λ₀ is in the base map already.
- An octave's weight is a smooth step from 0 to 1 as its wavelength goes from 1 to 3 screen pixels. It is never switched.
- Each octave adds a **slope** and a small **colour change**. Slopes are scale-free: an octave's height is proportional to its wavelength, so every octave tilts the surface by about the same amount.
- Both are zero-mean. Averaged over a base-map pixel, the surface is the base map.

Two kinds of octave exist so far:

- **Noise** (value noise with an exact gradient): rolling ground, dust and colour mottling.
- **Craters and boulders**: one per cell of a grid, cells halving per octave, so numbers rise as size falls. A crater is a bowl with a raised rim; a boulder is the same shape turned inside out. The base map can steer density: on the Moon the dark maria get fewer craters.

### Elevation

Elevation maps are 16-bit. Eight bits is not enough: on the Moon one step would be about 78 m *(calc)*, which shows as terraces on the maria at a low sun.

The view takes slopes from the elevation map by central differences and adds them to the detail ladder's slopes. Relief is **shading only** for now. Nothing casts a shadow on a mapped body yet.

### Earth

- **Coast.** The Fleetwright land file (Natural Earth 1:10M) is rasterised to an 8192 × 4096 signed distance field. Coasts stay sharp where the 2k colour map is a blur. Noise breaks the coast up below the field's 4.9 km pixel *(calc)*.
- **Coast colour.** The 2k map smears sea into land along the coast. Close in, the view reads land colour from a little way inland and sea colour from a little way out, along the distance field's gradient.
- **Sea.** Specular sun glint, masked by the coast field.
- **Night side.** City lights from a 2k map, as a placeholder for the city drawing system.
- **Air.** A thin limb and a blue haze that thickens toward the limb. No clouds yet.
- **Land.** A surface-class map drives the detail. MODIS land cover (17 IGBP classes at 0.05°) is reduced to each 2k pixel's **shares** of forest, cropland, barren ground and ice; the remainder is grass and shrub. Shares filter cleanly where class ids would not. Close in, noise breaks the shares into patches of one class each, and each class gets its own texture: canopy clumps for forest, a patchwork of plots for cropland (each district of about 45 km with its own grid direction), wind-streaked dunes over part of each desert, and smooth ice. Each class leans the base colour its own way, divided by the pixel's mean lean, so the map's colour is kept on average.

Earth is still plain close up: no rivers, lakes, roads or towns. That is acceptable, since the player spends little time there, and towns belong to the city drawing system.

### Light

One hard sun, black night side, no fill light, as the style anchors ask.

- Airless regolith is flatter than a matte ball. The view blends Lambert toward Lommel–Seeliger: 0.75 for the Moon, 0.35 for Mars, 0.6 for small bodies.
- Atmospheres are a path-length haze on the disc and an exponential glow off the limb. Mars gets a weak dusty one.

## Small bodies

### The data problem

Of 993 catalogue rows, 31 have axes and about a dozen bodies have a usable shape model. The generator must make a reasonable body from very little: radius, and sometimes axes, density, spin period, spectral type and albedo.

### A body is a distance volume

A cube of N³ cells. Each cell holds the signed distance to the surface, negative inside, in units of the body's radius, clamped to a band either side of the surface.

- It holds necks, overhangs and hollows.
- A real shape model converts to the same form, so a real shape is a drop-in replacement for a generated one.
- It casts shadows on itself for free: the view marches a ray toward the Sun through the same volume.
- The bench uses N = 160. On a long body one cell is about 3% of the radius *(calc)*. Features smaller than a few cells come from the detail ladder, not the shape.

The first prototype stored one radius per direction instead. It tore on necks and stretched detail along steep walls, so it was dropped.

### The character

The generator turns a row into seven weights from 0 to 1. Each is a smooth function of the row plus seeded rolls u. There are no category switches. With R the mean radius in km:

- **small** = 1 / (1 + (R / 120)²): how far the body is from pulling itself round.
- **tiny** = 1 / (1 + (R / 1.5)²).
- **rubble** = 1 at a density of 1.3 g/cm³ falling smoothly to 0 at 2.4. Without a density: 0.6 for dark bodies, 0.3 for bright ones.
- **fast** = 1 at a spin period of 3 h falling to 0 at 7 h. Without a period: 0.3.

| Weight | What it does | First-cut law |
| --- | --- | --- |
| Lumpiness | Broad bulges and hollows | 0.9 · small · (0.45 + 0.75u) |
| Facets | Flat faces, as on a broken fragment | small · (1 − 0.7 · rubble) · (0.25 + 0.75u) |
| Two lobes | One ellipsoid splits smoothly into two | small · the larger of: a step over a/b from 1.3 to 2.0, times (0.55 + 0.45u); and a rare roll |
| Spinning top | Rounder, with an equatorial ridge | tiny · rubble · (0.4 + 0.6 · fast) |
| Boulders | Boulders in place of small craters | 1.2 · tiny · (0.5 + 0.5 · rubble) |
| Grooves | Families of parallel pitted trenches | A roll, weaker on tiny bodies |
| Largest crater | Diameter of the biggest crater, in radii | 0.4 + 0.75u |

Where the row has no axes, the ratios are rolled: b/a = 1 − small · (0.06 + 0.42u^1.3) and c/b = 1 − small · (0.05 + 0.30u). Only ratios are ever used; the size comes from the mean radius.

A **variant** number reseeds the rolls. Variant 0 is the body. Other variants are bodies the same row could equally be, for campaign shake-ups or for bodies that are not in the catalogue.

### Building the shape

1. **Base solid.** One ellipsoid from the axis ratios. As Two lobes rises it splits into two ellipsoids in smooth union, unequal in size, with a slight bend if the body is elongated.
2. **Facets.** Eight planes each slice a share off, scaled by Facets.
3. **Lumps.** Low-frequency noise pushes the surface in and out.
4. **Spinning top.** The base is pulled toward round and an equatorial ridge is added.
5. **Craters.** From the largest down to 12% of the radius in diameter, numbers rising as D⁻². Each is a spherical cap cut into the surface where a random ray from the centre meets it, with a raised rim. Depth is 8–16% of diameter, less on rubble. Most are old and shallow.
6. **Sample** the result into the volume.

The long axis points at longitude 0 and the short axis is the pole, as for real tidally locked moons.

### Surface detail on a shape

The same ladder as on planets, with one change: it works in 3D.

- A crater's cell counts where its point lies close to the surface. The crater is then laid on the surface's tangent plane, so nothing stretches on steep walls.
- Grooves are where evenly spaced parallel planes cut the body, two families per body, pitted along their length.
- Colour is a tint from type and albedo with a slow drift between two units.

### How it compares with real shapes

Judged in the bench, real shape on the left, guess on the right, same light and surface:

| Body | Result |
| --- | --- |
| Phobos | A sibling of the real one: proportions, one big crater, grooves |
| Bennu | The best match: a boulder-covered spinning top from density, size and spin alone |
| Eros, Gaspra | Convincing elongated potatoes |
| Kleopatra | Gets a waist, milder than the real dog-bone |
| Toutatis | Too eager: a clean snowman where the real body is one lumpy piece |
| Vesta, Ceres | Near-round with craters, as they should be |

### Known flaws: the chisel marks

Generated bodies still look tooled in places. The causes are known:

- **Grooves are too regular.** They are straight, evenly spaced and all the same profile. Real grooves wander, fade and vary in width.
- **Large crater rims are thin sharp arcs.** Old craters show as faint complete circles. Real old rims are broken, slumped and overprinted.
- **Small craters are all perfect circles** with one profile. Real ones are elliptical on slopes, overlap, and degrade at different rates.
- **Albedo ignores the terrain.** Bright crater walls and dark dust ponds would hide a lot of the tooling.

These are tuning and detail work, not a change of approach.

## Resource cells on a shape

*Proposal, prototyped in the small-body bench (Cells, Cutaway, Sunlight and Ice picture views).*

[Resource Fields](resource-fields-grades-and-yield-curves.md) stores each field per cell of a surface grid and per depth band, and treats a small body as one cell. [Bases and Settlements](bases-settlements-and-the-civilian-economy.md) puts the fields on a geodesic grid and asks whether small bodies need more than a handful of sites. A grid addressed by direction from the centre fails on these shapes for the same reason the first shape format did: one direction can meet the surface twice, and a cell at the tip of Eros covers far more ground than one at its waist.

### The scheme

1. **Seeds.** Spread K points evenly over the real surface. Each new seed is the surface point farthest from all seeds so far.
2. **Patches.** Every surface point belongs to its nearest seed. Patches come out roughly equal in real area.
3. **Columns.** Every interior point belongs to the patch of its nearest surface point. The body is cut into columns that meet at the core.
4. **Depth.** A point's depth is its distance to the surface, which the volume already holds. Depth bands follow the real shape, necks included.
5. **Tonnage.** A column's mass is its share of the body's volume times the body's mass. All columns sum to the catalogue mass, so the mass ledger closes.
6. **Thin bands.** Regolith bands are metres thick; a volume cell on Phobos is about 350 m *(calc)*. A thin band's tonnage is patch area × thickness × density. The deep remainder takes what is left of the column.

So a cell's address is **body, patch, depth band**. On a sphere the scheme reduces to a geodesic grid with radial depth, so planets and potatoes share it.

### How many cells

K grows smoothly with real surface area and is never less than one. First cut: K = 1 + (area / 0.456 km²)^0.45, capped at 400 in the bench.

| Body | Surface area | Cells *(calc, bench)* |
| --- | --- | --- |
| Bennu | 0.8 km² | 2 |
| Toutatis | about 120 km² | 12 |
| Eros | about 1,100 km² | 33 |
| Phobos | about 1,550 km² | 41 |
| Vesta | about 870,000 km² | 400 (capped) |

A 500 t boulder stays one cell, as the resource doc says now. The exponent is the setting that decides how much the sim carries for 950 bodies.

**Agreed Nov 10:** this granularity is right for players choosing base sites and for cities to grow in. Whether resource fields need finer cells near tracts and features on large bodies is still open.

### What the shape gives the fields

The bases doc lists surface fields. Several fall out of the volume:

- **Sunlight and cold traps.** March toward the Sun from every surface point over one spin, with the body shadowing itself. The mean is the cell's insolation; a point that is never lit is a cold trap. The bench does this at a chosen solar latitude.
- **Area, and flat ground.** Real area per patch. Slope against local gravity needs the body's gravity and spin from the volume; not built yet.
- **Depth of column.** How far down a mine can go before it meets the next cell's ground or the core.
- **Craters as windows.** If layers are laid down on the body before the craters are cut, a big crater's floor exposes deeper material and its rim carries ejecta as overburden. Not built yet.
- **Lobes.** The two halves of a contact binary can draw different compositions.
- **Rubble as porosity.** The rubble weight can set density per column, checked against the catalogue density.

### Drawing and picking

No unwrapping. A second small volume holds each point's patch id. The view looks up the id where the ray lands and colours it from a per-cell table; a click does the same lookup. A base sits at a point in the body's frame and belongs to the cell that contains it.

Overlays draw a polity's **picture**, never the truth: colour for the estimate, hatching where the picture is still a guess.

### The look must not leak

A body's look depends only on what is measured: type, albedo, density and shape. Hidden resources are drawn from a separate seed stream. A crusted shake-up (ore under ordinary-looking rubble) stays hidden until someone drills.

## What the engine needs

The benches are WebGL shaders that draw each body per pixel. The game will not ship that as is.

- **The generator moves to C#.** It is pure functions over numbers: a row and a variant in, a volume out. It must give the same result on every machine, so it uses integer hashes and no platform maths that differs between CPUs.
- **Small bodies become meshes.** Build a mesh from the volume (marching cubes or similar) at a few levels of detail. Keep the volume for shadows if that proves cheaper than shadow maps.
- **Shapes are cached, not saved.** A body's shape is a function of its row and variant, so a save file stores neither.
- **Camera-relative coordinates.** The bench stops at 20 m per pixel on planets, where single-precision floats run out. The engine computes positions relative to the camera, as Fleetwright's map does.
- **Poles.** Equirectangular maps pinch at the poles, and the lunar south pole matters for play (ice). Mapped bodies should move to cube-face maps.
- **The shape is presentation only for now.** If bases, landings or lines of sight ever need the surface, they read the same volume, so the picture and the sim cannot disagree.

## Data and licensing

Sources stay out of git. Scripts rebuild everything from a local `sources/` folder; the art README carries the credits.

| Data | Source | Licence | Basis |
| --- | --- | --- | --- |
| Earth colour, night lights, elevation | NASA Blue Marble and Black Marble | Public domain | measured |
| Earth coast | Natural Earth 1:10M via Fleetwright's land file | Public domain | measured |
| Earth surface classes | MODIS MCD12C1 land cover, 2019 | Public domain | measured |
| Moon and Mars colour | Solar System Scope 2k maps, from NASA LRO and Viking data | CC BY 4.0 | measured |
| Moon elevation | LROC WAC GLD100, 79°S to 79°N | Public domain | measured |
| Mars elevation | MGS MOLA MEGDR, 4 px per degree | Public domain | measured |
| Small-body shapes | NASA PDS shape models and published papers, via CelestiaContent | CC0 or CC BY 4.0, per body | measured |
| Everything else | The generator | Ours | generated |

The prototype's files came from GitHub mirrors. Before anything ships, fetch each from its original source and check its licence. Two shape models (Gaspra, Vesta) had no licence file.

## Open questions

- [ ] Chisel marks: wandering grooves, broken rims, varied crater shapes, terrain-driven albedo.
- [ ] The Two lobes law is too eager (Toutatis). Lightcurve amplitude, where known, would be a better clue than elongation alone.
- [ ] `shape_km` in `bodies.csv` mixes semi-axes (Phobos) and full diameters (Eros, Ceres). The generator is unaffected, but the column should be made consistent.
- [x] Should a body's look follow its resource field? **No.** The look follows only what is measured; see "The look must not leak".
- [x] Resource cells: is the granularity right for base sites and cities? **Yes** (agreed Nov 10), at the first-cut law.
- [ ] Resource cells: whether large mapped bodies want finer cells near tracts and features, as the resource doc proposes.
- [ ] Resource cells and mining: when a column has lost a visible share of its mass, should the volume be carved (pits, hollowing, disassembly)? The ledger is the authority either way.
- [ ] Stratigraphy before craters, so crater floors expose depth; gravity and slope from the volume.
- [ ] Patch edges are straight lines between seeds. Should cells follow terrain (crater rims, the neck of a contact binary) instead?
- [ ] Gas giants, rings and the Sun: not prototyped. Banded flow shader over a 2k map is the plan.
- [ ] Icy bodies: comets, Kuiper belt objects and small icy moons need their own surface vocabulary (smooth plains, pits, jets), and different laws for rubble and facets.
- [ ] The Moon's poles: LOLA polar elevation and cube-face maps.
- [ ] Cast shadows on mapped bodies, so crater rims and mountains throw long shadows at the terminator.
- [x] Earth: surface-class map for land detail. **Done** in the planet bench (MODIS land cover as class shares).
- [ ] Earth: clouds as a map, a shader, or none on the strategic view. Rivers and lakes. Wetland and built-up shares are stored but unused.
- [ ] Surface classes for other bodies: Mars (dust, bedrock, polar cap, dune seas) and Titan could reuse the same share-map idea.
- [ ] Volume size against mesh quality: is 160 cells enough once shapes are meshes, and what does a level-of-detail chain cost for 950 bodies?
- [ ] Hemisphere fill for half-mapped bodies (Triton, the Uranian moons).

## Sources

- Benches, scripts and credits: [`art/planet-prototypes/README.md`](../../art/planet-prototypes/README.md).
- Body catalogue: `data/solar-system/bodies.csv`.
- Style: [`art/style-anchors/README.md`](../../art/style-anchors/README.md).
- Natural Earth, https://www.naturalearthdata.com/ (public domain), via world-atlas (ISC).
- NASA Visible Earth, Blue Marble and Black Marble.
- Friedl and Sulla-Menashe 2015, MCD12C1 MODIS/Terra+Aqua Land Cover Type Yearly L3 Global 0.05Deg CMG, NASA LP DAAC, https://doi.org/10.5067/MODIS/MCD12C1.006.
- Scholten et al. 2012, GLD100: the near-global lunar 100 m raster DTM from LROC WAC stereo image data.
- Smith et al. 2003, Mars Global Surveyor Laser Altimeter Mission Experiment Gridded Data Record (MEGDR), NASA PDS.
- Ernst et al. 2023, High-resolution shape models of Phobos and Deimos from stereophotoclinometry, https://doi.org/10.1186/s40623-023-01814-7.
- Gaskell 2008, Eros and Itokawa shape models, NASA PDS.
- Barnouin, Daly et al., OSIRIS-REx Altimetry Working Group, Bennu shape model.
- CelestiaContent, https://github.com/CelestiaProject/CelestiaContent (model files and their licence notes).
