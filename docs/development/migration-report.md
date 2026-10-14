# Migration report

Branch: `migration/stateless-github-2026-10-14`; base: `a64031c`.
Local root: `/workspace/project`. Initial working tree was clean; no uncommitted user
implementation was discarded. No robot source/build existed in the baseline repository.
The updated Codex-ready prompt and user-confirmed architecture govern this migration.

## Resulting tree

```text
AGENTS.md, README.md, requirements-dev.txt
docs/
  README.md
  project/       requirements, roadmap, open decisions, sources and source audit
  architecture/ system, transport, safety, decisions/0001–0004 and template
  hardware/     component and calibration planning
  development/  startup, worktrees, roles, testing, handoff, migration and validation
  research/     model verification plan
  features/     substantial-feature spec/plan/tasks template
  school/       requirements, evidence template, AI-assistance log
firmware/
  AGENTS.md
  motion-esp/README.md
  esp-cam/README.md
  manual-c3/README.md
server/         module README and scoped AGENTS.md
ai/             module README and scoped AGENTS.md
web/            module README and scoped AGENTS.md
contracts/      conventions, proposed models and scoped instructions
  motion/       command/telemetry/ownership requirements, no final wire schema
  camera/       proposed capture intent/outcome models
  lidar/        proposed LiDAR and rotating-ToF acquisition models
  server-api/   API/WS semantic requirements, no running endpoints
  events/       proposed stored observation model
  ai/           proposed local request/result models
tests/          contract tests and synthetic valid/invalid fixtures
scripts/        repository link/provenance/structure checks
resources/      original sources, historical exports/diagrams and archives
.github/        issue/PR templates and validation workflow
```

## Files and authority

Five old context files moved unchanged into a dated archive; README/context entrypoints
and resource status pages were edited. School originals, existing archives and binary
diagrams/exports remain at their paths with original bytes. Text snapshots of three
actually accessed Drive docs preserve audit provenance without replacing live documents.
The full old-to-new mapping, actions and original hashes are in [manifest](migration-manifest.json).
`git diff --stat` and PR file list enumerate newly created/edited/moved files.

Canonical entry: [docs/README.md](../README.md). Architecture: [system](../architecture/system.md).
Requirements: [requirements](../project/requirements.md). Interfaces: [contracts](../../contracts/README.md).
Approval/evidence precedence: [sources](../project/sources.md). Fresh startup and all role
boundaries: [startup](startup.md), [worktrees](worktrees.md), [roles](roles.md).

## Superseded active claims removed

- Fixed left/right ToF replaced by one angle/time-stamped rotating top ToF.
- Differential-drive yaw/turn-in-place replaced by calibrated front-steering requirements.
- C3 route uncertainty/laptop-only authority replaced by direct C3 input with final ESP authority.
- No active Pi, separate inference host, downward-edge sensing or serial-only driving architecture.
- Older resource summaries no longer compete with canonical documentation.
- Proposed rates/model APIs/acceptance figures are not presented as approved or measured facts.

Original history retains conflicting source text. Live school proposal/checklist contradictions
remain open in [source audit](../project/sources.md); they were not overwritten.

## Review limits and next task

Seven machine schemas are proposed internal data models; no motion packets, API routes,
timing thresholds, toolchains or hardware pinouts are frozen. Module READMEs identify
planned components and missing entry points; there is no PC Server implementation yet.
No empty placeholder code tree or autonomous orchestration framework is added.

Read [validation](validation.md) for commands/results and fresh-worktree exercise.
Remaining decisions D1–D11 are in [open decisions](../project/open-decisions.md), with
GitHub issues linked when created. No robot trial, model benchmark or teacher approval is claimed.

Recommended first development task: resolve motion board, steering/scanner hardware,
pins/power and local-stop design in a reviewed hardware/interface sheet. Then implement
an ESP bench slice with motors disabled at boot, contact/command-loss stop and measured
evidence before integrating wireless floor driving.

Migration PR is for review; do not merge without user approval. Existing/future chats
must adopt current repository startup rules; historical messages cannot be rewritten.
