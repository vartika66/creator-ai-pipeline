# Interview Prep — Creator AI Pipeline

Real interview questions based on exactly what you built.
Updated every time a new feature is added.

---

## Python Basics

**Q: What is a virtual environment and why do you use it?**
A: A virtual environment is an isolated Python environment for each project. It keeps dependencies separate so they don't conflict. Similar to node_modules in JavaScript. Created with `python -m venv .venv` and activated with `source .venv/bin/activate`.

**Q: What are f-strings in Python?**
A: f-strings embed variables inside strings using curly braces with an f prefix. For example `f"Today we learn about {topic}"`. Equivalent to template literals in JavaScript.

**Q: What does `if __name__ == "__main__"` mean?**
A: It means only run this code if the file is run directly, not when imported by another file. Our `script_generator.py` uses this so `main()` only runs when called directly, not when `api.py` imports it.

**Q: What is a decorator in Python?**
A: A decorator wraps a function to add extra behaviour. FastAPI uses decorators like `@app.get("/")` to define routes. Similar to middleware in Express.js.

**Q: How do you read and write files in Python?**
A: Using `open()` with a `with` statement. The `with` statement automatically closes the file even if an error occurs. We used `json.dump()` to save scripts to JSON files.

**Q: What is list comprehension?**
A: A concise way to create lists in one line. For example `[s.id for s in scripts]` instead of a full for loop. Used heavily in AI and data processing code.

**Q: What is `os.makedirs` and why use `exist_ok=True`?**
A: `os.makedirs` creates a folder and all parent folders. `exist_ok=True` prevents an error if the folder already exists. We used it to create the `data/` folder automatically.

---

## FastAPI

**Q: What is FastAPI and why did you choose it?**
A: FastAPI is a modern Python REST API framework. We chose it because it auto-generates docs at `/docs`, uses type hints for validation, is async-first, and is very similar to Express.js.

**Q: What is Pydantic?**
A: Pydantic validates request and response data. We define shapes using classes that inherit from `BaseModel`. FastAPI automatically validates incoming requests and returns clear errors if data is wrong.

**Q: What is Uvicorn?**
A: Uvicorn is an ASGI server that runs FastAPI. Equivalent to nodemon in JavaScript. The `--reload` flag restarts automatically when code changes.

**Q: What is the `/docs` endpoint?**
A: FastAPI auto-generates interactive Swagger UI documentation at `/docs`. You can test all endpoints directly in the browser without writing any frontend code.

**Q: What is dependency injection in FastAPI?**
A: FastAPI's `Depends()` function injects dependencies into route handlers. We use `db: Session = Depends(get_db)` to automatically provide a database session to every route that needs one — and automatically close it when done.

**Q: What is the difference between `@app.get` and `@app.post` and `@app.delete`?**
A: These correspond to HTTP methods. GET fetches data, POST creates data, DELETE removes data. We use all three for our scripts CRUD API.

---

## Databases and SQLAlchemy

**Q: What is SQLAlchemy?**
A: SQLAlchemy is Python's most popular database ORM (Object Relational Mapper). It lets you interact with databases using Python classes and objects instead of writing raw SQL. Like Prisma or Sequelize in the JavaScript world.

**Q: What is an ORM?**
A: ORM stands for Object Relational Mapper. It maps database tables to Python classes. Instead of writing `SELECT * FROM scripts` you write `db.query(Script).all()`. Much safer and more readable than raw SQL.

**Q: What is SQLite and why did you use it?**
A: SQLite is a lightweight database that stores everything in a single file. It is built into Python — no server needed, no installation. Perfect for development and early stage products. We used it because it requires zero configuration and works immediately.

**Q: How does your database session management work?**
A: We use a `get_db()` generator function that creates a database session, yields it to the route handler, then closes it automatically in the `finally` block. FastAPI's `Depends()` handles this lifecycle automatically.

**Q: What is a primary key?**
A: A unique identifier for each row in a database table. In our scripts table, `id` is the primary key — it auto-increments so every script gets a unique number automatically.

**Q: What does `index=True` mean on a SQLAlchemy column?**
A: It creates a database index on that column, making queries that filter by that column much faster. We indexed the `topic` column so searching scripts by topic is fast even with thousands of records.

**Q: What is the difference between `db.add()`, `db.commit()`, and `db.refresh()`?**
A: `db.add()` stages the new record in memory. `db.commit()` saves it permanently to the database. `db.refresh()` reloads the record from the database so we get the auto-generated ID and timestamp back.

**Q: How would you migrate to PostgreSQL when you scale?**
A: Change one line — the `DATABASE_URL` in `database.py` from `sqlite:///./data/scripts.db` to `postgresql://user:password@host/dbname`. SQLAlchemy handles the rest because all our queries use the ORM, not raw SQL.

---

## System Design

**Q: How is your project structured and why?**
A: Separation of concerns. `script_generator.py` handles business logic. `database.py` handles data models and DB connection. `api.py` handles HTTP routing. Each file has one responsibility — easy to maintain and test independently.

