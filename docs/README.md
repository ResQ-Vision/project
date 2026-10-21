# Documentation entry point

Read [project scope](project/requirements.md), [current architecture](architecture/system.md),
[source hierarchy](project/sources.md) and [startup](development/startup.md) first.
Then select a role below. Read archived sources only when resolving provenance questions.

| Role | Read next | Owned module | Shared interfaces |
| --- | --- | --- | --- |
| Integration / planning | [Roadmap](project/roadmap.md), [open decisions](project/open-decisions.md) | docs/project, docs/architecture | [All contracts](../contracts/README.md) |
| Motion and safety | [Hardware](hardware/README.md), [safety](architecture/safety.md) | [motion STM32](../firmware/motion-stm32/README.md) | motion commands, telemetry, arbitration |
| C3 controller | [Arbitration](../contracts/motion/README.md) | [manual C3](../firmware/manual-c3/README.md) | direct manual commands, authority |
| Camera | [Events](../contracts/events/README.md) | [ESP CAM](../firmware/esp-cam/README.md) | capture request/response |
| Server / links | [Transport](architecture/transport.md), [API](../contracts/server-api/README.md) | [server](../server/README.md) | telemetry, camera, LiDAR, authority, events |
| Localization / mapping / navigation | [Frames](../contracts/conventions.md), [safety](architecture/safety.md) | server localization/mapping/navigation | scan, telemetry, commands |
| AI | [Model research](research/ai-model.md) | [AI worker](../ai/README.md) | inference requests/responses |
| Frontend | [API](../contracts/server-api/README.md), [events](../contracts/events/README.md) | [web](../web/README.md) | status, manual intent, event display |
| Test / evidence | [Testing](development/testing.md) | [tests](../tests/README.md) | schemas, fixtures, fault scenarios |
| School writing | [School requirements](school/requirements.md) | docs/school, original references | evidence and AI assistance records |

[Roles and boundaries](development/roles.md) define handoffs; [worktrees](development/worktrees.md)
isolate concurrent changes. Use
[feature specifications](features/README.md) for larger tasks and
[ADRs](architecture/decisions/README.md) for significant decisions.

Approval state: architecture is user-confirmed; draft schemas remain proposed.
Implementation/evidence state: [validation](development/validation.md).

Hebrew school documentation: [project explanation](school/project-description.md),
[book outline and completion tracking](school/book-plan.md), and
[live-proposal update and source review](school/source-review-2026-10-14.md).
