"""
create_clean_landscape_template.py
Creates the Full HD (1920x1080) landscape master template for full-length YouTube broadcasts:
1. Upscales to 1920x1080 Full HD with Lanczos anti-aliasing.
2. Clears the inner golden photo box with transparent alpha cutout so any 16:9 photo or video can sit underneath.
3. Cleans the yellow and red 3D headline banners.
4. Cleans the subtitle ticker bar.
5. Generates a live proof-of-concept sample (feasibility_demo_landscape.png).
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

TEMPLATE_PATH = Path("C:/Users/mr_un/.gemini/antigravity/brain/a40d7958-d2a6-434b-bf71-f01f0b882465/.user_uploaded/media_1794225005609_4d1d8927.jpg")
DEST_DIR = Path("assets/templates")
DEST_DIR.mkdir(parents=True, exist_ok=True)
MASTER_PNG = DEST_DIR / "bharatbeacon_master_landscape.png"
ARTIFACT_DIR = Path("C:/Users/mr_un/.gemini/antigravity/brain/a40d7958-d2a6-434b-bf71-f01f0b882465")
OUTPUT_DEMO = ARTIFACT_DIR / "feasibility_demo_landscape.png"

def get_font(size: int, bold: bool = True, impact: bool = False, italic: bool = False):
    import os
    if impact:
        path = "C:/Windows/Fonts/impact.ttf"
    elif bold and italic:
        path = "C:/Windows/Fonts/segoeuiz.ttf"
    elif bold:
        path = "C:/Windows/Fonts/segoeuib.ttf"
    elif italic:
        path = "C:/Windows/Fonts/segoeuii.ttf"
    else:
        path = "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(path):
        path = "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if (bbox[2] - bbox[0]) <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def build_landscape_master_and_demo():
    # 1. Load original 1024x576 and scale to standard 1920x1080
    raw = Image.open(TEMPLATE_PATH).convert("RGBA")
    im = raw.resize((1920, 1080), Image.Resampling.LANCZOS)
    W, H = im.size
    
    # 2. Clean Headline Banners
    # Yellow Banner: x: 40 to 800, y: 380 to 570
    # The text 'YOUR ARTICLE' is black, background is radiant yellow (RGB: 255, 220, 0)
    pixels = im.load()
    for y in range(380, 560):
        for x in range(40, 800):
            r, g, b, a = pixels[x, y]
            # Replace dark pixels of text
            if r > 180 and g > 150 and b < 100:
                pass # Already yellow
            elif (r + g + b) / 3 < 120 and x < 760: # Text pixel
                # Blend with yellow gradient
                pixels[x, y] = (255, 218, 0, 255)
                
    # Red Banner: x: 30 to 800, y: 555 to 720
    # The text 'HEADLINE HERE' is white, background is crimson red
    for y in range(560, 715):
        for x in range(30, 800):
            r, g, b, a = pixels[x, y]
            # White text: r>200, g>200, b>200
            if r > 180 and g > 180 and b > 180 and x < 770:
                # Replace with surrounding red gradient
                pixels[x, y] = (190, 15, 25, 255)

    # Slight blur on banners to eliminate text edges seamlessly
    y_blur = im.crop((50, 385, 780, 555)).filter(ImageFilter.GaussianBlur(4))
    im.paste(y_blur, (50, 385))
    r_blur = im.crop((40, 565, 780, 710)).filter(ImageFilter.GaussianBlur(4))
    im.paste(r_blur, (40, 565))

    # 3. Clean Subtitle Ticker Bar
    # x: 140 to 1270, y: 778 to 852
    ticker_w = 1270 - 140
    ticker_h = 852 - 778
    ticker_patch = Image.new("RGBA", (ticker_w, ticker_h), (6, 14, 38, 255))
    t_draw = ImageDraw.Draw(ticker_patch)
    for ty in range(ticker_h):
        t_draw.line([(0, ty), (ticker_w, ty)], fill=(8 + ty // 3, 16 + ty // 3, 45 + ty // 3, 255))
    im.paste(ticker_patch, (140, 778))

    # 4. Transparent Cutout for the Right Image Box
    # 1024x576 coords scaled by 1.875:
    # x: 848 to 1884, y: 229 to 733
    fx0, fy0, fx1, fy1 = 848, 229, 1884, 733
    mask_cut = Image.new("L", (W, H), 255)
    m_draw = ImageDraw.Draw(mask_cut)
    m_draw.rounded_rectangle([fx0, fy0, fx1, fy1], radius=34, fill=0)
    
    r, g, b, a = im.split()
    new_a = Image.composite(a, Image.new("L", (W, H), 0), mask_cut)
    master = Image.merge("RGBA", (r, g, b, new_a))
    
    master.save(MASTER_PNG, "PNG")
    master.save(ARTIFACT_DIR / "bharatbeacon_master_landscape.png", "PNG")
    print(f"[OK] Master Landscape Template created at: {MASTER_PNG}")

    # 5. NOW RENDER LIVE DEMONSTRATION WITH REAL DATA!
    canvas = Image.new("RGBA", (W, H), (10, 8, 22, 255))
    
    # Load actual news image
    img_candidates = list(Path("output/temp").glob("story_*.jpg"))
    if img_candidates:
        story_img = Image.open(img_candidates[0]).convert("RGBA")
    else:
        story_img = Image.new("RGBA", (1036, 504), (40, 80, 160, 255))
        
    box_w = fx1 - fx0
    box_h = fy1 - fy0
    
    # Scale and center crop photo to fill golden box exactly
    img_aspect = story_img.width / story_img.height
    box_aspect = box_w / box_h
    if img_aspect > box_aspect:
        nh = box_h
        nw = int(nh * img_aspect)
    else:
        nw = box_w
        nh = int(nw / img_aspect)
        
    resized_photo = story_img.resize((nw, nh), Image.Resampling.LANCZOS)
    cx = (nw - box_w) // 2
    cy = (nh - box_h) // 2
    cropped = resized_photo.crop((cx, cy, cx + box_w, cy + box_h))
    
    # Paste photo on base layer
    canvas.paste(cropped, (fx0, fy0))
    
    # Overlay the master broadcast graphics (golden frame with 3D bevels overlays seamlessly!)
    canvas.paste(master, (0, 0), mask=master)
    
    # Render Headline
    draw = ImageDraw.Draw(canvas)
    f_impact = get_font(52, bold=True, impact=True)
    f_sub = get_font(30, bold=True, italic=True)
    
    # Line 1 on Yellow Banner: Black Impact font
    line1 = "ANCIENT SIBERIAN TOMB"
    bbox1 = draw.textbbox((0, 0), line1, font=f_impact)
    lw1 = bbox1[2] - bbox1[0]
    draw.text((410 - lw1 // 2, 435), line1, fill=(10, 10, 15), font=f_impact)
    
    # Line 2 on Red Banner: Crisp White Impact font
    line2 = "2,800-YEAR-OLD SECRETS REVEALED"
    bbox2 = draw.textbbox((0, 0), line2, font=f_impact)
    lw2 = bbox2[2] - bbox2[0]
    draw.text((410 - lw2 // 2, 605), line2, fill=(255, 255, 255), font=f_impact)
    
    # Render Live Spoken Subtitle in Ticker Bar
    subtitle_text = "Archaeologists discovered royal gold armor and untouched ceremonial weapons..."
    draw.text((150, 792), subtitle_text, fill=(255, 255, 255), font=f_sub)
    
    canvas.save(OUTPUT_DEMO, "PNG")
    print(f"[OK] Live Landscape Demonstration created at: {OUTPUT_DEMO}")

if __name__ == "__main__":
    build_landscape_master_and_demo()
