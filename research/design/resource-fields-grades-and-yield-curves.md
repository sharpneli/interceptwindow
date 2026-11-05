# Intercept Window: Resource Fields, Grades and Yield Curves

Nov 2, 2026 · @Teemu · proposal (shake-up rule updated Nov 5)

How the solar-system resource baseline ([`studies/solar-resources/`](../studies/solar-resources/)) becomes game data. A body's resources are **fields of grade and tonnage**, mining is a **process block whose output depends on grade**, and everything a polity knows about a field is **a picture with uncertainty**. The yield curve (cost per tonne of product against how much has already been taken) falls out of those three things; nobody writes it by hand.

## The short version

- **A deposit is a distribution, not a number.** Each resource in each place is a grade–tonnage distribution by depth: how many tonnes of rock sit at each concentration. Lognormal is the default shape, as in terrestrial resource assessment.
- **The yield curve is derived.** Mine the best ground first and the marginal grade falls, so cost per tonne of product rises with cumulative extraction. Cutoff grade is where marginal cost meets price, so it moves with energy price, tech and demand. There is no fixed yield and no "site exhausted" switch.
- **Grade is the specific throughput of the mine.** A mine block processes rock at s_rock tonnes per tonne of plant per year; product per tonne of plant is s_rock × grade × recovery. That number goes straight into the manufacturing growth law, so rich ground grows industry faster.
- **Energy per kg of product is a fixed term plus a term in 1/grade.** For lunar polar ice, about 0.8 kWh/kg is sublimation whatever the grade; heating the regolith around it adds 0.3 kWh/kg at 5.6 wt % and 15 kWh/kg at 0.1 wt % *(calc)*.
- **Two modes per element.** A concentrated mode (ore, ice, brine, metal grains) that ordinary process blocks can reach, and a dispersed mode (atoms in silicate lattices) that only universal separation reaches. Off Earth most elements have little or no concentrated mode, which is why the far end of the manufacturing ladder flattens the map.
- **Content is three layers per body:** a coarse background field, **tracts** (areas where a deposit type can occur, with a deposit-count prior) and **features** (named known deposits: Cabeus, Compton–Belkovich, 1986 DA).
- **Knowledge is frozen at late 2026, and the truth is a campaign variable.** The game ships before Psyche, MMX's samples or any new lunar ground truth, so it lives with today's knowledge. The baseline's confidence codes become prior widths; each campaign seed draws its own truth from them; prospecting narrows each polity's picture.
- **Default world: drawn from the priors; optional shake-ups on top.** A shake-up may change what is hidden (a moon's core, an unprospected depth, ore under a thin rubble crust on a known body) but never what is definitely measured, so a metal-cored Mimas keeps Mimas's mass, density and orbit. Shake-ups are deliberate exceptions, a handful per campaign, for society-scale turning points.
- **Mass is conserved exactly.** Every extraction is a balance in [`design/mass-ledger-element-groups-and-conservation.md`](mass-ledger-element-groups-and-conservation.md): rock out, product, tailings and vented gas in, to the gram.
- **The start state (roughly 2030–2040 holdings and tech) says which draws are already public.** A 2035 start would have Psyche's metal fraction and Phobos samples in hand, so those are drawn at setup and shown to everyone; buried lunar ice per crater is still unknown and must be prospected.
- **Drives set demand.** Each drive concept in [`studies/drive-survey-concepts-ranges-and-minimum-sizes.md`](../studies/drive-survey-concepts-ranges-and-minimum-sizes.md) consumes specific resources (hydrogen, xenon, fissile, deuterium, ³He, lithium). The resource map and the drive catalogue are one economy.

## The model

### 1. Fields: what a place holds

A body carries one field per resource kind. A resource kind is a product (water, oxygen, Fe-Ni, thorium, ³He…) bound in a **form** that sets which process blocks can take it:

| Form | Examples | Reached by |
| --- | --- | --- |
| Ice in regolith | Lunar and Mercury polar cold traps, Martian ground ice | Excavate + heat, or in-situ heating |
| Massive ice | Martian polar layered deposits, icy moons, Saturn's rings, comets | Cut, melt, or bag and heat |
| Regolith-bound | Lunar O₂, Fe, Ti (ilmenite), ³He, KREEP minerals | Excavate + beneficiate + chemistry |
| Hard rock | Silicic domes, crustal ores, Vesta basalt | Drill, blast, crush |
| Native metal | M-type asteroids, metal grains in S-types and regolith | Cut or magnetic separation + carbonyl refining |
| Hydrated mineral | C-type clays, Ceres crust | Heat to dehydrate |
| Brine / salt | Ceres faculae, Bennu-like evaporites, Enceladus plume | Collect, evaporate |
| Atmosphere | Mars CO₂/N₂/Ar, Venus N₂, Titan N₂/CH₄, giant planets H₂/He/³He | Intake + separation; no depletion at game scale |
| Liquid | Titan seas | Pump |

Each field is stored per **cell** of the surface grid from [`design/bases-settlements-and-the-civilian-economy.md`](bases-settlements-and-the-civilian-economy.md) and per **depth band**. A cell's entry for one resource is a handful of numbers:

| Number | Meaning |
| --- | --- |
| `T` | Tonnes of host material in this cell and depth band |
| `μ, σ` | Lognormal grade parameters: median grade e^μ, spread σ (natural log) |
| `overburden` | Barren cover above the band (dry lag, ejecta, dust), in metres |
| `form` | As above; sets which process blocks apply |
| `mineralogy` | Grain size and host mineral, as a beneficiation factor: how much a physical separation step can concentrate it before chemistry |
| `confidence` | Prior width in each polity's picture (section 7) |
| `composition` | The host material's composition vector over the mass ledger's element groups; it holds the dispersed mode and makes every extraction an exact mass balance |

Small bodies are one site, as the bases doc already says: a 500 t boulder or a 3 km metal asteroid is one cell whose T is its whole mass. Atmospheres are one reservoir per body with a fixed grade.

### 2. Grade and tonnage: the lognormal

Grades in natural deposits are skewed: most rock is poor and a little is rich. A lognormal captures that with two numbers and gives closed forms for everything a mine needs. For a cutoff grade g_c:

```latex
T(g_c) = T_0\left[1-\Phi\!\left(\frac{\ln g_c-\mu}{\sigma}\right)\right] \qquad M(g_c) = M_0\left[1-\Phi\!\left(\frac{\ln g_c-\mu-\sigma^2}{\sigma}\right)\right] \qquad M_0 = T_0\,e^{\mu+\sigma^2/2}
```

T is the rock above cutoff, M the product it contains, and M/T its average grade. Terrestrial geology has two versions of this idea: Lasky's cumulative tonnage–grade law (tonnage rising geometrically as grade falls arithmetically), and the lognormal deposit models behind USGS resource assessments. The lognormal is the safer form, because Lasky's law predicts physically impossible tonnages below some limiting grade.

**Worked example** *(calc, illustrative parameters)*: a lunar cold-trap cell with median 1 wt % ice and σ = 1.2, so a mean of about 2 wt %:

| Cutoff grade | Share of the rock above it | Share of the water above it | Average grade above it |
| --- | --- | --- | --- |
| 0.3 % | 84 % | 99 % | 2.4 % |
| 1 % | 50 % | 89 % | 3.6 % |
| 2 % | 28 % | 73 % | 5.3 % |
| 5 % | 9 % | 44 % | 10 % |
| 10 % | 2.8 % | 24 % | 18 % |

**Reading:** almost half the water sits in a tenth of the ground. Finding that tenth is prospecting's whole value, and a mine that can't tell rich ground from poor (no selective mining) pays the average grade instead.

### 3. The mine as a process block

A mine is a process block like the ones in [`design/manufacturing-and-the-dependency-ladder.md`](manufacturing-and-the-dependency-ladder.md), with grade as its input:

| Field | Meaning | Lunar ice example |
| --- | --- | --- |
| `s_rock` | Tonnes of host material handled per tonne of plant per year | Engineered number (excavator and heater throughput) |
| `recovery r(g)` | Share of the product actually extracted, rising with grade: r = r_max · g / (g + g_half) | r_max and g_half are engineered numbers; no hard cutoff |
| `e_dig` | kWh per tonne of host material excavated, hauled and prepared | Placeholder; terrestrial crushing and grinding alone is ~9–13 kWh/t (Bond work index), ~20 kWh/t for a full plant |
| `e_strip` | kWh per tonne of overburden moved | Dry lag above buried ice |
| `e_extract` | kWh per tonne of host material for the extraction step | Heating regolith from ~40 K to ~200 K: ~55 kJ/kg *(placeholder)* |
| `e_product` | kWh per kg of product, independent of grade | Sublimating ice: ~0.83 kWh/kg *(from the Lunar Ice Miner energy basis)* |
| Environment, labour, plant bill | As for any process block | Permanent darkness, 40 K, abrasive dust |

**Product per tonne of plant per year** is s_rock · g · r(g). That is the s in the growth law r = s · f · a / k, so the grade of the ground a company sits on sets how fast its plant can copy itself. Two companies with the same blocks on different craters grow at different rates, and the better crater is worth fighting over.

**Energy per kg of product:**

```latex
e(g) = e_{\text{product}} + \frac{(1+R)\,e_{\text{dig}} + e_{\text{extract}}}{g\cdot r(g)} \qquad R = \frac{\text{overburden}}{\text{deposit thickness}}
```

For lunar icy regolith, heat only, perfect recovery *(calc)*:

| Ice grade | Regolith heated per kg of water | Heat per kg of water |
| --- | --- | --- |
| 90 % | 0.1 kg | 0.83 kWh |
| 30 % | 2.3 kg | 0.87 kWh |
| 10 % | 9 kg | 0.97 kWh |
| 5.6 % (LCROSS) | 17 kg | 1.09 kWh |
| 2 % | 49 kg | 1.58 kWh |
| 1 % | 99 kg | 2.34 kWh |
| 0.5 % | 199 kg | 3.87 kWh |
| 0.1 % | 999 kg | 16.1 kWh |

Heat is the cheap part where sunlight can be piped in. The expensive part is the plant that handles 17–999 kg of 40 K regolith per kg of water, which is why s_rock · g, not the energy, decides the economics at low grade.

### 4. The yield curve and depletion

Sort a site's cells and depth bands by delivered cost and take the cheapest first. Cumulative output against marginal cost is the **yield curve**. For the worked example above, mined best-first *(calc, heat only)*:

| Share of the cell's water taken | Marginal grade | Marginal heat per kg |
| --- | --- | --- |
| First 10 % | ~20 % | ~0.9 kWh |
| 44 % | 5 % | ~1.1 kWh |
| 73 % | 2 % | ~1.6 kWh |
| 89 % | 1 % | ~2.3 kWh |
| 99 % | 0.3 % | ~5.9 kWh |

- **Depletion is stock arithmetic.** Each band keeps its remaining T, μ, σ after mining takes the upper tail. Nothing flips to "exhausted"; the curve just climbs.
- **Cutoff is an outcome:** the grade at which marginal cost equals the delivered price at the mine's market. A propellant price spike at a depot lowers every mine's cutoff and widens every reserve.
- **Tech moves the curve,** never the deposit: higher s_rock, lower e_dig, lower g_half (better recovery from poor ground), cheaper energy.
- **Firms read the same curve.** A firm's investment score in the bases doc is expected return after tax, transport and risk; the yield curve is its revenue side.
- **Higher-grade ground gets mined first in reality too.** DeYoung and Singer's review of mineral supply makes exactly this point: cheap metal comes first, the biggest deposits supply most of it, and the long-run effect of depletion is rising real cost rather than running out.

### 5. Two modes: ore and atoms

Skinner's thesis holds that for geochemically scarce elements the crust's distribution is bimodal: a small amount in ore minerals, and most of it scattered through ordinary silicate lattices, with an energy gap (the "mineralogical barrier") between the modes. Whether the barrier is real for every element is debated; as a model shape it is exactly what the game needs.

- **Concentrated mode:** what the field's lognormal describes. Ordinary process blocks (excavation, beneficiation, chemistry) reach it.
- **Dispersed mode:** the body's bulk abundance of the element, everywhere, at chondritic or crustal level. Recovery by ordinary blocks is near zero.
- **The universal separation block** from the manufacturing doc reaches the dispersed mode at an energy set per kg of rock, so its cost per kg of product is that energy divided by abundance. Above roughly a part per million, any rock becomes ore for what it contains.
- **Off Earth the concentrated mode is thin or missing** for most elements (Rule 3 of [`studies/solar-resources/01-model.md`](../studies/solar-resources/01-model.md): ore needs water, heat and time). The Moon has KREEP minerals but no uranium ore; asteroids have native metal but no thorium deposits. That makes universal separation a bigger deal in space than on Earth, and it is how "whole-body disassembly" arrives without a new system.
- **Beneficiation sits between the modes.** In KREEP, thorium, uranium and the rare earths sit in accessory minerals (apatite, merrillite, zircon, monazite). A physical separation step can concentrate those grains before any chemistry, so the cell's `mineralogy` number matters as much as its grade.

### 6. Tracts and features: where content goes

Fields are generated from three layers, following the structure of USGS three-part assessments (permissive tracts, grade–tonnage models, and an estimated number of undiscovered deposits per tract, combined by Monte Carlo):

| Layer | What it is | Examples | Data source |
| --- | --- | --- | --- |
| **Background** | Smooth, coarse field of bulk composition and regolith depth | Lunar highland anorthosite; mare TiO₂; Martian Th 0.2–1 ppm; chondritic asteroid bulk | Orbital maps (gamma, neutron, multispectral) |
| **Tract** | An area where a deposit type can occur, with a grade–tonnage model and a prior on how many deposits it holds | Lunar south-polar PSRs (ice); the Procellarum KREEP Terrane (Th, REE); Martian impact-hydrothermal craters (sulphide or uranium ore, conf. D); Tharsis margins (Ni-Cu-PGM, conf. D) | Geology + the baseline's confidence codes |
| **Feature** | A named, located deposit with its own grade–tonnage and depth | Cabeus, Shoemaker, Compton–Belkovich, Gruithuisen Domes, 1986 DA, Psyche, Kraken Mare, Sputnik Planitia | The baseline docs |

- **Undiscovered deposits are drawn,** not authored. A tract's deposit count is sampled per campaign from its prior; each drawn deposit takes a size and grade from the tract's grade–tonnage model and a hidden location inside the tract.
- **Asteroids work the same way.** The known NEA catalogue is the features; the undiscovered population is drawn from the NEOWISE size–frequency model (about 13,200 NEAs over 140 m, of which about 38 % were catalogued in 2023) with class shares from the spectral surveys. A 1986 DA-class metal body in an easy orbit is therefore something a campaign may or may not contain, and someone has to find it.
- **Comets arrive as a flux.** Long-period comets are drawn from the real arrival statistics: a time-limited volatile and deuterium source that nobody can plan for years ahead.
- **Grid resolution follows the features,** not the body. Polar cold traps are 1–50 km across and need fine cells; a lunar highland plain doesn't. This is a partial answer to the bases doc's open question on resolution per body: an adaptive grid, fine where tracts and features are, coarse elsewhere.

### 7. Knowledge: frozen in 2026, true per campaign

The game will ship before Psyche reaches its asteroid (Aug 2029), before MMX's Phobos samples land (2031) and before any new ground truth from the lunar poles. So the game lives with late-2026 knowledge, and the baseline docs are that knowledge.

**The truth is a campaign variable.** Every uncertain number in the baseline becomes a prior; each campaign seed draws its own truth; each polity holds a picture of it.

| Baseline confidence | Prior on a field number | Meaning in play |
| --- | --- | --- |
| **A** (sampled or measured in situ) | ±10–20 % (σ_ln ≈ 0.1–0.2) | Effectively known |
| **B** (good remote sensing) | factor ~2 (σ_ln ≈ 0.5–0.7) | Worth checking before a big investment |
| **C** (inferred, modelled) | factor 3–10 (σ_ln ≈ 1–2) | Prospect before building |
| **D** (speculative) | Presence itself uncertain: probability p, then a C-width size | Tracts with a deposit-count prior |

- **Draws are hierarchical.** Body totals come first and are consistent with what is measured in aggregate (an orbital neutron map constrains the top metre across a whole polar region); cells share out the total; depth bands below what sensors see get wider priors. Confidence falls with depth, which is real: neutron spectrometers see half a metre.
- **Knowledge at start is set by the start state.** Anything the start state's history would already have measured is drawn at setup and shown to every polity. Anything still unmeasured stays hidden.
- **Prospecting is the picture.** Each instrument is a source with a footprint, a depth and an error, fused by the same code as [`design/detection-and-the-picture.md`](detection-and-the-picture.md):

| Source | Footprint | Depth seen | What it narrows |
| --- | --- | --- | --- |
| Orbital gamma/neutron spectrometer | Tens of km | ~0.5–1 m | Th, K, U, Fe, H (ice) averages per cell |
| Orbital radar | km | Metres to km | Thick ice, buried layers (Mars MFF, Mercury) |
| Multispectral imaging | Metres | Surface | Ti (ilmenite), maturity, so ³He |
| Rover or lander with spectrometers | Metres | Surface to ~1 m | One cell's top band |
| Drill core | A point | Its depth | One column's grade profile |
| Mining itself | Where it digs | Where it digs | The actual grade, as a by-product |

- **Information has a price and a value.** A drilling campaign costs a lander and months; skipping it means building a mine on the prior. Firms in the bases doc invest on their own picture, so a firm with better prospecting picks better ground.
- **Prospecting data is property.** A company's drill logs are an asset it can sell, hide or have stolen; a published survey moves every rival's picture at once. Claim jumping is buying a rival's picture.

**The big uncertain numbers and a first proposal for their priors** (placeholders, to be tuned):

| Quantity | Prior proposal | Known at a 2030–2040 start? |
| --- | --- | --- |
| Lunar polar ice, total | Log-uniform 0.1–6 Gt, median ~1 Gt; per-crater share weighted by cold-trap area and age (older traps hold more, buried deeper) | Totals partly; per-crater grade and depth mostly not |
| Lunar polar ice depth | Dry lag 0.1–1 m; ice-bearing layers to ≥10 m in the oldest traps | No |
| Lunar ³He grade | Field from TiO₂ and maturity maps; 1–20 ppb; narrow (A/B) | Mostly yes |
| Compton–Belkovich extent at depth | Felsic, Th-rich body below the surface feature: present with high probability (B/C), volume wide (C) | Partly |
| Mercury polar ice | Log-uniform 10¹⁴–1.4×10¹⁵ kg | Partly (BepiColombo-era orbital data; depth still open) |
| Mars Medusae Fossae ice fraction | C | No |
| Mars ore tracts (sulphide, Ni-Cu-PGM, uranium) | D: deposit counts per tract with p ≪ 1 each | No |
| 16 Psyche metal fraction | Uniform 30–80 % by mass | **Yes** (orbiter from 2029): drawn at setup, public |
| Phobos and Deimos origin | 50 % captured primitive body (hydrated, organics), 50 % Mars ejecta (dry) | **Yes** (MMX samples 2031): drawn at setup, public |
| Undiscovered NEAs | Drawn from the NEOWISE size distribution and spectral class shares | The large ones mostly; many 100–300 m bodies not |
| Ceres near-surface brines | C | No |
| Jupiter Trojan interiors | C | Surfaces partly (Lucy flybys) |

**Settings:** *drawn world* (**the default, decided Nov 2**: truth drawn from the priors), *baseline world* (truth = the baseline medians, for testing), and *authored* (a scenario sets values by hand). On top of any of them, optional **shake-ups** (section 9) push a campaign outside the priors for replayability.

### 8. The start state: roughly 2030–2040

The start is a state, not a date, per the initial notes; these are the assumptions for a start that looks like the 2030s.

- **Holdings:** small crewed and robotic presence at the lunar south pole; first propellant-from-ice pilot plants and depots; asteroid prospectors of the Keck-retriever or smaller class; nothing industrial beyond the Moon. All enrichment, reprocessing and fuel fabrication are on Earth.
- **Knowledge:** the baseline docs, plus whatever the start state says was measured since 2026, drawn from the priors and made public (table above).
- **Earth's fissile position:** the Red Book picture (~7.9 Mt U identified recoverable, concentrated in a few countries and one giant deposit) as the starting supply side, abstracted per the drive and weapon docs.
- **Drives available:** the battler set from the drive survey (cards 1, 3, 4, 8, 11, 14, 15, 16, 17) as principles; which polities hold engineered blocks for which concept is part of the start state.

### 9. Shake-ups: optional tweaks outside the priors

Priors give variety inside what science allows. Shake-ups are optional campaign settings that go further, to give a campaign a different shape: a region that becomes a power, a rush, a scarcity. They follow one rule.

**A shake-up may change what is hidden, never what is definitely measured.** A body's mass, density, orbit, size and observed surface composition stay exactly as observed, and the mass ledger ([`design/mass-ledger-element-groups-and-conservation.md`](mass-ledger-element-groups-and-conservation.md)) must still close. A shake-up rearranges the unmeasured interior, the unprospected depth, the uncatalogued population.

**What "measured" covers** (decided Nov 5). A reflectance spectrum measures a body's surface, and an orbital gamma-ray or neutron spectrometer sees about the top half-metre to a metre (the depths in section 7's prospecting table). Neither says what lies a few metres down. So a shake-up may put something under a thin crust of rubble or regolith lag on a body that is already catalogued and characterised, as long as its measured bulk density still allows it. Planetary scientists may wince; that's accepted.

