# Fresh-agent startup

1. Clone `https://github.com/ResQ-Vision/project.git`; inspect status/remotes and fetch origin.
   Use latest `origin/main`; the documentation migration is merged. Preserve existing working changes.
2. Inspect open issues and PRs through GitHub or a connected GitHub tool. CLI examples:
   `gh issue list --repo ResQ-Vision/project` and `gh pr list --repo ResQ-Vision/project`.
   If access fails, record the limitation; do not invent an empty task list or merge state.
3. Read root `AGENTS.md`, `docs/README.md`, architecture and assigned role/module files.
   Use `docs/project/open-decisions.md` to identify blocked work. No chat history is needed.
4. Select one issue with explicit acceptance criteria and dependencies. Unmerged changes
   are not available APIs. For a larger change use `docs/features/template.md`.
5. Create an isolated worktree/branch using [worktrees](worktrees.md), based on latest main.
   Read ancestor/scoped AGENTS.md.
   Contract edits require coordinated review and version/fixture changes before consumers.
6. Install/run checks from README. Robot-module builds are not available yet; their READMEs
   list toolchain choices to resolve. Do not substitute a docs check for a firmware build.
7. Implement the small change, applicable tests and canonical documentation. Record source
   state and actual measurements only. Run required checks and inspect the diff.
8. Commit, push and open a PR with issue, behavior, test evidence, limits and approval needs.
   Use `.github/pull_request_template.md`. Review precedes merge; do not merge into main without authorization.

## Reusable prompt for any ResQ-Vision coding chat

> Work from the latest ResQ-Vision/project main branch and GitHub issue <number>.
> Read AGENTS.md and docs/README.md, then only my role's canonical documents.
> Inspect open PRs and dependencies. Do not rely on this chat's historical context.
> Keep proposed interfaces distinct from approved ones. Implement a focused change,
> run applicable tests, update evidence/docs and open a PR; hand off its commit and limitations.

This repository governs agents that read it. This migration cannot inject permanent
instructions into every existing/future chat or rewrite their historical messages.
