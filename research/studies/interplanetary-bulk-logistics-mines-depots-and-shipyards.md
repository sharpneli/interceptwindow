# Interplanetary Bulk Logistics – Mines, Depots and Shipyards

Continuation of [`studies/mass-drivers-throwing-catching-and-bulk-logistics.md`](mass-drivers-throwing-catching-and-bulk-logistics.md). That doc covered throwing and catching; this one covers everything else: how bulk moves when there is no driver, what an asteroid mine does today and later, how a shipyard in a moon's orbit gets fed, and the general shape of freight in the interplanetary age. Numbers marked *(calc)* were computed for this doc; Δv-map values marked *(approx.)* are standard rounded figures from the mission-design literature.

## The short answer

- **Moving a tonne has four costs, not one:** propellant (set by Δv and exhaust velocity), vehicle time (capital tied up per trip), pipeline inventory (cargo in flight is unpaid stock), and windows (waiting for geometry). Games usually model only the first.
- **Fleet size follows Little's law:** vehicles = throughput × round-trip time ÷ payload per trip. Slow, efficient freight needs huge fleets and holds huge stock in flight.
- **Staging in space is the main lever.** Buy propellant at every node instead of carrying it. Depots turn one long rocket equation into several short ones.
- **A contemporary asteroid mine is a prospector, not a mine.** The best realistic design is still the 2012 Keck study: a 40 kW electric spacecraft that bags a ~500 t boulder and drags it to high lunar orbit over 6–10 years. Water for propellant near the Moon is the first product; metals to Earth come last, if ever.
- **A shipyard is mostly a propellant business.** For a yard in lunar orbit, the shuttles that bring material up burn 1–2 t of lunar propellant for every tonne they deliver *(calc)*. Hydrogen, not oxygen or metal, is the scarce input.
- **Cheap Earth launch competes hard near Earth.** ISRU wins by distance: modestly in cislunar space, decisively at Mars, the belt and the outer moons.
- **The far end looks like sea freight.** Bulk goes slow on low-thrust barge trains between hub depots; value-dense goods and people go fast; windows give the trade its seasons until torch drives make time, not Δv, the main cost.

## The four costs of moving a tonne

### Propellant

Delivered fraction of a self-propelled cargo, e^(−Δv/ve) *(calc)*:

| Δv | Plain steam, ve 3.5 km/s | Hydrolox, 4.4 | Dissociated steam, 6.4 (theoretical) | NTR or water electrothermal, 10 | Electric, 30 |
| --- | --- | --- | --- | --- | --- |
| 0.5 km/s | 0.87 | 0.89 | 0.92 | 0.95 | 0.98 |
| 1 km/s | 0.75 | 0.80 | 0.86 | 0.90 | 0.97 |
| 2 km/s | 0.56 | 0.63 | 0.73 | 0.82 | 0.94 |
| 3 km/s | 0.42 | 0.51 | 0.63 | 0.74 | 0.90 |
| 5 km/s | 0.24 | 0.32 | 0.46 | 0.61 | 0.85 |

- **Below ~1 km/s almost anything works,** including water pushing itself with crude solar-thermal steam.
- **Above ~3 km/s chemical freight loses most of its cargo** unless it refuels on the way.
- **Dissociated steam would make water-pushes-itself viable to ~3 km/s.** Vance et al. (2024) calculate that water heated by concentrated sunlight to ~4,000 K at 1 bar splits into atomic hydrogen and oxygen, which recombine in the nozzle and give a theoretical Isp of 643–659 s (ve ~6.3–6.5 km/s), better than hydrolox. That is analysis only, with no hardware test, no thrust figure and no system mass, and it relies on refractory carbides holding up at ~4,000 K. Atomic oxygen at that temperature is also highly oxidising (an inference here, not from the paper), which makes chamber life the real unknown.

### Vehicle time

Electric thrust per unit power is small: F = 2ηP / ve. At ve 30 km/s and 60 % efficiency, **1 MW gives 40 N** *(calc)*.

