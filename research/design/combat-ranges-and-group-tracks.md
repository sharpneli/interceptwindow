# Intercept Window: Combat Ranges and Group Tracks

Nov 1, 2026 · @Teemu

What ranges fights happen at, how those ranges move with tech, and when a fleet can be treated as one object. The numbers are first-cut estimates, to be replaced by the Atomic Rockets survey, the beams study and the guidance study ([`studies/research-agenda.md`](../studies/research-agenda.md)). The scaling laws are the part to keep: they say which tech blocks move which range.

## The short version

- **A distant fleet is a group track:** a centroid, a velocity and a spread. It is a blob, not a point. A point is a blob with zero spread, so one model covers both and there is no cutoff.
- **The group track is for the picture, aiming and the scheduler. Damage never reads it.** Hits always resolve per ship, under the one hit contract.
- **Each weapon family has its own range limit:** unguided kinetics by the target's agility, lasers by diffraction, missiles by a Δv duel. They scale differently with tech, so who outranges whom changes by era.
- **Ranges grow with tech, but so does the target's agility.** That keeps gun ranges short until macron speeds arrive.

## Group tracks

### Where a fleet is effectively a point

The measure is the fleet's extent D against the lengths that matter at range R. A fleet spaced against nuclear bursts is roughly 10–100 km across.

- **The picture, because optics says so.** A passive sensor resolves about 1.22 λ / aperture. Ships closer together than that look like one contact with a total brightness:

  | Sensor | Resolution | At 10⁴ km | At 10⁵ km | At 10⁶ km |
  | --- | --- | --- | --- | --- |
  | 10 µm IR, 1 m aperture | 12 µrad | 120 m | 1.2 km | 12 km |
  | 10 µm IR, 10 m aperture | 1.2 µrad | 12 m | 120 m | 1.2 km |
  | 3 µm IR, 1 m aperture | 3.7 µrad | 37 m | 370 m | 3.7 km |

  Beyond about 10⁶ km a formation is one unresolved blob. "Two warships or one hot freighter?" falls out of the optics, which is the misidentification the picture needs. Lidar and radar can split a blob by range and Doppler, so going active trades stealth for resolution. [`design/detection-and-the-picture.md`](detection-and-the-picture.md) has the full detection model.
- **Aim and time of flight on long shots.** Missiles at 10⁴–10⁶ km and late-era lasers at 10⁵ km see a fleet only about as wide as their own aim error.
- **The scheduler's broad phase.** As in collision detection: compute when an intercept window opens against the group's bounding sphere (centroid distance minus radius). That estimate is conservative, so the speed drop is never late. Refine per ship as the window approaches. **The broad phase changes cost, never outcome.**
- **The shooter's own fleet.** Kilometres of launch spread don't matter at 10⁵ km. Datalink light-lag across a 1,000 km formation is about 3 ms.

### Where it stops being one

All of these are at the terminal end, where intra-fleet geometry decides the outcome:

- **Burst radius against spacing.** A megaton's soft-kill radius is tens of kilometres, comparable to the formation. Spacing decides whether one warhead hits one ship or five.
- **Point-defence mutual support.** Ships cover each other only inside their point-defence range.
- **Clouds.** A sandcaster cone narrower than the formation hits ships, not "the fleet".
- **Early-era guns.** Gun range (tens of km) is about the size of the fleet, so geometry is the whole fight.
- **Sensor baseline.** A spread fleet triangulates its own contacts, with range error σR ≈ R² σθ / B ([`design/detection-and-the-picture.md`](detection-and-the-picture.md)). At 0.1 µrad bearing precision, a 100 km fleet ranges a contact at 10⁵ km to about 10 km, but at 10⁶ km only to about 1,000 km. Fleet spread helps at combat range; strategic ranging needs pickets with baselines of 10⁶ km or more. Light-lag across a picket line matters only to AI nodes, which fuse at c; the player's relay is instant.

### Formation is doctrine

Spacing pulls several ways at once, so it's a doctrine choice with no single right answer:

| Spread out | Close up |
| --- | --- |
| One burst or cloud hits fewer ships | Point defence covers neighbours |
| Wider sensor baseline, better passive ranging | Harder to resolve into separate contacts at range |
| Harder to cover with one missile wave | Easier to manoeuvre together; less light-lag inside the group |

Formation spacing belongs in doctrine as values (per side, overridden per group), like Fleetwright's evasion field. The AI reads the enemy's weapons from its picture to pick it, so misreading the threat leads to the wrong spacing.

### How to build it

