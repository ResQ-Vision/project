# Recorded event model

Status: proposed `0.1-draft`; owners: events + localization + AI.
Model: [event](event.schema.json). Next decision: D9 timing, triggers and storage policy.

Record event/capture/map IDs, trigger reason, image reference, timestamp/quality and
the robot observation pose at capture, with uncertainty. A null pose/time is unknown,
not the map origin or image arrival time. Location is not the hazard's measured position.

Persist image and event before queuing inference. Associate late results by event ID
and reviewed schema/model version. Pending/completed/unknown are analysis states;
completed hazard labels are advisory. Failure/cancellation/invalid results must not
be turned into “no hazard detected”. Storage/retention/queue size and image hashing
need implementation decisions; do not promise unbounded logs or a particular filesystem.
