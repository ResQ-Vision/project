# Camera acquisition models

Status: proposed `0.1-draft`; owners: camera + events. Next decision: D9 timing, limits and API.
Models: [request](capture-request.schema.json), [response](capture-response.schema.json).

The server allocates a capture ID; camera reports success with image reference and
acquisition clock/time, or failed/unavailable with a reason. An unknown capture timestamp
is null and cannot support precise capture-pose association. `image_ref` is an opaque
application/storage reference; transfer bytes and URL/authentication policy are unresolved.

Bound image dimensions/bytes, request concurrency and timeout in reviewed configuration.
Persist image/event before analysis. Retries reuse correlation IDs according to an
approved idempotency policy; duplicate/late captures must not update a different event.
Camera loss is visible and does not itself authorize motion or clear a stop.
