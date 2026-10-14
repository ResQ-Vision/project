# Project-book verification

Task date: 14 October 2026. Engineering baseline: `7224443a6ea9e6dfed1ed7f16bf8c659134734d6`.
Branch: `codex/project-book-20261014`, isolated from the dirty hardware-review checkout.
No firmware/server/web implementation or architecture changes. No hardware or model tests.

## Scope and evidence

The original DOCX template and previous-year PDF were read without modifying them.
Template: all 13 rendered pages reviewed, actual styles/section/TOC and declaration
slots inspected. Previous-year PDF: text extracted from all 61 pages, cover/contents
and representative diagram/hardware pages visually inspected. It is a design reference,
not a current component specification. The GitHub main version of the Yotam skill was
used; its two missing referenced sample files were not invented.

The exported progress book retains template package parts, page geometry, unsigned
forms, styles and footer. Instructional/example body content is replaced with source-backed
draft chapters. New diagram is conceptual, with unresolved electrical paths labeled.
The official-proposal correction in open PR #13 is recorded as separate progress,
not imported into the main baseline or silently merged. No live school document was edited.

## Checks

Final software checks used Python 3.11.15:

| Check | Observed result |
| --- | --- |
| `python scripts/check_repository.py` | Passed: 65 Markdown files, 191 local links, 4 school originals, 56 migration entries, 3 snapshots, 7 proposed schemas |
| `python -m unittest discover -s tests -v` | 8 passed: existing 2 contract tests plus 6 document regressions |
| `python -m pip check` | No broken requirements found |
| `git diff --check` | Passed |
| Renderer plus page inspection | 21 pages; all inspected, no clipping/overlap/missing glyphs; hardware chapter orphan page removed |
| Contents cache against rendered PDF | All 19 chapter/declaration entries point to actual chapter starts |
| Template preservation tests | Untouched package parts and section XML identical; source template hash unchanged |
| Final figure correction | Only page 6 changed from previous reviewed render; other 20 PNGs byte-identical, corrected page inspected |
| `render_and_diff.py` template versus export | Completed; all 21 final PNGs identical to the reviewed final render. Body replacement and expansion are intentional; one A4 section and template page furniture retained |

The first book-test run exposed a mistaken test phrase (`אינו` rather than the
manuscript's `אינה`); the assertion was corrected and the complete suite rerun.
The diagram was corrected during visual QA so the motion link visibly attaches to
PC Server, not the advisory AI worker. The PNG is rasterized from the retained SVG
with bundled Sharp, at 144 DPI, and embedded without changing section geometry.

Final DOCX SHA-256: `33346fa9572591b6a2dceeebef35c21bbe48d4cc276609f2e9d488c85ca2f63c`.
Rendered page maps and images were kept in task-local QA; they are not independent
project-book sources or claimed hardware results.
The initial dependency install using system Python 3.14 failed: pinned rpds-py 0.22.3
uses PyO3 0.23.3, which supports up to Python 3.13. Dependencies were installed successfully
under the repository's Python 3.11 CI baseline without changing any dependency pin.

The builder uses standard-library Python only. Rendering used the bundled Documents
runtime (Python 3.12.14) and its packaged renderer; PDF extraction was used to locate
actual chapter starts and verify cached contents pagination. Word live-field refresh
was unavailable; update-fields is enabled, and the delivered cache uses the rendered pages.

No physical result, benchmark, supervisor approval, partner identity or school-specific
deadline was fabricated. Human review, component choice, implementation and measured
evidence remain outstanding, as listed in the book and canonical open decisions.
