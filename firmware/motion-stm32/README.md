# Motion STM32 controller

Status: planned module; no executable implementation or hardware results yet.

An isolated [Wi-Fi LED experiment](../experiments/wifi-led/README.md) now has
compilable source. It is separate from this planned motion module and has no
physical upload, LED or motion-safety validation.

## Ownership

Own rear encoder feedback, front steering, IMU, contacts, local stops and final C3/laptop authority. Do not apply differential-drive kinematics or obsolete ToF assumptions.

Read [architecture](../../docs/architecture/system.md),
[safety](../../docs/architecture/safety.md) and
[interfaces](../../contracts/motion/README.md).

## Build and tests

Selected board: Hiwonder ROS Robot Controller V1.2, STM32F407VET6 (owner photos).
Obtain complete V1.2 firmware sources, matching schematic and recoverable factory image;
pin compiler/SDK/debugger and prove build/flash/restore before motion bring-up. Vendor
Keil/serial/SWD tutorials are research leads, not a verified local toolchain. Add real
build/config commands and native tests with the first implementation PR.

Wireless host/C3 transport is unresolved; STM32 is the final motion authority, not a
radio bridge. Do not assume onboard WiFi, ESP-NOW, factory ownership enforcement or
command-loss safety. Read [board context](../../docs/hardware/stm32-controller.md).

Repository contract checks run from root using `python -m unittest discover -s tests -v`
after installing root development requirements. They do not execute this module.

Before integration: valid/invalid/stale messages, restart/reconnect and resource-failure
scenarios must be tested against the reviewed contract version. Record actual evidence.
