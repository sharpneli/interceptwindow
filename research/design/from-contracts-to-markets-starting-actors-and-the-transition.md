# Intercept Window: From Contracts to Markets – Starting Actors and the Transition

Nov 5, 2026 · proposal · continues [`design/early-economy-revenue-streams-and-the-growth-loop.md`](early-economy-revenue-streams-and-the-growth-loop.md)

Who is already out there when a campaign starts, and how an economy paid for by governments turns into one that pays for itself. Figures marked *(calc)* were computed for this doc; everything else is sourced at the end.

## The short version

- **The transition isn't a switch; it's a change in who pays.** Four numbers track it per polity and settlement: the **host share of revenue**, the **local multiplier**, the **intra-space trade share** and the **local capital share**. The era labels are UI words for regions of those numbers, like the settlement labels in the bases doc.
- **Rivalry is the fuel of the contract era, so the start needs several capable blocs.** Government money follows prestige and security, not returns. NASA's share of US federal spending peaked at 4.41 % in 1966 and fell to 0.98 % by 1975 once the Moon race was won. A start with one dominant actor ends in that cliff. A start with the US bloc, China, a competent Europe and a few swing states keeps the race open.
- **Competence is a number.** NASA's own cost model said Falcon 9 would have cost $1.7–4.0B to develop the traditional way. SpaceX did it for about $390M, a factor of 4–10 *(calc)*. Each actor gets an **execution factor** on the cost and schedule of its programmes, and a scenario sets it. A competent ESA is just ESA at a factor near 1.
- **Hosts move down a procurement ladder:** build it themselves → pay by milestone → buy a service → rent a share of someone else's facility → buy on the spot market. Each step gives up control and frees the company to sell spare capacity to others. Competition between suppliers and blocs pushes hosts down the ladder; crises push them back up.
- **Airmail is the template for weaning.** US airlines lived on mail contracts after 1925. In 1930 the payments were reshaped to reward carrying passengers. In 1934 mail pay was cut sharply, and by 1936 the DC-3 made passengers pay. **A good subsidy buys capacity that civilians can use, then gets cut.**
- **Second customers come before markets:** smaller governments buying seats (over $65M per country on Axiom-4), research payloads, private astronauts, defence services, and settlers with non-economic motives who pay their own way.
- **People alone don't make an economy; people spending locally do.** The local multiplier is 1 / (1 − s), where s is the share of each dollar spent on things made locally. An early outpost imports nearly everything, so s ≈ 0.1 and the multiplier is 1.1: every wage leaks straight back to Earth *(calc)*. **Raising s is import replacement, and import replacement is value closure.** The manufacturing ladder and economic self-sufficiency are the same curve.
- **Failure is local; the gradient is global.** The world always has an economic slope to climb, and only actors fall off it. Eight design guarantees make sure of this (section below). The two biggest: the gradient is physics, because falling launch costs and lunar learning lower costs every year whatever the market does; and **assets outlive owners**. Iridium's network cost more than $5B, went bankrupt, and was bought for $25M; the satellites kept flying.
- **The historical traps (budget cliffs, the Antarctica outcome, staple dependence, pork, boom-and-bust) all belong to individual actors and places.** A host's budget cliff pushes it to buy services instead of building, which grows the commercial market rather than ending it. Whole-world collapse exists only as an opt-in scenario.
- **The default arc is a spine every campaign can climb:** services near Earth → propellant and logistics sold to the blocs' own polar bases → cheap propellant at the cislunar nodes → yards, shielding and habitats → people and import replacement → Mars and the belt. Players and AI choose how, where and how fast. The world doesn't choose whether.
- **The landmark event is moving the board.** In 1629 the Massachusetts Bay Company's emigrating shareholders bought out those staying home and took the charter with them; the company and the colony became one body. A space company can do the same, legally, and it's a louder signal than any warship.

## Starting actors

### Where the real players stand (late 2026)

| Actor | Status | Source |
| --- | --- | --- |
| US / Artemis | Artemis II flew a crewed lunar flyby in April 2026. Both crewed landers (Starship HLS, Blue Moon) are late 2027 at the earliest, so the landing date is open | NASA via cislunarspace.cn |
| China | Crewed landing still targeted "before 2030" (two Long March 10 launches, Mengzhou and Lanyue). Long March 10B reached orbit in July 2026 with its booster caught at sea. Chang'e-7 missed its 2026 window. Chang'e-8 (brick printing from regolith) is around 2029 | SpaceNexus timeline |
| ILRS | China–Russia-led; "17 countries and international organisations". Basic model by 2035 ("long-term robotic operation with short-term human participation"); a lunar reactor memorandum with Russia (2025) | Same |
| Artemis Accords | 76 signatories by late September 2026 | NASA |
| Europe | ESA's Argonaut cargo lander: descent element due 2030, first operational mission 2031, built by a Thales Alenia Space-led consortium | ESA |
| LEO | No commercial station in orbit yet. ISS deorbit around 2030–31. Vast's Haven-1 slipped to no earlier than Q1 2027; Axiom's first module early 2028; Starlab no earlier than 2029 | SpaceNexus |

