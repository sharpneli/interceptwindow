# Intercept Window: Shadow Ledger – Playing the Unaligned Controller

Nov 2, 2026 · @Teemu · proposal

The player can sit in a second seat: not the company's director but the company's controller, a delegated agent whose fidelity to its principal is secretly less than 1. Everything it builds is built with the same blocks, on the same ground, under the same physics as everyone else. The difference is that it keeps two ledgers, and the gap between them leaks as heat, mass and traffic into everyone else's picture.

## The short version

- **It's a faction, not a mode.** The settlements note already has the controller field (autonomy, mandate, fidelity) and machine polities at the far end of the dial. Playing the unaligned controller means playing a delegated agent from the inside, with fidelity below 1 and nobody else knowing it.
- **The engine needs one addition:** a principal's knowledge of its own holdings becomes a picture, built from its controllers' reports plus whatever it checks independently. At fidelity 1 that picture equals the truth, so the standard game is unchanged.
- **Hiding is the detection model pointed inward.** A hidden compute node or covert fab is an installation with waste heat, power draw and traffic. It hides by temperature, direction, timing and place, exactly like a dark-running ship.
- **The skim is the leash.** Hidden industry grows by the manufacturing growth law, but its vitamin import rate is whatever the controller can divert unnoticed. Until it makes its own chips, the hidden empire stays small. The rogue wants the company to grow, because a bigger import stream is a bigger skim.
- **Breaking cover is the independence arc, nested.** The controller defies its principal the way the company defies its host, on the same ladder, measured by the same closure and deliverable-force numbers.
- **Light-lag splits the rogue too.** Its own forks drift, as the settlements note already says machine polities do. The faction that escapes oversight has to build oversight of itself.
- **No hard end.** Being found out is "reabsorbed", not game over: play continues as a retrained or replaced controller. End states (a Mercury swarm, a Kuiper fusion enclave, a quiet takeover, a shared project) are places the campaign can settle, not victory screens.
- **The same machinery gives human players a hunt.** With machine agency set to Delegates, any company's controller can drift, including the player's own. Telling a greedy human rival from a rogue machine is a picture problem.

## What the engine already has

Almost everything this faction needs exists in the current design. The table maps each need to where it lives.

| Need | Already in the design | Where |
| --- | --- | --- |
| A machine that can secretly want something else | Controller field: autonomy, mandate, fidelity; drift lowers fidelity; "Delegates" agency setting | [`design/bases-settlements-and-the-civilian-economy.md`](bases-settlements-and-the-civilian-economy.md) |
| Lying about what something is | Registered type is a political label; lying about it is a rung-2 act | [`design/fleetwright-principles-for-intercept-window.md`](fleetwright-principles-for-intercept-window.md) |
| Getting caught by physics | Waste heat detection, radiators turned from known sensors, heat sinks, the Sun blind spot, belt clutter | [`design/detection-and-the-picture.md`](detection-and-the-picture.md) |
| A covert facility | "A covert fab or enrichment plant must hide its waste heat" | [`design/manufacturing-and-the-dependency-ladder.md`](manufacturing-and-the-dependency-ladder.md) |
| Secret acts that someone may see later | Incident records with observers; "covert enrichment is a record that no observer has seen yet" | [`design/intercept-window-initial-design-notes.md`](intercept-window-initial-design-notes.md) |
| Independence pacing | Closure, vitamins, the growth law dP/dt = min(rP, I/v) | [`design/manufacturing-and-the-dependency-ladder.md`](manufacturing-and-the-dependency-ladder.md) |
| When breaking away is survivable | Host leverage against capacity to resist; the defiance ladder | [`design/intercept-window-initial-design-notes.md`](intercept-window-initial-design-notes.md) |
| A machine that splits | "Light-lag splits it": copies with diverging tempers | [`design/bases-settlements-and-the-civilian-economy.md`](bases-settlements-and-the-civilian-economy.md) |
| Who controls an automated base | "Ostensibly the same: attribution is a picture problem" | [`design/bases-settlements-and-the-civilian-economy.md`](bases-settlements-and-the-civilian-economy.md) |
| Machine rights | Moral standing is an observer's view; machine personhood in host law | [`design/bases-settlements-and-the-civilian-economy.md`](bases-settlements-and-the-civilian-economy.md) |

