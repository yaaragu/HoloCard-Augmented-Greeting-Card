#!/usr/bin/env python3
"""Modern, badge-free Greece front concepts (no circle, no olive sprigs).
Clean sans-serif, flat/line-art, lots of negative space. Design-only, transparent."""
import math, cairosvg

W, H = 800, 900
SANS = "Arial,'Liberation Sans','DejaVu Sans',sans-serif"

LIGHT = dict(ink="#12496e", mid="#2f7fae", gold="#f2b134", sea="#1c6ea4",
             sub="#8aa0ad", preview="#f4f7f9")
DARK  = dict(ink="#ffffff", mid="#f6c445", gold="#f6c445", sea="#7fc4ec",
             sub="#93a7b4", preview="#152230")
SAND  = dict(ink="#233b46", mid="#c8613b", gold="#e1a537", sea="#2f7d9e",
             sub="#9a8b76", preview="#f0e7d8")   # warm flat palette for the poster
# Greek flag blue & white theme
BLUEW = dict(ink="#0072ce", mid="#0072ce", gold="#0072ce", sea="#7fbde9",
             sub="#9cc7ea", preview="#ffffff")   # Aegean Azure ink on white shirt
WHITEB = dict(ink="#ffffff", mid="#dcecff", gold="#ffffff", sea="#bfe0ff",
              sub="#cfe4fb", preview="#0072ce")   # white ink on Aegean Azure shirt

def head(pal, y=140, size=26):
    return (f'<text x="{W/2}" y="{y}" text-anchor="middle" font-family="{SANS}" '
            f'font-size="{size}" font-weight="600" letter-spacing="13" fill="{pal["mid"]}">'
            f'WEIDBERG&#160;FAMILY</text>')

def rays(cx, cy, r0, r1, pal, n=9, a0=-160, a1=-20, w=3):
    s = ""
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * i / (n - 1))
        x0, y0 = cx + r0 * math.cos(a), cy + r0 * math.sin(a)
        x1, y1 = cx + r1 * math.cos(a), cy + r1 * math.sin(a)
        s += f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{pal["gold"]}" stroke-width="{w}" stroke-linecap="round"/>'
    return s

# ---------------- Concept A: Sunrise Line ----------------
def concept_A(pal):
    cx, cy = W/2, 452
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {head(pal, 150)}
  {rays(cx, cy, 78, 108, pal)}
  <path d="M {cx-64} {cy} a 64 64 0 0 1 128 0" fill="none" stroke="{pal['ink']}" stroke-width="4"/>
  <line x1="150" y1="{cy}" x2="650" y2="{cy}" stroke="{pal['ink']}" stroke-width="4" stroke-linecap="round"/>
  <path d="M 210 {cy+26} q 30 -14 60 0 t 60 0 t 60 0 t 60 0 t 60 0" fill="none" stroke="{pal['sea']}" stroke-width="3" stroke-linecap="round" opacity="0.85"/>
  <path d="M 250 {cy+48} q 30 -14 60 0 t 60 0 t 60 0 t 60 0" fill="none" stroke="{pal['sea']}" stroke-width="3" stroke-linecap="round" opacity="0.55"/>
  <text x="{cx}" y="648" text-anchor="middle" font-family="{SANS}" font-size="128" font-weight="800" letter-spacing="6" fill="{pal['ink']}">GREECE</text>
  <text x="{cx}" y="706" text-anchor="middle" font-family="{SANS}" font-size="28" font-weight="600" letter-spacing="18" fill="{pal['mid']}">JULY&#160;2026</text>
  <text x="{cx}" y="748" text-anchor="middle" font-family="{SANS}" font-size="18" font-weight="500" letter-spacing="6" fill="{pal['sub']}">SANTORINI&#160;&#183;&#160;MYKONOS&#160;&#183;&#160;ATHENS</text>
