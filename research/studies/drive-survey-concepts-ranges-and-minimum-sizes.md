# Intercept Window: Drive Survey – Concepts, Ranges and Minimum Sizes

Nov 2, 2026 · @Teemu · research (Atomic Rockets propulsion survey, first pass)

Eighteen drive concepts cover everything worth having from Atomic Rockets' engine lists, from chemical rockets to antimatter. Each is a **principle** with a smooth band of performance; an engineering project picks one point inside the band its polity can currently reach and freezes it as a drive block. Nothing here is a fixed block copied from a table (the Terra Invicta approach this replaces). The source tables are anchors on the curves, not the curves themselves.

The model is the same three layers as [`design/weapon-blocks-and-engineering-projects.md`](../design/weapon-blocks-and-engineering-projects.md): a physics law, a few engineered numbers that improve from a start value toward a ceiling, and a spec the player asks for. The output fields are the ones [`design/ship-generator-slots-and-physical-model.md`](../design/ship-generator-slots-and-physical-model.md) already reads.

## The short version

- **Variants fold into concepts.** NERVA, Pewee, SNRE, cermet, pebble bed, Timberwind and MITEE are one concept (solid-core NTR) at different points of the same curves: fuel temperature, core power density and floor mass.
- **Every drive block has five things that matter:** exhaust velocity ve, jet power per unit P, unit mass, its waste-heat streams and life. Thrust follows from F = 2P / ve.
- **Waste heat is a list of streams, each with a native temperature,** not one fraction. Radiator area goes as Q / T⁴, so a cold stream costs far more radiator than a hot one of the same power. +100 K on a 600 K loop cuts its radiator area by 46 %.
- **Mass is a floor plus a slope:** m = m₀ + a·(P / 1 GW)^β. The floor m₀ is the minimum-size driver (critical mass, moderator, pusher plate, pulsed-power bank, magnets). A drive below its knee power m₀/a is heavy for its power, never forbidden.
- **Floors fall into four classes.**
  - **None:** chemical, electric thrusters, sails, solar thermal.
  - **About a tonne:** solid-core NTR, set by criticality.
  - **Tens of tonnes:** gas cores, micro-pulse, pulsed fusion.
  - **About 100 t and up:** Orion's pusher plate. Magnetic-confinement fusion has no hard floor, but its mass grows only as √P, so it is terrible small and excellent large.
- **"Capital ships first" falls out of the numbers.** At 1 MW a fusion drive weighs about 2 t per MW of jet power; at 100 GW it weighs about 6.5 kg per MW. Nobody codes a size limit.
- **Ve ceilings are physics; floors and slopes are engineering.** Solid-core NTR stops near 13 km/s because the core melts. Electric drives stop where power-plant mass does. Fusion's ceiling is a few per cent of light speed.
- **Antimatter removes floors.** Catalysed micro-pulse (ICAN-II, 27 t at 12 GW) and antimatter solid core (no critical mass) are what late tech does to minimum sizes.

## Master table

ve in km/s. Specific mass in kg per MW of **jet** power (½ F ve), engine only: no power plant, radiators for the power plant, shadow shield or tanks. "Floor" is the smallest credible unit and what sets it. Basis follows the realism gradient: **D** demonstrated, **S** studied, **P** physics-only.

| # | Concept | Basis | ve (km/s) | Specific mass (kg/MW jet), start → best studied | Floor (smallest unit) | Largest single unit studied | Engine T/W | Waste heat to radiators |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Chemical | D | 1.8–4.6 (ceiling ~5) | 0.8 → 0.4 | None | ~10–15 GW per chamber | 50–150 | ~0 |
| 2 | Electrothermal | D→S | 3–20 | ~700–2,000 (MW-class) | None | ~1 MW per thruster | ~0.01 | (1−η) of input, η 0.3–0.8 |
| 3 | Electrostatic (ion, Hall) | D→S | 15–70 (studied to ~210) | ~8,000–15,000 today → ~2,000 | None (watts) | ~0.1 MW per thruster | ~10⁻³ | (1−η), η 0.55–0.75 (→0.95) |
| 4 | Electromagnetic plasma (MPD, VASIMR, PIT) | D→S | 15–60 (geared 30–300) | ~17,000 (VX-200) → ~500 | Efficiency floor ~0.1 MW per thruster | ~3 GW (physics-only design) | ~10⁻³ | (1−η), η 0.4–0.8 |
| 5 | Mass driver | S | 1–30 | 500–3,200 | Track length v²/2a | ~0.3 GW | ~0.01 | ~10–15 % of input |
| 6 | Solar and beamed thermal | D→S | 7–10 (solar), 20–40 (laser) | engine tiny; mirror dominates | None; scales with collector | Set by mirror or beam | 0.01–4 | Small |
| 7 | Sails (photon, laser, magnetic, electric) | D→S | propellantless | n/a: thrust per kg of sail | None | Area-limited | 10⁻⁴–10⁻² N/kg | None |
| 8 | Solid-core NTR | D→S | 8–10 (H₂), to ~13 | 12 → 0.7 | **~1.2–1.8 t** (criticality, HEU) | 12–14 GW | 2–7 → 20–30 | ~5 % during burn; decay heat after |
| 9 | Liquid / vapor / droplet core NTR | S | 10–20 | 5 → 1.3 | ~1–7 t | ~56 GW | 2–10 | Small; fissile loss in exhaust |
| 10 | Gas core, closed cycle (light bulb) | S | 15–31 | 13 → 0.7 | **~30 t** (gaseous critical mass, 400–1,600 atm) | ~80 GW | 0.4–10 | Wall load, regenerated |
| 11 | Gas core, open cycle | S | 20–50 (MAX ~98) | 97 → 0.8 (MAX 0.1) | **~45 t** (moderator ~36 t) | ~150 GW | 0.04–20 | ~6 %; radioactive exhaust |
| 12 | Nuclear salt-water rocket | S (contested) | 66–80 (90 % HEU: ~4,700, P) | ~0.1 engine, ~1.5 ship | Unstudied below ~0.3 TW | 0.4–30 TW | ~40 | Small; exhaust is a fission plume |
| 13 | Fission fragment | S | 300 (afterburner) to 15,000 | 1,000 → 3.5 | ~9 t (dusty plasma) to ~110 t | ~2.6 GW | 10⁻⁵–10⁻² | ~70 % |
| 14 | External pulse (Orion, Medusa) | S | 18–42 at 100–4,000 t, 118 at 10,000 t; Medusa 490–980 | 4 → 1.5 | **~90–110 t** (10 m pusher plate) | ~24 TW (10,000 t ship) | 1–5 | ~0 |
| 15 | Magnetic-nozzle micro-pulse (Mini-Mag Orion, PuFF, Z-pinch, ICAN) | S | 93–200 (AIM ~600) | 290 → 1.4 | ~30–200 t (pulsed power, coils) | ~150 GW | 0.004–1 | Moderate |
| 16 | Magnetic-confinement fusion (steady) | S→P | 67–350 pure; ~11–14 with afterburner; ceiling ~8,000 | **~2,000 at 1 MW → 65 at 1 GW → 6.5 at 100 GW** | No hard floor; m ∝ √P | ~200 GW (P), TW torches | 10⁻³–10⁻¹ → >1 (P) | D-T ~80 %; D-³He ~25 %; varies with fuel |
| 17 | Pulsed fusion (ICF, MIF, Z-pinch fusion) | S→P | 50–760; plasma-jet MIF to ~9,000 | 1,900 → 0.3 | **~40–250 t** (driver per pulse) | ~130 GW (Thio MTF), TW (P) | 10⁻³–1 | 25 % → <1 % |
| 18 | Antimatter annihilation (solid, gas, plasma, beam core) | P | 11–13 solid; 12–49 gas; 45–7,800 plasma; ~100,000 beam | 2.5 solid; 17–3 plasma | **None from criticality** | Physics-only | ~4 (solid core) | ~⅓ gammas to shields, ~⅓ neutrinos lost |

