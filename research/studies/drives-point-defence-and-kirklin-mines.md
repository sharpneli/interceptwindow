# Intercept Window: Drives, Point Defence and Kirklin Mines

Nov 2, 2026 · @Teemu

A continuation of [`studies/atomic-rockets-weapons-coverage-and-gaps.md`](atomic-rockets-weapons-coverage-and-gaps.md), digging into three families it flagged: the drive as a weapon, point defence, and Kirklin mines. The goal here is breadth of concepts, each with its physics, a real or studied anchor where one exists, and first-cut numbers. Damage modelling is a separate study; cyber and electronic attack are in other sessions.

Numbers are first-cut, computed from simple laws or taken from the sources listed, and tagged by basis (demonstrated, studied, physics-only) per decision 9 in [`design/fleetwright-principles-for-intercept-window.md`](../design/fleetwright-principles-for-intercept-window.md).

## The short version

- **Every drive is a weapon in proportion to its jet power, and the power is huge.** Pushing 1,000 t at 1 g takes ~50 GW of jet at 10 km/s exhaust velocity and ~5 TW at 1,000 km/s. Divergence limits reach: even a terawatt exhaust spreading at 0.1 rad is down to ~3 kW/m² at 100 km.
- **Some drives are weapons without aiming.** A D-T fusion torch puts ~80 % of its power into 14 MeV neutrons in every direction. At 1 TW that is a lethal dose in seconds at 10 km and in under a minute at 100 km. Antimatter drives shed gamma rays the same way.
- **Beamed-propulsion infrastructure is the long-range version:** laser arrays, plasma-beam stations, ion-beam "shepherds" and mass-driver reaction engines all point energy or mass at things, by design.
- **Point defence in space has one hard truth:** a missile killed in its terminal phase keeps coming as debris. Defence has to deflect, vaporise or kill it early, or accept fragments. Nuclear missiles are the exception: a hit disables the warhead.
- **Defenders have a mass advantage:** their interceptors don't need to be accelerated to the attack's closing speed. ToughSF estimates 60 t of cheap plate drones can answer a 1,000 t missile wave.
- **Kirklin mines turn the attacker's closing speed into the weapon.** A gram of anything at 100 km/s carries more than a kilogram of TNT. The catch is timing: the mine must reveal itself late enough that the missile can't dodge, and its mass grows with the square of the uncertainty it has to cover.

## Part 1: The drive as a weapon

### The rule and the numbers

Larry Niven's Kzinti lesson: a reaction drive's efficiency as a weapon is proportional to its efficiency as a drive. Atomic Rockets traces the idea back to John W. Campbell in 1930.

**Jet power** = ½ × thrust × exhaust velocity. For 1 g on a 1,000 t ship:

| Exhaust velocity | Jet power | Propellant flow |
| --- | --- | --- |
| 10 km/s (NTR-class) | ~50 GW | ~1 t/s |
| 100 km/s (fusion with added mass) | ~500 GW | ~100 kg/s |
| 1,000 km/s (torch) | ~5 TW | ~10 kg/s |
| 10,000 km/s (pure fusion products) | ~50 TW | ~1 kg/s |

A photon drive is the extreme: thrust is P/c, so each newton needs ~300 MW of light. 1,000 t at 0.01 g is a ~30 TW photon drive, which if collimated is a 30 TW laser pointing backwards.

### What limits it

**Divergence.** Intensity at range R for a jet spreading at half-angle θ is about P / (π (θR)²):

| Jet power | Half-angle | At 10 km | At 100 km | At 1,000 km |
| --- | --- | --- | --- | --- |
| 1 TW | 0.3 rad | 35 kW/m² | 350 W/m² | 3.5 W/m² |
| 1 TW | 0.1 rad | 320 kW/m² | 3.2 kW/m² | 32 W/m² |
| 1 TW | 0.01 rad | 32 MW/m² | 320 kW/m² | 3.2 kW/m² |
| 100 TW | 0.01 rad | 3.2 GW/m² | 32 MW/m² | 320 kW/m² |

