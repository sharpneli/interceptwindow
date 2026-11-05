# Intercept Window: Strategic Beams – X-ray and Gamma FELs

Nov 2, 2026 · @Teemu

A deep dive on the end point of the laser ladder: free electron lasers (FELs) pushed to hard X-ray and gamma-ray wavelengths, as fixed installations that could threaten much of the inner solar system. The question is how far such a beam really reaches, what limits it, what it does when it arrives, and what a target can do about it. Companion to [`studies/weapons-survey-long-range-concepts.md`](weapons-survey-long-range-concepts.md); feeds the beams study in [`studies/research-agenda.md`](research-agenda.md).

Numbers are first-cut estimates computed from standard scaling laws and a few real data points. The structure is the part to keep.

## The short version

- **Diffraction stops being the limit.** At 1 MeV the wavelength is about 10⁻¹² m, a million times shorter than an infrared laser's. Even a millimetre-wide beam with no optics at all spreads to only about 120 m at 1 AU.
- **Three other limits take over, in this order:**
  - **the picture:** the shooter can't aim better than its sensors can fix the target, about 15 km at 1 AU even for the best network in [`design/detection-and-the-picture.md`](../design/detection-and-the-picture.md);
  - **the bloom:** in the 1,000 s round trip at 1 AU, a target jinking at only 10⁻³ m/s² can be anywhere in a 500 m sphere;
  - **pointing:** holding 1 m at 1 AU needs about 7 picoradians, far beyond anything built.
- **So a strategic beam sweeps boxes, it doesn't snipe.** The cost of a kill is the lethal fluence times the box area.
- **Gamma rays make sweeping affordable,** because they kill crews and soft electronics with very little energy per square metre. About 320 J/m² of 1 MeV gammas gives 1 Gy in water. A lethal 10 Gy over a 15 km box is about 0.7 TJ: 7 s at 100 GW.
- **Structure is almost immune.** Gamma beams don't burn holes efficiently. They are a radiation weapon, a "neutron bomb on a beam".
- **The physics allows a gamma FEL; the engineering is far off.** 1 MeV photons need about 40–70 GeV electrons and a beam quality 10–100× better than today's. Today's X-ray FELs deliver watts on average; a weapon needs gigawatts.
- **The installation can't hide.** At percent-level efficiency a 1 GW beam means about 100 GW of waste heat, visible across the inner system. It is a fixed, known, high-value target.

## Why shorter wavelength reaches further

Spot diameter is about 2.44 λ R / D for an aperture D. If optics existed at every wavelength, a 10 m aperture would give:

| Wavelength | At 1,000 km | At 1 light-second | At 0.1 AU | At 1 AU | At 30 AU |
| --- | --- | --- | --- | --- | --- |
| CO₂ infrared, 10.6 µm | 2.6 m | 780 m | 39 km | 390 km | 12,000 km |
| Near-infrared, 1.06 µm | 0.26 m | 78 m | 3.9 km | 39 km | 1,200 km |
| Ultraviolet, 250 nm | 6 cm | 18 m | 910 m | 9 km | 270 km |
| Soft X-ray, 10 nm | 2 mm | 0.7 m | 37 m | 370 m | 11 km |
| Hard X-ray, 0.1 nm (12 keV) | — | 7 mm | 0.4 m | 3.7 m | 110 m |
| Gamma, 1 MeV | — | — | 5 mm | 5 cm | 1.4 m |
| Gamma, 10 MeV | — | — | — | 5 mm | 14 cm |

**The catch: there are almost no optics below about 1 nm.**

- **Soft and hard X-rays** can be reflected only at grazing incidence. Chandra-style nested mirrors reach about a metre across. So an X-ray beam can be expanded to roughly 1 m, not 10 m.
- **Gamma rays** have no practical mirrors or lenses at all (crystal diffraction lenses exist but are tiny and inefficient). The beam is as wide as its source.

