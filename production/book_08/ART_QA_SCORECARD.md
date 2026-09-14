# Book 08 — Pets — Art QA Scorecard

Use this scorecard for all 60 final coloring illustrations in B015 and B016 before artwork is marked **Approved**.

## Per-page checks

Each illustration must pass every item below.

- [ ] Correct subject matches `catalog/books/book_08/animals.csv` and the assigned B015/B016 prompt.
- [ ] Anatomy is plausible and recognizable for the specific breed/species.
- [ ] Main subject occupies roughly 55–70% of the page.
- [ ] Entire subject is visible; no accidental cropping of ears, tails, paws, fins, wings, shells, or limbs.
- [ ] Strong smooth outer contour with thinner interior detail lines.
- [ ] Large, simple enclosed coloring areas suitable for ages 4–8.
- [ ] Pure black line art on a clean white background.
- [ ] No grayscale, shading, hatching, gradients, texture fills, or baked-in color.
- [ ] Habitat/prop details are simple and uncluttered, normally 5–10 large elements or fewer.
- [ ] No words, letters, numbers, signatures, watermarks, decorative borders, or generated text.
- [ ] Artwork stays inside the 0.50-inch MIST° safe-area target.
- [ ] Lower caption/fact area remains visually clear for separately typeset text.
- [ ] No obvious AI artifacts, merged anatomy, duplicate body parts, malformed eyes, broken paws, impossible joints, or stray marks.
- [ ] Final master is a clean portrait PNG, preferably 2550×3300 px.
- [ ] Filename exactly matches `production/book_08/artwork_manifest.csv`.

## Batch gate — B015, pages 9–67

- [ ] All 30 expected files are present.
- [ ] All 30 subjects match rows 1–30 of the canonical catalog.
- [ ] All 30 files pass every per-page check.
- [ ] `artwork_manifest.csv` rows 1–30 are marked `Approved` / `Pass` only after visual review.

## Batch gate — B016, pages 69–127

- [ ] All 30 expected files are present.
- [ ] All 30 subjects match rows 31–60 of the canonical catalog.
- [ ] All 30 files pass every per-page check.
- [ ] `artwork_manifest.csv` rows 31–60 are marked `Approved` / `Pass` only after visual review.

## Book-level approval gate

Book 08 artwork is production-ready only when **60/60** illustrations pass, both batches pass their 30/30 gates, filenames match the manifest, and the interior assembly manifest maps every approved image to the correct odd-numbered coloring page.
