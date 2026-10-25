# Wi-Fi to STM32 LED bench experiment

Implemented source and successful cross-compilation, 25 October 2026. **ESP32 uploaded
and AP startup messages observed; STM32 ROM identified and flash backed up, but the
LED firmware has not been flashed or tested on STM32.** This replaces STM32 application firmware when
flashed; it does not extend the factory program. Disconnect motors and servos for
this LED experiment. It implements no rover control or local motor safety.

## Environments checked

On the owner's Mac, Arduino IDE, Arduino ESP32 core 3.3.0, PlatformIO, and a standalone
ARM GCC were already installed. No CubeIDE app was found in the checked application
locations. CubeIDE/Keil are unnecessary for this implementation.

Installed for this experiment: PlatformIO ST STM32 platform 20.0.0, STM32 Arduino
framework 3.0.0 (package 4.30000.0), its ARM GCC 12.3.1 and CMSIS dependencies;
Homebrew stm32flash 0.7 for a prospective USB serial bootloader route. Used existing
PlatformIO Core **6.2.0** at `$HOME/.platformio/penv/bin/pio`. Homebrew's separate
`pio` is 6.1.18 and warns about mixed versions; use the explicit executable below.
ESP32 builds use pinned espressif32 6.12.0, Arduino 2.0.17 and Xtensa GCC 8.4.0.
Arduino IDE's separately installed core is not the core used by PlatformIO.

Software builds validate these packages for compilation. They do not establish that
USB drivers, the cable/adapter, bootloader entry, board power or upload work. At the
initial check, `/dev/cu.*` listed only Bluetooth-Incoming-Port and debug-console; no board
was detected. Later ESP32 detection/upload is recorded below. Both boards need a power source during the experiment. One USB cable
can flash them sequentially; it cannot power both independently at once.

## Photo review and proposed wiring

Photos identify Hiwonder ROS Robot Controller **V1.2** and see-sys **CS-ESP32-BBA**.
The ESP32 module appears to be a classic ESP32-WROOM board; its exact module marking
must be checked before using the generic esp32dev profile. GPIO16/17 assume a WROOM
module without a PSRAM conflict; do not apply them to WROVER, S3 or C3 by assumption.
The photos do not establish electrical continuity, voltage, or power polarity.
The ESP32 ends of the two jumper wires are loose; no completed link is shown.
The exact occupied STM32 header positions cannot be reliably confirmed from angle
and wire colour. Identify labels directly, with power off.

| ESP32 | Hiwonder STM32 header | Purpose |
| --- | --- | --- |
| GPIO17 / TX2 | PC11 | ESP32 TX → STM32 USART3 RX |
| GPIO16 / RX2 | PC10 | STM32 USART3 TX → ESP32 RX |
| GND | GND | Shared signal reference |

UART is **115200 baud, 8 data bits, no parity, 1 stop bit**, with 3.3 V logic.
Three inter-board connections are needed for this bidirectional experiment; add
GND, rather than relying on incidental ground through USB. Keep TX/RX crossed.
Do not connect 5V, VIN or 3V3 rails between the boards for this wiring plan.
Power each board through its documented input. Never put 5 V on ESP32 GPIO.

STM32 PC10/PC11 alternate function 7 is USART3 on the MCU. Confirm the V1.2 schematic
has no conflicting loads on those header nets before connecting.
The code targets **PE10, active-low**, based on Hiwonder's general LED tutorial.
The same tutorial calls the factory blinking LED blue. It does not establish that
the owner's red LED is programmable or that V1.2 uses the same LED circuit.
If the red light is the power indicator, it cannot be controlled by this code.
Confirm PE10 and the actual LED before flashing; the prototype profile is provisional.

## Architecture and code

```text
Phone/laptop browser
    │ Wi-Fi + HTTP
    ▼
ESP32: access point, embedded webpage, HTTP server
    │ 3.3 V UART, commands + correlated acknowledgements
    ▼
STM32: command parser → PE10 LED output → pin readback acknowledgement
```

