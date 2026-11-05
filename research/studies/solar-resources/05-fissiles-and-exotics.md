# 05 — Fissiles and Exotics

Covers: fission feedstock (U, Th), fusion fuels (D, ³He, Li), antimatter, noble gases for electric propulsion, precious/critical metals, and the life-support bottlenecks (N, P).

This file stays at the level of **geography, grades and supply-chain structure**. It deliberately does not go into device or weapon physics; for game purposes, fissile demand (e.g. per Orion pulse unit) should be an abstract number set by the design, not derived from engineering.

---

## 1. Fission: the facts that shape the map

1. **Only one fissile nuclide occurs naturally in quantity: ²³⁵U**, at ~0.72 % of natural uranium. Because all solar-system bodies formed together and ²³⁵U decays at the same rate everywhere, **the isotope ratio is essentially the same everywhere** (Earth's Oklo natural reactor is the famous local exception, and it is *depleted*). There is no "rich isotope" location anywhere — only places with more or less uranium.
2. **Fertile material** — ²³⁸U and ²³²Th — can be converted into fissile material only by neutron irradiation in a reactor followed by chemical separation. Plutonium does not occur naturally in useful amounts.
3. Therefore: **fissile supply = feedstock × processing capacity.** Feedstock (U/Th-bearing rock) exists on several bodies at low grade; processing (enrichment plants, breeder reactors, reprocessing) exists only on Earth. At lunar grades, the ²³⁵U content of rock is ~0.01 ppm, so off-Earth fissile production would favour **breeding** (thorium or uranium) over enrichment.

**Consequence for Orion-style drives and weapons:** the strategic chokepoint is not ore, it's **industrial plant**. Whoever holds enrichment/breeding/reprocessing capacity controls fissile supply, regardless of who holds the rock. Off Earth, the Moon is the only place with both meaningful feedstock and a shallow well.

### Abstract supply chain (game-level)

```
U/Th-bearing rock ──► Concentrate ──► [Enrichment]  ──────────────► Fissile stock ──► Fabricated units
   (mine/beneficiate)   (chem plant)   [Reactor + reprocessing]  ─┘   (safeguarded)      (pulse units, fuel, …)
```

Every arrow is a facility; every facility is a node that can be built, taxed, inspected, blockaded or attacked. Keep conversion ratios abstract (e.g. "X tonnes of KREEP concentrate per fissile unit") and tune for gameplay.

---

## 2. Where the U/Th feedstock is

| Location | Th | U | Form | Accessibility | Conf. |
|---|---|---|---|---|---|
| **Earth — ore deposits** | (Australia ~1.39 Mt Th identified) | **~7.9 Mt identified recoverable**; ~5.9 Mt < USD 130/kg; ~7.9 Mt more undiscovered; ~57 Mt unconventional | Ore: 0.1 % to >10 % U | Deep well (9.4 km/s), all industry is here | A |
| Earth — continental crust | ~10 ppm | ~1–4 ppm | Granite, etc. | Not ore | A |
| Earth — seawater | — | ~3.3 ppb → ~4.5×10⁹ t total | Dissolved | Enormous, very dilute | A |
| **Moon — Compton–Belkovich** (farside) | **14–26 ppm** (earlier est. 40–55 ppm in the core) | ~0.27 × Th | Silicic volcanic rock | Shallow well; farside (no direct Earth line-of-sight) | B |
| **Moon — silicic domes in the PKT** (Gruithuisen, Hansteen Alpha, Mairan, Lassell) | Granitic samples 20–65 ppm | ~0.27 × Th | Granite/felsite | Shallow well; nearside | B |
| **Moon — Procellarum KREEP Terrane** | up to ~7 ppm (avg few ppm) | up to ~2 ppm | Regolith/breccia | Huge area; nearside | B |
| Moon — highlands | ~1 ppm or less | ~0.3 ppm | | | B |
| **Venus — Venera 8 site** | 6.5 ppm | 2.2 ppm | Granitoid-like? | Practically inaccessible | A (low precision) |
| Venus — lowland basalts | 1.5–2 ppm | ~0.65 ppm | Basalt | Inaccessible | A (low precision) |
| **Mars — crust** | 0.2–1 ppm (avg 0.6) | (K/Th ≈ 5 300; U not well mapped) | Basalt, sediments | 5 km/s escape | B |
| Mars — hypothetical hydrothermal / LIP / impact ores | ? | ? | Vein / roll-front / impact-related | — | **D** |
| Mercury | 0.22 ppm | 0.09 ppm | Surface | Deep solar well | B |
| Vesta (HED basalts) | few tenths ppm (order of magnitude) | lower | Basalt | 0.36 km/s escape | C |
| Chondritic asteroids | ~0.03 ppm | ~0.01 ppm | Primordial | Easy | A |
| Metal asteroids | ≈ 0 | ≈ 0 | — | — | A |
| Icy moons, comets, KBOs | Chondritic in rock fraction, buried under ice | | | | C |

### Ranking (baseline)

1. **Earth** — ore-grade, industrialized, deep well. Effective monopoly today.
2. **Moon** — only off-Earth feedstock worth discussing: large low-grade PKT + small high-grade silicic domes (Compton–Belkovich is the single best off-Earth thorium site known).
3. **Mars** — low bulk grade, but the **only off-Earth body where real ore deposits are geologically plausible.** The best "undiscovered deposit" candidate.
4. Venus — evolved crust may exist; surface conditions make it a long-term reserve at best.
5. Everything else — negligible.

---

## 3. Fusion fuels

### Deuterium (D)

| Source | D/H | Notes |
|---|---|---|
| Earth's oceans | 1.56×10⁻⁴ | ~5×10¹³ t of D (derived) — effectively unlimited |
| Comet 67P (Jupiter-family) | 5.3×10⁻⁴ (3.4× Earth) | Richest common natural source per kg of water |
| Oort cloud comets | ~2× Earth | |
| Enceladus plume | above Earth's | |
| Saturn's rings, most icy moons | ≈ Earth | |
| Phoebe | highest measured in the solar system | Small, captured |
| Giant planet H₂ | ~2×10⁻⁵ (Jupiter/Saturn); somewhat higher for Uranus/Neptune | Lower than water sources |

**Model note:** deuterium is **everywhere there is water**; what matters is having an isotope-separation plant. Comet ice gives a ~3× head start. Not a scarcity resource — a processing resource.

### Helium-3

| Source | Grade | Inventory | Practicality |
|---|---|---|---|
| Earth — atmosphere | ~7 ppt of air | ~37 000 t | Not extractable economically |
| Earth — tritium decay (from weapons/reactor programs) | — | small (kg per year scale) | Current real supply |
| **Moon — high-Ti mature mare regolith** | ~10–20 ppb | > 1 Mt (whole Moon, estimate) | ~50 000 t regolith per kg; near-term commercial target (Interlune, 2030s) |
| Mercury | Solar-wind implanted; similar processes | unknown | Deep well, hot |
| **Uranus / Neptune atmospheres** | ³He mass fraction ~1.5–1.9×10⁻⁵ | effectively unlimited | ~1 000× better grade than the Moon; needs nuclear propulsion |
| Saturn atmosphere | lower He fraction, protosolar-like ratio | effectively unlimited | Middle ground |
| Jupiter atmosphere | ³He/⁴He ~1–1.7×10⁻⁴ | effectively unlimited | Worst well + radiation |

**Model note:** ³He is the textbook "Moon now, ice giants later" resource. Near-term demand is cryogenics/quantum computing and neutron detection, not fusion.

### Lithium (for D–T fusion via tritium breeding; also batteries)

Lithophile → concentrated in planetary crusts and brines. Earth (salars, pegmatites, seawater) is overwhelmingly the best source. Chondrites carry only ~ppm Li. Off Earth, KREEP-like evolved crust and Martian evaporites are the plausible candidates (conf. C/D).

---

## 4. Antimatter

| Item | Value | Conf. |
|---|---|---|
| Earth's trapped antiproton belt (inner Van Allen belt; detected by PAMELA) | **~160 ng** (Bickford estimate); other integrations give only a few ng | B/C |
| Replenishment | ~2 ng/yr (estimate) | C |
| Energy content | ~10 kWh for 160 ng | — |
| Best natural trap | Saturn's magnetosphere (ring–cosmic-ray interactions), per Bickford | C/D |
| Proposed use scale | ~10 µg of antiprotons proposed for a 100-t, one-year Jupiter round trip (catalysed/hybrid propulsion concept) | D |

**Model note:** natural antimatter is a **catalyst-scale resource** (nanograms to micrograms), never bulk fuel. In a setting, it fits as a rare, magnetically-harvested trigger/catalyst for advanced drives, with Saturn as the premium source and Earth's belt as a tiny, contested local supply.

---

## 5. Noble gases for electric propulsion (an underrated bottleneck)

| Gas | Best sources | Notes |
|---|---|---|
| Xenon | Earth's atmosphere (~0.09 ppm by volume, standard value) | **Very scarce everywhere**; the preferred ion-thruster propellant |
| Krypton | Earth's atmosphere (~1 ppm) | Cheaper Xe substitute |
| Argon | Earth's atmosphere (~0.93 %); **Mars atmosphere (~2 %)** | Abundant; lower-performance propellant |

**Model note:** if the setting uses ion/Hall thrusters widely, **xenon becomes an Earth-monopoly good** exported up the well, and Mars becomes the off-Earth argon supplier. Easy, realistic tension.

---

## 6. Precious and critical metals

| Resource | Best sources | Grade | Notes |
|---|---|---|---|
| **PGMs (Pt, Pd, Ir, Os, Ru, Rh), Au** | M-type asteroids (1986 DA, Psyche, others), metal grains in S-types | ~10 ppm PGMs, ~1 ppm Au in iron-meteorite metal | Orders of magnitude richer than average crust, comparable to good terrestrial ore; **no rock to dig through — metal is the ore** |
| Ni, Co | M-types (~8 % Ni), S-type metal grains | % level | |
| Fe | Everywhere: M-types, S-types, lunar regolith metal and ilmenite, Martian hematite | | Structural metal never scarce in space |
| Ti | Lunar high-Ti maria (ilmenite) | % level | |
| Al | Lunar highlands (anorthosite) | High | Energy-intensive to refine |
| **REE** | Lunar KREEP (urKREEP ~1 200 ppm total REE; Nd ~180 ppm, Dy ~65 ppm) | | C-type asteroids are ~25–500× poorer in Nd/Dy |
| Cu, Zn, Pb, Ag | Earth ores; Mercury's sulfur-rich crust (?); Mars hydrothermal (?) | | Chalcophile ores need hydrothermal systems → Earth (A), Mars (D) |

---

## 7. Life-support bottlenecks: nitrogen and phosphorus

Hydrogen and oxygen are easy (water ice, oxide rock). Carbon is moderate (CO₂ on Mars, C-types, comets, Titan). **Nitrogen and phosphorus are the hard ones** for any off-Earth biosphere.

| Element | Inner system sources | Outer system sources |
|---|---|---|
| **N** | Earth atmosphere; **Venus atmosphere (~4× Earth's N₂)**; Mars atmosphere (~2–3 %, thin); Bennu-type C-types (ammonia-rich); Ceres (ammoniated clays); lunar polar ice (NH₃ traces) | **Titan atmosphere**; Triton & Pluto N₂ ice; comets (N-depleted but present) |
| **P** | Earth; lunar KREEP (phosphates); Bennu-type C-types (phosphate salts); chondritic phosphates | **Enceladus ocean (≥100× Earth-ocean phosphate)** |

**Model note:** a self-sufficient off-Earth agriculture economy needs an N source *and* a P source. In the inner system that means Venus/Mars atmospheres + C-type asteroids + KREEP. This "fertilizer geography" is a quiet but powerful driver of settlement patterns.
