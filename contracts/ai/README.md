# Local AI application models

Status: proposed `0.1-draft`; owners: AI + events.
Models: [request](request.schema.json), [result](result.schema.json).
Next decision: D7 model/runtime/actual API; D9 categories/quality/thresholds.

Request carries event/capture IDs, stored image reference and fixed category IDs.
Result carries the same event ID, status, advisory label, category scores, quality,
actual model/runtime identity and latency. Synthetic fixtures do not identify a real runtime.
Score domain [0,1] is a proposed adapter convention, not verified native model output
or calibrated hazard probability. Category identities/normalization remain evaluation work.

Unknown covers timeout/unavailable/poor evidence/invalid output; it cannot be scored as safe.
Completed responses require model/runtime identity and acceptable image quality.
Do not accept raw model output without adapter/schema/semantic validation. Bound requests,
image sizes, memory, queue and retries. Authentication and local IPC choice remain open.
AI can update recorded event analysis only; it cannot arm, command, disarm safety or clear stops.
