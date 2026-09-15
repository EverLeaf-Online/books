# Production Tracking

This folder is the compact operational view of the MIST° Animal Coloring Adventures pipeline.

Use `animal-series-status.csv` as the canonical lightweight tracker for book-level state. It is intentionally separate from the larger production workbook so repository status can be reviewed without opening a spreadsheet.

Status meanings:
- `KDP Review`: submitted to Amazon and waiting on review. Do not revise the submitted edition while review is active.
- `Production Staged`: metadata, source mapping, prompt packs, build config, artwork manifest, QA scorecard, and assembly manifest are ready, but approved original artwork/final files are not complete.
- `Blocked on Original Art`: the current next release target cannot advance to final interior/cover production until approved original illustrations exist.

Catalog/source cleanup is complete across Books 2–30, including Book 20 conservation/taxonomy review. The active series-wide bottleneck is now approved original artwork.

A book is not `Finished` until approved original artwork, final paperback/hardcover interiors and covers, Previewer QA, physical proof review, and the KDP publishing sequence have all been completed.
