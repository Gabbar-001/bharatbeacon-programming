import os
import sys
import shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.append(str(Path(__file__).resolve().parent))
import config

SAMPLE_DIR = config.OUTPUT_DIR / "samples"
SAMPLE_DIR.mkdir(parents=True, exist_ok=True)

SAMPLE_STORY = {
    "title": "Scientists Just Found Dinosaur Blood Preserved Inside a 115-Million-Year-Old Fossil",
    "category": "SCIENCE & DISCOVERY",
    "summary": "Fossilized soft tissue extracted in Brazil reveals intact red blood cells that survived against all known laws of biological decay.",
    "index": 1,
    "total": 10
}

IMG_SRC = config.TEMP_DIR / "story_2.jpg"
if not IMG_SRC.exists():
    IMG_SRC = config.ASSETS_DIR / "stock" / "science.jpg"
if not IMG_SRC.exists():
    IMG_SRC = config.ASSETS_DIR / "stock" / "top.jpg"

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

# ==============================================================================
# STYLE 1: CINEMATIC GLASSMORPHISM (Vox / Netflix Documentary Style)
# ==============================================================================
def render_style_1(is_shorts: bool = True) -> Path:
    W, H = (1080, 1920) if is_shorts else (1920, 1080)
    
    base = Image.open(IMG_SRC).convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
    blurred_bg = base.filter(ImageFilter.GaussianBlur(radius=45))
    
    overlay = Image.new("RGBA", (W, H), (8, 12, 24, 220))
    canvas = Image.alpha_composite(blurred_bg.convert("RGBA"), overlay)
    draw = ImageDraw.Draw(canvas)

    if is_shorts:
        # Header
        draw.text((60, 70), "🔴 INDIA HOURLY NEWS", font=get_font(32, bold=True), fill=(255, 255, 255))
        draw.text((W - 60, 70), "01 / 10", font=get_font(32, bold=True), fill=(245, 158, 11), anchor="rt")
        draw.line([(60, 120), (W - 60, 120)], fill=(255, 255, 255, 40), width=2)

        # Hero Image
        img_w, img_h = 960, 780
        img_x, img_y = (W - img_w) // 2, 170
        hero = Image.open(IMG_SRC).convert("RGB").resize((img_w, img_h), Image.Resampling.LANCZOS)
        mask = Image.new("L", (img_w, img_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (img_w, img_h)], radius=24, fill=255)
        canvas.paste(hero, (img_x, img_y), mask)
        draw.rounded_rectangle([(img_x, img_y), (img_x + img_w, img_y + img_h)], radius=24, outline=(255, 255, 255, 90), width=3)

        # Glass Info Card
        card_w, card_h = 960, 520
        card_x, card_y = (W - card_w) // 2, img_y + img_h + 35
        draw.rounded_rectangle([(card_x, card_y), (card_x + card_w, card_y + card_h)], radius=24, fill=(18, 26, 44, 235), outline=(255, 255, 255, 50), width=2)
        draw.line([(card_x + 30, card_y), (card_x + 200, card_y)], fill=(59, 130, 246), width=5)

        # Category Pill
        pill_text = f"● {SAMPLE_STORY['category']}"
        draw.rounded_rectangle([(card_x + 40, card_y + 35), (card_x + 360, card_y + 85)], radius=12, fill=(30, 58, 138, 200), outline=(96, 165, 250, 160), width=1)
        draw.text((card_x + 60, card_y + 48), pill_text, font=get_font(24, bold=True), fill=(191, 219, 254))

        # Headline
        font_hl = get_font(44, bold=True)
        wrapped = wrap_text(SAMPLE_STORY["title"], font_hl, card_w - 80, draw)
        hl_y = card_y + 115
        for line in wrapped[:4]:
            draw.text((card_x + 40, hl_y), line, font=font_hl, fill=(255, 255, 255))
            hl_y += 60

        draw.text((W // 2, H - 240), "✨ Canary Yellow Synced Subtitles Display Here", font=get_font(30, bold=True), fill=(250, 204, 21), anchor="mm")
    else:
        # Long-form 16:9 layout
        # Header
        draw.text((70, 45), "🔴 INDIA HOURLY NEWS", font=get_font(30, bold=True), fill=(255, 255, 255))
        draw.text((W - 70, 45), "STORY 01 OF 10", font=get_font(26, bold=True), fill=(245, 158, 11), anchor="rt")
        draw.line([(70, 90), (W - 70, 90)], fill=(255, 255, 255, 40), width=2)

        # Left Hero Image
        img_w, img_h = 960, 840
        img_x, img_y = 70, 130
        hero = Image.open(IMG_SRC).convert("RGB").resize((img_w, img_h), Image.Resampling.LANCZOS)
        mask = Image.new("L", (img_w, img_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (img_w, img_h)], radius=24, fill=255)
        canvas.paste(hero, (img_x, img_y), mask)
        draw.rounded_rectangle([(img_x, img_y), (img_x + img_w, img_y + img_h)], radius=24, outline=(255, 255, 255, 90), width=3)

        # Right Glass Card
        card_x = img_x + img_w + 40
        card_w = W - card_x - 70
        card_y = img_y
        card_h = img_h
        draw.rounded_rectangle([(card_x, card_y), (card_x + card_w, card_y + card_h)], radius=24, fill=(18, 26, 44, 235), outline=(255, 255, 255, 50), width=2)
        draw.line([(card_x + 40, card_y), (card_x + 220, card_y)], fill=(59, 130, 246), width=5)

        # Category Pill
        pill_text = f"● {SAMPLE_STORY['category']}"
        draw.rounded_rectangle([(card_x + 50, card_y + 60), (card_x + 380, card_y + 115)], radius=12, fill=(30, 58, 138, 200), outline=(96, 165, 250, 160), width=1)
        draw.text((card_x + 75, card_y + 75), pill_text, font=get_font(26, bold=True), fill=(191, 219, 254))

        # Headline
        font_hl = get_font(42, bold=True)
        wrapped = wrap_text(SAMPLE_STORY["title"], font_hl, card_w - 100, draw)
        hl_y = card_y + 160
        for line in wrapped[:4]:
            draw.text((card_x + 50, hl_y), line, font=font_hl, fill=(255, 255, 255))
            hl_y += 56

        # Summary
        hl_y += 30
        font_sm = get_font(26, bold=False)
        wrapped_sm = wrap_text(SAMPLE_STORY["summary"], font_sm, card_w - 100, draw)
        for line in wrapped_sm[:4]:
            draw.text((card_x + 50, hl_y), line, font=font_sm, fill=(203, 213, 225))
            hl_y += 40

    out_file = SAMPLE_DIR / f"style_1_glassmorphism_{'shorts' if is_shorts else 'longform'}.png"
    canvas.save(out_file, "PNG")
    return out_file

# ==============================================================================
# STYLE 2: NEO-POP VIRAL CREATOR (MrBeast / Daily Dose Style)
# ==============================================================================
def render_style_2(is_shorts: bool = True) -> Path:
    W, H = (1080, 1920) if is_shorts else (1920, 1080)
    canvas = Image.new("RGBA", (W, H), (12, 14, 22, 255))
    draw = ImageDraw.Draw(canvas)
    
    draw.rectangle([(20, 20), (W - 20, H - 20)], outline=(239, 68, 68), width=6)
    draw.rectangle([(28, 28), (W - 28, H - 28)], outline=(245, 158, 11), width=2)

    if is_shorts:
        draw.rectangle([(40, 50), (W - 40, 170)], fill=(220, 38, 38, 255))
        draw.text((W // 2, 110), "⚡ 10 UNBELIEVABLE HEADLINES ⚡", font=get_font(50, impact=True), fill=(255, 255, 255), anchor="mm")

        draw.rounded_rectangle([(W // 2 - 160, 200), (W // 2 + 160, 260)], radius=30, fill=(245, 158, 11))
        draw.text((W // 2, 230), "🔥 #1 OF 10", font=get_font(34, bold=True), fill=(0, 0, 0), anchor="mm")

        img_w, img_h = 960, 780
        img_x, img_y = (W - img_w) // 2, 290
        hero = Image.open(IMG_SRC).convert("RGB").resize((img_w, img_h), Image.Resampling.LANCZOS)
        canvas.paste(hero, (img_x, img_y))
        draw.rectangle([(img_x - 4, img_y - 4), (img_x + img_w + 4, img_y + img_h + 4)], outline=(245, 158, 11), width=5)

        box_w, box_h = 960, 460
        box_x, box_y = (W - box_w) // 2, img_y + img_h + 35
        draw.rounded_rectangle([(box_x, box_y), (box_x + box_w, box_y + box_h)], radius=16, fill=(24, 28, 42, 250), outline=(255, 255, 255, 50), width=3)
        draw.text((box_x + 30, box_y + 30), f"DISCOVERY // {SAMPLE_STORY['category']}", font=get_font(26, bold=True), fill=(248, 113, 113))

        font_hl = get_font(46, impact=True)
        wrapped = wrap_text(SAMPLE_STORY["title"].upper(), font_hl, box_w - 60, draw)
        text_y = box_y + 85
        for idx, line in enumerate(wrapped[:4]):
            if idx in (1, 2):
                bbox = draw.textbbox((box_x + 30, text_y), line, font=font_hl)
                draw.rectangle([(bbox[0] - 6, bbox[1] - 4), (bbox[2] + 6, bbox[3] + 4)], fill=(234, 179, 8))
                draw.text((box_x + 30, text_y), line, font=font_hl, fill=(0, 0, 0))
            else:
                draw.text((box_x + 30, text_y), line, font=font_hl, fill=(255, 255, 255))
            text_y += 65
    else:
        # Long-form 16:9
        draw.rectangle([(40, 40), (W - 40, 130)], fill=(220, 38, 38, 255))
        draw.text((W // 2, 85), "⚡ INDIA HOURLY NEWS: TOP 10 DEVELOPMENTS ⚡", font=get_font(44, impact=True), fill=(255, 255, 255), anchor="mm")

        img_w, img_h = 960, 840
        img_x, img_y = 60, 160
        hero = Image.open(IMG_SRC).convert("RGB").resize((img_w, img_h), Image.Resampling.LANCZOS)
        canvas.paste(hero, (img_x, img_y))
        draw.rectangle([(img_x - 4, img_y - 4), (img_x + img_w + 4, img_y + img_h + 4)], outline=(245, 158, 11), width=5)

        card_x = img_x + img_w + 40
        card_w = W - card_x - 60
        card_y, card_h = img_y, img_h
        draw.rounded_rectangle([(card_x, card_y), (card_x + card_w, card_y + card_h)], radius=16, fill=(24, 28, 42, 250), outline=(255, 255, 255, 50), width=3)

        draw.rounded_rectangle([(card_x + 40, card_y + 40), (card_x + 240, card_y + 95)], radius=20, fill=(245, 158, 11))
        draw.text((card_x + 140, card_y + 68), "🔥 #1 OF 10", font=get_font(28, bold=True), fill=(0, 0, 0), anchor="mm")

        draw.text((card_x + 40, card_y + 125), f"DISCOVERY // {SAMPLE_STORY['category']}", font=get_font(26, bold=True), fill=(248, 113, 113))

        font_hl = get_font(46, impact=True)
        wrapped = wrap_text(SAMPLE_STORY["title"].upper(), font_hl, card_w - 80, draw)
        text_y = card_y + 180
        for idx, line in enumerate(wrapped[:4]):
            if idx in (1, 2):
                bbox = draw.textbbox((card_x + 40, text_y), line, font=font_hl)
                draw.rectangle([(bbox[0] - 6, bbox[1] - 4), (bbox[2] + 6, bbox[3] + 4)], fill=(234, 179, 8))
                draw.text((card_x + 40, text_y), line, font=font_hl, fill=(0, 0, 0))
            else:
                draw.text((card_x + 40, text_y), line, font=font_hl, fill=(255, 255, 255))
            text_y += 65

        text_y += 30
        font_sm = get_font(26, bold=False)
        wrapped_sm = wrap_text(SAMPLE_STORY["summary"], font_sm, card_w - 80, draw)
        for line in wrapped_sm[:3]:
            draw.text((card_x + 40, text_y), line, font=font_sm, fill=(203, 213, 225))
            text_y += 38

    out_file = SAMPLE_DIR / f"style_2_neopop_{'shorts' if is_shorts else 'longform'}.png"
    canvas.save(out_file, "PNG")
    return out_file

# ==============================================================================
# STYLE 3: DARK EDITORIAL MINIMALIST (NatGeo / Wired / BBC Style)
# ==============================================================================
def render_style_3(is_shorts: bool = True) -> Path:
    W, H = (1080, 1920) if is_shorts else (1920, 1080)
    canvas = Image.new("RGBA", (W, H), (9, 11, 15, 255))
    draw = ImageDraw.Draw(canvas)

    if is_shorts:
        draw.text((60, 75), "INDIA HOURLY", font=get_font(30, bold=True), fill=(255, 255, 255))
        draw.text((260, 78), "|  SPECIAL REPORT", font=get_font(22, bold=False), fill=(148, 163, 184))
        draw.text((W - 60, 78), "STORY 01 OF 10", font=get_font(22, bold=True), fill=(217, 119, 6), anchor="rt")
        draw.line([(60, 125), (W - 60, 125)], fill=(30, 41, 59), width=1)

        img_w, img_h = 960, 840
        img_x, img_y = (W - img_w) // 2, 175
        hero = Image.open(IMG_SRC).convert("RGB").resize((img_w, img_h), Image.Resampling.LANCZOS)
        mask = Image.new("L", (img_w, img_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (img_w, img_h)], radius=16, fill=255)
        canvas.paste(hero, (img_x, img_y), mask)
        draw.rounded_rectangle([(img_x, img_y), (img_x + img_w, img_y + img_h)], radius=16, outline=(51, 65, 85), width=2)

        text_x = 60
        text_y = img_y + img_h + 45
        draw.text((text_x, text_y), SAMPLE_STORY["category"].upper(), font=get_font(22, bold=True), fill=(245, 158, 11))
        draw.line([(text_x, text_y + 35), (text_x + 120, text_y + 35)], fill=(245, 158, 11), width=3)

        text_y += 55
        font_hl = get_font(42, bold=True)
        wrapped = wrap_text(SAMPLE_STORY["title"], font_hl, W - 120, draw)
        for line in wrapped[:4]:
            draw.text((text_x, text_y), line, font=font_hl, fill=(255, 255, 255))
            text_y += 58

        text_y += 15
        font_sm = get_font(24, bold=False)
        wrapped_sm = wrap_text(SAMPLE_STORY["summary"], font_sm, W - 120, draw)
        for line in wrapped_sm[:2]:
            draw.text((text_x, text_y), line, font=font_sm, fill=(148, 163, 184))
            text_y += 34
    else:
        # Long-form 16:9
        draw.text((70, 50), "INDIA HOURLY NEWS", font=get_font(28, bold=True), fill=(255, 255, 255))
        draw.text((360, 52), "|  GLOBAL SCIENCE & DISCOVERY ARCHIVE", font=get_font(22, bold=False), fill=(148, 163, 184))
        draw.text((W - 70, 52), "DISPATCH 01 OF 10", font=get_font(22, bold=True), fill=(217, 119, 6), anchor="rt")
        draw.line([(70, 95), (W - 70, 95)], fill=(30, 41, 59), width=1)

        img_w, img_h = 980, 860
        img_x, img_y = 70, 135
        hero = Image.open(IMG_SRC).convert("RGB").resize((img_w, img_h), Image.Resampling.LANCZOS)
        mask = Image.new("L", (img_w, img_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (img_w, img_h)], radius=16, fill=255)
        canvas.paste(hero, (img_x, img_y), mask)
        draw.rounded_rectangle([(img_x, img_y), (img_x + img_w, img_y + img_h)], radius=16, outline=(51, 65, 85), width=2)

        text_x = img_x + img_w + 60
        text_y = img_y + 40
        draw.text((text_x, text_y), SAMPLE_STORY["category"].upper(), font=get_font(24, bold=True), fill=(245, 158, 11))
        draw.line([(text_x, text_y + 35), (text_x + 140, text_y + 35)], fill=(245, 158, 11), width=3)

        text_y += 65
        font_hl = get_font(42, bold=True)
        wrapped = wrap_text(SAMPLE_STORY["title"], font_hl, W - text_x - 70, draw)
        for line in wrapped[:4]:
            draw.text((text_x, text_y), line, font=font_hl, fill=(255, 255, 255))
            text_y += 56

        text_y += 35
        font_sm = get_font(26, bold=False)
        wrapped_sm = wrap_text(SAMPLE_STORY["summary"], font_sm, W - text_x - 70, draw)
        for line in wrapped_sm[:4]:
            draw.text((text_x, text_y), line, font=font_sm, fill=(148, 163, 184))
            text_y += 38

    out_file = SAMPLE_DIR / f"style_3_editorial_{'shorts' if is_shorts else 'longform'}.png"
    canvas.save(out_file, "PNG")
    return out_file

# ==============================================================================
# STYLE 4: CYBER TECH HUD NEWSROOM (Futuristic HUD Theme)
# ==============================================================================
def render_style_4(is_shorts: bool = True) -> Path:
    W, H = (1080, 1920) if is_shorts else (1920, 1080)
    canvas = Image.new("RGBA", (W, H), (6, 10, 20, 255))
    draw = ImageDraw.Draw(canvas)

    grid_spacing = 90
    for x in range(0, W, grid_spacing):
        draw.line([(x, 0), (x, H)], fill=(15, 28, 54, 80), width=1)
    for y in range(0, H, grid_spacing):
        draw.line([(0, y), (W, y)], fill=(15, 28, 54, 80), width=1)

    if is_shorts:
        draw.text((60, 60), "◈ SYSTEM ARCHIVE", font=get_font(26, bold=True), fill=(0, 242, 254))
        draw.text((W - 60, 60), "SEC-01 // 10", font=get_font(26, bold=True), fill=(157, 78, 221), anchor="rt")
        draw.line([(60, 105), (W - 60, 105)], fill=(0, 242, 254, 100), width=2)

        img_w, img_h = 960, 780
        img_x, img_y = (W - img_w) // 2, 160
        hero = Image.open(IMG_SRC).convert("RGB").resize((img_w, img_h), Image.Resampling.LANCZOS)
        canvas.paste(hero, (img_x, img_y))

        brk_len = 50
        brk_col = (0, 242, 254)
        draw.line([(img_x - 10, img_y - 10), (img_x - 10 + brk_len, img_y - 10)], fill=brk_col, width=4)
        draw.line([(img_x - 10, img_y - 10), (img_x - 10, img_y - 10 + brk_len)], fill=brk_col, width=4)
        draw.line([(img_x + img_w + 10, img_y - 10), (img_x + img_w + 10 - brk_len, img_y - 10)], fill=brk_col, width=4)
        draw.line([(img_x + img_w + 10, img_y - 10), (img_x + img_w + 10 - brk_len, img_y - 10)], fill=brk_col, width=4)
        draw.line([(img_x - 10, img_y + img_h + 10), (img_x - 10 + brk_len, img_y + img_h + 10)], fill=brk_col, width=4)
        draw.line([(img_x - 10, img_y + img_h + 10), (img_x - 10, img_y + img_h + 10 - brk_len)], fill=brk_col, width=4)
        draw.line([(img_x + img_w + 10, img_y + img_h + 10), (img_x + img_w + 10 - brk_len, img_y + img_h + 10)], fill=brk_col, width=4)
        draw.line([(img_x + img_w + 10, img_y + img_h + 10), (img_x + img_w + 10, img_y + img_h + 10 - brk_len)], fill=brk_col, width=4)

        box_w, box_h = 960, 480
        box_x, box_y = (W - box_w) // 2, img_y + img_h + 40
        draw.rectangle([(box_x, box_y), (box_x + box_w, box_y + box_h)], fill=(10, 18, 36, 235), outline=(0, 242, 254, 120), width=2)
        draw.rectangle([(box_x, box_y), (box_x + 180, box_y + 8)], fill=(0, 242, 254))

        draw.text((box_x + 35, box_y + 35), f"ANOMALY // {SAMPLE_STORY['category']}", font=get_font(24, bold=True), fill=(0, 242, 254))

        font_hl = get_font(42, bold=True)
        wrapped = wrap_text(SAMPLE_STORY["title"], font_hl, box_w - 70, draw)
        text_y = box_y + 90
        for line in wrapped[:4]:
            draw.text((box_x + 35, text_y), line, font=font_hl, fill=(255, 255, 255))
            text_y += 58
    else:
        # Long-form 16:9
        draw.text((70, 45), "◈ QUANTUM TELEMETRY FEED", font=get_font(26, bold=True), fill=(0, 242, 254))
        draw.text((W - 70, 45), "ANOMALY 01 // 10", font=get_font(26, bold=True), fill=(157, 78, 221), anchor="rt")
        draw.line([(70, 90), (W - 70, 90)], fill=(0, 242, 254, 100), width=2)

        img_w, img_h = 960, 840
        img_x, img_y = 70, 130
        hero = Image.open(IMG_SRC).convert("RGB").resize((img_w, img_h), Image.Resampling.LANCZOS)
        canvas.paste(hero, (img_x, img_y))

        brk_len = 50
        brk_col = (0, 242, 254)
        draw.line([(img_x - 8, img_y - 8), (img_x - 8 + brk_len, img_y - 8)], fill=brk_col, width=4)
        draw.line([(img_x - 8, img_y - 8), (img_x - 8, img_y - 8 + brk_len)], fill=brk_col, width=4)
        draw.line([(img_x + img_w + 8, img_y - 8), (img_x + img_w + 8 - brk_len, img_y - 8)], fill=brk_col, width=4)
        draw.line([(img_x + img_w + 8, img_y - 8), (img_x + img_w + 8, img_y - 8 + brk_len)], fill=brk_col, width=4)
        draw.line([(img_x - 8, img_y + img_h + 8), (img_x - 8 + brk_len, img_y + img_h + 8)], fill=brk_col, width=4)
        draw.line([(img_x - 8, img_y + img_h + 8), (img_x - 8, img_y + img_h + 8 - brk_len)], fill=brk_col, width=4)
        draw.line([(img_x + img_w + 8, img_y + img_h + 8), (img_x + img_w + 8 - brk_len, img_y + img_h + 8)], fill=brk_col, width=4)
        draw.line([(img_x + img_w + 8, img_y + img_h + 8), (img_x + img_w + 8, img_y + img_h + 8 - brk_len)], fill=brk_col, width=4)

        card_x = img_x + img_w + 40
        card_w = W - card_x - 70
        card_y, card_h = img_y, img_h
        draw.rectangle([(card_x, card_y), (card_x + card_w, card_y + card_h)], fill=(10, 18, 36, 235), outline=(0, 242, 254, 120), width=2)
        draw.rectangle([(card_x, card_y), (card_x + 220, card_y + 8)], fill=(0, 242, 254))

        draw.text((card_x + 45, card_y + 50), f"ANOMALY // {SAMPLE_STORY['category']}", font=get_font(26, bold=True), fill=(0, 242, 254))

        font_hl = get_font(42, bold=True)
        wrapped = wrap_text(SAMPLE_STORY["title"], font_hl, card_w - 90, draw)
        text_y = card_y + 115
        for line in wrapped[:4]:
            draw.text((card_x + 45, text_y), line, font=font_hl, fill=(255, 255, 255))
            text_y += 56

        text_y += 30
        font_sm = get_font(26, bold=False)
        wrapped_sm = wrap_text(SAMPLE_STORY["summary"], font_sm, card_w - 90, draw)
        for line in wrapped_sm[:4]:
            draw.text((card_x + 45, text_y), line, font=font_sm, fill=(203, 213, 225))
            text_y += 38

    out_file = SAMPLE_DIR / f"style_4_cyber_hud_{'shorts' if is_shorts else 'longform'}.png"
    canvas.save(out_file, "PNG")
    return out_file

def generate_all_samples():
    print("[*] Rendering 4 Styles for both Shorts (9:16) and Long-form (16:9)...")
    for is_s in [True, False]:
        render_style_1(is_shorts=is_s)
        render_style_2(is_shorts=is_s)
        render_style_3(is_shorts=is_s)
        render_style_4(is_shorts=is_s)
    print("[OK] All 8 sample images rendered in output/samples/")

if __name__ == "__main__":
    generate_all_samples()
