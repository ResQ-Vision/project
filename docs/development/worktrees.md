# Isolated concurrent development

Read root AGENTS.md and current status first. Each concurrent significant task owns
a branch and worktree; multiple Codex threads must not edit a shared checkout blindly.

```sh
git status --short
git fetch origin
git worktree list
git worktree add ../resq-issue-123 -b feature/123-short-name origin/main
cd ../resq-issue-123
```

Substitute the real issue/branch name. Check for existing branch/worktree before adding.
An uncommitted local change is not in origin/main; preserve it and document its owner.
Do not reset/clean/stash/discard user work or force-push/merge someone else's branch.
Never run destructive Git commands concurrently against the same working tree.

Read relevant local files again in the new worktree. Shared contracts land in a reviewed
PR before dependent consumer work assumes their approval. A peer PR is not a merged API.
If explicitly stacking branches, record base PR/commit and rebase/test once it merges.

Run applicable tests in your worktree, inspect diff, commit, push and open a PR.
Remove only your clean, completed worktree after verifying handoff; never force removal
of a worktree with uncommitted changes. Git history and PR remain the handoff record.
