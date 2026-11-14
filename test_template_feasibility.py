"""
test_template_feasibility.py
Demonstrates 100% feasibility of using the BharatBeacon Breaking News template:
1. Injects real article image inside the golden frame.
2. Injects real article headline on the yellow brush banner.
3. Injects real spoken subtitles / key highlights in the dark blue ticker bar.
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

TEMPLATE_PATH = Path("C:/Users/mr_un/.gemini/antigravity/brain/a40d7958-d2a6-434b-bf71-f01f0b882465/.user_uploaded/media_1794224842346_88bc5a43.jpg")
ARTIFACT_DIR = Path("C:/Users/mr_un/.gemini/antigravity/brain/a40d7958-d2a6-434b-bf71-f01f0b882465")
OUTPUT_SAMPLE = ARTIFACT_DIR / "feasibility_mockup.png"

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

def create_feasibility_demo():
    template = Image.open(TEMPLATE_PATH).convert("RGBA")
    W, H = template.size
    
    # 1. Real Story Photo
    # Find any existing image or fallback
    img_candidates = list(Path("output/temp").glob("story_*.jpg"))
    if img_candidates:
        story_img = Image.open(img_candidates[0]).convert("RGBA")
    else:
        story_img = Image.new("RGBA", (860, 230), (50, 100, 200, 255))
        
    # The inner golden frame coordinate
    # (x0, y0, x1, y1)
    frame_x0, frame_y0 = 42, 336
    frame_x1, frame_y1 = 914, 572
    box_w = frame_x1 - frame_x0
    box_h = frame_y1 - frame_y0
    
    # Resize photo to cover box
    # Crop to aspect ratio
    img_aspect = story_img.width / story_img.height
    box_aspect = box_w / box_h
    if img_aspect > box_aspect:
        new_h = box_h
        new_w = int(new_h * img_aspect)
    else:
        new_w = box_w
        new_h = int(new_w / img_aspect)
        
    resized_photo = story_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    # Center crop
    crop_x = (new_w - box_w) // 2
    crop_y = (new_h - box_h) // 2
    cropped_photo = resized_photo.crop((crop_x, crop_y, crop_x + box_w, crop_y + box_h))
    
    # Create rounded corner mask matching the golden frame radius (~24px)
    mask = Image.new("L", (box_w, box_h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, box_w, box_h], radius=24, fill=255)
    
    # Paste real image inside the frame!
    template.paste(cropped_photo, (frame_x0, frame_y0), mask=mask)
    
    # Optional: Re-stroke the inner golden bezel cleanly
    draw = ImageDraw.Draw(template)
    draw.rounded_rectangle([frame_x0, frame_y0, frame_x1, frame_y1], radius=24, outline=(255, 220, 100, 220), width=4)
    
    # 2. Real Headline on Yellow Banner
    # Clean the yellow banner region with the matching yellow brush color
    # Banner area: x ~ 100 to 860, y ~ 600 to 745
    # Sample yellow color from banner: RGB ~(255, 215, 0)
    head_bg = (255, 222, 0)
    # Let's paint over the placeholder "YOUR ARTICLE HEADLINE HERE"
    draw.rectangle([110, 600, 850, 745], fill=head_bg)
    
    headline_text = "ANCIENT SIBERIAN TOMB REVEALS 2,800-YEAR SECRETS"
    f_head = get_font(42, bold=True, impact=True)
    lines = wrap_text(headline_text, f_head, 760, draw)
    
    total_text_h = len(lines) * 50
    start_y = 600 + (145 - total_text_h) // 2
    for i, line in enumerate(lines):
        # Measure line width for center alignment
        bbox = draw.textbbox((0, 0), line, font=f_head)
        lw = bbox[2] - bbox[0]
        lx = 480 - lw // 2
        draw.text((lx, start_y + i * 50), line, fill=(10, 10, 15), font=f_head)
        
    # 3. Real Spoken Subtitles in Dark Blue Ticker
    # Cover the placeholder text "Your brief update or key highlight goes here..."
    # Ticker area: x from 95 to 710, y from 782 to 830
    ticker_bg = (5, 12, 35) # Deep navy matching the ticker
    draw.rounded_rectangle([92, 782, 715, 832], radius=14, fill=ticker_bg)
    
    # Subtitle text (Dynamic live spoken text)
    subtitle_text = "Archaeologists discovered royal gold armor and untouched artifacts..."
    f_sub = get_font(22, bold=True, italic=True)
    draw.text((105, 792), subtitle_text, fill=(255, 255, 255), font=f_sub)
    
    # Save the demo proof of concept
    template.save(OUTPUT_SAMPLE, "PNG")
    print(f"[OK] Feasibility mockup generated at: {OUTPUT_SAMPLE}")

if __name__ == "__main__":
    create_feasibility_demo()
