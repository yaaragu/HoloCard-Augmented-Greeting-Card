#!/usr/bin/env python3
"""Weidberg Greece designs: named back roster, dark colorway, new island-map image,
and front+back layout sheets. Design-only, transparent background, print-ready."""
import math, cairosvg
from PIL import Image, ImageDraw, ImageFont

W, H = 800, 900
CX, CY, R = 400, 420, 150
NAMES = ["Jon", "Talia", "Abby", "David", "Benny", "Yaara", "Eli", "Wendy"]

# ---- colorways (ink meant to print on a light vs a dark shirt) ----
LIGHT = dict(head="#12496e", mid="#2f7fae", gold="#f2b134", olive="#7cae4e",
             oliveDk="#5f8f3e", sub="#6b8697", ring="#0f4f76", name="#12496e",
             rule="#2f7fae", preview="#f3f6f9")
DARK  = dict(head="#ffffff", mid="#f6c445", gold="#f6c445", olive="#9ccc65",
             oliveDk="#6f9e3e", sub="#cdd8e0", ring="#f6c445", name="#ffffff",
             rule="#f6c445", preview="#152230")

DEFS = """
  <defs>
    <radialGradient id="sun" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ffe08a"/><stop offset="0.7" stop-color="#f6c445"/>
      <stop offset="1" stop-color="#f2b134"/></radialGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#4aa8d8"/><stop offset="1" stop-color="#1c6ea4"/></linearGradient>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#eaf6ff"/><stop offset="1" stop-color="#cfe8fb"/></linearGradient>
    <linearGradient id="stone" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e6dcc7"/></linearGradient>
  </defs>
"""

def backdrop(sun_x=72, sun_y=-78, sea_y=55):
    return f"""      <rect x="{-R}" y="{-R}" width="{2*R}" height="{R+sea_y}" fill="url(#sky)"/>
      <circle cx="{sun_x}" cy="{sun_y}" r="38" fill="url(#sun)"/>
      <rect x="{-R}" y="{sea_y}" width="{2*R}" height="{R-sea_y}" fill="url(#sea)"/>
      <path d="M {-R} {sea_y} q 30 12 60 0 t 60 0 t 60 0 t 60 0 t 60 0" fill="none" stroke="#ffffff" stroke-width="3" opacity="0.55"/>"""

SANTORINI = backdrop(72, -78) + """
      <g fill="#ffffff" stroke="#c9d6df" stroke-width="2">
        <rect x="-120" y="-20" width="70" height="78"/><rect x="-58" y="-45" width="60" height="103"/>
        <rect x="0" y="-10" width="55" height="68"/><rect x="48" y="-40" width="60" height="98"/></g>
      <path d="M -95 -20 a 20 20 0 0 1 40 0 Z" fill="#1c7fc0"/>
      <path d="M -28 -45 a 18 18 0 0 1 36 0 Z" fill="#1565a8"/>
      <path d="M 62 -40 a 22 22 0 0 1 44 0 Z" fill="#1c7fc0"/>
      <path d="M -75 -45 v 16 M -83 -37 h 16" stroke="#0f4f76" stroke-width="3"/>
      <path d="M 84 -66 v 16 M 76 -58 h 16" stroke="#0f4f76" stroke-width="3"/>"""

def columns(x0, yt, yb, n, w, gap):
    return "".join(f'<rect x="{x0+i*(w+gap)}" y="{yt}" width="{w}" height="{yb-yt}" fill="url(#stone)" stroke="#cbbf9e" stroke-width="1"/>' for i in range(n))
PARTHENON = backdrop(95, -88, 70) + f"""
      <rect x="-118" y="58" width="236" height="12" fill="#efe7d4" stroke="#cbbf9e"/>
      <rect x="-108" y="46" width="216" height="12" fill="#f5eede" stroke="#cbbf9e"/>
      {columns(-96, -18, 46, 7, 18, 12)}
      <rect x="-104" y="-30" width="208" height="14" fill="#f5eede" stroke="#cbbf9e"/>
      <path d="M -110 -30 L 0 -92 L 110 -30 Z" fill="url(#stone)" stroke="#cbbf9e" stroke-width="2"/>
      <path d="M -104 -32 L 0 -84 L 104 -32 Z" fill="#efe7d4"/>"""

def pin(x, y, c="#b23a3a"):
    return f'<g transform="translate({x},{y})"><path d="M0 0 C -11 -15 -11 -27 0 -27 C 11 -27 11 -15 0 0 Z" fill="{c}"/><circle cy="-18" r="4.5" fill="#ffffff"/></g>'
