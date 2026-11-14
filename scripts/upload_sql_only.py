import os
import sys
import json
from pathlib import Path

# Add project root
sys.path.append(str(Path(__file__).resolve().parent.parent))
import config
from content_plan.day1_data import DAY1_MASTERCLASSES
from src.youtube_publisher import upload_video

OUT_DIR = config.LONGFORM_OUTPUT_DIR
output_video = OUT_DIR / "MASTERCLASS_DAY01_SQL.mp4"

if not output_video.exists():
    print(f"Error: {output_video} does not exist!")
    sys.exit(1)

with open("playlists.json", "r", encoding="utf-8") as f:
    playlist_map = json.load(f)

# Find SQL course
sql_course = [c for c in DAY1_MASTERCLASSES if c["track"] == "sql"][0]
pl_key = sql_course["playlist_key"]
playlist_id = playlist_map.get(pl_key, {}).get("id")

description = f"""{sql_course['title']}

Welcome to Day 1 of our 60-Day Full-Stack Bootcamp!
Master production-grade coding with visual PPT presentations, memory diagrams, and hands-on code examples.

TIMESTAMPS:
00:00 Welcome to SQL Database Engineering
00:29 The ACID Guarantees Explained
01:02 Table Creation & Column Constraints
01:32 Foreign Keys & The Orphaned Row Disaster
02:04 FAANG Interview Challenge: DELETE vs TRUNCATE vs DROP
02:37 Day 1 Summary & Homework Challenge

📚 PLAYLIST: {playlist_map.get(pl_key, {}).get('title')}
👉 Subscribe for daily episodes across Python, Java, MongoDB, and SQL!

#Coding #Programming #Sql #SoftwareEngineering #TechBootcamp
"""

metadata = {
    "title": sql_course["title"][:100],
    "description": description,
    "video_path": str(output_video),
    "tags": sql_course["tags"],
    "playlist_id": playlist_id,
    "publish_at": sql_course["publish_at"]
}

print(f"Attempting to upload SQL Day 1 Masterclass to YouTube...")
video_id = upload_video(metadata)

if video_id:
    print(f"SUCCESS! SQL Masterclass scheduled: https://youtu.be/{video_id}")
    print(f"Playlist ID: {playlist_id}")
else:
    print("Upload failed or daily limit still active. You can retry anytime with 'python scripts/upload_sql_only.py'.")
