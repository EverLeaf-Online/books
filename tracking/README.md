# Production Tracking

This folder is the compact operational view of the MIST° Animal Coloring Adventures pipeline.

Use `animal-series-status.csv` as the canonical lightweight tracker for book-level state. It is intentionally separate from the larger production workbook so repository status can be reviewed without opening a spreadsheet.

Status meanings:
- `KDP Review`: submitted to Amazon and waiting on review.
- `Production Staged`: metadata, build config, source mapping, and production packet exist, but original artwork/final files are not complete.
- `Blocked on Original Art`: the next release target cannot advance to final interior/cover production until approved original illustrations exist.
- `Conservation QA Required`: Book 20 requires current status verification before upload.

A book is not `Finished` until approved original artwork, final paperback/hardcover interiors and covers, Previewer QA, physical proof review, and the KDP publishing sequence have all been completed.
