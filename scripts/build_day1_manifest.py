import os
import sys
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Add project root
sys.path.append(str(Path(__file__).resolve().parent.parent))
import config
from content_plan.day1_shorts_data import DAY1_SHORTS
from content_plan.day1_data import DAY1_MASTERCLASSES

with open("playlists.json", "r", encoding="utf-8") as f:
    pls = json.load(f)

IST = timezone(timedelta(hours=5, minutes=30))
# Tonight midnight (Nov 15, 2026, 00:00:00 IST)
base_midnight = datetime(2026, 11, 15, 0, 0, 0, tzinfo=IST)

manifest = []

# 1. 20 Tech Shorts
for s in DAY1_SHORTS:
    hr = s["hour_ist"]
    dt_ist = base_midnight.replace(hour=hr, minute=0, second=0)
    dt_utc = dt_ist.astimezone(timezone.utc)
    iso_utc = dt_utc.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    track = s["track"]
    pl_key = s["playlist_key"]
    pl_id = pls.get(pl_key, {}).get("id")
    vpath = config.SHORTS_OUTPUT_DIR / f"SHORT_DAY01_H{hr:02d}_{track.upper()}.mp4"

    desc = f"""{s['title']}

Day 1 of our 60-Day Full-Stack Bootcamp!
Topic: {s['badge']}
{s['caption']}

📚 Full Day 1 Masterclass playlist: {pls.get(pl_key, {}).get('title')}
👉 Subscribe to BharatBeacon for hourly coding tutorials and interview hacks!

#Shorts #Coding #Programming #{track.capitalize()} #SoftwareEngineering
"""

    manifest.append({
        "type": "short",
        "hour_ist": hr,
        "schedule_ist": dt_ist.strftime("%d %b %Y, %I:%M %p IST"),
        "publish_at_utc": iso_utc,
        "title": s["title"][:100],
        "description": desc,
        "tags": ["Shorts", "Coding", track.capitalize(), "Programming", "Learn to Code", "Computer Science", "Interview"],
        "video_path": str(vpath.resolve()),
        "playlist_key": pl_key,
        "playlist_id": pl_id,
        "track": track,
        "exists": vpath.exists(),
        "file_size_kb": vpath.stat().st_size / 1024 if vpath.exists() else 0
    })

# 2. 4 Long-form Masterclasses
masterclass_schedule = {
    "python": (10, "python_longform"),
    "java": (12, "java_longform"),
    "mongodb": (14, "mongodb_longform"),
    "sql": (18, "sql_longform")
}

for mc in DAY1_MASTERCLASSES:
    track = mc["track"]
    hr, pl_key = masterclass_schedule[track]
    dt_ist = base_midnight.replace(hour=hr, minute=0, second=0)
    dt_utc = dt_ist.astimezone(timezone.utc)
    iso_utc = dt_utc.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    pl_id = pls.get(pl_key, {}).get("id")
    vpath = config.LONGFORM_OUTPUT_DIR / f"MASTERCLASS_DAY01_{track.upper()}.mp4"

    # Chapter breakdown
    chapter_lines = []
    dur_cursor = 0.0
    for idx, sl in enumerate(mc["slides"], start=1):
        m = int(dur_cursor // 60)
        sec = int(dur_cursor % 60)
        chapter_lines.append(f"{m:02d}:{sec:02d} {sl['title']}")
        dur_cursor += 30.0  # Approx

    desc = f"""{mc['title']}

Welcome to Day 1 of our 60-Day Full-Stack & Database Engineering Masterclass!
Master production-grade coding with visual PPT presentations, memory diagrams, and hands-on code examples.

TIMESTAMPS:
{chr(10).join(chapter_lines)}

📚 PLAYLIST: {pls.get(pl_key, {}).get('title')}
👉 Subscribe to BharatBeacon for daily episodes across Python, Java, MongoDB, and SQL!

#Coding #Programming #{track.capitalize()} #SoftwareEngineering #TechBootcamp #Database
"""

    manifest.append({
        "type": "masterclass",
        "hour_ist": hr,
        "schedule_ist": dt_ist.strftime("%d %b %Y, %I:%M %p IST"),
        "publish_at_utc": iso_utc,
        "title": mc["title"][:100],
        "description": desc,
        "tags": mc["tags"],
        "video_path": str(vpath.resolve()),
        "playlist_key": pl_key,
        "playlist_id": pl_id,
        "track": track,
        "exists": vpath.exists(),
        "file_size_kb": vpath.stat().st_size / 1024 if vpath.exists() else 0
    })

manifest.sort(key=lambda x: (x["hour_ist"], 0 if x["type"] == "short" else 1))

out_manifest_path = config.OUTPUT_DIR / "day1_production_manifest.json"
with open(out_manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)

print("=" * 70)
print(f"  DAY 1 PRODUCTION MANIFEST GENERATED: {len(manifest)} EPISODES")
print(f"  Saved to: {out_manifest_path}")
print("=" * 70)
for m in manifest:
    badge = "[MASTERCLASS]" if m["type"] == "masterclass" else "[SHORT]      "
    status = "OK" if m["exists"] else "MISSING"
    print(f"  {m['schedule_ist']} | {badge} [{m['track'].upper():7s}] ({status}) -> {m['title'][:45]}...")
