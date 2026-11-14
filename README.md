# 🎓 BharatBeacon — 60-Day Tech Masterclass & Viral Shorts Engine

Autonomous, production-ready cloud video generation and YouTube publishing system for technical bootcamps across 4 core engineering stacks:
* 🐍 **Python** (60 Days Zero to Hero)
* ☕ **Java** (60 Days Core to Enterprise)
* 🍃 **MongoDB** (60 Days NoSQL Mastery)
* 🐬 **SQL** (60 Days Query Optimization & Relational Mastery)

---

## ⚡ Architecture & Daily Schedule

Every day at **8:00 PM IST (14:30 UTC)**, GitHub Actions automatically executes the end-to-end pipeline:
1. **Reads Day Index:** Checks `output/current_day_tracker.json` (e.g. Day 2, Day 3).
2. **Generates Code Graphics:** High-resolution syntax highlighted cards with Pygments and Pillow.
3. **Synthesizes Audio:** High-clarity voiceovers with Edge-TTS.
4. **Encodes Ultra-Fast MP4:** FFmpeg H.264 rendering with audio ducking and transitions.
5. **Schedules YouTube Releases:** Publishes 24 videos scheduled hourly starting at midnight (00:00 IST).
6. **Routes into Playlists:** Directly assigns each video to its dedicated YouTube playlist.
7. **Updates Day Counter:** Automatically increments tracker and commits back to repository `main`.

---

## 📂 Repository Structure

```
├── .github/workflows/
│   └── daily_tech_bootcamp.yml      # GitHub Actions daily schedule (8:00 PM IST)
├── assets/
│   ├── fonts/                       # JetBrains Mono, Segoe UI, Arial Bold
│   ├── music/                       # Swoosh and audio transitions
│   └── templates/                   # Clean master broadcast cards
├── content_plan/
│   ├── day1_data.py                 # Day 1 Masterclasses (Python, Java, Mongo, SQL)
│   ├── day1_shorts_data.py          # Day 1 Viral Shorts (20 episodes)
│   ├── day2_data.py                 # Day 2 Masterclasses
│   └── day2_shorts_data.py          # Day 2 Viral Shorts
├── output/
│   ├── current_day_tracker.json     # Current active day index
│   └── day1_upload_progress.json    # Published episode IDs and schedules
├── scripts/
│   ├── produce_and_upload_day1.py   # Day 1 batch renderer
│   └── schedule_day1_uploads.py     # YouTube scheduler script
├── src/
│   ├── tech_animator.py             # Pygments syntax highlighter & frame renderer
│   ├── tech_masterclass_builder.py  # 16:9 Long-form course builder
│   ├── tts_engine.py                # Edge-TTS voice synthesizer
│   └── youtube_publisher.py         # YouTube v3 API resumable uploader
├── config.py                        # Paths, voice, resolution configs
├── playlists.json                   # 8 dedicated YouTube playlist IDs
├── requirements.txt                 # Dependencies (pillow, pygments, edge-tts, etc.)
└── run_daily_tech.py                # Main CLI & GitHub Actions driver
```

---

## 📺 YouTube Playlist IDs

| Stack | Format | Playlist ID | Link |
| :--- | :--- | :--- | :--- |
| **Python** | Long-form Masterclass | `PLZMwwKlRTaj0` | [Playlist](https://www.youtube.com/playlist?list=PLZMwwKlRTaj0) |
| **Python** | Viral Shorts | `PLAYfkU-guA_s` | [Playlist](https://www.youtube.com/playlist?list=PLAYfkU-guA_s) |
| **Java** | Long-form Masterclass | `PLEcSKSE74kf8` | [Playlist](https://www.youtube.com/playlist?list=PLEcSKSE74kf8) |
| **Java** | Viral Shorts | `PLAbl3Hjt9xes` | [Playlist](https://www.youtube.com/playlist?list=PLAbl3Hjt9xes) |
| **MongoDB**| Long-form Masterclass | `PLL3DADVzng50` | [Playlist](https://www.youtube.com/playlist?list=PLL3DADVzng50) |
| **MongoDB**| Viral Shorts | `PLV-RkSFBoHzI` | [Playlist](https://www.youtube.com/playlist?list=PLV-RkSFBoHzI) |
| **SQL** | Long-form Masterclass | `PLJQH5RXmQ8JA` | [Playlist](https://www.youtube.com/playlist?list=PLJQH5RXmQ8JA) |
| **SQL** | Viral Shorts | `PLFPXUdMgM0HI` | [Playlist](https://www.youtube.com/playlist?list=PLFPXUdMgM0HI) |

---

## 🚀 Cloud Setup & Secrets

The GitHub Actions workflow requires 2 repository secrets:
* `YOUTUBE_CLIENT_SECRETS`: OAuth2 client secrets JSON.
* `YOUTUBE_TOKEN_JSON`: Authenticated YouTube API token JSON.
