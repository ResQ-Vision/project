# Acquisition models and timing

Status: proposed `0.1-draft`; owners: server acquisition + motion firmware.
Models: [LiDAR scan](scan.schema.json), [rotating ToF sample](rotating-tof.schema.json).
Next decisions: D3 scanner mechanics/angles; D6 LiDAR model/bridge/bandwidth/clock mapping.

LiDAR scan samples have angle in radians and range in metres; null range is unknown.
The timestamp refers to scan acquisition start, with a per-point time offset so a moving
robot's scan is not assumed simultaneous. Scan/clock/frame IDs make replay and calibration explicit.
Quality reflects producer knowledge; consumers still validate range, coverage, age and faults.
Actual sensor range limits, angular convention/mount transform and clock offset require selection.

A single rotating ToF sample reports angle, distance, acquisition timestamp and angle quality.
Unknown angle is null; commanded angle without measured/calibrated evidence is only estimated.
Do not treat a full sweep as simultaneous side measurements or convert it into LiDAR evidence.

USB is the tethered LiDAR bench path; driving requires a validated compatible wireless bridge.
Missing/stale LiDAR stops autonomy. Derive age/coverage thresholds from actual scan and
stopping tests; sample arrays/schema checks alone cannot establish a safe obstacle monitor.
