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
