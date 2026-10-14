# ESP CAM S3

Status: planned module; no executable implementation or hardware results yet.

## Ownership

Own bounded capture requests, capture IDs, image transfer and capture-time quality. Send images to PC Server over WiFi; local safety remains with motion ESP32.

Read [architecture](../../docs/architecture/system.md),
[safety](../../docs/architecture/safety.md) and
[interfaces](../../contracts/camera/README.md).

## Build and tests

Select exact board/sensor and pinned toolchain; add build instructions and real capture tests with the first implementation.

Repository contract checks run from root using `python -m unittest discover -s tests -v`
after installing root development requirements. They do not execute this module.

Before integration: valid/invalid/stale messages, restart/reconnect and resource-failure
scenarios must be tested against the reviewed contract version. Record actual evidence.
