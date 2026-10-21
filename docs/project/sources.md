# Source of truth and contradictions

Audit date: 14 October 2026. Exact source metadata, chat coverage and snapshot hashes:
[source-audit.json](source-audit.json). Latest inspected GitHub main: `a64031c`, including
the earlier merged PR removing obsolete host descriptions. Initial local tree was clean
on `work` at `a5c83d0`; migration branch was created from fetched main without discarding work.
Actual repository root is `/workspace/project`, beneath selected `/workspace`.

## Authority by responsibility

Follow-up: [live source review and authorized proposal edits, 14 October](../school/source-review-2026-10-14.md).
The user subsequently corrected the official working document to
[this proposal](https://docs.google.com/document/d/1_ZeKJPhYXvrlZp5wWuPeibg2ie_6kLH27qAnhqbATOU/edit).
It was read and corrected in place. The earlier document is a historical source, not
the working proposal. The table below and archived snapshot hashes describe the migration
read, not either document's current wording. The engineering checklist still requires alignment.

1. Latest explicit user decisions establish project direction. In this migration the user
   reconfirmed front steering and direct C3 → motion STM32 controller. A subsequent explicit decision
   removed separate ToF in favor of LiDAR-only distance sensing; see ADR 0005. The user
   designated the linked [tldraw board](https://www.tldraw.com/f/4aOaHZDyKxk2AseGkkgxy?d=v-358.-186.2651.1825.page) as תרשים מלבנים; corrections are pending.
2. The [user-selected live Hebrew proposal](https://docs.google.com/document/d/1_ZeKJPhYXvrlZp5wWuPeibg2ie_6kLH27qAnhqbATOU/edit)
   governs official school wording, not proof of implementation or technical compatibility.
3. The [engineering checklist](https://docs.google.com/document/d/1hNu4UcTtAlyoXaPMbntPuTFcWa2hmmdRNgN7wtSWM7A/edit)
   is implementation planning, subject to subsequent approved decisions.
4. Approved GitHub ADRs/interfaces govern implementation. Current ADRs record approved
   direction; schemas are explicitly proposed, pending review.
5. Actual code and tests establish implemented behavior; actual instrumented evidence
   establishes measured hardware/model performance. Neither may be inferred from proposals.
6. Old chats, generated diagrams/exports and assistant suggestions are supporting historical
   evidence. Dates alone do not turn them into approved or tested requirements.

## Sources read and observed differences

Historical observations from the migration audit follow. They do not designate today's
working proposal or describe the corrected live text.

| Source | Modification observed | Use / contradictions |
| --- | --- | --- |
| Specified original proposal | 12 Oct 2026, 14:55 Jerusalem | Laptop/local AI; still fixed side ToF and wheel-difference yaw descriptions |
| Engineering checklist | 12 Oct 2026, 14:55 Jerusalem | Detailed planning; side ToF, serial-first examples and generic differential-drive assumptions; WiFi update appended |
| [Edited proposal copy](https://docs.google.com/document/d/1_ZeKJPhYXvrlZp5wWuPeibg2ie_6kLH27qAnhqbATOU/edit) | 14 Oct 2026, 08:46 Jerusalem | Includes rear drive/front steering and WiFi; retains side ToF, home AI-host and edge-testing claims in other sections |
| Core planning/research/writing chats | Through 12 Oct 2026 | One laptop, remove downward sensors, rotating ToF/front steering; C3 direct link confirmed |
| Latest migration prompt + answer | 14 Oct 2026 | Codex-ready local repository; retain latest design and remove conflicting active statements |
| School circular תשפ״ז | Original preserved | Current school IoT/subsystem/AI-evidence requirements, not project-specific trial results |
| Prior-year guidelines/templates | Historical | Structural references; do not inherit obsolete dates as current commitments |
| Existing diagrams/PDF/Word/concept art | Historical snapshots | Not current sensor/host/wiring authority, even when filenames say “current” |

## Resolution

Active repository docs now use [system.md](../architecture/system.md) and approved ADRs.
Fixed side-ToF, differential-drive/turn-in-place, server-only C3 authority, Pi/home-host,
downward-edge and serial-only-driving assertions are removed from active architecture.
Original historical files are retained unchanged or archived; they may still contain those words.
The migration itself did not edit official documents. Subsequent user-authorized edits
aligned the working proposal, and the user selected its URL above. D11 retains checklist,
illustration/layout and school-acceptance review; proposal selection is resolved.

Model identity/runtime/API/performance claims remain unverified research leads.
Checklist timing/rate numbers are proposals, not approved measured safety thresholds.
Acceptance figures remain planned targets, not completed tests.

## Chat coverage limits

Full paginated histories of the five core project chats were read; the pinned migration
prompt chat was read. Archived Codex listings on local/durable hosts were inspected, with
related architecture and diagram histories reviewed as supporting material.
An unrelated repository explanation and a hardware-model question were inspected and excluded.
The local “Create sensor block diagram” example concerns smart glasses and is excluded.

Available listing is limited to 50 recent unpinned chats plus pinned chats. Archived ChatGPT
history cannot be listed from this cloud caller. All identified Codex source chats were read to completion.
This audit cannot certify unseen chats were recovered or broadcast rules into them.
Useful accessible ResQ-Vision decisions are now in Git; existing chats should use
[startup](../development/startup.md) against current files before further work.

## Latest controller and hardware context — 21 October 2026

The owner explicitly replaced the motion ESP32 with Hiwonder ROS Robot Controller V1.2;
photos establish STM32F407VET6 and board revision. The owner read LD-1501MG on the
steering servo; rear motors are likely JGB37-520R30-12 from partial label/photo and matching
vendor chassis documentation. The owner accepts the available battery as sufficient.
[ADR 0006](../architecture/decisions/0006-stm32-motion-controller.md) and
[board context](../hardware/stm32-controller.md) govern current implementation planning.
Earlier ESP32 wiring, exports, live proposal readbacks and school text are historical
until aligned; no new live-document/diagram update or physical test is claimed here.