For scale, sunlight at Earth is 1.4 kW/m², and the ranges doc's laser kill placeholder is 10⁸ W/m². Most drives are lethal at kilometres and a nuisance at hundreds of km. Magnetic-nozzle divergence is the engineered number that decides which; plume detachment studies (VASIMR, fusion magnetic nozzles) are where the data lives.

**Other limits:**

- **Aiming means turning the ship.** The drive is a spinal mount, so a long ship aims slowly.
- **What comes out matters.** A chemical plume is hot gas plus unburned droplets (1–100 µm at 1–3 km/s, which pit solar arrays and radiators on the ISS). A fusion exhaust is ions at tens to thousands of km/s, effectively a particle beam with poor collimation. Fission fragments leave at 3–5 % of light speed and stop in microns, sandblasting and contaminating the surface.
- **Atmospheres:** Atomic Rockets quotes Luke Campbell and Rick Robinson doubting that a torch drive could even run in dense air; the energy would mostly heat the ship and the air around it. Hovering over a city is a Hollywood problem; drive plumes are a space weapon.

### Emission without aiming

Some drives irradiate everything around them, which matters as much for traffic rules as for weapons.

**D-T fusion:** about 80 % of the fusion power leaves as 14.1 MeV neutrons in every direction. Rough unshielded dose rate (fluence-to-dose about 520 pSv·cm² for 14 MeV neutrons; to be checked in the radiation study):

| Fusion power | At 10 km | At 100 km | At 1,000 km |
| --- | --- | --- | --- |
| 1 GW | 0.015 Sv/s | 0.15 mSv/s | ~5 mSv/h |
| 100 GW | 1.5 Sv/s | 0.015 Sv/s | 0.5 Sv/h |
| 1 TW | 15 Sv/s | 0.15 Sv/s | 5 Sv/h |

A terawatt D-T torch is a lethal neutron source to unshielded crews within about 100 km in under a minute, whichever way it points. Its own crew lives behind a shadow shield. D-He3 and p-B11 drives emit far fewer neutrons (side reactions only), which makes **fuel choice a weapons and traffic-law question.**

**Antimatter beamed-core drives:** proton–antiproton annihilation turns about 39 % of the propellant's mass into high-energy gamma rays. The charged pions are the exhaust; the gammas go everywhere.

**Nuclear salt-water rockets:** Zubrin's reference design gives 13 MN at 66 km/s, about 430 GW of jet, and the exhaust is still-fissioning radioactive steam. In space it disperses quickly; near a body or a station it is contamination.

### Catalogue: drives and what they shoot

| Drive | What comes out | As a weapon | Basis |
| --- | --- | --- | --- |
| Chemical, NTR | Hot gas, droplets | Erosion, contamination, heating at close range; ISS keeps radiators and arrays out of thruster plumes by angle | Demonstrated |
| Ion and Hall thrusters | Ions at ~30 km/s, 2–15° divergence | The **ion beam shepherd** pushes debris from tens of metres away without contact; 100 mN for 7 months moves a 5 t object by ~360 m/s. A gray-zone way to shove someone's satellite out of its slot | Studied |
| Magnetic-nozzle plasma (VASIMR class) | Plasma at tens of km/s | Hot, divergent; short-range | Studied |
| Nuclear salt water | Fissioning steam | Radioactive contamination; high thrust | Studied |
| Fission fragment rocket | Heavy ions at 3–5 % c | Surface sandblasting and radioactive contamination along the beam | Studied |
| Orion pulse units | Plasma jets into the pusher plate | The pulse unit pointed the other way **is** a Casaba; the plate itself is a nuclear-rated shield | Studied |
| Medusa | Bombs detonated between the ship and a sail ahead of it | The ship flies behind a stream of nuclear detonations; anything in front of it is in the blast zone | Studied (Solem, LANL) |
| Fusion torch, D-T | Plasma plus omnidirectional neutrons | Directed plume plus a neutron sphere | Physics-only at torch scale |
| Fusion torch, D-He3 or p-B11 | Fast charged products | Directed plume, few neutrons | Physics-only |
| Antimatter beamed core | Pions near c plus gamma rays | Plume plus a gamma sphere | Physics-only |
| Photon drive | Light | A laser of the drive's full power | Physics-only |
| Mass-driver reaction engine | Pellets | A stream of bullets: NASA's tug example fires 16 g pellets at 10 km/s, 10 a second, about 0.8 MJ each. NASA's study notes solid pellets are a hazard to other craft and forbids orbits where they linger | Studied |

