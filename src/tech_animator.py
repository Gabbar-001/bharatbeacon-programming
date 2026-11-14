import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from PIL import Image, ImageDraw, ImageFont
import pygments
from pygments.lexers import get_lexer_by_name, PythonLexer, JavaLexer, SqlLexer, JsonLexer
from pygments.token import Token

# Add project root
sys.path.append(str(Path(__file__).resolve().parent.parent))
import config

FONT_MONO = config.ASSETS_DIR / "fonts" / "consolab.ttf"
FONT_TITLE = config.ASSETS_DIR / "fonts" / "segoeuib.ttf"
FONT_TEXT = config.ASSETS_DIR / "fonts" / "arialbd.ttf"

# Tokyo Night Theme Palette
COLOR_BG = (15, 17, 26)         # Deep slate background
COLOR_CARD = (26, 27, 38)       # Elevated card background
COLOR_CARD_BORDER = (41, 46, 66)
COLOR_TEXT_MAIN = (240, 243, 246)
COLOR_TEXT_MUTED = (110, 115, 141)
COLOR_ACCENT = (122, 162, 247)   # Python/Tech Cyan
COLOR_PYTHON = (56, 189, 248)   # Bright Sky Blue
COLOR_JAVA = (251, 146, 60)     # Orange
COLOR_MONGO = (52, 211, 153)    # Emerald Green
COLOR_SQL = (168, 85, 247)      # Violet

# Pygments Token Color Map (Tokyo Night)
TOKEN_COLORS = {
    Token.Keyword: (247, 118, 142),           # Pink/Rose
    Token.Keyword.Constant: (255, 158, 100),  # Orange
    Token.Keyword.Declaration: (187, 154, 247),# Violet
    Token.Keyword.Namespace: (247, 118, 142),
    Token.Name.Function: (122, 162, 247),     # Cyan/Blue
    Token.Name.Class: (224, 175, 104),        # Yellow/Gold
    Token.Name.Builtin: (122, 162, 247),
    Token.String: (158, 206, 106),            # Bright Green
    Token.Number: (255, 158, 100),            # Orange
    Token.Operator: (137, 221, 255),          # Ice Blue
    Token.Punctuation: (187, 194, 207),
    Token.Comment: (86, 95, 137),             # Muted Grey/Lavender
    Token.Text: (192, 202, 245),              # Soft White
}

def get_font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(str(path), size)
    except Exception:
        return ImageFont.load_default()

