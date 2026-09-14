# Book 12 — Reptiles & Amphibians Artwork QA Scorecard

## Production batches
- **B023:** subjects 1–30
- **B024:** subjects 31–60
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

## Reptiles & Amphibians-specific accuracy checks
- [ ] Scales, shells, limbs, toes, tails, crests, frills, and gills match the named species or group
- [ ] Snakes are not given limbs; lizards, crocodilians, turtles, frogs, and salamanders keep plausible body plans
- [ ] Turtle/tortoise shells and crocodilian snouts remain anatomically recognizable
- [ ] Amphibian skin is represented with clean contours rather than texture-heavy shading
- [ ] Venomous species are shown neutrally and educationally, not striking at the viewer

## Batch gate
A batch is **Approved** only when all 30 images pass every required check. Any failed image is marked **Needs Fix** in `artwork_manifest.csv` and must be regenerated or corrected before assembly.

## Book gate
Book 12 may enter final interior assembly only when:
- B023 = 30/30 Approved
- B024 = 30/30 Approved
- artwork manifest has no Queued, Generating, Generated, Needs Fix, or Not Reviewed entries
- all 60 expected filenames are present in the canonical artwork workspace
