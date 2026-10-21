# C3 manual controller

Status: planned module; no executable implementation or hardware results yet.

## Ownership

Send manual intent directly to motion STM32 controller. Use explicit ownership and fresh deadman input; report lost authority. Do not route this approved manual path through the laptop.

Read [architecture](../../docs/architecture/system.md),
[safety](../../docs/architecture/safety.md) and
[interfaces](../../contracts/motion/README.md).

## Build and tests

Exact board, controls, transport and firmware toolchain remain unresolved. No firmware build is available yet.

Repository contract checks run from root using `python -m unittest discover -s tests -v`
after installing root development requirements. They do not execute this module.

Before integration: valid/invalid/stale messages, restart/reconnect and resource-failure
scenarios must be tested against the reviewed contract version. Record actual evidence.

Here “direct” means bypassing the laptop. The radio/bridge compatible with STM32 remains unresolved; native ESP-NOW reception on the Hiwonder board is not assumed.
