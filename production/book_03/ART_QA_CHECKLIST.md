# Book 3 Artwork QA — Farm Animals

Use this checklist for every illustration in B005-B006 before moving the file into the approved-art workspace.

## Per-image visual QA
- [ ] Correct subject and breed/type where specified
- [ ] Child-friendly ages 4-8 appearance
- [ ] Anatomy is plausible; no extra/missing limbs, eyes, ears, tails, horns, wings, or hooves
- [ ] Main subject is clearly recognizable at a glance
- [ ] Main subject occupies roughly 55-70% of usable drawing area
- [ ] Full body shown when practical; no accidental cropping
- [ ] Simple farm-appropriate setting
- [ ] Roughly 5-10 large supporting background elements maximum
- [ ] Large enclosed coloring spaces; no dense micro-detail
- [ ] Bold smooth outer contours; thinner interior detail lines
- [ ] Pure black line art on pure white only
- [ ] No grayscale, shading, cross-hatching, gradients, textures, or solid black backgrounds
- [ ] No words, letters, numbers, signatures, watermarks, page numbers, or decorative borders
- [ ] Important linework stays inside the 0.50-inch safe-content target
- [ ] Lower caption/fact area remains clean
- [ ] No duplicate composition that makes two pages look nearly identical

## Technical QA
Run:
`python build/tools/validate_artwork.py --art-dir production/artwork-workspace/book_03 --expected 60 --strict`

Preferred source master: 2550 x 3300 px at approximately 300 DPI.

## Batch sign-off
### B005 — subjects 01-30
- [ ] 30/30 generated
- [ ] 30/30 visually reviewed
- [ ] 30/30 technically validated
- [ ] 30/30 approved

### B006 — subjects 31-60
- [ ] 30/30 generated
- [ ] 30/30 visually reviewed
- [ ] 30/30 technically validated
- [ ] 30/30 approved

Interior assembly may begin only after both batches are fully approved.
