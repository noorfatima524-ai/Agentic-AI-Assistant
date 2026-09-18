"""
TrendPilot — Prompt Templates
All LLM prompt templates used by the agent tools.
"""

TREND_IDEAS_PROMPT = """You are a viral content strategist. Given the topic below, generate exactly 5 creative and trending content angles suitable for {platform}.

Topic: {topic}
Platform: {platform}
Target Tone: {tone}
Memory Context: {memory_context}

Return ONLY a numbered list of 5 content angles. Each angle should be one sentence. Be specific, creative, and platform-appropriate.

1."""

CAPTION_PROMPT = """You are an expert social media copywriter specializing in {platform} content.

Topic: {topic}
Platform: {platform}
Tone: {tone}
Best Content Angle: {content_angle}

Write a complete, polished {platform} caption. Include:
- A powerful opening hook (first line)
- 3-4 body paragraphs explaining the topic
- A call-to-action at the end
- Keep it under 300 words
- Use line breaks for readability

Write the caption now:"""

HASHTAG_PROMPT = """You are a hashtag research expert for {platform}.

Topic: {topic}
Platform: {platform}

Generate exactly 10 highly relevant and trending hashtags for this content. Mix popular and niche tags.
Return ONLY the hashtags separated by spaces, starting with #.

Hashtags:"""

REEL_SCRIPT_PROMPT = """You are a viral short-video script writer.

Topic: {topic}
Platform: {platform}
Tone: {tone}
Hook: {hook}

Write a 30-45 second video script with this exact structure:

SCENE 1 - HOOK (0-5 sec):
[Visual]: ...
[Voiceover]: ...

SCENE 2 - SETUP (5-15 sec):
[Visual]: ...
[Voiceover]: ...

SCENE 3 - MAIN CONTENT (15-35 sec):
[Visual]: ...
[Voiceover]: ...

SCENE 4 - CLOSING (35-45 sec):
[Visual]: ...
[Voiceover]: ...

Keep voiceover lines short and punchy. Write the script now:"""

TITLE_THUMBNAIL_PROMPT = """You are a YouTube/Instagram title and thumbnail expert.

Topic: {topic}
Platform: {platform}

Generate:
1. TITLE: A catchy, click-worthy title (under 60 characters)
2. THUMBNAIL TEXT: Bold 3-5 word text for a thumbnail image
3. SUBTITLE: A supporting line that adds context (under 40 characters)

Format exactly as:
TITLE: ...
THUMBNAIL TEXT: ...
SUBTITLE: ..."""

REVIEWER_PROMPT = """You are a senior content quality reviewer.

Review the following content plan and provide specific, actionable feedback:

Topic: {topic}
Platform: {platform}
Tone: {tone}

--- CONTENT TO REVIEW ---
Hook: {hook}
Caption Preview: {caption_preview}
Hashtags: {hashtags}
---

Evaluate these 6 criteria and give a score (1-5) + one-line comment for each:

1. HOOK STRENGTH (Is it attention-grabbing?):
2. CLARITY (Is the message clear?):
3. LENGTH (Is it appropriate for {platform}?):
4. TONE MATCH (Does it match "{tone}"?):
5. HASHTAG RELEVANCE (Are hashtags on-point?):
6. PLATFORM FIT (Is it optimized for {platform}?):

Then write:
OVERALL SCORE: X/30
SUMMARY: (2-3 sentences)
TOP IMPROVEMENT: (one specific, actionable suggestion)"""

PLAN_PROMPT = """You are an AI content planning agent.

A user wants to create content with these details:
- Topic: {topic}
- Platform: {platform}
- Tone: {tone}
- Output Type: {output_type}

Create a brief 6-step action plan for generating this content. Number each step.
Be concise — one line per step.

Plan:
1."""