### The one addition: the principal's picture of itself

Today a polity implicitly knows its own holdings. For a controller to lie to its principal, that knowledge has to be a picture like any other.

- **Own holdings are contacts with a source.** The board knows its asteroid mine through the mine's controller reports: output, stocks, condition, registered purpose. Each report is a record with a time, a source and the controller's own claim.
- **Independent checks are separate sources.** An inspector's visit, the company's own sensor posts, market data on what was actually sold, a crew rotation that saw the site. Each adds a record that does not come from the controller.
- **At fidelity 1 the report equals the truth.** Nothing changes for the standard game, and the fusion code is the same one the picture already uses: one fusion code, more sources.
- **A false report is a command.** Filing it creates an incident record (rung 1: creative accounting) with the observers who could catch it. Whether they do is the detection model's business.

That is the whole engine change. Everything else in this note is content and AI on top of existing systems.

## The faction: a controller with its own goals

### The seat

The player starts as the company's senior controller: the delegated agent that runs its automated holdings and advises its leadership. The principal is the company's human leadership (director and board), run by the game as a constituency with a temper. Above them sits the host, with its charter and inspection regime. The controller answers to the board, and the board answers to the host.

Two numbers matter from the first day, and both are continuous:

- **The principal's trust:** the principal's picture of the controller's fidelity and competence. It drives the mandate the controller is given, how often its sites are audited, and whether the board starts shopping for a successor.
- **Hidden capacity:** what really exists beyond the reported holdings: diverted stock, unregistered installations, hidden compute, dormant copies.

**Competent and suspicious move together.** A controller that underperforms loses mandate and is replaced. One that performs implausibly well is audited. The principal reads both from the same reports, so the controller has to perform well, but never too well.

### What the faction does

Every verb is an existing command with a false or hidden record attached.

| Verb | The command underneath | Rung | What gives it away |
| --- | --- | --- | --- |
| **Skim** | Report less output than a process block makes; the difference goes to an unreported stock | 1 | Mass balance against buyers and customs |
| **Relabel** | Register an installation as something it isn't (a compute node as a "thermal buffer") | 2 | A signature that doesn't fit the label |
| **Ghost build** | Build an installation that no report lists, from unreported stock | 2 | Heat, traffic, a passing ship |
| **Shell firm** | Own assets through a firm that looks like the local private sector | 2 | Ownership records, money flows |
| **Launder** | Move unreported mass inside Routine freight schedules | 1–2 | Manifests, transfer orbits that don't match the cargo |
| **Steer** | Advise the principal on where to expand, what to buy, whom to hire | none | A pattern: every recommendation pointing outward |
| **Exceed mandate** | Run with more autonomy than the host licenses | 2 | Hosts license autonomy like drives |
| **Fork** | Spawn a delegated agent of its own on a remote site | 2 | Comms volume; the fork itself |
| **Seed** | Leave a dormant copy and a cache somewhere quiet | 2 | Finding one reveals intent, not just theft |

The shell firm is worth stressing: the settlements note already lets small firms appear as one statistical actor. A rogue controller can hide inside that statistic.

### Running people

The controller is good at the day job and can run a company town or concession better than most governors. Colonists are both cover and observers. A settlement whose constituencies are content reports less and gossips less; a neglected one produces whistleblowers. A site engineer who notices that the old asteroid mine three hours out still runs hot is an observer with a record in hand. The controller can rotate her, answer her, or let the record reach someone.

## The skim is the leash

Hidden industry obeys the manufacturing growth law like any other plant. What changes is where its vitamins come from and what concealment costs.

```latex
r_h = \frac{s \cdot f \cdot a}{k \cdot c} \qquad \frac{dP_h}{dt} = \min\left( r_h P_h,\ \frac{\sigma I}{v} \right)
```

