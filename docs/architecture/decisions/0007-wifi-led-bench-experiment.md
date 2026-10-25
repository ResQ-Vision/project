# ADR 0007: Isolated ESP32 to STM32 Wi-Fi LED experiment

Status: Proposed implementation, 25 October 2026. Scope authorized by direct owner
request: connect to an ESP32 over Wi-Fi and use a webpage to control an STM32 LED.
The owner reports USB cable/adapter only, with no SWD probe. This does not approve
a permanent rover radio bridge or change accepted motion-controller ADR 0006.

Implement a self-contained bench experiment under firmware/experiments/wifi-led.
ESP32 hosts an access point and embedded HTTP page; a three-wire, 3.3 V UART link
carries explicit LED state commands and acknowledgements to STM32. STM32 owns the
LED output. Correlated acknowledgements and a fresh status query prevent the UI
from claiming confirmation based solely on an ESP32 transmission.

Use PlatformIO with pinned ESP32 and STM32 Arduino platforms for reproducible builds
on macOS. Bare-metal startup/register code would add unnecessary maintenance for this
experiment; a CubeIDE installation is optional. Use STM32 HSI 16 MHz to avoid an
unverified external oscillator profile. USB serial ISP is the proposed STM32 upload
path; bootloader entry, upload and restoration are unverified.

Alternative: reuse a factory LED command. Deferred because complete V1.2 firmware
and an applicable LED packet were not established; do not send guessed motor-control
packets. A direct ESP32-to-LED wire would bypass STM32 firmware and would not test
the requested MCU-to-MCU link. Router mode can follow later if needed; AP mode
avoids external infrastructure for the first experiment.

Consequences: custom firmware overwrites the STM32 application. Motors/servos must
be disconnected for this experiment; the demo provides no motor stop system.
PC10/PC11 USART3, PE10 active-low and ESP32 GPIO16/17 are provisional board-profile
choices pending exact module/revision validation. The owner's red light may be a
power LED. UART has no CRC/authentication/replay protection and cannot be promoted
to the motion protocol. ACK means GPIO readback, not measured LED illumination.

Source/build/tests and the remaining upload/bench procedure are in the
[experiment README](../../../firmware/experiments/wifi-led/README.md).
This work does not close hardware/firmware/authority Issues #2, #3 or #9.