Notes on the table:

- **Electric rows exclude the power plant**, which usually dominates. Thruster plus PPU alone is 4–10 kg per kWe today. The power block is summarised in "What electric drives need from the power block" below.
- **Rows 14, 16 and 17 are where torchships come from.** Row 12 is the dark horse, row 18 the endgame.
- **Ranges** are taken from the source designs listed under each concept card, with jet power recomputed as ½ F ve wherever a source quoted reactor power instead.

## The block model

### Layer 1: the law

The same few relations hold for every concept:

```latex
P_{\mathrm{jet}} = \tfrac{1}{2} F v_e, \qquad \dot m = \frac{F}{v_e}, \qquad F = \frac{2 P_{\mathrm{jet}}}{v_e}
```

- **Thermal rockets** (chemical, NTR, solar and laser thermal, gas core, antimatter thermal) set ve by temperature and molar mass, ve ∝ √(T / M), plus a bonus from dissociation at low pressure.
- **Electric rockets** pick ve freely; efficiency depends on it, η(ve) = η_max / (1 + (v_L / ve)²), where v_L is the ionisation or frozen-flow loss velocity (about 10–15 km/s for xenon).
- **Nuclear and fusion plasma drives** pick ve between a pure-exhaust maximum and whatever an afterburner (added cold propellant) brings it down to, at roughly constant jet power.

### The mass law: floor, slope and soft ceiling

```latex
m(P) = m_0 + a \left(\frac{P}{1\,\mathrm{GW}}\right)^{\beta} \left[1 + \left(\frac{P}{P_{\max}}\right)^{n}\right]
```

- **m₀, the floor:** everything a unit needs regardless of power. A critical core and reflector, a gas-core moderator, a pusher plate, a capacitor bank. This is the minimum-size driver.
- **a and β, the slope:** β = 1 for nearly everything. Magnetic-confinement fusion fits β ≈ 0.5, because confinement improves with size (the fit is in card 16).
- **P_max, the per-unit ceiling:** nozzle throat heat flux, thrust density, electrode erosion or magnetic-nozzle bell size. The bracket makes going past it steeply heavier rather than forbidden; n ≈ 4 is a placeholder. Beyond P_max the sensible design is a cluster, with its own plume-interaction and failure-mode costs.
- **Knee power P_k = m₀ / a** (for β = 1): the power at which specific mass is twice its large-size value. Below the knee the floor dominates. The Rover-lineage NTR fit gives P_k ≈ 0.3 GW, which is exactly where Borowski placed the SNRE as the "right-sized" engine.
- **Shadow shields, radiators for the power plant, and tanks** are separate parts in the ship generator. Don't fold them into m₀.

### Layer 2: engineered numbers

Each concept card lists its engineered numbers with a start value, a ceiling and a basis tag, exactly as weapon families do. The common ones:

| Number | What it is | Typical lever |
| --- | --- | --- |
| **Ve ceiling parameter** | Fuel or wall temperature (thermal), beam voltage or loss velocity (electric), confinement quality (fusion) | Materials, cooling, magnets |
| **m₀ (floor)** | Mass of the fixed core of one unit | Fuel form, enrichment, compact moderators, pulsed-power density |
| **a (slope)** | Mass per GW above the floor | Power density of the core, magnet field, thruster current density |
| **P_max (per unit)** | Largest unit before the soft ceiling | Nozzle and electrode materials, throat cooling |
| **η or ε** | Jet efficiency (electric) or waste-heat fraction (everything else) | Frozen-flow losses, radiation losses, neutron fraction |
| **Native temperature per heat stream** | Hottest coolant outlet temperature a component tolerates | Materials (creep, corrosion), coolant choice |
| **Life** | Full-power burn hours, restarts, propellant throughput | Erosion, fuel burn-up, cathode wear |

Engineered numbers move by the weapon doc's effort curve: each doubling of cumulative effort closes a fixed share of the remaining gap in orders of magnitude. Most drive numbers span less than a decade (ve, η), so the curve on the gap itself works as well. Specific mass spans two to three decades, so it uses the log form.

### Layer 3: the spec

An engineering project asks for a block:

- **Concept, jet power per unit and a target ve.** Gear-shifting concepts ask for a ve range instead, [ve_low, ve_high], and pay for its width.
- **Propellant** where the concept allows a choice (NTR, mass driver, electrothermal).
- **Options:** afterburner (LANTR, fusion afterburner), bimodal power take-off, enrichment (HEU or LEU), fusion fuel (D-T, D-³He, p-¹¹B, catalysed D-D), antimatter ignition.

The project reports what comes out against the polity's current numbers ("ve 9.4 km/s asked, 9.1 deliverable"), costs it, and freezes a block version. The designer never refuses a spec. A spec beyond P_max or below the knee builds and is reported as heavy.

### What the block hands the ship generator

| Field | Notes |
| --- | --- |
| ve, or [ve_low, ve_high] | Plus a ve multiplier per allowed propellant |
| P_jet per unit, unit mass | From the mass law; thrust and T/W are derived |
| Heat streams | Each: power (share of reference power), native temperature, timing (burn, after shutdown, per pulse, always), and whether it is cold (needs lifting). Sizes the radiator loops; see below |
| Input power (electric only) | P_jet / η, drawn from a power block |
| Propellant | Density, cryogenic flag, hydrogenous flag, corrosive class (oxidising or reducing, for solid cores) |
| Life | Full-power hours, restarts, cool-down flow after shutdown |
| Consumables | Fissile, fusion fuel or antimatter per second |
| Emissions | Neutrons and gammas per MW, exhaust radioactivity, plume temperature. Feeds the shadow shield, detection and inspections |
| Nozzle family | Bell, magnetic nozzle, pusher plate; sets aft geometry |

### Waste heat: streams, each with a native temperature

A waste-heat fraction alone can't size radiators, because radiated power per square metre goes as T⁴. A block hands the ship generator a list of heat streams. Each has a power and the hottest temperature at which it can leave the component (its **native temperature**: the coolant outlet temperature the materials tolerate).

**Why the temperature matters as much as the power.** Radiated power per face at emissivity 0.85:

| Loop temperature | 300 K | 400 K | 600 K | 900 K | 1,200 K | 1,500 K |
| --- | --- | --- | --- | --- | --- | --- |
| kW per m² per face | 0.4 | 1.2 | 6.3 | 32 | 100 | 244 |
| Area left after +100 K | 0.32 | 0.41 | 0.54 | 0.66 | 0.73 | 0.77 |

The second row is the CoaDE effect: +100 K on a 400 K loop more than halves its radiator, while the same 100 K on a 1,500 K loop saves under a quarter. Cold streams are where the radiator mass hides.

**How streams become radiator loops** (contract with [`design/ship-generator-slots-and-physical-model.md`](../design/ship-generator-slots-and-physical-model.md)):

- **Loop temperature:** each stream feeds a loop at T_loop = min(T_native − ΔT_hx, the radiator block's maximum). ΔT_hx is the heat-exchanger drop, a radiator-block number (placeholder 30–100 K).
- **Running cooler is allowed and reported;** running hotter than native needs a heat pump.
- **Streams can share a loop** only at the colder stream's temperature. One shared loop is simpler and has fewer circuits to lose; the report shows the area it costs.
- **Sink temperature** (sunlight, nearby planets) is subtracted: area goes as Q / (εσ(T_loop⁴ − T_sink⁴)). It matters only for cool loops.
- **The radiator block** (panels, wire loops, droplets) brings its own temperature ceiling and coolant. The usable temperature is the lower of drive and radiator, so both technology lines matter.

**Power conversion is a choice, not a native temperature.** A heat engine's efficiency falls as its reject temperature rises, η = f · (1 − T_c / T_h), where f is the fraction of Carnot reached. Radiator area per kWe is smallest at T_c / T_h ≈ 0.75 (an ideal engine) to ≈ 0.78 (an engine at half of Carnot). Example at T_h = 1,200 K and half of Carnot:

| Reject temperature | Conversion efficiency | Relative radiator area per kWe |
| --- | --- | --- |
| 500 K | 29 % | 81 |
| 700 K | 21 % | 33 |
| 900 K | 12.5 % | 22 (near the optimum, ~940 K) |

So the converter block offers its hot-side temperature, and the generator suggests the reject temperature with the lightest radiators. The player may pick another, and the report shows the trade.

**Cold streams need lifting.** Superconducting magnets, cryogenic propellant and electronics produce heat below any useful loop temperature. Lifting it to a 300 K loop costs at least (T_loop − T_cold) / T_cold watts per watt: 2.9 at 77 K, 14 at 20 K, 74 at 4 K. Real cryocoolers are several times worse. That power comes from the power block and its own waste heat joins the loop.

**Native temperature is an engineered number.** It climbs with materials work, like ve. A project may also run a component below its ceiling for longer life; a placeholder life law is life halving every ~50 K above a rated temperature (Larson–Miller-style creep).

**Signatures.** A hotter radiator is smaller for the same power. The total infrared output is unchanged, but the peak moves to shorter wavelengths (Wien: 9.7 µm at 300 K, 3.2 µm at 900 K, 1.9 µm at 1,500 K). This feeds the band choices in [`design/detection-and-the-picture.md`](../design/detection-and-the-picture.md). A smaller radiator is also easier to keep edge-on and cheaper to armour.

#### Heat streams by concept

Shares are of the drive's reference power. Temperatures marked * are placeholders from general engineering knowledge, for the heat-rejection and power studies to replace.

| Concept | Stream | Share | Native temperature | Notes |
| --- | --- | --- | --- | --- |
| Chemical | — | ~0 | — | Regenerative cooling into the propellant |
| Electric thrusters (2–5) | Thruster losses | (1 − η) of input | Thruster body ~600–900 K*; MPD cathode 1,500–2,500 K* | Largely radiated by the thruster itself |
| | Power processing (PPU) | ~3–10 % of input* | ~320–400 K* (electronics) | The costliest heat per watt on the ship |
| | Power plant reject | 2–5× the electric output | Chosen as above: Brayton ~400–600 K*, thermoelectric or thermionic ~800–1,000 K* | Belongs to the power block |
| Solid-core NTR | Nozzle and reflector heating | ~5 % | Carried by the propellant during the burn | Regenerated |
| | Decay heat after shutdown | a few %, falling over hours | Core-hot at first* | Bleed propellant, or a hot loop |
| | Shield heating | ≪1 %* | ~400–600 K* | Steady while burning |
| Gas cores (10, 11) | Wall and moderator cooling | ~6 % (porous wall) | Moderator-limited, ~900–1,000 K* | Transparent wall in the closed cycle |
| Fission fragment | Moderator | most of the reactor's heat | Low* (oil or heavy-water moderators) | Dusty-plasma reactor: a 28 t moderator radiator against a 1 t generator radiator, for the same plant |
| Orion | — | ~0 | — | Plate ablation carries it away |
| Magnetic-confinement fusion | Neutrons into blanket and shield | D-T ~80 %, D-³He ~5 % | ~700–1,000 K*, higher with liquid-metal blankets* | The dominant stream for D-T |
| | Bremsstrahlung and synchrotron on the first wall | D-³He ~20 % | ~1,000–1,500 K* | Shrinks with a hotter first wall |
| | Magnet heat leak | small | 20 K (HTS) or 4 K (LTS) | Lifted at the cryocooler penalty above |
| Pulsed fusion | Driver losses (capacitors, lasers, guns) | large at low gain | ~350–450 K* | Electronics-class temperatures |
| | Nozzle, liner and neutron heating | — | Medium to high* | HOPE MTF carries 22 t of medium-temperature radiators, 21 t of high-temperature ones and a 7 t propellant cryocooler: three streams, three temperatures |
| Antimatter | Gamma heating of target and shields | ~⅓ | Tungsten can run very hot* | Neutrinos (~⅓) need no radiator |
| Ship, not drive | Crew, life support, computers | small | ~290–310 K | Always on, even when cold-coasting |

### Worked example: one concept, three projects

Solid-core NTR, liquid hydrogen. ve = 8.83 km/s × √(T / 2,726 K), fitted to SNRE and Pewee.

| Block | Know-how | Spec | ve | Thrust | Mass | T/W | Real anchor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mk 1 | Rover-era graphite: T 2,750 K, m₀ 1.2 t, a 4.0 t/GW | 0.3 GW | 8.87 km/s | 68 kN | 2.4 t | 2.9 | SNRE: 73 kN, 2.4 t |
| Mk 1 large | same | 1.5 GW | 8.87 km/s | 338 kN | 7.2 t | 4.8 | NERVA-derivative: 334 kN, 10.1 t |
| Mk 4 | particle bed: T 3,100 K, m₀ 0.15 t, a 0.7 t/GW | 2 GW | 9.42 km/s | 425 kN | 1.55 t | 28 | Timberwind 45: 393 kN, 1.5 t, T/W 30 |
| Mk 4 small | same | 0.05 GW | 9.42 km/s | 11 kN | 0.18 t | 5.9 | MITEE: 14 kN, 0.2 t |

The Mk 1 and Mk 4 rows differ only in engineered numbers. Nothing in code knows what "pebble bed" is.

## Concept cards

Each card: what it is, ranges, floor and what sets it, the engineered numbers a project improves, and the anchor designs. Specific masses are kg per MW of jet power unless stated.

### Chemical

#### 1. Chemical rockets

Fuel and propellant are the same mass; energy per kilogram caps ve.

- **ve:** storable hypergolics 3.1–3.3 km/s; RP-1/LOX 3.0–3.5; methalox 3.7; hydrolox 4.4–4.6; H₂/F₂ 4.7. ISRU metal/oxygen 1.8–2.7 (aluminium 2.6, silicon 2.7, iron 1.8). Ceiling: hydrolox ideal ~5.2 km/s (528 s).
- **Specific mass:** 0.4–0.8 kg/MW (RD-253 0.44, F-1 and SSME 0.79). T/W 50–150.
- **Floor:** none. A 4 kg Shuttle RCS thruster runs at 6 MW of jet power.
- **Per unit:** ~10–15 GW per chamber (F-1 11.5 GW, one Shuttle SRB 15 GW). Above that, cluster.
- **Waste heat:** effectively none; regenerative cooling returns it to the propellant.
- **Propellant is the option:** the propellant choice sets ve, density, cryogenic class and storability. Hydrolox boils off; methalox and storables keep.
- **Engineered numbers:** fraction of ideal ve reached (~0.85 → 0.97), engine T/W, restarts and life. Boil-off belongs to tankage.
- **Anchors:** F-1, SSME, RD-253, Raptor, Shuttle RCS, Al/LOX lunar booster.

### Electric (thrusters; power comes from a power block)

#### 2. Electrothermal (resistojet, arcjet, microwave electrothermal)

Electricity heats propellant, which leaves through a nozzle. Cheap, any volatile works, low ve.

- **ve:** resistojet 3 km/s (hydrazine) up to ~10 (tungsten, H₂, studied). Arcjet 5–20 (H₂). MET on water ~10.
- **Efficiency:** resistojet ~0.8, arcjet 0.35–0.52, MET 0.81 (studied).
- **Specific mass:** 60 MWe-class designs at 713 (arcjet), 877 (tungsten resistojet), 2,095 (MET).
- **Floor:** none. **Per unit:** ~0.1–1 MW (a 32-thruster cluster of 100 N arcjets in the source).
- **Engineered numbers:** heater temperature (ve ceiling), η, life.
- **Role:** water- and ammonia-fed tugs and station-keeping; the bridge from ISRU volatiles to electric propulsion.
- **Anchors:** resistojet, ArcJet, MET Steamer, tungsten resistojet, Wakefield e-beam.

#### 3. Electrostatic (gridded ion and Hall)

Ions accelerated by an electric field. Highest efficiency at moderate ve, lowest thrust density.

- **ve:** Hall 15–30 km/s (lab 10–80). Gridded ion 30–70 demonstrated (NSTAR 31, NEXT 41, Herakles 69); studied up to 80–210 (argon ion at 210 km/s, 96 % efficient, in the source table).
- **Efficiency:** Hall 0.56–0.67 (modern up to ~0.75); ion 0.60–0.70+ (studied to 0.95).
- **Thruster + PPU mass, kg per kWe:** XR-5 Hall 2.7 + 2.8; AEPS Hall 3.8 + 4.0; NSTAR 3.6 + 6.4; NEXT-C 2.0 + 5.1; Herakles 1.8 + 2.5. Per MW of jet that is roughly 7–15 t today. MW-class studies reach about 2,100–2,600 kg/MW.
- **Floor:** none; thrusters run from watts.
- **Per unit:** ~0.1 MW. The X3 Hall thruster reached 102 kW and 5.4 N in the lab at 230 kg. Gridded ion is space-charge limited, so big power means big grid area and many units. Hall thrusters have no space-charge limit and are more compact.
- **Life:** NEXT ran 48,000 h and 450 kg of xenon throughput in ground test. Hall life is limited by channel and pole erosion; magnetic shielding helps.
- **Propellants:** xenon, krypton, argon, iodine; studied magnesium, bismuth, cadmium. Argon is about 1,000× cheaper than xenon.
- **Engineered numbers:** η_max and v_L, kg per kWe (thruster and PPU), kg throughput per kW, per-unit power.
- **Anchors:** NSTAR (Dawn), NEXT-C (DART), AEPS (Gateway), X3/XR-100, Starlink argon Hall thrusters.

#### 4. Electromagnetic plasma (MPD, VASIMR, pulsed inductive and plasmoid)

Lorentz force or RF heating plus a magnetic nozzle. Scales to high power per unit and shifts gears.

- **ve:** MPD 15–60 km/s (Stuttgart applied-field 46 km/s at 62 %). VASIMR ~50 km/s demonstrated (about 2 N at 80 kW for 88 h, 2021), and 29–294 km/s by gear at constant power (studied). Plasmoid thrusters 20–500 km/s (studied).
- **Efficiency:** 0.4–0.6 now; studied 0.72–0.79.
- **Thruster + PPU, kg per kWe:** ALPHA2 lithium MPD 0.5 + 1.5 (designed); VASIMR 9.5 + 0.5. MW-class designs come to about 1,700–1,900 kg/MW of jet; the 3 GW HOPE MPD reaches 490.
- **Floor:** an **efficiency floor**, not a mass floor. Self-field MPD needs hundreds of kW per thruster to work well. Model as η(P) = η_max · P / (P + P_c) with P_c ~ 0.1–0.3 MW (placeholder).
- **Per unit:** 0.1–0.2 MW demonstrated (VX-200, a lithium MPD at 120 kW in 2026); MW per thruster studied; GW is physics-only.
- **Life:** cathode erosion above ~100 A/cm² for MPD; electrodeless VASIMR and pulsed inductive designs avoid it.
- **Gears:** VASIMR-type designs trade ve for thrust at constant power. This is the clearest gear-shifter in the electric family.
- **Anchors:** VX-200/VX-200SS, SX3, ALPHA2, HOPE MPD, MPD T-Wave, pulsed plasmoid, ponderomotive VASIMR.

#### 5. Mass driver (reaction engine)

A coilgun throwing pellets of whatever is at hand. The worst specific mass of the electric family, but the propellant is free in the belt.

- **ve:** 1–30 km/s. **Efficiency:** 0.85–0.9.
- **Specific mass:** 500 (30 km/s) to 3,200 (9.8 km/s) kg/MW.
- **Floor:** track length L = ve² / 2a. At 10⁴ m/s² a 10 km/s driver is 5 km long; at 10⁵ m/s² a 30 km/s driver is 4.5 km. Length and accelerator mass, not power, set the minimum size.
- **Propellant:** regolith, slag, ice. Every pellet is also a projectile: an asteroid tug is a gun pointed away from its destination.
- **Anchors:** O'Neill-style mass-driver tugs (two Atomic Rockets entries).

### External power and propellantless

#### 6. Solar and beamed thermal (Solar Moth, laser thermal)

Sunlight or a laser heats propellant through a window or cavity. The power plant stays outside the ship.

- **ve:** solar 7.8–9.8 km/s, materials-limited by the cavity (hafnium carbide, ~1,000 s). Laser thermal with seeded hydrogen plasma 20–40 km/s (studied).
- **Efficiency (beam to jet):** 0.3 (laser thermal) to 0.65 (Solar Moth) to 0.87 (Mirror Steamer).
- **Mass:** the engine is tiny (Solar Moth: 100 kg for 18 MW). The collector dominates: 175 m inflatable mirror for that 18 MW at 1 AU. Collected power falls as 1/r²: 1,361 W/m² at Earth, 44 % of that at Mars, 3.7 % at Jupiter.
- **Floor:** none; scales with mirror area.
- **Engineered numbers:** cavity temperature, mirror areal mass, concentration ratio.
- **Politics:** laser thermal makes the beam station a leverage point; whoever owns the laser owns the ship's thrust.
- **Anchors:** Solar Moth, Mirror Steamer, laser thermal, ablative laser.

#### 7. Sails (photon, laser, magnetic, electric)

No propellant at all. Thrust per area, not per watt.

- **Photon sail:** 9 µN/m² at 1 AU (about 8.2 with real reflectivity), falling as 1/r². Sail-only acceleration a_c ≈ 8.2 / σ mm/s², with σ in g/m².
  - **Areal density:** IKAROS ~10 g/m² (demonstrated); 5 µm Mylar ~7; carbon-fibre 3 (studied); physics-only lattice designs ~0.1, lithium-film limit ~0.02.
  - So a_c goes from ~0.8 mm/s² to ~80 mm/s². A ship whose sail is a third of its mass sees a third of that.
- **Laser sail:** thrust 2P/c, about 6.7 N per GW on a perfect reflector. Needs the beam station (as card 6).
- **Electric sail:** ~0.01 N per kg of tether at 1 AU (300 N from 30 t in the source); thrust falls more slowly with distance than a photon sail's 1/r².
- **Magnetic sail:** ~110 N from 20 t at 1 AU (studied). **M2P2** (plasma-inflated): roughly constant with distance, because the bubble grows as the solar wind thins.
- **Floor:** none. **Limits:** milligee-class accelerations; magnetic and electric sails don't work inside planetary magnetospheres. Atomic Rockets puts the practical minimum for orbit changes near 5 milligees, which photon sails don't reach.
- **Role:** slow freight, probes, pickets that need no propellant resupply.

### Fission thermal

#### 8. Solid-core NTR

A reactor whose coolant is the propellant. Demonstrated in ground tests (Rover/NERVA, 1955–72); the DRACO flight demonstrator was cancelled in 2025, before flight.

- **ve with hydrogen:** 8.0–8.3 km/s demonstrated (825–850 s). Studied 9.2–10.6 (Pewee 9.2, particle bed 9.5, LEU INsTAR 10.6). Low-pressure dissociation 11.9–13.2 at reduced thrust (LPNTR, monatomic MITEE). Ceiling ~13 km/s, near the melting point of carbide fuels.
- **ve law:** ve ≈ 8.83 km/s × √(T / 2,726 K) for H₂. Fuel temperature T goes 2,750 K (Rover) → 3,100 K (particle bed) → ~3,600 K (carbides near melting; the colloid core reaches 11.3–11.8 km/s but loses 20–28 kg of uranium a minute).
- **Other propellants, ve relative to H₂:**

  | Propellant | Ideal (full dissociation) | Corrosion-limited (NASA ISRU study) |
  | --- | --- | --- |
  | Methane | 0.78 | soot clogs the core |
  | Ammonia | 0.63 | 0.39–0.40 (345–360 s) |
  | Water | 0.50 | 0.28–0.35 (250–315 s); SiC cladding survives one flight |
  | CO₂ | 0.41 | oxidising |
  | CO, N₂ | 0.33 | inert |

  At equal reactor power, heavier propellant gives about twice the thrust. Oxidising and reducing propellants need different cladding; a core rated for both is a late engineered number.
- **Mass law fits:**
  - Rover lineage: m₀ ≈ 1.2 t, a ≈ 4.0 t/GW (criticality-limited engine, SNRE, Pewee). Specific mass ~12 kg/MW at 0.15 GW, ~6 at 0.5 GW.
  - Particle bed / MITEE: m₀ ≈ 0.15 t, a ≈ 0.7 t/GW (Timberwind 45, 250 and MITEE). T/W 20–30.
  - Dumbo (folded flow, studied, unbuilt): 0.35 kg/MW, T/W 71.
- **Floor:** criticality. The smallest Rover-derived engine is 33 kN, 145 MW, 1.77 t with 27.5 kg of U-235 at 93 % enrichment. Borowski calls it too small to do much, even in a cluster of three.
  - **Enrichment is a spec option.** HEU gives the lowest floor and the most political attention. LEU (≤ 20 %) needs more moderator and neutron-transparent materials, which raises the floor; the four-concept NASA comparison found LEU cermet may have too little reactivity margin to build at all.
- **Per unit:** 12 GW studied (Timberwind 250), 14 GW (Dumbo); Atomic Rockets' "NTR Solid MAX" is 42 GW.
- **Shadow shield:** ~2 t per engine for a crewed ship at 80 m separation (SNRE). A separate part in the generator.
- **Waste heat:** ~5 % of thermal power is deposited in nozzle and reflector, mostly regenerated into the propellant (vapor-core study: 88 MW of 1,769 MW). After shutdown, decay heat (a few per cent of full power, falling over hours) must be carried off by bleeding propellant or by radiators.
- **Life:** tens of minutes to hours of full-power burn (Pewee 79 min over 4 burns; Russian NPPS 5 h). Atomic Rockets cites about one day of full power before fuel needs reprocessing. Xenon poisoning can block a restart for 1–2 days in moderated designs.
- **Gears and options:**
  - **LANTR:** oxygen injected after the throat. ve 9.2 → 6.3 km/s, thrust ×2.7 (67 → 184 kN).
  - **Bimodal:** a closed Brayton loop makes electricity while coasting (Russian NPPS: 50 kWe for two years; High Frontier's dual-mode design: 60 MWe).
- **Engineered numbers:** fuel temperature, core power density (sets a), floor (fuel form, moderator), life, cladding resistance (propellant classes), restart time.

#### 9. Liquid, vapor and droplet core NTR

The core starts molten or vaporised, so the solid-core temperature limit moves up.

- **ve:** vapor core 9.8–11.8 km/s; colloid core 11.3–11.8; centrifugal liquid core 14.7–17.7; liquid core 16; LARS and droplet core 19.6.
- **Specific mass:** LARS 5.1 kg/MW (1 t at 0.2 GW); vapor core 3.8 (6.8 t at 1.8 GW); droplet core 2.1; liquid core 1.25 (70 t at 56 GW). T/W 2–10.
- **Floor:** ~1–7 t.
- **Penalty:** uranium carried out in the exhaust. Model **fissile retention** as an engineered number; it drives fuel cost, contamination and inspection signatures.
- **Basis:** studied only. A natural mid-game rung between solid core and gas core.

#### 10. Gas core, closed cycle (nuclear light bulb)

A fissioning uranium plasma inside transparent fused-silica walls heats seeded hydrogen by radiation. No fuel leaves the engine.

- **ve:** 15–31 km/s (the full studied range is 10.8–31.4).
- **Specific mass:** 13 kg/MW (early 57 t at 4.5 GW) → 8.6 (NASA light bulb, 32 t at 3.7 GW) → 0.67 (Liberty Ship, seven engines of 54 t at 80 GW each). A small vortex-confined variant runs 131.
- **Floor:** ~30 t, set by the critical mass of gaseous uranium at 400–1,600 atm and the pressure vessel around it.
- **Per unit:** ~80 GW studied (the source range is 0.6–231 GW, 30–300 t).
- **Ve limit:** heat load on the transparent wall. **Engineered numbers:** wall transmissivity and cooling, cavity pressure, floor.
- **Anchors:** NASA/UARL light bulb reports, Liberty Ship.

#### 11. Gas core, open cycle

The uranium plasma is in direct contact with the propellant. Highest-performing fission thermal drive, with a radioactive exhaust.

- **ve:** 20–50 km/s studied (35 km/s first generation, 50 second generation); Atomic Rockets' MAX is 98 km/s.
- **Specific mass:** 97 kg/MW (porous-wall design, 52 t at 0.54 GW) → 18 (193 t at 10.8 GW) → 3.3 (200 t at 61 GW) → 0.8 (coaxial, 127 t at 157 GW) → 0.1 (MAX).
- **Floor:** the porous-wall table gives the cleanest minimum-size curve in the survey: a fixed ~36 t moderator in every size, so m ≈ 45 t + 14 t/GW. T/W rises from 0.04 to 0.23 across that table.
- **Fuel loss:** hydrogen-to-uranium flow ratios of 14–106 in a vortex design, so uranium leaves at 1–7 % of the propellant flow. That is a fissile bill, a fallout plume, and an exhaust that any spectrometer reads as a gas core.
- **Waste heat:** ~6 % to radiators (porous-wall table).
- **Engineered numbers:** fuel retention, cavity pressure, moderator mass, ve ceiling.
- **Politics:** firing near a habitat or planet is an incident; inspection regimes will key on it.

#### 12. Nuclear salt-water rocket (NSWR)

Uranium salt dissolved in water reaches criticality in the exhaust stream: a continuous Orion. Studied (Zubrin, 1991); whether an engine survives it is disputed.

- **ve:** 66 km/s (20 % enriched uranium tetrabromide); 78 km/s (Zubrin's ship). With 90 % enrichment Atomic Rockets lists ~4,700 km/s, which belongs in the physics-only column.
- **Specific mass:** 0.08 kg/MW for the engine (33 t at 426 GW, T/W 40); ~1.5 kg/MW at ship level.
- **Floor:** unstudied below ~0.3 TW. The reaction needs a critical mass in the stream at all times, which suggests a minimum mass flow and so a large minimum power. Treat the floor as a placeholder until someone works it out.
- **Hazards:** the exhaust is a sustained fission plume; fissile consumption is enormous. A planetary-scale incident generator and a strategic drive in one.
- **Engineered numbers:** plenum survival (the contested one), enrichment, salt concentration.

#### 13. Fission fragment

Fission products themselves are the exhaust, steered by magnetic fields.

- **ve:** 5,000–15,000 km/s pure (Werka FFRE 5,170, dusty plasma 15,000). An afterburner adds hydrogen: 314 km/s at 100× the thrust (AFFRE).
- **Specific mass:** Werka 1,020 kg/MW (113 t, 43 N); AFFRE 368; dusty plasma 3.5–55 (9 t at 0.2–2.6 GW).
- **Floor:** ~9 t (dusty plasma) to ~110 t (Werka: reactor plus moderator).
- **Waste heat:** large. AFFRE turns a 2.5 GW reactor into 0.73 GW of jet, so ~70 % goes to radiators.
- **Role:** high-Δv, very low-thrust cargo and deep-space work: the one fission concept with torch-class ve.

### Pulse

#### 14. External pulse (Orion, Medusa)

Nuclear charges detonated behind a pusher plate (Orion) or ahead of a tethered canopy (Medusa). Studied in depth (1958–65), never flown with nuclear units.

- **ve rises with size:**

  | Design | Propulsion module or ship | Pulse unit | ve |
  | --- | --- | --- | --- |
  | NASA 10 m | 91 t module | 141 kg | 18.2 km/s |
  | USAF 10 m | 108 t | 79 kg, 1 kt | 25.8 km/s |
  | NASA 20 m | 358 t module | 450 kg, ~3–5 kt | 30.9 km/s |
  | 4,000 t ship | — | 1,150 kg, 5 kt (vacuum) | 42 km/s |
  | 10,000 t ship | — | 15 kt (vacuum) | 118 km/s |

  Fusion pulse units reach ~73 km/s. Medusa's canopy gives 490–980 km/s (studied).
- **Specific mass:** 4.2 kg/MW (USAF 10 m) → 1.45 (20 m module). T/W 1–5: one of the few non-chemical drives that can lift off.
- **Floor:** ~90–110 t, set by a 10 m pusher plate and shock absorbers, with ve still poor at that size. Orion "improves with size" is literal: bigger plates intercept more of each burst.
- **Pulse units:** each needs a near-critical fissile charge regardless of yield, so small units cost much more fissile per kiloton. Pulse-unit yield and fissile per unit are warhead-block numbers, shared with [`design/weapon-blocks-and-engineering-projects.md`](../design/weapon-blocks-and-engineering-projects.md).
- **Waste heat:** negligible; the plate ablates a thin layer per shot.
- **Engineered numbers:** plate intercept fraction, ve at a given plate diameter, absorber mass, pulse rate. Pulse-unit numbers come from the warhead line.
- **Politics:** every pulse is a nuclear detonation. A pulse-unit factory is a Casaba factory with a different jig.

#### 15. Magnetic-nozzle micro-pulse (Mini-Mag Orion, Z-pinch fission, PuFF, antimatter-catalysed)

Small fissile or fission-fusion targets compressed and ignited inside a magnetic nozzle, without a plate.

- **ve:** 93–157 km/s (Mini-Mag Orion), 157 (Z-pinch microfission), 190 (HOPE Z-pinch), 196 (PuFF), 132 (ICAN-II, antimatter-catalysed), ~600 (AIM, antimatter-catalysed D-³He).
- **Specific mass:** 1.4–4 kg/MW (Mini-Mag Orion, 120–200 t at 30–147 GW); 10 (PuFF, 30 t at 2.9 GW); 26 (HOPE Z-pinch); 290 (Z-pinch microfission, 193 t at 0.67 GW). ICAN-II: 2.3 (27 t at 12 GW).
- **Floor:** ~30–200 t of pulsed power, capacitors and coils. Compression lets each target go critical with far less fissile than an Orion unit.
- **Antimatter ignition** (ACMF/ICAN, AIM) replaces the compression driver with nanograms of antiprotons, which is why ICAN-II reaches 27 t. Make it an option on this concept and on card 17, gated by antimatter supply.
- **Engineered numbers:** driver energy per pulse, target gain, coil field, pulse rate.

### Fusion

Fuel is a spec option on both fusion concepts. It moves where the energy ends up:

| Fuel | MeV per reaction | Into charged particles (thrust) | Into neutrons | Ignition | Exhaust ceiling | Fuel source |
| --- | --- | --- | --- | --- | --- | --- |
| D-T | 17.6 | ~21 % | ~79 % | 5 keV, easiest | 8.7 % c | Tritium bred from lithium (12.3 yr half-life) |
| D-D (catalysed) | ~24 | — | ~40–60 % | ~45 keV | 4.3 % c | Any water |
| D-³He | 18.3 | ~75 % | ~5 % (side reactions) | ~30 keV | 8.9 % c | Lunar regolith (~1 t per 10⁸ t), gas giants |
| p-¹¹B | 8.7 | ~100 % | ~0 (side reactions) | ~200 keV; Lawson ~500× D-T | 4.5 % c | Common |

The waste-heat fraction ε of a fusion block comes mostly from the fuel's neutron and radiation share. D-T is the easiest to burn and the worst to fly: 80 % of the output is neutrons that shields absorb and radiators reject.

#### 16. Magnetic-confinement fusion, steady state (tokamak, mirror, gasdynamic mirror, FRC / Direct Fusion Drive)

A continuously burning plasma, with exhaust bled through a magnetic nozzle.

- **ve:** 67 km/s (D-T tokamak) to 314–347 (D-³He mirror cell, Discovery II), and 1,240–3,050 km/s pure exhaust in gasdynamic mirror studies. With a hydrogen afterburner: 11–14 km/s at 13–250× the thrust. Physics ceiling ~8,000 km/s (Atomic Rockets' MC-Fusion MAX).
- **Specific mass falls with size:**

  | Design | Jet power | Engine mass | kg/MW |
  | --- | --- | --- | --- |
  | Direct Fusion Drive (FRC) | 0.4 MW (1 MW fusion) | 1.4 t | ~3,500 |
  | D-³He mirror cell | 1.7 GW | 107 t | 64 |
  | D-T gasdynamic mirror | 1.35 GW | 101 t | 75 |
  | D-T tokamak | 2.2 GW | 197 t | 88 |
  | MC-Fusion MAX (physics-only) | 200 GW | 0.6 t | 0.003 |

- **Fit:** m ≈ 65 t × √(P / 1 GW), so a = 65 t at β = 0.5 and m₀ ≈ 0. That gives ~2 t at 1 MW (DFD sits right on it), 65 t at 1 GW and 650 t at 100 GW. Specific mass is 2,000 → 65 → 6.5 kg/MW across that span. This is "capital ships first" with no size rule in code.
- **Engineered numbers:** the coefficient a (65 t → ~1 t over the long game; the physics-only anchor implies ~0.04), magnet field (fusion power density rises as the fourth power of field), neutron and radiation fractions by fuel, afterburner range.
- **Per unit:** the magnetic-nozzle bell must keep its walls under a temperature limit, so bell radius grows with √P. At 1 TW and a 3,000 K component limit: D-T needs a 120 m bell, D-D 130 m, D-³He 66 m; active cooling shrinks these 2–3×.
- **Fuel matters for mass too:** a D-³He gasdynamic mirror radiates more power than it produces as thrust, and comes out 30× heavier than the D-T version (3,015 t against 101 t, both 5 cm plasma radius). The fuel option moves a, ε and ve together.
- **Basis:** net-gain fusion in magnetic confinement had not been demonstrated as of this survey. Every number here is studied or physics-only.

#### 17. Pulsed fusion (inertial confinement, magneto-inertial, Z-pinch fusion, plasma-jet MIF)

Fuel pellets or liners compressed and burned one pulse at a time. Power is energy per pulse times pulse rate.

- **ve:** 50 km/s (Slough FDR, lithium liner) to 170 (VISTA), 690–760 (HOPE MTF, Thio MTF). Plasma-jet MIF studies: 1,200–8,900 km/s. MIF "gear shift" from ~50 km/s up to the maximum.
- **Specific mass:** 1,940 kg/MW (D-D laser inertial, 243 t at 0.13 GW); 58 (HOPE MTF, 116 t at 2 GW); 1.6 → 0.3 (Thio MTF, the same 41 t engine at 40 Hz and 200 Hz, 25 → 129 GW). MIF studies quote 10–100 kW/kg (100–10 kg/MW).
- **Floor:** the driver needed for one pulse (capacitors, lasers, plasma guns, theta-pinch coils): ~40–250 t across the studies. Target gain G (50–70 studied) rises with driver energy per pulse.
- **Throttle by pulse rate:** the same hardware covers a wide power range. Slough's engine goes from 2.6 MW to 0.3 GW by cutting the pause between pulses from 180 s to 14 s. So the block has a floor set by pulse energy, and a slope that is mostly radiators, recharge and the nozzle, sized for the maximum rate.
- **Waste heat:** 25 % (HOPE MTF: 493 MW of waste at 2 GW of jet) down to 0.1–1 % in the most optimistic plasma-jet MIF.
- **Engineered numbers:** gain per pulse, driver mass per joule, maximum pulse rate, waste fraction, antimatter ignition option.
- **Basis:** inertial-confinement target gain above 1 has been reached in the laboratory (NIF, 2022), but only with a building-sized laser. Every drive figure here is studied or physics-only.

### Antimatter

#### 18. Antimatter annihilation drives (solid, gas, plasma and beam core)

Annihilation energy heats propellant (solid, gas and plasma cores), or the charged pions are the exhaust (beam core). Physics-only, per the realism rule.

- **ve:** solid core 10.8–12.8 km/s (an NTR with a tungsten target instead of a reactor); liquid core ~19.6; gas core 12–49; plasma core 45–590 (moderate-density studies) and 980–7,840 km/s; beam core ~100,000 km/s (one-third of light speed).
- **Mass:** solid core 7–11 t at 2.7 GW (~2.5–4 kg/MW), T/W ~4. Gas core 95–182 t. Plasma core ~500 t in the source.
- **No criticality floor.** The tungsten target only has to stop the pions and cool; designs range from a 0.33 t core (28 cm cube) to 5 t. Antimatter removes the minimum-size rule that shapes the whole fission branch.
- **Antimatter use:** ~13–15 µg/s for a 2.7 GW solid core. The mass ratio of an optimised antimatter ship never needs to exceed ~4.9, whatever the Δv.
- **Waste:** about a third of annihilation energy is gammas to shields (radiators again), about a third neutrinos, lost.
- **Production, storage and the magazine** come from the antimatter section of the weapon blocks doc; the drive and the weapon share the supply chain.

## What electric drives need from the power block

Electric concepts (2–5) are only as good as the power block behind them. This is a pointer for the power study, not its answer. Figures are kg per kWe of electric output.

| Source | Today (demonstrated or flown) | Studied | Notes |
| --- | --- | --- | --- |
| Solar PV | 10–16 (flexible to rigid) | ~4 thin film with rigging; 1.4 lab CIGS | Falls as 1/r²: ~2× worse at Mars, ~27× at Jupiter |
| RTG | ~200 (6 % efficient) | 60–100 | Single units above ~1 kW are impractical |
| Fission electric | SNAP-10A ~500; Kilopower ~24 unshielded (10 kWe, 236 kg) | Prometheus 40–50 incl. radiators; goal ~10 at 1 MWe; RMBLR 1–2 at 20 MWe | Floor: a critical core (~50 kg HEU minimum per Atomic Rockets) |
| Fission fragment MHD | — | ~0.09 (448 MWe, 38 t; radiators ~75 % of the mass) | Physics-heavy |
| Beamed power receiver | — | ~0.1–1 (laser), <0.1 (microwave) | The power plant stays home |

- **Yardstick:** Jeff Greason's one-month Mars trip needs about 66 km/s of ve and a power supply of ~6 kW/kg (0.17 kg/kWe). Nothing demonstrated is within 50× of that.
- **Waste heat:** practical plants reject 2–5 units of heat per unit of electricity, which is the radiator study's problem.

## Folded, merged and left out

| What | Where it went | Why |
| --- | --- | --- |
| NERVA, Pewee, SNRE, cermet, pebble bed, Timberwind, MITEE, twisted ribbon, INsTAR, Dumbo | Card 8 | Points on one concept's curves |
| LANTR, bimodal NTR | Card 8 options | Afterburner and power take-off |
| Colloid core, centrifugal NTR, LARS | Card 9 | Same principle, different fuel retention |
| Vortex-confined, coaxial, porous wall, hybrid-fuel gas cores | Card 11 | Open-cycle geometries |
| FEEP, colloid electrostatic, radioisotope electrostatic | Card 3 | Same law, different ion source |
| PPT, PIT, helicon, plasmoid | Card 4 | Same law, different coupling |
| Laser ablative, Wakefield e-beam | Cards 6 and 2 | Beamed and electrothermal heating |
| ICAN, ACMF, AIM | Cards 15 and 17, as antimatter ignition | Removes a driver; isn't a separate drive |
| IEC / polywell / fusors | Card 16, low-maturity end | Steady confinement, unproven |
| Metastable chemicals (He*, metallic hydrogen, atomic hydrogen) | Left out; possible physics-only chemical propellant later | Storage unsolved or self-detonating |
| Photon rocket, Epstein drive, reactionless drives | Left out | Fiction, or physics forbids the mass budget |

## Open questions

- [ ] Fit m₀, a and β for every card from the anchors with a small script (the reference script lives with this study); store the anchors as data with source tags.
- [ ] The soft-ceiling exponent n and P_max per concept: placeholder n ≈ 4. Is reliability (failure rate rising past P_max) a better penalty than mass?
- [ ] LEU against HEU floors for solid core: quantify the floor increase from the NASA four-concept comparison and INsTAR.
- [ ] NSWR minimum power: work out the minimum mass flow for a critical stream, or leave it as a stated input.
- [ ] Orion ve against plate diameter as a smooth law: the anchors give 18 → 118 km/s across 10 m to 10,000 t; fit plate intercept fraction.
- [ ] Pulsed fusion: target gain against driver energy per pulse, from the warhead conversion and bursts studies, so drive pulses and warheads share one curve.
- [ ] Afterburner modes as a ve range on the block, or as a second block? Proposal: range on the block, with mixing losses reported.
- [ ] Plume emissions per concept (neutrons, gammas, radioactive exhaust, plume temperature) for the exhaust and plumes study and for inspections.
- [ ] Replace the * temperatures in the heat-stream table with sourced values (heat-rejection and power studies): PPU, Brayton and thermionic reject, gas-core moderator, fusion blanket and first wall.
- [ ] Ship generator: "Radiator temperature" is one design input today. It becomes one temperature per loop, with streams assigned to loops, the shared-loop penalty reported, and the converter reject temperature suggested at the optimum.
- [ ] Heat pumps as a part: lifting a stream above its native temperature to shrink radiators, at a power cost. Worth it for small cold streams on warships with armoured radiators?
- [ ] Which concepts the scenario battler carries: proposal cards 1, 3, 4, 8, 11, 14, 15, 16, 17.

## Sources

- **Atomic Rockets (Project Rho), read in full through the browser on Nov 2, 2026:**
  - [Engine Intro and drive table](https://projectrho.com/public_html/rocket/engineintro.php)
  - [Engine List 1](https://projectrho.com/public_html/rocket/enginelist.php): chemical, beamed and solar thermal, electrothermal, electrostatic, electromagnetic, mass drivers, sails, and the thruster/PPU specific-mass tables
  - [Engine List 2](https://projectrho.com/public_html/rocket/enginelist2.php): every nuclear thermal concept, NSWR, fission fragment
  - [Engine List 3](https://projectrho.com/public_html/rocket/enginelist3.php): antimatter, fusion fuels and engines, Orion, Mini-Mag Orion, Z-pinch, PuFF, Medusa, ICF, MIF, ICAN, AIM
  - [Power Plant](https://projectrho.com/public_html/rocket/power.php) and [Fusion Fuel](https://projectrho.com/public_html/rocket/fusionfuel.php): power-block figures and the fusion fuel table
- **Present-day anchors:**
  - [DRACO (Wikipedia)](https://en.wikipedia.org/wiki/Demonstration_Rocket_for_Agile_Cislunar_Operations): cancelled 2025; ~20 % enriched fuel, >800 s goal
  - [Hall-effect thruster (Wikipedia)](https://en.wikipedia.org/wiki/Hall-effect_thruster): ranges, X3 mass and power, erosion
  - [X3 record test (NextBigFuture)](https://www.nextbigfuture.com/2017/10/x3-ion-thruster-achieves-record-102-kilowatts-of-power-and-5-4-newtons-of-thrust.html): 102 kW, 5.4 N
  - [NEXT ion thruster (Wikipedia)](https://en.wikipedia.org/wiki/NASA_Evolutionary_Xenon_Thruster): 6.9 kW, 48,000 h, 450 kg throughput
  - [Magnetoplasmadynamic thruster (Wikipedia)](https://en.wikipedia.org/wiki/Magnetoplasmadynamic_thruster): ve, efficiency, power, erosion
  - [Ad Astra, VX-200SS 2021 paper](https://www.adastrarocket.com/wp-content/uploads/2021/12/2021_AIAA_ASCEND_VASIMR.pdf): 88 h at 80 kW
  - [Solar sail (Wikipedia)](https://en.wikipedia.org/wiki/Solar_sail): thrust per area, areal densities
- **Internal:** [`design/weapon-blocks-and-engineering-projects.md`](../design/weapon-blocks-and-engineering-projects.md) (three-layer model, effort curve, realism gradient), [`design/ship-generator-slots-and-physical-model.md`](../design/ship-generator-slots-and-physical-model.md) (block fields), [`design/intercept-window-initial-design-notes.md`](../design/intercept-window-initial-design-notes.md) (minimum-size drivers by era), [`studies/research-agenda.md`](research-agenda.md) (propulsion survey).
- **Derived numbers** (jet powers, specific masses, the NTR and fusion fits, the worked example) are computed from the source tables; jet power is ½ F ve throughout.
