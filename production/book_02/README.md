# Book 2 — Ocean Animals Coloring Book for Kids Ages 4-8

Primary next-release target for MIST° Animal Coloring Adventures.

## Locked metadata
- Subtitle: 60 Bold & Easy Sea Creatures with Fun Facts
- Author: Paul Thach
- Imprint: MIST°
- 60 coloring pages / 128 total pages
- Paperback: 8.5 x 11, B&W white paper, no bleed, matte
- Hardcover: 8.25 x 11, B&W white paper, no bleed, matte
- Paperback target price: $9.99
- Hardcover target price: $17.99
- Publishing order: Kindle title record -> Paperback -> Hardcover

## Source files
- `catalog/books/book_02/animals.csv`
- `catalog/books/book_02/page_map.csv`
- `build/configs/book_02.json`
- `kdp/book_02.txt`
- `production/book_02/artwork_manifest.csv`
- `production/book_02/interior_assembly_manifest.csv`
- `production/book_02/ART_QA_SCORECARD.md`

## Artwork
- Batch B003: subjects 01-30
- Batch B004: subjects 31-60
- Approved art root: `production/artwork-workspace/book_02/`
- Preferred master size: 2550 x 3300 px
- Pure black line art on pure white
- No baked-in text, captions, page numbers, signatures, watermarks, grayscale, shading, gradients, or decorative borders
- Keep important linework inside the 0.50-inch safe-content target

## Canonical production path
`production/book_02/` is now the canonical Book 2 production directory.

The older `production/book-02-ocean/` directory is retained temporarily only for compatibility with any historical references. Do not add new production files there. New QA, manifests, assembly records, and release-prep files belong under `production/book_02/`.

## Completion gate
Book 2 is not considered finished until all of these are complete:
- [ ] 60 original illustrations generated
- [ ] all 60 pass species/anatomy visual QA
- [ ] all 60 pass technical artwork validation
- [ ] paperback 128-page interior built
- [ ] hardcover 128-page interior built
- [ ] paperback cover built from final 128-page geometry
- [ ] exact current KDP hardcover template retrieved and cover built from it
- [ ] fonts embedded / no annotations / no placeholders
- [ ] KDP Previewer has no blocking errors
- [ ] physical proof reviewed
- [ ] Kindle title record created first
- [ ] paperback submitted second
- [ ] hardcover submitted third

## Current blocker
Approved original artwork. Do not generate placeholder KDP files or reuse Book 1 shortcut-derived artwork.
