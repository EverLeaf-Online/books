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
- `Shortfin Mako Shark` must match shortfin mako anatomy.
- `Great Hammerhead Shark` must show the species' very wide hammer-shaped head and tall first dorsal fin.
- `Spiny Dogfish` must show a slender body and dorsal spines.
- `Pacific Electric Ray` should have a rounded disc and stout tail typical of torpedo rays.
- `Smooth Butterfly Ray` should have an extremely broad disc and very short tail.
- `Common Guitarfish` and `Shovelnose Guitarfish` must retain the flattened ray-like front plus shark-like tail, while remaining visually distinct from each other.
- `Smalltooth Sawfish` must have a long saw-like rostrum while retaining a ray body plan.
- `Clearnose Skate` must read as a skate with a broad diamond-shaped disc and clear snout area.
- `Ocellate River Stingray` must show a rounded river-stingray disc with simplified eye-like spot markings.
- Remaining broad catalog labels requiring final species-level visual review before release: Devil Ray, Mobula Ray, Baby Shark, and Ray Pup.
- `Manta Ray Pup`, `Baby Shark`, and `Ray Pup` should read clearly as juvenile animals without becoming cartoonishly infant-like.

## Status rules

Use only: `Queued`, `Generating`, `Generated`, `Needs Fix`, `Approved`.

QA status is only: `Not Reviewed`, `Pass`, `Needs Fix`.

Do not mark the book ready for interior build until every row is `Approved` and every QA row is `Pass`.
