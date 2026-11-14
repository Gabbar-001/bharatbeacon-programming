import os
import sys
import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.append(str(Path(__file__).resolve().parent))
import config

OUTPUT_DIR = config.OUTPUT_DIR / "samples" / "50_styles"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Collect real images from output/temp
temp_images = sorted(list(config.TEMP_DIR.glob("story_*.jpg")))
if not temp_images:
    temp_images = [config.ASSETS_DIR / "stock" / "science.jpg"]

def get_font(size: int, bold: bool = True, impact: bool = False):
    if impact:
        path = "C:/Windows/Fonts/impact.ttf"
    elif bold:
        path = "C:/Windows/Fonts/segoeuib.ttf"
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

# Sample headlines for variety
HEADLINES = [
    ("Ancient Siberian Tomb Reveals 2,800-Year-Old Secrets", "MYSTERY", "🏺"),
    ("Scientists Found 115-Million-Year-Old Dinosaur Blood in Fossil", "DISCOVERY", "🦖"),
    ("Ancient Ocean Full of Giant Predators Stuns Biologists", "OCEAN", "🌊"),
    ("Hidden Climate Superpower: Ocean Snow Absorbs Massive Carbon", "EARTH", "❄️"),
    ("Stupendously Large Primordial Black Holes Detected in Deep Space", "SPACE", "🕳️"),
    ("Why Most Cats Hate It When You Touch Their Belly or Tail", "PSYCHOLOGY", "🐾"),
    ("NASA Swift Observatory Captured Best Photos Before Burning Up", "ASTRONOMY", "🛰️"),
    ("Nuclear Blast Could Deflect Asteroids from Hitting Earth", "COSMOS", "💥"),
    ("Mysterious Gas Leaks Suggest Mars Is Still Volcanically Active", "PLANETARY", "🌋"),
    ("Astronomers Unveil Sharpest View of the Early Universe", "TELESCOPE", "🔭")
]

# 10 Distinct Color Themes (Each generates 5 unique layout styles)
THEMES = [
    {
        "name": "Cosmic Violet & Cyan",
        "bg_top": (10, 5, 25), "bg_bot": (35, 10, 70),
        "accent": (0, 242, 254), "accent2": (157, 78, 221),
        "card_bg": (20, 15, 45, 230), "pill_bg": (120, 40, 200),
        "tag": "NEBULA HUD"
    },
    {
        "name": "Sunset Synthwave & Hot Pink",
        "bg_top": (25, 5, 25), "bg_bot": (75, 15, 50),
        "accent": (255, 0, 127), "accent2": (255, 136, 0),
        "card_bg": (35, 12, 35, 235), "pill_bg": (230, 0, 100),
        "tag": "CYBER RETRO"
    },
    {
        "name": "Toxic Emerald & Acid Lime",
        "bg_top": (4, 20, 14), "bg_bot": (10, 50, 35),
        "accent": (191, 255, 0), "accent2": (0, 255, 178),
        "card_bg": (12, 32, 24, 235), "pill_bg": (0, 160, 100),
        "tag": "BIO MATRIX"
    },
    {
        "name": "Royal Cobalt & Molten Gold",
        "bg_top": (8, 16, 40), "bg_bot": (18, 32, 75),
        "accent": (255, 184, 0), "accent2": (59, 130, 246),
        "card_bg": (15, 28, 55, 235), "pill_bg": (217, 119, 6),
        "tag": "ROYAL LUXE"
    },
    {
        "name": "Magma Crimson & Solar Flare",
        "bg_top": (35, 5, 8), "bg_bot": (75, 15, 15),
        "accent": (255, 50, 50), "accent2": (255, 160, 30),
        "card_bg": (40, 12, 15, 240), "pill_bg": (220, 38, 38),
        "tag": "SOLAR PULSE"
    },
    {
        "name": "Holographic Iridescent",
        "bg_top": (15, 12, 35), "bg_bot": (40, 25, 75),
        "accent": (112, 214, 255), "accent2": (255, 112, 166),
        "card_bg": (28, 20, 50, 230), "pill_bg": (130, 90, 220),
        "tag": "VAPOR GLOW"
    },
    {
        "name": "Laser Cyan & Acid Blue",
        "bg_top": (5, 10, 25), "bg_bot": (10, 35, 60),
        "accent": (0, 229, 255), "accent2": (0, 255, 140),
        "card_bg": (10, 24, 45, 240), "pill_bg": (0, 140, 200),
        "tag": "TECHNO PULSE"
    },
    {
        "name": "Warm Terracotta & Plum",
        "bg_top": (30, 12, 35), "bg_bot": (65, 25, 45),
        "accent": (255, 179, 133), "accent2": (255, 107, 107),
        "card_bg": (38, 18, 36, 235), "pill_bg": (180, 50, 80),
        "tag": "SUNSET DUSK"
    },
    {
        "name": "Neo-Brutalist High-Contrast",
        "bg_top": (12, 14, 24), "bg_bot": (20, 25, 45),
        "accent": (255, 230, 0), "accent2": (43, 76, 255),
        "card_bg": (24, 28, 48, 245), "pill_bg": (255, 220, 0),
        "tag": "NEO POP"
    },
    {
        "name": "Obsidian Prism & Multi-Neon",
        "bg_top": (6, 8, 14), "bg_bot": (15, 18, 28),
        "accent": (255, 75, 140), "accent2": (0, 230, 255),
        "card_bg": (16, 20, 32, 240), "pill_bg": (70, 70, 220),
        "tag": "PRISM AURA"
    }
]