| Tug | Total mass moved | Days per km/s *(calc)* |
| --- | --- | --- |
| Keck asteroid retriever, 40 kW | ~520 t | ~3,700 |
| 1 MW electric tug | 500 t | 145 |
| 1 MW electric tug | 2,000 t | 580 |
| 10 MW electric tug | 2,000 t | 53 |

- **Low-thrust freight is propellant-cheap and time-expensive.** The power plant is the costly part, so it should never wait: tugs drop containers and leave, like a locomotive leaving its wagons.

### Pipeline inventory and fleet size

| Case | Throughput | Round trip | Payload | Fleet *(calc)* | Stock in flight *(calc)* |
| --- | --- | --- | --- | --- | --- |
| Belt water to cislunar, electric tugs | 100,000 t/yr | 3 yr | 500 t | 600 tugs | 150,000 t |
| Lunar shuttle to orbit yard | 30,000 t/yr | ~1 week | 50 t | ~12 landers | ~150 t |

- **Carrying cost** on cargo worth $1,000/kg at destination, 5 % a year *(calc)*: $25/kg for 6 months, $105/kg for 2 years, $490/kg for 8 years. Slow freight only makes sense for cheap bulk.
- **Pipeline length cuts both ways in a blockade.** A blockade at the nodes bites only after the in-flight stock and the stockpile are used up. But the in-flight stock is itself exposed for the whole transit, and a raider can destroy it, divert it or seize it. That cuts supply at once and may hand the raider a prize (see Vulnerability).

### Windows

Synodic period (time between identical alignments) and Hohmann transfer time *(calc, circular coplanar orbits)*:

| Route | Synodic period | Hohmann transfer |
| --- | --- | --- |
| Earth–Venus | 1.6 yr | 146 d |
| Earth–Mars | 2.1 yr | 259 d |
| Earth–Ceres | 1.3 yr | 472 d |
| Earth–Jupiter | 1.1 yr | 2.7 yr |
| Earth–Saturn | 1.0 yr | 6.0 yr |
| Mars–Ceres | 3.2 yr | 574 d |
| Ceres–Vesta | **17.2 yr** | 750 d |
| Jupiter–Saturn | 19.9 yr | 10 yr |

- **Bodies at similar distances are far apart in time.** Ceres and Vesta line up for a cheap transfer once every 17 years. Belt-internal trade runs on hubs and continuous low thrust, not direct Hohmann hops.
- **Inclination is hidden Δv.** Ceres sits at about 10.6°, Pallas at about 35°; neither shows in the coplanar numbers.
- **Typical relative speeds between random belt objects are around 5 km/s,** the belt's average collision speed. The belt is not a dense neighbourhood.

## Where things are: Δv

### Earth–Moon space *(approx.)*

| Leg | Δv |
| --- | --- |
| Earth surface → LEO | ~9.4 km/s |
| LEO → trans-lunar injection | ~3.1–3.2 |
| LEO → NRHO (direct) | ~3.5–4 |
| LEO → Earth–Moon L1 | ~3.8 |
| LEO → GEO | ~3.9 |
| Lunar surface → LLO | ~1.9 |
| LLO ↔ NRHO | ~0.7–0.8 |
| Lunar surface ↔ NRHO | ~2.6–2.8 |
| Lunar surface → Earth–Moon L1 | ~2.5 |
| Best near-Earth asteroids → high lunar orbit (lunar flyby capture) | ~0.1–0.2 (Keck study: 160 m/s for 2008 HU4) |

### Interplanetary *(calc, Hohmann, no aerobraking, 300 km departure orbit)*

| Route | Departure burn | Capture to low orbit |
| --- | --- | --- |
| Earth → Mars | 3.6 km/s | 2.1 (or ~0 with aerocapture) |
| Earth → Vesta | 4.5 | 4.2 |
| Earth → Ceres | 4.9 | 4.6 |
| Mars → Ceres | 2.4 | 2.5 |
| Earth → Jupiter | 6.3 | aerocapture or a moon flyby; propulsive capture is large |

