# Intercept Window: Detection and the Picture

Nov 1, 2026 · @Teemu

What a polity can know about a ship, how it learns it, what it costs, and what the player sees. The starting point is "there ain't no stealth in space": anything burning hard can't hide. But being seen gives a bearing, not a position. The numbers are first-cut estimates for the detection study ([`studies/research-agenda.md`](../studies/research-agenda.md)); the structure is the part to keep.

## The short version

- **Space isn't stealthy, it's foggy.** The fog is in range, count, identity and intent, not in whether something is there.
- **A passive sensor gives an excellent bearing and no range.** A contact seen by one sensor is a needle along the line of sight.
- **Range is bought,** with one of:
  - baseline (several sensors, triangulation);
  - time (watching a coasting arc curve);
  - Δv (manoeuvring the observer);
  - emissions (radar, lidar);
  - assumptions (brightness plus a guessed class, as good as the identification).
- **Light-lag plus thrust turns every fix into a growing bloom.** A burning ship is seen but not known. A coasting ship is known, if found.
- **The player sees the polity's fused picture, relayed instantly** (decided Nov 1). Each reading is as old as the light that made it, but reaches the player the moment the sensor takes it. Sensor placement is the player's lever on how old the picture is.
- **Sensors cost money and are targets.** Small observation posts scattered around and big telescopes far apart for triangulation are strategic investments.

## Five questions, five limits

| Question | What limits it | Typical answer |
| --- | --- | --- |
| Is something there? | Signal against sensitivity, search time, clutter | Burning: yes, far away. Cold: maybe, close, if a sensor is looking that way |
| Which direction? | Aperture and signal-to-noise: σθ ≈ (λ/D) / SNR | Excellent, well under a microradian |
| How far? | A single passive sensor measures nothing along the line of sight | The expensive number |
| What is it, and how many? | Angular resolution, spectra | Mostly inference |
| Where will it be? | Light-lag plus the acceleration it might use | Coasting: very well. Burning: a growing bloom |

## Detection

**Calibration.** NEO Surveyor's published sensitivity is about 110 µJy (5σ) in three minutes at 8 µm with a 0.5 m telescope. Scale it by aperture squared and the square root of integration time, and model each source as a blackbody of its power and temperature. Order of magnitude only.

| Source | 0.5 m, 3 min | 1 m warship, 10 min | 4 m picket, 1 h stare |
| --- | --- | --- | --- |
| Cold hull, shaded, 50 kW at 200 K | 1×10⁵ km | 3×10⁵ km | 2×10⁶ km |
| Sun-warmed hull, ~1 MW at 280 K | 9×10⁵ km | 2.5×10⁶ km | 1.5×10⁷ km (0.1 AU) |
| Fission or NTR radiators, 10 MW at 600 K | 3.5×10⁶ km | 1×10⁷ km | 6×10⁷ km (0.4 AU) |
| Fusion waste heat, 10 GW at 1,500 K | 0.34 AU | ~1 AU | ~6 AU |

What follows:

- **Range grows only as √power at a fixed temperature.** Halving the heat buys little; hiding is about temperature, direction and timing.
- **"Cold coast plus late burn" is real** through the early and mid eras. A quiet hull is visible at cislunar-to-0.1 AU distances, not across the system.
- **Fusion-era drives are visible across the inner system** to a dedicated picket from their waste heat alone. Hot plumes are brighter still in shorter wavelengths.
- **Less pessimistic for stealth than Atomic Rockets,** which assumes big staring telescopes everywhere. The working rule: you get the detection you pay for.

**Sensitivity isn't coverage:**

- **Search rate.** A sensor covers a patch of sky at a time. Cued tracking of a known contact is cheap; surveying the sky for cold contacts at depth is expensive and slow.
- **The Sun.** Surveys can't look close to the Sun (NEO Surveyor goes down to 45° elongation). An approach from sunward is a real geometric blind spot, the space version of Chelyabinsk.
- **Occlusion.** Planets and moons block lines of sight.
- **Clutter.** In the belt, a cold ship has the IR signature of a modest asteroid. It stands out only when it moves off a Kepler arc, runs warmer than the rocks, or shows up as metal on radar.

## The bearing and the needle

**Bearing is cheap.** A 1 m telescope at 3 µm has λ/D ≈ 3 µrad. Centroiding at SNR 100 gives about 30 nrad, roughly 4.5 km sideways at 1 AU. The uncertainty volume is a needle: a few km wide and unbounded along the line of sight. That is the sonar bearing strobe of this game.

