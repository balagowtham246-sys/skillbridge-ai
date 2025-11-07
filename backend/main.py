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

app = FastAPI(title="SkillBridge AI", version="2.1")

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
    courses = recommend_courses(data.goal_role)
    summary = generate_summary(data.goal_role, data.current_skills, domain)

    result = {
        "goal": data.goal_role.title(),
        "domain": domain,
        "recommended_courses": courses,
        "summary": summary
    }

    # Log every user request
    log_user_request(data, result)
    return result


# ---------------------------------------------
#  API 2: View Analytics  (GET)
# ---------------------------------------------
@app.get("/analytics")
def get_analytics():
    log_file = "logs/usage_log.json"
    if not os.path.exists(log_file):
        return {"message": "No data yet!"}

    with open(log_file, "r", encoding="utf-8") as f:
        entries = [json.loads(line) for line in f]

    total_requests = len(entries)
    domain_counts = {}
    for e in entries:
        domain = e["domain"]
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

    most_popular_domain = (
        max(domain_counts, key=domain_counts.get) if domain_counts else None
    )

    return {
        "total_requests": total_requests,
        "popular_domains": domain_counts,
        "top_domain": most_popular_domain,
    }


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
