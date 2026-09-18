# TrendPilot — Test Cases

Run these 10 test inputs to validate the agent. Record results below.

---

## Test Case Table

| # | Topic | Platform | Tone | Expected Output | Result | Notes |
|---|-------|----------|------|-----------------|--------|-------|
| 1 | YOLOv8 helmet detection | LinkedIn | Professional | Post + hashtags | | |
| 2 | AI internship experience | LinkedIn | Motivational | Post | | |
| 3 | Python learning journey | Instagram Reels | Casual & Friendly | Reel script | | |
| 4 | Machine learning project | X / Twitter | Short & Punchy | Short post | | |
| 5 | Data annotation struggles | LinkedIn | Humorous | Post | | |
| 6 | Model failed in production | Instagram Reels | Humorous | Reel script | | |
| 7 | Final year project | LinkedIn | Professional | Post + Reel Script | | |
| 8 | Computer vision project | YouTube Shorts | Professional + Exciting | Video script | | |
| 9 | Debugging FastAPI | X / Twitter | Humorous | Short post | | |
| 10 | Open-source contribution | LinkedIn | Inspirational | Post | | |

---

## Test Case Details

### Test 1 — YOLOv8 Helmet Detection (LinkedIn, Professional)
- **Input topic:** YOLOv8 helmet detection project for safety monitoring
- **Platform:** LinkedIn
- **Tone:** Professional
- **Output type:** Post + Hashtags
- **Tools called:** Trend Idea Generator, Caption Writer, Hashtag Generator, Content Reviewer, File Saver
- **Expected:** Well-structured post with technical terms, 8-10 relevant hashtags
- **Actual output:** *(fill in after running)*
- **Saved file:** `outputs/generated_posts/yolov8_helmet_linkedin_YYYYMMDD.md`
- **Result:** ✅ / ❌
- **Notes:**

---

### Test 2 — AI Internship Experience (LinkedIn, Motivational)
- **Input topic:** My experience as an AI intern at PITB — lessons learned
- **Platform:** LinkedIn
- **Tone:** Motivational
- **Output type:** Post
- **Tools called:** Trend Idea Generator, Caption Writer, Hashtag Generator, File Saver
- **Expected:** Inspiring post about growth and learning, motivational language
- **Actual output:** *(fill in after running)*
- **Result:** ✅ / ❌
- **Notes:**

---

### Test 3 — Python Learning Journey (Instagram Reels, Casual & Friendly)
- **Input topic:** How I went from zero to Python programmer in 3 months
- **Platform:** Instagram Reels
- **Tone:** Casual & Friendly
- **Output type:** Reel Script
- **Tools called:** Trend Idea Generator, Caption Writer, Reel Script Generator, File Saver
- **Expected:** Fun, conversational 30-45 second script with relatable moments
- **Actual output:** *(fill in after running)*
- **Result:** ✅ / ❌
- **Notes:**

---

### Test 4 — Machine Learning Project (X / Twitter, Short & Punchy)
- **Input topic:** I trained my first ML model and it actually works
- **Platform:** X / Twitter
- **Tone:** Short & Punchy
- **Output type:** Post
- **Tools called:** Caption Writer, Hashtag Generator, File Saver
- **Expected:** Concise post under 280 characters, punchy language
- **Actual output:** *(fill in after running)*
- **Result:** ✅ / ❌
- **Notes:**

---

### Test 5 — Data Annotation Struggles (LinkedIn, Humorous)
- **Input topic:** 500 images labeled by hand — what I learned about data annotation
- **Platform:** LinkedIn
- **Tone:** Humorous
- **Output type:** Post
- **Tools called:** Trend Idea Generator, Caption Writer, Hashtag Generator, Content Reviewer, File Saver
- **Expected:** Witty post that still conveys technical learning
- **Actual output:** *(fill in after running)*
- **Result:** ✅ / ❌
- **Notes:**

---

### Test 6 — Model Failed in Production (Instagram Reels, Humorous)
- **Input topic:** When your model works on validation but fails in production
- **Platform:** Instagram Reels
- **Tone:** Humorous
- **Output type:** Post + Reel Script
- **Tools called:** Trend Idea Generator, Caption Writer, Reel Script Generator, Hashtag Generator, File Saver
- **Expected:** Funny, relatable script — meme energy
- **Actual output:** *(fill in after running)*
- **Result:** ✅ / ❌
- **Notes:**

---

### Test 7 — Final Year Project (LinkedIn, Professional)
- **Input topic:** My final year project — Helmet Safety Detection System using YOLOv8 and Raspberry Pi
- **Platform:** LinkedIn
- **Tone:** Professional
- **Output type:** Post + Reel Script
- **Tools called:** All 7 tools
- **Expected:** Professional portfolio-style post with structured reel script
- **Actual output:** *(fill in after running)*
- **Result:** ✅ / ❌
- **Notes:**

---

### Test 8 — Computer Vision Project (YouTube Shorts, Professional + Exciting)
- **Input topic:** Building a real-time object detection system with OpenCV and YOLO
- **Platform:** YouTube Shorts
- **Tone:** Professional + Exciting
- **Output type:** Post + Reel Script + Title & Thumbnail
- **Tools called:** All 7 tools
- **Expected:** Exciting video script with catchy YouTube title and thumbnail text
- **Actual output:** *(fill in after running)*
- **Result:** ✅ / ❌
- **Notes:**

---

### Test 9 — Debugging FastAPI (X / Twitter, Humorous)
- **Input topic:** 4 hours debugging a FastAPI endpoint — it was a missing comma
- **Platform:** X / Twitter
- **Tone:** Humorous
- **Output type:** Post
- **Tools called:** Caption Writer, Hashtag Generator, File Saver
- **Expected:** Very short, funny tweet-style post
- **Actual output:** *(fill in after running)*
- **Result:** ✅ / ❌
- **Notes:**

---

### Test 10 — Open-Source Contribution (LinkedIn, Inspirational)
- **Input topic:** I made my first open-source contribution to a computer vision library
- **Platform:** LinkedIn
- **Tone:** Inspirational
- **Output type:** Post
- **Tools called:** Trend Idea Generator, Caption Writer, Hashtag Generator, Content Reviewer, File Saver
- **Expected:** Inspiring post encouraging others to contribute to open source
- **Actual output:** *(fill in after running)*
- **Result:** ✅ / ❌
- **Notes:**

---

## Error Analysis

| Test Case | Problem Found | Possible Reason | Fix Applied |
|-----------|---------------|-----------------|-------------|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

*(Fill in after running all 10 tests)*

---

## Suggested Improvements

1. **Better tone prompts:** Add explicit examples in the prompt for each tone (e.g., sample jokes for humorous tone).
2. **Platform-specific constraints:** Enforce character limits per platform (e.g., 280 chars for Twitter) in the caption tool.
3. **Structured output validation:** Add a post-generation validator that checks minimum quality before saving.
