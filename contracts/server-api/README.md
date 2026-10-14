# PC Server API and WebSocket requirements

Status: proposed semantics; owners: server + web. Next decision: D4/D5 protocol/auth/ownership.
No running endpoints or final route/payload names are implied by this document.

HTTP must support component health, current state/map, event/image retrieval and capture
intent. WebSocket or equivalent live channel must carry telemetry, mode/owner acknowledgement,
sensor age/quality, pose/map revisions, stop cause and event/analysis changes.

Manual controls submit intent to server under explicit selected ownership and command
expiry; the server forwards only fresh eligible intent to motion ESP32. Direct C3 ownership
must be visible and cannot be overridden merely by an active browser connection.
Map/pose revision IDs, units/frame, clock context and uncertainty must be defined in the API PR.

Specify API version negotiation, IDs, auth/origin policy, message sizes/rates, reconnect
snapshot/resync and failure errors. Reject invalid/unauthorized input without changing
drive state; lost lease/reconnect cannot re-arm. UI displays unknown/unavailable separately
from “no hazard detected”. A domain is unnecessary for the initial same-WLAN browser demo.

Add OpenAPI/typed WebSocket schemas with the first approved server contract, rather than
invent routes here. Use the event/AI DTO schemas for review of persistence/advisory boundaries.
