# Error documentation workflow

Approved by the user on 21 October 2026: keep detailed error history in GitHub,
with a lightweight repository index and selective reading by agents.

## Record every encountered error

Record failures encountered during project work, including software bugs, failed commands,
setup/dependency/access errors, CI/build/test failures, hardware/integration faults and
incorrect generated artifacts that require correction. Record errors fixed immediately,
not just unresolved blockers. Expected negative-test outcomes are test evidence, not new
incidents; unexpected failures in those tests are incidents. Do not invent missing history.

Use one Issue labeled `error-log` per significant defect. Add `bug` for product defects.
Routine setup/command/artifact errors may share one dated session Issue, but each distinct
failure needs a numbered entry with the fields below. Repeated identical failures may be
grouped with observed dates/counts; preserve changed symptoms and unsuccessful attempts.
Search existing Issues before creating duplicates. Link related development tasks.

Record promptly once the failure is understood enough to describe; update investigation
as work continues and finish the record before PR/handoff. Do not postpone recording until
root cause or a fix is known. Use `unknown`, `not attempted` or `not verified` honestly.

## Required detail in the Issue

- Occurrence date/time and timezone, recording date and reporter. If exact time/date is
  unknown, say so; for retrospective records distinguish event date from recording date.
- Module, OS/toolchain/dependency versions, relevant hardware/configuration, base commit,
  feature branch and affected contract/version where applicable.
- Expected versus observed behavior, exact error text, triggering command/action, working
  directory, input/preconditions and reproducible steps, or why reproduction is unavailable.
- Impact, including affected data, integration and any hardware/safety implications.
- Investigation chronology: attempted fixes, their actual results, and relevant logs or
  screenshots. Distinguish hypotheses from confirmed cause; preserve unsuccessful attempts.
- Root cause (or unknown), workaround versus permanent fix, exact changed behavior/files,
  and fixing commit/PR; for an operational correction with no code change, say so.
- Verification date, environment/version, exact commands/procedure, actual outcome and
  regression coverage (or reason unavailable). Separate software tests from physical tests.
- Remaining limitations, next action/owner if known, and current resolution state.

Keep sanitized, relevant log excerpts in the Issue; attach or commit stable evidence and
link it. Do not rely only on expiring CI artifacts, local paths or inaccessible chats.
Never upload credentials, tokens, personal data or secrets; mark redactions explicitly.

## Resolution and retention

Use these explicit states in the Issue body: `investigating`, `fix proposed`, `fix merged`,
`verified`, or `deferred / unresolved`. GitHub open/closed alone is not verification.
For code fixes, keep the Issue open until the fix is merged into the intended branch and
verification is recorded. An independently verified command/environment correction can
close without a code merge; record that distinction. Deferred/rejected work must retain
its unresolved status and reason, not claim verification. Reopen/link a recurrence.

Keep closed Issues and their investigation/evidence. Append dated corrections rather than
silently rewriting an earlier failed attempt as a success. An ADR is only needed when the
fix changes a major design decision; do not duplicate incident narratives in architecture docs.

## Index and selective reading

[docs/errors/README.md](../errors/README.md) is a discovery index: date, module, short
symptom/search keywords and Issue link only. The linked Issue owns detail and current status.
Add/update the index with the task PR, including fixed session errors. Do not copy whole
Issues or raw logs into context, startup, roadmap or AGENTS files.

Normal startup reads the brief agent rule, not the historical index or Issue bodies.
When diagnosing a failure, search index keywords/module first, then search `error-log`
Issues (open and closed) if needed, and read only matching records. Directly relevant
open blockers/safety faults remain required task context; selective reading must not hide them.

Examples:

```sh
rg -n -i 'encoder|timeout' docs/errors/README.md
gh issue list -R ResQ-Vision/project --label error-log --state all --search 'encoder timeout' --limit 30
gh issue view 17 -R ResQ-Vision/project
```

Issue templates guide manual creation; API/CLI-created Issues must include the same fields.
If GitHub is unavailable, keep a sanitized pending record locally, disclose the blocker,
and publish/index it when access returns. Never claim it was saved in GitHub before it was.

## PR and handoff

Every PR/handoff declares `Errors encountered: <Issue links> / none`. `none` is a factual
statement, not a default to leave unchanged. Link all relevant session/defect records,
update their evidence and the index before handoff, and report publication blockers.
The repository checker validates local documentation links; it cannot prove completeness
or truth of error reporting. Reviewer inspection remains necessary; no automatic capture
of every tool/agent failure is implied. Historical backfill is incomplete unless audited.
