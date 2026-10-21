# Hardware planning and measurement

Status: STM32 controller and steering-servo identities are owner-confirmed; rear motor identification is a strong inference. Pinouts, firmware and integration are not validated.

| Component | Planned quantity | Selection evidence required |
| --- | --- | --- |
| Hiwonder ROS Robot Controller V1.2 / STM32F407VET6 | 1 | Board/MCU confirmed from photos; matching firmware/schematic, drivers and local-stop validation required |
| Rear encoder motors, likely JGB37-520R30-12 | 2 | Photo shows 30:1; matching Hiwonder chassis docs support model inference; verify driver current and encoder pinout |
| Front steering / LD-1501MG digital PWM servo | 1 servo + linkage | Servo label confirmed by owner; supply/interface, travel limits, wheelbase and feedback/calibration remain open |
| Onboard IMU | 1 | Exact V1.2 IMU identity, firmware driver, bias/noise and mount transform |
| Contact sensors | Front and rear | Polarity, wiring failure behavior, local-stop measurements |
| ESP CAM S3 | 1 | Exact board/sensor, image format, power and WiFi transfer |
| 2D LiDAR | 1 | Electrical/data interface, field of view, scan rate, wireless bridge compatibility |
| C3 controller | 1 | Board, input controls, power, direct radio path and deadman design |
| Onboard motor drivers / existing battery / supply interfaces | Board + owner-provided battery | Battery accepted as sufficient by owner; driver limits, correct board/servo rails, protection and stop behavior remain integration checks |
| Physical emergency stop | Proposed | Hardware design and measured stop independent of software |
| Laptop beside arena | 1 | OS/toolchains, wireless connectivity and concurrent AI/control resource budget |

No separate ToF sensor/rotation mechanism or downward edge sensors belong to the baseline. No cliff detection
is claimed. Original diagrams are historical and cannot establish the purchase/wiring plan.

Deliver a reviewed BOM with datasheet links, connector/pin matrix, bus addresses,
power budget, mounting drawing and calibrated chassis geometry before wiring integration.
Do not infer purchase, tested compatibility or safe ratings from a conceptual illustration.
Validate LiDAR mount transform, scan coverage and acquisition timestamp quality against
the selected sensor. The removed ToF rotation mechanism needs no wiring or calibration.

Use [safety gates](../architecture/safety.md) and [open decisions](../project/open-decisions.md).

## Superseded ESP32 electrical reference

The [EasyEDA chart and candidate BOM](electrical-chart.md) provide an editable
historical module interconnect from 19 October 2026. Its ESP32 pins, external driver,
IMU, servo and power allocations do not describe the selected STM32 build. Preserve
it as reference only. The current [STM32 drawing](stm32-electrical-chart.md) provides
a readable connector-level design-review package; actual V1.2 pin mapping remains open.

Current evidence and open questions: [STM32 controller](stm32-controller.md).

## Current electrical drawing

Use the [revision B STM32 electrical drawing](stm32-electrical-chart.md) for
sharing and review: native EasyEDA source, two-page vector PDF and SVGs.
