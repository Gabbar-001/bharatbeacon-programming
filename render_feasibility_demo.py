"""
render_feasibility_demo.py
Renders a live demonstration using the master overlay:
- Real article image placed under the golden frame.
- Real article headline centered on the yellow brush banner.
- Real spoken subtitles / key highlight in the dark blue ticker bar.
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

MASTER_PATH = Path("assets/templates/bharatbeacon_master.png")
ARTIFACT_DIR = Path("C:/Users/mr_un/.gemini/antigravity/brain/a40d7958-d2a6-434b-bf71-f01f0b882465")
OUTPUT_PATH = ARTIFACT_DIR / "feasibility_demo_master.png"

def get_font(size: int, bold: bool = True, impact: bool = False, italic: bool = False):
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

def render_demo():
    master = Image.open(MASTER_PATH).convert("RGBA")
    W, H = master.size
    
    # 1. Base Layer with Real Story Image
    canvas = Image.new("RGBA", (W, H), (10, 8, 20, 255))
    
    # Load actual news image
    img_candidates = list(Path("output/temp").glob("story_*.jpg"))
    if img_candidates:
        story_img = Image.open(img_candidates[0]).convert("RGBA")
    else:
        story_img = Image.new("RGBA", (868, 232), (40, 80, 160, 255))
        
    # Resize to fit the window exactly: (44, 338, 912, 570)
    box_w = 912 - 44
    box_h = 570 - 338
    
    # Fit & crop
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
    
    # Paste photo on canvas
    canvas.paste(cropped, (44, 338))
    
    # 2. Paste Master Overlay on top (golden frame with 3D bevels overlays seamlessly!)
    canvas.paste(master, (0, 0), mask=master)
    
    # 3. Render Real Headline
    draw = ImageDraw.Draw(canvas)
    headline_text = "SCIENTISTS UNVEIL 2,800-YEAR-OLD SIBERIAN SECRETS"
    f_head = get_font(38, bold=True, impact=True)
    lines = wrap_text(headline_text, f_head, 740, draw)
    
    total_h = len(lines) * 46
    start_y = 600 + (145 - total_h) // 2
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=f_head)
        lw = bbox[2] - bbox[0]
        lx = 480 - lw // 2
        draw.text((lx, start_y + i * 46), line, fill=(10, 10, 15), font=f_head)
        
    # 4. Render Real Subtitle Ticker
    subtitle_text = "Archaeologists discovered royal gold armor and untouched artifacts..."
    f_sub = get_font(21, bold=True, italic=True)
    draw.text((105, 792), subtitle_text, fill=(255, 255, 255), font=f_sub)
    
    canvas.save(OUTPUT_PATH, "PNG")
    print(f"[OK] Live feasibility demonstration generated at: {OUTPUT_PATH}")

if __name__ == "__main__":
    render_demo()
