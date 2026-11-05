# Intercept Window: Nothing Beyond the Sun – Initial Design Notes

Oct 30, 2026 · @Teemu

## Title

**Intercept Window: Nothing Beyond the Sun** (chosen Oct 30, 2026; previous working title "Belt Charter").

- **Main title:** names the central concept of both the defense and combat layers (see glossary below). It is a technical term from orbital mechanics, which fits the hard-SF positioning.
- **Subtitle:** a statement of scope. The first game stays within the solar system. A sequel or expansion that reaches beyond it changes the subtitle, so the subtitle marks the moment the scope changes.
- **Tagline candidates:** "Every ship is a weapon. Hold your speed." / "Come in slow, or don't come in at all."
- [ ] Check "Intercept Window" against Steam listings and trademark registries before any public use.

### Glossary: the three meanings of "intercept window"

The phrase does three jobs in this project. Keep them distinct in code, UI and docs.

1. **Defense (traffic control).** The span of distance and time in which a defender's layered systems can still stop an inbound ship, or grind its debris to burn-up size, before it reaches a protected body. Because killing a fast ship leaves a debris shotgun on the same trajectory, the window shrinks as closing speed rises. Speed-limit envelopes are derived from it: a ship must hold its speed low enough that the next defense tier still has a window. Closing too fast is itself the threat, since any ship is a kinetic weapon.
2. **Combat (engagement).** The interval in which a weapon, missile or ship can achieve an intercept with a target given both trajectories, delta-v and sensor range. Missile swarms, especially retrograde swarms on the same orbit closing at combined orbital velocity, exist only as intercept windows: brief, predictable and lethal. The player's combat decisions are about creating, denying and surviving them.
3. **Simulation (scheduling).** One of the decision points the time-compression system computes ahead of time (alongside closest approach, sensor contact, burn end and envelope violation). The sim compresses time to the next window and drops out of compression when one opens.

The independence arc below has a fourth, thematic echo (the period in which breaking away is both possible and survivable), but that is flavour for marketing and writing, not a term used in code or UI.

## Vision and scope

A long-form strategy game covering the period in which independent space colonies form: from the first chartered asteroid-mining ventures to sovereign polities. The company and charter layer is background that shapes the environment; the player-facing focus is colony and base building, ship design and physics-based combat (CoaDE with a strategic campaign layer and greater reach).

- **Setting scope:** the first game stays within the solar system, as the subtitle states. The data model should not rule out other systems (Aurora 4X-style jump points are a possible sequel direction), but no content for them is built.

- **Arc:** contemporary tech and asteroid mining at the start; solar-system colonisation and torchships firing deuterium-filled macron streams at the end.
- **Inspirations:** Rule the Waves and our own naval game for the strategic layer and ship design in context; Children of a Dead Earth for the realistic combat sim and orbital mechanics; Terra Invicta for the solar-system view and colonisation (not the aliens); Aurora 4X for depth, simulation-first design and emergent history; Solar Expanse for the tone of a company-run, all-objects-in-motion solar system.
- **Detail level:** deep simulation strategy in the CoaDE / Terra Invicta / Aurora 4X class. Not a mobile game, not a scripted campaign.
- **No rails, no fixed dates:** eras are tech states, not calendar dates. They emerge from the tech system, research investment and economics, and different polities can be in different eras at the same time. Nothing in the design should assume a scheduled event or a fixed year.
- **Gap being filled:** CoaDE has a superb designer and combat sim but only a fixed mission chain, with no strategic layer.
- **Theme:** in space, every industrial tool is a weapon. Mining lasers, mass drivers, pulse tugs and fusion drives start as infrastructure and end up in combat, so militarisation grows out of the economy.

**Stack and build order:** C# on .NET with the SDL3 GPU API, as Fleetwright. Only the initial C# + SDL3 GPU scaffolding is taken from Fleetwright's first commits; everything else is bespoke. The game is built from the ground up, piece by piece: first a solar system, then ships in it, and onward.

**The first game is a scenario battler,** as in Fleetwright. Ships in space that move, burn and fight are a massive undertaking on their own and the foundation of everything after. Scenarios stand in for charters, economy and research, and the battler is where the ships are tested and fine-tuned. The living solar system is then built on the same simulation, not beside it.

**Scope rule:** design the data model for the long-term dream (up to disassembling planets), but build content for the first game only. Consider a vertical slice of the mid-game first, where mining, colonies and first conflicts overlap, to avoid three half-finished eras.

### Design principles (shared with Fleetwright)

These rules come from our naval game; [`design/fleetwright-principles-for-intercept-window.md`](fleetwright-principles-for-intercept-window.md) has the reasoning, the sources and what is new here.

- **No hard cutoffs.** Nothing becomes a different kind of thing at a hidden size, count or threshold. Ships, drives, envelopes and politics all scale smoothly; where something really must switch, the switch is a stated input or a warning.
- **Physics as numbers in the design, never by period.** Drives, weapons and materials are tech blocks of physical numbers. An era is a label on a family of blocks, and a polity's tech state is the set of blocks it holds.
- **One clock, tiers picked by the asked speed:** Routine (schedules), Rails (Kepler), Coarse, Fine. Never picked by attention or zoom. The sim never reads the display.
- **Fine is the gold standard.** Coarse approximates it by running the same code or fitting to it, never by hand-set numbers.
- **Each polity has its own picture:** contacts with time, source and uncertainty. Light-lag makes this physics. The player sees their polity's fused picture, relayed instantly; [`design/detection-and-the-picture.md`](detection-and-the-picture.md) has what a picture can hold and what it costs.
- **One command path:** the player and AI polities issue the same commands. Intent goes down, reports come up, and doctrine sits around both.
- **Incidents are records.** Every act on the defiance ladder is a command whose full record (what, where, who could see it and when) feeds the polities' politics.
- **The designer never refuses; the world does, and only for physical reasons.** Breaking a charter is allowed and recorded.
- **Deterministic and headless:** commands go in, a snapshot comes out, every number is in settings, and each system has its own seeded stream.
- **Effects are source-neutral.** Weapons don't carry their own damage code. They produce a few kinds of thing: **bursts** (energy and an output partition), **projectile clouds** (impactors with mass, density and velocity) and **beams** (power, wavelength, spot and dwell). One model handles each kind, whatever made it: a fragmenting missile and a sandcaster gun throwing similar pellets do the same damage, and so does a fission warhead versus an antimatter one of matching output.

