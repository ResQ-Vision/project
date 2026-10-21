---
name: Bug or significant error record
about: Detailed persistent failure, investigation and fix history
title: '[Error] '
labels: error-log, bug
---

## Record identity
Occurrence date/time + timezone (or unknown):
Recording date / reporter:
Module / environment / versions / hardware / base commit / branch:
Resolution state: investigating / fix proposed / fix merged / verified / deferred-unresolved

## Expected and observed behavior
Exact error / triggering command or action / working directory:
Reproduction steps and inputs (or why unavailable):
Impact / data / integration / safety:

## Investigation and attempts
Dated attempts and actual outcomes, including unsuccessful fixes:
Sanitized logs / screenshots / durable evidence links:
Confirmed root cause (or unknown; separate hypotheses):

## Fix and verification
Workaround versus permanent fix / changed files or operational correction:
Fix commit / PR (or no code change):
Verification date / environment / exact checks / actual results:
Regression coverage or why unavailable; software versus physical evidence:
Remaining limits / next action / owner if known:

Keep this record even after resolution; do not claim unobserved hardware results.
Index it in docs/errors/README.md. Follow docs/development/error-documentation.md.
