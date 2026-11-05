# Intercept Window: Research Agenda

Oct 30, 2026 · @Teemu (updated Nov 1)

The studies needed at the same depth as the impact and burst studies: physical models that are source-neutral, sourced, and checked against a yardstick before anything is built on them. Ordered by what the scenario battler needs first.

**How each study is done** (the Fleetwright pattern):

- **The question:** what the model must decide in the game.
- **The model:** inputs as physical numbers, smooth across regimes, no hard cutoffs.
- **The yardstick:**
  - reference calculations for mechanisms;
  - real test data where it exists;
  - the ranges where each source holds.
- **A reference script:** checks mechanisms only, never a second engine.
- **What stays rough:** detail goes only where outcomes are decided.

## Tier 1: effects (what weapons and accidents produce)

These are the source-neutral models every weapon and every accident reuses.

| Study | What it decides | Starting points |
| --- | --- | --- |
| **Hypervelocity impacts** | Projectile clouds against single and spaced walls, across the ballistic, shatter, hypervelocity and vaporising regimes | NASA ballistic limit equations (Christiansen), Holsapple cratering scaling, Tate–Alekseevskii, CoaDE |
| **Bursts** | Nuclear, antimatter and accident bursts: output partition, propagation, attenuation, deposition | Glasstone & Dolan *The Effects of Nuclear Weapons*, Starfish Prime records, CoaDE, Atomic Rockets |
| **Beams** | Lasers and particle beams. Spot size by diffraction, pointing jitter and range; coupling into the target (absorption, ablation, the plasma's shielding, pulsed vs continuous); reflective and ablative counters, spinning; damage to the beam's own optics. Charged versus neutral particle beams and their range limits | Laser-ablation propulsion and directed-energy literature, Atomic Rockets, CoaDE |
| **Exhaust and plumes** | The drive as a weapon and a hazard. Energy flux by distance and angle; neutron and gamma emission from fusion exhaust (D-T against aneutronic); magnetic nozzle divergence. Feeds the envelopes and the inspection protocols | Atomic Rockets drive pages, fusion propulsion studies (e.g. Daedalus, VISTA) |
| **Debris evolution** | How a cloud spreads and lingers: the debris shotgun behind the speed-limit envelopes, collateral near stations, Kessler cascades in busy orbits | Orbital-debris modelling (NASA ORDEM, ESA MASTER), fragmentation events (ASAT tests) |

## Tier 1: the ship as a machine

These decide what a ship *is*, and size the designer's numbers.

| Study | What it decides | Starting points |
| --- | --- | --- |
| **Heat rejection** | Usually the biggest mass driver. Radiator kinds (panels, heat pipes, liquid droplet, belt), specific mass against temperature (the T⁴ law). **Armoured radiators** (CoaDE's approach): thickness as an input, conduction along the fin (fin efficiency by thickness, conductivity and length), damage edge-on against face-on, and how a holed fin or a punctured coolant loop degrades. Heat sinks and stored coolant for burst loads, combat with radiators retracted, heat as a detection signature | Atomic Rockets heat-radiator pages, NASA radiator studies, CoaDE |
| **Power** | Fission, fusion, solar, RTGs and batteries: specific power, start-up and scram times, conversion (Brayton, Rankine, thermionic, MHD), what a damaged reactor does | Atomic Rockets power plants, NASA SP-100 and Kilopower |
| **Propulsion survey** | The drive blocks from chemical to torch: thrust, exhaust velocity, specific power, waste heat, minimum size curves; propellant storage (cryogenic boil-off), drop tanks, staging | **The whole Atomic Rockets archive** (agreed), with primary sources it cites |
| **Structures** | Spine loading under thrust, specific strength of materials, long-structure vibration, docking and burn loads, the length limit at high g | Spacecraft structures texts, materials data |
| **Armour materials** | Density-led at hypervelocity, but the ballistic regime needs strength data; ceramics, composites, metals, ices and propellant as shielding; spaced layouts | Feeds from the impact study, materials handbooks |

## Tier 1: knowing and hitting

The two picture studies start from [`design/detection-and-the-picture.md`](../design/detection-and-the-picture.md), whose numbers are first-cut estimates for them to replace.

| Study | What it decides | Starting points |
| --- | --- | --- |
| **Detection and search** | The picture's first half. IR detection of hulls, radiators and plumes against the sky background by aperture, band and integration time; search rate (sky area per hour at a given depth) as distinct from sensitivity; solar exclusion and occlusion by bodies; clutter, especially asteroid confusion in the belt; the limits of stealth (cold coasting, heat sinks, directional radiators); plume spectroscopy for identifying drives, and for weighing a burning ship (jet power and exhaust velocity give thrust, the measured acceleration then gives mass); decoys | NEO Surveyor and NEOWISE sensitivity and survey simulations, IR astronomy detector data, Atomic Rockets "no stealth in space" |
| **Ranging, tracking and fusion** | The picture's second half. Bearing precision by centroiding; triangulation by baseline; angles-only orbit determination from short and long arcs (admissible regions); range by observer manoeuvre, including the free baseline of a sensor's own orbit; radar and lidar reach against cross-section and material; Doppler from plume lines; fusing reports of different ages under light-lag; track growth (the along-track banana, the burner's bloom); unresolved groups and count estimation | Milani's admissible regions and space-surveillance initial orbit determination, bearings-only target motion analysis, planetary radar (Goldstone), debris laser ranging |
| **Guidance and intercept** | Missiles and interceptors: Δv against target Δv, proportional navigation in space, terminal homing, fuzing (decisive for nukes), Lambert and Hill-frame intercepts, closing-speed geometry (retrograde swarms) | Missile guidance texts, ABM and ASAT test records |
| **Kinetic launchers** | Coilguns, railguns, mass drivers: muzzle velocity, efficiency, barrel and rail wear, recoil, power and heat a shot, rate of fire | Electromagnetic launch literature, Atomic Rockets |
| **Point defence and saturation** | Hit chances against missiles and clouds by weapon, engagement timelines inside the intercept window, saturation | Derived from the above; naval CIWS history as shape only |
| **Warhead conversion** | Nuclear shaped charges (Casaba-Howitzer), bomb-pumped X-ray lasers (Excalibur), antimatter storage and containment failure, all as burst blocks | Atomic Rockets, declassified Project Orion and Casaba-Howitzer material |

## Tier 1: inside the ship (Fleetwright's flooding and fire)

| Study | What it decides | Starting points |
| --- | --- | --- |
| **Radiation and the crew** | Dose from the environment (GCR, solar particle events, the belts), from the ship's own reactor and drive (shadow shields), and from weapons; acute effects and their timelines (when a dosed crew stops working) | NCRP and NASA radiation limits, acute radiation syndrome data |
| **Electronics vulnerability** | Total dose, single-event upsets, X-ray and neutron thresholds, hardening and its cost | Radiation-hardening literature, nuclear effects testing |
| **Internal damage** | Decompression through holes (orifice law, as Fleetwright's flooding), fire in spacecraft atmospheres (pressure and O₂ share), coolant and propellant leaks, cryogenic tank rupture, loss of attitude control and tumbling, a damaged reactor | Spacecraft fire research (ISS, Apollo 1), pressure-vessel data |
| **Damage control and repair** | What crews can patch in a pressure suit, how fast; spare parts; Fleetwright's repair parties as man-minutes | Spaceflight EVA and repair records |
| **Crew and acceleration** | Sustained g tolerance by duration and posture, crash couches, what high-thrust combat does to a crew | Aerospace medicine data |

## Tier 2: the living solar system (after the battler)

| Study | What it decides |
| --- | --- |
| **Ephemerides and bodies** | Orbits, masses, spheres of influence and moons from JPL data; the epoch as a constant |
| **Transfers** | Δv maps, launch windows, transfer times by drive: the deliverable-force model |
| **Resources** | Composition by asteroid class and body, volatiles, the extraction cost curves |
| **Industry in space** | ISRU, bootstrap ratios, what can't be made locally (chip fabs, fusion components): the dependency ladder's data |
| **Research and engineering** | Development cost and time curves, learning curves (Wright's law): how engineering improves a block's numbers continuously |
| **Economics** | Launch and transport costs, the value of mass in each place |
| **Habitats and population** | Spin gravity, life support, growth, what colonists need |
| **Space law** | The Outer Space Treaty, registration (the "type" label inspectors read), the bans on nuclear weapons in space, liability: the starting rules polities break |
| **Historical analogues** | Chartered companies (EIC, HBC, VOC): governance, charter revocation, independence cases (USA, Latin America, the Dutch Revolt), the Cod Wars and gray-zone practice. Shapes only, not numbers |

## Order

1. **The Atomic Rockets survey** first. It sets the battler's range and gives the base points every other Tier 1 study needs.
2. **The effects:** impacts, bursts, beams and plumes. Everything that fights reads these.
3. **The ship as a machine:** heat, power, structures and armour, so the designer has real numbers.
4. **Knowing and hitting, then inside the ship.**
5. **Tier 2** when the living solar system starts.