def render_sample(sample_id: int, theme: dict, headline_info: tuple, layout_variant: int) -> Path:
    W, H = 1080, 1920
    title, cat_name, icon = headline_info
    img_idx = (sample_id - 1) % len(temp_images)
    hero_path = temp_images[img_idx]

    # 1. Base Gradient Canvas
    canvas = Image.new("RGBA", (W, H), theme["bg_top"])
    draw = ImageDraw.Draw(canvas)

    # Gradient interpolation
    for y in range(H):
        r = float(y) / H
        c = (
            int(theme["bg_top"][0] * (1 - r) + theme["bg_bot"][0] * r),
            int(theme["bg_top"][1] * (1 - r) + theme["bg_bot"][1] * r),
            int(theme["bg_top"][2] * (1 - r) + theme["bg_bot"][2] * r),
            255
        )
        draw.line([(0, y), (W, y)], fill=c)

    # 2. Ambient Colorful Glow Aura behind hero image
    aura_y = 650
    for rad in range(500, 50, -25):
        alpha = int(45 * (1.0 - rad / 500.0))
        glow_col = (theme["accent"][0], theme["accent"][1], theme["accent"][2], alpha)
        draw.ellipse([(W//2 - rad, aura_y - rad), (W//2 + rad, aura_y + rad)], fill=glow_col)

    # Secondary glow
    for rad in range(400, 40, -20):
        alpha = int(35 * (1.0 - rad / 400.0))
        glow_col2 = (theme["accent2"][0], theme["accent2"][1], theme["accent2"][2], alpha)
        draw.ellipse([(W//2 - rad + 100, aura_y - rad + 80), (W//2 + rad + 100, aura_y + rad + 80)], fill=glow_col2)

    # 3. Outer Decorative Frame / Grid
    if layout_variant in (1, 3):
        draw.rectangle([(25, 25), (W - 25, H - 25)], outline=(theme["accent"][0], theme["accent"][1], theme["accent"][2], 120), width=3)
    elif layout_variant == 2:
        draw.line([(30, 30), (180, 30)], fill=theme["accent"], width=5)
        draw.line([(30, 30), (30, 180)], fill=theme["accent"], width=5)
        draw.line([(W - 30, 30), (W - 180, 30)], fill=theme["accent2"], width=5)
        draw.line([(W - 30, 30), (W - 30, 180)], fill=theme["accent2"], width=5)

    # 4. Top Header & Channel Identity
    draw.text((65, 75), f"{icon} INDIA HOURLY NEWS", font=get_font(32, bold=True), fill=(255, 255, 255))
    draw.text((W - 65, 75), f"#{sample_id:02d} // 50", font=get_font(30, bold=True), fill=theme["accent"], anchor="rt")
    draw.line([(65, 125), (W - 65, 125)], fill=(255, 255, 255, 40), width=2)

    # 5. Hero Image Placement (960x780)
    img_w, img_h = 960, 780
    img_x, img_y = (W - img_w) // 2, 175

    try:
        hero = Image.open(hero_path).convert("RGB").resize((img_w, img_h), Image.Resampling.LANCZOS)
    except Exception:
        hero = Image.new("RGB", (img_w, img_h), (30, 40, 60))

    if layout_variant in (0, 2):
        mask = Image.new("L", (img_w, img_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (img_w, img_h)], radius=28, fill=255)
        canvas.paste(hero, (img_x, img_y), mask)
        draw.rounded_rectangle([(img_x, img_y), (img_x + img_w, img_y + img_h)], radius=28, outline=theme["accent"], width=4)
    elif layout_variant == 1:
        canvas.paste(hero, (img_x, img_y))
        draw.rectangle([(img_x - 4, img_y - 4), (img_x + img_w + 4, img_y + img_h + 4)], outline=theme["accent"], width=6)
        draw.rectangle([(img_x + 8, img_y + 8), (img_x + img_w - 8, img_y + img_h - 8)], outline=theme["accent2"], width=2)
    else:
        mask = Image.new("L", (img_w, img_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (img_w, img_h)], radius=16, fill=255)
        canvas.paste(hero, (img_x, img_y), mask)
        draw.rounded_rectangle([(img_x, img_y), (img_x + img_w, img_y + img_h)], radius=16, outline=(255, 255, 255, 80), width=3)

    # 6. Floating Category Pill on Image corner
    pill_text = f"⚡ {cat_name} • {theme['tag']}"
    draw.rounded_rectangle([(img_x + 30, img_y + 30), (img_x + 460, img_y + 90)], radius=14, fill=theme["pill_bg"])
    pill_font_col = (0, 0, 0) if theme["pill_bg"] == (255, 220, 0) else (255, 255, 255)
    draw.text((img_x + 50, img_y + 45), pill_text, font=get_font(24, bold=True), fill=pill_font_col)

    # 7. Content Card Below Image
    card_w, card_h = 960, 520
    card_x, card_y = (W - card_w) // 2, img_y + img_h + 35
    draw.rounded_rectangle([(card_x, card_y), (card_x + card_w, card_y + card_h)], radius=24, fill=theme["card_bg"], outline=(theme["accent"][0], theme["accent"][1], theme["accent"][2], 120), width=2)
    draw.line([(card_x + 35, card_y), (card_x + 240, card_y)], fill=theme["accent"], width=6)

    # Theme & Style ID Label
    style_label = f"DESIGN STYLE #{sample_id:02d} : {theme['name'].upper()}"
    draw.text((card_x + 45, card_y + 40), style_label, font=get_font(22, bold=True), fill=theme["accent"])

    # Headline
    font_hl = get_font(44, bold=True, impact=(layout_variant == 1))
    wrapped = wrap_text(title, font_hl, card_w - 90, draw)
    text_y = card_y + 95
    for idx, line in enumerate(wrapped[:4]):
        if idx == 1 and layout_variant in (1, 3):
            # Highlight box behind line
            bbox = draw.textbbox((card_x + 45, text_y), line, font=font_hl)
            draw.rectangle([(bbox[0] - 6, bbox[1] - 4), (bbox[2] + 6, bbox[3] + 4)], fill=theme["accent"])
            txt_col = (0, 0, 0) if sum(theme["accent"]) > 400 else (255, 255, 255)
            draw.text((card_x + 45, text_y), line, font=font_hl, fill=txt_col)
        else:
            draw.text((card_x + 45, text_y), line, font=font_hl, fill=(255, 255, 255))
        text_y += 62

    # Bottom Animated Subtitle Preview Zone
    draw.rounded_rectangle([(W//2 - 320, H - 260), (W//2 + 320, H - 190)], radius=18, fill=(10, 15, 28, 240), outline=theme["accent2"], width=2)
    draw.text((W // 2, H - 225), "🔥 CANARY YELLOW SUBTITLE PREVIEW", font=get_font(24, bold=True), fill=(250, 204, 21), anchor="mm")

    out_path = OUTPUT_DIR / f"sample_{sample_id:02d}.png"
    canvas.save(out_path, "PNG")
    return out_path

def build_contact_sheets(all_samples):
    """Combines 50 samples into 5 overview collage boards (10 per sheet) for instant scanning."""
    print("[*] Creating 5 Overview Contact Sheets (10 designs per sheet)...")
    CONTACT_DIR = config.OUTPUT_DIR / "samples" / "contact_sheets"
    CONTACT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 5 sheets of 10 samples (2 columns x 5 rows)
    # Each thumbnail: 360 x 640
    thumb_w, thumb_h = 360, 640
    sheet_w = thumb_w * 2 + 60
    sheet_h = thumb_h * 5 + 120
    
    for sheet_idx in range(5):
        sheet_img = Image.new("RGB", (sheet_w, sheet_h), (12, 16, 28))
        draw = ImageDraw.Draw(sheet_img)
        
        start_id = sheet_idx * 10 + 1
        end_id = start_id + 9
        sheet_title = f"FRONTEND DESIGN COLLECTION: SAMPLES #{start_id:02d} - #{end_id:02d}"
        draw.text((sheet_w // 2, 45), sheet_title, font=get_font(32, bold=True), fill=(255, 255, 255), anchor="mm")
        
        for i in range(10):
            sid = start_id + i
            sample_file = all_samples[sid - 1]
            thumb = Image.open(sample_file).convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            
            col = i % 2
            row = i // 2
            x = 20 + col * (thumb_w + 20)
            y = 80 + row * (thumb_h + 15)
            
            sheet_img.paste(thumb, (x, y))
            draw.rectangle([(x, y), (x + thumb_w, y + thumb_h)], outline=(245, 158, 11), width=2)
            # Label
            draw.rectangle([(x + 10, y + 10), (x + 110, y + 45)], fill=(0, 0, 0, 220))
            draw.text((x + 60, y + 27), f"#{sid:02d}", font=get_font(22, bold=True), fill=(245, 158, 11), anchor="mm")
            
        sheet_path = CONTACT_DIR / f"contact_sheet_{sheet_idx + 1}.png"
        sheet_img.save(sheet_path, "JPEG", quality=90)
        print(f"    Saved Sheet {sheet_idx+1}: {sheet_path.name}")

def main():
    print("[*] Generating 50 Unique, Colorful Frontend Visual Designs...")
    all_sample_paths = []
    
    for i in range(1, 51):
        theme_idx = (i - 1) // 5
        layout_variant = (i - 1) % 5
        headline_idx = (i - 1) % len(HEADLINES)
        
        theme = THEMES[theme_idx]
        headline = HEADLINES[headline_idx]
        
        path = render_sample(i, theme, headline, layout_variant)
        all_sample_paths.append(path)
        if i % 10 == 0:
            print(f"    Rendered {i}/50 samples...")

    print("[OK] All 50 individual designs generated in output/samples/50_styles/")
    build_contact_sheets(all_sample_paths)

if __name__ == "__main__":
    main()
