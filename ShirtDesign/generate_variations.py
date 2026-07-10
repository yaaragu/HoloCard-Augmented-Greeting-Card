#!/usr/bin/env python3
"""Generate Weidberg-family Greece vacation shirt design variations.

Each design is print-ready: no shirt silhouette, transparent background,
editable vector. Only the central emblem image changes between variations.
"""
import cairosvg

W, H = 800, 900
CX = 400          # emblem centre x
CY = 420          # emblem centre y
R = 150           # emblem radius

DEFS = """
  <defs>
    <radialGradient id="sun" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ffe08a"/>
      <stop offset="0.7" stop-color="#f6c445"/>
      <stop offset="1" stop-color="#f2b134"/>
    </radialGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#4aa8d8"/>
      <stop offset="1" stop-color="#1c6ea4"/>
    </linearGradient>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#eaf6ff"/>
      <stop offset="1" stop-color="#cfe8fb"/>
    </linearGradient>
    <linearGradient id="stone" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff"/>
      <stop offset="1" stop-color="#e6dcc7"/>
    </linearGradient>
  </defs>
"""

def frame(inner):
    """Common typographic frame; `inner` is the emblem art (already positioned)."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="'Georgia','Times New Roman',serif">
{DEFS}
  <!-- WEIDBERG / FAMILY VACATION -->
  <text x="{CX}" y="122" text-anchor="middle" font-size="70" font-weight="bold" fill="#12496e" letter-spacing="4">WEIDBERG</text>
  <text x="{CX}" y="164" text-anchor="middle" font-size="27" fill="#2f7fae" letter-spacing="11">FAMILY&#160;VACATION</text>

  <!-- Emblem -->
  <g transform="translate({CX},{CY})">
    <circle r="{R}" fill="url(#sea)" stroke="#0f4f76" stroke-width="7"/>
    <clipPath id="clip"><circle r="{R-4}"/></clipPath>
    <g clip-path="url(#clip)">
{inner}
    </g>
    <!-- olive branches flanking -->
    <g stroke="#5f8f3e" stroke-width="5" fill="#7cae4e">
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

  <!-- GREECE -->
  <text x="{CX}" y="678" text-anchor="middle" font-size="78" font-weight="bold" fill="#12496e" letter-spacing="10">GREECE</text>

  <!-- Greek-key divider -->
  <g transform="translate({CX-120},706)" stroke="#2f7fae" stroke-width="6" fill="none" stroke-linejoin="miter">
    <path d="M0 20 h18 v-16 h16 v16 h-9 v-9 h9
             M43 4 h18 v16 h16 v-16 h-9 v9 h9
             M86 20 h18 v-16 h16 v16 h-9 v-9 h9
             M129 4 h18 v16 h16 v-16 h-9 v9 h9
             M172 20 h18 v-16 h16 v16 h-9 v-9 h9"/>
  </g>

  <!-- SUMMER JULY 2026 -->
  <text x="{CX}" y="782" text-anchor="middle" font-size="32" fill="#2f7fae" letter-spacing="7">SUMMER&#160;&#8226;&#160;JULY&#160;2026</text>
  <text x="{CX}" y="820" text-anchor="middle" font-size="19" font-style="italic" fill="#6b8697" letter-spacing="1">&#963;&#945;&#962;&#160;&#960;&#945;&#961;&#945;&#954;&#945;&#955;&#974; &#8212; &#8220;Please&#8221;, pack the sunscreen!</text>
</svg>"""

# sky + sun + sea backdrop shared by scenic emblems
def backdrop(sun_x=70, sun_y=-80, sea_y=55):
    return f"""      <rect x="{-R}" y="{-R}" width="{2*R}" height="{R+sea_y}" fill="url(#sky)"/>
      <circle cx="{sun_x}" cy="{sun_y}" r="38" fill="url(#sun)"/>
      <rect x="{-R}" y="{sea_y}" width="{2*R}" height="{R-sea_y}" fill="url(#sea)"/>
      <path d="M {-R} {sea_y} q 30 12 60 0 t 60 0 t 60 0 t 60 0 t 60 0" fill="none" stroke="#ffffff" stroke-width="3" opacity="0.55"/>"""

