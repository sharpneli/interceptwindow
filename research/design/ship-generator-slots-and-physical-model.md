# Intercept Window: Ship Generator – Slots and Physical Model

Oct 30, 2026 · from the browser shape bench ("Intercept Window Shipyard")

A starting point for the C# ship generator. It records what the browser prototype settled: which choices a design makes, how they combine, what physical numbers each choice produces, and what the prototype only faked. The prototype's numbers are placeholders fitted by eye; the structure is the part to keep. Physics comes first; the exact look of each component is iterated later and never touches the physics (Fleetwright principle: looks dress parts, never move or reshape them).

## Contract

The same three-stage pipeline as [`design/intercept-window-initial-design-notes.md`](intercept-window-initial-design-notes.md), section "The ship generator":

1. **Design:** tech blocks plus slot choices plus numeric inputs. Plain data, no geometry.
2. **Generator:** solves the mass budget and lays out the parts. Output is the **physical model**: parts with geometry, mass, materials, thermal properties, armour layers, internal spaces, occluders for shadowing, and a report.
3. **Drawing:** reads the physical model only. The mesh is the hitbox.

Rules carried over:

- **The designer never refuses.** A slot is a single choice, so exclusive options can't collide. Real geometric clashes are resolved by layout rules. Everything else builds and is reported.
- **No hard cutoffs.** Every quantity varies smoothly with its inputs. Where the prototype used thresholds (e.g. two radiator wings becoming four), the C# version should make them stated inputs or report them.
- **Monotone sizing.** Adding mass never yields a lighter ship. Add the lever sweep (`mono-check`) from the start.
- **Deterministic.** Same design, same model, same hash.

## Design inputs

### Blocks and numbers

| Input | Notes |
| --- | --- |
| Drive block × units | Exhaust velocity, thrust or jet power, unit mass or specific power, waste-heat fraction, propellant (density, tankage fraction, cryogenic, hydrogenous), nozzle family. The nozzle family sets the aft geometry; it is not a slot. |
| Δv, payload | Payload sets the crew count and the pressure-hull volume. |
| Armour material | A material block: density, heat capacity, conductivity, emissivity, vaporisation temperature and heat. |
| Nose armour, side armour | Thicknesses. With an umbrella, the nose value goes to the shield. With a spun belt, the side value goes to the belt. |
| Bumper count and standoff | 0–3 Whipple plates. |
| Spin rate | rpm for a roll or a belt. |
| Radiator temperature, fin thickness | Fin thickness applies to panels only. |
| Fit | Point defence, laser, spinal coilgun, missiles (count) and launch hatches. |

### Slots

Each slot is one choice. Families from the design discussion are presets: named slot combinations, like Fleetwright's named block sets.

| Slot | Options |
| --- | --- |
| **Backbone** (load path) | Truss spine · Shell (monocoque) · Apex cone |
| **Section** | Round · Faceted · Flat |
| **Taper** | None · Tapered · Lance |
| **Tankage** | Integral · Strap-on · Drop tanks |
| **Hab ring** | None · One ring · Counter-rotating pair |
| **Kinetic armour layout** | Envelope · Citadel · Tanks forward · Rubble jacket |
| **Crew shelter** | None · Storm shelter · Detachable lifeboat |
| **Frontal protection** | Umbrella (on/off) plus bumpers (count). These combine with each other and with any backbone. |
| **Laser defence** | None · Roll the whole ship · Decoupled spun belt |
| **Radiators** | Panel wings · Wire loops · Droplet sheets · Radiating skin · Sleeve outlet |

### Presets in the prototype

