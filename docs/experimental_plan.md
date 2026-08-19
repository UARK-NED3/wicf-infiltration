# Proposed partner experiment: WICF door-open infiltration

## Objective

Test whether door-open duration, adjacent-room psychrometrics, pressure, door geometry, and infiltration controls predict event refrigeration burden sufficiently well to select escalation-alarm thresholds with acceptable nuisance burden.

## Test blocks

| Block | Hypothesis | Controlled comparison | Primary response |
|---|---|---|---|
| Baseline | Event burden increases after flow establishes. | 5, 15, 30, 60, 120 s held-open events; no traffic. | Integrated event load and recovery time. |
| Adjacent-room state | Warmer/more humid air increases event burden. | At natural operating variation or controlled HVAC states. | Latent/sensible thermal balance; frost/condensate indicator. |
| Door protection | Protection changes effective exchange, not merely alarm behavior. | Door only; strip curtain; approved alternative. | Calibrated exchange/load ratio relative to door only. |
| Traffic/pressure | Traffic and pressure can dominate buoyancy-only predictions. | Empty vs representative passage; documented pressure states. | Model residual and peak recovery demand. |

## Minimum instrumentation and data contract

- Door state: magnetic/reed switch or equivalent, ≥1 Hz, synchronized time base; log each open/close event.
- Air state: adjacent inventory room and WICF dry-bulb/RH at ≥1 Hz; document sensor calibration and placement.
- Differential pressure: room-to-WICF, range adequate for expected Pa-scale differences, ≥1 Hz.
- Refrigeration response: circuit electrical power and, if available, suction/discharge/evaporator air state; identify compressor/controller state.
- Context: door dimensions, curtain type/state, traffic type/count, product staging, shift, defrost state, and maintenance faults.

Do not publish raw facility telemetry, employee/video data, store identifiers, layouts, or proprietary controls without an agreed data-rights and de-identification plan.

## Analysis and acceptance criteria

Pre-register event windows (e.g., 5 min pre-open through return to a stated steady criterion), estimate uncertainty, and hold out whole doors/days/shifts for validation. A candidate alarm policy should report false-alarm rate, missed long-open events, percentile door-open duration, energy/load proxy, recovery time, and operational/safety feedback. The first model upgrade should be a calibrated reduced-order event model; CFD is justified only if measured residuals show geometry/traffic effects that the reduced-order model cannot represent.

## No-go gates

- No operational setpoint from simulated load alone.
- No inference of product temperature or food safety without product-temperature measurements and the relevant operational standard.
- No claimed curtain energy credit without a matched measured comparison.
- No generalization across stores/doors without a held-out-site validation split.
