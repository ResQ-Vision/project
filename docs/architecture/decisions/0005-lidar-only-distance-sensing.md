# ADR 0005: LiDAR-only distance sensing

Controller/link references below are partially superseded by [ADR 0006](0006-stm32-motion-controller.md), 21 October 2026: use Hiwonder V1.2 STM32; local safety and laptop-bypassing manual-path requirements remain.
Status: Accepted direction. Date: 14 October 2026.
Approval source: direct user request in the project-manager chat: the ToF will no
longer be used because LiDAR is preferred and considered enough for the planned design.

Remove the separate ToF sensor and its rotation mechanism. Use the existing planned
2D LiDAR for distance/obstacle sensing and mapping. This supersedes only the ToF part
of ADR 0002; front steering, rear encoder motors, IMU/contacts, one laptop, direct C3
and ESP-local independent stops remain the baseline.

Consequences: remove ToF BOM/wiring/calibration work and retire its unimplemented draft
schema/fixtures from active contracts. The historical model and fixtures are preserved
under resources/archive/tof-contract-2026-10-14. No executable producer/consumer exists.
The remaining six schemas stay proposed 0.1-draft; their payloads are unchanged.

LiDAR range/coverage, mount transform, scan timing, wireless bridge, stale-scan policy
and stopping envelope still need selection and measured evidence (D6/D10, Issues #4/#9).
The user's design preference does not establish hardware safety or measured sufficiency.
No separate ToF fallback is available; local contact/command-loss stops remain required.

The user's term תרשים מלבנים refers to the
[editable tldraw board](https://www.tldraw.com/f/4aOaHZDyKxk2AseGkkgxy?d=v-358.-186.2651.1825.page).
A dedicated chat is assigned to correct that board. Current exports and earlier proposal
readbacks are historical evidence; live proposal/checklist alignment is tracked by #6.
