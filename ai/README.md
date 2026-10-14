# Laptop-local AI worker

Status: planned module; no executable implementation or hardware results yet.

## Ownership

Own runtime adapter, bounded requests, queue/timeouts and advisory responses. Run on the same laptop as server; never import/control motor authorization.

Read [architecture](../docs/architecture/system.md),
[safety](../docs/architecture/safety.md) and
[interfaces](../contracts/ai/README.md).

## Build and tests

Model/projector/runtime/API must be verified and pinned before real inference. No weights, runtime server or benchmarks are provided.

Repository contract checks run from root using `python -m unittest discover -s tests -v`
after installing root development requirements. They do not execute this module.

Before integration: valid/invalid/stale messages, restart/reconnect and resource-failure
scenarios must be tested against the reviewed contract version. Record actual evidence.
