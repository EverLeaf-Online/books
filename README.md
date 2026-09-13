# MIST° Animal Coloring Adventures

Canonical production repository for the **MIST° Animal Coloring Adventures** Amazon KDP series.

## Catalog

- **30 books** total — catalog intentionally capped at 30
- **60 coloring pages per book**
- **128 print pages per book**
- **1,800 original-art briefs**
- **60 artwork batches** (`B001`–`B060`)
- Target age: **4–8**
- Author: **Paul Thach**
- Imprint / brand: **MIST°**

## Current publishing status

Book 1 — *Animal Coloring Book for Kids Ages 4–8*

- Kindle title record: **Blocked** because coloring books are not suited to Kindle
- Paperback: **In Review**
- Hardcover: **In Review**
- Original MIST° replacement artwork: staged in **B001–B002**

Books 2–30 have content, facts, page maps, listing metadata, production packets, artwork briefs, and build configuration prepared. The current production gate is approved original artwork.

## Repository layout

```text
catalog/                 Canonical catalog source and per-book animal/fact/page-map files
metadata/                KDP listing/upload metadata for Books 1–30
production/
  packets/               Per-book production packet files
  artwork-batches/       B001–B060 prompt packs
  artwork-workspace/     Approved-art drop structure and instructions
  book-01-replacement/   Book 1 original-art replacement source material
build/
  configs/               30 self-contained build configs
  tools/                 Interior/front-matter/art-QA build tools
qa/                      QA reports and readiness notes
docs/                    Roadmap, art direction, production rules
tracking/                Latest production tracker workbook
artifacts/               Packaged snapshots and generated export bundles
```

## Production sequence

1. Original artwork
2. Artwork QA
3. 128-page interior assembly
4. Paperback cover
5. Exact-template hardcover cover
6. KDP Previewer
7. Physical proofs
8. KDP publishing order: **Kindle title record → Paperback → Hardcover**

## KDP print standard

- Paperback: **8.5 × 11 in**, B&W, white paper, no bleed, matte
- Hardcover: **8.25 × 11 in**, B&W, white paper, no bleed, matte
- 128 pages
- Coloring pages on odd/right-hand pages
- Blank reverse after each coloring page
- KDP minimum gutter at 128 pages: **0.375 in**
- MIST° safe-content target: **0.50 in**
- 300 DPI source-art target
- Hardcover cover dimensions must come from the **current KDP hardcover calculator/template**; never derive them from the paperback formula

## Source of truth

The newest tracker, source files, build tools, QA files, and packaged production snapshot in this repository are the canonical project state. Superseded tracker/package versions stay out of the main tree unless deliberately archived.
