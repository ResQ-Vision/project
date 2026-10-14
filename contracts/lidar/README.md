# Acquisition models and timing

Status: proposed `0.1-draft`; owners: server acquisition + motion firmware.
Model: [LiDAR scan](scan.schema.json).
Next decision: D6 LiDAR model/bridge/bandwidth/clock mapping.
ADR 0005 removes the separate ToF; its proposed model is [archived](../../resources/archive/tof-contract-2026-10-14/README.md), with no implemented consumers.

LiDAR scan samples have angle in radians and range in metres; null range is unknown.
The timestamp refers to scan acquisition start, with a per-point time offset so a moving
robot's scan is not assumed simultaneous. Scan/clock/frame IDs make replay and calibration explicit.
Quality reflects producer knowledge; consumers still validate range, coverage, age and faults.
Actual sensor range limits, angular convention/mount transform and clock offset require selection.

USB is the tethered LiDAR bench path; driving requires a validated compatible wireless bridge.
Missing/stale LiDAR stops autonomy. Derive age/coverage thresholds from actual scan and
stopping tests; sample arrays/schema checks alone cannot establish a safe obstacle monitor.
