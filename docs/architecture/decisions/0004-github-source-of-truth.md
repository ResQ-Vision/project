# ADR 0004: Stateless GitHub development

Status: Accepted workflow. Date: 14 October 2026.
Source: user migration brief, applied to all accessible ResQ-Vision chats.

Keep current architecture, decisions, interfaces, module instructions, tasks and evidence
in a modular monorepo. Chats are disposable and are not a required runtime or development dependency.
AGENTS.md is the shared instruction format, with specialized directory-scoped instructions.

Independent agents work from issues and latest main, on feature branches with tests/docs,
then open reviewable PRs. Larger features use spec/plan/tasks; important decisions use ADRs.
No custom multi-agent orchestration framework is introduced.

Official proposal wording remains in its live Google Doc. Approved implementation
specifications belong in reviewed GitHub contracts/ADRs; snapshots are historical evidence.
The migration is not permission to merge its own PR or to rewrite live school documents.