With realistic optics:

| Beam | Effective aperture | Spot at 1 light-second | At 0.1 AU | At 1 AU |
| --- | --- | --- | --- | --- |
| Hard X-ray (0.1 nm), 1 m grazing-incidence expander | 1 m | 7 cm | 3.7 m | 37 m |
| Gamma 1 MeV, 1 mm source, no optics | beam waist | 0.24 m | 12 m | 120 m |
| Gamma 1 MeV, 1 cm source, no optics | beam waist | 2.4 cm | 1.2 m | 12 m |
| Gamma 10 MeV, 1 mm source, no optics | beam waist | 2.4 cm | 1.2 m | 12 m |

(No-optics divergence is λ / (π w₀) for a beam waist w₀; spot diameter is twice that times range.)

Even without optics, X-ray and gamma beams put spots of metres to a hundred metres at 1 AU. Diffraction has stopped mattering.

## What limits it instead

### Pointing

To keep a spot on a target of size d at range R, the beam must point to about d / R:

| Range | Pointing for a 1 m spot |
| --- | --- |
| 1,000 km | 1 µrad |
| 1 light-second | 3 nrad |
| 0.1 AU | 70 prad |
| 1 AU | 7 prad |

For scale, Hubble-class pointing stability is tens of nanoradians. And the shooter can only aim at where it *sees* the target: an IR image's centroid is good to about (λ/D) / SNR, tens of nanoradians for a big telescope. The beam can be far sharper than the shooter's eye.

### The picture

[`design/detection-and-the-picture.md`](../design/detection-and-the-picture.md) gives triangulated fixes of about 15 km at 1 AU for two 0.1 µrad telescopes an AU apart, and about 2,200 km for a 10⁶ km baseline. That fix error is the aim error. The beam's own 120 m spot is irrelevant next to it.

### The bloom

The shooter sees the target as it was R/c ago, and the beam arrives R/c later. In that round trip of 2R/c, the target's reachable sphere has radius ½ a (2R/c)²:

| Range | Round trip | 10⁻⁴ m/s² | 10⁻³ m/s² | 10⁻² m/s² | 0.1 m/s² | 1 g |
| --- | --- | --- | --- | --- | --- | --- |
| 10 light-seconds | 20 s | 2 cm | 20 cm | 2 m | 20 m | 2 km |
| 0.1 AU | 100 s | 0.5 m | 5 m | 50 m | 500 m | 49 km |
| 1 AU | 1,000 s | 50 m | 500 m | 5 km | 50 km | 4,900 km |
| 5 AU | 83 min | 1.3 km | 13 km | 130 km | 1,300 km | 120,000 km |

- **Stations and habitats** can afford 10⁻⁴–10⁻³ m/s² of random station-keeping. That inflates a 1 AU shot from a point to a 50–500 m sphere: a real but modest defence.
- **Ships under thrust** are out of reach of point aiming beyond about 0.1 AU.
- **Coasting ships that don't know they're targeted** are as predictable as stations, until they jink.

### So: sweep the box

Since the beam can't hit a point, it covers the uncertainty region. Required energy:

**E ≈ F_kill × A_box,  A_box ≈ π (σ_picture² + r_bloom²),  F_kill = dose × (fluence per Gy) × 2^(shield / HVL)**

The sweep is only affordable if the kill fluence is low. That is what makes gamma rays the interesting case.

## What gamma rays do on arrival

Gamma rays don't stop at the surface. They lose energy along a path tens of centimetres long in water or hull material, depositing dose in everything they cross.

From NIST attenuation data for water:

| Photon energy | Half-value layer in water | Fluence for 1 Gy | Character |
| --- | --- | --- | --- |
| 10 keV (soft-ish X-ray) | ~1.3 mm | — | Surface heating and ablation, like a laser |
| 100 keV | ~4 cm | — | Shallow volumetric |
| 1 MeV | ~10 cm | ~320 J/m² | Deep, hull-penetrating |
| 2 MeV | ~14 cm | ~380 J/m² | |
| 5 MeV | ~23 cm | ~520 J/m² | |
| 10 MeV | ~31 cm | ~640 J/m² | Hardest to shield |

