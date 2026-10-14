# Engineering plan — current laptop-hosted architecture

Sources: [Hebrew proposal](https://docs.google.com/document/d/1fzNJpmtbakEgXjv7uT-z_8NCtRAehNbJFDoFE5lqjn0/edit) and [implementation checklist](https://docs.google.com/document/d/1hNu4UcTtAlyoXaPMbntPuTFcWa2hmmdRNgN7wtSWM7A/edit), updated 12 October 2026. This is a plan, not evidence of built hardware.

## Stage goals

Demonstrate safe manual motion, local stops, autonomous obstacle reaction, odometry, an initial planar occupancy map and a phone-accessible dashboard. Add event capture and advisory image assessment without blocking motion. Use a measured, flat, bounded test arena. Full SLAM, autonomous coverage, 3D sensing and real hazardous-area operation are not initial commitments.

## Computing and physical responsibilities

- Motion ESP: encoder acquisition, wheel-speed PI/PID (candidate), IMU/side-ToF/contact-sensor input, local stop, command watchdog, motor-driver output. Safety checks must remain responsive when any other component fails.
- Navigation laptop placed beside arena: sensor reception, time/pose estimation, 2D mapping, navigation, web service, stored image events and isolated local inference worker. No onboard Raspberry Pi and no separate inference desktop.
- ESP CAM S3: independent camera firmware sending images to the laptop by WiFi.
- 2D LiDAR: scan data to laptop through USB in bench setup; during driving a **yet-to-be-chosen wireless acquisition bridge** compatible with the actual sensor is required. An MCU with UART LiDAR is a draft option; do not assume a USB-only LiDAR can attach to an ordinary MCU without USB host support.
- A C3-based controller adds another manual input source; exact input hardware and command route are undecided. One active authority for browser/C3/autonomy, explicit transitions and stop on stale input.

## Communications

- ESP <-> laptop: WiFi for actual rover motion. USB UART is for tethered bench debugging, programming and recovery.
- ESP CAM S3 -> laptop: WiFi imagery and capture requests.
- LiDAR -> laptop: USB in the lab; verified wireless acquisition adapter during motion (device choice, power, bandwidth and latency pending).
- Phone/browser <-> laptop: WiFi/WebSocket.
- Laptop process <-> laptop inference worker: bounded local IPC/API, independently restartable.
- Separate school internet exchange: still requires an identified external endpoint/protocol and measured test; local AI does not qualify.

Proposed wireless control design uses bounded fresh UDP commands, protocol/session/sequence checks, authenticated endpoints and local command expiry. This is **not yet an implemented or approved final protocol**. Do not silently reuse the previous USB-serial-only production contract. Define the transport-independent messages once; test both WiFi and bench adapters against them.

## Candidate algorithms and boundaries

1. Finite state machine for disarmed, ready, manual, autonomous, obstacle handling and latched fault; explicit re-arm.
2. Wheel-speed PI/PID with encoder feedback, calibrated differential-drive odometry and IMU assistance.
3. Filter noisy readings, label ages/invalidity, monitor LiDAR freshness and robot clearance.
4. Initial reactive avoidance plus conservative ESP-local protection; bumper contact stops are not pre-contact avoidance.
5. Occupancy grid transformed from 2D LiDAR scans using estimated pose; distinguish unknown/free/occupied.
6. A* only after a usable map and pose measurements; scan matching/full SLAM are possible later additions.

The exact ESP model, pins, encoder resolution, motor driver, battery, sensor models, scan bridge, power budget, timeout and safe speed require decisions before powered driving.

## Camera and AI

Associate recorded still images with event ID, capture time, estimated observation pose, trigger reason and confidence/quality. Inference uses intended Cloudflare Clef-Flash Q8_0 on the **same laptop**, in a separate worker with bounded queue and timeout. Output is scored predefined choices about visual obstructions, narrow openings or insufficient imagery. Pending/failure/low confidence must be displayed distinctly. Scores are not validated safety probabilities; AI never controls emergency stopping or navigation authorization.

Test model/runtime support and performance while the laptop simultaneously runs mapping and the web service. No successful benchmark has been recorded.

## Safety and acceptance

Physical emergency motor disable, hardware watchdog, command loss, invalid sensors, motor enable behavior, WiFi loss and post-fault re-arm need explicit implementation and bench verification. A proposed stop policy is documented in the linked implementation checklist; proposed timing numbers there are recommendations, not measured results.

The live proposal's **planned** targets remain five collision-free trials, a stop within 1 second after command loss and mean pose error <=30 cm in a small arena. Define test methodology, worst-case distance, arena dimensions and error metrics before claiming achievement. A physical emergency stop is an engineering recommendation and still needs implementation.

## Milestones

1. Confirm school subsystem compliance and select hardware, wiring, safety arrangement, WiFi protocol and LiDAR bridge.
2. Bench-test ESP motor/encoder, stops, sensors and command expiry.
3. Demonstrate manual motion via laptop and C3 control-owner arbitration.
4. Validate wireless LiDAR/camera telemetry and pose/calibration.
5. Implement occupancy mapping and controlled obstacle-aware autonomous operation.
6. Build responsive map/events dashboard and asynchronous local AI assessment.
7. Perform integrated repeatable measured acceptance tests and finish documented evidence.

Preserve early work in the archive; the 7 October Raspberry Pi diagram and proposal exports are no longer current.