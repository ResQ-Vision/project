# Tests and evidence boundaries

`contracts/` contains software checks of proposed application models and synthetic
valid/invalid fixtures in `fixtures/`. They cover unknown pose/range/time, acquisition
clock identity, camera failure, invalid scores, poor imagery and forbidden motor fields.

Run `python -m unittest discover -s tests -v` after installing root requirements-dev.txt.
No integration, firmware, navigation or inference implementation exists yet; do not
add an empty integration folder or report the current suite as a hardware test.
Actual component/integration tests arrive with implementation and reviewed contracts.
See [test plan](../docs/development/testing.md) for planned physical procedures.
