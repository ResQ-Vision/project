# Living project book

[book.md](book.md) is the editable Hebrew manuscript. [resq-vision-book.docx](resq-vision-book.docx)
is its reviewed Word export, following the user-supplied 2026 template. This is an
unfinished progress book, not a final submission or a technical specification.
Canonical architecture/contracts remain authoritative. No robot code was implemented.

The template's declaration and approval wording is retained as unsigned forms, with
a draft warning. Cover fields other than the known author/project/year remain blank.
Do not infer a current school, supervisor, partner or approval from last year's example.
The prior-year PDF informs presentation only; its components/code do not belong to this rover.
The repository Hebrew skill is used; its two referenced sample files are unavailable,
as recorded in the skill README. No claim is made that those samples were read.

## Update after every meaningful project change

1. Read the relevant canonical documents and actual code, evidence and GitHub work.
2. Update affected chapters in `book.md` and append an identified engineering/AI log row.
   Separate proposed, approved direction, implemented, simulated and measured results.
   Include the student's actual contribution only when recorded by that student.
3. Update [source-map.json](source-map.json) with the reviewed baseline, source hashes
   and open-PR state. It pins a snapshot; updates are deliberate, not inferred automatically.
4. Build the export from the retained template, then render and inspect every page.
   Never edit only the generated DOCX and overwrite that edit with a later build.
5. Refresh the contents page through the builder's `--page-map` option after rendering.
   This produces a static, correctly paginated snapshot. Word's live TOC field is also
   preserved and marked for update on opening. Recheck pagination after major edits.
6. Run the repository checks, book regression tests and `git diff --check`; record
   exact outcomes in [validation.md](validation.md). Commit the manuscript and export
   together in the feature PR. No automatic monitor is created by this task.

## Reproduce

The builder uses only Python's standard library. From the repository root:

```sh
python scripts/build_project_book.py
python -m unittest discover -s tests -v
python scripts/check_repository.py
```

Rendering uses the Codex Documents skill's `render_docx.py` with `--emit_pdf`;
that renderer and a Word-compatible layout engine are separate from the book builder.

For a changed manuscript, first build without the old cache by supplying a nonexistent
task-local path with `--page-map /tmp/resq-new-page-map.json`. Render that draft, identify
the actual starting page of every Heading 1 chapter, and update `page-map.json`.
Its `_manuscript_sha256` must be the SHA-256 of the exact `book.md` bytes. Rebuild with
the complete cache and render once more to verify that the contents page did not move
the chapters. The builder rejects incomplete or stale page maps.
Use a fresh output directory for each QA pass. A build alone does not establish visual quality.

The renderer's PDF/images are QA intermediates, not independent manuscript sources.
The source Word template stays byte-for-byte unchanged. Styles, page geometry and
headers/footers are retained. Only document body, update-fields setting and the new
diagram relationship/media are edited; package preservation is regression tested.

To edit the diagram, change `system-diagram.svg` and rasterize it to
`system-diagram.png` at 144 DPI with the bundled Node Sharp dependency, then rebuild
and visually inspect the Word export. The PNG is a derivative, not a separate design source.
See [template-contract.md](template-contract.md) for intentional content replacements.

Source and deliverable fingerprints are in `source-map.json` and the validation record.
The previous-year PDF remains at its user-supplied local path; it is not uploaded or
copied into Git. Review the source mapping before using a different year's template.
