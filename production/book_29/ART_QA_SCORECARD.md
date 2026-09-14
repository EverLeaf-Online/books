# Book 29 — Animal Families — Art QA Scorecard

## Release gate

All 60 illustrations must pass before interior assembly is approved.

- Book gate: **60/60 Pass**
- B057 gate: **30/30 Pass**
- B058 gate: **30/30 Pass**
- Source catalog: `catalog/books/book_29/animals.csv`
- Artwork manifest: `production/book_29/artwork_manifest.csv`
- Interior assembly manifest: `production/book_29/interior_assembly_manifest.csv`

## Per-image checks

- Correct subject/habitat and recognizable anatomy
- One clear main family grouping; approximately 55–70% of usable drawing area
- Bold smooth outer contours with simpler thinner interior lines
- Large enclosed coloring spaces appropriate for ages 4–8
- Important anatomy remains inside the 0.50-inch safe-content area
- Lower page remains clear enough for separately typeset subject name and fun fact
- Pure black line art on white; no grayscale, shading, hatching, gradients, textures, borders, signatures, logos, watermarks, words, letters, or generated captions
- No cropped important anatomy, duplicated limbs/fins/wings, malformed faces, tangencies, or clutter
- Expected filename and batch assignment exactly match the artwork manifest

## Subject-specific review

- Every scene must visibly communicate a parent/young or family relationship, not merely multiple unrelated adults.
- Young animals must have plausible juvenile proportions and species-appropriate markings.
- Avoid implying family structures that conflict with the accompanying fact; show the relationship described by the catalog.
- Keep both adult and young readable without shrinking the main subjects below the intended coloring-book scale.
- For aquatic, bird, reptile, amphibian, and invertebrate families, preserve species-appropriate anatomy and egg/young stages where applicable.
- Do not add labels such as “mom,” “dad,” or “baby” inside generated art.

## Status rules

Use only: `Queued`, `Generating`, `Generated`, `Needs Fix`, `Approved`.

QA status is only: `Not Reviewed`, `Pass`, `Needs Fix`.

Do not mark the book ready for interior build until every row is `Approved` and every QA row is `Pass`.