**Shake-ups are deliberate exceptions, not the rule.** They exist to give a campaign a few meaningful, society-scale turning points. A shake-up campaign enables a handful, never a world rebuilt from them, and the default world stays drawn from the priors.

**Worked example: a metal-cored Mimas** *(calc)*. Mimas has a mass of 3.75×10¹⁹ kg and a mean density of about 1.15 g/cm³, and its orbit and libration point to an ocean beneath 20–30 km of ice (Lainey et al., 2024). What its core is made of is not measured. Holding mass and density fixed:

| Core | Core share of Mimas's mass | Core mass | Core radius (of 198 km) |
| --- | --- | --- | --- |
| Silicate rock (the prior) | ~28 % | 1.0×10¹⁹ kg | ~94 km |
| Iron-nickel metal (the shake-up) | ~22 % | 8.1×10¹⁸ kg | ~63 km |

- **Same moon from outside.** Gravity, orbit and surface are unchanged; only the core's composition vector differs, and the ice and ocean take up the volume the denser core gives back.
- **8×10¹⁸ kg of Fe-Ni** is comparable to the metal in 16 Psyche, sitting in the Saturn system beside the solar system's cleanest water (the rings), its hydrocarbons and nitrogen (Titan) and its phosphate (Enceladus). Saturn stops being a volatiles-only region and gets the one thing the outer system lacked.
- **It pays off only in the long term.** The metal lies under ~135 km of ice and ocean. Early industry can't reach it; deep drilling, then a hollowed or disassembled Mimas (escape velocity ~0.16 km/s), can. That fits a campaign arc: a slow-building outer power.
- **Somebody has to find it.** A gravity-field survey or seismic sounding of Mimas is the prospecting that reveals it.

