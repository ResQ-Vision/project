# Architecture decisions

Accepted means the user confirmed the direction, not that code or hardware is validated.
This migration PR is still subject to review. Proposed protocols are tracked separately.

| ADR | Status | Decision |
| --- | --- | --- |
| [0001](0001-laptop-and-independent-safety.md) | Controller/link updated by 0006 | One laptop hosts server and isolated advisory AI; STM32-local safety |
| [0002](0002-front-steering-rotating-tof.md) | Partially superseded by 0005 | Front steering/rear encoder motors retained; separate ToF removed |
| [0003](0003-direct-c3-authority.md) | Controller/link updated by 0006 | C3 connects directly to motion STM32 controller; final authority enforced there |
| [0004](0004-github-source-of-truth.md) | Accepted workflow | Modular GitHub knowledge and Issue/branch/PR workflow |
| [0005](0005-lidar-only-distance-sensing.md) | Accepted direction | Remove separate ToF/rotation mechanism; use 2D LiDAR for distance sensing |
| [0006](0006-stm32-motion-controller.md) | Accepted direction | Hiwonder V1.2 STM32 replaces motion ESP32; battery accepted; radio integration open |

New decisions use [template](template.md). Record approval source/date, alternatives,
consequences, verification gaps and supersession links. Do not call a PR-approved interface
accepted until the relevant reviewer has actually approved it.
