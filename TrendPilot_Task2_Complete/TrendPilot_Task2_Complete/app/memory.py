"""
TrendPilot — Memory Tool
Stores previous topics, platforms, and generated outputs using JSON.
"""

import json
import os
from datetime import datetime

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "..", "outputs", "saved_results", "memory.json")


def _load_memory() -> list:
    """Load memory from JSON file."""
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def _save_memory(data: list) -> None:
    """Save memory to JSON file."""
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def store_memory(topic: str, platform: str, tone: str, output_summary: str) -> str:
    """Store a new entry in memory."""
    memory = _load_memory()
    entry = {
        "id": len(memory) + 1,
        "timestamp": datetime.now().isoformat(),
        "topic": topic,
        "platform": platform,
        "tone": tone,
        "output_summary": output_summary[:300],  # Store first 300 chars as summary
    }
    memory.append(entry)
    _save_memory(memory)
    return f"✅ Memory saved. Total entries: {len(memory)}"


def get_recent_memory(n: int = 3) -> list:
    """Retrieve the n most recent memory entries."""
    memory = _load_memory()
    return memory[-n:] if memory else []


def get_memory_context() -> str:
    """Return a formatted string of recent memory for use in prompts."""
    recent = get_recent_memory(3)
    if not recent:
        return "No previous sessions found."
    lines = ["Previous sessions:"]
    for entry in recent:
        lines.append(
            f"  - [{entry['timestamp'][:10]}] Topic: {entry['topic']} | "
            f"Platform: {entry['platform']} | Tone: {entry['tone']}"
        )
    return "\n".join(lines)


def clear_memory() -> str:
    """Clear all memory entries."""
    _save_memory([])
    return "🗑️ Memory cleared."


def get_all_memory() -> list:
    """Return all memory entries."""
    return _load_memory()
