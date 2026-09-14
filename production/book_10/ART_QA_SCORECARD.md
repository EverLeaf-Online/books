# Book 10 — Birds — Artwork QA Scorecard

## Scope
- B019: illustrations 01–30
- B020: illustrations 31–60
- Target interior pages: 9–127, odd pages only
- Target trim: 8.5 × 11 in
- Master art target: 2550 × 3300 PNG

## Page-level approval checklist
Each illustration must pass every item before `qa_status` can move to `Pass`.

- [ ] Correct species/bird type and recognizable anatomy
- [ ] Wings, feet, beak, tail, eyes, and feather groups are plausible for the named bird
- [ ] No accidental extra limbs, duplicated wings, merged toes, broken beaks, or impossible joints
- [ ] Subject occupies roughly 55–70% of the page
- [ ] Entire subject remains inside the 0.50 in safe area
- [ ] Bold smooth outer contours with simpler thinner interior detail
- [ ] Large enclosed coloring areas suitable for ages 4–8
- [ ] Pure black line art on white; no gray, shading, hatching, gradients, textures, or color
- [ ] No words, letters, numbers, labels, signatures, watermarks, or decorative border
- [ ] Habitat elements are simple, large, and secondary to the bird
- [ ] Lower caption/fact area remains visually clear
- [ ] No cropped wings, tail, feet, crest, or bill
- [ ] File name exactly matches `artwork_manifest.csv`
- [ ] Artwork visually matches the listed subject and fact context

## Bird-specific checks
- Flight-capable birds: wing shape and feather placement must be believable.
- Raptors: talons and hooked bills must be strong but child-friendly, not graphic.
- Parrots/toucans/hornbills: bill proportions must remain species-appropriate.
- Waterbirds: webbed feet, leg length, bill shape, and body posture must fit the species.
- Flightless birds: do not add oversized functional flight wings.
- Do not mix defining traits from different species simply to make the page more decorative.

## Batch gates
### B019
- [ ] 30/30 generated
- [ ] 30/30 file names verified
- [ ] 30/30 page-level QA reviewed
- [ ] 0 unresolved `Needs Fix`
- [ ] Ready for assembly

### B020
- [ ] 30/30 generated
- [ ] 30/30 file names verified
- [ ] 30/30 page-level QA reviewed
- [ ] 0 unresolved `Needs Fix`
- [ ] Ready for assembly

Book 10 is assembly-ready only after both batches pass completely.