## Player entity: chartered company

The player runs a chartered company that can mature into a state, modelled on the East India and Hudson's Bay companies.

1. **Start:** a mining venture with Earth-side investors and a sponsoring government granting rights.
2. **Growth:** the charter grants territorial powers: running habitats, policing stations, arming haulers "for protection".
3. **Late game:** sovereign in all but name; declaring independence, or being absorbed back, is a real decision point.

**What the player directly controls:** ship design, fleet operations, where bases and colonies go and how they are built, and the company's posture toward its host. All of it happens inside rules set by other polities: charters, licences, traffic envelopes, inspection regimes. The player can break those rules at any time; the game is about when breaking them is survivable.

**Power comes from constituencies, not ownership.** Early on the player answers to shareholders and the sponsor; later colonists, crews and allied habitats gain weight. The resulting organisational structure (board, governorship, republic, corporate state, guild federation) depends on whom the player empowered along the way.

**AI polities are the same structures** at different points on that path: Earth governments, chartered companies, breakaway colonies. The player is one of them, not a special entity.

**Light-lag forces delegation.** Distant governors and captains act on standing orders, and colonies the player founded can drift and develop their own interests.

Rejected alternative: playing an interest group inside a polity (Victoria 3 style). Harder to tie to fleet design and combat.

## Conflict axes and the dependency curve

The player is both colonizer and potential independence movement, caught between Earth and its own colonists.

| Axis | What is contested | Each side's leverage | Historical analogues |
| --- | --- | --- | --- |
| Company vs host | Charter terms, revenue share, taxes, governor appointments, right to arm ships and own torch drives | Host: capital, skilled people, legitimacy, high-tech components. Company: resources the host wants, distance | American Revolution, East India Company |
| Company vs colonists | Company towns, labour conditions, votes on habitats the company built | Colonists: labour, local legitimacy. Company: ownership, supply | Creole vs peninsular tensions in Latin America |
| Company vs rivals | Overlapping claims, claim jumping, proxy fights for rival hosts | Fleets, charters, host backing | Anglo-Dutch company wars |

**Dependency curve.** Self-sufficiency arrives in tiers: volatiles, structural metals, then electronics, chip fabs and fusion components. Independence becomes viable once the host can no longer cut off critical goods or project force. Force projection depends on delta-v and launch windows, so tech progression feeds directly into politics. Drives and other tech blocks can be bought or engineered at home: a company flying Earth-made drives depends on Earth for them, and whether a sale includes the know-how or only finished units is part of the deal.

**Most conflict sits below open war:** disputes, embargoes, ship seizures, blockades, limited skirmishes. Real battles are rare turning points.

**Proliferation flashpoint.** Fissile enrichment in the belt for Orion pulse units is both a genuine need and a cover story, making it a natural host–colony crisis (inspections, sanctions, covert facilities).

## Independence arc: the leverage curve

The player can tell Earth to go to hell at any moment. Do it too early and Earth crushes them; by the endgame Earth is a backwater and the question has moved on. The arc is the crossing of two curves, and the game is reading where they are.

### The two curves

**Host leverage** over the company, computed per host–company pair and per location:

- **Dependency:** which goods on the self-sufficiency ladder the company still imports from the host, and how long stockpiles last.
- **Deliverable force:** not the host's total fleet but what it can put into the company's orbit: warship tonnage × reachable delta-v × launch windows × transit time × ability to sustain it on arrival.
- **Political will:** the host's domestic appetite for a distant war, other crises it faces, cost already sunk.
- **Legitimacy:** whether colonists, crews, investors and other powers still see the charter as binding.

**Company capacity to resist:** self-sufficiency tier, own fleet and defense layers, constituency support (colonists and crews actually willing to fight), stockpiles, and outside recognition or allies.

Independence is viable roughly when deliverable force plus dependency leverage falls below resistance capacity, for long enough to survive the response. "Long enough" matters: Earth may lose the first round and come back.

### How Earth's leverage evolves by era

Eras here are tech states, not dates, and each side can be in a different one. A company that reaches fusion before Earth gets an early window; an Earth that reaches torch drives first can close it.

| Era | Distance | Earth's leverage | Effect |
| --- | --- | --- | --- |
| Chemical / early fission | Huge: launch windows, multi-year transits | Total. Company imports electronics, reactors, people, spares | Defiance is economic suicide; Earth doesn't even need a fleet |
| Nuclear thermal / pulse | Large but shrinking | Earth controls fissile supply and pulse-unit production; can mount a punitive expedition per window | Window of maximum danger: company has enough to provoke, not enough to resist |
| Early fusion | Months | Earth's industrial lead shrinking; belt chip fabs and fusion components come online | First realistic independence window |
| Torch era | Days to weeks | Earth's share of solar output small; Earth now imports from space | Earth can still strike, but can no longer sustain a war or afford the embargo it would trigger |

**Distance is a decaying shield.** Better drives shrink the solar system for everyone. If Earth fields torch fleets while it still has the industrial lead, the company's distance protection evaporates. The underlying race: does the company's industry outgrow Earth's before drive tech removes distance as a defense? This ties independence directly to who gets which drive tech first, which is why drive rights are charter clauses.

### Earth's decline (backwater, not ruin)

