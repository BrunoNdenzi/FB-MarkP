from PIL import Image, ImageDraw, ImageFont
import os
import math

TILES_DIR = os.path.join(os.path.dirname(__file__), "Tiles")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "contact_sheet.jpg")

THUMB_W = 400
THUMB_H = 300
COLS = 4
PADDING = 16
LABEL_H = 28
BG_COLOR = (30, 30, 30)
LABEL_COLOR = (220, 220, 220)

# Collect only images
exts = {".jpg", ".jpeg", ".png", ".webp"}
images = sorted(
    [f for f in os.listdir(TILES_DIR) if os.path.splitext(f)[1].lower() in exts]
)

if not images:
    print("No images found in Tiles/")
    exit(1)

rows = math.ceil(len(images) / COLS)
cell_w = THUMB_W + PADDING
cell_h = THUMB_H + LABEL_H + PADDING

sheet_w = COLS * cell_w + PADDING
sheet_h = rows * cell_h + PADDING

sheet = Image.new("RGB", (sheet_w, sheet_h), BG_COLOR)
draw = ImageDraw.Draw(sheet)

# Try to load a font, fall back to default
try:
    font = ImageFont.truetype("arial.ttf", 14)
except Exception:
    font = ImageFont.load_default()

for idx, fname in enumerate(images):
    row = idx // COLS
    col = idx % COLS
    x = PADDING + col * cell_w
    y = PADDING + row * cell_h

    path = os.path.join(TILES_DIR, fname)
    try:
        img = Image.open(path)
        img.thumbnail((THUMB_W, THUMB_H), Image.LANCZOS)
        # Centre thumbnail in its cell
        offset_x = x + (THUMB_W - img.width) // 2
        offset_y = y + (THUMB_H - img.height) // 2
        sheet.paste(img, (offset_x, offset_y))
    except Exception as e:
        print(f"  Skipping {fname}: {e}")
        continue

    # Label below thumbnail
    label = os.path.splitext(fname)[0]
    if len(label) > 42:
        label = label[:39] + "..."
    draw.text((x, y + THUMB_H + 4), label, fill=LABEL_COLOR, font=font)

sheet.save(OUTPUT_PATH, "JPEG", quality=90)
print(f"Contact sheet saved to: {OUTPUT_PATH}")
print(f"  {len(images)} images  |  {COLS} columns  |  {rows} rows")
