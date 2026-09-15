#!/usr/bin/env python3
"""Structural and cross-file preflight for the 30-book MIST° catalog."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIGS = ROOT / "build" / "configs"
BATCH_MANIFEST = ROOT / "production" / "artwork-batches" / "manifest.csv"
PROMPT_DIR = ROOT / "production" / "artwork-batches" / "prompts"
PROMPT_RE_PREFIX_DASH = re.compile(r"^(\d{1,2})\s*[—–-]\s*([^:]+):\s")
PROMPT_RE_MIDDLE_DASH = re.compile(r"^(\d{1,2})\s+(.+?)\s+[—–-]\s+")
PROMPT_RE_NUMBERED_TITLE = re.compile(r"^(\d{1,2})\.\s+(.+?)\s*$")


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def expected_batches(book_number):
    first = book_number * 2 - 1
    return f"B{first:03d}", f"B{first + 1:03d}"


def load_batch_manifest(errors):
    if not BATCH_MANIFEST.exists():
        errors.append("Missing production/artwork-batches/manifest.csv")
        return {}

    rows = read_csv(BATCH_MANIFEST)
    by_id = {}
    for row in rows:
        batch_id = (row.get("Batch ID") or "").strip()
        if not batch_id:
            errors.append("Artwork batch manifest contains a row without Batch ID")
            continue
        if batch_id in by_id:
            errors.append(f"Duplicate artwork batch id: {batch_id}")
        by_id[batch_id] = row

    expected_ids = {f"B{i:03d}" for i in range(1, 61)}
    found_ids = set(by_id)
    missing = sorted(expected_ids - found_ids)
    extra = sorted(found_ids - expected_ids)
    if missing:
        errors.append(f"Artwork batch manifest missing: {', '.join(missing)}")
    if extra:
        errors.append(f"Artwork batch manifest has unexpected ids: {', '.join(extra)}")
    return by_id


def parse_prompt_subjects(path):
    subjects = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        stripped = line.strip()
        match = PROMPT_RE_PREFIX_DASH.match(stripped)
        if match:
            subjects.append((int(match.group(1)), match.group(2).strip()))
            continue
        match = PROMPT_RE_MIDDLE_DASH.match(stripped)
        if match:
            subjects.append((int(match.group(1)), match.group(2).strip()))
            continue
        match = PROMPT_RE_NUMBERED_TITLE.match(stripped)
        if match:
            subjects.append((int(match.group(1)), match.group(2).strip()))
    return subjects


def check_book(book_number, cfg, batch_rows, errors):
    prefix = f"Book {book_number}"
    if cfg.get("total_pages") != 128 or cfg.get("coloring_pages") != 60:
        errors.append(f"{prefix}: expected 128 total pages / 60 coloring pages")

    if book_number == 1:
        return

    catalog_dir = ROOT / "catalog" / "books" / f"book_{book_number:02d}"
    production_dir = ROOT / "production" / f"book_{book_number:02d}"
    animals_path = catalog_dir / "animals.csv"
    page_map_path = catalog_dir / "page_map.csv"
    artwork_path = production_dir / "artwork_manifest.csv"
    assembly_path = production_dir / "interior_assembly_manifest.csv"

    for path in (animals_path, page_map_path, artwork_path, assembly_path):
        if not path.exists():
            errors.append(f"{prefix}: missing {path.relative_to(ROOT)}")
    if any(not p.exists() for p in (animals_path, page_map_path, artwork_path, assembly_path)):
        return

    animals = read_csv(animals_path)
    page_map = read_csv(page_map_path)
    artwork = read_csv(artwork_path)
    assembly = read_csv(assembly_path)

    if len(animals) != 60:
        errors.append(f"{prefix}: expected 60 animals, found {len(animals)}")
    if len(page_map) != 128:
        errors.append(f"{prefix}: expected 128 page-map rows, found {len(page_map)}")
    if len(artwork) != 60:
        errors.append(f"{prefix}: expected 60 artwork-manifest rows, found {len(artwork)}")
    if len(assembly) != 60:
        errors.append(f"{prefix}: expected 60 assembly-manifest rows, found {len(assembly)}")
    if not (len(animals) == len(artwork) == len(assembly) == 60):
        return

    expected_pages = list(range(9, 128, 2))
    pages = [int(r.get("interior_page") or 0) for r in animals]
    if pages != expected_pages:
        errors.append(f"{prefix}: coloring pages must be 9,11,...,127")

    expected_numbers = list(range(1, 61))
    numbers = [int(r.get("number") or 0) for r in animals]
    if numbers != expected_numbers:
        errors.append(f"{prefix}: animal numbers must be 1..60 in order")

    batch_a, batch_b = expected_batches(book_number)
    expected_batch_by_index = [batch_a] * 30 + [batch_b] * 30

    for idx, (animal, art, assembled) in enumerate(zip(animals, artwork, assembly), start=1):
        subject = (animal.get("animal") or "").strip()
        fact = (animal.get("fact") or "").strip()
        page = str(animal.get("interior_page") or "").strip()
        number = str(animal.get("number") or "").strip()
        expected_batch = expected_batch_by_index[idx - 1]

        if (art.get("number") or "").strip() != number:
            errors.append(f"{prefix} #{idx}: artwork number differs from catalog")
        if (assembled.get("number") or "").strip() != number:
            errors.append(f"{prefix} #{idx}: assembly number differs from catalog")
        if (art.get("interior_page") or "").strip() != page:
            errors.append(f"{prefix} #{idx}: artwork page differs from catalog")
        if (assembled.get("interior_page") or "").strip() != page:
            errors.append(f"{prefix} #{idx}: assembly page differs from catalog")
        if (art.get("subject") or "").strip() != subject:
            errors.append(f"{prefix} #{idx}: artwork subject differs from catalog ({subject!r})")
        if (assembled.get("subject") or "").strip() != subject:
            errors.append(f"{prefix} #{idx}: assembly subject differs from catalog ({subject!r})")
        if (assembled.get("fact") or "").strip() != fact:
            errors.append(f"{prefix} #{idx}: assembly fact differs from catalog")
        if (art.get("batch") or "").strip() != expected_batch:
            errors.append(f"{prefix} #{idx}: artwork batch should be {expected_batch}")
        if (assembled.get("batch") or "").strip() != expected_batch:
            errors.append(f"{prefix} #{idx}: assembly batch should be {expected_batch}")

        art_filename = (art.get("expected_filename") or "").strip()
        assembly_filename = (assembled.get("expected_filename") or "").strip()
        if art_filename != assembly_filename:
            errors.append(f"{prefix} #{idx}: expected filename differs between manifests")
        if not art_filename.startswith(f"{idx:02d}_") or not art_filename.endswith(".png"):
            errors.append(f"{prefix} #{idx}: malformed expected filename {art_filename!r}")

    page_lookup = {}
    for row in page_map:
        try:
            page_lookup[int(row.get("page") or 0)] = (row.get("content") or "").strip()
        except ValueError:
            errors.append(f"{prefix}: non-numeric page in page_map.csv")
    for idx, animal in enumerate(animals):
        page = expected_pages[idx]
        subject = (animal.get("animal") or "").strip()
        if page_lookup.get(page) != subject:
            errors.append(f"{prefix}: page map page {page} should be {subject!r}")
        reverse = page + 1
        if page_lookup.get(reverse) != "Blank reverse":
            errors.append(f"{prefix}: page map page {reverse} should be 'Blank reverse'")

    for part, batch_id, subjects in (
        (1, batch_a, [r["animal"].strip() for r in animals[:30]]),
        (2, batch_b, [r["animal"].strip() for r in animals[30:]]),
    ):
        batch = batch_rows.get(batch_id)
        if not batch:
            errors.append(f"{prefix}: missing batch metadata for {batch_id}")
            continue
        if (batch.get("Book #") or "").strip() != str(book_number):
            errors.append(f"{prefix}: {batch_id} has wrong Book #")
        if (batch.get("Part") or "").strip() != str(part):
            errors.append(f"{prefix}: {batch_id} has wrong Part")
        if (batch.get("Illustrations") or "").strip() != "30":
            errors.append(f"{prefix}: {batch_id} must contain 30 illustrations")

        expected_range = f"{subjects[0]} -> {subjects[-1]}"
        if (batch.get("Animal Range") or "").strip() != expected_range:
            errors.append(
                f"{prefix}: {batch_id} Animal Range should be {expected_range!r}"
            )

        prompt_name = (batch.get("Prompt Pack") or "").strip()
        prompt_path = PROMPT_DIR / prompt_name
        if not prompt_name or not prompt_path.exists():
            errors.append(f"{prefix}: missing prompt pack for {batch_id}: {prompt_name!r}")
            continue
        prompt_subjects = parse_prompt_subjects(prompt_path)
        expected_prompt_numbers = list(range(1, 31)) if part == 1 else list(range(31, 61))
        found_numbers = [n for n, _ in prompt_subjects]
        found_subjects = [s for _, s in prompt_subjects]
        if found_numbers != expected_prompt_numbers:
            errors.append(f"{prefix}: {batch_id} prompt numbering is not the expected 30-item range")
        if found_subjects != subjects:
            errors.append(f"{prefix}: {batch_id} prompt subjects differ from animals.csv")


def main():
    errors = []
    configs = sorted(CONFIGS.glob("book_*.json"))
    if len(configs) != 30:
        errors.append(f"Expected 30 configs, found {len(configs)}")

    batch_rows = load_batch_manifest(errors)
    seen_books = set()
    for path in configs:
        cfg = json.loads(path.read_text(encoding="utf-8"))
        book_number = int(cfg["book_number"])
        seen_books.add(book_number)
        check_book(book_number, cfg, batch_rows, errors)

    if seen_books != set(range(1, 31)):
        errors.append("Build configs must cover book numbers 1..30 exactly once")

    print(f"Configs checked: {len(configs)}")
    print("Cross-check scope: catalogs, page maps, production manifests, batch manifest, prompt packs")
    if errors:
        for error in errors:
            print("ERROR:", error)
        raise SystemExit(1)
    print("PASS: 30-book catalog and production mappings are synchronized.")


if __name__ == "__main__":
    main()