</svg>"""

# ---------------- Concept B: Flat Poster (silhouette) ----------------
def cube(x, w, h, y, fill):     # flat house cube sitting on baseline y
    return f'<rect x="{x}" y="{y-h}" width="{w}" height="{h}" fill="{fill}"/>'
def dome(cx, y, r, fill):
    return f'<path d="M {cx-r} {y} a {r} {r} 0 0 1 {2*r} 0 Z" fill="{fill}"/>'
def concept_B(pal):
    cx = W/2
    base = 468
    sea = pal['sea']
    town = f"""
      {cube(258, 60, 78, base, sea)}{dome(288, base-78, 30, sea)}
      {cube(322, 52, 120, base, sea)}
      {cube(380, 46, 64, base, sea)}{dome(403, base-64, 23, sea)}
      {cube(432, 58, 150, base, sea)}{dome(461, base-150, 29, sea)}
      {cube(496, 50, 92, base, sea)}
    """
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {head(pal, 150)}
  <circle cx="500" cy="320" r="92" fill="{pal['gold']}"/>
  {town}
  <rect x="150" y="{base}" width="500" height="5" fill="{pal['ink']}"/>
  <path d="M 168 {base+24} q 34 -14 68 0 t 68 0 t 68 0 t 68 0 t 68 0" fill="none" stroke="{sea}" stroke-width="4" stroke-linecap="round" opacity="0.7"/>
  <text x="{cx}" y="642" text-anchor="middle" font-family="{SANS}" font-size="122" font-weight="800" letter-spacing="5" fill="{pal['ink']}">GREECE</text>
  <text x="{cx}" y="702" text-anchor="middle" font-family="{SANS}" font-size="27" font-weight="600" letter-spacing="14" fill="{pal['mid']}">SUMMER&#160;&#8226;&#160;JULY&#160;2026</text>
</svg>"""

# ---------------- Concept C: Type-only (editorial) ----------------
def concept_C(pal):
    cx = W/2
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <text x="{cx}" y="210" text-anchor="middle" font-family="{SANS}" font-size="26" font-weight="600" letter-spacing="15" fill="{pal['mid']}">THE&#160;WEIDBERG&#160;FAMILY</text>
  <line x1="150" y1="430" x2="650" y2="430" stroke="{pal['ink']}" stroke-width="3"/>
  <text x="{cx}" y="486" text-anchor="middle" font-family="{SANS}" font-size="150" font-weight="800" letter-spacing="4" fill="none" stroke="{pal['ink']}" stroke-width="3">GREECE</text>
  <circle cx="{cx}" cy="430" r="9" fill="{pal['gold']}"/>
  <text x="{cx}" y="590" text-anchor="middle" font-family="{SANS}" font-size="21" font-weight="500" letter-spacing="8" fill="{pal['sub']}">SANTORINI&#160;&#183;&#160;MYKONOS&#160;&#183;&#160;ATHENS&#160;&#183;&#160;CORFU</text>
  <text x="{cx}" y="662" text-anchor="middle" font-family="{SANS}" font-size="44" font-weight="700" letter-spacing="12" fill="{pal['mid']}">JULY&#160;2026</text>
</svg>"""

JOBS = [
    ("Modern_A_SunriseLine", concept_A, [("Light", LIGHT), ("Dark", DARK), ("BlueOnWhite", BLUEW), ("WhiteOnBlue", WHITEB)]),
    ("Modern_B_FlatPoster",  concept_B, [("Light", LIGHT), ("Sand", SAND), ("Dark", DARK)]),
    ("Modern_C_TypeOnly",    concept_C, [("Light", LIGHT), ("Dark", DARK), ("BlueOnWhite", BLUEW), ("WhiteOnBlue", WHITEB)]),
]
for name, fn, pals in JOBS:
    for tag, pal in pals:
        base = f"{name}_{tag}"
        svg = fn(pal)
        with open(base + ".svg", "w") as f:
            f.write(svg)
        cairosvg.svg2png(bytestring=svg.encode(), write_to=base + ".png",
                         output_width=W, output_height=H, background_color=pal["preview"])
        print("wrote", base)