- Earth's economy can keep growing in absolute terms while its share of solar-system output falls.
- The gravity well makes Earth the most expensive place in the system to export from, so heavy industry moves out once it can.
- Leverage inverts: Earth comes to depend on space volatiles, metals and energy. A colonial embargo eventually hurts Earth more than Earth's hurts the colonies.
- Earth keeps the largest population, universities, culture and the oldest legitimacy. "Backwater" means politically marginal, not empty. Historical feel: a former imperial core that still matters, but no longer sets the agenda.
- Late in the torch era Earth is the system's most valuable hostage: every passing torchship is a threat to it, so its traffic-control demands shape inner-system politics. Its atmosphere still gives it a terminal defense layer airless habitats lack.
- In the endgame the antagonists are peer polities: other ex-colonies, rival companies turned states. Former colonies may compete for influence over Earth, inverting the original relationship.

### Defiance is a ladder, not a button

"Screw you" is reachable in one click, but most play happens on the rungs below it. Each rung has a matching host response, and both sides choose how far to climb.

| Rung | Company action | Typical host response |
| --- | --- | --- |
| 1. Foot-dragging | Late revenue, creative accounting, slow-walking audits | Warnings, audit demands, credit tightening |
| 2. Charter violations | Unlicensed armament, unregistered drives, harbouring fugitives, covert enrichment | Fines, inspection regimes, export licence denials |
| 3. Open noncompliance | Refusing inspections, expelling auditors, seizing host property | Targeted embargo of critical tiers, asset seizure in the inner system, freezing Earth-side accounts |
| 4. De facto autonomy | Expelling the governor, colonist assembly takes over, own currency | Charter revocation, claims reassigned to a rival company, blockade |
| 5. Declaration | Formal independence | Punitive expedition, attempted reconquest |
| 6. Recognition | Other powers trade with and recognise the new polity | Diplomatic pressure on recognisers; negotiated settlement or prolonged war |

**Breaking rules is allowed; only physics refuses.** The world refuses what the company physically can't do (tech it lacks, a hull larger than its yards). What a charter forbids (a torch drive, armament over the licence) is allowed and becomes an incident record. How visible the work is (yard size, emissions, supply chain) decides who learns of it and when.

**Proxy enforcement is the host's cheap option.** Earth often won't send its own fleet. Revoking a charter and handing the claims to a rival company (letters of marque in effect) lets Earth fight at someone else's expense, and turns the company-vs-host axis into company-vs-rivals.

**Inner-system holdings are hostages.** A near-Earth station, Earth-side bank accounts and Earth-based staff are within easy reach. Independence can be partial: outer holdings break away while inner ones are seized or kept loyal. Moving assets outward before defying Earth is itself a visible warning sign.

### Declaring too early is not game over

Between the declaration and the arrival of Earth's response there is a gap set by light-lag, transit time and Earth's decision process. That gap is playable: stockpile, fortify, court rivals for recognition, or negotiate a climb-down.

Possible outcomes if the company loses:

- **Reabsorbed:** charter reinstated on harsher terms (garrison, appointed governor, drive restrictions, reparations). Play continues as a punished company that can try again later. Rule the Waves' continue-after-defeat approach is the model.
- **Insurgency or exile:** remnants withdraw to the outer system and fight a long, low-intensity war.
- **Fragmentation:** some colonies stay loyal, others hold out; the company splits.

### Why not just wait? (dominance check)

If Earth only declines, waiting is always optimal and the decision is dead. Counterpressures:

- **Earth reads the trend too.** Rising self-sufficiency is visible: shipyards, chip fabs, torch drives. AI hosts tighten preemptively: demanding garrisons, restricting drive tech, planting loyalist governors, splitting the charter. Waiting invites a preventive war while Earth still has the advantage.
- **Colonists won't wait.** If constituencies want independence and the company stalls, a colonial movement declares without it, possibly against it. The company-vs-colonists axis punishes being too loyal.
- **Rivals move first.** The first polity to break free gets the recognition, defectors and alliances. Or Earth uses the player to crush it, which is its own option.
- **Charter clock.** Renewal and review dates are natural flashpoints, forcing renegotiation on Earth's schedule.
- **Distance decays** (above): waiting through a period where Earth gets torch fleets first can close the window for a generation.
- **Staying has real value.** Earth's protection against rivals, access to high tech, legitimacy, investors. Never formally declaring and sliding into de facto sovereignty is a valid end state, not a failure.

### Earth is not one actor

Earth has several governments and blocs. The player's sponsor has rivals, and those rivals may back the company (France in 1778 is the template): arms, recognition, credit. Defecting the charter to a different host is a middle path between loyalty and independence, and a provocation of its own. Earth blocs also decline at different rates.

### Modelling notes

- Leverage is computed per (host, company, location), not globally, so the map shows where the company is exposed.
- The player sees an intelligence estimate with uncertainty, not a precise bar: e.g. "Earth could place roughly N kt of warships in Ceres orbit within X months." Better pickets and agents narrow the estimate; misreading it is a legitimate way to lose.
- AI polities use the same model to decide when to defy their own hosts and how hard to push back on their own colonies.
- Host responses are chosen through the host's own politics (cost, distance, domestic opinion, competing crises), so the same provocation gets different answers at different times.

## Resources: extraction cost curves

Bodies are modelled by bulk composition plus an extraction cost curve, never as fixed deposits like "Mars has X megatons of metal".

- Mars holds its full 6.4×10²³ kg; the question is what is extractable at the current energy price and tech level.
- Cost drivers: depth, concentration, gravity-well depth for export, energy cost.
- Early game: only surface concentrates pay off. Later: deep mining and gravity-well export. Long-term dream: whole-body disassembly as the curve flattens.

This lets the first game ship with modest content while the planet-disassembly dream remains an extension, not a rewrite.

## Propulsion progression and ship sizing

Drive limits define natural ship sizes; size classes should emerge in the designer, not be hardcoded.

**Binding constraints:**

- **Per-unit power ceiling:** nozzle walls, chamber materials and magnetic nozzle field strength cap one drive's power. Beyond that, cluster, at the cost of plume interaction and failure modes.
- **Waste heat:** radiator area scales with power, not volume, and is usually the main mass sink.

**Radiators can be armoured** (following CoaDE, against the usual "radiators can't be armoured"). Radiators glow, gloriously, and they're a design choice, not a fixed weakness:

- **Thickness is a design input,** with a real thermal conduction model. A thicker fin weighs more, but conducts heat out to its edges well enough that much of the extra mass still radiates. The designer shows the trade between specific mass and toughness, like any other lever.
- **Orientation is the armour.** A flat radiator kept edge-on to the threat presents only its thin edge and a small cross-section, so it takes surprisingly little to keep it from being shredded. **A side shot is devastating:** a radiator caught face-on presents its whole area.
- **That makes attitude a combat skill.** Keeping the radiators edge-on to the threat axis is part of posture, like the drive's orientation in an inspection. Threats from several directions (a crossfire, a flanking missile wave, a cloud spreading past the ship) are dangerous because no attitude is edge-on to all of them. A nearby burst, radiating in every direction, hits whatever faces it.
- **Retraction, heat sinks and stored coolant** are the other options: fight with radiators folded and run on stored heat capacity for a while.
- **Heat is also a signature:** a hot radiator is visible, and pointing it away from an observer is part of hiding.
- **Structural length limit:** spine compression under thrust scales with density × acceleration × length, so high-g ships are compact and big ships are gentle.
- **Fixed overheads:** crew shielding, sensors and reactor minimums cost roughly the same at any size, pushing hulls bigger.
- **Mounting area:** stern area scales with L² while mass scales with L³, but clustering and long spine hulls soften this.

| Drive era | Minimum size driver | Size tendency |
| --- | --- | --- |
| Chemical | Negligible | Tiny to huge; sized by payload and mass ratio |
| Fission electric | Reactor criticality; power-limited thrust | Reactor-and-radiator tugs |
| Nuclear thermal | Reactor criticality | Modest per engine; clustered |
| Nuclear pulse (Orion) | Pusher plate and shock absorbers | Large; improves with size |
| Magnetic confinement fusion | Confinement improves strongly with size | Capital ships first; small craft stay fission/chemical |
| Late torch drives | Minimum shrinks with tech | Torch-drive missiles at the end: the strategic shift |

The rows are families of tech blocks, not switches. Each "minimum size driver" is a curve, so a drive below its sweet spot is poor (heavy for its power), never forbidden. "Capital ships first" has to come out of the scaling, not out of a size limit in code.

**Construction infrastructure** plays the role of RTW's dock size: assembly yards cap hull size until upgraded. As in Fleetwright, the designer never refuses an oversized design; it reports it. The world refuses at lay-down.

## Torchships: strategic weapons, defense and speed limits

Once torch drives exist, every merchant captain can commit an atrocity, which makes torchships a political problem before a military one.

**Scale:** a 1,000 t ship at 100 km/s carries about 5×10¹⁵ J (\~1.2 Mt); at 1,000 km/s, over 100 Mt. A 1 TW drive releases about a quarter kiloton per second down its plume.

**Political consequences:**

- Torch-drive rights become a charter clause and a host–colony flashpoint.
- Traffic control becomes defense: approach corridors, deceleration burns pointed away from inhabited bodies, inspections, transponders. Deviation from a declared trajectory is an alarm.
- Crew and captain loyalty becomes a strategic asset.
- A colony with a few torchships has second-strike capability, which forces the independence question.

**Speed-limit envelopes.** Killing a fast ship leaves a debris shotgun on the same trajectory. With \~1 km/s fragment spread, the cloud needs \~6,400 s to outgrow Earth, so a 100 km/s ship must die \~640,000 km out, beyond the Moon. Allowed closing speed therefore falls with distance, scaled by the defender's reliable kill range. Better defenses allow looser limits and more efficient trade; weak defenders must impose costly slowdowns.

| Layer | Range | Systems and notes |
| --- | --- | --- |
| Detection | Solar system | Burning torches are visible everywhere, but one sensor gives a bearing, not a range; the threat is a cold coast plus late burn. Distributed pickets buy warning time, and pickets far apart buy triangulated positions ([`design/detection-and-the-picture.md`](detection-and-the-picture.md)). |
| Long | Light-seconds | Free-electron lasers; range set by diffraction (shorter wavelength, bigger optics). Ablating one side deflects rather than fragments. Light-second reach takes large fixed installations; warship lasers reach about 10⁵ km even in the torch era ([`design/combat-ranges-and-group-tracks.md`](combat-ranges-and-group-tracks.md)). |
| Medium | Thousands of km | Sandcasting pellet clouds, kinetic interceptors, macron streams, pre-placed corridor mines. |
| Short | Hundreds of km | Nuclear bursts and dense pellet fields grind debris to burn-up size. |
| Terminal | Atmosphere | Earth's atmosphere is a last-ditch shield airless habitats lack, an asymmetry that shapes who can provoke whom. |

**Gray-zone drama:** a merchant with a drive fault drifts out of its envelope. Shooting or not shooting can each start a war or a massacre.

## Combat and time model

One unified real-time simulation with time compression, as in the naval game, with no separate combat mode.