- The ESP32 creates `ResQ-LED-Lab` with demonstration password `resq-led-lab`.
  No router, Internet, laptop server or cloud hosting is required. The page is
  compiled into ESP32 flash. Change the public demonstration password before sharing.
- Browser buttons send same-origin JSON POSTs. The ESP32 sends one UART request,
  waits at most 750 ms for an ACK with the current request ID, then answers HTTP.
  Wrong ID/state cannot produce success. A timeout returns HTTP 504 and unknown state;
  the STM32 may still have applied a command whose acknowledgement was lost.
- Status refresh queries the STM32, rather than trusting an ESP32 cached value.
  The browser has a 4-second request limit, disables buttons while waiting, and
  supports manual retry. No automatic command retransmission is used.
- STM32 owns the LED output. It boots OFF, retains the last requested state during
  link loss, and returns OFF after reset. There is no LED watchdog. It uses a 16 MHz
  internal HSI clock rather than assuming the generic board's external crystal.
- The STM32 Arduino 3.0 concrete UART class is `Uart`; the ESP32 core uses
  `HardwareSerial`. Both constructors here take RX first, TX second.
  STM32 uses `PC_11_ALT1, PC_10_ALT1` explicitly for USART3/AF7. Plain PC11/PC10
  select UART4/AF8 in the pinned generic variant, despite being the same physical pins.
- This plain UART demo has no CRC, authentication, motion ownership or replay
  defence. IDs correlate replies only. Do not reuse it as a rover motion protocol.
  It does not resolve the C3/radio architecture under ADR 0006.

Wire protocol, LF terminated (not CRLF): `LED 1234ABCD 1`, `LED 1234ABCD 0`,
`GET 1234ABCD`; replies `ACK 1234ABCD 1` or `ACK 1234ABCD 0`.
IDs are exactly eight uppercase hexadecimal digits. Malformed/oversized frames
are ignored; overflow is discarded through LF. STM32 expires partial frames after
100 ms and discards through the next LF. After an interrupted frame, one subsequent
request may time out while framing recovers. Reported state is GPIO input readback,
not an optical measurement of the LED.

Sources: [ESP32 firmware](esp32/src/main.cpp), [embedded webpage](esp32/include/web_page.h),
[STM32 firmware](stm32/src/main.cpp), [shared protocol](shared/protocol.h).
Design scope is recorded in [ADR 0007](../../../docs/architecture/decisions/0007-wifi-led-bench-experiment.md).

## Build and software checks

From this directory:

```sh
"$HOME/.platformio/penv/bin/pio" run -d esp32
"$HOME/.platformio/penv/bin/pio" run -d stm32
c++ -std=c++11 -Wall -Wextra -Werror -fsanitize=undefined tests/protocol_test.cpp -o /tmp/resq-led-protocol-test
/tmp/resq-led-protocol-test
```

Generated binaries are under each project's `.pio/build/<environment>/firmware.bin`.
Do not flash the generic STM32 build until the board profile and recovery route are
confirmed. `.pio` is ignored. No downloaded frameworks/binaries are committed.

## USB upload and recovery

1. Connect the ESP32 by a USB data cable. Identify its actual serial device with
   `pio device list` using the same explicit PlatformIO executable. If no device
   appears, inspect the data cable, adapter and actual USB bridge before installing
   a driver. No CH340/CP210x driver requirement has been diagnosed yet.
2. With confirmed module/profile, upload ESP32:
   `"$HOME/.platformio/penv/bin/pio" run -d esp32 -t upload --upload-port /dev/cu.YOUR_ESP_PORT`.
   The port text is a placeholder. Its serial monitor is 115200 baud.
