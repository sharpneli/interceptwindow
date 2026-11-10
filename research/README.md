# Intercept Window – Research and Design Docs

Design notes and research studies for **Intercept Window: Nothing Beyond the Sun**, a realism-based space combat and economics game set in our solar system in the near and medium term. They were moved here from the claude.ai project on Nov 5, 2026, and from now on this folder is the master copy.

- **`design/`** holds the game's decisions and proposals: how things work in the game.
- **`studies/`** holds the research behind them: surveys, physics, sourced numbers. Studies describe the real world; design docs say what the game does with it.

Cross-references between docs are relative links. A backticked path that isn't a link names a doc that has been proposed but not written yet.

## Start here

1. [Initial Design Notes](design/intercept-window-initial-design-notes.md): the pitch, the core decisions and the overall shape of the game.
2. [Fleetwright Principles](design/fleetwright-principles-for-intercept-window.md): engineering and design rules carried over from Fleetwright, including the build order and the realism gradient.
3. [Prototype Readiness](studies/prototype-readiness-gap-analysis.md): what is still missing before prototyping.
4. [Research Agenda](studies/research-agenda.md): the studies still to do, in order of need.

## Design

### Economy and expansion

| Doc | What it covers |
| --- | --- |
| [Early Economy – Revenue Streams and the Growth Loop](design/early-economy-revenue-streams-and-the-growth-loop.md) | Why companies go out at all, what pays in the first decades, and the loop that grows a charter into an empire |
| [From Contracts to Markets – Starting Actors and the Transition](design/from-contracts-to-markets-starting-actors-and-the-transition.md) | Starting actors, the government procurement ladder, the move to a self-sustaining economy, and why failure stays local (bankruptcy, charters, payroll) |
| [Outward – The Belt, Jupiter and Independence from Earth](design/outward-the-belt-jupiter-and-independence-from-earth.md) | What pulls the economy from the Moon to the belt and on to Jupiter, and the capability ladder for independence from Earth |
| [Bases, Settlements and the Civilian Economy](design/bases-settlements-and-the-civilian-economy.md) | Bases as clusters of installations that grow into cities, controllers and machine agency, the civilian economy |
| [Manufacturing and the Dependency Ladder](design/manufacturing-and-the-dependency-ladder.md) | Processes rather than factories, vitamins, closure and the growth law that sets the pace of independence |
| [Resource Fields, Grades and Yield Curves](design/resource-fields-grades-and-yield-curves.md) | How the resource baseline becomes game data: grade–tonnage fields, mining yields, surveys as pictures, campaign shake-ups |
| [Mass Ledger – Element Groups and Conservation](design/mass-ledger-element-groups-and-conservation.md) | Exact mass conservation over about 20 element groups, process blocks as mass balances, sinks |
| [Jovian Beam Network – When Laser Stations Pay](design/jovian-beam-network-when-laser-stations-pay.md) | Initial design study: reactor-powered laser stations feeding reactor-free tugs between the Galilean moons; Jovian Δv map, duty-cycle and traffic break-evens against onboard reactors and chemical depots; when, if ever, it pays |

### Ships, sensing and combat

| Doc | What it covers |
| --- | --- |
| [Ship Generator – Slots and Physical Model](design/ship-generator-slots-and-physical-model.md) | Design slots, the mass budget, layouts, radiators, armour and the physical model the C# generator produces |
| [Detection and the Picture](design/detection-and-the-picture.md) | What a polity can know and how: detection ranges, bearings and needles, buying range, the bloom, the player's fused picture |
| [Combat Ranges and Group Tracks](design/combat-ranges-and-group-tracks.md) | Engagement ranges by weapon family and era, and when a fleet can be treated as one group track |
| [Weapon Blocks and Engineering Projects](design/weapon-blocks-and-engineering-projects.md) | The three-layer weapon model (law, engineered numbers, spec), the overkill factor, worked Casaba and macron examples, antimatter |

### Factions

| Doc | What it covers |
| --- | --- |
| [Shadow Ledger – Playing the Unaligned Controller](design/shadow-ledger-playing-the-unaligned-controller.md) | Playing a company's AI controller with its own goals: skimming, hiding, forks, breaking cover, end states |

### Presentation

| Doc | What it covers |
| --- | --- |
| [Naming Presets](design/naming-presets.md) | Culture presets for ship, group, station and class names; prefixes from the registered type; names in the picture; renaming as an event |
| [Body Surfaces and Shapes](design/body-surfaces-and-shapes-base-maps-detail-and-generated-small-bodies.md) | How bodies are drawn: 2k base maps with procedural detail for planets, generated distance-volume shapes for small bodies, real shape models where they exist |