ISLANDSMAP = """
      <g stroke="#ffffff" stroke-width="2" opacity="0.30" fill="none">
        <path d="M -140 -70 q 20 8 40 0 t 40 0"/><path d="M -150 60 q 20 8 40 0 t 40 0 t 40 0"/>
        <path d="M 30 100 q 20 8 40 0 t 40 0"/></g>
      <g fill="#e6dcc7" stroke="#c7b998" stroke-width="2">
        <path d="M -112 -34 q 20 -22 46 -8 q 26 -2 20 22 q 6 20 -20 24 q -30 12 -46 -8 q -18 -14 0 -30 Z"/>
        <path d="M 44 -78 q 24 -16 44 4 q 18 4 8 24 q 2 18 -22 18 q -26 6 -34 -14 q -12 -22 4 -32 Z"/>
        <path d="M -18 44 q 26 -14 50 4 q 22 6 12 26 q 0 18 -26 18 q -30 4 -40 -18 q -10 -24 4 -30 Z"/></g>
      <path d="M -74 -18 Q -14 -74 66 -50 Q 44 4 8 66" fill="none" stroke="#b23a3a" stroke-width="3" stroke-dasharray="7 7" stroke-linecap="round"/>
      <circle cx="-74" cy="-18" r="5" fill="#ffffff" stroke="#b23a3a" stroke-width="3"/>
      <circle cx="66" cy="-50" r="5" fill="#ffffff" stroke="#b23a3a" stroke-width="3"/>
""" + pin(8, 66)

EMBLEMS = {"Santorini": SANTORINI, "Parthenon": PARTHENON, "IslandsMap": ISLANDSMAP}

def frame(art, pal):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="'Georgia','Times New Roman',serif">
{DEFS}
  <text x="{CX}" y="122" text-anchor="middle" font-size="70" font-weight="bold" fill="{pal['head']}" letter-spacing="4">WEIDBERG</text>
  <text x="{CX}" y="164" text-anchor="middle" font-size="27" fill="{pal['mid']}" letter-spacing="11">FAMILY&#160;VACATION</text>
  <g transform="translate({CX},{CY})">
    <circle r="{R}" fill="url(#sea)" stroke="{pal['ring']}" stroke-width="7"/>
    <clipPath id="clip"><circle r="{R-4}"/></clipPath>
    <g clip-path="url(#clip)">
{art}
    </g>
    <g stroke="{pal['oliveDk']}" stroke-width="5" fill="{pal['olive']}">
      <path d="M {-R} 22 q -38 30 -52 78" fill="none"/>
      <ellipse cx="{-R-28}" cy="58" rx="10" ry="5" transform="rotate(-35 {-R-28} 58)"/>
      <ellipse cx="{-R-42}" cy="80" rx="10" ry="5" transform="rotate(-25 {-R-42} 80)"/>
      <ellipse cx="{-R-50}" cy="103" rx="10" ry="5" transform="rotate(-15 {-R-50} 103)"/>
      <path d="M {R} 22 q 38 30 52 78" fill="none"/>
      <ellipse cx="{R+28}" cy="58" rx="10" ry="5" transform="rotate(35 {R+28} 58)"/>
      <ellipse cx="{R+42}" cy="80" rx="10" ry="5" transform="rotate(25 {R+42} 80)"/>
      <ellipse cx="{R+50}" cy="103" rx="10" ry="5" transform="rotate(15 {R+50} 103)"/>
    </g>
  </g>
  <text x="{CX}" y="678" text-anchor="middle" font-size="78" font-weight="bold" fill="{pal['head']}" letter-spacing="10">GREECE</text>
  <g transform="translate({CX-120},706)" stroke="{pal['rule']}" stroke-width="6" fill="none" stroke-linejoin="miter">
    <path d="M0 20 h18 v-16 h16 v16 h-9 v-9 h9 M43 4 h18 v16 h16 v-16 h-9 v9 h9 M86 20 h18 v-16 h16 v16 h-9 v-9 h9 M129 4 h18 v16 h16 v-16 h-9 v9 h9 M172 20 h18 v-16 h16 v16 h-9 v-9 h9"/>
  </g>
  <text x="{CX}" y="782" text-anchor="middle" font-size="32" fill="{pal['mid']}" letter-spacing="7">SUMMER&#160;&#8226;&#160;JULY&#160;2026</text>
  <text x="{CX}" y="820" text-anchor="middle" font-size="19" font-style="italic" fill="{pal['sub']}" letter-spacing="1">&#963;&#945;&#962;&#160;&#960;&#945;&#961;&#945;&#954;&#945;&#955;&#974; &#8212; &#8220;Please&#8221;, pack the sunscreen!</text>
