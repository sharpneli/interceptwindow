# Jovian Beam Network – When Laser Stations Pay

Nov 10, 2026 · @Teemu · proposal, first cut

An initial design study: under what conditions would someone build reactor-powered laser stations and relay mirrors around Jupiter so that cheap, reactor-free tugs can ride the beams between the Galilean moons? It works out the Jovian Δv map, compares beam-fed tugs with tugs that carry their own power (fission, fusion) and with plain chemical tugs fed by water depots, and turns the result into economic conditions and a game model. It builds on [Beamed Energy](../studies/beamed-energy-power-beaming-launch-and-cislunar-uses.md), the [Drive Survey](../studies/drive-survey-concepts-ranges-and-minimum-sizes.md) and [Outward](outward-the-belt-jupiter-and-independence-from-earth.md). Figures marked *(calc)* were computed for this doc; costs are relative, not dollars.

## The short version

- **Beam networks beat reactors on every hull, easily.** An impulsive tug burns for ~1–3 hours per 12-day round trip, a duty cycle of ~1–2 % *(calc)*. A shared station working 30–60 % of the time can cost **15–60 times more per watt** than an onboard power plant and still win.
- **But the real rival is the chemical tug, and it is hard to beat.** Every Jovian hop is only ~1–2.5 km/s per burn, and water is everywhere. A LOX/LH₂ tug refuelled from local water needs no onboard reactor either, and its energy chain (electrolysis, ~60–70 %) is about three times as efficient as a laser chain (~20 %). On intra-Jovian hops the two use about the same energy per kg delivered *(calc)*.
- **So the network pays only where chemistry struggles.** Those places are:
  - burns above ~4–5 km/s (Io runs, leaving or entering the Jovian system, deep perijove work);
  - high-thrust kicks for low-thrust ships (nuclear-electric and fusion freighters climbing out of Jupiter's well);
  - landers and uncrewed tugs where cryogenics and crew-rated reactors are the expensive part;
  - high traffic, so that stations stay busy.
- **The traffic bar is a port's, not an outpost's.** A node station stays 30 % busy at ~5–15 burns a day, about **10⁵ t/yr of cargo per route** *(calc)*. That is the scale of the whole belt-to-cislunar water trade in [Interplanetary Bulk Logistics](../studies/interplanetary-bulk-logistics-mines-depots-and-shipyards.md). It is mid-to-late game.
- **Build nodes, not a web.** High-thrust burns happen near the moons, within ~30,000–50,000 km. A station with a 5 m optic reaches a 10–20 m tug receiver there *(calc)*. Links between moons need 20–60 m relay mirrors, so a relay web is a later upgrade.
- **Fusion strengthens the case rather than ending it.** Fusion engine mass scales as √P, so a 10–100 MW fusion tug carries ~7–21 t of engine *(calc)*. Big fusion plants are cheap per watt; small craft can't carry them. **A beam network is how small craft use fusion.** That gives the network a permanent niche if fusion arrives.
- **A station is a weapon by construction.** A 160 MW station with a 5 m optic puts ~10⁸ W/m², the combat placeholder intensity, on a target 3,000 km away *(calc)*. A natural monopoly with a gun: charters, regulation and seizure are the politics.
- **Verdict:** feasible with known physics; uneconomic early. It becomes worth building when a Jovian economy reaches ~10⁵ t/yr per route, when outbound and inbound interplanetary traffic gathers at a Callisto gateway, and when laser stations get within a few times the cost per watt of electrolysis plants.

## The map: Jovian Δv

Patched-conic Hohmann transfers between 100 km circular orbits, with no gravity assists *(calc)*:

| Route | Departure burn | Arrival burn | Total | Transfer | Window every |
| --- | --- | --- | --- | --- | --- |
| Ganymede – Callisto | 1.13 km/s | 0.99 km/s | 2.13 km/s | 5.8 d | 12.5 d |
| Europa – Ganymede | 1.08 | 1.10 | 2.18 | 2.6 d | 7.0 d |
| Io – Europa | 1.36 | 1.19 | 2.55 | 1.3 d | 3.5 d |
| Europa – Callisto | 2.15 | 1.60 | 3.75 | 4.7 d | 4.5 d |
| Io – Ganymede | 2.48 | 1.91 | 4.39 | 2.1 d | 2.4 d |
| Io – Callisto | 3.67 | 2.34 | 6.00 | 4.0 d | 2.0 d |

| Other legs | Δv |
| --- | --- |
| Surface to low orbit (Io, Europa, Ganymede, Callisto) | 1.85, 1.46, 2.00, 1.78 km/s |
| Callisto low orbit to a Saturn-bound departure (v∞ ≈ 5.6 km/s at Jupiter) | 3.56 km/s |
| Same from Ganymede | 4.21 km/s |
| Low-thrust spiral out of Jupiter from Callisto's orbit | ~8.2 km/s; 95 days at 0.001 m/s², 9.5 days at 0.01 m/s² |

What the map says:

- **Burns are small and frequent.** Most burns are 1–2.5 km/s, and windows open every few days. That favours high-thrust, refuel-at-every-stop tugs.
- **Landing costs as much as the hop.** Getting off Ganymede costs about as much as getting to Callisto. Surface mass drivers ([Mass Drivers](../studies/mass-drivers-throwing-catching-and-bulk-logistics.md)) take bulk uplift; people and fragile cargo need landers.
- **Io and the system's edge are the expensive ends.** Io runs and interplanetary departures are where exhaust speed starts to matter.
- **Gravity-assist tours** (as Galileo, Juno and Europa Clipper flew) cut these numbers a lot, but take weeks to months. They suit bulk, not passengers.

## The candidates

Propellant and stationary electric energy per kg of final mass, for one burn *(calc)*. Beam chain: laser 50 %, capture 85 %, beam to jet 50 % (~21 % end to end). Hydrogen costs ~240 MJ/kg to make (electrolysis at 70 % plus liquefaction).

| Tug | ve | 1.5 km/s: propellant / energy | 3 km/s | 5 km/s | Onboard power plant |
| --- | --- | --- | --- | --- | --- |
| Chemical LOX/LH₂ from water | 4.4 km/s | 0.41 kg / 12 MJ | 0.98 / 29 | 2.1 / 62 | None |
| Beam thermal, water (~2,500 K) | ~2.7 km/s | 0.74 / 14 | 2.0 / 37 | 5.4 / 98 | None |
| Beam thermal, hydrogen (2,500 K) | 8.4 km/s | 0.20 / 80 | 0.43 / 176 | 0.81 / 333 | None |
| Beam plasma thermal, water (dissociated, 5,000 K; physics-only) | ~6–7 km/s | ~0.26 / ~26 | ~0.59 / ~58 | ~1.2 / ~115 | None |
| Solid-core NTR, hydrogen | 8.8 km/s | 0.19 / 45 (H₂ only) | 0.41 / 99 | 0.77 / 186 | Fission core, 1.5–2.5 t |
| Fusion, afterburner (ve ~12) or pure (ve ~100+) | 12–300 km/s | small | small | small | 7–34 t at 10–270 MW jet |
| Fission-electric | 20–50 km/s | tiny | tiny | tiny | 450–2,250 t for 45 MWe |

Reading the table:

- **Chemical from water is the incumbent.** It has no reactor on board, the best energy chain, and mature engines; LOX keeps well in the Jovian cold. Its costs are electrolysis and liquefaction plants at every depot, liquid-hydrogen boil-off, and mass ratios that climb steeply above ~4–5 km/s.
- **Beam-water thermal is the simplest tug ever.** It is a water tank, a heat exchanger, a nozzle and a light concentrator, with no cryogenics, no turbopumps and nothing radioactive. It carries twice the propellant of a chemical tug and needs a beam station.
- **Beam-hydrogen thermal** halves the propellant but spends far more energy making hydrogen. It only pays on the big burns.
- **NTR is mass-light** (the core is ~1.5 t): its case is not mass. Against it, the beam wins on fissiles (imported from the inner system; [Outward](outward-the-belt-jupiter-and-independence-from-earth.md)), core cost per hull, crew dose and who is allowed to own reactors.
- **Fusion on small hulls is heavy and low-thrust.** At 81 MW of jet power a fusion engine is ~18 t and gives 0.008 m/s² on 200 t without an afterburner. Fusion belongs on big interplanetary ships.
- **Electric tugs are far too slow here.** A 10 MWe tug moving 500 t needs ~3 months per moon hop, against 6 days by Hohmann. They also crawl through the radiation belts.

## Economics

### Against onboard power: the duty-cycle law

A tug's onboard plant earns only while it burns. A station earns whenever any tug is burning near it.

- **Beam wins when:** c_onboard − c_receiver > (d / u) × c_station, all per watt delivered to the jet.
  - d: the tug's duty cycle (fraction of its life spent burning).
  - u: the station's utilization (fraction of its time beaming to a customer).
- **Jovian tugs:** four burns of 25–85 minutes per 12.5-day Ganymede–Callisto round trip gives d ≈ 0.006–0.018 *(calc)*.

| Tug duty cycle d | Station may cost (× onboard $/W), u = 0.3 | u = 0.6 |
| --- | --- | --- |
| 0.01 (impulsive tug) | 30× | 60× |
| 0.02 | 15× | 30× |
| 0.05 | 6× | 12× |
| 0.2 (busy electric tug) | 1.5× | 3× |
| 0.8 (always-on electric tug) | ~0.4× | 0.75× |

**Impulsive tugs and shared stations are a natural match. Continuous-thrust tugs gain little from beams except mass.** The installed station power is d/u of what a fleet of reactor tugs would carry in total, ~3–7 % for impulsive traffic.

### Against chemical: storage beats peak power

Both need a stationary plant at the node. The difference is when they need its power:

- **A chemical depot runs its electrolysers around the clock** and stores the energy as propellant.
- **A beam station delivers at burn time.** For the same annual energy, its lasers must be ~2–11 times the electrolysis plant's power, at u = 0.6–0.1 *(calc)*. A station can buffer its reactor's output (flywheels, batteries, thermal storage), but the lasers and optics are still sized for the peak.
- **So beam-water thermal ties with chemical on intra-Jovian hops only when installed lasers plus optics cost about u times what electrolysis plus liquefaction plus cryogenic storage cost per watt** (~0.3–0.6 ×). Today lasers cost one to two orders of magnitude more per watt than electrolysers (Parkin quotes $100–1,000/W for laser beam directors). That gap is the main technology gate.
- **Where chemistry falls behind anyway:**
  - burns above ~4–5 km/s, where LOX/LH₂ mass ratios pass ~2.5–3;
  - liquid hydrogen logistics at many small nodes;
  - tugs that must be cheap enough to lose (uncrewed, radiation-zone work).

### The traffic threshold

A station with a ~400 MWe laser bank (enough for a 200 t tug at 0.3 m/s²) *(calc)*:

| Station utilization | Burns per day per node | Round trips per day | Cargo per route (100 t a trip, one way) |
| --- | --- | --- | --- |
| 10 % | 2–5 | 1–3 | 3–10 × 10⁴ t/yr |
| 30 % | 5–16 | 3–8 | 1–3 × 10⁵ t/yr |
| 60 % | 10–31 | 5–16 | 2–6 × 10⁵ t/yr |

Shorter, harder burns (1 m/s²) need a bigger laser bank but serve more tugs a day. **Below a few × 10⁴ t/yr per route, stations idle and chemical depots win.**

### The economic factors

| Factor | Pushes toward the network when… | Pushes away when… |
| --- | --- | --- |
| Traffic density | Many burns per day per node (u ≥ 0.3) | Outpost traffic, a few ships a month |
| Burn size | Big burns: Io, the system's edge, perijove, interplanetary capture | 1–2 km/s moon hops |
| Laser and optics $/W | Within a few × electrolysis-plant $/W | Today's 10–100× gap |
| Onboard power cost and mass | Fission cores costly or restricted; fusion √P mass on small hulls | Cheap small reactors appear |
| Fissile supply | Fissiles imported from the inner system; few big cores burn them better than many small ones | Local fissiles or D-D fusion everywhere |
| Cost of capital | Cheap capital, anchor tenants, a charter monopoly (railway economics: high fixed, low marginal cost) | Expensive capital: Metzger's lunar model has finance at 73–82 % of cost ([Early Economy](early-economy-revenue-streams-and-the-growth-loop.md)) |
| Radiation | Uncrewed, simple, rad-hard tugs; thermal receivers shrug off doses that kill solar cells | — |
| Shared plant | The station's reactor also powers a base or a smelter, so beaming is a sideline | A dedicated reactor for beaming alone |
| Gateway traffic | Interplanetary ships arriving and leaving through Callisto | Little interplanetary traffic |
| Security | Owner wants a guarded chokepoint | Rivals or regulators won't allow a privately owned gun |

## Network architecture

### Stage 1: node stations (no relays)

One station per busy moon. It beams to tugs during the departure and capture burns near the moon.

| Placement | Range to burning tugs | Optics | Pros | Cons |
| --- | --- | --- | --- | --- |
| **Moon surface** (on the base) | 100–2,000 km | ~1 m | Shares the base reactor; ice shields it; cold ground and ice help with heat | Sees only part of each low orbit: short, hard burns or several stations along the ground track |
| **Moon L1/L2 halo** (Ganymede ~32,000 km, Callisto ~50,000 km) | 10,000–50,000 km | ~5 m | Sees the whole near-moon zone and long burns | Needs its own reactor and radiators in space |

Beam reach for a 5 m optic *(calc)*:

| Range | 1.06 µm spot | 0.53 µm spot | Capture into a 10 m / 20 m receiver (1.06 µm) |
| --- | --- | --- | --- |
| 10,000 km | 5 m | 2.6 m | ~100 % / 100 % |
| 30,000 km | 16 m | 8 m | 78 % / ~100 % |
| 50,000 km | 26 m | 13 m | 42 % / 89 % (at 0.53 µm: 89 % / 100 %) |

The tug's receiver is a light concentrator (a mirror or inflatable dish) that focuses the beam into the heat exchanger, as in Kare's design. A 10–20 m concentrator is cheap compared with a reactor.

### Stage 2: the Callisto gateway

Callisto is the natural first node:

- It is the base the Outward doc already picks (low radiation, ~0.1 mSv a day).
- It is the cheapest exit from the Jovian system (3.56 km/s to a Saturn-bound v∞, against 4.21 from Ganymede).
- It is where interplanetary traffic gathers.

Gateway services:

- **Departure and capture kicks for low-thrust ships.** A nuclear-electric or fusion freighter at 0.001–0.01 m/s² takes 10–95 days to spiral out of Jupiter. A beam-fed booster tug docks, pushes it through a ~3.5 km/s Oberth burn in hours, and returns.
- **Beam-fed landers** for Callisto's 1.8 km/s surface leg, where cryogenics on every lander is the pain.
- **Selling power by the beam-hour** to bases and to ships in eclipse behind Callisto or Jupiter.

### Stage 3: relays and a web

Linking nodes across 0.4–1.2 million km takes relay mirrors of ~33–57 m at 1.06 µm, ~23–40 m at 0.53 µm or ~16–28 m in the ultraviolet *(calc, 98 % capture)*. With relays, one large fusion or fission plant can feed several nodes, and low-thrust tugs can ride the beam between moons. This is the [Laser Weapon Web](../studies/weapons-sweep-missed-concepts.md) without the weapon role. Mid-to-late tech.

### Power source by era

| Era | Station power | Plant → beam | Notes |
| --- | --- | --- | --- |
| Fission | Brayton or Rankine reactors, 100 MWe–1 GWe; the base plant doubles as the beam plant | ~35 % × 50 % ≈ 17 % of reactor heat | Fissiles imported. A stationary plant's mass doesn't matter, so heavier, safer, cheaper designs work |
| Fusion | D-D or D-³He plants with direct conversion | ~60 % × 50 % ≈ 30 % (physics-only) | Deuterium from any water. Big plants beat small ones per watt, which is the network's long-run edge |

Waste heat dominates the station: a ~400 MWe laser bank fed by a fission plant rejects ~0.9 GW (~0.7 GW at the reactor, ~0.2 GW at the lasers) *(calc)*. A surface station can use the moon's cold ice as part of the heat sink; an orbital one needs the radiator mass laws of the [Ship Generator](ship-generator-slots-and-physical-model.md).

## Risks and politics

- **Single point of failure.** A station outage strands every beam tug at that node. Tugs fly abort-safe trajectories (a failed escape burn leaves an eccentric moon orbit, not a crash), and nodes need spare capacity or a second station.
- **Dual use.** A station is a combat laser within ~3,000 km (~10⁸ W/m² on a 1.5 m spot) and a sensor-killer out to 30,000 km (~10⁶ W/m²) *(calc)*. See [Weapons Sweep](../studies/weapons-sweep-missed-concepts.md) for intensity caps as a charter clause.
- **Natural monopoly.** One station per node; the owner sets the price of motion at that moon. Expect charters, rate regulation, nationalisation and sabotage. The station is a leverage point, as the Drive Survey says of laser thermal.
- **Light and heat.** The station and its beams are bright to sensors ([Detection and the Picture](detection-and-the-picture.md)): a node's traffic is public knowledge.

## Feasibility: when, if ever

| Phase | Jovian economy | Best tug | Beam network |
| --- | --- | --- | --- |
| First presence (a Callisto base, science at Europa) | 10²–10³ t/yr | Chemical from water; NTR for long hops | **No.** Stations would idle |
| Growing hub (Callisto industry, Ganymede mining, a Saturn waystation) | 10⁴ t/yr per route | Chemical; NTR | **Gateway only:** one Callisto station sharing the base reactor, kicking low-thrust interplanetary ships and powering landers |
| Mature Jovian economy | 10⁵ t/yr per route | Beam-water and beam-plasma tugs where laser $/W allows | **Node stations** at Callisto and Ganymede, later Europa (radiation-hard, remote) |
| Fusion era | Large | Fusion for interplanetary hulls; beam tugs for everything small | **Relay web** fed by a few big fusion plants; the network is how small craft use fusion |

**If ever:** yes, on known physics, but late. The gate is economic, not physical: traffic density and the cost per watt of lasers against electrolysers.

## Model proposal for Intercept Window

- **Beam station** is an installation block: reactor (or base plant tap), laser bank (peak watts), optic (aperture, λ), waste heat. Its reach and capture come from the Goubau law, so there are no range numbers in code.
- **Beam service** is a market at the node, priced per beam-hour or per delivered MJ. Utilization emerges from traffic; idle stations lose money. Owners can refuse service, which is a political act.
- **Beam tug** is a ship design with a receiver slot (concentrator area and heat-exchanger rating) and a propellant (water, hydrogen). Its burns are only possible inside a station's footprint, so route planning places periapsides in coverage.
- **Chemical depots stay the default.** The network has to win in the landed-cost price field ([Early Economy](early-economy-revenue-streams-and-the-growth-loop.md)), not by script.
- **Dual use is automatic:** the station's beam reads into the same deposition model as any weapon.

## Open questions

- [ ] Do we want gravity-assist tours as a cheap, slow bulk mode in the Jovian system? It would undercut both chemical and beam tugs for bulk.
- [ ] Laser $/W over the game's timeline: a tech curve, or a market price driven by production volume?
- [ ] Is beam-plasma thermal with water (~6–7 km/s) worth a block, or too speculative? It is the variant that beats chemical on big burns without making hydrogen.
- [ ] Surface or Lagrange stations first? Surface shares the base plant; Lagrange covers more of the burn zone.
- [ ] How much of a node's traffic is landers? If most of it is, surface stations plus mass drivers may be the whole answer.
- [ ] Should a station's beam intensity cap be a charter term from the start, to keep stations from being warships?
- [ ] Recheck the Δv map with assists and with real ephemerides from the [body catalogue](../studies/solar-system-body-catalogue.md).

## Sources

- [Beamed Energy – Power Beaming, Beam-Driven Launch and Cislunar Uses](../studies/beamed-energy-power-beaming-launch-and-cislunar-uses.md): diffraction, Goubau capture, efficiency chains, Parkin's $/W figures, Kare's heat-exchanger design.
- [Drive Survey](../studies/drive-survey-concepts-ranges-and-minimum-sizes.md): NTR ve law and floor, fusion mass law (65 kg/MW at 1 GW, m ∝ √P), fission-electric specific mass.
- [Outward](outward-the-belt-jupiter-and-independence-from-earth.md): Callisto as the base, radiation, fissiles from the inner system, HOPE study.
- [Interplanetary Bulk Logistics](../studies/interplanetary-bulk-logistics-mines-depots-and-shipyards.md): tug-and-container, depots, electric tug rates, trade-flow scale.
- [Early Economy](early-economy-revenue-streams-and-the-growth-loop.md): landed-cost price field, cost of capital.
- Moon masses, radii and orbits: standard values (JPL), as in the [body catalogue](../studies/solar-system-body-catalogue.md).
