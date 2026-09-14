# Book 30 — Animal Homes & Habitats — Art QA Scorecard

## Release gate

All 60 illustrations must pass before interior assembly is approved.

- Book gate: **60/60 Pass**
- B059 gate: **30/30 Pass**
- B060 gate: **30/30 Pass**
- Source catalog: `catalog/books/book_30/animals.csv`
- Artwork manifest: `production/book_30/artwork_manifest.csv`
- Interior assembly manifest: `production/book_30/interior_assembly_manifest.csv`

## Per-image checks

- Correct subject/habitat and recognizable anatomy
- One clear main subject/home composition; approximately 55–70% of usable drawing area
- Bold smooth outer contours with simpler thinner interior lines
- Large enclosed coloring spaces appropriate for ages 4–8
- Important anatomy and structural details remain inside the 0.50-inch safe-content area
- Lower page remains clear enough for separately typeset subject name and fun fact
- Pure black line art on white; no grayscale, shading, hatching, gradients, textures, borders, signatures, logos, watermarks, words, letters, or generated captions
- No cropped important anatomy, malformed structures, duplicated limbs, tangencies, or clutter
- Expected filename and batch assignment exactly match the artwork manifest

## Subject-specific review

- The home/habitat must be as visually recognizable as the animal and must match the named subject.
- Distinguish built structures (nest, lodge, web, hive, mound) from general habitats (savanna, reef, water hole, cliff).
- Show entrances/openings and structural form clearly where the subject is a burrow, den, cavity, sett, holt, or crevice.
- `Penguin Nest` (#43): depict a plausible stone nest or sheltered ice-free nesting ground; never draw a nest constructed from ice.
- Habitat pages should remain simple enough for ages 4–8; do not turn the background into dense scenery.
- Keep environmental context biologically plausible and avoid mixing incompatible species or habitat elements.

## Catalog review

The former `Penguin Ice Nest` wording has been resolved as `Penguin Nest` throughout the catalog, page map, B060 prompt, artwork manifest, and assembly manifest.

## Status rules

Use only: `Queued`, `Generating`, `Generated`, `Needs Fix`, `Approved`.

QA status is only: `Not Reviewed`, `Pass`, `Needs Fix`.

Do not mark the book ready for interior build until every row is `Approved` and every QA row is `Pass`.
