#!/usr/bin/env python3
"""Export every design to print-ready files: a scalable vector PDF and a
transparent 300 DPI PNG at a real print size. Outputs to ShirtDesign/print/."""
import os, re, glob, cairosvg

OUT = "print"
os.makedirs(OUT, exist_ok=True)
DPI = 300

# physical print width (inches) by design canvas width
WIDTH_IN = {800: 12.0, 1000: 11.0}

# design SVGs to export (skip helper/temp svgs)
svgs = sorted(
    f for f in glob.glob("*.svg")
    if not f.startswith(("preview_", "contact_sheet"))
)

def canvas_wh(text):
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', text) or re.search(r'width="(\d+)" height="(\d+)"', text)
    return (int(m.group(1)), int(m.group(2))) if m else (800, 900)

done = []
for svg in svgs:
    with open(svg) as f:
        data = f.read()
    w, h = canvas_wh(data)
    win = WIDTH_IN.get(w, 12.0)
    px = int(round(win * DPI))
    scale = px / w
    stem = os.path.splitext(svg)[0]
    pdf = os.path.join(OUT, stem + ".pdf")
    png = os.path.join(OUT, f"{stem}_{DPI}dpi.png")
    cairosvg.svg2pdf(bytestring=data.encode(), write_to=pdf)
    cairosvg.svg2png(bytestring=data.encode(), write_to=png,
                     output_width=px, output_height=int(round(h * scale)))
    done.append((stem, f'{win:.0f}x{win*h/w:.1f} in', f'{px}x{int(round(h*scale))} px'))

w0 = max(len(d[0]) for d in done)
for stem, size_in, size_px in done:
    print(f"{stem:<{w0}}  {size_in:>12}  {size_px:>12}  (pdf + png)")
print(f"\n{len(done)} designs -> {OUT}/  (transparent PNG @ {DPI} DPI + vector PDF)")
