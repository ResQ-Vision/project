# PC Server

Status: planned module; no executable implementation or hardware results yet.

## Ownership

Own communication adapters, server-side browser/autonomy intent selection, ESP authority acknowledgements, telemetry validation, localization, mapping, navigation, persistent events and APIs. Separate control from heavy image/AI work.

Read [architecture](../docs/architecture/system.md),
[safety](../docs/architecture/safety.md) and
[interfaces](../contracts/README.md).

## Build and tests

Language/framework and module builds remain unresolved. Python/FastAPI is a historical candidate, not a final decision. Add dependency lock and run/test commands with the first implementation. Subdirectories are created only when they contain useful code.

Repository contract checks run from root using `python -m unittest discover -s tests -v`
after installing root development requirements. They do not execute this module.

Before integration: valid/invalid/stale messages, restart/reconnect and resource-failure
scenarios must be tested against the reviewed contract version. Record actual evidence.
