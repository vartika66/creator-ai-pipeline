# Interview Prep — Creator AI Pipeline

These are real interview questions based on exactly what you built.
Updated as you build more features.

---

## Python Basics

**Q: What is a virtual environment and why do you use it?**
A: A virtual environment is an isolated Python environment for each project. It keeps project dependencies separate so they don't conflict with each other. Similar to node_modules in JavaScript. You create it with `python -m venv .venv` and activate it with `source .venv/bin/activate`.

---

**Q: What is the difference between a list and a dictionary in Python?**
A: A list is an ordered collection of items accessed by index — like `points[0]`. A dictionary is a key-value store accessed by key — like `script["topic"]`. In our project, we store script data as a dictionary and the 3 main points as a list inside it.

---

**Q: What are f-strings in Python?**
A: f-strings are a way to embed variables inside strings. You prefix the string with f and put the variable in curly braces. For example `f"Today we will learn about {topic}"`. They are the Python equivalent of template literals in JavaScript.

---

**Q: What is the difference between `*args` and `**kwargs` in Python?**
A: `*args` allows a function to accept any number of positional arguments as a tuple. `**kwargs` allows any number of keyword arguments as a dictionary. For example `def func(*args, **kwargs)`. Used in many AI libraries internally.

---

**Q: What does `if __name__ == "__main__"` mean?**
A: It means — only run this code if this file is being run directly, not when it is imported by another file. In our project, `script_generator.py` has this so the `main()` function only runs when you call the file directly, not when `api.py` imports it.

---

**Q: What is a decorator in Python?**
A: A decorator is a function that wraps another function to add extra behaviour. In FastAPI we use decorators like `@app.get("/")` and `@app.post("/generate-script")` to define API routes. They are similar to middleware in Express.js.

---

**Q: How do you read and write files in Python?**
A: Using the `open()` function with a `with` statement. For example:
```python
with open("file.json", "w") as f:
    json.dump(data, f, indent=4)
```
The `with` statement automatically closes the file when done — even if an error occurs.

---

**Q: What is the difference between `json.dump` and `json.dumps`?**
A: `json.dump` writes JSON to a file object. `json.dumps` converts JSON to a string. In our project we use `json.dump` to save scripts directly to a file.

---

**Q: What is list comprehension in Python?**
A: A concise way to create lists in one line. For example `[x * 2 for x in numbers]` instead of writing a full for loop. Used heavily in AI and data processing code.

---

**Q: What is `os.makedirs` and why did you use `exist_ok=True`?**
A: `os.makedirs` creates a folder and all parent folders if they don't exist. `exist_ok=True` means don't throw an error if the folder already exists. We used it to create the `data/` folder automatically when saving scripts.

---

## FastAPI

**Q: What is FastAPI and why did you choose it?**
A: FastAPI is a modern Python web framework for building REST APIs. We chose it because it is fast, automatically generates API documentation at `/docs`, uses Python type hints for validation, and is async-first. It is similar to Express.js in JavaScript but more powerful for AI applications.

---

**Q: What is Pydantic and how does it work with FastAPI?**
A: Pydantic is a data validation library. In FastAPI we define request and response shapes using Pydantic models — classes that inherit from `BaseModel`. FastAPI automatically validates incoming requests against these models and returns clear error messages if the data is wrong.

---

**Q: What is the difference between `@app.get` and `@app.post`?**
A: `@app.get` handles GET requests — used for fetching data. `@app.post` handles POST requests — used for sending data to create something. In our project, `GET /` returns a welcome message and `POST /generate-script` takes a topic and style and returns a script.

---

**Q: What is Uvicorn?**
A: Uvicorn is an ASGI server that runs FastAPI applications. It is the equivalent of nodemon in JavaScript. The `--reload` flag makes it automatically restart when you change your code during development.

---

**Q: What is the `/docs` endpoint in FastAPI?**
A: FastAPI automatically generates interactive API documentation using Swagger UI at `/docs`. It lets you test all your endpoints directly in the browser without writing any frontend code. This is built in — you don't need to configure anything.

---

**Q: How do you handle different request body structures in FastAPI?**
A: By defining a Pydantic model for the request body. For example:
```python
class ScriptRequest(BaseModel):
    topic: str
    style: str = "educational"
```
The `= "educational"` sets a default value so the field is optional.

---

**Q: What is async in FastAPI and when would you use it?**
A: FastAPI supports async route handlers using `async def` instead of `def`. You use async when your route needs to make external API calls or database queries — so it doesn't block other requests while waiting. For our Hugging Face API calls we will use async.

---

## Git and GitHub

**Q: What is the difference between `git add`, `git commit`, and `git push`?**
A: `git add` stages your changes — tells git which files to include. `git commit` saves a snapshot of those changes locally with a message. `git push` uploads your commits to GitHub so others can see them.

---

**Q: What is a `.gitignore` file?**
A: A file that tells git which files and folders to never track or push to GitHub. We added `.env` to `.gitignore` so our secret API tokens never get pushed to GitHub accidentally.

---

**Q: What is an SSH key and why did you use it?**
A: An SSH key is a cryptographic key pair used to authenticate with GitHub without a password. We used it so we could push to our personal GitHub account from a laptop that is also connected to a company GitHub account — using separate SSH keys for each.

---

**Q: Why did you use port 443 for SSH?**
A: Port 22 is the default SSH port but many corporate networks block it. Port 443 is the HTTPS port which is almost never blocked. GitHub supports SSH over port 443 via `ssh.github.com` for exactly this reason.

---

## System Design

**Q: How is your project structured and why?**
A: The project follows a separation of concerns pattern. `script_generator.py` handles the business logic of generating and saving scripts. `api.py` handles HTTP routing and request validation. This means if we want to change how scripts are generated, we only touch one file — not the API layer.

---

**Q: Where do you store generated scripts and why JSON?**
A: In a `data/` folder as individual JSON files with timestamps in the filename. JSON is human readable, easy to parse, and works well with Python's built-in `json` library. Each file has a timestamp so scripts never overwrite each other.

---

**Q: How would you scale this API if 1000 users were using it simultaneously?**
A: Currently the API is synchronous and single server. To scale we would make route handlers async, add a task queue like Celery for heavy AI processing, deploy multiple instances behind a load balancer on AWS or GCP, and use a database like PostgreSQL instead of saving to JSON files.

---

**Q: What would you add to make this production ready?**
A: Authentication so only registered users can call the API, rate limiting so users can't abuse it, a proper database instead of JSON files, error handling and logging, environment-based configuration, and CI/CD pipeline for automatic deployment.

---

## AI and Machine Learning (Coming Soon — update as you build)

**Q: What is Hugging Face?**
A: Hugging Face is the largest open source AI platform. It hosts thousands of pretrained models that developers can use for free. It is like npm but for AI models. We use their Inference API to generate scripts without needing a GPU.

**Q: What is the difference between training a model and using a pretrained model?**
A: Training a model means teaching it from scratch on a dataset — requires massive compute and data. Using a pretrained model means taking a model someone else already trained and either using it directly or fine-tuning it on your own smaller dataset. We use pretrained models to save time and cost.

**Q: What is fine-tuning?**
A: Fine-tuning means taking a pretrained model and training it further on your own specific data. For example taking LLaMA and training it on 1000 YouTube scripts so it generates better YouTube-style content. It is much cheaper than training from scratch.

**Q: What is LoRA?**
A: LoRA stands for Low-Rank Adaptation. It is a technique that lets you fine-tune a large model by only updating a small number of extra parameters instead of all billions of parameters. This makes fine-tuning much faster and cheaper while achieving similar results.

---

## Behavioural Questions

**Q: Tell me about a project you built from scratch.**
A: Talk about this project — explain the problem (creators spending hours on scripts), the solution (AI pipeline that generates scripts automatically), the tech stack, and what you learned. Mention that you built it while learning Python simultaneously.

---

**Q: How do you learn new technologies?**
A: Talk about your learn-apply-repeat approach — you don't just watch tutorials, you immediately apply each concept to your real project. Every Corey Schafer video you watched was immediately used in the creator AI pipeline.

---

**Q: How do you handle being stuck on a problem?**
A: Under 15 minutes — Google the exact error. Under 30 minutes — ask AI tools like Claude with full context. Over 30 minutes — identify the knowledge gap, go back to the relevant resource, then return to the problem. Never spend more than 30 minutes stuck without seeking help.

---

**Q: Why do you want to work in AI?**
A: Be honest — talk about building this project, discovering how AI pipelines work, the excitement of connecting models to real products, and the massive career opportunity in AI engineering right now.

---

*This file is updated every time a new feature is built.*
*Last updated: Day 1*