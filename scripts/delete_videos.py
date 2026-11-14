import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.youtube_publisher import get_youtube_service

service = get_youtube_service()
if not service:
    print("Failed to get YouTube service")
    sys.exit(1)

videos_to_delete = [
    {"id": "caa4wo8JDzo", "title": "Python Day 1: How Python Actually Manages Memory"},
    {"id": "ce1SVzzQIzg", "title": "Java Day 1: Inside the JVM: Bytecode, ClassLoader"}
]

for v in videos_to_delete:
    vid = v["id"]
    title = v["title"]
    try:
        print(f"Deleting video: {vid} ({title})...")
        service.videos().delete(id=vid).execute()
        print(f"  [SUCCESS] Deleted {vid} from YouTube channel.")
    except Exception as e:
        print(f"  [ERROR] Failed to delete {vid}: {e}")
