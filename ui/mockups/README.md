# UI Mockups

Nov 8, 2026 · @Teemu · mockup v0.2

Interactive HTML mockups of the game's main screen: a full-screen 3D map of the solar system with floating windows. They are the visual and interaction reference for building the real UI, as Fleetwright's UI was built from its HTML mockups. They were made on a claude.ai design canvas, and the `.dc.html` files here are byte-identical copies of the canvas boards.

## Open them

Open `index.html` in a browser for all four boards side by side, or open a board on its own for full-size, real mouse input. No server or build step is needed; `file://` works. Fonts come from Google Fonts and fall back to system fonts offline.

| Board | What it shows |
| --- | --- |
| [`Main.dc.html`](Main.dc.html) | The map with the UI hidden: four translucent plates and a report ticker. Interactive |
| [`Local.dc.html`](Local.dc.html) | Unit windows open at the Moon: TF Kestrel, Shackleton Depot, UNSA Resolute, track U-0412 |
| [`Transfer.dc.html`](Transfer.dc.html) | The transfer planner as a window, with its preview arc on the system map |
| [`Input.dc.html`](Input.dc.html) | The input grammar, window rules, zoom bands, symbols and colour tokens |

`Local` and `Transfer` embed `Main` with a preset (`init-windows=units` or `transfer`). Any preset or camera can be opened directly, e.g. `Main.dc.html?init-windows=units&init-focus=tf-kestrel&init-log-d=5`.

## What is real and what is placeholder

- **Real:** body positions from [`data/solar-system/bodies.csv`](../../data/solar-system/README.md) on Kepler rails; Lambert transfers for the porkchop plot and the window strip (checked to about 10 m closure over a 400-day arc); light-time ages; closest-approach searches.
- **Placeholder:** the scenario (date 2043-01-20, fleets, stations, contacts, log entries), ship stats, the Ceres traffic envelope, burn durations and the classification numbers.
- **Not in the mockup:** the ship designer (a full-screen tool), the ledger and polity screens, and the engagement and ship zoom bands' contents.

## Files

| File | What it is |
| --- | --- |
| `*.dc.html` | The boards, in the canvas's Design Component format: markup with `{{holes}}`, `<sc-for>`, `<sc-if>` and a `DCLogic` class |
| `canvas.json` | The canvas index: board layout and titles |
| `support.js` | dc-lite, a small open-source stand-in for the canvas runtime, so the boards run outside claude.ai |
| `vendor/preact.min.js` | Preact 10.24.3, the renderer dc-lite uses (MIT licence in `vendor/preact-LICENSE.txt`) |
| `dc-data.js` | The body catalogue in the compact form the boards fetch; generated |
| `make_dc_data.py` | Rebuilds `dc-data.js` from `bodies.csv` |
| `index.html` | The gallery page |

## Updating from the canvas

Copy the changed `.dc.html` files and `canvas.json` from the canvas over these. Keep `support.js`: the canvas serves its own runtime under that name, and this one stands in for it. If a board starts using a canvas feature dc-lite lacks (a new tag or attribute rule), extend `support.js`. If the catalogue changes, rerun `make_dc_data.py`.

## Design decisions recorded here

The rules sheet (`Input.dc.html`) is the written summary. The main ones:

- **Clicks follow Fleetwright:** left-click selects, right-click acts, and an armed order is confirmed with the left button and cancelled with the right.
- **Camera:** never free. It always centres on an object. Middle-click centres on what is under the cursor, the wheel zooms logarithmically toward it, and dragging orbits around it.
- **Windows, not panels:** the map fills the screen. Selecting opens the object's window as a preview that the next selection replaces; pinning keeps it. Delete closes every unpinned window, as in Transport Tycoon.
- **Unit windows open on a live vignette** of the ships or station, so the map rarely needs to zoom that close. Foreign ships show registry imagery and tracks show only the sensor's blob.
- **Only the ship designer and similar tools take the full screen.**