(Half-value layers from μ/ρ; fluence per Gy from μ_en/ρ. Narrow-beam values; build-up and pair-production secondaries ignored.)

**Hard X-rays are surface weapons; gammas are volume weapons.** A 12 keV X-ray FEL heats the first millimetre and drives ablation, a long-reach version of an ordinary laser. A MeV gamma beam irradiates the crew and electronics inside.

### Rough damage thresholds

Placeholders for the radiation-and-crew and electronics-vulnerability studies:

| Effect | Dose (Gy) |
| --- | --- |
| Likely fatal over weeks, untreated | ~5–10 |
| Incapacitation within minutes to hours | tens to ~100 |
| Commercial electronics degraded | ~100–1,000 |
| Radiation-hardened electronics | ~10³–10⁶ |
| Structural damage by heating | far higher; not the mechanism |

### Energy to sweep a box (1 MeV, unshielded)

| Target dose | 1 km box | 15 km box | 100 km box |
| --- | --- | --- | --- |
| 10 Gy (crew lethal) | 3 GJ · 0.03 s at 100 GW | 0.7 TJ · 7 s | 32 TJ · 5 min |
| 1,000 Gy (crew down fast, soft electronics) | 0.3 TJ · 3 s | 73 TJ · 12 min | 3.2 PJ · 9 h |
| 10,000 Gy (hardened electronics) | 3.2 TJ · 32 s | 730 TJ · 2 h | 32 PJ · 4 days |

Read with the bloom and picture tables: a gamma installation that can fix a station to 1 km kills its crew almost instantly; one that can fix a ship only to 100 km needs minutes even for the crew, and can't reach hardened electronics at all.

### Shielding changes everything

Each half-value layer doubles the required fluence. A crew behind 1 m of water or propellant:

- **at 1 MeV:** about 10 half-value layers, ×1,000 the fluence;
- **at 10 MeV:** about 3 half-value layers, ×9 the fluence.

So the photon energy is a real design trade. Higher energy needs a bigger accelerator but defeats shielding. Ships already carry shadow shields against their own reactors; propellant tanks and water walls become armour against gamma beams, and orientation matters.

### Atmospheres are shields

- **Earth:** the air column is about 1,000 g/cm², dozens of attenuation lengths. A gamma beam deposits its energy in the upper atmosphere; nothing reaches the ground.
- **Mars:** about 16 g/cm², roughly one attenuation length. Partial shelter.
- **Airless bodies, stations and ships:** fully exposed.