| Preset | Slot combination |
| --- | --- |
| Cislunar tug | Chemical · spine · round · integral · envelope · panels |
| Rock-jacket hauler | Fission electric · spine · strap-on · rubble · storm shelter · droplet sheets |
| Shield escort | NTR · spine · faceted · umbrella + 1 bumper · citadel · storm shelter · panels |
| Inspection cutter | NTR · shell · faceted · tapered · drop tanks · citadel · storm shelter · panels · missiles |
| Pulse frigate | Orion · shell · round · envelope · lifeboat · panels · coilgun · missiles |
| Lance cruiser | MCF · shell · faceted · lance · 2 bumpers · citadel · storm shelter · spun belt · wire loops · missiles |
| Sleeve raider | NTR · shell · faceted · citadel · storm shelter · sleeve · 48 missiles |
| Apex-cone transport | MCF · apex cone · radiating-skin cone · storm shelter |
| Torch liner | Torch · spine · tapered · counter-rotating ring pair · lifeboat · panels |

## Three kinds of conflict

1. **Same slot:** exclusive by construction (one backbone).
2. **Geometric:** resolved by layout, shown as a disabled option only where the choice has no meaning. In the prototype:
   - The apex cone forces the radiating-skin cone and ignores taper.
   - A pusher plate or magnetic nozzle owns the aft end.
   - "Tanks forward" is only geometric on a shell. On a spine or cone it is reported as doing nothing.
3. **Physical penalties:** allowed and reported. These are the design decisions:
   - Rolling ship with panel wings: panels sweep face-on once per turn.
   - Droplet sheets above about 0.001 g: coolant loss.
   - Spin angular momentum: slower flips, unless counter-rotating.
   - Umbrella: protects only inside its cover cone.
   - Tanks forward: protection falls as propellant burns.
   - Rubble jacket: huge mass, Δv cost everywhere except where the rubble is free.
   - Hab ring on a warship: the largest unarmoured target in the fight.
   - Radiating skin: can't also be thick armour.
   - Long spine at high acceleration: compression grows with acceleration × length.

## Mass budget

The prototype solves a fixed point, because armour and tank geometry depend on propellant volume, which depends on dry mass.

```
fixed  = payload + drive + reactor + shadow shield + radiators + weapons + missiles
       + shelter + hab ring + armour(geometry)
R      = exp(Δv / ve), capped where tankage would outweigh propellant
dry    = fixed / (1 − k_tank·(R − 1) − k_struct)
prop   = dry · (R − 1);   tanks = k_tank · prop;   structure = k_struct · dry
repeat: propellant volume → layout → armour areas → fixed
```

Eight iterations converged for every combination tried. In C#, converge to a tolerance and report non-convergence rather than looping a fixed count.

- **Drop tanks:** the prototype puts 60 % of propellant in droppable tanks and reports combat mass after jettison. C# should solve this as a proper two-stage rocket equation, with the drop fraction as an input.
- **Structure** is a flat 6 % of dry mass. C# should size it from loads: spine compression ∝ thrust, the length limit, and docking and burn loads.

## Backbones and layout

All layouts run along the thrust axis, nose at +Y.

### Truss spine

- **Front to aft:** frontal protection, pressure hull (crew space), hab ring, tanks, radiators, drive.
- **Pressure hull:** a lathe profile. Radius R = clamp(∛(V/3π), 1.6, 14) m, length = V/πR². The nose cone length depends on taper: 0.7R, 1.5R or 3.2R.
- **Tanks:** capsules in rows. Integral tanks are inline on the axis. Strap-on and drop tanks form a ring of 3–8 around the spine. Count and rows are chosen to keep the stack near 2.4 cluster diameters.
- **Truss:** triangular. Width ∝ hull radius; member radius ∝ √thrust.
- **Armour:** only the crew space carries side armour. The spine and tanks rely on distance and are unarmoured.

### Shell (monocoque)

The outer profile is one radius function r(s) of distance from the tip: a cone of fixed half-angle, capped at a maximum radius.

| Taper | Half-angle | Tip radius | Cap radius |
| --- | --- | --- | --- |
| None | 55° (blunt nose) | 0.15 R₀ | R₀ |
| Tapered | 9° | 0.4 m | 1.25 R₀ |
| Lance | 2.4° | 0.3 m | 3.2 R₀ |

