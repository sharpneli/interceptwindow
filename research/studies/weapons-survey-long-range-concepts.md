# Intercept Window: Weapons Survey – Long-Range Concepts

Nov 2, 2026 · @Teemu

A survey of realistic and semi-realistic weapon concepts, with weight on the ones that reach further than the usual tens-to-thousands of kilometres: fast kinetics, fixed laser installations, nuclear-driven beams, particle beams and short-wavelength (X-ray and gamma) beams. It feeds the Atomic Rockets survey and the beams, kinetic-launcher and warhead-conversion studies in [`studies/research-agenda.md`](research-agenda.md), and fills the "Not yet estimated" rows of [`design/combat-ranges-and-group-tracks.md`](../design/combat-ranges-and-group-tracks.md). The X-ray and gamma FEL idea has its own deep dive in [`studies/strategic-beams-x-ray-and-gamma-fels.md`](strategic-beams-x-ray-and-gamma-fels.md).

All numbers are first-cut estimates, computed from the scaling laws in the ranges doc. The structure (what limits each family, what it can threaten, what counters it) is the part to keep.

## The short version

- **Long range is real, but only against predictable targets.** Past about a light-second, every weapon's reach is set less by its own physics than by the target's freedom to move during the round trip and by how well the shooter knows where the target is.
- **A weapon can't outshoot its picture.** A beam that can put a 50 m spot at 1 AU is useless if the polity's sensors can only fix the target to 15 km there ([`design/detection-and-the-picture.md`](../design/detection-and-the-picture.md)). The shooter then has to sweep the whole error box, and the cost of a kill becomes energy × area.
- **That splits weapons into two tiers.** *Tactical* weapons (guns, warship lasers, missiles) fight ships that dodge, at the ranges in the ranges doc. *Strategic* weapons (km-scale laser arrays, X-ray and gamma beams, relativistic projectiles) threaten things that can't dodge or don't know to: stations, habitats, mines, sensors, power arrays, coasting ships on known arcs.
- **Most strategic weapons are dual-use infrastructure.** A planetary-defence laser, a laser-sail launcher, a lunar mass driver and an Orion drive's pulse units are all weapons with another job. That is a good fit for the gray-zone and treaty layer.
- **Shorter wavelength buys range only if you can still point and focus it.** Diffraction range grows as aperture / wavelength. X-rays and gammas shrink the wavelength by 10³–10⁶, but there are almost no optics for them, so the beam is only as wide as its source, and pointing at picoradians becomes the limit.
- **Gamma beams are crew and electronics killers, not hole punchers.** They pass through decimetres of hull and deposit dose. About 300 J/m² of 1 MeV gammas gives 1 Gy, so sweeping a whole 15 km error box to a lethal 10 Gy takes under 1 TJ. Vaporising even a centimetre of aluminium across that box would take about a hundred thousand times more.

## What limits range

Each family is limited by one of five things. They scale differently with tech, which is what makes the range ladder shift by era.

| Limit | Applies to | Scales as | What beats it |
| --- | --- | --- | --- |
| **Diffraction** | Lasers, all beams | Spot ≈ 2.44 λ R / D | Bigger aperture, shorter wavelength |
| **Dodge** | Unguided kinetics | R ≈ v √(2s / a) | Faster projectile, bigger cloud, less agile target |
| **Δv duel** | Missiles, kill vehicles, smart pellets | R ≈ v_close · Δv_missile / a_target | Missile Δv and acceleration |
| **Light-lag bloom** | Every weapon, decisively for beams | Bloom ≈ ½ a (2R/c)² | Only target agility (or target predictability) |
| **The picture** | Every weapon | Fix error from `Detection and the Picture.md` (σR ≈ R² σθ / B) | Sensor baseline, depth, active ranging |

Two derived rules:

- **The bloom grows with the square of range,** so even a milli-g jink defeats a point-aimed beam at AU distances. At 1 AU the round trip is about 1,000 s: a station random-walking at 10⁻³ m/s² can be anywhere in a 500 m sphere, a ship at 0.01 m/s² in a 5 km one, a ship at 1 g in a 5,000 km one.
- **Pointing precision is bounded by the sensor's own resolution.** You can't aim more finely than you can see the target's image. For an IR sensor that's about (λ/D) / SNR, tens of nanoradians at best for a large telescope, far coarser than what an X-ray or gamma beam's diffraction would allow.

## Reality ladder

