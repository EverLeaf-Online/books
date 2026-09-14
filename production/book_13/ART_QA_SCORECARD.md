# Book 13 — Dogs — Art QA Scorecard

## Gate

No illustration enters the interior until it is marked **Pass** here and **Approved** in `artwork_manifest.csv`.

## Page-level checks

- [ ] Correct subject/breed identity and recognizable defining traits
- [ ] Plausible anatomy and proportions for the specific subject
- [ ] Bold, smooth black outer contours with simpler thinner interior detail
- [ ] Pure black line art on a clean white background
- [ ] No grayscale, shading, hatching, gradients, textures, words, letters, numbers, signatures, or watermarks
- [ ] Main subject occupies about 55–70% of the page without crowding
- [ ] All important anatomy remains inside the 0.50-inch safe area
- [ ] No accidental crops, tangencies, doubled limbs, malformed paws/hooves, or floating parts
- [ ] Large enclosed coloring shapes suitable for ages 4–8
- [ ] Habitat/props limited to a few large, simple elements
- [ ] Lower caption zone stays clear for separately typeset subject name and fact
- [ ] Final master is 2550×3300 PNG (300 DPI target)

## Subject-specific accuracy

- [ ] Breed-defining head, ear, muzzle, tail, coat, and body traits remain distinguishable
- [ ] Brachycephalic breeds are simplified without exaggerating unhealthy facial structure
- [ ] Long-bodied, giant, toy, sighthound, spitz, herding, and working breeds keep believable proportions
- [ ] Coat patterns and furnishings are suggested with clean shapes rather than dense texture

## Batch gates

### B025 — subjects 1–30
- [ ] 30/30 files present with canonical filenames
- [ ] 30/30 page-level checks passed
- [ ] 30/30 marked Approved in `artwork_manifest.csv`

### B026 — subjects 31–60
- [ ] 30/30 files present with canonical filenames
- [ ] 30/30 page-level checks passed
- [ ] 30/30 marked Approved in `artwork_manifest.csv`

## Release gate

- [ ] 60/60 illustrations approved
- [ ] Interior assembly manifest filenames match approved art exactly
- [ ] No duplicate subject art or accidental reuse
- [ ] Final interior preflight passes with no blockers
