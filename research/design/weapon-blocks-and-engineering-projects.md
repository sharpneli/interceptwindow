# Intercept Window: Weapon Blocks and Engineering Projects

Nov 2, 2026 · @Teemu · proposal

How a weapon goes from "the principle is known" to "we have one" to "we have a thousand of them and they are absurd". Each weapon family gets the same three-layer model: a physics law that never changes, engineered numbers that improve with projects and experience, and a spec the player picks. Nothing caps the spec. Overkill falls out of the arithmetic; cost, heat, fuel, visibility and politics are what push back.

The tone target is Charles Stross's *Accelerando*: early decades where a better shaped charge takes a test programme and a political crisis, and a late game where machine polities iterate weapon blocks faster than human committees can read the reports. There are two worked examples: the nuclear shaped charge (Casaba-Howitzer) and macron accelerators with payloads. Antimatter gets its own physics-only endgame section, and the other families get one-page sketches.

Physics and first-cut numbers come from [`studies/weapons-survey-long-range-concepts.md`](../studies/weapons-survey-long-range-concepts.md) and [`studies/strategic-beams-x-ray-and-gamma-fels.md`](../studies/strategic-beams-x-ray-and-gamma-fels.md). All numbers are placeholders for the research agenda's studies; the structure is the part to keep.

## The short version

- **Research opens a principle; an engineering project produces a block.** That split is already decided ([`design/intercept-window-initial-design-notes.md`](intercept-window-initial-design-notes.md)). This note says what a weapon block contains and how its numbers move.
- **Every family has three layers:**
  - **the law:** fixed physics, e.g. jet speed = √(2 η Y / m);
  - **the engineered numbers:** a few efficiencies and quality factors, each with a physical ceiling, improved by engineering effort and tests;
  - **the spec:** what the player asks for (yield, aperture, muzzle velocity, count). Unbounded.
- **Range and damage are computed, never tabulated.** The designer report shows reach against each target class as a continuous function, plus an **overkill factor** (delivered over needed).
- **The hilarious tiers are the same formula with bigger numbers.** A gigaton Casaba throws a tonne of tungsten at a tenth of light speed, and the only rule involved is the one that also describes the 1985 test.
- **The pace accelerates.** Engineering effort is people plus design compute, and compute grows with industry. Machine polities climb the curves fast, and fewer physical tests means less for anyone to see.
- **Realism thins with distance from today; physics never does** (Teemu, Nov 2). Near-present blocks must match engineering data; far-future blocks only have to respect physics. Physics is the only final limit in the game.
- **Payloads multiply.** A macron carrying fusion fuel releases tens of thousands of times its kinetic energy at 100 km/s. The multiplier falls as 1/v², so payloads make slow macrons hit like fast ones.
- **Antimatter is the endgame, physics-only.** It decouples a weapon's power from the ship's reactor: the gun's power plant is in its magazine.

## Realism gradient: engineering near, physics far

A rule of thumb for every block in the game, not only weapons (Teemu, Nov 2):

| Distance from today | What a block must match | Example |
| --- | --- | --- |
| **Demonstrated** | Engineering data: real hardware, tests, failure modes | Chemical missiles, kW lasers, KKVs, the Grenadier test |
| **Studied** | Published design studies, scaled honestly | Casaba-Howitzer, DE-STAR, macron accelerators, Starshot |
| **Physics-only** | Conservation laws, material strength limits, diffraction, thermodynamics, light speed; nothing else | Gamma FELs, antimatter macrons and beams, gigaton Casabas |

How it maps onto the model:

- **Every engineered number carries a basis tag** at each point of its curve. Start values and the early curve come from demonstrated or studied sources. The ceiling is always a physics limit. The far end of the curve is physics-only.
- **Realism thins along the curve.** The first Casaba's numbers must be defensible against declassified Orion material; the hundredth only needs to stay under its ceiling.
- **Physics-only families have no engineering start point.** Their first block's numbers are placeholders chosen for play, tagged as such, and bounded only by physics. They are honest about being guesses.
- **Physics is the only final limit.** Nothing in the game is forbidden except what physics forbids. Everything else is cost, time, visibility and politics.
- **Deviations are logged exceptions.** The rule lives in [`design/fleetwright-principles-for-intercept-window.md`](fleetwright-principles-for-intercept-window.md) (decision 9), which keeps the list of logged exceptions. A weapon block that breaks it for play goes on that list.

## The model

### Layer 1: the law

Each family has one or two governing relations, taken from the research docs. They convert engineered numbers plus spec into performance: speed, spot size, fluence at range, time of flight. The law is code; it doesn't vary between polities.

### Layer 2: engineered numbers

A handful of parameters per family that a polity's engineering actually improves: efficiencies, beam quality, cone angle, specific mass, reliability. Each one has:

- **a starting value** where the principle is first demonstrated (often terrible: the one real nuclear shaped-charge test put 0.007 % of its yield into the jet);
- **a physical ceiling** it can approach but never pass (placeholder until the studies set it);
- **a curve** connecting them.

**The curve: each doubling of cumulative engineering effort closes a fixed share of the remaining gap, measured in orders of magnitude.**

