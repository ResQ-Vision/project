# Motion ESP32

Status: planned module; no executable implementation or hardware results yet.

## Ownership

Own rear encoder feedback, front steering, IMU, contacts, local stops and final C3/laptop authority. Do not apply differential-drive kinematics or obsolete ToF assumptions.

Read [architecture](../../docs/architecture/system.md),
[safety](../../docs/architecture/safety.md) and
[interfaces](../../contracts/motion/README.md).

## Build and tests

PlatformIO/ESP-IDF/Arduino and exact board are unresolved. Choose/pin toolchain and add reproducible build/config plus native tests in the first implementation PR.

Repository contract checks run from root using `python -m unittest discover -s tests -v`
after installing root development requirements. They do not execute this module.

Before integration: valid/invalid/stale messages, restart/reconnect and resource-failure
scenarios must be tested against the reviewed contract version. Record actual evidence.
