#!/usr/bin/env python3
"""Build every MIST° book whose 60 approved artwork files pass preflight."""
import argparse, json, subprocess, sys
from pathlib import Path


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',default='.')
    ap.add_argument('--edition',choices=['paperback','hardcover','both'],default='both')
    args=ap.parse_args()
    root=Path(args.root).resolve()
    configs=sorted((root/'build'/'configs').glob('book_*.json'))
    validator=root/'build'/'tools'/'validate_artwork.py'
    builder=root/'build'/'tools'/'build_interior.py'
    built=skipped=0
    for cfg_path in configs:
        cfg=json.loads(cfg_path.read_text(encoding='utf-8'))
        n=cfg['book_number']
        art_dir=root/cfg['artwork_root']
        v=subprocess.run([sys.executable,str(validator),'--art-dir',str(art_dir),'--expected',str(cfg.get('coloring_pages',60))])
        if v.returncode!=0:
            print(f'SKIP Book {n:02d}: artwork not ready')
            skipped+=1
            continue
        editions=['paperback','hardcover'] if args.edition=='both' else [args.edition]
        for edition in editions:
            out=root/cfg['output_root']/f'{edition}_interior.pdf'
            out.parent.mkdir(parents=True,exist_ok=True)
            subprocess.check_call([
                sys.executable,str(builder),str(cfg_path),'--edition',edition,
                '--art-dir',str(art_dir),'--output',str(out)
            ],cwd=root)
        built+=1
    print(f'Ready books built: {built}; skipped: {skipped}')

if __name__=='__main__':
    main()
