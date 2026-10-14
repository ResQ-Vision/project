# ResQ-Vision — exploration rover (planning project)

A two-student, five-unit high-school Electronics and Computers Engineering project. The planned prototype autonomously navigates a controlled arena, avoids obstacles, creates an initial planar map, and associates camera images with estimated observation positions. Image analysis is advisory, not a safety certification.

## Current architecture (updated from live proposal, 12 October 2026)

- **Motion ESP on rover:** motor-driver outputs, two encoder motors, IMU, left/right ToF, front/rear contact bumpers, wheel feedback and local stop on invalid or expired commands.
- **Navigation laptop beside the arena:** receives telemetry, LiDAR scans and ESP CAM S3 images; handles localization, initial 2D occupancy mapping, navigation, event storage and the browser backend.
- **ESP CAM S3:** separate image-capture module sending images to the laptop over WiFi.
- **2D LiDAR:** scans the arena plane. A compatible wireless acquisition bridge for untethered driving remains to be selected and tested; USB to laptop is for bench testing.
- **Manual C3 controller:** an additional proposed manual command source beside the browser, with explicit handover and one active controller at a time.
- **AI:** Cloudflare Clef-Flash Q8_0 is the intended advisory image-decision model, hosted in a separate worker on the **same navigation laptop**. Runtime compatibility and concurrent workload remain unmeasured.
- **Communication:** ESP telemetry and motion commands use WiFi when driving; USB serial is for tethered laboratory debugging. Browser access is via WiFi and WebSocket. Actual wireless message format, authentication and timing remain design/test work.

**There is no Raspberry Pi or separate home-PC inference host in the current architecture.** Previous documents and diagrams showing either are outdated. Local laptop AI calls alone do not meet the school's separate internet data-exchange requirement.

## Project limits

Initial goals: safe manual driving, obstacle avoidance, wheel odometry, an initial 2D map and map-linked camera events. Full SLAM, 3D mapping, complete autonomous coverage, actual hazardous-site operation, and verified AI hazard detection are not yet delivered or committed. The older cleaning-robot concept is archived only.

The proposal's figures of five collision-free trials, stop within one second of command loss, and mean location error at most 30 cm are **targets**, not measured results. Exact hardware, wiring, radio links, power budget, braking and supervisor approval remain open.

## Authoritative and working sources

- [Live Hebrew proposal](https://docs.google.com/document/d/1fzNJpmtbakEgXjv7uT-z_8NCtRAehNbJFDoFE5lqjn0/edit) — authoritative for proposal wording, updated 12 October 2026.
- [ResQ-Vision build architecture and staged checklist](https://docs.google.com/document/d/1hNu4UcTtAlyoXaPMbntPuTFcWa2hmmdRNgN7wtSWM7A/edit) — implementation baseline, including updated wireless-plan note.
- [Current context](resources/context/README.md)
- [Engineering plan](resources/context/engineering-plan.md)
- [AI model notes](resources/context/ai-model.md)
- [Proposal folder and export status](resources/proposal/README.md)
- [Diagrams and historical assets](resources/diagrams/README.md)
- [Original school sources and manifest](resources/sources.json)
- [Historical cleaning concept](resources/archive/cleaning-concept-2026-10-05/README.md)

This GitHub repository presently contains planning materials and source references, not verified working robot firmware. The October 7 Word/PDF exports and block diagram show an older architecture: consult the newer native Google Doc and build specification.