- **R₀:** set from total internal volume, ∛(V/6π).
- **Filling the profile:** internal items fill it from the front, each starting where the profile is wide enough for it. The crew space needs room for its shelter. Each item takes the length that holds its volume (conformal frustum tanks).
- **Item order:** crew, magazine, tanks. With "tanks forward": tanks, crew, magazine.
- **The empty tip:** on a lance, the forward cone is empty and solid, which is the armoured tip.
- **Armour areas:** come from the profile. The nose zone runs up to the first item, the side zone is the rest.
- **Envelope:** side armour on the whole shell.
- **Citadel or tanks forward:** a thin 5 mm skin, plus a citadel tube around the crew span.

### Apex cone (VISTA-style)

- **Shape:** a hollow cone with a 50° half-angle. The apex and drive are aft; the wide rim faces forward and carries a lithium coil shield torus about 1 m thick.
- **The cone is the radiator.** Its area sets its size: R_front = max(8 m, √(A / (π·1.305))).
- **Crew:** three pods on the outer surface near the rim. **Propellant:** six spheres mid-cone.
- **Flight:** blunt end forward. Frontal protection (bumpers, umbrella) mounts ahead of the rim.
- The VISTA reference: 50° half-angle, 13 m magnet radius, a 1 m liquid-lithium shield, about 6,000 t, everything in the coil shield's shadow.

### Section

- **Faceted:** an 8-gon hull and tanks with flat normals. Flat armour plates sit over a round pressure vessel, because pressure vessels can't have corners.
- **Flat:** the hull scaled 1.7 : 1/1.7 across, wide in the radiator plane. Faceted plus flat gives a hexagonal blade.
- **Mounting radius:** mounts read the surface radius per axis, including the facet inset cos(π/n).

## Radiators

The radiator budget is computed from waste heat (drive waste + housekeeping + crew) and temperature T.

| Type | Model | Area or size | Notes |
| --- | --- | --- | --- |
| Panel wings | Two-sided C–C fin, fin efficiency η = tanh(mL)/mL with m = √(2h/kt), h = 4εσT³, half pipe pitch L = 5 cm | A = Q / (2εσT⁴η) per face | Thickness trades mass against η. Wings sit in planes containing the axis: two, or four above 2,500 m² each. Coolant loops in bands along the wing. |
| Wire loops | 1 mm tungsten wire, ε ≈ 0.3, radiating all round | length = Q / (εσT⁴·πd) | Kilometres of wire in about eight big loops. Small cross-section, roughly indifferent to attitude. Each loop is a loop circuit. |
| Droplet sheets | Tin sheet, effective ε ≈ 0.6, both faces | A = Q / (2εσT⁴), about 0.6 kg/m² plus generator and collector | Very light. Limited to about 0.001 g. Unbreakable by bursts in the prototype, because droplets recirculate. |
| Radiating skin | Hull skin with coolant, one face | A = Q / (εσT⁴) | An aft barrel on spine or shell; the whole cone on the apex cone. Cannot double as armour. |
| Sleeve outlet | Insulated tube around the ship; a hot plate inside the open aft end radiates like a cavity | aperture A = Q / (σT⁴) | Heat leaves only into the aft cone, which gives directional stealth. Tube about 12 kg/m². Only practical at low waste heat. |

Every radiator is made of loop circuits. Damage that breaks a circuit stops the coolant flow, and that region cools. The report shows capacity lost. Folded panels mean the reactor runs at housekeeping power.

## Armour

### Zones and layers

- **Zones:** nose, side envelope, citadel, umbrella, bumpers, spun belt, rubble jacket, coil shield and sleeve tube. Each zone's mass is reported separately.
- **Layer stack to model in C#,** outside in. The prototype used a single skin over a single core.
  1. Bumpers at standoff. Several thin plates beat one thick plate.
  2. A sacrificial low-Z layer, for X-ray ablation and lasers.
  3. The main wall, which is density-led at hypervelocity. Penetration goes as L·√(ρp/ρt), so the mass needed scales as √ρt: low density is more mass-efficient but bulkier. Report the trade rather than pick a winner.
  4. A spall liner.
  5. A hydrogenous neutron layer.
