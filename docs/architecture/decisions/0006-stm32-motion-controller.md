# ADR 0006: Hiwonder STM32 motion controller replaces motion ESP32

Status: Accepted direction. Date: 21 October 2026.
Approval: direct owner request in the project-manager chat: update project context for
the new STM32 and drop the ESP32. Owner also accepts the existing battery as sufficient.

Select Hiwonder ROS Robot Controller V1.2 with STM32F407VET6 as the rover motion controller.
Its identity is confirmed by the supplied board photos. Remove the standalone motion ESP32
from the active design. Do not select a replacement ESP32 bridge by implication.

Interpretation of scope: this replaces the **motion controller** discussed in this exchange.
The separately planned ESP CAM S3 camera and C3 handheld role are retained; the owner has
not requested new camera/handheld hardware. Neither radio compatibility nor connectivity
is assumed. C3 intent must still bypass the laptop and reach the final STM32 authority,
with the physical radio/bridge design open under D4/D5.

STM32 owns motor/steering control, feedback, local stopping, command freshness, stopped
handover and explicit re-arm. Keep front steering/two rear encoder motors, LiDAR-only
ranging, contacts, one laptop and advisory isolated AI. No Raspberry Pi or other onboard
computer is added. Use board USB serial for bench planning only after revision checks;
untethered control and LiDAR acquisition still require compatible reviewed links.

This partially supersedes controller/link references in ADRs 0001, 0003 and 0005.
Local independent stopping and final actuator authority requirements remain unchanged.
The active module is firmware/motion-stm32; the old motion-esp README is a redirect.
No implemented firmware producer/consumer or packet schema requires migration. Draft
application schema payloads/versions are unchanged; future motion contracts must name
STM32 and define the unverified authority/freshness/telemetry behavior explicitly.

Consequences: obtain matching V1.2 firmware/schematic/factory image and demonstrate
build/flash/restore. Verify actual driver limits, encoder levels, servo rail, pin mapping,
IMU identity, independent inhibit and physical stop/recovery behavior. Do not equate
vendor examples with implemented safety. Record the owner's battery acceptance without
inventing its voltage/capacity or claiming measured compatibility; do not reopen battery
selection as a prerequisite. Refer to [hardware context](../../hardware/stm32-controller.md).

The ESP32-based EasyEDA chart and previews are superseded historical references, not a
V1.2 wiring plan. Preserve their bytes and label their entry points; STM32 electrical
redrawing remains follow-up work. Official proposal, project-book PR #14 and live tldraw
board need alignment (#6); this repository update does not claim those external edits.
