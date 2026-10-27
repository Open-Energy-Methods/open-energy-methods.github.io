# Open Energy Methods — website

GitHub Pages home for **Open Energy Methods**, an independent open-source engineering research workbench created and maintained by Abhijith Sivaprasadan. It publishes projects, experiments, numerical models, reusable methods and technical field notes.

This is deliberately **not** written like a startup brochure. See the [editorial voice guide](https://github.com/Open-Energy-Methods/.github/blob/main/docs/EDITORIAL_VOICE.md) before adding or rewriting public copy.

**Site:** https://open-energy-methods.github.io/  
**Repository:** https://github.com/Open-Energy-Methods/open-energy-methods.github.io

## Architecture
Static HTML/CSS, no JavaScript build step, no telemetry or cookies. GitHub Pages deploys from the repository root of the `main` branch when Pages is configured to use `Deploy from a branch`. The `.nojekyll` marker disables Jekyll processing.

- `index.html` — creator-maintained engineering workbench and experiment overview.
- `notes/001-a-pass-isnt-proof.html` — worked technical field note explaining a compensating error missed by conservation-only checks.
- `assets/site.css` — responsive styles based on the supplied OEM design tokens (navy #0C2B47, teal #3B787E, IBM Plex / Outfit).
- Brand mark is served from the canonical SVG maintained in `Open-Energy-Methods/.github/assets/brand`.

## Website UI/UX issues

See the [prioritized UI/UX backlog](docs/UI_UX_BACKLOG.md) and [website issue tracker](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues). Issues are grouped by P0/P1/P2 impact and estimated engineering effort. File website bugs here, and EnerLint scientific/code bugs in the [EnerLint tracker](https://github.com/Open-Energy-Methods/enerlint/issues).

## Local preview
```sh
python -m http.server 8000
# open http://localhost:8000/
```

## Updating content
Write from concrete questions, experiments and evidence rather than mission-statement templates. Use the creator's own voice (first person when appropriate), but never invent biographical anecdotes. Preserve scientific claim boundaries: EnerLint is an experimental alpha, not an accredited certification service or industrially validated technology. Label planned capabilities as planned. Keep all project links grounded in the public repositories. Do not publish the founder's confidential research bible, business assumptions, or personal circumstances here.

## Publishing
In GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: main / (root)**, then save. The site URL is the organization's GitHub Pages domain.

Copyright in OEM logos belongs to their respective owner(s); the separately maintained brand repository governs their use. This site content is not a license grant for the brand artwork.
