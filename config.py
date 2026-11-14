import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"
ASSETS_DIR = BASE_DIR / "assets"
OUTPUT_DIR = BASE_DIR / "output"
CONTENT_PLAN_DIR = BASE_DIR / "content_plan"

FONTS_DIR = ASSETS_DIR / "fonts"
MUSIC_DIR = ASSETS_DIR / "music"
TEMPLATES_DIR = ASSETS_DIR / "templates"

LONGFORM_OUTPUT_DIR = OUTPUT_DIR / "longform"
SHORTS_OUTPUT_DIR = OUTPUT_DIR / "shorts"
TEMP_DIR = OUTPUT_DIR / "temp"
METADATA_DIR = OUTPUT_DIR / "metadata"

# Create directories if not exist
for p in [LONGFORM_OUTPUT_DIR, SHORTS_OUTPUT_DIR, TEMP_DIR, METADATA_DIR, FONTS_DIR, MUSIC_DIR, TEMPLATES_DIR]:
    p.mkdir(parents=True, exist_ok=True)

# Voiceover Settings (Clear, natural Indian female voice)
TTS_VOICE = "en-IN-NeerjaNeural"
TTS_RATE = "+0%"
TTS_PITCH = "+0Hz"

# Video Specifications
LONGFORM_WIDTH = 1920
LONGFORM_HEIGHT = 1080
SHORTS_WIDTH = 1080
SHORTS_HEIGHT = 1920
FPS = 30

# Channel Branding
CHANNEL_NAME = "BharatBeacon"
CHANNEL_HANDLE = "@BharatBeacon"
CHANNEL_TAGLINE = "Empowering Developers & Engineers"

# YouTube Settings
YOUTUBE_AUTO_UPLOAD = True
YOUTUBE_PRIVACY = "public"