```latex
\ln\frac{x_{\max}}{x(K)} = \ln\frac{x_{\max}}{x_0}\cdot\left(1+\frac{K}{K_0}\right)^{-b}
```

- **K:** cumulative engineering effort on this block line (design work, prototypes, tests).
- **K₀:** the effort scale for the family; nuclear and FEL lines are expensive, coilguns cheap.
- **b:** the learning exponent. Wright's law in the manufacturing note (10–30 % per doubling) is the production-cost version of the same idea.
- **For "smaller is better" numbers** (cone angle, emittance, specific mass) the same curve runs downward toward a floor.

Working in orders of magnitude matters: shaped-charge coupling climbs from 10⁻⁴ toward 10⁻¹, which is three decades, and early projects should buy decades quickly, late ones the last factor of two slowly.

**Know-how is the state.** These numbers are what a polity knows, per the manufacturing note: buying a block gives its numbers once; buying know-how gives the curve; stealing either is an incident.

### Layer 3: the spec

The player's engineering project asks for a block: "a Casaba with 1 Mt yield, a 100 kg jet, aimed for a 1 mrad cone". The project:

- **checks the spec against the current engineered numbers** and reports what will actually come out (the cone the team can deliver, the efficiency it expects);
- **costs it:** effort, time, materials (fissile and fusion fuel for nukes, superconductor tape for coilguns, laser diodes for arrays), facility time;
- **produces a block version** ("Mk 3") with frozen numbers, which ships can carry and factories can build;
- **adds to K** whether or not the design is ever produced. Failed prototypes still teach.

The designer never refuses a spec, as with ships. A spec beyond the current curve is reported as "expected to fall short: will deliver 3 mrad, not 1".

### Tests

Some families can't climb far without physical tests, and some tests are loud.

| Family | What a test is | Who can see it |
| --- | --- | --- |
| Nuclear shaped charge, bomb-pumped X-ray laser | A nuclear detonation in space | Everyone with an X-ray or gamma sensor; a system-wide incident |
| Lasers, FELs, particle beams | Firing at a target range | Waste heat and the target's glow; local |
| Coilguns, macron guns | Firing slugs into a catcher or into deep space | Projectiles that someone may track |
| Missiles | Flight tests | Drive plumes; like any burn |

- **Tests multiply effort.** A project with tests gains more K per unit cost than one without.
- **Simulation substitutes partly.** Design compute replaces some testing, as stockpile stewardship does today. This is where machine polities pull ahead *quietly*: they can climb a nuclear line with fewer detonations, and so fewer incident records.

### What pushes back

Nothing forbids a gigaton device or a 4,500 km coilgun. These do:

- **Materials:** fissile and fusion fuel, tungsten, superconductor, diodes. Vitamins in the manufacturing sense.
- **Heat and power:** beams and launchers need reactors and radiators; the ship generator sizes them.
- **Visibility:** big installations are seen; nuclear tests are seen by everyone; production lines show in the mass balance.
- **Politics:** each test, production run and deployment is an incident on the defiance ladder, read by every observer through their temper.
- **Delivery:** a weapon must reach a firing position. A gigaton Casaba is a one-shot device that still needs a bus, a cold coast and a picture.

## Report labels: the overkill factor

The designer and the fire-control display show, for a chosen target class and range:

**Overkill factor = delivered fluence (or dose, or energy) / what that target class needs.**

As with the picture, the labels are words on a continuous number, never levels in code:

| Overkill factor | Label |
| --- | --- |
| below 1 | Insufficient |
| 1–3 | Adequate |
| 3–30 | Thorough |
| 30–1,000 | Excessive |
| above 1,000 | Hilarious |

The label belongs to the pairing, not the weapon. A Mk 5 Casaba is "Insufficient" against a buried compute vault and "Hilarious" against a solar farm.

## Worked example: the nuclear shaped charge

### The principle

A nuclear device that sends a large share of its output into a narrow jet of propellant (plasma, droplets or particles) instead of a sphere. Project Orion's pulse units already did this toward a pusher plate; Casaba-Howitzer was the effort to narrow the cone into a weapon. The only known test (Operation Grenadier, 1985) drove about 1 kg of tungsten and molybdenum to about 70 km/s from an 8 kt device. That is the starting point.

Per the initial design notes, the device itself is a **warhead block** (yield and mass as inputs, from the bursts and warhead studies), never engineered from components. The Casaba project engineers what happens to that yield, not how the device makes it.

### Layer 1: the law

- **Jet energy:** E = η Y, with η the coupling efficiency and Y the yield.
- **Jet speed:** v = √(2E / m) for a jet of mass m, with the relativistic form once v passes about 0.05c.
- **The jet is a cone** of half-angle θ. At range R its radius is θR, so the fluence is E / (π θ² R²).
- **Fluence range,** the farthest range at which fluence still reaches what the target needs (F_kill):

  **R_fluence = (1/θ) √(E / (π F_kill))**

