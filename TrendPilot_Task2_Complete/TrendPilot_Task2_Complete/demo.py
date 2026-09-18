"""
TrendPilot — CLI Demo
Run this script for a terminal-based demo of the TrendPilot agent.

Usage:
    python demo.py
    python demo.py --topic "YOLOv8 Helmet Detection" --platform LinkedIn --tone Professional
"""

import argparse
import sys
import os

# Ensure project root is on path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.agent import run_agent
from app.tools import ACTIVE_MODEL, OLLAMA_URL


PLATFORMS = [
    "LinkedIn",
    "Instagram Reels",
    "TikTok",
    "YouTube Shorts",
    "X / Twitter",
    "Facebook",
]

TONES = [
    "Professional",
    "Professional + Exciting",
    "Motivational",
    "Casual & Friendly",
    "Humorous",
    "Inspirational",
    "Short & Punchy",
]

OUTPUT_TYPES = [
    "Post",
    "Post + Reel Script",
    "Reel Script",
    "Post + Reel Script + Title & Thumbnail",
]


def print_banner():
    print("\n" + "═" * 62)
    print("  🚀  TrendPilot — Agentic AI Content Assistant")
    print("  AIRI PITB Internship Task 2")
    print(f"  Model: {ACTIVE_MODEL}  |  Ollama: {OLLAMA_URL}")
    print("═" * 62)


def pick_option(prompt: str, options: list) -> str:
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        try:
            choice = int(input("  Enter number: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except (ValueError, KeyboardInterrupt):
            pass
        print("  Invalid choice. Try again.")


def print_result(result: dict):
    sep = "─" * 60

    print(f"\n{sep}")
    print("  AGENT OUTPUT")
    print(sep)

    print(f"\n📋 TOPIC     : {result['topic']}")
    print(f"📱 PLATFORM  : {result['platform']}")
    print(f"🎨 TONE      : {result['tone']}")
    print(f"🤖 MODEL     : {result['model']}")

    print(f"\n💡 CONTENT ANGLES:")
    for i, idea in enumerate(result.get("content_ideas", []), 1):
        prefix = "★" if i == 1 else f"{i}."
        print(f"  {prefix} {idea}")

    print(f"\n🪝 HOOK:\n  {result.get('hook', '')}")

    print(f"\n📝 CAPTION:\n{result.get('caption', '')}")

    print(f"\n🏷️  HASHTAGS:\n  {result.get('hashtags', '')}")

    reel = result.get("reel_script", "")
    if reel:
        print(f"\n🎬 REEL SCRIPT:\n{reel}")

    print(f"\n🎯 TITLE          : {result.get('title', '')}")
    print(f"   THUMBNAIL TEXT : {result.get('thumbnail_text', '')}")

    score = result.get("review_score")
    if score:
        print(f"\n⭐ QUALITY SCORE  : {score}/30")

    print(f"\n💾 SAVED FILE:\n  {result.get('saved_file', 'Not saved')}")
    print(f"\n{sep}\n")


def main():
    parser = argparse.ArgumentParser(description="TrendPilot CLI Demo")
    parser.add_argument("--topic", type=str, default=None, help="Content topic")
    parser.add_argument("--platform", type=str, default=None, help="Target platform")
    parser.add_argument("--tone", type=str, default=None, help="Content tone")
    parser.add_argument("--output", type=str, default=None, help="Output type")
    args = parser.parse_args()

    print_banner()

    # Gather inputs
    if args.topic:
        topic = args.topic
        print(f"\n✅ Topic: {topic}")
    else:
        topic = input("\n📌 Enter your topic: ").strip()
        if not topic:
            topic = "YOLOv8 Helmet Detection Project"

    if args.platform and args.platform in PLATFORMS:
        platform = args.platform
    else:
        platform = pick_option("📱 Choose platform:", PLATFORMS)

    if args.tone and args.tone in TONES:
        tone = args.tone
    else:
        tone = pick_option("🎨 Choose tone:", TONES)

    if args.output and args.output in OUTPUT_TYPES:
        output_type = args.output
    else:
        output_type = pick_option("📦 Choose output type:", OUTPUT_TYPES)

    print(f"\n⚡ Running agent… (this may take 30–120 seconds)\n")

    try:
        result = run_agent(
            topic=topic,
            platform=platform,
            tone=tone,
            output_type=output_type,
            verbose=True,
        )
        print_result(result)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
        sys.exit(0)
    except Exception as exc:
        print(f"\n❌ Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
