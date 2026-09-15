# Book 20 — Endangered Animals — Art QA Scorecard

Batches: **B039 / B040**

## Page-level pass criteria
- Correct subject identity and recognizable anatomy.
- No extra, missing, merged, or malformed limbs, wings, eyes, ears, tails, digits, horns, fins, or shells.
- Pure black line art on white only; no grayscale, shading, hatching, gradients, texture fills, words, letters, numbers, signatures, or watermarks.
- Bold smooth outer contours with simpler thinner interior detail.
- Subject occupies roughly 55–70% of the page and remains fully inside the 0.50-inch safe area.
- Large enclosed coloring shapes suitable for ages 4–8; no dense micro-detail or tiny trapped spaces.
- Habitat uses only a few large supporting elements and does not overpower the animal.
- Lower caption/fact area remains visually clear.
- No accidental border, crop, or clipped anatomy.

## Endangered-animal-specific checks
- Do not add sensational injury, traps, cages, weapons, or distress imagery.
- Species distinctions must remain visible for similar subjects such as rhinos, elephants, orangutans, tigers, pangolins, sea turtles, and crocodilians.
- Great hammerhead head shape, largetooth sawfish rostrum, gharial snout, pangolin scales, and condor/eagle bill and foot anatomy must be recognizable.
- `Saola` must show two long nearly parallel horns and clean white facial-marking regions.
- `Hainan Gibbon` must be a tailless gibbon with very long arms in a tropical canopy, not a tarsier or generic monkey.
- `Hirola` must show antelope proportions, curved horns, and the pale eye markings that distinguish the species.
- `Wild Bactrian Camel` must be the wild two-humped camel form, not a domestic Bactrian camel illustration with decorative tack.
- `Largetooth Sawfish` must retain a ray body plan with a long robust toothed rostrum.
- Marine mammals and sharks must use plausible fins/flippers and body proportions.
- Conservation status is not printed in the artwork itself.

## Conservation-source gate
The catalog has been normalized so the previous Near Threatened/generalized entries no longer drive release ambiguity:

- `White Rhino` -> **Saola**
- `Philippine Tarsier` -> **Hainan Gibbon**
- `Saiga` -> **Hirola**
- `Bactrian Camel` -> **Wild Bactrian Camel**
- `Sawfish` -> **Largetooth Sawfish**

The collection may include Vulnerable, Endangered, and Critically Endangered animals; those categories all fall within IUCN's threatened-species grouping. Final art approval must still match the exact named subject.

## Batch approval gate
A batch is approved only when **30/30 images** are marked `Pass` in `artwork_manifest.csv`. Any `Needs Fix` image blocks that batch from interior assembly.