### Beamed propulsion: drives that live off the ship

These are weapons by construction, because their job is to point energy at a distant craft:

| System | What it projects | Basis |
| --- | --- | --- |
| Laser sail arrays (Starshot, DE-STAR) | Laser light, GW–TW | Studied; already in the weapons survey |
| Laser broom and ground laser debris removal | Pulsed laser ablation to nudge debris | Studied |
| MagBeam (Winglee, 2004) | A magnetised plasma beam from a station, pushing a craft's magnetic sail (about 11.7 km/s in the study) | Studied |
| Particle-beam and pellet-stream propulsion | Neutral beams or pellets to a magsail | Studied (Singer, Nordley, Benford) |

**Design hook:** a polity that builds a beamed-propulsion network around the system has built a weapons network. Every station is a long-range gun, and every craft riding the beam depends on the station's goodwill.

### Defensive uses of the drive

- **Orion's pusher plate** is made to take nuclear blasts at close range; an Orion turns its plate toward incoming nukes.
- **The plume as a screen:** a torch pointed at an incoming missile wave puts plasma and neutrons in its path. Missiles behind a burning torch are under fire from its drive.
- **The plume blinds:** sensors looking at a torch's plume see little else (a detection-doc hook).

### Doctrine and gray-zone hooks

- **Exhaust envelopes.** Stations need keep-out cones for plumes, as the ISS already has for thrusters. A torch freighter that burns toward a station has committed an incident whether or not it hit anything.
- **Jon's law** (Atomic Rockets, Jon Souza): any interesting drive is a weapon of mass destruction; only the timescale differs. Atomic Rockets suggests range-safety rules, remote self-destruct mandates or military-only torch drives. All three are charter clauses in this game's terms.
- **Accidental Kzinti.** A drive fault pointed at a station is the "fault or probe?" incident the design notes already want.
- **Fuel law.** D-T torches near habitats could be banned outright, which favours D-He3 and pushes the Jovian deuterium and helium-3 economy.

## Part 2: Point defence

### The problem

- **A dead missile still arrives.** In space a missile hit in its terminal phase keeps its velocity as fragments. Atomic Rockets' long analysis (Ian Mallett) concludes that kinetic point defence close in is nearly worthless against kinetic missiles, and that the defence has to act before the terminal phase.
- **Nukes are the exception.** John Schilling, quoted on Atomic Rockets: nuclear warheads are fragile and don't detonate sympathetically, so a solid hit disables one. That pushes nuclear attackers to detonate early, at standoff.
- **Above about 3 km/s** a projectile carries more energy than its own mass in TNT, so a missile's warhead is optional; the missile is a guided slug.
- **Missiles attack the flanks.** Launched sideways, they swing round and come in on the sides, beating sloped frontal armour.

### Layers by range

| Layer | Goal | Typical tools |
| --- | --- | --- |
| Long (≳100 km) | Deflect: a few m/s of lateral push at 100 km makes a missile miss (ToughSF) | Lasers, particle beams, k-slug sand clouds |
| Middle (10–100 km) | Destroy or divert before the terminal phase | Interceptors, Kirklin mines, plate drones, nuclear interceptors |
| Close (≲10 km) | Break up or deflect what's left | Guns, EFP bricks, active protection systems |
| Last | Absorb fragments | Whipple shields, spaced armour, tanks forward |

### Catalogue

**Kinetic, hard kill:**