# ---------- V0: Santorini ----------
santorini = backdrop(sun_x=72, sun_y=-78) + f"""
      <g fill="#ffffff" stroke="#c9d6df" stroke-width="2">
        <rect x="-120" y="-20" width="70" height="78"/>
        <rect x="-58" y="-45" width="60" height="103"/>
        <rect x="0" y="-10" width="55" height="68"/>
        <rect x="48" y="-40" width="60" height="98"/>
      </g>
      <path d="M -95 -20 a 20 20 0 0 1 40 0 Z" fill="#1c7fc0"/>
      <path d="M -28 -45 a 18 18 0 0 1 36 0 Z" fill="#1565a8"/>
      <path d="M 62 -40 a 22 22 0 0 1 44 0 Z" fill="#1c7fc0"/>
      <path d="M -75 -45 v 16 M -83 -37 h 16" stroke="#0f4f76" stroke-width="3"/>
      <path d="M 84 -66 v 16 M 76 -58 h 16" stroke="#0f4f76" stroke-width="3"/>"""

# ---------- V1: Parthenon / Acropolis ----------
def columns(x0, y_top, y_bot, n, w, gap):
    s = ""
    for i in range(n):
        x = x0 + i*(w+gap)
        s += f'<rect x="{x}" y="{y_top}" width="{w}" height="{y_bot-y_top}" fill="url(#stone)" stroke="#cdбc9a" stroke-width="1"/>'.replace("cdбc9a","cbbf9e")
    return s
parthenon = backdrop(sun_x=95, sun_y=-88, sea_y=70) + f"""
      <!-- steps -->
      <rect x="-118" y="58" width="236" height="12" fill="#efe7d4" stroke="#cbbf9e"/>
      <rect x="-108" y="46" width="216" height="12" fill="#f5eede" stroke="#cbbf9e"/>
      <!-- columns -->
      {columns(-96, -18, 46, 7, 18, 12)}
      <!-- architrave -->
      <rect x="-104" y="-30" width="208" height="14" fill="#f5eede" stroke="#cbbf9e"/>
      <!-- pediment -->
      <path d="M -110 -30 L 0 -92 L 110 -30 Z" fill="url(#stone)" stroke="#cbbf9e" stroke-width="2"/>
      <path d="M -104 -32 L 0 -84 L 104 -32 Z" fill="#efe7d4"/>"""

# ---------- V2: Mykonos windmill ----------
mykonos = backdrop(sun_x=-78, sun_y=-70, sea_y=60) + f"""
      <!-- tower -->
      <path d="M -34 55 L -26 -46 L 26 -46 L 34 55 Z" fill="url(#stone)" stroke="#cbbf9e" stroke-width="2"/>
      <rect x="-30" y="-58" width="60" height="14" rx="3" fill="#efe7d4" stroke="#cbbf9e"/>
      <!-- conical roof -->
      <path d="M -34 -58 L 0 -96 L 34 -58 Z" fill="#7a5a3a" stroke="#5f4527" stroke-width="2"/>
      <!-- windows/door -->
      <rect x="-8" y="20" width="16" height="30" fill="#1c6ea4"/>
      <rect x="-22" y="-30" width="12" height="12" fill="#1c6ea4"/>
      <rect x="10" y="-30" width="12" height="12" fill="#1c6ea4"/>
      <!-- sail blades -->
      <g stroke="#8a6a44" stroke-width="4" fill="#ffffff" fill-opacity="0.9">
        <g transform="translate(0,-62)">
          <rect x="-3" y="-70" width="6" height="70"/>
          <rect x="0" y="-3" width="70" height="6"/>
          <rect x="-70" y="-3" width="70" height="6"/>
          <rect x="-3" y="0" width="6" height="70"/>
          <path d="M 6 -60 L 44 -6 L 6 -6 Z" fill="#eef4f8"/>
          <path d="M 60 6 L 6 44 L 6 6 Z" fill="#eef4f8"/>
          <path d="M -6 60 L -44 6 L -6 6 Z" fill="#eef4f8"/>
          <path d="M -60 -6 L -6 -44 L -6 -6 Z" fill="#eef4f8"/>
        </g>
      </g>"""

