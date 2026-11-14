from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.tech_animator import (
    render_code_card,
    render_memory_diagram,
    render_split_comparison_card,
    render_presentation_slide,
    COLOR_BG,
    COLOR_CARD,
    COLOR_ACCENT,
    COLOR_PYTHON,
    COLOR_JAVA,
    COLOR_MONGO,
    COLOR_SQL
)

ARTIFACT_DIR = Path(r"C:\Users\mr_un\.gemini\antigravity\brain\a40d7958-d2a6-434b-bf71-f01f0b882465")

# 1. Slide 1: Tokyo Night Code Walkthrough
code1 = """def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper"""

card1 = render_code_card(code1, language="python", filename="memoize.py")
slide1 = render_presentation_slide(
    track_title="PYTHON PERFORMANCE PATTERNS",
    episode_info="TEMPLATE #01: TOKYO NIGHT",
    slide_title="Function Memoization & Closure Memory Caching",
    bullet_points=[
        "Closures capture the surrounding lexical scope on the Heap.",
        "The cache dictionary persists across multiple function calls.",
        "Avoid unbounded cache growth in long-running production processes."
    ],
    right_image=card1,
    accent_color=COLOR_PYTHON
)
slide1.save(ARTIFACT_DIR / "sample_template_01_tokyo_night.png")

# 2. Slide 2: Memory Architecture (Stack vs Heap)
card2 = render_memory_diagram(width=800, height=500)
slide2 = render_presentation_slide(
    track_title="SYSTEM ARCHITECTURE DEEP DIVE",
    episode_info="TEMPLATE #21: STACK VS HEAP",
    slide_title="Inside Process Memory: Stack Frames vs Heap Objects",
    bullet_points=[
        "Stack: Fast, thread-safe, sequential LIFO allocation for primitive types.",
        "Heap: Dynamic reference storage managed by Garbage Collection (GC).",
        "Pointers on the stack reference object memory addresses on the heap."
    ],
    right_image=card2,
    accent_color=(122, 162, 247)
)
slide2.save(ARTIFACT_DIR / "sample_template_21_memory_blueprint.png")

# 3. Slide 3: Anti-Pattern vs Pro-Fix
bad_c = """# ❌ ANTI-PATTERN: N+1 Database Query
users = User.objects.all()
for u in users:
    # 100 queries fired!
    print(u.profile.bio)"""

good_c = """# ✅ PRO FIX: Eager Load via JOIN
users = User.objects.select_related(
    'profile'
).all()
for u in users:
    print(u.profile.bio)"""

card3 = render_split_comparison_card(bad_c, good_c)
slide3 = render_presentation_slide(
    track_title="DATABASE QUERY OPTIMIZATION",
    episode_info="TEMPLATE #29: CODE DIFF PRO-FIX",
    slide_title="The Dreaded N+1 Query Anti-Pattern in Production",
    bullet_points=[
        "Naive ORM iterations trigger a separate network query for every child record.",
        "Eager loading compiles a single SQL INNER JOIN at the database engine level.",
        "Reduces database connection pool exhaustion and query latency by up to 98%."
    ],
    right_image=card3,
    accent_color=(239, 68, 68)
)
slide3.save(ARTIFACT_DIR / "sample_template_29_anti_pattern_split.png")

print("[OK] Rendered 3 sample slide PNGs in artifact directory.")