</svg>"""

def little_key(x, y, pal):
    return f'<g transform="translate({x},{y}) scale(0.8)" stroke="{pal["rule"]}" stroke-width="6" fill="none" stroke-linejoin="miter"><path d="M0 20 h18 v-16 h16 v16 h-9 v-9 h9 M43 4 h18 v16 h16 v-16 h-9 v9 h9 M86 20 h18 v-16 h16 v16 h-9 v-9 h9 M129 4 h18 v16 h16 v-16 h-9 v9 h9 M172 20 h18 v-16 h16 v16 h-9 v-9 h9"/></g>'

def olive_sprig(x, y, flip, pal):
    s = -1 if flip else 1
    return (f'<g transform="translate({x},{y}) scale({s},1)" stroke="{pal["oliveDk"]}" stroke-width="4" fill="{pal["olive"]}">'
            f'<path d="M0 0 q 34 -6 60 -30" fill="none"/>'
            f'<ellipse cx="20" cy="-6" rx="9" ry="4.5" transform="rotate(-20 20 -6)"/>'
            f'<ellipse cx="38" cy="-15" rx="9" ry="4.5" transform="rotate(-30 38 -15)"/>'
            f'<ellipse cx="54" cy="-27" rx="9" ry="4.5" transform="rotate(-40 54 -27)"/></g>')

def back(pal):
    rows = ""
    y0, dy = 300, 56
    for i, n in enumerate(NAMES):
        rows += f'<text x="{CX}" y="{y0+i*dy}" text-anchor="middle" font-size="44" font-weight="bold" fill="{pal["name"]}" letter-spacing="3">{n.upper()}</text>'
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="'Georgia','Times New Roman',serif">
{DEFS}
  <text x="{CX}" y="120" text-anchor="middle" font-size="60" font-weight="bold" fill="{pal['head']}" letter-spacing="5">TEAM&#160;WEIDBERG</text>
  <text x="{CX}" y="162" text-anchor="middle" font-size="26" fill="{pal['mid']}" letter-spacing="8">GREECE&#160;&#8226;&#160;SUMMER&#160;2026</text>
  {little_key(CX-96, 190, pal)}
  {olive_sprig(CX-150, 268, False, pal)}{olive_sprig(CX+150, 268, True, pal)}
  {rows}
  {little_key(CX-96, 720, pal)}
  <text x="{CX}" y="792" text-anchor="middle" font-size="21" font-style="italic" fill="{pal['sub']}" letter-spacing="1">eight Weidbergs &#8226; one Greek summer</text>
</svg>"""

def render(svg, png, pal):
    with open(png[:-4] + ".svg", "w") as f:
        f.write(svg)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=png, output_width=W, output_height=H,
                     background_color=pal["preview"])

made = []
for name, art in EMBLEMS.items():
    for tag, pal in (("Light", LIGHT), ("Dark", DARK)):
        fn = f"Front_{name}_{tag}"
        render(frame(art, pal), fn + ".png", pal)
        made.append(fn)
for tag, pal in (("Light", LIGHT), ("Dark", DARK)):
    fn = f"Back_Roster_{tag}"
    render(back(pal), fn + ".png", pal)
    made.append(fn)
print("designs:", ", ".join(made))

# ---- front+back layout sheets (PIL compositing) ----
def load_font(size, bold=True):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"]:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()

for name, tag, pal, fg in (("Santorini", "Light", LIGHT, "#12496e"),
                           ("Santorini", "Dark", DARK, "#f6c445"),
                           ("IslandsMap", "Dark", DARK, "#f6c445")):
    front = Image.open(f"Front_{name}_{tag}.png").convert("RGB")
    roster = Image.open(f"Back_Roster_{tag}.png").convert("RGB")
    pad, gap, top = 40, 60, 70
    sheet = Image.new("RGB", (pad*2 + W*2 + gap, top + H + pad), pal["preview"])
    sheet.paste(front, (pad, top))
    sheet.paste(roster, (pad + W + gap, top))
    d = ImageDraw.Draw(sheet)
    f = load_font(34)
    d.text((pad + W//2, 30), "FRONT", fill=fg, font=f, anchor="mm")
    d.text((pad + W + gap + W//2, 30), "BACK", fill=fg, font=f, anchor="mm")
    out = f"Layout_{name}_{tag}.png"
    sheet.save(out)
    print("layout:", out)