| Concept | How it works | Anchor and numbers | Basis |
| --- | --- | --- | --- |
| Gatling CIWS | Walks a stream of rounds onto the target using its own radar | Phalanx: ~75 rounds/s at ~1,100 m/s, 1,550-round magazine, effective to ~1.5 km, fires automatically at ~2 km | Demonstrated |
| Hypervelocity guided rounds | Guided shells from railguns or conventional guns | US Navy HVP programme (later cancelled); space version: guided k-slugs | Demonstrated (tests) |
| Sand-burst k-slugs | Railgun shells that open into fine sand clouds in the missile's path before the terminal phase | Atomic Rockets suggestion; repeated hits strip Whipple shields | Studied |
| Plate drones | Cheap plates launched in a stream into the missile's path | ToughSF: 3 kg each (1 m, 2 mm plate), >100/s from a low-velocity coilgun, ~530 m/s Δv; a missile cutting a plate absorbs ~3 MJ | Studied |
| Reactive EFP bricks | Sensors on the hull fire metal slugs at an incoming projectile | ToughSF: detonate at 1–2 km, slugs at ~2.5 km/s, 35–45 MJ per impact | Studied |
| Active protection (Trophy-style) | Radar plus explosively formed penetrators fired in a matrix | Trophy defeats guided missiles and rockets but not kinetic penetrators; can be saturated | Demonstrated |
| Hit-to-kill interceptors | Small rockets that ram | SM-3, Brilliant Pebbles; Golden Dome space-based interceptors (12 firms, $3.2 B, orbital flight tests from 2027) | Demonstrated |
| Multiple kill vehicles | A carrier dispensing 8–20 small kill vehicles of ~4.5 kg each | Kills every credible object in a cluster rather than picking the warhead from decoys | Studied |
| Co-orbital shrapnel interceptor | Matches orbit, detonates a fragmentation warhead nearby | Soviet Istrebitel Sputnikov: ~1,400 kg, intercept in 1–2 orbits, operational from 1973 | Demonstrated |
| Nail cloud | A cloud of nails placed in a target's path | A 1980 SPS military study: 100 kg of 5 cm nails (~6,000), 35 m cloud, 11 km/s closing, ~1.6 hits/m² | Studied |
| Kirklin mines | Part 3 | | |

**Nuclear:**

| Concept | How it works | Anchor and numbers | Basis |
| --- | --- | --- | --- |
| Exo-atmospheric X-ray kill | X-rays blow off a warhead's heat shield | Spartan's W71: ~5 Mt; lethal radius 6–19 km against hard and soft targets, up to ~48 km in good conditions | Demonstrated (deployed with Safeguard) |
| Nuclear anti-missile missile | Burst kills by radiation and shock within a radius | Atomic Rockets/Eric Rozier hit-probability model: kill area over the target's possible displacement area | Studied |
| Wide-angle Casaba as a wave sweeper | One shaped charge clears a whole missile wave | ToughSF; its flash may mission-kill the defender's own sensors and mirrors | Studied |
| Bomb-pumped X-ray lasers | Many rods, many targets, one burst | Excalibur; in the weapons survey | Tested, contested |

**Directed energy:**

| Concept | How it works | Anchor and numbers | Basis |
| --- | --- | --- | --- |
| Laser PD, today | Burns through a target with seconds of dwell | Iron Beam: ~100 kW, ~7–10 km, ~4 s dwell, deploying from late 2025; cost per shot a few dollars of energy, ~$2,000 all-in | Demonstrated |
| Laser PD, space, defocused | Defocus to cover the whole missile and boil off armour, rather than drill holes | ToughSF: 62.5 MW per turret; a 4.4 kg armoured missile needs ~131 MJ, about 2 s; four turrets kill ~13–20 missiles in a pass | Studied |
| Laser deflection | Ablation thrust pushes the missile off course | A few m/s at 100 km is enough; hundreds of m/s at 1 km | Studied |
| Broadside lasers | Many fixed small mirrors on the flanks, no slewing | ToughSF: roughly doubles kills, no switching time | Studied |
| Flash coolers | Expendable coolant charges that cut a laser's recycle time | Attack Vector: Tactical's rule: a laser has a "magazine" of coolant | Game mechanic, physically sound |
| Particle beams | Kill electronics by dose | SDI estimates of 100–1,000 MW to disable an ICBM | Studied |

**Soft kill and deception:**

| Concept | How it works | Notes |
| --- | --- | --- |
| Dazzling seekers | Laser into the missile's sensors | Atomic Rockets doubts it: seekers use many bands, radar, or dead reckoning |
| Jamming and spoofing | Radio and lidar deception | Other sessions (cyber and EW) |
| Decoys for the defended ship | Balloons, heated shrouds, chaff | Covered in the detection doc |
| Clouds as shields | Sand or dust around the ship | Atomic Rockets is sceptical: the cube-square law means you can't carry enough |

