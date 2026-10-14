# Requirements and acceptance criteria

ResQ-Vision is a paired 5-unit electronics/computing final project, exam code 841589,
annual IoT theme. Its prototype operates in a flat, bounded laboratory arena.

Baseline goals: manual driving, independent local stops, obstacle-aware autonomous
movement, estimated pose, initial 2D occupancy map, timed camera events and advisory image analysis.
The motion model must represent front steering and two powered rear wheels.

Initial mapping may use calibrated odometry and IMU with LiDAR. Full SLAM, A*,
object localization and video are later features subject to evidence and explicit scope review.
The robot cannot assume it can turn in place. Its rotating ToF has time-varying coverage.

Analysis labels possible hazards, no hazard detected or unknown. It cannot establish
human safety, grant motor authority or clear faults. Trials are not real rescue operations.

Confirmed direction is recorded in [ADRs](../architecture/decisions/README.md).
The current bill of materials is [hardware planning](../hardware/README.md), not a purchase list.

| Status | What exists at migration |
| --- | --- |
| Approved direction | Laptop-hosted system, front steering, rotating ToF, direct C3 input |
| Proposed | Versioned message schemas, failure policies, transport/security/timing choices |
| Implemented | Documentation, schema fixtures, repository checks and CI configuration |
| Measured hardware / AI | No evidence in this repository; no migration hardware trials |

Planned acceptance targets: five collision-free trials, physical standstill within one
second of command loss, mean estimated-position error at most 0.30 m in a defined arena.
These are proposal targets, not school-wide requirements or verified results.
See [school requirements](../school/requirements.md) and [test plan](../development/testing.md).

## Baseline requirement map

| Requirement | Acceptance / evidence | Current status |
| --- | --- | --- |
| R1 Local motion safety | Independent contact and freshness stops under server/network/AI failure | Approved requirement; implementation pending |
| R2 Front steering and rotating ToF | Calibrated rear-speed/steering model and angle/time-stamped samples; no simultaneous side coverage assumption | Approved direction; hardware/calibration open |
| R3 One final owner | ESP32 gates direct C3 and laptop intent; explicit handover/expiry/re-arm | Approved requirement; protocol/tests pending |
| R4 Initial 2D map | Unknown/free/occupied cells and measured pose/map comparison in controlled arena | Planned; implementation pending |
| R5 Advisory camera events | Persist event/image, associate capture-time observation pose, bounded AI and unknown failures | Planned; model/runtime unresolved |
| R6 School compliance | Working prototype, approved subsystem split, external controller Internet exchange and authentic work/AI evidence | Requirements identified; supervisor confirmation pending |
| R7 Stateless development | Canonical docs, isolated branch/worktree, available checks and reviewable Git handoff | Migration implements; see validation record |

[Test procedures](../development/testing.md) define planned evidence. Numerical target
acceptance is subject to arena/speed/load/metric definitions in open decisions D10.