How firmly each concept is grounded. "Status" is about the physics and engineering, not the weapon as a system.

| Concept | Status | Basis |
| --- | --- | --- |
| Hit-to-kill interceptors (KKVs) | Demonstrated | ABM and ASAT tests; Brilliant Pebbles hardware |
| Solid-state and fibre lasers, kW–100 kW | Demonstrated | Fielded naval and air-defence systems |
| Neutral particle beam in space | Demonstrated (sub-weapon) | BEAR, 1989 |
| Hard X-ray FEL | Demonstrated (lab, watts) | European XFEL, LCLS, SACLA |
| Nuclear shaped charge | One known test | Operation Grenadier, 1985 |
| Bomb-pumped X-ray laser | Tested, results contested | Project Excalibur, ~10 tests 1978–88 |
| Kinetic bombardment | Studied | Project Thor, USAF 2003 study |
| Km-scale phased laser arrays | Studied | DE-STAR, Breakthrough Starshot |
| Laser-sail and pellet-stream launchers at 0.01–0.2c | Studied, far engineering | Starshot, Singer, Nordley |
| Coherent gamma-ray FEL | Physics allowed, far beyond today | FEL scaling; emittance needs ~10–100× today's |
| Graser (nuclear isomer gamma laser) | Unsolved physics | Decades of failed or contested attempts |
| Relativistic kill vehicles (0.5c+) | Physics allowed, energy absurd for this era | Out of scope except as a ceiling |
| Nicoll-Dyson beam, stellar engines | Speculative megastructure | Out of scope |

## Kinetics

### Unguided slugs and clouds

Covered in [`design/combat-ranges-and-group-tracks.md`](../design/combat-ranges-and-group-tracks.md): range grows as v / √a, so it stays near 100 km until macron speeds. What this survey adds is what happens when the projectile gets *much* faster and the target is *much* less agile.

Dodge-limited range, R = v √(2s/a), for a miss tolerance s of 10 m (a single hull) or 1 km (a projectile cloud or a large station):

| Projectile speed | vs station jinking at 10⁻³ m/s², s = 10 m | Same, s = 1 km cloud | vs warship at 0.1 m/s², s = 10 m | Time to cross 0.1 AU |
| --- | --- | --- | --- | --- |
| 1,000 km/s (torch macrons) | 1.4×10⁵ km | 1.4×10⁶ km | 14,000 km | 4.2 h |
| 0.01c (3,000 km/s) | 4.2×10⁵ km | 4.2×10⁶ km | 42,000 km | 1.4 h |
| 0.1c | 4.2×10⁶ km | 0.28 AU | 4.2×10⁵ km | 8 min |
| 0.2c | 8.5×10⁶ km | 0.57 AU | 8.5×10⁵ km | 4 min |

The aim error from the picture adds to this: a dumb projectile only hits if the shooter's fix is better than s.

**Energy on target.** 1 kg at 10 km/s carries about 12 kg of TNT equivalent; at 1,000 km/s about 0.12 t; at 0.01c about 1 kt; at 0.1c about 110 kt; at 0.2c about 440 kt. Velocity, not mass, is the lever.

### Guided kill vehicles (KKVs)

- **What:** a small rocket that rams the target. No warhead; the closing speed is the warhead.
- **Grounding:** Brilliant Pebbles (SDI, 1989–93) planned several thousand interceptors of 50–100 kg in low orbit, each with a kill vehicle of only a few kg to about 20 kg, sized to kill boosting ICBMs. Hover tests ran until 1992.
- **Range:** the Δv duel in the ranges doc. A KKV is a missile without a warhead, so it is cheaper, smaller and colder, which delays the target's dodge clock.
- **Game hook:** the cheap swarm interceptor. Thousands of small, cold, autonomous pebbles parked along approach corridors are a defensive minefield that the detection model makes hard to see.

### Macron guns and smart pellets

- **What:** coilguns or electrostatic accelerators firing tiny projectiles (grams down to micrograms) at hundreds to thousands of km/s. "Smart pellets" (G. David Nordley's idea, also used in Orion's Arm) add a few nanograms of guidance and homing.
- **Grounding:** ToughSF's long-range coilgun analysis argues pellet guns don't lose energy with distance and can be very efficient, unlike beams. Singer's 1979 pellet-stream propulsion concept is the same machine pointed at a sail.
- **Range:** dumb pellets follow the table above. Smart pellets turn the dodge limit into a Δv duel with a tiny projectile, which is cheap to give a small Δv but hard to give much acceleration.
- **Game hook:** the torch-era gun that outranges lasers against agile ships, as long as the picture is good. Also a strategic area weapon: a 1 km pellet cloud at 0.01c threatens a station at millions of km.

