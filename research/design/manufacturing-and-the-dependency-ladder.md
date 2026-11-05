# Intercept Window: Manufacturing and the Dependency Ladder

Nov 2, 2026 · @Teemu

Manufacturing is modelled as **processes, not factories**: a product needs a set of processes at a given quality, each process needs feedstock, energy and its own plant, and a polity's independence is the share of that tree it can run itself. The pacing comes from the tree, not from a timeline.

## The short version

- **A process is a tech block.** Smelting, casting, machining, winding, crystal growth, lithography: each is a block of physical numbers (energy per kg, throughput per tonne of plant, achievable quality, feedstock grade, what environment it needs). Research opens the principle; engineering improves the numbers.
- **A product is a bill of processes,** not a recipe unlocked by tech level. A tank shell needs rolled or printed metal at modest quality. A turbopump needs precision machining, bearings and alloys. A fusion magnet needs superconductor tape. A flight computer needs a chip fab.
- **Closure is the measure of independence:** the share of a product's (or a plant's) bill that can be run locally, counted by mass and by value separately. Mass closure comes early (90 % or more is bulk metal, rock and volatiles). Value closure comes last, held back by a few **vitamins**: chips, sensors, bearings, catalysts, superconductor, fissile fuel.
- **Quality is continuous, never a gate.** A belt-made bearing is not forbidden; it is worse (lower speed rating, shorter life, heavier for the load). A design made from local parts builds, and its report shows the cost. That is the no-hard-cutoffs rule applied to industry.
- **Plant builds plant.** The fastest growth comes from factories that spend most of their output on more factories. Growth rate is set by the plant's specific throughput (kg of product per kg of plant per year) and by the trickle of vitamins from outside.
- **Energy is the master input.** Every process has a kWh/kg. As processes get more general, energy per kg rises and the need for specific ores falls. The two far limits: a universal assembler, where atoms of the right elements plus energy make anything; and transmutation, where energy alone makes the elements. Both are curves at the far end of the same model, not new systems.
- **Earth stays the cheapest source of the hardest things for a long time.** The ladder is not "space can't make X" but "space makes X worse, slower and dearer than Earth sells it", until it doesn't. That crossover, per product, is the dependency curve.

## What the real world says (late 2026)

In 2026 every in-space manufacturing process exists only at grams-to-kilograms demonstration scale, so a contemporary-tech start means near-total Earth dependence. That is the honest starting point, and it matches the design notes.

