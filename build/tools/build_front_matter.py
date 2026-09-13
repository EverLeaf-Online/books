#!/usr/bin/env python3
"""Generate embedded-font 8-page front matter PDFs for all 30 MIST° books."""
import argparse, csv, json
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

REG_FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD_FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('MISTSans',REG_FONT))
pdfmetrics.registerFont(TTFont('MISTSans-Bold',BOLD_FONT))

def wrap(c,text,font,size,max_width):
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
    rows=[]; p=root/cfg['animal_csv']
    with p.open(encoding='utf-8-sig') as f:
        for idx,r in enumerate(csv.DictReader(f),1):
            animal=r.get('animal') or r.get('Animal')
            fact=r.get('fact') or r.get('final_fact') or ''
            if animal: rows.append((idx,animal.strip(),fact.strip()))
    if len(rows)!=60: raise SystemExit(f"Book {cfg['book_number']}: expected 60 rows, got {len(rows)}")
    return rows

def build(root,cfg,edition,out):
    fmt=cfg[edition]; W,H=fmt['trim_width_in']*inch,fmt['trim_height_in']*inch; animals=load_animals(root,cfg)
    c=canvas.Canvas(str(out),pagesize=(W,H),pageCompression=1); c.setTitle(cfg['title']+' - Front Matter'); c.setAuthor(cfg['author']); safe=.55*inch
    for page in range(1,9):
        if page==1:
            y=H-2*inch; c.setFont('MISTSans-Bold',24)
            for line in wrap(c,cfg['title'],'MISTSans-Bold',24,W-1.3*inch): c.drawCentredString(W/2,y,line); y-=.36*inch
            c.setFont('MISTSans',15)
            for line in wrap(c,cfg['subtitle'],'MISTSans',15,W-1.5*inch): c.drawCentredString(W/2,y,line); y-=.28*inch
            c.setFont('MISTSans-Bold',14); c.drawCentredString(W/2,2*inch,cfg['author']); c.setFont('MISTSans-Bold',13); c.drawCentredString(W/2,1.55*inch,cfg['imprint'])
        elif page==2:
            c.setFont('MISTSans-Bold',16); c.drawString(safe,H-inch,'Copyright'); c.setFont('MISTSans',10.5)
            text=f"© 2026 {cfg['author']}. Published under the {cfg['imprint']} imprint. All rights reserved."
            y=H-1.45*inch
            for line in wrap(c,text,'MISTSans',10.5,W-2*safe): c.drawString(safe,y,line); y-=15
            c.drawString(safe,y-15,'Printed via Amazon KDP.')
        elif page==3:
            c.setFont('MISTSans-Bold',22); c.drawCentredString(W/2,H-2*inch,'THIS BOOK BELONGS TO'); c.line(1.2*inch,H-4.1*inch,W-1.2*inch,H-4.1*inch)
        elif page==4:
            c.setFont('MISTSans-Bold',23); c.drawCentredString(W/2,H-1.55*inch,'WELCOME!'); c.setFont('MISTSans',13)
            text=f"Welcome to your {cfg['theme'].lower()} coloring adventure! Inside you'll find 60 bold and easy coloring pages, each with a short fun fact."
            y=H-2.35*inch
            for line in wrap(c,text,'MISTSans',13,W-1.8*inch): c.drawString(.9*inch,y,line); y-=20
        elif page==5:
            c.setFont('MISTSans-Bold',22); c.drawCentredString(W/2,H-1.35*inch,'COLORING TIPS'); c.setFont('MISTSans',13); y=H-2.2*inch
            for tip in ['Crayons, colored pencils, and markers all work great.','If you use markers, place a spare sheet behind the page.','There is no wrong way to color an animal.','Take your time and have fun.']:
                c.drawString(inch,y,'• '+tip); y-=.55*inch
        elif page==6:
            c.setFont('MISTSans-Bold',22); c.drawCentredString(W/2,H-1.2*inch,'COLOR TEST PAGE')
            for y in (7.4,5.45):
                for x in (1.55,3.15,4.75,6.35): c.circle(x*inch*(W/(8.5*inch)),y*inch,.46*inch,stroke=1,fill=0)
        elif page==7:
            c.setFont('MISTSans-Bold',17); c.drawCentredString(W/2,H-.8*inch,'ANIMAL ADVENTURE CHECKLIST'); c.setFont('MISTSans',8.2); cols=[.52*inch,W/2+.12*inch]; y0=H-1.25*inch
            for i,(num,animal,_) in enumerate(animals):
                col=0 if i<30 else 1; rr=i if i<30 else i-30; y=y0-rr*.295*inch; x=cols[col]
                c.rect(x,y-.075*inch,.12*inch,.12*inch,stroke=1,fill=0); c.drawString(x+.18*inch,y-.012*inch,f'{num:02d}. {animal}'[:35])
        c.showPage()
    c.save()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); args=ap.parse_args(); root=Path(args.root).resolve(); out=root/'generated'/'front-matter'; out.mkdir(parents=True,exist_ok=True); count=0
    for cfg_path in sorted((root/'build'/'configs').glob('book_*.json')):
        cfg=json.loads(cfg_path.read_text(encoding='utf-8'))
        for edition in ('paperback','hardcover'):
            build(root,cfg,edition,out/f"Book_{cfg['book_number']:02d}_{edition}_front_matter.pdf"); count+=1
    print(f'Generated {count} front-matter PDFs.')

if __name__=='__main__': main()
