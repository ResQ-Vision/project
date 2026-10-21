# Motion, telemetry and ownership requirements

Status: proposed interface requirements; confirmed architectural behavior is in ADRs.
Owners: motion STM32 controller, C3 and server. Next review: D2–D5 in docs/project/open-decisions.md.
No final field names, packets, transport or timing thresholds are defined here.

## Motion intent and telemetry

Represent commanded forward/reverse speed (m/s) and front-steering angle (rad), or a
reviewed calibrated rear-wheel/steering-target model. Do not use differential-drive
wheel difference as the yaw model. Steering zero/sign/limits, wheelbase and rear-speed
conversion require actual geometry/calibration. Include explicit stop and disarm behavior.

The approved command specification must define version, identity, boot/session, ordering,
active ownership, freshness, validity bounds, acknowledgements and invalid-command behavior.
Only accepted fresh commands may renew receiver-local command age. Select authentication,
packet sizes, rate and watchdog from measured hardware limits; checklist rates are examples.

Telemetry needs acquisition clock/time, encoder counts, steering target and observed/estimated
angle with quality, IMU, contact state, motor/stop state,
acknowledged active owner and last accepted command. Specify validity/age/units per reading.
There is no separate ToF; LiDAR coverage/freshness is handled by the acquisition contract.

## Authority at the actuator boundary

- PC Server selects browser versus autonomous intent; C3 sends directly to motion STM32 controller.
- Motion STM32 controller enforces one final owner across laptop and C3. Display only acknowledged ownership.
- Explicit source selection/handovers stop motion, revoke old intent and establish a new
  ownership/session boundary. Choose the exact epoch/lease/acknowledgement design in review.
- Out-of-order/replayed/wrong-session/unauthorized messages cannot move or renew freshness.
- STOP must safely override movement under the approved authentication/fault rules.
- Lost handover, source loss, reboot or reconnect may not resume previous movement automatically.
- Define fault latch/clear/arm independently of mode selection. Clearing a fault does not arm motors.

## Required integration evidence

Test simultaneous C3/server intent; losing each link; stale/replayed commands; partial
handover; firmware/server reboot; sensor/bus stalls; contacts and physical standstill.
No machine motion schema is added merely to imply these decisions are settled.