- **Dodge range.** The cone is a shotgun: the target must leave a disc of radius θR during the flight time R/v, which gives **R_dodge = 2 v² θ / a.**
- **Effective range** is the smallest of fluence range, dodge range and the picture's fix error compared with the cone radius.

So **range grows as √(ηY) / θ.** Cone angle is the biggest engineering lever, efficiency second, yield a distant third because of the square root.

### Layer 2: engineered numbers

| Number | Start (Grenadier) | Ceiling (placeholder) | What improves it |
| --- | --- | --- | --- |
| Coupling η | ~0.007 % | ~20 % | Channel design, propellant plate, radiation case |
| Cone half-angle θ | ~0.1 rad (assumed) | ~10 µrad | Propellant shaping, plate uniformity, device symmetry |
| Jet mass per kt | ~0.1 kg | design choice | Spec trade, not a ceiling |
| Reliability | low | ~99 % | Tests, production experience |
| Device mass per yield | from the warhead block | from the warhead block | The warhead line, not this one |

### Layer 3: the ladder

Two placeholder damage thresholds: **10⁶ J/m²** strips radiators, sensors, solar arrays and thin structure; **10⁸ J/m²** holes a warship's armour.

| Tier | Yield | η | Jet | θ | Jet speed | Range at 10⁶ J/m² | Range at 10⁸ J/m² |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Grenadier** (1985, real) | 8 kt | 0.007 % | 1 kg | 0.1 rad | 70 km/s | 0.3 km | 30 m |
| **Mk 1, Orion-derived** | 5 kt | 0.5 % | 10 kg | 50 mrad | 145 km/s | 3.6 km | 0.4 km |
| **Mk 3, fission-era spear** | 50 kt | 2 % | 20 kg | 10 mrad | 650 km/s | 115 km | 12 km |
| **Mk 5, megaton lance** | 1 Mt | 5 % | 100 kg | 1 mrad | 2,000 km/s | 8,000 km | 800 km |
| **Hilarious** | 1 Gt | 10 % | 1 t | 0.1 mrad | 0.1c | 3.6 million km | 365,000 km |
| **Accelerando** | 100 Gt | 20 % | 10 t | 10 µrad | 0.4c | 3.4 AU | 0.3 AU |

What the ladder shows:

- **The early tiers are knife-fight weapons.** Mk 1 reaches kilometres. It is a nuke that hits one thing well instead of everything badly.
- **The mid tiers rival warship lasers.** A Mk 5 lance strips radiators at 8,000 km, about a fusion-era laser's reach, from a missile-sized device, and holes armour at 800 km.
- **Dodging stops mattering early.** The cone is wide enough at range that even against a 1 g target the dodge range runs from about 10⁵ km (Grenadier) to 10⁷ km (hilarious), always beyond the fluence range. Fluence and the picture are the limits.
- **The damage mode changes at the top.** At 0.1c each nucleon in the jet carries about 4 MeV; at 0.4c about 90 MeV. The jet stops in the target's first microns to millimetres and blows the surface off, like X-ray blow-off on a huge scale. The hilarious tiers sandblast and spall rather than drill. Bunkers under regolith shrug; everything exposed is gone.
- **"Accelerando" is physics-only.** A 100 Gt device is a fusion-economy artefact, plausible only once someone is burning Jupiter's deuterium. With antimatter-triggered pure fusion (below) it needs no fissile material at all, so deuterium is the only limit on its yield.

### What pushes back, specifically

- **One shot per device.** Every Casaba is a nuclear warhead consumed. Fissile and fusion fuel per kt is a warhead-block number; at the top, deuterium supply is the limit.
- **Standoff for the firing platform.** The device detonates; whatever launched it must be far away. Casabas ride missiles or buses.
- **Tests are system-wide incidents.** Every rung up the η and θ curves wants detonations unless design compute substitutes.
- **Treaties.** Nuclear weapons in orbit are the oldest ban in the book; an Orion fleet is a Casaba magazine with a drive attached, and every observer knows it.
- **Proliferation:** an Orion drive's pulse-unit factory is a Casaba factory with a different jig.

### Scenario: the Jovian strike

The user story that started this: a swarm of hilarious-tier Casabas sent into the Jovian system to stop an unaligned AI CEO from finishing its megaproject (the Jovian Entity in [`design/shadow-ledger-playing-the-unaligned-controller.md`](shadow-ledger-playing-the-unaligned-controller.md)).

- **Standoff:** buses coast in cold and fire from 10⁶ km, outside the Entity's warship-class lasers. The jet crosses that distance in about 35 s; surface installations on Io can't dodge, so the bloom is zero and the picture is good.
- **One shot:** a cone 100 km in radius at 10⁶ km delivers about 1.3×10⁷ J/m², "Excessive" against radiators, solar arrays and surface plants, "Insufficient" against anything under metres of rock.
- **The swarm:** covering Io's facing hemisphere takes about 660 shots. A thousand-device swarm is the right order of magnitude to strip a moon's surface industry in one pass.
- **The Entity's counters:** bury the compute; keep radiators retractable or on the far side; kill buses before they reach firing range (its strategic lasers against cold, coasting, predictable buses); hold the attacker's own fixed assets at risk; and simply do the same back.
- **The record:** a thousand gigaton detonations in the Jovian system is the top of the defiance ladder, seen by everyone, and changes every observer's view of whoever ordered it.

