#!/usr/bin/env python3
"""Basic source-art preflight for MIST° coloring pages."""
import argparse,re
from pathlib import Path
from PIL import Image

EXTS={'.png','.jpg','.jpeg','.webp'}

def number_from_name(name):
    m=re.search(r'(?:^|_)(0?[1-9]|[1-5][0-9]|60)(?:_|\.|-)',name)
    return int(m.group(1)) if m else None

def analyze(path):
    issues=[]
    try:
        im=Image.open(path).convert('RGB')
    except Exception as e:
        return [f'ERROR cannot open: {e}']
    w,h=im.size
    if w<2000 or h<2600:
        issues.append(f'ERROR low resolution {w}x{h}')
    elif w<2550 or h<3300:
        issues.append(f'WARN preferred production size is 2550x3300; got {w}x{h}')
    sample=im.resize((max(1,w//12),max(1,h//12)))
    px=list(sample.getdata())
    color_ratio=sum(1 for r,g,b in px if max(r,g,b)-min(r,g,b)>5)/max(1,len(px))
    if color_ratio>0.005:
        issues.append(f'WARN colored-pixel ratio {color_ratio:.2%}')
    mx=max(8,round(w*(0.50/8.5)))
    my=max(8,round(h*(0.50/11.0)))
    boxes=[(0,0,w,my),(0,h-my,w,h),(0,0,mx,h),(w-mx,0,w,h)]
    dark=total=0
    for box in boxes:
        crop=im.crop(box).convert('L').resize((max(1,(box[2]-box[0])//8),max(1,(box[3]-box[1])//8)))
        vals=list(crop.getdata())
        dark+=sum(1 for v in vals if v<220)
        total+=len(vals)
    ratio=dark/max(1,total)
    if ratio>0.003:
        issues.append(f'WARN ink inside approximate 0.50-inch safe border ({ratio:.2%})')
    return issues

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--art-dir',required=True)
    ap.add_argument('--expected',type=int,default=60)
    ap.add_argument('--strict',action='store_true')
    args=ap.parse_args()
    root=Path(args.art_dir)
    files=[p for p in root.rglob('*') if p.suffix.lower() in EXTS]
    numbered={}
    for p in files:
        n=number_from_name(p.name)
        if n is not None:
            numbered.setdefault(n,p)
    missing=[n for n in range(1,args.expected+1) if n not in numbered]
    print(f'Artwork directory: {root}')
    print(f'Images: {len(files)} | numbered: {len(numbered)} | expected: {args.expected}')
    if missing:
        print('MISSING:',missing)
    errors=warnings=0
    for n,p in sorted(numbered.items()):
        for issue in analyze(p):
            print(f'{n:02d} {p.name}: {issue}')
            errors+=issue.startswith('ERROR')
            warnings+=issue.startswith('WARN')
    print(f'Summary: {errors} errors, {warnings} warnings')
    if missing or errors or (args.strict and warnings):
        raise SystemExit(1)

if __name__=='__main__':
    main()