- **Gaps:** filled with low-density stuffing (aerogel) as an option. CoaDE players find filled gaps often beat empty ones.

### Layouts

| Layout | What carries armour |
| --- | --- |
| Envelope | The whole crew space on a spine; the whole shell on a shell. |
| Citadel | A thin skin everywhere, and the side armour on a tube around crew, reactor controls and magazine. Tanks outside are expendable. |
| Tanks forward | Propellant ahead of the crew is the frontal shield, hydrogenous when it is hydrogen. Report protection at full and at empty tanks. |
| Rubble jacket | About 2 m of bagged regolith (≈ 1,500 kg/m³) around the crew space. Free local mass in the belt; feeds the dependency curve. |

### Frontal protection

- **Umbrella:** shield radius = 1.15 × the widest body radius, standing off ahead of the nose on struts. Its cover half-angle is reported, atan((R_u − R_body) / distance). Mass grows with the radius squared, so an umbrella over wide strap-on tanks gets very heavy, and that is reported.
- **Bumpers:** spaced 0.6 × standoff apart, radius covering the frontal silhouette. Tandem precursor rounds can defeat them, so they are a counterable choice.

### Laser defence by spin

- **Dwell spread:** a spinning surface spreads a beam over (2πR · f) / spot. The prototype assumes a 0.25 m spot, a placeholder until the beam study exists. Contra-rotating shells roughly double it; nose wobble adds about 3–4×.
- **Spin does nothing against kinetics.** Repeated hits unbalance a spun shell.
- **Roll the whole ship:** report rim acceleration ω²R and gyroscopic resistance to turning. Panels can't stay edge-on.
- **Decoupled belt:** a rotating armour shell around the citadel on bearings. Assumed contra-rotating, so it adds no net angular momentum.

## Crew shelter