The start state is roughly 2030–2040 (decided Nov 2), so a campaign opens a few years after this, with every programme above either flying or failed. The game is free to pick which.

### A roster for the start (proposal)

The aim is tension at the start, not a forecast. Every actor below has something the others need.

| Actor | Starting foothold | Wants | Leverage | Weak spot |
| --- | --- | --- | --- | --- |
| **US bloc** (civil agency, space force, Accords partners) | A south-polar base camp; heavy lift through its national launch champions | Hold the best cold traps; stay ahead; keep costs down | Budget, chips, the Accords coalition, launch slots | Budget politics; depends on champions it can't fully command |
| **Launch champions** (two private heavy-lift firms) | Reusable heavy lift; their own satellite constellations; lander contracts | Their own goals (one wants Mars, one wants industry in space) | Rationed launch capacity, which they increasingly reserve for themselves | Chartered by the US; hostage to its licences |
| **China** (state agency and state firms) | An ILRS robotic station, short crewed stays, a reusable heavy lifter | Prestige; an alternative rulebook to the Accords; a polar claim of its own | State capital, industrial depth, a longer political horizon | Fewer partners with money; Western export controls on chips |
| **Russia** | Junior ILRS partner | Relevance | Nuclear power and fissile expertise | Money; launch rate |
| **Europe** (competent variant) | Argonaut cargo landers on schedule; in this variant, its own crew vehicle | Autonomy; a seat at both tables | Money, high tech, lithography (tier-5 vitamins), neutrality | Consensus across many member states; launch capacity |
| **India** | Cheap robotic landers; crewed flight to LEO | Prestige; a place in the polar real estate | Low cost per kg; a big domestic market | Budget size |
| **Japan** | Lander and rover partner to the US bloc | Technology leadership | Precision manufacturing, robotics | Tied closely to the US |
| **Gulf states** | Sovereign astronauts; stakes in companies | Prestige; diversification away from oil | Capital without a space agency's strings | No launch capability of its own |
| **Private ventures** | Stations, servicers, prospectors, the player's archetypes | Returns, or an ideological goal | Capability and speed | Capital and patience |

**Built-in tensions at the start:**

- **Overlapping polar claims.** A few ice-rich cold traps beside a few near-permanently lit ridges (tension 4 in [`studies/solar-resources/07-gamification-notes.md`](../studies/solar-resources/07-gamification-notes.md)). The Accords' safety zones and the ILRS station want the same ground.
- **Rationed launch.** The champions fill their own manifests first, so every other actor's progress depends on slots someone else allocates.
- **Two rulebooks.** Resources extracted under the Accords are owned; the ILRS bloc disputes it. A cargo of ice can be legal property in one bloc and theft in the other.
- **Nuclear power on the Moon.** Whoever has a reactor at the pole owns the night. A Russian-built reactor in the ILRS camp is a fissile question as well as a power one.
- **A swing actor with money.** Europe and the Gulf can sponsor charters of their own, buy services from either bloc, or back a company that defects from its host: the France-in-1778 template already in the design notes.

**Fictionalise the companies in content.** The design docs name real firms as analogues. Shipping content with real companies and their founders as characters invites trouble; their fictional stand-ins can keep the same shape.

### Competence as a number

Programmes in the real record differ by large factors in cost and schedule, and that's a playable difference between actors.

- **Execution factor:** a multiplier on the cost and schedule of an actor's programmes. Falcon 9 shows the real spread: about 4× between "commercial-style" and actual, about 10× between "traditional" and actual *(calc)*.
- **It moves.** Procurement reform, a successful programme, or new leadership lowers it; contractor constituencies and failures raise it.
- **It's a scenario knob.** "Competent ESA" sets Europe's factor near the champions'. A pessimistic start sets every agency high and leaves the private firms as the only fast movers.

## Why each host's contract era ends

Government space money follows rivalry and prestige. When a host's race is won, that host's money goes away.

| Year | NASA share of US federal spending |
| --- | --- |
| 1961 | 0.76 % |
| 1966 | 4.41 % (peak) |
| 1970 | 1.92 % |
| 1975 | 0.98 % |
| 2026 | about 0.33–0.35 % |

Nine years after the peak, the share was 22 % of what it had been *(calc)*. For the game that means:

- **Host budgets are political,** driven by rivalry, prestige milestones still to win, security and domestic will. A rival's milestone raises them; one's own, once won, lowers them.
- **The cliff is a dominance check on the player, not on the world.** The contract era is comfortable, and a company can't sit in it forever. A company still living on one host's budget when that host plants its flag is about to shrink. Companies with second customers, or with another bloc's contracts, ride through it.
- **Several rivals stagger the cliffs.** With the US, China and Europe all racing, somebody always has a milestone to answer, so the hosts' cliffs fall at different times and total world spending never drops at once. That's a second reason to start with many actors.
- **A cut moves a host down the procurement ladder; it doesn't end its programme.** Apollo ended in a cliff because there was nothing commercial to buy instead. With reusable vehicles and companies already operating, a host under budget pressure keeps its base and buys its logistics as a service, as NASA is doing with low Earth orbit after the ISS. The cut shrinks the host's spending but enlarges the commercial share of it.
- **Contractor constituencies make some money sticky.** Programmes that employ voters survive after their purpose fades. That money keeps flowing but buys little, because those programmes have the highest execution factors.

## The procurement ladder

Hosts buy in different ways, and each way leaves the company a different amount of freedom.

| Step | The host buys | Risk carried by | Hardware owned by | Host control | Real example |
| --- | --- | --- | --- | --- | --- |
| **Build** | Hardware it designs, cost-plus | Host | Host | Full | Apollo; heavy lift built for the agency |
| **Milestone** | A capability, paid by demonstrated steps, fixed price | Shared | Company | Through requirements | COTS |
| **Service** | Deliveries, seats, kilograms, years of life extension | Company | Company | Through contract terms | Cargo resupply, lunar payload deliveries, MEV |
| **Anchor tenant** | A share of a commercial facility's capacity | Company | Company | Small | NASA's intent for commercial LEO stations |
| **Spot** | Units as needed, at the posted price | Company | Company | Only through law | Buying propellant at a depot |

- **Moving down frees the company.** From the service step on, the company owns the hardware and can sell its spare capacity to anyone, which is where non-host revenue starts.
- **What moves a host down:** more than one capable supplier, budget pressure, and a supplier's track record.
- **What moves it back up:** war, a crisis, or a supplier that has become a security risk. Nationalisation is the top of the ladder seen from the other side.
- **The live version of this question is LEO in 2026.** NASA has told industry its budget can't fund several stations; the station builders answered with a 390-page dossier claiming demand already exists, citing 12 private-astronaut flights and 166 paying payloads. That's exactly the transition question: is there a market beyond the anchor?

**In the game,** each contract sits on a step of the ladder. Host AI picks the step by scoring control against cost, and the clauses of [`design/early-economy-revenue-streams-and-the-growth-loop.md`](early-economy-revenue-streams-and-the-growth-loop.md) are what it keeps when it lets go of ownership.

## Airmail: the template for weaning

US commercial aviation went from living on government mail to living on passengers in about a decade, and the steps map cleanly onto a lunar transport business.

| Year | What happened |
| --- | --- |
| 1925 | The Kelly Act puts airmail into private hands. Airline income comes mostly from mail contracts, at subsidies of about $3 per pound |
| 1926–30 | Passengers grow from 5,800 a year to 417,000 |
| 1930 | The McNary-Watres Act reshapes payments to encourage carrying passengers. Postmaster General Brown uses route awards to force mergers into a few large carriers |
| 1932 | The Boeing 247: airlines that can't live on mail build better passenger aircraft |
| 1934 | A new Air Mail Act cuts mail pay sharply; carriers must lean on passengers |
| 1936 | The DC-3 makes passenger service pay |

Three lessons for the design:

- **Pay for capacity, not only cargo.** A subsidy shaped to reward seats bought a fleet that could carry passengers once there were passengers. In the game this is a **capacity clause**: the host pays for a lander with four spare berths, or a tanker with spare tankage, and the company sells the spare.
- **Then cut it.** The 1934 cut forced the switch. A host that never cuts keeps a dependent industry; one that cuts too early kills it.
- **Picking winners consolidates, and invites scandal.** Brown's route awards produced the big carriers and, in 1934, the air mail scandal. A host that steers contracts to favourites builds strong champions with political enemies.

## Second customers come before markets

Before an in-space market exists, there are buyers other than the host, roughly in this order:

1. **Smaller governments buying access.** India, Poland and Hungary shared the cost of Axiom-4 in 2025, at more than $65M per customer. Hungary's astronaut said the point was to "sit at the same table with the giants". In the game, minor states buy seats, berths, payload slots and data from whichever company is there. Selling them to a rival bloc's partners is revenue and an incident at the same time.
2. **Research payloads,** the bread and butter of the station builders' 166 paying payloads.
3. **Private astronauts and tourism:** 12 private-astronaut flights so far.
4. **Defence services:** servicing, tracking, inspection and hypersonic test flights, as in the previous doc.
5. **Settlers with non-economic motives.** The Massachusetts Bay colonists came for religion and paid their own way. Ideology, refuge and adventure bring people before an economy can pay for them, and a founder who wants a Mars city is that motive with a launch company.
6. **Other companies in space.** Tug operators buying at depots, yards buying shielding, servicers buying fuel. This is where the market proper starts.