### Laser-sail projectiles

- **What:** a light sail pushed by a ground or space laser array. Breakthrough Starshot's reference design uses a phased array of about 100 GW, km-scale, to push gram-scale craft to about 0.2c in a few minutes.
- **As a weapon:** a 1 g sail at 0.2c carries about 1.9 TJ (roughly 0.44 kt). The launch costs about 18 TJ of beam energy (100 GW for about 3 minutes), so it is an inefficient but very long-range delivery.
- **The bigger threat is the launcher itself.** A 100 GW array a few km across, at about 1 µm, is a laser that puts a spot about 100 m across at 1 AU. A Starshot-class launcher is a strategic beam weapon whether anyone calls it one or not.
- **Game hook:** the interstellar-probe programme that every neighbour reads as a superweapon. Pure dual-use.

### Relativistic kill vehicles

- **What:** projectiles at a large fraction of c. Energy grows past rest-mass energy: 1 kg at 0.99c is about 130 Mt.
- **In this game's era:** reaching 0.1c with kilogram masses needs launch infrastructure on the scale of the Starshot array or larger, so RKVs belong at the far end of the torch era or beyond. At 0.01c (≈1 kt per kg) they are already strategic.
- **Limits:** no terminal guidance to speak of, so they hit only predictable targets (planets, stations, slow ships). Any matter in the path destroys them; a cloud of sand in their way is a shield.
- **Defence:** see the launch (the launcher is huge and hot), compute the track, put something in the way or nudge the projectile early. A tiny deflection far out becomes a large miss.

### Kinetic bombardment and redirected rocks

- **Project Thor** ("rods from God"): a tungsten rod 6.1 m by 0.3 m (about 8 t) hitting at Mach 10 carries about 48 GJ, roughly 11.5 t of TNT, per the 2003 USAF estimate. Orbital velocity is about 8 km/s, but the rod arrives at about 3 km/s after atmospheric drag.
- **Heliocentric drops are far stronger.** A rock falling in from the belt arrives at 10–30 km/s; energy goes as v², so 10–100× a Thor rod per kg.
- **Asteroid redirection** is the slow, visible, deniable-until-it-isn't WMD. The planetary-defence systems built against it (lasers, impactors) are themselves weapons.
- **Lunar mass drivers** (built for exports) are bombardment launchers by default.
- **Legality hook:** the Outer Space Treaty bans orbital nuclear, chemical and biological weapons but not inert kinetics, so kinetic bombardment sits in the gray zone the design already uses.

## Lasers

### Warship lasers

Covered in the ranges doc: R ∝ D √P / λ, topping out around 10⁵ km for a warship in the torch era. CoaDE's experience agrees that lasers are mainly point defence until they get very large, and that multi-GW UV lasers end up on stations because of power and radiator mass.

### Fixed phased-array installations

- **What:** modular arrays of phase-locked kW-class lasers, km across, powered by large solar arrays.
- **Grounding:** Lubin's DE-STAR studies.
  - DE-STAR 1 (10 m array) evaporates space debris at about 10⁴ km.
  - DE-STAR 4 (10 km array) engages asteroids beyond 1 AU and can fully evaporate a 500 m asteroid within a year.
  - Lubin's popular description puts a 70 GW array's spot at about 30 m at 1 AU. The ranges-doc formula agrees: a 10 km aperture at 1.06 µm gives a 39 m spot at 1 AU, about 60 MW/m² from 70 GW.
- **As a weapon:** an AU-range beam against anything predictable. Against a manoeuvring ship it is limited by the bloom and the picture, not diffraction.
- **Game hook:** the "planetary defence" installation every polity wants and every rival fears. It's large, fixed, hot and slow to build: a high-value target and a casus belli in its own right.

### Relay mirrors and lens drones

- **What:** drones that carry large focusing mirrors forward, so a ship's laser is refocused close to the target. Both a LessWrong piece on "helio-selenic" drone telescopes and Strange Horizons' survey of deep-space weapons describe the idea.
- **Range:** extends the effective aperture to the drone's mirror, near the target.
- **Limits:** the mirror must hold position within its own focusing range, and the target will shoot it. Likely good for one or two shots.
- **Game hook:** a consumable that turns a short-range laser into a long-range one. Pairs with the missile layer.

