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
- **SQLAlchemy** — database ORM
- **SQLite** — database (zero config, built into Python)
- **Pydantic** — data validation
- **Rich** — beautiful terminal output
- **OpenAI SDK** — used to call Hugging Face router
- **LLaMA 3.1 8B** — AI model via Hugging Face router

---

## Project Structure

```
creator-ai-pipeline/
├── src/
│   ├── __init__.py
│   ├── script_generator.py   ← generates scripts (template + AI)
│   ├── api.py                ← FastAPI REST API
│   └── database.py           ← SQLAlchemy models and DB setup
├── data/
│   ├── scripts.db            ← SQLite database
│   └── script_*.json         ← legacy JSON saves
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
pip install fastapi uvicorn rich sqlalchemy python-dotenv openai requests
```

### Step 4 — Add environment variables

Create a `.env` file in the root:

```
HUGGINGFACE_API_TOKEN=your_token_here
```

Get your token from huggingface.co/settings/tokens

### Step 5 — Run the API

```bash
uvicorn src.api:app --reload
```

API live at: `http://127.0.0.1:8000`
Docs at: `http://127.0.0.1:8000/docs`

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
Generates a template-based video script and saves to database.

**Request:**
```json
{ "topic": "how to grow on youtube", "style": "educational" }
```

**Styles:** educational / entertaining / motivational

### POST /generate-ai-script
Generates a full AI-powered script using LLaMA 3.1 8B.

**Request:**
```json
{ "topic": "revolt of 1857", "style": "educational" }
```

### GET /scripts
Returns all saved scripts ordered by most recent first.

### GET /scripts/{script_id}
Returns full details of a specific script by ID.

### DELETE /scripts/{script_id}
Deletes a script by ID.

---

## Database Schema

```
scripts table
├── id             INTEGER  primary key, auto increment
├── topic          STRING   indexed
├── style          STRING   educational / entertaining / motivational
├── hook           TEXT
├── problem        TEXT
├── points         TEXT     JSON array
├── cta            TEXT
├── generated_text TEXT     full AI generated script
├── source         STRING   template / llama-3.1-8b
└── created_at     DATETIME auto set on creation
```

---

## Roadmap

- [x] Script generator with 3 styles
- [x] AI script generation with LLaMA 3.1 8B
- [x] Save scripts to JSON files
- [x] FastAPI REST API
- [x] Auto docs at /docs
- [x] SQLite database with SQLAlchemy
- [x] Full CRUD endpoints
- [ ] User authentication with JWT
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
| Day 1 | Script generator with 3 styles |
| Day 1 | Save scripts to JSON files |
| Day 1 | FastAPI REST API |
| Day 1 | Connected LLaMA 3.1 8B via Hugging Face router |
| Day 2 | SQLite database with SQLAlchemy |
| Day 2 | Full CRUD endpoints |

---

## Author

Vartika — building an AI content tool for YouTubers and influencers.