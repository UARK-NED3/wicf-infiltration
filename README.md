# WICF door-infiltration screening analysis

This repository contains a **screening-level**, reproducible analysis for deciding when a walk-in cooler/freezer (WICF) door-open alarm deserves experimental evaluation. It models buoyancy-driven, two-way doorway exchange and the sensible-plus-latent refrigeration load introduced by warmer, more humid air.

Repository scope, evidence, and reuse boundaries are also available in the
[NED3 resource manifest](.ned3/resource-manifest-v0.1.json).

## What this is—and is not

- **Decision:** identify a defensible starting range for a *door-open escalation alarm* and the measurements needed before setting an operational alarm.
- **Evidence class:** simulated/derived results using transparent assumed geometry and a public weather sensitivity dataset. No Walmart, HFA, facility, product, alarm-log, door-cycle, or energy data are included or implied.
- **Not a setpoint:** outputs are not safety, food-quality, or operational alarm requirements. A door-open alarm must preserve egress, loading, and process requirements and be validated at the intended site.

The reported baseline is a personnel door opening from a 24 C, 50% RH inventory room into a 2 C cooler or -18 C freezer. The 2025 Bentonville, AR daily reanalysis dataset is a separate climate sensitivity input—not a claim about actual room conditions.

## Preliminary result

With the default 0.90 m × 2.10 m doorway and an effective exchange multiplier of 0.40 (a deliberately explicit, unvalidated representation of obstructions/curtains), the model predicts that the 3 s flow-establishment time is important, but that cumulative refrigeration load rises rapidly after it. The generated report provides the exact values.

**Screening recommendation:** evaluate an escalating alert at 15–30 s and a high-priority/alarm condition at 45–60 s for these baseline configurations. Treat this only as a testable starting hypothesis: a higher effective exchange coefficient, larger doorway, direct outdoor exposure, or a dehumidified/more-protective vestibule can move the proper threshold materially.

## Run

Requires Python 3.10+ and no third-party packages.

```powershell
py -3 scripts/run_screening.py
py -3 -m unittest discover -s tests -v
```

The first command regenerates `results/summary.csv`, `results/climate_sensitivity.csv`, `results/door_open_load.svg`, and `reports/preliminary_results.md`. The public data input is already cached under `data/raw/`; its source URL, retrieval date, license/status, and SHA-256 are recorded in [`data/DATA_MANIFEST.md`](data/DATA_MANIFEST.md).

## Model boundary

The model treats the open doorway as a vertical, two-layer, buoyancy-driven exchange. It does not resolve people, pallets, forklifts, traffic-induced flow, HVAC pressurization, wind, frost, product thermal mass, refrigeration-control response, or strip-curtain mechanics. Consequently, it is suitable for scenario ranking and experimental design—not load sizing or guaranteed energy savings.

## Proposed partner test

See [`docs/experimental_plan.md`](docs/experimental_plan.md) for the instrumentation, test matrix, acceptance metrics, and no-go conditions. The minimal dataset is synchronized door state, room/WICF temperature and RH, differential pressure, traffic state, and refrigeration electrical/load response.

## Sources

- ASHRAE, *Refrigerated-Facility Loads*, Chapter 24 (2022): door-open fraction, 3 s flow-establishment evidence, and infiltration-load context. Accessed 2026-08-19. <https://handbook.ashrae.org/Handbooks/R22/SI/R22_Ch24/R22_ch24_si.aspx>
- U.S. DOE, *Walk-In Coolers and Walk-In Freezers*: definition and current federal context. Accessed 2026-08-19. <https://www.energy.gov/cmei/buildings/walk-coolers-and-walk-freezers>
- U.S. DOE, 2024 WICF final rule: prescriptive infiltration-minimizing methods including strip doors and spring-hinged doors. Accessed 2026-08-19. <https://www.energy.gov/sites/default/files/2024-11/wicf-ecs-fr-pdf.pdf>
- Open-Meteo Historical Weather API / ERA5-family reanalysis input, cached exactly as retrieved. <https://open-meteo.com/en/docs/historical-weather-api>

## License

Code and repository-authored documentation are released under the MIT License. The external data remains subject to its provider terms; see the manifest.
