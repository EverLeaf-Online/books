#!/usr/bin/env python3
"""Build a 128-page MIST° KDP interior after all 60 approved art files exist."""
import argparse, csv, json, re
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image

REG_FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD_FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('MISTSans', REG_FONT))
pdfmetrics.registerFont(TTFont('MISTSans-Bold', BOLD_FONT))

def wrap_text(text, font, size, max_width, c):
    words=text.split(); lines=[]; cur=''
    for word in words:
        trial=word if not cur else cur+' '+word
        if c.stringWidth(trial,font,size)<=max_width: cur=trial
        else:
            if cur: lines.append(cur)
            cur=word
    if cur: lines.append(cur)
    return lines

def load_animals(root,cfg):
    path=root/cfg['animal_csv']; rows=[]
    with path.open(encoding='utf-8-sig') as f:
        for idx,r in enumerate(csv.DictReader(f),1):
            animal=r.get('animal') or r.get('Animal') or r.get('name') or r.get('animal_name')
            fact=r.get('fact') or r.get('final_fact') or r.get('Fun Fact') or ''
            page=r.get('interior_page') or r.get('Interior Page') or (9+(idx-1)*2)
            number=r.get('number') or r.get('index') or idx
            if animal: rows.append({'number':int(number),'animal':animal.strip(),'fact':fact.strip(),'page':int(page)})
    if len(rows)!=60: raise SystemExit(f'Expected 60 animal rows, found {len(rows)} in {path}')
    return rows

def scan_art(art_dir):
    root=Path(art_dir); found={}
    if not root.exists(): return found
    files=[]
    for ext in ('*.png','*.jpg','*.jpeg','*.webp'): files.extend(root.rglob(ext))
    for p in files:
        m=re.search(r'(?:^|_)(0?[1-9]|[1-5][0-9]|60)(?:_|\.|-)',p.name) or re.match(r'^(0?[1-9]|[1-5][0-9]|60)\D',p.name)
        if m: found.setdefault(int(m.group(1)),p)
    return found

def front(c,page,cfg,animals,W,H):
    safe=.55*inch
    if page==1:
        y=H-2*inch; c.setFont('MISTSans-Bold',24)
        for line in wrap_text(cfg['title'],'MISTSans-Bold',24,W-1.3*inch,c): c.drawCentredString(W/2,y,line); y-=.36*inch
        c.setFont('MISTSans',15)
        for line in wrap_text(cfg['subtitle'],'MISTSans',15,W-1.5*inch,c): c.drawCentredString(W/2,y,line); y-=.28*inch
        c.setFont('MISTSans-Bold',14); c.drawCentredString(W/2,2*inch,cfg.get('author','Paul Thach')); c.drawCentredString(W/2,1.55*inch,cfg.get('imprint','MIST°'))
    elif page==2:
        c.setFont('MISTSans-Bold',16); c.drawString(safe,H-inch,'Copyright'); c.setFont('MISTSans',10.5)
        text=f"© 2026 {cfg.get('author','Paul Thach')}. Published under the {cfg.get('imprint','MIST°')} imprint. All rights reserved."
        y=H-1.45*inch
        for line in wrap_text(text,'MISTSans',10.5,W-2*safe,c): c.drawString(safe,y,line); y-=15
        c.drawString(safe,y-15,'Printed via Amazon KDP.')
    elif page==3:
        c.setFont('MISTSans-Bold',22); c.drawCentredString(W/2,H-2*inch,'THIS BOOK BELONGS TO'); c.line(1.2*inch,H-4.1*inch,W-1.2*inch,H-4.1*inch)
    elif page==4:
        c.setFont('MISTSans-Bold',23); c.drawCentredString(W/2,H-1.55*inch,'WELCOME!')
    elif page==5:
        c.setFont('MISTSans-Bold',22); c.drawCentredString(W/2,H-1.35*inch,'COLORING TIPS')
        c.setFont('MISTSans',13); y=H-2.2*inch
        for tip in ['Crayons, colored pencils, and markers all work great.','If you use markers, place a spare sheet behind the page.','There is no wrong way to color an animal.','Take your time and have fun.']:
            c.drawString(inch,y,'• '+tip); y-=.55*inch
    elif page==6:
        c.setFont('MISTSans-Bold',22); c.drawCentredString(W/2,H-1.2*inch,'COLOR TEST PAGE')
        for y in (7.4,5.45):
            for x in (1.55,3.15,4.75,6.35): c.circle(x*inch*(W/(8.5*inch)),y*inch,.46*inch,stroke=1,fill=0)
    elif page==7:
        c.setFont('MISTSans-Bold',17); c.drawCentredString(W/2,H-.8*inch,'ANIMAL ADVENTURE CHECKLIST'); c.setFont('MISTSans',8.2)
        cols=[.52*inch,W/2+.12*inch]; y0=H-1.25*inch
        for i,a in enumerate(animals):
            col=0 if i<30 else 1; rr=i if i<30 else i-30; y=y0-rr*.295*inch; x=cols[col]
            c.rect(x,y-.075*inch,.12*inch,.12*inch,stroke=1,fill=0); label=f"{a['number']:02d}. {a['animal']}"; c.drawString(x+.18*inch,y-.012*inch,label[:35])

