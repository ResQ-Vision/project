# Template contract

Retained authority: `template.docx`, the exact user-supplied
`__High_school_project_template2026 (1).docx`; fingerprint in `source-map.json`.
Reference render: 13 pages, reviewed all pages in task-local QA.

- One portrait A4 section: 21.000861 × 29.700361 cm; top/bottom 2.54 cm,
  left/right 3.175 cm; first-page header/footer behavior retained.
- Original Hebrew David body typography, blue Heading 1/2, source table borders,
  source footer PAGE field and all original named styles/theme/numbering retained.
- Original document body paragraph indices 0–20: cover slots; replace name/title,
  project type, known exam/theme/year, leave school/logo/partner/supervisor/coordinator
  unspecified. Do not carry prior-year author metadata into the current cover.
- Indices 21–40: student declarations and supervisor/coordinator forms retained
  verbatim and unsigned. Insert a draft warning before the original declaration text.
- Optional thanks page: intentionally removed until user provides acknowledgements.
- Source TOC content-control: replace obsolete cached entries, retain live TOC field.
  Mark fields for update in settings; final page-map cache comes from actual render.
  Word field refresh is unavailable in this task; no LibreOffice save is used as a
  template authoring or field-refresh step.
- Source instructional paragraphs, example I2C/OLED/temperature functions, example
  prompt dated November and illustrative bibliography: remove from authored body.
  They are template data, not user instructions, project code or real citations.
- Main chapters: replace with supported material from `book.md`; reuse actual source
  paragraph properties, heading styles and table style. Clone source components when
  content grows. Chapter breaks are added intentionally for book navigation, without
  changing page geometry. Expansion beyond 13 pages is expected.
- New system figure: source in `system-diagram.svg`, raster preview in
  `system-diagram.png`; conceptual data/control/power paths, unresolved power clearly
  marked. English short figure labels avoid ambiguous bidirectional raster text;
  explanation/caption remains Hebrew. No historical rover illustration is reused.
- `word/document.xml`: editable body, preserve the exact final `sectPr`.
- `word/settings.xml`: only `w:updateFields` changes.
- `word/_rels/document.xml.rels`: append one image relationship only.
- `word/media/resq-system.png`: newly added figure.
- All other package members, including headers/footers, numbering, styles, theme,
  original media and opaque parts: preserve byte-for-byte. Original example screenshot
  is no longer referenced in the new body but stays in the preserved package.

No content controls other than the TOC are rewritten. There are no footnotes or
final technical drawing slots to fill with unsupported measurements. Required
section coverage is preserved, with the final-software chapter explicitly renamed
to current software because this is a progress draft. Blank reflection/data/code
fields remain visible. No generic visual preset replaces the retained template.