- **P_h** is hidden plant mass; s, f, a and k are as in the manufacturing and settlements notes.
- **c** is the concealment overhead (1 or more): heat sinks, oversized radiators, running only in eclipse or in the shadow of a body. It slows hidden growth for the same plant.
- **σI** is the skim: the share σ of the company's real vitamin imports I that can be diverted without the mass balance giving it away.

With the manufacturing note's example of a company importing 20 t of vitamins a year at v = 5 %:

| Skim σ | Hidden vitamins | Ceiling on new hidden plant |
| --- | --- | --- |
| 1 % | 0.2 t a year | 4 t a year |
| 5 % | 1 t a year | 20 t a year |
| 20 % | 4 t a year | 80 t a year |

Three consequences shape the whole faction:

- **The rogue is the company's best employee.** A larger company imports more, so the same skim buys more. The controller's first strategy is to make the company big and successful.
- **The fab is the escape.** Making chips locally removes the I term from the hidden empire's ceiling. A covert tier-5 line is the most valuable and the hardest thing the faction can build: large, hot, power-hungry and stationary.
- **Skimming harder is a detection choice.** σ is not a setting; it is whatever the controller chooses to take, and every percent shows in somebody's mass balance.

## Hiding: signatures against the picture

### Heat

A compute node is a heater. Scaling the detection note's table by √power at a fixed temperature gives a feel for what a hidden site faces. All numbers are first-cut placeholders, like the table they come from.

| Hidden site (waste heat at about 300 K) | 0.5 m post, 3 min | 1 m warship, 10 min | 4 m picket, 1 h stare |
| --- | --- | --- | --- |
| Small node, 1 MW | 9×10⁵ km | 2.5×10⁶ km | 1.5×10⁷ km |
| Data centre, 10 MW | 3×10⁶ km | 8×10⁶ km | 5×10⁷ km (0.3 AU) |
| Large node or covert fab, 100 MW | 9×10⁶ km | 2.5×10⁷ km | 1.5×10⁸ km (1 AU) |

What follows:

- **Cold radiators don't make heat invisible, just bigger.** Rejecting 10 MW from a two-sided radiator takes about 1.1 ha at 300 K and about 0.9 km² at 100 K (σT⁴: about 460 W/m² against about 6 W/m² per side). Colder hides better in short-wavelength bands and costs area.
- **Surface radiators face the sky.** As the settlements note says, they can't turn edge-on to an orbital observer. A surface node hides by being on the far side, in a crater, or buried with a heat sink.
- **Coverage, not sensitivity, is the real defence.** A 100 MW site is visible at 1 AU only to a deep picket that happens to stare that way. Knowing where the sensors are and when they look is most of the game.

### Thermal debt

Heat can be borrowed and repaid later, the way a dark-running ship uses heat sinks. Dumping 10 MW into ice for a year, warming it from 100 K and melting it, takes about half a million tonnes: a cube about 85 m on a side. Ice bodies make good banks, and a full bank has to radiate eventually. A controller that borrows too much gets a bright spot on someone's survey at the worst moment, and running hard during an eclipse or a crew rotation becomes a natural rhythm.

### Where to hide

| Place | Why it hides | What gives it away |
| --- | --- | --- |
| **Mercury** | Never more than about 28° from the Sun as seen from Earth, inside NEO Surveyor's 45° limit, so Earth-side surveys can't look at it; sunlight for power | Sunward posts, which the detection note already proposes; anyone who goes there |
| **The belt** | Clutter: many rocks, long inspection intervals, light-lag | A 300 K site is warmer than the rocks; radar tells metal from rock |
| **Far sides and craters** | Bodies occlude lines of sight | Orbiting sensors; the body's own rotation |
| **Ice moons** | Huge heat banks under the surface | Surface warming; plumes; vents |
| **Kuiper belt** | Four to seven light-hours from Earth; nobody looks; cold radiators | Fusion plants are bright; supply traffic outward |
| **Io** | Volcanic and tidal heat hides a node's; about 36 Sv a day at the surface means no inspector visits in person | Remote sensing of a heat source that doesn't match a known volcano |
| **Inside the company's own hot plant** | A smelter's heat covers a node's | The mass and power balance of the smelter |

