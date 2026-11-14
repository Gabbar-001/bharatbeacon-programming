"""
create_clean_master_template.py
Creates a high-precision, reusable broadcast template from the uploaded BharatBeacon image:
1. Cuts out the inner image box with transparency (alpha channel) so images/video sit under the frame.
2. Cleanly clears the headline banner placeholder while preserving the yellow brush background.
3. Cleanly clears the subtitle ticker placeholder while preserving the dark navy glow.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

TEMPLATE_PATH = Path("C:/Users/mr_un/.gemini/antigravity/brain/a40d7958-d2a6-434b-bf71-f01f0b882465/.user_uploaded/media_1794224842346_88bc5a43.jpg")
DEST_DIR = Path("assets/templates")
DEST_DIR.mkdir(parents=True, exist_ok=True)
MASTER_PNG = DEST_DIR / "bharatbeacon_master.png"

def make_master_template():
    im = Image.open(TEMPLATE_PATH).convert("RGBA")
    W, H = im.size
    
    # 1. Clean the Yellow Headline Banner
    # The text 'YOUR ARTICLE HEADLINE HERE' is black.
    # In the region x: 120-840, y: 600-745, pixels that are dark (black text) are replaced by the surrounding bright yellow.
    pixels = im.load()
    # Yellow background color average in that area: RGB(255, 218, 0)
    for y in range(595, 750):
        for x in range(110, 850):
            r, g, b, a = pixels[x, y]
            # If it's the black text (brightness < 120)
            if (r + g + b) / 3 < 135:
                # Replace with surrounding yellow gradient
                # Top is slightly more orange-yellow, bottom is vibrant yellow
                ratio = (y - 595) / 155
                yr = 255
                yg = int(200 + ratio * 25)
                yb = int(0 + ratio * 10)
                pixels[x, y] = (yr, yg, yb, 255)
                
    # Smooth the yellow banner region slightly to remove pixel seams
    box_blur = im.crop((110, 595, 850, 750)).filter(ImageFilter.GaussianBlur(3))
    im.paste(box_blur, (110, 595))
    
    # 2. Clean the Subtitle Ticker Bar
    # x: 92 to 720, y: 780 to 832
    # The ticker has a dark blue gradient with top specular line
    ticker_w = 720 - 92
    ticker_h = 832 - 780
    ticker_patch = Image.new("RGBA", (ticker_w, ticker_h), (8, 16, 42, 255))
    t_draw = ImageDraw.Draw(ticker_patch)
    # Draw subtle inner gradient
    for ty in range(ticker_h):
        alpha = int(ty / ticker_h * 15)
        t_draw.line([(0, ty), (ticker_w, ty)], fill=(12 + alpha, 22 + alpha, 55 + alpha, 255))
    im.paste(ticker_patch, (92, 780))
    
    # 3. Create Transparent Window for the Image
    # Golden frame inner coordinates: (44, 338, 912, 570)
    # We clear the alpha channel inside this rounded rect so images can sit UNDER the frame!
    mask_cut = Image.new("L", (W, H), 255)
    m_draw = ImageDraw.Draw(mask_cut)
    m_draw.rounded_rectangle([44, 338, 912, 570], radius=24, fill=0)
    
    # Apply mask to alpha channel
    r, g, b, a = im.split()
    # Combine original alpha with cut mask
    new_a = Image.composite(a, Image.new("L", (W, H), 0), mask_cut)
    master = Image.merge("RGBA", (r, g, b, new_a))
    
    master.save(MASTER_PNG, "PNG")
    # Also save to artifact directory for easy reference
    master.save("C:/Users/mr_un/.gemini/antigravity/brain/a40d7958-d2a6-434b-bf71-f01f0b882465/bharatbeacon_master.png", "PNG")
    print(f"[OK] Master template created: {MASTER_PNG}")

if __name__ == "__main__":
    make_master_template()
