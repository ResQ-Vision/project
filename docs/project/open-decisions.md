# Unresolved decisions

Architecture choices in ADRs are confirmed. The following engineering and school decisions
remain open; owners are roles, not inferred assignments of an active chat.

| ID | Decision / artifact | Owner | Blocks |
| --- | --- | --- | --- |
| D1 | Hiwonder V1.2 / STM32F407 selected; LD-1501MG confirmed; rear motor model inferred; battery accepted. V1.2 drivers/pins/rails, C3/camera/LiDAR details and wiring sheet remain open | Motion + integration | Wiring and builds |
| D2 | Front steering geometry, actuator/feedback, limits, turning radius and rear-speed calibration | Motion + localization | Control and pose |
| D3 | Separate ToF/rotation mechanism removed by user; LiDAR coverage/timing validation remains under D6/D10 | Integration | ToF selection is no longer a blocker |
| D4 | Direct C3 radio, identities, inputs/deadman, final STM32 owner/lease/epoch/re-arm protocol | Motion + C3 + server | Integrated driving |
| D5 | STM32 untethered-link/bench framing/authentication, replay/session behavior, watchdog/leases, physical emergency stop and braking | Motion + server | Safe floor trials |
| D6 | LiDAR sensor/bridge/electrical compatibility, bandwidth, timing and reliability | Server acquisition | Untethered mapping |
| D7 | Laptop OS/toolchains and pinned model/projector/runtime/API, bounded queues and concurrent resource budget | AI + server | Real inference |
| D8 | School approval: paired independent subsystems, controller Internet exchange, exact deadlines and assessment | Students + supervisor | School acceptance |
| D9 | Capture trigger/timing uncertainty, storage/retention, categories and measured model thresholds | Events + AI | Useful advisory events |
| D10 | Arena geometry/speed/load, stop timing reference, pose metric/sample count, map-quality criteria | Test + students | Acceptance evidence |
| D11 | Align engineering checklist and review working-proposal illustrations/layout against accepted ADRs; working URL selected | School writing + user | Current official submission |

Do not finalize timing constants or packet formats from checklist examples. Propose them
with rationale, hardware bounds and a test plan, then record reviewed approval.
The migration creates draft application schemas only; it does not close these decisions.

D11 progress, 14 October: the user corrected the target to
[the official working proposal](https://docs.google.com/document/d/1_ZeKJPhYXvrlZp5wWuPeibg2ie_6kLH27qAnhqbATOU/edit).
That document's text/tables were corrected directly; proposal selection is resolved.
See [source review](../school/source-review-2026-10-14.md). Checklist alignment,
illustration/layout review and school acceptance remain open; issue #6 is not completed.

Confirmed: one laptop; front steering; C3 manual path to STM32, bypassing laptop; transport TBD; LiDAR-only distance sensing; no separate ToF or downward sensors. See [ADR 0005](../architecture/decisions/0005-lidar-only-distance-sensing.md).
User decisions override conflicting historical proposal direction. The working proposal's
prior alignment predates ADR 0006; STM32/servo/motor wording and diagrams require a new review. See [source audit](sources.md).

## GitHub work queue

| Issue | Task |
| --- | --- |
| [#2](https://github.com/ResQ-Vision/project/issues/2) | Is the Hiwonder V1.2 STM32 board electrically compatible with our chassis? |
| [#3](https://github.com/ResQ-Vision/project/issues/3) | How will STM32 enforce control ownership across C3 and laptop links? |
| [#4](https://github.com/ResQ-Vision/project/issues/4) | Select and validate untethered LiDAR acquisition and timestamping |
| [#5](https://github.com/ResQ-Vision/project/issues/5) | Verify Clef-Flash Q8_0 image runtime and concurrent laptop resource budget |
| [#6](https://github.com/ResQ-Vision/project/issues/6) | Align the official proposal with current architecture and verify school acceptance requirements |
| [#9](https://github.com/ResQ-Vision/project/issues/9) | Can we build V1.2 firmware and demonstrate independent local stops? |
| [#10](https://github.com/ResQ-Vision/project/issues/10) | Target-laptop image-runtime smoke test; first slice of #5 |
| [#11](https://github.com/ResQ-Vision/project/issues/11) | Read-only server status/event API review; enables server/web consumers |

PRs #7 and #8 are merged; latest `main` is the review baseline. No decision D1–D11
is closed by the PM audit. D11 has the partial proposal progress recorded above.
Begin engineering with #2; #3/#4 require its hardware bounds. Run #6 school follow-up,
#10 AI compatibility and #11 read-only API review independently. See [roadmap](roadmap.md).

21 October update: [ADR 0006](../architecture/decisions/0006-stm32-motion-controller.md)
selects the Hiwonder STM32 board. Battery sufficiency is accepted from the owner and is
not an open selection blocker. Firmware access/toolchain, board/chassis electrical
compatibility, wireless/C3 transport and physical stopping remain unverified (#2/#3/#9).
The old ESP32 candidate wiring chart is superseded; do not reuse its pin matrix.
