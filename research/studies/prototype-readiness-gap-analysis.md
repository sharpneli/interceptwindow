# Intercept Window: Prototype Readiness – Gap Analysis

Nov 2, 2026 · analysis of all 29 project docs

A read of every design and research doc against one question: is anything basic missing before prototyping starts? The build order is fixed ([`design/fleetwright-principles-for-intercept-window.md`](../design/fleetwright-principles-for-intercept-window.md), section 10): first a solar system, then ships in it, then onward piece by piece. So the test is what each prototype step needs, and whether a doc already answers it.

## The short version

- **The research is deep where the fighting is, and thin where the build starts.** Weapons, drives, detection and the campaign economy have strong docs. The first two prototype steps (a solar system on rails, then a ship that burns in it) have no study and no design doc at all.
- **The Research Agenda has the order backwards for the build.** Ephemerides and transfers sit in Tier 2, "after the battler", while the build order makes the solar system step one and the battler's slice starts in cislunar space.
- **Five gaps block the first code:**
  1. **Orbits, frames and propagation:** including the fact that cislunar space is three-body, and that thrusting ships need rails too.
  2. **Time and numerics:** time resolution, determinism scope, hit-finding at hypervelocity, GPU precision.
  3. **Ship orders and manoeuvre planning:** how anyone tells a ship where to go, and how the UI shows it.
  4. **The first playable:** the battler's slice is still undecided in two docs, and no scenario is specified.
  5. **Attitude:** posture is core gameplay, but rotation is a prototype placeholder.
- **Two more gaps block combat, not motion,** and can run in parallel: the effects studies (impacts, bursts) the notes say come before any weapon, and a minimal ship-function model behind "no hit points".
- **Most of the rest can wait.** Resources, the mass ledger, logistics, manufacturing, settlements and the shadow ledger are good Tier 2 work and stay off the prototype path, apart from the owner, jurisdiction and controller fields already planned as scaffolding.

## Coverage against the build order

| Step | What it needs | Covered by | State |
| --- | --- | --- | --- |
| **P1. Solar system on rails** | Body ephemerides, frames, precision, time, rendering at system scale | Clock tiers (Fleetwright principles); "heliocentric doubles, Hill frame locally" | **Gap.** Principles only; no model |
| **P2. One ship that burns** | Ship from the generator, drive blocks, thrusting propagation, attitude | Ship generator; drive survey | **Partial.** Ship and drives yes; propagation of thrust and attitude no |
| **P3. Two ships, orders, intercepts** | Command vocabulary, solvers (Lambert, rendezvous), event finding, display frames | Command principles (Fleetwright); intercept windows in the notes | **Gap.** No ship-level orders or manoeuvre UX |
| **P4. Sensing and the picture** | Detection, fusion, uncertainty shapes | Detection and the Picture; Combat Ranges | **Good** for a first cut |
| **P5. Shooting and damage** | Weapon blocks, effect models, hit-finding, ship function | Weapon blocks; weapon surveys; ship generator hooks | **Partial.** Weapons surveyed; effect models and function model missing |
| **P6. Scenario that plays itself** | Scenario spec, end conditions, minimal AI, doctrine | Command and doctrine principles | **Gap.** No scenario spec |
| **Later: living solar system** | Resources, logistics, industry, settlements, politics | Ten docs | **Ahead of need** |

## Blockers for the first code

### 1. Orbits, frames and propagation

The design asserts "analytic coasting on Kepler rails, jumping a month costs the same as a second". That is right for most of the solar system and wrong for the part the battler starts in. Six questions are open:

**a. Body ephemerides.** Two workable routes:

