# 07 — Gamification Notes

Nothing in files 01–06 has been altered for gameplay. This file lists (1) the conflict points that **already exist in the real baseline**, (2) the optional **shake-ups** that push a campaign beyond the priors for replayability, and (3) what has been decided and what is still open.

---

## Part 1 — Tensions already built into reality

The baseline is less "flat" than it might seem. Before moving anything, these fall out naturally:

| # | Tension | Why it's real | Game hook |
|---|---|---|---|
| 1 | **Fissile duopoly: Earth vs Moon** | Earth has all ore-grade U and all processing plants; the Moon has the only off-Earth feedstock in a shallow well (KREEP, silicic domes) | Whoever controls the lunar nearside PKT and the farside Compton–Belkovich complex is the only rival to Earth for Orion-drive fuel |
| 2 | **Processing ≠ ore** | Natural U is 0.72 % ²³⁵U everywhere; fissiles must be manufactured (enrichment or breeding + reprocessing) | Enrichment/breeder/reprocessing sites are the real strategic targets; ore without plant is leverage, not power |
| 3 | **Inner metals & fissiles vs outer volatiles** | Rule 1/2 in `01-model.md` | Built-in trade axis (and blockade axis) between inner and outer powers |
| 4 | **Lunar south pole real estate** | Ice concentrated in a few named craters (Cabeus ~10 Mt scale) next to rare near-permanently lit ridges | Small number of high-value claims, adjacent to each other → classic flashpoint |
| 5 | **The belt is Ceres** | Ceres holds ~35–39 % of the belt's mass and its water, ammonia and salts | Ceres as natural capital/port; everyone else in the belt depends on it for volatiles |
| 6 | **Fertilizer geography (N, P)** | N and P are the scarce life-support elements; best sources are Venus/Titan atmospheres, Bennu-type asteroids, KREEP, Enceladus | Habitats need imports or specific claims → quiet dependency web |
| 7 | **Xenon** (if ion drives are common) | Xenon is rare everywhere; Earth's atmosphere is the only practical source | Earth export monopoly; Mars argon as the cheap substitute |
| 8 | **Drive tech re-weights the map** | Rocket equation (`01-model.md` §3); each drive concept also consumes specific resources ([`design/resource-fields-grades-and-yield-curves.md`](../../design/resource-fields-grades-and-yield-curves.md), "Drives set the demand") | A breakthrough (or proliferation) of pulse/fusion drives makes Earth exports, Mars and gas-giant ³He cheap, and turns fissile from an inventory into a flow |
| 9 | **Uncertainty is per campaign** | The game's knowledge is frozen at late 2026; uncertain numbers are priors drawn per seed (`01-model.md` §6) | No two campaigns have the same Psyche, the same buried lunar ice or the same undiscovered NEAs; prospecting and drill logs are valuable property |
| 10 | **Ephemeral resources** | Comets outgas each perihelion; long-period comets pass once; Saturn's rings are slowly raining into the planet | Time-limited windows, "claim before it's gone" scenarios |

---

## Part 2 — Variety inside the priors, shake-ups outside them

### Inside the priors (the default world)

These need no setting: the default drawn world produces them in some campaigns and not others.

- Psyche metal-dominant or mostly rubble (metal fraction 30–80 %).
- Compton–Belkovich large at depth (a 2023 Nature study reported remote detection of a granitic batholith there).
- Phobos a captured hydrated body, or dry Mars ejecta.
- Shallow brine pockets on Ceres.
- Lunar ³He hotspots in mature high-Ti maria.
- Mercury's polar ice at the top of its range (toward 10¹⁵ kg).
- An undiscovered metal NEA in an easy orbit (drawn from the population model).
- A long-period comet passing during the campaign (drawn from the arrival flux).

### Shake-ups (optional, for replayability)

**The rule: change what is hidden, never what is definitely measured.** Mass, density, orbit, size and observed surface composition stay as observed, and the mass ledger must close. A shake-up rearranges an unmeasured interior, an unprospected depth or the uncatalogued population.