def coloring(c,row,art_path,W,H):
    safe=.50*inch; cap=.82*inch; art_x=safe; art_y=safe+cap+.18*inch; art_w=W-2*safe; art_h=H-art_y-safe
    if art_path:
        with Image.open(art_path) as im: iw,ih=im.size
        scale=min(art_w/iw,art_h/ih); dw,dh=iw*scale,ih*scale; dx=art_x+(art_w-dw)/2; dy=art_y+(art_h-dh)/2
        c.drawImage(ImageReader(str(art_path)),dx,dy,dw,dh,preserveAspectRatio=True,mask='auto')
    else:
        c.rect(art_x,art_y,art_w,art_h,stroke=1,fill=0); c.setFont('MISTSans-Bold',18); c.drawCentredString(W/2,art_y+art_h/2,f"ARTWORK SLOT - {row['animal']}")
    c.setFont('MISTSans-Bold',15); c.drawCentredString(W/2,.55*inch+cap-.10*inch,row['animal'])
    c.setFont('MISTSans',9.8); y=.83*inch
    for line in wrap_text(row['fact'],'MISTSans',9.8,W-1.2*inch,c)[:3]: c.drawCentredString(W/2,y,line); y-=.14*inch

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('config'); ap.add_argument('--edition',choices=['paperback','hardcover'],required=True); ap.add_argument('--art-dir',required=True); ap.add_argument('--output',required=True); ap.add_argument('--allow-placeholders',action='store_true'); args=ap.parse_args()
    cfg_path=Path(args.config).resolve(); root=cfg_path.parents[2] if cfg_path.parent.name=='configs' else Path.cwd(); cfg=json.loads(cfg_path.read_text(encoding='utf-8'))
    animals=load_animals(root,cfg); art=scan_art(args.art_dir); missing=[a['number'] for a in animals if a['number'] not in art]
    if missing and not args.allow_placeholders: raise SystemExit(f'Missing {len(missing)} artwork files: {missing}')
    fmt=cfg[args.edition]; W,H=fmt['trim_width_in']*inch,fmt['trim_height_in']*inch; out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(out),pagesize=(W,H),pageCompression=1); c.setTitle(cfg['title']); c.setAuthor(cfg.get('author','Paul Thach')); by_page={a['page']:a for a in animals}
    for page in range(1,129):
        if page<=8: front(c,page,cfg,animals,W,H)
        elif page in by_page: coloring(c,by_page[page],art.get(by_page[page]['number']),W,H)
        c.showPage()
    c.save(); print(f'Built {out} ({args.edition}, 128 pages).')

if __name__=='__main__': main()
