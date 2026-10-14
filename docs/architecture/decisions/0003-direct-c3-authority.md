# ADR 0003: Direct C3 manual path

Status: Accepted direction. Date: 14 October 2026.
Source: research chat 12 October (“it should connect to the esp 32 directly”);
reconfirmed explicitly in the migration.

The C3 controller sends manual-driving commands directly to motion ESP32, bypassing
the laptop. Browser and autonomy intent still pass through PC Server.

Final motor authority must therefore be enforced on motion ESP32 across both links.
The server coordinates its own intent sources and observes the ESP's acknowledged owner;
it cannot be the only authority gate. Source selection, command expiry and explicit
stopped handovers are required. C3 loss must not automatically enable server/autonomy motion.

Exact C3 board, controls, transport, identities, acknowledgements, leases and ownership
epochs remain proposed. This ADR does not choose ESP-NOW or a numerical timeout.
Fault-injection tests must cover simultaneous commands, replay, reconnect and lost handover.
