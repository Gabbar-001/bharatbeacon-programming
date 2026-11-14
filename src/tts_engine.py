import os
import sys
import asyncio
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple
import edge_tts

sys.path.append(str(Path(__file__).resolve().parent.parent))
import config

def get_audio_duration(file_path: Path) -> float:
    try:
        cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(file_path)
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return float(res.stdout.strip())
    except Exception as e:
        print(f"Error getting duration for {file_path}: {e}")
        return 5.0

def format_ass_time(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def build_ass_subtitles(sentence_chunks: List[Dict], output_ass: Path, is_shorts: bool = True):
    """
    Generates high-impact, modern viral subtitles in ASS format.
    - Shorts: Dynamic 2-3 word bursts, large bold typography, bright yellow & white keywords, thick stroke & shadow.
    - Long-form: Elegant broadcast closed-caption style, 5-6 words per cue, positioned safely above lower third.
    """
    if is_shorts:
        play_x, play_y = 1080, 1920
        font_name = "Segoe UI"
        font_size = 34
        margin_v = 388
        margin_l = 155
        margin_r = 75
        alignment = 1  # Bottom-Left next to red chevron >> inside the 85px Ticker Bar
        outline = 2.0
        shadow = 1.0
        chunk_size = 3
    else:
        play_x, play_y = 1920, 1080
        font_name = "Segoe UI"
        font_size = 32
        margin_v = 258
        margin_l = 155
        margin_r = 670
        alignment = 1  # Bottom-Left next to red chevron >> in Ticker Bar
        outline = 2.0
        shadow = 1.0
        chunk_size = 4

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {play_x}
PlayResY: {play_y}

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: StyleDefault,{font_name},{font_size},&H00FFFFFF,&H000000FF,&H00000000,&H80000000,-1,1,0,0,100,100,0,0,1,{outline},{shadow},{alignment},{margin_l},{margin_r},{margin_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    dialogues = []
    for sc in sentence_chunks:
        text = sc.get("text", "").strip()
        offset = sc.get("offset", 0) / 10_000_000.0
        duration = sc.get("duration", 0) / 10_000_000.0

        words = text.split()
        if not words:
            continue

        total_chars = sum(len(w) for w in words)
        cur_t = offset

        for i in range(0, len(words), chunk_size):
            grp = words[i:i + chunk_size]
            grp_chars = sum(len(w) for w in grp)
            grp_dur = (grp_chars / total_chars) * duration

            if is_shorts:
                # First word highlighted in bright yellow, remaining in white
                if len(grp) >= 2:
                    cue_text = r"{\c&H0000FFFF}" + grp[0].upper() + r"{\c&H00FFFFFF} " + " ".join(grp[1:]).upper()
                else:
                    cue_text = r"{\c&H0000FFFF}" + grp[0].upper()
            else:
                cue_text = " ".join(grp)

            start_str = format_ass_time(cur_t)
            end_str = format_ass_time(cur_t + grp_dur)
            dialogues.append(f"Dialogue: 0,{start_str},{end_str},StyleDefault,,0,0,0,,{cue_text}")
            cur_t += grp_dur

    output_ass.parent.mkdir(parents=True, exist_ok=True)
    with open(output_ass, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(dialogues) + "\n")

async def synthesize_speech(
    text: str,
    output_audio: Path,
    output_ass: Path = None,
    output_srt: Path = None,
    is_shorts: bool = True,
    voice: str = None
) -> float:
    selected_voice = voice or config.TTS_VOICE
    output_audio.parent.mkdir(parents=True, exist_ok=True)

    max_retries = 3
    for attempt in range(max_retries):
        try:
            speech_rate = "+10%" if is_shorts else config.TTS_RATE
            comm = edge_tts.Communicate(
                text=text,
                voice=selected_voice,
                rate=speech_rate,
                pitch=config.TTS_PITCH
            )

            submaker = edge_tts.SubMaker() if output_srt else None
            sentence_chunks = []

            with open(output_audio, "wb") as f:
                async for chunk in comm.stream():
                    if chunk["type"] == "audio":
                        f.write(chunk["data"])
                    elif chunk["type"] in ("SentenceBoundary", "WordBoundary"):
                        sentence_chunks.append(chunk)
                        if submaker:
                            submaker.feed(chunk)

            if output_srt and submaker:
                with open(output_srt, "w", encoding="utf-8") as f:
                    f.write(submaker.get_srt())

            if output_ass:
                build_ass_subtitles(sentence_chunks, output_ass, is_shorts=is_shorts)

            dur = get_audio_duration(output_audio)
            await asyncio.sleep(0.3)
            return dur
        except Exception as e:
            print(f"[TTS Notice] Voice attempt {attempt+1}/{max_retries} paused: {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(3 * (attempt + 1))
            else:
                raise e

def generate_voiceover_sync(
    text: str,
    output_audio: Path,
    output_ass: Path = None,
    output_srt: Path = None,
    is_shorts: bool = True,
    voice: str = None
) -> float:
    return asyncio.run(synthesize_speech(text, output_audio, output_ass, output_srt, is_shorts, voice))

def format_shorts_script(stories: List[Dict]) -> List[Dict]:
    """Generates punchy, rapid-fire scripts for YouTube Shorts (<60s total) with natural news transitions"""
    segments = []

    segments.append({
        "type": "intro",
        "text": "Welcome to BharatBeacon — India's Window to the World! Here are your top 10 headlines this hour.",
        "display_title": "TOP 10 IN 60 SECONDS",
        "story": None
    })

    transitions = [
        "Our top headline:",
        "In national news:",
        "Turning to business:",
        "In sports updates:",
        "Next up:",
        "In technology:",
        "Meanwhile:",
        "In another key update:",
        "Next report:",
        "And finally:"
    ]

    for idx, s in enumerate(stories, 1):
        # If AI Pre-Generation Engine provided a Champion Hook, use it directly!
        if s.get("champion_hook") and s["champion_hook"].get("text"):
            narration = s["champion_hook"]["text"]
        else:
            raw_title = s["title"].rstrip(".")
            words = raw_title.split()
            if len(words) > 8:
                short_title = " ".join(words[:8])
            else:
                short_title = raw_title

            prefix = transitions[(idx - 1) % len(transitions)]
            narration = f"{prefix} {short_title}."

        segments.append({
            "type": "story",
            "index": idx,
            "text": narration,
            "display_title": s["title"],
            "story": s
        })

    segments.append({
        "type": "outro",
        "text": "Subscribe to BharatBeacon — India's Window to the World for updates every single hour!",
        "display_title": "SUBSCRIBE FOR HOURLY UPDATES",
        "story": None
    })

    # Double-Check Verification & Content Alignment Gate
    from src.double_check_engine import double_check_and_certify
    segments = double_check_and_certify(stories, segments, is_shorts=True)

    return segments

def format_longform_script(stories: List[Dict]) -> List[Dict]:
    """Generates comprehensive, detailed scripts for 16:9 broadcast (~5 mins) with natural broadcast flow"""
    segments = []

    segments.append({
        "type": "intro",
        "text": "Namaste and welcome to BharatBeacon — India's Window to the World. Bringing you the top ten major developments across the nation and the world this hour. Let us begin with the headlines.",
        "display_title": "HOURLY NEWS BULLETIN",
        "story": None
    })

    transitions = [
        "Starting with our top story this hour:",
        "In another major national development:",
        "Turning to business and markets across the country:",
        "In sports headlines today:",
        "Next, in technology and digital updates:",
        "Moving forward with key updates across India:",
        "In other significant developments:",
        "Meanwhile, authorities report that:",
        "Taking a look at our next major report:",
        "And rounding up this hourly news bulletin:"
    ]

    for idx, s in enumerate(stories, 1):
        # If AI Pre-Generation Engine provided a retention storyboard, use it!
        if s.get("storyboard") and s["storyboard"].get("full_script"):
            narration = s["storyboard"]["full_script"]
        else:
            cat = s.get("category", "National").title()
            title = s["title"].rstrip(".")
            summary = s.get("summary", "")
            prefix = transitions[(idx - 1) % len(transitions)]

            if summary and summary != s["title"]:
                narration = f"{prefix} {title}. {summary}"
            else:
                narration = f"{prefix} {title}. Observers and authorities are monitoring developments closely as further details arrive."

        segments.append({
            "type": "story",
            "index": idx,
            "text": narration,
            "display_title": s["title"],
            "story": s
        })

    segments.append({
        "type": "outro",
        "text": "Those were the top ten stories making headlines this hour. For continuous news coverage, breaking alerts, and the next hourly update, make sure to like and subscribe to BharatBeacon — India's Window to the World. Have a wonderful day ahead.",
        "display_title": "STAY INFORMED - SUBSCRIBE",
        "story": None
    })

    # Double-Check Verification & Content Alignment Gate
    from src.double_check_engine import double_check_and_certify
    segments = double_check_and_certify(stories, segments, is_shorts=False)

    return segments

if __name__ == "__main__":
    test_text = "Namaste India! Here are your top 10 breaking news headlines today."
    test_audio = config.TEMP_DIR / "test_styled_voice.mp3"
    test_ass = config.TEMP_DIR / "test_styled_voice.ass"
    dur = generate_voiceover_sync(test_text, test_audio, output_ass=test_ass, is_shorts=True)
    print(f"Generated test audio ({dur:.2f}s) and ASS subtitles at {test_ass}")