**Passive and structural:**

- Whipple shields and spaced armour (ship generator).
- Tanks forward: propellant as a shield (ship generator).
- **Active magnetic shielding** (superconducting coils) deflects charged particles; studied for cosmic rays; useless against neutral beams, neutrons, gammas and slugs.
- **Evasion:** ToughSF notes a missile with ~500 m/s of manoeuvring Δv can be exhausted by a warship jinking at 5 m/s².

**Capture and non-destructive:** RemoveDEBRIS (2018–19) caught a cubesat with a net and fired a tethered harpoon at ~20 m/s into a target in orbit. Ion beam shepherds push without contact. These are gray-zone tools against satellites more than point defence.

### The laser–missile debate

Atomic Rockets calls it the "purple/green" debate (from SFConSim-L): an argument that never resolves because it rests on assumptions.

- **Laser side:** light can't be dodged; anything you can see you can hit; missiles must close, so they can't juke without missing.
- **Missile side:** lasers can be saturated, missiles can be fired from beyond laser range, and a laser that is hit is no longer reusable.
- **The deciding numbers:** laser recycle and cooling time, the energy per area to kill or deflect a missile, missile armour, and cost per shot on each side. In this game those are engineered numbers in blocks, so the debate resolves differently per era and per polity, which is the right outcome.
- **The defender's mass advantage:** ToughSF's estimate is that a 1,000 t missile wave can be answered by about 60 t of plate drones, and each standard laser raises the attacker's required wave by about 250 t. Stealth warheads are the attacker's best route to an even exchange.

### The attacker's counters (penetration aids)

From ICBM practice, adapted:

