import os
import sys
import subprocess
from pathlib import Path
from typing import Dict, List

# Add project root
sys.path.append(str(Path(__file__).resolve().parent.parent))
import config
from src.tech_animator import (
    render_code_card,
    render_memory_diagram,
    render_split_comparison_card,
    render_presentation_slide,
    COLOR_PYTHON,
    COLOR_JAVA,
    COLOR_MONGO,
    COLOR_SQL
)
from src.tts_engine import generate_voiceover_sync, get_audio_duration

VOICE_NARRATOR = "en-IN-NeerjaExpressiveNeural"
TEMP_BUILD = config.TEMP_DIR / "masterclass_build"
TEMP_BUILD.mkdir(parents=True, exist_ok=True)

def render_segment(img_path: Path, audio_path: Path, output_mp4: Path, duration: float) -> bool:
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
    return res.returncode == 0

def concat_segments(segment_files: List[Path], final_output: Path) -> bool:
    concat_list = TEMP_BUILD / f"concat_{final_output.stem}.txt"
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

def build_full_masterclass(course_data: Dict, output_path: Path) -> Dict:
    """
    Renders a full 10-12 minute masterclass presentation with PPT-style animated slides,
    code cards, memory diagrams, and synchronized audio.
    """
    track = course_data["track"]
    title = course_data["title"]
    accent = course_data["accent_color"]
    slides = course_data["slides"]

    print("\n" + "=" * 65)
    print(f"  BUILDING FULL MASTERCLASS: {title.upper()}")
    print(f"  Track: {track} | Slides: {len(slides)}")
    print("=" * 65)

    segments = []
    total_slides = len(slides)
    total_duration = 0.0
    chapters = []

    for idx, s in enumerate(slides, start=1):
        slide_id = f"{track}_s{idx}"
        slide_title = s["title"]
        print(f"   [{idx:2d}/{total_slides}] Rendering: {slide_title} ...")

        # Track chapter timestamp
        m = int(total_duration // 60)
        sec = int(total_duration % 60)
        chapters.append(f"{m:02d}:{sec:02d} {slide_title}")

        # 1. Voiceover
        audio_path = TEMP_BUILD / f"audio_{slide_id}.mp3"
        dur = generate_voiceover_sync(s["speech"], audio_path, is_shorts=False, voice=VOICE_NARRATOR)
        total_duration += dur
        print(f"         Audio: {dur:.1f}s")

        # 2. Visual Card
        card_img = None
        card_type = s.get("card_type")
        if card_type == "code":
            card_img = render_code_card(s["code"], language=track, width=840, height=480, filename=s.get("filename", "main.py"))
        elif card_type == "memory":
            card_img = render_memory_diagram(width=840, height=480)
        elif card_type == "split":
            card_img = render_split_comparison_card(s["bad_code"], s["good_code"], width=860, height=480)

        # 3. Full Slide Frame
        slide_img = render_presentation_slide(
            track_title=course_data["track_title"],
            episode_info=course_data["episode_info"],
            slide_index=idx,
            total_slides=total_slides,
            slide_title=slide_title,
            bullet_points=s["bullets"],
            right_image=card_img,
            accent_color=accent
        )
        slide_img_path = TEMP_BUILD / f"slide_{slide_id}.jpg"
        slide_img.save(slide_img_path, quality=95)

        # 4. Render Video Segment
        seg_mp4 = TEMP_BUILD / f"seg_{slide_id}.mp4"
        render_segment(slide_img_path, audio_path, seg_mp4, dur)
        segments.append(seg_mp4)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    concat_segments(segments, output_path)

    m = int(total_duration // 60)
    sec = int(total_duration % 60)
    print(f"\n[OK] FULL MASTERCLASS READY: {output_path.name} ({m:02d}:{sec:02d})")

    return {
        "title": title,
        "video_path": str(output_path),
        "duration_seconds": total_duration,
        "chapters": chapters,
        "track": track
    }
