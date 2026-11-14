import sys
from pathlib import Path

# Add project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.tech_animator import (
    render_code_card,
    render_memory_diagram,
    render_split_comparison_card,
    render_presentation_slide,
    render_shorts_frame,
    COLOR_PYTHON
)

out_dir = Path("output/demo_frames")
out_dir.mkdir(parents=True, exist_ok=True)

# 1. Slide 1: Introduction to Python Memory
code_intro = """a = [1, 2, 3]
b = a  # Does NOT copy!
b.append(99)

print(f"a: {a}")
# Output: [1, 2, 3, 99]
print(f"id(a) == id(b): {id(a) == id(b)}")
# True! Shared Reference!"""

card_1 = render_code_card(code_intro, language="python", width=840, height=480, filename="pointers.py")
slide_1 = render_presentation_slide(
    track_title="PYTHON MASTERCLASS",
    episode_info="DAY 01 OF 60",
    slide_index=1,
    total_slides=4,
    slide_title="Variables Are Pointers, Not Boxes",
    bullet_points=[
        "Variables in Python store memory references, not raw values.",
        "Assigning a = b creates a second pointer to the EXACT same object in RAM.",
        "Modifying mutable objects like lists through b alters a instantly!"
    ],
    right_image=card_1,
    accent_color=COLOR_PYTHON
)
slide_1.save(out_dir / "slide_1.jpg", quality=95)
print("[OK] Saved slide_1.jpg")

# 2. Slide 2: Stack vs Heap Memory Architecture
mem_diagram = render_memory_diagram(width=840, height=480)
slide_2 = render_presentation_slide(
    track_title="PYTHON MASTERCLASS",
    episode_info="DAY 01 OF 60",
    slide_index=2,
    total_slides=4,
    slide_title="Stack vs Heap: What Happens in RAM",
    bullet_points=[
        "Stack: High-speed thread memory storing local variable references.",
        "Heap: Global memory pool where objects and lists physically exist.",
        "Garbage Collector tracks references and frees memory when count = 0."
    ],
    right_image=mem_diagram,
    accent_color=COLOR_PYTHON
)
slide_2.save(out_dir / "slide_2.jpg", quality=95)
print("[OK] Saved slide_2.jpg")

# 3. Slide 3: The Production Trap vs Pro Fix
bad_code = """# ❌ THE ROOKIE TRAP
def register(user, perms=[]):
    perms.append("read")
    return perms

admin = register("admin")
guest = register("guest")
# guest gets ['read', 'read']!"""

good_code = """# ✅ THE PRO FIX
def register(user, perms=None):
    if perms is None:
        perms = []
    perms.append("read")
    return perms

# Fresh list created per call!"""

split_card = render_split_comparison_card(bad_code, good_code, width=860, height=480)
slide_3 = render_presentation_slide(
    track_title="PYTHON MASTERCLASS",
    episode_info="DAY 01 OF 60",
    slide_index=3,
    total_slides=4,
    slide_title="Anti-Pattern: Mutable Default Arguments",
    bullet_points=[
        "Default arguments are evaluated ONCE when the function is defined.",
        "Passing a mutable list as default makes all function calls share that list!",
        "Always use perms=None and initialize the list inside the function."
    ],
    right_image=split_card,
    accent_color=COLOR_PYTHON
)
slide_3.save(out_dir / "slide_3.jpg", quality=95)
print("[OK] Saved slide_3.jpg")

# 4. Vertical Shorts Frame
short_code = """a = [1, 2, 3]
b = a
b.append(99)

print(a) # Guess what prints!"""

short_card = render_code_card(short_code, language="python", width=920, height=360, filename="riddle.py", font_size=26)
short_frame = render_shorts_frame(
    track_badge="PYTHON TRICK #1 • DAY 1",
    hook_text="Why a = b in Python breaks production at 2 AM",
    code_img=short_card,
    caption_text="Never assign lists without .copy()!",
    riddle_text="Output: [1, 2, 3, 99] 😱",
    accent_color=COLOR_PYTHON
)
short_frame.save(out_dir / "short_frame.jpg", quality=95)
print("[OK] Saved short_frame.jpg")
