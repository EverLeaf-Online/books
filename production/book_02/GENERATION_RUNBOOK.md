# Book 2 — Ocean Animals — Artwork Generation Runbook

Book 2 is the first active original-art release target. B003/B004 are the only artwork batches in this runbook.

## Source of truth

- Artwork manifest: `production/book_02/artwork_manifest.csv`
- QA scorecard: `production/book_02/ART_QA_SCORECARD.md`
- B003 prompts: `production/artwork-batches/prompts/B003_book_02_ocean_01-30.txt`
- B004 prompts: `production/artwork-batches/prompts/B004_book_02_ocean_31-60.txt`
- Approved workspace: `production/artwork-workspace/book_02/`
- Expected structure:
  - `production/artwork-workspace/book_02/B003/`
  - `production/artwork-workspace/book_02/B004/`

Do not substitute filenames, reorder subjects, or bake animal names/facts into the artwork.

## Generation packet export

Validate that the prompt packs still match the artwork manifest:

```bash
python build/tools/export_artwork_jobs.py --book 2
```

Export the 60 machine-readable generation jobs when needed:

```bash
python build/tools/export_artwork_jobs.py --book 2 --output production/book_02/generation_jobs.csv
```

The exported CSV contains the exact batch, page, subject, filename, output path, source prompt pack, full image prompt, production status, and QA status for every illustration.

## Production waves

Generate and review in 10-image waves instead of allowing 60 unchecked images to accumulate.

### Wave 1 — B003 items 01–10
Bottlenose Dolphin through Walrus.

### Wave 2 — B003 items 11–20
Manatee through Green Sea Turtle.

### Wave 3 — B003 items 21–30
Loggerhead Sea Turtle through Blue Tang.

**B003 gate:** all 30 files must exist with exact filenames and pass visual + technical QA before B003 is considered complete.

### Wave 4 — B004 items 31–40
Angelfish through Flying Fish.

### Wave 5 — B004 items 41–50
Parrotfish through Hermit Crab.

### Wave 6 — B004 items 51–60
Lobster through Albatross.

**B004 gate:** all 30 files must exist with exact filenames and pass visual + technical QA before B004 is considered complete.

## Per-wave workflow

1. Generate only the current 10-image wave from the canonical prompt pack.
2. Save each PNG directly under its assigned B003/B004 output folder using the exact manifest filename.
3. Run technical validation against the Book 2 artwork root.
4. Perform visual species/anatomy QA using `ART_QA_SCORECARD.md`.
5. Mark failures `Needs Fix`; regenerate only failed items.
6. Change an item to `Approved` / `Pass` only after both visual and technical checks succeed.
7. Start the next wave only after the current wave has no unresolved `Needs Fix` items.

## Technical gate

Preferred master: **2550 × 3300 PNG**.

```bash
python build/tools/validate_artwork.py \
  --art-dir production/artwork-workspace/book_02 \
  --expected 60
```

During partial production, image count will be below 60; that is expected. The final Book 2 gate requires exactly 60 valid images.

## Locked visual standard

- black line art on white only
- no grayscale, color, shading, gradients, hatching, textures, text, signatures, logos, watermarks, or borders
- bold smooth outer contours and simpler inner detail
- large enclosed coloring spaces suitable for ages 4–8
- main subject roughly 55–70% of the usable drawing area
- all important anatomy inside the 0.50-inch safe-content target
- lower page left reasonably clear for separately typeset animal name + fact
- simple habitat context only; no clutter
- anatomically plausible subject with no duplicated or malformed body parts

## Completion handoff

When B003 and B004 are both 30/30 Approved and Pass:

1. run full artwork validation;
2. build paperback and hardcover interiors;
3. confirm 128 pages and blank reverses;
4. build paperback cover from final page geometry;
5. use the current exact KDP hardcover template for hardcover cover production;
6. clear KDP Previewer;
7. order proofs;
8. publish in the locked order: Kindle title record → Paperback → Hardcover.