- **Size:** 2.5 m³ per crew member; crew = clamp(2 + payload/50 t, 2, 80).
- **Layers, outside in:** about 1 m of water (borated in C#), then a 2 cm tungsten liner, then the couches. The liner sits inside the water because water captures neutrons and emits hard capture gammas, which the high-Z layer stops.
- **Shape:** a sphere when the crew space allows it, otherwise a cylinder of the same volume. The prototype costs it as a sphere either way; C# should cost the real shape.
- **Mass example:** a 2.5 m radius sphere in 1 m of water ≈ 114 t of water.
- **Lifeboat:** the shelter plus a motor and a separation ring (+20 %, +5 t). A surviving crew is a distinct outcome from a lost ship.
- **Uses:** the water jacket doubles as drinking water, coolant reserve and emergency reaction mass. Time to general quarters is a readiness number, like missile staging time.

## Hab rings

- **Size:** 0.4 g at 3 rpm gives R ≈ 40 m, with a 2.5 m tube, four spokes and a hub.
- **Pair:** counter-rotates and cancels angular momentum. A single ring adds gyroscopic resistance.
- **Use:** intended for liners and long-haul civilian ships; reported as a large soft target on anything armed.

## Fittings

- **Missiles:** an internal magazine, about 3 m³ per round, and side hatches. Each hatch stages one round per cycle (3 s placeholder): open the rail, cold-push the round out at about 1.6 m/s, reset. Rounds coast clear and ignite together. Hatch count sets staging time, not swarm size. On a rolling ship, rounds leave with the rim's tangential velocity.
- **Turrets and sensors** mount on the crew-space surface. The pressure-hull radius sets their position and facing.
- **Coilgun:** spinal, along the axis through the nose.

## Report

The minimum report the C# designer should produce. Every number is live as levers move.

- **Mass:** wet, dry, propellant, combat mass after drop tanks; breakdown by system and armour by zone.
- **Propulsion:** Δv (and cap), thrust, jet power, reactor thermal, acceleration full and empty, full-burn time, kinetic energy at half Δv.
- **Heat:** waste heat, radiator type, area and mass, fin efficiency, layout, and capacity lost after damage.
- **Agility:** moment of inertia, 180° flip time on RCS, gyroscopic factor, spin rim acceleration, laser dwell spread.
  - Prototype rule: RCS sized for 3 cm/s², acting as a couple at the ship's ends. C# should use real thruster blocks.
- **Exposure:** the umbrella cover cone, and the share of radiator area facing a given threat direction, averaged over a roll if spinning.
- **Crew:** crew count, shelter, and dose estimates inside and outside the shelter for a reference burst.
- **Remarks:** the physical penalties from "Three kinds of conflict", phrased as consequences, never as refusals.

## Thermal and damage hooks

The prototype already carries what later systems read. Keep the contracts.

- **Canonical thermal nodes:** every part has nodes (vertices at the same position merged) with area and normal.
  - Hull parts have a skin layer and a core layer, with conduction between them and across the surface.
  - Radiators have one thin layer and a circuit index per node.
  - Nozzles and plates have a "hot when burning" target.
- **Integration:** implicit radiation cooling (Newton on T + c·T⁴), exact skin–core exchange, explicit lateral conduction with sub-steps. Same at any time compression.
- **Bursts:** one source-neutral deposition pass. Fluence ∝ partition × yield / 4πr² × cos θ, with shadowing from simple occluder primitives (cylinders and discs per part), and ablation above the vaporisation temperature with blow-off impulse.
  - C# should replace the occluders with the real hitbox.
  - It should also apply the impact-cloud and beam models from the research agenda through the same deposition event.
- **Dose:** the prototype uses kerma-style coefficients with exponential attenuation, separating metal and hydrogenous layers (gamma λ ≈ 250 kg/m²; neutrons λ ≈ 600 metal, 120 hydrogenous). These are order-of-magnitude placeholders for the "Radiation and the crew" study.
- **Look:** the look reads node temperatures as black-body colour (Planck at three wavelengths, camera exposure) or an IR palette. It never invents or hides heat.

## Looks (later)

Looks are indexed by polity and style and only dress parts. The prototype tried five as data-driven material sets:
- Bare engineering
- Earth fleet grey (paint, panel lines, hull bands, registry)
- Chartered company (weathered livery, hazard banding, stencil)
- Low-signature coat (matte black; IR shows it hides nothing)
- Schematic (fills by system, outlines)

Panel lines, bands, weathering and markings came from a small shader pass over ship-local coordinates, not geometry. Keep that separation, and iterate the component visuals once the physical model is settled.

## What the prototype faked (to do properly in C#)

- **Fixed-count mass iteration** and a flat structure fraction. **Drop tanks** as a fixed 60 % fraction.
- **Shelter mass** costed as a sphere even when it becomes a cylinder.
- **Occlusion:** approximate primitives, and approximate for parts that spin separately.
- **Single-layer armour** (skin + core) instead of the layer stack. No real Whipple physics yet; bumpers are mass and occluders only.
- **Wire-loop geometry** drawn as eight thick bundles; their real cross-section is about 1 mm.
- **Every block number,** including drives, radiator constants, laser spot, RCS capability and dose coefficients. These wait for the Atomic Rockets survey and the Tier 1 studies.
- **Turn time** from a lumped mass list rather than the real part inertia.

## Open questions

- [ ] Armour layer stack as a designer input: per zone, or one stack with per-zone thickness?
- [ ] Shelter capacity: the whole crew, or a duty crew while others are elsewhere?
- [ ] Do drop tanks need their own small structure and attachment mass in the hitbox, and can they be shot off early?
- [ ] Spun belt bearings: failure modes when hit (seizure, imbalance), and their effect on turning.
- [ ] Radiator types as tech blocks (wire, droplet fluids, fin materials) rather than fixed constants.
- [ ] How faceting, flattening and taper feed the drag-free but laser-relevant surface angles in the beam model.
- [ ] Should "Tanks forward" also be possible on a spine, with tanks ahead of the crew module?
