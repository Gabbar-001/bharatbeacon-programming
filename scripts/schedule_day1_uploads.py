import os
import sys
import json
import time
from pathlib import Path

# Add project root
sys.path.append(str(Path(__file__).resolve().parent.parent))
import config
from src.youtube_publisher import upload_video, get_youtube_service

MANIFEST_PATH = config.OUTPUT_DIR / "day1_production_manifest.json"
PROGRESS_PATH = config.OUTPUT_DIR / "day1_upload_progress.json"

if not MANIFEST_PATH.exists():
    print(f"Error: Manifest file {MANIFEST_PATH} not found.")
    sys.exit(1)

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

# Load existing progress
uploaded_ids = {}
if PROGRESS_PATH.exists():
    try:
        with open(PROGRESS_PATH, "r", encoding="utf-8") as f:
            uploaded_ids = json.load(f)
    except Exception:
        uploaded_ids = {}

print("=" * 70)
print(f"  SCHEDULING DAY 1 TECH VIDEOS TO YOUTUBE")
print(f"  Total in manifest: {len(manifest)} | Already uploaded: {len(uploaded_ids)}")
print("=" * 70)

for idx, item in enumerate(manifest, start=1):
    vpath = item["video_path"]
    title = item["title"]
    schedule_ist = item["schedule_ist"]
    publish_utc = item["publish_at_utc"]
    badge = "[MASTERCLASS]" if item["type"] == "masterclass" else "[SHORT]      "

    if vpath in uploaded_ids:
        vid = uploaded_ids[vpath].get("video_id")
        print(f"[{idx:2d}/{len(manifest)}] ALREADY SCHEDULED: {badge} {schedule_ist} -> https://youtu.be/{vid}")
        continue

    print(f"\n[{idx:2d}/{len(manifest)}] Scheduling: {badge} {title[:50]}...")
    print(f"     Target Release: {schedule_ist} ({publish_utc})")
    print(f"     Playlist:       {item.get('playlist_key')} ({item.get('playlist_id')})")

    meta = {
        "title": title,
        "description": item["description"],
        "video_path": vpath,
        "tags": item["tags"],
        "playlist_id": item.get("playlist_id"),
        "category_id": "27",  # Education
        "publish_at": publish_utc
    }

    try:
        vid = upload_video(meta)
        if vid and vid != "staged_locally":
            uploaded_ids[vpath] = {
                "video_id": vid,
                "title": title,
                "schedule_ist": schedule_ist,
                "publish_at_utc": publish_utc,
                "playlist_id": item.get("playlist_id"),
                "type": item["type"],
                "uploaded_at": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            with open(PROGRESS_PATH, "w", encoding="utf-8") as pf:
                json.dump(uploaded_ids, pf, indent=2)
            print(f"     --> SUCCESS! Scheduled: https://youtu.be/{vid}")
        else:
            print(f"     --> Upload returned: {vid}")
    except Exception as e:
        err_msg = str(e)
        print(f"     [!] Upload failed: {err_msg}")
        if "quotaExceeded" in err_msg or "uploadLimitExceeded" in err_msg:
            print("\n[QUOTA NOTICE] YouTube API daily upload quota reached.")
            print("Quota resets daily at Midnight Pacific Time (PT) / 1:30 PM IST.")
            break
        else:
            # Continue to next video if single item failure
            continue

print("\n" + "=" * 70)
print(f"  BATCH COMPLETED: {len(uploaded_ids)} / {len(manifest)} VIDEOS SCHEDULED ON YOUTUBE!")
print("=" * 70)