3. Connect the Hiwonder **UART1 USB-C** programming port. Do not confuse it with
   UART2 or assume either USB connector is native DFU. Hiwonder describes serial
   ISP with DTR-low reset and RTS-high bootloader selection. The Mac stm32flash
   control-signal polarity/sequence on this V1.2 board has not been established.
   Confirm the revision's entry procedure, enter its ROM bootloader, then use the
   actual serial device in the commands below. No automatic entry sequence is
   provided as verified. USB alone can be sufficient; ST-Link is not a prerequisite
   for the vendor's serial route, but USB uploading has not been tested here.
4. Before overwriting, obtain and verify a recoverable factory image and/or read a
   backup when readout is permitted. The pre-existing local
   `stm32-setup/vendor/RosRobotControllerM4-factory.hex` has not been verified by this
   experiment for V1.2 identity or restore success. A filename alone is insufficient.

After confirmed bootloader entry, these are standard stm32flash commands, not
commands executed against the owner's board:

```sh
# Read-only connection/chip information. Replace the port placeholder first.
stm32flash /dev/cu.YOUR_STM32_PORT
# Preserve the 512 KiB STM32F407VE flash before overwriting, if readout is allowed.
stm32flash -r /tmp/stm32-before-led.bin -S 0x08000000:0x80000 /dev/cu.YOUR_STM32_PORT
# WRITE: replaces the current application, verifies bytes and starts at flash.
stm32flash -w stm32/.pio/build/hiwonder_f407/firmware.bin -v -g 0x0 /dev/cu.YOUR_STM32_PORT
```

Keep the backup outside `/tmp` after reading it. Never disable read protection as
a workaround: unprotect can erase flash. A saved backup still requires an actual
restore test. Restore the reviewed factory image before reconnecting rover actuators.

## Actual bench procedure, pending

After profile confirmation and upload, connect the three UART wires while powered
off; then power both boards. Join `ResQ-LED-Lab`, retain the connection if the phone
says it has no Internet, and open the HTTP address printed by ESP32 Serial Monitor
(normally `http://192.168.4.1`). Press ON and OFF and observe the actual user LED.
Record the printed SSID/IP, board markings, pin continuity, firmware revision,
USB devices, commands, replies, LED response and reset behavior. Disconnect UART
and confirm the website reports unknown state rather than success; reconnect and
use Check connection. Distinguish a lost ACK from a command that was not applied.

## Verification recorded on 25 October 2026

- ESP32 and STM32 firmware compiled using their pinned platforms.
- Native protocol tests passed with warnings as errors and UndefinedBehaviorSanitizer:
  malformed input, length/hex bounds, overlong-frame recovery, ID/state ACK matching.
  AddressSanitizer could not run on this host; see error log.
- Repository checker and all 13 existing unit tests passed. These include historical
  drawing tests and do not validate this hardware.
- Browser plugin not available; regular Playwright used installed Chrome with a
  temporary mock HTTP server at `http://127.0.0.1:52262`. Desktop 1280×800 and mobile
  390×844 screenshots inspected. Page identity/content, ON/OFF requests, JSON bodies,
  504 unknown state, retry, busy controls, timeout, mobile overflow and no JavaScript
  runtime errors passed. This tests the actual embedded HTML against simulated
  replies, not the ESP32 HTTP implementation, radio or UART. No framework overlay
  was present; expected HTTP 504 in the failure scenario is intentional.
- At the initial software-check stage, no board upload, restore, physical LED,
  electrical, wireless or safety test had been performed. Later ESP32 results follow.

### Later ESP32 USB bring-up, same date

Owner connected the ESP32 through its own USB connector and reported red LEDs lit.
Mac enumerated CP2102 (VID:PID 10C4:EA60) at `/dev/cu.usbserial-0001` without a new
driver installation. Esptool 4.9.0 with explicit `--chip esp32` identified
ESP32-D0WD-V3 revision 3.1, 40 MHz crystal and 4 MB flash. Chip autodetection initially
failed on a short response; the successful explicit-chip retry is logged in #26.