**Q: Why did you use SQLite instead of PostgreSQL?**
A: SQLite requires zero setup and is perfect for development and early stage products. When we get real users we switch to PostgreSQL by changing one line — the database URL. SQLAlchemy abstracts away the database-specific code.

**Q: What is CRUD and how did you implement it?**
A: CRUD stands for Create, Read, Update, Delete — the four basic database operations. We implemented Create with `POST /generate-script`, Read with `GET /scripts` and `GET /scripts/{id}`, and Delete with `DELETE /scripts/{id}`. Update comes next.

**Q: How would you add pagination to the GET /scripts endpoint?**
A: Add `skip` and `limit` parameters. For example `db.query(Script).offset(skip).limit(limit).all()`. Then the API accepts `?skip=0&limit=10` query parameters. This prevents returning thousands of records at once.

**Q: What would you add to make this production ready?**
A: User authentication so each user only sees their own scripts, rate limiting, error handling and logging, environment-based configuration, input validation, and a CI/CD pipeline for automatic deployment.

---

## AI and Machine Learning

**Q: What is Hugging Face?**
A: The largest open source AI platform. Hosts thousands of pretrained models. Like npm but for AI models. We use their router API to call LLaMA 3.1 without needing our own GPU.

**Q: What is LLaMA?**
A: LLaMA (Large Language Model Meta AI) is Meta's open source language model. The 3.1 8B version has 8 billion parameters and is free to use. It generates human-like text from prompts.

**Q: What is the difference between a base model and an instruct model?**
A: A base model just predicts the next token — it completes text. An instruct model is fine-tuned to follow instructions and have conversations. We use `llama3.1:8b-instruct` — the instruct version — because we want it to follow our script writing instructions.

**Q: What is prompt engineering?**
A: Designing the text instructions you send to an AI model to get the best output. We engineered our prompt to specify the exact script structure — HOOK, PROBLEM, MAIN POINTS, CTA — and the style. Better prompts = better scripts.

**Q: What is the difference between training and inference?**
A: Training teaches a model by updating its parameters on a large dataset — costs millions of dollars. Inference is using an already trained model to generate responses — what we're doing. We never train from scratch, we use pretrained models.

**Q: What is fine-tuning?**
A: Taking a pretrained model and training it further on your own specific data. We plan to fine-tune LLaMA on thousands of viral YouTube scripts so it generates better creator-specific content than a general model.

**Q: What is LoRA?**
A: Low-Rank Adaptation — a technique to fine-tune large models by only updating a small number of extra parameters instead of all billions. Makes fine-tuning fast and cheap while achieving similar results to full fine-tuning.

**Q: What is tokenization?**
A: Converting text into numbers (tokens) that the model can process. "revolt of 1857" becomes something like [1494, 310, 220]. LLaMA has a vocabulary of 32,000 tokens. This is the first step in every LLM inference call.

**Q: What is the Hugging Face router and why did you use it?**
A: The Hugging Face router is their new inference API endpoint that replaced the old api-inference.huggingface.co. It uses an OpenAI-compatible format so we can use the OpenAI SDK to call it, making our code very clean and portable.

---

## Git and GitHub

**Q: What is the difference between git add, git commit, and git push?**
A: `git add` stages changes. `git commit` saves a snapshot locally with a message. `git push` uploads commits to GitHub.

**Q: What is a .gitignore file?**
A: Tells git which files never to track. We added `.env` so API tokens never get pushed to GitHub accidentally, and `.venv/` so the virtual environment (hundreds of MB) never gets committed.

**Q: What is an SSH key and why did you use it?**
A: An SSH key authenticates with GitHub without a password. We used it to push to a personal GitHub account from a laptop also connected to a company account — using separate SSH keys for each.

**Q: Why did you use port 443 for SSH?**
A: Port 22 (default SSH) is blocked on many corporate networks. Port 443 (HTTPS) is almost never blocked. GitHub supports SSH over port 443 via ssh.github.com.

---

## Behavioural Questions

**Q: Tell me about a project you built from scratch.**
A: Talk about this project — the problem (creators spending hours on scripts), the solution (AI pipeline), tech stack, and what you learned. Mention you built it while learning Python simultaneously — shows ability to learn fast and ship real things.

**Q: How do you learn new technologies?**
A: Learn-apply-repeat. Never just watch tutorials — immediately apply each concept to a real project. Every Python concept learned was used the same day in the creator AI pipeline.

**Q: How do you handle being stuck on a problem?**
A: Under 15 minutes — Google the exact error. Under 30 minutes — ask AI tools with full context. Over 30 minutes — identify the knowledge gap, go back to the source, then return. Never spend more than 30 minutes stuck without seeking help.

**Q: How did you handle the Hugging Face API changing their endpoint?**
A: When the old endpoint returned a 410 error with a message pointing to the new router URL, I read the error message carefully, updated the URL and payload format to match their new OpenAI-compatible API, and tested until it worked. Error messages are documentation — read them carefully.

---

*Updated every time a new feature is built.*
*Last updated: Day 1 — Database + CRUD complete*