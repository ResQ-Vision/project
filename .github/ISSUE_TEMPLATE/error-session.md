---
name: Development error session
about: Group routine setup, command or artifact failures without losing details
title: '[Errors][YYYY-MM-DD] module or task'
labels: error-log
---

Session date/timezone / reporter / task / branch:

Copy the section below for EVERY distinct failure; group only identical repetitions,
with observed dates/counts. Keep unsuccessful attempts. Do not replace entries with a
success-only summary. Follow docs/development/error-documentation.md and index the Issue
in docs/errors/README.md before handoff.

## E1 — short symptom
### Record identity
Occurrence date/time + timezone (or unknown):
Recording date / reporter:
Module / environment / versions / hardware / base commit / branch:
Resolution state: investigating / fix proposed / fix merged / verified / deferred-unresolved

### Expected and observed behavior
Exact error / triggering command or action / working directory:
Reproduction steps and inputs (or why unavailable):
Impact / data / integration / safety:

### Investigation and attempts
Dated attempts and actual outcomes, including unsuccessful fixes:
Sanitized logs / screenshots / durable evidence links:
Confirmed root cause (or unknown; separate hypotheses):

### Fix and verification
Workaround versus permanent fix / changed files or operational correction:
Fix commit / PR (or no code change):
Verification date / environment / exact checks / actual results:
Regression coverage or why unavailable; software versus physical evidence:
Remaining limits / next action / owner if known:
