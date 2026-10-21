# Superseded ESP32 EasyEDA electrical reference

**Superseded on 21 October 2026 by [ADR 0006](../architecture/decisions/0006-stm32-motion-controller.md).**
The following 19 October ESP32 candidate chart is preserved for history only. It is not
wiring guidance for Hiwonder V1.2 STM32, LD-1501MG or the owner's actual rear motors/battery.
No GPIO, power allocation or external driver/IMU choice below transfers automatically.
Use [current board context](stm32-controller.md). A new V1.2 chart remains follow-up work;
its absence must not be interpreted as approved wiring. Historical JSON/SVG/CSV bytes
and regression tests remain unchanged and do not validate the selected STM32 board.

Historical status: **candidate module interconnect for review**, 19 October 2026. The user
requested likely parts now and will supply exact class models later. These are
substitutable candidates, not evidence of the parts owned, an approved BOM, a
finished safety circuit or permission to assemble/power the rover.

Based on `main` at `4b7f085`, [ADR 0005](../architecture/decisions/0005-lidar-only-distance-sensing.md),
[transport](../architecture/transport.md), [safety](../architecture/safety.md) and
open Issues [#2](https://github.com/ResQ-Vision/project/issues/2),
[#3](https://github.com/ResQ-Vision/project/issues/3) and
[#4](https://github.com/ResQ-Vision/project/issues/4).
There is one laptop, direct C3 input to motion ESP32, separate camera and LiDAR-only
ranging. The contracts and firmware remain proposals/guidance.

## Editable files

- [EasyEDA Standard project JSON](../../hardware/easyeda/resq-vision-electrical.json)
- [Candidate components, sheet layout and pin assignments](../../hardware/easyeda/design.json)
- [Pin/net matrix CSV](../../hardware/easyeda/pin-matrix.csv)
- [Deterministic generator](../../hardware/easyeda/build_chart.py)

Five sheets cover power/safety gaps, motion/driver, motors/encoder translation,
IMU/contacts/steering, and camera/C3/LiDAR boundaries. Matching net names join
sheets; wireless relationships are notes, never electrical wires. C3 and tethered
LiDAR have distinct USB power/ground domains. Unused module pins are omitted.
Module pins use header labels or explicitly stated header positions, not invented
package pad numbers. Symbols have no PCB footprints or simulation models.

Open [EasyEDA Standard](https://easyeda.com/editor), choose **File → Open → EasyEDA**
and select the project JSON. Alternatively, **File → File Source**, paste its
contents and choose **Create New Document**. Save a local copy after native edits.
To regenerate from the candidate matrix, run from the repository root:

```sh
python3 hardware/easyeda/build_chart.py
```

Edit `design.json` to replace models, header positions, voltage domains and pin
assignments together, then regenerate and re-import. Regeneration replaces the
JSON/CSV; export native EasyEDA edits separately before regenerating.

## Candidate BOM and source checks

Sources checked on 19 October 2026. These parts illustrate compatible roles;
stock, class inventory, cost and mechanical suitability were not verified.

| Reference | Candidate / quantity | Electrical basis and limits |
| --- | --- | --- |
| U1 | Espressif ESP32-DevKitC V4, WROOM-32E / 1 | [Official guide](https://documentation.espressif.com/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html): 5 V header input and 3.3 V GPIO. J2/J3 pin assignments in CSV apply only to this board. USB and external power must not be supplied together. |
| U3 | Cytron MDD10A / 1 | [Manufacturer product](https://www.cytron.io/c-dc-motor-drivers/p-10amp-5v-30v-dc-motor-driver-2-channels), [logic comparison](https://sg.cytron.io/education-motor-driver), [PWM/DIR tutorial](https://www.cytron.io/tutorial/using-mdd10a-arduino-uno): dual brushed-motor driver, 5–30 V, 10 A/channel, 3.3–5 V control. Verify control-header order against actual revision. No separate ENABLE input is assumed. |
| M1, M2 | Pololu 4865, MP 12 V 47:1 encoder gearmotor / 2 | [Manufacturer](https://www.pololu.com/product/4865): 170 RPM no-load and 1.8 A extrapolated stall per motor; gearbox and wheel fit remain unknown. Encoder supply is 3.5–20 V and outputs swing to its supply. |
| U4 | TI SN74LVC125A, SOIC-14 on adapter / 1 | [Datasheet](https://www.ti.com/lit/gpn/sn74lvc125a): four 5 V tolerant inputs, 3.3 V supply and outputs. All four active-low enables tied low; 100 nF bypass C1. This protects ESP inputs from the candidate encoders' 5 V outputs. |
| U5 | Adafruit LSM6DSOX breakout / 1 | [Pinouts](https://learn.adafruit.com/lsm6dsox-and-ism330dhc-6-dof-imu/pinouts): supply VIN at 3.3 V for 3.3 V I2C; onboard pull-ups, default address 0x6A. This statement applies to the Adafruit breakout. |
| SV1 | Hitec HS-422 / 1 | [Manufacturer](https://hitecrcd.com/hs-422-deluxe-standard-servo/): 4.8–6 V, 800 mA listed stall. Steering torque/linkage and observed-angle feedback are unresolved. |
| U6 | TI SN74AHCT1G125, SOT-23-5 on adapter / 1 | [Datasheet](https://www.ti.com/lit/ds/symlink/sn74ahct1g125.pdf): 4.5–5.5 V supply, 2 V input-high minimum; translates 3.3 V PWM to 5 V. C2 is 100 nF. Supply it from the servo rail so an inhibited servo is not driven by a powered buffer. |
| U7 | Waveshare ESP32-S3-CAM-OV5640 / 1 | [Manufacturer guide](https://docs.waveshare.com/ESP32-S3-CAM-OVxxxx): S3 camera board. Use its USB-C power interface, not guessed raw camera pins; Wi-Fi image transport remains a firmware task. |
| U8 | Espressif ESP32-C3-DevKitM-1 / 1 | [Official guide](https://documentation.espressif.com/esp-dev-kits/en/latest/esp32c3/esp32-c3-devkitm-1/index.html): independent handheld USB power; controls/deadman and transport remain unassigned. |
| L1 | SLAMTEC RPLIDAR A1 development kit / 1 | [Manufacturer](https://www.slamtec.com/en/lidar/a1spec): 5 V sensor, 3.3 V UART. Chart uses the kit USB adapter for tethered bench acquisition; raw connector pins and untethered bridge are not assigned. |
| U2 | Pololu D24V50F5, item 2851 / 1 | [Manufacturer specs](https://www.pololu.com/product/2851/specs): 5 V output, typically up to 5 A, thermally limited; input at least about 6–6.2 V and at most 38 V. Provisionally fed by a current-limited 12 V bench source. |
| R1, R2, RP1 | 10 kΩ resistors / 6 total | Proposed bias values: two contact pull-ups and four independent PWM/DIR pull-downs. RP1 is a logical group of four resistors, not a selected resistor-network footprint. |
| S1, S2 | NC mechanical contacts / 2 | Exact model and mounting TBD. Open contact or broken wire reads high; a short to ground is not detected. Debounce/fault handling need review. |
| B1, S0, X1 | Protected 3S battery candidate, E-stop, hardware inhibit | No exact devices selected. Battery and E-stop terminals are intentionally open. X1 is an unimplemented functional boundary, not a working circuit. |

## Power and stop decisions that remain open

The 5 V rail has a **5 A candidate regulator rating**, not a measured budget.
Reserve planning allowances of 1 A for U1/IMU/encoders/buffers, 1 A for the camera
and 0.8 A for the servo: 2.8 A total and 2.2 A nominal margin. The 1 A values are
engineering allocations, not measured or vendor maximum currents. Tethered LiDAR
and C3 are supplied separately. Measure startup peaks, regulator temperature,
noise and reset behavior; revise allocations before integration.

The two motors give a 3.6 A combined extrapolated stall figure at 12 V. It is
neither a permitted continuous operating current nor a fuse rating. Source limits,
wire/connector ratings, protection, transients and regulator input power remain
unresolved. A 3S battery reaches 12.6 V; do not connect it as an approved 12 V
motor source without reviewing actual motor voltage/current limits, protection,
charging and regeneration behavior. No charger/BMS wiring is supplied.

X1 must inhibit motor and steering energy independently of laptop/network/AI,
and behave safely on boot/reset and faults. Its internal switching, feedback,
contact ratings, power loss behavior and braking/coast response need a reviewed
design and measurements. The physical E-stop is deliberately not reduced to a GPIO
button. Bias resistors do not establish an independent stop. Driver test buttons
also require consideration during power-inhibit validation.

D1/D2/D4/D5/D6/D10 stay open. No new hardware choice is elevated to an accepted ADR.
When class models arrive, review all nets and GPIO reservations, recheck logic
thresholds, replace these candidates and measure bench behavior before floor trials.

## Integration choice and validation

The plugin-directory EasyEDA search returned no connector. A third-party
[EasyEDA Pro MCP bridge](https://github.com/Dogmeat88/EasyEDA-MCP) was inspected;
it requires EasyEDA Pro and an in-editor bridge extension. It was not installed
or exercised. The Standard editor and its native JSON import avoid adding an
unverified runtime dependency to this software repository.

Run repository checks and the electrical-chart regression tests as described in
[testing](../development/testing.md). Structural checks cover pin/net connectivity,
encoder translation, separated supplies and unresolved power boundaries. They
are not ERC, SPICE simulation, a firmware build or physical testing.

### Verified editor result

The project was imported into EasyEDA Standard 6.5.60. All five native sheet SVGs
were exported through **File → Export → SVG Source** and visually reviewed:
[power](../../hardware/easyeda/previews/01-power.svg),
[motion](../../hardware/easyeda/previews/02-motion.svg),
[encoders](../../hardware/easyeda/previews/03-encoders.svg),
[sensors/steering](../../hardware/easyeda/previews/04-sensors.svg), and
[camera/radio boundaries](../../hardware/easyeda/previews/05-radio.svg).
The [editor screenshot](../../hardware/easyeda/previews/easyeda-editor.png) records
the native editing view. These are module interconnect drawings, with passive
functions represented by labeled module symbols; they are not fabrication schematics.

The native project source was read back from EasyEDA and all four electrical
regression checks passed against that readback as well as the generated JSON.
The repository checker and full six-test suite passed under Python 3.11.15 with
pinned development requirements. The initial Python 3.14 dependency installation
failed because the pinned rpds-py build does not support it; verification used the
repository's documented Python 3.11 baseline instead. No ERC, simulation,
firmware or physical tests were run. Cloud saving was not performed: the editor
is logged out, and the versioned local JSON is the durable editable artifact.
