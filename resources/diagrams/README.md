# Rover architecture diagrams — provenance and status

The [live Hebrew proposal](https://docs.google.com/document/d/1fzNJpmtbakEgXjv7uT-z_8NCtRAehNbJFDoFE5lqjn0/edit) and [October 12 implementation baseline](https://docs.google.com/document/d/1hNu4UcTtAlyoXaPMbntPuTFcWa2hmmdRNgN7wtSWM7A/edit) replace the Raspberry Pi architecture shown in older exports.

**Outdated assets:** `current-proposal-block-diagram.png`, the former `build_current_diagram.py`, and tldraw exports with Raspberry Pi or home-PC inference are historical. The diagram is not the authoritative current architecture and must not be regenerated as a current figure. Source assets are kept for reference and Git history; the old generator has been disabled to avoid accidental regeneration.

## Current planned architecture

- Rover motion ESP: motors, encoders, IMU, side ToF, front/rear bumpers and local stop.
- Navigation laptop beside the arena: mapping, navigation, server, image/event storage and AI worker.
- ESP CAM S3: WiFi image capture.
- 2D LiDAR: USB to laptop for lab tests; appropriate wireless acquisition bridge required for actual rover movement.
- Phone/laptop browser: WiFi/WebSocket.
- C3 controller: additional manual input, one active control owner, explicit handover and failsafe expiry.
- WiFi carries live ESP motion commands/telemetry; USB UART is for tethered lab debugging.
- Separate internet exchange for school IoT requirement remains undecided.

Retain the [tldraw board](https://www.tldraw.com/f/4aOaHZDyKxk2AseGkkgxy) and exported source files as historical design references. A new diagram should be generated from the verified laptop-based architecture, not by recoloring or renaming a Pi box without updating the links.