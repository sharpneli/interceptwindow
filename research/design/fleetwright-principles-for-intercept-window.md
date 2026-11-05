# Intercept Window: Principles Carried Over from Fleetwright

Oct 30, 2026 · @Teemu

A read of Fleetwright's design docs (the naval game, pre-alpha) for decisions that should hold in Intercept Window too. Sources read: `docs/world/architecture.md`, `docs/battle/plan.md`, `coarse.md`, `command.md`, `command-ui.md`, `fighting.md`, `fire-control.md`, `shells-armour-damage.md`, `fire.md`, `damage-control.md`, `smoke.md`, `night.md`, `magazines.md`, `crew.md`, `workers.md`, `docs/missions/plan.md`, `docs/map-ui/README.md`, `docs/map-ui/launch.md`, `docs/designer-ui/overview.md`, `docs/shipgen/DECISIONS.md`, `research/REQUESTS.md`.

**Status:** proposals, with Teemu's answers of Oct 30, Nov 1 and Nov 2 folded in (listed under "Decided" at the end). Where a Fleetwright decision conflicts with the initial notes, the notes have been updated to follow Fleetwright and the change is listed at the end.

## The short version

| # | Principle | In Fleetwright | What it means here |
| --- | --- | --- | --- |
| 1 | **No hard cutoffs** | "Your ship is 10 cm too long, now it's a fundamentally different kind of ship" is banned; no hard switches anywhere | Drive families, ship sizes, envelopes and politics all scale smoothly. Eras are labels, not switches. |
| 2 | **Physics as numbers in the design, never by period** | A year is only a template's label; 10 t of armour weighs 10 t in any year | A drive is a block of numbers, produced by research and engineering in the campaign. "Fusion era" is a name for a family of blocks, not a game state. Fits "no fixed dates" exactly. |
| 3 | **Clock tiers on one clock, picked by the asked speed** | Routine, Rails, Coarse, Fine; the speed picks the tier, never attention or zoom | Kepler orbits are rails (KSP is the precedent Fleetwright itself cites). Mining and freight are routines. |
| 4 | **Fine is the gold standard; coarse approximates it** | A rung ladder and a parity bench; never hand-set coarse numbers | Answers the open question on calibrating the statistical resolver. |
| 5 | **Each side has its own picture** | Fog of war is knowledge of entities: what is known, when, from what source, with uncertainty | Light-lag turns this from game friction into physics. The leverage estimate is a picture. |
| 6 | **One command path for player and AI** | The player and the AI issue the same commands; an NPC navy is a command source | Already in the notes ("AI polities are the same structures"). Fleetwright shows how to build it. |
| 7 | **Intent down, reports up, doctrine around** | Tasks down the chain, status codes up, doctrine as presets defined by values | Governors and captains on standing orders under light-lag. |
| 8 | **The incident record** | The "insane captain": firing in peacetime is a command, recorded in full, and the record feeds relations | The defiance ladder is this mechanism generalised. |
| 9 | **The designer never refuses; the world does** | Limits are reported, not enforced; the check happens when a ship is commissioned or laid down | Split the world's refusal in two: a physical "can't" and a legal "mustn't". |
| 10 | **Deterministic, headless, commands in and snapshot out** | Every number in `SimSettings`, seeded streams, no allocation in a step | The same engineering rules, written fresh. Only the initial C# + SDL3 GPU scaffolding is taken from Fleetwright. |

## 1. Scaling: no cutoffs, physics as numbers

### No arbitrary size cutoffs

This is the most strongly held rule in the Fleetwright docs (`DECISIONS.md`: "after many games with that, the user has an allergy to it"). A ship 10 cm longer, with one more crewman or 1 mm more calibre, must never become a different kind of ship: no feature appearing or vanishing, and no step in weight, volume or crew at a hidden threshold. The allowed alternatives:

1. a smooth rule;
2. a design input whose default comes from the old rule;
3. where something really must switch, a stated input or a warning in the report, never a silent change.

The rule spread through every later system:

- **Fire:** "No size cutoffs: anything that scales with the ship scales smoothly with it."
- **Damage control:** "No hard switches, no size cut-offs. Eras differ by their numbers."
- **Night:** "Interpolate on light, never switch on time of day."
- **Smoke:** "No hard switches. No row by navy or type."
- **Crew:** "A station's work falls smoothly with its men."

**For Intercept Window:**

- **The drive table must be curves, not rows.** "Magnetic confinement fusion: capital ships first; small craft stay fission" should come out of the confinement-vs-size scaling curve. No minimum hull size is coded. Below the curve's sweet spot the drive is simply poor: heavy for its power, so a small ship pays dearly for it.
- **Envelopes are graded.** The allowed closing speed is a continuous function of distance and of the defender's kill range, as the notes already have it. Enforcement responses are graded by doctrine (warn, shadow, dazzle, disable, kill), not triggered by a single line.
- **Politics too:** constituency weight, legitimacy and dependency are continuous. A colony doesn't "become a republic" at 50,001 people. Any structural change of government is an event with a stated cause.
- **Monotone sizing** (`DECISIONS.md`: "if I remove a gun the weight should go down"): adding mass to a design never gives a lighter ship. Fleetwright has a `mono-check` tool that sweeps the design levers and lists reversals. Build the same check into the spaceship designer from day one.