## Worked example 2: macrons with payloads

The second worked example, because it shows a payload slot on a weapon block. The source is ToughSF's survey of hypervelocity macron accelerators (Nov 2019).

### The principle

A **macron** is a macroscopic particle, from tens of nanometres to about a millimetre. Charged, it can be accelerated electrostatically or magnetically far beyond what a railgun or coilgun can do, because tiny objects are very strong for their size and hold a large charge per kilogram. ToughSF's target range is 10–10,000 km/s.

**What the article rules out:** railguns and coilguns (the particles can't survive railgun heating, and coilguns can't make the fields they need).

### Layer 1: the laws

**The accelerator.** Each type has its own speed law:

| Type | Speed law | What limits it |
| --- | --- | --- |
| Linear electrostatic | v = √(2 V · q/m) | Voltage; field emission; switching losses in multi-stage machines (about 3 MV/m) |
| Circular | v = r · B · q/m | Bend radius and magnet strength, independent of voltage; best for very high q/m |
| Beam "pushrod" | Pushed by an electron or proton beam without contact, so no heating | The macron's tensile strength; the beam's current density |

ToughSF's worked results for 100 m-class machines:

| Accelerator | Fastest of the article's sample macrons |
| --- | --- |
| 10 MV single stage | ~900 km/s (10 nm nanolattice sphere) |
| 100 m multi-stage, 300 MV | ~4,900 km/s |
| 100 m ring, 10 T | ~20,000 km/s |
| 100 m proton pushrod | ~11,700 km/s (1 mm hollow diamond) |

So 100-metre machines already reach a few per cent of light speed. The barrel isn't the limit; charge per kilogram, strength and power are.

**Charge per kilogram** is bounded by field emission at the surface and by the macron's tensile strength. Shaping (hollow shells, long needles) raises it: a 1:2000 tube has 7.6 times the surface area of a sphere of the same volume, and a nanotube-like needle about 131 times.

**On target**, energy per macron = ½ m v² + payload energy. The **payload multiplier** is:

**M = 1 + (payload fraction × energy density × burn fraction) / (½ v²)**

