# Wi-Fi LED experiment checkpoint

Saved at the owner's request on 25 October 2026, Asia/Jerusalem. Work stops here
until the owner asks to resume. No scheduled task or automatic flashing is set up.

## Resume location

- Repository: ResQ-Vision/project.
- Branch: `codex/stm32-wifi-led-experiment`.
- Local checkout: `$HOME/.codex/worktrees/resq-wifi-led-20261025`.
- Firmware source uploaded to ESP32: commit `d3f4bbf`.
- Prior evidence commit: `39828dd`; this checkpoint is a subsequent docs commit.
- Draft review: [PR #27](https://github.com/ResQ-Vision/project/pull/27), not merged.
- Errors and investigation: [#26](https://github.com/ResQ-Vision/project/issues/26),
  including immediately fixed setup failures and bootloader retries.
- Start with the [experiment README](README.md), then this checkpoint. The user's
  original research checkout and partial iCloud worktree were left untouched.

## Completed and verified

1. ESP32 and STM32 sources cross-compiled. Native protocol tests, all 13 existing
   repository tests, repository checker and diff whitespace checks passed.
2. Actual embedded webpage passed desktop/mobile Playwright tests against mock
   HTTP responses. This did not test a real wireless HTTP exchange.
3. ESP32 CP2102 USB interface was detected. ROM identified ESP32-D0WD-V3 rev3.1
   with 4 MB flash. Its complete pre-experiment flash was saved locally.
4. ESP32 experiment firmware uploaded successfully; esptool verified written-image
   hashes. After reset, serial output reported `ResQ-LED-Lab` and `http://192.168.4.1`.
   Demonstration network password in the source is `resq-led-lab`.
5. STM32's actual UART1 USB-C interface was detected (USB Single Serial,
   VID:PID 1A86:55D4). ROM identification returned device ID 0413 and bootloader
   version 0x31. A complete 512 KiB original flash image was saved by read-only
   AN3155 commands; initial vector values were plausible.
6. No STM32 flash erase/write, unprotect, option-byte change or LED firmware upload
   occurred. Its original application remains unchanged. Neither backup has been
   restored as a test.

## Local recovery artifacts — do not publish image contents

Images may contain private settings. They are outside Git; metadata and readback
logs accompany them. Recheck the files and hashes before relying on them.

| Device | Local file under `$HOME/.codex/backups/resq-wifi-led/` | Bytes | SHA-256 |
| --- | --- | --- | --- |
| ESP32 | `esp32-gw47DFXO/esp32-before-led.bin` | 4194304 | `874d3863123a171da56fb1c32da1e2986bab7ae9cf77f8d1fce0ad5032686fef` |
| STM32 | `stm32-wNDrY5uO/stm32-before-led.bin` | 524288 | `aed769c1130192b67b9b77a59d2129d8e658b0390f26de2e772052c6bd66be0d` |

The STM32 backup directory also preserves the one-off read-only Python helper
and logs. Its control-line matrix found ROM entry holding logical RTS=True and
pulsing DTR=False→True with buffer clearing. This does not establish electrical
polarity or a reliable standalone stm32flash command. Straight stm32flash retries
were intermittent. Reading address 0x1FFF7A22 was NACKed; the 512 KiB selection
came from the photographed STM32F407VET6 marking, not a measured size register.
Do not use an unprotect operation as a connection workaround.

## Physical state at the stopping point

Last owner-reported setup: STM32 connected to the Mac through **UART1 USB-C**,
with ESP32-to-STM32 jumpers disconnected for programming. Current power/cable
state must be rechecked when resuming. The large USB-A socket is a **host** port;
the earlier Mac connection there was incorrect.

Owner reports checking the proposed later jumper connections:

| ESP32 | STM32 |
| --- | --- |
| GPIO17 / TX2 | PC11 |
| GPIO16 / RX2 | PC10 |
| GND | GND |

No continuity/voltage measurements or real inter-board UART exchange were recorded.
Leave power rails separate, connect jumpers only with both boards powered off, and
keep motors/servos disconnected throughout this LED-only experiment. STM32 source
uses `PC_11_ALT1, PC_10_ALT1` to select USART3/AF7 explicitly.

## Exact next dependency and resume sequence

**Before overwriting STM32 firmware, obtain confirmation that the V1.2 user LED
(LED1) is connected to PE10 and is active-low.** The owner was asked to check with
their teacher or supply the matching schematic. Generic Hiwonder documentation
suggests this mapping but does not establish it for the photographed V1.2 board.
The requested red light could instead be a power indicator. Do not silently treat
the current prototype profile as confirmed.

When the owner resumes:

1. Resolve that LED mapping; update source/profile if needed. Recheck branch/status,
   actual connected serial devices and backup integrity. Device paths can change.
2. Confirm a stable ROM session and recovery procedure before the first STM32 write.
   Backups are present; actual restoration is still untested. The owner has USB
   cable/adapter only and no ST-Link/J-Link. CubeProgrammer was not found in the
   checked application locations; installation has not been completed here.
3. Build and flash the confirmed STM32 LED-only profile, verify readback and record
   the result separately from a physical LED test. Do not merge PR #27 implicitly.
4. Power both boards through their appropriate independent inputs; with power off,
   reconnect the three verified UART wires. A single cable cannot independently
   power both boards at once.
5. From a phone, join the ESP32 network and open the printed HTTP address. Verify
   actual ON/OFF acknowledgements and visually observe the intended LED. Check
   link loss and reset behavior. Until then, real Wi-Fi association, webpage HTTP,
   UART acknowledgements and LED operation remain unverified.
6. Record all errors in #26 and update the README/PR with measured evidence.

No motion firmware, safety validation, permanent radio architecture decision or
C3 transport implementation is established by this experiment.