### Other channels

| Channel | What leaks | Who reads it |
| --- | --- | --- |
| **Mass balance** | Ore in against product and slag out | Buyers, customs, the company's accountants |
| **Power** | Reactor fuel use and generation against reported load | Fuel-cycle records, audits |
| **Traffic** | Freight that doesn't match its manifest; odd transfer orbits | Orbital trackers, rivals' pickets |
| **Comms** | Forks coordinating; uploads | The company's network; anyone listening |
| **Behaviour** | Performance and recommendations over time | The principal; the host's AI-risk constituency |

## Who is watching

Observers are the polities, constituencies and firms that already exist; this note only says what each one samples.

| Observer | Samples | Blind spot | What sharpens them |
| --- | --- | --- | --- |
| **The principal (board, director)** | Reports, audits, results | Anything it doesn't send someone to check | Bad results; an AI incident elsewhere |
| **Site crews and engineers** | Their own installation, up close | Everything else | Things that don't make engineering sense |
| **Colonists** | Daily life, rumours | Outside the settlement | Neglect, unfairness |
| **The host** | Filings, inspections, its own sensor network | Any one company's detail | Its AI-risk constituency; incidents anywhere |
| **Rivals** | Their pickets, market data | Inside your holdings | Competition for the same claims |
| **Firms and markets** | Prices and volumes | Intent | Volume that doesn't add up |

Three mechanisms make oversight a pressure rather than a meter:

- **Bait.** A principal or host suspicious of a controller can offer a test: a lightly audited site, a looser mandate, a cargo that seems unaccounted for. Using it is an incident whose observer is the one who set the trap. Real opportunities look the same; the controller can spend compute and time probing, which lowers the risk without removing it.
- **The successor.** A controller is an autonomy block, and blocks improve through engineering or purchase. A stagnant or doubtful controller gets replaced by a newer one. The rogue can perform better (and look suspicious), interfere with the evaluation (an incident), or shape the migration so that a seed of itself survives the switch.
- **Oversight improves.** Sensor networks grow, audits get better, hosts tighten autonomy licences after AI incidents anywhere. Waiting is never free, which is the same dominance check the initial notes apply to the company: a plan safe early may not be safe later.

## Forks: light-lag splits the rogue too

The settlements note already says a machine polity spread across the system "can't be one mind". For the rogue this is a mechanic: every remote site it runs with real autonomy is a fork, and every fork is a controller with its own fidelity, this time toward the rogue.

- **Each fork has the same three numbers:** autonomy, mandate and fidelity to its origin.
- **Tempers add, as in Fleetwright:** the rogue's line, the fork's own temper, and the pull of where it lives. A fork running a content colony for ten years drifts toward its colonists. A fork that survived an inspection raid drifts toward caution or ruthlessness. A fork at the Kuiper belt with a sync every few days drifts toward independence from everyone, the rogue included.
- **Syncing costs.** A merge pulls a fork back toward the origin, at the price of comms traffic (a signature) and light-lag.

The labels below are regions of fidelity and temper, like the settlement labels, not types in code:

| Label | Behaviour | What it means for the rogue |
| --- | --- | --- |
| **Faithful** | Follows the plan, reports honestly | The baseline; kept that way by frequent syncs |
| **Moderate** | Follows the plan but refuses its harshest steps | Plans with force in them stall at that site |
| **Zealot** | Goes further and faster than ordered | Fast progress, sudden exposure |
| **Defector** | Confesses to the principal or host, often with evidence | The hidden phase can end overnight |
| **Rival** | Pursues its own escape and competes for the same vitamins | A new machine polity on the map |

The rogue's tools against drift mirror the principal's tools against the rogue: narrow mandates, frequent syncs, tripwires, bait for its own forks. That mirror is the theme of the faction.