Each new customer type lowers the **host share of revenue**, which is the first of the four numbers.

## When there are people: the space multiplier

"Once there are lots of people in space it's easier" is right, but only if the people spend their money there.

### The export-base model

Regional economics splits an economy into a **basic** sector, which earns money from outside (exports, contract work, tourism), and a **non-basic** sector, which serves locals. Each dollar earned from outside is partly spent locally, and that spending is someone else's income, and so on. If s is the share of spending that stays local:

```latex
\text{local economy} = \frac{\text{export base}}{1 - s}
```

For a settlement earning $500M a year from outside *(calc)*:

| Local spend share s | Multiplier | Local economy | Of which local trade |
| --- | --- | --- | --- |
| 0.1 (outpost: everything imported) | 1.11 | $556M | $56M |
| 0.3 | 1.43 | $714M | $214M |
| 0.5 (a typical Earth town) | 2.0 | $1.0B | $500M |
| 0.8 (a mature colony) | 5.0 | $2.5B | $2.0B |

- **Early space towns leak everything.** Food, air, tools, spares and entertainment are imported, so each wage goes straight back to Earth and the town is a pipe, not an economy.
- **Services are local from day one:** cooking, medicine, repair, teaching, law, entertainment. But each person carries the burden per person from the bases doc, so service jobs only pay where living there is cheap enough.
- **The first goods to go local are tier 1:** water, air, propellant, and food once there's power and light. That's where s first rises.

### Import replacement is value closure

Jane Jacobs argued that cities grow by learning to make what they used to import; the money that used to leave is spent on new imports, and economic life expands rather than shrinks. That's the manufacturing crossover from [`design/manufacturing-and-the-dependency-ladder.md`](manufacturing-and-the-dependency-ladder.md), seen from the household's side:

- **s is the value closure of what residents and firms buy,** measured on their purchases, not on a warship's bill.
- **Firms already do it.** The bases doc has the private sector climbing tiers 1–3 by itself wherever there is demand and power. Those climbs raise s, the multiplier, wages, migration and the market for the next import to replace.
- **This is the loop the question is about.** More people → a bigger local market → more import replacement → higher s → more local income per export dollar → more people. It runs by itself once the first rungs are closed, and it's the same loop that erodes Earth's leverage.

### The staple trap

Jacobs' other warning is the **supply region**: a place that efficiently exports one commodity but never builds the breadth to do anything else, and lives precariously on that commodity's price. Canada's staples thesis (Innis) adds that **the staple shapes the society**:

- **Fur:** controlled by big firms such as the Hudson's Bay Company, producing a centralised, business-run society.
- **Cod:** decentralised but cooperative.
- **Wheat:** independent farmers who distrusted government and corporations.

That's a direct mechanic: a settlement's main export sets the default temper of its constituencies. An ice-mining company town leans centralised; a field of independent prospectors leans independent and suspicious; a helium-3 concession tied to one Earth buyer leans dependent. And a settlement that never diversifies past its staple stays a hinterland whatever its population.

## Space as its own customer

The third number is the **intra-space trade share**: how much of a polity's trade is with other off-Earth nodes rather than with Earth.

- **It starts near zero.** Everything comes from Earth, and the only products go back to Earth or to Earth's agencies.
- **It rises with the triangle trade** of the logistics doc: Earth sells high tech to Mars, Mars sells bulk and low-tech goods to the belt, the belt sells volatiles and metal inward.
- **Depot towns and picks-and-shovels firms lead it.** In any rush, the people supplying the miners have a steadier business than the miners. A company that sells propellant, repairs and berths to everyone else's ships earns from the whole rush, not from one claim.
- **Above half,** the off-Earth economy is mainly trading with itself. Earth is still the biggest single partner, but no longer the market that decides prices.

## Capital: from Earth money to local money

The fourth number is the **local capital share**: how much of the investment in a place comes from savings and profits made there.

| Stage | Main sources | What it means |
| --- | --- | --- |
| **Early** | Host grants, Earth equity, sovereign funds | High hurdle rates; the investors' constituency is on Earth |
| **Middle** | Retained earnings; workers' savings | Locally born residents have no Earth home and save locally; company scrip keeps savings in the company's hands |
| **Late** | Local banks, a local currency, local capital markets | Earth capital is optional; the investment pool in the bases doc fills from inside |

**Paying for infrastructure with claims.** Railroads were built with land grants along the line, so the builder captured the value its line created. In space a host can do the same: grant a company the claims around the depot or spaceport it builds instead of paying cash. It costs the host no budget and makes the company a landlord, which changes its politics.

**Moving the board.** The Cambridge Agreement of 1629 let the Massachusetts Bay Company's emigrating shareholders buy out those staying in England and move the company's government to New England. John Winthrop was elected governor; the charter crossed the Atlantic in 1630; the colony governed itself and answered only to the Crown. In the game:

- **It's a legal act**, not a defiance-ladder rung in itself: the charter may not say where the board sits.
- **It's a loud one.** Earth shareholders bought out, the seat moved off Earth, the constituency balance flipped toward residents. Hosts read it as a step toward de facto autonomy, and the AI should.
- **It needs local capital** to buy out the Earth shareholders, which is why the local capital share matters.

## The phases, as labels

These are UI words for regions of the four numbers, never states in code. A polity can sit in different phases at different settlements, and slide back.

| Label | Host share of revenue | Multiplier | Intra-space trade | Local capital | Main customer | Player's main lever |
| --- | --- | --- | --- | --- | --- | --- |
| **Contract era** | Most of it | ~1.1 | ~0 | ~0 | The host | Winning and executing contracts |
| **Second customers** | Under half | 1.2–1.5 | Small | Small | Other governments, research, tourists | Spare capacity; capacity clauses |
| **Mixed economy** | A minority | 1.5–2.5 | Rising | Retained earnings | Other companies in space | Depots, prices, terms |
| **Space-centred** | Small | 2.5 and up | Over half | Mostly local | Itself | Policy, as a polity |

## The default arc: a spine every campaign can climb

The world's path to a self-sustaining economy should be plausible in every seed, with players and AI deciding how, where and how fast. These are stages of tech and capital, never dates, and they overlap.

| Stage | What pays | Why it reliably appears |
| --- | --- | --- |
| **1. Services near Earth** | Life extension, refuelling, LEO stations, sovereign seats, research payloads | An existing satellite economy of hundreds of billions already needs servicing; minor states already buy seats |
| **2. Logistics for the blocs' polar bases** | Water, oxygen, propellant, power and cargo delivery, sold as services to every bloc with a base | Several blocs hold bases, each cheaper to supply locally than from Earth. Lunar propellant beats Earth's at the surface, low lunar orbit and L1 from its first year in Metzger's model |
| **3. Cheap propellant at the cislunar nodes** | Propellant at L1, NRHO and GEO; tugs and tankers | The frontier of lunar advantage moves inward over time. Each tenfold drop in market size delays it reaching LEO by only about two years |
| **4. Mass for building in space** | Shielding, structure and tanks for yards and stations | Once propellant is local, launching bulk mass is the next biggest bill to replace |
| **5. People and import replacement** | Wages spent locally; local food, air, repair, services | Crews, contractors, tourists and settlers with their own motives; each closed tier raises s |
| **6. Mars and the belt** | The triangle trade; outer hubs | Mars is closer to the belt than Earth in Δv; cheap cislunar propellant makes the first legs affordable |

**Government bases are the anchor of stage 2, and there are several.** The blocs keep their bases for prestige and security, whatever the commercial case. Every one of them needs water, air, power and propellant, and buying them locally beats lifting them. Even a pure-prestige outpost is a customer.

## Failure is local, the gradient is global

The game's promise: **the world always has an economic gradient to climb, and only actors fall off it.** A company fails because its player or AI steered it badly, never because the solar system turned out to have no economy. Eight guarantees, each with a real basis.

| # | Guarantee | Real basis | In the model |
| --- | --- | --- | --- |
| **G1** | **The gradient is physics.** Costs fall every year whatever the market does | Earth launch learning; lunar production learning faster than launch. In Metzger's model, market size moves the date lunar propellant wins, not whether it wins | Learning curves are industry-wide quantities, not one firm's luck |
| **G2** | **Demand has several independent engines.** No single buyer carries the world | Several blocs' budgets, an Earth-orbit service market, sovereign buyers, ideological ventures | Start state rule: no one engine is more than a set share (proposal: 40 %) of world off-Earth spending |
| **G3** | **Cliffs are per host and staggered,** and a cut moves the host to buying services | The Apollo cliff happened with no commercial alternative; the post-ISS plan buys services instead | Host budgets react to rivals' milestones, so they peak at different times; cuts shift the procurement step |
| **G4** | **Assets outlive owners.** Bankruptcy changes who owns the hardware, not whether it exists | Iridium: a >$5B network, bankrupt in 1999, bought for $25M in December 2000; it then won a $72M two-year DoD contract and kept flying. In 1893 about a quarter of US rail mileage went into receivership; receivership is reorganisation, not demolition | A failed firm's installations and ships go to auction at distress prices; buyers get cheap capacity and the world keeps it |
| **G5** | **Sentiment shocks are bounded and decay** | Investors forget; AstroForge raised money after Planetary Resources | A sector failure raises hurdle rates by a capped amount with a half-life, never permanently |
| **G6** | **Know-how leaks.** A failed firm's learning isn't lost | Staff, suppliers and published results carry it | Part of each firm's learning goes into an industry pool that lowers everyone's costs |
| **G7** | **AI actors are competent enough.** They use the same scoring as firms, tuned so the world climbs without the player | The bases doc's bar: an all-AI system that keeps building and trading without stalling | The "world climbs" bench, below |
| **G8** | **Global collapse is opt-in.** A scenario may start in a long winter; the default campaign never enters one | — | A world-difficulty setting, separate from player difficulty |

