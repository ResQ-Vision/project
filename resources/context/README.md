# Current project context — ResQ-Vision

Last aligned with the [live Hebrew proposal](https://docs.google.com/document/d/1fzNJpmtbakEgXjv7uT-z_8NCtRAehNbJFDoFE5lqjn0/edit) and the [build architecture checklist](https://docs.google.com/document/d/1hNu4UcTtAlyoXaPMbntPuTFcWa2hmmdRNgN7wtSWM7A/edit), both updated 12 October 2026. The repository's older October 7 Raspberry Pi plans are superseded.

## Scope

Pair project; 5 units; examination code 841589; annual IoT theme. A controlled-arena exploration rover demonstrates autonomous obstacle-aware movement, estimated pose/path, initial 2D occupancy mapping, manual controls and camera events with advisory image assessment.

The project does **not** contain a Raspberry Pi or a separate home-PC inference machine. There is no active cleaning mechanism. Full SLAM, complete exploration, 3D or elevation mapping, real rescue operation and validated safety diagnosis are outside the initial demonstration.

## Planned responsibilities

- **Motion ESP:** local motor control/feedback, encoders, IMU, left/right ToF, front/rear bumpers, command expiry and local stopping. Its motor safety must not rely on the laptop, AI or internet.
- **Laptop beside arena:** wireless rover communication, LiDAR acquisition, pose estimation, mapping, navigation, images/events, web backend and a separately isolated local AI worker.
- **Separate ESP CAM S3:** transfers still images over WiFi to the laptop.
- **2D LiDAR:** USB-to-laptop during tethered bench tests; untethered operation requires selecting and validating a wireless acquisition bridge matched to the sensor's actual interface and bandwidth.
- **C3-based manual controller:** additional planned manual source, subject to board/input/route selection. Browser, C3 and autonomy must have a single active control owner, explicit handover, expired commands and no surprise restart.
- **Phone/laptop browser:** observes map, path, controls, images, sensor state and AI outcomes.

Core proposed parts include two encoder-equipped DC motors, left/right ToF, IMU, 2D LiDAR, front/rear contact bumpers, battery/driver and ESP CAM S3. Four downward edge sensors appeared in the older snapshot but are **not listed in the latest proposal**; retain as a historical proposal/possible extension until explicitly approved. Optional motor-current and voltage telemetry are also not core commitments.

## Interfaces and verification

Motion commands/telemetry: WiFi during actual driving; USB UART for bench debugging. Camera: WiFi. Browser: WebSocket over WiFi. Laptop-hosted AI worker: bounded local IPC/API. The proposed fresh-packet UDP command design, security scheme, LiDAR bridge and timing limits need validation; no final protocol has been frozen. Laptop-local inference is **not** internet exchange for the IoT school requirement; an independent internet path remains to be defined and demonstrated.

Current proposed acceptance targets: five collision-free controlled-arena runs, command-loss stop within one second, and mean localization error at most 30 cm. Not achieved measurements. Dimensions, hardware, stop distance, calibrations, tests and reviewer/supervisor compliance remain open.

## AI behavior

Intended model: Cloudflare Clef-Flash Q8_0, running **on the navigation laptop**, separate from latency-sensitive control tasks. It scores predefined image questions. Do not treat model scores as calibrated hazard or human-safety probabilities. Events display pending, possible hazard, none detected or unknown, with failure and inadequate-image states. Compatibility, latency and accuracy still require tests.

## School documents and provenance

The editable Google Doc is the source for proposal wording. The separate architecture/checklist document captures more recent implementation planning. Repository PDF/Word exports, image diagrams and the October 7 Markdown draft are stale; do not use them to reverse the October 12 decisions. Original ministry/school references, extracts and historical assets remain preserved.

Both students must understand the integrated project. The school’s independent-subsystem, inputs/outputs, communication and internet requirements need explicit verification; a laptop does not automatically satisfy them. See [proposal work plan](proposal-plan.md) and [engineering plan](engineering-plan.md).