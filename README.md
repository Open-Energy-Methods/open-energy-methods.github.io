# Open Energy Methods — research workbench website

Public home for **Open Energy Methods**, an independent open-source energy-engineering research workbench created and maintained by **Abhijith Sivaprasadan**. OEM is not a registered company, university lab or certification body.

**Live website:** https://open-energy-methods.github.io/

## Editorial direction

The site exists to publish and explain actual projects, numerical models, computational experiments, reproducible research methods and field notes. **EnerLint is the first OEM project, not the total scope.** Other linked personal repositories remain independently owned and maintained.

Read the [OEM editorial and evidence policy](https://github.com/Open-Energy-Methods/.github/blob/main/docs/EDITORIAL_VOICE.md). Avoid corporate promises, false qualifications, fictitious users, claims of measured detection rates or unexplained third-party code/data.

## Website structure

- `index.html` — workbench homepage, real project index, scientific method, in-browser demonstration, notes and creator profile.
- `notes/001-a-pass-isnt-proof.html` — documented synthetic negative control and science boundaries.
- `assets/site.css` — legacy component styles used by the notes page.
- `assets/workbench.css` — warm-paper design extension drawn from the approved OEM design-language references.
- `assets/workbench.js` — small accessible **browser-only demo** of one declared steady first-law energy residual, not the EnerLint library.
- `assets/brand/` — checked-in copies of approved vector artwork, maintained canonically in [the OEM brand library](https://github.com/Open-Energy-Methods/.github/tree/main/assets/brand).
- `docs/UI_UX_BACKLOG.md` — prioritized issues; the [website issue tracker](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues) is authoritative.

The browser example deliberately tests **one** first-law residual with equal inlet/outlet mass flow, within an illustrative 1 W threshold. It does not check measurements, phase models, correct system boundaries, solver convergence, mass closure independently, or model validation. No inputs are transmitted. For the genuine package, see [EnerLint](https://github.com/Open-Energy-Methods/enerlint).

## Design system

Inspired by the supplied **Open Energy Methods — Design Language / Soul**:
- Approved OEM navy and teal mark unchanged.
- Warm paper `#F6F1E5`, deep paper `#EDE6D4`, rule `#DAD1BA`, ink `#0C2B47`, teal `#3B787E`, reviewer pencil `#B04A26`.
- Outfit headings, IBM Plex Sans body, IBM Plex Mono numeric material, Newsreader editorial voice. Web fonts have system fallbacks.
- Pencil marks are editorial annotations, **never** status colors. PASS/FAIL/invalid uses a word and a distinct shape.
- No UI framework, analytics or hosted JavaScript dependencies.

## Local development

```sh
python -m http.server 8000
# visit http://localhost:8000/
```

Test both the homepage and field note at 360, 390, 768 and desktop widths. Test keyboard navigation, open/closed mobile menus, changed numeric values, invalid values, reset and the unbalanced-work negative control.

## GitHub Pages publishing

GitHub Pages deploys from `main` / root, with `.nojekyll` committed. `robots.txt` and `sitemap.xml` describe public pages. Work must be merged into `main` before the automated Pages deployment.

## Brand and rights

The logo is published under the brand owner's rights and is **not** relicensed by this site's source files. Preserve the approved logo's clear space, shape and source attribution. Any third-party code, data or assets brought into OEM requires a separate rights and provenance review.
