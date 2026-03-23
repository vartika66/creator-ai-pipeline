from fastapi import FastAPI
from pydantic import BaseModel
from src.script_generator import generate_script, save_script

app = FastAPI()

class ScriptRequest(BaseModel):
    topic: str
    style: str = "educational"

class ScriptResponse(BaseModel):
    topic: str
    style: str
    hook: str
    problem: str
    points: list
    cta: str

@app.get("/")
def home():
    return {"message": "Welcome to Creator AI Pipeline API"}

@app.post("/generate-script", response_model=ScriptResponse)
def create_script(request: ScriptRequest):
    script = generate_script(request.topic, request.style)
    save_script(script)
    return script