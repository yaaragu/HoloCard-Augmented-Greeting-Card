#!/usr/bin/env python3
"""Build use_figma JS chunks that import every design SVG as a native vector
object, each inside a shirt-colored frame, arranged in a labeled grid."""
import json, os, textwrap

# ordered groups: (group title, [ (svg filename, shirt-bg hex) ... ])
def bg_for(name):
    if name.endswith("_Dark"): return "#152230"
    if name.endswith("_WhiteOnBlue"): return "#0d5eaf"
    if name.endswith("_Sand"): return "#f0e7d8"
    return "#ffffff"

GROUPS = [
    ("Modern A — Sunrise line-art", [
        "Modern_A_SunriseLine_Light", "ModernBack_A_SunriseLine_Light",
        "Modern_A_SunriseLine_Dark", "ModernBack_A_SunriseLine_Dark",
        "Modern_A_SunriseLine_BlueOnWhite", "ModernBack_A_SunriseLine_BlueOnWhite",
        "Modern_A_SunriseLine_WhiteOnBlue", "ModernBack_A_SunriseLine_WhiteOnBlue"]),
    ("Modern C — Editorial type-only", [
        "Modern_C_TypeOnly_Light", "ModernBack_C_TypeOnly_Light",
        "Modern_C_TypeOnly_Dark", "ModernBack_C_TypeOnly_Dark",
        "Modern_C_TypeOnly_BlueOnWhite", "ModernBack_C_TypeOnly_BlueOnWhite",
        "Modern_C_TypeOnly_WhiteOnBlue", "ModernBack_C_TypeOnly_WhiteOnBlue"]),
    ("Modern B — Flat poster", [
        "Modern_B_FlatPoster_Light", "Modern_B_FlatPoster_Sand", "Modern_B_FlatPoster_Dark"]),
    ("Scenic emblems (design-only)", [
        "WeidbergGreece_Santorini", "WeidbergGreece_Parthenon", "WeidbergGreece_Mykonos",
        "WeidbergGreece_Sailboat", "WeidbergGreece_OliveSun"]),
    ("Named badge set (front + roster)", [
        "Front_Santorini_Light", "Front_Santorini_Dark",
        "Front_Parthenon_Light", "Front_IslandsMap_Light", "Front_IslandsMap_Dark",
        "Back_Roster_Light", "Back_Roster_Dark"]),
    ("Tank mockup", ["WeidbergFamily_Greece_Tank"]),
]

def hexrgb(h):
    h = h.lstrip("#")
    return {"r": int(h[0:2],16)/255, "g": int(h[2:4],16)/255, "b": int(h[4:6],16)/255}

COLS = 4
CELLW, CELLH = 900, 1040
GROUP_GAP = 120

# assign positions; each group starts on a fresh row
placed = []          # (name, svg, bg, x, y)
y = 0
for title, names in GROUPS:
    for i, name in enumerate(names):
        col = i % COLS
        row = i // COLS
        x = col * CELLW
        yy = y + row * CELLH
        svg = open(name + ".svg").read()
        placed.append((name, svg, bg_for(name), x, yy))
    rows = (len(names) + COLS - 1)//COLS
    y += rows * CELLH + GROUP_GAP

# chunk by char budget
CHUNK_CHARS = 26000
chunks, cur, size = [], [], 0
for item in placed:
    add = len(item[1]) + 400
    if cur and size + add > CHUNK_CHARS:
        chunks.append(cur); cur, size = [], 0
    cur.append(item); size += add
if cur: chunks.append(cur)

os.makedirs("figma_chunks", exist_ok=True)
for ci, chunk in enumerate(chunks):
    items_js = []
    for name, svg, bg, x, yy in chunk:
        items_js.append("{name:%s, bg:%s, x:%d, y:%d, svg:`%s`}" % (
            json.dumps(name), json.dumps(hexrgb(bg)), x, yy, svg))
    body = "const items = [\n" + ",\n".join(items_js) + "\n];\n" + textwrap.dedent("""
    const ids = [];
    for (const it of items) {
      const frame = figma.createFrame();
      frame.name = it.name;
      frame.resize(800, 900);
      frame.x = it.x; frame.y = it.y;
      frame.clipsContent = false;
      frame.fills = [{type:'SOLID', color: it.bg}];
      frame.cornerRadius = 12;
      const art = figma.createNodeFromSvg(it.svg);
      art.name = it.name + " (vector)";
      frame.appendChild(art);
      art.x = 0; art.y = 0;
      ids.push(frame.id);
    }
    return { created: ids.length, ids };
    """)
    with open(f"figma_chunks/chunk_{ci:02d}.js", "w") as f:
        f.write(body)

print(f"{len(placed)} designs -> {len(chunks)} chunks")
for ci, chunk in enumerate(chunks):
    print(f"  chunk_{ci:02d}: {len(chunk)} designs, {os.path.getsize(f'figma_chunks/chunk_{ci:02d}.js')} chars")
