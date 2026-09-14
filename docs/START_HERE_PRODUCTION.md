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
- Books 2–30 have artwork manifests, QA scorecards, and interior assembly manifests
- B003–B060 prompt packs are present and normalized

## Book 1 handling

Book 1 is already submitted to KDP and is frozen until review finishes.

- Do not revise the submitted paperback or hardcover while review is active.
- Do not treat B001/B002 replacement work as an active release blocker.
- Resume Book 1 only if KDP returns a required correction or after review when a deliberate replacement edition/update is scheduled.

## Work order

1. Start original-art production with Book 2 B003/B004.
2. Continue through the first release wave: Book 8 B015/B016, Book 9 B017/B018, Book 13 B025/B026, Book 14 B027/B028.
3. Continue through the remaining B005–B060 batches according to release priority.
4. Validate each completed 60-image book with `build/tools/validate_artwork.py`.
5. Build interiors with `build/tools/build_all_ready.py`.
6. Produce paperback cover from the final 128-page manuscript.
7. Produce hardcover from the exact current KDP hardcover calculator/template.
8. Run KDP Previewer and clear every blocking flag.
9. Order paperback and hardcover proofs.
10. Publish each new title in the required order: **Kindle title record -> Paperback -> Hardcover**.

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

## Before final artwork approval

- Book 20: current conservation/taxonomy review
- Book 24: broad wetland labels review
- Book 26: broad cute-animal labels review
- Book 27: `Bowerbird` naming review
- Book 28: broad shark/ray labels review

Book 23, Book 25, and Book 30 previously flagged naming issues have already been corrected and propagated through their production files.
