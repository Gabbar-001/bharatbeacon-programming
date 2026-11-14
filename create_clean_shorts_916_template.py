"""
create_clean_shorts_916_template.py
Creates the official 1080x1920 native 9:16 broadcast overlay template from the newly uploaded BharatBeacon template:
1. Upscales media_1794226224406_c54256d5.jpg (576x1024) to 1080x1920 Full HD.
2. Clears the inner golden image box (62, 706, 1018, 1180) to transparent alpha.
3. Cleans the yellow brush headline banner placeholder text.
4. Cleans the subtitle ticker placeholder text.
5. Cleans the 'BREAKING NEWS' 3D banners so dynamic topic lines can be placed inside.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

TEMPLATE_PATH = Path("C:/Users/mr_un/.gemini/antigravity/brain/a40d7958-d2a6-434b-bf71-f01f0b882465/.user_uploaded/media_1794226224406_c54256d5.jpg")
DEST_DIR = Path("assets/templates")
DEST_DIR.mkdir(parents=True, exist_ok=True)
MASTER_916 = DEST_DIR / "bharatbeacon_master_916.png"
ARTIFACT_DIR = Path("C:/Users/mr_un/.gemini/antigravity/brain/a40d7958-d2a6-434b-bf71-f01f0b882465")

def build_916_master():
    raw = Image.open(TEMPLATE_PATH).convert("RGBA")
    # Resize to standard 1080x1920
    im = raw.resize((1080, 1920), Image.Resampling.LANCZOS)
    W, H = im.size
    
    # 1. Clean the Yellow Headline Banner (y: 1210 to 1460, x: 50 to 1030)
    # The text 'YOUR ARTICLE HEADLINE HERE' is black.
    # Background is bright yellow ~(255, 218, 0).
    pixels = im.load()
    for y in range(1210, 1455):
        for x in range(50, 1030):
            r, g, b, a = pixels[x, y]
            # Replace dark text pixels with surrounding yellow
            if (r + g + b) / 3 < 125:
                # Yellow vertical gradient
                ratio = (y - 1210) / 245
                yr = 255
                yg = int(210 + ratio * 20)
                yb = int(0 + ratio * 15)
                pixels[x, y] = (yr, yg, yb, 255)
                
    # Smooth yellow banner to eliminate text edges
    y_blur = im.crop((50, 1210, 1030, 1455)).filter(ImageFilter.GaussianBlur(3))
    im.paste(y_blur, (50, 1210))
    
    # 2. Clean Subtitle Ticker Bar (y: 1478 to 1560, x: 135 to 1020)
    # Fill with deep navy gradient matching the ticker
    tick_w = 1020 - 135
    tick_h = 1560 - 1478
    patch = Image.new("RGBA", (tick_w, tick_h), (8, 16, 48, 255))
    p_draw = ImageDraw.Draw(patch)
    for ty in range(tick_h):
        p_draw.line([(0, ty), (tick_w, ty)], fill=(4 + ty // 3, 12 + ty // 3, 50 + ty // 3, 255))
    im.paste(patch, (135, 1478))

    # 3. Clean BREAKING NEWS 3D Banner
    # Top 3D block: y: 400 to 505 (cyan/blue)
    # Bottom 3D block: y: 505 to 665 (crimson red)
    # Replace white text pixels inside the banner with banner gradient
    # Blue block (x: 140 to 920, y: 400 to 505)
    for y in range(400, 505):
        for x in range(140, 920):
            r, g, b, a = pixels[x, y]
            # White text
            if r > 180 and g > 180 and b > 180:
                # Blue block gradient
                pixels[x, y] = (15, 65, 175, 255)
    # Red block (x: 180 to 930, y: 505 to 665)
    for y in range(505, 665):
        for x in range(180, 930):
            r, g, b, a = pixels[x, y]
            # White text
            if r > 180 and g > 180 and b > 180:
                # Red block gradient
                pixels[x, y] = (195, 15, 25, 255)

    b_blur = im.crop((140, 400, 920, 505)).filter(ImageFilter.GaussianBlur(3))
    im.paste(b_blur, (140, 400))
    r_blur = im.crop((180, 505, 930, 665)).filter(ImageFilter.GaussianBlur(3))
    im.paste(r_blur, (180, 505))

    # 4. Transparent Cutout for the Golden Frame
    # (62, 706, 1018, 1180)
    fx0, fy0, fx1, fy1 = 62, 706, 1018, 1180
    mask_cut = Image.new("L", (W, H), 255)
    m_draw = ImageDraw.Draw(mask_cut)
    m_draw.rounded_rectangle([fx0, fy0, fx1, fy1], radius=34, fill=0)
    
    r, g, b, a = im.split()
    new_a = Image.composite(a, Image.new("L", (W, H), 0), mask_cut)
    master = Image.merge("RGBA", (r, g, b, new_a))
    
    master.save(MASTER_916, "PNG")
    master.save(ARTIFACT_DIR / "bharatbeacon_master_916.png", "PNG")
    print(f"[OK] Master 9:16 template created at: {MASTER_916}")

if __name__ == "__main__":
    build_916_master()
