import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

with open("token.json", "r") as f:
    token_data = json.load(f)

creds = Credentials.from_authorized_user_info(token_data)
yt = build("youtube", "v3", credentials=creds)

PLAYLISTS_TO_CREATE = [
    # 4 Long-form Playlists
    {
        "key": "python_longform",
        "title": "Python Masterclass (60 Days Zero to Hero)",
        "description": "Complete 60-day Python masterclass with animated presentations, memory architecture, and hands-on coding.",
        "type": "longform",
        "track": "python"
    },
    {
        "key": "java_longform",
        "title": "Java Masterclass (60 Days Core to Enterprise)",
        "description": "Complete 60-day Java masterclass covering JVM internals, OOP, collections, multithreading, and enterprise backend.",
        "type": "longform",
        "track": "java"
    },
    {
        "key": "mongodb_longform",
        "title": "MongoDB Complete Guide (60 Days NoSQL Mastery)",
        "description": "Comprehensive 60-day MongoDB course: BSON, CRUD, indexing, aggregation pipelines, and production schema design.",
        "type": "longform",
        "track": "mongodb"
    },
    {
        "key": "sql_longform",
        "title": "SQL Masterclass (60 Days Zero to Hero)",
        "description": "Master relational database engineering: ACID transactions, queries, complex JOINs, window functions, and indexing.",
        "type": "longform",
        "track": "sql"
    },
    # 4 Shorts Playlists
    {
        "key": "python_shorts",
        "title": "Python Shorts & Interview Tricks",
        "description": "Daily 45-second Python pro-tips, memory riddles, gotchas, and FAANG coding interview questions.",
        "type": "shorts",
        "track": "python"
    },
    {
        "key": "java_shorts",
        "title": "Java Shorts & OOP Riddles",
        "description": "Daily Java byte-sized tricks, memory gotchas, multithreading puzzles, and clean code secrets.",
        "type": "shorts",
        "track": "java"
    },
    {
        "key": "mongodb_shorts",
        "title": "MongoDB Shorts & Quick Tips",
        "description": "Daily NoSQL MongoDB tips, aggregation tricks, schema hacks, and SQL vs NoSQL comparisons.",
        "type": "shorts",
        "track": "mongodb"
    },
    {
        "key": "sql_shorts",
        "title": "SQL Shorts & Query Hacks",
        "description": "Daily SQL tricks: JOIN riddles, performance optimization, execution order, and database interview questions.",
        "type": "shorts",
        "track": "sql"
    }
]

created_map = {}

for pl in PLAYLISTS_TO_CREATE:
    body = {
        "snippet": {
            "title": pl["title"],
            "description": pl["description"]
        },
        "status": {
            "privacyStatus": "public"
        }
    }
    res = yt.playlists().insert(part="snippet,status", body=body).execute()
    pl_id = res["id"]
    created_map[pl["key"]] = {
        "id": pl_id,
        "title": pl["title"],
        "type": pl["type"],
        "track": pl["track"],
        "url": f"https://www.youtube.com/playlist?list={pl_id}"
    }
    print(f"[OK] Created Playlist: {pl['title']} -> ID: {pl_id}")

with open("playlists.json", "w", encoding="utf-8") as f:
    json.dump(created_map, f, indent=2)

print("\nSuccessfully saved all 8 playlist IDs to playlists.json!")
