"""
TrendPilot — Streamlit UI
Main web interface for the TrendPilot Agentic AI Content Assistant.
"""

import os
import sys

# Ensure the project root is on the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from app.agent import run_agent
from app.memory import get_all_memory, clear_memory
from app.tools import ACTIVE_MODEL, OLLAMA_URL

# ─── Page config ───────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="TrendPilot — AI Content Agent",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────

st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;700&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .block-container { padding-top: 1.5rem; }

    .tp-header {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        color: white;
    }
    .tp-header h1 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.4rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .tp-header p {
        font-size: 1rem;
        opacity: 0.75;
        margin: 0.4rem 0 0;
    }

    .tool-badge {
        display: inline-block;
        background: #312e81;
        color: #c7d2fe;
        font-size: 0.72rem;
        font-weight: 600;
        padding: 3px 10px;
        border-radius: 20px;
        margin: 2px 3px;
        letter-spacing: 0.3px;
    }

    .result-card {
        background: #1e1b4b;
        border: 1px solid #312e81;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
        color: #e0e7ff;
    }
    .result-card h4 {
        color: #818cf8;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin: 0 0 0.6rem;
    }

    .hook-text {
        font-size: 1.15rem;
        font-weight: 600;
        color: #a5f3fc;
        border-left: 3px solid #22d3ee;
        padding-left: 1rem;
        font-style: italic;
    }

    .hashtag-chip {
        display: inline-block;
        background: #1e3a5f;
        color: #7dd3fc;
        font-size: 0.8rem;
        padding: 3px 10px;
        border-radius: 20px;
        margin: 2px;
    }

    .score-badge {
        font-size: 1.4rem;
        font-weight: 700;
        color: #4ade80;
    }

    .status-bar {
        background: #111827;
        border: 1px solid #374151;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-size: 0.82rem;
        color: #9ca3af;
        margin-bottom: 1rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

# ─── Header ────────────────────────────────────────────────────────────────────

st.markdown(
    f"""
<div class="tp-header">
    <h1>🚀 TrendPilot</h1>
    <p>Agentic AI Content Assistant — AIRI PITB Internship Task 2</p>
</div>
<div class="status-bar">
    🤖 Model: <strong>{ACTIVE_MODEL}</strong> &nbsp;|&nbsp;
    🌐 Ollama: <strong>{OLLAMA_URL}</strong>
    &nbsp;&nbsp;
    <span class="tool-badge">Trend Ideas</span>
    <span class="tool-badge">Caption Writer</span>
    <span class="tool-badge">Hashtag Generator</span>
    <span class="tool-badge">Reel Script</span>
    <span class="tool-badge">Title & Thumbnail</span>
    <span class="tool-badge">Content Reviewer</span>
    <span class="tool-badge">File Saver</span>
    <span class="tool-badge">Memory</span>
</div>
""",
    unsafe_allow_html=True,
)

# ─── Sidebar ───────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("### ⚙️ Agent Settings")

    topic = st.text_area(
        "📌 Topic",
        value="YOLOv8 Helmet Detection Project",
        height=80,
        help="Describe your project or topic in detail.",
    )

    platform = st.selectbox(
        "📱 Platform",
        ["LinkedIn", "Instagram Reels", "TikTok", "YouTube Shorts", "X / Twitter", "Facebook"],
    )

    tone = st.selectbox(
        "🎨 Tone",
        [
            "Professional",
            "Professional + Exciting",
            "Motivational",
            "Casual & Friendly",
            "Humorous",
            "Inspirational",
            "Short & Punchy",
        ],
    )

    output_type = st.multiselect(
        "📦 Output Type",
        ["Post", "Reel Script", "Title & Thumbnail", "Hashtags"],
        default=["Post", "Reel Script"],
    )
    output_type_str = " + ".join(output_type) if output_type else "Post"

    st.divider()

    generate_btn = st.button(
        "⚡ Generate Content", type="primary", use_container_width=True
    )

    st.divider()
    st.markdown("### 🧠 Memory")
    memories = get_all_memory()
    if memories:
        st.caption(f"{len(memories)} session(s) stored")
        for m in memories[-3:]:
            st.markdown(
                f"- **{m['topic'][:30]}** › {m['platform']}",
                help=f"Tone: {m['tone']} | {m['timestamp'][:10]}",
            )
        if st.button("🗑️ Clear Memory", use_container_width=True):
            clear_memory()
            st.success("Memory cleared!")
            st.rerun()
    else:
        st.caption("No sessions yet.")

# ─── Main area ─────────────────────────────────────────────────────────────────

if generate_btn:
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("🤖 Agent running — calling tools, please wait…"):
            result = run_agent(
                topic=topic.strip(),
                platform=platform,
                tone=tone,
                output_type=output_type_str,
                verbose=True,
            )

        st.success(f"✅ Content generated! Saved to: `{result.get('saved_file', 'N/A')}`")

        # ── Plan ────────────────────────────────────────────────────────────────
        with st.expander("🗺️ Agent Plan", expanded=False):
            st.code(result.get("plan", "N/A"), language=None)

        # ── Main results ────────────────────────────────────────────────────────
        col1, col2 = st.columns([3, 2])

        with col1:
            st.markdown("#### 💡 Content Angles")
            ideas = result.get("content_ideas", [])
            for i, idea in enumerate(ideas, 1):
                badge = "⭐ Best" if i == 1 else f"{i}."
                st.markdown(f"**{badge}** {idea}")

            st.divider()

            st.markdown("#### 🪝 Hook")
            st.markdown(
                f'<p class="hook-text">{result.get("hook", "")}</p>',
                unsafe_allow_html=True,
            )

            st.divider()

            st.markdown("#### 📝 Caption")
            st.text_area(
                "Full Caption",
                value=result.get("caption", ""),
                height=250,
                label_visibility="collapsed",
            )

        with col2:
            st.markdown("#### 🏷️ Hashtags")
            hashtag_list = result.get("hashtag_list", [])
            chips_html = "".join(
                f'<span class="hashtag-chip">{h}</span>' for h in hashtag_list
            )
            st.markdown(chips_html, unsafe_allow_html=True)

            st.divider()

            st.markdown("#### 🎯 Title & Thumbnail")
            st.markdown(
                f"""
<div class="result-card">
    <h4>Title</h4>
    <p style="font-size:1rem;font-weight:600;">{result.get("title","")}</p>
    <h4 style="margin-top:1rem;">Thumbnail Text</h4>
    <p style="font-size:1.2rem;font-weight:700;color:#fbbf24;">{result.get("thumbnail_text","")}</p>
    <h4 style="margin-top:1rem;">Subtitle</h4>
    <p style="font-size:0.9rem;opacity:0.8;">{result.get("subtitle","")}</p>
</div>
""",
                unsafe_allow_html=True,
            )

            score = result.get("review_score")
            if score:
                st.markdown(
                    f'<p>Quality Score: <span class="score-badge">{score}/30</span></p>',
                    unsafe_allow_html=True,
                )

        # ── Reel script ──────────────────────────────────────────────────────────
        reel_script = result.get("reel_script", "")
        if reel_script:
            st.divider()
            st.markdown("#### 🎬 Reel / Video Script")
            st.text_area(
                "Script",
                value=reel_script,
                height=300,
                label_visibility="collapsed",
            )

        # ── Review ───────────────────────────────────────────────────────────────
        with st.expander("🔍 Content Review", expanded=False):
            st.text(result.get("review", "No review available."))

        # ── Save & download ──────────────────────────────────────────────────────
        saved_path = result.get("saved_file", "")
        if saved_path and os.path.exists(saved_path):
            with open(saved_path, "r", encoding="utf-8") as f:
                file_content = f.read()
            st.download_button(
                label="⬇️ Download Markdown Output",
                data=file_content,
                file_name=os.path.basename(saved_path),
                mime="text/markdown",
                use_container_width=True,
            )

else:
    # Welcome screen
    st.markdown(
        """
<div style="text-align:center; padding: 3rem 1rem; color: #6b7280;">
    <div style="font-size: 4rem;">🚀</div>
    <h3 style="color: #374151;">Ready to go viral?</h3>
    <p>Enter your topic in the sidebar and click <strong>Generate Content</strong>.<br>
    The agent will call 8 tools and produce a complete content plan for you.</p>
    <br>
    <p style="font-size:0.85rem;">
    <strong>Try this:</strong> Topic: <em>YOLOv8 Helmet Detection</em> • Platform: LinkedIn • Tone: Professional + Exciting
    </p>
</div>
""",
        unsafe_allow_html=True,
    )