### Dazzlers: the anti-sensor laser

- **Why it matters:** sensors are built to collect faint light, so they fail at intensities millions of times below what damages a hull. A 1 MW laser with a 1 m mirror still delivers about 20 W/m² at 10⁵ km. Focused by a target's 1 m telescope, that is over 10 W on a detector built to see 10⁻¹⁷ W/m² stars. Even at 1 AU the same laser still puts microwatts into the telescope, far above any star.
- **Out-of-band filtering is the defence,** so a **tunable** laser (an FEL) that can hit the sensor's own band is the attacker's answer.
- **Game hook:** blinding is the long-range laser mission long before killing is. It matches `Detection and the Picture.md`'s "sensors are the first targets" and gives every laser a strategic anti-sensor role.

## Nuclear-driven weapons

### Bare bursts

In vacuum there's no blast wave. A burst's output is mostly X-rays, falling as 1/R². Effective radius is tens of km for megatons against soft targets. To the bursts study.

### Nuclear shaped charges (Casaba-Howitzer)

- **What:** a nuclear device that channels much of its output into a narrow jet of plasma or particles. It grew out of Project Orion's pulse units, which were shaped charges aimed at the pusher plate.
- **Grounding:** Casaba-Howitzer (1960s, ARPA) is still largely classified. The only known nuclear shaped-charge test, in Operation Grenadier (1985), drove about 1 kg of tungsten and molybdenum to 70 km/s from an 8 kt device, about 0.007 % efficiency.
- **Fan estimates:** Lowther and Chung (Atomic Rockets) estimate a Casaba charge at about 115 kg and around 5 kt. These are secondary-source guesses, not data.
- **Range:** set by the jet's cone angle and the projectiles' dodge limit. Plausibly hundreds to a few thousand km against ships.
- **Game hook:** an Orion drive is a magazine of shaped charges pointed the wrong way. Turning pulse units into weapons is a refit, a doctrine change and a treaty breach all at once.

### Bomb-pumped X-ray lasers (Project Excalibur)

- **What:** a nuclear device surrounded by lasing rods; the burst pumps each rod for a nanosecond-scale pulse of soft X-rays before everything is destroyed.
- **Grounding:** Livermore's programme under SDI. Up to about fifty rods per device were envisioned, each aimed at a separate target. About ten known tests ran from 1978 to 1988. One account claimed several hundred terawatts at 1.4 nm; that was never officially confirmed. Results were disputed, the budget was cut in 1988 and the last planned test was cancelled in 1992.
- **Range:** with no mirrors, the beam divergence is about √(λ/L) for a rod of length L. At 1.4 nm that's about 37 µrad for a 1 m rod and 12 µrad for a 10 m rod, so a spot of 12–37 m at 1,000 km and 120–370 m at 10,000 km. Effective against fragile targets out to roughly 10³–10⁴ km, which matches the "hundreds or thousands of km" in period descriptions.
- **Game hook:** a one-shot, multi-target, nuclear point-defence or ambush weapon. A nuke that hits fifty things at a thousand km is a different weapon from a nuke that hits one thing at ten.

## Particle beams

