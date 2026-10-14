# Browser frontend

Status: planned module; no executable implementation or hardware results yet.

## Ownership

Render acknowledged mode/owner, sensor freshness, stop cause, pose/map uncertainty and events with pending/completed/unknown analysis. Send manual intent to PC Server; never silently reacquire drive authority.

Read [architecture](../docs/architecture/system.md),
[safety](../docs/architecture/safety.md) and
[interfaces](../contracts/server-api/README.md).

## Build and tests

Framework and build are not chosen. Add package lock and reproducible start/build commands in the first UI PR. Do not display mock values as measured results.

Repository contract checks run from root using `python -m unittest discover -s tests -v`
after installing root development requirements. They do not execute this module.

Before integration: valid/invalid/stale messages, restart/reconnect and resource-failure
scenarios must be tested against the reviewed contract version. Record actual evidence.
