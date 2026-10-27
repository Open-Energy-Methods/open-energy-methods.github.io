# Open Energy Methods — website

Official GitHub Pages site for the **Open Energy Methods** early-stage open-source scientific software initiative.

**Site:** https://open-energy-methods.github.io/  
**Repository:** https://github.com/Open-Energy-Methods/open-energy-methods.github.io

## Architecture
Static HTML/CSS, no JavaScript build step, no telemetry or cookies. GitHub Pages deploys from the repository root of the `main` branch when Pages is configured to use `Deploy from a branch`. The `.nojekyll` marker disables Jekyll processing.

- `index.html` — public landing page.
- `assets/site.css` — responsive styles based on the supplied OEM design tokens (navy #0C2B47, teal #3B787E, IBM Plex / Outfit).
- Brand mark is served from the canonical SVG maintained in `Open-Energy-Methods/.github/assets/brand`.

## Local preview
```sh
python -m http.server 8000
# open http://localhost:8000/
```

## Updating content
Preserve scientific claim boundaries: EnerLint is an experimental alpha, not an accredited certification service or industrially validated technology. Label planned capabilities as planned. Keep all project links grounded in the public repositories. Do not publish the founder's confidential research bible, business assumptions, or personal circumstances here.

## Publishing
In GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: main / (root)**, then save. The site URL is the organization's GitHub Pages domain.

Copyright in OEM logos belongs to their respective owner(s); the separately maintained brand repository governs their use. This site content is not a license grant for the brand artwork.
