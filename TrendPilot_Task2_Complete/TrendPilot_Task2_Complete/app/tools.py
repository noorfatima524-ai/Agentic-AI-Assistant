"""
TrendPilot — Agent Tools
All tools used by the TrendPilot agentic workflow.
"""

import os
import json
import re
from datetime import datetime
from typing import Optional

from app.prompts import (
    TREND_IDEAS_PROMPT,
    CAPTION_PROMPT,
    HASHTAG_PROMPT,
    REEL_SCRIPT_PROMPT,
    TITLE_THUMBNAIL_PROMPT,
    REVIEWER_PROMPT,
    PLAN_PROMPT,
)

# ─── Ollama Helper ─────────────────────────────────────────────────────────────

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
DEFAULT_MODEL = os.environ.get("OLLAMA_MODEL", "gemma3:4b")

# Fallback models in order of preference
FALLBACK_MODELS = ["llama3.2:3b", "phi3:mini", "qwen2.5:3b", "mistral:7b", "tinyllama"]


def _ask_ollama(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """Send a prompt to Ollama and return the response."""
    try:
        import requests  # noqa: PLC0415

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=120,
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as exc:  # noqa: BLE001
        return f"[Ollama Error] {exc}"


def _detect_model() -> str:
    """Detect which Ollama model is available."""
    try:
        import requests  # noqa: PLC0415

        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=10)
        if response.ok:
            models = [m["name"] for m in response.json().get("models", [])]
            if not models:
                return DEFAULT_MODEL
            # Prefer default, then fallbacks, then whatever is first
            for preferred in [DEFAULT_MODEL] + FALLBACK_MODELS:
                for m in models:
                    if preferred.split(":")[0] in m:
                        return m
            return models[0]
    except Exception:  # noqa: BLE001
        pass
    return DEFAULT_MODEL


ACTIVE_MODEL = _detect_model()

# ─── Tool 1: Trend Idea Generator ──────────────────────────────────────────────


def generate_trend_ideas(topic: str, platform: str, tone: str, memory_context: str = "") -> dict:
    """Generate 5 viral content angles for the given topic and platform."""
    print(f"\n[Tool Called]: Trend Idea Generator — {platform} / {topic}")

    prompt = TREND_IDEAS_PROMPT.format(
        topic=topic,
        platform=platform,
        tone=tone,
        memory_context=memory_context or "No previous sessions.",
    )
    raw = _ask_ollama(prompt, ACTIVE_MODEL)

    # Parse numbered list
    ideas = []
    for line in raw.split("\n"):
        line = line.strip()
        if re.match(r"^\d+[\.\)]\s+", line):
            cleaned = re.sub(r"^\d+[\.\)]\s+", "", line)
            if cleaned:
                ideas.append(cleaned)

    if not ideas:
        # Fallback: split by newlines and take non-empty lines
        ideas = [l.strip() for l in raw.split("\n") if l.strip()][:5]

    return {
        "status": "success",
        "ideas": ideas[:5],
        "best_angle": ideas[0] if ideas else "No ideas generated.",
    }


# ─── Tool 2: Hashtag Generator ─────────────────────────────────────────────────


def generate_hashtags(topic: str, platform: str) -> dict:
    """Generate 10 relevant hashtags for the topic and platform."""
    print(f"[Tool Called]: Hashtag Generator — {platform}")

    prompt = HASHTAG_PROMPT.format(topic=topic, platform=platform)
    raw = _ask_ollama(prompt, ACTIVE_MODEL)

    # Extract hashtags
    hashtags = re.findall(r"#\w+", raw)
    if not hashtags:
        hashtags = ["#AI", "#MachineLearning", "#Tech", "#Innovation", "#Python"]

    return {
        "status": "success",
        "hashtags": hashtags[:10],
        "hashtag_string": " ".join(hashtags[:10]),
    }


# ─── Tool 3: Caption Writer ─────────────────────────────────────────────────────


def write_caption(topic: str, platform: str, tone: str, content_angle: str) -> dict:
    """Write a polished post caption for the given platform."""
    print(f"[Tool Called]: Caption Writer — {platform}")

    prompt = CAPTION_PROMPT.format(
        topic=topic,
        platform=platform,
        tone=tone,
        content_angle=content_angle,
    )
    caption = _ask_ollama(prompt, ACTIVE_MODEL)

    # Extract the hook (first line)
    lines = [l for l in caption.split("\n") if l.strip()]
    hook = lines[0] if lines else "Check this out!"

    return {
        "status": "success",
        "caption": caption,
        "hook": hook,
    }


# ─── Tool 4: Reel Script Generator ─────────────────────────────────────────────