**What "measured" covers.** A reflectance spectrum measures a body's surface; an orbital gamma-ray or neutron spectrometer sees about the top half-metre to a metre. Neither says what lies a few metres down. So a shake-up may put something under a thin crust of rubble or regolith lag on a body that is already catalogued and characterised, as long as its measured bulk density still allows it. Planetary scientists may wince; that's accepted.

**Shake-ups are deliberate exceptions, not the rule.** They exist to give a campaign a few meaningful, society-scale turning points (a regional powerhouse, a rush, a broken monopoly). A shake-up campaign enables a handful, never a world rebuilt from them. The default world stays drawn from the priors.

| Shake-up | Stays as measured | What changes | Effect on the map | Plausibility |
| --- | --- | --- | --- | --- |
| **Metal-cored Mimas** | Mass, density (~1.15 g/cm³), orbit, surface, the ocean under 20–30 km of ice | Core is Fe-Ni instead of silicate: ~8×10¹⁸ kg of metal, core radius ~63 km *(calc; worked example in the design doc)* | Saturn gets the metal the outer system lacks; a slow-building regional powerhouse once deep extraction is possible | Low–medium: interior composition unmeasured; a metal core in a small icy moon is unusual |
| **Metal-rich Trojan** | Size and albedo of any characterised Trojan | A mid-sized, spectrally uncharacterised Trojan is a captured M-type | A Jovian metal hub at L4 or L5, outside the radiation belts | Low–medium |
| **Ice-filled Phobos** | Mass, density (~1.9 g/cm³), surface spectra, the drawn origin | Interior porosity is ice rather than voids | A water depot in Mars orbit at almost zero Δv | Medium |
| **Extinct comet in an easy orbit** | Every catalogued NEA | An undiscovered NEA is a dormant comet nucleus with an icy interior under a dry crust | A cislunar water bonanza and a claim race | Medium (some NEAs are extinct comets) |
| **Super-rich lunar crater** | Orbital neutron averages over the top half-metre | One cold trap holds a buried, nearly pure ice layer metres thick, Mercury-style | A single dominant south-polar claim | Medium |
| **Martian uranium province** | Orbital Th and K maps (crustal averages) | A tract holds real uranium ore bodies at depth | Breaks the Earth–Moon fissile duopoly; Mars becomes a nuclear power in its own right | Low–medium |
| **Granitic Venus highlands** | Lowland Venera and Vega values; radar topography | Ishtar Terra or the tesserae are evolved, Th/U-rich crust | A long-term fissile reserve for whoever can work Venus's surface | Low–medium |
| **Thin-shell window on Europa** | Gravity, surface composition | The ice shell is locally only a few km over the ocean | Ocean access in the Jovian system, at the cost of the radiation | Medium (depending on what a 2030s start treats as measured) |
| **Fissile-rich asteroid** | The chosen body's measured mass, bulk density, orbit and surface spectra | One body holds U and/or Th at ore grade, either uncatalogued or **hidden under a thin rubble crust on a known body**. The origin is handwaved (a crustal fragment of a destroyed protoplanet is the usual story) | **Belt independence before fusion;** whoever controls it becomes a regional powerhouse (below) | Very low by the baseline's rules, accepted as an optional random factor (Nov 5) |

Scenarios can still pin any value by hand (the *authored* setting).

### The fissile-rich asteroid in detail

Decided Nov 5: an optional random factor, off in the default world, on in a shake-up campaign. It contradicts Rules 2–3 of `01-model.md` (no asteroid class is a meaningful U/Th source), which is why it lives here and not in the priors.

