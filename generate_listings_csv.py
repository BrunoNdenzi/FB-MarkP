"""
Facebook Marketplace / Commerce Manager Listing CSV Generator
Project: Tile Warehouse Sales — Charlotte NC

HOW TO USE:
  1. Edit the LISTINGS section below to update prices, titles, or descriptions
  2. Run:   python generate_listings_csv.py
  3. Output: listings_catalog.csv
  4. Upload to Facebook Commerce Manager:
       business.facebook.com
       > Commerce Manager > Catalog > Data Sources > Re-upload data file

HOW TO UPDATE A PRICE:
  - Find the listing by its id (e.g. TILE-WL-004 for wood-look)
  - Change the "price" value  (format must be: "50.00 USD")
  - Re-run script — new CSV is generated automatically
  - Re-upload listings_catalog.csv to Facebook

NOTE ON IMAGES AND VIDEOS:
  Images and videos are pulled from GitHub raw URLs.
  The FB-MarkP repository must be set to PUBLIC for Facebook to load them.
  If private, host files on Imgur or Google Drive (public link) instead.
"""

import csv
import urllib.parse

# ─────────────────────────────────────────────────────────
# SETTINGS
# ─────────────────────────────────────────────────────────
BASE_IMAGE_URL = "https://raw.githubusercontent.com/BrunoNdenzi/FB-MarkP/main/Tiles/"
STORE_LINK     = "https://www.facebook.com/marketplace/charlotte"
OUTPUT_FILE    = "listings_catalog.csv"
BRAND          = "Warehouse Direct"
CATEGORY       = "Building Materials > Flooring > Tile"
AVAILABILITY  = "in stock"
CONDITION     = "new"
MAX_EXTRA_IMAGES = 5


def img(filename):
    """Convert an image filename to a fully encoded GitHub raw URL."""
    return BASE_IMAGE_URL + urllib.parse.quote(filename)


def vid(filename):
    """Convert a video filename to a fully encoded GitHub raw URL."""
    return BASE_IMAGE_URL + urllib.parse.quote(filename)


