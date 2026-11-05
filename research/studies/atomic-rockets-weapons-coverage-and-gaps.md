# Intercept Window: Atomic Rockets Weapons – Coverage and Gaps

Nov 2, 2026 · @Teemu

The first slice of the Atomic Rockets survey (item 1 in [`studies/research-agenda.md`](research-agenda.md)): the weapons pages only. It maps what Atomic Rockets covers against what our docs already have ([`studies/weapons-survey-long-range-concepts.md`](weapons-survey-long-range-concepts.md), [`studies/strategic-beams-x-ray-and-gamma-fels.md`](strategic-beams-x-ray-and-gamma-fels.md), [`design/weapon-blocks-and-engineering-projects.md`](../design/weapon-blocks-and-engineering-projects.md), [`design/combat-ranges-and-group-tracks.md`](../design/combat-ranges-and-group-tracks.md), [`design/detection-and-the-picture.md`](../design/detection-and-the-picture.md)), lists what's missing by priority, and collects the numbers worth keeping.

Read in the built-in browser on Nov 2, 2026. Atomic Rockets is a compilation: much of it quotes ToughSF, Luke Campbell, Rick Robinson, Ken Burnside and fiction. Numbers taken from it are starting points to trace to their primary sources, per the realism gradient (decision 9 in [`design/fleetwright-principles-for-intercept-window.md`](../design/fleetwright-principles-for-intercept-window.md)).

## The short version

- **Our long-range end is ahead of Atomic Rockets.** Strategic beams, picture-limited ranges, sweep energy, gamma dose economics and the overkill ladders are mostly not there.
- **Our near end is thin.** Atomic Rockets has much more on what decides close fights and early eras: nuclear burst effects in vacuum, weapon mounts and arcs, point defence and missile tactics, armour against lasers, laser waste heat and optics vulnerability.
- **Three families are missing outright:** the drive as a weapon (the Kzinti lesson), cyber attack on ships, and EMP. All three fit systems we already have.
- **One family is new and important for the power chain:** nuclear reactor-pumped lasers, which skip electricity and reach several kW of beam per kg.
- **One correction:** a bulk antimatter bomb is inefficient, because the first annihilation blows the rest apart. Antimatter beams and macrons avoid this, which makes them the better endgame weapons, not just the flashier ones.
- **Several concepts are excluded by physics** (plasma guns, force fields, meson guns, tractor beams, nova bombs). The realism rule handles them: out unless logged as exceptions.

## Pages read

