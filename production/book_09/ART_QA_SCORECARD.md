# Book 09 — Dinosaur Art QA Scorecard

## Scope
- Book: Dinosaur Coloring Book for Kids Ages 4–8
- Batches: B017 (pages 9–67) and B018 (pages 69–127)
- Total illustrations: 60
- Master format: 2550 × 3300 PNG, portrait 8.5 × 11
- Art style: bold & easy black line art for ages 4–8

## Page-level pass criteria
Each illustration must pass every item below before `qa_status` changes to `Pass`.

- [ ] Correct subject/species or prehistoric animal for the assigned catalog row
- [ ] Plausible anatomy for the intended animal; no accidental extra/missing limbs, heads, tails, horns, wings, digits, teeth, or fins
- [ ] Historically/scientifically reasonable silhouette for the subject; avoid movie-monster exaggeration
- [ ] Main subject occupies roughly 55–70% of the usable page area
- [ ] Entire subject remains inside the 0.50-inch safe area; no cropped anatomy
- [ ] Bold smooth outer contour with simpler/thinner interior detail
- [ ] Large enclosed coloring regions appropriate for ages 4–8
- [ ] Pure black line work on white background
- [ ] No grayscale, shading, hatching, gradients, texture fills, color, or muddy anti-aliased gray areas
- [ ] No words, letters, numbers, signatures, logos, watermarks, or decorative borders inside generated art
- [ ] Habitat/context limited to roughly 5–10 large simple elements
- [ ] No clutter or excessive tiny coloring spaces
- [ ] Lower caption/fact area remains visually clear for separately typeset text
- [ ] Illustration is clearly distinct from adjacent pages and not a duplicate pose/composition
- [ ] Filename exactly matches `artwork_manifest.csv`

## Prehistoric-specific review
- Feathered dinosaurs should not automatically be rendered as naked movie-style reptiles where evidence strongly supports feathers.
- Pterosaurs, marine reptiles, prehistoric fish, mammals, and birds must not be incorrectly presented as dinosaurs.
- Avoid speculative features presented as certainty when the source animal is known mainly from incomplete fossils.
- Favor recognizable, kid-friendly accuracy over hyper-detailed reconstruction.

## Batch gates
### B017 — subjects 01–30
- [ ] 30/30 expected files present
- [ ] 30/30 page-level QA passes
- [ ] No duplicate files or subject mismatches
- [ ] Naming and page mapping match manifest
- [ ] Batch approved for assembly

### B018 — subjects 31–60
- [ ] 30/30 expected files present
- [ ] 30/30 page-level QA passes
- [ ] No duplicate files or subject mismatches
- [ ] Naming and page mapping match manifest
- [ ] Batch approved for assembly

## Book-level release gate
Book 09 artwork is release-ready only when all 60 rows in `artwork_manifest.csv` are `Approved` and all 60 QA rows are `Pass`. Final interior assembly must then be preflighted for page order, blank reverses, margins, embedded fonts, and KDP print compatibility.
