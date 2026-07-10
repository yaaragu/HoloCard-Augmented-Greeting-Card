# Weidberg Family Vacation — Greece Shirt Designs

Custom summer designs for the Weidberg family's July 2026 trip to Greece.

## Design-only variations (no shirt, transparent background)

These are **print-ready graphics**: no garment silhouette, transparent background,
so the same art drops onto any shirt style or color. Only the central image
changes between them.

| File | Central image |
|------|---------------|
| `WeidbergGreece_Santorini.svg` | Santorini cliff houses + blue domes |
| `WeidbergGreece_Parthenon.svg` | Acropolis / Parthenon temple |
| `WeidbergGreece_Mykonos.svg`   | Mykonos windmill |
| `WeidbergGreece_Sailboat.svg`  | Aegean sailboat |
| `WeidbergGreece_OliveSun.svg`  | Sun inside an olive wreath (minimal) |

Each has a matching `preview_<name>.png` (800×900, rendered on a light-gray card
for visibility — the SVG itself is transparent).

Shared frame: **WEIDBERG / FAMILY VACATION** over **GREECE**, a Greek-key
(meander) divider, and **SUMMER · JULY 2026**. Palette: Aegean blues, olive
green, sun gold.

## Named + colorway set (front & back)

For the 8-person family: **Jon, Talia, Abby, David, Benny, Yaara, Eli, Wendy.**

- **Back roster** — `Back_Roster_Light.svg` / `Back_Roster_Dark.svg`
  ("TEAM WEIDBERG" + all 8 names + Greek-key trim).
- **Front colorways** — each front comes in a **Light** (dark ink, for a light
  shirt) and **Dark** (white/gold ink, for a dark shirt) version:
  `Front_Santorini_{Light,Dark}.svg`, `Front_Parthenon_{Light,Dark}.svg`,
  `Front_IslandsMap_{Light,Dark}.svg`.
- **New image** — `Front_IslandsMap_*` : a stylized Aegean island-hop map with a
  dashed travel route and a destination pin.
- **Front + back layout sheets** — `Layout_Santorini_{Light,Dark}.png`,
  `Layout_IslandsMap_Dark.png` (print reference showing both panels together).

Regenerate with `python3 generate_named.py` (needs `cairosvg` + `pillow`).
To change or reorder names, edit the `NAMES` list at the top of that script.

## Modern set (chosen direction — no badge, sans-serif)

Two badge-free, modern designs with matching fronts and back rosters, in
**Light** (dark ink on a light shirt) and **Dark** (white/gold ink on a dark
shirt) colorways:

- **A — Sunrise line-art** — `Modern_A_SunriseLine_*` (front),
  `ModernBack_A_SunriseLine_*` (back), `ModernLayout_A_SunriseLine_*` (front+back sheet)
- **C — Editorial type-only** — `Modern_C_TypeOnly_*` (front),
  `ModernBack_C_TypeOnly_*` (back), `ModernLayout_C_TypeOnly_*` (front+back sheet)

Backs read **THE WEIDBERGS** / roster of all 8 names, styled to match each
front (no Greek-key border).

### Transparent (no background) exports

`Transparent_<concept>_<Front|Back>_<Light|Dark>.png` — true alpha PNGs with no
background, ready to drop straight onto any shirt color/mockup. The `.svg`
sources are transparent as well; the other `.png` previews only add a
background so the art is visible on screen.

Regenerate: `python3 generate_modern.py && python3 generate_modern_back.py`.

## Tank-top mockup (original)

- `WeidbergFamily_Greece_Tank.svg` — the Santorini art shown on a sleeveless
  tank silhouette (`preview.png`), for July heat.

## Regenerating

`generate_variations.py` builds every design-only SVG + PNG:

```bash
python3 generate_variations.py    # needs: pip install cairosvg
```

## Printing / editing

Open any SVG in Illustrator, Inkscape, or Figma. Vectors scale to any size
with no quality loss. For DTG/screen printing, export the transparent SVG at
300 DPI at the final print dimensions.
