# Selected STM32 motion hardware

Owner decision: 21 October 2026; [ADR 0006](../architecture/decisions/0006-stm32-motion-controller.md).
Replace the motion ESP32 with **Hiwonder ROS Robot Controller V1.2 / STM32F407VET6**.
The board underside and chip markings are visible in the owner's photos. This confirms
identity, not a working firmware build or validated electrical/safety behavior.

| Item | Evidence / status |
| --- | --- |
| Controller | Owner photos show Hiwonder, Ros Robot Controller V1.2 and STM32F407VET6; M1–M4 motor connectors visible |
| Steering | Owner read LD-1501MG digital servo label; mounted front linkage visible |
| Rear motors | Owner read JGB37-5…; photo shows 30:1; **likely JGB37-520R30-12**, inferred using matching chassis docs, not fully readable label |
| Battery | Owner states existing battery is sufficient; accepted project input. Model/capacity are not recorded; no new battery-selection task is required |
| Camera/C3 | Separate ESP CAM S3 and C3 manual-controller role retained. Their ESP-family chips are not the removed motion ESP32 |

## Vendor research, not measurements

[Hiwonder chassis documentation](https://docs.hiwonder.com/projects/Ackermann-Chassis/en/latest/docs/2_STM32_Version_checked.html)
identifies JGB37-520R30-12 motors and LD-1501MG steering for the matching chassis family.
[Motor specifications](https://www.hiwonder.com/products/hall-encoder-dc-geared-motor)
list 12 V, 30:1, 320 RPM no-load, 0.36 A rated / 3.2 A stall per R30 motor,
and 3.3–5 V A/B Hall encoder supply. Treat these as conditional on the motor identity;
verify the V1.2 driver's continuous/peak limits and connector mapping before integration.

The [servo documentation](https://wiki.hiwonder.com/projects/Ackermann-Chassis/en/latest/docs/3_Arduino_Version_formatted.html)
recommends 6–8.4 V and 20 ms PWM with nominal 500–2500 microsecond pulses.
Do not equate full servo travel with safe steering travel. Exact V1.2 servo-rail routing,
current capacity and signal thresholds must be checked; neither a 5 V socket nor raw
battery supply is automatically approved for this servo. These are interface checks,
not a request to reselect the owner's battery.

[General board specifications](https://www.hiwonder.com/products/ros-robot-control)
and [hardware course](https://wiki.hiwonder.com/projects/ROS-Robot-Control-Board/en/latest/docs/1_Controller_Hardware_Course.html)
mix revision details. Do not import older pinouts, supply limits, IMU identities or motor
ratings as V1.2 facts. Existing ESP32 EasyEDA files are superseded reference artifacts.

## Questions to resolve before bring-up

1. Can we obtain complete V1.2 firmware, matching schematic and a restorable factory image?
   [Support thread](https://forum.hiwonder.com/t/source-code-for-ros-robot-controller-v1-2/285)
   links tutorials but does not resolve complete factory-source access.
2. Can our toolchain build, flash, restore and debug this board? Vendor
   [Keil/USB/SWD guidance](https://wiki.hiwonder.com/projects/ROS-Robot-Control-Board/en/latest/docs/2_STM32_Development_Fundamentals.html)
   is not a verified local setup. Pin compiler, SDK, programmer and firmware versions.
3. Are motor/encoder/servo rails, connectors and driver ratings compatible with the actual chassis?
4. Can the laptop read required encoder/IMU/stop/owner telemetry with defined time/quality?
5. Which untethered laptop and C3 link reaches STM32 without routing C3 through the laptop?
   No WiFi or ESP-NOW capability, radio bridge, or Raspberry Pi addition is selected.
6. Can STM32 enforce independent local stops, one owner, valid-command expiry, stopped
   handover and explicit re-arm across boot/reset/reconnect? Factory behavior is unverified.
7. How does independent physical motor/steering inhibition work on this board?

Track focused work in #2, #3 and #9. No firmware, bench trial, physical stopping,
model benchmark, PCB/ERC or complete system validation is established by this context update.

## Electrical drawing

The [revision B drawing](stm32-electrical-chart.md) presents this hardware context
as a two-sheet EasyEDA/PDF review package. Its logical terminal names are not
physical V1.2 pin assignments; the electrical and safety questions above stay open.
