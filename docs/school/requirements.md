# School requirements and evidence

Pair project, 5 units, exam code 841589, IoT theme. Original sources are preserved in
`resources/originals/`, with checksums in [manifest](../../resources/sources.json).
Text extraction loses tables/formatting; consult original pages for final assessment.

## Current-year authority

[תשפ״ז circular](../../resources/originals/חוזר%20מפמר%20תשפז%20-%20הנדסת%20אלקטרוניקה%20ומחשבים.pdf):
- Page 15: paired project includes at least two controllers, with one receiving/sending
  information through the Internet. Same-laptop AI calls do not satisfy this exchange.
- Page 22: paired project requires two independent communicating projects/subsystems,
  with at least one controller Internet-connected; a working physical prototype is required.
  Count alone does not establish approval of the chosen subsystem split.
- Pages 25–26: engineering work log plus AI-assistance annex with key prompts, critical
  analysis, adjustments and clarity about independent versus AI-assisted work; actual
  component measurement/debugging evidence and student understanding of code/hardware.

These pages are identified by PAGE markers in the checked-in extraction. Verify the PDF
layout when preparing a formal citation. Supervisor/examiner acceptance is not recorded.

## Prior-year and template sources

[תשפ״ו guidelines](../../resources/originals/הנחיות%20וקריטריונים%20לביצוע%20פרויקטים%20תשפו.docx)
are historical. They state a single proposal PDF and a coordinator deadline of 30 October.
Do not carry that deadline forward as a confirmed תשפ״ז school date.
Two original proposal templates have identical SHA-256 values; both are retained.
Their fields/structure are useful, not proof that the current proposal is approved.

## Current proposal and conflicts

[Specified live proposal](https://docs.google.com/document/d/1fzNJpmtbakEgXjv7uT-z_8NCtRAehNbJFDoFE5lqjn0/edit)
governs official wording. A [newer edited copy](https://docs.google.com/document/d/1_ZeKJPhYXvrlZp5wWuPeibg2ie_6kLH27qAnhqbATOU/edit)
contains mixed old/new descriptions. Neither is silently overwritten by this migration.
Use [source audit](../project/sources.md) and [D11](../project/open-decisions.md) to resolve
which live version is to be submitted and align it with user-confirmed architecture.

Five collision-free trials, ≤1 s physical command-loss stop and ≤0.30 m mean position
error are planned project targets from the proposal. No original school source reviewed
here establishes them as universal grading thresholds. Define the actual test protocol.

## Required records

Use [AI assistance log](ai-assistance.md), [evidence template](evidence-template.md) and
[test procedures](../development/testing.md). Retain original measurements, logs/images,
code/config versions, faults and corrections. The migration provides no physical results.
