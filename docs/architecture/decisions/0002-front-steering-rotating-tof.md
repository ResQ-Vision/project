# ADR 0002: Front steering and rotating top ToF

Status: Partially superseded by [ADR 0005](0005-lidar-only-distance-sensing.md): the separate ToF and rotation mechanism are removed. Front steering/rear encoder motors remain accepted. Date: 14 October 2026.
Source: writing chat 12 October; explicit answer during migration:
“keep rotating tof, front sterring direct c3 to esp 32, delte all of the things that conflict this”.

Use four wheels: two powered rear wheels with encoders and two steerable front wheels.
Use one top-mounted ToF sensor rotating through 360 degrees, separate from 2D LiDAR.
Retain IMU and front/rear contacts. Four downward sensors are removed from the baseline.

This supersedes fixed left/right ToF and differential-drive/turn-in-place assumptions
in active documentation. Original proposal wording still contains contradictions;
live Google Docs are retained and tracked in the source audit, not silently rewritten.

Consequences: select scanner mechanism, angle observation, wiring strategy and sample
timing; choose steering linkage/actuator and calibrate front-steering kinematics.
Rear wheel speeds must reflect turning geometry. No full-coverage/drop-safety claim
can be made from this design choice. No dimensions or measured capabilities are implied.
