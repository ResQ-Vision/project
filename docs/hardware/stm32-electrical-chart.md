# STM32 electrical drawing, revision B

This is the current shareable **design-review drawing**, based on merged
[ADR 0006](../architecture/decisions/0006-stm32-motion-controller.md) and
[PR #20](https://github.com/ResQ-Vision/project/pull/20), main `897c03e`.
It supersedes the old chart as the presentation entry point. The historical
ESP32 files are preserved unchanged.

## Deliverables

- [Two-page vector PDF, landscape A3](../../output/pdf/resq-vision-stm32-electrical.pdf)
- [Editable native EasyEDA project](../../hardware/easyeda-stm32/resq-vision-stm32.json)
- [Assembly SVG](../../hardware/easyeda-stm32/01-assembly.svg)
- [Interfaces and connector reference SVG](../../hardware/easyeda-stm32/02-interfaces.svg)
- [Logical terminal matrix](../../hardware/easyeda-stm32/logical-terminals.csv)
- [Evidence/status manifest](../../hardware/easyeda-stm32/drawing-manifest.json)

The first sheet shows the retained battery, Hiwonder V1.2/STM32F407VET6, two rear
motor/encoder harnesses, LD-1501MG steering and front/rear contacts. The second
sheet shows one laptop, the separate ESP CAM S3, direct C3-to-STM32 intent and
LiDAR acquisition, followed by connector-function references and six review checks.
Dashed paths are graphical interface intent, not conductive wires. Contact polarity,
bias and GPIO selection are unassigned. All terminal IDs are logical names, not
claimed physical V1.2 connector positions or MCU pins. Solid paths show intended
assembly functions; their actual connector/rail compatibility still needs #2 review.

## Evidence and decisions

- Controller and LD-1501MG identity: owner-confirmed in merged GitHub hardware context.
- Existing battery: retained and accepted by owner; no replacement model, capacity,
  voltage or purchase task is invented.
- Rear motor model JGB37-520R30-12: **likely**, not fully confirmed from the label.
- Onboard motor drivers and IMU: shown within the board; no external Cytron driver,
  external IMU, encoder translator or guessed V1.2 driver/IMU chip is added.
- Exact S3 camera board, C3 hardware and LiDAR model are left unselected; the earlier
  candidate parts are not silently carried forward.
- No motion ESP32, assumed ESP32 radio bridge, separate ToF, Raspberry Pi or second
  inference computer is added. The camera/C3 ESP-family roles remain.
- Source [2] is the [Hiwonder STM32 chassis guide](https://docs.hiwonder.com/projects/Ackermann-Chassis/en/latest/docs/2_STM32_Version_checked.html).
  It supports motor-harness **functions** and the servo's white signal / red supply /
  black return, and recommends 6-8.4 V for LD-1501MG. It does not prove the V1.2
  socket order, selected servo rail, firmware behavior or measured compatibility.
- The [general board course](https://wiki.hiwonder.com/projects/ROS-Robot-Control-Board/en/latest/docs/1_Controller_Hardware_Course.html)
  mixes revisions, so its pin numbers, power limits and IMU identity are not copied.

Open gates A-F map to existing Issues [#2](https://github.com/ResQ-Vision/project/issues/2),
[#3](https://github.com/ResQ-Vision/project/issues/3),
[#4](https://github.com/ResQ-Vision/project/issues/4), and
[#9](https://github.com/ResQ-Vision/project/issues/9). Physical input/protection,
motor-driver limits, encoder levels, servo routing, contact inputs, independent
inhibition and compatible radio/acquisition remain unresolved. This PDF is ready
to send for project/design review; it is not a fabrication or assembly release.

## Open and edit

In [EasyEDA Standard](https://easyeda.com/editor), choose **File > File Source**,
paste the project JSON and choose **Create New Document**. Both sheets contain
native editable shapes, grouped device symbols, terminals and wires, not flattened
images. Save/export a copy before regenerating. A cloud account save is not assumed.

The geometry and wording have one source, the dependency-light
[generator](../../hardware/easyeda-stm32/build_chart.py). It emits native EasyEDA,
SVG, CSV, status manifest and a vector PDF from the same drawing operations.
For regeneration, use Python 3.11 with `reportlab` installed:

```sh
python hardware/easyeda-stm32/build_chart.py
```

ReportLab is only needed to regenerate the PDF; normal repository checks and tests
use existing development requirements. No runtime module or contract is changed.
Verification is recorded in the PR: repository checks, focused terminal/topology
regressions, native EasyEDA readback and visual review of both rendered PDF pages.
No ERC/SPICE, firmware build or physical tests are claimed.

Errors encountered: [redraw session #22](https://github.com/ResQ-Vision/project/issues/22).
