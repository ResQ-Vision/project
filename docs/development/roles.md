# Independent development roles

These are ownership boundaries, not a requirement to create ten permanent chats.
Combine roles when useful, but keep each PR focused. Core student ownership from the
proposal: Yotam leads motion/sensors; Ilay leads laptop/camera/mapping/AI; both integrate.

| Role | Owns | Handoff / dependency |
| --- | --- | --- |
| Integration and architecture | docs/project, ADRs, issue dependencies | Approved requirements/contracts; review cross-module changes |
| Motion / hardware safety | firmware/motion-stm32, wiring/calibration evidence | Rear feedback + front steering + local stops; command/telemetry fixtures |
| Manual controller | firmware/manual-c3 | Direct C3 intent/authority integration; same freshness/safety gate as laptop |
| Camera | firmware/esp-cam | Capture IDs, timing/quality and bounded images; fixtures to server |
| Server communications/control | server communication/control/telemetry/API | Validate both adapters, coordinate server intent, observe final STM32 authority |
| Localization / mapping | server localization/mapping | Front-steering model, timestamped pose/scan quality, unknown/free/occupied map |
| Navigation | server navigation | Conservative swept-footprint decisions; depends on validated stops/pose/map |
| Events and AI | server events, ai | Persist image/event first; bounded inference, unknown outcomes, no drive authority |
| Frontend | web | Show acknowledged owner, stop cause, freshness and uncertainty; manual intent to server |
| Validation and school evidence | tests, docs/school | Independent contract tests, physical evidence, engineering and AI-assistance logs |

Shared contracts belong to interface review; a module owner cannot silently revise a
neighbor's units, timestamps, states or packet format. Record blockers in issues.
Do not assume peer branches merged. Rebase/merge main and re-run affected tests when needed.
For concurrent schema edits, agree the contract PR first and regenerate examples/consumers
from that merged version. Resolve conflicts explicitly; never choose the newest file blindly.
