# Open Energy Methods — website UI/UX backlog
**Baseline:** 27 October 2026.  
**Source of truth:** [GitHub Issues](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues). This page is an index, not a separate issue tracker.

## Current workbench direction
OEM is an independent engineering research workbench, **created and maintained by Abhijith Sivaprasadan**. Its priority for 2026–27 is publishing real projects, numerical models, experiments, reusable methods and field notes. EnerLint is its first project, not its exclusive scope. Company formation, customer acquisition and commercialization are not website success metrics. See the [workbench strategy tracker](https://github.com/Open-Energy-Methods/.github/issues/25).

## Prioritization method
An editorial **ROI ranking**, not an empirically quantified business ROI or a guaranteed time-to-deliver. Rank = expected benefit to the first-time visitor, scientific credibility, accessibility and maintainer effort **relative** to estimated effort/risk. Reassess after accessibility and user testing.

- **P0 — Fix first:** Visible layout/accessibility/interaction risk; likely high benefit or a trust issue.
- **P1 — High-leverage build:** Onboarding, scientific communication, evidence context, developer workflow and regression automation.
- **P2 — Polish/scale:** Lower urgency until more pages and visitors exist.

Effort ranges and acceptance tests live in the individual issues. Issues tagged P0/P1/P2 in their titles because issue-label availability may vary.

## P0 — critical and very high ROI (9)
| Issue | Workstream |
|---|---|
| [#1](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/1) | Viewport inset and sticky-header validation |
| [#2](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/2) | Mobile menu dismissal |
| [#3](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/3) | Tablet header collisions |
| [#4](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/4) | Keyboard accessibility |
| [#5](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/5) | Zoom and reflow |
| [#6](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/6) | Mobile table scrolling |
| [#7](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/7) | Link checker CI |
| [#8](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/8) | Serve OEM logo locally |
| [#9](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/9) | Hero hierarchy |

## P1 — valuable follow-on improvements (18)
| Issue | Workstream |
|---|---|
| [#33](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/33) | Project index with actual repositories and ownership boundaries |
| [#34](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/34) | Publication template for projects, numerical experiments and methods |
| [#35](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/35) | Field-note index and reproducible publishing workflow |
| [#10](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/10) | First-time visitor onboarding |
| [#11](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/11) | Copy install commands |
| [#12](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/12) | EnerLint detail page |
| [#13](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/13) | Input → check → result walkthrough |
| [#14](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/14) | Traceable research roadmap |
| [#15](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/15) | About and governance |
| [#16](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/16) | Scientific issue templates |
| [#17](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/17) | Synchronized release status |
| [#18](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/18) | Social-preview image |
| [#19](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/19) | Reusable CSS components |
| [#20](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/20) | Automated accessibility CI |
| [#23](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/23) | Viewport screenshot regression |
| [#24](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/24) | Performance budgets |
| [#25](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/25) | Evidence-status vocabulary |
| [#26](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/26) | Readable typographic rhythm |

## P2 — deferred polish and scale (6)
| Issue | Workstream |
|---|---|
| [#27](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/27) | Branded 404 |
| [#28](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/28) | Site provenance policy |
| [#29](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/29) | Font/third-party request audit |
| [#30](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/30) | Sitemap/canonical CI |
| [#31](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/31) | UI pattern library |
| [#32](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/32) | Multi-page information architecture |

## Suggested first five
1. **[#1](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/1)** Confirm viewport inset and sticky offsets against real screenshots (the CSS fix has been committed; testing is open).
2. **[#3](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/3)** Prevent collisions on laptop/tablet navigation.
3. **[#2](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/2)** Make mobile menu dismissal intuitive.
4. **[#4](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/4)** Fix focus/keyboard issues before adding new interactions.
5. **[#8](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/8)** Serve logo and favicon from versioned local assets; eliminate hotlink failure point.

For the new publishing direction, start **[#33](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/33)** as soon as the responsive basics are sound; it improves the site's usefulness more directly than corporate-style About or growth sections.

In parallel, **[#7](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues/7)** helps ensure that links to live science documentation never silently rot.

## Scientific content guardrails
Open Energy Methods is an **independent, creator-maintained engineering research workbench**. EnerLint is its **first experimental alpha project**, with limited exported-output residual checks. Future research may include other areas of computational energy engineering, not only verification. We do not claim external benchmarking success, validation with physical measurements, engineering certification, real paying clients, affiliations or releases not present in the public project source. Present planned features as *planned*.

## Current housekeeping
- CSS viewport inset was committed on 27 October 2026; acceptance remains tracked by #1.
- #21 and #22 were closed as duplicate issue submissions, superseded by #19 and #20.