- **Analytic coasting:** ballistic trajectories propagate with Kepler's equations, so jumping a month costs the same as a second and stays exact.
- **Multi-rate bubbles:** numerical integration only where objects thrust or interact. An engagement is a region where the sim works harder.
- **Decision-driven compression:** the sim computes time to the next decision (closest approach, sensor contact, intercept window, burn end, envelope violation), compresses to it, then drops. Aurora 4X's interrupts are a precedent.
- **Consistent cadence across eras:** decision rhythm ≈ range ÷ closing speed. Early: 1,000 km at 10 km/s ≈ 100 s. Torch era: 300,000 km at 1,000 km/s ≈ 300 s. Ranges and speeds grow together.
- **Clock tiers, as in the naval game:** Routine (mining and freight as schedules), Rails (Kepler), Coarse and Fine, all on one clock. **The asked speed picks the tier**, for every engagement at once, never attention or zoom. Fleetwright tried picking by attention first and dropped it. A hit is the same in both tiers; coarse approximates the *rate* of hits.
- **Coarse is calibrated against fine:** the same code where possible, fitted tables where it must be, never hand-set numbers. A parity bench plays scenarios both ways over many seeds, within agreed bands.
- **Concurrency:** doctrine and delegation for minor incidents (justified by light-lag) so one skirmish doesn't stall the whole solar system. Captains don't queue requests for the player. Their notices go to the log, and a user-configurable interest table decides what drops the speed or pauses (no decision queue, no camera jumps).
- **Speed drops are the sim's, at the exact event time.** The player never overshoots a contact or an envelope violation.
- **Higher tiers are close enough, not exact.** Routine and rails may collapse procedures into durations (a docking skipped, a similar wait added to the cargo transfer), as long as outcomes land near the fine version and dropping in at any moment finds a plausible state. Exactness is kept where outcomes are decided: fights in fine and coarse.
- **The player's orders are instant;** the player is the exception to light-lag. AI polities and commanders send orders and receive reports at c. The player's picture is relayed instantly too: each sensor reading reaches the player when it is taken, though it is as old as its light ([`design/detection-and-the-picture.md`](detection-and-the-picture.md)).

**Engagement range spread:** all-out war even with near-future tech means long-range missile exchanges, but enforcement actions produce knife fights (next section). The sim must handle kilometres to light-seconds, likely needing different UI per scale.

**Combat ranges and group tracks** ([`design/combat-ranges-and-group-tracks.md`](combat-ranges-and-group-tracks.md)). Each weapon family has its own range limit, and they scale differently with tech:

- **Unguided kinetics** are limited by the target's dodge. Ranges stay around 100 km until macron speeds push them to thousands of km.
- **Lasers** are limited by diffraction, R ∝ D · √P / λ. They grow fastest, from about 50 km to about 10⁵ km for warships.
- **Missiles** are limited by a Δv duel against the target's dodge, which starts when the target sees the missile.

A distant fleet is a group track (centroid, velocity and spread) for the picture, aiming and the scheduler. Hits always resolve per ship.

### Posture against dodging

A ship can either present its armoured nose and edge-on radiators to the threat, or dodge. It can't do both well:

- **Dodging means thrusting sideways to the threat.** The main drive points aft, so a real dodge means turning away from the nose-on posture, exposing the flanks and the radiators' faces, or making do with weak lateral thrusters. Long-spined ships turn slowly, which costs more time.
- **Whether a dodge works is geometry.** In the projectile's time of flight (range ÷ closing speed), lateral acceleration *a* moves the ship ½ *a* t². A dodge works when that clearly exceeds the weapon's aim error and spread. Far out, flight times are long and erratic bursts make unguided shots miss. Close in, the time is too short, so the ship turns nose-on and weathers it. Somewhere between lies the crossover, and that's the decision.
- **The crossover depends on the weapon:**
  - **Unguided kinetics:** dodge far, weather close. Faster projectiles shrink the zone where dodging pays.
  - **Clouds:** the spread already covers small dodges. Only getting out of the cone helps, and that takes time.
  - **Missiles and guided kill vehicles:** dodging works only by outlasting their Δv or acceleration, so endgame jinks against a missile with little Δv left.
  - **Lasers:** light-speed shots can't be dodged at short range. At light-second ranges, the shooter aims at where the light showed the target a round trip ago, so random jinks spoil the aim and dodging pays again.
  - **Nuclear bursts:** distance from the burst matters, not the line of fire. Dodging means staying clear of where a warhead can get to before it detonates.
- **It changes with tech, with nothing hard-coded.** Faster guns, better guidance and longer-ranged lasers shrink the dodging zone; higher-thrust drives and stronger lateral thrusters widen it. The balance between dodging and armour shifts as blocks change, and it comes out of the same geometry every time.
- **It's doctrine and captain's judgement.** Fleetwright's doctrine already has an evasion field (steady, zigzag, chase salvos, and from what range). Here it becomes a rule by weapon and range: jink beyond the crossover, nose-on inside it. The captain reads the threat's kind from the picture, so misidentifying a weapon is a mistake that costs ships.
- **The coarse tier must capture it.** Fleetwright found dodging is where coarse is weakest, and gave it its own parity layer. The same goes here: coarse ships must jink and turn nose-on as fine ones do, and the bench measures hit rates by threat, range and target agility.

## Enforcement engagements and damage channels

In enforcement actions, range is set by politics: neither side fires first, so they end up alongside each other, where everything is lethal.

- **Matched velocity:** inspections need relative speeds of metres per second. Missiles barely arm; CIWS guns and close-range lasers dominate.
- **First shot is decisive:** posture is the gameplay. Weapons hold/free, firing solutions, whether a targeting-laser lock is a hostile act.
- **The drive is a weapon:** a ship flipping its drive toward an inspector can kill it, so protocols dictate orientation and drive state; rotation is an alarm.
- **Collateral:** debris near stations or busy orbits threatens everyone, restraining the enforcer and giving smugglers leverage.
- **Nonlethal toolkit:** sensor dazzling, tethers and nets, drive-disabling shots, docking clamps, boarding. Analogues: Cod Wars, South China Sea water cannons, Strait of Hormuz seizures.
- **Fine-tier model:** Clohessy–Wiltshire (Hill) equations for relative motion near a reference orbit; cheap, analytic, and capture counterintuitive orbital maneuvering.

**Damage channels instead of hit points:** thermal load, ablation, spall, radiation dose, component activation.

*Example: D-T pellet fields.* 200 µm shells (\~10 µg) at 1,000 km/s carry \~5 kJ each (\~1 g TNT). Impact fusion becomes plausible near 1,000–1,400 km/s, though thresholds are uncertain and burn fraction low; fusion at best roughly doubles the energy. The distinctive effect is 14 MeV neutrons irradiating crew and electronics. A decelerating torchship's forward plume vaporises pellets, so fields mainly threaten ships coasting or accelerating inbound, exactly those breaking speed limits.

## Nuclear weapons in space

