# Mass Drivers – Throwing, Catching and Bulk Logistics

Survey of mass-driver logistics from today's hardware to the far end: what it takes to throw cargo, what it takes to catch it, and where the real bottlenecks sit. Written for Intercept Window; numbers marked *(calc)* are first-principles calculations done for this doc, the rest come from the sources at the end.

## The short answer

- **Throwing is the easy half.** Energy is cheap (under 1 kWh per kg to leave the Moon) and the physics was demonstrated in 1976. Infrastructure mass, power and dust are the engineering problems, not principle.
- **Catching is three separate problems:** precision (miss distance = velocity error × flight time), momentum (every catch is a thrust event on the catcher) and relative energy (what the cargo and the catcher must absorb).
- **The relative velocity at the catch decides everything.** The working rule of every realistic design is: *put the catcher on the payload's own orbit*, so the catch speed is only the launch dispersion. O'Neill's L2 catcher, a co-orbital tug and a periapsis catcher on an eccentric orbit are all this one trick.
- **A surface launch can never reach a closed orbit by itself.** A single impulse at the surface gives an orbit whose low point is the surface. Something must add a second impulse at the high point: a kick motor on the payload, a tug, or a catcher.
- **Early on, payloads are smart.** A guidance unit and a small motor per payload cost far less than a precision catcher. Dumb streams with big catchers come later, when throughput makes per-payload avionics the dominant cost.
- **Open-loop interplanetary streams are not realistic.** Over months of flight the velocity tolerance drops to micrometres per second. Interplanetary cargo is smart, or it is guided en route, or the catcher is very large and manoeuvrable.

## Physics that shapes every design

### The two-impulse rule

A payload leaving a launcher on an airless body follows an ellipse whose perilune is the launch point. After one revolution it is back at launch altitude.

- **Moon** *(calc)*: a tangential launch to a 100 km apolune needs about 1,703 m/s, reaches the high point after about 57 minutes, and needs **23 m/s** there to circularise. To a 20 km apolune: 1,685 m/s and 4.8 m/s. To 500 km: 1,782 m/s and 96 m/s.
- **A failed circularisation is a projectile aimed at home.** It comes back down roughly 2 hours later, within a few tens of kilometres of the launcher (the Moon has turned about a degree under the orbit).
- **Earth** *(calc, drag ignored)*: a payload leaving the atmosphere at 60 km altitude at 7.8 km/s and 10° climb coasts to about 1,050 km and needs about **670 m/s** to circularise. At 7.0 km/s and 20°, about 1,620 m/s. Drag and heating through the lower atmosphere add to that.
- **Escape trajectories** avoid the second impulse at the launch body but simply move the problem to the destination.

### Track length, acceleration and cargo classes

Track length L = v² / 2a *(calc)*:

| Target speed | 3 g | 30 g | 100 g | 1,000 g | 10,000 g |
| --- | --- | --- | --- | --- | --- |
| Lunar orbit, 1.68 km/s | 48 km | 4.8 km | 1.4 km | 144 m | 14 m |
| Lunar escape, 2.38 km/s | 96 km | 9.6 km | 2.9 km | 289 m | 29 m |
| Earth gun exit, 8 km/s | 1,088 km | 109 km | 33 km | 3.3 km | 330 m |
| Earth, 10 km/s | 1,700 km | 170 km | 51 km | 5.1 km | 510 m |

- **g tolerance sorts cargo.** Raw regolith, ingots, ice and propellant in stout tanks take thousands of g. Hardened electronics take ~10,000 g (SpinLaunch showed a 1U CubeSat surviving that in 2025). Thin solar arrays, radiators and optics want tens of g. People want 3 g, which makes Earth-to-orbit tracks continental and lunar ones ~50–100 km.
- **A lunar driver at 30 g is under 10 km long** and can carry almost any manufactured product. This is why the Moon is the natural mass-driver site.

### Energy and power

- **Kinetic energy per kg** *(calc)*: 0.79 kWh at lunar escape, 8.9 kWh at 8 km/s, 16.8 kWh at 11 km/s. Even at Earth this is a few dollars of electricity per kg.
- **Muzzle power = throughput × v²/2.** The 1977 design's 600,000 t a year at 2.4 km/s is about 19 kg/s and **~55 MW** of muzzle power *(calc)*. A million tonnes a year at 8 km/s from Earth is about **1 GW**.
- **Infrastructure, not energy, sets the price.** Solar plus storage through the 14-day lunar night, coil and capacitor mass, foundations in loose regolith and dust protection on every moving part are what critics of lunar electromagnetic launch focus on.