- **What it is.** One body, drawn per campaign when the shake-up is on, with a location (an NEA, a main-belt body, a Trojan), a size, a U:Th ratio, a grade from the low end of terrestrial ore upward, and a **cover depth**: none, or a rubble crust metres to tens of metres thick. The location decides whose region it empowers: an NEA arms cislunar space, a Ceres-adjacent body arms the belt, a Trojan arms Jupiter.
- **The body may already be on the map.** With a crust, it can be a catalogued, even well-known asteroid whose spectra say "ordinary". The check is bulk density: the drawn ore body must fit inside what the measured density allows.
- **It has to be found, and the crust decides how.** Uncovered, an orbital gamma-ray spectrometer sees the Th and U, so a survey reveals it. Covered, orbital surveys see only the rubble; finding it takes a drill core, an impactor that digs a crater, seismic sounding, or simply mining into it. A crusted body can sit unnoticed for decades on a route everyone flies past, and the company that bores into it for water strikes it by surprise. Who finds it first, and whether they publish, is a picture question ([`design/resource-fields-grades-and-yield-curves.md`](../../design/resource-fields-grades-and-yield-curves.md), prospecting).
- **It ends the belt's inward dependence on fuel.** The belt's missing element before fusion is fissile ([`design/outward-the-belt-jupiter-and-independence-from-earth.md`](../../design/outward-the-belt-jupiter-and-independence-from-earth.md)). With local feedstock, a belt network can reach rungs 3 and 5 of the independence ladder without the Moon or Earth.
- **Ore is still not power (tension 2).** Natural uranium is 0.72 % ²³⁵U here as everywhere, and thorium has to be bred. The controller needs enrichment or breeding and reprocessing plant, and a thorium-rich body needs a seed of fissile from outside to start breeding. **That plant is the proliferation flashpoint of the design notes, moved to the belt:** inspections, sanctions, covert facilities, and a host that will very much want to know.
- **It's a magnet for conflict.** One body, one claim, everyone's interest. Expect claim jumping, a host's demand for a garrison, a rival bloc's offer of recognition, and the first place someone thinks a warship is worth sending past Mars.

---

## Part 3 — Decided and open

**Decided (Teemu, Nov 2, 2026):**

- **Knowledge is frozen at current data.** The game will ship before 2029, so it lives with today's knowledge; real missions are not reveal events.
- **Start state roughly 2030–2040:** almost modern day. Holdings and tech of that period form the start state (no fixed date in code, per the initial notes).
- **Drive classes are the drive survey's concepts** ([`studies/drive-survey-concepts-ranges-and-minimum-sizes.md`](../drive-survey-concepts-ranges-and-minimum-sizes.md)); the battler proposal is cards 1, 3, 4, 8, 11, 14, 15, 16, 17.
- **Granularity follows the bases design:** places, not slots; fields on the body's surface grid; mining on yield curves, not fixed yields.
- **The default world is drawn from the priors.** Optional shake-ups add replayability, under the rule above.
- **Fissile representation is left open,** to keep things simple until the fuel-cycle design.
- **Elements may be clumped; mass is conserved exactly** ([`design/mass-ledger-element-groups-and-conservation.md`](../../design/mass-ledger-element-groups-and-conservation.md)).

**Decided (Nov 5, 2026):**

- **A fissile-rich asteroid is an optional random shake-up,** with a handwaved origin. It replaces the earlier "crustal-fragment asteroid" and "asteroid uranium ore" rows.
- **Shake-ups may hide things under a thin crust on known bodies.** "Measured" means definitely measured today: surface spectra and the top metre seen by orbital spectrometers stay true; what lies beneath is fair game if bulk density allows it.
- **Shake-ups are intentional exceptions** for society-scale turning points: a handful per campaign, never the rule.

**Still open:**

1. **Factions and powers:** map them onto the Part 1 tensions (Earth blocs, Moon, Mars, Ceres, Saturn system)? A first roster is in [`design/from-contracts-to-markets-starting-actors-and-the-transition.md`](../../design/from-contracts-to-markets-starting-actors-and-the-transition.md).
2. **Which draws are public at start,** and whether a polity's pre-start missions give it private knowledge.
3. **Shake-up presets:** which shake-ups a "shake-ups" campaign enables, how many at once, and whether each is revealed at setup or must be found.
4. **The fissile-rich asteroid:** its draw probability, size and grade ranges, and whether it can ever appear outside a shake-up campaign.
5. The open questions in [`design/resource-fields-grades-and-yield-curves.md`](../../design/resource-fields-grades-and-yield-curves.md) and [`design/mass-ledger-element-groups-and-conservation.md`](../../design/mass-ledger-element-groups-and-conservation.md).
