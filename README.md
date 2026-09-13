# MIST° Animal Coloring Adventures

Canonical production repository for the 30-book MIST° Animal Coloring Adventures KDP catalog.

Author: **Paul Thach**  
Imprint / brand: **MIST°**  
Series: **MIST° Animal Coloring Adventures**  
Catalog cap: **30 books**

The repository stores the source-of-truth catalog data, per-book animal/fact lists, page maps, KDP metadata, production packets, artwork-batch manifests/prompts, build tooling, QA rules, and production documentation.

## Production standard

- 60 coloring pages per book
- 128 print pages per book
- Paperback: 8.5 × 11 in, B&W, white paper, no bleed, matte
- Hardcover: 8.25 × 11 in, B&W, white paper, no bleed, matte
- Coloring pages on odd/right-hand pages
- Blank reverse after every coloring page
- KDP minimum gutter at 128 pages: 0.375 in
- MIST° safe-content target: 0.50 in
- Source artwork target: 300 DPI
- Animal name + fact are typeset separately from artwork
- Hardcover covers always use the exact current KDP hardcover template/calculator
- Publishing order: Kindle title record → Paperback → Hardcover

## Repository map

- `catalog/` — catalog index and per-book content sources
- `kdp/` — KDP listing/upload metadata
- `production/` — production packets, artwork batches, manifests, and working control data
- `build/configs/` — one build config per book
- `build/tools/` — validation, interior-building, and cover-spec helpers
- `docs/` — roadmap, art direction, workflow, and production notes
- `qa/` — QA reports and preflight records
- `artwork/` — approved-art drop structure and batch folders
- `releases/` — intentional final/submitted binary artifacts only

## Current status

The catalog is capped at 30 books: **1,800 coloring pages / 3,840 total print pages**.

Book 1 print editions are in KDP review; its original-art replacement is staged in B001–B002. Books 2–30 have content/listing production prepared. The active bottleneck is original MIST° artwork generation + QA, after which interiors, covers, Previewer checks, and proofs can proceed.

## Build flow

1. Generate original artwork from the batch prompt pack.
2. Put only approved art into the matching `artwork/book_XX/bXXX/` folder.
3. Run artwork validation.
4. Build the 128-page interior.
5. Build the paperback cover from the final manuscript page count.
6. Build hardcover cover from the exact current KDP hardcover template.
7. Run KDP Previewer and fix every blocking issue.
8. Order/approve physical proofs.
9. Publish in the required order: Kindle title record → Paperback → Hardcover.

See `docs/START_HERE_PRODUCTION.md` and `build/tools/README.md` for the operational workflow.