**Resolution decides counting.** Separating two ships 10 km apart at 1 AU needs about a 55 m aperture at 3 µm (1.22 λR / spacing). A fleet at interplanetary range is one point. See [`design/combat-ranges-and-group-tracks.md`](combat-ranges-and-group-tracks.md) for the group track.

## Buying range

| Method | Accuracy | What it costs |
| --- | --- | --- |
| **Triangulation** between sensors with baseline B | σR ≈ R² σθ / B | Sensors, and both must see the target |
| **Angles over time** (coasting target) | Gravity curves the arc; a short arc says almost nothing | Days of watching for heliocentric arcs; fails if the target burns |
| **Observer manoeuvre** (submarine target motion analysis) | Good, given geometry | Δv, and the observer's burn is visible |
| **Photometric** (brightness plus an assumed class) | As good as the identification | A misidentification becomes a range error |
| **Radar** | ~10 m in range, ~mm/s in range rate | Lights up the emitter; the echo falls as R⁴ |
| **Lidar,** cued by the passive bearing | ~1 m | The target's laser warning gets the shooter's exact bearing |
| **Doppler** from the plume's spectral lines | Radial velocity only | Free, but only for burning ships |

### Triangulation: near-exact positions

The method the sensor network is built for. Range error grows with the square of the range and falls with the baseline:

| Bearing precision | Baseline | At 10⁷ km | At 1 AU | At 5 AU |
| --- | --- | --- | --- | --- |
| 1 µrad | 10⁴ km | 10,000 km | 2×10⁶ km | 6×10⁷ km |
| 1 µrad | 10⁶ km | 100 km | 22,000 km | 6×10⁵ km |
| 0.1 µrad | 10⁶ km | 10 km | 2,200 km | 56,000 km |
| 0.1 µrad | 1 AU | 0.07 km | 15 km | 370 km |

- **Big telescopes far apart give near-exact positions.** Two deep-stare telescopes ("turbotelescopes") an AU apart, one near Earth and one near Mars, fix a bright contact at 1 AU to about 15 km.
- **Both must see the target.** A far baseline means a sensor far from the target, so it needs depth. That is why triangulation anchors are big telescopes, and why small posts alone give needles, not fixes.
- **Each sensor sees the target at a different moment,** because the light reaches them at different times. For a coasting target the fusion solves this exactly. For a burning target the fix holds at the observation moments and the bloom grows from there, unless Doppler or a third sensor pins the acceleration.

### The other methods

- **Angles over time.** Astronomers call it the "too short arc" problem: a few nights of angles and angle rates leave the range and range rate unknown, and many orbits fit equally well. Astronomers narrow it by assuming the object is bound to the Sun. A ship can be on any trajectory, so its admissible region is wider.
- **Observer manoeuvre.** In bearings-only tracking, the observer must outmanoeuvre the target to get its range. The space twist: a sensor in planetary orbit gets free manoeuvres from its own orbit, a baseline of twice its orbit radius every half period, against any target outside that gravity well.
- **Radar.** Goldstone (500 kW, 70 m) tracks asteroids at millions of km and measures their velocity very precisely. Reach grows only with the square root of target size.
  - **Warship-scale radar** (~1 MW, 10 m) reaches roughly 10⁶ km against a large hull.
  - **Radar tells metal from rock,** which makes it the belt's discriminator.
  - **The target hears the pulse at R²,** far beyond the emitter's own R⁴ reach.
- **Lidar.** Ground stations today range uncooperative debris at up to about 1,700 km with ~1.5 m telescopes, to metre precision. A warship with weapon-class optics, cued by its own IR bearing, puts its spot nearly on the target, so the echo falls as R², not R⁴. Rough estimate: a kW-class lidar ranges a 50 m hull at about 10⁶ km.

## Light-lag plus thrust: the bloom

A fix t seconds old has a reachable sphere of radius ½ a t² around the coasting prediction:

| Distance | Lag | 0.1 m/s² target | 1 g target |
| --- | --- | --- | --- |
| 10⁶ km | 3.3 s | 0.6 m | 55 m |
| 0.1 AU | 50 s | 125 m | 12 km |
| 1 AU | 8.3 min | 12 km | 1,250 km |
| 5 AU | 42 min | 310 km | 31,000 km |