- **Mars is closer to the belt than Earth in Δv.** Zubrin's "triangle trade" argument (Earth sells high tech to Mars, Mars sells bulk and low-tech goods to the belt) rests on this.

### Moons and small bodies: surface to low orbit *(calc, orbital speed at the surface, no losses)*

| Body | Orbital speed | Escape | Local feedstock |
| --- | --- | --- | --- |
| Moon | 1.68 km/s | 2.38 | Oxygen and metals everywhere; water ice only in polar shadows |
| Phobos | 8 m/s | 11 m/s | Probably carbon-rich rock; water uncertain |
| Deimos | 4 m/s | 6 m/s | Similar to Phobos |
| Ceres | 0.37 | 0.52 | Ice, salts, clays, carbon |
| Enceladus | 0.17 | 0.24 | Almost pure ice |
| Europa | 1.43 | 2.03 | Ice; extreme radiation |
| Callisto | 1.73 | 2.44 | Ice and rock; low radiation for the Jovian system |
| Ganymede | 1.94 | 2.74 | Ice and rock; heavy radiation |
| Titan | 1.87 | 2.64 | Hydrocarbons, ice, nitrogen; thick atmosphere |

## The toolkit when there is no mass driver

| Mode | ve or effect | Strength | Weakness | Era |
| --- | --- | --- | --- | --- |
| **Chemical with local propellant** (hydrolox, methalox, LOX + imported fuel) | 3.5–4.5 km/s | High thrust; landers and short hops | Needs propellant at both ends | Now |
| **Solar-thermal water** (TransAstra's Omnivore concept; Vance et al. 2024) | ~3.5 km/s plain steam (engineered number); 6.3–6.5 km/s theoretical with dissociated steam at ~4,000 K | Propellant is the cargo; no power plant; unpurified water works | Needs sunlight (the paper keeps Isp to ~2.8 AU by cutting flow, so thrust falls); 4,000 K chamber unproven | Near (plain), mid (dissociated) |
| **Electric tug** (solar, later nuclear) | 20–50 km/s | Tiny propellant bill | Slow; costly power plant; slow through radiation belts | Now, small |
| **Nuclear thermal** | ~9 km/s | Doubles chemical ve, high thrust | Reactor politics, hydrogen storage | Mid |
| **Aerocapture and aerobraking** | Free Δv at bodies with air | Earth, Mars, Venus, Titan arrivals | Heat shield per cargo; not at the Moon or belt | Near |
| **Gravity assists and low-energy capture** | Hundreds of m/s saved | Lunar flyby capture of asteroid cargo | Adds months; geometry-bound | Now |
| **Sails** | No propellant | Light, slow, standing freight | Low thrust per area, falls with 1/r² | Mid |
| **Cyclers** | Heavy mass stays in a repeating orbit | Shielded habitats for people | Cargo must still match speed at both ends | Mid |
| **Tethers** | Momentum exchange | Cheap repeated pickups | Needs balanced traffic | Mid–far |
| **Fusion torches** | 100s–1,000s of km/s | Windows stop mattering | Physics-heavy | Far |

Two principles run through all of them:

- **Depots.** Never carry propellant you could buy at the next node. A route Earth → Mars → Ceres that refuels in high Mars orbit pays two short rocket equations, not one long one. In-space cryogenic transfer is still unproven at scale: the first Starship ship-to-ship demonstration was planned for no earlier than late 2026, and a crewed lunar landing is estimated to need about ten tanker flights.
- **Tug plus container.** The drive and power plant are the expensive part; cargo is a dumb can. Tugs push trains of standard containers and drop them, so the expensive part keeps moving. This is the space version of river barges.

## A contemporary asteroid mine

### Where things stand in late 2026

- **AstroForge** lost contact with its first deep-space craft, Odin, soon after its early-2025 launch. Its second, DeepSpace-2 (~200 kg, under $10.5M including launch), was scheduled for Q4 2026: a lunar flyby, ~9 months to one of ~28 candidate metal-rich asteroids, then imaging and possibly a landing or impact. The long-term aim is platinum-group metals for Earth.
- **Karman+** raised $20M for a 2027 demonstration of rendezvous and material extraction; its stated product is asteroid water to refuel satellites, as water or split into hydrogen and oxygen.
- **TransAstra** proposes optical mining: concentrated sunlight spalls a bagged asteroid, volatiles are collected, and its Omnivore solar-thermal thruster runs on the harvested water and other volatiles. Mini Bee (250 kg) is the demonstrator; Honey Bee and Queen Bee would take ~10 m and ~40 m bodies.
- **Nobody has yet mined anything.** The sample-return record is grams (Hayabusa2, OSIRIS-REx).

### The reference design: Keck asteroid retrieval (2012)

- **Target:** a ~7 m near-Earth asteroid, 250–1,000 t, ~500 t headline.
- **Vehicle:** 40 kW solar electric, Isp 3,000 s, 5.5 t dry, ~12–13 t xenon, one Atlas V-class launch (~18 t to LEO).
- **Capture:** an inflatable bag ~10 m long and ~15 m across, cinched shut; de-spin by thrusters.
- **Timeline:** 1.6–2.2 years spiralling out of LEO, ~2 years to the asteroid, ~90 days there, 2–6 years back. **6–10 years total.**
- **Return:** a lunar flyby captures the asteroid into a stable high lunar orbit at almost zero extra Δv. For 2008 HU4 the return leg needed only ~160 m/s.
- **Leverage:** ~28 kg returned per kg launched, up to ~70 with more time or power.
- **Cost:** ~$2.6B for the first mission, ~$1B for each repeat.
- **Yield:** a 500 t carbonaceous body might hold ~100 t water, ~100 t carbon compounds, ~90 t metals and ~200 t silicates.

### What a 2030s mine actually does

1. **Pick the target for return Δv and windows, not grade.** The cheapest asteroids have Earth-like orbits, so they come back to cheap alignments only every decade or more. A mine works a catalogue of targets in rotation.
2. **Bag the whole body or a boulder.** A bag is a container, a dust shield and a processing vessel at once.
3. **Process on the way home.** Heat the bag (sunlight or waste heat) and freeze out water. The years in transit are the refinery's residence time.
4. **Pay for the trip with the cargo.** Part of the water feeds the thrusters (solar-thermal or water-fed electric).
5. **Deliver to a stable high lunar orbit or a distant retrograde orbit.** Sell water as propellant and shielding; keep the carbon and nitrogen, which the Moon lacks.

**Economics against Earth launch.** If heavy launch to LEO costs ~$100/kg, putting a tonne in NRHO costs roughly 2.7 tonnes of LEO mass for chemical transfer *(calc)*, so ~$270/kg plus tug costs. 100 t of water is then worth tens of millions of dollars, against ~$1B per Keck-style mission. A first asteroid mine pays only if:

- vehicles become cheap and reusable, so a mission costs tens of millions rather than billions;
- Earth launch capacity, not price, becomes the limit; or
- the material is needed far from Earth, where Earth competes worse.

**Metals for Earth are the worst business.** World platinum supply is under ~200 t a year; a single large return would crash the price it was counting on.

## Later asteroid mining

| Stage | What changes | Logistics |
| --- | --- | --- |
| **1. Prospector-retrievers** (2030s–40s) | Keck-class bags, ~10²–10³ t per return | Single vehicles, years per trip, delivery to high lunar orbit |
| **2. Resident mines** | Processing at the asteroid; local water fuels the tugs | Shuttle tugs carry product containers to cislunar depots; the mine does not move |
| **3. Belt hubs** | Ceres or a large C-type becomes the depot and yard | Hub-and-spoke because belt neighbours are 5 km/s and decades of synodic time apart; Mars as the cheap supplier (triangle trade) |
| **4. Nuclear-electric barge trains** | 10–100 MW tugs, 10³–10⁴ t trains | Continuous flows; inventory in flight dominates; schedules like shipping lines |
| **5. Torches** | Δv nearly free | Time is the cost; bulk still prefers efficient slow drives because torch propellant (hydrogen, deuterium) is a commodity itself |

## Worked example: feeding a shipyard in lunar orbit

### Where to put the yard

| Site | From lunar surface | From LEO | For | Against |
| --- | --- | --- | --- | --- |
| **LLO** | ~1.9 km/s | ~4 | Cheapest from the surface; short trips | Mascons perturb orbits; eclipses every ~2 h; heat cycling |
| **NRHO** | ~2.6–2.8 | ~3.5–4 | Stable; little eclipse; cheap from Earth; Gateway heritage | Surface access only near the low point, about once a week |
| **Earth–Moon L1** | ~2.5 | ~3.8 | Access any time; doorway to everything | Unstable; needs small regular station-keeping |
| **Surface** | 0 | — | Gravity, shielding, raw material on site | Finished ships must be launched; large thin structures cannot be |

The rest of the example uses **NRHO**, the most likely early site.

### Bill of materials and sources

| Input | Share | Best source | Notes |
| --- | --- | --- | --- |
| **Propellant** | Usually the largest flow | Lunar polar water (hydrogen) plus regolith oxygen | Oxygen is ~86 % of hydrolox and ~78 % of methalox by mass *(calc)* |
| **Structure** (aluminium, iron, titanium, glass) | Bulk of dry mass | Lunar regolith: aluminium from highlands, iron and titanium from mare basalt and ilmenite | Energy-hungry refining; plant on the surface |
| **Carbon, nitrogen** | Small but essential | Carbonaceous near-Earth asteroids, or Earth | Lunar soil has only ~100 ppm of each |
| **Shielding** | Bulk, low grade | Regolith, slag, water | Anything heavy and local |
| **Vitamins** (electronics, bearings, superconductor tape, reactor fuel) | ~1–5 % of dry mass | Earth | The dependency ladder decides when this shrinks |
| **People and consumables** | Small | Earth | Plus regolith shielding for their quarters |

### The shuttle bill *(calc)*

A reusable hydrolox lander (Isp 450 s) fills up on the surface and flies cargo up:

| Destination | Lander 20 t dry, 50 t cargo | 30 t dry, 100 t cargo |
| --- | --- | --- |
| LLO | 1.16 t propellant per t delivered | 1.02 |
| Earth–Moon L1 | 1.65 | 1.44 |
| NRHO | 1.86 | 1.61 |

- **If the cargo is propellant,** only 35–50 % of what the surface plant makes reaches the yard. The yard pays in propellant to receive propellant.
- **From Earth instead,** each tonne at NRHO needs ~2.7 t in LEO with chemical transfer, or ~1.3 t with a slow electric spiral (~7 km/s through the radiation belts) *(calc)*.

### Annual flows for a mid-size yard *(calc, illustrative)*

Assume the yard turns out 10,000 t of ship dry mass a year and loads 20,000 t of propellant into them.

| Flow | Tonnes a year | Source | Vehicle | Trips |
| --- | --- | --- | --- | --- |
| Structure and shielding | ~9,500 | Lunar surface plant | Hydrolox shuttles | ~190 at 50 t |
| Propellant for the ships | 20,000 | Lunar polar water and regolith oxygen | Same shuttles | ~400 |
| Propellant burned by the shuttles | ~56,000 | Lunar | — | — |
| Carbon, nitrogen, extra water | ~10²–10³ | Carbonaceous asteroids or Earth | Electric tugs into high lunar orbit, then short hops | A few deliveries a year |
| Vitamins at 5 % of dry mass | ~500 | Earth | Heavy launcher plus transfer | ~1,300 t of LEO mass a year |

- **About 600 lander flights a year, roughly two a day,** with a fleet of about a dozen landers if each turns around weekly.
- **The surface plant makes ~76,000 t of propellant a year.** Hydrolox is hydrogen-limited, so that needs ~100,000 t of water. At ~5 % ice by mass (LCROSS found roughly this at Cabeus crater) that is ~2 Mt of polar regolith dug a year: a mid-size terrestrial mine, in permanent darkness at ~40 K.
- **Electrolysis alone** is at least 4.4 kWh per kg of water; with losses and hydrogen liquefaction a working figure is ~7 kWh/kg, so ~80 MW average for the water alone *(calc)*.
- **Lessons:**
  - **The yard is a propellant business** that also welds hulls. Its real capacity is set by the polar ice mines and their power.
  - **Moving the yard to LLO cuts the shuttle bill by ~40 %** at the cost of a messier orbit.
  - **Methalox or metal fuels change the scarce input.** Lunar oxygen with imported methane needs ~22 % of the propellant imported. Aluminium powder burned with lunar oxygen needs nothing imported, at poorer Isp.

### The same template at other moons

| Yard | Local bulk | Scarce or imported | Pipeline to Earth |
| --- | --- | --- | --- |
| **High Mars orbit, fed from Deimos and Phobos** | Rock and possibly volatiles at near-zero Δv | Water if the moons are dry; vitamins | Windows every 2.1 years; ~9 months transfer |
| **Callisto orbit** | Water and rock, 1.7 km/s up, low radiation | Vitamins, fissile fuel | Windows every 13 months; ~2.7 years transfer, so 3–4 years from order to delivery |
| **Ceres orbit** | Water, carbon, salts, 0.4 km/s up | Metals in quantity, vitamins | Windows every 15 months; ~16 months transfer |
| **Titan or Saturn orbit** | Hydrocarbons, nitrogen, water | Vitamins | ~6 years transfer; stockpiles measured in years |

The farther out the yard, the larger its vitamin stockpile has to be, measured in windows rather than months. This is the vitamin cap from [`design/manufacturing-and-the-dependency-ladder.md`](../design/manufacturing-and-the-dependency-ladder.md), made spatial.

## Bulk logistics in the interplanetary age

### Freight classes

| Class | Examples | Value per kg | Mode | Typical pace |
| --- | --- | --- | --- | --- |
| **Bulk** | Water, ore, slag, shielding, raw metal | Low | Self-propelled cargo, electric barge trains, low-energy routes | Years; continuous flow |
| **Containers** | Parts, refined metals, food | Medium | Tug + container on minimum-energy transfers | One window per trip |
| **Express** | Vitamins, medicine, weapons, spares | High | Fast transfers, high-Δv drives | Months |
| **People** | Crews, settlers | Highest | Cyclers or fast ships, shielded | Months |

### Network shape

- **Hubs sit at the edges of gravity wells:** LEO, Earth–Moon L1 and L2, NRHO, high Mars orbit, Ceres orbit, Callisto orbit. Cargo crosses a well once and is traded at the rim.
- **Propellant has a price at every node,** set by its local source plus delivery. That price field is what routes freight. Water is the oil of this economy.
- **Liner and tramp trade both appear.** Liners run fixed schedules on window-driven routes (Earth–Mars every 26 months); tramps chase cargo between belt hubs.
- **Low thrust widens windows but does not remove them.** A continuous-thrust tug can leave a few months either side of the ideal date at modest cost; it still cannot fight phase.

### Eras

| Era | Typical drive | What sets the cost | Logistics looks like |
| --- | --- | --- | --- |
| **Now–2030s** | Chemical, small solar-electric | Earth launch price | Everything comes from Earth; first propellant depots; asteroid demos |
| **Cislunar industry** | Chemical landers on local propellant; 100 kW–1 MW electric tugs | Lunar propellant plants and lander turnaround | Moon feeds the orbital yards; asteroids supply carbon, nitrogen and water |
| **Interplanetary** | Nuclear thermal, MW electric, solar-thermal water | Windows and pipeline inventory | Hubs and depots at Mars, Ceres, outer moons; Mars–belt triangle trade |
| **Mature** | 10–100 MW nuclear-electric barge trains | Power plant capital | Continuous bulk flows; shipping lines; cyclers for people |
| **Torch** | Fusion | Time and fuel | Windows irrelevant for express; bulk still slow to save fuel |

## Vulnerability

- **Tugs are slow, bright and predictable.** Large arrays, long burns and fixed routes make them easy to track and impossible to escort for years. Their protection is the defence of the nodes and the threat of retaliation.
- **Depots and yards are fixed choke points.** Whoever holds the hub prices the propellant.
- **Cargo in flight is a hostage.** 150,000 t in the pipeline is a large exposed asset with no way to turn back.

### Two kinds of blockade

- **Closing the nodes is slow.** Holding or denying a hub stops new cargo, but its bite comes only after the pipeline and the stockpile drain, which can take years at outer-system yards.
- **Raiding the pipeline is fast.** It hits the stock already in flight, so the victim loses supply at once and the stockpile has to cover the gap from the start. A long pipeline is both a long delay for a node blockade and a big target for a raider.

### What it costs to raid a pipeline

| Action | What the raider needs | Cost | What's left afterwards |
| --- | --- | --- | --- |
| **Destroy** | An intercept: a crossing shot or missile, no velocity match | Cheap | Debris that keeps flying toward the victim's capture point, unless the hit also changes its path |
| **Divert** (nudge it off course) | Brief contact or a push on a dumb or disabled cargo | Very cheap with time left (table below) | An intact derelict in solar orbit, recoverable later by whoever finds it first |
| **Seize** | Full rendezvous: match the cargo's velocity, then redirect it to the raider's own node | Expensive: often a sizeable share of the transfer Δv itself | A prize for the raider |

Δv for a small nudge to make a cargo miss its destination, ≈ miss distance ÷ time left *(calc)*:

| Time left | Miss by 1,000 km | 10,000 km | 100,000 km |
| --- | --- | --- | --- |
| 10 days | 1.2 m/s | 12 m/s | 116 m/s |
| 30 days | 0.4 m/s | 3.9 m/s | 39 m/s |
| 100 days | 0.12 m/s | 1.2 m/s | 12 m/s |
| 300 days | 0.04 m/s | 0.4 m/s | 3.9 m/s |

- **Denial is cheap; capture is expensive.** A few m/s months out makes a cargo miss a lunar or Mars capture entirely. Taking it for yourself means paying close to what its owner paid to send it.
- **A cargo with a working drive corrects the nudge,** so the raider first has to disable the drive, or target dumb containers with no drive of their own.
- **Destroying the cargo can be worse for the victim than losing it.** The debris still arrives at the victim's capture point, as a cloud the catcher or depot has to avoid.
- **Seizure is cheapest for a raider already on a similar path,** for example a ship launched in the same window. Once alongside, the nudge table works for the raider: a few m/s with months left moves the arrival from the victim's station to the raider's own station in the same planetary system. Sending the cargo to a different planet is not cheap.
- **Defender responses:**
  - **Arm or escort at departure and arrival,** where the routes converge, rather than along years of transit.
  - **Spread the stock** across many small containers on varied departure dates and trajectories, so no single strike takes much.
  - **Add decoys and stealthy dumb cargo.** Detection decides who can find the stock at all (see [`design/detection-and-the-picture.md`](../design/detection-and-the-picture.md)).
  - **Scuttle charges or self-diversion** deny the raider a prize.
  - **Insure,** then retaliate against the raider's own pipeline.
- **This is prize law again.** Whether capturing cargo in flight is legitimate seizure, piracy or an act of war is a jurisdiction question, which ties into owner and jurisdiction in [`design/bases-settlements-and-the-civilian-economy.md`](../design/bases-settlements-and-the-civilian-economy.md).

## Model proposal for Intercept Window

### Pieces

- **Route graph:** nodes at bodies, orbits, Lagrange points and depots; edges with Δv (impulsive and low-thrust), an aerobraking flag, transfer time and a window function from the synodic period.
- **Vehicle blocks** from the Drive Survey's numbers: ve, jet power, specific mass and reuse. Landers, tugs, self-propelled cargo and later torches are the same block at different points.
- **Freight classes** with value per kg, g tolerance, perishability and whether the cargo can be burned as propellant.
- **Fleets from Little's law,** and inventory in flight as an asset on the balance sheet.
- **Propellant price at every node,** computed from its source and the cheapest delivery route.
- **Flows run as Routine schedules,** as [`design/manufacturing-and-the-dependency-ladder.md`](../design/manufacturing-and-the-dependency-ladder.md) already specifies. Convoys surface only when something interesting happens.

### Choices

| Decision | Options | Recommended | Why |
| --- | --- | --- | --- |
| **Cost model** | (a) Δv only. (b) Propellant, vehicle time, inventory and windows | (b) | Time and inventory are what make slow freight different from fast, and what makes blockades take time |
| **In-flight cargo** | (a) Abstract stock, safe until it arrives. (b) Tracked objects that can be destroyed, diverted or seized | (b) | Raiding the pipeline is the fast blockade, and a seized cargo is the prize that makes raiding pay |
| **Routing** | (a) Point-to-point only. (b) Hub graph with depots | (b) | Depots are the main real lever and create natural strategic points |
| **Windows** | (a) Ignore. (b) Synodic function per edge, softened for low thrust | (b) | Gives the outer system its seasons and makes stockpiles matter |
| **Low-thrust physics** | (a) Impulsive only. (b) Δv × efficiency factor plus time from thrust and power | (b) | Electric tugs are the bulk carriers for most of the game; their time cost must show |
| **Propellant** | (a) Universal resource. (b) Typed (water, hydrogen, oxygen, methane, xenon, metal fuel) with a price per node | (b) | Hydrogen scarcity on the Moon and water as currency are central dynamics |

## Open questions

- [x] ~~Fix the solar-thermal water ve from a primary source.~~ Partly answered by Vance et al. (2024): 643–659 s theoretical for dissociated steam at ~4,000 K and 1 bar; 450–750 s across the temperatures they consider. Model it as a tech curve: plain steam (~350 s) early, dissociated steam (~650 s) once a chamber material survives.
- [ ] Still open for solar-thermal water: thrust per square metre of mirror, system specific mass, and chamber life at 3,000–4,000 K. These set how long a self-propelled water cargo takes, which the paper doesn't give.
- [ ] A Δv table for low-thrust spirals versus impulsive legs on the main edges (LEO–NRHO, high lunar orbit–Mars, Mars–Ceres).
- [ ] Lunar polar ice tonnage and grade distributions, for a depletion curve.
- [ ] Price and specific-mass curves for 1–100 MW nuclear-electric tugs, from the power-block study.

## Sources

- [Keck Institute – Asteroid Retrieval Feasibility Study, final report (2012)](https://kiss.caltech.edu/final_reports/Asteroid_final_report.pdf)
- [OCBJ – AstroForge prepares second asteroid mission](https://www.ocbj.com/technology/astroforge-prepares-second-asteroid-mission/)
- [Aviation Week – Karman+ raises $20M for asteroid mining demo in 2027](https://aviationweek.com/space/commercial-space/karman-raises-20m-asteroid-mining-demo-2027)
- [Vance et al. (2024), A Solar Thermal Steam Propulsion System Using Disassociated Steam for Interplanetary Exploration, Aerospace 11(1) 84](https://www.mdpi.com/2226-4310/11/1/84)
- [Universe Today – TransAstra's robotic asteroid mining spacecraft wins NASA grant](https://www.universetoday.com/articles/robotic-asteroid-mining-spacecraft-wins-a-grant-from-nasa)
- [Wikipedia – Starship Propellant Transfer Demonstration](https://en.wikipedia.org/wiki/Starship_Propellant_Transfer_Demonstration)
- Companion doc: [`studies/mass-drivers-throwing-catching-and-bulk-logistics.md`](mass-drivers-throwing-catching-and-bulk-logistics.md)
- Power and drive numbers: [`studies/drive-survey-concepts-ranges-and-minimum-sizes.md`](drive-survey-concepts-ranges-and-minimum-sizes.md)