- **Many warheads per bus** (MIRV); **buses that dispense sub-missiles**.
- **Decoys:** balloons, heated shrouds so temperature can't separate warhead from decoy, chaff, booster fragments.
- **Jammers.**
- **Cosmosols:** particle clouds to hide objects and absorb beams.
- **Kinetic cluster warheads** that fire rods at interceptors.
- **Nuclear blackout:** a burst that blinds radar for minutes.
- **Short boost, stealth bus, cold coast, late burn** (the detection doc's favourite).
- **Space additions:** flank approaches, spinning and Whipple-armoured missiles, sand munitions to clear plate drones and blind EFP sensors (ToughSF), terminal sprints, and standoff nuclear detonation.

## Part 3: Kirklin mines

### What they are

From the Attack Vector: Tactical wargame (credited to Kirk Spencer): cheap chemical interceptors against expensive torch missiles. The mine doesn't need speed or a warhead; it only needs to be in the way, because the missile's own closing speed supplies the energy. Launched at the right moment, a mine either destroys the missile or forces it to swerve so late that it misses the ship. Atomic Rockets' summary adds the predictable answer: missiles become buses of sub-munitions and decoys, and then the mines become buses too.

### The physics

**Energy is free.** A 1 g pellet carries about 12 g of TNT equivalent at 10 km/s, 1.2 kg at 100 km/s and 120 kg at 1,000 km/s. Any mass in the path is a warhead.

**Timing is everything.** A missile with lateral acceleration a can dodge a cloud of radius r if it has more than t = √(2r/a) of warning. So the mine has to reveal itself (or burst) no earlier than that before the encounter, at a distance of closing speed × t:

| Missile lateral accel | Cloud radius | Max warning | Burst distance at 10 km/s | At 100 km/s | At 1,000 km/s |
| --- | --- | --- | --- | --- | --- |
| 10 m/s² | 10 m | 1.4 s | 14 km | 140 km | 1,400 km |
| 10 m/s² | 100 m | 4.5 s | 45 km | 450 km | 4,500 km |
| 100 m/s² | 10 m | 0.45 s | 4.5 km | 45 km | 450 km |
| 100 m/s² | 100 m | 1.4 s | 14 km | 140 km | 1,400 km |
| 1,000 m/s² | 10 m | 0.14 s | 1.4 km | 14 km | 140 km |

Fast closures help the mine: at torch closing speeds a burst hundreds of km out is already too late to dodge.

**Mass grows with the uncertainty squared.** A cloud of radius r that gives ~95 % odds of at least one hit on a missile of cross-section A needs about 3/A pellets per square metre:

**mass ≈ π r² × (3 / A) × pellet mass**

| Cloud radius | 1 g pellets, A = 0.1 m² | 0.1 g pellets |
| --- | --- | --- |
| 10 m | ~9 kg | ~1 kg |
| 100 m | ~940 kg | ~94 kg |

So **a Kirklin mine is a sensor problem.** A good fix on the missile lets the cloud be small and cheap; a vague fix makes it heavy. That ties mines straight to the detection doc: burning missiles are easy to fix, cold ones aren't.

**Forced swerves cost the missile Δv.** A missile that dodges early must spend Δv to re-aim at the ship, from a budget that ToughSF puts around 500 m/s for a small missile.

### Variants

| Variant | Idea | Basis |
| --- | --- | --- |
| Sand cloud | A cheap rocket bursts a pellet cloud across the missile's predicted path | Studied |
| Plate | A thin, wide plate (ToughSF plate drone) | Studied |
| EFP brick | Fires slugs at the last moment from a stand-off | Studied |
| Nail cloud | The 1980 SPS anti-satellite cloud, reversed | Studied |
| Nuclear Kirklin | A cheap low-yield burst in the path | Studied |
| Drop-tank Kirklin | Jettisoned tanks or propellant ice released into the attack path; ships already carry them | Physics-only idea |
| Propellant curtain | Vented water or propellant droplets; at torch closing speeds, droplets are lethal | Physics-only idea |
| Smart pebbles | Mines with seekers and a few m/s of Δv to stay in the path | Studied (Brilliant Pebbles shrunk) |
| Kirklin bus | One carrier dispensing many small mines, answering missile buses | Game concept |
| Parked minefields | Mines pre-placed along approach corridors or orbits | Studied (IS, nail cloud); legal gray zone |

### Counters

- **Buses and decoys:** the missile splits so one mine can't cover all.
- **Sweepers:** sand munitions fired ahead of the missile wave to clear mines and blind their sensors (ToughSF).
- **Standoff warheads:** a missile carrying a Casaba or bomb-pumped laser fires before it reaches the mine. **Mines are best against kinetic missiles and weak against nuclear standoff missiles**, which pushes attackers toward nukes.
- **Late terminal sprint:** hold Δv in reserve and sprint inside the mine's timing window.
- **Shoot the mines:** they're cheap, slow and easy for lasers to kill.
- **Whipple-armoured missiles** survive fine sand, forcing mines to carry heavier pellets.
- **Slow closures:** at a few km/s, pellets aren't lethal, so mines matter most against torch-era missiles.

### Gray-zone notes

- **Inert mass in orbit isn't banned.** A parked Kirklin field is legal in the way kinetic bombardment is, and an incident the moment anyone notices.
- **Mines are debris.** A field left in an orbit is a Kessler hazard; the debris-evolution study reads it.

## What to add to the weapon blocks

| Family | Law | Engineered numbers | Spec |
| --- | --- | --- | --- |
| **Drive as weapon** | Intensity P / π(θR)²; isotropic neutron or gamma flux P_iso / 4πR² | Nozzle divergence, neutron fraction (fuel), exhaust velocity and species | The drive itself; weapon use is a doctrine choice |
| **Beamed-propulsion stations** | As lasers, plasma beams or particle beams | As those families | Station power and aperture |
| **Point-defence guns** | Dodge law plus rate of fire | Muzzle velocity, rate, tracking accuracy | Calibre, rate, magazine |
| **Point-defence lasers** | Laser family, plus dwell and recycle time | Recycle time, flash-cooler charges, defocus control | Power, mirrors, count |
| **Interceptors and kill vehicles** | Missile Δv duel | Divert Δv, seeker, kill vehicles per carrier | Size, count |
| **Kirklin mines** | Burst timing t = √(2r/a); mass ∝ r² | Pellet mass, cloud uniformity, burst timing accuracy, seeker | Cloud radius, pellet count |
| **Active protection** | Short-range EFP matrix | Reaction time, slug velocity | Coverage, reloads |

**Lasers:** reactor-pumped lasers (fission fragments or reactor heat pumping the medium directly, several kW of beam per kg in ToughSF's analysis) and frequency doubling (half the wavelength, double the range, 20–30 % efficiency loss) go into the laser family as engineered options, not as a separate family. Done in [`design/weapon-blocks-and-engineering-projects.md`](../design/weapon-blocks-and-engineering-projects.md).

## Open questions

- [ ] Magnetic-nozzle divergence by drive family: the number that sets every drive's weapon reach (exhaust and plumes study).
- [ ] Neutron and gamma dose from torch drives, shielded and unshielded, with real fluence-to-dose data (radiation and crew study).
- [ ] Should exhaust keep-out cones and fuel-type bans be charter clauses from the start?
- [ ] Laser recycle time and flash-cooler charges as engineered numbers: they settle the laser–missile debate per era.
- [ ] Kirklin mine burst timing as a fire-control problem: how good must the picture be?
- [ ] Do fragments of a missile killed late follow the original trajectory closely enough to still hit? (Damage study.)
- [ ] Parked minefields and the debris model: how long do they last in heliocentric and planetary orbits?

## Sources

- Atomic Rockets: [Exotic Weapons (propulsion systems, Kzinti lesson, Jon's law)](https://projectrho.com/public_html/rocket/spacegunexotic.php); [Projectile Weapons (missiles, Kirklin mines)](https://projectrho.com/public_html/rocket/spacegunconvent.php); [Warship Defenses (point defence, laser vs missile)](https://projectrho.com/public_html/rocket/spacewardefense.php).
- ToughSF: [Space Warship Design III](https://toughsf.blogspot.com/2016/09/space-warship-design-iii-final.html) (laser PD, plate drones, EFP bricks, defender's mass advantage).
- Drives: [Ion Beam Shepherd (Bombardelli & Peláez)](https://ar5iv.arxiv.org/html/1102.1289); [ISS plume impingement (NASA)](https://ntrs.nasa.gov/api/citations/20100019171/downloads/20100019171.pdf); [fusion drive exhaust (arXiv 2108.01689)](https://arxiv.org/pdf/2108.01689); [fission-fragment rocket](https://en.wikipedia.org/wiki/Fission-fragment_rocket); [nuclear salt-water rocket](https://en.wikipedia.org/wiki/Nuclear_salt-water_rocket); [antimatter rocket](https://en.wikipedia.org/wiki/Antimatter_rocket); [Medusa (Centauri Dreams)](https://www.centauri-dreams.org/2024/04/17/medusa-deep-space-via-nuclear-pulse/); [MagBeam (University of Washington)](https://www.washington.edu/news/2004/10/14/new-propulsion-concept-could-make-possible-90-day-round-trip-to-the-red-planet/); [mass-driver reaction engines (NASA SP-428 via NSS)](https://nss.org/settlement/nasa/spaceres/III-3.html); [TV Tropes, Weaponized Exhaust](https://tvtropes.org/pmwiki/pmwiki.php/Main/WeaponizedExhaust).
- Point defence: [Phalanx CIWS](https://en.wikipedia.org/wiki/Phalanx_CIWS); [Trophy](https://en.wikipedia.org/wiki/Trophy_(countermeasure)); [Iron Beam](https://www.wikiwand.com/en/Iron_Beam); [W71 (Spartan)](https://en.wikipedia.org/wiki/W71); [Multiple Kill Vehicle](https://www.globalsecurity.org/space/systems/mkv.htm); [anti-satellite weapons, including Istrebitel Sputnikov](https://en.wikipedia.org/wiki/Anti-satellite_weapon); [Golden Dome space-based interceptors](https://www.executivegov.com/articles/space-force-golden-dome-orbital-interceptor); [penetration aids](https://en.wikipedia.org/wiki/Penetration_aid); [SPS military implications (nail cloud)](https://ssi.org/wp-content/fbs/sps-stinevajk-1980/94); [RemoveDEBRIS harpoon](https://spaceflightnow.com/2019/02/15/experimental-british-satellite-tests-harpoon-in-orbit/); [NASA active magnetic shielding](https://ntrs.nasa.gov/citations/20130000761).