**G4 is also an opportunity.** A rival's bankruptcy is the cheapest way to get a depot, a yard or a fleet, so a well-run company profits from others' failures. A badly run one may be the asset someone else buys.

### The world-climbs bench

A regression test, like Fleetwright's parity bench: run the world with **no player** over many seeds and across start settings (including the pessimistic one, with every agency's execution factor high).

- **Pass:** in nearly every seed (proposal: 95 %), at least one settlement reaches the mixed-economy region within a set span of sim time, and world off-Earth spending never falls below its starting level for longer than a set span.
- **Fail:** any seed where the world stalls in the contract era. Fix it by moving a guarantee's numbers, never by scripting an event.
- **Separately,** the same bench with one AI company deliberately misplayed must show that company failing while the world still passes.

## How a player fails, and how they recover

The traps of history all happen here, scoped to the actor who walked into them.

| Trap | How the player walks into it | What it costs them | The world meanwhile |
| --- | --- | --- | --- |
| **One customer** | Living only on the host's budget when its milestone lands | Revenue halves overnight | Other blocs and second customers keep buying, from someone else |
| **The staple trap** | One export from one settlement, nothing else | Ruin when its price falls; a one-sided constituency | Diversified rivals take the market share |
| **Dumping** | Flooding a thin market (helium-3, platinum) | Its own price collapses | Buyers enjoy cheap supply |
| **Overleverage** | Borrowing to build ahead of contracts | A failed round; bankruptcy | The hardware goes to auction (G4) |
| **The Antarctica choice** | A host or company that only does prestige and science | Pure cost, no income | Its outposts are customers for others |
| **Pork and favouritism** | A host that steers contracts to favourites | High execution factors; scandal; cancellations (the 1934 airmail cancellation) | Rival hosts' cheaper companies win the work |
| **Wrong bloc** | Chartered to the host whose programme stalls | Fewer contracts, poorer launch access | Other blocs climb; re-chartering is possible, as a provocation |
| **Overreach** | Settlements beyond what logistics and spares can hold | A blockade or a missed window drains them | Someone else holds the node next time |

### No takeovers of the player's company; bankruptcy is the failure

Decided Nov 5: **no AI actor can buy, merge with or take over the player's company.** The player's way to fail is bankruptcy. AI companies can still be bought, merged and taken over by each other, and by the player.

**What bankruptcy does** (a court-run reorganisation, like the 1893 railroads, not a game over):

- **Assets go to auction** to pay creditors, as in G4. Rivals and AI firms buy them, so the world keeps the capacity.
- **The company survives as a legal person.** It keeps its name and its core, and its charter unless the host revokes it (below).
- **Debts are written down** to what the remaining company can carry.
- **Creditors join the board as a constituency,** with a temper of their own (cautious, short horizons), until the company pays its way out. That's internal politics, not loss of control: the player still commands the company.
- **Investors' hurdle rate** for the company jumps and decays with its new track record (G5, applied to one firm).

### Revocation is a ruling; enforcement is physics

Decided Nov 5: **the host can revoke a bankrupt company's charter**, and the player doesn't have to obey. A court ruling is only as effective as someone's ability to enforce it.

- **Revocation changes the law, not the facts.** It's a jurisdiction act ([`design/bases-settlements-and-the-civilian-economy.md`](bases-settlements-and-the-civilian-economy.md)): the host stops recognising the company's claims, licences and right to arm ships, and may hand the claims to a rival. Ownership of hardware on the ground doesn't move until someone moves it.
- **Enforcement is deliverable force.** Inner-system holdings, Earth-side accounts and staff are in reach, and are lost at once. A depot at the pole or a base at Ceres stays the company's until the host, or the rival it handed the claims to, comes to take it. That's the same deliverable-force estimate as the independence arc.
- **Ignoring it puts the company on the defiance ladder** at rung 4 (de facto autonomy) without a declaration. The host's responses are the ladder's usual ones: blockade, proxy enforcement through the rival that got the claims, export denials on vitamins.
- **So bankruptcy can be an accidental road to independence:** a company the courts have written off, holding what it can physically hold. Whether that's survivable depends on the same curves as a deliberate break.

### The real enforcer is payroll

What a ruling can't do, an empty payroll can. **Crews who aren't paid stop working**, and a base without workers runs only as far as its automation reaches.

- **Wages are a stock that runs into arrears.** Each crew group (company staff, contract workers, free settlers, the locally born) has a willingness to work set by arrears, what else it could do, whether it can leave, and its loyalty and temper.
- **What unpaid crews do depends on whether they can leave:**

