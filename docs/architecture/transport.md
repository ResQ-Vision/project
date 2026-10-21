# Transport boundaries

Status: links are approved direction; wire formats, authentication and thresholds are proposed.

| Link | Driving configuration | Bench configuration | Open choices |
| --- | --- | --- | --- |
| Hiwonder V1.2 ↔ PC Server | Compatible wireless bridge/link TBD | Board USB serial / UART after revision check | Bridge hardware, framing, keys, replay/session checks |
| C3 → motion STM32 controller | Direct wireless input | Selected board's debugging interface | Compatible radio/bridge into STM32, acknowledgements and authority handover |
| ESP CAM S3 ↔ laptop | WiFi | WiFi plus programming cable | Capture API, bounded sizes/timeouts, capture-time clock mapping |
| LiDAR → laptop | Validated compatible wireless bridge | Direct USB where supported | Sensor, electrical interface, USB-host needs, bandwidth, timestamp quality |
| Browser ↔ laptop | HTTP/WebSocket on reachable WLAN | Same | Authentication, API version, origin policy and ownership leases |
| Server ↔ AI | Local IPC/API on laptop | Same | Runtime adapter, queue/memory limits and timeout |

Do not assume a USB-only LiDAR works on a basic UART MCU. Select the acquisition bridge
from the actual sensor datasheet and validate bandwidth, power and timestamp behavior.
Serial-first rates from the engineering checklist apply only as historical bench recommendations.
UDP framing, ESP-NOW and 300 ms leases have not been selected by this migration.

Transport-independent [models](../../contracts/README.md) do not authorize a wire protocol.
Record packet limits, endian/framing details, authentication, reboot/session behavior,
freshness and fault recovery in a reviewed interface PR before hardware integration.

Use receiver-local monotonic time for freshness. Cross-device monotonic timestamps need
clock identifiers and an explicit offset/uncertainty estimate; UTC is for logs only.

A domain is unnecessary for initial local browser access to the laptop on the same WLAN.
This does not establish Internet exchange or Internet remote-driving capability.
School Internet use must involve the approved controller subsystem and a real external
exchange; offline behavior must not compromise local stops. See [requirements](../school/requirements.md).

ADR 0006 removes the ESP32 motion board. No replacement ESP32 radio bridge is selected.
The C3 manual path still bypasses the laptop, but its physical radio/bridge is unresolved.
A serial-to-radio adapter may be proposed; the STM32 must enforce freshness/ownership
independently. Neither a generic USB HOST port nor the ROS product name establishes
LiDAR support, WiFi, or a need for a Raspberry Pi. See [board context](../hardware/stm32-controller.md).
