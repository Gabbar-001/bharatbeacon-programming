import json
import sys
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

sys.path.append(str(Path(__file__).resolve().parent.parent))

with open("token.json", "r", encoding="utf-8") as f:
    token_data = json.load(f)

creds = Credentials.from_authorized_user_info(token_data)
yt = build("youtube", "v3", credentials=creds)

pl_file = Path("playlists.json")
playlist_map = {}
if pl_file.exists():
    with open(pl_file, "r", encoding="utf-8") as f:
        playlist_map = json.load(f)

NEWS_PLAYLISTS = [
    {
        "key": "news_longform",
        "title": "BharatBeacon | India Daily In-Depth News Bulletins",
        "description": "Comprehensive daily long-form news coverage from BharatBeacon — India's Window to the World. Covering national affairs, defense, science, economy, and global diplomacy.",
        "type": "longform"
    },
    {
        "key": "news_shorts",
        "title": "BharatBeacon | Top 10 Breaking News in 60 Seconds #Shorts",
        "description": "Hourly viral news updates in under 60 seconds from BharatBeacon. Catch the latest top stories across India and the globe in crisp, rapid-fire format.",
        "type": "shorts"
    }
]

print("=" * 60)
print("  CREATING DEDICATED YOUTUBE NEWS PLAYLISTS")
print("=" * 60)

for p in NEWS_PLAYLISTS:
    key = p["key"]
    title = p["title"]
    desc = p["description"]
    
    # Check if already created
    if key in playlist_map and playlist_map[key].get("id"):
        print(f"[EXISTS] {title} -> {playlist_map[key]['url']}")
        continue

    try:
        res = yt.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title,
                    "description": desc,
                    "defaultLanguage": "en"
                },
                "status": {
                    "privacyStatus": "public"
                }
            }
        ).execute()

        pl_id = res["id"]
        pl_url = f"https://www.youtube.com/playlist?list={pl_id}"
        print(f"[CREATED] {title} -> {pl_url}")

        playlist_map[key] = {
            "id": pl_id,
            "title": title,
            "type": p["type"],
            "url": pl_url
        }
    except Exception as e:
        print(f"[ERROR] Failed to create {title}: {e}")

with open(pl_file, "w", encoding="utf-8") as f:
    json.dump(playlist_map, f, indent=2)

print("\nSaved updated playlists to playlists.json!")
