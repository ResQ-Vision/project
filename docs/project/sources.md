# Source of truth and contradictions

Audit date: 14 October 2026. Exact source metadata, chat coverage and snapshot hashes:
[source-audit.json](source-audit.json). Latest inspected GitHub main: `a64031c`, including
the earlier merged PR removing obsolete host descriptions. Initial local tree was clean
on `work` at `a5c83d0`; migration branch was created from fetched main without discarding work.
Actual repository root is `/workspace/project`, beneath selected `/workspace`.

## Authority by responsibility

Follow-up: [live source review and authorized proposal edits, 14 October](../school/source-review-2026-10-14.md).
The specified proposal was edited after this migration audit; the table below and archived
snapshot hashes describe the earlier read, not its current wording. The engineering
checklist and alternate proposal copy still require alignment.

1. Latest explicit user decisions establish project direction. In this migration the user
   reconfirmed front steering, rotating top ToF and direct C3 → motion ESP32.
2. The [specified live Hebrew proposal](https://docs.google.com/document/d/1fzNJpmtbakEgXjv7uT-z_8NCtRAehNbJFDoFE5lqjn0/edit)
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
The official docs are not edited: D11 records the remaining school-document contradiction
and choice of which proposal version to submit. No competing active master context is added.

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