### Physics as numbers in the design, never by period

Fleetwright's first damage principle: "Differences between periods come from material science, given in the design as numbers." Nothing reads a year. A shell, a plate, a plant or a rangefinder is a **tech block**: physical numbers with a name as the label, written to a catalogue by a tool from the research tables. A design carries the blocks it uses. **Calibrated levels become presets:** "level 3" is a named combination of blocks, not a type.

**The fixed catalogue is a placeholder** (Teemu, Oct 30). Fleetwright has no research system yet, so its catalogues of hand-made blocks exist to let scenarios be played. In the campaign, **research and engineering systems produce the blocks.** The lasting part of the principle is the contract: the sim and the designer read a block's physical numbers and never ask where it came from or what year it is.

This is the mechanical answer to "no rails, no fixed dates":

- A drive is a block: exhaust velocity, specific power, maximum power per unit, waste-heat fraction, minimum mass curve, fuel. "Early fusion" is a label on a family of blocks.
- **In the campaign, research and engineering are separate systems** (Teemu, Oct 30; Fleetwright will have the same split). **Research drives what is known:** it opens a principle (magnetic-confinement fusion). **Engineering produces the drives:** it turns known principles into concrete blocks whose numbers depend on what was invested and learned, so a polity's third-generation fusion drive is better than its first, and two polities' "early fusion" drives differ. Numbers improving continuously with engineering fits "no hard cutoffs" better than unlocking fixed catalogue rows would.
- **A block can be bought or engineered at home.** A polity either designs its own drives or purchases them from others. That ties tech straight into the dependency curve: a company flying Earth-made drives depends on Earth for them, and engineering its own is a step up the self-sufficiency ladder. Selling or licensing a block is trade and diplomacy, and whether the buyer gets the block, the engineering know-how, or only finished units is part of the deal.
- **More real research here than in Fleetwright.** Admiralties rarely funded basic research; they mostly engineered from what industry and science offered. Here research is a main activity of polities and companies, with engineering on top of it.
- **In a scenario, a preset catalogue stands in for research,** as in Fleetwright today.
- A polity's tech state is the set of blocks it holds and can build (Fleetwright's `TechSet`). The designer and the sim never know whether a block came from research or a preset.
- Two polities "in different eras" just hold different blocks. Nothing in the sim has an era variable.
- **Allow silliness** (Fleetwright: "nothing in the block is limited by period or plausibility, only by what can physically be"). A player's odd drive is a block like any other, provided it passes the physics checks (jet power ≤ reactor power, waste heat accounted for).

This replaces the initial notes' "pulse-unit and warhead yields are set per tech level". They are numbers in a block, and research and engineering decide which blocks a polity has and what their numbers are.

### Realism gradient: engineering near, physics far (Teemu, Nov 2)

How realistic a block must be depends on how far it is from today:

| Distance from today | What a block must match |
| --- | --- |
| **Demonstrated** | Engineering data: real hardware, tests, failure modes |
| **Studied** | Published design studies, scaled honestly |
| **Physics-only** | Conservation laws, material strength limits, diffraction, thermodynamics, light speed; nothing else |

- **Every engineered number carries a basis tag** along its curve. Start values and the early curve come from demonstrated or studied sources; the ceiling is always a physics limit; the far end of the curve is physics-only.
- **Physics is the only final limit.** Nothing in the game is forbidden except what physics forbids. Everything else is cost, time, visibility and politics.
- **Deviations are logged exceptions.** When the game breaks this rule (for play, pacing or because nobody knows the physics yet), the break is listed under "Logged exceptions" at the end of this doc: what deviates, from which rule, why, and what would remove it. An unlogged deviation is a bug.

[`design/weapon-blocks-and-engineering-projects.md`](weapon-blocks-and-engineering-projects.md) applies the gradient to weapons.

## 2. Time: clock tiers on one clock

Fleetwright's `architecture.md` is the most directly transferable document. Its core idea: **what can be known in closed form isn't stepped, it's evaluated; the sim jumps between events.** Fleetwright cites Kerbal Space Program's "on rails" as the prior art. Here the rails are literal.

