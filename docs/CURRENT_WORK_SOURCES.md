# Current-work evidence register — Open Energy Methods

**Page snapshot date:** 27 October 2026  
**Status:** descriptive public-source compilation, not a peer review or a scientific meta-analysis.  
**Scope:** `index.html` and `projects/index.html` only. Each source remains authoritative for its own study design, input assumptions, software status and licensing. Links may change after this snapshot.

| Project | Repository ownership | Source of quantitative claims | What the numbers do **not** establish |
|---|---|---|---|
| [EnerLint](https://github.com/Open-Energy-Methods/enerlint) | OEM org repo | [Foundation results (27 Oct)](https://github.com/Open-Energy-Methods/enerlint/blob/main/docs/RESULTS.md), [protocol](https://github.com/Open-Energy-Methods/enerlint/blob/main/docs/BENCHMARK_PROTOCOL.md), [roadmap](https://github.com/Open-Energy-Methods/enerlint/blob/main/docs/ROADMAP.md) | No real-world detection rate, formal independent review, distribution, external validation or certification. |
| [ThermoTwin-F](https://github.com/abhijith-sivaprasadan/thermotwin) | Creator's personal repo | [Source-only v2.0.0-beta.1 release](https://github.com/abhijith-sivaprasadan/thermotwin/releases/tag/v2.0.0-beta.1), [DOI 10.5281/zenodo.23679426](https://doi.org/10.5281/zenodo.23679426), [release gate](https://github.com/abhijith-sivaprasadan/thermotwin/blob/main/docs/RELEASE_GATE.md), [property comparison](https://github.com/abhijith-sivaprasadan/thermotwin/blob/main/docs/INDEPENDENT_BENCHMARKS.md) | DOI and CI do not establish measured-plant validation, IF97 compliance, GUI acceptance or industrial qualification. |
| [OpenSteamOpt](https://github.com/abhijith-sivaprasadan/opensteamopt) | Creator's personal repo | [README reference table](https://github.com/abhijith-sivaprasadan/opensteamopt), [hashed reference manifest](https://github.com/abhijith-sivaprasadan/opensteamopt/blob/main/artifacts/reference/manifest.json), [verification](https://github.com/abhijith-sivaprasadan/opensteamopt/blob/main/docs/VERIFICATION.md), [model card](https://github.com/abhijith-sivaprasadan/opensteamopt/blob/main/docs/MODEL_CARD.md) | Synthetic comparator improvement is not real savings, emissions reporting, operational optimization or safety validation. |
| [Kerala2040](https://github.com/abhijith-sivaprasadan/kerala2040) | Creator's personal repo | [Evidence freeze 23 Oct](https://github.com/abhijith-sivaprasadan/kerala2040/blob/main/docs/RESEARCH_FREEZE_2026-10-23.md), [source register](https://github.com/abhijith-sivaprasadan/kerala2040/blob/main/docs/evidence_register.md), [ML robustness](https://github.com/abhijith-sivaprasadan/kerala2040/blob/main/docs/DAILY_DEMAND_ML_ROBUSTNESS_V0_2.md) | Not complete hourly/15-min measured telemetry, operational shortfall attribution, causal weather effect, multi-year forecasting or bankable 2040 scenarios. |

## Editorial rules

1. **Do not equate evidence tiers.** EnerLint synthetic residual checks, ThermoTwin cross-implementation numerical comparisons, OpenSteamOpt synthetic optimization fixtures, and Kerala2040 official-source audits answer different questions.
2. **Specify what is being counted.** EnerLint 6/6 is a count of prespecified mutations; OpenSteamOpt percentages are relative to an author-built comparator; Kerala2040 FY annual consumer-side and SLDC daily operational totals are different series.
3. **Never promote a result by implication.** A DOI is citable archiving; a successful CI run is software execution; neither implies formal review or observed industrial performance.
4. **Preserve personal-repo ownership.** Linked ThermoTwin-F, OpenSteamOpt and Kerala2040 are **not** claimed as OEM-owned repositories, modules, commercial products or projects with independent external contributors.
5. **Update deliberately.** Before changing public figures, re-open the linked source at its latest applicable tag/freeze and update page snapshot metadata. For release claims use the exact release tag and commit rather than branch-level results alone.
6. **Publish corrections.** Report errors in [website issues](https://github.com/Open-Energy-Methods/open-energy-methods.github.io/issues). Keep the previous text in git history.

## Current research directions, not product promises

Real independent comparisons of EnerLint with incumbent diagnostics, validated parameter/property references for ThermoTwin-F, calibrated plant data for OpenSteamOpt and measured interval-level operations evidence for Kerala2040 remain **uncompleted** or explicitly outside current accepted public findings. They should not appear as shipped functionality.
