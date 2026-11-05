# Solar System Resources — Baseline Model

A research-based baseline of **what resources exist where in the solar system, in what concentration, and how hard they are to get out**, including fission feedstock (for Orion-type drives and other uses), fusion fuels and other exotics. Compiled November 2026 from mission data and peer-reviewed literature. Nothing has been moved or invented for gameplay; proposed tweaks live separately in `07-gamification-notes.md`.

## Files

| File | Contents |
|---|---|
| `01-model.md` | The conceptual model: why things are where they are, node schema, confidence scale, cost model, Δv tables, accessibility tiers, frozen knowledge and campaign priors |
| `02-inner-system.md` | Mercury, Venus, Earth (as reference), Moon, Mars, Phobos & Deimos |
| `03-small-bodies.md` | Asteroid classes, NEAs, main belt (Ceres, Vesta, Psyche…), Bennu/Ryugu sample results, Trojans, comets, Kuiper belt, Oort cloud |
| `04-outer-system.md` | Giant planet atmospheres (³He, D), Jovian moons, Saturn's rings, Titan, Enceladus, Uranus/Neptune, Triton, Pluto |
| `05-fissiles-and-exotics.md` | U/Th feedstock geography, fission supply-chain structure, D, ³He, Li, antimatter, xenon, PGMs, REE, N & P |
| `06-summary-tables.md` | Resource → location and location → resource matrices; confidence snapshot |
| `07-gamification-notes.md` | Tensions already present in reality; how former tweaks become campaign draws; decisions and open questions |
| `sources.md` | All sources, grouped by topic |

## Ten takeaways

1. **Abundance is rarely the constraint; concentration, gravity-well depth and processing are.** Most resources exist somewhere in vast amounts at useless grades.
2. **Position sorted the system by volatility.** Inner system: metals and rock, volatile-poor. Outer system: water, nitrogen, carbon, ³He, but no accessible metals or fissiles. That inner/outer split is the system's built-in trade axis.
3. **Differentiation is nature's refinery.** Siderophile metals (Fe, Ni, PGMs, Au) went to cores → metal asteroids. Lithophile incompatibles (U, Th, REE, K, P) went to crusts → Earth's continents, lunar KREEP, Martian crust. Metal asteroids contain essentially no uranium or thorium.
4. **Ore needs water + heat + time.** Only Earth has true ore bodies at scale. Mars is the only other body where they're geologically plausible (unconfirmed).
5. **Fissiles are manufactured, not mined.** Natural uranium is 0.72 % ²³⁵U everywhere in the solar system. Fissile supply = U/Th feedstock × enrichment/breeding/reprocessing capacity — and all that capacity is on Earth.
6. **The Moon is the only off-Earth fissile feedstock in a shallow well**: the large, low-grade Procellarum KREEP Terrane (up to ~7 ppm Th) and small, higher-grade silicic domes — best is farside Compton–Belkovich (~14–26 ppm Th). Earth holds ~7.9 Mt of identified recoverable uranium at ore grades.
7. **Water is plentiful and widely distributed**: lunar poles (~10⁸–6×10⁹ t, baseline ~1 Gt), Mercury's poles (10¹¹–10¹² t), Mars (millions of km³), C-type asteroids (5–20 wt %), Ceres (~2×10²⁰ kg), Saturn's rings (1.5×10¹⁹ kg of near-pure ice), icy-moon oceans.
8. **Nitrogen and phosphorus are the hidden bottlenecks** for life support and agriculture. Best sources: Venus and Titan atmospheres, ammonia-rich C-types (Bennu), Ceres, lunar KREEP, Enceladus.
9. **³He: Moon now (10–20 ppb), ice giants later (~1 000× richer gas, very deep wells).** Deuterium is everywhere water is; comets are ~3× richer.
10. **Drive technology re-weights the whole map.** With chemical rockets Earth is the most expensive place in the inner system to export from; with pulse/fusion drives, gravity wells flatten and gas giants open up.

## Conventions

- Units: SI; t = metric tonne; ppm/ppb by mass unless stated.
- Confidence: **A** in-situ/sample measured · **B** good remote sensing · **C** inferred/modelled · **D** speculative.
- "Derived" = arithmetic on cited figures; "standard value" = textbook constant.
- Knowledge cutoff: 2 November 2026. The game ships before Psyche, MMX's samples or new lunar ground truth arrive, so this baseline is the game's knowledge; uncertain numbers become campaign priors (`01-model.md` §6).
- How this becomes game data (fields, grade–tonnage, yield curves, priors, prospecting, drive demand): [`design/resource-fields-grades-and-yield-curves.md`](../../design/resource-fields-grades-and-yield-curves.md).
- Mass conservation and element groups: [`design/mass-ledger-element-groups-and-conservation.md`](../../design/mass-ledger-element-groups-and-conservation.md).