Read all 4,194,304 bytes of pre-existing ESP32 flash into a local backup outside
the repository before writing; a local JSON manifest records size, SHA-256 and
source identity. The image may contain private settings and was not published.
Backup restoration has not been tested.

Uploaded the ESP32 project from source commit `d3f4bbf` using:

```sh
"$HOME/.platformio/penv/bin/pio" run -d esp32 -t upload --upload-port /dev/cu.usbserial-0001
```

PlatformIO reported SUCCESS; esptool verified written-image hashes and hard reset
the board. A subsequent reset with a 115200-baud serial capture yielded:

```text
Join Wi-Fi: ResQ-LED-Lab
Open http://192.168.4.1
```

These application messages follow a successful `WiFi.softAP` return in the source.
They confirm application startup and the reported AP address. A phone association,
real HTTP/page interaction and radio reliability have not yet been observed.
STM32 application upload/restore, inter-board UART acknowledgements, actual LED operation and electrical/
motor safety remain untested. Owner reports checking the three jumper connections;
this is not a continuity or voltage measurement.

### Later STM32 UART1 identification and backup, same date

With its actual UART1 USB-C connected, the Mac enumerated USB Single Serial
(VID:PID 1A86:55D4). STM32 ROM identification returned device ID `0x0413`
(STM32F40xxx/41xxx) and bootloader version `0x31`. No manual button presses were
needed for the successful session. The family ID alone does not identify flash size.

Automatic DTR/RTS entry with stm32flash was intermittent: one identification
succeeded, subsequent backup attempts failed before reading. A local PySerial
investigation helper tested a bounded control-line matrix, flushed stale input,
then used ST AN3155 Get ID and Read Memory commands only. Successful matrix entry
held logical RTS=True and pulsed logical DTR=False→True. These are API signal
values, not measured voltage levels. A standalone equivalent stm32flash sequence
has not been demonstrated reliable; the earlier generic examples remain conditional
on confirmed bootloader entry.

A read of the flash-size register address `0x1FFF7A22` was NACKed after the address;
cause unknown. Retried using the owner's photographed STM32F407VET6 marking to
select the 512 KiB range `0x08000000` through `0x0807FFFF`. All 524,288 bytes were
read and saved locally, with SHA-256
`aed769c1130192b67b9b77a59d2129d8e658b0390f26de2e772052c6bd66be0d`.
Initial stack `0x20017C60` and reset vector `0x08000321` are plausible application
vectors; they do not verify every byte or prove that restoration will succeed.
Backup, manifest, read-only helper and relevant logs are preserved outside Git.
No erase/write/unprotect/option-byte operation was issued.

STM32 firmware remains unchanged. Before overwriting, confirm the V1.2 user LED
net/polarity: PE10 active-low is still based on generic vendor material, not the
matching revision schematic. USB/ROM backup success does not resolve this pin
question or validate the motion system. Error investigation is in session #26.

Errors encountered: [session record #26](https://github.com/ResQ-Vision/project/issues/26).

Primary references:
[Hiwonder hardware course](https://wiki.hiwonder.com/projects/ROS-Robot-Control-Board/en/latest/docs/1_Controller_Hardware_Course.html),
[Hiwonder LED and UART1 upload tutorial](https://wiki.hiwonder.com/projects/ROS-Robot-Control-Board/en/latest/docs/2_STM32_Development_Fundamentals.html),
[ST RM0090](https://www.st.com/resource/en/reference_manual/dm00031020-stm32f405415-stm32f407417-stm32f427437-and-stm32f429439-advanced-arm-based-32-bit-mcus-stmicroelectronics.pdf),
[Espressif Wi-Fi API](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/wifi.html),
[STM32 Arduino API](https://github.com/stm32duino/Arduino_Core_STM32/wiki/API).
Generic vendor documentation and MCU alternate functions are leads, not revision-specific
electrical validation.
