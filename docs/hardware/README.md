# Hardware planning and measurement

Status: component roles are confirmed; exact models/availability/pinouts are unresolved.

| Component | Planned quantity | Selection evidence required |
| --- | --- | --- |
| Motion ESP32 | 1 | GPIO/encoder peripherals, WiFi coexistence, USB/UART and real-time timing |
| Rear DC motors with encoders | 2 | Rated/stall current, encoder scale, driver sizing |
| Front steerable wheels and mechanism | 2 wheels + mechanism | Linkage, actuator, limits, wheelbase, angle feedback/calibration |
| IMU | 1 | Bias/noise calibration, mount transform and bus |
| Contact sensors | Front and rear | Polarity, wiring failure behavior, local-stop measurements |
| ESP CAM S3 | 1 | Exact board/sensor, image format, power and WiFi transfer |
| 2D LiDAR | 1 | Electrical/data interface, field of view, scan rate, wireless bridge compatibility |
| C3 controller | 1 | Board, input controls, power, direct radio path and deadman design |
| Motor driver / battery / regulators | To select | Current/voltage budget, fuse, enable default and brake/coast behavior |
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

## Provisional electrical chart

The [EasyEDA chart and candidate BOM](electrical-chart.md) provide an editable
module interconnect with likely parts authorized for temporary planning on
19 October 2026. Exact class hardware, safety power stage and LiDAR bridge still
need confirmation; this does not close the hardware review.
