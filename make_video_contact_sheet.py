import cv2
from PIL import Image, ImageDraw, ImageFont
import os
import math

TILES_DIR = os.path.join(os.path.dirname(__file__), "Tiles")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "contact_sheet_videos.jpg")

THUMB_W = 400
THUMB_H = 300
COLS = 4
PADDING = 16
LABEL_H = 28
BG_COLOR = (30, 30, 30)
LABEL_COLOR = (220, 220, 220)

videos = sorted(
    [f for f in os.listdir(TILES_DIR) if os.path.splitext(f)[1].lower() == ".mp4"]
)

if not videos:
    print("No MP4 files found in Tiles/")
    exit(1)

def extract_thumb(video_path, width, height):
    cap = cv2.VideoCapture(video_path)
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # Seek to ~25% into the video for a representative frame
    target = max(0, total // 4)
    cap.set(cv2.CAP_PROP_POS_FRAMES, target)
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()
    cap.release()
    if not ret:
        return None
    # Convert BGR -> RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    img.thumbnail((width, height), Image.LANCZOS)
    return img

rows = math.ceil(len(videos) / COLS)
cell_w = THUMB_W + PADDING
cell_h = THUMB_H + LABEL_H + PADDING

sheet_w = COLS * cell_w + PADDING
sheet_h = rows * cell_h + PADDING

sheet = Image.new("RGB", (sheet_w, sheet_h), BG_COLOR)
draw = ImageDraw.Draw(sheet)

try:
    font = ImageFont.truetype("arial.ttf", 14)
except Exception:
    font = ImageFont.load_default()

for idx, fname in enumerate(videos):
    row = idx // COLS
    col = idx % COLS
    x = PADDING + col * cell_w
    y = PADDING + row * cell_h

    path = os.path.join(TILES_DIR, fname)
    print(f"  Processing {fname}...")
    img = extract_thumb(path, THUMB_W, THUMB_H)

    if img:
        offset_x = x + (THUMB_W - img.width) // 2
        offset_y = y + (THUMB_H - img.height) // 2
        sheet.paste(img, (offset_x, offset_y))
    else:
        print(f"    Could not extract frame from {fname}")

    label = os.path.splitext(fname)[0]
    if len(label) > 42:
        label = label[:39] + "..."
    draw.text((x, y + THUMB_H + 4), label, fill=LABEL_COLOR, font=font)

sheet.save(OUTPUT_PATH, "JPEG", quality=90)
print(f"\nVideo contact sheet saved to: {OUTPUT_PATH}")
print(f"  {len(videos)} videos  |  {COLS} columns  |  {rows} rows")
