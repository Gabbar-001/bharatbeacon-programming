"""
test_916_composition.py
Renders a live demonstration with the official 9:16 template:
- Real article image inside golden frame.
- Topic line in place of BREAKING NEWS.
- Headline auto-wrapped cleanly inside yellow brush banner.
- Subtitle rendered centered inside the dark blue ticker box.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

MASTER_PATH = Path("assets/templates/bharatbeacon_master_916.png")
ARTIFACT_DIR = Path("C:/Users/mr_un/.gemini/antigravity/brain/a40d7958-d2a6-434b-bf71-f01f0b882465")
OUTPUT_PATH = ARTIFACT_DIR / "mockup_916_perfect.png"

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

def render_916_demo():
    master = Image.open(MASTER_PATH).convert("RGBA")
    W, H = master.size # 1080, 1920
    
    canvas = Image.new("RGBA", (W, H), (10, 8, 22, 255))
    
    # 1. Real Story Photo
    fx0, fy0, fx1, fy1 = 62, 706, 1018, 1180
    box_w = fx1 - fx0
    box_h = fy1 - fy0
    
    img_candidates = list(Path("output/temp").glob("story_*.jpg"))
    if img_candidates:
        story_img = Image.open(img_candidates[0]).convert("RGBA")
    else:
        story_img = Image.new("RGBA", (box_w, box_h), (40, 80, 160, 255))
        
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
    
    # 2. Paste Master Template Over It
    canvas.paste(master, (0, 0), mask=master)
    
    draw = ImageDraw.Draw(canvas)
    
    # 3. Topic Line In Place of BREAKING NEWS:
    # Top 3D block (y: 410 to 495, center ~ 455): Category/Topic Hook
    # Bottom 3D block (y: 520 to 650, center ~ 585): Main Topic Subject
    f_topic_top = get_font(52, bold=True, impact=True)
    f_topic_bot = get_font(68, bold=True, impact=True)
    
    topic_line_top = "⚡ SPECIAL INVESTIGATION"
    topic_line_bot = "SIBERIAN TOMB DISCOVERY"
    
    bbox_t = draw.textbbox((0, 0), topic_line_top, font=f_topic_top)
    lw_t = bbox_t[2] - bbox_t[0]
    draw.text((540 - lw_t // 2, 430), topic_line_top, fill=(255, 255, 255), font=f_topic_top)
    
    bbox_b = draw.textbbox((0, 0), topic_line_bot, font=f_topic_bot)
    lw_b = bbox_b[2] - bbox_b[0]
    draw.text((540 - lw_b // 2, 545), topic_line_bot, fill=(255, 255, 255), font=f_topic_bot)
    
    # 4. Article Headline On Yellow Brush Banner (y: 1210 to 1455, height: 245)
    # Full article headline wrapped nicely
    headline = "Ancient Siberian Tomb Reveals Surprising Secrets of Cannabis Use 2,800 Years Ago"
    f_head = get_font(42, bold=True, impact=True)
    wrapped = wrap_text(headline.upper(), f_head, 880, draw)
    
    # If more than 3 lines, reduce font size
    if len(wrapped) > 3:
        f_head = get_font(36, bold=True, impact=True)
        wrapped = wrap_text(headline.upper(), f_head, 880, draw)
        
    line_h = 46 if f_head.size < 40 else 52
    total_h = len(wrapped) * line_h
    start_y = 1210 + (245 - total_h) // 2
    for i, line in enumerate(wrapped):
        bbox_l = draw.textbbox((0, 0), line, font=f_head)
        lw_l = bbox_l[2] - bbox_l[0]
        draw.text((540 - lw_l // 2, start_y + i * line_h), line, fill=(10, 10, 15), font=f_head)
        
    # 5. Subtitle In Blue Ticker Box (y: 1478 to 1563, height: 85, center ~ 1520)
    # Cleanly centered vertically inside the 85px box!
    f_sub = get_font(28, bold=True, italic=True)
    subtitle_demo = "burial rituals and animal sacrifices, offering rare insights..."
    # y=1498 places the 28pt text right in the vertical center of the 85px box!
    draw.text((155, 1498), subtitle_demo, fill=(255, 255, 255), font=f_sub)
    
    canvas.save(OUTPUT_PATH, "PNG")
    print(f"[OK] 9:16 Mockup rendered cleanly at: {OUTPUT_PATH}")

if __name__ == "__main__":
    render_916_demo()
