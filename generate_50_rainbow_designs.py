"""
generate_50_rainbow_designs.py
Generates 50 TRULY UNIQUE, FULL-SPECTRUM RAINBOW frontend visual designs for YouTube Shorts (1080x1920).
Every single frame incorporates multiple/all colors of the rainbow (Red, Orange, Yellow, Green, Cyan, Blue, Violet, Pink)
with 50 completely distinct layout structures, compositions, and graphical styles.
Also outputs 5 overview contact sheets (10 designs per sheet).
"""

import os
import sys
import math
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.append(str(Path(__file__).resolve().parent))
import config

OUTPUT_DIR = config.OUTPUT_DIR / "samples" / "50_rainbow"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
CONTACT_DIR = config.OUTPUT_DIR / "samples" / "contact_sheets_rainbow"
CONTACT_DIR.mkdir(parents=True, exist_ok=True)

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

# Full 8-Color Rainbow Spectrum
RAINBOW_COLORS = [
    (255, 30, 80),    # Crimson Pink
    (255, 105, 0),   # Radiant Orange
    (255, 215, 0),   # Solar Yellow
    (0, 235, 110),   # Electric Lime Green
    (0, 240, 255),   # Laser Cyan
    (30, 110, 255),  # Deep Royal Blue
    (150, 45, 255),  # Vivid Purple
    (255, 20, 190)   # Hot Magenta
]

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

def create_rainbow_strip_image(width, height, horizontal=True):
    """Creates a smooth interpolated rainbow gradient surface."""
    im = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(im)
    steps = len(RAINBOW_COLORS)
    if horizontal:
        seg_w = width / (steps - 1)
        for x in range(width):
            t = (x / width) * (steps - 1)
            idx = int(t)
            idx = min(idx, steps - 2)
            ratio = t - idx
            c1 = RAINBOW_COLORS[idx]
            c2 = RAINBOW_COLORS[idx + 1]
            r = int(c1[0] * (1 - ratio) + c2[0] * ratio)
            g = int(c1[1] * (1 - ratio) + c2[1] * ratio)
            b = int(c1[2] * (1 - ratio) + c2[2] * ratio)
            draw.line([(x, 0), (x, height)], fill=(r, g, b, 255))
    else:
        seg_h = height / (steps - 1)
        for y in range(height):
            t = (y / height) * (steps - 1)
            idx = int(t)
            idx = min(idx, steps - 2)
            ratio = t - idx
            c1 = RAINBOW_COLORS[idx]
            c2 = RAINBOW_COLORS[idx + 1]
            r = int(c1[0] * (1 - ratio) + c2[0] * ratio)
            g = int(c1[1] * (1 - ratio) + c2[1] * ratio)
            b = int(c1[2] * (1 - ratio) + c2[2] * ratio)
            draw.line([(0, y), (width, y)], fill=(r, g, b, 255))
    return im

def draw_rainbow_frame(draw, bbox, width=10, radius=24):
    """Draws a rounded frame with rainbow segments along its perimeter."""
    x0, y0, x1, y1 = bbox
    # Draw 4 sides with gradient lines
    c_count = len(RAINBOW_COLORS)
    # Top
    step_w = (x1 - x0) / c_count
    for i in range(c_count):
        draw.line([(x0 + i * step_w, y0), (x0 + (i + 1) * step_w, y0)], fill=RAINBOW_COLORS[i], width=width)
    # Right
    step_h = (y1 - y0) / c_count
    for i in range(c_count):
        draw.line([(x1, y0 + i * step_h), (x1, y0 + (i + 1) * step_h)], fill=RAINBOW_COLORS[(i + 2) % c_count], width=width)
    # Bottom
    for i in range(c_count):
        draw.line([(x1 - i * step_w, y1), (x1 - (i + 1) * step_w, y1)], fill=RAINBOW_COLORS[(i + 4) % c_count], width=width)
    # Left
    for i in range(c_count):
        draw.line([(x0, y1 - i * step_h), (x0, y1 - (i + 1) * step_h)], fill=RAINBOW_COLORS[(i + 6) % c_count], width=width)

def draw_rainbow_bar(draw, x, y, width, height=8):
    """Draws a horizontal full-spectrum rainbow bar."""
    step = width / len(RAINBOW_COLORS)
    for i, col in enumerate(RAINBOW_COLORS):
        draw.rectangle([x + i * step, y, x + (i + 1) * step, y + height], fill=col)

def draw_rainbow_badge(canvas, text, x, y, font, category="DISCOVERY"):
    draw = ImageDraw.Draw(canvas)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pad_x, pad_y = 28, 12
    bx0, by0, bx1, by1 = x, y, x + tw + pad_x * 2, y + th + pad_y * 2
    
    # Rainbow outer stroke
    draw_rainbow_bar(draw, bx0, by0, bx1 - bx0, height=4)
    draw_rainbow_bar(draw, bx0, by1 - 4, bx1 - bx0, height=4)
    # Dark card
    draw.rounded_rectangle([bx0, by0 + 4, bx1, by1 - 4], radius=12, fill=(15, 12, 28, 240))
    # Text
    draw.text((x + pad_x, y + pad_y), text, fill=(255, 255, 255), font=font)

def create_base_canvas(img_path):
    """Creates base 1080x1920 canvas with dark starry/nebula gradient and blurred photo backing."""
    canvas = Image.new("RGBA", (1080, 1920), (10, 8, 22, 255))
    try:
        raw_img = Image.open(img_path).convert("RGBA")
        # Blurred atmospheric background
        bg_blur = raw_img.resize((1080, 1920)).filter(ImageFilter.GaussianBlur(55))
        # Dim the background to 30% brightness so rainbow pops intensely
        dimmer = Image.new("RGBA", (1080, 1920), (8, 6, 18, 190))
        canvas.paste(bg_blur, (0, 0))
        canvas.paste(dimmer, (0, 0), mask=dimmer)
    except Exception:
        pass
    return canvas

def load_focal_image(img_path, target_size=(880, 880)):
    try:
        raw = Image.open(img_path).convert("RGBA")
        raw = raw.resize(target_size, Image.Resampling.LANCZOS)
        return raw
    except Exception:
        im = Image.new("RGBA", target_size, (40, 40, 60, 255))
        return im

