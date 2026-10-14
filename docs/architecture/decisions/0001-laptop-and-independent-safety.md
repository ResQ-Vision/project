# ADR 0001: Laptop deployment and independent safety

Status: Accepted direction. Date: 14 October 2026.
Source: migration brief; planning chat 12 October; user confirmation in this migration.

One laptop beside the arena hosts PC Server, mapping, navigation, storage, web APIs and
the separate local AI worker. AI receives bounded work and cannot block control, clear
faults or authorize motors. Motion ESP32 provides independent local stops and freshness.

The former onboard Raspberry Pi and separate home inference PC are superseded.
WiFi is the driving link; USB/UART is a tethered bench/debugging path.
Untethered LiDAR needs a verified wireless acquisition bridge.

Consequences: resource isolation and combined laptop-load measurements are required.
Local AI does not meet school Internet-exchange requirements. Exact model/runtime,
device models and safe timing remain open. This ADR records no completed experiment.