- **Neutral particle beams.** Charged beams blow themselves apart and are bent by magnetic fields, so space weapons strip and neutralise them. The BEAR experiment (July 1989) flew a neutral hydrogen beam accelerator to about 200 km altitude, operated it and propagated the beam as predicted. SDI saw them first as decoy discriminators, then as hard-kill weapons.
- **Range:** set by divergence, which has a thermal floor around 0.2 µrad (Benford's analysis, as summarised by ToughSF). Weapon-class divergence of about 1 µrad would give a 1 m spot at 1,000 km and 10 m at 10⁴ km. First cut: thousands to tens of thousands of km.
- **Damage:** deep penetration and volumetric deposition, like gamma rays: electronics and crew first, structure much later. Mirrors don't help the target.
- **Relativistic electron beams** may propagate far further in the solar-wind plasma than older analyses thought; a 2024 arXiv paper argues for ranges beyond 100 AU for propulsion. Treat as speculative.
- **Game hook:** the mid-range radiation weapon. Out-ranges warship lasers in some eras, can't be reflected, and is the natural precursor to gamma beams.

## Short-wavelength beams: X-ray and gamma

The deep dive is [`studies/strategic-beams-x-ray-and-gamma-fels.md`](strategic-beams-x-ray-and-gamma-fels.md). In brief:

- **Hard X-ray FELs exist today.** The European XFEL reaches 0.05 nm from a 17.5 GeV linac, but at watts of average power and about 1.5 % extraction efficiency at best in high-power FELs.
- **A gamma FEL needs roughly 40–70 GeV electrons for 1 MeV photons,** and a beam quality 10–100× better than today's best. That's a late-era technology block, not a near-future one.
- **Without optics, the beam is as wide as its source,** but at gamma wavelengths that's enough: a 1 mm source diverges at about 0.4 nrad, a spot about 120 m across at 1 AU.
- **The real limits are pointing, the picture and the bloom.** So a gamma beam sweeps error boxes, and it can afford to because it kills crews with little energy per square metre.
- **Grasers** (gamma lasers from nuclear isomers) remain unsolved physics; a game can use them only as a speculative tech.

## The far end (out of scope, as ceilings)

- **Nicoll-Dyson beam:** a Dyson swarm used as one phased-array laser, a star's output as a weapon at light-year ranges. Useful only as a reminder of where the scaling laws go.
- **Stellar engines** (Shkadov and Caplan thrusters) move stars over millions of years. Not weapons on any game timescale.
- **Antimatter:** a fuel and a warhead; storage failure is a burst. To the warhead conversion study.

## Ranges by era, with the strategic tier

Extends the table in [`design/combat-ranges-and-group-tracks.md`](../design/combat-ranges-and-group-tracks.md). The tactical columns are copied from there; the strategic column is new and assumes a predictable target and a good picture.

| Era | Tactical reach (vs agile ships) | New long-range options | Strategic reach (vs predictable targets) |
| --- | --- | --- | --- |
| Chemical | Missiles ~10⁴ km | KKV swarms; kinetic bombardment; bare nukes | Orbital bombardment of a planet below |
| Fission / NTR | Missiles ~5×10⁴ km; lasers ~600 km | Nuclear shaped charges; bomb-pumped X-ray lasers; neutral particle beams | ~10³–10⁴ km (one-shot nuclear beams) |
| Fusion | Missiles ~3×10⁵ km; lasers ~7,000 km | Km-scale laser arrays (DE-STAR class); relay mirrors; macron guns; dazzlers | ~1 AU for fixed arrays; system-wide for blinding sensors |
| Torch | Missiles ~10⁷ km; lasers ~1.5×10⁵ km | Laser-sail launchers; pellet streams at 0.01c; X-ray FEL installations | ~1 AU for beams; 0.1–0.5 AU for fast projectiles |
| Late torch / beyond | — | Gamma FELs; RKVs at 0.1c | Inner system for beams, limited by picture and sweep energy |

## What this means for design

- **A strategic tier emerges on its own.** No special rules are needed: the same scaling laws that set tactical ranges make huge fixed installations reach AU distances against targets that can't dodge. The design question is only what those installations cost and who is allowed to build them.
- **Predictability becomes a liability.** Stations, habitats, mines, solar farms and anything coasting on a published trajectory can be shot from very far away. Counters, in order of cost:
  - **jitter:** milli-g random station-keeping inflates the bloom at AU range from metres to hundreds of metres;
  - **shielding:** propellant, water and regolith against gammas and particles; reflective and ablative layers against lasers;
  - **occlusion:** hide behind a body; there is no line of sight through a planet;
  - **deterrence:** hold the shooter's own fixed installations at risk;
  - **blinding:** kill the shooter's sensors; a long-range beam with a bad picture has to sweep a bigger box.
- **Envelopes and declared trajectories get teeth.** A freighter on its declared trajectory is predictable, and so shootable. That's a reason to deviate, which inspection then sees as a violation.
- **Dual-use infrastructure is the arms race.** Planetary defence, interstellar probes, power beaming and export mass drivers all build strategic weapons as a side effect. Treaties can't ban the capability, only argue about intent.
- **Sensors are the hinge.** Every strategic weapon needs a picture good enough to point it. Detection investment and anti-sensor attacks decide who can use the long reach.

## Open questions

- [ ] Damage thresholds for gamma and particle beams against crew, electronics and structure, as a function of shielding mass (beams study and radiation-and-crew study).
- [ ] Sweep model: how a beam covers an error box (raster, statistical spray, re-acquisition after a partial fix), and what that does to hit probability.
- [ ] Jitter costs: propellant and power for a station to random-walk at 10⁻⁴–10⁻³ m/s² continuously.
- [ ] Pointing tech block: what stability a fixed installation can reach (Hubble-class tens of nrad, interferometric beyond), and how it scales.
- [ ] Do strategic installations need a separate treaty and incident model, or does the existing defiance ladder cover them?
- [ ] Macron and smart-pellet launcher numbers for the kinetic-launchers study.
- [ ] Casaba-Howitzer cone angle and energy fraction from the declassified Orion material (warhead conversion study).

## Sources

- Laser range and space combat: [ToughSF, guns and shields](https://toughsf.blogspot.com/2016/08/space-warship-design-ii-guns-and-shields.html); [ToughSF, the solution to long range space combat](https://toughsf.blogspot.com/2016/10/the-solution-to-long-range-space-combat.html?m=1); [Strange Horizons, weapons of deep space warfare](https://strangehorizons.com/wordpress/non-fiction/articles/hunters-in-the-great-dark-part-2-the-weapons-of-deep-space-warfare/); [LessWrong, helio-selenic laser telescope](https://lesswrong.com/posts/vRdtKig3QEiCyaYLs/helio-selenic-laser-telescope-in-space).
- Children of a Dead Earth: [TV Tropes summary](https://tvtropes.org/pmwiki/pmwiki.php/Videogame/ChildrenOfADeadEarth); [Steam discussion of weapon roles](https://steamcommunity.com/app/476530/discussions/0/152391285464575750/?l=finnish).
- Brilliant Pebbles: [GlobalSecurity](https://www.globalsecurity.org/space/systems/bp.htm); [Aerospace Projects Review](https://www.aerospaceprojectsreview.com/blog/?p=1420).
- Breakthrough Starshot: [IEEE Spectrum](https://spectrum.ieee.org/how-do-you-fly-to-alpha-centauri-in-just-20-years-ride-a-laser-beam); [Universe Today on the laser array](https://www.universetoday.com/151478/sending-a-spacecraft-to-another-star-will-require-a-million-lasers-working-together).
- Relativistic kill vehicles: [Orion's Arm RKKS](https://www.orionsarm.com/eg-article/4771ba89da222).
- Kinetic bombardment: [Wikipedia, Kinetic bombardment](https://en.wikipedia.org/wiki/Kinetic_bombardment).
- DE-STAR: [Lubin et al., Toward directed energy planetary defense](https://dspace.mit.edu/handle/1721.1/88427); [Lubin, Directed Energy Missions for Planetary Defense](https://arxiv.org/pdf/1604.03511); [Popular Science interview](https://www.popsci.com/science/article/2013-06/death-star/).
- Nuclear shaped charges: [Wikipedia, Nuclear shaped charge](https://en.wikipedia.org/wiki/Nuclear_shaped_charge); [Wikipedia, Casaba-Howitzer](https://en.wikipedia.org/wiki/Casaba-Howitzer); [ToughSF, The Nuclear Spear](https://toughsf.blogspot.com/2016/06/the-nuclear-spear-casaba-howitzer.html?m=1); [NextBigFuture on Lowther and Chung's estimates](https://www.nextbigfuture.com/2018/09/orion-space-battleships-could-still-be-built-in-a-nuclear-space-race.html).
- Project Excalibur: [Wikipedia](https://en.wikipedia.org/wiki/Project_Excalibur); [Rocketry Forum quoting OPN's X-ray laser history](https://www.rocketryforum.com/threads/sdi-program-nuclear-warhead-pumped-x-ray-laser.163413/latest).
- Neutral particle beams: [BEAR, GlobalSecurity](https://www.globalsecurity.org/space/systems/bear.htm); [Smithsonian BEAR accelerator](https://si.edu/object/neutral-particle-beam-accelerator-beam-experiment-aboard-rocket%3Anasm_A20070004000); [Gsponer, particle beam propagation](https://arxiv.org/pdf/physics/0409157); [long-range relativistic electron beams, arXiv 2407.09414](https://arxiv.org/pdf/2407.09414v3); [Centauri Dreams on beam divergence](https://centauri-dreams.org/?p=31411).
- Nicoll-Dyson and stellar engines: [Orion's Arm](https://orionsarm.com/eg-article/48fe49fe47202); [Universe Today, Shkadov thruster](https://www.universetoday.com/103896/could-we-move-the-sun/).
- Detection formula and stealth: [ToughSF, stealth in space](https://toughsf.blogspot.com/2016/03/stealth-in-space-is-possible.html?m=1).
