# Beamed Energy – Power Beaming, Beam-Driven Launch and Cislunar Uses

Nov 10, 2026 · @Teemu · first cut

A survey of moving energy by beam instead of by wire or fuel tank: microwave and laser launchers, laser ablation, beamed power to rovers, satellites and tugs, and space solar power. It asks how realistic the KSP Interstellar picture is (an orbital microwave emitter heating a launcher's propellant), finds the physics that caps each system, and lists what has actually flown or been tested as of November 2026. It complements [Mass Drivers](mass-drivers-throwing-catching-and-bulk-logistics.md) (throwing mass) and card 6 of the [Drive Survey](drive-survey-concepts-ranges-and-minimum-sizes.md) (beamed thermal drives). Numbers marked *(calc)* were computed for this doc; the rest come from the sources at the end.

## The short version

- **The idea is real; the scale is the catch.** Microwave-thermal and laser-thermal rockets are sound physics, studied since the 1970s and tested at small scale: a helium thruster above 500 s in 2015, heat-exchanger tubes above 2,000 K in 2013, a laser lightcraft to 71 m in 2000. Nothing has reached orbit.
- **Launch needs megawatts per kg of payload, for a few minutes.** About 1–2 MW of grid power per kg for large rockets *(calc; Parkin: under 1 MW/kg)*, rising to 10–20 MW per kg for 100 kg-class rockets (Parkin). Energy is cheap (~150–200 kWh per kg of payload, a few tens of dollars). Peak power is the cost: a 100 kg payload needs a facility of a few hundred MW to ~2 GW.
- **Diffraction decides who can talk to whom.** Spot size ≈ 2.44 λR/D. A 2.45 GHz beam from a 10 m dish in LEO makes a 12 km spot on the ground *(calc)*. A small dish in orbit beaming microwaves to a rocket, as in many games, cannot work. Launch beams need millimetre waves or light, ground arrays of hundreds of metres, or a chain of stations downrange.
- **The atmosphere caps microwave launch from below.** Air breaks down into plasma at only ~7 MW/m² near 43 km altitude at 10 GHz, and the ceiling rises roughly with frequency squared. That is why microwave launch designs use 94–140 GHz, not the 2.45 GHz of power satellites.
- **In vacuum, lasers win everywhere.** A 1 m laser optic covers a satellite's solar array at 1,000 km; a 5–12 m optic at Earth–Moon L1 covers a lunar base *(calc)*. Microwaves need kilometre apertures at the same ranges.
- **The receiver's waste heat is the real limit in space.** A passively cooled photovoltaic receiver takes only ~2–5 suns before it overheats *(calc)*. Above that, the radiator is the receiver's mass.
- **End-to-end efficiency is modest.** Microwave DC-to-DC can reach ~50–65 %; laser wall-plug to electric is ~15–30 % today. Beamed thermal propulsion skips the electrical conversion at the receiver.
- **Cislunar is where beamed power earns its keep first:** power into permanently shadowed craters and through the 14-day lunar night, power-sharing between satellites, laser debris nudging and beam-fed tugs. Two companies (Star Catcher, Volta Space) are building toward this now; on-orbit demos were planned for 2026.
- **Every beam station is a weapon** ([Drives, Point Defence and Kirklin Mines](drives-point-defence-and-kirklin-mines.md), [Weapons Sweep](weapons-sweep-missed-concepts.md)). A launch laser is a long-range gun pointed upward.

## How realistic is the KSP Interstellar picture?

The core loop (a power plant somewhere else, a beam, a receiver that heats propellant) is good physics. Kevin Parkin's microwave thermal rocket and Jordin Kare's laser heat-exchanger rocket are exactly this. Where game versions usually stretch:

| Game shortcut | Real constraint | Fix |
| --- | --- | --- |
| A modest dish in orbit beams to a rocket | 2.45 GHz from a 10 m dish spreads to ~12 km at 400 km *(calc)* | Ground arrays of 100–1,000 m at 94–245 GHz, or lasers |
| The emitter is in orbit | An orbiting emitter is overhead for minutes per pass; it also has to be powered by GW of space solar | Put the emitter on the ground near the launch site, on a high, dry mountain; add stations downrange |
| Any frequency through the air | Water vapour absorbs millimetre waves; rain kills them; air breaks down above a few MW/m² at low frequency | 94 and 140 GHz windows; launch on dry days; higher frequency raises the breakdown ceiling |
| Kilowatts launch tonnes | ~1–20 MW per kg of payload, less for bigger rockets | GW-class facilities for tonne payloads |
| Receivers are small parts | Receiver area sets how much power you can take; at launch the heat exchanger is most of the vehicle's underside | Model receiver area and its heat limit |
| Relays are free | Each relay is a large precision mirror; DARPA only began relay tests in 2025 | Relays cost aperture and pointing; a few % loss each |

Laser ablation launch is also real. It is a chemical-rocket-like engine whose energy arrives by beam; Phipps' relation (below) ties its thrust per watt to its exhaust speed.

## The physics that sets every limit

### Diffraction: spot size and capture

- **Spot diameter (first null):** d ≈ 2.44 λ R / D, for wavelength λ, range R and transmit aperture D.
- **Capture efficiency (Goubau):** τ = √(A_t A_r) / (λ R); fraction captured ≈ 1 − e^(−τ²). τ = 1 catches 63 %, τ = 1.5 catches 89 %, τ = 2 catches 98 %.
- **The aperture product is the price of the link.** For τ = 2, √(A_t A_r) = 2λR. Range and wavelength trade one for one against area.

Spot sizes *(calc)*:

| Link | λ | Range | Transmitter | Spot |
| --- | --- | --- | --- | --- |
| Microwave dish in LEO to ground | 12.2 cm (2.45 GHz) | 400 km | 10 m | 12 km |
| Power satellite, GEO to ground | 12.2 cm | 35,800 km | 1 km | 10.7 km |
| Lunar orbit to surface, microwave | 5.2 cm (5.8 GHz) | 100 km | 10 m | 1.3 km |
| Ground array to rocket | 3.2 mm (94 GHz) | 100 / 300 km | 100 m | 8 / 23 m |
| Satellite to satellite, laser | 1.06 µm | 1,000 km | 1 m | 2.6 m |
| Lunar orbit to surface, laser | 1.06 µm | 100 km | 0.1 m | 2.6 m |
| Earth–Moon L1 to lunar surface | 1.06 µm | 58,000 km | 1 / 5 m | 150 / 30 m |
| Earth (or Earth orbit) to Moon | 1.06 µm | 384,000 km | 10 m | 99 m |
| Crater-rim tower into a crater | 1.06 µm | 5 km | 0.5 m | 3 cm |

Equal apertures needed for 98 % capture (τ = 2) *(calc)*:

| Link | Each aperture |
| --- | --- |
| 2.45 GHz from GEO | 3.3 km |
| 5.8 GHz from GEO | 2.2 km |
| 94 GHz over 300 km | 49 m |
| 1.06 µm over 100 km | 0.5 m |
| 1.06 µm over 1,000 km | 1.6 m |
| 1.06 µm, Earth–Moon L1 to surface | 12.5 m |
| 1.06 µm, Earth to Moon | 32 m |
| 1.06 µm over 0.5 AU (Earth–Mars, close) | 450 m |
| 1.06 µm over 1 AU | 640 m |

**Read:** microwaves are a short-range or giant-aperture technology. Lasers reach the Moon with telescope-class optics. Beyond cislunar space, even lasers need hundreds of metres; that is the laser-sail and relay-web regime.

### Pointing

Jitter σ adds a spot of about R σ: 1 cm at 100 km for 0.1 µrad, 38 m at the Moon *(calc)*. Sub-microradian pointing is demonstrated for laser communications. For a moving rocket, tracking through the atmosphere is the hard part, and NASA's 2024 debris-laser review lists acquisition and handover as unproven.

### The receiver's heat

What the receiver doesn't convert, it must radiate.

- **Passive photovoltaic receiver** *(calc)*: a two-sided panel at 350 K rejects ~1.5 kW/m². With 50–60 % cell efficiency it takes ~3–4 kW/m² of laser, about **2–3 suns**, and delivers ~1.5–2.3 kW/m² of electricity. At 400 K, ~4–5 suns. Cells lose efficiency as they warm, so hotter is not free.
- **Above that, the radiator is the receiver.** Concentrated beams onto small cells need a pumped loop and a radiator sized for the waste heat, which brings back the radiator mass laws of the [Ship Generator](../design/ship-generator-slots-and-physical-model.md).
- **Thermal receivers** dodge this: the heat *is* the product. A heat exchanger or absorbing propellant takes MW/m² because the propellant carries the heat away.
- **Star Catcher's tests** delivered 1–10 suns onto unmodified solar panels: the upper end is about where passive panels top out.

### Efficiency chains

| Stage | Microwave | Laser |
| --- | --- | --- |
| Electricity → beam | Magnetron or solid-state 70–85 %; gyrotron ~50 % | Diode lasers 50–70 %; fibre lasers 30–50 % |
| Beam → receiver | 90–98 % if apertures are sized (τ ≥ 2); spillage often 25 % at launch | 70–95 %, set by aperture, atmosphere and jitter |
| Receiver → electricity | Rectenna 80–85 % at 2.45–5.8 GHz, lower at mm-wave | Tuned PV: 68.9 % record (GaAs, 858 nm); 55 % multijunction at 1,070 nm |
| End to end | ~50–65 % best case *(calc)*; SPS studies assumed ~50 % | ~15–30 % *(calc)*; DARPA measured >20 % laser-out to electric |

**Basis:** the cell records are demonstrated; whole-system numbers are studied. Brown's JPL–Raytheon 1975 test moved 30 kW over about 1.6 km, at only about 10 % end-to-end.

### The atmosphere

- **Microwave breakdown.** Free electrons accelerated by the beam ionise air. Parkin's calculator puts the minimum breakdown intensity at **~6.8 MW/m² near 43 km for 10 GHz**, and the plasma then reflects the beam. Higher frequency raises the limit. A rough f² scaling *(calc, physics-only)* gives ~0.4 MW/m² at 2.45 GHz, ~0.6 GW/m² at 94 GHz and ~1.3 GW/m² at 140 GHz. A launch heat exchanger needs a few MW/m² *(calc: 60 MW onto ~15 m² for a 100 kg payload)*, so **2.45 GHz launch beams fail in the stratosphere; mm-waves clear it**.
- **Absorption and weather.** Below ~35 GHz the beam tolerates weather. The 94 and 140 GHz windows are clear on dry days at high sites; clouds and rain block them. Lasers are blocked by cloud outright and need adaptive optics against turbulence; high-power CW beams also bloom (the air they heat defocuses them).
- **Safety.** The 1970s power-satellite beam peaked at 23 mW/cm² (230 W/m²) at the rectenna centre. UK Space Solar sizes its apertures so the beam cannot exceed ~245 W/m², a quarter of sunlight. Launch beams are millions of times brighter and need cleared airspace; Parkin notes the beam is ~1,000 times weaker at bird altitudes than at the rocket.

## Launch and lift methods

### Beamed thermal: microwave and laser heat-exchanger rockets

A beam heats a heat exchanger; hydrogen (or methane, ammonia, water) flows through it and out a nozzle. It is a nuclear thermal rocket whose reactor stays on the ground.

- **Exhaust speed is set by temperature:** ve ≈ 8.83 km/s × √(T / 2,726 K) for hydrogen (the NTR law from the Drive Survey). At 2,000 K: ~7.6 km/s (~770 s); at 2,500 K: ~8.5 km/s (~860 s) *(calc)*. Parkin targets >2,000 K with slush hydrogen, >1,500 K with ammonia or methane.
- **Payload fraction:** Parkin claims 3–12 times the payload of a chemical rocket of the same size. A first-cut sizing (9.4 km/s, tanks 15 % of propellant) gives ~18–23 % payload with hydrogen *(calc)*.
- **Power per kg of payload** *(calc: thrust-to-weight 1.5, 50 % beam-to-jet, 75 % beam capture, 50 % wall-plug)*: ~0.6 MW of beam at the vehicle and ~1.5 MW from the grid. Parkin: ~10 MW per kg for the smallest rockets, under 1 MW per kg for the largest.
- **Energy per kg of payload:** ~160 kWh from the grid *(calc)*, against 32 MJ (~9 kWh) of orbital energy in the payload itself. Parkin estimates $10–100 per kg in electricity.
- **Throughput is a capital question.** By the first-cut sizing a 100 MW facility launches ~60 kg per shot; Parkin's own page quotes ~2 GW from the grid for ~100 kg, so small rockets do far worse than the ideal. Ascent takes 3–6 minutes, so the plant can store energy between shots and fire often.
- **Range kills small arrays.** For 89 % capture onto a 5–20 m² heat exchanger *(calc)*:

| Frequency | 100 m array | 300 m array | 1 km array |
| --- | --- | --- | --- |
| 35 GHz | 15–31 km | 46–93 km | 154–308 km |
| 94 GHz | 41–83 km | 124–249 km | 414–828 km |
| 140 GHz | 62–123 km | 185–370 km | 617–1,234 km |
| 245 GHz | 108–216 km | 324–648 km | 1,080–2,160 km |

A rocket reaches orbit several hundred km downrange. So a real facility is a **large array or a chain of stations along the ground track**. Parkin cites ~100 m for modern microwave directors and ~1 m per beam module for lasers; he accepts up to 25 % spillage.

- **Laser version (Kare, 1990s):** the same heat exchanger under a laser. Lasers hit the vehicle from far further away (3 m optic: 0.9 m spot at 1,000 km), but cost $100–1,000 per watt against $1–10 per watt for microwaves (Parkin's figures), and clouds stop them. Island One's summary lists propellant temperatures from 2,600 K (metal exchanger) to ~15,000 K (laser-absorbing hydrogen plasma).
- **Status:** heat-exchanger tubes above 2,000 K in a 110 GHz beam at DIII-D (Aug 2013); a small rocket to a few tens of metres (early 2014); Escape Dynamics' helium thruster above 500 s (2015). Escape Dynamics closed at the end of 2015 for lack of funding. **Studied; partially demonstrated.**

### Hotter propellant: absorbing plasmas and seeded gas

Absorb the beam in the propellant itself (seeded with carbon, or as a laser-sustained plasma) and the wall stays cooler than the gas. Gas at 5,000–15,000 K gives ~1,300–2,000 s and more; the Drive Survey's card 6 lists 20–40 km/s for seeded hydrogen plasma (studied). The limits are wall heat flux, radiation losses from the plasma and keeping the plasma stable. **Studied; physics-only at the high end.**

### Laser ablation propulsion

A pulsed laser vaporises a solid propellant (plastic, metal) on the vehicle; the plume is the exhaust.

- **The law:** C_m × v_e = 2 η, where C_m is thrust per beam watt and η the ablation efficiency (≤ 1, likely ≤ 0.5). So thrust per watt and exhaust speed trade directly *(Phipps)*.

| Isp | Thrust per MW at η = 1 | at η = 0.5 |
| --- | --- | --- |
| 200 s | 1,020 N | 510 N |
| 500 s | 410 N | 200 N |
| 1,000 s | 200 N | 100 N |
| 2,000 s | 100 N | 50 N |
| 5,000 s | 41 N | 20 N |
| Photon pressure (the floor) | 0.0067 N | — |

- **Isp above ~500 s needs pulsed lasers;** continuous lasers manage ~200 s. Up to 7,500 s has been measured (KrF laser on aluminium).
- **For Earth launch** it behaves like a chemical rocket fed by beam (~500 s), so it is no better than beamed thermal and needs more power per kg *(calc: ~2.4 MW wall-plug per kg)*.
- **Where it shines:** small impulses on things you don't own (debris, missiles; see below), and airless bodies.
- **Status:** studied; lab-demonstrated thrust; no orbital launch.

### Lightcraft (air-breathing pulsed laser)

A reflector on the craft focuses the pulsed beam into the air behind it, making a detonation that pushes the craft. Air is the reaction mass at low altitude; above it, an onboard ablator. **Record: 71 m in 10.5 s (October 2000, White Sands), from a 10 kW pulsed CO₂ laser,** spinning at >10,000 rpm for stability. Work moved to Brazil's hypersonic wind tunnels after Myrabo retired. **Demonstrated as a toy; orbit is studied only.** The 71 m flight is the most honest data point for "how far have laser launchers got".

### Beamed electric

Beam onto photovoltaic cells, power an electric thruster. High Isp, low thrust: **not a launch method** but the best tug. See cislunar uses below.

### Non-beam launch assist

Covered elsewhere; listed so the ladder is complete.

| Method | Reach | Basis | Where |
| --- | --- | --- | --- |
| Lunar mass driver | Lunar orbit and escape; <1 kWh/kg | Studied; 1976 hardware | [Mass Drivers](mass-drivers-throwing-catching-and-bulk-logistics.md) |
| Guns (HARP, SHARP) | 180 km altitude; ~3 km/s | Demonstrated | Mass Drivers |
| Centrifugal (SpinLaunch) | Suborbital, ~10,000 g | Demonstrated suborbital | Mass Drivers |
| Tethers, launch loops, orbital rings | Orbit with a second impulse | Studied | Mass Drivers; [Weapons Sweep](weapons-sweep-missed-concepts.md) |

### Launch comparison

| Method | ve | Wall-plug power per kg payload | Best site | Basis |
| --- | --- | --- | --- | --- |
| Microwave thermal (H₂, ~2,000–2,500 K) | 7.5–8.5 km/s | ~1–20 MW (Parkin) | Earth, high dry site | Partly demonstrated |
| Laser thermal (exchanger) | 7.5–9 km/s | ~1–3 MW at scale *(calc)*, costlier watts | Earth, clear sky | Studied |
| Laser plasma thermal | 13–40 km/s | Lower per kg, harder engine | Vacuum stages | Studied / physics-only |
| Laser ablation | 2–5 km/s typical | ~2–3 MW | Moon, small payloads | Lab |
| Lightcraft | Air-breathing, then ablator | — | Earth, small | 71 m flight |
| Lunar mass driver | Is the launcher | Tens of kW average, MW bursts | Moon | Studied |

*(Power column: first-cut calc or Parkin's range; treat as ±a factor of 2 at best.)*

## Beyond launch: cislunar and in-space uses

### Power into the dark

- **Permanently shadowed craters** hold the Moon's ice and never see sunlight. A laser on a sunlit crater rim reaches a rover 5 km away with a 3 cm spot from a 0.5 m optic *(calc)*. No atmosphere, no breakdown, no weather.
- **The lunar night** lasts ~14 Earth days. Batteries for that are heavy; a beam from orbit or from a sunlit peak replaces them.
- **Volta Space** is building a lunar constellation (three satellites initially) to beam laser power to surface assets; it demonstrated an 850 m link on Earth and planned a spacecraft-to-spacecraft demo in Earth orbit for 2026. Its seed investor estimates ~1 GW of total power need for announced lunar missions through 2035 (company claim).
- **From Earth–Moon L1:** a 5 m optic makes a 30 m spot on the surface; 12.5 m gives 98 % capture into a 12.5 m receiver *(calc)*. A single L1 station sees the whole near side.

### Satellite-to-satellite power

- **Star Catcher** collects sunlight in orbit and re-beams it, at wavelengths suited to solar cells, onto customers' existing arrays. On the ground it delivered **>1.1 kW of electrical power** (Kennedy Space Center, announced Nov 2025), beating DARPA's 800 W, including recharging Intuitive Machines' Lunar Terrain Vehicle. It raised $65M (May 2026), reports seven power purchase agreements, and planned its first on-orbit beaming demo for later in 2026.
- **Geometry** *(calc)*: a 1 m laser optic covers a 2.6 m spot at 1,000 km, so one power node serves a ring of clients within ~1,000 km. Passive arrays cap the useful flux at a few suns, so the gain is mostly **power through eclipse and power for undersized arrays**, not unlimited power.

### Beam-fed tugs

- **Beamed electric:** Brophy's NIAC study sized a 100 MW laser, a 175 m PV array and a 58,000 s lithium ion engine for 100–200 km/s missions (Phase II: 400 MW, 2 km array, 110 m PV). Its open questions are the cislunar ones too: PV over 50 % at the laser line, 200 g/m² arrays, high-voltage arrays in plasma.
- **Cislunar scale** *(calc)*: a 10 m laser optic at Earth–Moon distance gives a ~100 m spot, so a tug with a 30–100 m array can be fed anywhere on the LEO-to-lunar-orbit path from one station. The tug's array is lighter than a solar array of the same output only up to the passive heat limit (~2–5 suns).
- **Beamed thermal:** an NTR-class tug (~800–900 s) with no reactor. Thrust is higher than electric; the tug carries a heat exchanger and tanks. Good for crewed or time-critical cislunar hops; the station must track it through the burn.
- **Beam-fed landers on the Moon:** a lander heating lunar water gets only ~2.5–2.8 km/s *(calc, water at 2,000–2,500 K, rough)*. Lunar ascent (~1.9 km/s to low orbit) then needs a mass ratio of ~2.1 *(calc)*, all of it local water. With hydrogen made from that water, ~7.6 km/s and a mass ratio of ~1.3.

### Lunar launch: beam or driver?

- **A lunar mass driver** spends ~1.4 MJ/kg of kinetic energy to reach orbital speed, ~0.6 kWh/kg from the grid *(calc, 70 % efficient)*.
- **A beamed ascent** spends ~7–11 kWh per kg of payload *(calc)*, with vehicle, propellant and tracking on top.
- **So bulk goes by driver and people and fragile cargo go by beam or rocket.** Beams win on flexibility: any landing pad within line of sight, no track, gentle acceleration.

### Laser ablation on things you don't own

- **Debris removal (Phipps, ORION/L'ADROIT studies):** a 1.06 µm laser with ~7 kJ pulses, ~12 Hz (~80–90 kW average) and a 13 m mirror would nudge small debris by ~12 cm/s per shot, out to 1,000 km. About 150 m/s re-enters a target. All ~100,000 small objects in ~9 months; large objects at ~$1M each against ~$27M for deorbit kits (studied).
- **NASA OTPS (2024):** ground-laser remediation may be among the most valuable debris actions, but needs ~10 kJ, ~10 ns, ~10 Hz lasers (beyond today's state of the art), realistic test data on dirty, tumbling targets, and demonstrated find–fix–handover. A weak nudge can make things worse.
- **Same tool, other uses:** nudging an asteroid, deflecting a missile (a few m/s at 100 km is enough; [Drives, Point Defence and Kirklin Mines](drives-point-defence-and-kirklin-mines.md)), or nudging a rival's satellite. Dual-use by construction.

### Space solar power to Earth

| System | What | When | Basis |
| --- | --- | --- | --- |
| 1970s NASA/DOE reference | 2.45 GHz, ~1 km transmitter in GEO, ~10 km rectenna, peak 23 mW/cm², ~50 % end to end | 1978–86 studies | Studied |
| Caltech MAPLE (SSPD-1) | First beamed power from orbit, detected on the ground | June 2023 | Demonstrated (tiny power) |
| JAXA OHISAMA | 2 m² panel in a 400 km orbit, ~1 kW microwave test to receivers in Suwa | Planned 2026 | Planned |
| Aetherflux | Infrared laser from LEO to 5–10 m ground stations | Planned 2026 | Planned |
| Overview Energy | Wide, low-intensity near-infrared beam from a plane at 5 km; LEO demo by 2028, GEO by 2030 | Dec 2025 (airborne) | Demonstrated (airborne) |
| DARPA POWER | 800 W over 8.6 km, ground to ground, 30 s | May 2025 | Demonstrated |

*I could not confirm whether the OHISAMA, Aetherflux and Star Catcher 2026 on-orbit demos have flown as of Nov 10, 2026.*

Microwave power satellites face the diffraction table: a 2.45 GHz link from GEO wants ~3 km apertures. Lasers shrink the apertures but face clouds. **Power from space is a cislunar product long before it is an Earth product.**

### Relays and webs

DARPA POWER Phase 2 is testing integrated relays and vertical links. A relay is a large precision mirror that adds a few per cent of loss and a target to defend. The armed version of a relay network is the [Laser Weapon Web](weapons-sweep-missed-concepts.md).

## What ultimately limits each system

| Limit | Law | Where it bites | Can engineering beat it? |
| --- | --- | --- | --- |
| Diffraction | d ≈ 2.44 λR/D; τ = √(A_t A_r)/(λR) | Everything over distance; microwaves worst | Only by shorter λ or bigger apertures. X-ray beams ([Strategic Beams](strategic-beams-x-ray-and-gamma-fels.md)) are the end of the ladder |
| Optical figure and pointing | Surface error ≲ λ/20; spot grows by Rσ | Large laser optics; Earth–Moon links | Yes, slowly: active optics, phased arrays |
| Air breakdown | ~7 MW/m² minimum near 43 km at 10 GHz, rising ~f² | Microwave launch | Raise frequency (but absorption rises) |
| Atmosphere | Absorption, cloud, turbulence, blooming | All ground-to-space links | Partly: high dry sites, adaptive optics, site diversity |
| Receiver heat | Waste = (1 − η) × incident; passive ~1.5 kW/m² at 350 K | PV receivers in space | Only with radiators (mass) or thermal receivers |
| Thermal rocket temperature | ve ∝ √(T/M) | Heat-exchanger rockets ~2,000–3,000 K | Plasma absorption reaches 5,000–15,000 K; walls are the limit |
| Ablation trade | C_m × v_e = 2η ≤ 2 | Thrust per watt vs Isp | No: it's energy conservation |
| Photon pressure | F = 2P/c, 6.7 N per GW | Sails, the floor of every beam push | No |
| Power cost | ~1–20 MW per kg payload for launch | Launch rate | Capital: $/W of sources and arrays |
| Safety and law | e.g. ~245 W/m² by design for power satellites | Beams over people, airspace | Policy, not physics |

## Era ladder

The near, mid and far rows are projections for the game, not forecasts.

| Era | What exists | Typical numbers |
| --- | --- | --- |
| **Now (2025–26)** | kW-class ground laser links over km; sunlight re-beaming tests; first on-orbit demos planned | 0.8–1.1 kW; 8.6 km; 1–10 suns; >20 % efficient |
| **Near (2030s)** | Lunar laser power for crater rovers and night survival; satellite power nodes in LEO/GEO; first ground-laser debris nudging; small beamed-thermal sounding rockets | 10–100 kW links; 1–1,000 km; meter-class optics |
| **Mid (2040s–60s)** | MW-class beamed-thermal launch for small payloads; beam-fed cislunar tugs; L1 power stations; first MW space solar to Earth | 100 MW–1 GW facilities; 10–30 m optics |
| **Far** | GW launch farms; system-wide laser relay webs; laser sails and beam-riding magsails | GW–TW; 100 m–km optics; X-ray beams at the end |

## What this means for the game

These are hooks, not decisions:

- **Beam stations are infrastructure with a dual role.** A launch facility, a lunar power node and a debris laser are all long-range guns. They belong in the same blocks as weapons, with an intensity cap as a charter clause ([Weapons Sweep](weapons-sweep-missed-concepts.md)).
- **Power as a service.** A beam node sells kWh to ships and bases within its τ ≥ 1 footprint. Price and reach follow from aperture, λ and range, so no extra rules are needed. Whoever owns the node can cut a client's power (leverage, as the Drive Survey notes).
- **Launch beams are capital-bound.** Launch rate ≈ beam power ÷ (power per kg). Energy is a small cost; the $/W of sources and arrays is the large one. Weather windows make throughput stochastic at Earth sites, but not on the Moon.
- **Downrange chains.** A beamed-thermal launch site is a line of stations, not a point; each station is a vulnerability.
- **Detection:** a MW–GW beam is a lighthouse. Scatter off air, dust and the receiver makes it visible to sensors ([Detection and the Picture](../design/detection-and-the-picture.md)).
- **Mass ledger:** beamed thermal craft burn hydrogen, methane, ammonia or water, so beams create demand for volatiles, not fuel imports ([Mass Ledger](../design/mass-ledger-element-groups-and-conservation.md)).

## Open questions

- [ ] Should beamed launch be an Earth-side company asset at game start, or an early-era research goal? Real status suggests the latter (nothing past tens of metres).
- [ ] Model receiver capacity as area × heat limit, with a pumped-radiator upgrade? That keeps one law for PV, rectennas and thermal receivers.
- [ ] Is the microwave breakdown ceiling worth modelling, or just a rule that launch beams use mm-waves or light?
- [ ] Weather at Earth beam sites: per-site availability fraction, or skip?
- [ ] Price beam power per delivered kWh, or rent the beam per hour? The second exposes capital cost, which is the real constraint.
- [ ] Does the beam-relay web need its own study (relay loss, mirror mass, pointing), shared with the weapons side?
- [ ] Recheck the 2026 on-orbit demos (OHISAMA, Aetherflux, Star Catcher, Volta) when results are published.

## Sources

**Beamed thermal launch**
- Parkin Research, [Microwave Thermal Rockets](https://parkinresearch.com/?p=1850) (2015): temperatures, power per kg, costs, DIII-D test, 2014 flight.
- Parkin, [The Microwave Thermal Thruster and Its Application to the Launch Problem](https://thesis.library.caltech.edu/2405/) (Caltech PhD thesis, 2006).
- Parkin Research, [Microwave breakdown](https://parkinresearch.com/engineering-inference-engine/microwave-breakdown/): breakdown minimum near 43 km at 10 GHz.
- Wikipedia, [Escape Dynamics](https://en.wikipedia.org/wiki/Escape_Dynamics): 2015 thruster test, >500 s with helium; shutdown at the end of 2015.
- Satnews, [Escape Dynamics thruster test](https://satnews.com/2015/07/27/the-worlds-first-combustion-free-externally-powered-space-launch-thruster-successfully-tested-by-escape-dynamics/) (July 2015).
- Island One, [Laser rocket launcher (laser-thermal propulsion)](https://fennetic.net/mirrors/www.islandone.org/LEOBiblio/SPBI115.HTM): propellant temperatures by absorber.
- NASA NTRS, [Kare et al., laser launch studies](https://ntrs.nasa.gov/citations/19910012844) (1991).

**Laser ablation and lightcraft**
- Phipps et al., [Optimum parameters for laser ablation propulsion](https://www.photonicassociates.com/Optimum_parameters.pdf): C_m–Isp relation and table.
- Phipps et al., [Removing Orbital Debris with Lasers](https://arxiv.org/pdf/1110.3835) (2012).
- NASA OTPS, [Ground-Based Laser Debris Remediation TIM](https://ntrs.nasa.gov/api/citations/20240005687/downloads/2024%20-%20OTPS%20-%20Ground-Based%20Laser%20Debris%20TIM%20v3.pdf) (2024).
- Wikipedia, [Lightcraft](https://en.wikipedia.org/wiki/Lightcraft): 1997 and 2000 flights.

**Power beaming demonstrations and companies**
- DARPA, [Program sets distance record for power beaming](https://darpa.mil/news/2025/darpa-program-distance-record-power-beaming) (May 2025).
- Military & Aerospace Electronics, [Star Catcher claims new record for wireless optical power transmission](https://militaryaerospace.com/power/news/55327979/star-catcher-claims-new-record-for-wireless-optical-power-transmission-at-kennedy-space-center) (Nov 2025).
- VCA Online, [Star Catcher raises $65 million](https://www.vcaonline.com/news/2026051206/star-catcher-raises-65-million-to-build-the-first-power-grid-in-space/) (May 2026).
- Payload, [Volta Space wants to beam power to the Moon](https://payloadspace.com/volta-space-wants-to-beam-power-to-the-moon).
- pv magazine USA, [Volta Space Technologies laser-enabled lunar PV power network](https://pv-magazine-usa.com/2026/04/13/volta-space-technologies-leverages-government-partnerships-and-funding-to-develop-laser-enabled-lunar-pv-power-network/) (Apr 2026).
- New Atlas, [Aetherflux 2026 laser power demo](https://newatlas.com/energy/laser-beamed-space-solar-power-aetherflux-2026-test).
- PR Newswire, [Aetherflux announces orbital data center](https://www.prnewswire.com/news-releases/aetherflux-announces-orbital-data-center-targets-q1-2027-302635961.html) (Dec 2025).
- The Register, [Overview Energy airborne beaming](https://www.theregister.com/2025/12/11/spacepower_startup_beam_energy_solar_farms/) (Dec 2025).
- AL Circle, [OHISAMA: Japan's 2026 mission](https://www.alcircle.com/news/ohisama-japans-2026-satellite-mission-to-transmit-wireless-solar-energy-from-space-117374) (Feb 2026).
- POWER Magazine, [Space solar power prototype beams first power to Earth](https://www.powermag.com/space-solar-power-prototype-beams-first-power-to-earth/) (July 2023).
- Wikipedia, [Space-based solar power](https://en.wikipedia.org/wiki/Space-based_solar_power): reference system apertures, 23 mW/cm², Brown's 1975 test.

**Receivers and beamed electric**
- Fraunhofer ISE, [Record 68.9 % GaAs cell under laser light](https://www.materials.fraunhofer.de/en/press/ise---record-efficiency-of-68-9--for-gaas-thin-film-photovoltaic.html).
- [55 % efficient multijunction laser power converters for 1,070 nm](https://library.kab.ac.ug/Record/doaj-art-ad51d24be4fa4970993514cf76afaa83/Description).
- Centauri Dreams, [Laser beaming and infrastructure](https://www.centauri-dreams.org/2018/04/06/laser-beaming-and-infrastructure/) (Brophy's NIAC laser-electric study).

**Internal**
- [Drive Survey](drive-survey-concepts-ranges-and-minimum-sizes.md) (card 6 and the NTR ve law), [Mass Drivers](mass-drivers-throwing-catching-and-bulk-logistics.md), [Drives, Point Defence and Kirklin Mines](drives-point-defence-and-kirklin-mines.md), [Weapons Sweep](weapons-sweep-missed-concepts.md), [Strategic Beams](strategic-beams-x-ray-and-gamma-fels.md).