# ---------- V3: Aegean sailboat ----------
sailboat = backdrop(sun_x=-82, sun_y=-82, sea_y=40) + f"""
      <!-- distant island -->
      <path d="M 30 40 q 40 -34 92 0 Z" fill="#9fb6c4" opacity="0.7"/>
      <!-- mast + sails -->
      <line x1="6" y1="-96" x2="6" y2="34" stroke="#5f4527" stroke-width="5"/>
      <path d="M 4 -92 L 4 24 L -70 24 Z" fill="#ffffff" stroke="#cdd8e0" stroke-width="2"/>
      <path d="M 10 -60 L 10 24 L 64 24 Z" fill="#eef4f8" stroke="#cdd8e0" stroke-width="2"/>
      <!-- hull -->
      <path d="M -84 34 Q 0 74 84 34 L 66 52 Q 0 78 -66 52 Z" fill="#b23a3a" stroke="#7d2626" stroke-width="2"/>
      <!-- little flag -->
      <path d="M 6 -96 l 26 8 l -26 8 Z" fill="#1c6ea4"/>"""

# ---------- V4: Olive wreath + sun (minimal) ----------
def wreath_leaves(direction):
    s = ""
    import math
    start, end = (-70, 70) if direction == 1 else (110, 250)
    for deg in range(start, end+1, 14):
        rad = math.radians(deg)
        lx = 118*math.cos(rad)
        ly = 118*math.sin(rad)
        s += f'<ellipse cx="{lx:.1f}" cy="{ly:.1f}" rx="15" ry="7" transform="rotate({deg+90:.0f} {lx:.1f} {ly:.1f})" fill="#7cae4e" stroke="#5f8f3e" stroke-width="1.5"/>'
    return s
olive = f"""      <rect x="{-R}" y="{-R}" width="{2*R}" height="{2*R}" fill="url(#sky)"/>
      <circle cx="0" cy="0" r="62" fill="url(#sun)"/>
      <g stroke="#f2b134" stroke-width="5" stroke-linecap="round">
        <line x1="0" y1="-92" x2="0" y2="-108"/>
        <line x1="0" y1="92" x2="0" y2="108"/>
        <line x1="-92" y1="0" x2="-108" y2="0"/>
        <line x1="92" y1="0" x2="108" y2="0"/>
        <line x1="-65" y1="-65" x2="-77" y2="-77"/>
        <line x1="65" y1="-65" x2="77" y2="-77"/>
        <line x1="-65" y1="65" x2="-77" y2="77"/>
        <line x1="65" y1="65" x2="77" y2="77"/>
      </g>
      <path d="M 0 -118 a 118 118 0 0 1 0 236" fill="none" stroke="#5f8f3e" stroke-width="3"/>
      <path d="M 0 -118 a 118 118 0 0 0 0 236" fill="none" stroke="#5f8f3e" stroke-width="3"/>
      {wreath_leaves(1)}{wreath_leaves(-1)}"""

variations = {
    "Santorini": santorini,
    "Parthenon": parthenon,
    "Mykonos":   mykonos,
    "Sailboat":  sailboat,
    "OliveSun":  olive,
}

previews = []
for name, art in variations.items():
    svg = frame(art)
    fn = f"WeidbergGreece_{name}.svg"
    with open(fn, "w") as f:
        f.write(svg)
    png = f"preview_{name}.png"
    cairosvg.svg2png(url=fn, write_to=png, output_width=W, output_height=H,
                     background_color="#f3f6f9")
    previews.append(png)
    print("wrote", fn, "+", png)

# contact sheet
tiles = "".join(
    f'<image href="preview_{n}.png" x="{(i%3)*270}" y="{(i//3)*304}" width="264" height="297"/>'
    for i, n in enumerate(variations)
)
sheet = f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="810" height="608"><rect width="810" height="608" fill="#e8edf1"/>{tiles.replace("href","xlink:href")}</svg>'
with open("contact_sheet.svg", "w") as f:
    f.write(sheet)
cairosvg.svg2png(url="contact_sheet.svg", write_to="contact_sheet.png",
                 output_width=810, output_height=608)
print("wrote contact_sheet.png")