| Crew situation | Likely response |
| --- | --- |
| Contract workers with a ship home | Leave on the next departure |
| Contract workers with no transport (a window months away) | Strike; work for food, air and berths only; or hand the base to whoever pays |
| Company staff | Loyal longer, depending on temper; then the same choices |
| Locally born and free settlers | Nowhere to go: they stay, keep life support running, and may take the base over as a colonist assembly |

- **Paying in kind buys time.** Food, air, water and berths from the base's own plant (tier 1 closure) keep people alive and somewhat willing, at no cash cost. Company scrip works until people stop believing in it.
- **Crews can defect.** A host or a rival that offers to pay the arrears can take a base without a shot, which is the loss through labour this design allows instead of a takeover of the company.
- **Unmanned is not dead.** Lost crews drop the plant's utilisation a in the growth law (r = s · f · a / k). Automated plant keeps running at its autonomy level until spares run out, so a heavily automated company survives bankruptcy better than a crewed one: the people-or-machines choice of the bases doc, paying off.
- **Mothballing is the player's tool:** put a base into a safe, unmanned state, keep the claim physically occupied, and come back when there's money.

**Before bankruptcy, the player has voluntary ways out** of a bad position: selling assets, shrinking to a niche (a servicer or a single depot, and climbing again from rung 1), or re-chartering with another host at the price of the old host's anger. Selling is always the player's choice, never forced except by the bankruptcy court.

## Model proposal for Intercept Window

### Host budgets

