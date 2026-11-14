import json
from pathlib import Path

ARTIFACT_DIR = Path(r"C:\Users\mr_un\.gemini\antigravity\brain\a40d7958-d2a6-434b-bf71-f01f0b882465")
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
HTML_OUT = ARTIFACT_DIR / "ppt_templates_showcase.html"
MD_OUT = ARTIFACT_DIR / "50_ppt_templates_catalog.md"

# Import TEMPLATES from scripts/build_template_showcase.py
import sys
sys.path.append(str(Path(__file__).resolve().parent))
from templates_data import TEMPLATES

def render_slide_preview(t):
    ltype = t.get("layout_type")
    accent = t.get("accent", "#38bdf8")
    card_bg = t.get("card_bg", "#1a1b26")
    border = t.get("border", "#292e42")
    text_c = t.get("text", "#c0caf5")

    if ltype == "code_window":
        code_lines = t["sample_code"].split("\n")
        code_html = "".join([f"<div class='flex'><span class='text-zinc-600 select-none w-6 text-right pr-2 text-xs'>{i+1}</span><span class='text-xs font-mono'>{line}</span></div>" for i, line in enumerate(code_lines[:5])])
        return f"""
        <div class="rounded-lg p-3 border" style="background-color: {card_bg}; border-color: {border}; color: {text_c};">
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-zinc-700/50 text-xs">
            <div class="flex items-center gap-1.5">
              <div class="w-2.5 h-2.5 rounded-full bg-rose-500"></div>
              <div class="w-2.5 h-2.5 rounded-full bg-amber-500"></div>
              <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
              <span class="ml-2 font-mono text-zinc-400">snippet.{t.get('lang', 'py')}</span>
            </div>
            <span class="px-2 py-0.5 rounded text-[10px] font-semibold uppercase" style="color: {accent};">{t.get('lang', 'code')}</span>
          </div>
          <div class="space-y-0.5 font-mono text-xs">{code_html}</div>
        </div>
        """

    elif ltype == "arch_diagram":
        nodes = t.get("nodes", [])
        nodes_html = "".join([f"""
          <div class="flex-1 p-2 rounded-lg border text-center" style="background: {card_bg}; border-color: {border};">
            <div class="text-xs font-bold" style="color: {accent};">{n[0]}</div>
            <div class="text-[10px] text-zinc-400 mt-0.5">{n[1]}</div>
          </div>
        """ for n in nodes])
        return f"""
        <div class="rounded-lg p-3 border" style="background-color: {card_bg}; border-color: {border};">
          <div class="text-xs font-bold mb-2 flex items-center justify-between" style="color: {text_c};">
            <span>{t.get('arch_title', 'Architecture Layout')}</span>
            <span class="text-[10px] px-2 py-0.5 rounded bg-zinc-800 text-zinc-300">Live Bus</span>
          </div>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-2">{nodes_html}</div>
        </div>
        """

    elif ltype == "memory_diagram":
        s_items = "".join([f"<div class='p-1.5 rounded bg-sky-950/40 border border-sky-800/40 text-[11px] font-mono'><span class='text-sky-300'>{item[0]}</span> <span class='text-zinc-400'>({item[1]})</span></div>" for item in t.get("stack_items", [])])
        h_items = "".join([f"<div class='p-1.5 rounded bg-purple-950/40 border border-purple-800/40 text-[11px] font-mono'><span class='text-purple-300'>{item[0]}</span> -> <span class='text-zinc-300'>{item[1]}</span></div>" for item in t.get("heap_items", [])])
        return f"""
        <div class="grid grid-cols-2 gap-2 text-xs">
          <div class="p-2.5 rounded-lg border" style="background: {card_bg}; border-color: {border};">
            <div class="font-bold text-sky-400 mb-1.5">STACK (Execution Frames)</div>
            <div class="space-y-1">{s_items}</div>
          </div>
          <div class="p-2.5 rounded-lg border" style="background: {card_bg}; border-color: {border};">
            <div class="font-bold text-purple-400 mb-1.5">HEAP (Object Storage)</div>
            <div class="space-y-1">{h_items}</div>
          </div>
        </div>
        """

    elif ltype == "split_diff":
        return f"""
        <div class="grid grid-cols-2 gap-2 text-xs font-mono">
          <div class="p-2.5 rounded-lg border border-red-500/30 bg-red-950/20">
            <div class="font-bold text-red-400 mb-1">{t.get('bad_title')}</div>
            <pre class="text-[10px] text-zinc-300 whitespace-pre-wrap">{t.get('bad_code')}</pre>
          </div>
          <div class="p-2.5 rounded-lg border border-emerald-500/30 bg-emerald-950/20">
            <div class="font-bold text-emerald-400 mb-1">{t.get('good_title')}</div>
            <pre class="text-[10px] text-zinc-300 whitespace-pre-wrap">{t.get('good_code')}</pre>
          </div>
        </div>
        """

    elif ltype == "benchmark_bar":
        b_html = "".join([f"""
          <div>
            <div class="flex justify-between text-[11px] mb-1">
              <span class="font-semibold text-zinc-200">{b[0]}</span>
              <span class="font-mono text-zinc-400">{b[1]} <strong class="text-emerald-400 ml-1">({b[3]})</strong></span>
            </div>
            <div class="w-full bg-zinc-800 rounded-full h-2">
              <div class="{b[2]} h-2 rounded-full"></div>
            </div>
          </div>
        """ for b in t.get("benchmarks", [])])
        return f"""
        <div class="rounded-lg p-3 border space-y-2.5" style="background: {card_bg}; border-color: {border};">
          <div class="text-xs font-bold text-sky-400">⚡ Execution Speed Benchmark (N = 1,000,000)</div>
          {b_html}
        </div>
        """

    elif ltype == "dos_and_donts":
        donts = "".join([f"<li class='text-[11px] text-rose-300 flex items-start gap-1'><span>❌</span><span>{d}</span></li>" for d in t.get("donts", [])])
        dos = "".join([f"<li class='text-[11px] text-emerald-300 flex items-start gap-1'><span>✅</span><span>{d}</span></li>" for d in t.get("dos", [])])
        return f"""
        <div class="grid grid-cols-2 gap-2 text-xs">
          <div class="p-2.5 rounded-lg border border-red-500/30 bg-red-950/20">
            <div class="font-bold text-rose-400 mb-1.5">DON'T (Anti-Patterns)</div>
            <ul class="space-y-1">{donts}</ul>
          </div>
          <div class="p-2.5 rounded-lg border border-emerald-500/30 bg-emerald-950/20">
            <div class="font-bold text-emerald-400 mb-1.5">DO (Production Best Practice)</div>
            <ul class="space-y-1">{dos}</ul>
          </div>
        </div>
        """

    elif ltype == "er_diagram":
        u_rows = "".join([f"<div class='flex justify-between text-[10px] font-mono'><span class='text-blue-300'>{r[0]}</span><span class='text-zinc-400'>{r[1]}</span></div>" for r in t.get("table_users", [])])
        o_rows = "".join([f"<div class='flex justify-between text-[10px] font-mono'><span class='text-amber-300'>{r[0]}</span><span class='text-zinc-400'>{r[1]}</span></div>" for r in t.get("table_orders", [])])
        return f"""
        <div class="grid grid-cols-2 gap-2 text-xs">
          <div class="p-2 rounded-lg border" style="background: {card_bg}; border-color: {border};">
            <div class="font-bold text-blue-400 border-b border-zinc-700/50 pb-1 mb-1">TABLE: users</div>
            <div class="space-y-0.5">{u_rows}</div>
          </div>
          <div class="p-2 rounded-lg border" style="background: {card_bg}; border-color: {border};">
            <div class="font-bold text-amber-400 border-b border-zinc-700/50 pb-1 mb-1">TABLE: orders (FK)</div>
            <div class="space-y-0.5">{o_rows}</div>
          </div>
        </div>
        """

    elif ltype == "riddle_card":
        return f"""
        <div class="rounded-lg p-3 border text-center" style="background: {card_bg}; border-color: {border};">
          <div class="inline-block px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40 mb-1.5">💡 FAANG INTERVIEW RIDDLE</div>
          <div class="text-xs font-semibold text-zinc-100 mb-2">{t.get('question')}</div>
          <div class="p-2 rounded bg-zinc-900/80 border border-zinc-800 text-[11px] text-zinc-400 italic">
            🔍 Hint: {t.get('hint')}
          </div>
        </div>
        """

    elif ltype == "hero_opener":
        goals = "".join([f"<div class='flex items-center gap-1.5 text-[11px] text-zinc-300'><span class='text-sky-400'>•</span><span>{g}</span></div>" for g in t.get("goals", [])])
        return f"""
        <div class="rounded-lg p-3 border text-left" style="background: {card_bg}; border-color: {border};">
          <div class="inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/40 mb-1">{t.get('episode')}</div>
          <div class="text-sm font-extrabold text-white tracking-tight mb-2">{t.get('title')}</div>
          <div class="space-y-1 border-t border-zinc-800 pt-1.5">{goals}</div>
        </div>
        """

    elif ltype == "recap_card":
        pts = "".join([f"""
          <div class="flex items-start gap-2 p-1.5 rounded bg-zinc-900/60 border border-zinc-800 text-[11px]">
            <span class="font-bold font-mono px-1.5 py-0.5 rounded bg-blue-500/20 text-blue-400">{p[0]}</span>
            <span class="text-zinc-300">{p[1]}</span>
          </div>
        """ for p in t.get("points", [])])
        return f"""
        <div class="rounded-lg p-2.5 border space-y-1.5" style="background: {card_bg}; border-color: {border};">
          <div class="text-xs font-bold text-blue-400">📝 Day 1 Key Takeaways</div>
          {pts}
        </div>
        """

    elif ltype == "terminal_card":
        return f"""
        <div class="rounded-lg p-3 border font-mono text-xs" style="background: #090d13; border-color: #1e293b;">
          <div class="flex items-center gap-1 mb-2 text-zinc-500 text-[10px]">
            <span class="text-emerald-400">engineer@macbook</span>:<span class="text-sky-400">~/masterclass</span> <span class="text-purple-400">(git:main)</span> $
          </div>
          <pre class="text-[11px] text-emerald-300 whitespace-pre-wrap">{t.get('command')}</pre>
          <div class="mt-2 pt-2 border-t border-zinc-800/80 text-[10px] text-zinc-400">{t.get('output')}</div>
        </div>
        """

    elif ltype == "roadmap_card":
        phases = "".join([f"""
          <div class="flex items-center justify-between p-1.5 rounded bg-zinc-900/70 border border-zinc-800 text-[11px]">
            <span class="font-semibold text-blue-300">{p[0]}</span>
            <span class="text-[10px] text-zinc-400">{p[1]}</span>
          </div>
        """ for p in t.get("phases", [])])
        return f"""
        <div class="rounded-lg p-2.5 border space-y-1.5" style="background: {card_bg}; border-color: {border};">
          <div class="text-xs font-bold text-sky-400">🗺️ 60-Day Masterclass Roadmap Progression</div>
          {phases}
        </div>
        """

    elif ltype == "outro_card":
        return f"""
        <div class="rounded-lg p-3 border text-center" style="background: {card_bg}; border-color: {border};">
          <div class="text-[10px] font-bold text-sky-400 uppercase tracking-widest">{t.get('next_up')}</div>
          <div class="text-xs font-bold text-white mt-1 mb-2">{t.get('next_title')}</div>
          <div class="inline-block px-3 py-1 rounded-full text-[11px] font-semibold bg-red-600 hover:bg-red-500 text-white shadow-lg cursor-pointer">
            🔔 {t.get('cta')}
          </div>
        </div>
        """

    # Generic fallback
    return f"""
    <div class="rounded-lg p-3 border text-center" style="background: {card_bg}; border-color: {border}; color: {text_c};">
      <div class="text-xs font-bold mb-1" style="color: {accent};">{t['name']} Layout</div>
      <p class="text-[11px] text-zinc-400">{t['desc']}</p>
    </div>
    """

