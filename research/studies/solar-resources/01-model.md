# 01 — The Model: How Resources Are Distributed and How to Represent Them

This file is the conceptual backbone. The other files are data; this one explains *why* things are where they are, and proposes a representation for the setting/game.

---

## 1. Three rules that explain most of the map

### Rule 1 — The solar system started chemically uniform; position sorted it by volatility

All bodies formed from the same nebula. CI chondrites are the reference for that bulk composition (Lodders et al. 2025). What differs between bodies is mainly **which components condensed where**:

| Zone | What condensed | Result today |
|---|---|---|
| Inside ~2 AU (hot) | Metals, silicates; little water | Rocky planets, S-type asteroids, Moon, Mercury |
| ~2.5–4 AU (snow line region) | + hydrated minerals, some water ice | C-type asteroids, Ceres (≈25 wt% water) |
| Beyond Jupiter | + abundant water ice, ammonia | Icy moons, Trojans (D/P types), Bennu's parent body |
| Beyond Neptune | + CO, N₂, CH₄ ices | Pluto/Triton nitrogen, comets, Kuiper belt |

**Consequence:** volatiles (H, C, N, noble gases) get *more* abundant the further out you go. Refractory metals are everywhere in roughly chondritic proportions — but only concentrated where something concentrated them (Rule 2).

### Rule 2 — Differentiation is the only natural "refinery"

A body that melted separates by Goldschmidt affinity:

| Affinity | Elements (examples) | Goes to | Where you find it concentrated |
|---|---|---|---|
| **Siderophile** (iron-loving) | Fe, Ni, Co, Pt-group, Au, Re | Metal core | M-type asteroids (exposed cores: Psyche, 1986 DA), iron meteorites |
| **Lithophile, incompatible** | U, Th, K, REE, P, Li, Zr | Last melt → crust | Planetary crusts: Earth continents, lunar KREEP, Martian crust, silicic domes |
| **Lithophile, compatible** | Mg, Si, Al, Ca, Ti | Mantle/crust bulk | Everywhere rocky; ilmenite (Ti) in lunar maria |
| **Chalcophile** (sulfur-loving) | Cu, Zn, Pb, Ag, S | Sulfides | Mercury's crust is sulfur-rich; Earth sulfide ores |
| **Atmophile / volatile** | H, C, N, noble gases | Atmospheres, ices | Outer solar system, cold traps, giant planet envelopes |

**Consequence for fissiles:** U and Th are lithophile and incompatible. They are *absent* from metal asteroids, at primordial trace levels (~ppb) in undifferentiated asteroids, and enriched only in the crusts of bodies that melted and fractionated — Earth, Moon, Mars, Venus, Mercury, Vesta.

### Rule 3 — Ore needs water, heat and time; essentially only Earth has had all three at scale

Differentiation gets U/Th to a few ppm. Getting to mineable ore (0.1–20 % U) took Earth's hydrothermal systems, oxidizing groundwater, sedimentary basins and plate tectonics. Off Earth:

