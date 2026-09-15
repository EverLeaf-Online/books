#!/usr/bin/env python3
"""Export machine-readable artwork generation jobs from canonical MIST° prompt packs.

The exporter does not generate images. It combines batch-level art direction,
per-subject scene prompts, artwork manifests, and the batch manifest into a CSV that can
feed an image-generation/QA workflow without duplicating production metadata by hand.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BATCH_MANIFEST = ROOT / "production" / "artwork-batches" / "manifest.csv"
PROMPT_DIR = ROOT / "production" / "artwork-batches" / "prompts"

# Prompt packs currently use four normalized layouts:
#   01 — Subject: scene
#   01 Subject — scene
#   01. Subject — scene
#   01. Subject\nScene on the next nonblank line
SUBJECT_RE_PREFIX_DASH = re.compile(
    r"^\s*(\d{1,2})\s*[—–-]\s*([^:]+):\s*(.+?)\s*$"
)
SUBJECT_RE_MIDDLE_DASH = re.compile(
    r"^\s*(\d{1,2})\s+(.+?)\s+[—–-]\s+(.+?)\s*$"
)
SUBJECT_RE_DOT_MIDDLE_DASH = re.compile(
    r"^\s*(\d{1,2})\.\s+(.+?)\s+[—–-]\s+(.+?)\s*$"
)
SUBJECT_RE_NUMBERED_TITLE = re.compile(r"^\s*(\d{1,2})\.\s+(.+?)\s*$")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def is_direction_heading(line: str) -> bool:
    normalized = line.strip().upper()
    return normalized == "GLOBAL ART DIRECTION" or normalized.startswith("SHARED ART DIRECTION")


def parse_prompt_pack(path: Path) -> tuple[str, dict[int, tuple[str, str]]]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()

    try:
        direction_index = next(i for i, line in enumerate(lines) if is_direction_heading(line))
    except StopIteration as exc:
        raise ValueError(
            f"{path}: missing GLOBAL ART DIRECTION or SHARED ART DIRECTION heading"
        ) from exc

    direction_lines: list[str] = []
    subjects: dict[int, tuple[str, str]] = {}
    seen_subject = False
    pending_number: int | None = None
    pending_subject: str | None = None

    for raw in lines[direction_index + 1 :]:
        line = raw.strip()
        if not line:
            continue

        prefix = SUBJECT_RE_PREFIX_DASH.match(line)
        dot_middle = SUBJECT_RE_DOT_MIDDLE_DASH.match(line)
        middle = SUBJECT_RE_MIDDLE_DASH.match(line)
        numbered = SUBJECT_RE_NUMBERED_TITLE.match(line)

        if pending_number is not None:
            if prefix or dot_middle or middle or numbered:
                raise ValueError(
                    f"{path}: item {pending_number} is missing its scene prompt before {line!r}"
                )
            subjects[pending_number] = (pending_subject or "", line)
            pending_number = None
            pending_subject = None
            seen_subject = True
            continue

        if prefix:
            number = int(prefix.group(1))
            subject = prefix.group(2).strip()
            scene = prefix.group(3).strip()
            if number in subjects:
                raise ValueError(f"{path}: duplicate subject number {number}")
            subjects[number] = (subject, scene)
            seen_subject = True
            continue

        if dot_middle:
            number = int(dot_middle.group(1))
            subject = dot_middle.group(2).strip()
            scene = dot_middle.group(3).strip()
            if number in subjects:
                raise ValueError(f"{path}: duplicate subject number {number}")
            subjects[number] = (subject, scene)
            seen_subject = True
            continue

        if middle:
            number = int(middle.group(1))
            subject = middle.group(2).strip()
            scene = middle.group(3).strip()
            if number in subjects:
                raise ValueError(f"{path}: duplicate subject number {number}")
            subjects[number] = (subject, scene)
            seen_subject = True
            continue

        if numbered:
            number = int(numbered.group(1))
            if number in subjects:
                raise ValueError(f"{path}: duplicate subject number {number}")
            pending_number = number
            pending_subject = numbered.group(2).strip()
            seen_subject = True
            continue

        if not seen_subject:
            cleaned = line.removeprefix("- ").strip()
            if cleaned.upper() != "PROMPTS:":
                direction_lines.append(cleaned)
        else:
            raise ValueError(f"{path}: unexpected text after subject prompts: {line!r}")

    if pending_number is not None:
        raise ValueError(f"{path}: item {pending_number} is missing its scene prompt")
    if not direction_lines:
        raise ValueError(f"{path}: art direction is empty")
    if not subjects:
        raise ValueError(f"{path}: no numbered subject prompts found")

    return " ".join(direction_lines), subjects


def export_book(book_number: int, output: Path | None) -> int:
    if book_number < 2 or book_number > 30:
        raise ValueError("Book number must be between 2 and 30; Book 1 is frozen during KDP review.")

    manifest_path = ROOT / "production" / f"book_{book_number:02d}" / "artwork_manifest.csv"
    if not manifest_path.exists():
        raise FileNotFoundError(manifest_path)

    artwork_rows = read_csv(manifest_path)
    if len(artwork_rows) != 60:
        raise ValueError(f"Book {book_number}: expected 60 artwork rows, found {len(artwork_rows)}")

    batch_rows = [r for r in read_csv(BATCH_MANIFEST) if int(r["Book #"]) == book_number]
    if len(batch_rows) != 2:
        raise ValueError(f"Book {book_number}: expected exactly 2 batch rows, found {len(batch_rows)}")

    batch_info = {r["Batch ID"]: r for r in batch_rows}
    parsed_packs: dict[str, tuple[str, dict[int, tuple[str, str]]]] = {}

    jobs: list[dict[str, str]] = []
    for row in artwork_rows:
        number = int(row["number"])
        batch = row["batch"]
        if batch not in batch_info:
            raise ValueError(f"Book {book_number} item {number}: unknown batch {batch}")

        info = batch_info[batch]
        pack_name = info["Prompt Pack"]
        pack_path = PROMPT_DIR / pack_name
        if not pack_path.exists():
            raise FileNotFoundError(pack_path)

        if batch not in parsed_packs:
            parsed_packs[batch] = parse_prompt_pack(pack_path)
        global_direction, subject_prompts = parsed_packs[batch]

        if number not in subject_prompts:
            raise ValueError(f"{pack_name}: missing prompt for item {number}")
        prompt_subject, scene = subject_prompts[number]
        manifest_subject = row["subject"].strip()
        if prompt_subject != manifest_subject:
            raise ValueError(
                f"Book {book_number} item {number}: manifest subject {manifest_subject!r} "
                f"does not match prompt subject {prompt_subject!r}"
            )

        filename = row["expected_filename"].strip()
        output_folder = info["Output Folder"].rstrip("/")
        jobs.append(
            {
                "book_number": str(book_number),
                "batch": batch,
                "number": str(number),
                "interior_page": row["interior_page"],
                "subject": manifest_subject,
                "expected_filename": filename,
                "output_path": f"{output_folder}/{filename}",
                "prompt_pack": pack_name,
                "full_prompt": f"{global_direction} SUBJECT SCENE: {scene}",
                "status": row["status"],
                "qa_status": row["qa_status"],
            }
        )

    if len(jobs) != 60:
        raise ValueError(f"Book {book_number}: expected 60 exported jobs, found {len(jobs)}")

    expected_numbers = list(range(1, 61))
    actual_numbers = [int(job["number"]) for job in jobs]
    if actual_numbers != expected_numbers:
        raise ValueError(f"Book {book_number}: job numbers must be 1..60 in order")

    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        fields = [
            "book_number",
            "batch",
            "number",
            "interior_page",
            "subject",
            "expected_filename",
            "output_path",
            "prompt_pack",
            "full_prompt",
            "status",
            "qa_status",
        ]
        with output.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(jobs)
        print(
            f"Wrote {len(jobs)} artwork jobs to "
            f"{output.relative_to(ROOT) if output.is_relative_to(ROOT) else output}"
        )
    else:
        print(f"PASS: Book {book_number} exports cleanly to 60 artwork generation jobs.")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--book", type=int, required=True, help="Book number, 2-30")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional CSV output path. Omit to validate the generation-job export only.",
    )
    args = parser.parse_args()

    output = args.output
    if output is not None and not output.is_absolute():
        output = ROOT / output
    return export_book(args.book, output)


if __name__ == "__main__":
    raise SystemExit(main())
