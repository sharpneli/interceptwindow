# Intercept Window: Bases, Settlements and the Civilian Economy

Nov 2, 2026 · @Teemu · proposal

## The short version

A base is never a different kind of thing from a city. It is a cluster of installations on a body, and a civilization is the same cluster grown large, owned mostly by others and run by policy. The player's hand shrinks because the player's share of what is built shrinks, not because a tier flips.

- **Places, not slots.** A body's surface is a field of terrain, ice, ore, sunlight and radiation. Anything can be built anywhere; poor ground and crowding cost more, never forbid. No outpost / settlement / colony tiers.
- **Installations are designed like ships.** Habitats, reactors, radiator fields, mines, fabs, yards and batteries are tech blocks with geometry, mass and heat. They are light entities until something engages them, and they take hits through the same source-neutral damage model as ships.
- **Ownership is separate from jurisdiction.** Every installation has an owner (the company, a host, a rival, private firms, households, a colony government) and sits under someone's law.
- **A private sector invests on its own,** on the same command path as the player. The player's levers move from placing modules, to building public infrastructure, to setting policy, as the player's share of capital falls.
- **Living somewhere has a cost per person.** Aurora's colony cost, made continuous and local: the capital and energy it takes to keep one person alive and well at this spot. Paraterraforming and terraforming lower it region by region.
- **Mars becomes Earth-like from the inside out.** Roofed and aerogel-covered regions first, an open atmosphere last. A breathable open Mars is an exaton-scale, multi-century project, so it is the long dream, not a milestone.
- **Attacks work at every scale** because everything is physical: strikes on installations, blockades that drain imported spares, seizures that change jurisdiction. Against a big colony, bombardment is an atrocity on the incident record; orbit, imports and hostages are the real levers.
- **People or machines is the central colonisation choice.** Automation keeps control and grows fastest, but runs on imported chips and protects nothing; settlers bring markets, defenders and in time independence. A machine polity is the far end of the same controller dial, and from outside its bases look just like a company's automated ones.

## What other games do

Most games make settlement size a discrete state that unlocks slots; the ones that feel alive add a private sector that builds without being told. Victoria 3, Distant Worlds 2 and Aurora 4X do the latter best.

