import os
import sys
import subprocess
from pathlib import Path

# Add project root
sys.path.append(str(Path(__file__).resolve().parent.parent))
import config
from src.tech_animator import (
    render_code_card,
    render_memory_diagram,
    render_split_comparison_card,
    render_presentation_slide,
    render_shorts_frame,
    COLOR_PYTHON
)
from src.tts_engine import generate_voiceover_sync, get_audio_duration

DEMO_DIR = Path("output/demos")
DEMO_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DEMO = config.TEMP_DIR / "demo_work"
TEMP_DEMO.mkdir(parents=True, exist_ok=True)

VOICE_FEMALE = "en-IN-NeerjaExpressiveNeural"

def render_video_segment(img_path: Path, audio_path: Path, output_mp4: Path, duration: float) -> bool:
    """Renders a single video clip from an image and an audio file using FFmpeg."""
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-framerate", "30",
        "-i", str(img_path),
        "-i", str(audio_path),
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-g", "30",
        "-keyint_min", "30",
        "-c:a", "aac",
        "-ar", "44100",
        "-ac", "2",
        "-b:a", "192k",
        "-t", f"{duration:.3f}",
        str(output_mp4)
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"Segment render failed for {output_mp4.name}: {res.stderr[-300:]}")
        return False
    return True

def concat_segments(segment_files: list, final_output: Path) -> bool:
    concat_list = TEMP_DEMO / "concat_list.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for seg in segment_files:
            escaped = str(seg.resolve()).replace("\\", "/")
            f.write(f"file '{escaped}'\n")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list),
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "44100",
        "-ac", "2",
        "-movflags", "+faststart",
        str(final_output)
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if concat_list.exists():
        concat_list.unlink()
    return res.returncode == 0

def build_longform_demo() -> Path:
    print("\n--- [1/2] Building Day 1 Long-Form Masterclass Demo (16:9) ---")

    slides_data = [
        {
            "id": "slide_1",
            "title": "Variables Are Pointers, Not Boxes",
            "bullets": [
                "Variables in Python store memory references, not raw values.",
                "Assigning a = b creates a second pointer to the EXACT same object in RAM.",
                "Modifying mutable objects like lists through b alters a instantly!"
            ],
            "card_type": "code",
            "code": "a = [1, 2, 3]\nb = a  # Does NOT copy!\nb.append(99)\n\nprint(f\"a: {a}\")\n# Output: [1, 2, 3, 99]\nprint(f\"id(a) == id(b): {id(a) == id(b)}\")\n# True! Shared Reference!",
            "speech": (
                "Welcome to Day 1 of our 60-Day Python Masterclass. Most programmers believe a variable "
                "in Python is a box that holds a value. That mental model is dead wrong. In Python, variables "
                "are sticky notes pointing to memory blocks in RAM."
            )
        },
        {
            "id": "slide_2",
            "title": "Stack vs Heap: What Happens in RAM",
            "bullets": [
                "Stack: High-speed thread memory storing local variable references.",
                "Heap: Global memory pool where objects and lists physically exist.",
                "Garbage Collector tracks references and frees memory when count reaches 0."
            ],
            "card_type": "memory",
            "speech": (
                "When you execute Python code, local variable names live on the fast thread Stack, but the actual "
                "objects live on the Heap. When you write a equals b, Python does not duplicate the list. "
                "Both variables point to the exact same memory address."
            )
        },
        {
            "id": "slide_3",
            "title": "Anti-Pattern: Mutable Default Arguments",
            "bullets": [
                "Default arguments are evaluated ONCE when the function is defined.",
                "Passing a mutable list as default makes all function calls share that list!",
                "Always use perms=None and initialize the list inside the function."
            ],
            "card_type": "split",
            "bad_code": "# ❌ THE ROOKIE TRAP\ndef register(user, perms=[]):\n    perms.append('read')\n    return perms\n\nadmin = register('admin')\nguest = register('guest')\n# guest gets ['read', 'read']!",
            "good_code": "# ✅ THE PRO FIX\ndef register(user, perms=None):\n    if perms is None:\n        perms = []\n    perms.append('read')\n    return perms\n\n# Fresh list created per call!",
            "speech": (
                "Here is the rookie trap that breaks production microservices. Defining a function with a default "
                "empty list evaluates that list only once at module load time. Every single user call shares that "
                "exact same list in memory. Always use None and initialize inside."
            )
        },
        {
            "id": "slide_4",
            "title": "FAANG Interview Challenge: Integer Caching",
            "bullets": [
                "Python pre-allocates small integers from -5 to 256 at startup for speed.",
                "x = 256; y = 256 -> x is y is True (Reuses cached memory address).",
                "x = 257; y = 257 -> x is y is False (Allocates separate memory blocks!)."
            ],
            "card_type": "code",
            "code": "x = 256\ny = 256\nprint(x is y)  # True! (Pre-allocated in cache)\n\na = 257\nb = 257\nprint(a is b)  # False! (Separate Heap blocks)",
            "speech": (
                "Here is a classic FAANG interview riddle. Why does x is y return True for 256, but False for 257? "
                "Because Python pre-allocates small integers from negative five to 256 at startup. "
                "Drop your answer to today's homework in the comments, and subscribe for Day 2 tomorrow."
            )
        }
    ]

    segments = []
    total_slides = len(slides_data)

    for idx, s in enumerate(slides_data, start=1):
        print(f"   Rendering Masterclass Slide {idx}/{total_slides}: {s['title']}")

        # 1. Generate Voiceover
        audio_path = TEMP_DEMO / f"long_{s['id']}.mp3"
        dur = generate_voiceover_sync(s["speech"], audio_path, is_shorts=False, voice=VOICE_FEMALE)
        print(f"      Voiceover duration: {dur:.2f}s")

        # 2. Render Visual Card
        if s["card_type"] == "code":
            card_img = render_code_card(s["code"], language="python", width=840, height=480, filename="memory.py")
        elif s["card_type"] == "memory":
            card_img = render_memory_diagram(width=840, height=480)
        elif s["card_type"] == "split":
            card_img = render_split_comparison_card(s["bad_code"], s["good_code"], width=860, height=480)
        else:
            card_img = None

        # 3. Render Full Slide
        slide_img = render_presentation_slide(
            track_title="PYTHON MASTERCLASS",
            episode_info="DAY 01 OF 60",
            slide_index=idx,
            total_slides=total_slides,
            slide_title=s["title"],
            bullet_points=s["bullets"],
            right_image=card_img,
            accent_color=COLOR_PYTHON
        )
        slide_img_path = TEMP_DEMO / f"long_{s['id']}.jpg"
        slide_img.save(slide_img_path, quality=95)

        # 4. Render Video Segment
        seg_mp4 = TEMP_DEMO / f"seg_long_{s['id']}.mp4"
        render_video_segment(slide_img_path, audio_path, seg_mp4, dur)
        segments.append(seg_mp4)

    final_longform = DEMO_DIR / "demo_python_day1_masterclass.mp4"
    concat_segments(segments, final_longform)
    print(f"[OK] Masterclass Video Ready: {final_longform}")
    return final_longform

