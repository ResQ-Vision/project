# Shared coding instructions

ResQ-Vision is a controlled-arena exploration rover with a laptop-hosted PC Server,
a separate AI worker on that laptop, and STM32-local motion safety. Start at docs/README.md.

1. Fetch the latest repository state before work. Read `README.md`, `docs/README.md`,
   `docs/development/startup.md`, relevant open issues/PRs and only the documents for your role.
2. Use approved ADRs and interfaces. `contracts/` currently contains proposed v0.1
   application models, not approved firmware packet formats. Do not deploy these as frozen protocols.
3. Use an isolated worktree for concurrent tasks (see docs/development/worktrees.md).
   Never reset, discard, force-push or run destructive Git operations against a peer working tree.
   Work on a focused feature branch based on latest `origin/main`; never assume another
   chat's branch was merged. Check the working tree before editing; preserve others' changes.
4. Keep changes small and testable. Larger features use the spec/plan/tasks template in
   `docs/features/`; a Spec Kit-inspired workflow is sufficient without an orchestration framework.
5. Respect module ownership in `docs/development/roles.md` and directory-scoped instructions.
   Coordinate shared contracts through issues and reviewed PRs, not hidden chat agreements.
6. Update canonical documentation when behavior changes. Do not add a master context dump
   or duplicate architecture/protocol instructions in several places.
7. Run the checks in `docs/development/testing.md` plus applicable module tests.
   Report failed/unavailable checks and their cause; do not claim tests you did not run.
8. Label proposed, approved direction, implemented and measured separately. Never invent
   hardware tests, model benchmarks, teacher approval, component availability or measurements.
9. Do not rely on inaccessible conversations. Persist useful decisions, evidence and unresolved
   work in this repository or GitHub issues before handoff. Chat excerpts are historical evidence only.
10. Hand off the branch/commit/PR, scope, tests, evidence, limits and next dependencies using
    `docs/development/handoff-template.md`.
11. Major hardware, safety, architecture or protocol changes require explicit owner approval
    recorded in an ADR and reviewed PR. Routine fixes within approved scope can proceed.
12. Preserve original school sources and Git history. Historical generators/exports must not
    overwrite live Google Docs. Keep school prose separate from code/contracts.
13. AI analysis is advisory and isolated from motor authorization. The motion STM32 controller must stop
    independently of server, network and AI. Follow `docs/architecture/safety.md`.
14. This migration PR must not be merged without user review. A clean checkout must remain usable
    without chat history; do not place required startup state only in local files.

15. Record every encountered error, even if fixed immediately, in a GitHub Issue labeled
    `error-log`; group routine failures in a dated session Issue with separate detailed entries.
    Follow [error documentation](docs/development/error-documentation.md): dates, exact symptom,
    environment/reproduction, failed attempts, cause or unknown, fix and actual verification.
    Link records in the PR/handoff and add short discovery entries in `docs/errors/README.md`.
    Do not read the error archive at normal startup. When diagnosing, search its index/module
    keywords and read only relevant Issues (including closed ones); always read relevant open
    blockers/safety faults. Report GitHub outages and preserve pending records until published.
