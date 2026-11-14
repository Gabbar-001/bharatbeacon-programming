import os
import sys
import time
import subprocess
from pathlib import Path

# Add project root
sys.path.append(str(Path(__file__).resolve().parent.parent))
import config
from content_plan.day1_shorts_data import DAY1_SHORTS
from src.tech_animator import (
    render_code_card,
    render_shorts_frame,
    COLOR_PYTHON,
    COLOR_JAVA,
    COLOR_MONGO,
    COLOR_SQL
)
from src.tts_engine import generate_voiceover_sync

COLOR_MAP = {
    "python": COLOR_PYTHON,
    "java": COLOR_JAVA,
    "mongodb": COLOR_MONGO,
    "sql": COLOR_SQL
}

SHORTS_OUT = config.SHORTS_OUTPUT_DIR
SHORTS_OUT.mkdir(parents=True, exist_ok=True)
TEMP_BUILD = config.TEMP_DIR / "day1_shorts_build"
TEMP_BUILD.mkdir(parents=True, exist_ok=True)

print("=" * 65)
print(f"  RENDERING ALL {len(DAY1_SHORTS)} DAY 1 TECH SHORTS (9:16 VERTICAL)")
print("=" * 65)

rendered_shorts = []
start_total = time.time()

for idx, item in enumerate(DAY1_SHORTS, start=1):
    hr = item["hour_ist"]
    track = item["track"]
    title = item["title"]
    accent = COLOR_MAP.get(track, COLOR_PYTHON)

    out_file = SHORTS_OUT / f"SHORT_DAY01_H{hr:02d}_{track.upper()}.mp4"
    print(f"\n[{idx:2d}/{len(DAY1_SHORTS)}] Hour {hr:02d}:00 IST [{track.upper()}] -> {out_file.name}")
    t0 = time.time()

    # 1. Voiceover Synthesis
    audio_path = TEMP_BUILD / f"audio_h{hr:02d}_{track}.mp3"
    dur = generate_voiceover_sync(item["speech"], audio_path, is_shorts=True)
    print(f"      • Voiceover: {dur:.1f}s")

    # 2. Syntax-Highlighted Code Card
    code_card = render_code_card(
        item["code"],
        language=track,
        width=920,
        height=380,
        filename=f"day1_{track}.code",
        font_size=22
    )

    # 3. 9:16 Kinetic Shorts Frame
    frame = render_shorts_frame(
        track_badge=item["badge"],
        hook_text=item["hook_text"],
        code_img=code_card,
        caption_text=item["caption"],
        riddle_text=item["riddle_text"],
        accent_color=accent
    )
    frame_path = TEMP_BUILD / f"frame_h{hr:02d}_{track}.jpg"
    frame.save(frame_path, quality=95)

    # 4. Ultrafast FFmpeg Render
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-framerate", "30",
        "-i", str(frame_path),
        "-i", str(audio_path),
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-ar", "44100",
        "-b:a", "192k",
        "-t", f"{dur:.3f}",
        str(out_file)
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    elapsed = time.time() - t0
    size_kb = out_file.stat().st_size / 1024
    print(f"      • Rendered {size_kb:.1f} KB in {elapsed:.1f}s")

    rendered_shorts.append({
        "hour_ist": hr,
        "track": track,
        "title": title,
        "video_path": str(out_file),
        "playlist_key": item["playlist_key"],
        "duration_seconds": dur
    })

print("\n" + "=" * 65)
print(f"  SUCCESS: ALL {len(rendered_shorts)} SHORTS RENDERED IN {time.time()-start_total:.1f}s!")
print("=" * 65)