def generate_reel_script(topic: str, platform: str, tone: str, hook: str) -> dict:
    """Create a 30-45 second video/reel script."""
    print(f"[Tool Called]: Reel Script Generator — {platform}")

    prompt = REEL_SCRIPT_PROMPT.format(
        topic=topic,
        platform=platform,
        tone=tone,
        hook=hook,
    )
    script = _ask_ollama(prompt, ACTIVE_MODEL)

    return {
        "status": "success",
        "script": script,
    }


# ─── Tool 5: Title & Thumbnail Generator ────────────────────────────────────────


def generate_title_thumbnail(topic: str, platform: str) -> dict:
    """Generate catchy title and thumbnail text."""
    print(f"[Tool Called]: Title & Thumbnail Generator")

    prompt = TITLE_THUMBNAIL_PROMPT.format(topic=topic, platform=platform)
    raw = _ask_ollama(prompt, ACTIVE_MODEL)

    # Parse structured output
    title = subtitle = thumbnail = ""
    for line in raw.split("\n"):
        if line.startswith("TITLE:"):
            title = line.replace("TITLE:", "").strip()
        elif line.startswith("THUMBNAIL TEXT:"):
            thumbnail = line.replace("THUMBNAIL TEXT:", "").strip()
        elif line.startswith("SUBTITLE:"):
            subtitle = line.replace("SUBTITLE:", "").strip()

    return {
        "status": "success",
        "title": title or f"How I Built {topic}",
        "thumbnail_text": thumbnail or topic[:20],
        "subtitle": subtitle or "My AI Journey",
    }


# ─── Tool 6: Content Reviewer ──────────────────────────────────────────────────


def review_content(
    topic: str,
    platform: str,
    tone: str,
    hook: str,
    caption: str,
    hashtags: str,
) -> dict:
    """Review generated content and provide improvement suggestions."""
    print(f"[Tool Called]: Content Reviewer")

    caption_preview = caption[:200] + "..." if len(caption) > 200 else caption

    prompt = REVIEWER_PROMPT.format(
        topic=topic,
        platform=platform,
        tone=tone,
        hook=hook,
        caption_preview=caption_preview,
        hashtags=hashtags,
    )
    review = _ask_ollama(prompt, ACTIVE_MODEL)

    # Extract overall score
    score_match = re.search(r"OVERALL SCORE:\s*(\d+)/30", review)
    score = int(score_match.group(1)) if score_match else None

    return {
        "status": "success",
        "review": review,
        "score": score,
    }


# ─── Tool 7: File Saver ─────────────────────────────────────────────────────────


def save_output(
    topic: str,
    platform: str,
    tone: str,
    content_angle: str,
    hook: str,
    caption: str,
    hashtags: str,
    reel_script: str,
    title: str,
    thumbnail_text: str,
    review: str,
    output_type: str = "post",
) -> dict:
    """Save the final generated content to a Markdown file."""
    print(f"[Tool Called]: File Saver")

    # Create safe filename
    safe_topic = re.sub(r"[^\w\s-]", "", topic.lower()).strip()
    safe_topic = re.sub(r"[\s]+", "_", safe_topic)[:40]
    safe_platform = platform.lower().replace("/", "_").replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{safe_topic}_{safe_platform}_{timestamp}.md"

    # Determine output folder
    if "script" in output_type.lower() or "reel" in output_type.lower():
        folder = os.path.join(
            os.path.dirname(__file__), "..", "outputs", "generated_scripts"
        )
    else:
        folder = os.path.join(
            os.path.dirname(__file__), "..", "outputs", "generated_posts"
        )

    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)

    content = f"""# TrendPilot — Generated Content
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Model:** {ACTIVE_MODEL}

---

## 📋 Input Details
| Field | Value |
|-------|-------|
| **Topic** | {topic} |
| **Platform** | {platform} |
| **Tone** | {tone} |
| **Output Type** | {output_type} |

---

## 💡 Content Angle
{content_angle}

---

## 🪝 Hook
> {hook}

---

## 📝 Caption
{caption}

---

## 🏷️ Hashtags
{hashtags}

---

## 🎬 Reel / Video Script
{reel_script}

---

## 🎯 Title & Thumbnail
**Title:** {title}
**Thumbnail Text:** {thumbnail_text}

---

## 🔍 Content Review
{review}

---

*Generated by TrendPilot — AIRI PITB AI Internship Task 2*
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return {
        "status": "success",
        "filepath": filepath,
        "filename": filename,
        "message": f"✅ Output saved to: {filepath}",
    }


# ─── Helper: Agent Planner ──────────────────────────────────────────────────────


def create_plan(topic: str, platform: str, tone: str, output_type: str) -> str:
    """Generate a brief agent plan for the given task."""
    prompt = PLAN_PROMPT.format(
        topic=topic, platform=platform, tone=tone, output_type=output_type
    )
    return _ask_ollama(prompt, ACTIVE_MODEL)