### Precision: miss distance = velocity error × flight time

| Route | Flight time | Miss allowed | Velocity tolerance |
| --- | --- | --- | --- |
| Moon surface to LLO catcher *(calc)* | ~1 h | 10 m | ~3 mm/s |
| Moon surface to L2 catcher (1977 study) | days | ~50 m | ~10 cm/s along track, ~1 cm/s lateral, ~1 mm/s vertical |
| Moon to Mars, open loop *(calc)* | ~200 days | 100 m | ~6 µm/s |

- **The along-track tolerance is loose for L2** because trajectories can be chosen whose arrival point is insensitive to launch speed (Heppenheimer's "achromatic" trajectories). Vertical and lateral errors remain tight.
- **Disturbances grow with flight time:** lunar mascons (low lunar orbits are unstable except at a few "frozen" inclinations), solar radiation pressure on light payloads, Earth and Sun tides, and outgassing from ice cargo.
- **Open-loop interplanetary aim is not possible.** Something must correct the trajectory en route.

### Momentum: every catch is a thrust event

A catcher that absorbs a payload of mass m arriving at relative speed Δv picks up momentum m·Δv. It must pay that back to stay on station.

| Catch speed | Electric reboost propellant per kg caught (Isp 3,000 s) *(calc)* |
| --- | --- |
| 25 m/s | 0.85 g |
| 1.5 km/s | 51 g |
| 5 km/s | 170 g |

- **At low catch speed the momentum bill is negligible.** At km/s it becomes a real propellant stream.
- **Free reaction mass is on board.** O'Neill's catchers and tugs carried their own small mass drivers firing waste slag. The cargo pays for its own delivery.
- **A station that both throws and catches can balance its own momentum.** This is the basis of the long-term "momentum bank" networks below.

### Relative energy: what the catch does to the cargo

| Catch speed | Energy per kg | Stopping distance at 100 g | at 1,000 g |
| --- | --- | --- | --- |
| 25 m/s | 0.3 kJ | 0.3 m | 3 cm |
| 200 m/s | 20 kJ | 20 m | 2 m |
| 1.5 km/s | 1.1 MJ | 1.1 km | 115 m |
| 2.6 km/s | 3.4 MJ | 3.4 km | 345 m |
| 5 km/s | 12.5 MJ | 12.7 km | 1.3 km |

*(calc)*

- **Below ~200 m/s, a net, bag or foam bed works.** The catch is a hard landing, not a collision.
- **Above ~1 km/s, an unconditioned impact destroys the cargo.** At 2.4 km/s the energy is about 2.9 MJ/kg, comparable to what it takes to heat and boil off water ice. Dumb impact catching of bulk material only works slowly.
- **A km/s catch needs a deceleration track**, which is a mass driver run in reverse and can recover most of the energy as electricity.

## Catching: the option space

Ordered roughly by catch speed, from gentlest to hardest.

| # | Method | Catch speed | Payload needs | Catcher needs | Throughput | Era |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **No catch:** payload is the product | — | Full spacecraft | Nothing | Unlimited | Now (with rockets) |
| 2 | **Smart payload, rendezvous at a depot** | ~0 | Guidance, kick motor, docking aid | Robotic arm or net, depot | Docking cadence, minutes to hours each | Near |
| 3 | **Dumb payload, co-orbital catcher** (catcher on payload's own orbit, e.g. O'Neill L2) | Dispersion only, m/s to tens of m/s | Mass, maybe a reflector | Wide aperture, station-keeping, libration tracking | Several per second | Mid |
| 4 | **Dumb payload, nearby-orbit catcher** (e.g. LLO catcher at apolune) | Tens of m/s | Mass | Net or bag, reboost | Bursts per catcher pass | Mid |
| 5 | **Momentum-exchange tether** (rotovator tip catch) | ~0 at tip, but timing to the millisecond | Grapple fixture, often terminal guidance | Tether, reboost or balanced traffic | Low to medium | Mid–far |
| 6 | **Periapsis catcher on an eccentric orbit** (Oberth catch) | Hundreds of m/s from interplanetary arrivals | Guidance | Catcher in near-escape orbit | Medium | Mid–far |
| 7 | **Regenerative decelerator** (reverse mass driver) | Up to km/s | Conductive or magnetic jacket, terminal guidance to thread the bore | Long track, power handling, momentum budget | Several per second | Far |
| 8 | **Atmosphere** (aerocapture, direct entry) | Any | Heat shield, guidance | Nothing (a planet) | Unlimited | Near for Earth/Mars returns |
| 9 | **Ground impact** (a pit or crater) | ≲1 km/s to keep material | Nothing | Target area | Unlimited | Any, but crude and dangerous |

### 1. No catch: the payload is its own destination

- **SpaceX's 2026 lunar plan is this case.** The stated aim is to build AI compute satellites on the Moon and fling them straight into deep space. A finished satellite with its own thrusters needs no catcher.
- **Dyson-swarm schemes are the same.** Mercury drivers throw self-deploying mirrors or collectors; the "logistics" ends when the product unfolds.
- **Limit:** only works for products, not bulk feedstock.

### 2. Smart payload, docking at a depot

- **This is how every Earth-launched gun payload must work.** The payload is a small rocket with a heat shield; it circularises and is collected like any satellite.
- **On the Moon the "smart" part is tiny.** 23 m/s is under 1 % of the payload mass in propellant *(calc)*; a cold-gas or small solid motor plus a cheap guidance board.
- **Bottleneck:** docking cadence. Robotic capture takes minutes at best, so a depot handles hundreds to thousands per day, not several per second.

### 3. Dumb payload, co-orbital catcher: O'Neill's design

The 1977 NASA Ames summer study and Heppenheimer's 1978 mass-catcher paper set the pattern:

- **Driver:** a ~1,000 t machine (excluding power) throwing payloads above ~10 kg at 2,400 m/s, several per second, about 600,000 t a year; conversion efficiency around 90 %.
- **Catcher at Earth–Moon L2,** where payloads arrive close to the catcher's own motion by trajectory design. It must track lunar librations and do modest station-keeping; moving the material on to a processing orbit costs only 10–30 m/s.
- **Catcher shape:** a large cone. Debris from earlier impacts builds a regolith-like lining that absorbs later arrivals, so payloads do not rebound.
- **Accuracy:** ~10 cm/s along track, ~1 cm/s lateral, ~1 mm/s vertical, for ~50 m miss at L2.
- **Proposed corrections:** optical scanning of each payload just after release, so the trajectory is measured before it leaves the range of correction. (A downrange correction station that nudges each payload is the natural extension; it trades a fixed installation for avionics in every payload.)
- **Arrival speed:** the exact figure in Heppenheimer's design could not be confirmed for this survey. It is low by construction; treat it as an engineered number in the game.

### 4. Dumb payload, nearby-orbit catcher (lunar LLO)

- **Geometry** *(calc)*: a catcher in a circular 100 km equatorial orbit meets an equatorial launch's apolune at about 23 m/s relative speed. Stopping that takes 30 cm at 100 g.
- **Timing:** the catcher passes the apolune point once per orbit (~2 h). The driver fires a burst as the window opens, not a steady stream.
- **Mascons** make most low lunar orbits decay or wander within months; catchers sit in frozen orbits or burn to stay put.
- **Missed payloads are not long-lived debris**; they come down within one revolution. That is a safety problem near the launcher and a cleaning mechanism for orbit.

### 5. Tethers

- **A lunar rotovator** in low orbit can have its tip nearly at rest relative to the surface at the bottom of its swing. A mass driver then only needs to toss cargo up to the tip at modest speed.
- **An Earth hybrid** (gun or hypersonic plane plus orbital tether) would cut the Earth kick stage, but tip timing must be right to milliseconds and every catch drags the tether down. Tethers stay balanced only if mass goes out as well as in.

### 6. Periapsis catch on an eccentric orbit

Interplanetary arrivals hit the destination at v∞ of a few km/s. A catcher in a circular low orbit sees a large relative speed; a catcher in a near-parabolic orbit with periapsis at the arrival point sees only roughly v∞² / 2v_esc *(calc, 300 km periapsis)*:

| Arrival | Relative to circular catcher | Relative to near-parabolic catcher |
| --- | --- | --- |
| Mars, v∞ 2.65 km/s | 2.1 km/s | **0.7 km/s** |
| Earth, v∞ 3 km/s | 3.6 km/s | **0.4 km/s** |
| Earth, from the Moon (v∞ ~0.8 km/s) | 3.2 km/s | **~0.03 km/s** |
| Ceres, v∞ 5 km/s | 4.7 km/s | 4.5 km/s |

- **Deep wells help; small bodies don't.** A Ceres catcher gets no help from Ceres' gravity; the cargo must brake itself or hit a long deceleration track.
- **The caught mass ends up on an eccentric orbit.** A slow electric tug or aerobraking passes take it the rest of the way, or the catcher is a cycler that unloads elsewhere.

### 7. Regenerative decelerator

- **A coilgun run backwards** turns the payload's relative kinetic energy back into current. At 100 g, a 1.5 km/s catch needs ~1.1 km of track.
- **The payload must thread a bore of centimetres to metres** after hours to months in flight. That needs terminal guidance on the payload or a catcher that steers its mouth, or both.
- **Combined with outbound launches it becomes a momentum bank:** catch inbound, throw outbound, store the energy in between.

### 8. Atmosphere as catcher

- **Lunar cargo headed for Earth** arrives near 11 km/s and can aerobrake into LEO or enter directly. This is The Moon is a Harsh Mistress logistics, and physically sound with ablative shells.
- **Mars** works the same way with lighter shields.
- **Cost:** a heat shield and guidance per payload; the shield is mass that never becomes product.

### 9. Ground impact

- **Below roughly 1 km/s** a bulk load into a regolith pit keeps much of its material; above, most of it melts or vaporises.
- **It is the same act as a bombardment.** One tonne at 11 km/s carries about 14.5 t of TNT equivalent *(calc)*.

## Regime by regime

### Earth surface to orbit (now to mid-term)

- **The payload is always a rocket.** Air drag and heating at 7–10 km/s in the low atmosphere are severe, so designs exit at altitude (StarTram's mountain-top or high-altitude muzzle) or exit slow and let a rocket do more (SpinLaunch's ~2 km/s release plus upper stage).
- **Kick stage** *(calc)*: 0.7–1.6 km/s to circularise plus drag losses means 1–2 km/s, i.e. **~30–50 % of the flying mass is propellant** at Isp ~300 s, before heat shield and structure.
- **Catching is ordinary rendezvous** at a depot. Bulk, g-tolerant cargo (water, propellant, metal stock, food) is the natural trade.
- **Where real companies stand (late 2026):**
  - **SpinLaunch** has pivoted to building a satellite constellation, Meridian, whose first customer link was scheduled to fly on a conventional SpaceX rideshare, Transporter-18, in October 2026. Its kinetic launcher is no longer the headline product.
  - **Longshot** reached Mach 4.6 with its Oakland prototype and is building a ~500 m multi-injection gas gun in Tonopah, Nevada, aiming at Mach 5 for 100 kg payloads and hypersonic testing; its long-term goal is a ~12-mile gun putting 100 kg in orbit for around $150 per kg.
  - **Historical:** Project HARP's 16-inch gun reached about 180 km altitude in the 1960s; LLNL's SHARP light-gas gun reached about 3 km/s in the 1990s.
- **Verdict:** physically real, commercially unproven. Hypersonic testing pays first. Against a reusable heavy rocket near $100/kg, an Earth gun has to win on cadence and marginal cost for bulk cargo only.

### Moon (near to mid-term; the strongest case)

- **The physics is benign:** no air, 1.68 km/s to orbit, 2.38 km/s to escape, short tracks at moderate g.
- **The engineering is not trivial.** Critics of lunar electromagnetic launch stress infrastructure mass delivered from Earth, foundations in unconsolidated regolith, abrasive charged dust on kilometres of moving parts, and power through the lunar night.
- **Economics depend on what Earth launch costs.** Casey Handmer's May 2026 analysis argues that if Starship-class launch is cheap, launch is only a few percent of the cost of space hardware, so a lunar driver only pays if Earth launch capacity becomes a binding limit at very large scale.
- **Live interest:** SpaceX published a lunar mass-driver concept in March 2026 as part of its lunar factory plans.
- **Natural sequence:** smart payloads to a depot in LLO or at L1/L2 first, then dumb bulk to a co-orbital catcher once tonnage justifies it, then direct throws to Earth (aerobraking) and deep space.
- **Earth escape from the Moon** needs about 2.41 km/s at the surface; a Mars transfer without an Earth flyby about 3.25 km/s *(calc)*. A powered Earth flyby lowers that.
- **A fixed track points one way.** The Moon is tidally locked, so a near-side driver's launch direction is fixed relative to Earth and sweeps once a month in inertial space. Interplanetary windows recur monthly per driver, inside the synodic windows.

### Mars, its moons, the belt and Mercury (mid-term)

- **Phobos and Deimos:** escape speeds of about 11 and 6 m/s. Anything thrown is "launched"; catching is a slow rendezvous.
- **Mars surface:** thin air still heats a 3.5–4 km/s projectile. A driver up the flank of a Tharsis volcano reduces this; most designs still need a kick stage.
- **Ceres:** ~0.5 km/s escape, no air; a short, gentle driver. Arrivals at Ceres get no gravity help (table above).
- **Mercury:** ~4.25 km/s escape, no air, abundant sunlight; the classic site for Dyson-swarm material.
- **Interplanetary cargo is smart.** Cheap guidance (star tracker, radio beacon, cold-gas thrusters) per container is the only way to land within metres after months. The alternative is laser-tracked pellets nudged en route by photon pressure, a far-term concept.

### Far term and the ultimate end

- **Momentum-bank networks.** Stations that both catch and throw, recovering energy regeneratively. Net momentum imbalance is paid by electric thrust or by throwing waste slag away. Logistics becomes a network of streams rather than ships.
- **Launch loops and orbital rings at Earth.** A launch loop still releases payloads on an ellipse, so it still needs a kick or a tether catch. An orbital ring accelerates payloads along the ring at ring altitude and releases them into a closed orbit: no kick stage at all. Run backwards, the ring is the catcher for inbound cargo.
- **Pellet-stream propulsion.** A ship becomes the catcher: it reflects or absorbs a pellet stream from a fixed driver (Singer 1980; later "mass beam" studies by Nordley and Crowl). Pellets must be self-guiding or laser-steered. Logistics, propulsion and weaponry become the same infrastructure.
- **Dyson-scale extraction.** Mercury and asteroid drivers throw self-deploying products; no catch at all.

## Dual use and vulnerability

- **Every payload is a kinetic round.** A tonne at Earth arrival speed is ~14.5 t TNT. A driver able to hit a catcher at L2 within 50 m can hit a city.
- **Every miss is an impactor or debris.** Near the Moon, misses fall back within an orbit; at L-points and interplanetary, they linger.
- **Catchers are the soft target.** They are huge, slow, predictable and fixed to a known point. Kill or blind the catcher and the driver stops being useful, without touching the driver.
- **Streams are predictable.** A stream can be interdicted along its path, or salted with debris.
- **Tugs are the choke point early on.** In smart-payload and depot architectures, whoever owns the collection fleet owns the route.

## What strategy games simplify

Strategy games tend to treat a driver as a pipe between two endpoints (in Aurora a mineral packet needs a receiving driver at the far end). The realistic version adds:

- **Geometry and windows.** A driver is fixed to a rotating body; launch direction and destinations open and close.
- **A separate catch capacity**, often lower than throw capacity, set by catcher type and catch speed.
- **Precision as a technology level.** Dispersion × flight time against catcher aperture gives a loss fraction.
- **Payload classes by g tolerance and by smart vs dumb.** Smart payloads cost avionics; dumb ones need better catchers.
- **A momentum budget at the catcher** and a debris or impact cost for misses.

## Model proposal for Intercept Window

### Blocks

- **Driver block:** v_max, acceleration a (sets the cargo classes allowed), track length L = v²/2a, payload mass, cadence, power (throughput × v²/2 ÷ efficiency), fixed launch azimuth, and site.
- **Payload class:** g rating; smart or dumb; for smart, cost and mass of guidance and kick (Δv from the two-impulse calculation).
- **Catcher block:** catch-speed limit, aperture, throughput, energy recovery fraction, reboost source (electric thrust or slag driver).
- **Route:** launch site to catcher with flight time T, window schedule, required Δv at arrival, and dispersion σ = σ_v·T (smart payloads cut σ to near zero).
- **Loss:** probability a payload falls outside the aperture; each loss becomes an impact event, debris or a return to the launch area.

### Technology ladder

| Tier | What exists | Catching |
| --- | --- | --- |
| 0 (today) | Earth gas guns and centrifuges for hypersonic testing | None; suborbital |
| 1 | Earth gun + kick stage to depot; first lunar driver with smart payloads | Rendezvous and robotic capture |
| 2 | Lunar bulk export at 10⁵ t a year scale | Co-orbital catchers at L1/L2 or in LLO; slag-driver reboost |
| 3 | Moon to Earth and Mars streams; Phobos and Ceres drivers | Periapsis catchers, aerocapture, regenerative decelerators; momentum banking |
| 4 | Orbital rings, pellet-stream ships, Mercury Dyson throwers | The ring or the ship is the catcher, or no catch at all |

### Choices

| Decision | Options | Recommended | Why |
| --- | --- | --- | --- |
| **Catch modelling** | (a) Pipe, no catcher. (b) Catcher as a separate block with capacity and catch speed. (c) Full per-payload trajectories | (b) | The catcher is where the physics and the vulnerability live; per-payload trajectories add nothing a player sees |
| **Precision** | (a) Ignore. (b) Loss fraction from σ_v·T against aperture | (b) | Turns guidance into an engineered number and creates debris and impact incidents naturally |
| **Smart vs dumb** | (a) One payload type. (b) Player choice per route | (b) | A real trade: avionics per kg against catcher investment; early game smart, late game dumb |
| **Earth launch** | (a) Leave out. (b) Gun to depot with kick stage as a cargo-only route | (b) | Real, contested and cheap enough to matter for bulk propellant and water |
| **Dual use** | (a) Separate weapon. (b) Any driver can be re-aimed, with aim precision from its tech | (b) | Matches the doc's existing view of the lunar driver as industrial asset and weapon |

## Sources

- [Space-Based Manufacturing from Nonterrestrial Materials (1977 NASA Ames study, NSS)](https://nss.org/?p=29416)
- [Mass catcher (Wikipedia; cites Heppenheimer 1978, J. Spacecraft and Rockets 15(4))](https://en.wikipedia.org/wiki/Mass_catcher)
- [Space Studies Institute research report: Mass Driver I–III](https://ssi.org/?p=25)
- [Space.com – Elon Musk wants to put a satellite catapult on the Moon](https://www.space.com/astronomy/moon/elon-musk-wants-to-put-a-satellite-catapult-on-the-moon-its-not-a-new-idea)
- [SpaceQ – SpaceX's lunar manufacturing and mass driver plan](https://spaceq.ca/scaling-its-orbital-data-centre-spacexs-lunar-manufacturing-and-mass-driver-plan/)
- [Casey Handmer – How to build a lunar mass driver (May 2026), via mirror](https://hackernews-dynamic.seasondane.workers.dev/news/48293617)
- [Orbit Codex – Mass drivers](https://orbitcodex.com/knowledge-base/mass-drivers)
- [Green Launch – Infrastructure mass on the Moon](https://greenlaunch.space/feeds/blog/lunar-launch-infrastructure-mass)
- [Green Launch – Lunar mass driver vs light-gas gun](https://greenlaunch.space/feeds/blog/lunar-mass-driver-vs-light-gas-gun)
- [SpinLaunch Meridian / Transporter-18 (Business Wire via Mammoth Times)](https://business.mammothtimes.com/mammothtimes/article/bizwire-2026-2-3-spinlaunch-appoints-former-kymeta-ceo-walter-berger-to-advisory-board-to-support-growth-of-meridian-leo-constellation)
- [TechCrunch – Longshot to build space gun in the desert](https://techcrunch.com/2024/09/25/longshot-space-closes-over-5m-in-new-funding-to-build-space-gun-in-the-desert)
- [Payload – Longshot is gunning for kinetic space launch](https://payloadspace.com/longshot-is-gunning-for-kinetic-space-launch)
