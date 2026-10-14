# Available checks and planned validation

## Available software checks

From root, install `requirements-dev.txt` in a virtualenv as in README. Then run:

```sh
python scripts/check_repository.py
python -m unittest discover -s tests -v
```

Repository check verifies active Markdown local file/fragment links, original-source
hashes, source-snapshot integrity, migration manifest and draft schema syntax.
The contract suite exercises synthetic valid/invalid cases; it does not run a robot.
CI uses Python 3.11. Dependencies are pinned, including jsonschema's direct/transitive requirements.
No firmware/server/web/model build can be claimed until toolchains/entry points exist.

## Planned physical/integration tests

Before bench/floor work, review hardware and safety gates. Record code/config/hardware,
instruments, battery, arena/floor/load, speed, sensor state and raw evidence per run.

| Test | Procedure / evidence | Gate |
| --- | --- | --- |
| Local stop | Wheels raised; contacts, valid-command loss, malformed/replay input, reset, blocking bus/scanner work | Motor disable/physical response independent of laptop/AI |
| Ownership | Simultaneous laptop/C3, source loss, lost handover, reboots/reconnect | One acknowledged ESP owner; no automatic motion restart |
| Steering/LiDAR | Calibrate steering limits/turning radius, LiDAR mount/time/coverage, rear encoder signs | Front-steering model and measured LiDAR coverage; no ToF fallback |
| Acquisition | LiDAR/camera invalid/stale/disconnect, radio bandwidth, clock offsets | Autonomy stops on LiDAR loss; uncertain capture/pose stays unknown |
| Stop geometry | Forward/reverse/turning at defined speed/load; command-loss trigger to standstill | Proposal target ≤1 s plus recorded worst stopping distance |
| Pose/map | Survey checkpoints and arena walls; compare capture-time estimate | Target mean Euclidean error ≤0.30 m; worst error/count and map comparison |
| Navigation | Five predefined full arena trials, obstacle/freshness faults | Target five collision-free runs with no unexplained safety bypass |
| Events/AI | Stored IDs, late/invalid/poor-image/timeouts, labeled images and combined laptop load | Correct association and unknown failures; no AI motor authority |
| School Internet | Approved controller subsystem exchanges actual external data | Demonstrated exchange and safe offline behavior |

Use [evidence template](../school/evidence-template.md). Targets are not completed results.
Unit/schema tests cannot verify local watchdog timing, physical braking or image-model accuracy.
