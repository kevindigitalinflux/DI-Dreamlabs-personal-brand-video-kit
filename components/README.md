# Components

Ready-to-use Hyperframes sub-compositions for 1080x1920 reels. Each is one HTML file you can read and edit.

| File | What it does |
|---|---|
| `hook-giant.html` | The first spoken line as four large rows that slam in on their words |
| `logo-row.html` | A title card plus up to four tool or partner tiles with logo slots |
| `checklist.html` | Three outcomes with ticks |
| `pay-board.html` | Counting salary rows with ADVERTISED / TYPICAL tags and a permanent honesty footer (example figures only) |
| `offer-card.html` | Sale card that builds line by line, ends on the URL and holds to the last frame; logo slot in the brand line |
| `brand.css` | Shared styles and the colour and font variables |
| `make-captions.mjs` | Word timings to 1-to-3-word caption clips for the low band |
| `instantiate.mjs` | Builds a demo project from `brand.json` |

## Try it

```
node components/instantiate.mjs brand/brand.example.json videos/component-demo
cd videos/component-demo
node <launcher> check --timeout 60000 --json
node <launcher> preview
```

`<launcher>` is the Hyperframes plugin's pinned `scripts/plugin-cli.mjs` (see `SETUP.md`). The demo uses placeholder logos (A, B, C, D and Y) and a grey stand-in for the presenter.

## Use YOUR logo

1. Put your logo in `brand/logos/` (git-ignored) and copy it to the project's `assets/logos/` as `primary.svg` (or `.png`; then edit the `src` in `offer-card.html`).
2. For the logo row, replace `logo-a.svg` to `logo-d.svg` and the labels with your tools or partners, or delete an `<img>` and keep the text.
3. Logos sit on the light tile only. Never on the accent colour. Use a logo you do not own only with written permission.

## Using a component in a real video

Copy the file into your project's `compositions/`, mount it in `index.html` the way `instantiate.mjs` does (a `div` with `data-composition-src`), and set `data-beats` to the frame numbers (30 fps, counted from the start of the component) of the spoken words, taken from your word timings. A logo starts 3 frames before its word. Every effect must start on its word. Duplicate a file and rename its id prefix to use it twice.

Replace all example text and figures. Every salary figure needs a source and a posting-day re-check.