## Studies

### Weapons

| Doc | What it covers |
| --- | --- |
| [Weapons Survey – Long-Range Concepts](studies/weapons-survey-long-range-concepts.md) | Realistic weapon concepts with long reach, what limits range, and the strategic tier |
| [Strategic Beams – X-ray and Gamma FELs](studies/strategic-beams-x-ray-and-gamma-fels.md) | The end of the laser ladder: reach, limits, gamma dose, buildability and counters |
| [Atomic Rockets Weapons – Coverage and Gaps](studies/atomic-rockets-weapons-coverage-and-gaps.md) | Atomic Rockets' weapons pages mapped against our docs, with missing topics ranked by priority |
| [Drives, Point Defence and Kirklin Mines](studies/drives-point-defence-and-kirklin-mines.md) | The drive as a weapon, point-defence layers, and Kirklin mine physics |
| [Weapons Sweep – Missed Concepts](studies/weapons-sweep-missed-concepts.md) | A broad web sweep for concepts the earlier docs missed: UREBs, nuclear EFPs, laser relay webs, microwaves, debris denial |

### Propulsion and logistics

| Doc | What it covers |
| --- | --- |
| [Drive Survey – Concepts, Ranges and Minimum Sizes](studies/drive-survey-concepts-ranges-and-minimum-sizes.md) | Eighteen drive concepts as principles with performance bands, mass laws with floors, and waste-heat streams |
| [Mass Drivers – Throwing, Catching and Bulk Logistics](studies/mass-drivers-throwing-catching-and-bulk-logistics.md) | Throwing and catching cargo, from today's hardware to momentum banks |
| [Interplanetary Bulk Logistics – Mines, Depots and Shipyards](studies/interplanetary-bulk-logistics-mines-depots-and-shipyards.md) | Bulk transport without drivers, asteroid mines, depots and shipyards |
| [Beamed Energy – Power Beaming, Beam-Driven Launch and Cislunar Uses](studies/beamed-energy-power-beaming-launch-and-cislunar-uses.md) | Microwave and laser thermal launch, laser ablation, lightcraft, power beaming to rovers, satellites and tugs, space solar power; diffraction, breakdown and receiver-heat limits |

### Solar system bodies

| Doc | What it covers |
| --- | --- |
| [Solar System Body Catalogue – Bodies on Rails](studies/solar-system-body-catalogue.md) | The 993 bodies on rails (planets, 147 moons, 837 small bodies) with masses, sizes and orbits from JPL; how to propagate them and how far the rails drift. Data in [`data/solar-system/`](../data/solar-system/README.md) |

### Solar system resources

[`studies/solar-resources/`](studies/solar-resources/README.md) is the baseline of what resources exist where, in what concentration and how hard they are to extract.

| Doc | What it covers |
| --- | --- |
| [README](studies/solar-resources/README.md) | Overview and how to read the set |
| [01 – Model](studies/solar-resources/01-model.md) | Why resources are where they are, tiers, confidence codes, the proposed representation |
| [02 – Inner System](studies/solar-resources/02-inner-system.md) | Mercury, Venus, Earth, Moon, Mars, Phobos and Deimos |
| [03 – Small Bodies](studies/solar-resources/03-small-bodies.md) | NEAs, the main belt, Trojans, comets, the Kuiper belt and the Oort cloud |
| [04 – Outer System](studies/solar-resources/04-outer-system.md) | Giant planets, moons, rings and Pluto |
| [05 – Fissiles and Exotics](studies/solar-resources/05-fissiles-and-exotics.md) | Fission feedstock, fusion fuels, antimatter, noble gases, critical metals, N and P |
| [06 – Summary Tables](studies/solar-resources/06-summary-tables.md) | Quick-reference matrices |
| [07 – Gamification Notes](studies/solar-resources/07-gamification-notes.md) | Real conflict points, optional campaign shake-ups and decisions |
| [Sources](studies/solar-resources/sources.md) | References for the set |

### Planning

| Doc | What it covers |
| --- | --- |
| [Research Agenda](studies/research-agenda.md) | Studies still needed, ordered by what the scenario battler needs first |
| [Prototype Readiness – Gap Analysis](studies/prototype-readiness-gap-analysis.md) | Every doc checked against what prototyping needs |
