# Intercept Window: Naming Presets

Nov 8, 2026 · @Teemu · proposal

How ships, groups, stations and classes get their names. Every polity draws from a **culture preset**: a data file of themed name pools, one per category, with rules for prefixes, reuse and running out. Names are labels and never feed the sim, but a ship's registered name and prefix are political facts, so renaming and false registry entries are acts the world can see.

## The short version

- **A preset is data, not code.** It is a set of pools, one per category (warships, auxiliaries, survey ships, merchants, groups, stations, classes, settlements), each with a theme, a list of names and a rule for when the list runs out.
- **Category rules make a navy readable.** As the Imperial Japanese Navy named battleships after provinces and destroyers after weather, a preset gives each kind of hull its own theme. A player learns to read "what is this?" from a name, provided the name is known at all.
- **Presets layer:** culture, then polity, then company. A Finnish-sponsored charter takes the Kalevala preset and can override any pool.
- **The prefix follows the registered type,** not the physical ship. Registering an escort as a survey ship changes its prefix, and that lie is a rung-2 act ([Initial Design Notes](intercept-window-initial-design-notes.md), "Defiance is a ladder").
- **Names belong to the picture.** An unidentified track carries a designation from the sensor network (U-0412), never its true name. The name appears only once a transponder, registry match or identification supplies it.
- **Renaming is an event.** A charter that declares independence may rename its fleet, as navies did after independence. Observers then have to link the new names to the old signatures.
- **Deterministic:** names are drawn from their own seeded stream, so the same seed names the same fleet.

## Categories

| Category | Example from the Kalevala preset | Notes |
| --- | --- | --- |
| Warships | Väinämöinen, Ilmarinen, Lemminkäinen | Heroes and smiths; the most prestigious pool |
| Auxiliaries (tankers, tenders) | Sampo, Kantele | Objects and forces from the epic |
| Survey and science | Louhi, Tapio, Ilmatar | Wanderers, seers and spirits of the wild |
| Merchants and tugs | Kaleva 4, Kaleva 6 | A series name plus a number; merchants are many and cheap to name |
| Groups (task forces, trains) | Tuulihaukka (kestrel), Kotka (eagle), Joutsen (swan) | Birds; group names outlive their ships |
| Ship classes | Kantele, Aallotar, Tuuri, Kaira | Separate pool, or the first hull's name, by preset rule |
| Stations | Shackleton Depot, Ceres Hub | Site name plus function by default; habitats draw from a place pool (Pohjola, Sariola) |
| Settlements | from the place pool | Settlers may rename a town, which is a small political signal |

Track designations (U-0412) and registry numbers are not part of a preset. They come from the sensor network or registry that issued them.

## What a preset holds

```yaml
preset: kalevala
language: fi
gloss: en              # optional translations shown beside native names
prefix:
  armed: IWS           # chosen by registered type, not physical type
  merchant: MV
  survey: IRV
pools:
  warship:   { theme: heroes and smiths, names: [Väinämöinen, Ilmarinen, Lemminkäinen, Kullervo, Joukahainen, Ukko], exhaust: ordinal }
  auxiliary: { theme: objects of the epic, names: [Sampo, Kantele, Iku-Turso, Tuli], exhaust: ordinal }
  survey:    { theme: wanderers and seers, names: [Louhi, Tapio, Ilmatar, Mielikki, Pellervo], exhaust: ordinal }
  merchant:  { theme: series, series: [Kaleva, Pohja, Sariola], numbering: sequential }
  group:     { theme: birds, names: [Tuulihaukka, Kotka, Joutsen, Kurki, Korppi, Huuhkaja] }
  class:     { theme: instruments and spirits, names: [Kantele, Aallotar, Tuuri, Kaira], rule: pool }
  place:     { names: [Pohjola, Sariola, Tuonela, Kalevala] }
reuse:
  lost_names_return_after_years: 10
```

- **Exhaustion rules:** `ordinal` (Väinämöinen II), `series` (Kaleva 12) or `fallback` to a second pool. A pool never just stops.
- **Reuse:** a name stays reserved while its hull exists, and a lost ship's name returns to the pool after a delay, as navies honour lost ships. Reuse is a setting.
- **Native or translated:** each name is stored in the preset's language with an optional gloss. The player chooses whether the UI shows Tuulihaukka or Kestrel. The mockups used English group names; with the preset on they would be native.

