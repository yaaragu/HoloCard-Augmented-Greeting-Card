#!/usr/bin/env python3
"""Modern back rosters matching concepts A (Sunrise line-art) and C (Editorial
type-only), in light + dark colorways, plus front+back layout sheets."""
import math, cairosvg
from PIL import Image, ImageDraw, ImageFont

W, H = 800, 900
SANS = "Arial,'Liberation Sans','DejaVu Sans',sans-serif"
NAMES = ["Jon", "Talia", "Abby", "David", "Benny", "Yaara", "Eli", "Wendy"]

LIGHT = dict(ink="#12496e", mid="#2f7fae", gold="#f2b134", sea="#1c6ea4",
             sub="#8aa0ad", hair="#c4d3dd", preview="#f4f7f9")
DARK  = dict(ink="#ffffff", mid="#f6c445", gold="#f6c445", sea="#7fc4ec",
             sub="#93a7b4", hair="#33475a", preview="#152230")
BLUEW = dict(ink="#0072ce", mid="#0072ce", gold="#0072ce", sea="#7fbde9",
             sub="#9cc7ea", hair="#cfe6f7", preview="#ffffff")   # Aegean Azure on white
WHITEB = dict(ink="#ffffff", mid="#dcecff", gold="#ffffff", sea="#bfe0ff",
              sub="#cfe4fb", hair="#3f93d6", preview="#0072ce")   # white on Aegean Azure

def rays(cx, cy, r0, r1, pal, n=9, a0=-160, a1=-20, w=2.5):
    s = ""
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * i / (n - 1))
        s += (f'<line x1="{cx+r0*math.cos(a):.1f}" y1="{cy+r0*math.sin(a):.1f}" '
              f'x2="{cx+r1*math.cos(a):.1f}" y2="{cy+r1*math.sin(a):.1f}" '
              f'stroke="{pal["gold"]}" stroke-width="{w}" stroke-linecap="round"/>')
    return s

def sunrise_mini(cx, cy, pal):
    r = 34
    return (rays(cx, cy, r+8, r+30, pal) +
            f'<path d="M {cx-r} {cy} a {r} {r} 0 0 1 {2*r} 0" fill="none" stroke="{pal["ink"]}" stroke-width="3"/>'
            f'<line x1="{cx-150}" y1="{cy}" x2="{cx+150}" y2="{cy}" stroke="{pal["ink"]}" stroke-width="3" stroke-linecap="round"/>')

# ---------- Back for concept A (Sunrise line-art) ----------
def back_A(pal):
    rows = ""
    y0, dy = 356, 56
    for i, n in enumerate(NAMES):
        rows += (f'<text x="{W/2}" y="{y0+i*dy}" text-anchor="middle" font-family="{SANS}" '
                 f'font-size="42" font-weight="600" letter-spacing="3" fill="{pal["ink"]}">{n.upper()}</text>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <text x="{W/2}" y="150" text-anchor="middle" font-family="{SANS}" font-size="58" font-weight="800" letter-spacing="2" fill="{pal['ink']}">THE&#160;WEIDBERGS</text>
  <text x="{W/2}" y="192" text-anchor="middle" font-family="{SANS}" font-size="22" font-weight="600" letter-spacing="12" fill="{pal['mid']}">GREECE&#160;&#183;&#160;JULY&#160;2026</text>
  {sunrise_mini(W/2, 268, pal)}
  {rows}
  <text x="{W/2}" y="812" text-anchor="middle" font-family="{SANS}" font-size="18" font-weight="500" letter-spacing="6" fill="{pal['sub']}">SANTORINI&#160;&#183;&#160;MYKONOS&#160;&#183;&#160;ATHENS</text>
</svg>"""

# ---------- Back for concept C (Editorial type-only) ----------
def back_C(pal):
    top = 214
    dy = 62
    body = f'<line x1="150" y1="{top}" x2="650" y2="{top}" stroke="{pal["ink"]}" stroke-width="3"/>'
    for i, n in enumerate(NAMES):
        by = top + 44 + i*dy
        body += (f'<text x="{W/2}" y="{by}" text-anchor="middle" font-family="{SANS}" '
                 f'font-size="34" font-weight="700" letter-spacing="7" fill="{pal["ink"]}">{n.upper()}</text>')
        body += f'<line x1="150" y1="{by+20}" x2="650" y2="{by+20}" stroke="{pal["hair"]}" stroke-width="1.5"/>'
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <text x="{W/2}" y="150" text-anchor="middle" font-family="{SANS}" font-size="26" font-weight="600" letter-spacing="14" fill="{pal['mid']}">THE&#160;WEIDBERG&#160;FAMILY</text>
  {body}
  <text x="{W/2}" y="{top + 44 + 8*dy + 20}" text-anchor="middle" font-family="{SANS}" font-size="24" font-weight="700" letter-spacing="10" fill="{pal['mid']}">GREECE&#160;&#183;&#160;JULY&#160;2026</text>
</svg>"""

def render(svg, base, pal):
    with open(base + ".svg", "w") as f:
        f.write(svg)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=base + ".png",
                     output_width=W, output_height=H, background_color=pal["preview"])

BACKS = {"A_SunriseLine": back_A, "C_TypeOnly": back_C}
for name, fn in BACKS.items():
    for tag, pal in (("Light", LIGHT), ("Dark", DARK), ("BlueOnWhite", BLUEW), ("WhiteOnBlue", WHITEB)):
        base = f"ModernBack_{name}_{tag}"
        render(fn(pal), base, pal)
        print("wrote", base)

# ---------- front + back layout sheets ----------
def font(size):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", size)
    except Exception:
        return ImageFont.load_default()

for concept, front_stub in (("A_SunriseLine", "Modern_A_SunriseLine"),
                            ("C_TypeOnly", "Modern_C_TypeOnly")):
    for tag, pal, fg in (("Light", LIGHT, "#12496e"), ("Dark", DARK, "#f6c445"),
                         ("BlueOnWhite", BLUEW, "#0d5eaf"), ("WhiteOnBlue", WHITEB, "#ffffff")):
        front = Image.open(f"{front_stub}_{tag}.png").convert("RGB")
        back = Image.open(f"ModernBack_{concept}_{tag}.png").convert("RGB")
        pad, gap, top = 40, 60, 70
        sheet = Image.new("RGB", (pad*2 + W*2 + gap, top + H + pad), pal["preview"])
        sheet.paste(front, (pad, top))
        sheet.paste(back, (pad + W + gap, top))
        d = ImageDraw.Draw(sheet)
        f = font(34)
        d.text((pad + W//2, 30), "FRONT", fill=fg, font=f, anchor="mm")
        d.text((pad + W + gap + W//2, 30), "BACK", fill=fg, font=f, anchor="mm")
        out = f"ModernLayout_{concept}_{tag}.png"
        sheet.save(out)
        print("layout:", out)

# ---------- transparent (no background) PNG exports ----------
transparent = []
for concept, front_stub in (("A_SunriseLine", "Modern_A_SunriseLine"),
                            ("C_TypeOnly", "Modern_C_TypeOnly")):
    for tag in ("Light", "Dark", "BlueOnWhite", "WhiteOnBlue"):
        for role, src in (("Front", f"{front_stub}_{tag}.svg"),
                          ("Back", f"ModernBack_{concept}_{tag}.svg")):
            out = f"Transparent_{concept}_{role}_{tag}.png"
            cairosvg.svg2png(url=src, write_to=out, output_width=W, output_height=H)
            transparent.append(out)
print("transparent:", len(transparent), "files (no background)")