# --- 50 INDIVIDUAL UNIQUE LAYOUT GENERATORS ---
def generate_sample(index: int, headline_info, img_path):
    headline, cat, icon = headline_info
    canvas = create_base_canvas(img_path)
    draw = ImageDraw.Draw(canvas)
    
    # Fonts
    f_num = get_font(42, bold=True, impact=True)
    f_badge = get_font(34, bold=True)
    f_head = get_font(52, bold=True)
    f_impact = get_font(60, bold=True, impact=True)
    f_meta = get_font(28, bold=False)
    
    # Design #01: Rainbow Conic Aura HUD
    if index == 1:
        # Full circular rainbow halo
        cx, cy = 540, 780
        focal = load_focal_image(img_path, (760, 760))
        # Draw multiple concentric rainbow rings
        for r_idx, col in enumerate(RAINBOW_COLORS):
            radius = 390 + r_idx * 12
            draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], outline=col, width=6)
        # Paste focal image with circle mask
        mask = Image.new("L", (760, 760), 0)
        ImageDraw.Draw(mask).ellipse([0, 0, 760, 760], fill=255)
        canvas.paste(focal, (cx - 380, cy - 380), mask=mask)
        # Floating Rainbow HUD brackets
        draw_rainbow_bar(draw, 140, 220, 800, height=8)
        draw.text((140, 160), f"⚡ RAINBOW AURA // {cat}", fill=(255, 255, 255), font=f_badge)
        # Headline Box
        draw.rounded_rectangle([100, 1260, 980, 1720], radius=30, fill=(15, 12, 30, 235), outline=(0, 240, 255), width=3)
        draw_rainbow_bar(draw, 100, 1260, 880, height=10)
        lines = wrap_text(headline, f_head, 800, draw)
        for i, line in enumerate(lines):
            draw.text((140, 1310 + i * 70), line, fill=(255, 255, 255), font=f_head)
        draw.text((140, 1620), "TAP TO DISCOVER MORE  ➤", fill=RAINBOW_COLORS[2], font=f_meta)

    # Design #02: Horizontal Spectral Prism Ribbon
    elif index == 2:
        # Top half image
        focal = load_focal_image(img_path, (960, 680))
        canvas.paste(focal, (60, 260))
        # 7-stripe thick rainbow prism ribbon crossing the middle
        y_ribbon = 960
        for i, col in enumerate(RAINBOW_COLORS):
            draw.rectangle([0, y_ribbon + i * 16, 1080, y_ribbon + (i + 1) * 16], fill=col)
        # Badge
        draw_rainbow_badge(canvas, f"🔥 BREAKING // {cat}", 80, 160, f_badge)
        # Bottom glass container
        draw.rounded_rectangle([60, 1140, 1020, 1720], radius=28, fill=(12, 10, 25, 240))
        draw_rainbow_frame(draw, (60, 1140, 1020, 1720), width=6)
        lines = wrap_text(headline, f_impact, 880, draw)
        for i, line in enumerate(lines):
            c = RAINBOW_COLORS[i % len(RAINBOW_COLORS)]
            draw.text((100, 1220 + i * 80), line, fill=c, font=f_impact)

    # Design #03: Cyberpunk Rainbow Neon Matrix
    elif index == 3:
        # Grid lines on entire canvas cycling rainbow
        for gy in range(0, 1920, 60):
            c = RAINBOW_COLORS[(gy // 60) % len(RAINBOW_COLORS)]
            draw.line([(0, gy), (1080, gy)], fill=(*c[:3], 60), width=2)
        focal = load_focal_image(img_path, (840, 720))
        canvas.paste(focal, (120, 400))
        draw_rainbow_frame(draw, (115, 395, 965, 1125), width=8)
        # Neon Corner reticles in 4 distinct rainbow colors
        draw.line([(90, 370), (160, 370)], fill=RAINBOW_COLORS[0], width=8)
        draw.line([(90, 370), (90, 440)], fill=RAINBOW_COLORS[0], width=8)
        draw.line([(990, 370), (920, 370)], fill=RAINBOW_COLORS[2], width=8)
        draw.line([(990, 370), (990, 440)], fill=RAINBOW_COLORS[2], width=8)
        draw.line([(90, 1150), (160, 1150)], fill=RAINBOW_COLORS[4], width=8)
        draw.line([(90, 1150), (90, 1080)], fill=RAINBOW_COLORS[4], width=8)
        draw.line([(990, 1150), (920, 1150)], fill=RAINBOW_COLORS[6], width=8)
        draw.line([(990, 1150), (990, 1080)], fill=RAINBOW_COLORS[6], width=8)
        # Headline
        draw.rounded_rectangle([100, 1240, 980, 1700], radius=20, fill=(10, 8, 20, 245), outline=RAINBOW_COLORS[4], width=4)
        draw_rainbow_bar(draw, 100, 1240, 880, height=12)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((130, 1310 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #04: Diagonal Rainbow Light Blades
    elif index == 4:
        # Draw 8 diagonal multi-color slashes behind photo
        for i, col in enumerate(RAINBOW_COLORS):
            offset = -300 + i * 220
            draw.polygon([(offset, 0), (offset + 120, 0), (offset + 700, 1920), (offset + 580, 1920)], fill=(*col[:3], 140))
        focal = load_focal_image(img_path, (860, 680))
        canvas.paste(focal, (110, 440))
        draw_rainbow_bar(draw, 110, 430, 860, height=10)
        draw_rainbow_bar(draw, 110, 1120, 860, height=10)
        # Headline Card
        draw.rounded_rectangle([110, 1220, 970, 1720], radius=26, fill=(15, 12, 28, 240))
        draw_rainbow_frame(draw, (110, 1220, 970, 1720), width=6)
        lines = wrap_text(headline, f_head, 800, draw)
        for i, line in enumerate(lines):
            draw.text((140, 1290 + i * 72), line, fill=(255, 255, 255), font=f_head)

    # Design #05: Rainbow Equalizer Visualizer
    elif index == 5:
        focal = load_focal_image(img_path, (920, 720))
        canvas.paste(focal, (80, 320))
        draw_rainbow_frame(draw, (75, 315, 1005, 1045), width=8)
        # Multi-color audio equalizer bars across width
        num_bars = 32
        bar_w = 26
        for b in range(num_bars):
            col = RAINBOW_COLORS[b % len(RAINBOW_COLORS)]
            bar_h = 40 + int(math.sin(b * 0.4) * 60 + 70)
            bx = 80 + b * 29
            draw.rounded_rectangle([bx, 1140 - bar_h, bx + bar_w, 1140], radius=6, fill=col)
        # Headline
        draw.rounded_rectangle([80, 1220, 1000, 1720], radius=24, fill=(10, 8, 22, 240), outline=(255, 255, 255), width=3)
        draw_rainbow_bar(draw, 80, 1220, 920, height=8)
        lines = wrap_text(headline, f_head, 840, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #06: Double Rainbow Chromatic Halo
    elif index == 6:
        # Two large overlapping glowing circles
        cx1, cy1 = 440, 680
        cx2, cy2 = 640, 780
        draw.ellipse([cx1 - 380, cy1 - 380, cx1 + 380, cy1 + 380], outline=RAINBOW_COLORS[0], width=12)
        draw.ellipse([cx1 - 360, cy1 - 360, cx1 + 360, cy1 + 360], outline=RAINBOW_COLORS[1], width=10)
        draw.ellipse([cx1 - 340, cy1 - 340, cx1 + 340, cy1 + 340], outline=RAINBOW_COLORS[2], width=8)
        draw.ellipse([cx2 - 380, cy2 - 380, cx2 + 380, cy2 + 380], outline=RAINBOW_COLORS[4], width=12)
        draw.ellipse([cx2 - 360, cy2 - 360, cx2 + 360, cy2 + 360], outline=RAINBOW_COLORS[6], width=10)
        draw.ellipse([cx2 - 340, cy2 - 340, cx2 + 340, cy2 + 340], outline=RAINBOW_COLORS[7], width=8)
        focal = load_focal_image(img_path, (800, 680))
        canvas.paste(focal, (140, 420))
        draw_rainbow_frame(draw, (140, 420, 940, 1100), width=6)
        # Headline Box
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=32, fill=(12, 10, 24, 240))
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_impact, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1290 + i * 85), line, fill=RAINBOW_COLORS[(i * 2) % len(RAINBOW_COLORS)], font=f_impact)

    # Design #07: Stained-Glass Rainbow Mosaic Grid
    elif index == 7:
        # 8 vibrant geometric stained glass wedges around top
        for idx, col in enumerate(RAINBOW_COLORS):
            x_m = idx * 135
            draw.polygon([(x_m, 0), (x_m + 135, 0), (x_m + 70, 240)], fill=(*col[:3], 180))
            draw.polygon([(x_m, 1920), (x_m + 135, 1920), (x_m + 70, 1760)], fill=(*col[:3], 180))
        focal = load_focal_image(img_path, (860, 720))
        canvas.paste(focal, (110, 360))
        draw_rainbow_frame(draw, (105, 355, 975, 1085), width=10)
        draw.rounded_rectangle([100, 1180, 980, 1680], radius=24, fill=(15, 12, 30, 245), outline=RAINBOW_COLORS[3], width=4)
        draw_rainbow_bar(draw, 100, 1180, 880, height=10)
        lines = wrap_text(headline, f_head, 800, draw)
        for i, line in enumerate(lines):
            draw.text((130, 1260 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #08: Prism Split-Screen Triad
    elif index == 8:
        # 3 vertical rainbow gradient pillars
        for p in range(3):
            px0 = 60 + p * 330
            c = RAINBOW_COLORS[p * 2]
            c_next = RAINBOW_COLORS[(p * 2 + 2) % len(RAINBOW_COLORS)]
            draw.rounded_rectangle([px0, 120, px0 + 300, 1800], radius=20, fill=(*c[:3], 40), outline=c_next, width=3)
        focal = load_focal_image(img_path, (860, 680))
        canvas.paste(focal, (110, 380))
        draw_rainbow_frame(draw, (110, 380, 970, 1060), width=8)
        draw.rounded_rectangle([100, 1180, 980, 1680], radius=28, fill=(12, 10, 26, 245))
        draw_rainbow_bar(draw, 100, 1180, 880, height=12)
        lines = wrap_text(headline, f_head, 800, draw)
        for i, line in enumerate(lines):
            draw.text((130, 1260 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #09: Rainbow Glitch Scanline Broadcast
    elif index == 9:
        # Glitch RGB offsets
        focal = load_focal_image(img_path, (860, 680))
        canvas.paste(focal, (110, 380))
        # Rainbow Glitch Horizontal bars
        glitch_y = [420, 560, 710, 850, 990, 1120]
        for idx, gy in enumerate(glitch_y):
            col = RAINBOW_COLORS[idx % len(RAINBOW_COLORS)]
            draw.rectangle([80, gy, 1000, gy + 12], fill=(*col[:3], 200))
        # TV Warning Header
        draw.rectangle([0, 160, 1080, 240], fill=(255, 30, 80))
        draw_rainbow_bar(draw, 0, 240, 1080, height=8)
        draw.text((120, 175), "/// CRITICAL DISCOVERY SCAN ///", fill=(255, 255, 255), font=f_badge)
        # Headline Box
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=16, fill=(10, 10, 20, 245), outline=RAINBOW_COLORS[4], width=4)
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1290 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #10: Curved Rainbow Liquid Wave
    elif index == 10:
        # S-Curve rainbow ribbons
        for i, col in enumerate(RAINBOW_COLORS):
            points = []
            for y_step in range(0, 1920, 40):
                x_val = 540 + math.sin(y_step * 0.003 + i * 0.4) * 380
                points.append((x_val, y_step))
            for p_idx in range(len(points) - 1):
                draw.line([points[p_idx], points[p_idx + 1]], fill=col, width=14)
        focal = load_focal_image(img_path, (840, 700))
        canvas.paste(focal, (120, 400))
        draw_rainbow_frame(draw, (120, 400, 960, 1100), width=8)
        draw.rounded_rectangle([100, 1220, 980, 1720], radius=32, fill=(12, 10, 26, 240))
        draw_rainbow_bar(draw, 100, 1220, 880, height=10)
        lines = wrap_text(headline, f_head, 800, draw)
        for i, line in enumerate(lines):
            draw.text((130, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #11: Rainbow Neon Polaroid with Splatters
    elif index == 11:
        # Polaroid white border with multi-colored corners
        draw.rounded_rectangle([100, 280, 980, 1180], radius=24, fill=(245, 245, 250), outline=(255, 255, 255), width=4)
        focal = load_focal_image(img_path, (800, 680))
        canvas.paste(focal, (140, 320))
        # Draw rainbow drips at bottom of polaroid
        for i, col in enumerate(RAINBOW_COLORS):
            dx = 140 + i * 100
            dh = 30 + (i % 3) * 25
            draw.rounded_rectangle([dx, 1000, dx + 40, 1000 + dh], radius=10, fill=col)
        # Rainbow bar under polaroid
        draw_rainbow_bar(draw, 140, 1100, 800, height=14)
        # Headline in vibrant card below
        draw.rounded_rectangle([90, 1240, 990, 1720], radius=24, fill=(14, 12, 28, 245))
        draw_rainbow_frame(draw, (90, 1240, 990, 1720), width=6)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1310 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #12: Cosmic Rainbow Stargate Portal
    elif index == 12:
        # Concentric rainbow ovals receding in 3D
        cx, cy = 540, 720
        for i in range(12):
            col = RAINBOW_COLORS[i % len(RAINBOW_COLORS)]
            rx = 480 - i * 30
            ry = 380 - i * 24
            if rx > 50 and ry > 50:
                draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], outline=col, width=5)
        focal = load_focal_image(img_path, (680, 540))
        canvas.paste(focal, (200, 450))
        draw_rainbow_frame(draw, (200, 450, 880, 990), width=6)
        draw.rounded_rectangle([90, 1200, 990, 1720], radius=32, fill=(10, 8, 24, 245), outline=RAINBOW_COLORS[4], width=4)
        draw_rainbow_bar(draw, 90, 1200, 900, height=12)
        lines = wrap_text(headline, f_impact, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1280 + i * 85), line, fill=RAINBOW_COLORS[(i * 3) % len(RAINBOW_COLORS)], font=f_impact)

    # Design #13: Rainbow Honeycomb Hex-Grid
    elif index == 13:
        # Hexagons on canvas border
        focal = load_focal_image(img_path, (860, 720))
        canvas.paste(focal, (110, 360))
        draw_rainbow_frame(draw, (105, 355, 975, 1085), width=8)
        # Honeycomb cells around frame in rainbow
        hex_y = [240, 240, 240, 240, 1160, 1160, 1160, 1160]
        hex_x = [180, 420, 660, 900, 180, 420, 660, 900]
        for h_idx in range(len(hex_x)):
            col = RAINBOW_COLORS[h_idx % len(RAINBOW_COLORS)]
            draw.regular_polygon((hex_x[h_idx], hex_y[h_idx], 42), n_sides=6, fill=(*col[:3], 160), outline=(255, 255, 255))
        draw.rounded_rectangle([90, 1240, 990, 1720], radius=24, fill=(12, 10, 26, 245))
        draw_rainbow_bar(draw, 90, 1240, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1310 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #14: Aurora Borealis Spectral Wave
    elif index == 14:
        # Vertical curtains of colors
        for i, col in enumerate(RAINBOW_COLORS):
            x_start = i * 135
            draw.rectangle([x_start, 0, x_start + 135, 1920], fill=(*col[:3], 45))
        focal = load_focal_image(img_path, (880, 680))
        canvas.paste(focal, (100, 420))
        draw_rainbow_bar(draw, 100, 410, 880, height=10)
        draw_rainbow_bar(draw, 100, 1100, 880, height=10)
        draw.rounded_rectangle([90, 1200, 990, 1720], radius=28, fill=(10, 8, 22, 245))
        draw_rainbow_frame(draw, (90, 1200, 990, 1720), width=6)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1280 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #15: 3D Rainbow Ribbon Helix
    elif index == 15:
        focal = load_focal_image(img_path, (860, 700))
        canvas.paste(focal, (110, 380))
        # Draw winding rainbow ribbons crossing over image
        for i, col in enumerate(RAINBOW_COLORS):
            y_rib = 300 + i * 110
            draw.line([(60, y_rib), (1020, y_rib + 80)], fill=col, width=10)
        draw_rainbow_frame(draw, (110, 380, 970, 1080), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=26, fill=(12, 10, 25, 245), outline=RAINBOW_COLORS[2], width=4)
        draw_rainbow_bar(draw, 90, 1220, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #16: Neo-Brutalist Multi-Color Block Collage
    elif index == 16:
        # Thick offset 3D blocks in rainbow colors
        draw.rectangle([130, 310, 990, 1030], fill=RAINBOW_COLORS[0])
        draw.rectangle([115, 295, 975, 1015], fill=RAINBOW_COLORS[2])
        focal = load_focal_image(img_path, (840, 700))
        canvas.paste(focal, (100, 280))
        draw.rectangle([100, 280, 940, 980], outline=(0, 0, 0), width=10)
        # Headline in Brutalist yellow block with magenta shadow
        draw.rectangle([110, 1160, 990, 1680], fill=RAINBOW_COLORS[7])
        draw.rectangle([90, 1140, 970, 1660], fill=RAINBOW_COLORS[2], outline=(0, 0, 0), width=8)
        draw_rainbow_bar(draw, 90, 1140, 880, height=12)
        lines = wrap_text(headline, f_impact, 800, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1210 + i * 85), line, fill=(0, 0, 0), font=f_impact)

    # Design #17: Rainbow Laser Grid Cage
    elif index == 17:
        # 3D perspective wireframe box
        for i, col in enumerate(RAINBOW_COLORS):
            draw.line([(100 + i * 110, 200), (40 + i * 125, 1200)], fill=col, width=3)
            draw.line([(40, 300 + i * 100), (1040, 300 + i * 100)], fill=col, width=3)
        focal = load_focal_image(img_path, (840, 680))
        canvas.paste(focal, (120, 420))
        draw_rainbow_frame(draw, (120, 420, 960, 1100), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=24, fill=(8, 6, 18, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #18: Prismatic Flare Starburst
    elif index == 18:
        # Starburst rays from top-left (0,0) in all 8 rainbow colors
        for i, col in enumerate(RAINBOW_COLORS):
            draw.polygon([(0, 0), (i * 150, 600), ((i + 1) * 150, 600)], fill=(*col[:3], 90))
        focal = load_focal_image(img_path, (880, 700))
        canvas.paste(focal, (100, 400))
        draw_rainbow_frame(draw, (100, 400, 980, 1100), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=28, fill=(14, 10, 26, 245), outline=RAINBOW_COLORS[1], width=4)
        draw_rainbow_bar(draw, 90, 1220, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #19: Segmented Rainbow Speedometer Gauge
    elif index == 19:
        # Rainbow gauge arc
        cx, cy = 540, 360
        for i, col in enumerate(RAINBOW_COLORS):
            start_ang = 180 + i * 22.5
            end_ang = start_ang + 20
            draw.arc([cx - 260, cy - 260, cx + 260, cy + 260], start=start_ang, end=end_ang, fill=col, width=20)
        draw.text((cx - 140, cy - 30), "VIRAL INDEX 99.8%", fill=(255, 255, 255), font=f_badge)
        focal = load_focal_image(img_path, (880, 640))
        canvas.paste(focal, (100, 480))
        draw_rainbow_frame(draw, (100, 480, 980, 1120), width=6)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=26, fill=(12, 10, 26, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #20: Rainbow Filmstrip Cinema
    elif index == 20:
        # Filmstrip sprockets on left and right borders in rainbow hues
        for y_sp in range(100, 1800, 100):
            col = RAINBOW_COLORS[(y_sp // 100) % len(RAINBOW_COLORS)]
            draw.rounded_rectangle([30, y_sp, 70, y_sp + 60], radius=8, fill=col)
            draw.rounded_rectangle([1010, y_sp, 1050, y_sp + 60], radius=8, fill=col)
        focal = load_focal_image(img_path, (880, 720))
        canvas.paste(focal, (100, 340))
        draw_rainbow_bar(draw, 100, 330, 880, height=10)
        draw_rainbow_bar(draw, 100, 1060, 880, height=10)
        draw.rounded_rectangle([100, 1180, 980, 1720], radius=24, fill=(15, 12, 28, 245), outline=RAINBOW_COLORS[5], width=4)
        draw_rainbow_bar(draw, 100, 1180, 880, height=10)
        lines = wrap_text(headline, f_head, 800, draw)
        for i, line in enumerate(lines):
            draw.text((130, 1260 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #21: Diamond Prismatic Lozenge
    elif index == 21:
        # 4 Corner laser beams shooting to center in rainbow
        draw.line([(0, 0), (540, 720)], fill=RAINBOW_COLORS[0], width=8)
        draw.line([(1080, 0), (540, 720)], fill=RAINBOW_COLORS[2], width=8)
        draw.line([(0, 1440), (540, 720)], fill=RAINBOW_COLORS[4], width=8)
        draw.line([(1080, 1440), (540, 720)], fill=RAINBOW_COLORS[6], width=8)
        focal = load_focal_image(img_path, (820, 680))
        canvas.paste(focal, (130, 420))
        draw_rainbow_frame(draw, (130, 420, 950, 1100), width=10)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=28, fill=(10, 8, 24, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_impact, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 85), line, fill=RAINBOW_COLORS[(i * 2 + 1) % len(RAINBOW_COLORS)], font=f_impact)

    # Design #22: Rainbow Vaporwave Horizon
    elif index == 22:
        # Horizontal gradient steps
        for step in range(8):
            y_s = 900 + step * 35
            col = RAINBOW_COLORS[step]
            draw.rectangle([60, y_s, 1020, y_s + 18], fill=col)
        focal = load_focal_image(img_path, (880, 600))
        canvas.paste(focal, (100, 260))
        draw_rainbow_frame(draw, (100, 260, 980, 860), width=8)
        draw.rounded_rectangle([80, 1240, 1000, 1720], radius=24, fill=(14, 10, 26, 245), outline=RAINBOW_COLORS[3], width=4)
        draw_rainbow_bar(draw, 80, 1240, 920, height=10)
        lines = wrap_text(headline, f_head, 840, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1320 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #23: Multi-Pill Floating Dashboard
    elif index == 23:
        # 6 floating pills across the screen in rainbow colors
        pills = [("HOT", RAINBOW_COLORS[0]), ("TRENDING", RAINBOW_COLORS[1]), ("FACT", RAINBOW_COLORS[2]),
                 ("SCIENCE", RAINBOW_COLORS[3]), ("VERIFIED", RAINBOW_COLORS[4]), ("VIRAL", RAINBOW_COLORS[6])]
        for p_idx, (p_text, p_col) in enumerate(pills):
            px = 70 + (p_idx % 3) * 320
            py = 180 + (p_idx // 3) * 80
            draw.rounded_rectangle([px, py, px + 280, py + 55], radius=25, fill=p_col)
            draw.text((px + 45, py + 12), p_text, fill=(0, 0, 0), font=f_meta)
        focal = load_focal_image(img_path, (880, 700))
        canvas.paste(focal, (100, 420))
        draw_rainbow_frame(draw, (100, 420, 980, 1120), width=8)
        draw.rounded_rectangle([80, 1220, 1000, 1720], radius=26, fill=(12, 10, 25, 245))
        draw_rainbow_bar(draw, 80, 1220, 920, height=12)
        lines = wrap_text(headline, f_head, 840, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #24: Rainbow Neon Circuit Traces
    elif index == 24:
        # Glowing circuit traces in rainbow
        for i, col in enumerate(RAINBOW_COLORS):
            trace_y = 150 + i * 200
            draw.line([(50, trace_y), (250, trace_y), (350, trace_y + 80), (1030, trace_y + 80)], fill=col, width=4)
            draw.ellipse([240, trace_y - 10, 260, trace_y + 10], fill=col)
        focal = load_focal_image(img_path, (860, 680))
        canvas.paste(focal, (110, 420))
        draw_rainbow_frame(draw, (110, 420, 970, 1100), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=28, fill=(10, 8, 22, 245), outline=RAINBOW_COLORS[4], width=4)
        draw_rainbow_bar(draw, 90, 1220, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #25: Chromatic Aberration 3D Glass
    elif index == 25:
        # Offset 3D RGB glass borders
        draw.rounded_rectangle([80, 360, 960, 1080], radius=28, fill=(255, 0, 80, 160))
        draw.rounded_rectangle([120, 400, 1000, 1120], radius=28, fill=(0, 240, 255, 160))
        focal = load_focal_image(img_path, (840, 680))
        canvas.paste(focal, (120, 400))
        draw_rainbow_bar(draw, 100, 240, 880, height=14)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=28, fill=(12, 10, 26, 245))
        draw_rainbow_frame(draw, (90, 1220, 990, 1720), width=6)
        lines = wrap_text(headline, f_impact, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1290 + i * 85), line, fill=RAINBOW_COLORS[(i * 2) % len(RAINBOW_COLORS)], font=f_impact)

    # Design #26: Rainbow Spiral Vortex
    elif index == 26:
        # Concentric spiral arms
        cx, cy = 540, 720
        for arm in range(8):
            col = RAINBOW_COLORS[arm]
            for step in range(30):
                ang = step * 0.2 + arm * (math.pi / 4)
                dist = 80 + step * 14
                px = cx + math.cos(ang) * dist
                py = cy + math.sin(ang) * dist
                draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=col)
        focal = load_focal_image(img_path, (760, 640))
        canvas.paste(focal, (160, 440))
        draw_rainbow_frame(draw, (160, 440, 920, 1080), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=32, fill=(10, 8, 24, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #27: Split Diagonal Blade with Multi-Glow
    elif index == 27:
        # 45-degree angle blade
        focal = load_focal_image(img_path, (920, 680))
        canvas.paste(focal, (80, 360))
        # Rainbow blade line
        draw.line([(0, 1060), (1080, 1140)], fill=RAINBOW_COLORS[0], width=16)
        draw.line([(0, 1080), (1080, 1160)], fill=RAINBOW_COLORS[2], width=14)
        draw.line([(0, 1100), (1080, 1180)], fill=RAINBOW_COLORS[4], width=12)
        draw.line([(0, 1120), (1080, 1200)], fill=RAINBOW_COLORS[6], width=10)
        draw.rounded_rectangle([80, 1260, 1000, 1720], radius=24, fill=(12, 10, 26, 245))
        draw_rainbow_bar(draw, 80, 1260, 920, height=10)
        lines = wrap_text(headline, f_head, 840, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1340 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #28: Rainbow Hologram HUD Card
    elif index == 28:
        # Crosshairs and telemetry
        focal = load_focal_image(img_path, (860, 680))
        canvas.paste(focal, (110, 380))
        draw_rainbow_frame(draw, (110, 380, 970, 1060), width=6)
        # Radar circles in corners
        draw.ellipse([80, 240, 200, 360], outline=RAINBOW_COLORS[0], width=4)
        draw.ellipse([880, 240, 1000, 360], outline=RAINBOW_COLORS[4], width=4)
        draw_rainbow_bar(draw, 240, 290, 600, height=8)
        draw.rounded_rectangle([90, 1180, 990, 1720], radius=24, fill=(8, 6, 18, 245), outline=RAINBOW_COLORS[3], width=4)
        draw_rainbow_bar(draw, 90, 1180, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1260 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #29: Neon Rainbow Graffiti Stencil
    elif index == 29:
        # Drip lines and splatter
        for i, col in enumerate(RAINBOW_COLORS):
            draw.rectangle([80 + i * 115, 200, 160 + i * 115, 280], fill=col)
            draw.line([(120 + i * 115, 280), (120 + i * 115, 340 + (i % 4) * 30)], fill=col, width=8)
        focal = load_focal_image(img_path, (880, 680))
        canvas.paste(focal, (100, 420))
        draw_rainbow_frame(draw, (100, 420, 980, 1100), width=8)
        draw.rounded_rectangle([80, 1220, 1000, 1720], radius=28, fill=(14, 10, 28, 245))
        draw_rainbow_bar(draw, 80, 1220, 920, height=12)
        lines = wrap_text(headline, f_impact, 840, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1290 + i * 85), line, fill=RAINBOW_COLORS[(i * 3) % len(RAINBOW_COLORS)], font=f_impact)

    # Design #30: Rainbow Sine-Wave Audio Waveform
    elif index == 30:
        # Oscillating wave lines across screen
        for i, col in enumerate(RAINBOW_COLORS):
            pts = []
            for x_val in range(60, 1020, 20):
                y_val = 1140 + math.sin(x_val * 0.015 + i * 0.5) * 45
                pts.append((x_val, y_val))
            for p_idx in range(len(pts) - 1):
                draw.line([pts[p_idx], pts[p_idx + 1]], fill=col, width=6)
        focal = load_focal_image(img_path, (880, 680))
        canvas.paste(focal, (100, 360))
        draw_rainbow_frame(draw, (100, 360, 980, 1040), width=8)
        draw.rounded_rectangle([90, 1240, 990, 1720], radius=26, fill=(12, 10, 25, 245))
        draw_rainbow_bar(draw, 90, 1240, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1320 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #31: Multi-Color Segmented Ring Clock
    elif index == 31:
        cx, cy = 540, 720
        # 12-hour rainbow segments
        for seg in range(12):
            col = RAINBOW_COLORS[seg % len(RAINBOW_COLORS)]
            ang_s = seg * 30
            draw.arc([cx - 420, cy - 420, cx + 420, cy + 420], start=ang_s, end=ang_s + 24, fill=col, width=16)
        focal = load_focal_image(img_path, (760, 640))
        canvas.paste(focal, (160, 440))
        draw_rainbow_frame(draw, (160, 440, 920, 1080), width=6)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=30, fill=(10, 8, 24, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #32: Vertical Rainbow Barcode Matrix
    elif index == 32:
        # Barcode stripes on top and bottom
        for b in range(40):
            col = RAINBOW_COLORS[b % len(RAINBOW_COLORS)]
            bx = 80 + b * 23
            bw = 6 if b % 2 == 0 else 14
            draw.rectangle([bx, 160, bx + bw, 260], fill=col)
            draw.rectangle([bx, 1740, bx + bw, 1840], fill=col)
        focal = load_focal_image(img_path, (880, 720))
        canvas.paste(focal, (100, 320))
        draw_rainbow_frame(draw, (100, 320, 980, 1040), width=8)
        draw.rounded_rectangle([90, 1160, 990, 1660], radius=24, fill=(12, 10, 26, 245), outline=RAINBOW_COLORS[4], width=4)
        draw_rainbow_bar(draw, 90, 1160, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1240 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #33: Prism Diamond Crystal Facets
    elif index == 33:
        # Faceted corner triangles in rainbow
        draw.polygon([(0, 0), (280, 0), (0, 280)], fill=RAINBOW_COLORS[0])
        draw.polygon([(1080, 0), (800, 0), (1080, 280)], fill=RAINBOW_COLORS[2])
        draw.polygon([(0, 1920), (280, 1920), (0, 1640)], fill=RAINBOW_COLORS[4])
        draw.polygon([(1080, 1920), (800, 1920), (1080, 1640)], fill=RAINBOW_COLORS[6])
        focal = load_focal_image(img_path, (860, 700))
        canvas.paste(focal, (110, 380))
        draw_rainbow_frame(draw, (110, 380, 970, 1080), width=8)
        draw.rounded_rectangle([90, 1200, 990, 1700], radius=28, fill=(14, 10, 28, 245))
        draw_rainbow_bar(draw, 90, 1200, 900, height=12)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1280 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #34: Rainbow Stadium Jumbo-Tron
    elif index == 34:
        # LED dot matrix rows around image
        for row in range(6):
            col = RAINBOW_COLORS[row]
            for col_dot in range(24):
                dx = 80 + col_dot * 39
                draw.ellipse([dx, 200 + row * 24, dx + 14, 214 + row * 24], fill=col)
                draw.ellipse([dx, 1120 + row * 24, dx + 14, 1134 + row * 24], fill=col)
        focal = load_focal_image(img_path, (880, 640))
        canvas.paste(focal, (100, 400))
        draw_rainbow_frame(draw, (100, 400, 980, 1040), width=8)
        draw.rounded_rectangle([80, 1300, 1000, 1760], radius=24, fill=(10, 8, 20, 245))
        draw_rainbow_bar(draw, 80, 1300, 920, height=10)
        lines = wrap_text(headline, f_head, 840, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1370 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #35: Floating Rainbow Glass Spheres
    elif index == 35:
        # Translucent rainbow orbs
        for i, col in enumerate(RAINBOW_COLORS):
            ang = i * (math.pi / 4)
            ox = 540 + math.cos(ang) * 440
            oy = 720 + math.sin(ang) * 440
            draw.ellipse([ox - 45, oy - 45, ox + 45, oy + 45], fill=(*col[:3], 180), outline=(255, 255, 255), width=3)
        focal = load_focal_image(img_path, (800, 680))
        canvas.paste(focal, (140, 400))
        draw_rainbow_frame(draw, (140, 400, 940, 1080), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=32, fill=(12, 10, 26, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #36: Triple Nested Rainbow Frames
    elif index == 36:
        # 3 nested colored frames
        draw.rounded_rectangle([60, 260, 1020, 1160], radius=30, outline=RAINBOW_COLORS[0], width=8)
        draw.rounded_rectangle([90, 290, 990, 1130], radius=26, outline=RAINBOW_COLORS[2], width=6)
        draw.rounded_rectangle([120, 320, 960, 1100], radius=22, outline=RAINBOW_COLORS[4], width=6)
        focal = load_focal_image(img_path, (800, 680))
        canvas.paste(focal, (140, 360))
        draw.rounded_rectangle([80, 1240, 1000, 1720], radius=26, fill=(10, 8, 22, 245), outline=RAINBOW_COLORS[6], width=4)
        draw_rainbow_bar(draw, 80, 1240, 920, height=10)
        lines = wrap_text(headline, f_head, 840, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1320 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #37: High-Voltage Rainbow Arc
    elif index == 37:
        # Lightning / electric bolts
        for i, col in enumerate(RAINBOW_COLORS):
            y_l = 220 + i * 110
            draw.line([(50, y_l), (200, y_l - 30), (450, y_l + 25), (750, y_l - 20), (1030, y_l)], fill=col, width=4)
        focal = load_focal_image(img_path, (860, 680))
        canvas.paste(focal, (110, 420))
        draw_rainbow_frame(draw, (110, 420, 970, 1100), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=28, fill=(12, 10, 26, 245), outline=RAINBOW_COLORS[2], width=4)
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_impact, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1290 + i * 85), line, fill=RAINBOW_COLORS[(i * 2 + 1) % len(RAINBOW_COLORS)], font=f_impact)

    # Design #38: Rainbow Origami Triangle Facets
    elif index == 38:
        # Triangular facets behind
        for i, col in enumerate(RAINBOW_COLORS):
            x1 = 60 + i * 120
            draw.polygon([(x1, 160), (x1 + 60, 260), (x1 - 60, 260)], fill=(*col[:3], 190))
            draw.polygon([(x1, 1180), (x1 + 60, 1080), (x1 - 60, 1080)], fill=(*col[:3], 190))
        focal = load_focal_image(img_path, (880, 720))
        canvas.paste(focal, (100, 320))
        draw_rainbow_frame(draw, (100, 320, 980, 1040), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=26, fill=(10, 8, 22, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #39: Holographic Caution Tape & Stamp
    elif index == 39:
        # Caution tapes across screen
        for i, col in enumerate(RAINBOW_COLORS):
            draw.rectangle([0, 180 + i * 14, 1080, 180 + (i + 1) * 14], fill=col)
            draw.rectangle([0, 1120 + i * 14, 1080, 1120 + (i + 1) * 14], fill=col)
        focal = load_focal_image(img_path, (880, 720))
        canvas.paste(focal, (100, 340))
        draw_rainbow_frame(draw, (100, 340, 980, 1060), width=8)
        draw.rounded_rectangle([90, 1260, 990, 1720], radius=24, fill=(15, 12, 28, 245))
        draw_rainbow_bar(draw, 90, 1260, 900, height=12)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1330 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #40: Rainbow Horizon Sunrise
    elif index == 40:
        # Slices of rising sun
        cx, cy = 540, 1100
        for i, col in enumerate(RAINBOW_COLORS):
            rad = 480 - i * 40
            draw.arc([cx - rad, cy - rad, cx + rad, cy + rad], start=180, end=360, fill=col, width=16)
        focal = load_focal_image(img_path, (860, 640))
        canvas.paste(focal, (110, 320))
        draw_rainbow_frame(draw, (110, 320, 970, 960), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=28, fill=(12, 10, 26, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #41: Concentric Rainbow Bullseye Target
    elif index == 41:
        cx, cy = 540, 720
        for i, col in enumerate(RAINBOW_COLORS):
            rad = 420 - i * 35
            draw.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], outline=col, width=6)
        # Crosshair lines
        draw.line([(cx - 450, cy), (cx + 450, cy)], fill=(255, 255, 255, 180), width=2)
        draw.line([(cx, cy - 450), (cx, cy + 450)], fill=(255, 255, 255, 180), width=2)
        focal = load_focal_image(img_path, (700, 580))
        canvas.paste(focal, (190, 430))
        draw_rainbow_frame(draw, (190, 430, 890, 1010), width=6)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=30, fill=(10, 8, 24, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_impact, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1290 + i * 85), line, fill=RAINBOW_COLORS[(i * 3) % len(RAINBOW_COLORS)], font=f_impact)

    # Design #42: Rainbow Neon Ladder / Steps
    elif index == 42:
        # Horizontal ladder steps
        for i, col in enumerate(RAINBOW_COLORS):
            step_w = 400 + i * 70
            sx = 540 - step_w // 2
            sy = 1120 + i * 16
            draw.rounded_rectangle([sx, sy, sx + step_w, sy + 10], radius=5, fill=col)
        focal = load_focal_image(img_path, (880, 700))
        canvas.paste(focal, (100, 340))
        draw_rainbow_frame(draw, (100, 340, 980, 1040), width=8)
        draw.rounded_rectangle([90, 1280, 990, 1740], radius=24, fill=(14, 10, 26, 245))
        draw_rainbow_bar(draw, 90, 1280, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1350 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #43: Prism Light Leak Editorial
    elif index == 43:
        # Diagonal rainbow strip cutting through
        draw.polygon([(0, 200), (400, 0), (1080, 1400), (680, 1600)], fill=(*RAINBOW_COLORS[4][:3], 70))
        for i, col in enumerate(RAINBOW_COLORS):
            draw.line([(0, 300 + i * 20), (1080, 1380 + i * 20)], fill=col, width=4)
        focal = load_focal_image(img_path, (860, 700))
        canvas.paste(focal, (110, 380))
        draw_rainbow_frame(draw, (110, 380, 970, 1080), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=28, fill=(12, 10, 26, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #44: Rainbow Particle Sparkle Nebula
    elif index == 44:
        # Random multi-colored stars/dots
        random.seed(44)
        for _ in range(120):
            rx = random.randint(50, 1030)
            ry = random.randint(100, 1820)
            r_col = random.choice(RAINBOW_COLORS)
            r_sz = random.randint(3, 10)
            draw.ellipse([rx, ry, rx + r_sz, ry + r_sz], fill=r_col)
        focal = load_focal_image(img_path, (860, 680))
        canvas.paste(focal, (110, 420))
        draw_rainbow_frame(draw, (110, 420, 970, 1100), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=28, fill=(10, 8, 22, 245), outline=RAINBOW_COLORS[1], width=4)
        draw_rainbow_bar(draw, 90, 1220, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #45: Multi-Tone Split Quad
    elif index == 45:
        # 4 corners in 4 complementary rainbow pairs
        draw.rectangle([0, 0, 540, 960], fill=(*RAINBOW_COLORS[0][:3], 40))
        draw.rectangle([540, 0, 1080, 960], fill=(*RAINBOW_COLORS[2][:3], 40))
        draw.rectangle([0, 960, 540, 1920], fill=(*RAINBOW_COLORS[4][:3], 40))
        draw.rectangle([540, 960, 1080, 1920], fill=(*RAINBOW_COLORS[6][:3], 40))
        draw_rainbow_bar(draw, 0, 955, 1080, height=10)
        draw.line([(540, 0), (540, 1920)], fill=(255, 255, 255), width=4)
        focal = load_focal_image(img_path, (840, 680))
        canvas.paste(focal, (120, 380))
        draw_rainbow_frame(draw, (120, 380, 960, 1060), width=8)
        draw.rounded_rectangle([90, 1200, 990, 1700], radius=26, fill=(12, 10, 26, 245))
        draw_rainbow_bar(draw, 90, 1200, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1280 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #46: Rainbow Terminal Code Matrix
    elif index == 46:
        # Matrix code symbols running vertically in rainbow
        symbols = "0101XYZ#@!%&*"
        for col_idx in range(16):
            col = RAINBOW_COLORS[col_idx % len(RAINBOW_COLORS)]
            cx_pos = 60 + col_idx * 64
            for row_idx in range(24):
                cy_pos = 100 + row_idx * 75
                draw.text((cx_pos, cy_pos), symbols[(col_idx + row_idx) % len(symbols)], fill=(*col[:3], 120), font=f_meta)
        focal = load_focal_image(img_path, (860, 680))
        canvas.paste(focal, (110, 420))
        draw_rainbow_frame(draw, (110, 420, 970, 1100), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=24, fill=(6, 6, 14, 250), outline=RAINBOW_COLORS[3], width=4)
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #47: Curved Rainbow Ribbon Arch
    elif index == 47:
        # Triumphal rainbow arch at top
        cx, cy = 540, 220
        for i, col in enumerate(RAINBOW_COLORS):
            rad = 340 - i * 16
            draw.arc([cx - rad, cy - rad, cx + rad, cy + rad], start=180, end=360, fill=col, width=12)
        focal = load_focal_image(img_path, (880, 720))
        canvas.paste(focal, (100, 360))
        draw_rainbow_frame(draw, (100, 360, 980, 1080), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=28, fill=(12, 10, 26, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #48: Rainbow Radar Sweep
    elif index == 48:
        cx, cy = 540, 720
        # Radar pie slice sweep in rainbow colors
        for i, col in enumerate(RAINBOW_COLORS):
            ang = 30 + i * 12
            draw.line([(cx, cy), (cx + math.cos(math.radians(ang)) * 480, cy + math.sin(math.radians(ang)) * 480)], fill=col, width=6)
        draw.ellipse([cx - 440, cy - 440, cx + 440, cy + 440], outline=(255, 255, 255), width=4)
        focal = load_focal_image(img_path, (760, 640))
        canvas.paste(focal, (160, 440))
        draw_rainbow_frame(draw, (160, 440, 920, 1080), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=30, fill=(10, 8, 24, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=12)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #49: Geometric Rainbow Tessellation
    elif index == 49:
        # Diamond / cube patterns in rainbow
        for r in range(4):
            for c in range(8):
                col = RAINBOW_COLORS[(r + c) % len(RAINBOW_COLORS)]
                bx = 60 + c * 125
                by = 140 + r * 60
                draw.polygon([(bx, by + 30), (bx + 60, by), (bx + 120, by + 30), (bx + 60, by + 60)], fill=(*col[:3], 150))
        focal = load_focal_image(img_path, (880, 700))
        canvas.paste(focal, (100, 400))
        draw_rainbow_frame(draw, (100, 400, 980, 1100), width=8)
        draw.rounded_rectangle([90, 1220, 990, 1720], radius=26, fill=(12, 10, 26, 245))
        draw_rainbow_bar(draw, 90, 1220, 900, height=10)
        lines = wrap_text(headline, f_head, 820, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1300 + i * 75), line, fill=(255, 255, 255), font=f_head)

    # Design #50: Ultimate Rainbow Prism Supreme
    elif index == 50:
        # Everything combined into the flagship showstopper:
        # 1. Conic circular halo
        cx, cy = 540, 720
        for i, col in enumerate(RAINBOW_COLORS):
            rad = 440 + i * 8
            draw.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], outline=col, width=5)
        # 2. Hero photo
        focal = load_focal_image(img_path, (820, 680))
        canvas.paste(focal, (130, 420))
        draw_rainbow_frame(draw, (130, 420, 950, 1100), width=10)
        # 3. Rainbow equalizer bars along base
        for b in range(24):
            col = RAINBOW_COLORS[b % len(RAINBOW_COLORS)]
            bar_h = 25 + int(math.sin(b * 0.5) * 35 + 40)
            bx = 140 + b * 34
            draw.rounded_rectangle([bx, 1180 - bar_h, bx + 22, 1180], radius=5, fill=col)
        # 4. Floating category chips
        draw_rainbow_badge(canvas, f"🌟 ULTIMATE SPECTRUM // {cat}", 120, 180, f_badge)
        # 5. Bottom glassmorphic container with rainbow frame
        draw.rounded_rectangle([80, 1240, 1000, 1740], radius=32, fill=(10, 8, 22, 245))
        draw_rainbow_bar(draw, 80, 1240, 920, height=14)
        draw_rainbow_frame(draw, (80, 1240, 1000, 1740), width=6)
        lines = wrap_text(headline, f_impact, 840, draw)
        for i, line in enumerate(lines):
            draw.text((120, 1310 + i * 85), line, fill=RAINBOW_COLORS[(i * 2) % len(RAINBOW_COLORS)], font=f_impact)
        draw.text((120, 1640), "✨ ALL COLORS SPECTRUM ACTIVATED ✨", fill=(255, 255, 255), font=f_meta)

    # Top indicator badge with index number on all samples
    draw.rounded_rectangle([60, 60, 260, 135], radius=18, fill=(0, 0, 0, 220), outline=(255, 255, 255), width=2)
    draw_rainbow_bar(draw, 60, 60, 200, height=5)
    draw.text((80, 75), f"#{index:02d} RAINBOW", fill=(255, 255, 255), font=f_num)

    # Save
    out_file = OUTPUT_DIR / f"rainbow_sample_{index:02d}.png"
    canvas.save(out_file, "PNG", quality=95)
    return out_file

def generate_contact_sheets():
    """Builds 5 contact sheets (10 thumbnails each)."""
    print("[*] Generating 5 Rainbow Contact Sheets (10 thumbnails each)...")
    samples = sorted(list(OUTPUT_DIR.glob("rainbow_sample_*.png")))
    f_title = get_font(40, bold=True, impact=True)
    
    # 5 sheets x 10 thumbnails (2 rows x 5 cols)
    # Thumbnail size: 270 x 480
    # Sheet size: 5 * 270 + 6 * 20 = 1350 + 120 = 1470 w, 2 * 480 + 3 * 20 + 100 = 960 + 60 + 100 = 1120 h
    thumb_w, thumb_h = 270, 480
    pad = 24
    header_h = 110
    sheet_w = 5 * thumb_w + 6 * pad
    sheet_h = 2 * thumb_h + 3 * pad + header_h
    
    sheet_files = []
    for sheet_idx in range(5):
        sheet = Image.new("RGBA", (sheet_w, sheet_h), (12, 10, 24, 255))
        draw = ImageDraw.Draw(sheet)
        
        # Rainbow top bar
        draw_rainbow_bar(draw, 0, 0, sheet_w, height=12)
        
        start_num = sheet_idx * 10 + 1
        end_num = start_num + 9
        title = f"🌈 RAINBOW MULTI-COLOR SHOWCASE: DESIGNS #{start_num:02d} - #{end_num:02d}"
        draw.text((pad, 36), title, fill=(255, 255, 255), font=f_title)
        
        for i in range(10):
            sample_num = start_num + i
            sample_path = OUTPUT_DIR / f"rainbow_sample_{sample_num:02d}.png"
            if sample_path.exists():
                col_i = i % 5
                row_i = i // 5
                tx = pad + col_i * (thumb_w + pad)
                ty = header_h + pad + row_i * (thumb_h + pad)
                
                thumb = Image.open(sample_path).resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
                sheet.paste(thumb, (tx, ty))
                # Rainbow border around thumbnail
                draw_rainbow_frame(draw, (tx - 2, ty - 2, tx + thumb_w + 2, ty + thumb_h + 2), width=3)
        
        out_sheet = CONTACT_DIR / f"rainbow_contact_sheet_{sheet_idx + 1}.png"
        sheet.save(out_sheet, "PNG")
        sheet_files.append(out_sheet)
        print(f"    Saved Rainbow Sheet {sheet_idx + 1}: {out_sheet.name}")
    return sheet_files

def main():
    print("[*] Generating 50 TRULY UNIQUE Full-Spectrum Rainbow Designs...")
    for idx in range(1, 51):
        h_info = HEADLINES[(idx - 1) % len(HEADLINES)]
        img = temp_images[(idx - 1) % len(temp_images)]
        generate_sample(idx, h_info, img)
        if idx % 10 == 0:
            print(f"    Rendered {idx}/50 rainbow samples...")
    print("[OK] All 50 Rainbow Designs Generated Successfully!")
    generate_contact_sheets()
    print("[OK] All 5 Rainbow Contact Sheets Generated!")

if __name__ == "__main__":
    main()