- **At combat ranges** (≤10⁶ km) the bloom is metres. Own sensors give fire-control quality, and the limit is the dodge geometry in [`design/combat-ranges-and-group-tracks.md`](combat-ranges-and-group-tracks.md). Terra Invicta's "everything is seen" is roughly right here.
- **At strategic ranges** a burning ship is a needle that becomes a bloom: seen but not known. A coasting ship, once ranged, has a tight banana that stays tight until it lights up again: known, if found.
- **The lag that counts is from the target to the sensor.** The player's relay is instant (below), so a post near the action shortens the bloom directly.

## What, and how many

- **Count** comes from total brightness divided by an assumed per-ship signature, so it is only as good as the identification.
- **Spectra** give radiator temperature and the plume's lines, and so the drive family.
- **A burning ship can in principle be weighed.**
  - Plume brightness gives jet power; line widths or shifts give exhaust velocity; together they give thrust.
  - The measured acceleration then gives mass.
  - To be checked in the detection study. It is the passive counter to decoys.
- **Decoys** are cheap while coasting (a heated balloon) and expensive while burning: matching the plume *and* the acceleration means carrying the mass.

## The player's picture (decided, Nov 1)

The player sees **the polity's fused picture**, never the truth, and sees it **in real time as the sensors see it.**

- **The relay is instant.** A reading reaches the player the moment the sensor takes it, wherever the sensor is.
- **The reading is still old.** It is as old as the light that made it: a picket 2 light-hours from a contact shows it as it was 2 hours earlier.
- **So the player is an FTL observer of their own sensor network.** They can react at once to a reading on the far side of the system. That is the accepted cheat, matching the instant orders decided Oct 30.
- **AI polities, governors and AI-run units fuse at c.** A report travels from the sensor to each node at light speed, so their pictures are older. This includes the player's own AI-run units (decided Oct 30): a unit acts on its own node's picture until the player takes it over.
- **The player and their own governor at Saturn see different pictures.** That's the sensing side of the "Sir, why are we burning towards Jupiter?" oddity.

**What this does to play:**

- **For the player, the only lag is target to nearest sensor.** Pushing small posts close to where things happen shortens it. That's a direct, readable payoff for sensor placement.
- **For the AI, the relay geometry matters too** (sensor to node). AI polities value relays and the placement of their decision nodes, not just sensors.
- **The interest table reads the player's picture.** Speed drops come from picture events (a detection, a range lock, an identification change) at the moment the reading is taken.

**One implementation.** Observations are records: the time taken, the sensor's position, the measurement and its noise. A node's picture is the fusion of the records that have arrived at the node by now. The player's picture is the same fusion with arrival time equal to observation time. One fusion code, two arrival rules.

**The UI shows age as well as shape.** Each contact shows when its light left it. The display draws the estimate at the current time with its uncertainty shape, and the last observed position as a ghost.

## Sensors as an investment

