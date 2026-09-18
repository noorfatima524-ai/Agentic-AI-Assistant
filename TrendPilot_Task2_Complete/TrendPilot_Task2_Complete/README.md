# 🚀 TrendPilot — Local Agentic AI Content Assistant

> **AIRI PITB AI Internship — Task 2**  
> An end-to-end Agentic AI project using Ollama + a local LLM

---

## 📌 Project Overview

**TrendPilot** is a local Agentic AI assistant that takes a user's project topic and produces a complete, ready-to-post viral content plan. It is powered by a small local LLM running through **Ollama** (recommended: Gemma 3:4B).

Unlike a simple chatbot, TrendPilot **plans → uses tools → reviews → saves** — demonstrating a full agentic workflow.

**What the agent produces:**
- 5 viral content angles (ideas)
- A platform-specific caption with a strong hook
- 10 relevant hashtags
- A 30–45 second reel/video script
- A catchy title and thumbnail text
- A quality review with an improvement suggestion
- A saved Markdown file of all outputs

---

## 🧰 Tech Stack

| Component | Choice |
|-----------|--------|
| Language | Python 3.9+ |
| Local LLM | Ollama |
| Recommended Model | Gemma 3:4B (fallback: Llama 3.2:3b, Phi-3 Mini, Qwen 2.5:3b) |
| UI | Streamlit |
| Memory | JSON file |
| Output format | Markdown (.md) |
| CLI demo | Python argparse |

---

## 🗂️ Project Structure

```
TrendPilot_Task2_Complete/
│
├── app/
│   ├── __init__.py
│   ├── main.py        # Streamlit UI
│   ├── agent.py       # Agent orchestrator (10-step workflow)
│   ├── tools.py       # 7 agent tools
│   ├── memory.py      # JSON-based memory tool
│   └── prompts.py     # All LLM prompt templates
│
├── outputs/
│   ├── generated_posts/     # Saved LinkedIn/Instagram posts (.md)
│   ├── generated_scripts/   # Saved reel scripts (.md)
│   └── saved_results/       # memory.json
│
├── tests/
│   └── test_cases.md        # 10 test cases + error analysis table
│
├── screenshots/             # (add your screenshots here)
├── report/                  # (add your final report PDF here)
│
├── README.md
├── requirements.txt
└── demo.py                  # CLI demo
```

---

## ⚙️ Setup & Installation

### 1. Install Ollama

Download from [https://ollama.com](https://ollama.com) and verify:

```bash
ollama --version
```

### 2. Pull a local model

```bash
ollama pull gemma3:4b
# OR if your hardware is limited:
ollama pull llama3.2:3b
ollama pull phi3:mini
```

### 3. Test the model

```bash
ollama run gemma3:4b
# Try: "Give me 5 viral LinkedIn post ideas about AI internships."
```

### 4. Clone and install dependencies

```bash
git clone <your-repo-url>
cd TrendPilot_Task2_Complete
pip install -r requirements.txt
```

---

## 🚀 Running the App

### Option A: Streamlit Web UI

```bash
streamlit run app/main.py
```

Open `http://localhost:8501` in your browser.

### Option B: CLI Demo

```bash
# Interactive mode
python demo.py

# Non-interactive mode
python demo.py --topic "YOLOv8 Helmet Detection" --platform LinkedIn --tone Professional
```

---

## 🤖 Agent Workflow

```
User Input (Topic + Platform + Tone + Output Type)
     ↓
[1] Load Memory Context
     ↓
[2] Create Agent Plan
     ↓
[3] Generate 5 Trend Ideas  ← Tool: Trend Idea Generator
     ↓
[4] Write Caption + Hook    ← Tool: Caption Writer
     ↓
[5] Generate Hashtags       ← Tool: Hashtag Generator
     ↓
[6] Generate Reel Script    ← Tool: Reel Script Generator
     ↓
[7] Title & Thumbnail       ← Tool: Title & Thumbnail Generator
     ↓
[8] Review Content          ← Tool: Content Reviewer
     ↓
[9] Save Output to File     ← Tool: File Saver (Mandatory)
     ↓
[10] Store to Memory        ← Tool: Memory Tool
     ↓
Final Output Returned
```

---

## 🛠️ Tools Implemented

| # | Tool | Description |
|---|------|-------------|
| 1 | **Trend Idea Generator** | Generates 5 viral content angles for the topic and platform |
| 2 | **Caption Writer** | Writes a polished post caption with a strong hook |
| 3 | **Hashtag Generator** | Produces 10 relevant and trending hashtags |
| 4 | **Reel Script Generator** | Creates a 30–45 sec video script with 4 scenes |
| 5 | **Title & Thumbnail Generator** | Generates a catchy title, thumbnail text, and subtitle |
| 6 | **Content Reviewer** | Reviews 6 quality criteria and gives a score out of 30 |
| 7 | **File Saver** *(Mandatory)* | Saves the full content plan as a `.md` file |
| 8 | **Memory Tool** | Stores previous topics/outputs in `memory.json` |

---

## 🧪 Example Output

**Input:**
- Topic: YOLOv8 Helmet Detection Project
- Platform: LinkedIn
- Tone: Professional + Exciting
- Output: Post + Reel Script

**Agent output (excerpt):**

```
Hook:
I trained an AI model to detect helmet safety violations — 
and the biggest lesson wasn't the model, it was the data.

Caption:
This week, I completed an end-to-end Helmet Safety Detection 
system using YOLOv8. Here's what the journey looked like...

Hashtags:
#ComputerVision #YOLOv8 #AI #DeepLearning #MachineLearning 
#Python #SafetyTech #ObjectDetection #OpenCV #Internship

Quality Score: 26/30
Saved File: outputs/generated_posts/yolov8_helmet_linkedin_20240918.md
```

---

## 📊 Testing

10 test cases are documented in `tests/test_cases.md`, covering:
- LinkedIn professional posts
- Instagram/TikTok reel scripts
- X/Twitter short posts
- YouTube Shorts video scripts
- Humorous, motivational, and inspirational tones

---

## 🔧 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_URL` | `http://localhost:11434` | Ollama server URL |
| `OLLAMA_MODEL` | `gemma3:4b` | Model to use |

---

## 🌐 Google Colab

Use the provided `TrendPilot_Task2_Google_Colab.ipynb` notebook to run this project in Google Colab:
1. Upload the project ZIP
2. Run the setup cells
3. Configure your Ollama URL (external server recommended for Colab)
4. Launch Streamlit via ngrok

---

## 📋 Marking Criteria Covered

- ✅ Problem understanding & project idea
- ✅ Ollama setup & local model usage
- ✅ Agent workflow design (10 steps)
- ✅ Tool implementation (7 tools + memory)
- ✅ Memory & file saving
- ✅ Demo interface (Streamlit + CLI)
- ✅ Testing (10 test cases)
- ✅ README & documentation
- ✅ LinkedIn/GitHub portfolio readiness

---

## 👤 Author

Built as part of **AIRI Team PITB — AI Internship Task 2**  
*End-to-End Agentic AI Project Assignment*

---

*#AgenticAI #Ollama #LocalLLM #Python #AIInternship #PITB #AIRI #MachineLearning*
