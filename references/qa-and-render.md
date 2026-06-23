# QA And Render

## Final QA Gates

Content QA:

- Every claim has evidence.
- Numbers, quotes, legal statements, and financial claims have source traces.
- Source meaning is not overstated.
- Dense detail is preserved in notes or appendix when necessary.

Design QA:

- One slide has one primary role.
- One slide has one main claim.
- Hierarchy has three levels or fewer.
- Same-role slides use consistent title, margin, footer, and source-note treatment.
- Text does not overflow or become unreadable.

Asset QA:

- Preserved images have source trace.
- Factual images are not replaced by generated imagery.
- Critical regions are not cropped.
- Generated/replacement images are only non-factual and decorative.

Chart QA:

- Period, unit, baseline, and source are visible.
- Rebuilt values match source data or confidence is recorded.
- Original figure is preserved in appendix when needed.
- No axes, legends, labels, footnotes, or source notes are cropped.

Flow QA:

- First 3 slides establish context, problem/opportunity, and thesis.
- 5-8 slide rhythm shifts are present.
- Section sequence matches the chosen archetype.
- Appendix supports trust without overloading body slides.

Render QA:

- Render PPTX to PDF/images.
- Generate `contact_sheet.jpg`.
- Check title readability at thumbnail size.
- Check missing images, unexpected crop, low contrast, inconsistent footer/source notes, and text overflow.

## Useful Commands

Convert a scaffold outline to PPTX:

```bash
python3 scripts/outline_to_pptx.py slide_outline.json --out deck.pptx
```

Make a contact sheet from rendered PNG/JPG slides:

```bash
python3 scripts/make_contact_sheet.py rendered_slides/*.png --out contact_sheet.jpg
```

Check local toolchain:

```bash
python3 scripts/check_toolchain.py
```

Validate production artifacts:

```bash
python3 scripts/validate_deck_job.py OUTPUT_DIR --phase draft
python3 scripts/validate_deck_job.py OUTPUT_DIR --phase final
```

## Completion Rule

Do not claim a final deck is complete unless:

- `validate_deck_job.py --phase final` passes, or every failure is explicitly reported
- PPTX path exists
- exported PDF or rendered slide images exist
- contact sheet exists
- QA report states pass/fail/skipped checks

If a render tool is unavailable, say so and deliver a draft with explicit skipped render QA.