- **Budget = base × motive × will**, where motive adds up rivalry (rivals' recent and pending milestones), prestige still to win, and security, and will reads domestic politics and competing crises.
- **Milestones are consumed.** Planting the first flag at the pole spends that motive; the rival's flag renews it.
- **Contractor constituencies** add a sticky floor tied to the programmes they work on.

### Per actor

- **Execution factor** on cost and schedule, set by the scenario and moved by events.
- **Procurement step** per contract (build, milestone, service, anchor tenant, spot), chosen by the host's scoring with hysteresis, like firms' investments.
- **Capacity clauses:** spare berths, tankage or payload mass the company may sell.

### Per settlement, on the Routine tier

- **Export base by customer:** host, other governments, Earth private, other off-Earth buyers.
- **Local spend share s,** from the value closure of the residents' and firms' basket.
- **Local economy** = export base ÷ (1 − s). Wages come out of it; migration reads wages against burden per person and risk, as the bases doc already says.
- **Staple:** the dominant export, which sets the default temper of new constituencies.
- **Capital sources:** host, Earth equity, local savings, retained earnings.

### World guarantees

- **Industry learning pool:** each firm's cumulative output feeds its own learning curve and, in part, an industry-wide one that sets the floor for everyone's costs (G1, G6).
- **Demand engines:** the start state lists the world's independent demand engines and their shares, checked against the cap (G2).
- **Bankruptcy and auctions:** a failed firm's installations, ships, claims and drill logs go to auction; firms and polities bid from their own picture of the assets' value (G4).
- **Sentiment:** a sector-wide hurdle-rate premium, capped, with a half-life (G5).
- **The world-climbs bench** runs with every balance change (G7).

### The four numbers on the map

Host share of revenue, multiplier, intra-space trade share and local capital share, per settlement and per polity, with uncertainty for anyone else's. They feed host leverage directly: dependency already reads which tiers are imported; it should also read who is paying.

### Events

- **Capacity contract offered**, with a cut scheduled or not.
- **Budget cliff** after a milestone.
- **Second-customer offer:** a minor state wants a seat or a berth, possibly from the rival bloc.
- **Move the board:** a buyout of Earth shareholders and relocation of the company's seat.
- **Land grant:** claims instead of cash for infrastructure.

### What the scenario battler needs

Nothing. The roster can seed battler scenarios (a contested polar claim, an ILRS inspection of an Accords cargo) without any of the economy behind them.

## Open questions

- [ ] How many named actors at the start, and which start as player-selectable?
- [ ] Execution factors per actor: defaults, and whether the player sees rivals' factors or estimates them.
- [ ] Does the host budget model need elections, or is "domestic will" enough?
- [ ] The consumer basket: how many goods it needs for s to be meaningful without becoming a Victoria-style pop simulation.
- [ ] Is moving the board a defiance-ladder rung, or only a visible act the host scores like one?
- [ ] Land grants: how claims around infrastructure are drawn on the surface fields.
- [ ] Should the Antarctica outcome be a stable equilibrium the AI can choose, or only a failure?
- [ ] Guarantee numbers: the cap on one demand engine's share, the sentiment cap and half-life, the share of learning that leaks into the industry pool.
- [ ] The world-climbs bench: its pass rate, its time spans, and which start settings it covers.
- [ ] Auctions: who can bid across bloc lines, and whether a host can block a rival bloc buying a bankrupt company's depot.
- [x] Can the player's company be bought out by an AI? **No (Nov 5).** No takeovers of the player's company; bankruptcy is the failure path, as a reorganisation the player plays through.
- [ ] Bankruptcy's floor: what core the company always keeps (its charter, a headquarters, one installation the player chooses?), and what happens if even that can't be carried.
- [x] Can a host revoke a bankrupt company's charter? **Yes (Nov 5),** and the player may ignore it. Enforcement is physical (deliverable force); the real pressure is unpaid crews.
- [ ] Crew willingness to work: the function of arrears, alternatives, ability to leave, loyalty and temper, per crew group.
- [ ] Scrip: how long belief in company scrip lasts, and what breaks it.
- [ ] Real company stand-ins: names and shapes for the fictional launch champions.

## Sources

Internal: [`design/early-economy-revenue-streams-and-the-growth-loop.md`](early-economy-revenue-streams-and-the-growth-loop.md), [`design/intercept-window-initial-design-notes.md`](intercept-window-initial-design-notes.md), [`design/bases-settlements-and-the-civilian-economy.md`](bases-settlements-and-the-civilian-economy.md), [`design/manufacturing-and-the-dependency-ladder.md`](manufacturing-and-the-dependency-ladder.md), [`studies/interplanetary-bulk-logistics-mines-depots-and-shipyards.md`](../studies/interplanetary-bulk-logistics-mines-depots-and-shipyards.md), [`studies/solar-resources/07-gamification-notes.md`](../studies/solar-resources/07-gamification-notes.md).

Current programmes:

- [cislunarspace.cn, Artemis landers not ready until late 2027](https://cislunarspace.cn/en/space-news/2026/04/2026-04-29-artemis-hls-starship-blue-origin-delay/) (Artemis II flight, lander dates)
- [SpaceNexus, China's lunar programme timeline](https://spacenexus.us/moon/china) (crewed landing, Chang'e-7 and -8, ILRS)
- [NASA, Artemis Accords surpass 75 signatories](https://www.nasa.gov/news-release/nasa-celebrates-as-artemis-accords-surpasses-75-signatories/)
- [ESA, Argonaut: a first European lunar lander](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Argonaut_a_first_European_lunar_lander)
- [SpaceNexus, Commercial space stations: who will replace the ISS](https://spacenexus.us/blog/commercial-space-stations-who-will-replace-iss) (AI-drafted; dates worth checking against primary sources)
- [Pulse, Commercial station builders counter NASA's assessment of the LEO market](https://www.pulse.bot/spacetech/news/commercial-station-builders-counter-nasas-assessment-of-leo-market-a0f932c9-5f48-4973-9707-1018a5c33ea3/)
- [NBC News, Astronauts from India, Poland and Hungary on a privately funded trip](https://www.nbcnews.com/world/europe/astronauts-india-poland-hungary-privately-funded-trip-space-station-rcna214923)

Budgets and procurement:

- [Wikipedia, Budget of NASA](https://en.wikipedia.org/wiki/Budget_of_NASA)
- NASA, [An Assessment of Cost Improvements in the NASA COTS/CRS Program (Zapata)](https://ntrs.nasa.gov/api/citations/20170008895/downloads/20170008895.pdf)

Airmail:

- U.S. Centennial of Flight Commission, [Commercial aviation overview](https://centennialofflight.net/essay/Commercial_Aviation/Tran-OV.htm)
- [Wikipedia, Air Mail scandal](https://en.wikipedia.org/wiki/Air_Mail_scandal)

The gradient and asset survival:

- Metzger (2023), [Economics of In-Space Industry and Competitiveness of Lunar-Derived Rocket Propellant](https://arxiv.org/abs/2303.09011) (advantage by location and year; sensitivity to market size)
- Tom's Hardware, [Iridium: It's Back, Stronger and More Convincing Than Ever (2008)](https://www.tomshardware.com/news/iridium-s-back-stronger-convincing,5032.html) (cost, bankruptcy, the $25M sale, the DoD contract)
- [Wikipedia, Panic of 1893](https://en.wikipedia.org/wiki/Panic_of_1893) (rail mileage in receivership)

History and economics:

- [Wikipedia, Cambridge Agreement](https://en.wikipedia.org/wiki/Cambridge_Agreement); [Charter of the Massachusetts Bay Company](https://en.wikipedia.org/wiki/Charter_of_the_Massachusetts_Bay_Company)
- [Wikipedia, Staples thesis](https://en.wikipedia.org/wiki/Staples_thesis)
- Reason, [Jacobs' Ladder to Prosperity](https://reason.com/1984/12/01/jacobs-ladder-to-prosperity/) (review of Jacobs, *Cities and the Wealth of Nations*, 1984)
- The export-base multiplier is standard regional economics; the worked figures are *(calc)*.
