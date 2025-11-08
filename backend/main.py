# -------------------------------
# SkillBridge AI Backend - main.py
# Version 2.1  |  Bala's Pro Mode
# -------------------------------

import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(__file__))   # Ensures ai_engine is found

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import json

# 🔹 Import local AI engine modules
from ai_engine.recommender import recommend_courses
from ai_engine.summarizer import generate_summary
from ai_engine.utils import detect_domain
from ai_engine.role_predictor import predict_role

# 🔹 Import database functions
from database import init_db, log_event, get_all_analytics

# Initialize FastAPI app
app = FastAPI(title="SkillBridge AI", version="2.1")

# 🔹 Initialize database at startup
init_db()

# 🔹 Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Input schema
class SkillInput(BaseModel):
    current_skills: list[str]
    goal_role: str


# ---------------------------------------------
#  Helper: Log user requests to /logs/usage_log.json
# ---------------------------------------------
def log_user_request(data, result):
    os.makedirs("logs", exist_ok=True)
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "goal": data.goal_role,
        "skills": data.current_skills,
        "domain": result["domain"],
        "recommended_courses": result["recommended_courses"],
    }
    with open("logs/usage_log.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")


# ---------------------------------------------
#  API 1: Generate Learning Path  (POST)
# ---------------------------------------------
@app.post("/generate_path")
def generate_path(data: SkillInput):
    domain = detect_domain(data.goal_role)
    courses = recommend_courses(data.current_skills)
    summary = generate_summary(data.goal_role, data.current_skills, domain)

    result = {
        "goal": data.goal_role.title(),
        "domain": domain,
        "recommended_courses": courses,
        "summary": summary
    }

    # Log every user request (JSON + DB)
    log_user_request(data, result)
    log_event("/generate_path", {"goal_role": data.goal_role, "current_skills": data.current_skills}, result)
    return result


# ---------------------------------------------
#  API 2: View Analytics  (GET)
# ---------------------------------------------
@app.get("/analytics")
def analytics():
    return {"analytics": get_all_analytics()}


# ---------------------------------------------
#  API 3: Detect Domain  (POST)
# ---------------------------------------------
@app.post("/detect_domain")
def get_domain(data: dict):
    text = data.get("text", "")
    result = detect_domain(text)
    log_event("/detect_domain", {"text": text}, {"domain": result})
    return {"domain": result}


# ---------------------------------------------
#  API 4: Recommend Courses  (POST)
# ---------------------------------------------
@app.post("/recommend")
def recommend(data: dict):
    skills = data.get("skills", [])
    result = recommend_courses(skills)
    log_event("/recommend", {"skills": skills}, result)
    return result


# ---------------------------------------------
#  API 5: Generate Summary  (POST)
# ---------------------------------------------
@app.post("/summarize")
def summarize(data: dict):
    text = data.get("text", "")
    result = generate_summary(text, [], "General")
    log_event("/summarize", {"text": text}, {"summary": result})
    return {"summary": result}


# ---------------------------------------------
#  API 6: Predict Role and Career Path  (POST)
# ---------------------------------------------
@app.post("/predict_role")
def predict(data: dict):
    skills = data.get("skills", [])
    result = predict_role(skills)
    log_event("/predict_role", {"skills": skills}, result)
    return result


# ---------------------------------------------
#  Root & Health Routes
# ---------------------------------------------
@app.get("/")
def root():
    return {"message": "SkillBridge AI backend is running ✅"}


@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------
# Run command (in terminal):
# cd backend
# ..\venv\Scripts\activate
# uvicorn main:app --reload
# ---------------------------------------------
