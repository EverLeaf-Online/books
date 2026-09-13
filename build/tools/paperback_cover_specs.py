#!/usr/bin/env python3
"""Paperback cover size helper for MIST° B&W white-paper books. Hardcover must use the exact KDP calculator/template."""
import argparse

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pages',type=int,default=128)
    ap.add_argument('--trim-width',type=float,default=8.5)
    ap.add_argument('--trim-height',type=float,default=11.0)
    args=ap.parse_args()
    spine=args.pages*0.002252
    cover_w=0.125+args.trim_width+spine+args.trim_width+0.125
    cover_h=0.125+args.trim_height+0.125
    print(f'Pages: {args.pages}')
    print(f'Paperback spine: {spine:.6f} in')
    print(f'Paperback full cover: {cover_w:.6f} x {cover_h:.6f} in')
    print('Hardcover: use exact KDP hardcover calculator/template; do not derive from paperback.')

if __name__=='__main__':
    main()
