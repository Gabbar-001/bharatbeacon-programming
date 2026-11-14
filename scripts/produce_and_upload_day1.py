import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Add project root
sys.path.append(str(Path(__file__).resolve().parent.parent))
import config
from content_plan.day1_data import DAY1_MASTERCLASSES
from src.tech_masterclass_builder import build_full_masterclass
from src.youtube_publisher import upload_video

OUT_DIR = config.LONGFORM_OUTPUT_DIR
OUT_DIR.mkdir(parents=True, exist_ok=True)

with open("playlists.json", "r", encoding="utf-8") as f:
    playlist_map = json.load(f)

print("=" * 65)
print("   PRODUCING & SCHEDULING ALL 4 DAY 1 MASTERCLASSES")
print("=" * 65)

results = []

for course in DAY1_MASTERCLASSES:
    track = course["track"]
    output_video = OUT_DIR / f"MASTERCLASS_DAY01_{track.upper()}.mp4"

    # 1. Build the full masterclass presentation video
    res = build_full_masterclass(course, output_video)

    # 2. Get target playlist ID
    pl_key = course["playlist_key"]
    playlist_id = playlist_map.get(pl_key, {}).get("id")

    # 3. Format description with chapter timestamps and links
    chapter_text = "\n".join(res["chapters"])
    description = f"""{course['title']}

Welcome to Day 1 of our 60-Day Full-Stack Bootcamp!
Master production-grade coding with visual PPT presentations, memory diagrams, and hands-on code examples.

TIMESTAMPS:
{chapter_text}

📚 PLAYLIST: {playlist_map.get(pl_key, {}).get('title')}
👉 Subscribe for daily episodes across Python, Java, MongoDB, and SQL!

#Coding #Programming #{track.capitalize()} #SoftwareEngineering #TechBootcamp
"""

    metadata = {
        "title": course["title"][:100],
        "description": description,
        "video_path": str(output_video),
        "tags": course["tags"],
        "playlist_id": playlist_id,
        "publish_at": course["publish_at"]
    }

    # 4. Upload & Schedule to YouTube
    print(f"\nUploading and Scheduling {track.upper()} Masterclass...")
    video_id = upload_video(metadata)

    results.append({
        "track": track,
        "title": course["title"],
        "video_id": video_id,
        "playlist_id": playlist_id,
        "publish_at": course["publish_at"],
        "duration": res["duration_seconds"]
    })

print("\n" + "=" * 65)
print("   DAY 1 MASTERCLASSES COMPLETED & SCHEDULED ON YOUTUBE!")
print("=" * 65)
for r in results:
    m = int(r["duration"] // 60)
    s = int(r["duration"] % 60)
    print(f"• [{r['track'].upper():7s}] {r['title'][:45]}... ({m:02d}:{s:02d}) -> ID: {r['video_id']}")
