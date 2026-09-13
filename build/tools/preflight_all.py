#!/usr/bin/env python3
"""Structural preflight for the 30-book MIST° catalog."""
import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIGS = ROOT / "build" / "configs"


def main():
    errors=[]
    configs=sorted(CONFIGS.glob("book_*.json"))
    if len(configs)!=30:
        errors.append(f"Expected 30 configs, found {len(configs)}")
    for p in configs:
        cfg=json.loads(p.read_text(encoding="utf-8"))
        n=cfg["book_number"]
        if cfg.get("total_pages")!=128 or cfg.get("coloring_pages")!=60:
            errors.append(f"Book {n}: expected 128 total pages / 60 coloring pages")
        if n==1:
            continue
        src=ROOT / "catalog" / "books" / f"book_{n:02d}" / "animals.csv"
        if not src.exists():
            errors.append(f"Book {n}: missing {src.relative_to(ROOT)}")
            continue
        with src.open(encoding="utf-8-sig") as f:
            rows=list(csv.DictReader(f))
        if len(rows)!=60:
            errors.append(f"Book {n}: expected 60 animals, found {len(rows)}")
        pages=[int(r.get("interior_page") or 0) for r in rows]
        if pages!=list(range(9,128,2)):
            errors.append(f"Book {n}: coloring pages must be 9,11,...,127")
    print(f"Configs checked: {len(configs)}")
    if errors:
        for e in errors:
            print("ERROR:",e)
        raise SystemExit(1)
    print("PASS: 30-book catalog structure is consistent.")

if __name__=="__main__":
    main()