**Second example: a fissile-rich asteroid under a crust.** One body holds uranium and/or thorium at ore grade, with a handwaved origin, either uncatalogued or hidden on a known body under a rubble crust metres to tens of metres thick. Its spectra still say "ordinary", its measured density still fits, and only a drill core, an impactor crater, seismic sounding or mining into it reveals the ore. It gives one region fuel feedstock before fusion, which makes its controller a regional powerhouse ([`design/outward-the-belt-jupiter-and-independence-from-earth.md`](outward-the-belt-jupiter-and-independence-from-earth.md)). The draw details are in [`studies/solar-resources/07-gamification-notes.md`](../studies/solar-resources/07-gamification-notes.md).

Other shake-ups are listed in [`studies/solar-resources/07-gamification-notes.md`](../studies/solar-resources/07-gamification-notes.md), each with what stays measured and what changes.

## Drives set the demand

Every drive concept consumes something. The table maps the drive survey's concepts to the resources they pull on, which is what turns the resource map into an economy.

| Drive concept (survey card) | Propellant or working mass | Consumable fuel | What it does to the map |
| --- | --- | --- | --- |
| Chemical (1) | H₂/O₂, CH₄/O₂, storables; Al or Si with O₂ | — | Water ice and carbon become propellant; oxygen from any rock covers 78–86 % of the mass; hydrogen is the scarce half on the Moon |
| Electrothermal (2) | Water, ammonia, H₂, almost any volatile | — | Unpurified water anywhere becomes propellant |
| Electrostatic: ion, Hall (3) | Xenon, krypton, argon; iodine, magnesium | — | **Xenon is an Earth-atmosphere monopoly;** argon from Mars or Earth is the cheap substitute |
| Electromagnetic plasma (4) | Argon, hydrogen, lithium | — | Argon and hydrogen; lithium for some designs |
| Mass driver (5) | Any rock, slag or ice | — | Propellant is free at any body; every pellet is a projectile |
| Solar and beamed thermal (6) | Water, H₂ | — | Water again; sunlight falls as 1/r² |
| Sails (7) | None | — | Sail material only |
| Solid-core NTR (8) | H₂ best; water, ammonia, methane, CO₂ with suitable cladding | Fissile core inventory (HEU or LEU) | Hydrogen-rich ice is the premium propellant; fissile is an inventory, not a flow |
| Liquid, vapour, droplet core (9) | H₂ | Fissile lost in the exhaust | Fissile becomes a flow |
| Gas core, closed (10) | H₂ | Fissile inventory | As NTR, larger inventory |
| Gas core, open (11) | H₂ | Fissile lost at 1–7 % of propellant flow | **A heavy fissile flow** and a radioactive exhaust |
| Nuclear salt-water (12) | Water | Fissile salt | **The largest fissile flow of any drive** |
| Fission fragment (13) | Fission products (+ H₂ afterburner) | Fissile | Fissile flow at very high ve |
| External pulse, Orion (14) | Pulse units (+ plate ablation) | Fissile per pulse unit (warhead line) | **Fissile per unit, and units by the thousand;** the proliferation flashpoint |
| Micro-pulse (15) | Targets in a magnetic nozzle | Fissile or fission–fusion targets; antimatter option | Less fissile per pulse than Orion; antiprotons as an alternative |
| Magnetic-confinement fusion (16) | Plasma (+ H₂ or water afterburner) | D-T (deuterium from water, tritium bred from lithium), D-³He, catalysed D-D (water only), p-¹¹B | Fuel choice picks the resource: lithium (Earth crust and brines), ³He (Moon, ice giants) or just water |
| Pulsed fusion (17) | Plasma, liners | As above; lithium liners in some designs | As above |
| Antimatter (18) | H₂ or water | Antiprotons | Production, not mining; natural traps hold nanograms |