| Capability | Demonstrated or studied | Key numbers | Source |
| --- | --- | --- | --- |
| Oxygen from CO₂ (Mars) | Flown, 2021–2023 | 15 kg, 300 W unit; 122 g total, best 12 g/h | [MOXIE](https://Www.Wikipedia.org/wiki/MOXIE) |
| Oxygen from regolith, carbothermal | Vacuum-chamber tests, TRL 6 | About 11–16 g O₂ per kWh delivered | [Azami et al. 2024 review](https://arxiv.org/pdf/2408.05823) |
| Oxygen from ilmenite, H₂ reduction | End-to-end energy model | 24.3 kWh per kg of liquid O₂ at 10 % ilmenite | [Leger et al. 2025](https://publikationen.bibliothek.kit.edu/1000180152) |
| Molten regolith electrolysis | 25 kg vacuum run; plant studies | Plant: 6.8 t, 311 kW → 25 t ferrosilicon + 23.9 t O₂ a year | [Azami et al. 2024 review](https://arxiv.org/pdf/2408.05823), [NASA KSC](https://ntrs.nasa.gov/api/citations/20250005608/downloads/MRE_SRR_Core_presentation.pdf) |
| Molten salt (FFC Cambridge) | Lab pilot on simulant | 96 % of oxygen out at 950 °C; leaves mixed Al-Fe-Si, Fe-Si-Ti, Ca-Si-Al powders | [ESA](https://esa.int/Space_in_Member_States/United_Kingdom/Oxygen_and_metal_powder_extracted_from_moonrocks), [review](https://arxiv.org/pdf/2408.05823) |
| Carbonyl (Mond) refining of asteroid Ni-Fe | Proposed only | Pure Fe, Ni, Co from native metal at modest heat; residue rich in PGMs | [Lewis et al.](https://core.ac.uk/works/24868691) |
| Sintered or melted regolith | Lab and chamber tests | Compressive strength 2.5 MPa (solar) to 345 MPa (laser, vacuum); brittle ceramic | [Azami et al. 2024 review](https://arxiv.org/pdf/2408.05823) |
| Metal 3D printing in orbit | ISS, 2024 | 180 kg printer, stainless wire and laser; first part took months | [ESA](https://www.esa.int/Newsroom/Press_Releases/ESA_3D_prints_first_metal_part_on_the_International_Space_Station), [Airbus](https://www.airbus.com/en/newsroom/stories/2024-09-behind-the-scenes-of-the-first-metal-part-to-be-3d-printed-aboard-the-iss) |
| Semiconductor crystal growth in orbit | Free-flyer, Dec 2025 | 1,000 °C plasma; target GaN, SiC, AlN, diamond; seeds go to Earth fabs | [Space Forge](https://www.spaceforge.com/press-releases/space-forge-ignites-a-new-industrial-era-delivering-world-first-capability-for-orbital-semiconductor-manufacturing) |
| Solar cells from regolith | Lab evaporation; design studies | Lunar Si cells about 5–10 % efficient; 200 kg crawler, about 1 MW in several years | [Ignatiev et al.](https://iafastro.directory/iac/archive/browse/IAC-05/A5/1/2436/) |
| Chips on Earth, for scale | Industrial | Hundreds of process steps; 250–500 kWh for one 50 g wafer | [Escholarship LCA](https://escholarship.org/content/qt7931209f/qt7931209f.pdf), [Uniba](https://ricerca.uniba.it/handle/11586/8698) |
| Self-expanding lunar industry | Studies | 1980: 100 t seed copies itself in a year. 2012: 12–41 t landed over about 20 years, six generations | [NASA AASM](https://NSS.org/wp-content/uploads/2017/07/1982-Self-Replicating-Lunar-Factory.pdf), [Metzger et al.](https://arxiv.org/pdf/1612.03238) |

Five things the record says that the game should keep:

- **Oxygen comes first, metal falls out of it.** Every regolith process is an oxygen plant with metal as a by-product. The first rung is a propellant economy, and crude alloys appear as its waste.
- **The first metal is a mongrel.** FFC and MRE give whatever alloy the rock dictates (ferrosilicon, Al-Fe-Si). Metzger models early local hardware as 2.5 times heavier than Earth-built for the same job, falling to parity only after several generations.
- **Energy per kg spans about seven orders of magnitude,** from tens of kWh/kg for oxygen to thousands for wafers, and far more for transmutation (see "The limits").
- **Plant mass per unit of output decides growth.** An MRE plant makes about seven times its own mass a year; a 3D printer near its own mass in months. A chip fab is the opposite extreme.
- **Chips are the vitamin that does not go away.** Metzger's own model shows that without local chip-making, the import mass grows exponentially with the industry it feeds. Electronics closure goes 90 %, 95 %, 99 %, 100 % across his last four generations.

## The model: processes, materials, bills and closure

The model has four pieces: process blocks, materials as grades, a bill of processes per product, and closure measured per polity and location. Nothing in it names an era.

### Process blocks

A process is a tech block like a drive: physical numbers with a name as label. Research opens the principle (molten regolith electrolysis, carbonyl refining, EUV lithography); engineering improves the numbers.

| Field | What it holds | Example: MRE plant |
| --- | --- | --- |
| Feedstock | Material grades it accepts, and how output varies with them | Any silicate; highland regolith is easier than mare |
| Reagents | What it consumes or loses per kg | Electrodes, refractory wear |
| Energy | Electric and thermal kWh/kg, separately (thermal can be raw sunlight) | About 56 kWh per kg of product |
| Output | Material grade or part, with its quality numbers | Ferrosilicon, O₂ |
| Specific throughput | kg of product per kg of plant per year | About 7 |
| Plant bill | What the plant itself is made of, as processes | Refractories, power electronics, electrodes |
| Environment | Gravity, vacuum, cleanliness, temperature it needs | Gravity helps melt handling; vacuum free |
| Labour | Robot- or crew-hours per kg, and the autonomy level it needs | Low once running |

Two fields deserve stress. **Environment** is where location enters: carbonyl liquids are hard to separate in free fall, so a belt refinery wants spin; deposition and electron-beam work want vacuum, which the Moon gives free. **Plant bill** is what makes the model recursive: a process can only run where its own plant can be built or delivered.

### Materials as grades, not names

A material is a composition plus property numbers: density, strength, stiffness, conductivity, maximum service temperature, purity, radiation tolerance. "Mare ferrosilicon, Ceres grade" is a material like any other. The ship generator already takes material blocks for armour; local materials plug into the same slots with different numbers.

This is where the no-hard-cutoffs rule pays off. A designer can build a radiator from local aluminium-silicon alloy instead of Earth copper-carbon. It builds; the report shows the fin efficiency drop and the mass rise.

### Quality is a curve, not a gate

Every part type maps its inputs' quality to its performance. A turbopump's power-to-mass falls with alloy strength. A bearing's life falls with surface finish. A magnet's field falls with superconductor quality. A computer's speed falls with feature size and defect density.

- **Below the sweet spot a part is poor, never forbidden,** exactly as with drives below their size sweet spot.
- **Metzger's crudeness factor is the simplest form** of this curve: one mass multiplier per generation (2.5, then 1.5, then 1.0).
- **The report says it in consequences:** "local-grade turbopump: 1.6× mass, half the rated life".

### Bills of processes and closure

A product is a tree: parts, their materials, and the processes that make each. Closure is the share of that tree a polity can run itself, at a given location, from inputs it holds.

```latex
\text{closure}_{\text{mass}} = \frac{\sum_{\text{local leaves}} m}{\sum_{\text{all leaves}} m} \qquad \text{closure}_{\text{value}} = \frac{\sum_{\text{local leaves}} c}{\sum_{\text{all leaves}} c}
```

Here m is mass and c is the cost of making that leaf (embodied energy, labour and plant time). The two numbers diverge sharply, and the gap is the game:

- **Mass closure comes early.** Tanks, trusses, armour, shielding water, radiator fins and propellant are most of a ship's mass and need only bulk processes.
- **Value closure comes late.** It is held back by **vitamins**: items that are a small share of mass and a large share of cost. Chips, sensors, precision bearings, catalysts, superconductor tape, fissile fuel.
- **Closure is per location,** like leverage. A company with a chip line at Ceres and none at Vesta is closed at one and dependent at the other, and the map should show it.
- **A bought block counts as a leaf.** Buying a drive outright, buying its parts, or holding the processes to make it are three different closure states, which is how "bought or engineered at home" from the design notes becomes mechanical.

## The ladder: from Earth-reliant to self-sufficient

The dependency curve's tiers (volatiles, structural metals, electronics, chip fabs, fusion components) refine into seven families of processes. They are labels on families of process blocks, not unlocks: a polity can hold some of tier 5 and none of tier 3, and pay for it in imports.

| Tier | What it makes | Key processes | Leaves it still imports | What it ends |
| --- | --- | --- | --- | --- |
| **0. Assembly and repair** | Ships and stations from Earth kits; module swaps; refuelling with imported propellant | Docking, robotic assembly, welding, inspection | Everything | Nothing; it buys flexibility, not independence |
| **1. Volatiles** | Water, O₂, H₂, CH₄, CO, N₂: propellant, coolant, shielding water, life support | Ice mining, heating, electrolysis, Sabatier, regolith oxygen, liquefaction | The plants, their electronics and power | The largest import by mass: propellant is 50–80 % of a ship's wet mass |
| **2. Bulk structure** | Tank shells, trusses, armour plate, bumpers, crude radiator fins, hull shells, rubble jackets, crude rails | MRE, FFC, carbonyl refining, casting, rolling, wire-arc printing, sintering | Everything that moves, spins, switches or computes | Most of a ship's dry mass |
| **3. Refined and precision** | Controlled alloys, polymers, seals, carbon fibre, machined parts, bearings, pumps, valves, turbomachinery, nozzles, cryotanks | Alloying, machining, grinding, lapping, heat treatment, carbon and nitrogen chemistry, metrology | Machine tools at first; electronics; catalysts | Spare parts, and the hardware of tiers 1–2 themselves |
| **4. Power and propulsion hardware** | Solar cells, motors, generators, radiators to spec, heat exchangers, reactor and drive bodies | Thin-film deposition, winding, magnet making, nuclear-grade machining | Fuel, control electronics, superconductor | The power-plant import; drives minus their hard cores |
| **5. Electronics** | Power electronics, cables, boards, then logic at coarse nodes, then sensors, then fine nodes | Crystal growth, doping, deposition, lithography, packaging, ultrapure chemicals | Lithography optics, focal-plane detectors, fine-node chips | The vitamin stream, step by step |
| **6. Nuclear and exotic** | Fissile and fusion fuel, superconductor tape, plasma-facing tungsten, large optics, laser media | Enrichment, breeding, isotope separation, tape deposition, mirror casting and polishing | Whatever the polity has not engineered yet | Drive rights in practice: the last thing the host can withhold |

### What each tier means in play

- **Tier 1 is the first lever.** A company that makes its own propellant can refuel anyone, so its depot is leverage over passing traffic. Earth's first loss is not industry but refuelling.
- **Tier 2 gives "local hulls, Earth insides".** A belt-built warship whose hull, tanks and armour are local but whose drive, reactor and fire control are Earth-made is still a hostage to Earth's spares.
- **Tier 3 is bootstrapped precision.** Precision is made from less precision: flat plates lapped against each other, screws cut and recut, machines that build better machines. Machine tools are therefore a strategic import, and their sale is the space version of an export-controlled machine-tool deal.
- **Tier 5 does not need Earth's best to matter.** Spacecraft computers already fly on decades-old, radiation-hardened nodes. A local line at a coarse node can run a warship; it cannot match Earth's fire-control and sensor processing. The curve, not a switch, decides how much that costs in a fight.
- **Sensors are their own vitamin.** Infrared focal-plane arrays sit at the far end of tier 5. That ties manufacturing directly to [`design/detection-and-the-picture.md`](detection-and-the-picture.md): a company that cannot make detectors buys its picture's quality from Earth.
- **Tier 6 is where the politics concentrates.** Enrichment is the proliferation flashpoint already in the notes; superconductor tape gates fusion drives and magnetic nozzles; large optics gate laser range. Each is a small, visible, high-value facility.

### The fuel cycle is a sub-ladder

Nuclear fuel follows its own rungs, each a separate facility with its own visibility: mining (uranium and thorium are scarce in most asteroids, richer in some lunar terrains), conversion and enrichment, breeding in reactors, fuel fabrication, reprocessing. Fusion fuel is easier at the bottom (deuterium comes from any water) and harder at the top (tritium must be bred from lithium; helium-3 must be mined from regolith or gas giants). Pulse units and warheads draw on the same cycle, which is why the line between the two is mostly intent.

## What can be built where

Mapped onto the ship generator's parts, the most mass goes local first and the most value goes local last. Armour is the happy accident: at hypervelocity, protection is density-led, so crude local plate loses little.

### Ship parts against the ladder

| Part (shipgen) | Lowest tier that can make it | What a local-grade version costs | What still needs high tiers |
| --- | --- | --- | --- |
| Propellant, coolant, shielding water | 1 | Nothing: the molecule is the same | Cryogenic storage hardware (3) |
| Rubble jacket | 0 | Nothing; free mass where the rubble is | — |
| Armour plate, Whipple bumpers | 2 | Little at hypervelocity (density-led); more against slow ballistic rounds, where strength matters | High-strength ceramics and composites (3) |
| Truss spine, structure | 2 | Lower specific strength: higher structure fraction, shorter length limit at high g | Aerospace alloys, carbon fibre (3) |
| Tank shells | 2 | Higher tankage fraction, so less Δv for the same mass | Light cryotanks and insulation (3) |
| Radiator fins | 2 | Lower conductivity: worse fin efficiency, more mass for the same heat | Carbon-carbon fins, heat pipes, droplet generators (3–4) |
| Pressure hull, crew shelter, hab ring | 2 | Heavier shells | Seals, polymers, life-support machinery (3) |
| Turbopumps, valves, RCS thrusters, chamber and nozzle | 3 | Heavier, shorter-lived, lower chamber pressure | Superalloys, fine machining (3+) |
| Point-defence guns, coilgun barrels and coils | 3–4 | Heavier mounts, more barrel wear, lower muzzle velocity | Capacitors and fast switching (5) |
| Fission reactor and NTR core | 4 | Lower specific power, more shielding | Fuel (6), control electronics (5) |
| Orion pusher plate and absorbers | 2–3 | Heavier plate | Pulse units: fissile (6) plus precision (3) |
| Magnetic-confinement fusion drive | 4–6 | Weaker field means a bigger, heavier drive for the same power | Superconductor tape, plasma-facing tungsten, cryoplant, power electronics (5–6) |
| Laser weapon | 4–6 | Smaller or rougher mirror means shorter range (R ∝ D) | Large optics, gain media or FEL accelerator (6) |
| Missiles | 2–5 | Airframe and motor go local early | Seekers (5), warheads (6) |
| Sensors, fire control, computers | 5 | Coarse-node computing: slower solutions, poorer tracking | Focal-plane arrays, fine-node chips (5+) |

The report should say this in the designer's language. A belt-built frigate with local tanks and spine might read: "Δv −14 % against the Earth-built twin; fire control and drive core imported (Earth)."

### Facilities and where they want to be

Facilities are bundles of process blocks at a location: mine, refinery, foundry and mill, machine shop, chemical plant, fab, fuel plant, assembly yard. Each has a throughput, a power draw, a footprint others can see, and its own bill. Five location factors decide where they go:

- **Feedstock.** Ice at lunar poles, comets and C-type asteroids; native Ni-Fe in M-types and scattered through regoliths; silicates everywhere; thorium-rich terrains on the Moon. Bodies keep their bulk composition and extraction cost curves, as the design notes require.
- **Power.** Sunlight falls as 1/r²: about 1,361 W/m² at Earth, about 180 W/m² at Ceres and about 50 W/m² at Jupiter. Belt industry therefore leans on reactors or very large mirrors, which pulls it toward the fuel cycle.
- **Gravity.** Some processes want it (melt handling, settling, liquid separation), so spin facilities or small moons win. Others want free fall (crystal growth, big thin structures).
- **Export Δv.** The gravity well taxes every kilogram shipped out. That is why heavy industry leaves Earth, and why a lunar mass driver is an industrial asset as much as a weapon.
- **Exposure.** A fab or enrichment plant is large, hot, power-hungry and stationary. Where it sits decides who can see it, and who can reach it.

**Yards are cheap in space; what goes in them is not.** The design notes cap hull size by assembly yard, like Rule the Waves' docks. In free fall a yard is mostly truss, which tier 2 makes easily, so yard size stops binding early. The binding limit becomes the inside of the ship.

## Bootstrapping and growth

Industry grows by spending its output on more industry, and the vitamin stream from outside caps that growth. Those two facts set the whole pace of independence, with no dates anywhere.

### The growth law

```latex
r = \frac{s \cdot f}{k} \qquad \frac{dP}{dt} = \min\left( r P,\ \frac{I}{v} \right) \qquad t_{2} = \frac{\ln 2}{r}
```

- **P** is plant mass. **s** is specific throughput (kg of product per kg of plant per year). **f** is the share of output reinvested in plant rather than sold or spent. **k** is the crudeness factor of local plant.
- **I** is the vitamin import rate (kg a year) and **v** is the vitamin share of new plant mass.
- Below the cap, growth is exponential with doubling time t₂. Once rP exceeds I/v, growth turns **linear**: the industry can only add as much plant as its imported chips and bearings can equip.

Metzger's first-generation lunar set is about 5 % electronics by mass (391 kg of 7.7 t), all imported. With r = 0.6 a year (doubling about every 14 months) and 20 t a year of imports, a 20 t seed reaches roughly 8,000 t in ten years at full closure. At v = 1 % it passes 6,000 t and then adds only about 2,000 t a year; at v = 5 % only about 400 t a year.

**Chart: "With 1 % of plant imported, the industry is 120× smaller by year 20."** Plant mass on a log scale over 20 years, from the growth law above (seed 20 t, r = 0.6 a year, I = 20 t a year):

| Year | Full closure | 1 % imported | 5 % imported |
| --- | --- | --- | --- |
| 0 | 20 t | 20 t | 20 t |
| 5 | 401 t | 401 t | 401 t |
| 10 | 8.1 kt | 6.3 kt | 2.3 kt |
| 15 | 162 kt | 16 kt | 4.3 kt |
| 20 | 3.2 Mt | 26 kt | 6.3 kt |

That is the dependency curve in one line: **Earth's leverage is I, and the company's escape is driving v toward zero.** Every vitamin the company learns to make raises its ceiling; every export control on one lowers it.

### Four ways to bootstrap

| Strategy | How it works | Upfront cost | Weakness | Historical shape |
| --- | --- | --- | --- | --- |
| **Seed factory** | Land a complete, closed set that copies itself (NASA 1980: 100 t, one copy a year) | Very high | All-or-nothing; one missing part stops everything | None: nobody has done it |
| **Technology spiral** | Land a small sub-replicating set; each generation is cruder, then better; closure rises step by step (Metzger: 12–41 t over about 20 years) | Low | Slow early; needs teleoperation, then autonomy | Industrialisation itself, replayed fast |
| **Import substitution** | Earth ships kits; locals make whatever costs most to import, first propellant, then bulk, then parts | Ongoing | Never escapes the vitamin cap on its own | Colonial economies, the chartered companies |
| **Specialised network** | Different sites close different tiers (belt metals, outer-system volatiles, a lunar fab) and trade | Moderate | The trade lanes are targets; closure exists only for the network | Metzger's "ecology, not replicator" |

All four should be playable, because they are just different investment orders over the same process blocks. AI polities will pick by their temper and their host's posture.

### Pacing levers that are physics, not scripts

- **Specific throughput** of each process block sets the doubling time. Bulk processes run at a few times their own mass a year; a 3D printer near its own mass in months; a fab at a tiny fraction.
- **Delivered price from Earth.** Each product has a crossover where local making beats buying. Cheap launch delays local bulk industry but also cheapens the seed, so it cuts both ways.
- **Autonomy.** Metzger's generations need robots that move from teleoperation to supervised autonomy. Light-lag makes teleoperation fail beyond the Moon, which ties industry to the existing delegation mechanics.
- **Learning curves.** A new line's yield and cost improve with cumulative output (Wright's law, typically 10–30 % per doubling; approximate). A company's first local chips are poor and dear; its thousandth batch is not.
- **Know-how.** A process block's engineered numbers are knowledge. Buying plant without know-how gives Earth's numbers once; buying know-how lets the company improve them. Stealing it is an incident.

## The limits: atoms, energy and transmutation

There are three far limits, and they make three different things meaningless: the mineral, the structure and the element. Each is a curve at the far end of the same process model, so the data model covers them without new systems.

**Chart: "Energy per kg climbs six orders of magnitude from oxygen to transmutation."** kWh per kg made or processed, log scale:

| Process | kWh per kg | Basis |
| --- | --- | --- |
| Liquid O₂, ilmenite reduction | 19–30 | Model (Leger et al. 2025) |
| FeSi + O₂, molten electrolysis | 56 | Plant study (Azami et al. 2024) |
| O₂, carbothermal reduction | 63–91 | Vacuum tests (CaRD, in Azami et al. 2024) |
| Ionising rock for mass sorting (per kg of rock) | 14–100 | Estimate (PPPL $10/kg energy cost) |
| Silicon wafer, Earth fab | 5,000–10,000 | Measured (Uniba wafer LCA) |
| One element up, by spallation | 3.4M–67M | Computed in this doc |
| A 1 ppm element by mass sorting | 14M–100M | Computed in this doc |

The last two ranges overlap: below about 1 ppm, making an element beats finding it.

| Limit | What becomes meaningless | What still matters | Rate limit | Standing in 2026 |
| --- | --- | --- | --- | --- |
| **Universal separation** (plasma mass sorting) | The mineral: any rock yields every element it holds | Elemental abundance; energy per kg of rock | Throughput and power | Proposed for nuclear waste; ionising solid waste costs about $10/kg in energy ([PPPL](https://www.princeton.edu/news/2015/12/10/pppl-physicists-propose-new-plasma-based-method-treat-radioactive-waste)) |
| **Universal assembly** (atoms plus a file) | The structure: any configuration from elements | Element feedstock, power, heat rejection | Cooling | Theory only; a primitive nanofactory design: 10 kg unit, 4 kg of product in 3 h, a copy in about 15 h ([Phoenix](https://jetpress.org/volume13/Nanofactory.pdf)) |
| **Transmutation** (neutrons in, new elements out) | The element: any element from neighbouring ones | Neutron supply and energy | Neutron flux | Real for breeding and isotopes; about 25 MeV of beam per spallation neutron ([ATW comparison](https://core.ac.uk/download/71195276.pdf)) |

### Separation makes the mineral meaningless first

Atomise and ionise the feed, then sort by mass. The energy is set per kg of rock, not per kg of product, so an element's cost scales as 1/abundance. Above roughly a part per million, any body is an ore body for anything it contains. This is the cheapest of the three limits and arrives first; it turns prospecting into energy budgeting.

### Assembly makes the structure meaningless

Given elements and energy, an assembler builds any configuration from a file. Three consequences matter for the game:

- **Feedstock shifts to carbon.** Early designs are diamondoid, so carbon-rich bodies (C-type asteroids, comets) become the prized feedstock, not metal.
- **Heat is the throttle.** Phoenix's design is cooling-limited, and in space cooling means radiators. The same fin and T⁴ physics that sizes warships sizes factories.
- **Closure jumps to almost 1.** With a copy every 15 hours, the growth law's ceiling is the only limit left. That is either the endgame or a runaway, and is a balance decision (see "Paths").

### Transmutation makes the element meaningless last

Neutron capture plus beta decay moves a nucleus up one element; spallation and fission move it down. Breeding fissile fuel (thorium to U-233, U-238 to plutonium) and tritium from lithium are transmutation already, so this tier begins in the fuel cycle.

- **Energy cost by accelerator:** at 25–150 MeV per useful neutron, one capture step costs about 3×10⁶ to 7×10⁷ kWh per kg. That is 3 to 60 kilotons of TNT equivalent per kg moved one element.
- **By fusion neutrons it is almost free in energy.** D-T fusion makes one 14 MeV neutron per 17.6 MeV released, so a fusion economy gets neutrons as a by-product. 1 GW of D-T fusion makes about 3.5×10²⁰ neutrons a second: roughly 1 t a year moved one element up (A ≈ 60, every neutron captured).
- **So transmutation is rate-limited, not energy-limited,** once fusion exists. A 1 TW torch-era plant could move about 1,000 t a year. That is a vitamin supply, never a bulk one.
- **The crossover with separation sits around 0.1–10 ppm.** Below that, making an element costs less than finding it.

Turning energy straight into matter (9×10¹⁶ J per kg) and fusing light elements into iron are beyond any plausible industry and stay out of the model.

## Paths: design choices and a recommendation

The recommended path is a hybrid: real process blocks and quality curves underneath, so ship numbers are physical, with the player managing facilities and investment rather than recipes. The table lists the choices that remain.

| Decision | Options | Recommended | Why |
| --- | --- | --- | --- |
| **Granularity** | (a) Full recipe chains per part, Factorio-style. (b) Closure numbers per tier family only. (c) Process blocks underneath, facilities and tiers on top | (c) | Physical where it decides (part quality into ship numbers), rough where it does not (internal logistics). Same rule as Fleetwright's flooding and damage control |
| **How capability arrives** | (a) Research unlocks discrete recipes. (b) Research opens principles; engineering improves process numbers continuously, with learning curves | (b) | Identical to the drive-block decision of Oct 30; no hard cutoffs |
| **What paces independence** | (a) A scripted tier order. (b) Emergent: crossover prices, the vitamin cap, autonomy, know-how, export controls | (b) | Eras are tech states, never dates; different polities climb in different orders |
| **Bills of processes** | (a) Hand-written per product. (b) Generated from the ship generator's parts, each part mapped to processes and grades | (b) | The generator already knows every part; the report can show origin and closure per design for free |
| **Bootstrapping** | One fixed strategy, or all four (seed, spiral, substitution, network) | All four | They are investment orders over the same blocks; AI tempers pick among them |
| **Universal assembler** | (a) Leave out. (b) Far-end process block with heat throttle and near-total closure. (c) In the data model, out of content | (c) for now | "Design the data model for the dream, build content for the first game" |
| **Transmutation** | (a) Leave out. (b) Breeding only. (c) Breeding plus neutron-flux-limited vitamin transmutation | (c) | Breeding is needed anyway for pulse units and fission; the rest is the same neutron model at higher flux |
| **Scenario battler** | No industry, or preset local-grade blocks | Preset local-grade blocks | Lets the battler test the quality curve: a belt-built frigate with crude armour and imported fire control against its Earth twin |

### What the player actually does

- **Places and sizes facilities**, as the notes already say for bases and colonies. Flows between them run as Routine schedules, never as micromanaged convoys unless something interesting happens.
- **Chooses what to make and what to buy,** per product and per location. The designer shows each part's origin and the closure it implies.
- **Invests in process blocks:** research for principles, engineering for numbers, and purchases of plant or know-how from others.
- **Reads dependency on the map:** closure by tier per location, vitamin stockpiles in months, and the import stream that feeds them.

## Ties to the rest of the design

Manufacturing is not a separate layer: it feeds the dependency curve, the picture, the incident record and the ship designer through numbers they already read.

- **Dependency curve.** The host-leverage term "dependency" becomes concrete: which tiers the company still imports, its vitamin share v, and how many months its stockpiles last under embargo. The growth law gives the cost of an embargo in lost growth.
- **Drive rights.** Earth controlling torch drives means, in practice, Earth controlling tier 6: superconductor tape, fusion components, enrichment. A charter clause on drives is an export control on vitamins.
- **The picture.** Facilities are large, hot, stationary and power-hungry. A covert fab or enrichment plant must hide its waste heat, with the same radiator orientation and timing tricks as a dark-running ship ([`design/detection-and-the-picture.md`](detection-and-the-picture.md)).
- **Incidents.** Buying a controlled machine tool, running an unlicensed fab, stealing know-how and covert enrichment are rung-2 acts on the defiance ladder, each recorded with who could observe it.
- **Ship designer.** Local materials are material blocks with worse numbers; the report shows each part's origin and the design's closure. Charter terms can include "built in host yards" or "host-made drive only" clauses.
- **Combat endurance.** A fleet far from tier-3 shops cannot replace a turbopump or a radiator loop. Spares and repair depth become logistics, like Fleetwright's damage-control parties at campaign scale.
- **Light-lag and delegation.** Teleoperation works from Earth to the Moon (about 2.5 s round trip) and fails in the belt, so early industry clusters near its operators until autonomy improves. The same lag that forces delegated captains forces autonomous factories.
- **Resources.** Universal separation is what flattens the extraction cost curves in the design notes, toward whole-body disassembly. The two models are one.
- **Time tiers.** Industry lives on the Routine tier as rates and schedules. Dropping in finds a plausible state: a smelter mid-batch, a freighter mid-transfer.

## Open questions

- [ ] Granularity of closure on the map: seven tier families, or per process block?
- [ ] How "value" is counted for value closure: embodied energy, labour and plant time, or delivered market price?
- [ ] Crudeness curves per part type: where does the data come from? Proposal: a materials-grades study added to the research agenda's Tier 1.
- [ ] Know-how as a number: an engineering level per process block per polity, and how it leaks through trade, defectors and espionage.
- [ ] Vitamin shelf life: chips keep, some chemicals and fuels do not. Does stockpiling need decay?
- [ ] Facilities as targets: do fabs and enrichment plants get hitboxes and damage like ships?
- [ ] Autonomy as a research line: Metzger's teleoperation-to-autonomy ladder, tied to light-lag.
- [ ] Universal assembler: long-term content, or only a data-model possibility?
- [ ] The "Industry in space" and "Research and engineering" Tier 2 studies should produce the first process-block catalogue.

## Sources

- [Metzger, Muscatello, Mueller and Mantovani, Affordable, rapid bootstrapping of space industry (2012)](https://arxiv.org/pdf/1612.03238)
- [Freitas and Gilbreath, Advanced Automation for Space Missions, ch. 5 (NASA CP-2255, 1982)](https://NSS.org/wp-content/uploads/2017/07/1982-Self-Replicating-Lunar-Factory.pdf)
- [Azami et al., A Comprehensive Review of Lunar-based Manufacturing and Construction (2024)](https://arxiv.org/pdf/2408.05823)
- [Leger et al., Modeling energy requirements for oxygen production on the Moon (2025)](https://publikationen.bibliothek.kit.edu/1000180152)
- [NASA KSC, Molten Regolith Electrolysis core sample analysis](https://ntrs.nasa.gov/api/citations/20250005608/downloads/MRE_SRR_Core_presentation.pdf)
- [Schreiner, MRE reactor modeling and optimization (MIT thesis)](https://dspace.mit.edu/handle/1721.1/98589)
- [ESA, Oxygen and metal powder extracted from moonrocks (Metalysis)](https://esa.int/Space_in_Member_States/United_Kingdom/Oxygen_and_metal_powder_extracted_from_moonrocks)
- [Lewis et al., Carbonyl extraction of lunar and asteroidal metals](https://core.ac.uk/works/24868691)
- [MOXIE](https://Www.Wikipedia.org/wiki/MOXIE)
- [ESA, First metal part 3D printed on the ISS (2024)](https://www.esa.int/Newsroom/Press_Releases/ESA_3D_prints_first_metal_part_on_the_International_Space_Station)
- [Airbus, Behind the scenes of the first metal part printed on the ISS](https://www.airbus.com/en/newsroom/stories/2024-09-behind-the-scenes-of-the-first-metal-part-to-be-3d-printed-aboard-the-iss)
- [Space Forge, plasma on ForgeStar-1 (Dec 2025)](https://www.spaceforge.com/press-releases/space-forge-ignites-a-new-industrial-era-delivering-world-first-capability-for-orbital-semiconductor-manufacturing)
- [Ignatiev et al., Solar cell fabrication on the Moon (IAC 2005)](https://iafastro.directory/iac/archive/browse/IAC-05/A5/1/2436/)
- [Semiconductor fab process and energy LCA (Escholarship)](https://escholarship.org/content/qt7931209f/qt7931209f.pdf)
- [Material and energy flow of wafer production (Uniba)](https://ricerca.uniba.it/handle/11586/8698)
- [Phoenix, Design of a Primitive Nanofactory (2003)](https://jetpress.org/volume13/Nanofactory.pdf)
- [PPPL, plasma mass filtering for nuclear waste (2015)](https://www.princeton.edu/news/2015/12/10/pppl-physicists-propose-new-plasma-based-method-treat-radioactive-waste)
- [Fusion against accelerator neutron sources for transmutation (ATW comparison)](https://core.ac.uk/download/71195276.pdf)
- [Accelerator neutron energy cost (US patent 5160696)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5160696)
