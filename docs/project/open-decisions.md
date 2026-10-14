# Unresolved decisions

Architecture choices in ADRs are confirmed. The following engineering and school decisions
remain open; owners are roles, not inferred assignments of an active chat.

| ID | Decision / artifact | Owner | Blocks |
| --- | --- | --- | --- |
| D1 | Exact ESP/C3/camera/LiDAR/motors/driver/battery, availability, budget, pins and power sheet | Motion + integration | Wiring and builds |
| D2 | Front steering geometry, actuator/feedback, limits, turning radius and rear-speed calibration | Motion + localization | Control and pose |
| D3 | Rotating ToF mechanism, measured/estimated angle, wiring, rate/coverage and stale-sector policy | Motion + integration | Scanner and obstacle claims |
| D4 | Direct C3 radio, identities, inputs/deadman, final ESP owner/lease/epoch/re-arm protocol | Motion + C3 + server | Integrated driving |
| D5 | WiFi/bench framing/authentication, replay/session behavior, watchdog/leases, physical emergency stop and braking | Motion + server | Safe floor trials |
| D6 | LiDAR sensor/bridge/electrical compatibility, bandwidth, timing and reliability | Server acquisition | Untethered mapping |
| D7 | Laptop OS/toolchains and pinned model/projector/runtime/API, bounded queues and concurrent resource budget | AI + server | Real inference |
| D8 | School approval: paired independent subsystems, controller Internet exchange, exact deadlines and assessment | Students + supervisor | School acceptance |
| D9 | Capture trigger/timing uncertainty, storage/retention, categories and measured model thresholds | Events + AI | Useful advisory events |
| D10 | Arena geometry/speed/load, stop timing reference, pose metric/sample count, map-quality criteria | Test + students | Acceptance evidence |
| D11 | Resolve two live proposal versions and engineering checklist wording against accepted ADRs | School writing + user | Current official submission |

Do not finalize timing constants or packet formats from checklist examples. Propose them
with rationale, hardware bounds and a test plan, then record reviewed approval.
The migration creates draft application schemas only; it does not close these decisions.

Confirmed: one laptop; rotating ToF; front steering; C3 direct to ESP32; no downward sensors.
User decisions override conflicting proposal technical direction; official school wording
still requires a deliberate document update. See [source audit](sources.md).

## GitHub work queue

| Issue | Task |
| --- | --- |
| [#2](https://github.com/yotam1001/project/issues/2) | Review motion hardware, front steering and rotating-ToF wiring before implementation |
| [#3](https://github.com/yotam1001/project/issues/3) | Specify and review final ESP32 authority across direct C3 and laptop links |
| [#4](https://github.com/yotam1001/project/issues/4) | Select and validate untethered LiDAR acquisition and timestamping |
| [#5](https://github.com/yotam1001/project/issues/5) | Verify Clef-Flash Q8_0 image runtime and concurrent laptop resource budget |
| [#6](https://github.com/yotam1001/project/issues/6) | Align the official proposal with current architecture and verify school acceptance requirements |

Begin with #2 hardware/interface review. Issues #3 and #4 depend on those hardware bounds.
The migration branch is the review baseline until its PR merges; these tasks are not completed.