| Page | What it covers |
| --- | --- |
| [Space Weapons Intro](https://projectrho.com/public_html/rocket/spacegunintro.php) | Engagement envelopes, weapon mounts and firing arcs, mount protection, a weapon classification scheme |
| [Projectile Weapons](https://projectrho.com/public_html/rocket/spacegunconvent.php) | Nukes in space (EMP, impulsive shock, radiation flux, neutron and salted bombs, shaped charges), kinetics (railguns, coilguns, the Almaz cannon, Kirklin mines), missiles and drones |
| [Beam Weapons](https://projectrho.com/public_html/rocket/spacegunconvent2.php) | Lasers (efficiency, combat mirrors, accuracy, optics, bomb-pumped and reactor-pumped lasers), particle beams, macrons |
| [Exotic Weapons](https://projectrho.com/public_html/rocket/spacegunexotic.php) | Antimatter, cyber, EMP, drives as weapons, ramming, relativistic weapons, and a long list of speculative and impossible ones |
| [Warship Defenses](https://projectrho.com/public_html/rocket/spacewardefense.php) | Evasion, camouflage, armour (including actively cooled armour), sandcasters, point defence, heat sinks |
| [Orbital Attack](https://projectrho.com/public_html/rocket/planetaryattack.php) and [Orbital Defense](https://projectrho.com/public_html/rocket/planetaryattack3.php) | The gravity gauge, Project Thor, the Orion bomber, asteroid and laser bombardment, fortresses, surface-to-orbit missiles |

## Coverage map

Status: **covered** (in our docs at comparable depth), **partial** (named but thin), **missing**, **excluded** (fails physics; out unless logged).

### Nuclear

| Atomic Rockets topic | Status | Where it should go |
| --- | --- | --- |
| Bursts in vacuum: no fireball, X-ray flash, fluence by range | partial | Bursts study |
| Impulsive shock (X-ray blow-off) and spall | partial (ship generator's ablation hook) | Bursts study; armour |
| EMP in space (system-generated, not atmospheric) | missing | Electronics vulnerability study |
| Neutron (enhanced radiation) warheads | missing | Bursts study; radiation and crew |
| Salted bombs | missing | Bursts study (fallout on bodies, activation) |
| Pure fusion and chemically ignited fusion devices | partial (antimatter-catalysed only) | Warhead conversion |
| Nuclear shaped charges, Casaba-Howitzer | covered | — |
| Bomb-pumped X-ray lasers | covered | — |

### Lasers

| Atomic Rockets topic | Status | Where it should go |
| --- | --- | --- |
| Diffraction range | covered | — |
| Efficiency and waste heat; open-cycle cooling | partial | Beams study; heat rejection |
| Reactor-pumped lasers (direct nuclear pumping) | **missing** | Beams study; power study; laser family |
| Frequency doubling (halve λ, double range, 20–30 % loss) | missing | Laser family engineered numbers |
| Combat mirrors and powersat weapons | covered (relay mirrors) | — |
| Mirror armour | partial | Armour study |
| Accuracy error budget | missing | Fire control; beams study |
| Optics vulnerability, shutters, shooting down the barrel | missing | Beams study; ship generator |
| Laser bombardment through atmospheres | missing | Beams study (orbit–surface) |

### Particle beams

| Atomic Rockets topic | Status | Where it should go |
| --- | --- | --- |
| Neutral particle beams, SDI, BEAR | covered | — |
| Space charge blooming (charged beams) | covered | — |
| Neutron beams (thermal bloom only) | missing | Beams study |
| Bremsstrahlung: charged beams as X-ray sources inside the target | missing | Beams study |
| Damage by dose and volumetric heating; APS power estimates | partial | Beams study |
| Recombination glow (neutral beams are visible) | missing | Detection: beams have signatures |
| Macrons and payloads | covered | — |

### Kinetics and missiles

| Atomic Rockets topic | Status | Where it should go |
| --- | --- | --- |
| Railguns, coilguns | covered (sketch) | Kinetic launchers study |
| Almaz space cannon (1975) | **missing** | Demonstrated anchor for the chemical-era gun |
| Kirklin mines | **missing** | Point defence study; new block |
| Missile flank tactics and k-slug terminal phase | missing | Guidance and intercept study |
| Missile defence options | partial | Point defence study |
| Drones | partial | Guidance study |
| Optimal missile mass ratio ("poor man's R-bomb") | missing | Guidance study; missile designer |
| Hit probability against a dodging target | covered | — |

### Exotic

| Atomic Rockets topic | Status | Where it should go |
| --- | --- | --- |
| Antimatter energy, cost, containment | covered | Correction below |
| Antimatter bomb inefficiency | **missing** | Weapon blocks doc (correction) |
| Antimatter-catalysed weapons | covered | — |
| Cyber attack ("space hackers") | **missing** | Shadow Ledger's software front; electronics; new family |
| EMP weapons (e-bombs) | **missing** | Electronics vulnerability study |
| Drives as weapons (Kzinti lesson) | **missing** from weapons docs | Exhaust and plumes study; weapon blocks doc |
| Weapon recoil as thrust (anti-Kzinti lesson) | missing | Ship generator |
| Every interesting drive is a WMD (Jon's law) | covered in spirit (envelopes) | — |
| Ramming | partial (KKVs) | Guidance study |
| Relativistic weapons | covered | — |
| Nanotech and self-replicators | partial (Shadow Ledger, universal assembler) | Out of weapons scope for now |
| X-ray bomb (conventional explosive X-ray source) | missing | Low priority |
| Neutrino gun | missing | Physics-only far end |
| Hafnium isomer bomb | missing | Physics-only; triggering contested |
| Subnuclear (bottom-quark) bomb | missing | Physics-only energy store |
| Strangelet bomb | missing | Unknown physics: logged exception only |
| Collapsing (californium) rounds | missing | Low priority |
| Plasma guns, meson accelerators, tractor beams, Medusa weapons, nut-crackers, nova bombs | **excluded** | Out unless logged |

### Defences

| Atomic Rockets topic | Status | Where it should go |
| --- | --- | --- |
| Evasion and the light-lag hit formula | covered | — |
| Camouflage, disguise, Q-ships | partial (decoys, weighing burning ships) | Detection |
| Armour layers, Whipple shields | covered (ship generator) | — |
| Actively cooled armour, sloping, star-pyramid shapes | **missing** | Armour study; ship generator |
| Armour doctrine by range (long, short, all-range) | missing | Armour study |
| Sandcasters | partial; Atomic Rockets doubts them as laser defence | Beams study (test, don't assume) |
| Force fields | excluded | — |
| Kinetic point defence (CIWS models) | missing | Point defence study |
| Nuclear anti-missile missiles, hit probability model | missing | Point defence study |
| Laser against missile (the "purple/green" debate) | missing | Point defence study |
| Heat sinks | covered | — |

### Orbital attack and defence

| Atomic Rockets topic | Status | Where it should go |
| --- | --- | --- |
| The gravity gauge (the high ground) | partial | Orbital defence design |
| Project Thor | covered | — |
| Asteroid bombardment and national Spaceguards | partial | Politics: who watches asteroid orbits |
| Orion bomber (1965 military Orion) | missing | Drive and warship reference |
| Project Pluto (nuclear ramjet missile) | missing | Atmospheric bodies only; low |
| Burning glass (solar mirror weapon) | missing | Low; fragile but cheap |
| Orbital fortresses, interdiction platforms | missing | Orbital defence design |
| Planetary fortresses, deep defences, surface-to-orbit missiles | missing | Bases and settlements |
| 1959-era space fleet counterforce study | missing | Doctrine shapes |

### Mounts and classification

| Atomic Rockets topic | Status | Where it should go |
| --- | --- | --- |
| Engagement envelopes (weapon engagement zones) | covered | — |
| Mount types (racks, turrets, broadsides, spinal), firing arcs, 3D arcs | partial (turrets and spinal coilgun) | Ship generator fittings |
| Mount protection | missing | Ship generator |
| Weapon classification scheme | missing | Useful taxonomy for the designer UI |

## What's missing, by priority

### High: decides fights in the scenario battler's slice

1. **Nuclear effects in vacuum.** The bursts study needs these first.
   - X-ray and neutron fluence fall as yield over range squared. Atomic Rockets quotes roughly F_x ≈ 2.6×10²⁷ · Y/R² X-rays per m² and F_n ≈ 1.8×10²³ · Y/R² neutrons per m² (Y in kt, R in m).
   - Impulsive shock: about 10⁹–10¹¹ W/cm² for a microsecond vaporises a surface fast enough to drive a shock and spall. Atomic Rockets' estimate puts the impulsive-shock radius of a 1 Mt burst at only a few hundred metres; at 1 km it still vaporises surface.
   - EMP in deep space is **system-generated** (the burst's X-rays and gammas knock electrons out of the target's own skin and drive currents inside it), not the atmospheric kind.
   - Neutron (enhanced radiation) warheads put about 40 % of yield into 14 MeV neutrons instead of about 5 %. Spacecraft shielding and reactor shadow shields blunt them.
2. **Mounts, arcs and recoil.** Turrets, broadsides and spinal mounts trade arcs against size; spinal mounts aim by turning the whole ship, which is slow for a long ship. The anti-Kzinti lesson: any powerful weapon is also a thruster, so off-axis fire spins the ship. This belongs in the ship generator's fittings and report.
3. **Point defence and missile tactics.**
   - Missiles faster than about 3 km/s carry more kinetic energy than their mass in TNT, so non-nuclear warheads are mostly pointless.
   - Missiles launched sideways can swing round and come in on the target's flanks, beating sloped frontal armour.
   - **Kirklin mines:** cheap chemical interceptors that only need to get in the way of an expensive torch missile; the closing speed does the work. Counter: the missile becomes a bus of sub-munitions and decoys.
   - Nuclear anti-missile missiles: hit probability is the kill area over the target's possible displacement area.
4. **Reactor-pumped lasers.** Fission fragments or the reactor's heat pump the lasing medium directly, skipping the electrical conversion chain. ToughSF's analysis (quoted on the beams page) finds several kW of beam per kg for well-designed versions. This changes the laser family's specific mass and the whole power-to-heat chain; it belongs in the laser block's engineered numbers.
5. **Armour against lasers.** Actively cooled armour (liquid tin flowing through carbon, absorbing gigawatts per square metre while it heats), compound sloping (star-pyramid shapes) and spin together shorten a laser's effective range several times, and flank attacks undo much of the sloping. The armour study and the ship generator's layer stack need these.
6. **Drives as weapons.** A drive's exhaust power is a weapon in proportion to how good a drive it is, though exhausts diverge fast. Our research agenda already has the exhaust and plumes study; the weapon blocks doc should treat the drive as a family, and the envelope system already treats every torch freighter as a potential weapon.
7. **Cyber attack.** Commands sent over a radio link to vent, scram or detonate; air gaps, Faraday cages and emission security as defences. This is the Shadow Ledger's software front generalised to every polity: a weapon family whose range is the comms link and whose counter is architecture.
8. **The Almaz cannon.** Salyut 3 (Almaz 2, 1974–75) carried a modified aircraft cannon, aimed by turning the whole station, and test-fired it by remote control. Reported trial ranges were 500–3,000 m. It is the demonstrated anchor for the chemical-era gun.

### Medium: shapes later eras and other systems

- **Laser error budget and optics vulnerability.** A long list of real error sources (sensor resolution, boresight, slew distortion, thermal distortion); unshuttered optics focus an enemy's beam into your own laser; adaptive mirrors limit the damage. For the beams study and fire control.
- **Laser waste heat.** A weapon laser is a furnace that makes coherent light as a by-product. Open-cycle cooling vents hot gas, which is visible and dangerous to anything behind. Reference: Martin Marietta's Zenith Star design, a ~2 MW hydrogen-fluoride laser with a 2 m mirror and about 300 km effective range.
- **Frequency doubling:** halving the wavelength doubles range at a 20–30 % efficiency cost. A clean engineered-number step for the laser family.
- **Particle beam signatures and side effects.** Neutral beams glow from recombination, so they aren't invisible. Charged beams make bremsstrahlung X-rays inside the target. SDI-era estimates put 100–1,000 MW of beam power on disabling an ICBM by dose.
- **Optimal missile mass ratio.** For a fixed launch mass, kinetic energy on target peaks at a mass ratio of e² (about 7.4), when the missile reaches twice its exhaust velocity; burning more lowers the delivered energy. A design rule for the missile designer.
- **Laser bombardment through atmospheres.** Ultraviolet below about 200 nm and harder is absorbed by air; water vapour blocks infrared bands; thermal blooming spreads beams. Tunable FELs pick windows. This sets which beams cross Earth's, Mars's and Titan's atmospheres, alongside the gamma-ray note in the strategic beams doc.
- **Orbital defence architecture.** The gravity gauge, orbital fortresses and interdiction platforms, planetary fortresses buried deep, surface-to-orbit missile families, and a 1959 study's three-layer space fleet (low, intermediate and deep-space forces). Shapes for the bases doc and doctrine.
- **Spaceguards as politics.** In a divided system, each power watches asteroid orbits so nobody nudges one quietly. A natural gray-zone mechanic for the incident record.
- **Military Orion.** General Atomic's 1965 Orion proposals (8, 10 and 12 m pusher plates, specific impulse about 2,700–3,700 s); Orion drives shrug off weapons that would disable chemical engines.
- **Q-ships and disguise.** A warship mimicking a freighter's plume and acceleration; our detection doc already says matching both costs mass.

### Physics-only far end

- **Neutrino beams** from very high-energy muon colliders produce a measurable radiation hazard far from the machine. As a weapon it is feeble, but it is the only beam that ignores occlusion: planets don't stop it.
- **Bottom-quark fusion** releases about 4 % of rest mass, more than fusion, but its fuel must be manufactured at tiny efficiency. It is an energy store like antimatter, but worse.
- **Nuclear isomers (hafnium-178m2)** store large energy for decades, but triggered release was never credibly shown. Same physics family as the graser.
- **Strangelets** depend on an unconfirmed hypothesis. If used, they're a logged exception, not physics-only.

### Excluded unless logged

Plasma guns (a plasmoid expands and dissipates), force fields, meson accelerators, tractor beams, Medusa weapons, planet nut-crackers, nova bombs (except via strangelets) and mirror armour as a complete laser defence. Atomic Rockets reaches the same verdicts.

## Corrections to our docs

- **Antimatter bombs are inefficient.** When bulk antimatter meets matter, the first annihilations at the surface blow both apart before most of it reacts. Getting a large fraction to annihilate needs it to hit a planet or be finely mixed. **Beams and macrons avoid this:** each particle or macron annihilates inside the target's own matter. Done: [`design/weapon-blocks-and-engineering-projects.md`](../design/weapon-blocks-and-engineering-projects.md) now gives antimatter warhead blocks an annihilation coupling number, low for bare bombs, near one for beams and macrons.
- **Containment detail.** Static fields can't hold a stable trap (Earnshaw's theorem), so traps use changing fields (Penning traps). Forward's bulk storage idea is a snowball of antihydrogen below 2 K, levitated magnetically in vacuum. This fills the "physics-only placeholder" for the antimatter magazine.
- **Sandcasters.** Our ranges doc treats clouds as offensive, which is fine. Atomic Rockets is sceptical that dust clouds can defend against lasers. The beams study should test this, not assume either way.

## Proposed next steps

1. ~~Fold the antimatter correction into the weapon blocks doc.~~ Done, with the containment detail.
2. **Add to the research agenda:** cyber attack and EMP under electronics vulnerability; reactor-pumped lasers under beams; weapon mounts and recoil under structures or the ship generator; orbital defence architecture under Tier 2.
3. **Weapon blocks doc:** sketches for the drive as a weapon, Kirklin mines and point defence, and cyber.
4. **Continue the Atomic Rockets survey** with the pages linked from these: heat radiators, power plants, radiation, detection, warship design and the engine lists.

## Sources

- Atomic Rockets: [Space Weapons Intro](https://projectrho.com/public_html/rocket/spacegunintro.php), [Projectile Weapons](https://projectrho.com/public_html/rocket/spacegunconvent.php), [Beam Weapons](https://projectrho.com/public_html/rocket/spacegunconvent2.php), [Exotic Weapons](https://projectrho.com/public_html/rocket/spacegunexotic.php), [Warship Defenses](https://projectrho.com/public_html/rocket/spacewardefense.php), [Orbital Attack](https://projectrho.com/public_html/rocket/planetaryattack.php), [Orbital Defense](https://projectrho.com/public_html/rocket/planetaryattack3.php).
- Primary sources named there and worth tracing: Glasstone & Dolan for burst effects; the APS directed-energy study (1987) for particle beams; ToughSF's reactor-laser and armour posts; General Atomic's 1965 Orion military applications; Oberg on the Almaz cannon.