**Hit probability** follows the dodge law, smoothly, with no cutoff (ToughSF's formula, the same physics as [`design/combat-ranges-and-group-tracks.md`](combat-ranges-and-group-tracks.md)):

**P_hit ≈ min(1, (s / ½ a t²)²),  t = R / v**

So beyond the range where P = 1, hit probability falls as 1/R⁴. ToughSF's example: 1,000 km/s macrons against a 5 m target dodging at 0.5 g hit about 30 % of the time at 2,000 km, and 10 % at about 2,650 km.

### Payloads

| Payload | How it releases | Energy density | Basis |
| --- | --- | --- | --- |
| **Inert** | Impact only | ½ v² | Demonstrated (14 km/s in 1962 with 0.1 µm iron spheres) |
| **Fission-enhanced** | Impact compresses a sub-milligram U-235 core with a DT shell to criticality | ~8×10¹³ J/kg at full burn | Studied (Winterberg); critical mass falls as v^(−12/5) |
| **Impact fusion** | Impact above about 100 km/s heats DT fuel to fusion (some sources say 50 km/s with a conical impactor) | ~3.3×10¹⁴ J/kg of fuel | Studied |
| **Antimatter-catalysed fusion** | Nanograms of antiprotons trigger fission or fusion in the fuel, with no impact-speed threshold | as fusion | Studied as propulsion (ICAN-II, AIMStar) |
| **Antimatter** | Annihilation | 1.8×10¹⁷ J per kg of antimatter | Physics-only (endgame, below) |

ToughSF's figures for the studied payloads:

- **Fission-enhanced, at 20 km/s:** a 0.04 g macron needs 24 m of accelerator and about 8.4 kJ. Multiplier about 38,000 at 10 % burn and 379,000 at full burn. A 1 MW accelerator firing about 120 a second releases 38–380 GW on target.
- **Impact fusion, at 100 km/s:** a 1 mm diamond shell holding 78 µg of DT reaches 100 km/s in a 31 cm pushrod. The multiplier is about 66,000. A 1 MW accelerator firing 2,500 a second releases up to 64 GW.

**The multiplier falls as 1/v²**, for a payload of half the macron's mass:

| Speed | DT, full burn | DT, 10 % burn | Antimatter 1 % | Antimatter 10 % |
| --- | --- | --- | --- | --- |
| 100 km/s | ×33,000 | ×3,300 | ×360,000 | ×3.6 million |
| 1,000 km/s | ×330 | ×34 | ×3,600 | ×36,000 |
| 10,000 km/s | ×4 | ×1.3 | ×37 | ×360 |

Two consequences shape the family:

- **Slow fusion macrons are the brute.** At 100 km/s, a megawatt accelerator puts tens of gigawatts on target, but only at short range: against a warship at 0.5 g the hit chance is 100 % to about 140 km, 10 % at 250 km, 1 % at 450 km.
- **Fast macrons don't need payloads.** At 10,000 km/s kinetic energy alone is close to fusion; the payload adds a few times. They reach 10× further against the same target (1 % at about 45,000 km).
- **Against stations,** which barely dodge, even slow macrons reach far: at 100 km/s against a 50 m station jinking at 10⁻³ m/s², the hit chance is 100 % out to about 30,000 km. The picture becomes the limit.

### Layer 2: engineered numbers

| Number | Start | Ceiling | Basis at the start |
| --- | --- | --- | --- |
| Charge per kg | ~1 C/kg (µm metal spheres) | ~1,500 C/kg and above (nanotube-class needles) | Demonstrated → physics |
| Accelerating gradient | ~0.6–3 MV/m | Field-emission limits, ~100–1,000 MV/m | Studied |
| Wall-plug efficiency | low (switch losses) | ~80 % (beam-pushrod tubes) | Studied |
| Fusion burn fraction on impact | ~0 below threshold, rising smoothly with speed | ~30 % (placeholder) | Studied → physics |
| Fissile mass per macron | ~0.2–0.04 g | falls with v^(−12/5) | Studied |
| Guidance per macron | none | smart pellets with a few nanograms of steering | Physics-only |

Burn fraction is a smooth function of impact speed, never a threshold, per the no-cutoffs rule.

### Layer 3: the ladder

| Tier | Accelerator | Macron and payload | Speed | On target per MW of accelerator |
| --- | --- | --- | --- | --- |
| **1962 lab** | Van de Graaff, 2 MV | 0.1 µm iron, inert | 14 km/s | laboratory only |
| **Mk 1 macron gun** | 10 MV single stage | µm carbon shells, inert | ~250 km/s | ~1 MW; anti-missile, anti-sensor |
| **Mk 3 fission spray** | 24 m linear | 0.04 g U-235 + DT | 20 km/s | 38–380 GW at knife range |
| **Mk 5 fusion hose** | 31 cm pushrod (per stage) | 1 mm diamond, 78 µg DT | 100 km/s | up to 64 GW, 100s of km against ships |
| **Torch-era lance** | 100 m ring or pushrod | needles and shells, inert or DT | 1,000–10,000 km/s | ×1–×330 per MW; 10³–10⁵ km against ships |
| **Hilarious** | km-scale pushrod array, GW | 1 mm shells with 1 % antimatter | 1,000 km/s | ×3,600: a GW accelerator puts ~3.6 TW on target, a fleet's worth of nukes a second |

### What pushes back

- **Fuel:** tritium for DT, U-235 for fission sprays, antimatter at the top. Each is a vitamin with its own production chain.
- **Fragility:** frozen DT doesn't survive a laser (ToughSF: carbon-fibre spheres take about 58 MW/m², carbon needles about 579 GW/m², DT ice much less). Fusion macrons are vulnerable to point defence in a way inert needles aren't.
- **Range:** slow payload macrons fight close; fast inert ones fight far. No macron does both.
- **Stealth works for them:** macrons are cold and tiny, almost impossible to see before impact. Whipple shields fail fast, because one hit opens a hole for thousands.
- **Every fission or fusion macron is a nuclear weapon** for the treaty layer. A fusion hose firing 2,500 micro-detonations a second is a very strange incident record.

## Endgame, physics only: antimatter

No engineering basis exists for antimatter weapons, so this family follows the physics-only rule: principle and ceilings from physics, start values as tagged placeholders.

### The physics

- **Energy:** annihilating antimatter with an equal mass of matter releases 1.8×10¹⁷ J per kg of antimatter. 1 µg ≈ 43 kg of TNT; 1 mg ≈ 43 t; 1 g ≈ 43 kt; 1 kg ≈ 43 Mt.
- **Where it goes:** proton–antiproton annihilation makes pions. Neutral pions decay to gamma rays; charged pions travel metres before decaying, and a large share (roughly a third, to be checked) ends up in neutrinos, which escape. So antimatter deposits deeply and volumetrically, like a gamma beam with structure-level energy.
- **Production is a battery charge.** Making antimatter costs at least as much energy as it returns. Today's accelerator production takes about ten billion times more energy than the antimatter holds; Robert Forward estimated a properly engineered factory might reach about one part in ten thousand. The physics ceiling is near unity (placeholder ~50 %).
- **Coupling:** a bulk antimatter bomb is inefficient. The first annihilations at the surface blow the antimatter and the matter apart before most of it reacts (Atomic Rockets, exotic weapons). Antimatter warhead blocks carry an **annihilation coupling** number: low for bare bombs, higher for finely mixed or target-impact designs, near one for beams and macrons, which annihilate inside the target's own matter. That is why beams and macrons are the endgame weapons, not bare bombs.
- **Storage:** charged antiprotons in Penning traps, neutral antihydrogen in magnetic traps (both demonstrated at tiny scales). No static field can hold a stable trap (Earnshaw's theorem), so traps use changing fields. Forward's bulk idea is a snowball of solid antihydrogen below 2 K, levitated magnetically in vacuum: physics-allowed, no engineering basis. A containment failure is a burst.

### Why it changes the endgame

**The gun's power plant is in the magazine.** Every other beam is limited by the shooter's reactor and radiators: a 1 GW laser at percent efficiency needs tens of GW of waste-heat rejection. An antimatter beam carries its energy in the particles. A ship firing 1 g/s of antihydrogen delivers about 180 TW on target while its own accelerator draws a tiny fraction of that. A small, cool ship can briefly hit like a Mercury Swarm.

### The weapons

| Weapon | What it is | Physics notes |
| --- | --- | --- |
| **Antimatter-catalysed nukes and macrons** | Nanograms of antiprotons ignite fission or pure fusion | The bridge tier. ICAN-II planned 140 ng of antiprotons for a whole Mars trip. Removes fissile limits and impact thresholds; enables pure-fusion Casabas |
| **Antimatter macrons** | A macron with antimatter held inside a shell | ×36,000 at 1,000 km/s with 10 % antimatter. A µg-class macron carries tens of kg of TNT; a mg-class one tens of tonnes |
| **Antihydrogen beam** | A neutral antihydrogen particle beam | Divergence as for neutral beams (floor about 0.2 µrad). Each particle adds 1.9 GeV of annihilation to its kinetic energy, so even a slow beam hits like a fast one. Deep deposition: crew, electronics and structure together |
| **Antimatter warheads** | Bare annihilation bursts | Mostly gammas and pions; compare with the bursts study |
| **Antimatter-driven Casaba** | Annihilation-triggered pure-fusion shaped charge | The Accelerando Casaba tier, with deuterium as the only fuel limit |

### The ladder

| Tier | Example | On target |
| --- | --- | --- |
| **Catalyst** | ng of antiprotons per fusion macron or warhead | as fusion; no fissile, no impact threshold |
| **Antimatter macron gun** | mg of antimatter a second in µg macrons | 43 t of TNT a second |
| **Antihydrogen lance** | 1 g/s neutral beam | ~180 TW-equivalent, from a small ship |
| **Hilarious** | a 1 kg antihydrogen pulse through a 1 µrad beam | 43 Mt into a 20 m spot at 10,000 km: about 6×10¹⁴ J/m² |

### What pushes back

- **Production is the economy.** At a factory efficiency of 10⁻⁴, a gram of antimatter (43 kt) costs about 2×10¹⁸ J of electricity, a terawatt for three weeks. Even at the physics ceiling it's a terawatt for a few minutes per gram. The Mercury Swarm and the Jovian deuterium economy are where antimatter is made.
- **The magazine is the most dangerous thing aboard.** A containment failure is a burst inside the ship; the damage model already handles accident bursts.
- **Factories are visible:** huge, hot, fixed, and stray annihilation gives a 511 keV gamma line anyone can read.
- **Treaties don't exist yet.** Nobody has banned what nobody can make. The first antimatter weapon test writes the treaty.

## The other families, sketched

Each sketch gives the law, the engineered numbers, the spec, a ladder and what pushes back. Numbers are from the research docs or computed from their laws.

### Lasers and phased arrays

- **Law:** spot ≈ 2.44 λR / D; intensity = P / spot area; then the picture and the bloom.
- **Engineered:** wall-plug efficiency, beam quality (M²), specific mass per kW, phasing precision for arrays, pointing stability, shortest practical wavelength, and for point defence, recycle time and flash-cooler charges.
- **Pumping options within the family:** electrically pumped (solid-state, fibre, FEL) or **reactor-pumped**, where fission fragments or reactor heat pump the lasing medium directly and skip the electrical chain (several kW of beam per kg in ToughSF's analysis). Reactor-pumped lasers are just lasers with different efficiency and specific-mass numbers, not a separate family.
- **Frequency doubling:** an engineered step that halves the wavelength and doubles range, at a 20–30 % efficiency cost.
- **Spec:** power, aperture, wavelength.

| Tier | Power, aperture, λ | Spot and intensity |
| --- | --- | --- |
| Naval laser (today) | 100 kW, 0.5 m, 1 µm | 5 cm at 10 km, ~5×10⁷ W/m² |
| Warship | 10 MW, 2 m, 500 nm | 0.4 m at 600 km, ~10⁸ W/m² |
| Station | 1 GW, 10 m, 100 nm | 3.7 m at 1 light-second |
| DE-STAR 4 (studied) | 70 GW, 10 km array, 1 µm | 39 m at 1 AU, ~6×10⁷ W/m² |
| **Hilarious: the Mercury Swarm's gun** | 10 TW, 1,000 km array, 1 µm | 2 m at Jupiter (5.2 AU); powered by about 3,700 km² of Mercury collectors |

- **Pushes back:** heat, power and aperture mass; the bloom (at Jupiter the Swarm's gun must sweep boxes, which drops it to around 20 kW/m², still enough to cook radiators and blind every sensor in the system); and the fact that the installation is the brightest object in the sky.

### Guns, railguns and coilguns (slugs)

For gram-to-kilogram slugs; macrons are the worked example above.

- **Law:** v² = 2 a L for a barrel of length L at acceleration a; range from the dodge law in [`design/combat-ranges-and-group-tracks.md`](combat-ranges-and-group-tracks.md).
- **Engineered:** field strength and switching speed, efficiency, rail and barrel wear, specific mass per metre.
- **Spec:** muzzle velocity, projectile mass, rate of fire. Payloads apply here too (a nuclear shell), with multipliers far larger at these low speeds.

| Tier | Muzzle velocity | Barrel at 10⁵ m/s² | Barrel at 10⁶ m/s² |
| --- | --- | --- | --- |
| Gun / early railgun | 3–10 km/s | 45–500 m | 5–50 m |
| Coilgun | 30 km/s | 4.5 km | 450 m |
| **Hilarious: the lunar mass driver** | 30 km/s, tonne-class slugs | 45 km of track at a gentler 10⁴ m/s² | — |

- **Pushes back:** rail wear, power per shot, waste heat; slugs stay dodge-limited, so their reach is the ranges doc's ~100 km against agile ships, and far more against stations and moons.

### Laser sails and pellet streams

- **Law:** photon thrust is 2P/c on a reflecting sail; launch energy is at least E_kinetic × c / (2v), more in practice.
- **Engineered:** sail reflectivity and areal mass, array power and aperture, acceleration tolerance.

| Tier | Launcher | Projectile | Energy on target |
| --- | --- | --- | --- |
| Starshot (studied) | 100 GW array | 1 g at 0.2c | ~0.44 kt |
| **Hilarious** | 10 TW (the Swarm's gun again) | 1 kg at 0.1c, at best one every ~4 minutes | ~110 kt each |

- **Pushes back:** dumb projectiles need a predictable target and a good picture; every launcher is also the laser above.

### Bomb-pumped X-ray lasers

- **Law:** divergence ≈ √(λ/L) for a rod of length L; energy per rod = coupling × yield / rods.
- **Engineered:** coupling into the rods, rod length and quality, shortest wavelength.
- **Spec:** yield, rod count, rod length.
- **Ladder:** an Excalibur-style device (tens of rods, ~1.4 nm, 10³–10⁴ km) up to a **hilarious "chandelier"**: a gigaton device with thousands of 10 m rods, each a separate shot at a separate target. One detonation, a fleet's worth of hits.
- **Pushes back:** like the Casaba, plus the contested physics: the curve's starting point is uncertain and its ceiling may be low.

### Particle beams

- **Law:** spot ≈ divergence × range; deep volumetric deposition.
- **Engineered:** divergence (floor around 0.2 µrad), particle energy, current, neutralisation efficiency.
- **Ladder:** BEAR (1989, sub-weapon) → a neutral beam at ~1 µrad reaching 10³–10⁴ km → relativistic electron beams if the speculative long-range propagation holds → **hilarious:** the antihydrogen lance from the antimatter section, the same beam physics with annihilation added to every particle.
- **Pushes back:** accelerator length and power; divergence floor.

### X-ray and gamma FELs

- **Law:** λ ≈ λ_u (1 + K²/2) / 2γ²; beam quality must satisfy emittance ≲ λ/4π; then the sweep model from the strategic-beams doc.
- **Engineered:** electron energy per metre of accelerator (plasma accelerators help), emittance, extraction efficiency, average power.

| Tier | Photons, power | Time to sweep a 15 km box to 10 Gy |
| --- | --- | --- |
| Research XFEL (today) | 25 keV, watts | Never |
| Hard X-ray weapon | 12 keV, MW | — (surface weapon, anti-sensor) |
| First gamma installation | 1 MeV, 1 GW | 12 min |
| Mature | 1 MeV, 100 GW | 7 s |
| **Hilarious: the Sterilizer** | 10 MeV, 10 TW | about 1 s, even behind a metre of water |

- **Pushes back:** efficiency (waste heat of 30–100× the beam), accelerator scale, atmospheres, and the picture.

### Kinetic bombardment and rock redirection

- **Law:** E = ½ m v²; v is set by orbits (orbital rods ~3 km/s at impact, belt rocks 10–30 km/s).
- **Engineered:** guidance, Δv per tonne moved, detection of the approach (for the defender).
- **Ladder:** a Thor rod (~48 GJ, 11.5 t TNT) → a 100 m rock at 20 km/s (~50 Mt) → **hilarious:** a 1 km moonlet (~50 Gt).
- **Pushes back:** years of visible preparation, and planetary-defence systems that are weapons themselves.

### Drives, point defence and Kirklin mines

Studied in [`studies/drives-point-defence-and-kirklin-mines.md`](../studies/drives-point-defence-and-kirklin-mines.md), which proposes their blocks:

- **The drive as a weapon:** intensity falls as P / π(θR)², so nozzle divergence is the engineered number; D-T drives add an omnidirectional neutron flux. **Hilarious:** a 50 TW pure-fusion torch pointed at whatever is behind it, or a 30 TW photon drive, which is a laser.
- **Point-defence guns, lasers and interceptors:** existing families with rate, recycle time and divert Δv as engineered numbers.
- **Kirklin mines:** expendable mass in the missile's path; burst timing t = √(2r/a) and cloud mass ∝ r² are the laws. **Hilarious:** a torch fleet dropping its empty tanks into an incoming wave at 1,000 km/s closing speed, every gram of tank worth 120 kg of TNT.

## The acceleration

The Accelerando feel comes from one term: what engineering effort is made of.

```latex
\frac{dK}{dt} = \left(h \cdot N_{\text{engineers}} + \kappa \cdot C_{\text{design}}\right)\cdot T
```

- **N:** people working the line; **h:** their productivity, set by know-how and tools.
- **C_design:** design compute assigned to the line; **κ:** how much a unit of compute is worth, itself a research line (autonomy, as in the manufacturing note).
- **T:** the test multiplier, above 1 when physical tests feed the line.

Consequences:

- **Early game, effort is people.** A human polity's Casaba line climbs over decades, gated by tests that are political crises.
- **Mid game, compute joins.** Compute grows with industry, industry grows by the manufacturing growth law, so effort grows exponentially for anyone who invests.
- **Late game, machine polities iterate in months.** Their κ·C dwarfs human staff. They also need fewer loud tests. The Jovian Entity's weapon blocks can be several marks ahead of its besiegers', and nobody saw the tests.
- **Ceilings keep it physical.** Every engineered number saturates at its ceiling. After that, the only way up is the spec, which means industry. Late-game overkill is an economy's size expressed as a weapon.

## In the sim

- **A family is data:** the law (code, shared), its engineered parameters with start, ceiling, curve and effort scale, its spec fields, its payload slots, its costs and test rules. Tagged with sources and a basis (demonstrated, studied, physics-only) per number, retunable without touching the sim.
- **A block version is a record:** family, polity, version, frozen numbers, provenance (engineered, bought, stolen), and the test incidents behind it.
- **The designer report adds:** reach against each target class as a continuous curve, the overkill factor and its label, costs, and the visibility of production.
- **Fire control reads the same law** with the polity's picture of the target, so a misidentified target gets the wrong overkill estimate.
- **Scenarios use a preset catalogue** of block versions fitted to the ladders here, as the initial notes already plan.

## Open questions

- [ ] The effort curve: is the log-gap form right for every family, or do some (coilgun efficiency) behave linearly?
- [ ] Ceilings for each engineered number, from the studies (warhead conversion for η and θ, beams for M² and emittance).
- [ ] Damage thresholds by target class, for the overkill factor: radiators, sensors, solar arrays, armoured hulls, buried installations, crew.
- [ ] Should tests be optional multipliers, or required gates for some steps (the first real Casaba)?
- [ ] How much can compute substitute for nuclear tests, and does that need its own ceiling?
- [ ] Multi-jet Casabas (several cones from one device, Excalibur-style): a spec option or a separate principle?
- [ ] Macron impact-fusion burn fraction as a smooth function of impact speed and macron shape: what the warhead conversion study should fit.
- [ ] Antimatter energy partition on annihilation (gammas, charged pions, neutrinos) and deposition depth, for the bursts and beams studies.
- [ ] Antimatter storage density and failure modes: the physics-only placeholders for the magazine.
- [ ] Should payload slots be general (any weapon that carries mass can take one), or per family?
- [ ] Should the hilarious label have a sound effect? (Proposed: yes.)

## Sources

- Internal: [`studies/weapons-survey-long-range-concepts.md`](../studies/weapons-survey-long-range-concepts.md), [`studies/strategic-beams-x-ray-and-gamma-fels.md`](../studies/strategic-beams-x-ray-and-gamma-fels.md), [`design/combat-ranges-and-group-tracks.md`](combat-ranges-and-group-tracks.md), [`design/manufacturing-and-the-dependency-ladder.md`](manufacturing-and-the-dependency-ladder.md), [`design/shadow-ledger-playing-the-unaligned-controller.md`](shadow-ledger-playing-the-unaligned-controller.md), [`design/intercept-window-initial-design-notes.md`](intercept-window-initial-design-notes.md).
- Macrons: [ToughSF, Hypervelocity Macron Accelerators](https://toughsf.blogspot.com/2019/11/hypervelocity-macron-accelerators.html) (accelerator types, charge-to-mass limits, payload multipliers, hit probability, laser survivability).
- Antimatter: [Centauri Dreams on production efficiency and Forward's factory estimate](https://www.centauri-dreams.org/2006/04/20/antimatters-advantages-and-the-catch/); [ICAN-II](https://en.wikipedia.org/wiki/ICAN-II) and [AIMStar](https://en.wikipedia.org/wiki/AIMStar) for antiproton-catalysed fission and fusion; annihilation energy from E = mc².
- External starting points are listed in the two research docs: Operation Grenadier's shaped-charge test, Casaba-Howitzer, Project Excalibur, DE-STAR, Breakthrough Starshot, BEAR, the European XFEL and Project Thor.
- All ladder numbers are computed from the laws above with placeholder engineered values and damage thresholds; the reference script lives with the warhead conversion study when it starts.