# Build the complete HTML Artifact
html_content = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <title>50 Master PPT Slide Templates Gallery</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }}
    .template-card.selected {{
      border-color: #38bdf8 !important;
      box-shadow: 0 0 0 2px #38bdf8, 0 10px 25px -5px rgba(56, 189, 248, 0.3) !important;
    }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-4 md:p-8 antialiased">

  <!-- Header Section -->
  <header class="max-w-7xl mx-auto mb-8 border-b border-slate-800 pb-6">
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-sky-400 text-xs font-bold mb-2">
          <span>✨ 50 PRODUCTION-GRADE PRESENTATION TEMPLATES</span>
        </div>
        <h1 class="text-3xl md:text-4xl font-black tracking-tight text-white">
          60-Day Tech Masterclass & PPT Design Gallery
        </h1>
        <p class="text-slate-400 text-sm mt-1 max-w-2xl">
          Choose from 50 handcrafted templates spanning dark IDE themes, FAANG system design, data structures, code diffs, database engineering, and interactive riddles.
        </p>
      </div>

      <!-- Live Selection Toolbar -->
      <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 shadow-xl flex items-center gap-3">
        <div>
          <div class="text-[11px] uppercase tracking-wider text-slate-400 font-semibold">Selected Templates</div>
          <div id="selection-counter" class="text-lg font-black text-sky-400">0 selected</div>
        </div>
        <button id="copy-btn" onclick="copySelected()" class="px-4 py-2 bg-sky-500 hover:bg-sky-400 text-slate-950 font-bold text-xs rounded-lg transition-all flex items-center gap-1.5 shadow-md">
          <span>📋 Copy IDs</span>
        </button>
      </div>
    </div>

    <!-- Category Filter Tabs -->
    <div class="flex flex-wrap gap-2 mt-6">
      <button onclick="filterCategory('all')" class="cat-btn active px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-sky-500 text-slate-950 transition-all">All (50)</button>
      <button onclick="filterCategory('ide')" class="cat-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 transition-all">💻 IDE Themes (10)</button>
      <button onclick="filterCategory('arch')" class="cat-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 transition-all">🏗️ Architecture & Cloud (10)</button>
      <button onclick="filterCategory('dsa')" class="cat-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 transition-all">🧠 Algorithms & Memory (8)</button>
      <button onclick="filterCategory('diff')" class="cat-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 transition-all">⚡ Code Diffs & Pro-Fixes (7)</button>
      <button onclick="filterCategory('db')" class="cat-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 transition-all">🗄️ Database & Schema (7)</button>
      <button onclick="filterCategory('edu')" class="cat-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 transition-all">🎓 Educational & Outros (8)</button>
    </div>
  </header>

  <!-- Grid of 50 Templates -->
  <main class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="templates-grid">
"""

# Append cards for all 50 templates
for t in TEMPLATES:
    preview_html = render_slide_preview(t)
    html_content += f"""
    <!-- Template Card #{t['id']} -->
    <div class="template-card bg-slate-900/90 border border-slate-800 rounded-2xl p-5 flex flex-col justify-between hover:border-slate-700 transition-all shadow-lg" data-id="{t['id']}" data-cat="{t['category']}">
      <div>
        <!-- Card Top Bar -->
        <div class="flex items-start justify-between gap-2 mb-3">
          <div>
            <div class="flex items-center gap-2">
              <span class="text-xs font-mono font-bold text-sky-400">#{t['id']:02d}</span>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold border {t['badge_color']}">{t['tag']}</span>
            </div>
            <h3 class="text-base font-bold text-white mt-1">{t['name']}</h3>
          </div>
          <!-- Color Swatch Dots -->
          <div class="flex items-center gap-1.5 p-1 rounded-md bg-slate-950/80 border border-slate-800">
            <div class="w-3.5 h-3.5 rounded-full border border-white/20" style="background-color: {t['bg']};" title="Background"></div>
            <div class="w-3.5 h-3.5 rounded-full border border-white/20" style="background-color: {t['card_bg']};" title="Card BG"></div>
            <div class="w-3.5 h-3.5 rounded-full border border-white/20" style="background-color: {t['accent']};" title="Accent"></div>
          </div>
        </div>

        <!-- Live Slide Preview -->
        <div class="rounded-xl overflow-hidden border border-slate-800 bg-slate-950 p-2.5 mb-3 shadow-inner">
          {preview_html}
        </div>

        <!-- Description -->
        <p class="text-xs text-slate-400 line-clamp-2 mb-4 leading-relaxed">
          {t['desc']}
        </p>
      </div>

      <!-- Action Button -->
      <button onclick="toggleSelect({t['id']})" id="btn-{t['id']}" class="w-full py-2 px-3 rounded-xl border border-slate-700 bg-slate-800/80 hover:bg-sky-500 hover:text-slate-950 hover:border-sky-400 text-xs font-bold text-slate-200 transition-all flex items-center justify-center gap-2">
        <span>⭐ Select This Template</span>
      </button>
    </div>
    """

html_content += """
  </main>

  <!-- Interactive JavaScript Logic -->
  <script>
    const selectedIds = new Set();

    function toggleSelect(id) {
      const card = document.querySelector(`.template-card[data-id="${id}"]`);
      const btn = document.getElementById(`btn-${id}`);

      if (selectedIds.has(id)) {
        selectedIds.delete(id);
        card.classList.remove('selected');
        btn.innerHTML = '<span>⭐ Select This Template</span>';
        btn.classList.remove('bg-sky-500', 'text-slate-950', 'border-sky-400');
        btn.classList.add('bg-slate-800/80', 'text-slate-200', 'border-slate-700');
      } else {
        selectedIds.add(id);
        card.classList.add('selected');
        btn.innerHTML = '<span>✅ Selected (Click to Unselect)</span>';
        btn.classList.remove('bg-slate-800/80', 'text-slate-200', 'border-slate-700');
        btn.classList.add('bg-sky-500', 'text-slate-950', 'border-sky-400');
      }
      updateCounter();
    }

    function updateCounter() {
      const counter = document.getElementById('selection-counter');
      counter.innerText = `${selectedIds.size} selected`;
    }

    function copySelected() {
      if (selectedIds.size === 0) {
        alert("Please select at least 1 template first by clicking 'Select This Template'!");
        return;
      }
      const list = Array.from(selectedIds).sort((a,b) => a - b);
      const text = `Selected Template IDs: [${list.join(', ')}]`;
      navigator.clipboard.writeText(text).then(() => {
        const copyBtn = document.getElementById('copy-btn');
        copyBtn.innerHTML = '<span>✓ Copied to Clipboard!</span>';
        setTimeout(() => {
          copyBtn.innerHTML = '<span>📋 Copy IDs</span>';
        }, 2000);
      });
    }

    function filterCategory(cat) {
      // Update Tab Styles
      document.querySelectorAll('.cat-btn').forEach(btn => {
        btn.classList.remove('bg-sky-500', 'text-slate-950');
        btn.classList.add('bg-slate-900', 'text-slate-300');
      });
      event.target.classList.remove('bg-slate-900', 'text-slate-300');
      event.target.classList.add('bg-sky-500', 'text-slate-950');

      // Filter Cards
      document.querySelectorAll('.template-card').forEach(card => {
        if (cat === 'all' || card.getAttribute('data-cat') === cat) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[OK] Saved HTML Showcase: {HTML_OUT}")

# Also build the Markdown Catalog Artifact
md_lines = [
    "# 50 Master PPT Slide Templates Catalog",
    "",
    "This catalog details all 50 handcrafted presentation slide templates for the **60-Day Full-Stack & Database Engineering Masterclass** and YouTube tech video production.",
    "",
    "> [!TIP]",
    f"> **Interactive Visual Gallery:** Open the interactive HTML gallery to preview all live slide cards, test color themes, and multi-select your favorites: [ppt_templates_showcase.html](file:///{str(HTML_OUT).replace(chr(92), '/')})",
    "",
    "---",
    "",
    "## Summary by Category",
    "",
    "| Category | Range | Focus & Design Aesthetic | Best For |",
    "| :--- | :--- | :--- | :--- |",
    "| **IDE & Dark Themes** | Templates 01–10 | Tokyo Night, Dracula, Monokai, Nord, Synthwave | Code walkthroughs, IDE syntax demos |",
    "| **Architecture & Cloud** | Templates 11–20 | AWS, GCP, Stripe, Uber, Kafka, Kubernetes | High-level system design & cloud topology |",
    "| **Algorithms & Memory** | Templates 21–28 | Stack vs Heap, Trees, Hash Tables, Big-O | LeetCode & core computer science fundamentals |",
    "| **Code Diffs & Fixes** | Templates 29–35 | Split Anti-Pattern vs Pro Fix, Benchmarks | Code quality, refactoring & security defense |",
    "| **Database & Schema** | Templates 36–42 | ER Diagrams, SQL vs NoSQL, B-Trees, ACID | Database engineering, schemas & query plans |",
    "| **Educational & Outros** | Templates 43–50 | Riddles, Steppers, Terminals, Roadmaps, Outros | Student retention, virality & homework CTAs |",
    "",
    "---",
    "",
    "## Detailed Template Breakdown",
    ""
]

for t in TEMPLATES:
    md_lines.append(f"### #{t['id']:02d}: {t['name']} (`{t['tag']}`)")
    md_lines.append(f"- **Category:** {t['category_name']}")
    md_lines.append(f"- **Palette:** Background `{t['bg']}` | Card `{t['card_bg']}` | Accent `{t['accent']}`")
    md_lines.append(f"- **Description:** {t['desc']}")
    md_lines.append(f"- **Layout Type:** `{t.get('layout_type')}`")
    md_lines.append("")

with open(MD_OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"[OK] Saved Markdown Catalog: {MD_OUT}")