| Fleetwright tier | How it advances | Intercept Window equivalent |
| --- | --- | --- |
| **Routine** (peacetime, up to ~1,000,000x) | A schedule. Position and rates (fuel, money, wear, training) are functions of time; no events inside it | Mining operations, scheduled freight services, colony production and consumption, station rotations. A year is one evaluation. |
| **Rails** | An analytic function of time from an anchor. Changes come as events that re-anchor | Kepler coasting arcs. A burn's start and end are events. Fuel and stores are linear over a leg. |
| **Coarse** (240x and up) | Fixed one-minute steps, kinematic and exact between steps | Burning ships and engagements at speed. Constant-thrust arcs need a cheap closed form or a short-arc approximation, checked against fine. |
| **Fine** (below 240x) | The fixed tick with every model | Engagements and enforcement knife fights in Hill-frame relative motion. |

Rules that carry over unchanged:

- **One world clock.** A reinforcement coasting on rails arrives at the battle at the right moment, and causality is never in doubt.
- **The speed picks the tier,** never attention or the zoom (decision 12). The asked speed is a logged command, so replays hold, and the same orders at different speeds may give different results; Fleetwright accepted that for the player's experience. **This replaces the initial notes' "fine tier for player-relevant fights, coarse for AI-vs-AI".** Fleetwright tried attention-picks-fidelity first and dropped it.
- **The sim never reads the display.** Fleetwright had a single exception (the map scale reaching the rails), removed it, and wrote "None may come back."
- **A model must say what step it needs.** A model that can't take a large step moves its entity into a finer tier while it's active (a flooding ship goes coarse). Here, a thrusting ship can't stay on Kepler rails, and a ship whose reactor is scrammed and venting heat can't sit on a routine.
- **Speed drops are the sim's, at the exact event time**, not the UI's a frame later. The player never overshoots a contact.
- **An interest table maps events to reactions** (nothing, a dispatch, a notification, a speed drop, a pause). It is user-configurable, with a per-group importance flag, and NPC events never slow the clock unless the player's rules say so.
- **Same at any compression** (smoke's "core rule"). Sources emit on a lattice of world times, caches fall due by world time, and a 1x run and a fast fine run give the same hash. Every model is dt-proof: Fleetwright checks that a 1 s and a 15 s step agree within the noise.
- **Quick transitions both ways.** Leaving a routine is one evaluation, and resuming it is one command. Dropping to 1x never causes a loading pause.

**The higher tiers only need to be close enough** (Teemu, Oct 30). This goes further than Fleetwright. Routine and rails don't have to match the finer tiers exactly. A procedure can collapse into a duration: a whole docking procedure is skipped and a similar wait is added to the cargo transfer. Likewise a refuelling is a stay at the station, and an inspection with no incident is a delay on the leg. What must hold:

- **The outcome is close:** times, quantities, costs and wear land near where the fine version would put them. Fitting these durations is the higher tiers' version of the parity bench, at looser bands.
- **Dropping in is seamless:** when the player drops to 1x or something becomes interesting, the entity is placed in a plausible state for that moment (mid-transfer, at the dock), with no jumps visible to the player.
- **Exactness stays where outcomes are decided:** Fine and Coarse in a fight, with the hit model the same in both, as in Fleetwright.

**Numbers worth noting:** 1,000,000x is a year in about 32 real seconds and a Hohmann transfer to Jupiter (about 2.7 years) in about 90 seconds. With collapsed procedures and nothing interacting, quiet periods can go faster still: the routine cap is a setting, not a design limit. Fleetwright's world time is a `long` of milliseconds since an epoch. **The epoch here is an ephemeris constant, not a start date**, which keeps "no fixed dates" intact. Heliocentric doubles give about millimetre precision at Neptune's distance, so Fleetwright's "Earth-centred doubles, flat only locally" becomes "heliocentric doubles, the Hill frame locally".

### Light entities: every merchant is a real track

Fleetwright tracks all ~9,000 British merchants of 1914 as **light entities** (a route, a nation, a tonnage, a cargo, and no condition tables). Only real positions let a raider deplete an area realistically and let a navy reroute traffic. An entity takes full state only when something engages it, and drops it afterwards. The light/full split is per entity, not per kind.

Here that is the traffic-control problem: every torch freighter must be a real track, because each one is a potential kinetic weapon and the envelope system must know where it is.

**One adaptation is new here.** In Fleetwright, relations gate the contact scan: at peace nobody is checked, and ships just pass. Here traffic control watches everyone in peacetime, so two scans are needed:

- **The hostile-contact scan,** gated by relations, as in Fleetwright.
- **The envelope check,** always on but analytic. When a leg or burn is anchored, solve once whether and when it enters any protected body's envelope above the allowed speed. That moment is an event, so nothing is checked per tick. This is "envelope violation" in the notes' decision list, built Fleetwright's way.

## 3. Knowledge: each side's picture

**Fog of war is knowledge of entities, not a visual effect** (Fleetwright decision 9). Each navy keeps a table of contacts: an entity or "unidentified", its classification as far as known (possibly wrong), its position and velocity with uncertainty, and the time and source of the report. Entries age. The player's snapshot is built from their own side's picture, and NPC admiralties plan from theirs, "so they're fooled by the same things the player is."

Here light-lag makes this physics, not a design choice:

- **Every report carries the time it was made and the time it arrived.** A contact at Jupiter is 35 to 52 light-minutes old before any processing. Fleetwright already stamps reports with time and source, and routes every read through one place so that delays can be added later. Here the delays are present from the start, for the AI polities and their commanders. The player's orders, and the relay of readings to the player's picture, are the exception (section 4).
- **Doubt has a shape** (`command-ui.md` principle 1). Each sensor leaves its own geometry:
  - A passive IR detection of a torch gives a good bearing and a poor range.
  - Two pickets give a cross-fix.
  - A coasting contact's uncertainty grows mostly along its track: orbital uncertainty stretches into a banana-shaped arc, not a circle. That is real physics and a readable UI shape.
- **Cold coasting is the night of this game.** Fleetwright's night plan ("interpolate on light"; "the background is the night's own") maps onto detection against the sky background: a cold hull against deep space, a lit drive against everything. "The threat is a cold coast plus a late burn" is the space version of a torpedo boat attack at night.
- **Misidentification is part of the picture.** A drive signature taken for a freighter's when it is a warship's is the space version of Fleetwright's battlecruiser taken for a battleship.
- **The independence leverage estimate is a picture-based estimate.** "Earth could place roughly N kt of warships in Ceres orbit within X months" is computed from the company's picture of Earth's yards and fleets, not from the truth. Misreading it is a legitimate way to lose, as the notes already say.
- **The UI shows the plot, not the truth.** That includes `command-ui.md`'s hurricane-cone warnings: soft edges, a best-estimate point, fans instead of cones, and an uncertainty area never drawn so it reads as a ship's size.

[`design/detection-and-the-picture.md`](detection-and-the-picture.md) works this out in physical numbers: what a sensor can detect, how range is bought, and what sensors cost.

## 4. Command, AI and the player's hand

### One command path

Fleetwright: "The player's navy and an NPC's are the same thing with a different command source." An NPC admiralty reads a frozen copy of its own picture on a job, writes commands that apply at the next step, and can't reach into the world. That is exactly "AI polities are the same structures"; Fleetwright shows how to make it deterministic and testable (an all-NPC world run headless).

### Intent down, reports up, doctrine around

From `command.md`:

- Each layer gets intent and gives orders, and never orders up or sideways.
- Each layer reports a small status code up (on task, engaged, falling out, can't), with a reason the UI shows as a tag ("subordinates explain themselves").
- **Rules with hysteresis, not search.** No planning by simulating ahead. Where there is a real choice, a pure scoring function picks, and it is tested on its own.
- **Nothing is idle without a reason.** Every task ends and hands the unit back up. That is what keeps a self-playing scenario from stalling.

**The bar:** "plays to an end in most seeds", not "plays well". A scenario that plays itself with the AI on every side is the first milestone; playing well is a later tuning pass.

**Here the chain is longer and slower:** polity → governor (a colony or station) → fleet → captain. Light-lag decides how much each layer gets to decide on its own. A governor at Saturn is mostly a doctrine-follower with a temper.

### Doctrine as presets defined by values

- Doctrine is a record of standing rules: engage, range, when outgunned, fall out, break off, fire, night, and so on.
- It is set per side, overridden per unit, and read down the tree.
- **A preset is a named set of values, as data, never code.** A navy's character lives in its presets.
- Here the same structure holds rules of engagement, envelope enforcement (warn, shadow, disable, kill), inspection posture (weapons tight or free, drive orientation) and what to do with smugglers.

### Tempers add

Aggression is set at three levels that add together: the side's, the admiral's and the captain's (`launch.md` decision 1). "A timid captain under a bold admiral fights harder than she would alone, and never as hard as a bold captain under the same flag."

- **Colony drift** ("colonies the player founded can drift") becomes the governor's temper, plus their constituency's pull, plus the polity's line.
- **Crew and captain loyalty as a strategic asset** (from the torchship section) is a captain's trait at the same level as temper.
- Fleetwright's crew principle applies: **the captain is the person.** Officers and crews are counts and a few numbers, with no individual personalities.

### The player's hand and the conn

From playtesting the Jutland scenario:

- **"When I hold the ship I hold the ship"** (decision 12). A unit under the player's direct order does what was ordered, and doctrine doesn't take it back.
- **The conn is absolute** (decision 13): an explicit switch under which nothing but the player moves the unit.
- **The AI commands the player's own side by default** (decision 14): "the game's scale is too big for anyone to steer every squadron." The player takes the units they want and hands them back.

All three fit a solar-system game even better than a naval one.

### The player's orders are instant (Teemu, Oct 30)

As in Fleetwright, **the player is the exception to light-lag.** The player's orders reach any unit at once, while AI polities, governors and admirals send theirs at c and carry on with their last orders until a new one arrives. The reason is play: the player may want to handle two skirmishes close in time but far apart in space without waiting out the lag in between.

- **Considered and parked: the placement of the player's own command nexus** as a meaningful choice, with orders leaving it at c. It stays open to arguments and playtesting.
- **Light-lag still shapes the player's game:**
  - Every AI polity's picture and orders are lagged, so the player's opponents and own subordinates under AI command act on old information.
  - The player's AI-run units act on doctrine between the player's interventions.
- **Decided (Teemu, Nov 1): the player sees the polity's fused picture, relayed instantly.** Each sensor reading reaches the player the moment the sensor takes it, wherever the sensor is. The reading is still as old as the light that made it: a picket 2 light-hours from a contact shows it as it was 2 hours earlier. So the player is an FTL observer of their own sensor network, and the only lag the player feels is from the target to the nearest sensor, which gives sensor placement a direct payoff. AI polities, governors and AI-run units fuse at c. The trade-off that was weighed:
  - **An unlagged player is an FTL observer.** They can react to events before light could carry the news anywhere, which can produce very interesting situations, to say the least: intercepting a declaration before it arrives, or answering a covert act nobody local has seen yet.
  - **Lag is annoying where the game needs micro.** Living under lag fits a game where you are one space-fleet admiral perfectly. It may not work in a game with several fleets and colonies needing kicking at once.
  - [`design/detection-and-the-picture.md`](detection-and-the-picture.md) has the details, including the single fusion implementation with two arrival rules.
- **Decided (Teemu, Oct 30): units under AI control follow the lag,** including the player's own. An AI-run unit acts only on what its own picture holds, and receives orders from its AI superiors at c. Only the player's direct hand is instant. So the player's faster-than-light view can't leak into the AI's decisions; it reaches the world only through units the player takes over. The visible oddity is accepted as the price: the player hops in, and the crew asks "Sir, why are we suddenly burning towards the Jovian system?" "No reason."

### No decision queue, no busywork

- **No decision queue** (decision 15): "a camera that jumps is extremely distracting." Notices go to the log, and the camera moves only when the player moves it.
- **The busywork test** (`map-ui/README.md`): "would a real admiral's staff have bothered him with it?" Here: would the board, or the governor's office, have bothered the director with it?
- **This replaces "Captains can request guidance"** in the initial notes. A request becomes a notice in the log, plus a speed drop if the interest table says so.

### One judgement every layer asks: the matchup

Fleetwright's `Matchup` estimates "who can fight whom": the share of the enemy's tonnage each side puts out of the fight for the share of its own. Every AI layer and the scout's reports read this one judgement. The key rule is **"the matchup mirrors the terminal"**: every change to the real damage model changes the matchup's estimate in the same commit, so "the AI's judgement never reads a different model from the one that fights."

**Here this is the deliverable-force side of the independence arc.**

- The host's "can I crush them?", the company's "can I survive the response?", the AI's choice between proxy enforcement, embargo and expedition, and the player's intelligence estimate should all be one implementation.
- That implementation is fed by each side's picture and kept consistent with the coarse resolver.
- It answers two open questions in the notes:
  - **How deliverable force is estimated:** a matchup over transfer-window reachability, written once.
  - **How AI hosts choose a response:** a scoring function over that matchup and the host's politics.

## 5. Politics: the incident record

Fleetwright's **"insane captain"** option is a small seed of this game's whole political layer:

- **Firing in peacetime is a command, not a contact.** Without the option the world refuses it; with the option, the player confirms it.
- **It's an incident, recorded in full:** who fired first, what each hit did, where it happened and who saw it. The record goes to the relations system, which turns it into a crisis that may or may not end in war.
- **The consequences read the same record:** the other nation's reaction, neutrals', and the player's own government ("a court-martial, the budget cut or raised by a war scare").
- **NPCs do it too, rarely:** a seeded rate of incidents (the Dogger Bank incident of 1904).
- **Relations sit behind an interface** ("may these two interact, and how") that tension, incidents and neutrals grow into without the encounter code changing.

**Decided (Teemu, Oct 30): the scaffolding for tension and incidents goes in from the start,** because gray-zone conflict is the core loop here. It is built piece by piece like everything else, though. The relations interface, incident records with their observers and the tension state exist as structure early, and the systems that read them come in their turn.

**Here the defiance ladder is this mechanism generalised.** Every rung action (unlicensed armament, a refused inspection, an unregistered drive, an expelled governor) is a command that produces an incident record:

- what was done, where and when;
- who could have observed it, and when each observer's report arrives, at the speed of light, from their pickets or agents.

Each host's politics then reads its own picture of the record, never the truth. Covert enrichment is a record that no observer has seen yet. The gray-zone drive-fault drama is an incident whose record is ambiguous ("a fault, or a probe?").

Fleetwright also records "who fired first" on every encounter. Enforcement knife fights need the same field, plus the lead-up (the targeting lock, the rotation toward the inspector), because posture *is* the incident.

### The world refuses, not the designer, and only physically

Fleetwright: the designer offers what the `TechSet` unlocks but **never refuses**. A design with locked tech builds and shows it in the remarks; the world refuses it when the player commissions it or lays it down. Limits (a treaty, a dock size) are reported in the designer, "amber over, green spare, never red".

This game needs that refusal split in two:

| Kind | Example | What the world does |
| --- | --- | --- |
| **Physical "can't"** | A drive block the polity hasn't researched; a hull larger than any yard it holds; components it can't make or buy | Refuses the command, like Fleetwright |
| **Legal "mustn't"** | A torch drive the charter forbids; armament over the licence; a design that breaks a traffic or treaty limit | **Allows it.** It's a rung-2 charter violation: an incident record, with how visible the work is (yard size, emissions, supply chain) deciding who learns of it and when |

The charter is never a `TechSet` filter. That is exactly "the player can break those rules at any time". Fleetwright's designer limits panel (presets such as "Washington 1922") becomes a "charter terms" preset: it shows which clauses a design breaks, and leaves the choice to the player.

Fleetwright's **"type is only a gameplay label"** (`DECISIONS.md`: battlecruisers and destroyers are just warships) fits the theme exactly. Physically a torch freighter is a warship. Its registered type is a political label that charters and inspectors read, and lying about it is a rung-2 act.

## 6. Ship design

- **Every mount and system is placed physically** (`DECISIONS.md` and the shipgen rules): sprites are drawn from hitboxes, and sensors are compiled from parts at their real heights. "Don't add geometry the drawing needs anywhere but the hitbox model." Here, radiators, drive, reactor, tanks, crew shielding and sensors are parts with geometry. They take hits, block arcs and set the thermal and radiation picture.
- **Combat endurance is the player's choice** (`DECISIONS.md`: "combat endurance vs weight tradeoff"). Here that covers propellant (Δv), magazine depth, radiator margin and stored coolant.
- **"The loadout is the admiral's, the armour the designer's"** (`shells-armour-damage.md` decision 6). Missiles, drones, sandcaster rounds and the propellant load for a mission are set per ship outside the design; hull, drive and radiators are not.
- **The trim sheet** (`designer-ui/overview.md`): 18 broad levers, each showing what one step down and one step up does to the total, measured by real builds in the background.
  - Steps that go the wrong way are shown in amber, not smoothed.
  - A Fit feature meets a set of limits by moving one lever or all of them evenly.
  - Here the totals are Δv, acceleration, mass and waste heat, and the limit presets are charter terms, yard size and envelope compliance.
- **Looks are visual only:** a polity's style changes the drawing, never the physics or the hitboxes.
- **The designer runs standalone:** a design goes in with a `DesignContext`, and a design comes back through a callback. Nothing of the designer lives in the world.

## 7. Combat and damage

### One hit contract

- **Damage takes a hit, not a shell flight** (`architecture.md`). The hit query and damage model accept a hit from any source: the fine tier's shells or the coarse resolver's samples.
- **"A hit is the same in both tiers"** (`coarse.md` decision 1). What coarse approximates is the rate of hits over time, which comes from motion and dodging, not the hits themselves.

Here the contract has to cover more kinds of deposition: kinetic impact, laser fluence over a dwell time, neutron and gamma flux, plume exposure and debris fluence. Proposal: **one deposition event**, carrying energy, area, duration, direction and spectrum (kinetic, thermal, radiation). The damage channels already in the notes (thermal load, ablation, spall, radiation dose, component activation) are what that event does. The same event applies in either tier.

### No hit points

- **Fleetwright:** "Sinking depends on the buoyancy model, not hit points. A ship sinking slowly should leave the enemy unsure whether it's going down."
- **Here a ship is lost through physical failures:**
  - loss of attitude control;
  - reactor scram with no power for the radiators;
  - **heat death**, when radiators are lost and stored coolant runs out;
  - crew dose;
  - a broken spine under thrust.
- **The uncertainty carries over:** a cold, coasting, silent hull could be dead or playing dead. That is gray-zone play for free.

### Rough where it doesn't decide, physical where it decides

From the fire and damage-control plans: water through a hole uses the orifice law because it decides who sinks, while the crew's side is "parties as units doing jobs measured in man-minutes" with no hoses or pipe network.

- **Physical here:** orbital mechanics, Δv, heat balance, the intercept window's geometry, deposition and the radiation dose.
- **Rough:** repair parties, the economy inside a hull and life support's details.

### No lumped battle factors

`crew.md`: "There's no factor on hits, rates or aim for being under fire." Morale acts only by moving people (to cover, or present but not working). Here, radiation dose works the same way: it acts by incapacitating crew at their stations, not as a factor on performance.

### Coarse approximates fine: the rung ladder

`coarse.md`'s principle, which answers the notes' open question on how the resolver is calibrated. Each piece sits on the highest rung that meets the speed target:

1. **The same code on the coarse clock.**
2. **The same code at a coarser cadence.**
3. **Fitted from fine by a bench**, stored with the fine chain's fingerprint. A kept test fails when fine changes and names the command to rerun.
4. **Never hand-set coarse numbers.** "A coarse result that's off is fixed by moving up a rung or refitting, never by tuning coarse against itself."

The parity process carries over too:

- `coarse-parity` runs a panel of duels, dodging, fights to the end and scenarios, played both ways over many seeds.
- **The bands:** ±15% on means, the winner's share within 10 points, and "a band never widens silently".
- **Dodging is where coarse is weakest,** and gets its own layer. Here that is the evasion of missiles and laser dwell by small, agile ships.

### The step mode

`coarse.md` J1, after Rule the Waves: run one coarse step (a minute), animate it smoothly, then pause; orders given while paused shape the next step. "Testing and playing are the same thing in the end." Here the natural step is the decision cadence the notes already define (range ÷ closing speed, about 100-300 s).

## 8. The yardstick problem

Fleetwright judges models against **history**: Jutland's hit rates, Seydlitz's flooding, the Dogger Bank. The rules attached:

- **History is the yardstick, not today's model.** A change is judged against the record, never by how close it stays to the previous version.
- **A record holds only where it was made:** a 1.4% hit rate at 16-18 kyd says nothing about 8 kyd.
- **Physics first, balance last,** and don't tune to history before the compensating systems exist ("more sinkings than history are fine" until damage control is in).

**This game has no torch-war history.** A layered yardstick is proposed:

1. **Physics reference calculations** for mechanisms: closed-form orbital mechanics, laser diffraction, heat balance, the debris-cloud growth already in the notes. These play the part Fleetwright's reference scripts (`*_ref.py`) play: checks on mechanisms, never targets for game numbers.
2. **Real data where it exists:** spaceflight performance, ballistic-missile intercept tests, high-energy laser tests, nuclear test effects, ISS debris-avoidance practice.
3. **Historical analogues for the politics, as shapes, not numbers:** the East India Company, the American Revolution, the Cod Wars. The check is whether the arc has the right shape (escalation, proxy enforcement, the recognition cascade), never whether a rate matches.
4. **The fine tier, for everything coarse,** as in Fleetwright.

The realism gradient (section 1) says which layer applies where: real data for demonstrated blocks, studies for studied ones, physics reference calculations alone for physics-only ones.

## 9. Engineering spine

**The stack is the same and the code is bespoke** (Teemu, Oct 30): C# on .NET with the SDL3 GPU API. The only code taken from Fleetwright is the initial C# + SDL3 GPU scaffolding from its first commits. Everything above that is written for this game. The rules below carry over as they are; the implementations don't:

- **Deterministic and headless.** The same start and the same commands give the same world. Each system draws from its own seeded RNG stream, and nothing reads the wall clock.
- **Commands in, snapshot out.** The UI never writes the world. The snapshot is triple-buffered and swapped by pointer. Rails and coarse entities are drawn by evaluating their tracks at render time, not by interpolation.
- **Every tuning number lives in `SimSettings`**, loaded from data.
- **Soft real time:** nothing allocates in a step, and no algorithm is worse than O(n log n). There is one spatial index for "what is near here" (heliocentric plus each body's sphere of influence, which needs its own design).
- **Workers are deterministic** (`workers.md`). Chunks have a fixed size, never derived from the worker count. Reductions run in chunk order. A test mode shuffles the chunks to catch order bugs.
- **Single implementation:** no second engine kept "for reference", and benches run the game's own code.
- **Looks never feed the sim** (smoke: "VFX is for fluff, and VFX never misleads"). A look may add detail the sim doesn't have, but never hides or invents what decides an outcome.
- **Zoom bands are not clock tiers.** This answers the notes' km-to-light-second UI question: the bands (system, body, orbit, engagement, ship) are display only, and the drawing changes at band edges.
- **The UI language** (`ui-language.md`): a workstation look of docked panes, outliners and ledgers, "never landing-page habits".
- **Saves** use indices at runtime and string ids in files. A save holds designs as data with content hashes, and ships are recompiled from them on load.

## 10. How Fleetwright was built, and what that suggests here

- **A deliverable module first.** Fleetwright's battle module is "the final game's whole ship simulation on this world, with missions standing in for politics and manufacturing". Nothing built for missions is thrown away when the campaign comes, because the campaign is "a bigger world with more systems switched on".
- **Built from the ground up, in baby steps:** an empty world, then one ship, then two, then shooting, with every step planned with the user before it's built. **The same order here** (Teemu, Oct 30): first a solar system, then ships in it, and onward piece by piece.
- **Released in cuts:** each release is a fully working cut that the next one widens, and "nothing in it may assume its era". That rule is what kept sensors, weapons and ranges open-ended.
- **Plan docs with one shape:** the aim, what exists (checked against the code), the principles, the yardstick, the user's decisions, then the steps.
- **Working habits:**
  - Benches before and after every change.
  - A refactor proves itself with identical hashes; a model change reports numbers against the yardstick.
  - Research goes into a requests file and doesn't block work.

**The first game is a scenario battler** (Teemu, Oct 30), as Fleetwright's battle module is. Ships in space that move, burn and fight are a massive undertaking on their own, and they are the foundation the living solar system is built on. As in Fleetwright, the scenario battler is also the place to test and fine-tune the ships themselves; the living solar system then uses that same simulation unchanged. It is the full-fidelity **ship and orbit simulation** (motion on rails and in burns, sensors and pictures, combat, damage), with scenarios standing in for charters, economy and research. The scenarios themselves can be about the politics: an inspection knife fight, a gray-zone envelope violation, a punitive expedition arriving after a declaration. Those exercise posture, the incident record and the picture before the strategic layer exists.

**Its slice is wide** (Teemu, Oct 30): from essentially contemporary chemical rockets in cislunar space, through nuclear pulse drives, to fusion. The base points come from a survey of the whole Atomic Rockets (Project Rho) archive, and the exact range is decided after that survey. Because eras are only tech blocks, a wide slice means more blocks and scenarios, not more systems. The weapons' period is open in the same way, and nuclear weapons in space are in.

## What changed in the initial notes

- **Vision:** a short "Design principles" section points here.
- **Propulsion:** the drive table is now described as families of tech blocks with smooth scaling, not a minimum-size switch.
- **Construction infrastructure:** the world refuses at lay-down. The designer reports and never refuses.
- **Combat and time:**
  - "Resolution tiers" now follows Fleetwright's speed-picks-the-tier rule.
  - "Captains can request guidance" became notices plus the interest table.
- **Data and sourcing:** "Tech-gated inputs" is now tech blocks plus a `TechSet`.
- **Defiance ladder:** a note on physical versus legal refusal.
- **Open questions:** proposals added for the resolver's calibration, deliverable force, the hard end condition and the yardstick.

## Decided (Teemu, Oct 30 to Nov 2)

1. **Tech blocks come from research and engineering in the campaign,** as two separate systems: research drives what is known, and engineering produces the drives. Blocks can be bought from others or designed at home. Fleetwright gets the same split, though this game has more actual research. Fleetwright's fixed catalogues are a placeholder for scenario play until it has a research system; here too a preset catalogue stands in only in scenarios (section 1).
2. **The player's orders are instant.** The player is the exception to light-lag, so that two skirmishes close in time can both be handled. A command nexus whose placement matters was considered and is open to arguments and playtesting (section 4).
3. **The higher tiers only need to be close enough.** Procedures can collapse into durations (docking skipped, a similar wait added to the cargo transfer), so quiet periods can run faster than Fleetwright's caps (section 2).
4. **Scaffolding for tension and incidents goes in from the start,** built piece by piece: a solar system first, then ships in it, and so on (sections 5 and 10).
5. **Same stack, bespoke code.** C# and the SDL3 GPU API; only the initial C# + SDL3 GPU scaffolding comes from Fleetwright's first commits (section 9).
6. **Units under AI control follow the lag,** the player's own included; only the player's direct hand is instant. The crew's puzzlement when the player acts on news they can't have is the accepted price (section 4).
7. **The first game is a scenario battler:** ships in space that move, burn and fight, with scenarios standing in for the strategic layer. It is the foundation and test bench for the living solar system, which uses the same simulation. Its slice runs from contemporary chemical rockets around the Moon through pulse drives to fusion, with the base points from an Atomic Rockets survey (section 10).
8. **The player sees the polity's fused picture, relayed instantly** (Nov 1). Each reading reaches the player when the sensor takes it, though it is as old as its light, so the player is an FTL observer of their own sensor network and sensor placement sets how old the player's picture is. AI polities and AI-run units fuse at c (section 4; [`design/detection-and-the-picture.md`](detection-and-the-picture.md)).
9. **Realism gradient; physics is the only final limit** (Nov 2). The closer a block is to today, the more it must match engineering data; the further out, the more only physics bounds it. Nothing is forbidden except what physics forbids. Deviations are allowed but always logged as exceptions, below (section 1).

## Still open

Nothing from this read. The player's picture, the last open item, was decided on Nov 1 (decision 8).

## Logged exceptions

Deviations from the principles above, each with what deviates, which rule it breaks, why, and what would remove it. An unlogged deviation is a bug.

| What deviates | Rule broken | Why | What would remove it |
| --- | --- | --- | --- |
| The player's instant orders and instant picture relay | Physics (light speed) | Play: handling several distant skirmishes at once (decisions 2 and 8) | A command nexus with orders at c, if playtesting ever favours it |
