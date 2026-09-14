# Book 28 — Sharks & Rays — Art QA Scorecard

## Release gate

All 60 illustrations must pass before interior assembly is approved.

- Book gate: **60/60 Pass**
- B055 gate: **30/30 Pass**
- B056 gate: **30/30 Pass**
- Source catalog: `catalog/books/book_28/animals.csv`
- Artwork manifest: `production/book_28/artwork_manifest.csv`
- Interior assembly manifest: `production/book_28/interior_assembly_manifest.csv`

## Per-image checks

- Correct subject/habitat and recognizable anatomy
- One clear main subject; approximately 55–70% of usable drawing area
- Bold smooth outer contours with simpler thinner interior lines
- Large enclosed coloring spaces appropriate for ages 4–8
- Important anatomy remains inside the 0.50-inch safe-content area
- Lower page remains clear enough for separately typeset subject name and fun fact
- Pure black line art on white; no grayscale, shading, hatching, gradients, textures, borders, signatures, logos, watermarks, words, letters, or generated captions
- No cropped important anatomy, duplicated limbs/fins/wings, malformed faces, tangencies, or clutter
- Expected filename and batch assignment exactly match the artwork manifest

## Subject-specific review

- Preserve clear shark-vs-ray body plans, fin counts, tails, gill placement, and head shapes.
- Manta/stingray/skate silhouettes must remain distinct and readable.
- Sawfish are rays; sawsharks are sharks. Do not swap their body plans.
- Broad catalog labels requiring final species-level visual review before release: Mako Shark, Dogfish Shark, Hammerhead Shark, Electric Ray, Butterfly Ray, Guitarfish, Shovelnose Ray, Sawfish, Skate, Devil Ray, Mobula Ray, Freshwater Stingray, Baby Shark, and Ray Pup.
- For `Mako Shark`, the current fact specifically describes the shortfin mako; verify the illustration matches that species before approval.
- `Manta Ray Pup`, `Baby Shark`, and `Ray Pup` should read clearly as juvenile animals without becoming cartoonishly infant-like.

## Status rules

Use only: `Queued`, `Generating`, `Generated`, `Needs Fix`, `Approved`.

QA status is only: `Not Reviewed`, `Pass`, `Needs Fix`.

Do not mark the book ready for interior build until every row is `Approved` and every QA row is `Pass`.