| Option | For | Against |
| --- | --- | --- |
| Keplerian mean elements with secular rates (JPL's approximate elements) | Analytic, tiny, plausible over any span, fits "no fixed dates" | Arc-minute errors; moons need their own sets |
| Full numerical ephemeris (JPL DE series) | Exact | Large tables; tied to a calendar span; more than a game needs |

Proposal: mean elements for planets and moons about their primaries, with the DE series used only as the yardstick.

**b. Cislunar space is three-body.** Several docs already rely on orbits that don't exist on Kepler rails:

- the logistics doc's yard at NRHO, depots at Earth–Moon L1, and lunar-flyby asteroid capture;
- the detection doc's sensors at Lagrange points;
- station-keeping, DROs and low-energy transfers generally.

Options: patched conics with Lagrange "anchored" stations (a logged exception); circular restricted three-body motion near the Earth–Moon pair; or point-mass n-body for ships everywhere (below). This has to be settled before P1, because it decides whether "rails" means a formula or a cached integration.

**c. Sphere-of-influence switching is a hard cutoff.** Patched conics flips a ship's primary at a radius, which is exactly the kind of hidden threshold rule 1 bans. Two honest ways out:

- **Log it** as an exception (cheap, KSP-like).
- **Make the physics n-body and the reference body a numerical convenience.** Ships feel all relevant point masses (Encke-style integration relative to the dominant body). Changing the reference body changes the arithmetic, never the trajectory, so no outcome depends on a threshold.

Proposal: the second. It also answers (b), and the Hill frame stays as the local frame for close work.

**d. Thrusting ships need rails too.** The principles say a thrusting ship can't stay on rails. But electric tugs burn for months to years ([`studies/interplanetary-bulk-logistics-mines-depots-and-shipyards.md`](interplanetary-bulk-logistics-mines-depots-and-shipyards.md)) and torches for days. Coarse-stepping all of them at one minute would make thrust the sim's main cost. Proposal: **a committed trajectory is a rail.**

- When a burn plan or a coast is committed, integrate it once at high accuracy and store it as piecewise Chebyshev polynomials.
- Render, schedule and find events against those polynomials, exactly as against a Kepler arc.
- Re-anchor when the plan changes (a new order, damage, a dodge).
- For the Routine tier, an averaged low-thrust model (Edelbaum-style Δv and time per leg) covers tugs nobody is watching.

Perturbations that reduce to secular rates (J2 nodal precession, the Moon's node) stay plain rails.

**e. Event finding needs a design.** Closest approach, sensor threshold crossing, envelope entry and intercept windows are all roots on pairs of arcs, often several per orbit. With every merchant a real track, the pair count is the scheduler's main cost. Needed:

- pair pruning (the spatial index the principles say "needs its own design");
- robust multi-root finding on arcs and polynomials, with a guarantee that the scheduler is never late;
- space-surveillance conjunction screening (apsis, orbit-path and time filters) as the starting point.

**f. Bodies as objects.** Rotation and pole orientation, shape (sphere or ellipsoid), atmosphere extent, occlusion and eclipse (solar power, thermal load, detection blind spots). A minimal set is needed for P1, since occlusion and eclipse feed detection and heat.

**Yardstick:** reference runs from GMAT, Orekit or poliastro; energy and angular-momentum drift benches; Kepler against integrator agreement on coasting arcs; a dt-proof check on the thrust integrator.

**Recommendation:** move Ephemerides and Transfers to Tier 1, first, and write `design/Orbits, Frames and Propagation.md` before P1.

### 2. Time and numerics

**Time resolution.** Fleetwright's world time is a `long` of milliseconds. At 1,000 km/s a millisecond is 1 km, and a 10 m hull at 10 km/s closing speed is crossed in 1 ms. Options:

| Representation | Range | Resolution |
| --- | --- | --- |
| `long` milliseconds (Fleetwright) | ±292 million years | Too coarse for torch-era fine work |
| `long` microseconds | ±292,000 years | Enough for scheduling |
| `long` nanoseconds | ±292 years | Too short for a long campaign |
| `Int128` nanoseconds, or tick plus double offset | Effectively unlimited | Fine for any event |

Proposal: integer ticks for the world clock, with event times solved as a tick plus a double offset, so hit and light-time solutions aren't quantised by the clock.

**Hits at hypervelocity can't be ticked.** The one hit contract says what a hit is, not how it's found. At 10–1,000 km/s no tick is small enough to catch an impact by overlap. The fine tier needs swept, analytic intersection in the relative frame (closest approach of a cloud or slug against hitboxes over the step), and the coarse tier works statistically from the start.

**Tick sizes per era are unset.** Coarse is one-minute steps in Fleetwright. A minute is 1,200 km at 20 km/s closing and 60,000 km at 1,000 km/s, beyond any gun range. The rule "a model says what step it needs" covers this; the numbers still need choosing.

**Precision.**

- Heliocentric doubles give about half a millimetre at Neptune, as the principles say. Relative motion for close fights should still be integrated in a local frame, so two independently propagated states don't add their errors at metre scale.
- **GPU floats are 32-bit.** A float 1 AU from the origin resolves only about 10 km. Camera-relative rendering and reversed or logarithmic depth have to be in the renderer from the first frame.

**Determinism scope.** "Same start, same commands, same world" is easy on one machine. Across machines it isn't: basic IEEE arithmetic in .NET is reproducible, but `Math.Sin`, `Exp`, `Pow` and friends call the platform's math library and can differ by OS and CPU. Decide now whether replays and bug reports must match across platforms. If yes, use a deterministic math library for transcendentals from the start; retrofitting it later touches everything.

### 3. Ship orders and manoeuvre planning

Nothing in the docs says how the player, or an AI captain, makes a ship go somewhere. In this genre that is the hardest UX problem (Children of a Dead Earth and Kerbal Space Program are the precedents, and the main source of complaints about both), and P2–P3 can't start without it.

What a design doc has to settle:

- **The command vocabulary,** as intents:
  - burn a vector at a time (the raw form);
  - go to an orbit, transfer to a body, rendezvous or match velocity;
  - intercept, hold station relative to something, keep inside an envelope;
  - flip and brake; evade per doctrine.
- **The solver behind each:** Lambert for transfers and intercepts, Clohessy–Wiltshire targeting for rendezvous, low-thrust approximations, constant-acceleration flip-and-burn in a gravity field.
- **How the trade is shown:** Δv against time (a porkchop or a slider), and feasibility reported as consequences ("needs 4.2 km/s, has 3.1"), never refused, per the designer rule.
- **Display frames:** which body or ship a trajectory is drawn relative to (heliocentric, body-centred, a target's Hill frame). Zoom bands are display-only, but frame choice is a separate and equally basic decision.
- **The abstraction level:** does the player ever plot raw burns, or only give intents? The tone of the docs ("ranging is never manual", intent down and reports up) suggests intents by default, with raw burns as a power-user tool.

Intercept windows (meaning 2 in the glossary) are this system's output, so the doc should define how a window is computed and drawn.

### 4. The first playable

Scenario ideas are scattered through the docs (an inspection knife fight, a gray-zone envelope violation, a punitive expedition, "the old mine runs hot"), but none is specified. Missing:

- **The battler's slice.** Two docs defer it: the notes' "which weapons period does the battler cover? Decide with the survey", and the drive survey's "which concepts the battler carries" (proposal: nine drive families). The surveys are done; the decision isn't. Nine drive families is wide for a first playable. A first cut could be chemical, one electric family and solid-core NTR, with missiles and kill vehicles, one gun and one laser. Nuclear weapons follow the bursts study.
- **A scenario spec format:** start state, sides, doctrine presets, objectives, and how a scenario ends. The campaign has no hard end, but a scenario still has to "play to an end in most seeds".
- **The minute-to-minute loop:** what the player looks at, what they decide and how often, how long a session runs. The decision cadence in the notes (about 100–300 s) is the right basis.
- **A fun hypothesis to test:** for example, "a playtester can win an intercept by choosing when to commit, without knowing orbital mechanics".

Proposal: two scenarios, in order. The first stays where Kepler holds (LEO to GEO) to prove rails, orders and intercept windows. The second moves into cislunar space and exercises the three-body answer from blocker 1.

### 5. Attitude and rotation

Posture carries a lot of the design: nose-on against kinetics, radiators edge-on, the dodge crossover, spinal mounts, drive orientation during inspections, roll against lasers. The rotation model behind it is the prototype's placeholder: RCS sized for 3 cm/s² as a couple at the ends, inertia from a lumped mass list. [`design/combat-ranges-and-group-tracks.md`](../design/combat-ranges-and-group-tracks.md) already notes that ignoring turn time flatters the dodger.

Needed:

- rigid-body attitude with the inertia tensor from the physical model;
- RCS and thrust-vectoring as blocks;
- a slew-time law (rate and angular-acceleration limits);
- spin and gyroscopic effects (hab rings, rolled ships, spun belts);
- what each tier does: simulated in fine, a duration in coarse, ignored on rails;
- time-to-turn as an input to dodge doctrine and to event scheduling.

Proposal: add an **attitude control and agility** study to Tier 1.

## Blocks combat, not motion

These can run in parallel with P1–P3.

### 6. The effects studies haven't started

The agenda's own order puts the effects (impacts, bursts, beams, plumes) second, and the notes say the hypervelocity impact study comes before any weapon is modelled. None of them exists yet. The six weapons docs are surveys of concepts and ranges, not the source-neutral deposition models every weapon will call. For the first combat prototype the minimum is:

- **impacts:** a cloud against single and spaced walls, smooth across regimes;
- **bursts:** fluence by output kind, ablation and impulse, dose;
- **lasers:** fluence, dwell and ablation.

### 7. Ship function behind "no hit points"

The docs say ships fail physically (attitude loss, scram, heat death, crew dose, a broken spine) and list the damage channels, but not the functional model that turns deposited damage into lost function. A minimal version for P5:

- components and what each needs (power, coolant loop, control, crew station);
- the power bus and coolant loops, already hinted at by radiator circuits in the ship generator;
- tanks and leaks, crew stations and dose, spine integrity;
- loss conditions as consequences of the above, never a counter.

The ship generator's internal spaces and connections are the right place to hang it.

**Missiles need a decision too.** Missiles are the main long-range weapon in the early eras, but no doc says how they are designed. Building them as small ships from the same generator keeps one pipeline, with the loadout set outside the design as the principles already say.

## Lesser gaps and housekeeping

- **The Research Agenda is stale.** It doesn't yet list the Nov 2 additions: cyber and EMP, reactor-pumped lasers, mounts and recoil, orbital defence architecture, the materials-grades study from the manufacturing note, and now orbits and attitude.
- **No performance budget.** Target counts for full ships, light tracks, projectile clouds and contacts per picture are worth setting now. Pictures scale as polities × contacts × sensors.
- **Communications model.** AI orders and reports travel at c, which needs link geometry (occlusion, relays). The player is instant, so this can wait until AI units act on lagged pictures.
- **Atmosphere scope.** Aerobraking and aerocapture appear in the logistics doc; Earth's atmosphere is the terminal defence layer; low orbits decay. Decide what is in the battler.
- **Crew and acceleration.** Already a Tier 1 study; it sets the torch-era dodge numbers.
- **A truth view for debugging.** Prototyping the picture needs a way to see the world as it is, behind a debug switch.
- **What the clock shows.** With no fixed dates, the UI still needs a time display (elapsed time, or years from the ephemeris epoch).
- **Hard-cutoff audit.** Thresholds worth listing or removing: SOI switching; the ship-generator prototype's clamps (pressure-hull radius 1.6–14 m, crew 2–80, radiator wings going from two to four above 2,500 m²); the mass ledger's open question on a neutron-activation threshold.

## What can wait

| Doc | Why it can wait | What to keep from it now |
| --- | --- | --- |
| Solar Resources (8 files), Resource Fields | Campaign content | Nothing for the battler |
| Mass Ledger | Campaign economy | The Int128 and mass-check bench habit is cheap to adopt early |
| Interplanetary Bulk Logistics, Mass Drivers | Campaign logistics | Its cislunar Δv table and NRHO yard are useful test cases for blocker 1 |
| Manufacturing and the Dependency Ladder | Campaign industry | Preset local-grade blocks in the battler, as the doc suggests |
| Bases, Settlements and the Civilian Economy | Campaign | Owner, jurisdiction and controller fields as day-one scaffolding |
| Shadow Ledger | Campaign faction | The controller field with fidelity |
| Strategic Beams, UREBs, antimatter, hilarious tiers | Far end of the ladders | Nothing; the laws are in the weapon blocks doc |

## Suggested order before and during the first code

1. **Decide the battler's first slice:** region, drive families, weapon families.
2. **Write `design/Orbits, Frames and Propagation.md`,** with a short time-and-numerics conventions section.
3. **Write `design/Ship Orders and Manoeuvre Planning.md`,** including display frames.
4. **Write the first-playable scenario spec.**
5. **Start the attitude study.**
6. **In parallel:** the impact and burst studies, then the minimal ship-function model.
7. **Then code P1 → P6,** benches first as in Fleetwright: propagation drift, determinism hashes, mono-check.

## Decisions needed

- [ ] Body ephemerides: mean elements, or a numerical ephemeris?
- [ ] Cislunar three-body motion: logged exception, restricted three-body near the Earth–Moon pair, or n-body for ships everywhere?
- [ ] SOI switching: log it, or make the reference body a numerical convenience only?
- [ ] Committed trajectories cached as polynomial rails?
- [ ] World-clock representation and resolution.
- [ ] Determinism scope: one machine, or across platforms?
- [ ] Player orders: intents only, raw burns, or both?
- [ ] The battler's first slice: region, drives, weapons.
- [ ] Missiles built by the ship generator?
- [ ] Atmospheres in the battler: none, aerobraking only, or entry and drag?

## Sources

Internal, all read in full or in the relevant sections: [`design/intercept-window-initial-design-notes.md`](../design/intercept-window-initial-design-notes.md), [`design/fleetwright-principles-for-intercept-window.md`](../design/fleetwright-principles-for-intercept-window.md), [`studies/research-agenda.md`](research-agenda.md), [`design/ship-generator-slots-and-physical-model.md`](../design/ship-generator-slots-and-physical-model.md), [`design/combat-ranges-and-group-tracks.md`](../design/combat-ranges-and-group-tracks.md), [`design/detection-and-the-picture.md`](../design/detection-and-the-picture.md), [`design/weapon-blocks-and-engineering-projects.md`](../design/weapon-blocks-and-engineering-projects.md), [`studies/drive-survey-concepts-ranges-and-minimum-sizes.md`](drive-survey-concepts-ranges-and-minimum-sizes.md), [`studies/atomic-rockets-weapons-coverage-and-gaps.md`](atomic-rockets-weapons-coverage-and-gaps.md), [`studies/drives-point-defence-and-kirklin-mines.md`](drives-point-defence-and-kirklin-mines.md), [`studies/weapons-sweep-missed-concepts.md`](weapons-sweep-missed-concepts.md), [`studies/weapons-survey-long-range-concepts.md`](weapons-survey-long-range-concepts.md), [`studies/strategic-beams-x-ray-and-gamma-fels.md`](strategic-beams-x-ray-and-gamma-fels.md), [`design/manufacturing-and-the-dependency-ladder.md`](../design/manufacturing-and-the-dependency-ladder.md), [`design/bases-settlements-and-the-civilian-economy.md`](../design/bases-settlements-and-the-civilian-economy.md), [`design/shadow-ledger-playing-the-unaligned-controller.md`](../design/shadow-ledger-playing-the-unaligned-controller.md), [`studies/interplanetary-bulk-logistics-mines-depots-and-shipyards.md`](interplanetary-bulk-logistics-mines-depots-and-shipyards.md), [`design/mass-ledger-element-groups-and-conservation.md`](../design/mass-ledger-element-groups-and-conservation.md), [`studies/solar-resources/README.md`](solar-resources/README.md). The other Solar Resources files, [`design/resource-fields-grades-and-yield-curves.md`](../design/resource-fields-grades-and-yield-curves.md) and [`studies/mass-drivers-throwing-catching-and-bulk-logistics.md`](mass-drivers-throwing-catching-and-bulk-logistics.md) were not read in full; they are campaign content, and their summaries and cross-references in the docs above were used instead.

Numbers computed here: time-representation ranges from 2⁶³ units; float32 resolution at 1 AU from a 24-bit mantissa; distances per millisecond and per minute from the stated speeds.
