# Intercept Window: Weapons Sweep – Missed Concepts

Nov 2, 2026 · @Teemu

A general web sweep, run in the built-in browser, for realistic and semi-realistic weapon concepts the earlier weapons docs missed. It follows [`studies/weapons-survey-long-range-concepts.md`](weapons-survey-long-range-concepts.md), [`studies/atomic-rockets-weapons-coverage-and-gaps.md`](atomic-rockets-weapons-coverage-and-gaps.md) and [`studies/drives-point-defence-and-kirklin-mines.md`](drives-point-defence-and-kirklin-mines.md). The goal is breadth: each concept gets its physics, an anchor, first-cut numbers, a basis tag (demonstrated, studied, physics-only) and the weapon family it belongs to. Damage modelling, cyber and electronic warfare are other sessions.

## The short version

- **The biggest miss: ultra-relativistic electron beams (UREBs).** Hard-SF communities call them the current "meta". At a few hundred GeV and milliamps, relativistic time dilation keeps a 1 GW beam from spreading for tens of millions of km. **But magnetic fields bend it:** the solar wind's ~5 nT field drifts a 1 TeV beam ~750 km sideways over 10⁶ km. Its reach is set by the picture of the magnetic field, not by spreading. Jupiter's magnetosphere would be a natural shield for the Jovian Entity.
- **Two particle-beam upgrades from ToughSF:** cold, laser-coupled particle beams with nanoradian divergence, and nuclear EFPs (solid metal driven by a nuclear blast), which the Casaba family should absorb.
- **A laser relay network (ToughSF's "Laser Weapon Web")** turns one big laser into a solar-system-wide weapon through cheap refocusing mirrors.
- **High-power microwaves** are now a real anti-satellite claim: a Chinese 20 GW pulsed driver was reported in February 2026. Power-beaming satellites can be weapon-proofed by aperture choice.
- **Real-world anchors since 2020:** a Russian satellite that released a projectile (Kosmos 2543, 2020), a Chinese tug that towed a dead satellite to a graveyard orbit (Shijian-21, 2022), and a reported Russian orbital nuclear anti-satellite programme (2024).
- **Orbit denial by debris** is a strategic weapon with a published estimate: thousands to tens of thousands of tonnes of fine debris to make low-orbit launches costly or impossible, decaying in days to months, so it must be kept up.
- **Early-era guns:** light-gas guns (up to ~8 km/s, demonstrated) and ram accelerators fill the gap between powder guns and railguns.
- **Infrastructure as launchers:** tethers, rotovators, centrifuges and launch loops all throw mass, so all can throw it at someone.
- **Compact plasma toroids (MARAUDER)** are the one "plasma gun" with real hardware behind it, and the one exception to the plasma-gun exclusion.

## Method

Searches run through DuckDuckGo in the built-in browser: general hard-SF weapon lists, ToughSF's archive, Worldbuilding Stack Exchange, Orion's Arm, Isaac Arthur, defence and space-security news, and specific technologies. Pages read in full where they had numbers. Reddit and Stack Exchange answers were blocked to the fetch tool, so the UREB physics comes from the Galactic Library wiki and the arXiv paper already cited in the weapons survey.

## New concepts at a glance

| Concept | Family | Basis | Key numbers | Priority |
| --- | --- | --- | --- | --- |
| Ultra-relativistic electron beams | Particle beams | Physics-only (weapon); accelerators demonstrated | 1 GW at 0.5–1 TeV keeps a 1 cm beam to 30–110 million km before doubling | **High** |
| Cold, laser-coupled particle beams | Particle beams | Studied | Nanoradian divergence; cm-scale spot at 10⁶ km for molecular beams | High |
| Nuclear EFP and nuclear HEAT | Casaba family | Studied | Up to ~21 % of yield into a solid projectile; 1 Mt → 2.7 t at 800 km/s | **High** |
| Laser Weapon Web | Lasers (relay) | Studied | 12 GW FEL in GEO, 200 m reflector, relay nodes ~80 million km apart | High |
| High-power microwaves | New: RF beams | Demonstrated (ground), claimed (anti-satellite) | 20 GW pulses reported (TPG1000Cs, 2026) | Medium |
| Weapon-proof power beaming | Policy and design | Studied | UK Space Solar caps beam intensity at ≤245 W/m² by aperture choice | Medium |
| Co-orbital projectile release | Kinetics | Demonstrated | Kosmos 2543 released a fast object near another satellite (2020) | Medium |
| Grapple-and-tow | Capture | Demonstrated | Shijian-21 docked with a dead satellite and moved it to a graveyard orbit (2022) | Medium |
| Orbital nuclear anti-satellite | Bursts | Reported programme | Linked by US officials to Kosmos 2553 (2024) | Medium |
| Deliberate debris denial | Strategic | Studied | ~6,000 t of fine debris to make launches costly; ~60,000 t to block them (pessimistic) | Medium |
| Compact toroid plasma gun (MARAUDER) | Plasma | Demonstrated (lab) | Shiva Star: 9.5 MJ bank; milligram toroids | Low |
| Light-gas guns | Kinetics | Demonstrated | 1.5–8 km/s | Medium (early eras) |
| Ram accelerators | Kinetics | Demonstrated | ~3 km/s achieved; >8 km/s in principle | Low |
| Rotovators, bolos, tether catapults | Infrastructure launchers | Studied | Tip speeds 1–3 km/s; catapults >30 km/s | Medium |
| Centrifugal launchers | Infrastructure launchers | Demonstrated (suborbital) | SpinLaunch: 33 m centrifuge, ~10,000 g | Low |
| Launch loops | Infrastructure | Studied | Failure is a spectacular hazard | Low |
| Metallic hydrogen | Explosives and propellant | Physics-only | ~200 MJ/kg if metastable, ~20× H₂/O₂ | Low |
| Photon-recycling thrusters | Pushers | Demonstrated (lab) | Recycled photons multiply light pressure | Low |
| Atom lasers ("bosers") | Beams | Physics-only | Coherent matter beams from a condensate | Low |

## Ultra-relativistic electron beams

**The idea.** Electrons are easy to accelerate. At energies of hundreds of GeV and above, time dilation slows the beam's self-repulsion so much that it barely spreads.

**The law** (from the Galactic Library wiki): the distance over which a beam's radius doubles is

**Z ≈ 132 · (γ² − 1)^(3/4) · r / √I** (metres; r in metres, I in amperes)

Computed for a 1 cm beam:

| Electron energy | Current | Beam power | Doubling distance |
| --- | --- | --- | --- |
| 10 GeV | 1 A | 10 GW | ~3,600 km |
| 10 GeV | 0.1 A | 1 GW | ~11,000 km |
| 100 GeV | 10 mA | 1 GW | ~1.1 million km |
| 500 GeV | 2 mA | 1 GW | ~29 million km |
| 1 TeV | 1 mA | 1 GW | ~110 million km (0.8 AU) |

Spreading stops being the limit at a few hundred GeV.

**What limits it: magnetic fields.** A charged beam curves in a field with radius E / (c·B). Computed:

| Beam | Field | Curvature radius | Sideways drift over 10⁶ km |
| --- | --- | --- | --- |
| 1 TeV | Solar wind, ~5 nT | ~670 million km | ~750 km |
| 1 TeV | Low Earth orbit, ~30 µT | ~110,000 km | ~450 km over just 10⁴ km |
| 1 TeV | Outer Jovian magnetosphere, ~100 nT | ~33 million km | ~15,000 km |
| 10 GeV | Solar wind, ~5 nT | ~6.7 million km | ~75,000 km |

- **The beam goes where the field takes it.** Shooting accurately means knowing the field along the whole path. The solar wind's field fluctuates, so a UREB's real reach is limited by **the picture of the magnetic field**, a new picture problem.
- **Planetary magnetospheres are shields.** Near Earth a TeV beam curves within a few hundred km. Jupiter's magnetosphere, far stronger, protects the Jovian Entity against UREBs.

**Damage.** Electrons make an electromagnetic cascade (bremsstrahlung and pair production) that deposits energy deep: a 10 GeV cascade in iron deposits ~98 % within ~35 cm. The pulse also makes an electromagnetic pulse in the target's electronics.

**Counters:** dense high-Z armour followed by hydrogen-rich layers (the wiki suggests ~10 t/m²); magnetic deflection, which bends the beam but sends its bremsstrahlung gammas on undeflected; distance and strong ambient fields.

**Also from the wiki:**
- **Bennett pinch:** in air, a high-current beam ionises its own channel and pinches; SDI-era studies expected 300 MeV electron beams to reach ~80 km altitude. Relevant to orbit-to-surface and surface-to-orbit fire.
- **Neutron beams** don't spread electrostatically but would irradiate the firing ship's own crew.

**Basis:** accelerators at these energies exist on the ground (km-scale); a weapon is physics-only. The arXiv paper already cited in the weapons survey argues long-range relativistic electron beams propagate in the solar wind for propulsion.

## Cold, laser-coupled particle beams

From ToughSF:
- **Cool the ions first** (stochastic, radiative or electron cooling in a storage ring) to near-zero emittance.
- **Let them condense** into molecules or droplets; joining atoms averages out their sideways velocities.
- **Guide them with a laser column** that pushes edge particles back toward the axis, like optical tweezers, over up to ~1,000 km.

**Results (theoretical minimums):** 100 MeV hydrogen at 54 → 5.4 nrad over 1,000 km with ~172 MW of laser; caesium-iodide molecules at 0.7 → 0.035 nrad, a ~3.5 cm spot at 10⁶ km.

**In combat:** excellent against stations and asteroid forts. Against a 10 m warship accelerating at 1 m/s², a 0.07c beam keeps a 100 % hit probability out to ~66,000 km (the dodge law again). Spraying the target's possible positions turns a low hit chance into a steady, lower damage rate.

**Counters:** magnetic-shield drones, plasma bubbles, counter-beams that heat the incoming beam, and lasers, which arrive first.

## Nuclear EFP and nuclear HEAT

From ToughSF. Variants of the nuclear shaped charge that drive **solid metal** instead of plasma:

- **Nuclear EFP:** a shallow metal plate, spaced from the device so the gas cools before it reaches the plate. Upper bound ~21 % of yield into the projectile (85 % directivity × 50 % filler × 50 % plate); practical 5–10 %.
  - 1 kt → over 21 t of metal at ~9 km/s.
  - Spaced, 1 Mt → 2.7 t at ~800 km/s; 10 m spacing gives 16.7 kg at 324 km/s.
- **Nuclear HEAT:** a steep cone makes a jet with a 60–90 km/s tip, but it fragments within metres, so it's a contact weapon.

**Why it matters:** a solid projectile holds together over distance where a plasma cone spreads, so the spaced NEFP's range is set by the dodge law, not by the cone. It belongs in the Casaba family as a spec option: plasma cone (Casaba), solid slug (NEFP), contact jet (HEAT).

## Laser Weapon Web

From ToughSF. A system-wide laser built from cheap parts:

- **A ground nuclear plant** beams power to relay satellites, which feed a **12 GW free-electron laser in GEO** at 200 nm with a **200 m, 1 mm-thick aluminium reflector**.
- **Refocusing mirror nodes** pick up the beam and pass it on. Node spacing is ~82 million km, so Mars needs about six nodes, with losses of a few per cent.
- **The beam stays on.** The last node deflects it onto a target when one appears, so only the final leg needs aiming in real time.
- **A targeting ship** can do the last focusing step close to the target.
- **Weaknesses:** the nodes are fragile and can be ambushed or hijacked; the web can't track accelerating ships well; replacement in wartime is slower than destruction.

**Design hook:** a beamed-propulsion or power-relay network is this web before it's armed. It fits the dual-use theme in the weapons survey.

## High-power microwaves

- **What:** broadband or narrowband RF pulses that upset or burn out electronics.
- **Anchors:** US Navy and DoD HPM programmes (counter-drone); Chinese researchers reported a compact ~20 GW pulsed driver (TPG1000Cs, February 2026; claims of satellite threat, tracking unproven).
- **In space:** wavelengths of centimetres diffract far worse than light, so an HPM weapon needs enormous antennas for range. Short-range soft kill, or a ground-to-low-orbit attack.
- **Weapon-proof power beaming:** UK Space Solar sizes its transmitting and receiving apertures so the beam can't exceed ~245 W/m², a quarter of sunlight. **Beam intensity limits by design are a charter or treaty clause the game can use:** a power satellite certified non-weapon by its aperture, and a rung-2 act if refitted.

## Real-world anchors since 2020

| Event | What it shows | Basis |
| --- | --- | --- |
| Kosmos 2543 released a fast object near another satellite (2020) | Satellites that carry and fire projectiles in orbit | Demonstrated |
| Shijian-21 docked with a dead Beidou satellite and towed it to a graveyard orbit (2022) | Capture-and-move: the non-destructive kill | Demonstrated |
| US officials linked Kosmos 2553 to a Russian orbital nuclear anti-satellite programme (2024) | Nuclear weapons in orbit are back on the table | Reported |
| Golden Dome space-based interceptor awards (2026) | Orbital interceptor fleets | In development |
| Chinese 20 GW HPM driver (2026) | Microwave anti-satellite claims | Claimed |

## Orbit denial by debris

- **The weapon is the environment.** A published estimate (Forethought): about 6,000 t of fine debris spread through low Earth orbit would make launches beyond Earth far more expensive, and about 60,000 t could block them on pessimistic assumptions; real requirements could be 10–1,000 times higher.
- **It decays.** Small particles fall out in days to months, so denial must be kept up.
- **It's visible.** Lifting thousands of tonnes is hard to hide, and launch sites can be watched.
- **Shielding beats it:** a Whipple bumper on a Falcon 9-sized rocket adds about 10 t against worst-case fragments.
- **Air University frames the cascade as a denial tool** for actors who don't depend on orbit, which is exactly the asymmetric position of a belt or outer-system polity against Earth.

## Early-era guns

| Gun | Muzzle velocity | Notes | Basis |
| --- | --- | --- | --- |
| Powder gun (Almaz cannon) | ~0.7–1 km/s | The demonstrated starting point | Demonstrated |
| Light-gas gun (two-stage, hydrogen) | 1.5–8+ km/s | Lab standard for hypervelocity tests; bulky, slow to reload | Demonstrated |
| Combustion or arc light-gas gun | similar | Self-contained variants | Studied |
| Ram accelerator | ~3 km/s achieved; >8 km/s in principle | Scramjet-like barrel; can fire ton-scale guided rounds | Demonstrated (lab) |
| Gyrojet-style rocket rounds | low | Almost recoilless, for small arms in free fall | Demonstrated (historical) |

These fill the kinetic ladder below the railgun, for the chemical era.

## Infrastructure as launchers

| System | What it throws | Basis |
| --- | --- | --- |
| Rotovators and bolos | Payloads at 1–3 km/s from the tip | Studied |
| Tether catapults | Above 30 km/s in principle | Studied |
| Centrifugal launchers | Suborbital payloads at ~10,000 g (SpinLaunch, 33 m) | Demonstrated (suborbital) |
| Launch loops | Payloads to orbit; a failure scatters a fast iron ribbon | Studied |

On airless bodies these are kinetic bombardment launchers by default, like lunar mass drivers.

## Smaller finds

- **Compact toroid plasma gun (MARAUDER, USAF, 1990s):** accelerated self-confined plasma rings of milligrams on the Shiva Star capacitor bank (9.5 MJ). The one plasma gun with real hardware; still short-range. A logged exception to the plasma-gun exclusion is not needed, since it is real physics.
- **Metallic hydrogen:** if it could be kept metastable, ~200 MJ/kg, about twenty times hydrogen–oxygen combustion. An explosive or propellant at the physics-only end.
- **Photon-recycling thrusters:** bouncing laser light between mirrors multiplies the push; a short-range shove for the ion-beam-shepherd class of gray-zone tools.
- **Gravity tractor:** a craft hovering near an asteroid tugs it by gravity alone; a silent, slow way to redirect a rock.
- **Atom lasers ("bosers"):** coherent beams of atoms from a Bose–Einstein condensate exist in labs; Orion's Arm weaponises them. Physics-only.
- **Ion bunches stored in rings** and released in milliseconds: pulse power for particle beams.
- **Electrodynamic tethers** deorbit satellites; attached to someone else's, they're a slow capture-and-drop.

## What to add to the weapon blocks

| Family | Addition |
| --- | --- |
| **Particle beams** | UREB as a spec point (energy, current, beam radius); the magnetic field picture as the range limit; cold laser-coupled beams as an engineered upgrade (emittance, laser column) |
| **Nuclear shaped charge** | Projectile type as a spec choice: plasma cone, spaced solid slug (NEFP), contact jet (HEAT) |
| **Lasers** | Relay networks as installations: node count, spacing and reflectivity |
| **RF beams (new)** | High-power microwaves: power, aperture, frequency; soft kill of electronics at short range |
| **Kinetics** | Light-gas guns and ram accelerators below railguns; co-orbital projectile release |
| **Strategic** | Orbit denial: debris mass, orbit band, decay rate |
| **Capture** | Grapple-and-tow, nets, harpoons, ion shepherds as one non-destructive family |
| **Infrastructure** | Tethers, centrifuges and loops as launchers with a weapon use |

## Open questions

- [ ] The magnetic field picture: should the solar wind's field be modelled (a slowly varying field map with uncertainty), so UREB aim error grows with range like the bloom?
- [ ] Magnetospheres as terrain: Earth's and Jupiter's fields deflect charged beams; with the radiation dose field already proposed, they make planets natural fortresses.
- [ ] UREB counters: armour mass per m² against cascades, and how the generator's layer stack handles high-Z plus hydrogenous layers.
- [ ] Do power-beaming satellites get a certified maximum intensity as a charter clause?
- [ ] Debris denial: does the debris-evolution study need a "deliberate dispersal" case?

## Sources

- UREBs: [Galactic Library, Particle Beam Weapons](https://www.galacticlibrary.net/wiki/Particle_Beam_Weapons); [geometrian, UREB ship](https://geometrian.com/projects/art/urebship/) (page unreadable to the fetch tool); [long-range relativistic electron beams, arXiv 2407.09414](https://arxiv.org/pdf/2407.09414v3).
- ToughSF: [Cold, Laser-Coupled Particle Beams](https://toughsf.blogspot.com/2019/02/cold-laser-coupled-particle-beams.html); [Nuclear EFP and HEAT](https://toughsf.blogspot.com/2017/05/nuclear-efp-and-heat.html); [Laser Weapon Web](https://toughsf.blogspot.com/2016/04/lww-laser-weapon-web.html); [Fusion without Fissiles](https://toughsf.blogspot.com/2022/03/fusion-without-fissiles-superbombs-and.html); [Electric Cannons and Kinetic Impactors](https://toughsf.blogspot.com/2016/03/electric-cannons-and-kinetic-impactors.html).
- Microwaves and power beaming: [The Defense News on the TPG1000Cs](https://www.thedefensenews.com/China-Claims-Development-of-20-Gigawatt-Microwave-Weapon-Capable-of-Damaging-Low-Earth-Orbit-Satellites/); [ONR high-power microwaves](https://www.onr.navy.mil/organization/departments/code-35/division-353/directed-energy-weapons-high-power-microwaves); [Space Solar safety FAQ](https://www.spacesolar.co.uk/faqs-category/societal-and-safety/).
- Real-world anchors: [US Space Command on Kosmos 2543](https://www.spacecom.mil/Newsroom/News/Article-Display/Article/2285098/russia-conducts-space-based-anti-satellite-weapons-test/); [SpaceNews on Shijian-21](https://spacenews.com/chinas-shijian-21-spacecraft-docked-with-and-towed-a-dead-satellite/); [Kosmos 2553](https://en.wikipedia.org/wiki/Kosmos_2553).
- Debris denial: [Forethought, space debris and launch denial](https://www.forethought.org/research/space-debris-and-launch-denial); [Air University, ablation cascade risks](https://www.airuniversity.af.edu/Office-of-Sponsored-Programs/Research/Article-Display/Article/3804145/risks-to-the-strategic-domain-of-space-from-an-ablation-cascade/).
- Guns and launchers: [Light-gas gun](https://en.wikipedia.org/wiki/Light-gas_gun); [Ram accelerator](https://en.wikipedia.org/wiki/Ram_accelerator); [SF Worldbuilding, kinetic weapons](https://sfworldbuilding.blogspot.com/2015/01/future-weapons-kinetic.html); [Momentum exchange tether](https://en.wikipedia.org/wiki/Momentum_exchange_tether); [SpinLaunch](https://en.wikipedia.org/wiki/SpinLaunch); [Launch loop](https://en.wikipedia.org/wiki/Launch_loop).
- Other: [MARAUDER and Shiva Star](https://www.researchgate.net/publication/224274894_Shiva_Star_-_Marauder_Compact_Torus_System); [Metallic hydrogen (Silvera)](https://web.stanford.edu/~cantwell/AA283_Course_Material/AA283_Resources/References/Silvera_metallic_hydrogen_paper.pdf); [Photonic laser thruster](https://encyclopedia.pub/entry/32250); [Gravity tractor](https://en.wikipedia.org/wiki/Gravity_tractor); [Orion's Arm weapons index](https://www.orionsarm.com/eg-topic/45b6caa75cbe4).