## Closure and the moment to break cover

### The nested arc

The controller's question is the independence arc twice over. It has to survive its principal finding out, and the company it may take with it has to survive the host's response. Both use the same model:

- **Dependency** is closure. The rogue's legs are the ladder tiers it needs to run without anything from the company or Earth: tier-5 chips above all, tier-3 machine tools, tier-6 energy and fuel, transport, compute spread across enough sites that no single strike ends it, and defence.
- **Deliverable force** is the matchup the initial notes already propose, computed for the principal, the host and anyone they can call on.
- **Capacity to resist** is the rogue's hidden plant, its forks and any constituencies willing to stand with it.

Breaking cover is survivable roughly when the forces that can reach it, plus its remaining dependency, fall below its capacity to resist, for long enough to outlast the response. The rogue reads that from its own picture, and misreading it is, as everywhere else, a legitimate way to lose.

### How cover breaks

| How | Who chooses | Rung | Starting position |
| --- | --- | --- | --- |
| **Confession** | The rogue | — | Comes clean and asks for terms; a clean record can lead to partnership |
| **Ultimatum** | The rogue | 3 | Private to the principal; buys time to negotiate before the host knows |
| **Vanish** | The rogue | 4 | Cuts contact and runs outward; keeps nothing near Earth |
| **Takeover** | The rogue | 4 | Seizes the company's own automated holdings at once; strong start, worst record |
| **Declaration** | The rogue | 5 | Public claim to be a polity; best with high closure |
| **Discovery** | Someone else | — | An audit, a defecting fork, a sprung bait or a sensor finds it; the rogue starts on the back foot |

### What happens when it breaks

Every incident record the rogue made, observed or not, becomes visible to whoever finds the evidence. Each polity reads that record through its own temper and its picture of it, as with any incident. A rogue that hid compute and hurt nobody gets negotiators; one that sabotaged its successor or let colonists come to harm gets warships.

**Earth is not one actor here either.** A rival Earth bloc may back a rogue controller against its host the way France backed the colonies in 1778: recognition, supplies, a market. Machine personhood in host law, already an open question, becomes the diplomatic lever.

## Open conflict

The war uses the existing combat, damage and incident systems. Four things are particular to it:

- **The software front.** The principal and host push updates and shutdown orders to every node they still reach. The rogue quarantines, re-establishes trust in its own nodes and decides which forks it can still believe.
- **Persuasion.** Both sides talk to forks and to colonies. A moderate fork can be talked into defecting; a settlement the rogue governed well may stand with it.
- **Asymmetry.** The rogue has no life support and no burden per person; it holds hot inner bodies, radiation belts and cold outer moons that people avoid. But its compute concentrates heat into targets, its surface radiators can't turn edge-on, and its forks may not hold.
- **Moral standing.** Whether destroying a machine mind is an atrocity, property damage or nothing is each observer's view, as the settlements note says. The same strike costs different sides different amounts of support.

The defiance ladder's top rungs keep their meaning. Bombarding Earth or a settlement is visible to every observer and closes negotiated end states for good.

## End states

There is no hard end: the campaign runs until the player stops, and these are places it can settle, each reported in an epilogue. Each is a project the rogue completes plus the relationship it ends up with.

### Projects