# ─────────────────────────────────────────────────────────
# LISTINGS
# To add a listing : copy any block, paste at end, change values
# To remove        : delete the block
# To update price  : change the "price" value and re-run
# To update video  : change the "video" value and re-run
# ─────────────────────────────────────────────────────────
LISTINGS = [

    # ── LISTING 1 — White Marble Polished 24x48 ───────────
    {
        "id"   : "TILE-WM-001",
        "title": "24x48 Polished Porcelain Tile - White Marble Look - $99/case - Charlotte",
        "description": (
            "Selling premium quality 24x48 polished porcelain tiles directly from warehouse. "
            "White marble look with natural grey veining. "
            "Works for floors, walls, bathrooms, kitchens, and feature walls. "
            "Brand new in boxes. Priced well below retail. "
            "$99 per case - multiple cases available. "
            "Pickup in Charlotte. Cash or Zelle. "
            "Size: 24x48 inches | Finish: Polished | Style: White marble with grey veining. "
            "Text for details and available quantity. Can hold with deposit."
        ),
        "price": "99.00 USD",
        "image_link": img("WhatsApp Image 2026-06-10 at 16.09.34 (2).jpeg"),
        "additional_images": [
            img("WhatsApp Image 2026-06-10 at 16.09.36 (1).jpeg"),
            img("WhatsApp Image 2026-06-10 at 16.09.42.jpeg"),
            img("WhatsApp Image 2026-06-10 at 16.09.37 (1).jpeg"),
            img("WhatsApp Image 2026-06-10 at 16.09.41.jpeg"),
            img("WhatsApp Image 2026-06-10 at 16.09.35.jpeg"),
        ],
        "video": vid("WhatsApp Video 2026-06-10 at 16.09.30.mp4"),
    },

    # ── LISTING 2 — Calacatta Gold Polished 24x48 ─────────
    {
        "id"   : "TILE-CG-002",
        "title": "24x48 Polished Porcelain Tile - Calacatta Gold Look - $99/case - Charlotte",
        "description": (
            "Warehouse surplus sale. 24x48 polished porcelain tiles with warm white base and gold and brown veining. "
            "Upscale look for kitchens, master bathrooms, or living areas. "
            "Brand new in boxes. Limited quantity. "
            "$99 per case. Pickup Charlotte area. Cash or Zelle. "
            "Size: 24x48 inches | Finish: Polished | Style: Calacatta Gold veining. "
            "Text to confirm availability."
        ),
        "price": "99.00 USD",
        "image_link": img("WhatsApp Image 2026-06-10 at 16.09.41 (1).jpeg"),
        "additional_images": [
            img("WhatsApp Image 2026-06-10 at 16.09.41 (2).jpeg"),
            img("WhatsApp Image 2026-06-10 at 16.09.41 (4).jpeg"),
        ],
        "video": vid("WhatsApp Video 2026-06-10 at 16.09.38.mp4"),
    },

    # ── LISTING 3 — Dark Charcoal Matte 24x48 ─────────────
    {
        "id"   : "TILE-DC-003",
        "title": "24x48 Dark Charcoal Porcelain Tile - Matte Finish - $70/case - Charlotte",
        "description": (
            "Warehouse clearance. Large format 24x48 dark charcoal slate look porcelain tile, matte finish. "
            "Perfect for modern bathrooms, commercial spaces, accent walls, or outdoor areas. "
            "Brand new in boxes. "
            "$70 per case. Pickup Charlotte area. Cash or Zelle. "
            "Size: 24x48 inches | Finish: Matte | Style: Dark charcoal slate look. "
            "Text for availability and quantity."
        ),
        "price": "70.00 USD",
        "image_link": img("WhatsApp Image 2026-06-10 at 16.09.33 (1).jpeg"),
        "additional_images": [
            img("WhatsApp Image 2026-06-10 at 16.09.34 (1).jpeg"),
        ],
        "video": vid("WhatsApp Video 2026-06-10 at 16.09.32 (3).mp4"),
    },

    # ── LISTING 4 — Wood-Look Plank ────────────────────────
    # PLACEHOLDER PRICE — update once warehouse confirms
    {
        "id"   : "TILE-WL-004",
        "title": "Wood-Look Plank Flooring - Warehouse Clearance Charlotte - Message for Price",
        "description": (
            "Warehouse surplus. Wood-look plank tile or luxury vinyl plank flooring. "
            "Warm brown tones, realistic wood grain look. "
            "Brand new in boxes. Multiple cases available. "
            "Price varies by quantity - message us with how many cases you need and we will confirm current pricing. "
            "Pickup in Charlotte. Cash or Zelle. "
            "Text for pricing and availability."
        ),
        "price": "50.00 USD",   # PLACEHOLDER — update once confirmed with warehouse
        "image_link": img("WhatsApp Image 2026-06-10 at 16.09.33.jpeg"),
        "additional_images": [
            img("WhatsApp Image 2026-06-10 at 16.09.35 (1).jpeg"),
        ],
        "video": vid("WhatsApp Video 2026-06-10 at 16.09.37.mp4"),
    },

    # ── LISTING 5 — Blue-Grey Large Format ────────────────
    # PLACEHOLDER PRICE — update once warehouse confirms
    {
        "id"   : "TILE-BG-005",
        "title": "Large Format Blue-Grey Porcelain Tile - Clearance Price - Charlotte",
        "description": (
            "Warehouse clearance sale. Large format blue-grey porcelain tile. "
            "Cool modern tone, great for bathrooms, kitchens, or accent walls. "
            "Brand new in boxes. "
            "Price varies - message us with quantity needed and we will confirm current pricing. "
            "Pickup Charlotte area. Cash or Zelle. "
            "Text for pricing and availability."
        ),
        "price": "50.00 USD",   # PLACEHOLDER — update once confirmed with warehouse
        "image_link": img("WhatsApp Image 2026-06-10 at 16.09.41 (3).jpeg"),
        "additional_images": [
            img("WhatsApp Image 2026-06-10 at 16.09.34.jpeg"),
        ],
        "video": vid("WhatsApp Video 2026-06-10 at 16.09.35.mp4"),
    },

    # ── LISTING 6 — Catch-All / Traffic Driver ─────────────
    {
        "id"   : "TILE-ALL-006",
        "title": "Charlotte Tile Warehouse Sale - Multiple Styles - 24x48 and 12x24 Available",
        "description": (
            "We have access to warehouse surplus tile inventory in Charlotte. "
            "Multiple styles available including white marble look, dark charcoal, wood-look flooring, and more. "
            "24x48 Polished $99/case. 24x48 Matte $70/case. 12x24 Polished $22/case. 12x24 Matte $12/case. "
            "Other styles - message for pricing. "
            "New in boxes. Priced below retail. Great for contractors, flippers, and homeowners. "
            "Pickup Charlotte area. Cash or Zelle. "
            "Text with what you are looking for and we will confirm availability."
        ),
        "price": "12.00 USD",
        "image_link": img("WhatsApp Image 2026-06-10 at 16.09.34 (1).jpeg"),
        "additional_images": [
            img("WhatsApp Image 2026-06-10 at 16.09.34 (2).jpeg"),
            img("WhatsApp Image 2026-06-10 at 16.09.33 (1).jpeg"),
            img("WhatsApp Image 2026-06-10 at 16.09.33.jpeg"),
            img("WhatsApp Image 2026-06-10 at 16.09.41 (3).jpeg"),
            img("WhatsApp Image 2026-06-10 at 16.09.38 (1).jpeg"),
        ],
        "video": vid("WhatsApp Video 2026-06-10 at 16.09.32 (1).mp4"),
    },

]


# ─────────────────────────────────────────────────────────
# CSV ENGINE — do not edit below this line
# ─────────────────────────────────────────────────────────
def generate_csv():
    extra_fields = [f"additional_image_link[{i}]" for i in range(MAX_EXTRA_IMAGES)]
    fieldnames = [
        "id", "title", "description", "availability", "condition",
        "price", "link", "image_link", "brand", "google_product_category",
        "video",
    ] + extra_fields

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for listing in LISTINGS:
            row = {
                "id"                      : listing["id"],
                "title"                   : listing["title"],
                "description"             : listing["description"],
                "availability"            : AVAILABILITY,
                "condition"               : CONDITION,
                "price"                   : listing["price"],
                "link"                    : STORE_LINK,
                "image_link"              : listing["image_link"],
                "brand"                   : BRAND,
                "google_product_category" : CATEGORY,
                "video"                   : listing.get("video", ""),
            }
            extras = listing.get("additional_images", [])
            for i in range(MAX_EXTRA_IMAGES):
                row[f"additional_image_link[{i}]"] = extras[i] if i < len(extras) else ""
            writer.writerow(row)

    print(f"\nGenerated : {OUTPUT_FILE}")
    print(f"Listings  : {len(LISTINGS)}")
    print(f"\nNext step : Re-upload to Facebook Commerce Manager")
    print(f"  business.facebook.com > Commerce Manager > Data Sources > Re-upload data file\n")


if __name__ == "__main__":
    generate_csv()