| Asset | Gives | Costs and weaknesses |
| --- | --- | --- |
| **Observation post** (small, wide-field IR) | Detection, bearing, coverage, short lag where placed | Cheap and many; shallow; each one gives only a needle |
| **Big telescope** ("turbotelescope") | Deep detection, precise centroid; anchors triangulation | Expensive and few; a fixed, known, high-value target |
| **Radar station** | Range and range rate; metal against rock | Emits, so everyone knows where it is; R⁴ reach |
| **Lidar** (often a laser weapon's optics) | Metre-level range on a cued contact | Announces itself to the target |
| **Ship sensors** | Own fire control; range by manoeuvre | Limited aperture; ranging costs Δv |
| **Shared or bought feeds** | Someone else's picture | Dependency; can be cut, delayed or spoofed |

**Network design trades three things:**

- **Coverage:** many small posts, so something is always looking and the lag is short.
- **Depth:** big apertures and long stares, so cold ships are found further out.
- **Baseline:** sensors far apart, so needles cross into fixes.

**Where sensors go:**

- Lagrange points and planetary orbits (an orbit's own motion gives a free baseline).
- Trojans and belt rocks.
- A ring of posts sunward of protected bodies, to close the Sun blind spot.
- Along approach corridors, for envelope enforcement.

**Ties to the rest of the design:**

- **Sensors are the first targets.** If nothing can hide, the side that blinds the other first gets stealth by subtraction. Blinding or destroying a sensor is an incident on the defiance ladder, and a likely opening move of a war.
- **Posts in someone else's space are espionage.** A covert post in a rival's claim is a record no one has seen yet, until they find it.
- **The picture is leverage.** A company that relies on its host's sensor network depends on it, and the host can cut or degrade the feed. Building one's own network is a step up the self-sufficiency ladder, next to chip fabs and drives.
- **Envelope enforcement needs range.** Proving a freighter is 5 % off its declared trajectory takes a good fix. Disputes over whose data to believe become part of the incident record.

## Doctrine and posture

- **Sensor posture** is a doctrine field: passive only, cued lidar, or full radar, with a rule for when to go active.
- **Ranging manoeuvres** are doctrine too: whether a captain spends Δv to range a contact, and how much.
- **Heat discipline:** heat sinks for dark running, and radiators edge-on and turned away from *known* sensors. Unknown posts are the risk.
- **Ranging is never manual.** The player decides whether to pay for range (build, emit, manoeuvre), never how to compute it.

## How it plays

1. **Strategic.** "Something 10 GW-class is burning sunward from Ceres": when does it arrive, where will it brake, how many ships? The answers depend on which sensors see it and how far apart they are.
2. **Approach.** Cold coasting, heat sinks, sunward approaches and the belt's clutter against a network that has to be paid for.
3. **Combat.** Knowledge is good. The fight is dodging, spoofing and saturation.
4. **Gray zone.** Envelope violations and covert work are only as provable as the picture is sharp.

## In the sim

- **A contact holds:** a bearing covariance; a range distribution (possibly only an admissible interval); kinematics; class hypotheses with weights; a count estimate; and the observation and arrival times.
- **No hard cutoffs.** "Detected", "tracked", "ranged" and "fire-control quality" are UI labels on a continuous covariance, never levels in code.
- **Uncertainty shapes:**
  - the **needle** (bearing only);
  - the **cross-fix lozenge** where needles meet;
  - the **banana** for a ranged coaster;
  - the **teardrop bloom** for a burner, stretched along its last seen thrust.
- **Misidentification propagates.** A wrong class gives a wrong photometric range and so a wrong intercept window in the AI's planning.
- **Events, not ticks.**
  - When a coasting target crosses a sensor's threshold is solved analytically on rails.
  - A burn's start is already an event.
  - Report arrival at an AI node is an event.
  - This fits decision-driven compression.
- **The coarse tier** works with detection probabilities per sensor–target pair over an interval, calibrated against fine on the parity bench, with search-rate cases (cold targets, sunward approaches) in the panel.

## Assumptions behind the numbers

All placeholders until the detection study reports.

- Sensitivity scaled from NEO Surveyor at 8 µm: aperture squared, square root of time, a single band.
- Sources are blackbodies radiating isotropically. Directional radiators and plume spectra change this.
- Bearing precision of 0.1–1 µrad after centroiding.
- Radar and lidar reaches are scaled from Goldstone and from ground debris laser ranging, to a factor of a few.

## Open questions

- [ ] Do AI polities get instant fusion as a difficulty or fairness setting?
- [ ] Search-rate model: sky area per hour at a given depth, per sensor block.
- [ ] Plume spectroscopy: can a burning ship really be weighed, and how well?
- [ ] Allied and bought feeds: instant to the player, or relayed at c to the player's nearest sensor or node?
- [ ] Covert posts: how they are found, and what finding one does to relations.
- [ ] Asteroid confusion density in the belt, and how fast a cold ship is picked out from it.
- [ ] If the command nexus is ever adopted, the player's picture would lag to it as well.

## Sources to start from

- NEO Surveyor sensitivity: [Mainzer, NEO Surveyor update](https://uvex2023.caltech.edu/system/media_files/binaries/45/original/Mainzer_NEOSurveyor_-_Amy_Mainzer.pdf?1680045689); solar elongation limit: [Masiero et al. 2024](https://doaj.org/article/8e06f064864748258f004fbfdc0aa6ed).
- The sunward blind spot: [NEOMIR, ESA](https://conference.sdo.esoc.esa.int/proceedings/neosst2/paper/116/NEOSST2-paper116.pdf).
- Too-short arcs and admissible regions: [Milani et al.](https://springerlink.bibliotecabuap.elogim.com/content/pdf/10.1007/s10569-004-6593-5.pdf).
- Bearings-only observability: [log-polar bearings-only tracking](https://arxiv.org/pdf/2406.19599v1).
- Planetary radar: [Radar astronomy](https://en.wikipedia.org/wiki/Radar_astronomy); [Goldstone tracking 2011 UL21](https://space.com/nasa-goldstone-radar-system).
- Debris laser ranging: [Zhang et al. 2024](https://www.mdpi.com/2072-4292/16/4/727).
- The stealth debate: Atomic Rockets' detection page; [CoaDE forum thread](https://childrenofadeadearth.boards.net/thread/28/stealth-space).
