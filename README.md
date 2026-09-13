# EverLeaf Books

Canonical repository for the **MIST° Animal Coloring Adventures** Amazon KDP production catalog.

## Catalog

- **30 books total**
- **60 coloring pages per book**
- **128 print pages per book**
- **1,800 total coloring illustrations**
- **3,840 total print pages**
- Author: **Paul Thach**
- Imprint / brand: **MIST°**

The catalog is intentionally capped at 30 books. Current work is focused on finishing the books, not adding more titles.

## Repository map

- `catalog/` — canonical catalog data and per-book animal/fact/page-map sources
- `catalog/books/book_XX/` — per-book content sources
- `build/configs/` — build configuration for all 30 books
- `build/tools/` — validation, sizing, and automated build utilities
- `docs/` — roadmap, art direction, production rules, and start-here workflow
- `qa/` — catalog QA reports
- `artwork/` — approved-art workspace structure and production notes
- `production/` — production manifests, batch tracking, and downstream assembly files as they are added

## Locked production standard

### Paperback
- 8.5 x 11 in
- black & white interior
- white paper
- no bleed
- matte cover
- 128 pages
- target price: $9.99

### Hardcover
- 8.25 x 11 in
- black & white interior
- white paper
- no bleed
- matte case laminate
- 128 pages
- target price: $17.99
- final cover dimensions must come from the exact current KDP hardcover calculator/template

### Interior rules
- 60 coloring pages
- coloring pages on odd/right-hand pages
- blank reverse after every coloring page
- minimum KDP gutter at 128 pages: 0.375 in
- MIST° safe-content target: 0.50 in
- source artwork target: 300 DPI
- animal name and fun fact are typeset separately from artwork

## Publishing order

The required workflow is:

1. **Kindle title record**
2. **Paperback**
3. **Hardcover**

Coloring books may be blocked as saleable Kindle editions, but the Kindle title record is still created first in this workflow.

## Production flow

1. Create original MIST° artwork
2. QA species/anatomy/line quality/safe margins
3. Assemble the 128-page interior
4. Build paperback cover from final manuscript specs
5. Build hardcover cover from the exact KDP template
6. Run KDP Previewer and fix every flag
7. Order paperback + hardcover proofs
8. Submit/publish in the required order

Start with `docs/START_HERE_PRODUCTION.md`.

## Current priority

- B001-B002: original-art replacement for Book 1
- continue artwork batches through B060
- assemble each interior immediately after its 60 illustrations pass QA
- no Book 31+ unless the catalog strategy is deliberately reopened

## Special QA

- Book 1: replace the existing shortcut-derived art with original MIST° artwork for long-term catalog quality.
- Book 20: re-check endangered-species conservation status immediately before upload.