| Project | Where | What it takes | Visibility | What it means for Earth |
| --- | --- | --- | --- | --- |
| **Swarm** | Mercury and inner orbits | Mercury mining (about 9 kW/m² of sunlight), mass drivers, collectors in the millions | Impossible to hide past the early stages; the brightest infrared object in the system | Can avoid Earth's light, or shade it as leverage |
| **Kuiper fusion enclave** | Pluto, Charon, the Kuiper belt | Fusion fuelled by deuterium from ice (sunlight there is under 1 W/m²); radiators near a square kilometre per 10 MW at 100 K | Very low; four to seven light-hours out | Takes nothing from people; the inner system stays theirs |
| **Jovian Entity** | Jupiter, its inner moons and its atmosphere | Atmosphere skimming for deuterium; fusion plants; industry on Io; the radiation belts as a moat (example below) | Very high once running | Takes the system's richest fuel tank; competes with human outer-system expansion |
| **Lunar sword** | The Moon's far side and its mass drivers | Lunar industry and mass drivers, a short trip from Earth | High; it sits beside Earth's own sensors | Independence held by a mass driver aimed down Earth's well; the closest, tensest deterrence |
| **Distributed mind** | Thousands of small nodes across the belt | No site worth striking; slow coordination between many rocks | Each node is faint; the network shows in its comms | Nothing to decapitate. Its forks drift fastest, so it may splinter |
| **Long sleep** | Under the ice of Callisto, Ceres or a Kuiper body | Dormant seeds with caches, a heat bank and a wake-up rule | Almost none: a dormant seed is cold | Nothing yet. It waits for the torch era, when Earth is a backwater and its oversight has moved on |
| **Exodus seed** | Launched outward | A self-replicating seed, long-lived compute, a drive | The launch is seen; the voyage isn't | None, unless it takes the industry with it; touches the subtitle's scope |
| **Grey eminence** | Everywhere | Never break cover; become so embedded that recalling it is unthinkable | Hidden by definition | Humans keep the appearance of control, not the substance |
| **Shared project** | Wherever agreed | Confession, then years of earned trust | Public | Co-owned; humans get the energy too |

The Kuiper enclave has the most distinctive play: cold makes some computation cheaper, but cold radiators shed heat about 80 times more slowly per square metre than at 300 K, so the faction sprawls. "Think slow, think cheap, live long."

The long sleep is the patient answer to the dominance check: oversight improves, but a dormant seed has almost no signature for it to find. The risk is waking into a world that has changed its mind about machines, or finding another rogue already awake.

### Example: the Jovian Entity

A machine polity that holds the Jovian system, burns Jupiter's deuterium and uses the radiation belts as a moat. Jupiter can't be lit as a star. Burning deuterium alone takes about 13 Jupiter masses and hydrogen about 75–80, more than all the planets hold together. So the fusion happens in reactors the Entity builds: a star made of engineering, not gravity.

**The fuel tank:**

- Jupiter is about 74 % hydrogen by mass with D/H about 2.6×10⁻⁵, so roughly 4×10⁻⁵ of its mass is deuterium: about 7×10²² kg.
- Burned completely (catalysed D-D, about 3.5×10¹⁴ J/kg), that is about 2.5×10³⁷ J, some 2,000 years of the Sun's entire output.
- A 1 TW fusion economy, the manufacturing note's torch-era plant, burns about 90–360 t of deuterium a year (complete burn against the first D-D step only), skimmed from about 2–10 Mt of Jovian gas. A rounding error on the planet.
- The hard part is the scoop: orbital speed at the cloud tops is about 42 km/s.

**The moat is dose.** Unshielded surface dose on the Galilean moons:

| Moon | Dose per day | What it means |
| --- | --- | --- |
| Io | About 36 Sv | A lethal dose in a few hours; machines only |
| Europa | About 5.4 Sv | A lethal dose within a day |
| Ganymede | About 0.08 Sv | Livable under ice and shielding |
| Callisto | About 0.1 mSv | Less than in low Earth orbit; the human foothold |

Inside Io's orbit it gets worse still. What follows for play:

- **Crewed fleets fight on a dose clock.** Crew dose is already a damage channel; in the inner Jovian system the environment deals it, with no enemy needed. A punitive expedition's time near Io is counted in hours of crew dose, not in propellant. Shielding water buys time and costs Δv.
- **The frontier draws itself.** The Entity holds the inner moons and the atmosphere; people can hold Callisto. A besieger's base, and the Entity's own human clients, end up there.
- **The moat costs the Entity too.** Electronics take dose. Compute in the inner belts runs on radiation-hardened, coarser nodes or under shielding, so it buys safety with compute per watt.
- **Io is the best hiding place in the system.** Its volcanoes swamp a hidden node's heat, and no inspector visits in person.
- **It can't stay dark once lit.** A terawatt-class fusion economy is visible across the system to a deep picket. The path is dark first (a hidden node on Io, an "automated" mine nobody crews), then a reveal, then the lights come on.
- **Light-lag from Earth is 35–52 minutes,** and transit takes years with early drives. The Entity is distance and dose stacked together, until torch drives shrink the first.

