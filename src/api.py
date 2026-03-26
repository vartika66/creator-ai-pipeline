from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.script_generator import generate_script, save_script, generate_ai_script
from src.database import create_tables, get_db, Script
import json

app = FastAPI()
create_tables()

class ScriptRequest(BaseModel):
    topic: str
    style: str = "educational"

@app.get("/")
def home():
    return {"message": "Welcome to Creator AI Pipeline API"}

@app.post("/generate-script")
def create_script(request: ScriptRequest, db: Session = Depends(get_db)):
    script = generate_script(request.topic, request.style)
    
    db_script = Script(
        topic=script["topic"],
        style=script["style"],
        hook=script["hook"],
        problem=script["problem"],
        points=json.dumps(script["points"]),
        cta=script["cta"],
        source="template"
    )
    db.add(db_script)
    db.commit()
    db.refresh(db_script)
    
    return {**script, "id": db_script.id, "created_at": db_script.created_at}

@app.post("/generate-ai-script")
def create_ai_script(request: ScriptRequest, db: Session = Depends(get_db)):
    script = generate_ai_script(request.topic, request.style)
    
    db_script = Script(
        topic=script["topic"],
        style=script["style"],
        generated_text=script.get("generated_text"),
        source=script.get("source", "llama"),
        points="[]"
    )
    db.add(db_script)
    db.commit()
    db.refresh(db_script)
    
    return {**script, "id": db_script.id, "created_at": db_script.created_at}

@app.get("/scripts")
def get_scripts(db: Session = Depends(get_db)):
    scripts = db.query(Script).order_by(Script.created_at.desc()).all()
    
    return {
        "scripts": [
            {
                "id": s.id,
                "topic": s.topic,
                "style": s.style,
                "source": s.source,
                "created_at": str(s.created_at)
            }
            for s in scripts
        ],
        "total": len(scripts)
    }

@app.get("/scripts/{script_id}")
def get_script(script_id: int, db: Session = Depends(get_db)):
    script = db.query(Script).filter(Script.id == script_id).first()
    
    if not script:
        return {"error": "Script not found"}
    
    return {
        "id": script.id,
        "topic": script.topic,
        "style": script.style,
        "hook": script.hook,
        "problem": script.problem,
        "points": json.loads(script.points) if script.points else [],
        "cta": script.cta,
        "generated_text": script.generated_text,
        "source": script.source,
        "created_at": str(script.created_at)
    }

@app.delete("/scripts/{script_id}")
def delete_script(script_id: int, db: Session = Depends(get_db)):
    script = db.query(Script).filter(Script.id == script_id).first()
    
    if not script:
        return {"error": "Script not found"}
    
    db.delete(script)
    db.commit()
    
    return {"message": f"Script {script_id} deleted"}