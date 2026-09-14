# MIST° Animal Series — Release Blockers

This file is the current release-gate source of truth for the 30-book Animal series.

## Book 1

Status: **Frozen — KDP review in progress**

- Paperback: In Review
- Hardcover: In Review
- Do not revise submitted files while review is active.
- Book 1 is not an active production blocker for Books 2–30.

## Books 2–30 — shared blocker

The primary blocker is original artwork.

A title cannot move to final interior/cover release until all 60 of its illustrations are:

- generated from the assigned prompt packs;
- saved under the exact expected filenames;
- visually reviewed;
- marked `Approved` in the artwork manifest; and
- marked `Pass` for QA.

After artwork approval, each book still requires:

1. final 128-page interior build;
2. automated artwork/interior validation;
3. PDF preflight;
4. paperback full-cover build and preflight;
5. hardcover cover from the current KDP calculator/template and preflight;
6. KDP Previewer with no blocking errors;
7. proof approval where required; and
8. KDP submission in the required format order.

## Catalog/source QA gates still open

### Book 20 — Endangered Animals
Before final upload, review current conservation suitability and taxonomy against recognized current sources. The current catalog intentionally avoids printing status labels on each page, but the title still requires the collection to remain defensible as an endangered/rare-animal book.

### Book 24 — River & Wetland Animals
Broad labels still needing a deliberate source-normalization decision before final artwork approval:

- River Otter
- Softshell Turtle
- Map Turtle
- Water Moccasin
- Leopard Frog
- Tree Frog
- Newt
- River Kingfisher

Do not silently invent a species during art review.

### Book 26 — Cute Animals
Resolved in this pass:

- `Panda` -> **Giant Panda**
- `Beluga` -> **Beluga Whale**

Broad labels still needing deliberate normalization or explicit generic approval before final artwork approval:

- Pika
- Rabbit
- Dwarf Rabbit
- River Otter
- Sloth
- Hummingbird
- Bluebird

### Book 27 — Rainforest Birds
- `Bowerbird` remains a broad label and requires a final naming/visual decision before approval.

### Book 28 — Sharks & Rays
Resolved in this pass:

- `Mako Shark` -> **Shortfin Mako Shark**, matching the existing fact and prompt intent.

Broad labels still requiring species-level visual/naming review:

- Dogfish Shark
- Hammerhead Shark
- Electric Ray
- Butterfly Ray
- Guitarfish
- Shovelnose Ray
- Sawfish
- Skate
- Devil Ray
- Mobula Ray
- Freshwater Stingray
- Baby Shark
- Ray Pup

## Catalog issues already resolved

These are no longer blockers:

- Book 15: duplicate Paso horse entry replaced with **American Bashkir Curly**.
- Book 21: corrected to **Greater Roadrunner**.
- Book 23: `Sidewinder Crab` mismatch replaced with **Ghost Crab** and propagated through catalog, page map, prompt pack, artwork manifest, assembly manifest, and QA.
- Book 25: duplicate `Lammergeier`/Bearded Vulture entry replaced with **Himalayan Snowcock** and propagated.
- Book 26: `Panda` normalized to **Giant Panda** and `Beluga` to **Beluga Whale**, including filenames and production manifests.
- Book 28: `Mako Shark` normalized to **Shortfin Mako Shark**, including filename and production manifests.
- Book 30: `Penguin Ice Nest` renamed **Penguin Nest** with corrected nesting wording and propagated.

## Prompt-pack coverage

- Book 1 B001/B002: frozen with Book 1 review; not an active release-wave requirement.
- Book 2 B003/B004: normalized prompt packs present.
- Books 3–30 B005/B060: normalized prompt packs present.

## Done definition — entire Animal series

The project is not `DONE` until:

- Book 1 review is resolved;
- Books 2–30 each have 60/60 approved original illustrations;
- every final interior and cover passes preflight;
- required proofs are approved;
- all intended KDP editions have been submitted; and
- repository tracking reflects the actual KDP state for all 30 titles.
