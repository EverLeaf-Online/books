# MIST° 30-Book Production Toolchain

All commands below run from the repository root.

## Install dependencies

```bash
python -m pip install -r build/requirements.txt
```

## Structural preflight

```bash
python build/tools/preflight_all.py
```

Checks all 30 build configs, the 60-animal standard, and odd coloring-page numbering.

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

This command now reads each book's `artwork_root` and `output_root` directly from `build/configs/book_XX.json` so the repository has one source of truth for paths.

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
3. Interior assembly
4. Paperback cover
5. Exact-template hardcover cover
6. KDP Previewer
7. Physical proofs
8. KDP publishing order: Kindle title record -> Paperback -> Hardcover
