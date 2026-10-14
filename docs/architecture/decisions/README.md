# Architecture decisions

Accepted means the user confirmed the direction, not that code or hardware is validated.
This migration PR is still subject to review. Proposed protocols are tracked separately.

| ADR | Status | Decision |
| --- | --- | --- |
| [0001](0001-laptop-and-independent-safety.md) | Accepted direction | One laptop hosts server and isolated advisory AI; ESP-local safety |
| [0002](0002-front-steering-rotating-tof.md) | Partially superseded by 0005 | Front steering/rear encoder motors retained; separate ToF removed |
| [0003](0003-direct-c3-authority.md) | Accepted direction | C3 connects directly to motion ESP32; final authority enforced there |
| [0004](0004-github-source-of-truth.md) | Accepted workflow | Modular GitHub knowledge and Issue/branch/PR workflow |

| [0005](0005-lidar-only-distance-sensing.md) | Accepted direction | Remove separate ToF/rotation mechanism; use 2D LiDAR for distance sensing |

New decisions use [template](template.md). Record approval source/date, alternatives,
consequences, verification gaps and supersession links. Do not call a PR-approved interface
accepted until the relevant reviewer has actually approved it.
