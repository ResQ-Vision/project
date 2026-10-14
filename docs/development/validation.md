# Migration validation record

Performed on 14 October 2026 in the actual workspace, Python 3.12. CI targets Python 3.11.
No hardware, physical stopping, firmware build, PC Server runtime or model inference
was exercised. Proposed schemas and synthetic fixtures validate application data only.

## Commands and actual results

| Command / check | Result |
| --- | --- |
| Virtualenv + `python -m pip install -r requirements-dev.txt` | Installed in migration checkout and fresh worktree |
| `python scripts/check_repository.py` | Passed: 58 Markdown paths, 139 local links; 4 school originals, 56 manifest entries, 3 snapshots, 7 proposed schemas |
| `python -m unittest discover -s tests -v` | 2 tests passed; 7 schema definitions and 28 fixture cases (12 valid, 16 invalid) |
| `python -m pip check` | No broken requirements found |
| `git diff --check` | Passed |
| School circular page-marker review | Confirmed paired-controller Internet/subsystem wording at pages 15/22 and AI evidence at pages 25–26 |
| Original/archive manifest hashes | Preserved files and five archived summaries match original bytes |

External Markdown URLs were not HTTP-link checked. Three live Drive documents were
actually fetched and their text preserved. GitHub CLI API requests returned Forbidden;
connected GitHub issue search/writes worked. CI configuration is added; remote-run results
are reported with the PR when available, not inferred from local tests.

## Fresh-worktree exercise

Created `validation/stateless-startup-2026-10-14` at migration commit `bb32c2c` using
`git worktree add`; followed repository instructions, installed dependencies in its own
virtualenv and ran both check commands successfully. No prior transcript was needed
to locate documentation or execute setup. This was a repository-only review and clean
worktree exercise, not a separately spawned Codex agent or hardware test.

| Startup question | Repository-only finding |
| --- | --- |
| Correct current architecture? | system.md and ADRs: one laptop, isolated AI, rotating ToF/front steering, direct C3 with final ESP authority |
| Confirmed versus open? | ADR status, open-decisions and proposed contract metadata distinguish them |
| PC Server implementation? | server/ is the owned planned module; no executable implementation/build exists yet |
| Firmware and interfaces? | Role navigation leads to the three firmware modules and contracts index |
| Available test commands? | README/testing specify venv, pinned requirements, repository and contract checks |
| Isolated change? | Added an adequate-image/inconclusive-analysis fixture in the separate branch; tests passed |
| Reviewable handoff? | Clean commit `4e2ebf4` and diff contain only that fixture, with scope/test evidence |

The primary migration checkout stayed clean at `bb32c2c` while the isolated exercise ran.
Afterward the useful example was deliberately incorporated by cherry-pick as `58630b0`.
The exercise did not alter main, merge the migration or publish a second PR.

## Remaining limits

Hardware/toolchains, running server/web/firmware, model API/performance, physical stop
timing, combined-load isolation and school approval remain unverified. Source coverage
cannot certify older unseen/nonenumerable chats. The repository carries known decisions,
not permanent broadcasts into other chats. See source audit and GitHub decision issues.
