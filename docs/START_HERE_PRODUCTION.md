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
- catalog naming/source cleanup is complete for Books 2–30
- Book 20 conservation/taxonomy review is complete
- structural preflight cross-checks catalogs, page maps, production manifests, artwork-batch metadata, and prompt subjects
- all Books 2–30 generation-job exports pass the production workflow: **29 books × 60 illustrations = 1,740 validated active jobs**

## Book 1 handling

Book 1 is already submitted to KDP and is frozen until review finishes.

- Do not revise the submitted paperback or hardcover while review is active.
- B001/B002 are explicitly frozen in the artwork batch manifest.
- Do not treat Book 1 replacement work as an active release blocker.
- Resume Book 1 only if KDP returns a required correction or after review when a deliberate update is scheduled.

## Work order

1. Start original-art production with Book 2 B003/B004.
2. Continue through the first release wave: Book 8 B015/B016, Book 9 B017/B018, Book 13 B025/B026, Book 14 B027/B028.
3. Continue through the remaining B005–B060 batches according to release priority.
4. Run `python build/tools/preflight_all.py` after catalog/prompt/manifest changes and before final builds.
5. Validate generation-job packaging with `python build/tools/export_artwork_jobs.py --book N`.
6. Validate each completed 60-image book with `build/tools/validate_artwork.py`.
7. Build interiors with `build/tools/build_all_ready.py`.
8. Produce paperback cover from the final 128-page manuscript.
9. Produce hardcover from the exact current KDP hardcover calculator/template.
10. Run KDP Previewer and clear every blocking flag.
11. Order paperback and hardcover proofs.
12. Publish each new title in the required order: **Kindle title record -> Paperback -> Hardcover**.

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

## Current blocker

There are no remaining catalog naming/source-review gates for Books 2–30, and the full production mapping/job-export CI is green.

The active bottleneck is now **original artwork production and approval**. A book cannot advance to final interior and cover production until all 60 illustrations are generated, visually reviewed, marked `Approved`, and marked `Pass` for QA.
