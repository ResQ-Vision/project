# Safety boundary and verification gates

Approved requirements: STM32-local stopping independent of laptop/network/AI; one active
command authority; command expiry; explicit transitions; AI cannot authorize movement.
Recovery state machine, emergency-stop hardware and exact sensor-fault policies below
are engineering proposals until reviewed and physically tested.

## Required behavior to specify and test

- Motor drive remains disabled at boot/reset and until an explicit valid arm/start.
- Malformed, stale, replayed, wrong-session or unauthorized commands never refresh freshness.
- Front/rear contact trips stop locally. Independent command loss also stops locally.
- A stop cannot be defeated by pending camera transfer, sensor acquisition, I2C stall or inference.
- Laptop browser/autonomy and direct C3 commands cannot overlap in actuator authority.
- Handover first stops/disarms, revokes the old owner and creates a fresh ownership session;
  prior commands cannot acquire authority again. Proposed epoch/lease models are in contracts/motion.
- LiDAR loss inhibits autonomous movement. Manual degraded movement has no approved policy;
  define and review it before enabling that behavior.
- Camera/AI failure produces unavailable/unknown information, not permission to move.
- Fault clearance, reconnect and process restart must require explicit re-arm; no automatic reverse recovery.

Select a physical emergency stop, brake/coast behavior, driver-enable default and power
protection as part of the hardware review. Software STOP is not proof of physical stopping.
The ≤1 s proposal target measures command loss to physical standstill; detection time
alone does not satisfy it. Derive timeout/speed from measured worst-case stopping distance.

## Front-steering and sensing limits

Measure wheelbase, rear track, steering limits, turning radius and swept footprint;
validate reverse and turning stops as well as forward motion. Do not plan turn-in-place.
LiDAR coverage, acquisition timing and stale-scan behavior require measured validation.
The separate ToF and its rotation mechanism are removed; they cannot provide a fallback.
LiDAR detects only obstacles intersecting its plane. Contacts stop after initial contact.
There are no downward edge sensors in the baseline; do not claim cliff/drop detection.
Use a flat arena with mechanical protection appropriate to the test.

## Evidence

Use [test procedures](../development/testing.md). Hardware tests require actual equipment,
recorded configuration and physical measurements; schema checks are not hardware safety tests.
Before floor driving, resolve hardware/power, local-stop timing, authority and protocol
issues in [open decisions](../project/open-decisions.md).
