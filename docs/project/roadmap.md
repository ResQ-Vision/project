# Roadmap and dependencies

## Verified baseline — 14 October 2026

Audit base: `main` at `1c27925da3e05a563f790b1aa9a120e3b9bee149`.
PRs [#1](https://github.com/ResQ-Vision/project/pull/1),
[#7](https://github.com/ResQ-Vision/project/pull/7) and
[#8](https://github.com/ResQ-Vision/project/pull/8) are merged.
Documentation, approved architectural direction, seven proposed data schemas and CI exist.
Firmware, server, web, localization/navigation and AI runtime are not implemented.
[Main CI](https://github.com/ResQ-Vision/project/actions/runs/38523894541) passed;
a fresh Python 3.11 checkout reproduced the repository check and two synthetic contract
tests (12 valid and 16 invalid fixtures). No bench, full-system or model benchmark evidence exists.
The recorded live-proposal correction is partial progress on #6; this audit did not reread the live document.
No GitHub milestones exist; the stages below are development gates, not scheduled commitments.

Current approved change: [ADR 0005](../architecture/decisions/0005-lidar-only-distance-sensing.md) removes the separate ToF and its rotation mechanism. Distance sensing now uses LiDAR; its bridge/coverage/timing validation remains open. Active contracts now contain six schemas and 24 fixtures; the original audit counts above are historical.

Current controller decision, 21 October: [ADR 0006](../architecture/decisions/0006-stm32-motion-controller.md)
replaces motion ESP32 with Hiwonder V1.2 STM32F407. Battery sufficiency is owner-accepted.
Prioritize V1.2 source/schematic/factory-image access and build/flash/restore, actual
motor/servo/driver compatibility, then wireless/C3 authority and local-stop bench evidence.
The ESP32 EasyEDA chart is superseded reference material, not the STM32 wiring plan.
The retained camera/C3 roles do not establish their transport to this board. No implementation
milestone is passed by this documentation change.

## Dates and submission

The school-specific proposal date around 15 October 2026 and progress-book date around
19 November 2026 remain provisional user reports. The current-year circular extraction,
page 18, states 30 October for coordinator submission; verify the original PDF and school
internal date through [#6](https://github.com/ResQ-Vision/project/issues/6).
Final submission is reported as one week after Passover 2027; exact day is unconfirmed.
No hardware milestone date is assigned without parts/capacity evidence.

## Milestones

| Stage | Current state / work | Exit evidence | Dependencies |
| --- | --- | --- | --- |
| Foundation | Documentation and draft-contract CI merged | Reproduced repository/fixture checks | Complete for this limited scope |
| 0 | Open: hardware/power, steering/LiDAR mounting and authority review | Approved wiring/power and interface sheets | #2, #3; school acceptance #6 |
| 1 | Not started: motion STM32 independent-stop bench slice | Raw wheels-raised contact/reset/command-loss/stall results | #9 after #2 and #3 |
| 2 | Not started: laptop, untethered LiDAR and camera bench | Validated timestamped scans/images/telemetry; bounded load | #4, hardware-specific contracts/toolchains |
| 3 | Not started: direct C3 + browser manual integration | One STM32 owner; measured forward/reverse/turning stops | Stages 1–2, approved #3 protocol |
| 4 | Not started: front-steering localization and initial occupancy map | Surveyed pose errors, LiDAR mount/coverage and map comparison | Calibrated chassis, timing and acquisition |
| 5 | Not started: bounded autonomous obstacle response | Five defined collision-free trials and fault evidence | Validated stops/pose/map; D10 test definitions |
| 6 | Not started: persisted events and advisory local AI | Correct association, unknown failures, labeled-image and load metrics | #5, #10, D9 and reviewed data interfaces |
| 7 | Open: school acceptance and final integration | Reproducible full-system records, student bring-up and engineering/AI logs | Baseline tests, approved subsystem split and Internet exchange |

Stages are dependency gates, not a rigid serial schedule: AI compatibility and read-only
API review may start before physical mapping. Schema checks do not pass hardware gates.

## Next priorities and parallel work

1. #6: confirm immediate submission date, official version, illustration/layout review,
   paired subsystem acceptance and actual controller Internet exchange. Keep #6 open.
2. #2: record actual components, pins/power, steering/LiDAR mounting mechanics and independent
   disable behavior. #3 may draft now but cannot finalize rates/watchdogs without hardware bounds.
3. #3 → #9: review authority/freshness/re-arm, then build and measure the first local-stop slice.
4. #4: validate a bridge against the actual LiDAR; a USB bench link is not an untethered solution.
5. #10 → #5: establish real image-runtime compatibility before adapter/accuracy/concurrent-load work.
6. #11: review the read-only status/event API; then create focused server-replay and web-display
   implementation tasks against its merged version.

Independent tracks now: hardware review #2, school/evidence #6, target-laptop AI smoke #10,
and read-only API review #11. LiDAR candidate research can proceed, but selection/testing
needs the actual sensor. Use separate branches/worktrees and one coordinated contract PR.
C3/server motion consumers depend on #3; server/web read-only consumers depend on #11.

Integration risks: incompatible direct-C3/laptop authority; blocking sensor/bus work delaying
local stops; front-steering geometry mistaken for differential drive; LiDAR stale/limited coverage;
USB/radio and clock mismatch; image/pose association errors; AI load starving server/control;
and school Internet requirements confused with same-WLAN or local AI traffic.

Detailed acceptance criteria stay in Issues, with decisions in [open decisions](open-decisions.md).
Full SLAM, A*, video and presentation polish remain secondary to the baseline gates.
