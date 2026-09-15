# MIST° 30-Book Production Toolchain

All commands below run from the repository root.

## Install dependencies

```bash
python -m pip install -r build/requirements.txt
```

## Structural + synchronization preflight

```bash
python build/tools/preflight_all.py
```

Checks the full 30-book production mapping, including:
- all 30 build configs;
- 128-page / 60-coloring-page structure;
- 60 catalog subjects per active production book;
- odd coloring-page numbering from 9 through 127;
- 128-row page maps and blank reverse pages;
- subject/fact/page synchronization between catalog, artwork manifest, and interior assembly manifest;
- B003-B060 batch assignments for Books 2-30;
- artwork batch manifest metadata and subject ranges; and
- all 30 prompt subjects in each production prompt pack against the current catalog.

Run this after any subject/fact/name change and before final production builds. It is designed to catch partial propagation such as a catalog rename that was not carried into a prompt pack or manifest.

A lightweight GitHub Actions check in `.github/workflows/production-preflight.yml` now compiles the production tools, runs this preflight, and validates artwork-job exports for the first release wave whenever relevant files change.

## Export artwork generation jobs

Validate that a book's two prompt packs still match its canonical artwork manifest:

```bash
python build/tools/export_artwork_jobs.py --book 2
```

Export a machine-readable 60-job CSV:

```bash
python build/tools/export_artwork_jobs.py \
  --book 2 \
  --output production/book_02/generation_jobs.csv
```

Each exported job includes the batch, item number, interior page, subject, exact expected filename, output path, source prompt pack, combined full prompt, production status, and QA status. The exporter fails instead of silently continuing if prompt-pack subjects drift from the artwork manifest.

Book 1 is intentionally excluded while the submitted KDP editions are under review.

## Front matter

```bash
python build/tools/build_front_matter.py --root .
```

Regenerates paperback and hardcover front matter for all 30 books with embedded fonts.

## Artwork QA

```bash
python build/tools/validate_artwork.py --art-dir production/artwork-workspace/book_02 --expected 60
```

Checks image count, resolution, obvious color contamination, and approximate 0.50-inch safe-zone ink. Visual species/anatomy QA is still required.

## Build one interior

```bash
python build/tools/build_interior.py build/configs/book_02.json --edition paperback --art-dir production/artwork-workspace/book_02 --output generated/book_02/paperback_interior.pdf
```

The builder creates exactly 128 pages, places coloring pages on odd pages 9-127, leaves blank reverses, typesets animal name and fun fact separately from the image, and preserves a conservative 0.50-inch content safety target.

Use `--allow-placeholders` only for internal assembly tests, never for a KDP upload.

## Build every artwork-ready book

```bash
python build/tools/build_all_ready.py --root . --edition both
```

This command reads each book's `artwork_root` and `output_root` directly from `build/configs/book_XX.json` so the repository has one source of truth for paths.

## Paperback cover dimensions

```bash
python build/tools/paperback_cover_specs.py --pages 128
```

For 128 pages, B&W white paper:
- spine = 0.288256 in
- full paperback cover = 17.538256 x 11.250000 in

Hardcover dimensions are intentionally not guessed. Use the exact current KDP hardcover calculator/template.

## Production order
1. Original artwork
2. Artwork QA
3. Structural/synchronization preflight
4. Interior assembly
5. Paperback cover
6. Exact-template hardcover cover
7. KDP Previewer
8. Physical proofs
9. KDP publishing order: Kindle title record -> Paperback -> Hardcover
