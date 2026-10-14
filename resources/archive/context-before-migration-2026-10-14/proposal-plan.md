# Current ResQ-Vision work plan

Updated against the live [proposal](https://docs.google.com/document/d/1fzNJpmtbakEgXjv7uT-z_8NCtRAehNbJFDoFE5lqjn0/edit) and [staged implementation checklist](https://docs.google.com/document/d/1hNu4UcTtAlyoXaPMbntPuTFcWa2hmmdRNgN7wtSWM7A/edit), last modified 12 October 2026.

1. Confirm school requirements, independent subsystem compliance, proposal deadline and supervisor approval. A laptop alone does not guarantee compliance.
2. Select exact motion ESP, C3 controller, DC motors/encoders, motor driver, two side ToF, IMU, two bumpers, ESP CAM S3, 2D LiDAR, battery and physical emergency stop. Finalize wiring, power, chassis and calibration.
3. Choose WiFi control/telemetry transport and a compatible wireless LiDAR acquisition bridge. WiFi applies during driving; USB/UART is for tethered bench testing.
4. Implement deterministic motion-ESP safety, feedback, command expiry and independent stop behavior. Measure physical stopping times/distances.
5. Implement laptop-side wireless ingestion, control-source arbitration (browser/C3/autonomy), odometry, initial 2D mapping and obstacle-aware navigation.
6. Implement WiFi camera capture, timed event records, phone web app, and laptop-local advisory AI in an isolated worker; test under combined processing load.
7. Define and demonstrate separate school-required internet data exchange. Calls between local laptop processes do not meet this requirement.
8. Run instrumented arena acceptance trials and produce the engineering project book with authentic evidence and AI assistance documentation.

Project: pair, 5 units, exam code 841589. Planned targets are five collision-free trials, <=1 s physical stop after command loss and <=30 cm mean localization error; none is a completed result.

The previous cleaning concept is archival. The October 7 GitHub proposal exports and Raspberry Pi diagram are outdated snapshots; do not regenerate the current proposal from them. The latest native Google Doc is authoritative for proposal wording. Full SLAM, 3D mapping and operational rescue claims are not initial commitments.