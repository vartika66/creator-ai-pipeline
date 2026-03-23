# Creator AI Pipeline

An AI-powered tool that helps YouTubers and influencers automatically generate scripts, clone their voice, and post content to their channels.

---

## What This Project Does

- Generates video scripts from a topic and style
- Saves generated scripts as JSON files with timestamps
- Exposes a REST API so anyone can call it from a browser or app
- (Coming soon) Voice cloning, video generation, auto-posting

---

## Tech Stack

- **Python** — core language
- **FastAPI** — REST API framework
- **Uvicorn** — server to run the API
- **Rich** — beautiful terminal output
- **Pydantic** — data validation
- **JSON** — saving script data

---

## Project Structure

```
creator-ai-pipeline/
├── src/
│   ├── __init__.py
│   ├── script_generator.py   ← generates scripts by topic and style
│   └── api.py                ← FastAPI REST API
├── data/                     ← saved scripts as JSON files
├── logs/                     ← log files (coming soon)
├── tests/                    ← tests (coming soon)
├── .env                      ← environment variables (never pushed to GitHub)
├── .gitignore                ← files to ignore in git
├── requirements.txt          ← Python dependencies
└── README.md                 ← this file
```

---

## Setup — Run This Project Locally

### Step 1 — Clone the repo

```bash
git clone git@github-personal:vartika66/creator-ai-pipeline.git
cd creator-ai-pipeline
```

### Step 2 — Create and activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

> On Windows use: `.venv\Scripts\activate`

### Step 3 — Install dependencies

```bash
pip install fastapi uvicorn rich
```

### Step 4 — Run the API

```bash
uvicorn src.api:app --reload
```

API will be live at: `http://127.0.0.1:8000`

---

## API Endpoints

### GET /
Returns a welcome message.

**Response:**
```json
{
  "message": "Welcome to Creator AI Pipeline API"
}
```

---

### POST /generate-script
Generates a video script based on topic and style.

**Request body:**
```json
{
  "topic": "how to grow on youtube",
  "style": "educational"
}
```

**Available styles:**
- `educational` — teaches the audience step by step
- `entertaining` — story based, day in the life format
- `motivational` — inspires and pushes the audience to take action

**Response:**
```json
{
  "topic": "how to grow on youtube",
  "style": "educational",
  "hook": "Today we are going to learn everything about how to grow on youtube.",
  "problem": "Most people get this wrong because they skip the fundamentals.",
  "points": [
    "Step 1 - What exactly is how to grow on youtube and why it matters",
    "Step 2 - The most important things to know about how to grow on youtube",
    "Step 3 - How to apply this knowledge today"
  ],
  "cta": "Drop your questions in the comments below!"
}
```

**Test it visually:**
Go to `http://127.0.0.1:8000/docs` — FastAPI generates a full interactive UI automatically.

---

## How Scripts Are Saved

Every time you generate a script, it is automatically saved as a JSON file inside the `data/` folder with a timestamp in the filename.

Example: `data/script_2025-03-20_14-30-00.json`

---

## What I Learned Building This

### Python concepts used
- Functions — `def generate_script()`, `def save_script()`
- Dictionaries — storing script data as key value pairs
- Lists — storing the 3 main points of each script
- f-strings — building dynamic text from variables
- if/elif/else — different script styles based on user input
- File handling — saving scripts using `open()` and `with`
- JSON — saving and reading structured data
- imports — using external libraries like `rich`, `fastapi`
- `os.makedirs` — creating folders from code
- `datetime` — adding timestamps to saved files

### Libraries used
- `rich` — colourful terminal output with panels
- `fastapi` — building REST APIs in Python
- `uvicorn` — running the FastAPI server
- `pydantic` — validating request and response data

---

## Roadmap

- [x] Script generator with 3 styles
- [x] Save scripts to JSON files
- [x] FastAPI REST API
- [x] Auto docs at /docs
- [ ] Connect real AI model from Hugging Face
- [ ] Voice cloning with XTTS v2
- [ ] Research agent with LangChain
- [ ] Video generation
- [ ] Auto posting to YouTube and Instagram
- [ ] Frontend dashboard in Next.js

---

## Development Log

| Date | What was built |
|------|---------------|
| Day 1 | Project setup, GitHub SSH, virtual environment |
| Day 1 | Basic script generator with terminal output |
| Day 1 | Style based script generation (educational, entertaining, motivational) |
| Day 1 | Save scripts to JSON files with timestamps |
| Day 1 | FastAPI REST API with /generate-script endpoint |
| Day 1 | Auto documentation at /docs |

---

## Author

Vartika — building an AI content tool for YouTubers and influencers.