Nuclear weapons are in the scenario battler, because in vacuum they work very differently from on the ground and that difference is good gameplay. Children of a Dead Earth's research is the reference to start from.

**Why they disappoint at range:**

- **No blast wave.** On the ground most of the yield goes into heating air, which makes the fireball and shock that do the damage. In vacuum there's no air, so most of the yield leaves as X-rays (roughly 70-80 %), with the rest as neutrons, gamma rays and fast bomb debris.
- **Everything falls off as 1/r².** Nothing carries the energy outward but radiation and debris, so the fluence on a target drops with the square of the distance. The effective radius only grows with the square root of the yield: 100× the yield buys 10× the radius.
- **So they must hit surprisingly close.** A rough estimate to check against CoaDE and the sources: from 1 kt, X-ray fluence is about 20 J/cm² at 1 km and about 2 kJ/cm² at 100 m. Heavy damage to an armoured hull needs tens to hundreds of metres; soft targets (sensors, thin structure, and thin radiators facing the burst) are hurt out to around a kilometre. A megaton pushes those distances out about 30×.

**What a burst does (the damage channels):**

- **X-ray ablation:** the surface layer flashes to vapour. Its blow-off drives a shock into the hull (spall, structural damage) and gives the ship an impulse. Radiators are the soft spot when they face the burst. A burst radiates in every direction, so the edge-on posture that protects them against a single threat axis protects them only from bursts in their own plane.
- **Neutrons and gammas:** crew dose and electronics damage at ranges where the hull is unharmed. Neutrons also activate the structure, making it radioactive.
- **Debris:** a fast plasma shell, mostly important very close.
- **No EMP in the ground sense away from a planet.** Near one, a burst can pump the radiation belts (Starfish Prime, 1962, which went on to kill satellites for months). That is collateral every polity in Earth orbit suffers, so a nuclear exchange near Earth is a political act as much as a military one.

### One burst model, source-neutral

The "big booms" simulation doesn't know what made the boom. A fission warhead, a fusion warhead, a future megaton-class antimatter missile, a pulse unit or a drive or reactor failing all go through the same calculations. Only the numbers describing the burst differ. Fleetwright has the same rule: one gas model serves a shell's burst and a magazine's venting alike, with no second engine.

**A burst is a block of numbers:**

- **Energy:** the yield.
- **Output partition:** how the energy splits between soft and hard X-rays (with a spectral temperature), gamma rays, neutrons (with their energy spectrum), charged particles and debris (mass and speed). This is where sources really differ. A fission burst is mostly soft X-rays. A fusion burst puts more into fast neutrons. A bare antimatter burst puts much of its energy into charged pions and hard gammas and little into X-rays, unless the warhead is built to convert it.
- **Geometry:** isotropic, or shaped into a cone or jet (Casaba-Howitzer-style), as a share of the energy in a direction and a spread.
- **Where and when:** a point and a time, and the velocity of the burst's centre.

**The calculations are shared:**

