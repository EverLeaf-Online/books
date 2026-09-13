# MIST° Production Start

The catalog is capped at **30 books**. Do not add Book 31+ unless the catalog strategy is deliberately reopened.

## Ready now

- 30-book catalog
- 1,800 coloring-page slots
- 60 artwork batches (B001-B060)
- 30 build configs
- per-book animal/fact CSVs and page maps
- production roadmap and QA reports
- standardized KDP trim, margin, pricing, and publishing-order rules

## Work order

1. Generate/approve B001-B002 for Book 1 replacement art.
2. Continue through B060.
3. Validate each completed 60-image book with `build/tools/validate_artwork.py`.
4. Build interiors with `build/tools/build_all_ready.py`.
5. Produce paperback cover from the final 128-page manuscript.
6. Produce hardcover from the exact current KDP hardcover calculator/template.
7. Run KDP Previewer and clear every flag.
8. Order paperback and hardcover proofs.
9. Publish in the required order: **Kindle title record -> Paperback -> Hardcover**.

## Locked production standard

- Paperback: 8.5 x 11 in, B&W white paper, no bleed, matte
- Hardcover: 8.25 x 11 in, B&W white paper, no bleed, matte
- 128 pages
- 60 coloring pages
- coloring pages on odd/right-hand pages
- blank reverse after every coloring page
- KDP gutter minimum at 128 pages: 0.375 in
- MIST° safe-content target: 0.50 in
- source artwork target: 300 DPI
- author: Paul Thach
- imprint/brand: MIST°

## Special QA

- Book 1 replacement art is high priority; current shortcut-derived art is not the long-term MIST° standard.
- Book 20 endangered-animal status claims must be rechecked against a current recognized authority immediately before upload.
