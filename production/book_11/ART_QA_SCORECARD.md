# Book 11 — Bugs & Butterflies Artwork QA Scorecard

## Production batches
- **B021:** subjects 1–30
- **B022:** subjects 31–60
- **Target:** 60 approved coloring illustrations before interior assembly

## Required checks for every page
- [ ] Correct subject and recognizable anatomy
- [ ] Child-friendly, plausible proportions for ages 4–8
- [ ] Bold smooth outer contours with thinner interior details
- [ ] Pure black line art on white; no grayscale, shading, hatching, gradients, or textures
- [ ] Subject occupies roughly 55–70% of the page
- [ ] All important anatomy stays inside the 0.50-inch safe area
- [ ] No cropped limbs, tails, wings, antennae, horns, shells, or other key anatomy
- [ ] Large enclosed coloring regions; no clutter or tiny unusable spaces
- [ ] Habitat/background uses only 5–10 large simple elements
- [ ] Lower caption area remains clear for separately typeset name and fact
- [ ] No words, letters, numbers, signatures, watermarks, logos, or decorative borders in artwork
- [ ] Master PNG is 2550×3300 or equivalent 300-DPI portrait quality
- [ ] Filename exactly matches `artwork_manifest.csv`

## Bugs & Butterflies-specific accuracy checks
- [ ] Insects show the correct number of legs when visible; spiders/scorpions are not drawn as insects
- [ ] Wings, antennae, mandibles, abdomens, and body segmentation match the named creature
- [ ] Butterfly/moth wing patterns are simplified for coloring without inventing misleading anatomy
- [ ] Aquatic insects and larvae are shown in plausible habitats when included
- [ ] Avoid scary or aggressive staging; venom/stingers may be anatomically present but not emphasized

## Batch gate
A batch is **Approved** only when all 30 images pass every required check. Any failed image is marked **Needs Fix** in `artwork_manifest.csv` and must be regenerated or corrected before assembly.

## Book gate
Book 11 may enter final interior assembly only when:
- B021 = 30/30 Approved
- B022 = 30/30 Approved
- artwork manifest has no Queued, Generating, Generated, Needs Fix, or Not Reviewed entries
- all 60 expected filenames are present in the canonical artwork workspace
