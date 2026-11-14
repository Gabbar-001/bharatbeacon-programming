import asyncio
import edge_tts
from pathlib import Path

out_dir = Path("output/voice_samples")
out_dir.mkdir(parents=True, exist_ok=True)

test_script = (
    "Welcome to Day 1 of our Python Masterclass! Today, we are diving deep into memory management "
    "and variable pointers. Stop writing slow loops like it is 1995 — let us master clean code together."
)

samples = [
    {
        "id": "sample_1_neerja_expressive",
        "voice": "en-IN-NeerjaExpressiveNeural",
        "rate": "+0%",
        "pitch": "+0Hz",
        "name": "Neerja Expressive (Indian English)",
        "desc": "Natural, modern, conversational Indian English accent with high emotional range."
    },
    {
        "id": "sample_2_neerja_snappy",
        "voice": "en-IN-NeerjaNeural",
        "rate": "+12%",
        "pitch": "+0Hz",
        "name": "Neerja Snappy (Indian English)",
        "desc": "Brisk, fast-paced technical tutorial speed (ideal for coding tutorials and Shorts)."
    },
    {
        "id": "sample_3_neerja_energetic",
        "voice": "en-IN-NeerjaNeural",
        "rate": "+8%",
        "pitch": "+3Hz",
        "name": "Neerja Upbeat & Warm (Indian English)",
        "desc": "Friendly, approachable tutor tone (like a senior software engineer mentoring you)."
    },
    {
        "id": "sample_4_aria_global_tech",
        "voice": "en-US-AriaNeural",
        "rate": "+6%",
        "pitch": "+0Hz",
        "name": "Aria Global Tech (Silicon Valley Style)",
        "desc": "Crisp, authoritative international tech style widely used on Fireship and tech explainers."
    }
]

async def generate_all():
    print("Generating voice samples...")
    for s in samples:
        file_path = out_dir / f"{s['id']}.mp3"
        comm = edge_tts.Communicate(test_script, voice=s["voice"], rate=s["rate"], pitch=s["pitch"])
        await comm.save(str(file_path))
        print(f"[OK] Generated: {file_path.name} -> {s['name']}")

if __name__ == "__main__":
    asyncio.run(generate_all())
