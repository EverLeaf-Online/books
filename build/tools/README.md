# MIST° 30-Book Production Toolchain

## Structural preflight
`python Tools/preflight_all.py`

Checks the 30 build configs, the 60-animal standard, and odd coloring-page numbering.

## Front matter
`python Tools/build_front_matter.py --root .`

Regenerates paperback and hardcover front matter for all 30 books with embedded fonts.

## Artwork QA
`python Tools/validate_artwork.py --art-dir artwork/book_02 --expected 60`

Checks image count, resolution, obvious color contamination, and approximate 0.50-inch safe-zone ink.
Visual species/anatomy QA is still required.

## Build one interior
`python Tools/build_interior.py Build_Configs/book_02.json --edition paperback --art-dir artwork/book_02 --output built/book_02/paperback_interior.pdf`

The builder creates exactly 128 pages, places coloring pages on odd pages 9-127, leaves blank reverses, typesets animal name and fun fact separately from the image, and preserves a conservative 0.50-inch content safety target.

Use `--allow-placeholders` only for internal assembly tests, never for a KDP upload.

## Build every artwork-ready book
`python Tools/build_all_ready.py --root . --edition both`

## Paperback cover dimensions
`python Tools/paperback_cover_specs.py --pages 128`

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
