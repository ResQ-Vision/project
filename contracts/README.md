# Shared interface requirements and proposed application models

All contracts here are **proposed**, version `0.1-draft`, pending owner/interface review.
None defines an approved firmware packet format, radio transport, timing constant or
running API. Machine models cover data whose meaning is useful to validate now; motion,
telemetry, ownership and API framing remain requirements in focused prose.

| Boundary | Canonical specification | Owner / next decision |
| --- | --- | --- |
| Motion, telemetry and final ownership | [Motion](motion/README.md) | Motion + C3 + server; approve D2–D5 before wire schema |
| Camera requests/results | [Camera](camera/README.md) | Camera + events; capture timing/transport/limits D9 |
| LiDAR acquisition timing | [Acquisition](lidar/README.md) | Acquisition + motion; hardware/frame/clock decision D6 |
| HTTP/WebSocket semantics | [Server API](server-api/README.md) | Server + web; endpoints/auth/owner acknowledgement D4/D5 |
| Recorded image/events | [Events](events/README.md) | Events; pose association/storage policy D9 |
| Local AI requests/results | [AI](ai/README.md) | AI + events; actual model/runtime/API D7/D9 |

Read [conventions](conventions.md). Each schema identifies draft status and owner using
metadata. JSON Schema Draft 2020-12 describes examples of internal application data,
not on-wire serialization. Fixtures are synthetic; tests validate shape and failure semantics.

Change contracts with a reviewed PR: document rationale/status, version, compatibility,
all affected producers/consumers and valid/invalid fixtures. Breaking changes need a new
version and explicit consumer migration. Draft examples do not bypass architecture approval.
Only claim an interface approved once its actual review is recorded.
