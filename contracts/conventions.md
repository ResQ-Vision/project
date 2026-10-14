# Proposed shared data conventions

Status: proposed `0.1-draft`; owners: interface reviewers across affected modules.
Adopt/revise these application conventions in a reviewed PR before integration.

- SI units: metres, seconds, radians, rad/s, m/s. Encoder ticks remain raw counts with
  calibration/sign/resolution stored separately. No default steering dimension is inferred.
- Proposed `base_link`: x forward, y left, z up; yaw counterclockwise. Proposed map origin
  is fixed at the recorded start pose. Scanner/camera/LiDAR transforms require calibration.
- Acquisition timestamps use nonnegative integer `monotonic_ns` plus `clock_id`.
  Clock IDs include device boot/session identity; values from different clocks cannot be
  compared directly. Clock offset/uncertainty and capture-time pose association are explicit work.
- Receiver-local monotonic arrival time governs command expiry, not sender UTC or
  comparison of unrelated device clocks. No timeout number is approved here.
- Opaque nonempty IDs correlate captures/events/requests. IDs are not proof of authorization.
  No filesystem path, radio address or globally unique generation algorithm is frozen.
- `schema_version` is `0.1-draft` in example models. Production version negotiation,
  framing, auth, session/replay checks and maximum sizes remain interface decisions.
- Unknown distances/poses/angles use null with quality metadata, not zero placeholders.
  Failed analysis means unknown; completed “no hazard detected” is not permission to move.
- Stored event position is the robot observation pose at capture, not the measured
  object location. Do not plot it as an object coordinate without additional geometry.

DTO schemas deliberately reject extra fields to expose interface drift in tests. Runtime
payload limits and range/health/freshness checks require hardware-informed bounds and tests.
Schema validation alone does not implement authentication, safety or semantic sensor validity.