**Consequences:**

- **Water is the one universal input.** Chemical, electrothermal, solar-thermal, NTR, NSWR and every fusion fuel cycle except p-¹¹B want hydrogen or deuterium, so water prices at the depots are the backbone of the price field, as the logistics research already says.
- **Fissile demand runs from inventory to flow.** Solid-core NTR and fission electric hold fissile as a core inventory. Open gas cores, NSWR, fission fragment and pulse drives burn it as a flow. The more a polity flies the second group, the more the Earth–Moon fissile geography of the baseline matters, and the more visible its fuel cycle becomes.
- **Fusion fuel is a choice of dependency.** D-T ties a fleet to lithium and breeding blankets; D-³He to the Moon now and the ice giants later; catalysed D-D to nothing but water, at the cost of more neutrons and harder ignition.
- **Xenon decides who can run big electric fleets** without Earth, until argon and krypton thrusters close the gap.

## In the sim

- **Every extraction is a mass balance** in the mass ledger: rock out of the field, product to a stock, tailings to a pile in the cell, vented volatiles to their sink. Nothing is created or destroyed.

- **Fields are data per body:** background grid, tracts and features, each tagged with source and confidence, retunable without touching the sim. The truth draw is seeded per body.
- **Mines run on the Routine tier.** Between events a mine's output is linear in time; each delivery or monthly cadence takes rock from the current band and updates T, μ, σ. A drop in grade is a re-anchoring event, not a tick.
- **Pictures of fields** use the picture's fusion code: one fusion, more sources. A drill core is a report with a time, a source and an error.
- **Firms and governors** score sites from their own picture of the field, their own cost blocks and the local price; rules with hysteresis, no search.
- **Consistency check:** a mine's growth must match the growth law with s = s_rock · g · r(g) on a bench, and depletion must never raise a band's grade (monotone, like the ship generator's mono-check).

## What the scenario battler needs

Almost nothing:

- **Hand-placed sites with fixed stocks:** a propellant depot to defend, an ice mine to raid, a metal asteroid to seize. Stocks drain and refill as Routine ledgers.
- **A mine as an installation** on the ground-installation pipeline, so it can be hit.
- **Not needed yet:** fields, tracts, priors, prospecting, yield curves.

## Suggested build order

1. Feature list per body from the baseline docs, with grade–tonnage and depth per feature (baseline world).
2. The mine process block: s_rock, r(g), e_dig, e_extract, e_product; output and energy per kg; a bench against the growth law.
3. Depletion per depth band and the derived yield curve; cutoff as an outcome.
4. Background fields and tracts; the seeded truth draw and the start-state "already known" rule.
5. Prospecting sources in the picture; drill logs as property.
6. Universal separation as the far-end block reaching the dispersed mode.

## Open questions

- [ ] Grade–tonnage parameters per feature and tract: a fitting pass over the baseline docs, with σ chosen per form (ice, regolith, hard rock, metal).
- [ ] Engineered-number ranges for mine blocks: s_rock, e_dig, r_max, g_half, from lunar excavation tests (RASSOR, IPEx) and terrestrial mining; start values and ceilings by the realism gradient.
- [ ] Ice-cemented regolith strength at 40 K and what it does to e_dig.
- [ ] Beneficiation factors for KREEP minerals: how far physical separation concentrates Th, U and REE before chemistry.
- [ ] Prior widths: are the A–D bands above right, and should priors be skewed (log-normal) or bounded (log-uniform)?
- [ ] Which draws are public at start for each start state; whether a polity's own pre-start missions give it private knowledge.
- [ ] Is selective mining (taking only the rich tail) an engineered number of the mine block, or a property of the picture's resolution?
- [ ] Atmospheres: a fixed grade, or a slowly depleting reservoir at Mars once terraforming starts to compete for the same gas?
- [ ] Undiscovered-NEA generation: how many to draw, down to what size, and how NEO Surveyor-era catalogues are represented in a 2030s start.
- [ ] Fissile representation: left open (decided Nov 2); the mass ledger's actinide group holds U and Th as one mass until then.
- [ ] Shake-up catalogue: which are on by default in a "shake-ups" campaign preset, and whether they are revealed at start or must be prospected.
- [ ] Crusted shake-ups: the range of cover depths, and how the bulk-density check is done (a fixed tolerance, or the body's measured density uncertainty).
- [ ] Mars ore tracts: which terrestrial deposit types are plausible analogues (impact-hydrothermal, magmatic Ni-Cu-PGM, sedimentary uranium), and their deposit-count priors.

## Sources

- Internal: [`studies/solar-resources/`](../studies/solar-resources/) (README and 01–07), [`design/bases-settlements-and-the-civilian-economy.md`](bases-settlements-and-the-civilian-economy.md), [`design/manufacturing-and-the-dependency-ladder.md`](manufacturing-and-the-dependency-ladder.md), [`studies/interplanetary-bulk-logistics-mines-depots-and-shipyards.md`](../studies/interplanetary-bulk-logistics-mines-depots-and-shipyards.md), [`studies/drive-survey-concepts-ranges-and-minimum-sizes.md`](../studies/drive-survey-concepts-ranges-and-minimum-sizes.md), [`design/weapon-blocks-and-engineering-projects.md`](weapon-blocks-and-engineering-projects.md), [`design/detection-and-the-picture.md`](detection-and-the-picture.md), [`design/outward-the-belt-jupiter-and-independence-from-earth.md`](outward-the-belt-jupiter-and-independence-from-earth.md).
- DeYoung (1981), [The Lasky cumulative tonnage–grade relationship: a reexamination](https://pubs.usgs.gov/publication/70011787), Economic Geology 76(5).
- DeYoung and Singer (1981), [Physical factors that could restrict mineral supply](https://www.usgs.gov/publications/physical-factors-could-restrict-mineral-supply), USGS.
- [Modelling the Skinner thesis: consequences of a lognormal or a bimodal resource base distribution](https://proceedings.systemdynamics.org/2014/proceed/abstracts/1417.html), System Dynamics Conference 2014.
- Cunningham et al. (2008), [Quantitative mineral resource assessment of undiscovered porphyry copper deposits in the Andes](https://pubs.usgs.gov/of/2008/1253), USGS OFR 2008-1253 (the three-part form).
- Thunder Said Energy, [Mining: crushing, grinding and comminution costs](https://thundersaidenergy.com/downloads/mining-crushing-grinding-and-communition-costs/): ~20 kWh/t integrated plant, Bond work indices 9–13 kWh/t.
- [Lunar Ice Miner, ICES 2022-130](https://www.1-act.com/wp-content/uploads/2022/07/ICES-2022-130-Lunar-Ice-Miner-FINAL-Manuscript.pdf): heating ice from 40 K and sublimating at 200 K, ~0.83 kWh per kg of water derived from its 2.3 kW at 2.78 kg/h.
- NASA, [ISRU Pilot Excavator bucket-drum scaling (ASCE Earth & Space 2022)](https://ntrs.nasa.gov/api/citations/20210025846/downloads/ASCE%20E%26S%202022-%20ISRU%20Pilot%20Excavator%20BD%20scaling.pdf): excavation energy per kg falls with drum size and cut speed.
- Cannon et al. (2020), via Eos, [Moon may hold billions of tons of subterranean ice at its poles](https://eos.org/research-spotlights/moon-may-hold-billions-of-tons-of-subterranean-ice-at-its-poles): gigaton-scale ice, oldest deposits buried ≥10 m.
- Lainey et al. (2024), via Eos, [That's no moon, it's an ocean world](https://eos.org/articles/thats-no-moon-its-an-ocean-world): Mimas's orbit and libration require an ocean beneath 20–30 km of ice.
- Mainzer et al., NEOWISE NEA population; Grav et al. (2023), NEO Surveyor known-object model: as cited in [`studies/solar-resources/sources.md`](../studies/solar-resources/sources.md).
- *(calc)* marks figures computed for this doc from the numbers above.
