import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

sys.path.append(str(Path(__file__).resolve().parent.parent))
import config

SECRETS_FILE = config.BASE_DIR / "client_secrets.json"
TOKEN_FILE = config.BASE_DIR / "token.json"
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.readonly"
]

def save_metadata(metadata: Dict, timestamp_str: str) -> Path:
    config.METADATA_DIR.mkdir(parents=True, exist_ok=True)
    meta_path = config.METADATA_DIR / f"METADATA_{metadata.get('format', 'news')}_{timestamp_str}.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)
    return meta_path

def get_youtube_service():
    """Initializes authorized YouTube Data API service if credentials exist."""
    # Auto-populate from environment secrets in CI/CD (e.g. GitHub Actions)
    if not SECRETS_FILE.exists() and os.environ.get("YOUTUBE_CLIENT_SECRETS"):
        SECRETS_FILE.parent.mkdir(parents=True, exist_ok=True)
        SECRETS_FILE.write_text(os.environ["YOUTUBE_CLIENT_SECRETS"], encoding="utf-8")
    if not TOKEN_FILE.exists() and os.environ.get("YOUTUBE_TOKEN_JSON"):
        TOKEN_FILE.parent.mkdir(parents=True, exist_ok=True)
        TOKEN_FILE.write_text(os.environ["YOUTUBE_TOKEN_JSON"], encoding="utf-8")

    if not SECRETS_FILE.exists():
        return None
    try:
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build

        creds = None

        if TOKEN_FILE.exists():
            try:
                creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
            except Exception:
                creds = None

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                    with open(TOKEN_FILE, "w", encoding="utf-8") as token:
                        token.write(creds.to_json())
                except Exception as refresh_err:
                    print(f"Token refresh notice: {refresh_err}. Re-prompting authorization...")
                    creds = None

            if not creds or not creds.valid:
                flow = InstalledAppFlow.from_client_secrets_file(str(SECRETS_FILE), SCOPES)
                print("\n[*] Starting local authentication server on http://localhost:8080/ ...")
                sys.stdout.flush()
                creds = flow.run_local_server(
                    port=8080,
                    prompt="consent",
                    access_type="offline"
                )
                with open(TOKEN_FILE, "w", encoding="utf-8") as token:
                    token.write(creds.to_json())

        return build("youtube", "v3", credentials=creds)
    except Exception as e:
        print(f"YouTube Auth Notice: {e}")
        return None

def verify_channel() -> Optional[Dict]:
    """Tests authentication and returns details of the authenticated YouTube channel."""
    service = get_youtube_service()
    if not service:
        return None
    try:
        req = service.channels().list(mine=True, part="snippet,statistics")
        resp = req.execute()
        items = resp.get("items", [])
        if not items:
            return None
        ch = items[0]
        return {
            "title": ch["snippet"]["title"],
            "id": ch["id"],
            "customUrl": ch["snippet"].get("customUrl", ""),
            "subscribers": ch["statistics"].get("subscriberCount", "Hidden"),
            "videoCount": ch["statistics"].get("videoCount", "0")
        }
    except Exception as e:
        print(f"Error fetching channel details: {e}")
        return None

def upload_video(metadata: Dict, privacy_status: str = None) -> Optional[str]:
    """Uploads video to YouTube channel or stages it locally if API is not yet linked."""
    video_path = metadata.get("video_path")
    if not video_path or not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}")
        return None

    if not config.YOUTUBE_AUTO_UPLOAD:
        print(f"[LOCAL STAGE] Auto-upload disabled in config. Video saved: {Path(video_path).name}")
        return "staged_locally"

    service = get_youtube_service()
    if not service:
        print(f"\n[STAGE MODE] Video ready locally: {Path(video_path).name}")
        print(f"  Title: {metadata.get('title')}")
        print(f"  --> To enable direct auto-upload, run 'python setup_youtube.py'")
        return "staged_locally"

    target_privacy = privacy_status or getattr(config, "YOUTUBE_PRIVACY", "public")

    try:
        from googleapiclient.http import MediaFileUpload

        status_body = {
            "privacyStatus": target_privacy,
            "selfDeclaredMadeForKids": False
        }

        # Support YouTube native scheduled releases
        if metadata.get("publish_at"):
            status_body["privacyStatus"] = "private"
            status_body["publishAt"] = metadata["publish_at"]

        body = {
            "snippet": {
                "title": metadata.get("title", "BharatBeacon Breaking News")[:100],
                "description": metadata.get("description", "")[:5000],
                "tags": metadata.get("tags", ["India News", "BharatBeacon", "News"]),
                "categoryId": metadata.get("category_id", "25"),  # 25 = News & Politics
                "defaultLanguage": "en",
                "defaultAudioLanguage": "en-IN"
            },
            "status": status_body
        }

        part_str = "snippet,status"
        if metadata.get("localizations"):
            body["localizations"] = metadata["localizations"]
            part_str = "snippet,status,localizations"

        media = MediaFileUpload(video_path, chunksize=1024*1024*4, resumable=True)
        request = service.videos().insert(
            part=part_str,
            body=body,
            media_body=media
        )

        display_status = f"SCHEDULED for {metadata.get('publish_at')}" if metadata.get("publish_at") else target_privacy.upper()
        print(f"\n[UPLOADING] Uploading {Path(video_path).name} to YouTube ({display_status})...")
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"  Progress: {int(status.progress() * 100)}%")

        video_id = response.get("id")
        video_url = f"https://youtu.be/{video_id}"
        print(f"  SUCCESS! Video Published/Scheduled: {video_url}")

        # Automatically insert into target YouTube playlist if specified
        playlist_id = metadata.get("playlist_id")
        if playlist_id:
            try:
                service.playlistItems().insert(
                    part="snippet",
                    body={
                        "snippet": {
                            "playlistId": playlist_id,
                            "resourceId": {
                                "kind": "youtube#video",
                                "videoId": video_id
                            }
                        }
                    }
                ).execute()
                print(f"  [PLAYLIST] Added video to playlist: {playlist_id}")
            except Exception as pl_err:
                print(f"  [!] Notice: Could not add to playlist {playlist_id}: {pl_err}")

        return video_id
    except Exception as e:
        print(f"YouTube Upload Failed: {e}")
        return None

if __name__ == "__main__":
    test_meta = {
        "format": "test",
        "video_path": str(config.SHORTS_OUTPUT_DIR / "SHORTS_test_run.mp4"),
        "title": "Test India News Update",
        "description": "Testing metadata generation",
        "tags": ["India News", "Test"]
    }
    saved = save_metadata(test_meta, "test")
    print(f"Saved test metadata to {saved}")
    upload_video(test_meta)