| Game | How settlements work | Take | Avoid |
| --- | --- | --- | --- |
| [Terra Invicta](https://hoodedhorse.com/wiki/Terra_Invicta/Habs) | Hab sites found by probe, each with fixed yields. A core module tiers outpost → settlement → colony; each tier unlocks more module slots ([20 at colony](https://wiki.hoodedhorse.com/Terra_Invicta/Project_ColonyCore)). Mining modules multiply the site's yield. | Bases as physical, attackable stations | Slots and core tiers are hard cutoffs; yields are fixed numbers, not cost curves; no civil economy |
| [Solar Nations 2](https://steamcommunity.com/sharedfiles/filedetails/?id=3726735090) (early access) | Bodies split into regions colonised over time with manpower; buildings per region. Mars and Venus terraform through a [mission chain](https://steamcommunity.com/app/2275440/discussions/0/586182021532002423/) once enough terraforming buildings stand. Colonial cultures [splinter and can rebel](https://grindnstrat.com/?p=6163). | Territory as area; colonial culture drifting toward independence | Terraforming as a building count; painted regions rather than places |
| [Solar Expanse](https://store.steampowered.com/app/2517120/Solar_Expanse_Demo/) | A company runs contracts; bases, fuel stations, launch sites and colonies are built and simply exist. | Company-run tone, everything in motion | Nothing to attack |
| [Aurora 4X](https://erikevenson.github.io/aurora-manual/5-colonies/5.1-establishing-colonies.html) | Colony cost sets infrastructure per colonist (100 units per million at cost 1.0). [Civilian shipping lines and mining complexes](https://erikevenson.github.io/aurora-manual/6-economy-and-industry/6.5-civilian-economy.html) form and act on their own, taxed, subsidised or contracted. Civilians reroute around hostile fleets, and since [v2.6](https://aurora4x.com/t/aurora-v2-6-0-patch-notes-september-6th-2025/23/3) won't deliver colonists to unprotected colonies. | One number for how hard a place is to live in; an autonomous civil sector; blockades that emerge from risk | Population thresholds unlock trade goods; civilian mines spawn by random roll |
| [Distant Worlds 2](https://www51.slitherine.com/news/distant-worlds-2-dev-diary-6) | A state economy (spaceports, taxes, facilities) and a private economy (mining stations, freighters, passenger ships). The state licenses mining stations; the private sector pays their upkeep and hauls the output. | The split: the state builds public goods and taxes, the private sector does the rest | The player still picks every mining site; a broke private sector can't rebuild |
| [Victoria 3](https://paradoxinteractive.com/games/victoria-3/news/dev-diary-71-autonomous-investment-in-1-2) | Pops pay dividends into an investment pool. With autonomous investment, a private queue builds what is profitable beside the government's queue, and economic law sets the split of construction. Buildings have [owners and can be privatised](https://admin-forum.paradoxplaza.com/forum/developer-diary/victoria-3-dev-diary-110-building-ownership-foreign-investment.1647879). | The split as a policy dial; ownership apart from the building | Arable-land style caps per state |
| [EU4](https://gameplay.tips/guides/1752-europa-universalis-iv.html) | A colonial nation forms when five colonised provinces sit in one region. It pays tariffs, and liberty desire drives independence. Leviathan added [crown, private-enterprise and self-governing](https://admin-forum.paradoxplaza.com/forum/developer-diary/europa-universalis-4-leviathan-development-diary-9th-of-march-2021.1461014/page-9) types. | Colonies become actors; charter type trades control for loyalty | The five-province switch |
| [Starsector](https://starsector.wiki.gg/wiki/Colony) | Colonies grow through discrete sizes; [industry slots](https://starsector.wiki.gg/wiki/Industry) grow with size; hazard rating scales upkeep and growth; accessibility sets trade. | Hazard ≈ colony cost; accessibility ≈ transport cost | Discrete sizes and slots |
| [X4: Foundations](https://store.steampowered.com/app/392160/X4_Foundations/) | NPC factions build and expand modular stations; ships, stations and ammunition are all made from resources in the simulated economy. | The NPC economy builds from the same parts as the player | |
| [Workers & Resources](https://lemm.ee/post/12629791/5281688) | Every building and worker is physical; projects are built with local labour and materials or bought with imported currency. | Build local or import: the dependency ladder in miniature | Full micromanagement can't scale to a planet |
| [Per Aspera](https://www.gamewatcher.com/reviews/Per-Aspera-review/13250) | Mars terraformed in staged steps, with mirrors, aerobraked asteroids and imported gases as levers. | Terraforming levers that are real physical projects | Stage gates; centuries compressed into hours |

## What to take and what to avoid

Take the mechanisms that make the economy run itself; drop every threshold that makes a settlement change kind.

**Take:**

- **Aurora's colony cost,** generalised into a continuous, local burden per person that terraforming lowers.
- **Distant Worlds 2's state/private split:** the player builds public goods and sets terms; firms do the rest and pay for it.
- **Victoria 3's investment pool and ownership:** private money builds what pays, the player's law sets how much room it has, and a building's owner is a separate fact from the building.
- **EU4's colonies as actors:** the charter type (crown, private enterprise, self-governing) maps directly onto our charter terms, and liberty desire onto constituency politics.
- **Aurora's risk-aware civilians:** freighters avoid danger and settlers avoid unprotected places, so a blockade is an emergent result of risk, not a special mechanic.
- **X4's one economy:** NPC firms build from the same blocks the player does.
- **Workers & Resources' build-local-or-import choice,** which is the dependency ladder at the scale of a single project.

**Avoid:**

- **Slots and site counts** (Terra Invicta, Starsector, Stellaris). They are hard cutoffs, and they cap the sprawl we want.
- **Tiers that change a settlement's kind** (Terra Invicta's cores, Starsector's sizes, EU4's five provinces, Aurora's population unlocks). Fleetwright's first rule bans them.
- **Fixed yields per site.** Our resources are extraction cost curves already; a site has a cost per tonne at today's energy price and tech, not a number.
- **Terraforming as a checklist** (Solar Nations 2). It should be industrial throughput into physical state variables.
- **Random spawns where physics could decide.** Firms appear where the expected return clears their hurdle, not on a dice roll.

## The ground: places, not slots

A body's surface is a set of fields, and a site is wherever someone builds. Nothing counts sites or caps them.

- **Surface fields** on a geodesic grid whose resolution is a setting, not a game rule:
  - elevation and slope;
  - insolation, including polar peaks of near-constant light and permanently shadowed cold traps;
  - ice depth and fraction, ore concentration by kind and depth, regolith depth;
  - lava tubes and caves (free volume and shielding);
  - local radiation dose, set by the atmospheric column above;
  - dust.
- **Off-surface sites:** orbits, Lagrange points, and small bodies taken whole (an asteroid is one site that can be hollowed).
- **The extraction cost curve, per cell.** The cost per tonne of a good delivered somewhere depends on concentration, depth, energy price, tech blocks and the gravity well to the destination. This is the existing resource model made local: ice 2 m down on a crater rim beats ice 30 m down on a plain.
- **Crowding is a cost, not a limit.** Installations compete for flat ground, sunlight, a radiator's view of cold sky, and safe distance (a reactor or a propellant depot beside habitats is a hazard). Each is a smooth penalty.
- **A settlement is a cluster, not a declaration.** Installations joined by local networks (power, pressure, roads, pipelines) form a cluster that the UI names and reports on. Two clusters that grow together merge; one cut in two splits. Like a group track, it is a representation, never a kind.
- **Claims are areas drawn on the fields.** A charter grants an area, a polity claims one, and an overlap is a dispute. Nothing is pre-cut into provinces.

## Installations: designed things, light until touched

An installation follows the ship generator's contract on the ground: blocks and numbers in, a physical model out, and the mesh is the hitbox.

- **Design:** tech blocks (reactor, radiators, habitat volume, ISRU plant, mine, smelter, fab, yard, mass driver, spaceport, sensor post, laser battery) plus numbers: capacity, metres of regolith overburden, burial depth, spacing.
- **Physical model:** geometry, mass, materials, heat budget, power draw, crew, hitboxes and a report. Radiators still size everything; on a surface they also see warm ground and part of the sky.
- **Designs are reused like ship designs.** A polity's standard habitat module or mine is a design; firms use their own or buy one.
- **Light until touched,** as Fleetwright's merchants: capacity, condition, stocks, owner and position. Full state (thermal nodes, internal spaces, damage) only while something engages it.
- **Districts: many small installations as one stock.** Ten thousand settler homes are not ten thousand entities. A district is a stock of one design family with a count, an area, a mean shielding and a spread, much like a group track. Damage resolves against its density, with correlated and independent hits kept apart, and is calibrated on the parity bench against fine runs where every building is explicit. Explicit or district is chosen per entity, never by size: whatever the player or a firm designs as a named installation stays explicit.
- **Wear and spares tie installations to the dependency ladder.** A fab consumes electronics-tier spares, a fusion plant fusion-tier ones. Cut the supply and capacity decays at a rate set by stockpile and wear, so an embargo bites gradually and visibly.

## People and the burden of living there

People are populations, not individuals, and they go where living pays after its burden, its transport and its risk.

- **Groups by constituency:** company staff, contract workers, free settlers and the locally born. Each group has skills, wages, loyalty toward the company and the host, and a temper; tempers add as in Fleetwright (polity line, governor, the group's own).
- **Burden per person,** generalising Aurora's colony cost: the capital and energy per head to keep someone alive and well here. Every input is continuous:
  - pressure and temperature to hold;
  - radiation dose to shield, from the column above and the overburden;
  - gravity, as a health cost over years;
  - light for food, and local water and volatiles.
- **What the burden buys:** habitat volume, life-support plant, power and maintenance per head. Overcrowding raises it, and unrest with it, smoothly.
- **Carrying capacity is an outcome, not a cap.** It is where population times burden meets what the settlement can build and maintain.
- **Migration reads risk from the group's own picture.** A recent strike, a blockade or raiders on the route lower the pull, so an unprotected colony draws few settlers: Aurora 2.6's rule, made continuous.
- **The locally born share grows** with births and time. They have no Earth home to return to, and their loyalty leans local: the creole constituency of the conflict axes.
- **Labour is a real input.** Automation substitutes for workers by tech block, and a fully automated outpost is allowed. It has no local constituency, so no settlers defend it and no local politics form; who controls it is covered under automation below.

## Who builds: ownership, the private sector and the control dial

The player always commands what the company owns. How much of a settlement that is falls as others build, and the player's main lever shifts with it.

**Two facts per installation: owner and jurisdiction.**

- **Owner:** who gets the output and decides its use. The company, a host state, a rival company, a named firm, the local private sector, households or a colony government.
- **Jurisdiction:** whose law applies on that ground: taxes, licences, inspections, who may arm it. A seizure changes jurisdiction while ownership survives as frozen assets and a grievance, which is how inner-system holdings become hostages.

**The private sector is AI polities in miniature.**

- Firms issue the same build, buy and hire commands as the company: one command path. A firm is a balance sheet, a few preferences and a temper.
- Large firms are named actors (shipping lines, mining houses, a rival's subsidiary). The many small ones in a settlement are one statistical actor, the local private sector, the way a district is one stock.
- The investment pool fills from retained profits, local savings and Earth capital chasing returns. Earth capital acts on light-lagged news of prices and risk.
- Firms score candidate projects by expected return after tax, licence cost, transport and risk, with hysteresis, and build the best one above a hurdle rate. Rules, no search, as in Fleetwright.
- Firms go broke, sell, merge, get bought, and get nationalised.

**The player's levers, in the order they tend to become the main one.** All are available at all times.

1. **Direct building:** the company's own installations, placed by hand or by its governor.
2. **Public infrastructure** that makes private projects pay: power grid, spaceport, mass driver, pipelines, sensors and defense. This is Distant Worlds 2's state role.
3. **Terms:** taxes, tariffs, licences and claims granted, labour law, immigration, and which ladder tiers outsiders may build. Keeping chip fabs in company hands is a choice with a price.
4. **Ownership moves:** privatise to raise cash and please settlers, nationalise to take control back, each at a political cost (Victoria 3).
5. **Security:** patrols and garrisons lower risk, which raises investment and migration.

**A settlement's economic law is a set of terms, not a mode.** Presets name common combinations, like doctrine presets, but every term is its own value:

| Preset | Who owns what | Gains | Costs |
| --- | --- | --- | --- |
| Company town | The company owns plant, housing and the store; outsiders build only by licence | Control and revenue capture | Slow growth; workers' resentment builds |
| Concession | The company keeps infrastructure and strategic plant; the rest is licensed | Growth with the key tiers held | Licensees gain weight and opinions |
| Free colony | Open investment; settlers own land and homes | Fastest growth, cheapest for the company | Least control; a colony with its own will |

**Constituency weight follows ownership and numbers.** Whoever owns and lives there gains weight in the settlement's politics. The resulting structure (board, governorship, republic, guild federation) is the initial notes' "whom the player empowered", read off this ledger. Giving settlers ownership buys growth and loyalty now and liberty desire later: EU4's colonial politics made physical.

**A governor runs the company's share by default.** The AI commands the player's own side, and the player takes the hand where they want it. The governor follows doctrine and standing orders under light-lag; the player's orders are instant.

## From one base to a civilization

Four numbers place a settlement on the path, and none of them is a state in code: the company's share of capital, closure per ladder tier, the locally born share, and burden per person. The labels below are UI words for regions of that space, like era names for families of blocks. Population figures are illustrative.

| Label | People | Closed through | Most capital owned by | Player's main lever | What an attack does |
| --- | --- | --- | --- | --- | --- |
| Outpost | 0–20, often robotic | Tier 0 only; the rest imported | The company | Places every installation | A raid destroys or takes it outright |
| Company town | 10²–10³ | Tier 1, volatiles | The company | Placement, wages, rotations | Strike the plant, cut resupply; crews evacuate or are held |
| Concession | 10³–10⁵ | Tier 2, bulk structure | Company infrastructure, licensed firms, settler homes | Infrastructure and licences | Blockade drains spares; a landing seizes it; settlers become hostages |
| Colony | 10⁵–10⁷ | Tiers 3–4 and coarse tier 5 | The private sector | Terms, taxes, security; holds strategic plant | Blockade is slow to bite; bombardment is an atrocity; politics decides |
| Civilization | 10⁷ and up | Fine tier 5 and tier 6 | The private sector and its own government | It is a polity; the company is one firm among many, or the state | A war between polities |

A settlement can move in either direction. A colony under blockade slides back down the closure column as spares run out; a company that nationalises climbs back up the ownership column and pays for it in loyalty. Earth-like Mars is this table's far end with burden per person near zero across whole regions.

## Manufacturing: how a settlement climbs the ladder

A settlement's climb is the manufacturing note's closure measured at one location, and the private sector climbs most of it on its own by import substitution. The company's real choice is the top of the ladder.

- **"Closed through" is closure.** The labels table above reads mass and value closure per tier at that location ([`design/manufacturing-and-the-dependency-ladder.md`](manufacturing-and-the-dependency-ladder.md)). Mass closure rises early with tiers 1–2; value closure waits on the vitamins.
- **Facilities are installations.** A smelter, a fab or an aerogel plant is a bundle of process blocks on the installation pipeline. The process block supplies energy per kg, specific throughput and environment; the installation supplies geometry, heat and hitboxes. One catalogue, two uses.
- **Firms do import substitution by themselves.** The manufacturing crossover (make locally once local cost beats the delivered price) is exactly the firms' investment score. Wherever there is demand and power, the private sector climbs tiers 1–3 without being told. The company decides what it keeps at the top: fabs, enrichment, superconductor tape. The concession preset is "keep the vitamins".
- **People and plant compete for output.** The growth law's f is the share of output reinvested in plant. A settlement also spends output on habitats, consumer goods and services, so its f is lower than an automated plant's. In return it adds labour, skills that speed the learning curves, and a local market that draws firms.
- **Labour enters the growth law as utilisation.** Plant without operators runs below its rated throughput, so r = s · f · a / k, with a (0 to 1) set by crew on site or by autonomy. A colony short of skilled workers has idle plant; an automated one is short of chips instead.
- **Burden falls with closure.** Habitats and life support are bills too: shells at tier 2, seals and machinery at tier 3, controls at tier 5. As closure rises, each settler needs fewer imported kilograms. Imported kilograms per person are what Earth's leverage over a colony's population really is.
- **A blockade is the growth law with I = 0.** Plant growth stops at once, capacity decays as spares run out, and holding time is vitamin stockpile divided by consumption. The siege model is the ledger, nothing more.
- **Bootstrapping strategies are settlement paths.** A seed factory or a technology spiral starts as an automated outpost. Import substitution is the company town to colony path. A specialised network is several settlements closing different tiers and trading, so closure exists only for the network, and its lanes become targets.
- **Terraforming is the same industry, and its limits come from the same numbers.** Aerogel, roof membranes and greenhouse-gas plants are process blocks with kWh/kg. Every regolith plant is also an oxygen plant, so venting by-product O₂ is a slow, real contribution, though regolith sinks eat some of it. Transmutation can't build an atmosphere: at about 1,000 t a year per TW of fusion, a nitrogen buffer of 1.9×10¹⁵ t must be found or imported.

## Automation and non-human actors

An automated company base and a machine polity's base can be the same hardware. The difference is where command authority sits, so both are modelled with one controller field on the same installation, and a machine polity is the far end of that field's dial.

### The controller

Every installation and ship has a controller. Three numbers describe it, all continuous:

- **Autonomy:** the share of tasks that run unattended. It comes from the manufacturing note's autonomy research line and costs tier-5 compute.
- **Mandate:** what the controller may decide without asking: production only, then investment, defense, trade, diplomacy.
- **Fidelity:** how reliably it does what its principal wants, under light-lag and over time. Drift lowers it.

The labels below are regions of those numbers, like the settlement labels:

| Controller | Lag it tolerates | What it needs | Typical use |
| --- | --- | --- | --- |
| Crew on site | Any | Life support: the burden per person | Company town |
| Remote operator | A few seconds; fails beyond the Moon | A link and operators at home | Early lunar plant |
| Supervised autonomy | Hours to days, with check-ins | Autonomy blocks; occasional human attention | Belt refinery |
| Delegated agent | Weeks; acts on a broad mandate | More compute; a wide mandate | A governor; an autonomous mining house |
| Independent agent | No principal | Its own goals | A machine polity |

### Automated bases under human control

An automated base is a delegated captain made concrete: standing orders, doctrine and light-lagged reports, on the same delegation mechanics as ships.

- **What automation gains:**
  - no burden per person, so nearly all output can go back into plant;
  - it runs where people can't: Io, Mercury, the radiation belts, the far belt;
  - the company keeps close to 100 % of capital, so automation is how to hold a place without settlers and their liberty desire.
- **What automation costs:**
  - robots and their brains are tier-5 vitamins, so automated industry has a higher vitamin share v and a lower ceiling under embargo;
  - no consumers means no local market, so firms don't follow;
  - no settlers means no defenders and no hostages. Striking an empty base is a property incident, not an atrocity, so automated holdings are cheaper to attack;
  - hosts license autonomy the way they license drives, and Earth's labour, safety and AI-risk constituencies weigh on that clause.
- **People or machines is the central colonisation choice.** People bring demand, defenders, politics and in time independence. Machines bring control and speed, and dependence on chips.

### Machine polities

A polity is a command path with goals, not a set of members, so a machine polity needs nothing new in the model. Its constituencies are its own processes, and perhaps human clients.

- **Its population is compute.** Burden per mind is power, cooling and replacement chips instead of air and food, and its births are fab output. Until it owns a fab it is the actor most exposed to Earth's chip leverage; once it has one, it grows by the manufacturing growth law with almost no consumption drag.
- **It wants different ground.** Its burden is low everywhere, so it settles hot inner bodies, radiation belts and cold outer moons. It competes with people for vitamins, power and lanes rather than for land.
- **Light-lag splits it.** A mind spread from Mars to Saturn can't be one mind: its parts act on old news and drift apart, the same delegation problem as captains. Machine polities have internal politics, copies with diverging tempers, and can fracture like human ones.
- **Moral standing is an observer's view.** Whether destroying a machine mind is an atrocity, property damage or nothing depends on who is watching. Incidents are recorded the same; each polity's temper weights them. Machine rights become a constituency question on Earth and in the colonies.
- **It arises without a hard cutoff.** A delegated agent's mandate widens (it runs investment, holds accounts through shell firms), fidelity falls (drift under lag, a principal gone bankrupt, independence granted on purpose), and at some point no one can recall it. "Machine polity" is the label for that end of the dial.

### Ostensibly the same: attribution is a picture problem

From outside, an automated company base and a machine polity's base share a signature: no habitat heat, the same plant, the same traffic. Who controls it is inferred from behaviour, communications and claims: intelligence, not sensing ([`design/detection-and-the-picture.md`](detection-and-the-picture.md)).

- **It cuts both ways in the gray zone.** A company can disown an incident as a rogue system, and a machine actor can fly a company's flag.
- **The incident record stores the act and who observed it;** attribution stays contested, like any covert act on the defiance ladder.

### How much agency machines have is a setting

The physics stays the same; only the controller numbers differ:

1. **Tools only:** fidelity is fixed at 1, and no machine polities exist.
2. **Delegates:** drift and defection are possible and rare; a machine polity can emerge during a campaign.
3. **Actors:** machine polities exist from the start.

The manufacturing note's runaway seed factory is the extreme case: an independent agent with a trivial temper and a universal assembler.

### Other non-humans, briefly

- **Modified humans** (adapted to low gravity or radiation, or long-lived) are constituencies with different burden coefficients. Nothing new is needed.
- **Aliens** are outside the realism brief. If ever added, the model is species-neutral: a polity with its own blocks, picture and temper.

## Attacks at every scale

Everything on the ground is a target in the same damage model as ships. The larger a settlement, the more an attack is decided by orbit, imports and politics rather than by hits.

- **Same effects, same deposition.** Bursts, projectile clouds and beams hit installations as they hit ships. Regolith overburden is armour, density-led at hypervelocity, so buried habitats are hard.
- **Surface radiators can't turn edge-on.** Radiators and solar fields face the sky, so an orbital threat always sees their face. That is the reverse of a ship's radiator problem, and a reason to bury heat sinks or run on stored cold during a strike.
- **The terminal layer grows with the atmosphere.** Column mass is pressure divided by gravity. Mars today holds about 0.16 t/m² against Earth's 10 t/m², which is no shield. At the Armstrong limit (62.7 mbar) it holds about 1.7 t/m², and a 1 bar Mars about 27 t/m², more than Earth because of the low gravity. Envelope speed limits around a body loosen as its column grows.
- **Blockade drains the ladder.** Imports of spares and goods stop, stockpiles run down, and capacity decays tier by tier. Freighters and settlers avoid risk by their own picture, so a few warships near the routes do most of the work. Self-sufficiency per tier is how long a settlement can hold out.
- **Seizure changes jurisdiction.** Landing troops or boarding a station transfers law and command. Ownership survives as frozen assets and hostages. Ground operations need their own abstraction (open question).
- **Scale changes what an attack means.** An outpost is destroyed or taken. A colony of a million can't be taken by hits without killing people, which is the top of the incident ladder and seen by every observer. Strikes on a district resolve against its density, calibrated against explicit layouts.
- **Fixed defenses carry the big optics.** A planet or station can mount what a warship can't: the planetary-defense laser row of [`design/combat-ranges-and-group-tracks.md`](combat-ranges-and-group-tracks.md) (30 m mirror, 10 GW, light-seconds), sensor posts, and point defense with no mass budget. Settlements are the protected bodies the envelopes are computed for.
- **Industry is the weapon, again.** A mass driver that exports ore can bombard. A mirror field that warms a basin can cook a settlement. A comet steered in for its volatiles is a kinetic strike in waiting. Dual use is recorded and watched like a torch drive.

## Making Mars like Earth

Mars becomes Earth-like the way the numbers allow: by roofing and warming regions until most people live with a near-zero burden, long before the open air is breathable.

**Habitability is local and continuous.** Each region carries pressure, temperature, water, radiation column, O₂ and buffer gas, open or enclosed. Turyshev's end-state labels are UI words on those numbers, the way "fusion era" names a family of blocks: E0 today, E1 recurrent liquid water, E2 protected agriculture under cover, E3 no pressure suit needed, E4 breathable.

**What the physics says:**

- Every millibar of global pressure is about 3.9×10¹⁵ kg of gas.
- Mars' accessible CO₂ is of order tens of millibars; about 20 mbar warms the planet by less than 10 K.
- Earth-like oxygen (21 kPa) is 8.2×10¹⁷ kg and takes at least 1.2×10²⁵ J to make from water: about 380 TW for a thousand years, before losses.
- A 50 kPa nitrogen buffer is 1.9×10¹⁸ kg. Mars' regolith probably can't supply it, so it is likely imported.
- A 2–3 cm silica aerogel layer warms the ground beneath it by roughly 50 K and blocks UV: regional habitability with today's materials.
- A roof 3 m high holding 50 kPa over the whole planet would contain roughly 6,000 times less gas than an open atmosphere at that pressure. The burden moves into structure, area and upkeep.

**Roofing Mars takes thousands of times less gas than thickening its air.** Mass of gas each target needs over the whole planet (Turyshev 2026, Tables III–IV and Eq. 70):

| Target | Gas mass |
| --- | --- |
| Roof over all of Mars, 3 m at 50 kPa | 3.0×10¹⁴ kg |
| Today's atmosphere, 6 mbar | 2.4×10¹⁶ kg |
| All accessible CO₂, ~20 mbar | 7.8×10¹⁶ kg |
| No pressure suit, 62.7 mbar | 2.4×10¹⁷ kg |
| Earth-like O₂ alone, 21 kPa | 8.2×10¹⁷ kg |
| Open atmosphere, 50 kPa | 1.9×10¹⁸ kg |
| Open atmosphere, 1 bar | 3.9×10¹⁸ kg |

The roof's figure is only the gas inside it; its real cost is structure, area and upkeep, which is exactly what an industrial colony is good at.

**So the path runs from the inside out:**

1. **Pressurised habitats,** buried for shielding.
2. **Covered ground:** aerogel fields and greenhouses, then roofed valleys and craters (worldhouses) at 10–50 kPa. Agriculture moves outdoors under cover, and burden per person falls.
3. **Regional microclimates:** seasons of liquid water in favoured basins, aerogel over ice-rich ground.
4. **Global warming and thickening:** super-greenhouse gas plants, reflector constellations, volatile imports by impact or capture, nitrogen from Titan or ammonia ices, perhaps a magnetic shield at Mars L1. Only past E3 do people walk outside without pressure suits.
5. **Oxygenation,** biological or industrial, over centuries or longer.

**Projects, not missions.** Each lever is an installation or a fleet with a throughput: an aerogel plant lays square kilometres a year, a gas plant adds infrared opacity, a reflector constellation adds watts per square metre, an impactor stream adds kilograms. The body's state variables integrate those flows against sinks (escape, freeze-out, oxidation of the regolith). A half-warmed planet is a real state, with seasonal lakes in Hellas and frozen plains elsewhere.

**Why the long dream still matters:**

- A near-zero burden over large regions makes population cheap to grow. Mars becomes the largest constituency off Earth.
- A thick atmosphere is a terminal defense layer, so terraforming changes what can threaten Mars.
- The levers are political. Volatiles delivered by impact are kinetic traffic near an inhabited planet; nitrogen from Titan is a dependency on the outer system; a reflector that warms a basin can burn a settlement.
- A worldhouse is a hostage. A breached roof over a million people is the gray-zone nightmare, so roofs are defended like ships.

## In the sim

The settlement economy lives almost entirely on the Routine tier, and drops to Coarse or Fine only where a fight touches the ground.

- **Stocks and flows on the Routine tier.** Between events every stock is linear in time, so a quiet year of a colony is one evaluation per settlement. Events re-anchor: a delivery, a price change, damage, a decision cadence for firms and governors. A stockpile running low is a notice through the interest table, never a change of state.
- **Markets per location.** Prices form where goods are; transport cost comes from Δv and launch windows. Price news travels at c to AI actors and Earth capital; the player sees the polity's picture, relayed instantly, as decided on Nov 1.
- **Firms and governors are scoring functions with hysteresis.** Deterministic, seeded per system, every number in settings, testable alone. Bar for the first cut: an all-AI system that keeps building and trading without stalling.
- **Light and full, explicit and district.** Installations are light until engaged; districts are stocks. Both are representations chosen per entity, and district damage is fitted from fine runs on the parity bench.
- **The body's state integrates slowly.** Atmosphere inventory by species, mean temperature, caps and sinks change over years, so they ride the Routine tier as smooth functions with re-anchoring when a project's throughput changes.
- **One matchup reads the same stocks.** How long a colony holds out under blockade and what force a host can deliver both read these ledgers, so the AI's judgement of a siege never uses a different model from the one that runs it.

## What the scenario battler needs

The battler needs installations as targets and stocks that drain; the private sector, migration and terraforming wait for the living solar system.

- **Installations as physical targets:** a mining outpost to raid, a station to inspect, a crater base with a laser battery. That means the ship generator's pipeline reused for ground designs, and the damage model working against overburden and surface radiators.
- **Stocks that drain:** a blockade scenario needs spares, propellant and food per settlement, consumption rates and capacity decay. A minimal Routine-tier ledger is enough.
- **Owner and jurisdiction fields from day one,** as scaffolding, like the incident records. A seizure scenario needs them even before any politics reads them.
- **A controller field from day one,** beside owner and jurisdiction. A raid on a crewed outpost and on an identical automated one is the cheapest test of the incident ladder: the same hits, a different record.
- **Not needed yet:** firms, the investment pool, migration, the surface fields beyond a few hand-placed sites, terraforming, machine polities.

**Suggested build order:**

1. Ground installation designer on the shipgen pipeline.
2. Damage against ground targets: overburden, surface radiators, districts as stocks.
3. Settlement ledger and blockade drain.
4. Owner and jurisdiction, and seizure.
5. In the campaign: surface fields and extraction curves, firms and the investment pool, people and migration.
6. Habitability state and terraforming projects.

## Open questions

- [ ] Surface grid: resolution per body, and whether small bodies need more than a handful of sites.
- [ ] Ground operations and seizure: how landings, garrisons and station boarding resolve.
- [ ] Named firms: how many, and when the local private sector spins one off.
- [ ] Money: one currency, host currencies, or local scrip (the company store is a political lever).
- [ ] Price formation per location under light-lag.
- [ ] Nationalisation by a colony government: what the company keeps, and whether it is a rung on the defiance ladder in reverse.
- [ ] Worldhouse failure modes and mass-casualty risk: how a breach propagates.
- [ ] Planetary protection and terraforming ethics as a constituency.
- [ ] Automation as a family of tech blocks, and whether fully automated holdings carry any politics at all.
- [ ] District calibration: which explicit layouts the parity bench uses.
- [ ] Controller numbers: how autonomy and mandate are researched and bought, and what drift rate light-lag implies.
- [ ] Machine personhood in host law: can a machine own assets directly, or only through shells?
- [ ] Default campaign setting for machine agency: tools, delegates or actors.
- [ ] Utilisation a in the growth law: crew-hours and robot-hours per kg of plant, per process block.

## Sources

- Turyshev, [Terraforming Mars: Mass, Forcing, and Industrial Throughput Constraints](https://arxiv.org/pdf/2603.00402), JPL, 2026: end states E0–E4, inventories, energy and the covered-area comparison.
- Jakosky & Edwards, [Inventory of CO₂ available for terraforming Mars](https://www.sci.news/space/mars-terraforming-06258.html), Nature Astronomy, 2018.
- Wordsworth, Kerber & Cockell, [Enabling martian habitability with silica aerogel](https://arxiv.org/pdf/1907.09089), Nature Astronomy, 2019.
- Green, [How to Give Mars an Atmosphere, Maybe](https://astrobiology.nasa.gov/news/how-to-give-mars-an-atmosphere-maybe/), NASA, 2017.
- Aurora 4X manual: [Civilian Economy](https://erikevenson.github.io/aurora-manual/6-economy-and-industry/6.5-civilian-economy.html), [Establishing Colonies](https://erikevenson.github.io/aurora-manual/5-colonies/5.1-establishing-colonies.html); [v2.6.0 patch notes](https://aurora4x.com/t/aurora-v2-6-0-patch-notes-september-6th-2025/23/3).
- [Distant Worlds 2 Dev Diary #6](https://www51.slitherine.com/news/distant-worlds-2-dev-diary-6) (state and private economy).
- Victoria 3 [Dev Diary #71](https://paradoxinteractive.com/games/victoria-3/news/dev-diary-71-autonomous-investment-in-1-2) (autonomous investment) and [#110](https://admin-forum.paradoxplaza.com/forum/developer-diary/victoria-3-dev-diary-110-building-ownership-foreign-investment.1647879) (building ownership).
- Terra Invicta wiki: [Habs](https://hoodedhorse.com/wiki/Terra_Invicta/Habs), [Colony Core](https://wiki.hoodedhorse.com/Terra_Invicta/Project_ColonyCore).
- Solar Nations 2: [community guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3726735090), [terraforming discussion](https://steamcommunity.com/app/2275440/discussions/0/586182021532002423/).
- EU4 [Leviathan dev diary](https://admin-forum.paradoxplaza.com/forum/developer-diary/europa-universalis-4-leviathan-development-diary-9th-of-march-2021.1461014/page-9) (colony types).
- Starsector wiki: [Colony](https://starsector.wiki.gg/wiki/Colony), [Industry](https://starsector.wiki.gg/wiki/Industry).
- [X4: Foundations](https://store.steampowered.com/app/392160/X4_Foundations/) store page.