Planetary surfaces under real atmospheres are safe from gamma beams. Lunar, asteroid and orbital targets are not. (Lasers have their own weather; kinetics don't care.)

## Can it be built?

### The FEL ladder

An FEL's wavelength is set by the electron energy and the undulator: λ ≈ λ_u (1 + K²/2) / (2γ²). With a 1–3 cm undulator period and K ≈ 1:

| Photons | Wavelength | Electron energy needed | Beam quality needed (normalised emittance) | Today |
| --- | --- | --- | --- | --- |
| Hard X-ray, 12 keV | 0.1 nm | 4–8 GeV | ≲0.1 µm at 8 GeV | Done (EuXFEL, LCLS, SACLA) |
| Gamma, 1 MeV | 1.2 pm | 40–70 GeV | ≲0.01 µm at 50 GeV | No |
| Gamma, 10 MeV | 0.12 pm | 130–220 GeV | ≲0.003 µm at 150 GeV | No |

(Beam quality requirement from the lasing condition: geometric emittance ≲ λ / 4π. Today's best injectors are around a few tenths of a micron; to be verified in the beams study.)

**Where real machines are:**

- **European XFEL** reaches photon wavelengths down to about 0.05 nm from a linac of up to 17.5 GeV. Its 2020 performance paper reports pulse energies up to 2 mJ and 6 W of average beam power.
- **High-power FELs** exist at long wavelengths: Jefferson Lab's energy-recovering IR FEL delivered 14.3 kW at 1.6 µm, with about 1.5 % extraction efficiency. The Navy funded it for shipboard defence.
- **Plasma accelerators** shrink the linac: Berkeley's BELLA reached 7.8 GeV in a 20 cm capillary in 2019. Beam quality and repetition rate are the open problems.

**The gap to a weapon:**

| Parameter | Today (X-ray FEL) | Gamma weapon |
| --- | --- | --- |
| Photon energy | ~25 keV | ~1–10 MeV |
| Average beam power | ~10 W | ~1–100 GW |
| Efficiency, wall-plug to beam | well under 1 % | a few % at best, even with energy recovery and tapering |
| Waste heat for 1 GW beam | — | ~30–100 GW |

That makes the gamma FEL a late-era tech block, not a near-future one.

### Other routes to gamma beams

- **Inverse Compton sources** bounce laser light off an electron beam and are real today. One compact design makes 10–20 MeV gammas in a footprint of about 4 × 22 m. But the gammas come out in a cone of roughly 1/γ (milliradians for a few hundred MeV electrons, by my estimate), so they're a short-range floodlight, not a long-range beam.
- **Grasers** (gamma lasers from nuclear isomers) have been chased since the 1960s. Vitaly Ginzburg listed one among the thirty most important problems in physics. The difficulty, sometimes called the graser dilemma, is that the conditions for gain and for enough excited nuclei seem incompatible, and there are no gamma mirrors. Recent proposals look at isomers driven by petawatt-class lasers. A Los Alamos 1979 report explored a nuclear-explosive-pumped graser: Excalibur's gamma cousin. Treat as speculative tech.

## What a gamma installation can threaten

| Target | Picture error | Bloom at 1 AU | Verdict |
| --- | --- | --- | --- |
| Station or habitat, known orbit, no jitter | metres–km (well tracked) | ~0 | Highly exposed, crew killable in seconds |
| Station with 10⁻³ m/s² jitter | km | ~500 m | Exposed; jitter barely helps against the picture error |
| Airless surface base | metres (fixed) | ~0 | Exposed unless buried under regolith (≈ shielding) |
| Earth-surface target | — | — | Safe behind the atmosphere |
| Coasting ship, tracked | ~15 km (best network) | ~0 until it jinks | Killable in seconds to minutes if unshielded |
| Burning ship at 0.1 m/s² | 15 km+ | ~50 km | Expensive; crew kill costs tens of TJ |
| Ship at 1 g | — | ~5,000 km | Out of reach at 1 AU; in reach within ~10 light-seconds |
| Sensors, solar arrays, radiators | fixed, known | ~0 | Cheap kills; electronics are the soft spot |

## Counters

In rough order of cost to the defender:

1. **Shielding:** water, propellant or regolith between the beam and what matters. Doubles the attacker's cost per half-value layer.
2. **Jitter:** random station-keeping, cheap for stations; mostly useful once the attacker's picture is good.
3. **Occlusion:** stay behind a planet or moon relative to the installation, or under an atmosphere.
4. **Spoil the picture:** kill or blind the attacker's sensors; spoof with decoys. A worse fix means a bigger box and a quadratically higher cost.
5. **Distance:** the box grows as R² from the picture and as R⁴ from the bloom. Cost of a kill climbs very steeply with range.
6. **Kill the installation:** it is huge, fixed, hot and visible; the obvious first-strike target. It has its own beam for self-defence, which is why deterrence is likely.
7. **Hardening:** rad-hard electronics turn a 10 Gy problem into a 10⁴ Gy one, ×1,000 the cost.

## Suggested game model

- **The threat is a continuous function, never a range circle.** For each target, the installation's cost to kill is E = F_kill × A_box, and time to kill is E / P. "In range" is a UI label on that, like the picture's labels.
- **Inputs are physical blocks:**
  - photon energy (from electron energy): sets the penetration and shielding trade;
  - beam quality: sets whether it lases at that wavelength at all, or falls back to an incoherent, short-range source;
  - average power and efficiency: set time to kill and the installation's waste heat;
  - source size and pointing stability: set the floor on the spot, rarely the binding limit;
  - the polity's picture of the target: usually the binding limit.
- **Damage reads the hit contract per target.** Dose to compartments by path length through shielding; crew and electronics take the damage, structure mostly doesn't.
- **The installation is a strategic asset like the big telescopes:** few, expensive, known, and the anchor of a polity's reach.

## Suggested era placement

| Era | Short-wavelength beams |
| --- | --- |
| Fission / NTR | Soft X-ray from bomb-pumped rods only (one-shot, see the survey) |
| Fusion | Hard X-ray FEL research installations; anti-sensor and anti-satellite use at ~10⁵–10⁶ km |
| Torch | Hard X-ray FEL weapons with grazing optics; first inverse-Compton gamma floodlights for point defence |
| Late torch / beyond | Gamma FELs as strategic installations; inner-system reach limited by the picture and sweep energy |

## Open questions

- [ ] Verify today's best normalised emittance and the scaling of FEL efficiency with tapering and energy recovery.
- [ ] Dose thresholds, time to incapacitation and electronics hardness levels (radiation-and-crew and electronics studies).
- [ ] Build-up factors and pair-production secondaries in real shield stacks; whether 10 MeV beams create dangerous secondary showers inside hulls.
- [ ] Sweep pattern: raster against statistical spray against re-fix after each pass, and the resulting kill probability.
- [ ] Should the X-ray and gamma beams also serve as lidar (they're coherent and precisely pointed), shrinking their own picture error?
- [ ] Waste-heat model for an FEL installation, and its detection signature.

## Sources

- FEL performance: [European XFEL overview](https://cavac.at/cavacopedia/European%20XFEL); [Decking et al. 2020, MHz-repetition-rate hard X-ray FEL](https://documenta.ciemat.es/items/a4bb6400-a095-40f5-a9d0-82f589b4e343/full); [EuXFEL very hard X-ray experiments, IPAC 2024](https://accelconf.web.cern.ch/ipac2024/pdf/MOPG48.pdf).
- High-power FEL and energy recovery: [The Development of Energy-Recovery Linacs](https://arxiv.org/pdf/2207.02095).
- Plasma acceleration: [Berkeley Lab, 7.8 GeV in 20 cm](https://newscenter.lbl.gov/2019/02/25/laser-drill-sets-a-new-world-record-in-laser-driven-electron-acceleration/).
- Inverse Compton gamma sources: [Placidi et al., compact FEL-driven ICS gamma source](https://accelconf.web.cern.ch/fel2019/papers/thp012.pdf).
- Grasers: [Wikipedia, Gamma-ray laser](https://bafybeiemxf5abjwjbikoz4mc3a3dla6ual3jsgpdr4cjr3oz3evfyavhwq.ipfs.4everland.io/wiki/Gamma-ray_laser.html); [Solem, On the feasibility of an impulsively driven gamma-ray laser (LANL, 1979)](https://www.osti.gov/servlets/purl/6010532); [laser-driven isomer graser proposal, arXiv 2503.15224](https://arxiv.org/pdf/2503.15224).
- Gamma attenuation: [NIST X-ray mass attenuation coefficients, water](https://physics.nist.gov/PhysRefData/XrayMassCoef/ComTab/water.html).
- Long-range laser installations for comparison: [Lubin et al., Toward directed energy planetary defense](https://dspace.mit.edu/handle/1721.1/88427).
