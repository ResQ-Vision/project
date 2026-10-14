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

[Official working proposal](https://docs.google.com/document/d/1_ZeKJPhYXvrlZp5wWuPeibg2ie_6kLH27qAnhqbATOU/edit)
governs official wording, as explicitly selected by the user on 14 October 2026.
It has been corrected directly to match accepted architecture. The
[previously linked document](https://docs.google.com/document/d/1fzNJpmtbakEgXjv7uT-z_8NCtRAehNbJFDoFE5lqjn0/edit)
is historical and must not replace this working document.
Use [source review](source-review-2026-10-14.md) and [D11](../project/open-decisions.md)
for the remaining checklist, illustration/layout and school-acceptance review.

Five collision-free trials, ≤1 s physical command-loss stop and ≤0.30 m mean position
error are planned project targets from the proposal. No original school source reviewed
here establishes them as universal grading thresholds. Define the actual test protocol.

## Required records

Use [AI assistance log](ai-assistance.md), [evidence template](evidence-template.md) and
[test procedures](../development/testing.md). Retain original measurements, logs/images,
code/config versions, faults and corrections. The migration provides no physical results.

## Documentation follow-up, 14 October 2026

The specified live proposal was updated with explicit user authorization to match accepted
front steering, rotating ToF and direct C3 architecture. See [readback and remaining review](source-review-2026-10-14.md).
The corrected working URL above supersedes the first document selection. The engineering
checklist remains unaligned; school approval remains open.
[Book planning and evidence tracking](book-plan.md) covers current-year sections 17–25.
The current-year extraction, page 18, also states a 30 October coordinator submission deadline;
verify the original PDF and the school's internal date. The earlier caution about importing
prior-year deadlines does not mean the current-year circular omits that date.

Subsequent design change: [ADR 0005](../architecture/decisions/0005-lidar-only-distance-sensing.md) removes the separate ToF. Earlier proposal readbacks are historical; #6 must align current live wording and the designated tldraw diagram. No school approval is implied.
