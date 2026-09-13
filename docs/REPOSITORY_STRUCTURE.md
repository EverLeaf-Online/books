# Repository organization

This repository is intentionally organized around the **current 30-book catalog**, not around chat/session version history.

## Canonical editable source

- `catalog/` — series master plus animal/fact and page-map source files.
- `metadata/kdp/` — KDP-ready listing metadata per title.
- `production/packets/` — per-book front matter copy, interior assembly manifest, cover brief, KDP preflight, and batch references.
- `production/artwork-batches/` — the 60 generation/production prompt packs.
- `production/artwork-workspace/` — approved-art drop structure; generated artwork is added only after QA.
- `build/configs/` and `build/tools/` — reproducible build/validation tooling.
- `qa/` — readiness reports and validation outputs.
- `docs/` — production rules, roadmap, art direction, and workflow documentation.

## Binary/current snapshots

- `tracking/` contains the latest tracker workbook.
- `artifacts/` contains packaged current snapshots/exports so the complete state is recoverable even if a generated binary is not browsable as text.

## No duplicate historical clutter

Superseded tracker versions, old queue variants, caches, and Python bytecode are intentionally not tracked. The full current production package is preserved as a versioned artifact.
