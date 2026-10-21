# ResQ-Vision

A school exploration-rover prototype for a flat, controlled arena: front steering,
initial 2D mapping, image capture and advisory hazard analysis.

**Start at [docs/README.md](docs/README.md).** A new coding chat needs only this
repository, its assigned issue, and the linked role documents.

Current direction, updated by the user on 21 October 2026:
- One laptop beside the arena runs the PC Server, navigation, mapping and a separate local AI worker.
- Hiwonder ROS Robot Controller V1.2 (STM32F407VET6) replaces the motion ESP32 and controls two rear encoder motors, front steering, IMU,
  front/rear contact sensors and independent local stops.
- A C3 manual controller sends commands directly to the motion STM32 controller.
- Separate ESP CAM S3 sends images to the laptop over WiFi.
- One 2D LiDAR uses USB on the bench; a compatible wireless bridge is unresolved for driving.

The owner accepts the available battery as sufficient; no further battery-selection request is open.
Motion wireless/C3 transport, V1.2 firmware access and electrical integration still need validation.
See [STM32 board context](docs/hardware/stm32-controller.md).

The architecture is approved direction. All message schemas are **proposed**, and
the robot modules contain ownership/build guidance, not working firmware or services.
No hardware trials or AI benchmarks have been performed by this migration.

## Development

Python 3.11 is the CI baseline; these checks also run on Python 3.12.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/check_repository.py
python -m unittest discover -s tests -v
```

Windows PowerShell activation: `.venv\Scripts\Activate.ps1`.

Use [AGENTS.md](AGENTS.md), the [startup procedure](docs/development/startup.md),
and [isolated worktrees](docs/development/worktrees.md) for concurrent tasks.
The workflow is Issue → feature branch → code/tests/docs → PR → review → merge.
The migration PR requires the user's review before merging.

## Evidence and planning

- [Architecture](docs/architecture/system.md) and [accepted decisions](docs/architecture/decisions/README.md)
- [Contract index](contracts/README.md) and [module roles](docs/development/roles.md)
- [Roadmap](docs/project/roadmap.md) and [open decisions](docs/project/open-decisions.md)
- [School requirements](docs/school/requirements.md) and [source hierarchy](docs/project/sources.md)
- [Migration report](docs/development/migration-report.md), [manifest](docs/development/migration-manifest.json)
- [Validation record](docs/development/validation.md)

Original school documents and historical assets remain under `resources/`.
They are evidence, not an alternative current specification.

Official working proposal, selected by the user on 14 October 2026:
[live Hebrew Google Doc](https://docs.google.com/document/d/1_ZeKJPhYXvrlZp5wWuPeibg2ie_6kLH27qAnhqbATOU/edit).
Use this document for proposal edits; earlier proposal URLs and exports are historical.