- **Propagation:** each output kind spreads with distance (1/r² for an isotropic burst, the cone's solid angle for a shaped one), with no medium to absorb it in vacuum. Near a planet the atmosphere and the magnetosphere act on it: the terminal shield on one side, belt-pumping on the other.
- **Attenuation through the target:** each output kind passes through each material by its own law (X-rays stopped at the surface, gammas and neutrons through the hull to the crew and electronics, charged particles depending on energy and any magnetic field).
- **Deposition into the damage channels:** surface ablation and the shock it drives, impulse on the ship, dose in each space, activation. These are the same channels as every other weapon, so a burst is just one more deposition event.

**What differs is data, not code.** A new warhead or source is a new burst block, produced by research and engineering like any other block. A new kind of output (some future exotic particle) adds an attenuation law and a deposition rule, without touching the rest.

**Weapons built around this,** from the Atomic Rockets archive, to be evaluated:

- **Proximity-fused warheads** on missiles. Fusing is decisive, since a miss by a kilometre is a miss.
- **Nuclear shaped charges** (Casaba-Howitzer): a burst channelled into a fast jet of plasma or pellets, which extends the reach well past the bare burst's.
- **Bomb-pumped X-ray lasers** (Excalibur): a burst turned into beams at long range.
- **Nuclear mines and corridor denial:** pre-placed bursts that only make sense with fusing this precise.

**Ties to the rest of the design:**

- Fissile material is the same proliferation flashpoint as Orion pulse units: a pulse unit is a nuke, and the line between the two is mostly intent.
- Nuclear use is the obvious top rung of the incident ladder, and observers detect it at once anywhere in line of sight.
- In the damage model a burst is one more deposition event (above), through the same channels as kinetics and lasers.

## Impacts: one model for everything that hits

As with bursts, the impact model doesn't know where a projectile came from. Weapons and events produce **projectile clouds**, and one model turns a cloud meeting a target into damage. A missile that fragments before the target and a sandblaster-style gun firing similar pellets give the same result if the clouds match.

**A cloud is a block of numbers:** the number of impactors, their mass distribution, their density, the cloud's mean velocity relative to the target and its spread (a cone and a velocity dispersion), and its shape over time. It's the same description at every scale:

- **Sources that make clouds:** sandcasters and pellet guns, flak and fragmenting warheads, shotgun-style kinetic kill vehicles, macron streams, pre-placed corridor mines, a single slug from a mass driver (a cloud of one), and the debris of a ship that was killed.
- **The debris shotgun is a cloud too.** The speed-limit envelopes are derived from how a dead fast ship's debris spreads. That calculation and a fragmenting missile's pattern are the same model, so the defence planning and the combat agree by construction.

**Physics by regime.** In the hypervelocity regime, the pressures at impact dwarf the materials' strength, so the event becomes hydrodynamic. For compact projectiles, the outcome then depends mainly on the projectile's mass, density and velocity and the target's density, not on the exact shape or alloy. The slower regimes are where it gets hard:

| Regime | Roughly (depends on the materials) | What decides the outcome |
| --- | --- | --- |
| **Ballistic** | below ~2–3 km/s | Strength, hardness, shape and obliquity: classic armour penetration, the hardest to model |
| **Shatter / transition** | ~3–7 km/s | The projectile breaks up on impact; strength still matters, and less as the speed rises |
| **Hypervelocity** | above ~7 km/s | Hydrodynamic: density ratio and energy; strength and shape matter little for compact projectiles |
| **Vaporising** | tens to hundreds of km/s and up | Projectile and target vaporise and then ionise; the impact behaves like a small explosion and hands its energy over to the **burst model** (at ~1,000 km/s, possibly with the D-T pellets fusing) |

- **No hard cutoffs:** the regimes blend smoothly across the boundaries, which are themselves material numbers, not constants in code.
- **Shape still matters in one case:** long rods. A rod's penetration in the hydrodynamic regime tends towards its length × √(projectile density / target density), so a rod goes deeper than a sphere of the same mass. The model takes the aspect ratio as an input, and it matters only for elongated projectiles.
- **Spaced armour wins at hypervelocity.** A thin bumper shatters and vaporises a fast impactor into a spreading cloud that the main wall can survive (the Whipple shield principle). This should come out of the model on its own, and it's a real design choice in the designer: whether to carry bumpers, how far out, and how thick. Against slow ballistic-regime rounds, bumpers help much less.
- **Many small hits add up:** sandblasting is fluence. Paint, sensors, radiators and optics erode under a cloud that doesn't hole the hull. The cloud model deposits into the same damage channels (ablation, spall, holes, impulse) as everything else.

**Fleetwright precedent:** a shell's burst is already split into "the burst makes fragments" (Gurney, Mott) and "fragments penetrate" (THOR equations), with the plate model separate. Here, the source makes a cloud, and the impact model takes it from there.

**The hypervelocity impact study** comes first, before any weapon is modelled: impact models for a range of impactor sizes, densities and speeds, against single walls and spaced walls. Sources to start from: NASA's ballistic limit equations for Whipple shields (Christiansen), cratering scaling laws (Holsapple), hydrodynamic penetration (Tate–Alekseevskii), and Children of a Dead Earth's impact research.

## Views: the commander's map and the eye candy

The same concept as Fleetwright: one continuous zoom, with **zoom bands that only change how things are drawn**, never what the sim does.

- **Zoomed out: the tactical layer.** Icons, tracks, trajectories, intercept windows, envelopes and uncertainty shapes: a commander guiding their forces. This is where the game is mostly played, from the whole system down to an engagement thousands of kilometres across.
- **Zoomed in: the eye-candy level.** The ship itself, close enough to see what is happening to it. The example to aim for: a hull after a nuclear attack, its armour glowing and visibly cooling as black-body radiation and conduction carry the heat away, the bright patch on the burst side spreading into the structure and dimming from white through orange to dull red.

**The look reads the sim; it never invents** (Fleetwright's "VFX is for fluff, and VFX never misleads"):

- **The glow is the sim's thermal state, drawn.** The hull and radiators carry a temperature field anyway, because heat decides radiator performance, damage (melting, ablation, spall) and the infrared signature. The look turns that field into black-body colour and brightness. The same field drives what enemies detect, what breaks, and what the player sees glowing, so the three always agree.
- **The look may add detail, not heat.** It can interpolate a coarse thermal grid smoothly, add surface texture, flicker and the conduction's soft edges. It never shows a hot spot where the sim has none, or hides one the sim has.
- **Radiators glow by the same rule.** A working radiator glows at its operating temperature, a damaged one cools unevenly where the coolant loop is broken, and a radiator dumping a burst load brightens. The player can read the ship's heat state by looking.
- **Visuals stay light until the gameplay systems are in** (Fleetwright decision 10): the tactical layer first, and a VFX pass later that can replace any look without touching the sim.

## The ship generator: technical inputs in, a 3D ship out

**This is a 3D game.** Ships are 3D models with relatively simplified shapes, in the vein of Children of a Dead Earth: cylinders, cones, trusses, tanks, plates and radiator panels, not greebled film models. Everything is **procedurally generated**, as Fleetwright's shipgen is.

**The pipeline is shipgen's, in 3D:**

1. **The design is the technical input:** drive and reactor blocks, tanks and propellant, radiators (area, thickness, layout), armour (layers, spacing, thickness by face), weapons and their mounts, sensors, crew spaces, and the spine. It's choices and numbers, with no hand-placed geometry.
2. **The generator lays out the ship:** it places the parts along the spine and around it, sizes the structure for the thrust, and outputs **the physical model**: parts with 3D geometry, mass and materials, the internal spaces and their connections (pressure, coolant, power), the armour layers, the hitboxes, and a report (mass, Δv, acceleration, heat budget, moments of inertia, turn rate).
3. **The drawing reads only the physical model** (Fleetwright: "Don't add geometry the drawing needs anywhere but the hitbox model"). The 3D mesh is generated from the same parts the sim hits, so what you see is what gets shot. A look may dress a part (panel lines, paint, a polity's style) but never move or reshape it.

**Rules carried over from shipgen:**

- **Design and drawing are separate,** with a plain-data contract between them. The design side is fast enough to rerun on every change in the designer; the mesh may lag behind.
- **No hard cutoffs, monotone sizing:** adding mass never makes a lighter ship, and nothing changes kind at a hidden size. Check it with a lever sweep like Fleetwright's `mono-check`.
- **The generator is permissive:** silly designs build and run. Limits are reported, never refused, and the world refuses only what is physically impossible.
- **Looks are visual only,** indexed by polity and style, never touching the physics or the hitboxes.
- **Regression from the start:** golden outputs for a set of reference designs, a fuzzer over mutated designs, and checks that the mesh and the hitboxes agree.

**Visual prototypes come early:** a few proto ships generated from technical inputs, to settle the shape language (how a pulse drive's pusher plate, a fusion torch, radiator wings, spaced armour and a long spine look together) before the generator's rules are written in earnest.

## Data and sourcing approach

## Data and sourcing approach

Engineering detail is input data gated by tech, not simulated; curves are fitted to Atomic Rockets (Project Rho) drive tables.

- **Tech blocks, not tech levels:** a drive, a pulse unit or a warhead is a block of physical numbers with a name as its label, and a design carries the blocks it uses. **In the campaign, research and engineering are separate systems:** research drives what is known (it opens a principle), and engineering produces the drives (a block whose numbers depend on what was invested), so drives improve continuously and two polities' versions differ. Blocks can be **bought from others or engineered at home**, so tech feeds the dependency curve directly. There is more real research here than in Fleetwright, where admiralties mostly engineered from what industry offered. In scenarios, a preset catalogue fitted to the sources stands in (as Fleetwright's catalogues do today, before its research system). The sim and the designer never know which. Yields are block inputs, not engineered from components; CoaDE-style component engineering is out of scope at this scale.
- **Drive tech as curves:** minimum power, maximum per-unit power, specific power, exhaust velocity, waste-heat fraction.
- **Data, not code:** each drive tech is a small parameter table tagged with its source, retunable without touching the sim.
- **Sanity check:** jet power = ½ × thrust × exhaust velocity. A drive implying more jet power than its reactor supplies is broken.
- **Watch waste heat:** many sources gloss over it, but it sizes the ships.
- **Nuclear industry stays abstract:** enrichment and pulse-unit production are facilities with power draw, throughput, cost and political visibility only.

## Open questions

- [x] Does the game continue after independence? **Yes.** Play continues past independence and past Earth becoming irrelevant, into a system of peer polities where torch-era combat lives.
- [x] What is the first game? **A scenario battler,** as Fleetwright's battle module: the full-fidelity ship and orbit sim, with scenarios standing in for charters, economy and research (inspections, envelope violations, a punitive expedition).
- [x] The scenario battler's range. **Wide:** from essentially contemporary chemical rockets in cislunar space, through pulse drives, to fusion.
- [ ] Survey the whole Atomic Rockets (Project Rho) archive for the base points: drives, power, radiators, sensors, weapons. Set the battler's exact range after it.
- [ ] Which weapons period does the battler cover (kinetics, lasers, missiles, nuclear-driven weapons)? *Decide with the survey.*
- [ ] Nuclear weapons in space: check the effect radii above against CoaDE's research and the sources (yield, X-ray fraction, ablation and hardening thresholds, crew dose).
- [ ] Hypervelocity impact study: models for various sizes, densities and speeds of impactor against single and spaced walls, across the regimes, before weapons are built on it.
- [ ] Visual prototypes of procedurally generated ships: settle the 3D shape language before the generator's rules.
- [ ] Beams: the matching source-neutral model for lasers and particle beams (power, wavelength, spot size by diffraction, dwell, target reflectivity and ablation).
- [ ] Combat ranges: replace the first-cut numbers in [`design/combat-ranges-and-group-tracks.md`](combat-ranges-and-group-tracks.md) after the beams and guidance studies. *Detection is in [`design/detection-and-the-picture.md`](detection-and-the-picture.md). The laser damage threshold and the target's lateral acceleration are the inputs that move every range.*
- [x] Start date and era timeline. **No fixed dates.** Eras emerge from the tech system; there is no scripted timeline.
- [ ] Tech system design: how research, industry and economics pace progression so eras emerge (and how far apart polities can drift in tech).
- [ ] Starting conditions: what tech state, polities and holdings a new campaign begins with (a start state, not a start date).
- [ ] Exact abstraction level of the combat sim per tier. *Calibration proposal: Fleetwright's rung ladder and parity bench.*
- [ ] How constituencies are modelled mechanically (influence, loyalty, legitimacy). *Tempers that add (polity, governor, captain) cover part of it.*
- [ ] UI for trajectories, intercepts and damage across km-to-light-second scales. *Proposal: zoom bands (display only) as in Fleetwright, separate from clock tiers.*
- [ ] How deliverable force is estimated cheaply enough to recompute per location. *Proposal: one "matchup" implementation over transfer-window reachability, fed by each side's picture and kept consistent with the coarse resolver. The host, the company, the AI and the player's intelligence estimate all use it.*
- [ ] How AI hosts decide between proxy enforcement, embargo and direct expedition. *Proposal: a scoring function over the matchup and the host's politics, with hysteresis, no search.*
- [ ] Is there a hard end condition, or does the campaign run until the player stops? *Proposal: no hard end. As in Fleetwright, a clock never ends a fight that's going on; the campaign runs until the player stops.*
- [ ] The yardstick: with no torch-war history, what are models judged against? *Proposal: physics reference calculations for mechanisms, real test data where it exists, political analogues as shapes only, and the fine tier for coarse.*
- [x] Light-lag and the player's orders. **Instant;** the player is the exception. A command nexus whose placement matters was considered and is open to arguments and playtesting.
- [x] Is the player's *picture* light-lagged, or only the AI polities' pictures? **Decided (Nov 1): the player sees the polity's fused picture, relayed instantly.** Each sensor reading reaches the player the moment it is taken, though it is as old as the light that made it, so the only lag the player feels is from the target to the nearest sensor. That makes the player an FTL observer of their own sensor network, which is the accepted cheat, and gives sensor placement a direct payoff. Units under AI control follow the lag, the player's own included (Oct 30), so the player's faster-than-light view reaches the world only through units the player takes over directly. See [`design/detection-and-the-picture.md`](detection-and-the-picture.md).
- [x] Tension and incidents in the first cut. **The scaffolding goes in from the start,** built piece by piece.
- [x] Code shared with Fleetwright. **Only the initial C# + SDL3 GPU scaffolding** from its first commits; everything else is bespoke. Same stack: C# and SDL3 GPU.
- [x] How exact the higher time tiers must be. **Close enough:** procedures may collapse into durations.
- [ ] Can Earth itself fracture or be absorbed by a former colony in the late game?
- [x] Working title: Intercept Window: Nothing Beyond the Sun.
- [ ] Trademark and Steam availability check for "Intercept Window".
