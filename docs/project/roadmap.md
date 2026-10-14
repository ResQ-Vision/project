# Roadmap and dependencies

Dates are planning context from 12 October chats, not independently verified school deadlines.
Proposal submission: around 15 October 2026 (school-specific, confirm).
Progress book: around 19 November 2026 (provisional user report).
Final deadline: one week after Passover 2027; exact day and school interpretation pending.
No date is assigned to a hardware milestone without parts/capacity evidence.

| Stage | Work | Exit evidence | Dependencies |
| --- | --- | --- | --- |
| 0 | Review BOM, front steering/scanner, wiring/power, authority, links | Approved interface and wiring/power sheets | Open D1–D5, school compliance |
| 1 | Motion ESP bench feedback and independent stops | Raw local-stop/reset/timeout tests with wheels raised | Stage 0 safety/hardware |
| 2 | Laptop, LiDAR bridge and ESP CAM bench | Timestamped validated scans/images/telemetry; bounded load | Stage 0 links, contracts |
| 3 | Direct C3 + browser manual integration | Single ESP authority; measured forward/reverse/turning stops | Stages 1–2, arbitration |
| 4 | Front-steering localization and initial occupancy map | Surveyed pose errors, scanner angles, map comparison | Calibrated chassis + acquisition |
| 5 | Bounded autonomous obstacle response | Five defined collision-free trials and fault injection evidence | Validated stops/pose/map |
| 6 | Stored events and advisory local AI | Correct event association, unknown failures, actual labeled-image/load metrics | Model/runtime and bounded interface |
| 7 | Acceptance and school handover | Reproducible run records, full-system student bring-up, engineering/AI logs | Baseline tests and supervisor requirements |

- [ ] Confirm exact proposal/progress/final deadlines with school.
- [ ] For the progress book, report architecture, literature, BOM gaps and authentic work completed.
- [ ] Demonstrate a separate Internet exchange appropriate to the school's paired-controller requirement.
- [ ] Close hardware, protocol and safety blockers before floor/autonomous driving.
- [ ] Evaluate A*/scan matching/video only after baseline gates and separate scope review.

This is a checklist, not a claim that any stage has passed. Track concrete work in
GitHub issues using [open decisions](open-decisions.md); completed tests go in evidence records.
