import os
import sys
import json
import time
import subprocess
import importlib
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Add project root
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

import config
from src.tech_masterclass_builder import build_full_masterclass
from src.tech_animator import (
    render_code_card,
    render_shorts_frame,
    COLOR_PYTHON,
    COLOR_JAVA,
    COLOR_MONGO,
    COLOR_SQL
)
from src.tts_engine import generate_voiceover_sync
from src.youtube_publisher import upload_video

COLOR_MAP = {
    "python": COLOR_PYTHON,
    "java": COLOR_JAVA,
    "mongodb": COLOR_MONGO,
    "sql": COLOR_SQL
}

def execute_daily_tech_pipeline():
    IST = timezone(timedelta(hours=5, minutes=30))
    now_ist = datetime.now(IST)
    print("=" * 70)
    print(f"  BHARATBEACON 60-DAY TECH BOOTCAMP: DAILY BATCH PIPELINE")
    print(f"  Execution Time: {now_ist.strftime('%d %b %Y, %I:%M %p IST')}")
    print("=" * 70)

    # 1. Load Day Tracker
    tracker_file = config.OUTPUT_DIR / "current_day_tracker.json"
    tracker = {}
    if tracker_file.exists():
        try:
            with open(tracker_file, "r", encoding="utf-8") as tf:
                tracker = json.load(tf)
        except Exception:
            pass

    target_day = tracker.get("next_day_to_run", 2)
    print(f"\n[BOOTCAMP] Producing Content for DAY {target_day:02d} OF 60")

    # Target date: Tomorrow (starts at 12:00 AM Midnight IST)
    target_date = (now_ist + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    target_date_str = target_date.strftime("%d %B %Y")
    print(f"           Scheduled Release: Starting {target_date_str} at 12:00 AM Midnight IST")

    # 2. Load Playlist IDs
    with open("playlists.json", "r", encoding="utf-8") as f:
        playlist_map = json.load(f)

    # 3. Import Curriculum Data for Target Day
    try:
        data_mod = importlib.import_module(f"content_plan.day{target_day}_data")
        masterclasses = getattr(data_mod, f"DAY{target_day}_MASTERCLASSES")
    except Exception as e:
        print(f"[!] Could not load day{target_day}_data: {e}")
        return

    try:
        shorts_mod = importlib.import_module(f"content_plan.day{target_day}_shorts_data")
        shorts_data = getattr(shorts_mod, f"DAY{target_day}_SHORTS")
    except Exception as e:
        print(f"[!] Could not load day{target_day}_shorts_data: {e}")
        shorts_data = []

    # 4. Render & Schedule 20 Shorts
    print(f"\n[1/2] Rendering & Scheduling {len(shorts_data)} Tech Shorts for Day {target_day}...")
    temp_shorts_dir = config.TEMP_DIR / f"day{target_day}_shorts"
    temp_shorts_dir.mkdir(parents=True, exist_ok=True)
    scheduled_shorts = []

    for idx, s in enumerate(shorts_data, start=1):
        hr = s["hour_ist"]
        track = s["track"]
        pl_key = s["playlist_key"]
        pl_id = playlist_map.get(pl_key, {}).get("id")
        accent = COLOR_MAP.get(track, COLOR_PYTHON)

        out_short = config.SHORTS_OUTPUT_DIR / f"SHORT_DAY{target_day:02d}_H{hr:02d}_{track.upper()}.mp4"
        dt_ist = target_date.replace(hour=hr, minute=0, second=0)
        dt_utc = dt_ist.astimezone(timezone.utc)
        iso_utc = dt_utc.strftime("%Y-%m-%dT%H:%M:%S.000Z")

        # Synthesize audio & frame if not already cached
        if not out_short.exists():
            audio_p = temp_shorts_dir / f"audio_h{hr:02d}.mp3"
            dur = generate_voiceover_sync(s["speech"], audio_p, is_shorts=True)
            card = render_code_card(s["code"], language=track, width=920, height=380, font_size=22)
            frame = render_shorts_frame(
                track_badge=s["badge"],
                hook_text=s["hook_text"],
                code_img=card,
                caption_text=s["caption"],
                riddle_text=s["riddle_text"],
                accent_color=accent
            )
            frame_p = temp_shorts_dir / f"frame_h{hr:02d}.jpg"
            frame.save(frame_p, quality=95)

            cmd = [
                "ffmpeg", "-y", "-loop", "1", "-framerate", "30",
                "-i", str(frame_p), "-i", str(audio_p),
                "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-ar", "44100", "-b:a", "192k",
                "-t", f"{dur:.3f}", str(out_short)
            ]
            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        meta = {
            "title": s["title"][:100],
            "description": f"{s['title']}\n\nDay {target_day} of 60-Day Full-Stack Bootcamp!\nTopic: {s['badge']}\n\nPlaylist: {playlist_map.get(pl_key, {}).get('title')}\nSubscribe to BharatBeacon!\n\n#Shorts #Coding #{track.capitalize()}",
            "video_path": str(out_short),
            "tags": ["Shorts", "Coding", track.capitalize(), "Programming", f"Day{target_day}"],
            "playlist_id": pl_id,
            "category_id": "27",
            "publish_at": iso_utc
        }

        print(f"   [{idx:2d}/{len(shorts_data)}] Scheduling Short H{hr:02d} ({dt_ist.strftime('%I:%M %p IST')})...")
        vid = upload_video(meta)
        scheduled_shorts.append({"hour": hr, "video_id": vid, "title": s["title"]})

        # Post-upload cleanup for this short
        if vid:
            try:
                if out_short.exists():
                    out_short.unlink(missing_ok=True)
                audio_p = temp_shorts_dir / f"audio_h{hr:02d}.mp3"
                frame_p = temp_shorts_dir / f"frame_h{hr:02d}.jpg"
                if audio_p.exists():
                    audio_p.unlink(missing_ok=True)
                if frame_p.exists():
                    frame_p.unlink(missing_ok=True)
            except Exception:
                pass

    # 5. Render & Schedule 4 Full Masterclasses
    print(f"\n[2/2] Rendering & Scheduling 4 Masterclasses for Day {target_day}...")
    masterclass_hours = {"python": 10, "java": 12, "mongodb": 14, "sql": 18}
    scheduled_masterclasses = []

    for mc in masterclasses:
        track = mc["track"]
        hr = masterclass_hours[track]
        pl_key = mc["playlist_key"]
        pl_id = playlist_map.get(pl_key, {}).get("id")

        out_mc = config.LONGFORM_OUTPUT_DIR / f"MASTERCLASS_DAY{target_day:02d}_{track.upper()}.mp4"
        dt_ist = target_date.replace(hour=hr, minute=0, second=0)
        dt_utc = dt_ist.astimezone(timezone.utc)
        iso_utc = dt_utc.strftime("%Y-%m-%dT%H:%M:%S.000Z")

        if not out_mc.exists():
            res = build_full_masterclass(mc, out_mc)
            chapters = res.get("chapters", [])
        else:
            chapters = [f"00:00 Introduction to Day {target_day}"]

        desc = f"""{mc['title']}

Welcome to Day {target_day} of our 60-Day Full-Stack & Database Engineering Masterclass!
Master production-grade coding with visual PPT presentations, memory diagrams, and hands-on code examples.

TIMESTAMPS:
{chr(10).join(chapters)}

📚 PLAYLIST: {playlist_map.get(pl_key, {}).get('title')}
👉 Subscribe to BharatBeacon for daily episodes across Python, Java, MongoDB, and SQL!

#Coding #Programming #{track.capitalize()} #SoftwareEngineering #TechBootcamp
"""

        meta = {
            "title": mc["title"][:100],
            "description": desc,
            "video_path": str(out_mc),
            "tags": mc["tags"],
            "playlist_id": pl_id,
            "category_id": "27",
            "publish_at": iso_utc
        }

        print(f"   Scheduling {track.upper()} Masterclass ({dt_ist.strftime('%I:%M %p IST')})...")
        vid = upload_video(meta)
        scheduled_masterclasses.append({"track": track, "video_id": vid, "title": mc["title"]})

        # Post-upload cleanup for this masterclass
        if vid:
            try:
                if out_mc.exists():
                    out_mc.unlink(missing_ok=True)
            except Exception:
                pass

    # 6. Post-Run Global Disk Cleanup: Purge temp slice segments and frame caches
    print("\n[CLEANUP] Cleaning up intermediate temp segments and cache directories...")
    try:
        import shutil
        if temp_shorts_dir.exists():
            shutil.rmtree(temp_shorts_dir, ignore_errors=True)
        mc_build = config.TEMP_DIR / "masterclass_build"
        if mc_build.exists():
            shutil.rmtree(mc_build, ignore_errors=True)
        # Sweep any remaining temporary build artifacts
        if config.TEMP_DIR.exists():
            for it in config.TEMP_DIR.iterdir():
                if it.is_file():
                    it.unlink(missing_ok=True)
                elif it.is_dir():
                    shutil.rmtree(it, ignore_errors=True)
        print("  [OK] Daily tech disk cleanup completed successfully.")
    except Exception as ce:
        print(f"  [!] Note on post-run cleanup: {ce}")

    # 7. Update Tracker
    tracker["last_scheduled_day"] = target_day
    tracker["next_day_to_run"] = target_day + 1
    tracker[f"day_{target_day}_scheduled_for"] = target_date.strftime("%Y-%m-%d")
    tracker["updated_at"] = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

    with open(tracker_file, "w", encoding="utf-8") as tf:
        json.dump(tracker, tf, indent=2)

    print("\n" + "=" * 70)
    print(f"  DAY {target_day} COMPLETED & SCHEDULED ON YOUTUBE!")
    print(f"  Next scheduled run will produce DAY {target_day + 1}!")
    print("=" * 70)

if __name__ == "__main__":
    execute_daily_tech_pipeline()
