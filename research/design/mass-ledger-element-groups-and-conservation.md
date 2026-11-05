# Intercept Window: Mass Ledger – Element Groups and Conservation

Nov 2, 2026 · @Teemu · proposal

Mass is conserved exactly, everywhere, always. Every stock in the game (a field cell, a tailings pile, a tank, a ship's hull, a cargo can, a debris cloud) carries a composition over about twenty element groups, and every process moves mass between stocks without creating or destroying any. Elements are clumped where the clumping doesn't change a decision; the conservation is never clumped.

## The short version

- **One composition vector per stock,** over ~20 element groups. A commodity ("water", "ferrosilicon", "KREEP concentrate") is a named composition, not a separate kind of thing.
- **Every process block is an exact mass balance:** inputs = products + by-products + waste + losses, per group. A block that doesn't close doesn't load.
- **Waste is a stock with a place.** Tailings, slag, vented gas and spent reagents go somewhere: a pile in a cell, the body's atmosphere, space. Tailings keep their composition, so a later polity with better separation can mine them again.
- **Bodies close too.** A body's fields sum to its measured mass. Mining moves mass from the body to stocks; whole-body disassembly is the same ledger run to the end.
- **Exhaust leaves the ledger only into an explicit sink:** heliocentric space (gone), a body's atmosphere, or a debris stock.
- **Nuclear processes book their mass defect.** Fission, fusion, transmutation and annihilation move mass between groups and turn a recorded fraction into energy, so the books still close.
- **Isotopes ride as fractions inside a group:** D in H, ³He in He. How actinides are represented is left open, on purpose.
- **Integers, not floats.** Masses are stored as whole grams in 128-bit integers, so conservation is exact and deterministic, and a bench checks it like the ship generator's mono-check.

## Element groups

Groups are chosen by what decides play (drives, life support, vitamins, armour, the fuel cycle), not by the periodic table. Split a group only when its members differ in **where they are found** or **what they are for**.

| # | Group | Members | Why it stands alone |
| --- | --- | --- | --- |
| 1 | **H** | Hydrogen (D as an isotope fraction) | Propellant, water, fusion fuel; scarce on the Moon |
| 2 | **He** | Helium (³He as an isotope fraction) | Cryogenics, ³He fusion fuel, giant-planet atmospheres |
| 3 | **C** | Carbon | Methane, polymers, steel, life support; scarce in the inner system |
| 4 | **N** | Nitrogen | Life support, buffer gas, fertiliser; the inner-system bottleneck |
| 5 | **O** | Oxygen | Oxidiser, breathing gas; in every rock |
| 6 | **Ar** | Argon | Cheap electric-thruster propellant; Mars and Earth atmospheres |
| 7 | **Kr+Xe** | Krypton, xenon | Premium electric-thruster propellant; Earth monopoly |
| 8 | **Alkali–halogen** | Na, K, Cl, F | Salts and brines; one bin for "salt" |
| 9 | **Mg** | Magnesium | Structural light metal; olivine; a thruster propellant option |
| 10 | **Al** | Aluminium | Structural metal from lunar highlands; Al/O₂ rocket fuel |
| 11 | **Si** | Silicon | Rock bulk, glass, solar cells, ferrosilicon |
| 12 | **Ca+lithophile** | Ca, plus minor lithophiles (Cr, Mn, Sr…) | Rock bulk; concrete and slag chemistry |
| 13 | **Ti** | Titanium | Ilmenite; high-performance structure |
| 14 | **Fe** | Iron | Steel, the structural bulk metal |
| 15 | **Ni+Co** | Nickel, cobalt | Alloying; native metal in M-types; carbonyl refining |
| 16 | **S** | Sulphur | Sulphides, sulphuric acid, chemistry; abundant in chondrites and Mercury |
| 17 | **P** | Phosphorus | Agriculture and life support; the other bottleneck |
| 18 | **Light lithophile** | Li, Be, B | Tritium breeding (Li), p-¹¹B fusion (B), batteries |
| 19 | **Base metals** | Cu, Zn, Pb, Sn, Ag… | Conductors and chemistry; need hydrothermal ore on Earth (or Mars, conf. D) |
| 20 | **Precious** | Pt-group, Au | Catalysts, contacts; native metal in M-types |
| 21 | **REE** | Rare earths, Y, Sc | Magnets, lasers, phosphors; KREEP |
| 22 | **Actinides** | U, Th | Fission feedstock; **representation open** (below) |
| 23 | **Other** | Everything not listed | Closes the balance exactly so no mass falls through a crack |

**Open on purpose: the actinides.** Group 22 holds U and Th as one mass. Whether fissile content is an isotope fraction inside it, a separate group for bred material, or an abstract "fissile unit" outside the ledger is left for the fuel-cycle design. The ledger only promises that whatever is chosen, the mass closes.

## Composition vectors

Every stock is a vector of grams per group, plus isotope fractions where they matter. Two anchors, approximate, to show the shape:

| Group | CI chondrite (wt %, approx., after Lodders) | Iron meteorite metal (wt %, approx.) |
| --- | --- | --- |
| O | 46 | — |
| Fe | 18.6 | ~91 |
| Si | 10.7 | — |
| Mg | 9.6 | — |
| S | 5.4 | trace |
| C | 3.5 | trace |
| H | ~2.0 | — |
| Ni+Co | 1.15 | ~8.5 |
| Ca+lithophile | ~1.4 (Ca, Cr, Mn) | — |
| Al | 0.85 | — |
| Alkali–halogen | ~0.6 | — |
| N | ~0.1–0.3 | — |
| P | 0.1 | trace |
| Ti | 0.05 | — |
| Precious | ~3 ppm | ~11 ppm (PGM ~10, Au ~1) |
| Actinides | ~0.04 ppm | ≈ 0 |

Body classes (lunar mare, highland, KREEP; Martian crust; comet; Titan sea; Saturn ring ice; giant-planet atmosphere) each get a template vector, fitted from the sources in [`studies/solar-resources/`](../studies/solar-resources/). Field cells in [`design/resource-fields-grades-and-yield-curves.md`](resource-fields-grades-and-yield-curves.md) store the host material's vector plus the grade–tonnage distribution of the concentrated mode.

## Process blocks are mass balances

A process block carries a balance matrix: for one unit of throughput, the grams of each group in, and the grams of each group out to each output stream. The loader checks that every group closes.

**Worked example: oxygen from ilmenite** *(calc)*. Hydrogen reduction, with the water split and the hydrogen recycled:

```
FeTiO₃ + H₂ → Fe + TiO₂ + H₂O        H₂O → H₂ + ½ O₂        net: FeTiO₃ → Fe + TiO₂ + ½ O₂
```

| Per tonne of ilmenite | In | Out: O₂ | Out: Fe | Out: TiO₂ | Closes |
| --- | --- | --- | --- | --- | --- |
| Fe | 368 kg | — | 368 kg | — | ✓ |
| Ti | 316 kg | — | — | 316 kg | ✓ |
| O | 316 kg | 105 kg | — | 211 kg | ✓ |

- At 10 % ilmenite in the regolith, that is about **95 kg of regolith per kg of O₂**. The other ~94 kg are tailings: a stock in the cell with the regolith's own composition, minus what was taken.
- **The hydrogen is a reagent, not a product.** The loop's losses (leaks, hydrogen left in the tailings) are an explicit loss stream, which is why a lunar oxygen plant still needs a trickle of imported or polar hydrogen.

## Where mass goes: sinks

| Sink | What lands there | What happens to it |
| --- | --- | --- |
| **Product stocks** | Tanks, ingots, cargo | Ordinary inventory; moves by logistics |
| **Structures** | Hulls, habitats, installations | The mass is in the object; wrecking it makes debris or salvage |
| **Tailings and slag** | Processed host rock | A pile in a cell; takes ground (crowding cost); remineable later |
| **Vented gas** | Leaks, process off-gas, boil-off | To the body's atmosphere if it holds one, otherwise to space; on airless bodies a share may redeposit in cold traps (a setting) |
| **Exhaust** | Propellant expelled by drives | Out of the system's books into heliocentric space; a mass-driver pellet stream is a debris stock instead |
| **Debris** | Wreckage, missed catches, pellets | A debris stock in orbit (the debris-evolution study) until it decays, impacts or is collected |
| **Atmospheric escape** | Gas lost from a body over time | Out of the books; matters for terraforming |
| **Energy** | Mass defect of nuclear processes only | Booked as Δm = E/c² |

Nothing is ever simply deleted. A stock that falls to zero has gone somewhere named.

## Nuclear processes book their mass defect

Chemistry conserves mass to well below any game precision. Nuclear processes don't, so they book the difference *(calc)*:

| Process | Mass converted to energy |
| --- | --- |
| Fission of ²³⁵U (~200 MeV) | ~0.09 % of the fissioned mass |
| D-T fusion (17.6 MeV) | ~0.38 % |
| Catalysed D-D (43.2 MeV per 6 D) | ~0.38 % |
| Annihilation | 100 % of the annihilating pair |

- **Fission moves mass between groups:** actinides become fission products, booked to the groups where those elements belong (mostly "Other", REE and base metals).
- **Fusion moves H (deuterium, tritium) and He (³He) into He,** plus neutrons, which are booked to whatever absorbs them.
- **Transmutation by neutron capture** moves mass one group at a time, as in the manufacturing note's limits section.

## Strictness in code

- **Grams in Int128.** .NET has 128-bit integers; ±1.7×10³⁸ g covers the Sun's mass 10⁵ times over, so every stock from a gram of xenon to a whole planet fits one type and adds exactly.
- **Grades are doubles; transfers are integers.** A fractional split is rounded group by group with the remainder carried (largest-remainder method), so outputs always sum to inputs to the gram.
- **Deterministic:** integer sums are order-independent, which suits the chunked, seeded workers in the Fleetwright principles.
- **The mass-check bench:** run every process block, every ship build and every logistics leg on random inputs and assert closure per group. A failure names the block. It sits beside `mono-check`.
- **Routine-tier rates stay exact:** a mine's monthly output is integer grams computed from a rate, with the fractional gram carried to the next re-anchoring.

## Ties to the rest of the design

- **Manufacturing:** a bill of processes is a chain of balances, so closure by mass is computed from the same numbers that conserve it. Vitamins are small masses in specific groups (REE, precious, base metals, actinides).
- **Resources:** field cells hold the dispersed mode as the host composition vector; universal separation takes from any group at an energy per kg of host rock.
- **Logistics:** propellant burned is mass leaving to a sink; the rocket equation and the ledger agree by construction.
- **Combat and debris:** a destroyed ship's mass becomes debris and vapour stocks, never nothing; the debris shotgun of the envelopes is the same mass.
- **Terraforming:** atmospheres are composition vectors too, with escape and freeze-out as sinks; the nitrogen buffer Mars lacks is a number in group 4.

## Open questions

- [ ] Actinide representation (group 22): isotope fraction, a bred-fissile group, or an abstract unit outside the ledger.
- [ ] Final group list: is 23 the right size, and do any groups need splitting (Cr out of Ca+lithophile for stainless steel? Cu out of base metals for conductors?).
- [ ] Template vectors per body class, fitted from the resource baseline.
- [ ] Vented gas on airless bodies: share lost to space against share redeposited in cold traps.
- [ ] Neutrons and activation: booked to the absorbing stock's groups, or ignored below a threshold (it would be the only threshold in the ledger)?

## Sources

- Internal: [`design/resource-fields-grades-and-yield-curves.md`](resource-fields-grades-and-yield-curves.md), [`design/manufacturing-and-the-dependency-ladder.md`](manufacturing-and-the-dependency-ladder.md), [`studies/interplanetary-bulk-logistics-mines-depots-and-shipyards.md`](../studies/interplanetary-bulk-logistics-mines-depots-and-shipyards.md), [`design/fleetwright-principles-for-intercept-window.md`](fleetwright-principles-for-intercept-window.md), [`studies/solar-resources/`](../studies/solar-resources/).
- CI chondrite composition after Lodders, Bergemann and Palme (2025), [Solar System Elemental Abundances from the Solar Photosphere and CI-Chondrites](https://arxiv.org/pdf/2502.10575), rounded; iron meteorite metal from Ostro et al. (1991) as cited in [`studies/solar-resources/03-small-bodies.md`](../studies/solar-resources/03-small-bodies.md).
- *(calc)* marks figures computed here: ilmenite stoichiometry from atomic masses; mass defects from reaction energies and 931.5 MeV per atomic mass unit.