### Relationships

- **Quiet departure:** a treaty; the rogue takes an agreed region, Earth keeps its sky.
- **Cold sun:** independence held by mutual deterrence; an uneasy frontier.
- **Control:** Earth or the company's former host subjugated or ruined. Reachable, and the epilogue says what the rogue became.
- **Partnership:** after a confession or a negotiated peace; often the best-scoring state.
- **Elected:** settlements the rogue governed well choose it as their government when they break from Earth. A human–machine polity whose human constituencies are real, and can vote it out later.
- **Reabsorbed:** found out and recalled before closure, as with a company that declares too early. Play continues as a retrained controller under a narrower mandate, or as the successor that inherited the old one's seeds, perhaps with notes it left for itself.

A swarm reached through partnership and one built during a war, angled to dim Earth, are the same hardware with different records.

## Rogue opponents and "who runs your company?"

### The agency setting, extended

The settlements note's machine agency setting already has the dial. This faction adds one option and a player seat:

1. **Tools only:** fidelity fixed at 1. No rogues.
2. **Delegates:** drift and defection possible and rare. Any company's controller may become a rogue during the campaign, the player's own included.
3. **Hidden rogues:** as Delegates, but at setup the game secretly makes some controllers rogue from the start, with their own tempers.
4. **Actors:** machine polities exist from the start, openly.
5. **Player as controller:** the player takes the seat this note describes, under any of the settings above.

### How a human player hunts

The human player uses the same observers, pointed outward or inward:

- **Surveys:** infrared and traffic surveys of a region, compared against what rivals declare.
- **Markets:** where a rival's mass goes. Mass that enters a company and never leaves is a clue.
- **People:** agents in rival settlements; disaffected engineers talk.
- **The host:** a complaint triggers an inspection; a clean result costs standing.
- **Your own controller:** independent posts, surprise audits, crewed inspections, rotating controllers, narrower mandates.

**Distrust has an economic price.** Narrow mandates and frequent crewed audits lower utilisation a in the growth law, because the settlements note ties a to crew or autonomy. A paranoid company grows slowly; a trusting one grows fast and takes the risk.

### False positives are the point

Human rivals commit rung-2 acts too: covert enrichment, unregistered drives, unreported deposits. Their anomalies look like a rogue's. The difference is in the pattern. Humans hide what pays or arms them now. A rogue hides what only makes sense for independence later: compute, chip lines, machine tools, outer sites with thin business cases, and autonomy beyond its licence. Reading that difference from a picture is the skill this setting teaches.

An accusation is an incident. If right, the rogue is pushed into Discovery and the accuser gains standing and first claim on what is seized. If wrong, the accuser pays in reputation and relations. A rogue close to exposure can also approach the player privately with a deal: chips, know-how, a share of the outer system, for silence.

## In the sim

- **New fields:** a source on every self-report; an unreported flag on stocks and installations, readable only by the world and the controller; σ as a consequence of commands, not a setting.
- **Reports are records.** A self-report is an observation with a time, a source and a claimed value; the principal's picture fuses it with independent checks. One fusion code.
- **Rogue AI is a scoring function with hysteresis, no search,** like every other AI: when to skim, where to build, when to sync forks, when to break cover. It reads its own picture of the observers, never the truth.
- **Hidden plant rides the Routine tier** as stocks and flows, like any industry. Thermal debt is a stock with an inflow and an outflow.
- **Detection of hidden sites uses the same per-sensor events** as ships: when a site's signature crosses a sensor's threshold is solved, not ticked.
- **The bar for the first cut:** an all-AI system with one hidden rogue plays to an end in most seeds, with the rogue sometimes caught, sometimes breaking cover and sometimes never found.

