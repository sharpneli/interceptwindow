# Intercept Window

**Intercept Window: Nothing Beyond the Sun** is a solar-system space combat, colonisation and economics game. It aims for realism in the near- and medium-term future. The game itself will be built in this repo later; for now the repo holds the design and research docs.

## Where things are

- `research/README.md` is the index of every doc. Start there.
- `research/design/` holds decisions and proposals: what the game does.
- `research/studies/` holds the research behind them: surveys, physics and sourced numbers about the real world.
- `research/studies/solar-resources/` holds the baseline of what resources exist where in the solar system.

This repo is the master copy of the docs. Their old copies in the claude.ai project "Intercept Window" are frozen as of Nov 5, 2026, so edit the docs here, not there.

## Before designing anything

Read these first:

1. `research/design/intercept-window-initial-design-notes.md`
2. `research/design/fleetwright-principles-for-intercept-window.md`
3. `research/studies/prototype-readiness-gap-analysis.md`

The rules that recur everywhere:

- **Physics is the only final limit.** Near-present blocks must match engineering data; far-future blocks only have to respect physics. That is the realism gradient, and deviations are logged as exceptions in the Fleetwright principles doc.
- **No hard cutoffs.** Quantities vary smoothly with their inputs. Labels such as "detected", "in range" or "hilarious" are words on a continuous number, never levels in code.
- **The designer never refuses.** It builds the design and reports the consequences.
- **Deterministic.** The same inputs give the same result.
- **Mass is conserved exactly** (`research/design/mass-ledger-element-groups-and-conservation.md`).
- **Players and AIs see a picture, never the truth** (`research/design/detection-and-the-picture.md`).
- **The world never fails globally early on.** Failure belongs to a badly run actor (`research/design/from-contracts-to-markets-starting-actors-and-the-transition.md`).

## Writing docs

- Write docs as Markdown with kebab-case filenames. Put each in `design/` or `studies/` according to what it is, and add it to `research/README.md`.
- Link other docs with relative links. A backticked path that isn't a link names a doc that has been proposed but not written yet.
- Each doc opens with a title line, then `date · @author · status`, then a short summary. Next comes a "The short version" section; open questions go in a checklist near the end and sources come last.
- Mark figures computed for a doc as *(calc)*, and tag numbers by basis (demonstrated, studied, physics-only) where that matters.
- Numbers are first-cut placeholders unless sourced. The structure (laws, what limits what) is the part to keep.
- Write short sentences in plain English, with lists and tables where readers will scan.
