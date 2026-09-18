"""
TrendPilot — Agent Orchestrator
Coordinates all tools in the agentic workflow.
"""

from app.tools import (
    generate_trend_ideas,
    write_caption,
    generate_hashtags,
    generate_reel_script,
    generate_title_thumbnail,
    review_content,
    save_output,
    create_plan,
    ACTIVE_MODEL,
)
from app.memory import store_memory, get_memory_context


def run_agent(
    topic: str,
    platform: str,
    tone: str,
    output_type: str = "Post + Reel Script",
    verbose: bool = True,
) -> dict:
    """
    Main agentic workflow.

    Steps:
      1. Load memory context
      2. Create a plan
      3. Generate trend ideas
      4. Write caption + hook
      5. Generate hashtags
      6. Generate reel script (if requested)
      7. Generate title & thumbnail
      8. Review content
      9. Save output
     10. Store to memory
    """

    def log(msg: str):
        if verbose:
            print(msg)

    log("\n" + "═" * 60)
    log("  🚀  TrendPilot Agent — Starting Workflow")
    log("═" * 60)
    log(f"  Topic    : {topic}")
    log(f"  Platform : {platform}")
    log(f"  Tone     : {tone}")
    log(f"  Output   : {output_type}")
    log(f"  Model    : {ACTIVE_MODEL}")
    log("═" * 60)

    result = {
        "topic": topic,
        "platform": platform,
        "tone": tone,
        "output_type": output_type,
        "model": ACTIVE_MODEL,
    }

    # ── Step 1: Memory context ──────────────────────────────────────────────────
    log("\n📂 Step 1: Loading memory context…")
    memory_ctx = get_memory_context()
    log(f"  {memory_ctx}")
    result["memory_context"] = memory_ctx

    # ── Step 2: Agent planning ──────────────────────────────────────────────────
    log("\n🗺️  Step 2: Creating agent plan…")
    plan = create_plan(topic, platform, tone, output_type)
    log(plan)
    result["plan"] = plan

    # ── Step 3: Trend ideas ─────────────────────────────────────────────────────
    log("\n💡 Step 3: Generating trend ideas…")
    ideas_result = generate_trend_ideas(topic, platform, tone, memory_ctx)
    ideas = ideas_result.get("ideas", [])
    best_angle = ideas_result.get("best_angle", topic)

    log("  Content angles:")
    for i, idea in enumerate(ideas, 1):
        log(f"    {i}. {idea}")

    result["content_ideas"] = ideas
    result["best_angle"] = best_angle

    # ── Step 4: Caption + hook ──────────────────────────────────────────────────
    log("\n✍️  Step 4: Writing caption…")
    caption_result = write_caption(topic, platform, tone, best_angle)
    caption = caption_result.get("caption", "")
    hook = caption_result.get("hook", "")

    log(f"  Hook: {hook[:80]}…")
    result["caption"] = caption
    result["hook"] = hook

    # ── Step 5: Hashtags ────────────────────────────────────────────────────────
    log("\n🏷️  Step 5: Generating hashtags…")
    hashtag_result = generate_hashtags(topic, platform)
    hashtags = hashtag_result.get("hashtag_string", "")
    log(f"  {hashtags}")
    result["hashtags"] = hashtags
    result["hashtag_list"] = hashtag_result.get("hashtags", [])

    # ── Step 6: Reel script ─────────────────────────────────────────────────────
    reel_script = ""
    if any(kw in output_type.lower() for kw in ["reel", "script", "video", "short"]):
        log("\n🎬 Step 6: Generating reel script…")
        script_result = generate_reel_script(topic, platform, tone, hook)
        reel_script = script_result.get("script", "")
        log("  Script generated ✓")
    else:
        log("\n🎬 Step 6: Reel script skipped (not in output type).")
    result["reel_script"] = reel_script

    # ── Step 7: Title & thumbnail ───────────────────────────────────────────────
    log("\n🎯 Step 7: Generating title & thumbnail…")
    title_result = generate_title_thumbnail(topic, platform)
    title = title_result.get("title", "")
    thumbnail_text = title_result.get("thumbnail_text", "")
    subtitle = title_result.get("subtitle", "")
    log(f"  Title: {title}")
    log(f"  Thumbnail: {thumbnail_text}")
    result["title"] = title
    result["thumbnail_text"] = thumbnail_text
    result["subtitle"] = subtitle

    # ── Step 8: Content review ──────────────────────────────────────────────────
    log("\n🔍 Step 8: Reviewing content quality…")
    review_result = review_content(topic, platform, tone, hook, caption, hashtags)
    review = review_result.get("review", "")
    score = review_result.get("score")
    if score:
        log(f"  Quality score: {score}/30")
    result["review"] = review
    result["review_score"] = score

    # ── Step 9: Save output ─────────────────────────────────────────────────────
    log("\n💾 Step 9: Saving output to file…")
    save_result = save_output(
        topic=topic,
        platform=platform,
        tone=tone,
        content_angle=best_angle,
        hook=hook,
        caption=caption,
        hashtags=hashtags,
        reel_script=reel_script,
        title=title,
        thumbnail_text=thumbnail_text,
        review=review,
        output_type=output_type,
    )
    saved_path = save_result.get("filepath", "")
    log(f"  {save_result.get('message', '')}")
    result["saved_file"] = saved_path

    # ── Step 10: Memory ─────────────────────────────────────────────────────────
    log("\n🧠 Step 10: Updating memory…")
    memory_msg = store_memory(topic, platform, tone, hook + " | " + hashtags)
    log(f"  {memory_msg}")

    log("\n" + "═" * 60)
    log("  ✅  TrendPilot Agent — Workflow Complete!")
    log("═" * 60 + "\n")

    return result