- **Mars** had water, volcanism (Tharsis) and impact-driven hydrothermal systems → *plausible* ore bodies, none confirmed. The one place where "prospecting reveals a deposit" is scientifically defensible.
- **Moon** had magmatic fractionation (KREEP, rare granites) but no water → enriched rock, not ore.
- **Venus** may have granitic crust fragments (Venera 8 site) but the surface is 470 °C / 90 bar.
- **Asteroids, icy moons** → primordial or aqueous-altered compositions, no ore-forming plumbing (except brines/salts on Ceres, Bennu's parent body, Enceladus).

**This is the single most important strategic fact in the baseline:** abundance is almost never the constraint. *Concentration*, *position in a gravity well*, and *industrial processing* are.

---

## 2. Node schema (proposed representation)

Represent the system as **resource nodes**. Each node:

| Field | Meaning | Example (Cabeus crater, Moon) |
|---|---|---|
| `host` | Body / region | Moon, south polar PSR |
| `resource` | What | Water ice (+ CO, NH₃, H₂S, CO₂ traces) |
| `form` | Ice / regolith / ore / gas / liquid / metal / brine | Ice mixed in regolith |
| `grade` | Concentration in the mined material | ~5.6 wt% (LCROSS) |
| `inventory` | Mass in the accessible layer | ~1×10⁷ t (estimate) |
| `access_depth` | Layer that counts | Top 1–10 m |
| `export_dv` | Δv from surface to the local hub orbit | ~1.7–1.9 km/s to low lunar orbit |
| `environment` | Hazards: cold, heat, radiation, pressure, dust | 40 K, permanent darkness, abrasive dust |
| `confidence` | A–D (below) | B |

**Confidence scale**

| Code | Meaning |
|---|---|
| **A** | Measured in situ or from returned samples |
| **B** | Remote sensing with good constraints (gamma/neutron spectrometry, radar, gravity) |
| **C** | Inferred/modelled from indirect evidence |
| **D** | Speculative / plausible but undemonstrated |

Confidence is itself a game lever: it sets the width of the campaign prior, and a C/D node can be upgraded or busted by prospecting.

In the game data, `grade` and `inventory` are not single numbers: each node is a grade–tonnage distribution per depth band (lognormal by default), stored on the body's surface grid as background fields, tracts and named features. See [`design/resource-fields-grades-and-yield-curves.md`](../../design/resource-fields-grades-and-yield-curves.md).

---

## 3. Delivered cost: grade × well depth

A simple and defensible cost model:

```
delivered_cost ≈ extraction_cost(grade, environment) × (1 / grade)
              + transport_cost(Δv)
```

- **Grade term.** Mass you must dig/process per kg of product. At 20 ppb He-3 you process 50 000 t of regolith per kg (100 % recovery). At 5.6 wt% lunar ice, ~18 kg of regolith per kg water.
- **Transport term.** Rocket equation: propellant mass ratio = exp(Δv / vₑ).

| Δv (km/s) | Mass ratio at vₑ = 4.4 km/s (H₂/O₂) | at vₑ = 9 km/s (nuclear thermal) | at vₑ = 30+ km/s (pulse/fusion) |
|---|---|---|---|
| 0.5 (small asteroid / Phobos) | 1.12 | 1.06 | ~1.02 |
| 1.9 (Moon surface → LLO) | 1.54 | 1.24 | ~1.07 |
| 4.1 (Mars surface → LMO) | 2.54 | 1.58 | ~1.15 |
| 9.4 (Earth surface → LEO) | 8.5 | 2.84 | ~1.37 |
| ~42 (Jupiter cloud tops → low orbit) | ~14 000 | ~107 | ~4 (at 30 km/s) |

(Arithmetic only; drag/gravity losses ignored.)

The grade term is worked out properly in [`design/resource-fields-grades-and-yield-curves.md`](../../design/resource-fields-grades-and-yield-curves.md): energy per kg of product is a fixed term plus a term in 1/grade, the mine's output per tonne of plant is throughput × grade × recovery, and the yield curve comes from mining the best ground first.

**Reading:** with chemical rockets, Earth is the most expensive place in the inner system to export from. A drive class change (nuclear thermal → pulse/fusion) collapses the map: Mars and Earth become cheap, and gas giants go from impossible to merely hard. **Drive technology level should be a global parameter that re-weights every node.**

---

## 4. Δv reference (approximate, impulsive, chemical, no gravity assists)

| Leg | Δv (km/s) | Note |
|---|---|---|
| Earth surface → LEO | ~9.4 | |
| LEO → Earth escape (C3 = 0) | ~3.2 | |
| LEO → trans-lunar injection | 3.2 | |
| TLI → low lunar orbit | 0.9 | |
| Low lunar orbit → lunar surface | ~1.7–1.9 | |
| Earth escape → most accessible NEAs | 0.8–2.0 | Several thousand known NEAs are cheaper to reach and return from than the lunar surface |
| LEO → Mars transfer | 3.6–4.3 | |
| Mars capture → Deimos transfer orbit | 0.2 | |
| Deimos transfer orbit → Deimos surface | 0.7 | |
| Phobos transfer orbit → Phobos surface | 0.5 | |
| Low Mars orbit → Mars surface | 4.1 | Inbound largely by aerobraking; outbound must be paid |
| LEO → Ceres transfer | ~4.9 | |
| Ceres transfer → low Ceres orbit | ~4.5–4.8 | Plane change dominates |
| LEO → Jupiter transfer | ~6.3 | |
| LEO → Saturn transfer | ~7.3 | |

**Surface-to-orbit cost by body (escape velocity, standard values)** — the "export tax":

| Body | Escape v (km/s) | Body | Escape v (km/s) |
|---|---|---|---|
| Vesta | 0.36 | Europa | 2.0 |
| Ceres | 0.51 | Moon | 2.4 |
| Pluto | 1.2 | Callisto | 2.4 |
| Triton | 1.5 | Titan | 2.6 (thick atmosphere helps landing, hinders ascent) |
| Ganymede | 2.7 | Mercury | 4.3 |
| Mars | 5.0 | Venus | 10.4 (+ 90 bar atmosphere) |
| Earth | 11.2 | Uranus | 21.3 |
| Neptune | 23.5 | Saturn | 35.5 |
| Jupiter | 59.5 | | |

Jovian moons sit deep inside Jupiter's well and radiation belts; Europa in particular is a high-radiation environment. Saturn's moons are much gentler.

---

## 5. Accessibility tiers (for game structure)

| Tier | Region | Typical Δv from LEO | Defining resources |
|---|---|---|---|
| **T0** | Earth | — (but 9.4 km/s to leave) | Everything, at ore grade. Fissiles. Industry. |
| **T1** | Cislunar: Moon, EML points, easy NEAs | 3–6 | Lunar polar ice, regolith metals/oxygen, KREEP thorium, He-3 (low grade), NEA water/metal |
| **T2** | Mars system, inner/middle main belt, Vesta, Psyche | 4–10 | Mars ice/CO₂/Ar, Phobos/Deimos staging, metal asteroids |
| **T3** | Outer belt, Ceres, Hygiea, Jupiter Trojans, Jovian moons | 9–15 | Water, ammonia, salts, carbon |
| **T4** | Saturn system | ~15+ | Ring ice, Titan hydrocarbons & N₂, Enceladus brines, magnetospheric antimatter (trace) |
| **T5** | Uranus, Neptune, Triton, Kuiper belt | very high (transit time dominates) | He-3 from ice giant atmospheres, N₂ ices, deuterium-rich water |
| **T6** | Oort cloud | — | Bulk volatiles; effectively interstellar |

Within any tier, transit time and launch windows matter as much as Δv (Mars windows every ~26 months is a real-world example that shapes logistics).

---

## 6. Knowledge is frozen at late 2026; the truth is a campaign variable

The game ships before the next round of ground truth arrives, so this baseline **is** the game's knowledge. Nothing measured after late 2026 enters the data. Instead, every uncertain number becomes a **prior** whose width comes from its confidence code, each campaign seed draws its own truth, and prospecting narrows each polity's picture. The mechanics are in [`design/resource-fields-grades-and-yield-curves.md`](../../design/resource-fields-grades-and-yield-curves.md).

The game's start state (roughly 2030–2040) decides which draws are already public. Real missions that would have reported by then are drawn at setup and shown to everyone; the rest stay hidden:

| Real mission | Would have measured | In a 2030–2040 start |
|---|---|---|
| MMX (launched 19/20 Oct 2026; Phobos samples to Earth 2031) | Phobos origin: captured primitive body (volatile-bearing) or Mars ejecta (dry) | Drawn at setup, public |
| NASA Psyche orbiter (arrives Aug 2029) | Metal fraction of the largest M-type asteroid | Drawn at setup, public |
| NEO Surveyor (planned launch Sept 2027) | Most NEAs >140 m | Large NEAs mostly known; many 100–300 m bodies still to find |
| Lucy Trojan flybys (from 2027) | Trojan surfaces and densities | Surfaces partly known; interiors not |
| Interlune and other lunar prospecting payloads (late 2020s) | Lunar ³He grade at a few sites | Grade field mostly known; ice per crater mostly not |
| Europa Clipper / JUICE (~2030–2031) | Icy moon shells and surface salts | Partly known |