## Worked preset: Kalevala

The national epic compiled by Elias Lönnrot (1835, expanded 1849). It suits a Finnish-sponsored charter well, and it has naval precedent: the Finnish Navy's coastal defence ships of the 1930s were *Väinämöinen* and *Ilmarinen*.

| Name | Who or what | Why it fits its pool |
| --- | --- | --- |
| Väinämöinen | The old sage and singer | Lead warship: wisdom and authority |
| Ilmarinen | The smith who forged the Sampo | Warship, or a shipyard's flagship |
| Lemminkäinen | The reckless hero | Fast, aggressive hulls |
| Kullervo | The tragic avenger | A warship name players will remember |
| Sampo | The mill that makes grain, salt and gold | Tanker or factory ship: the thing that makes wealth |
| Kantele | The instrument Väinämöinen made | Auxiliary or a class name |
| Louhi | Mistress of Pohjola, the north | Survey ship sent to cold, far places |
| Tapio, Mielikki | God and goddess of the forest | Survey and prospecting ships |
| Ilmatar | Spirit of the air, Väinämöinen's mother | Survey or sensor ships |
| Ahti | God of the waters | Fits the charter itself (Ahti Mining Charter) |
| Iku-Turso | A sea monster | Something nasty; also a Finnish submarine of the 1930s |
| Pohjola, Sariola, Tuonela | The north, its other name, the underworld | Stations and habitats; Tuonela for a far outer depot |

## Other presets to sketch

| Preset | Likely user | Category idea |
| --- | --- | --- |
| UN registry | UN Space Authority | Virtues for cutters (Resolute, Vigilant), cities and treaty names for larger hulls, scientists for survey ships |
| Martian | Tharsis Compact | Mars features: Olympus, Arsia, Pavonis for warships; valleys and craters for merchants |
| Norse | a Nordic consortium | Gods and ships of myth (Skíðblaðnir, Naglfar), ravens for scouts |
| Japanese, naval rule | a Japanese company | Provinces, mountains, rivers and weather, after the old navy's rules |
| Corporate | megacorps | Sponsor plus serial (Ventura Logistics 117), product lines as class names |
| Colonial | breakaway settlements | Settlement founders, local features, and renamed ships after independence |

## Rules that touch other systems

- **Looks never feed the sim** ([Fleetwright Principles](fleetwright-principles-for-intercept-window.md), section 9). A name changes nothing physical.
- **The registered type is a political label** (Fleetwright Principles, section 5). The prefix comes from it, so a false prefix is part of the same lie and is recorded the same way.
- **The picture holds names, not the truth** ([Detection and the Picture](detection-and-the-picture.md)). Each contact entry has a designation from the sensor network, and a name only with the source and confidence of its identification. A wrong name is a misidentification.
- **Renaming is recorded** like other acts: who renamed what, when, and who could see it. A mass renaming at independence is a signal other polities read.
- **Player edits are data.** The player can rename any ship or group, and edit or import presets. AI polities draw from the presets that suit their origin.

## Open questions

- [ ] Do classes default to their own pool or to the first hull's name? Proposal: a per-preset rule, with the pool as the default.
- [ ] Which presets ship with the first game? Proposal: Kalevala, UN registry, Martian and Corporate, enough to make the scenario battler's sides readable.
- [ ] Does a renamed ship keep a visible "ex-" name in the registry? Proposal: yes in the own polity's records, and in others' only when they have linked the identities.
- [ ] Do settlements pick names by vote or event once they gain constituency weight ([Bases, Settlements and the Civilian Economy](bases-settlements-and-the-civilian-economy.md))?

## Sources

- Elias Lönnrot, *Kalevala* (1835; expanded edition 1849): the names and roles in the worked preset.
- The Finnish coastal defence ships *Väinämöinen* and *Ilmarinen* (commissioned 1932 and 1934) and the submarine *Iku-Turso* (1931): precedent for Kalevala names on warships.