- **The formation spread is added to the track covariance.** When the spread is small next to the track uncertainty, it vanishes into it; when it's large, it dominates. The picture already has this machinery, including the along-track banana.
- **Two kinds of error, kept separate:**
  - **the centroid error,** correlated across every ship: if the aim is off for one, it's off for all, so a salvo hits wholesale or misses wholesale;
  - **the formation offsets,** independent per ship.

  A coarse resolver that lumps the two gets saturation and overkill wrong. The parity bench needs formation cases (a salvo against a tight group and against a dispersed one) to catch it.
- **The Hill frame is the group track.** The group's reference orbit plus Clohessy–Wiltshire offsets *is* "point plus spread", physically exact to first order. It holds while the offsets are small next to the orbit radius: fine for 10⁶ km offsets in heliocentric orbit, and for about 100 km in low Earth orbit.
- **A representation, not a tier.** The asked speed still picks the clock tier, never range or zoom. A coarse resolver that works on group tracks is calibrated against fine runs with every ship explicit, on the rung ladder like any other coarse piece.

## Engagement ranges by weapon family

### Unguided kinetics: the dodge limit

**R ≈ v_rel · √(2s / a)**

- **v_rel:** the projectile's speed relative to the target, including the platforms' closing speed.
- **s:** the miss tolerance (the target's half-size plus the cloud radius).
- **a:** the target's lateral acceleration, net of the time it takes to turn.

This is the dodge crossover from "Posture against dodging" in the design notes, turned into a range.

| Era | Case | Time of flight | Range |
| --- | --- | --- | --- |
| Chemical | 3 km/s, target 0.1 m/s², 10 m | 14 s | ~40 km |
| Chemical | Same, on an 8 km/s head-on pass | 14 s | ~110 km |
| Fission / NTR | 10 km/s, 0.3 m/s², 10 m | 8 s | ~80 km |
| Fusion | 20 km/s slug, 1 m/s² | 4.5 s | ~90 km |
| Fusion | Same, 100 m cloud | 14 s | ~280 km |
| Torch | 1,000 km/s macrons, 1 g | 1.4 s | ~1,400 km |
| Torch | Same, 100 m cloud | 4.5 s | ~4,500 km |
| Torch | Slug against a 3 g target | 0.8 s | ~800 km |

Range grows as v / √a. Through the fusion era agility rises about as fast as gun speed, so gun ranges stay roughly flat at about 100 km, which matches CoaDE experience. Macron speeds (×50) outrun torch agility (×10, so ×3 in range) and push kinetics to thousands of kilometres.

### Lasers: the diffraction limit

**R ≈ d · D / (2.44 λ),** with spot diameter **d = √(4P / (π I))**

- **D:** the mirror's diameter. **λ:** the wavelength. **P:** the beam power. **I:** the intensity needed to do damage, taken here as 10⁸ W/m² (a placeholder for the beams study).
- In short, **R ∝ D · √P / λ.** Laser range grows faster with tech than any other family's.

| Era | Power, wavelength, mirror | Spot | Range | Pointing stability needed |
| --- | --- | --- | --- | --- |
| Chemical | 1 MW, 1 µm, 1 m | 0.11 m | ~50 km | 2.4 µrad |
| Fission / NTR | 10 MW, 500 nm, 2 m | 0.36 m | ~600 km | 0.6 µrad |
| Fusion | 100 MW, 250 nm, 4 m | 1.1 m | ~7,000 km | 150 nrad |
| Torch | 1 GW, 100 nm FEL, 10 m | 3.6 m | ~150,000 km (0.5 light-s) | 25 nrad |
| Planetary defence | 10 GW, 100 nm, 30 m | 11 m | ~1.4 million km (4.6 light-s) | 8 nrad |

Two other limits, which take over at light-second ranges:

- **Pointing jitter** comes first. The torch-era case needs Hubble-class stability (about 25 nrad), and a fixed installation can manage that more easily than a warship under thrust.
- **Light-lag** comes later. The shooter aims at where the target will be after a round trip of 2R/c. A 1 g jink moves the target about 5 m in the 1 s round trip at 0.5 light-s, and about 420 m in 9 s at 4.6 light-s.

So the design notes' "light-seconds" long defence layer is right for large fixed installations, and doubly so for its deflection goal, which needs far less intensity than a kill. Warship lasers top out around 10⁵ km.

### Missiles: the Δv duel

**T ≈ Δv_missile / a_target,  R ≈ v_close · T**

Missile range isn't a distance. The target dodges by spending its own Δv at its acceleration, and the missile has to match the dodge. The missile also needs more acceleration than the target to close the endgame.

| Era | Missile Δv | Target dodge | Closing speed | Flight time | Range |
| --- | --- | --- | --- | --- | --- |
| Chemical | 2 km/s | 0.5 m/s² | 5 km/s | ~1 h | ~20,000 km |
| Fission / NTR | 5 km/s | 1 m/s² | 10 km/s | ~1.4 h | ~50,000 km |
| Fusion | 50 km/s | 3 m/s² | 20 km/s | ~4.6 h | ~330,000 km |
| Torch | 1,000 km/s | 1 g | 100 km/s | ~28 h | ~10 million km |

These are upper bounds against a target willing to spend all that Δv on dodging. Two things from [`design/detection-and-the-picture.md`](detection-and-the-picture.md) change how they play:

- **The duel starts when the target sees the missile.** A burning missile is seen at once. A cold-launched missile coasting in is seen only at the target's detection range for a small cold object. Scaling the detection doc's cold hull (50 kW at 200 K, about 3×10⁵ km for a 1 m warship sensor) by √power puts a 5 kW missile at about 10⁵ km. The dodge clock starts there, not at launch: cold coast plus late burn, for missiles.
- **The shooter needs a fix, not a bearing.** At combat ranges (≤10⁶ km) own sensors and lidar give fire-control quality, and the target's bloom is metres. Beyond that, a missile launched at a needle or a bloom must also carry the Δv to search it out, roughly the bloom radius over the remaining flight time.

Past those, missile range is capped by the guidance chain and by hours of flight in which the target can do more than dodge. In the torch era missiles become interplanetary weapons, the "strategic shift" row of the drive table.

### Not yet estimated

- **Particle beams:** neutral beams diverge at about microradians, which suggests thousands of kilometres. To the beams study.
- **Drive plumes:** the drive as a weapon and a hazard. To the exhaust and plumes study.
- **Nuclear shaped charges** (Casaba-Howitzer) and **bomb-pumped X-ray lasers:** their reach goes well past a bare burst's. To the warhead conversion study.

## Ranges by era

| Era | Unguided kinetics | Warship lasers | Missiles | What sets the fight |
| --- | --- | --- | --- | --- |
| Chemical | 40–110 km | ~50 km | ~10⁴ km | Missiles reach; guns and lasers about equal at knife range |
| Fission / NTR | ~80 km | ~600 km | ~5×10⁴ km | Lasers overtake guns |
| Fusion | 90–280 km | ~7,000 km | ~3×10⁵ km | Lasers dominate the middle distance |
| Torch | 800–4,500 km | ~1.5×10⁵ km | ~10⁷ km | Lasers set the stand-off; missiles go interplanetary |

## What this means for play

- **Early fights are passes.** With little Δv, the orbits set the range, and each weapon's window opens and closes in turn on the approach.
- **With torch Δv, the side with the longer reach picks the range** and holds it. Optics, power and wavelength become the deciding tech blocks.
- **The decision cadence in the notes holds** for the range-setting weapon. Range ÷ closing speed for lasers comes out at about 60 s (fission), 150 s (fusion) and 150 s (torch at 1,000 km/s). Gun windows are seconds long, which is the fine tier's knife fight.
- **The UI really does span kilometres to light-seconds,** as the notes expect. The zoom bands carry it.

## Assumptions behind the numbers

All of these are placeholders until the studies report.

- Damage intensity 10⁸ W/m² for continuous lasers. Pulsed beams and ablation physics may move this by an order of magnitude either way.
- Miss tolerance 10 m for a slug and 100 m for a cloud.
- Target lateral acceleration by era: 0.1, 0.3, 1 and 10 m/s². Turn time is ignored, which flatters the dodger.
- Missile Δv and closing speeds as in the missile table.
- Airy first-null spot diameter (2.44 λR/D); the central lobe holds about 84 % of the power.

## Open questions

- [ ] Laser damage threshold by wavelength, pulse length and target material (beams study). It moves every laser range in this doc.
- [ ] Lateral acceleration actually available, with turn time and RCS blocks. It moves every kinetic range.
- [ ] Signatures of cold missiles and kill vehicles (size, temperature, sun-warmed or shaded). [`design/detection-and-the-picture.md`](detection-and-the-picture.md) covers hulls; missile signatures set when the dodge clock starts.
- [ ] Coarse group-track resolver: the correlated error model, and formation cases on the parity bench.
- [ ] Formation spacing as a doctrine field: its values, and how the AI picks them from its picture.
- [x] Count estimation from an unresolved contact. **Covered in [`design/detection-and-the-picture.md`](detection-and-the-picture.md):** total brightness over an assumed per-ship signature, spectra, and weighing a burning ship from its plume and acceleration. Decoys are cheap while coasting and expensive while burning.