def build_shorts_demo() -> Path:
    print("\n--- [2/2] Building Day 1 Viral Short Demo (9:16) ---")

    short_code = """a = [1, 2, 3]
b = a  # Pointer copied!
b.append(99)

print(a)
# Output: [1, 2, 3, 99] 😱"""

    speech_short = (
        "Why does a equals b in Python break your code at 2 AM? Look at this code snippet. "
        "You think you made a copy, but when you append to b, a changes too! "
        "Both variables point to the exact same memory address. "
        "Never assign lists without using dot copy! Full Day 1 Masterclass link in the comments below."
    )

    audio_path = TEMP_DEMO / "short_audio.mp3"
    dur = generate_voiceover_sync(speech_short, audio_path, is_shorts=True, voice=VOICE_FEMALE)
    print(f"   Short Voiceover duration: {dur:.2f}s")

    code_card = render_code_card(short_code, language="python", width=920, height=380, filename="riddle.py", font_size=24)
    short_frame = render_shorts_frame(
        track_badge="PYTHON TRICK #1 • DAY 1",
        hook_text="Why a = b in Python breaks production at 2 AM",
        code_img=code_card,
        caption_text="Never assign lists without .copy()!",
        riddle_text="Output: [1, 2, 3, 99] 😱",
        accent_color=COLOR_PYTHON
    )
    short_frame_path = TEMP_DEMO / "short_frame.jpg"
    short_frame.save(short_frame_path, quality=95)

    final_short = DEMO_DIR / "demo_python_day1_short.mp4"
    render_video_segment(short_frame_path, audio_path, final_short, dur)
    print(f"[OK] Short Video Ready: {final_short}")
    return final_short

if __name__ == "__main__":
    longform_out = build_longform_demo()
    shorts_out = build_shorts_demo()
    print("\n" + "=" * 60)
    print("ALL DAY 1 DEMOS SUCCESSFULLY GENERATED!")
    print(f"1. Masterclass (16:9): {longform_out}")
    print(f"2. Viral Short  (9:16): {shorts_out}")
    print("=" * 60)