def draw_rounded_rect(draw: ImageDraw.Draw, bbox, radius: int, fill, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def render_code_card(
    code_text: str,
    language: str = "python",
    width: int = 800,
    height: int = 500,
    filename: str = "script.py",
    font_size: int = 22
) -> Image.Image:
    """
    Renders a stunning macOS-style VS Code window with Pygments syntax highlighting.
    """
    card = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)

    # Base Card
    draw_rounded_rect(draw, [0, 0, width - 1, height - 1], radius=16, fill=COLOR_CARD, outline=COLOR_CARD_BORDER, width=2)

    # Title Bar Header
    header_h = 44
    draw_rounded_rect(draw, [0, 0, width - 1, header_h], radius=16, fill=(31, 35, 53))
    draw.rectangle([0, header_h - 16, width - 1, header_h], fill=(31, 35, 53)) # Fill bottom round corners of header
    draw.line([(0, header_h), (width - 1, header_h)], fill=COLOR_CARD_BORDER, width=1)

    # macOS Window Dots (Red, Yellow, Green)
    dots = [(22, 22, (255, 95, 86)), (42, 22, (255, 189, 46)), (62, 22, (39, 201, 63))]
    for x, y, c in dots:
        draw.ellipse([x - 6, y - 6, x + 6, y + 6], fill=c)

    # Tab filename
    font_tab = get_font(FONT_TEXT, 15)
    draw.text((width // 2, 22), filename, font=font_tab, fill=COLOR_TEXT_MUTED, anchor="mm")

    # Syntax Highlighting with Pygments
    try:
        lexer = get_lexer_by_name(language.lower(), stripall=True)
    except Exception:
        lexer = PythonLexer(stripall=True)

    font_code = get_font(FONT_MONO, font_size)
    font_ln = get_font(FONT_MONO, font_size - 4)

    start_x = 75
    start_y = header_h + 20
    line_spacing = font_size + 10

    lines = code_text.strip().split("\n")
    for line_idx, line in enumerate(lines):
        curr_y = start_y + (line_idx * line_spacing)
        if curr_y > height - 30:
            break

        # Line Number
        ln_str = f"{line_idx + 1:2d}"
        draw.text((25, curr_y + 2), ln_str, font=font_ln, fill=(70, 75, 100))

        # Divider line next to line numbers
        draw.line([(58, start_y - 10), (58, height - 20)], fill=(36, 40, 59), width=1)

        # Tokens
        tokens = list(pygments.lex(line, lexer=lexer))
        curr_x = start_x

        for ttype, text in tokens:
            color = COLOR_TEXT_MAIN
            for k in TOKEN_COLORS:
                if ttype in k:
                    color = TOKEN_COLORS[k]
                    break

            draw.text((curr_x, curr_y), text, font=font_code, fill=color)
            try:
                w = font_code.getlength(text)
            except Exception:
                try:
                    w = draw.textlength(text, font=font_code)
                except Exception:
                    w = len(text) * 11
            curr_x += int(w)

    return card

def render_memory_diagram(width: int = 800, height: int = 500) -> Image.Image:
    """
    Renders an animated Stack vs Heap memory diagram showing pointer references.
    """
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw_rounded_rect(draw, [0, 0, width - 1, height - 1], radius=16, fill=COLOR_CARD, outline=COLOR_CARD_BORDER, width=2)

    font_h = get_font(FONT_TITLE, 20)
    font_b = get_font(FONT_TEXT, 16)
    font_mono = get_font(FONT_MONO, 18)

    # Header
    draw.text((width // 2, 28), "UNDER THE HOOD: STACK vs HEAP MEMORY", font=font_h, fill=COLOR_PYTHON, anchor="mm")
    draw.line([(30, 52), (width - 30, 52)], fill=COLOR_CARD_BORDER, width=1)

    # Left: Stack Box
    stack_box = [40, 75, 280, height - 40]
    draw_rounded_rect(draw, stack_box, radius=12, fill=(20, 24, 38), outline=(56, 189, 248), width=2)
    draw.text((160, 105), "STACK FRAME", font=font_h, fill=(56, 189, 248), anchor="mm")
    draw.text((160, 130), "(Variable Sticky Notes)", font=font_b, fill=COLOR_TEXT_MUTED, anchor="mm")

    # Variable Cards inside Stack
    var_a = [60, 160, 260, 230]
    draw_rounded_rect(draw, var_a, radius=8, fill=(30, 41, 59), outline=(56, 189, 248), width=1)
    draw.text((160, 185), "Variable: a", font=font_mono, fill=(240, 243, 246), anchor="mm")
    draw.text((160, 210), "ptr -> 0x7FFE", font=font_mono, fill=(122, 162, 247), anchor="mm")

    var_b = [60, 260, 260, 330]
    draw_rounded_rect(draw, var_b, radius=8, fill=(30, 41, 59), outline=(56, 189, 248), width=1)
    draw.text((160, 285), "Variable: b", font=font_mono, fill=(240, 243, 246), anchor="mm")
    draw.text((160, 310), "ptr -> 0x7FFE", font=font_mono, fill=(122, 162, 247), anchor="mm")

    # Right: Heap Box
    heap_box = [420, 75, width - 40, height - 40]
    draw_rounded_rect(draw, heap_box, radius=12, fill=(20, 24, 38), outline=(158, 206, 106), width=2)
    draw.text(((420 + width - 40) // 2, 105), "SHARED HEAP MEMORY", font=font_h, fill=(158, 206, 106), anchor="mm")
    draw.text(((420 + width - 40) // 2, 130), "(Actual Objects in RAM)", font=font_b, fill=COLOR_TEXT_MUTED, anchor="mm")

    # Heap Object Box
    obj_box = [460, 190, width - 80, 310]
    draw_rounded_rect(draw, obj_box, radius=10, fill=(30, 50, 40), outline=(158, 206, 106), width=2)
    draw.text(((460 + width - 80) // 2, 225), "Address: 0x7FFE", font=font_mono, fill=(158, 206, 106), anchor="mm")
    draw.text(((460 + width - 80) // 2, 265), "List: [1, 2, 3, 99]", font=get_font(FONT_MONO, 22), fill=(255, 255, 255), anchor="mm")

    # Pointer Arrows from Stack to Heap
    draw.line([(260, 195), (460, 235)], fill=(56, 189, 248), width=3)
    draw.polygon([(460, 235), (445, 225), (448, 242)], fill=(56, 189, 248))

    draw.line([(260, 295), (460, 265)], fill=(56, 189, 248), width=3)
    draw.polygon([(460, 265), (448, 255), (445, 275)], fill=(56, 189, 248))

    # Bottom Callout Badge
    callout = [60, height - 90, width - 60, height - 55]
    draw_rounded_rect(draw, callout, radius=6, fill=(40, 25, 30), outline=(247, 118, 142), width=1)
    draw.text((width // 2, height - 73), "Both variables point to the same memory block! id(a) == id(b)", font=font_b, fill=(247, 118, 142), anchor="mm")

    return img

def render_split_comparison_card(
    bad_code: str,
    good_code: str,
    bad_label: str = "❌ THE ROOKIE TRAP",
    good_label: str = "✅ THE INDUSTRY PRO FIX",
    width: int = 840,
    height: int = 500
) -> Image.Image:
    """
    Renders an animated side-by-side comparison card: Anti-Pattern vs Clean Code.
    """
    card = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)

    col_w = (width - 30) // 2

    # Left: Bad Code
    draw_rounded_rect(draw, [0, 0, col_w, height - 1], radius=14, fill=(28, 18, 24), outline=(247, 118, 142), width=2)
    draw.rectangle([0, 0, col_w, 42], fill=(45, 20, 30))
    draw.text((col_w // 2, 21), bad_label, font=get_font(FONT_TITLE, 15), fill=(247, 118, 142), anchor="mm")

    font_code = get_font(FONT_MONO, 17)
    for idx, l in enumerate(bad_code.strip().split("\n")):
        draw.text((20, 58 + idx * 26), l, font=font_code, fill=(240, 200, 200))

    # Right: Good Code
    start_r = col_w + 20
    draw_rounded_rect(draw, [start_r, 0, width - 1, height - 1], radius=14, fill=(18, 30, 24), outline=(52, 211, 153), width=2)
    draw.rectangle([start_r, 0, width - 1, 42], fill=(20, 45, 30))
    draw.text((start_r + col_w // 2, 21), good_label, font=get_font(FONT_TITLE, 15), fill=(52, 211, 153), anchor="mm")

    for idx, l in enumerate(good_code.strip().split("\n")):
        draw.text((start_r + 20, 58 + idx * 26), l, font=font_code, fill=(200, 245, 220))

    return card

def render_presentation_slide(
    track_title: str = "PYTHON MASTERCLASS",
    episode_info: str = "DAY 01 OF 60",
    slide_index: int = 1,
    total_slides: int = 5,
    slide_title: str = "Variables & Memory Allocation",
    bullet_points: List[str] = None,
    right_image: Image.Image = None,
    width: int = 1920,
    height: int = 1080,
    accent_color = COLOR_PYTHON
) -> Image.Image:
    """
    Renders a complete, professional 16:9 masterclass presentation slide.
    """
    slide = Image.new("RGB", (width, height), COLOR_BG)
    draw = ImageDraw.Draw(slide)

    # Subtle ambient background grid/gradient accents
    for x in range(0, width, 120):
        draw.line([(x, 0), (x, height)], fill=(20, 23, 34), width=1)
    for y in range(0, height, 120):
        draw.line([(0, y), (width, y)], fill=(20, 23, 34), width=1)

    # Top Header Bar
    draw.rectangle([0, 0, width, 100], fill=(20, 24, 38))
    draw.line([(0, 100), (width, 100)], fill=COLOR_CARD_BORDER, width=2)

    # Track Badge (Top-Left)
    badge_w = 360
    draw_rounded_rect(draw, [60, 24, 60 + badge_w, 76], radius=8, fill=(30, 41, 59), outline=accent_color, width=2)
    font_badge = get_font(FONT_TITLE, 18)
    draw.text((60 + badge_w // 2, 50), f"{track_title} • {episode_info}", font=font_badge, fill=accent_color, anchor="mm")

    # Slide Counter (Top-Right)
    font_meta = get_font(FONT_TITLE, 18)
    draw.text((width - 60, 50), f"SLIDE {slide_index:02d} / {total_slides:02d}", font=font_meta, fill=COLOR_TEXT_MUTED, anchor="rm")

    # Slide Headline
    font_headline = get_font(FONT_TITLE, 42)
    draw.text((60, 140), slide_title, font=font_headline, fill=COLOR_TEXT_MAIN)
    # Accent Underline
    draw.line([(60, 195), (60 + font_headline.getlength(slide_title), 195)], fill=accent_color, width=4)

    # Content Area
    content_y = 230
    left_w = 880

    if bullet_points:
        font_bullet = get_font(FONT_TEXT, 24)
        bullet_spacing = 90

        for b_idx, bullet in enumerate(bullet_points):
            by = content_y + (b_idx * bullet_spacing)
            if by > height - 160:
                break

            # Glowing bullet icon / dot
            draw_rounded_rect(draw, [60, by + 4, 95, by + 36], radius=6, fill=(30, 41, 59), outline=accent_color, width=2)
            draw.text((77, by + 20), f"{b_idx + 1}", font=get_font(FONT_TITLE, 16), fill=accent_color, anchor="mm")

            # Word wrap bullet text
            words = bullet.split(" ")
            lines = []
            curr_line = ""
            for w in words:
                test_line = f"{curr_line} {w}".strip()
                if font_bullet.getlength(test_line) < (left_w - 60):
                    curr_line = test_line
                else:
                    lines.append(curr_line)
                    curr_line = w
            if curr_line:
                lines.append(curr_line)

            for line_offset, line_txt in enumerate(lines[:2]):
                draw.text((115, by + line_offset * 32), line_txt, font=font_bullet, fill=COLOR_TEXT_MAIN)

    # Right Card / Image (e.g., Code Card, Memory Diagram, or Split Card)
    if right_image:
        right_x = width - right_image.width - 60
        right_y = content_y + 10
        slide.paste(right_image, (right_x, right_y), right_image if right_image.mode == "RGBA" else None)

    # Bottom Progress / Brand Bar
    bar_h = 45
    draw.rectangle([0, height - bar_h, width, height], fill=(18, 20, 30))
    draw.line([(0, height - bar_h), (width, height - bar_h)], fill=COLOR_CARD_BORDER, width=1)

    draw.text((60, height - bar_h // 2), "60-DAY FULL-STACK DEVELOPER BOOTCAMP", font=get_font(FONT_TITLE, 15), fill=COLOR_TEXT_MUTED, anchor="lm")
    draw.text((width - 60, height - bar_h // 2), "SUBSCRIBE FOR DAILY EPISODES & CODE REPO", font=get_font(FONT_TITLE, 15), fill=accent_color, anchor="rm")

    return slide

def render_shorts_frame(
    track_badge: str = "PYTHON TRICK #1 • DAY 1",
    hook_text: str = "Why a = b in Python will break your production code at 2 AM",
    code_img: Image.Image = None,
    caption_text: str = "Never assign mutable lists without .copy()",
    riddle_text: str = "id(a) == id(b) -> TRUE!",
    width: int = 1080,
    height: int = 1920,
    accent_color = COLOR_PYTHON
) -> Image.Image:
    """
    Renders a stunning 9:16 vertical frame for YouTube Shorts.
    """
    frame = Image.new("RGB", (width, height), COLOR_BG)
    draw = ImageDraw.Draw(frame)

    # Ambient glow in background
    for r in range(400, 0, -20):
        ratio = 1.0 - (r / 400.0)
        c = (int(accent_color[0] * 0.15 * ratio), int(accent_color[1] * 0.15 * ratio), int(accent_color[2] * 0.15 * ratio))
        draw.ellipse([width // 2 - r, 300 - r, width // 2 + r, 300 + r], fill=c)

    # Top Badge
    draw_rounded_rect(draw, [width // 2 - 250, 140, width // 2 + 250, 200], radius=10, fill=(30, 41, 59), outline=accent_color, width=2)
    draw.text((width // 2, 170), track_badge, font=get_font(FONT_TITLE, 22), fill=accent_color, anchor="mm")

    # Big Punchy Hook Headline
    font_hook = get_font(FONT_TITLE, 46)
    words = hook_text.split(" ")
    lines = []
    curr = ""
    for w in words:
        if font_hook.getlength(f"{curr} {w}".strip()) < (width - 160):
            curr = f"{curr} {w}".strip()
        else:
            lines.append(curr)
            curr = w
    if curr:
        lines.append(curr)

    hy = 250
    for l in lines[:3]:
        draw.text((width // 2, hy), l, font=font_hook, fill=COLOR_TEXT_MAIN, anchor="mm")
        hy += 60

    # Middle: Code Card
    if code_img:
        cx = (width - code_img.width) // 2
        cy = hy + 50
        frame.paste(code_img, (cx, cy), code_img if code_img.mode == "RGBA" else None)

    # Bottom Riddle / Output Box
    ry = height - 520
    draw_rounded_rect(draw, [80, ry, width - 80, ry + 120], radius=14, fill=(28, 18, 24), outline=(247, 118, 142), width=2)
    draw.text((width // 2, ry + 35), "⚡ GUESS THE OUTPUT ⚡", font=get_font(FONT_TITLE, 20), fill=(247, 118, 142), anchor="mm")
    draw.text((width // 2, ry + 78), riddle_text, font=get_font(FONT_MONO, 28), fill=(255, 255, 255), anchor="mm")

    # Kinetic Subtitle Ticker Bar
    sub_y = height - 340
    draw_rounded_rect(draw, [60, sub_y, width - 60, sub_y + 110], radius=16, fill=(15, 23, 42), outline=accent_color, width=3)
    draw.text((width // 2, sub_y + 55), caption_text, font=get_font(FONT_TITLE, 30), fill=(255, 255, 0), anchor="mm")

    # CTA Footer
    draw.text((width // 2, height - 120), "Full Day 1 Masterclass link in comments 👇", font=get_font(FONT_TITLE, 26), fill=COLOR_TEXT_MUTED, anchor="mm")

    return frame