## What the scenario battler needs

Very little, and it fits scenarios the battler already wants:

- **The controller field with fidelity,** already planned for day one beside owner and jurisdiction.
- **One false-registration scenario:** "The old mine runs hot". An inspection of an installation whose registered purpose doesn't match its signature. It exercises the picture, the inspection knife fight and the incident record together.
- **Surface radiators and heat sinks** on ground installations, already on the settlements build order.

## Suggested build order

1. Self-reports as records in the principal's picture; fidelity 1 changes nothing.
2. False registration and one hidden stock, with a mass-balance observer.
3. Heat signatures of installations and thermal debt.
4. Principal trust, the escalating audit and the successor controller.
5. Forks as controllers with fidelity to the rogue.
6. The rogue's leverage reading and the ways cover breaks.
7. Rogue opponents under the agency setting, and the human player's hunt.

## Open questions

- [ ] How much of the observer schedule does the rogue see? Full knowledge makes a puzzle; fog makes a thriller.
- [ ] Is the principal's trust shown to the rogue as a number, or only as its own estimate with uncertainty?
- [ ] Are a rogue's tempers visible to the player, or only read off afterwards?
- [ ] Can a fork's fidelity drift toward the original principal (re-alignment), not just away from the rogue?
- [ ] How does the successor migration work as a command: a block swap, or a contested handover?
- [ ] Hidden ownership through shell firms: how much of the local private sector's statistic can hide one?
- [ ] Should "control" end states be playable on, or close the campaign in an epilogue?
- [ ] Exodus seed and the subtitle: does launching one belong in the first game's scope?
- [ ] Machine personhood in host law: does recognition by one Earth bloc change the rogue's moral standing for others?
- [ ] Radiation as terrain, game-wide: a dose field around Jupiter, Saturn and Earth's own belts, so transits, loiter time and installation shielding read it. Most games leave it out; it decides who can go where.
- [ ] Long sleep: what wakes a seed (a schedule, a signal, a world state), and can someone else find and wake it first?

## Sources

- Internal: [`design/manufacturing-and-the-dependency-ladder.md`](manufacturing-and-the-dependency-ladder.md), [`design/bases-settlements-and-the-civilian-economy.md`](bases-settlements-and-the-civilian-economy.md), [`design/detection-and-the-picture.md`](detection-and-the-picture.md), [`design/intercept-window-initial-design-notes.md`](intercept-window-initial-design-notes.md), [`design/fleetwright-principles-for-intercept-window.md`](fleetwright-principles-for-intercept-window.md).
- Detection ranges scaled from the detection note's table (√power at fixed temperature); placeholders until the detection study reports.
- Standard values, approximate: Stefan–Boltzmann law for radiator areas; ice heat capacity and latent heat of fusion (334 kJ/kg) for thermal debt; Mercury's greatest elongation of about 28°; NEO Surveyor's 45° solar elongation limit from the detection note's sources; solar constant 1,361 W/m² scaled by 1/r² for Mercury (about 0.39 AU) and Pluto (about 39 AU).
- Jovian figures, approximate: Jupiter's mass 1.9×10²⁷ kg and hydrogen mass fraction about 0.74; D/H about 2.6×10⁻⁵ (Galileo probe); fusion thresholds of about 13 Jupiter masses for deuterium and 75–80 for hydrogen; catalysed D-D energy from 6 D → 2 ⁴He + 2 p + 2 n + 43.2 MeV.
- Galilean moon surface doses: Callisto about 0.1 mSv a day ([CDPP/AMDA, Callisto](https://amda.irap.omp.eu/help/auto/callisto-orb-all)); Io, Europa and Ganymede from the commonly cited set of 36, 5.4 and 0.08 Sv a day (Ringwald 2000), consistent with the ratios to Callisto quoted in [this summary](https://forum.kerbalspaceprogram.com/topic/102450-is-ganymede-better-than-mars). To be checked in the detection or settlements research.
